"""
Shard data stream used by the in-memory launchers.
"""

import threading


class ReadWriteStream:
    """A stream that allows read + write without the copy overhead.
    This is thread-safe.  Performing a read will lock the thread if you
    request < 0 max_read_size and the buffer is empty and the stream is
    open.

    This matches the prototypes (BinaryReader, BinaryWriter)
    """
    __slots__ = ('_buf', '_cond', '_open')

    def __init__(self) -> None:
        self._buf = bytearray()
        self._open = True
        self._cond = threading.Condition()

    def is_open(self) -> bool:
        """Is this stream still open for write?"""
        return self._open

    def close(self) -> None:
        """Close the stream for writing."""
        with self._cond:
            self._open = False
            self._cond.notify_all()

    def read(self, max_read_size: int = -1) -> bytes:
        """Continue to feed data until closed."""
        with self._cond:
            if len(self._buf) <= 0:
                while self.is_open() and len(self._buf) <= 0:
                    self._cond.wait(1.0)
                if not self.is_open():
                    return b''
            if max_read_size < 0 or max_read_size >= len(self._buf):
                max_read_size = len(self._buf)
            assert max_read_size > 0
            ret = self._buf[:max_read_size]
            self._buf = self._buf[max_read_size:]
        return ret

    def write(self, data: bytes) -> None:
        """Write data to the stream, if it's still open.."""
        with self._cond:
            if not self.is_open():
                raise OSError('stream is closed')
            self._buf.extend(data)
            self._cond.notify_all()
