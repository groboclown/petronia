
"""
Generic approach to moving events between handlers.
The approach here is that there is a many-to-one relationship between
handlers and event pipes.
"""

from typing import Dict, Iterable, Tuple, Callable, Optional, Union, Any
import re
import threading
from concurrent.futures import ThreadPoolExecutor
from petronia_common.util import (
    RET_OK_NONE,
    StdRet,
    PetroniaReturnError,
)
from petronia_common.util import i18n as _
from petronia_common.event_stream import (
    RawEventObject, EventForwarderTarget, BinaryWriter, BinaryReader,
    raw_event_id, raw_event_source_id, raw_event_target_id, as_raw_event_object_data,
    RawBinaryReader,
)
from .channel import EventChannel, InternalEventHandler
from .handler import EventTargetHandle
from .reservations import ChannelReservations, ChannelReservationCallback
from ..user_message import CATALOG


class EventRouter:
    """Routes events between destinations based on their registered
    event handlers.  Access to the router is intended to be run from
    within an asyncio process, because the read and write processes
    can run independently.  Each router should have its own lock.

    The router has a global target for the owner of the router to
    listen in on all events read by channels.  Injected events directed to a
    channel are not received by the global target.

    In this model, a channel represents a launcher process unit, and a handler represents a
    loaded extension within the channel.  A loaded extension can register multiple event listeners.
    """
    __slots__ = ('__channels', '__executor', '__lock', '__target', '__reservations',)

    def __init__(
            self,
            lock: threading.Semaphore,
            target: Optional[EventForwarderTarget] = None,
            executor: Optional[ThreadPoolExecutor] = None,
    ) -> None:
        if executor is None:
            self.__executor = ThreadPoolExecutor()
        else:
            self.__executor = executor
        self.__channels: Dict[str, EventChannel] = {}
        self.__reservations = ChannelReservations()
        self.__lock = lock
        self.__target = target

    def get_channel_for_handler(self, handler_id: str) -> Optional[str]:
        """Get the channel name that owns the handler_id."""
        with self.__lock:
            for channel in self.__channels.values():
                if channel.contains_handler_id(handler_id):
                    return channel.name
        return None

    def get_registered_channel_names(self) -> Iterable[str]:
        """Get all registered channel names."""
        with self.__lock:
            return list(self.__channels.keys())

    def add_reservation_callback(
            self,
            channel: Union[str, re.Pattern],
            callback: ChannelReservationCallback,
    ) -> StdRet[None]:
        """Add a channel pattern reservation.  When a channel with the given pattern is reserved,
        then the callback is invoked to see if it can be reserved, and if so, an event target
        handler to listen in on responses from the channel."""
        return self.__reservations.add_channel_reservation_callback(channel, callback)

    def register_channel(
            self,
            name: str,
            channel_creator: Callable[
                [],
                StdRet[Tuple[BinaryReader, BinaryWriter]],
            ],
    ) -> StdRet[None]:
        """Perform the channel registration process.

        If a channel with the same name is already registered, an error is returned.
        Otherwise, the channel is registered.

        The channel will be registered with an EOF target listener that will automatically
        close the channel in this router.  The channel launcher will need to close off the
        access correctly on its own as part of its stream handling.

        The channel_creator will not be called if the reservation of the channel name
        was prevented.
        """
        with self.__lock:
            reserve_resp = self.__reservations.reserve_channel(name)
            if reserve_resp.has_error:
                return reserve_resp.forward()
            target = reserve_resp.value
        mk_channel_resp = channel_creator()
        if mk_channel_resp.has_error:
            with self.__lock:
                self.__reservations.release_channel(name)
            return mk_channel_resp.forward()

        reader, writer = mk_channel_resp.result
        channel = EventChannel(name, reader, writer, self._on_channel_consume_error)
        if self.__target:
            channel.add_event_consumer(self.__target)
        if target:
            # print(f"Adding registered target to channel {name}")
            channel.add_event_consumer(target)

        def on_close() -> None:
            # print(f"Closing channel {name} due to EOF")
            self.__executor.submit(self.close_channel, name)

        channel.add_event_consumer(OnCloseTarget(on_close))

        # Register this channel with all the other channels, so it receives their messages,
        # and vice-versa.  Note that this is done before registering the new channel, so it
        # doesn't receive its own events.
        with self.__lock:
            for other in self.__channels.values():
                other.add_event_consumer(channel)
                channel.add_event_consumer(other)
            self.__channels[name] = channel

            # Process the stream in the background.
            # Note that this is done still within the lock,
            # to prevent weird issues with close_channel.
            self.__executor.submit(channel.process_stream)

        return RET_OK_NONE

    def close_channel(self, name: str) -> bool:
        """Close the registered channel.  If the channel is already
        closed, or isn't registered, False is returned.  This is done
        automatically when the channel encounters an EOF, but there
        may be situations where it needs to be done manually.  Stream
        closing must be done outside of this."""
        # Under the covers, this removes the channel from the internal
        # lists.
        with self.__lock:
            channel = self.__channels.get(name)
            if channel:
                del self.__channels[name]
                channel.close_access()
                self.__reservations.release_channel(name)
                return True
        # If the channel is reserved but not allocated yet,
        # then it isn't released.
        return False

    def add_handler(
            self, channel_name: str, handler_id: str,
            produces: Iterable[str], consumes: Iterable[EventTargetHandle],
            source_id_prefixes: Iterable[str],
    ) -> StdRet[None]:
        """Adds the handler to the channel with the given name.  If the
        handler ID is registered anywhere, or the channel does not exist, then
        an error is returned."""
        # This is intended to be an infrequent operation, so it is slow.
        with self.__lock:
            for channel in self.__channels.values():
                if channel.contains_handler_id(handler_id):
                    return StdRet.pass_errmsg(
                        CATALOG,
                        _('handler {handler_id} already registered in channel {name}'),
                        handler_id=handler_id,
                        channel=channel.name,
                    )
            maybe_channel = self.__channels.get(channel_name)
            if not maybe_channel:
                return StdRet.pass_errmsg(
                    CATALOG,
                    _('channel {name} not registered'),
                    name=channel_name,
                )
            return maybe_channel.add_handler(
                handler_id, produces, consumes, source_id_prefixes,
            ).forward()

    def remove_handler(self, handler_id: str) -> bool:
        """Removes the handler from its registered channel.
        Returns True if it was successfully removed."""
        # This is assumed to be an infrequent operation, so it is slow.
        with self.__lock:
            for channel in self.__channels.values():
                if channel.remove_handler(handler_id).ok:
                    return True
        return False

    def add_handler_listener(
            self,
            handler_id: str,
            event_id: Optional[str], target_id: Optional[str],
    ) -> bool:
        """Registers the event / target listener with the handler."""
        with self.__lock:
            for channel in self.__channels.values():
                if channel.contains_handler_id(handler_id):
                    ret = channel.add_handler_listener(handler_id, event_id, target_id)
                    return ret.ok
        return False

    def remove_handler_listener(
            self,
            handler_id: str,
            event_id: Optional[str], target_id: Optional[str],
    ) -> bool:
        """Removes the event / target listener from the handler."""
        with self.__lock:
            for channel in self.__channels.values():
                if channel.contains_handler_id(handler_id):
                    ret = channel.remove_handler_listener(handler_id, event_id, target_id)
                    return ret.ok
        return False

    def add_internal_event_handler(
            self, channel_name: str, handler: InternalEventHandler,
    ) -> StdRet[None]:
        """Add an internal event handler for the channel."""
        with self.__lock:
            channel = self.__channels.get(channel_name)
            if not channel:
                return StdRet.pass_errmsg(
                    CATALOG,
                    _('no such channel {name}'),
                    name=channel_name,
                )
            channel.add_internal_event_handler(handler)
        return RET_OK_NONE

    def inject_event(self, event: RawEventObject) -> StdRet[None]:
        """Injects an event into all the channels.
        If the event can be sent to multiple channels, then all the
        channels will be called, regardless of whether any one generates
        an error.  All errors are returned.

        For the moment, this only supports injecting object events, not binary blob events.
        Binary blob events require more work to properly support.
        """
        event_id = raw_event_id(event)
        source_id = raw_event_source_id(event)
        target_id = raw_event_target_id(event)
        event_data = as_raw_event_object_data(event)

        channels = []
        with self.__lock:
            for channel in self.__channels.values():
                if channel.can_consume(event_id, source_id, target_id):
                    channels.append(channel)

        for channel in channels:
            res = channel.consume_object(event_id, source_id, target_id, event_data)
            if res:
                # print(f"consume returned True for channel {channel.name}; closing it (1)")
                self.close_channel(channel.name)
        return RET_OK_NONE

    def inject_event_to_channel(
            self, channel_name: str, event: RawEventObject,
    ) -> StdRet[None]:
        """Injects an event into a single channel.  Used for a more secure communication.

        For the moment, this only supports injecting object events, not binary blob events.
        Binary blob events require more work to properly support.
        """
        event_id = raw_event_id(event)
        source_id = raw_event_source_id(event)
        target_id = raw_event_target_id(event)

        with self.__lock:
            channel = self.__channels.get(channel_name)
            if not channel:
                return StdRet.pass_errmsg(
                    CATALOG,
                    _('channel not registered ({channel})'),
                    channel=channel_name,
                )
        if channel.can_consume(event_id, source_id, target_id):
            event_data = as_raw_event_object_data(event)
            res = channel.consume_object(event_id, source_id, target_id, event_data)
            if res:
                self.close_channel(channel_name)
                # print(f"consume returned True for channel {channel.name}; closing it (2)")
        return RET_OK_NONE

    def _on_channel_consume_error(self, _name: str, error: PetroniaReturnError) -> bool:
        """Called when an error happened during the consume process."""
        if self.__target:
            return self.__target.on_error(error)
        return False


class OnCloseTarget(EventForwarderTarget):
    """Runs a callback when an EOF is encountered."""

    __slots__ = ('__callback',)

    def __init__(self, callback: Callable[[], None]) -> None:
        self.__callback = callback

    def can_consume(self, event_id: str, source_id: str, target_id: str) -> bool:
        return False

    def consume_object(
            self, event_id: str, source_id: str, target_id: str, event_data: Dict[str, Any],
    ) -> bool:
        return False

    def consume_binary(
            self, event_id: str, source_id: str, target_id: str, size: int,
            data_reader: RawBinaryReader,
    ) -> bool:
        data_reader(size)
        return False

    def on_error(self, error: PetroniaReturnError) -> bool:
        return False

    def on_eof(self) -> None:
        self.__callback()
