"""The main framework runner."""
from abc import ABC
from typing import Dict, Callable, Generic, Union, Optional, Any
import time
from .registry import (
    EventRegistryContext, EventObject, EventBinaryTarget, EventObjectTarget, EventObjectParser,
)
from ...event_stream import (
    BinaryWriter, EventForwarderTarget, EventForwarder, BinaryReader,
    RawEvent,
    is_raw_event_object, is_raw_event_binary,
    raw_event_source_id, raw_event_target_id, raw_event_binary_size,
    as_raw_event_object_data, as_raw_event_binary_data_reader,
)
from ...event_stream.thread_stream import ThreadedStreamForwarder
from ...event_stream.thread_writer import ThreadSafeEventWriter
from ...util import StdRet, PetroniaReturnError, T, RET_OK_NONE
from ...util import i18n as _
from ...util.message import USER_MESSAGE_CATALOG_EXCEPTION


def extension_runner(
        reader: BinaryReader, writer: BinaryWriter,
        *factories: Callable[[EventRegistryContext], StdRet[None]],
) -> StdRet[None]:
    """Main entry point for extensions."""
    context = EventRegistryContextImpl(reader, writer)
    for factory in factories:
        res = factory(context)
        if res.has_error:
            return res
    context.run()
    return RET_OK_NONE


class EventRegistryContextImpl(EventRegistryContext):
    """Implementation of the context used by the runner thread."""
    __slots__ = ('_writer', '_forwarder', '_obj_parsers',)

    def __init__(self, reader: BinaryReader, writer: BinaryWriter) -> None:
        self._writer = ThreadSafeEventWriter(writer)
        stream_forwarder = ThreadedStreamForwarder()
        self._forwarder = EventForwarder(reader, stream_forwarder)
        self._obj_parsers: Dict[str, EventObjectParser[Any]] = {}

    def run(self) -> None:
        """Run the source handling."""
        self._forwarder.handle_source()

    def register_event(self, event_id: str, parser: EventObjectParser[T]) -> StdRet[None]:
        self._obj_parsers[event_id] = parser
        return RET_OK_NONE

    def register_target(  # pylint:disable=too-many-arguments
            self, event_id: str, target_id: str, target: EventObjectTarget,
            source_id: Optional[str] = None,
            timeout: float = -1.0,
            parallel: bool = False,
    ) -> StdRet[None]:
        assert parallel is False, 'parallel running is not yet supported.'
        parser = self._obj_parsers.get(event_id)
        if not parser:
            return StdRet.pass_errmsg(
                USER_MESSAGE_CATALOG_EXCEPTION,
                _('No registered parser for {event_id}'),
                event_id=event_id,
            )
        self._forwarder.add_target(EventObjectForwarderTarget(
            event_id, source_id, target_id, timeout, parser, target,
        ))
        return RET_OK_NONE

    def register_binary_target(  # pylint:disable=too-many-arguments
            self, event_id: str, target_id: str, target: EventBinaryTarget,
            source_id: Optional[str] = None, timeout: float = -1.0,
            parallel: bool = False,
    ) -> StdRet[None]:
        assert parallel is False, 'parallel running is not yet supported.'
        self._forwarder.add_target(EventBinaryForwarderTarget(
            event_id, source_id, target_id, timeout, target,
        ))
        return RET_OK_NONE

    def send_event(self, source_id: str, target_id: str, event: EventObject) -> StdRet[None]:
        return self._writer.write_object_event(
            event.fully_qualified_event_name,
            source_id,
            target_id,
            event.export_data(),
        )

    def send_binary_event(
            self, source_id: str, target_id: str, event_id: str, data: Union[bytes, bytearray],
    ) -> StdRet[None]:
        return self._writer.write_binary_event(
            event_id,
            source_id,
            target_id,
            len(data),
            bytes(data),
        )


class AbstractEventForwarderTarget(EventForwarderTarget, ABC):
    """Common implementation for targets.  This is a single-threaded version."""

    __slots__ = ('_source_id', '_target_id', '_event_id', '_expires',)

    def __init__(
            self,
            event_id: str,
            source_id: Optional[str],
            target_id: str,
            timeout: float,
    ) -> None:
        self._event_id = event_id
        self._source_id = source_id
        self._target_id = target_id
        if timeout <= 0.0:
            self._expires = -1.0
        else:
            self._expires = time.time() + timeout

    def can_consume(self, event_id: str, source_id: str, target_id: str) -> bool:
        return (
                event_id == self._event_id
                and target_id == self._target_id
                and (self._source_id is None or source_id == self._source_id)
        )

    def on_error(self, error: PetroniaReturnError) -> bool:
        return self._remove_if_not_timed_out()

    def _remove_if_not_timed_out(self) -> bool:
        return time.time() > self._expires > 0.0


class EventObjectForwarderTarget(AbstractEventForwarderTarget, Generic[T]):
    """Target for event objects.  This is a single-threaded version."""

    __slots__ = ('_handler', '_parser')

    def __init__(  # pylint:disable=too-many-arguments
            self,
            event_id: str,
            source_id: Optional[str],
            target_id: str,
            timeout: float,
            parser: EventObjectParser[T],
            target: EventObjectTarget,
    ) -> None:
        AbstractEventForwarderTarget.__init__(self, event_id, source_id, target_id, timeout)
        self._handler = target
        self._parser = parser

    def on_eof(self) -> None:
        self._handler.on_close()

    def consume(self, event: RawEvent) -> bool:
        if not is_raw_event_object(event):
            return self._remove_if_not_timed_out()
        data = as_raw_event_object_data(event)
        event_res = self._parser.parse(data)
        if event_res.has_error:
            # TODO send error
            return self._remove_if_not_timed_out()
        ret = self._handler.on_event(
            raw_event_source_id(event),
            raw_event_target_id(event),
            event_res.result,
        )
        return ret or self._remove_if_not_timed_out()


class EventBinaryForwarderTarget(AbstractEventForwarderTarget):
    """General handler for binary events."""
    __slots__ = ('_handler',)

    def __init__(
            self,
            event_id: str,
            source_id: Optional[str],
            target_id: str,
            timeout: float,
            handler: EventBinaryTarget,
    ) -> None:
        AbstractEventForwarderTarget.__init__(self, event_id, source_id, target_id, timeout)
        self._handler = handler

    def on_eof(self) -> None:
        self._handler.on_close()

    def consume(self, event: RawEvent) -> bool:
        if not is_raw_event_binary(event):
            return self._remove_if_not_timed_out()
        source = raw_event_source_id(event)
        target = raw_event_target_id(event)
        size = raw_event_binary_size(event)
        data = as_raw_event_binary_data_reader(event)
        res = self._handler.on_event(source, target, size, data)
        return res or self._remove_if_not_timed_out()
