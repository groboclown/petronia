"""
A select-like worker thread that pulls from
"""

from typing import Iterable, Dict, Callable, Union, Optional
import os
import threading
import select
from ..event_stream.reader import BinaryReader


class StreamedBinaryReader:
    """Pushes data to a stream, and notifies a condition when the buffer is read.
    The buffer has no maximum size.  When data is read from the buffer, the
    condition is notified."""
    __slots__ = (
        '__condition', '__buffer', '__eof', '__waiter', '__lock', '__eof_read',
        '__buffer_empty',
    )

    def __init__(
            self,
            condition: Optional[threading.Condition] = None,
    ) -> None:
        self.__lock = threading.RLock()
        self.__condition = condition
        self.__waiter = threading.Condition(self.__lock)
        self.__buffer = bytearray()
        self.__eof = False
        self.__eof_read = False
        self.__buffer_empty = True

    def is_buffer_consumed(self) -> bool:
        """Is there no more data to read in this buffer?  This is done outside the lock."""
        # Because this is done outside the lock, we must be careful with which variable is
        # used.  Due to cross-thread issues, this cannot obtain the lock.  So, using a
        # value that does not have an internal check performed.
        return self.__buffer_empty

    def is_stream_consumed(self) -> bool:
        """Has an EOF been fed to the buffer, and has it been read?"""
        with self.__lock:
            return self.__eof_read

    def buffer_size(self) -> int:
        """Get the size of the buffer."""
        with self.__lock:
            return len(self.__buffer)

    def feed_data(self, buff: bytes) -> None:
        """Feed data to the stream."""
        if len(buff) > 0:
            with self.__lock:
                if self.__eof:
                    raise ValueError('already at EOF')
                self.__buffer_empty = False
                # print(f" -- (SBR {self._iid}) pumping {len(buff)} bytes of data ({buff})")
                self.__buffer += buff
                # print(f" -- (SBR {self._iid}) -- {len(self.__buffer)} bytes left to read (+
                # {len(buff)} bytes)")
                self.__waiter.notify_all()

    def feed_eof(self) -> None:
        """Feed an EOF to the stream."""
        # print(f" -- (SBR {self._iid}) told EOF to reader")
        with self.__lock:
            self.__eof = True
            self.__waiter.notify_all()

    def __call__(self, max_read_count: int = -1) -> bytes:
        return self.read_data(max_read_count)

    def read(self, max_read_size: int = -1) -> bytes:
        """Standard API for binary reader objects; BinaryReader protocol."""
        return self.read_data(max_read_size)

    def read_data(self, max_read_count: int) -> bytes:
        """Read data from the buffer, or wait for it to be loaded."""
        # print(f" {self} reading - {max_read_count} bytes from reader")

        # Should never happen, because this can cause problems.
        if max_read_count == 0:
            if self.__condition:
                # print(f" {self} reading -- notifying pumper {self.__condition}")
                with self.__condition:
                    self.__condition.notify_all()
            return b''

        # Loop through the retries for the read from buffer if its empty.
        while True:
            # print(f" {self} reading - grabbing lock")
            with self.__lock:
                if max_read_count < 0:
                    read_count = len(self.__buffer)
                else:
                    read_count = min(max_read_count, len(self.__buffer))

                # print(f" {self} reading -- computed read count: {read_count}")

                if read_count == 0:
                    # No data left to process.
                    if self.__eof:
                        # Always send the notify on EOF read.
                        self.__eof_read = True
                        if self.__condition:
                            # print(f" {self} reading -- notifying pumper {self.__condition}")
                            with self.__condition:
                                self.__condition.notify_all()
                        # print(f" {self} reading -- returning emtpy and releasing lock")
                        return b''

                    # There's data we're waiting on, which hasn't reached us yet.
                    # print(f" {self} reading -- waiting on data to come in.")
                    self.__waiter.wait_for(lambda: len(self.__buffer) > 0 or self.__eof)
                    # Try again...
                    # print(f" {self} reading -- trying read again and releasing lock")
                    continue

                ret = self.__buffer[:read_count]
                del self.__buffer[:read_count]
                # print(f" {self} reading -- {len(self.__buffer)} bytes left in reader
                # (read {ret})")
                if len(self.__buffer) <= 0:
                    self.__buffer_empty = True
                    if self.__eof:
                        # print(f" {self} reading -- completed read up to the EOF")
                        self.__eof_read = True
                if self.__condition:
                    # print(f" {self} reading -- notifying pumper {self.__condition}")
                    with self.__condition:
                        self.__condition.notify_all()
                # print(f" {self} reading - returning and releasing lock")
                return bytes(ret)


