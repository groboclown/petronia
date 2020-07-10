
"""
Generic approach to moving events between handlers.
The approach here is that there is a many-to-one relationship between
handlers and event pipes.
"""

from typing import Dict, Set, Callable, Coroutine, Any
import asyncio
from petronia_common.util import (
    RET_OK_NONE, RET_OK_TRUE, RET_OK_FALSE,
    StdRet,
)
from petronia_common.util import i18n as _
from petronia_common.event_stream import (
    BROADCAST_EVENT_TARGET_ID,
    RawEvent,
    raw_event_id,
    raw_event_source_id,
    raw_event_target_id,
)
from .handler import EventHandler


EventRouteDestinationCallback = Callable[[RawEvent], StdRet[None]]


class EventChannel:
    """
    A source and destination with the associated handlers.
    The handlers associated with the channel are viewed as being attached
    to "the other side" - writing events on the channel means that the
    handlers are listening / consuming the event, and reading from the
    channel means the handlers are sending / producing the event.
    """
    __slots__ = ('__name', '__handlers', '__callback', '__alive')

    def __init__(
            self,
            name: str,
            output_callback: EventRouteDestinationCallback,
    ) -> None:
        self.__name = name
        self.__callback = output_callback
        self.__handlers: Dict[str, EventHandler] = {}
        self.__alive = True

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
        return handler_id in self.__handlers

    def add_handler(self, handler: EventHandler) -> StdRet[None]:
        """Add an event handler to this channel.  If the
        handler already has the same ID registered, an error
        is returned."""
        if not self.__alive:
            return StdRet.pass_errmsg(
                _('route {name} is closed'),
                name=self.__name,
            )
        if handler.handler_id in self.__handlers:
            return StdRet.pass_errmsg(
                _('handler {handler_id} already registered in channel {name}'),
                handler_id=handler.handler_id, name=self.__name,
            )
        self.__handlers[handler.handler_id] = handler
        return RET_OK_NONE

    def remove_handler(self, handler_id: str) -> bool:
        """Attempts to remove the handler from the internal
        store.  If it is removed, then True is returned."""
        if handler_id in self.__handlers:
            del self.__handlers[handler_id]
            return True
        return False

    def get_handler_ids(self) -> Set[str]:
        """All the handler IDs that this channel handles.
        This allows the router to optimize the destinations."""
        return set(self.__handlers.keys())

    def can_produce(self, event: RawEvent) -> bool:
        """Can this channel produce this event?  That is, is an event
        read from the channel in the list of registered produced event IDs?"""
        if not self.__alive:
            return False
        source_id = raw_event_source_id(event)
        source_handler = self.__handlers.get(source_id)
        if source_handler:
            event_id = raw_event_id(event)
            return source_handler.can_produce(event_id)
        return False

    def can_consume(self, event: RawEvent) -> bool:
        """Can this channel consume this event?  That is, can an
        event ID be written to this channel?"""
        if not self.__alive:
            return False
        target_id = raw_event_target_id(event)
        if target_id == BROADCAST_EVENT_TARGET_ID:
            # This may be too slow...
            # Could instead first check the number of handlers, and if that
            # is over a limit, then just send it regardless of whether any
            # of them can handle this event.
            event_id = raw_event_id(event)
            for handler in self.__handlers.values():
                if handler.can_consume(event_id, None):
                    return True
            return False
        target_handler = self.__handlers.get(target_id)
        if target_handler:
            event_id = raw_event_id(event)
            return target_handler.can_consume(event_id, target_id)
        return False

    def create_producer_filter(
            self,
            lock: asyncio.Semaphore,
            pass_through_cb: Callable[[RawEvent], bool],
            invalid_source_cb: Callable[[RawEvent], bool],
    ) -> Callable[[RawEvent], Coroutine[Any, Any, bool]]:
        """
        Returns a function that acts as a filter for the event stream
        reader event handler (read == handler produced the event).
        If the event that was read can come
        from this single route, then it is passed on to the
        `pass_through_cb` function.  If it was not allowed to come from
        this single route, then it is passed to the
        `invalid_source_cb` function.  The return value from those
        callbacks is returned to the invocation, which controls whether
        to keep this

        :param lock:
        :param pass_through_cb:
        :param invalid_source_cb:
        :return:
        """
        async def callback(event: RawEvent) -> bool:
            async with lock:
                if not self.is_alive():
                    # If this channel is no longer alive, then
                    # tell the reader to stop reading.
                    return False
                if self.can_produce(event):
                    return pass_through_cb(event)
                return invalid_source_cb(event)
        return callback

    def consume(self, event: RawEvent) -> StdRet[bool]:
        """Attempt to consume the event.  This does not require
        the `can_consume` to have been called first, so calling
        both will be a performance penalty.  If this can't consume
        the event, False is returned.  If it is consumed, then
        either an error is generated (if the callback creates one)
        or True."""
        if self.can_consume(event):
            result = self.__callback(event)
            if result.error:
                return result.forward()
            return RET_OK_TRUE
        return RET_OK_FALSE
