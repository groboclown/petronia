"""Test the module."""

from typing import List, Iterable, Dict, Union
import unittest
import threading
import io
from .. import input_buffer


class StreamedBinaryReaderTest(unittest.TestCase):
    """Test the StreamedBinaryReader class."""

    def test_no_wait_read_integration(self) -> None:
        """Test reading from the stream when there is no waiting required."""
        reader = input_buffer.StreamedBinaryReader()

        # Empty initial state checks.
        self.assertTrue(reader.is_buffer_consumed())
        self.assertFalse(reader.is_stream_consumed())
        self.assertEqual(0, reader.buffer_size())

        # Feed in some data.
        reader.feed_data(b'1234')

        # With data checks.
        self.assertEqual(4, reader.buffer_size())
        self.assertFalse(reader.is_buffer_consumed())
        self.assertFalse(reader.is_stream_consumed())

        # Read exactly the buffer size.
        data = reader.read(4)

        # With data checks.
        self.assertEqual(b'1234', data)
        self.assertTrue(reader.is_buffer_consumed())
        self.assertFalse(reader.is_stream_consumed())
        self.assertEqual(0, reader.buffer_size())

        # Feed in more data.

        # Feed in some data.
        reader.feed_data(b'123456')

        # With data checks.
        self.assertEqual(6, reader.buffer_size())
        self.assertFalse(reader.is_buffer_consumed())
        self.assertFalse(reader.is_stream_consumed())

        # Read some of the buffer size.
        data = reader(2)

        # With data checks.
        self.assertEqual(b'12', data)
        self.assertFalse(reader.is_buffer_consumed())
        self.assertFalse(reader.is_stream_consumed())
        self.assertEqual(4, reader.buffer_size())

        # Send an EOF while there's data in the buffer.
        reader.feed_eof()
        self.assertFalse(reader.is_buffer_consumed())
        self.assertFalse(reader.is_stream_consumed())
        self.assertEqual(4, reader.buffer_size())

        # Read in all remaining data.
        data = reader.read_data(-1)
        self.assertEqual(b'3456', data)
        self.assertTrue(reader.is_buffer_consumed())
        self.assertTrue(reader.is_stream_consumed())
        self.assertEqual(0, reader.buffer_size())

    def test_feed_data_on_eof(self) -> None:
        """Send an EOF then send data."""
        reader = input_buffer.StreamedBinaryReader()
        reader.feed_eof()
        try:
            reader.feed_data(b'1')
            self.fail('did not raise value error')  # pragma no cover
        except ValueError as err:
            self.assertEqual('already at EOF', str(err))

    def test_read_data_on_eof(self) -> None:
        """Send an EOF then read data."""
        reader = input_buffer.StreamedBinaryReader()
        self.assertTrue(reader.is_buffer_consumed())
        self.assertFalse(reader.is_stream_consumed())

        reader.feed_eof()
        self.assertTrue(reader.is_buffer_consumed())
        self.assertFalse(reader.is_stream_consumed())
        self.assertEqual(0, reader.buffer_size())

        data = reader.read()
        self.assertEqual(b'', data)
        self.assertTrue(reader.is_buffer_consumed())
        self.assertTrue(reader.is_stream_consumed())
        self.assertEqual(0, reader.buffer_size())

    def test_feed_no_data(self) -> None:
        """Send an EOF then read data."""
        reader = input_buffer.StreamedBinaryReader()
        self.assertTrue(reader.is_buffer_consumed())
        self.assertFalse(reader.is_stream_consumed())

        reader.feed_data(b'')
        self.assertTrue(reader.is_buffer_consumed())
        self.assertFalse(reader.is_stream_consumed())
        self.assertEqual(0, reader.buffer_size())

    def test_read_zero_size(self) -> None:
        """Send an EOF then read data."""
        reader = input_buffer.StreamedBinaryReader()
        reader.feed_data(b'1')
        data = reader.read_data(0)
        self.assertEqual(b'', data)
        self.assertFalse(reader.is_buffer_consumed())
        self.assertFalse(reader.is_stream_consumed())
        self.assertEqual(1, reader.buffer_size())

    def test_thread_read(self) -> None:
        """Test reading and writing between threads."""
        state = [0]
        con_state = threading.Condition()
        reader = input_buffer.StreamedBinaryReader()

        # Note: all assertions happen after all condition stuff.
        data: List[bytes] = []

        def writer_thread() -> None:
            try:
                with con_state:
                    # print("writer thread: waiting for state 2")
                    con_state.wait_for(lambda: state[0] >= 2)
                    reader.feed_data(b'12345')
                    state[0] = 3
                    con_state.notify_all()
                    con_state.wait_for(lambda: state[0] >= 4)
                    reader.feed_eof()
            except:  # pragma no cover
                state[0] += 1000  # pragma no cover
                raise  # pragma no cover

        def reader_thread() -> None:
            try:
                with con_state:
                    # print("reader thread: waiting for state 1")
                    con_state.wait_for(lambda: state[0] >= 1)
                    state[0] = 2
                    con_state.notify_all()
                    # print("reader thread: set state 2; starting read")
                    # release the lock

                data.append(reader.read_data(5))
                # print("reader thread: read first batch of data; reading next batch of data")
                with con_state:
                    state[0] = 4
                    con_state.notify_all()
                    # print("reader thread: read data; setting state 4")
                data.append(reader.read_data(-1))
                with con_state:
                    state[0] = 5
                    con_state.notify_all()
                    # print("reader thread: read data; setting state 4")
            except:  # pragma no cover
                state[0] += 7000  # pragma no cover
                raise  # pragma no cover

        th1 = threading.Thread(target=writer_thread, daemon=True)
        th2 = threading.Thread(target=reader_thread, daemon=True)
        th1.start()
        th2.start()
        state[0] = 1
        with con_state:
            con_state.notify_all()
        th1.join(5)
        th2.join(5)
        self.assertFalse(th1.is_alive())
        self.assertFalse(th2.is_alive())
        self.assertEqual(5, state[0])
        self.assertEqual(
            [b'12345', b''],
            data,
        )


