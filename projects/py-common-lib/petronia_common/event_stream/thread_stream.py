
"""
A streaming reader that forks the read to many streams.
"""

from typing import List, Optional
import threading
from concurrent.futures import Future, ThreadPoolExecutor
from .defs import (
    RawBinaryReader,
    to_raw_event_binary,
)
from .forwarder import EventForwarderTarget


class ThreadedStreamForwarder:
    """Threaded version of a stream forwarder."""
    __slots__ = ('_executor',)

    def __init__(self, executor: Optional[ThreadPoolExecutor] = None) -> None:
        if executor is None:
            self._executor = ThreadPoolExecutor()
        else:
            self._executor = executor

    def __call__(  # pylint: disable=too-many-arguments,too-many-locals
            self,
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
        data is fully processed.

        Each reader is running in its own background thread, separate
        from this one.."""

        streams: List[StreamedBinaryReader] = []
        processes = []  # type: List[Future[bool]]
        to_remove: List[EventForwarderTarget] = []
        data_read_condition = threading.Condition()

        def can_read_next() -> bool:
            ret = True
            for stream in streams:
                ret = ret and stream.is_buffer_consumed()
            # print(f" -- Remaining stream data to read: {ret}")
            return ret

        def mk_handle_target(
                target: EventForwarderTarget,
                stream: StreamedBinaryReader,
        ) -> Future:
            ret = Future()  # type: Future[bool]

            def handle_target() -> None:
                res = target.consume(
                    to_raw_event_binary(event_id, source_id, target_id, blob_size, stream),
                )
                if res:
                    to_remove.append(target)
                ret.set_result(True)

            self._executor.submit(handle_target)
            return ret

        for tgt in targets:
            stm = StreamedBinaryReader(self._executor, data_read_condition)
            streams.append(stm)
            # Note: no await here.
            processes.append(mk_handle_target(tgt, stm))
        if not streams:
            # drain the reader
            while reader(read_size) != b'':
                pass
            return to_remove

        stream_future = Future()  # type: Future[bool]

        def forward_stream() -> None:
            running = True
            while running:
                # Process some data...
                data = reader(read_size)
                for stream in streams:
                    if not data:
                        # print(" !! sending EOF to stream")
                        stream.feed_eof()
                        running = False
                    else:
                        # print(f" !! sending {len(data)} bytes of data to stream")
                        stream.feed_data(data)

                # Wait for the forwarding to be consumed...
                with data_read_condition:
                    # print("Waiting on data to be read...")
                    if not can_read_next():
                        data_read_condition.wait_for(can_read_next)
            stream_future.set_result(True)

        self._executor.submit(forward_stream)
        processes.append(stream_future)
        for process in processes:
            process.result()
        return to_remove


class StreamedBinaryReader:
    """Pushes data to a stream, and notifies a condition when the buffer is read."""
    __slots__ = ('__condition', '__buffer', '__eof', '__waiter', '__executor',)

    def __init__(
            self,
            executor: ThreadPoolExecutor,
            condition: threading.Condition,
    ) -> None:
        self.__condition = condition
        self.__waiter = None  # type: Optional[Future[int]]
        self.__executor = executor
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

    def __call__(self, max_read_count: int = -1) -> bytes:
        return self.read_data(max_read_count)

    def read_data(self, max_read_count: int) -> bytes:
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
                self.__waiter = Future()
                # print(" -- -- waiting on data to come in.")
                try:
                    self.__waiter.result()
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
                with self.__condition:
                    self.__condition.notify_all()
            return ret
