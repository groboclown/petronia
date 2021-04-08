
"""
Each channel represents an event stream pipe, which has multiple producers and consumers
associated with it.  The channel is expected to perform its own internal routing of the
produced events, which means that events produced from a channel must not be directed
back into the channel.
"""

from typing import Iterable, List, Callable, Coroutine, Optional, Any, Dict
from enum import Enum
from petronia_common.util import (
    StdRet, PetroniaReturnError, T, RET_OK_NONE,
)
from petronia_common.util import i18n as _
from petronia_common.event_stream import (
    RawEvent,
    EventForwarderTarget,
    EventForwarder,
    BinaryWriter,
    BinaryReader,
    write_object_event_to_stream,
    write_binary_event_to_stream, RawBinaryReader,
)
from petronia_common.event_stream.thread_stream import ThreadedStreamForwarder
from .handler import EventHandlerSet, EventTargetHandle
from ..user_message import CATALOG, trace_event, trace_channel


EventRouteDestinationCallback = Callable[[RawEvent], Coroutine[Any, Any, StdRet[None]]]


class EventFilterResult(Enum):
    """Result from the internal event handler, describing how to handle the event and filter."""
    ALLOW_EVENT__KEEP_FILTER = 0x2 | 0
    ALLOW_EVENT__REMOVE_FILTER = 0x2 | 0x1
    FILTER_EVENT__KEEP_FILTER = 0 | 0
    FILTER_EVENT__REMOVE_FILTER = 0 | 0x1

    def allow_event(self) -> bool:
        """Is the event allowed to be used?"""
        return (int(self.value) & 0x2) == 0x2

    def remove_filter(self) -> bool:
        """Should the filter be removed after this event handling?"""
        return (int(self.value) & 0x1) == 0x1


InternalEventHandler = Callable[[str, str, str, RawEvent], EventFilterResult]