class StreamReadStateTest(unittest.TestCase):
    """Test the StreamReadState class"""

    def test_getters_callbacks(self) -> None:
        """Test calling the callbacks."""
        err_cb = OnErrorCallbackSpy()
        srs = input_buffer.StreamReadState(err_cb.on_err_cb)

        self.assertTrue(srs.is_active())
        err = OSError('this is my error')
        srs.on_error(err)
        self.assertEqual([err], err_cb.errs)

    def test_empty_stuff(self) -> None:
        """Test methods when no fds are registered."""
        err_cb = OnErrorCallbackSpy()
        srs = input_buffer.StreamReadState(err_cb.on_err_cb)

        self.assertTrue(srs.is_active())
        self.assertEqual(tuple(), srs.get_fds())
        self.assertIsNone(srs.get_stream(11))
        srs.close_fd(11)
        self.assertTrue(srs.is_active())

        def read_ready_cb(_fds: Iterable[int]) -> Dict[int, Union[bytes, Exception]]:
            raise Exception('should not be called')  # pragma no cover

        con = threading.Condition()
        # Wait for the thread to start running...
        # So we put this in the lock with the condition so we guarantee that we
        # are notified
        with con:
            loop_thread = srs.start_read_loop_thread(read_ready_cb, con)
            started_loop = con.wait(5)
        self.assertTrue(started_loop)
        self.assertTrue(loop_thread.is_alive())
        # At this point, the thread is waiting for fds or stop.
        self.assertTrue(srs.is_active())
        srs.stop()
        self.assertFalse(srs.is_active())
        loop_thread.join(5)
        self.assertFalse(loop_thread.is_alive())
        self.assertEqual([], err_cb.errs)

    def test_fd_read_loop_ok(self) -> None:
        """Test the run loop in a threaded environment when there are fds registered."""
        err_cb = OnErrorCallbackSpy()
        srs = input_buffer.StreamReadState(err_cb.on_err_cb)
        read_con = threading.Condition()
        stream_reader = srs.add_fd(10, read_con)

        self.assertTrue(srs.is_active())
        self.assertEqual((10,), srs.get_fds())
        self.assertIsNone(srs.get_stream(11))
        self.assertIs(stream_reader, srs.get_stream(10))
        self.assertTrue(srs.is_active())

        read_state = [0, 1]
        fds_called: List[List[int]] = []
        encountered_exception = OSError('foo')
        fds_response: List[Union[bytes, Exception]] = [
            b'abc', b'123', encountered_exception, b'a1', b'',
        ]

        def read_ready_cb(fds: Iterable[int]) -> Dict[int, Union[bytes, Exception]]:
            fds_called.append(list(fds))
            with read_con:
                read_con.wait_for(lambda: read_state[0] == read_state[1])
                read_state[0] += 1
                read_con.notify_all()
            # Prevent bad errors:
            if not fds_response:
                return {}  # pragma no cover
            return {10: fds_response.pop(0)}

        loop_thread = srs.start_read_loop_thread(read_ready_cb)

        # Let the loop call into the callback.
        while fds_response:
            # interact with the read_ready_cb function.
            with read_con:
                # Tell the read to start.
                read_state[0] = 1
                read_state[1] = 1
                read_con.notify_all()
                got_it = read_con.wait_for(lambda: read_state[0] == 2, 5)
                self.assertTrue(got_it)

        # Should be no more fds but still alive.
        self.assertTrue(srs.is_active())
        self.assertEqual((), srs.get_fds())

        # Should have encountered the error
        self.assertEqual([encountered_exception], err_cb.errs)

        # Should have called into the reader correctly
        self.assertEqual([[10], [10], [10], [10], [10]], fds_called)

        # Should have read in the data correctly.
        self.assertEqual(
            b'abc123a1',
            stream_reader.read(),
        )

        # wait for the read to finish.
        # wait for the next pass
        srs.stop()
        self.assertFalse(srs.is_active())
        loop_thread.join(5)
        self.assertFalse(loop_thread.is_alive())

    def test_stop_in_fd_wait(self) -> None:
        """Test stopping the loop while waiting for an FD to be added."""
        err_cb = OnErrorCallbackSpy()
        srs = input_buffer.StreamReadState(err_cb.on_err_cb)
        self.assertEqual((), srs.get_fds())

        def read_ready_cb(_fds: Iterable[int]) -> Dict[int, Union[bytes, Exception]]:
            raise Exception('should not be called')  # pragma no cover

        con = threading.Condition()
        # Wait for the thread to start running...
        # So we put this in the lock with the condition so we guarantee that we
        # are notified
        with con:
            loop_thread = srs.start_read_loop_thread(read_ready_cb, con)
            started_loop = con.wait(5)
            self.assertTrue(started_loop)
            # The loop should have notified this loop, and now is waiting
            # for the lock or waiting for fds to be added.
            self.assertTrue(loop_thread.is_alive())
            # At this point, the thread is waiting for fds or stop.
            self.assertTrue(srs.is_active())
            srs.stop()
        loop_thread.join(5)
        self.assertFalse(loop_thread.is_alive())
        self.assertEqual([], err_cb.errs)

    def test_read_loop_interrupted(self) -> None:
        """Test the read loop where the fd read causes an interrupt."""
        err_cb = OnErrorCallbackSpy()
        srs = input_buffer.StreamReadState(err_cb.on_err_cb)
        read_con = threading.Condition()
        srs.add_fd(10, read_con)

        def read_ready_cb(_fds: Iterable[int]) -> Dict[int, Union[bytes, Exception]]:
            srs.stop()
            raise InterruptedError()

        loop_thread = srs.start_read_loop_thread(read_ready_cb)
        loop_thread.join(5)
        self.assertFalse(loop_thread.is_alive())
        # interrupted errors should be skipped.
        self.assertEqual([], err_cb.errs)

    def test_read_loop_error(self) -> None:
        """Test the read loop where the fd read causes an interrupt."""
        err_cb = OnErrorCallbackSpy()
        srs = input_buffer.StreamReadState(err_cb.on_err_cb)
        read_con = threading.Condition()
        srs.add_fd(10, read_con)
        expected_error = OSError('my error')

        def read_ready_cb(_fds: Iterable[int]) -> Dict[int, Union[bytes, Exception]]:
            srs.stop()
            raise expected_error

        loop_thread = srs.start_read_loop_thread(read_ready_cb)
        loop_thread.join(5)
        self.assertFalse(loop_thread.is_alive())
        # interrupted errors should be skipped.
        self.assertEqual([expected_error], err_cb.errs)


