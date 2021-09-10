"""A simple implementation of an event runner.  Single threaded with only object events handled,
and one listener per event ID."""

from typing import Dict, List, Tuple, Callable, Optional, Union
from petronia_common.event_stream import (
    BinaryWriter, BinaryReader, RawEvent,
    read_event_stream,
    write_object_event_to_stream, write_binary_event_to_stream,
    is_raw_event_object, as_raw_event_object_data,
    is_raw_event_binary, as_raw_event_binary_data_reader, raw_event_binary_size,
    raw_event_id, raw_event_source_id, raw_event_target_id, RawBinaryReader,
)
from petronia_common.util import StdRet, RET_OK_NONE, T, PetroniaReturnError, enforce_all, not_none
from petronia_common.util import i18n as _
from .registry import (
    EventRegistryContext, EventObjectParser, EventObjectTarget, EventBinaryTarget, EventObject,
)
from .simple import StoppableBinaryReader
from ..extension_loader.annouce_start import send_announce_started
from ..defs import TRANSLATION_CATALOG

_HandlerId = Tuple[str, Optional[str]]


class SingleThreadedEventRegistryContext(EventRegistryContext):
    """Single-threaded event registry, supporting both objects and binary data."""
    __slots__ = (
        '__obj_handlers', '__bin_handlers',
        '__eof', '__writer', '__reader', '__on_error',
    )

    def __init__(
            self, reader: BinaryReader, writer: BinaryWriter,
            on_error: Optional[Callable[[PetroniaReturnError], bool]],
    ) -> None:
        self.__obj_handlers: Dict[str, ObjectEventHandler] = {}
        self.__bin_handlers: Dict[_HandlerId, EventBinaryTarget] = {}
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
        if event_id in self.__obj_handlers:
            if parser == self.__obj_handlers[event_id].parser:
                # Allow duplicate registration
                return RET_OK_NONE
            return StdRet.pass_errmsg(
                TRANSLATION_CATALOG,
                _('parser for event {event_id} already registered'),
                event_id=event_id,
            )
        self.__obj_handlers[event_id] = ObjectEventHandler(parser)
        return RET_OK_NONE

    def register_target(  # pylint:disable=too-many-arguments
            self,
            event_id: str,
            target_id: Optional[str],
            target: EventObjectTarget[T],
            source_id: Optional[str] = None,
            timeout: float = -1.0,
    ) -> StdRet[None]:
        handler = self.__obj_handlers.get(event_id)
        res = enforce_all(
            'register_target', TRANSLATION_CATALOG,
            (
                _('event ID {event_id} does not have a registered parser'),
                lambda: handler is not None,
            ),
            (
                _(
                    'a target handler for event "{event_id}", '
                    'target "{target_id}" is already registered'
                ),
                lambda: handler is None or not handler.has_target(target_id),
            ),
            (
                _("only targets that don't time out are supported."),
                lambda: timeout < 0,
            ),
            event_id=event_id,
            target_id=target_id,
        )
        if res:
            return StdRet.pass_error(res)
        not_none(handler).add_target(target_id, target)
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
        handler_id: _HandlerId = (event_id, target_id)
        handler = self.__bin_handlers.get(handler_id)
        res = enforce_all(
            'register_binary_target', TRANSLATION_CATALOG,
            (
                _(
                    'a binary target handler for event "{event_id}", '
                    'target "{target_id}" is already registered'
                ),
                lambda: handler is None,
            ),
            (
                _("only targets that don't time out are supported."),
                lambda: timeout < 0,
            ),
        )
        if res:
            return StdRet.pass_error(res)
        self.__bin_handlers[handler_id] = target
        return RET_OK_NONE

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

    def send_binary_event_stream(
            self, source_id: str, target_id: str, event_id: str, data_size: int,
            data: RawBinaryReader,
    ) -> StdRet[None]:
        return write_binary_event_to_stream(
            self.__writer, event_id, source_id, target_id, data_size, data,
        )

    def _event_listener(self, event: RawEvent) -> bool:
        """Process an event."""
        if not self.__reader.alive:
            # Stop reading
            return True

        event_id = raw_event_id(event)
        target_id = raw_event_target_id(event)

        if is_raw_event_binary(event):
            handler_id: _HandlerId = (event_id, target_id)
            bin_handler = self.__bin_handlers.get(handler_id)
            if bin_handler is None:
                handler_id = (event_id, None)
                bin_handler = self.__bin_handlers.get(handler_id)
            if bin_handler:
                res = bin_handler.on_event(
                    raw_event_source_id(event), target_id,
                    raw_event_binary_size(event),
                    as_raw_event_binary_data_reader(event),
                )
                if res:
                    # Remove the listener
                    del self.__bin_handlers[handler_id]

        elif is_raw_event_object(event):
            obj_handler = self.__obj_handlers.get(event_id)
            if not obj_handler:
                return False
            obj_target = obj_handler.get_target(target_id)
            if not obj_target:
                return False
            event_res = obj_handler.parser.parse(as_raw_event_object_data(event))
            if event_res.has_error:
                return self._error_listener(event_res.valid_error)
            res = obj_target.on_event(
                raw_event_source_id(event), raw_event_target_id(event),
                event_res.result,
            )
            if res:
                # remove the listener
                obj_handler.remove_target_handler(target_id, obj_target)

        # Stop reading if the reader has stopped.
        return not self.__reader.alive

    def _eof_listener(self) -> None:
        """Close off the handlers."""
        for obj_handler in self.__obj_handlers.values():
            obj_handler.on_close()
        for bin_handler in self.__bin_handlers.values():
            bin_handler.on_close()
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


class ObjectEventHandler:
    """Handler for a received event."""
    __slots__ = ('parser', '__targets', '__default')

    def __init__(self, parser: EventObjectParser) -> None:
        self.parser = parser
        self.__targets: Dict[str, EventObjectTarget] = {}
        self.__default: Optional[EventObjectTarget] = None

    def add_target(self, target_id: Optional[str], target: EventObjectTarget) -> bool:
        """Add a new target listener.  Returns False if already registered."""
        if target_id in self.__targets:
            return False
        if target_id is None:
            if self.__default is not None:
                return False
            self.__default = target
            return True
        self.__targets[target_id] = target
        return True

    def has_target(self, target_id: Optional[str]) -> bool:
        """Is the target_id registered?"""
        if target_id is None:
            return self.__default is not None
        return target_id in self.__targets

    def get_target(self, target_id: str) -> Optional[EventObjectTarget]:
        """Get the target with the ID."""
        if target_id in self.__targets:
            return self.__targets[target_id]
        return self.__default

    def remove_target_handler(self, target_id: str, obj_target: EventObjectTarget) -> None:
        """Remove the target handler"""
        if self.__default is obj_target:
            self.__default = None
        if target_id in self.__targets and self.__targets[target_id] is obj_target:
            del self.__targets[target_id]

    def on_close(self) -> None:
        """Send on_close to all targets."""
        if self.__default:
            self.__default.on_close()
        for target in self.__targets.values():
            target.on_close()
