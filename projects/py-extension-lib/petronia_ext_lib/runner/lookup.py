"""A lookup registry, which is much more complex than the simple one, but is much more efficient
for large number of targets at the expense of more memory.  It also handles binary events."""

from typing import Tuple, List, Dict, Callable, Union, Optional, Generic
import threading
import time
from petronia_common.event_stream import (
    BinaryReader, BinaryWriter, read_event_stream, write_object_event_to_stream,
    write_binary_event_to_stream, RawEvent, is_raw_event_object, raw_event_id,
    as_raw_event_object_data, raw_event_target_id, raw_event_source_id,
    raw_event_binary_size, as_raw_event_binary_data_reader,
)
from petronia_common.util import StdRet, PetroniaReturnError, T, RET_OK_NONE, EMPTY_DICT
from petronia_common.util import i18n as _
from . import registry, EventBinaryTarget, EventObjectTarget, EventObjectParser
from .registry import EventObject
from .simple import StoppableBinaryReader
from ..defs import TRANSLATION_CATALOG


class LookupEventRegistryContext(registry.EventRegistryContext):
    """The lookup event registry.  The registry is thread-safe.  Binary
    event handlers are allowed, but only one per event id, in order to
    prevent stream forking requirements (which means the handler must perform
    threading).

    Writing is performed within the same lock.  All event handling is performed
    within the lock, so the lock must be a re-entrant lock to do anything useful."""
    __slots__ = (
        '_object_targets', '_binary_targets',
        '__reader', '__writer', '_on_error', '_lock',
    )

    def __init__(
            self, reader: BinaryReader, writer: BinaryWriter,
            on_error: Optional[Callable[[PetroniaReturnError], bool]],
            lock: Optional[threading.RLock],
    ) -> None:
        self._lock = lock or threading.RLock()
        self.__writer = writer
        self.__reader = StoppableBinaryReader(reader)
        self._on_error: Callable[[PetroniaReturnError], bool] = on_error or noop_on_error
        self._object_targets: Dict[str, ParserHandler] = {}
        self._binary_targets: Dict[str, Tuple[float, EventBinaryTarget]] = {}

    def stop_reader(self) -> None:
        """Stop the reader.  This will only perform a stop when the next read begins.
        If a read is in progress, this will not interrupt it."""
        self.__reader.alive = False

    def process_reader(self) -> None:
        """Read all events until the reader completes, or a stop message is encountered."""
        read_event_stream(
            self.__reader,
            self._event_listener,
            self._eof_listener,
            self._error_listener,
        )

    def register_event(self, event_id: str, parser: EventObjectParser[T]) -> StdRet[None]:
        with self._lock:
            if event_id in self._object_targets:
                return StdRet.pass_errmsg(
                    TRANSLATION_CATALOG,
                    _('parser for event {event_id} already registered'),
                    event_id=event_id,
                )
            self._object_targets[event_id] = ParserHandler(parser)
        return RET_OK_NONE

    def register_target(
            self, event_id: str, target_id: Optional[str], target: EventObjectTarget[T],
            source_id: Optional[str] = None, timeout: float = -1.0,
    ) -> StdRet[None]:
        with self._lock:
            parser_handler = self._object_targets.get(event_id)
            if not parser_handler:
                return StdRet.pass_errmsg(
                    TRANSLATION_CATALOG,
                    _('event ID {event_id} does not have a registered parser'),
                    event_id=event_id,
                )
            parser_handler.add_handler(
                target_id, target, -1 if timeout <= 0 else time.time() + timeout,
            )
        return RET_OK_NONE

    def register_binary_target(
            self, event_id: str, target_id: Optional[str], target: EventBinaryTarget,
            source_id: Optional[str] = None, timeout: float = -1.0,
    ) -> StdRet[None]:
        with self._lock:
            if event_id in self._binary_targets:
                return StdRet.pass_errmsg(
                    TRANSLATION_CATALOG,
                    _(
                        'a target handler for binary event {event_id} is already registered'
                    ),
                    event_id=event_id,
                    source_id=source_id,
                    target_id=target_id,
                )
            self._binary_targets[event_id] = (
                -1 if timeout <= 0 else time.time() + timeout,
                target,
            )
        return RET_OK_NONE

    def send_event(self, source_id: str, target_id: str, event: EventObject) -> StdRet[None]:
        with self._lock:
            return write_object_event_to_stream(
                self.__writer, event.fully_qualified_event_name, source_id, target_id,
                event.export_data(),
            )

    def send_binary_event(
            self, source_id: str, target_id: str, event_id: str, data: Union[bytes, bytearray],
    ) -> StdRet[None]:
        with self._lock:
            return write_binary_event_to_stream(
                self.__writer, event_id, source_id, target_id,
                len(data), bytes(data),
            )

    def _event_listener(self, event: RawEvent) -> bool:
        """Process an event."""
        if not self.__reader.alive:
            # Stop reading
            return True

        # Handle the event sources first, then timeouts.

        event_id = raw_event_id(event)
        source_id = raw_event_source_id(event)
        target_id = raw_event_target_id(event)

        with self._lock:
            if is_raw_event_object(event):
                parser = self._object_targets.get(event_id)
                if not parser:
                    return False
                res = parser.handle_event(source_id, target_id, event)
                if res.has_error:
                    self._on_error(res.valid_error)
            else:
                listener = self._binary_targets.get(event_id)
                if listener:
                    listener[1].on_event(
                        source_id, target_id, raw_event_binary_size(event),
                        as_raw_event_binary_data_reader(event),
                    )

        self._handle_timeouts()

        # Stop reading if the reader has stopped.
        return not self.__reader.alive

    def _eof_listener(self) -> None:
        """Call the registered stuff, saying that it's closed."""
        with self._lock:
            for parser in self._object_targets.values():
                parser.on_eof()
            for _expires, target in self._binary_targets.values():
                target.on_close()

    def _error_listener(self, error: PetroniaReturnError) -> bool:
        """Error listener."""
        # If we've stopped, then return True to indicate a stop.
        # _on_error must be run within the lock.
        with self._lock:
            if self._on_error(error):
                # Forces a stop.
                self.__reader.alive = False
                return True
            self._handle_timeouts()
        return not self.__reader.alive

    def _handle_timeouts(self) -> None:
        """Clear out timed-out handlers.  Must be called from within a lock."""
        now = time.time()
        for parser in self._object_targets.values():
            parser.check_timeout(now)

        remove: List[str] = []
        for key, target_tuple in self._binary_targets.items():
            if 0 < target_tuple[0] < now:
                remove.append(key)
        for key in remove:
            self._binary_targets[key][1].on_close()
            del self._binary_targets[key]


