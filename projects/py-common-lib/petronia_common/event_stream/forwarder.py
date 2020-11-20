
"""
A streaming reader that forks the read to many streams.
"""

from typing import List, Callable, Coroutine, Optional, Any
import asyncio
from ..util import PetroniaReturnError, EMPTY_LIST
from .defs import (
    RawEvent, RawBinaryReader,
    raw_event_id, raw_event_source_id, raw_event_target_id,
    raw_event_binary_size,
    is_raw_event_object, is_raw_event_binary,
    as_raw_event_binary_data_reader,
    to_raw_event_binary,
)
from .reader import read_event_stream


READ_SIZE_LIMIT = 4 * 1024


class EventForwarderTarget:
    """Interface for targets of events."""
    __slots__ = ()

    def can_consume(self, event_id: str, source_id: str, target_id: str) -> bool:
        """Can this target handle the given event?"""
        raise NotImplementedError()  # pragma no cover

    def on_error(self, error: PetroniaReturnError) -> bool:
        """Handler for stream errors.  If this returns True, then
        the target is de-registered."""
        raise NotImplementedError()  # pragma no cover

    def on_eof(self) -> None:
        """Called when the stream is closed.  The target will no longer be
        used by the forwarder."""
        raise NotImplementedError()  # pragma no cover

    async def consume(self, event: RawEvent) -> bool:
        """Called if the `can_consume` method returns True.
        If this returns True, then the target will be de-registered."""
        raise NotImplementedError()  # pragma no cover


class EventForwarder:
    """
    Reads in packets from the source, and passes them to the targets.

    It's designed to not pass partial data to the targets.
    """
    __slots__ = ('__source', '__targets', '__pending_targets', '__filter', '__alive')

    def __init__(
            self, source: asyncio.StreamReader,
            event_filter: Optional[Callable[[str, str, str], bool]] = None,
    ) -> None:
        self.__source = source
        self.__filter = event_filter
        self.__targets: List[EventForwarderTarget] = []
        self.__pending_targets: List[EventForwarderTarget] = []
        self.__alive = True

    @property
    def alive(self) -> bool:
        """Is this forwarder still running?"""
        return self.__alive

    def add_target(self, target: EventForwarderTarget) -> None:
        """Add a new target to the forwarder.  The target will receive new
        messages once the next event comes in, or if the stream is already
        at an end.  The `on_eof` function can be called immediately."""
        if not self.__alive:
            target.on_eof()
        else:
            self.__pending_targets.append(target)

    async def handle_source(self) -> None:
        """Background pipe reader and forwarder to all the targets."""
        self._manage_targets(EMPTY_LIST)
        await read_event_stream(
            self.__source,
            self._event_listener,
            self._end_of_stream,
            self._error_listener,
        )

    def _end_of_stream(self) -> None:
        if self.__alive:
            self.__alive = False
            for target in self.__targets:
                target.on_eof()
            for target in self.__pending_targets:
                target.on_eof()
            self.__targets.clear()
            self.__pending_targets.clear()

    def _error_listener(self, error: PetroniaReturnError) -> bool:
        assert self.__alive
        to_remove: List[EventForwarderTarget] = []
        for target in self.__targets:
            if target.on_error(error):
                to_remove.append(target)
        return self._manage_targets(to_remove)

    async def _event_listener(self, event: RawEvent) -> bool:
        assert self.__alive
        event_id = raw_event_id(event)
        source_id = raw_event_source_id(event)
        target_id = raw_event_target_id(event)
        to_remove: List[EventForwarderTarget] = []
        to_call: List[EventForwarderTarget] = []

        if self.__filter and self.__filter(event_id, source_id, target_id):
            return self._manage_targets([])

        for target in self.__targets:
            if target.can_consume(event_id, source_id, target_id):
                to_call.append(target)
        if to_call:
            to_remove = await self._send_event(event, to_call)
        else:
            # No targets for this event.  So the event reader needs to
            # be drained.
            await EventForwarder._drain_event(event)
        return self._manage_targets(to_remove)

    async def _send_event(
            self, event: RawEvent, targets: List[EventForwarderTarget],
    ) -> List[EventForwarderTarget]:
        assert self.__alive
        to_remove: List[EventForwarderTarget] = []
        event_id = raw_event_id(event)
        event_source_id = raw_event_source_id(event)
        event_target_id = raw_event_target_id(event)

        if is_raw_event_object(event):
            # Simple handling, because the data is already fully read.
            for target in self.__targets:
                if target.consume(event):
                    to_remove.append(target)
        else:
            # Binary object.  This is more complicated.  We must forward the
            # event to each target, but in a memory safe way.
            to_remove = await stream_forwarder(
                event_id,
                event_source_id,
                event_target_id,
                raw_event_binary_size(event),
                as_raw_event_binary_data_reader(event),
                targets,
                READ_SIZE_LIMIT,
            )
        return to_remove

    @staticmethod
    async def _drain_event(event: RawEvent) -> None:
        if is_raw_event_binary(event):
            reader = as_raw_event_binary_data_reader(event)
            # Loop until we receive 0 bytes from the reader.
            while len(await reader()) > 0:
                pass
        # The other type is already fully read.

    def _manage_targets(self, removed: List[EventForwarderTarget]) -> bool:
        # Don't need to be alive to call this...
        new_targets: List[EventForwarderTarget] = []
        for target in self.__targets:
            if target not in removed:
                new_targets.append(target)
        new_targets.extend(self.__pending_targets)
        self.__pending_targets.clear()
        self.__targets = new_targets
        # Return True if there are no more targets to process the stream.
        return not self.__targets