class ReaderFunctionTest(unittest.TestCase):
    """Test the module reader functions."""

    def test_single_reader_loop__std(self) -> None:
        """Standard usage pattern for the reader loop."""
        err_cb = OnErrorCallbackSpy()
        reader = io.BytesIO(b'1234')
        writer = input_buffer.StreamedBinaryReader()
        input_buffer.single_reader_loop(reader, writer, on_err=err_cb.on_err_cb)
        self.assertEqual(b'1234', writer.read())
        self.assertEqual([], err_cb.errs)

    def test_single_reader_loop__eof(self) -> None:
        """Use EOFError to indicate end of loop, not empty data."""
        err_cb = OnErrorCallbackSpy()
        orig_buffer = b'abcdefghijklmnopqrstuvwxyz'
        reader = EofReader(orig_buffer, 5, 2)
        writer = input_buffer.StreamedBinaryReader()
        input_buffer.single_reader_loop(
            reader, writer,
            eof_on_empty_read=False,
            on_err=err_cb.on_err_cb,
        )
        self.assertEqual(orig_buffer, writer.read())
        self.assertEqual([], err_cb.errs)

    def test_single_reader_loop__error(self) -> None:
        """Raises an error on read."""
        err_cb = OnErrorCallbackSpy()
        reader = ErrorReader(OSError('my err'))
        writer = input_buffer.StreamedBinaryReader()
        input_buffer.single_reader_loop(
            reader, writer,
            on_err=err_cb.on_err_cb,
        )
        self.assertEqual(b'', writer.read())
        self.assertEqual([reader.err], err_cb.errs)

    def test_single_reader_loop__error_no_callback(self) -> None:
        """Raises an error on read but with no error callback."""
        reader = ErrorReader(OSError('my err'))
        writer = input_buffer.StreamedBinaryReader()
        input_buffer.single_reader_loop(reader, writer)
        self.assertEqual(b'', writer.read())


