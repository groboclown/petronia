"""A simple implementation of an event runner.  Single threaded with only object events handled,
and one listener per event ID."""

from typing import Dict, List, Callable, Optional, Union
from petronia_common.event_stream import (
    BinaryWriter, BinaryReader, RawEvent,
    read_event_stream,
    write_object_event_to_stream, write_binary_event_to_stream,
    is_raw_event_object, as_raw_event_object_data,
    raw_event_id, raw_event_source_id, raw_event_target_id,
)
from petronia_common.util import StdRet, RET_OK_NONE, T, PetroniaReturnError, enforce_all, not_none
from petronia_common.util import i18n as _
from .registry import (
    EventRegistryContext, EventObjectParser, EventObjectTarget, EventBinaryTarget, EventObject,
)
from ..extension_loader.annouce_start import send_announce_started
from ..defs import TRANSLATION_CATALOG


class SimpleEventRegistryContext(EventRegistryContext):
    """Single-threaded, object-only event registry.  The target registration is
    simplified where the target id is ignored."""
    __slots__ = ('__handlers', '__eof', '__writer', '__reader', '__on_error')

    def __init__(
            self, reader: BinaryReader, writer: BinaryWriter,
            on_error: Optional[Callable[[PetroniaReturnError], bool]],
    ) -> None:
        self.__handlers: Dict[str, EventHandler] = {}
        self.__writer = writer
        self.__reader = StoppableBinaryReader(reader)
        self.__on_error = on_error
        self.__eof: List[Callable[[], None]] = []

    def stop_reader(self) -> None:
        """Stop the reader.  This will only perform a stop when the next read begins.
        If a read is in progress, this will not interrupt it.  Note that, as this is
        supposed to be a single-threaded reader, there should be no way to stop progress
        during a read operation."""
        self.__reader.alive = False

    def process_reader(self, extension_name: Optional[str]) -> StdRet[None]:
        """Read all events until the reader completes, or a stop message is encountered.
        This will also send the started announcement if the extension name argument is
        non-None.
        """
        if extension_name:
            res = send_announce_started(self, extension_name)
            if res.has_error:
                return res
        read_event_stream(
            self.__reader,
            self._event_listener,
            self._eof_listener,
            self._error_listener,
        )
        return RET_OK_NONE

    def register_event(self, event_id: str, parser: EventObjectParser) -> StdRet[None]:
        if event_id in self.__handlers:
            if parser == self.__handlers[event_id]:
                # Allow duplicate registration
                return RET_OK_NONE
            return StdRet.pass_errmsg(
                TRANSLATION_CATALOG,
                _('parser for event {event_id} already registered'),
                event_id=event_id,
            )
        self.__handlers[event_id] = EventHandler(parser, None)
        return RET_OK_NONE

    def register_target(  # pylint:disable=too-many-arguments
            self,
            event_id: str,
            target_id: Optional[str],
            target: EventObjectTarget[T],
            source_id: Optional[str] = None,
            timeout: float = -1.0,
    ) -> StdRet[None]:
        handler = self.__handlers.get(event_id)
        res = enforce_all(
            'register_target', TRANSLATION_CATALOG,
            (_('simple implementation only supports None target id'), lambda: target_id is None),
            (
                _('event ID {event_id} does not have a registered parser'),
                lambda: handler is not None,
            ),
            (
                _('a target handler for event {event_id} is already registered'),
                lambda: handler is None or handler.target is None,
            ),
            (
                _("only targets that don't time out are supported."),
                lambda: timeout < 0,
            ),
            event_id=event_id,
        )
        if res:
            return StdRet.pass_error(res)
        not_none(handler).target = target
        return RET_OK_NONE

    def register_eof_target(self, callback: Callable[[], None]) -> StdRet[None]:
        self.__eof.append(callback)
        return RET_OK_NONE

    def register_binary_target(  # pylint:disable=too-many-arguments
            self,
            event_id: str,
            target_id: Optional[str],
            target: EventBinaryTarget,
            source_id: Optional[str] = None,
            timeout: float = -1.0,
    ) -> StdRet[None]:
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            _('binary targets not supported'),
        )

    def send_event(self, source_id: str, target_id: str, event: EventObject) -> StdRet[None]:
        return write_object_event_to_stream(
            self.__writer, event.fully_qualified_event_name, source_id, target_id,
            event.export_data(),
        )

    def send_binary_event(
            self, source_id: str, target_id: str, event_id: str, data: Union[bytes, bytearray],
    ) -> StdRet[None]:
        return write_binary_event_to_stream(
            self.__writer, event_id, source_id, target_id,
            len(data), bytes(data),
        )

    def _event_listener(self, event: RawEvent) -> bool:
        """Process an event."""
        if not self.__reader.alive:
            # Stop reading
            return True
        if not is_raw_event_object(event):
            # Only handle event objects.
            return False
        event_id = raw_event_id(event)
        handler = self.__handlers.get(event_id)
        if not handler:
            return False
        target = handler.target
        if not target:
            return False
        event_res = handler.parser.parse(as_raw_event_object_data(event))
        if event_res.has_error:
            return self._error_listener(event_res.valid_error)
        res = target.on_event(
            raw_event_source_id(event), raw_event_target_id(event),
            event_res.result,
        )
        if res:
            # remove the listener
            handler.target = None

        # Stop reading if the reader has stopped.
        return not self.__reader.alive

    def _eof_listener(self) -> None:
        """Close off the handlers."""
        for handler in self.__handlers.values():
            if handler.target:
                handler.target.on_close()
        for target in self.__eof:
            target()

    def _error_listener(self, error: PetroniaReturnError) -> bool:
        """Error listener."""
        # If we've stopped, then return True to indicate a stop.
        if self.__on_error:
            if self.__on_error(error):
                # Forces a stop.
                self.__reader.alive = False
                return True
        return not self.__reader.alive


class EventHandler:
    """Handler for a received event."""
    __slots__ = ('parser', 'target')

    def __init__(self, parser: EventObjectParser, target: Optional[EventObjectTarget]) -> None:
        self.parser = parser
        self.target = target


class StoppableBinaryReader:
    """Standard API for binary reader objects."""
    __slots__ = ('__proxy', 'alive')

    def __init__(self, proxy: BinaryReader) -> None:
        self.__proxy = proxy
        self.alive = True

    def read(self, max_read_size: int = -1) -> bytes:
        """Read the data."""
        if not self.alive:
            return b''
        return self.__proxy.read(max_read_size)
