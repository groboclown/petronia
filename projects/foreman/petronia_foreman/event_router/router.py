
"""
Generic approach to moving events between handlers.
The approach here is that there is a many-to-one relationship between
handlers and event pipes.
"""

from typing import Dict, List, Callable, Coroutine, Any
import asyncio
from petronia_common.util import (
    RET_OK_NONE,
    StdRet,
    collect_errors_from,
)
from petronia_common.util import i18n as _
from petronia_common.event_stream import (
    RawEvent,
)
from .handler import EventHandler
from .channel import EventChannel


EventRouteDestinationCallback = Callable[[RawEvent], StdRet[None]]


class EventRouter:
    """Routes events between destinations based on their registered
    event handlers.  Access to the router is intended to be run from
    within an asyncio process, because the read and write processes
    can run independently.  Each router should have its own lock."""
    __slots__ = ('__channels', '__lock',)

    def __init__(self, lock: asyncio.Semaphore) -> None:
        self.__channels: Dict[str, EventChannel] = {}
        self.__lock = lock

    async def add_channel(
            self,
            name: str,
            output_callback: EventRouteDestinationCallback,
            pass_through_cb: Callable[[RawEvent], bool],
            invalid_source_cb: Callable[[RawEvent], bool],
    ) -> StdRet[Callable[[RawEvent], Coroutine[Any, Any, bool]]]:
        """Registers a new channel to the router.  If a channel
        with the same name is already registered, an error is returned.
        Otherwise, the event stream read callback is returned."""
        async with self.__lock:
            if name in self.__channels:
                return StdRet.pass_errmsg(
                    _('channel {name} already registered'),
                    name=name,
                )
            channel = EventChannel(name, output_callback)
            callback = channel.create_producer_filter(
                self.__lock,
                pass_through_cb, invalid_source_cb,
            )
            self.__channels[name] = channel
            return StdRet.pass_ok(callback)

    async def close_channel(self, name: str) -> bool:
        """Close the registered channel.  If the channel is already
        closed, or isn't registered, False is returned."""
        # Under the covers, this removes the channel from the internal
        # lists.
        async with self.__lock:
            channel = self.__channels.get(name)
            if channel:
                del self.__channels[name]
                channel.close_access()
                return True
            return False

    async def add_handler(self, handler: EventHandler, channel_name: str) -> StdRet[None]:
        """Adds the handler to the channel with the given name.  If the
        handler ID is registered anywhere, or the channel does not exist, then
        an error is returned."""
        # This is intended to be an infrequent operation, so it is slow.
        async with self.__lock:
            for channel in self.__channels.values():
                if channel.contains_handler_id(handler.handler_id):
                    return StdRet.pass_errmsg(
                        _('handler {handler_id} already registered in channel {name}'),
                        handler_id=handler.handler_id,
                        channel=channel.name,
                    )
            maybe_channel = self.__channels.get(channel_name)
            if not maybe_channel:
                return StdRet.pass_errmsg(
                    _('channel {name} not registered'),
                    name=channel_name,
                )
            return maybe_channel.add_handler(handler).forward()

    async def remove_handler(self, handler_id: str) -> bool:
        """Removes the handler from its registered channel.
        Returns True if it was successfully removed."""
        # This is assumed to be an infrequent operation, so it is slow.
        async with self.__lock:
            for channel in self.__channels.values():
                if channel.remove_handler(handler_id):
                    return True
            return False

    async def send_event(self, event: RawEvent) -> StdRet[None]:
        """Sends the event to handlers that listen to the event.
        If the event can be sent to multiple channels, then all the
        channels will be called, regardless of whether any one generates
        an error.  All errors are returned."""
        ret_list: List[StdRet[bool]] = []

        # FIXME THIS IS VERY WRONG.
        # The event can be binary with a one-time reader.  This means
        # that we need to fork the reader once per channel, so it is
        # only read once.
        # And, because we're using asyncio, the 'consume' method should
        # be async.  This means the calls should be gathered together and
        # run async.

        # Send to all channels, regardless of the marked target.
        # This isn't too efficient.  Instead, we should have
        # each event ID and associated handles, including "*",
        # pointing to the associated channels, for the listeners.
        async with self.__lock:
            for channel in self.__channels.values():
                ret_list.append(channel.consume(event))

        error = collect_errors_from(*ret_list)
        if error:
            return StdRet.pass_error(error)
        return RET_OK_NONE