async def stream_forwarder(  # pylint: disable=too-many-arguments,too-many-locals
        event_id: str,
        source_id: str,
        target_id: str,
        blob_size: int,
        reader: RawBinaryReader,
        targets: List[EventForwarderTarget],
        read_size: int,
) -> List[EventForwarderTarget]:
    """Forwards a binary event to 1 or more targets.
    It needs to read in a bit of data (up to the read_size),
    pass that on to each of the targets' readers, wait for those
    targets to finish consuming that data, then repeat until the
    data is fully processed."""
    streams: List[StreamedBinaryReader] = []
    processes: List[Coroutine[Any, Any, None]] = []
    to_remove: List[EventForwarderTarget] = []
    data_read_condition = asyncio.Condition()

    def can_read_next() -> bool:
        ret = True
        for stream in streams:
            ret = ret and stream.is_buffer_consumed()
        # print(f" -- Remaining stream data to read: {ret}")
        return ret

    def mk_handle_target(
            target: EventForwarderTarget,
            stream: StreamedBinaryReader,
    ) -> Coroutine[Any, Any, None]:
        async def handle_target() -> None:
            res = await target.consume(
                to_raw_event_binary(event_id, source_id, target_id, blob_size, stream),
            )
            if res:
                to_remove.append(target)
        return handle_target()

    for tgt in targets:
        stm = StreamedBinaryReader(data_read_condition)
        streams.append(stm)
        # Note: no await here.
        processes.append(mk_handle_target(tgt, stm))
    if not streams:
        # drain the reader
        while await reader(read_size) != b'':
            pass
        return to_remove

    async def forward_stream() -> None:
        running = True
        while running:
            # Process some data...
            data = await reader(read_size)
            for stream in streams:
                if not data:
                    # print(" !! sending EOF to stream")
                    stream.feed_eof()
                    running = False
                else:
                    # print(f" !! sending {len(data)} bytes of data to stream")
                    stream.feed_data(data)

            # Wait for the forwarding to be consumed...
            async with data_read_condition:
                # print("Waiting on data to be read...")
                if not can_read_next():
                    await data_read_condition.wait_for(can_read_next)

    processes.append(forward_stream())
    await asyncio.gather(*processes)
    return to_remove


class StreamedBinaryReader:
    """Pushes data to a stream, and notifies a condition when the buffer is read."""
    __slots__ = ('__condition', '__buffer', '__eof', '__waiter', '__loop')

    def __init__(self, condition: asyncio.Condition) -> None:
        self.__loop = asyncio.events.get_event_loop()
        self.__condition = condition
        self.__waiter: Optional[asyncio.Future[int]] = None  # pylint: disable=unsubscriptable-object
        self.__buffer = bytearray()
        self.__eof = False

    def is_buffer_consumed(self) -> bool:
        """Is there no more data to read in this buffer?"""
        # print(f" -- buffer size == {len(self.__buffer)}")
        return len(self.__buffer) <= 0

    def feed_data(self, buff: bytes) -> None:
        """Feed data to the stream."""
        # print(f" -- pumping {len(buff)} bytes of data")
        self.__buffer += buff
        # print(f" -- -- {len(self.__buffer)} bytes left to read (+ {len(buff)} bytes)")
        if self.__waiter:
            # print(f" -- -- notified waiting code.")
            self.__waiter.set_result(1)

    def feed_eof(self) -> None:
        """Feed an EOF to the stream."""
        # print(f" -- told EOF to reader")
        self.__eof = True
        if self.__waiter:
            # print(f" -- -- notified waiting code.")
            self.__waiter.set_result(1)

    async def __call__(self, max_read_count: int = -1) -> bytes:
        return await self.read_data(max_read_count)

    async def read_data(self, max_read_count: int) -> bytes:
        """Read data from the buffer, or wait for it to be loaded."""
        # print(f" -- reading {max_read_count} bytes from reader")

        # Should never happen, because this can cause problems.
        if max_read_count == 0:
            return b''

        # Loop through the retries for the read from buffer if its empty.
        while True:
            if max_read_count < 0:
                read_count = len(self.__buffer)
            else:
                read_count = min(max_read_count, len(self.__buffer))

            # print(f" -- -- computed read count: {read_count}")

            if read_count == 0:
                # No data left to process
                if self.__eof:
                    return b''
                # Now there's data we're waiting on, which hasn't reached us yet.
                assert self.__waiter is None
                self.__waiter = self.__loop.create_future()
                # print(" -- -- waiting on data to come in.")
                try:
                    await self.__waiter
                finally:
                    self.__waiter = None
                # Try again...
                # print(" -- -- trying read again")
                continue

            ret = self.__buffer[:read_count]
            del self.__buffer[:read_count]
            # print(f" -- -- {len(self.__buffer)} bytes left in reader (read {ret})")
            if not self.__buffer:
                # print(f" -- -- notifying pumper")
                async with self.__condition:
                    self.__condition.notify_all()
            return ret