class StreamReadState:
    """Common state used by thread reader objects.  The underlying concept
    is to have a global, daemon thread that handles all FDs of a specific
    category."""
    __slots__ = ('__lock', '__fd_streams', '__active', '__on_err', '__condition')

    def __init__(self, on_err: Callable[[Exception], None]) -> None:
        self.__fd_streams: Dict[int, StreamedBinaryReader] = {}
        self.__lock = threading.Lock()
        self.__condition = threading.Condition(self.__lock)
        self.__active = True
        self.__on_err = on_err

    def is_active(self) -> bool:
        """Is this reader active?"""
        return self.__active

    def stop(self) -> None:
        """Stop the reader."""
        with self.__lock:
            self.__active = False
            self.__condition.notify_all()

    def add_fd(
            self, desc: int, condition: Optional[threading.Condition] = None,
    ) -> StreamedBinaryReader:
        """Add an fd + its buffered stream."""
        ret = StreamedBinaryReader(condition)
        with self.__lock:
            assert desc not in self.__fd_streams, f'Already registered fd {desc}'
            self.__fd_streams[desc] = ret
            self.__condition.notify_all()
        return ret

    def on_error(self, err: Exception) -> None:
        """Call the registered callback."""
        self.__on_err(err)

    def close_fd(self, desc: int) -> None:
        """Close off a fd.  Sends the EOF to the reader."""
        with self.__lock:
            if desc not in self.__fd_streams:
                # No-op if not registered.
                return
            self.__fd_streams[desc].feed_eof()
            del self.__fd_streams[desc]

    def get_stream(self, desc: int) -> Optional[StreamedBinaryReader]:
        """Get the stream for the file descriptor."""
        with self.__lock:
            return self.__fd_streams.get(desc)

    def get_fds(self) -> Iterable[int]:
        """Get all registered fds."""
        with self.__lock:
            return tuple(self.__fd_streams.keys())

    def _wait_for_fd(self) -> None:
        """Waits for FDs to be present, or the loop to end."""
        with self.__lock:
            self.__condition.wait_for(lambda: len(self.__fd_streams) > 0 or not self.__active)

    def start_read_loop_thread(
            self,
            read_ready_fds: Callable[[Iterable[int]], Dict[int, Union[bytes, Exception]]],
            loop_notice: Optional[threading.Condition] = None,
    ) -> threading.Thread:
        """Start the read loop in a thread."""
        assert self.is_active(), 'Not currently active'
        ret = threading.Thread(
            target=self.read_loop,
            args=(read_ready_fds, loop_notice,),
            daemon=True,
        )
        ret.start()
        return ret

    def read_loop(
            self,
            read_ready_fds: Callable[[Iterable[int]], Dict[int, Union[bytes, Exception]]],
            loop_notice: Optional[threading.Condition],
    ) -> None:
        """Run the loop to wait for FDs to be ready for read.
        The read_ready_fds callback takes in the list of FDs that are
        registered, and reads available data from those that have data
        available (should be non-blocking), and returns a dictionary
        of FD -> read data for those FDs that were read from; if the
        bytes value is empty, then it signals that the FD is closed.

        The loop_notice is mostly used as a debugging hook to tell
        the callers when the loop runs.
        """
        while self.is_active():   # pylint: disable=too-many-nested-blocks
            if loop_notice:
                with loop_notice:
                    loop_notice.notify_all()
            self._wait_for_fd()
            fds = self.get_fds()
            if not fds or not self.is_active():
                # This is another code-coverage situation where the continue line
                # is skipped on Windows Python.  Add in the print statement, and
                # it's magically covered.
                # print("Loop again; no fds found or not active.")
                continue
            try:
                read_data = read_ready_fds(fds)
            except InterruptedError:
                # This is acceptable for built-in read ready calls.
                continue
            except Exception as err:  # pylint: disable=broad-except
                self.on_error(err)
                continue

            for f_d, data in read_data.items():
                if isinstance(data, Exception):
                    self.on_error(data)
                else:
                    stream = self.get_stream(f_d)
                    if not stream:  # pragma no cover
                        # edge case that is really hard to test for.
                        continue  # pragma no cover
                    if data == b'':
                        stream.feed_eof()
                        self.close_fd(f_d)
                    else:
                        stream.feed_data(data)


def select_reader(
        fd_list: Iterable[int], timeout: int = 1, read_buffer_size: int = 1,
) -> Dict[int, Union[bytes, Exception]]:
    """Use the select operation to read in data from the file descriptors;
    for use with the `StreamReadState.read_loop`.

    See the documentation on the select.select function.  Windows will
    only work with network sockets.
    """
    readable, _, exceptional = select.select(
        fd_list, [], fd_list,
        timeout,
    )
    ret: Dict[int, Union[bytes, Exception]] = {}
    for ready_fds in (readable, exceptional):
        for f_d in ready_fds:
            try:
                data = os.read(f_d, read_buffer_size)
                ret[f_d] = data
            except EOFError:
                ret[f_d] = b''
            except Exception as err:  # pylint: disable=broad-except
                ret[f_d] = err
    return ret


def single_reader_loop(
        inp: BinaryReader, stream: StreamedBinaryReader,
        eof_on_empty_read: bool = True,
        buffer_read_size: int = 1,
        on_err: Optional[Callable[[Exception], None]] = None,
) -> None:
    """Runs in a loop reading from a single input I/O and pumps it into the
    stream.  Runs until EOF is encountered.  On an exception, the on_err callback
    is called, EOF is sent to the stream, and the read loop stops."""
    # debug_bytes_read = 0
    while True:
        try:
            # print(f"loop reader: reading {buffer_read_size} bytes from {inp.fileno()}
            # (so far: {debug_bytes_read})")
            data = inp.read(buffer_read_size)
            # debug_bytes_read += len(data)
            # print(f"loop reader:  read {repr(data)} from {inp.fileno()} (total:
            # {debug_bytes_read})")
            if data:
                stream.feed_data(data)
            elif eof_on_empty_read:
                stream.feed_eof()
                return
        except EOFError:
            stream.feed_eof()
            return
        except Exception as err:  # pylint: disable=broad-except
            if on_err:
                on_err(err)
            stream.feed_eof()
            return
