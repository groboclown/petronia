"""Thread-safe event writer."""

# pylint:disable=line-too-long

from typing import Tuple, Callable, Union, Optional
import threading
import concurrent.futures
from ..util.error import StdRet
from .defs import RawBinaryReader, MarshalledEventObject
from .writer import BinaryWriter, write_binary_event_to_stream, write_object_event_to_stream


class ThreadSafeEventWriter:
    """Writes events in a thread-safe way."""
    __slots__ = ('_writer', '_lock',)

    def __init__(
            self, writer: BinaryWriter, lock: Union[None, threading.Lock, threading.RLock] = None,
    ) -> None:
        self._writer = writer
        self._lock = lock or threading.Lock()

    def write_binary_event(
            self,
            event_id: str,
            source_id: str,
            target_id: str,
            binary_blob_size: int,
            binary_blob: Union[bytes, RawBinaryReader],
    ) -> StdRet[None]:
        """Write a binary event."""
        with self._lock:
            return write_binary_event_to_stream(
                self._writer, event_id, source_id, target_id,
                binary_blob_size, binary_blob,
            )

    def write_object_event(
            self,
            event_id: str,
            source_id: str,
            target_id: str,
            event_object: MarshalledEventObject,
    ) -> StdRet[None]:
        """Write an object event."""
        with self._lock:
            return write_object_event_to_stream(
                self._writer, event_id, source_id, target_id,
                event_object,
            )


class AsyncThreadSafeEventWriter(ThreadSafeEventWriter):
    """Writes events in a thread safe way, and
    adds the ability to write events in the background."""
    __slots__ = ('__executor',)

    def __init__(
            self,
            writer: BinaryWriter,
            executor: Optional[concurrent.futures.ThreadPoolExecutor] = None,
            lock: Union[None, threading.Lock, threading.RLock] = None,
    ) -> None:
        ThreadSafeEventWriter.__init__(self, writer, lock)
        self.__executor = executor or concurrent.futures.ThreadPoolExecutor()

    def async_write_object_event(
            self,
            event_id,
            source_id,
            target_id,
            event_object,
    ):
        # type: (str, str, str, MarshalledEventObject) -> concurrent.futures.Future[StdRet[None]]
        """Writes the event in a future action."""
        return self.__executor.submit(
            self.write_object_event,
            event_id, source_id, target_id, event_object,
        )

    def async_write_simple_binary_event(
            self,
            event_id,
            source_id,
            target_id,
            binary_blob,
    ):
        # type: (str, str, str, bytes) -> concurrent.futures.Future[StdRet[None]]
        """Write bytes as a binary event in a future action."""
        return self.__executor.submit(
            self.write_binary_event,
            event_id, source_id, target_id,
            len(binary_blob), binary_blob,
        )

    def async_write_binary_event(
            self,
            event_id,
            source_id,
            target_id,
            future_data_reader,
    ):
        # type: (str, str, str, Callable[[], Tuple[int, RawBinaryReader]]) -> concurrent.futures.Future[StdRet[None]]
        """Write a binary event in a future action.  The reading of the data
        will start in the future action as well.  The future_data_reader is called within
        the lock."""

        def callback() -> StdRet[None]:
            # This isn't a simple pass-through in the executor, because of the locking
            # requirement around creating the reader.
            with self._lock:
                binary_blob_size, binary_blob = future_data_reader()
                return write_binary_event_to_stream(
                    self._writer, event_id, source_id, target_id,
                    binary_blob_size, binary_blob,
                )

        return self.__executor.submit(callback)
