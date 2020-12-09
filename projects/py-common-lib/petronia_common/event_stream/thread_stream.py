
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
from ..util.input_buffer import StreamedBinaryReader


class ThreadedStreamForwarder:
    """Threaded version of a stream forwarder."""
    __slots__ = ('_executor',)

    def __init__(self, executor: Optional[ThreadPoolExecutor] = None) -> None:
        if executor is None:
            self._executor = ThreadPoolExecutor(4)
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
        from this one."""

        streams: List[StreamedBinaryReader] = []
        processes = []  # type: List[Future[bool]]
        to_remove: List[EventForwarderTarget] = []
        data_read_condition = threading.Condition()

        def all_consumed() -> bool:
            # print(f" -- {self} checking if {len(streams)} streams' data consumed")
            for stream in streams:
                if not stream.is_buffer_consumed():
                    # print(f" -- (TSF {self._iid}) stream has yet to consume all data: {stream}")
                    return False
            # print(f" -- (TSF {self._iid}) {len(streams)} streams consumed all buffer data")
            return True

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
            stm = StreamedBinaryReader(data_read_condition)
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
                # print(f" (TSF {self._iid}) Reading {read_size} bytes from reader.")
                data = reader(read_size)
                for stream in streams:
                    if not data:
                        # print(f" (TSF {self._iid})!! sending EOF to stream")
                        stream.feed_eof()
                        running = False
                    else:
                        # print(f" (TSF {self._iid})!! sending {len(data)} bytes of data to stream")
                        stream.feed_data(data)

                # Wait for the forwarding to be consumed...
                with data_read_condition:
                    # print(f" (TSF {self._iid}) Waiting on {data_read_condition} data to be read...")
                    data_read_condition.wait_for(all_consumed)
                    # print(f" (TSF {self._iid}) {data_read_condition} all sent data read")
            stream_future.set_result(True)
            # print(f" (TSF {self._iid}) completed stream forwarding process {stream_future}")

        # print(f" (TSF {self._iid}) submitting forward stream for processing")
        self._executor.submit(forward_stream)
        processes.append(stream_future)
        for process in processes:
            # print(f" (TSF {self._iid}) waiting for process {process} to complete")
            process.result()
        # print(f" (TSF {self._iid}) forward stream for processing completed")
        return to_remove
