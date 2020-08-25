
"""
Generic approach to moving events between handlers.
The approach here is that there is a many-to-one relationship between
handlers and event pipes.
"""

from typing import Dict, Iterable, List, Coroutine, Any
import asyncio
from petronia_common.util import (
    RET_OK_NONE,
    StdRet,
    collect_errors_from, PetroniaReturnError,
)
from petronia_common.util import i18n as _
from petronia_common.event_stream import (
    RawEventObject, EventForwarderTarget, BinaryWriter,
    raw_event_id, raw_event_source_id, raw_event_target_id,
)
from .channel import EventChannel
from .handler import EventTargetHandle


class EventRouter:
    """Routes events between destinations based on their registered
    event handlers.  Access to the router is intended to be run from
    within an asyncio process, because the read and write processes
    can run independently.  Each router should have its own lock."""
    __slots__ = ('__channels', '__lock', '__target')

    def __init__(self, lock: asyncio.Semaphore, target: EventForwarderTarget) -> None:
        self.__channels: Dict[str, EventChannel] = {}
        self.__lock = lock
        self.__target = target

    async def add_channel(
            self,
            name: str,
            reader: asyncio.StreamReader,
            writer: BinaryWriter,
    ) -> StdRet[Coroutine[Any, Any, None]]:
        """Registers a new channel to the router.  If a channel
        with the same name is already registered, an error is returned.
        Otherwise, the channel is registered.

        Returns the co-routine that starts the channel's processing.
        """
        async with self.__lock:
            if name in self.__channels:
                return StdRet.pass_errmsg(
                    _('channel {name} already registered'),
                    name=name,
                )
            channel = EventChannel(name, reader, writer, self._on_channel_consume_error)
            # Register this channel with all the other channels, so it receives their messages,
            # and vice-versa.  Note that this is done before registering the new channel, so it
            # doesn't receive its own events.
            for other in self.__channels.values():
                other.add_event_consumer(channel)
                channel.add_event_consumer(other)
            channel.add_event_consumer(self.__target)
            self.__channels[name] = channel
            return StdRet.pass_ok(channel.process_stream())

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

    async def add_handler(
            self, channel_name: str, handler_id: str,
            produces: Iterable[str], consumes: Iterable[EventTargetHandle],
    ) -> StdRet[None]:
        """Adds the handler to the channel with the given name.  If the
        handler ID is registered anywhere, or the channel does not exist, then
        an error is returned."""
        # This is intended to be an infrequent operation, so it is slow.
        async with self.__lock:
            for channel in self.__channels.values():
                if channel.contains_handler_id(handler_id):
                    return StdRet.pass_errmsg(
                        _('handler {handler_id} already registered in channel {name}'),
                        handler_id=handler_id,
                        channel=channel.name,
                    )
            maybe_channel = self.__channels.get(channel_name)
            if not maybe_channel:
                return StdRet.pass_errmsg(
                    _('channel {name} not registered'),
                    name=channel_name,
                )
            return maybe_channel.add_handler(handler_id, produces, consumes).forward()

    async def remove_handler(self, handler_id: str) -> bool:
        """Removes the handler from its registered channel.
        Returns True if it was successfully removed."""
        # This is assumed to be an infrequent operation, so it is slow.
        async with self.__lock:
            for channel in self.__channels.values():
                if channel.remove_handler(handler_id):
                    return True
            return False

    async def add_handler_listener(
            self,
            handler_id: str,
            event_id: str, target_id: str,
    ) -> bool:
        """Registers the event / target listener with the handler."""
        async with self.__lock:
            for channel in self.__channels.values():
                if channel.contains_handler_id(handler_id):
                    ret = channel.add_handler_listener(handler_id, event_id, target_id)
                    return ret.ok
        return False

    async def remove_handler_listener(
            self,
            handler_id: str,
            event_id: str, target_id: str,
    ) -> bool:
        """Removes the event / target listener from the handler."""
        async with self.__lock:
            for channel in self.__channels.values():
                if channel.contains_handler_id(handler_id):
                    ret = channel.remove_handler_listener(handler_id, event_id, target_id)
                    return ret.ok
        return False

    async def inject_event(self, event: RawEventObject) -> StdRet[None]:
        """Injects an event into all the channels.
        If the event can be sent to multiple channels, then all the
        channels will be called, regardless of whether any one generates
        an error.  All errors are returned.

        For the moment, this only supports injecting object events, not binary blob events.
        Binary blob events require more work to properly support.
        """
        futures: List[Coroutine[Any, Any, bool]] = []
        event_id = raw_event_id(event)
        source_id = raw_event_source_id(event)
        target_id = raw_event_target_id(event)

        async with self.__lock:
            for channel in self.__channels.values():
                if channel.can_consume(event_id, source_id, target_id):
                    futures.append(channel.consume(event))

        ret_list = await asyncio.gather(*futures)
        error = collect_errors_from(ret_list)
        if error:
            return StdRet.pass_error(error)
        return RET_OK_NONE

    def _on_channel_consume_error(self, _name: str, error: PetroniaReturnError) -> bool:
        """Called when an error happened during the consume process."""
        return self.__target.on_error(error)