def noop_on_error(_error: PetroniaReturnError) -> bool:
    """A no-op on-error callback."""
    return False


class ParserHandler(Generic[T]):
    """Handles the parser + event handlers."""
    __slots__ = ('parser', '_handlers', '_count')

    def __init__(self, parser: EventObjectParser[T]) -> None:
        self.parser = parser
        self._count = 0
        self._handlers: Dict[Optional[str], Dict[int, Tuple[float, EventObjectTarget[T]]]] = {}

    def add_handler(
            self,
            target_id: Optional[str], handler: EventObjectTarget, expires: float,
    ) -> None:
        """Add a handler."""
        next_id = self._count
        self._count += 1
        if target_id not in self._handlers:
            self._handlers[target_id] = {}
        self._handlers[target_id][next_id] = (expires, handler)

    def handle_event(
            self,
            source_id: str,
            target_id: str,
            event: RawEvent,
    ) -> StdRet[None]:
        """Handle this event object."""
        match1 = self._handlers.get(None, EMPTY_DICT)
        match2 = self._handlers.get(target_id, EMPTY_DICT)
        if not match1 and not match2:
            return RET_OK_NONE
        event_data_res = self.parser.parse(as_raw_event_object_data(event))
        if event_data_res.has_error:
            return event_data_res.forward()

        for matches in (match1, match2):
            remove: List[int] = []
            for index, target_tuple in matches.items():
                if target_tuple[1].on_event(source_id, target_id, event_data_res.result):
                    remove.append(index)
            for index in remove:
                del matches[index]

        return RET_OK_NONE

    def check_timeout(self, current_time: float) -> None:
        """Check the timeouts."""
        for handlers in self._handlers.values():
            remove: List[int] = []
            for index, target_tuple in handlers.items():
                if 0 < target_tuple[0] < current_time:
                    target_tuple[1].on_close()
                    remove.append(index)
            for index in remove:
                del handlers[index]

    def on_eof(self) -> None:
        """Call the end of stream functions."""
        for handlers in self._handlers.values():
            for _expires, target in handlers.values():
                target.on_close()