class EventChannel(EventForwarderTarget):
    """
    A source and destination with the associated handlers.
    The handlers associated with the channel are viewed as being attached
    to "the other side" - writing events on the channel means that the
    handlers are listening / consuming the event, and reading from the
    channel means the handlers are sending / producing the event.

    This also allows for internal handlers, which are special handlers for monitoring
    events intended only for communication between Foreman and the launcher that
    manages its own running extensions.
    """

    __slots__ = (
        '__name', '__handlers', '__forwarder', '__writer', '__alive', '__on_error',
        '__internal_handlers',
    )

    def __init__(
            self,
            name: str,
            reader: BinaryReader,
            writer: BinaryWriter,
            on_error: Callable[[str, PetroniaReturnError], bool],
    ) -> None:
        self.__name = name
        self.__forwarder = EventForwarder(
            name,
            reader, ThreadedStreamForwarder(), self._local_filter,
        )
        self.__writer = writer
        self.__handlers = EventHandlerSet()
        self.__on_error = on_error
        self.__internal_handlers: List[InternalEventHandler] = []
        self.__alive = True

    def __repr__(self) -> str:
        return f"EventChannel({self.__name})"

    def process_stream(self) -> None:
        """Run the stream processing."""
        # print(f"Channel {self.__name} processing source stream")
        self.__forwarder.handle_source()
        # print(f"Channel {self.__name} finished processing source stream")

    @property
    def name(self) -> str:
        """The event channel name."""
        return self.__name

    def get_handler_ids(self) -> Iterable[str]:
        """Get all known handler IDs"""
        return self.__handlers.get_handler_ids()

    def is_alive(self) -> bool:
        """Is this channel still receiving events and sending them?
        The channel can only be closed, which makes this return False."""
        return self.__alive

    def close_access(self) -> None:
        """Sets the alive flag to False, which stops this channel from
        allowing new handlers, producing events, and consuming events.
        This function may be safely called multiple times."""
        self.__alive = False
        # print(f"closing access to channel {self.__name}")

    def contains_handler_id(self, handler_id: str) -> bool:
        """Does this channel contain this handler?"""
        return self.__handlers.contains_handler_id(handler_id)

    def add_event_consumer(self, target: EventForwarderTarget) -> None:
        """Add the given target as a consumer for this channel's sent events
        (the events read in from the reader for the channel).  These are
        removed by their call-backs returning the correct value."""
        trace_channel(self.name, f'added listener {target}')
        self.__forwarder.add_target(target)

    def add_handler(
            self, handler_id: str,
            produces: Iterable[str], consumes: Iterable[EventTargetHandle],
            source_id_prefixes: Iterable[str],
    ) -> StdRet[None]:
        """Add an event handler to this channel.  If the
        handler already has the same ID registered, an error
        is returned."""
        if not self.__alive:
            return _create_route_closed_error(self.__name)
        trace_channel(
            self.name,
            f'added handler {handler_id}: can produce {produces}; can consume {consumes}; '
            f'allows producing prefixes {source_id_prefixes}',
        )
        return self.__handlers.add_handler(handler_id, produces, consumes, source_id_prefixes)

    def remove_handler(self, handler_id: str) -> StdRet[None]:
        """Attempts to remove the handler from the internal
        store.  If the handler is not registered, an error is returned.
        This can be safely called after the channel is closed."""
        trace_channel(self.name, f'removing handler {handler_id}')
        return self.__handlers.remove_handler(handler_id)

    def add_handler_listener(
            self,
            handler_id: str,
            event_id: Optional[str], target_id: Optional[str],
    ) -> StdRet[None]:
        """Registers the event / target listener with the handler."""
        if not self.__alive:
            return _create_route_closed_error(self.__name)
        trace_channel(
            self.name,
            f'{handler_id}: added listener for event [{event_id}] produced by <{target_id}>',
        )
        return self.__handlers.add_listener(handler_id, event_id, target_id)

    def remove_handler_listener(
            self,
            handler_id: str,
            event_id: Optional[str], target_id: Optional[str],
    ) -> StdRet[None]:
        """Removes the event / target listener from the handler."""
        if not self.__alive:
            return _create_route_closed_error(self.__name)
        trace_channel(
            self.name,
            f'{handler_id}: removed listener for event [{event_id}] produced by <{target_id}>',
        )
        return self.__handlers.remove_listener(handler_id, event_id, target_id)

    def add_internal_event_handler(self, handler: InternalEventHandler) -> StdRet[None]:
        """Add an internal event handler.  This can intercept events intended only for
        foreman that must never be broadcast out."""
        if not self.__alive:
            return _create_route_closed_error(self.__name)
        self.__internal_handlers.append(handler)
        return RET_OK_NONE

    def remove_internal_event_handler(self, handler: InternalEventHandler) -> StdRet[None]:
        """Remove an internal event handler.  If the handler is not registered, it will
        NOT return an error."""
        if not self.__alive:
            return _create_route_closed_error(self.__name)
        if handler in self.__internal_handlers:
            self.__internal_handlers.remove(handler)
        return RET_OK_NONE

    def can_produce(self, event_id: str, source_id: str) -> bool:
        """Can this channel produce this event?  That is, is an event
        read from the channel in the list of registered produced event IDs?"""
        if not self.__alive:
            # print(f"[{self}] cannot produce {event_id} @{source_id}; not alive")
            return False
        ret = self.__handlers.can_produce(event_id, source_id)
        trace_event(self.name, source_id, '<N/A>', event_id, f'can channel produce? {ret}')
        return ret

    def _local_filter(
            self, event_id: str, event_source_id: str, event_target_id: str, event: RawEvent,
    ) -> bool:
        # All event handlers are called, even if a filter does not allow the event
        # to be passed on.  Returns True if filtered, and False if allowed to be
        # produced by the channel.
        trace_event(
            self.name, event_source_id, event_target_id, event_id,
            'channel generated event; passing to listeners',
        )
        allow_event = self.can_produce(event_id, event_source_id)
        removed_handlers: List[InternalEventHandler] = []
        for handler in self.__internal_handlers:
            # Don't trace events going to internal handlers.
            # trace_event(
            #     self.name, event_source_id, event_target_id, event_id,
            #     f'sending event to internal handler {handler}',
            # )
            res = handler(event_id, event_source_id, event_target_id, event)
            if res.remove_filter():
                removed_handlers.append(handler)
            if not res.allow_event():
                allow_event = False
        for handler in removed_handlers:
            self.__internal_handlers.remove(handler)
        # print(f' - allowed to send? {allow_event}')
        return not allow_event

    # ------------------------------------------------------------------------------
    # Forwarder Target Methods.
    # These are called by other channels into this channel when the other
    # channel produces an event that this channel may consume.

    def can_consume(self, event_id: str, source_id: str, target_id: str) -> bool:
        """Can this channel consume this event?  That is, can an
        event ID be written to this channel?"""
        if not self.__alive:
            # print(f"channel {self.__name} can't consume; not alive")
            return False
        ret = self.__handlers.can_consume(event_id, target_id)
        if not ret:
            trace_event(self.name, source_id, target_id, event_id, f'cannot consume: {self.__handlers.consume_info()}')
        return ret

    def on_error(self, error: PetroniaReturnError) -> bool:
        # The other channel encountered a read error, and is telling this channel
        # about it.  This channel doesn't care about that message.
        if not self.__alive:
            return True
        # Do nothing...
        trace_channel(
            self.name,
            f'Ignored stream read errors: {[m.debug() for m in error.messages()]}',
        )
        return False

    def on_eof(self) -> None:
        # The other channel encountered an EOF, and is telling this channel
        # about it.  This channel doesn't care about that message.
        # trace_channel(self.name, 'Encountered EOF on other channel')
        pass

    def consume_object(
            self, event_id: str, source_id: str, target_id: str, event_data: Dict[str, Any],
    ) -> bool:
        # can_consume has already been called and returned True.
        if not self.__alive:
            return True
        trace_event(self.name, source_id, target_id, event_id, 'passing event into channel')
        ret = write_object_event_to_stream(
            self.__writer,
            event_id,
            source_id,
            target_id,
            event_data,
        )
        if ret.has_error:
            # This is a real error that the channel cares about.
            if self.__on_error(self.name, ret.valid_error):
                self.close_access()
                return True
        return False

    def consume_binary(
            self, event_id: str, source_id: str, target_id: str, size: int,
            data_reader: RawBinaryReader,
    ) -> bool:
        # can_consume has already been called and returned True.
        if not self.__alive:
            return True
        trace_event(self.name, source_id, target_id, event_id, 'passing binary event into channel')
        ret = write_binary_event_to_stream(
            self.__writer,
            event_id,
            source_id,
            target_id,
            size,
            data_reader,
        )
        if ret.has_error:
            # This is a real error that the channel cares about.
            if self.__on_error(self.name, ret.valid_error):
                self.close_access()
                return True
        return False


def _create_route_closed_error(route_name: str) -> StdRet[T]:
    return StdRet.pass_errmsg(
        CATALOG,
        _('route {name} is closed'),
        name=route_name,
    )
