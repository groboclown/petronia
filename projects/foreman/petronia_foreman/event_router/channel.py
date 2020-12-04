
"""
Each channel represents an event stream pipe, which has multiple producers and consumers
associated with it.  The channel is expected to perform its own internal routing of the
produced events, which means that events produced from a channel must not be directed
back into the channel.
"""

from typing import Iterable, Callable, Coroutine, Optional, Any
from petronia_common.util import (
    StdRet, PetroniaReturnError,
)
from petronia_common.util import i18n as _
from petronia_common.event_stream import (
    RawEvent,
    is_raw_event_object,
    raw_event_id,
    raw_event_source_id,
    raw_event_target_id,
    raw_event_binary_size,
    as_raw_event_object_data,
    as_raw_event_binary_data_reader,
    EventForwarderTarget,
    EventForwarder,
    BinaryWriter,
    BinaryReader,
    write_object_event_to_stream,
    write_binary_event_to_stream,
)
from petronia_common.event_stream.thread_stream import ThreadedStreamForwarder
from .handler import EventHandlerSet, EventTargetHandle
from ..user_message import CATALOG


EventRouteDestinationCallback = Callable[[RawEvent], Coroutine[Any, Any, StdRet[None]]]


class EventChannel(EventForwarderTarget):
    """
    A source and destination with the associated handlers.
    The handlers associated with the channel are viewed as being attached
    to "the other side" - writing events on the channel means that the
    handlers are listening / consuming the event, and reading from the
    channel means the handlers are sending / producing the event.
    """

    __slots__ = ('__name', '__handlers', '__forwarder', '__writer', '__alive', '__on_error',)

    def __init__(
            self,
            name: str,
            reader: BinaryReader,
            writer: BinaryWriter,
            on_error: Callable[[str, PetroniaReturnError], bool],
    ) -> None:
        self.__name = name
        self.__forwarder = EventForwarder(
            reader, ThreadedStreamForwarder(), self._cant_produce,
        )
        self.__writer = writer
        self.__handlers = EventHandlerSet()
        self.__on_error = on_error
        self.__alive = True

    def process_stream(self) -> None:
        """Run the stream processing."""
        self.__forwarder.handle_source()

    @property
    def name(self) -> str:
        """The event channel name."""
        return self.__name

    def is_alive(self) -> bool:
        """Is this channel still receiving events and sending them?
        The channel can only be closed, which makes this return False."""
        return self.__alive

    def close_access(self) -> None:
        """Sets the alive flag to False, which stops this channel from
        allowing new handlers, producing events, and consuming events.
        This function may be safely called multiple times."""
        self.__alive = False

    def contains_handler_id(self, handler_id: str) -> bool:
        """Does this channel contain this handler?"""
        return self.__handlers.contains_handler_id(handler_id)

    def add_event_consumer(self, target: EventForwarderTarget) -> None:
        """Add the given target as a consumer for this channel's events.  These are
        removed by their call-backs returning the correct value."""
        self.__forwarder.add_target(target)

    def add_handler(
            self, handler_id: str, produces: Iterable[str], consumes: Iterable[EventTargetHandle],
    ) -> StdRet[None]:
        """Add an event handler to this channel.  If the
        handler already has the same ID registered, an error
        is returned."""
        if not self.__alive:
            return StdRet.pass_errmsg(
                CATALOG,
                _('route {name} is closed'),
                name=self.__name,
            )
        return self.__handlers.add_handler(handler_id, produces, consumes)

    def remove_handler(self, handler_id: str) -> StdRet[None]:
        """Attempts to remove the handler from the internal
        store.  If it is removed, then True is returned.  This can be safely called
        after the channel is closed."""
        return self.__handlers.remove_handler(handler_id)

    def add_handler_listener(
            self,
            handler_id: str,
            event_id: Optional[str], target_id: Optional[str],
    ) -> StdRet[None]:
        """Registers the event / target listener with the handler."""
        if not self.__alive:
            return StdRet.pass_errmsg(
                CATALOG,
                _('route {name} is closed'),
                name=self.__name,
            )
        return self.__handlers.add_listener(handler_id, event_id, target_id)

    def remove_handler_listener(
            self,
            handler_id: str,
            event_id: Optional[str], target_id: Optional[str],
    ) -> StdRet[None]:
        """Removes the event / target listener from the handler."""
        if not self.__alive:
            return StdRet.pass_errmsg(
                CATALOG,
                _('route {name} is closed'),
                name=self.__name,
            )
        return self.__handlers.remove_listener(handler_id, event_id, target_id)

    def can_produce(self, event_id: str) -> bool:
        """Can this channel produce this event?  That is, is an event
        read from the channel in the list of registered produced event IDs?"""
        if not self.__alive:
            return False
        return self.__handlers.can_produce(event_id)

    def _cant_produce(self, event_id: str, _event_source_id: str, _event_target_id: str) -> bool:
        return not self.can_produce(event_id)

    # ------------------------------------------------------------------------------
    # Forwarder Target Methods.
    # These are called by other channels into this channel when the other
    # channel produces an event that this channel may consume.

    def can_consume(self, event_id: str, source_id: str, target_id: str) -> bool:
        """Can this channel consume this event?  That is, can an
        event ID be written to this channel?"""
        if not self.__alive:
            return False
        return self.__handlers.can_consume(event_id, target_id)

    def on_error(self, error: PetroniaReturnError) -> bool:
        # The other channel encountered a read error, and is telling this channel
        # about it.  This channel doesn't care about that message.
        if not self.__alive:
            return True
        # Do nothing...
        return False

    def on_eof(self) -> None:
        # The other channel encountered an EOF, and is telling this channel
        # about it.  This channel doesn't care about that message.
        pass

    def consume(self, event: RawEvent) -> bool:
        # can_consume has already been called and returned True.
        if not self.__alive:
            return True
        event_id = raw_event_id(event)
        source_id = raw_event_source_id(event)
        target_id = raw_event_target_id(event)
        ret: StdRet[None]
        if is_raw_event_object(event):
            ret = write_object_event_to_stream(
                self.__writer,
                event_id,
                source_id,
                target_id,
                as_raw_event_object_data(event),
            )
        else:
            ret = write_binary_event_to_stream(
                self.__writer,
                event_id,
                source_id,
                target_id,
                raw_event_binary_size(event),
                as_raw_event_binary_data_reader(event),
            )
        if ret.has_error:
            # This is a real error that the channel cares about.
            if self.__on_error(self.name, ret.valid_error):
                self.close_access()
                return True
        return False