class OnErrorCallbackSpy:
    """Common callback for on errors."""

    def __init__(self) -> None:
        self.errs: List[Exception] = []

    def on_err_cb(self, err: Exception) -> None:
        """on error callback"""
        self.errs.append(err)


class EofReader:
    """Reads to EOF, sends several blanks, then sends EOFError."""
    def __init__(self, data: bytes, max_read_count: int, empty_count: int) -> None:
        self.data = bytearray(data)
        self.max_read_count = max_read_count
        self.remaining_empty_count = empty_count

    def read(self, max_read_size: int = -1) -> bytes:
        """Run the read"""
        if len(self.data) <= 0 and max_read_size != 0:
            self.remaining_empty_count -= 1
            if self.remaining_empty_count <= 0:
                raise EOFError()
        if max_read_size < 0:
            # Shouldn't happen based calls above, but here just to be sure.
            max_read_size = self.max_read_count  # pragma no cover
        to_read = min(max_read_size, self.max_read_count, len(self.data))
        ret = self.data[:to_read]
        del self.data[:to_read]
        return bytes(ret)


class ErrorReader:
    """Reads to EOF, sends several blanks, then sends EOFError."""
    def __init__(self, err: Exception) -> None:
        self.err = err

    def read(self, max_read_size: int = -1) -> bytes:
        """Raise an error on read."""
        raise self.err
