"""Thread-safe event writer."""

from typing import Union
import threading
from ..util.error import StdRet
from .defs import RawBinaryReader, MarshalledEventObject
from .writer import BinaryWriter, write_binary_event_to_stream, write_object_event_to_stream


class ThreadSafeEventWriter:
    """Writes events in a thread-safe way."""
    __slots__ = ('__writer', '__lock',)

    def __init__(
            self, writer: BinaryWriter, lock: Union[None, threading.Lock, threading.RLock] = None,
    ) -> None:
        self.__writer = writer
        self.__lock = lock or threading.Lock()

    def write_binary_event(
            self,
            event_id: str,
            source_id: str,
            target_id: str,
            binary_blob_size: int,
            binary_blob: Union[bytes, RawBinaryReader],
    ) -> StdRet[None]:
        """Write a binary event."""
        with self.__lock:
            return write_binary_event_to_stream(
                self.__writer, event_id, source_id, target_id,
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
        with self.__lock:
            return write_object_event_to_stream(
                self.__writer, event_id, source_id, target_id,
                event_object,
            )
