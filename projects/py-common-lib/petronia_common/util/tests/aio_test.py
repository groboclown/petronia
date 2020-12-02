
"""Test the aio module."""

from typing import Optional
import unittest
import unittest.mock
import os
import asyncio
import tempfile
import shutil
from .. import aio


class AioTest(unittest.TestCase):
    """Test the aio functions."""

    def setUp(self) -> None:
        read_fd, write_fd = os.pipe()
        self.read_fd = read_fd
        self.write_fd = write_fd
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        for file_desc in (self.read_fd, self.write_fd):
            try:
                os.close(file_desc)
            except OSError:  # pragma no cover
                pass  # pragma no cover
        shutil.rmtree(self.tempdir)

    def test_aio_fd_reader__simple_default(self) -> None:
        """Simple read data."""

        async def test_run() -> None:
            # Ooh-ooh, stream reader, I believe you can get me through the bytes.
            read_stream = asyncio.StreamReader()
            os.write(self.write_fd, b'abc-123')

            # Close is really important.
            os.close(self.write_fd)

            await aio.aio_fd_reader(
                self.read_fd, read_stream, -1, None,
            )

            data = b''
            while not read_stream.at_eof():
                data += await read_stream.read(-1)
            self.assertTrue(read_stream.at_eof())
            self.assertEqual(b'abc-123', data)

        asyncio.run(test_run(), debug=True)

    def test_aio_fd_reader__async(self) -> None:
        """Simple read data."""

        async def run_writer() -> None:
            await asyncio.sleep(.2)
            os.write(self.write_fd, b'abc-123')
            await asyncio.sleep(.2)
            os.close(self.write_fd)

        async def run_reader(read_stream: asyncio.StreamReader) -> None:
            await aio.aio_fd_reader(
                self.read_fd, read_stream, 2, None,
            )

        async def run_pull(read_stream: asyncio.StreamReader) -> None:
            data = b''
            while not read_stream.at_eof():
                data += await read_stream.read(-1)
            self.assertTrue(read_stream.at_eof())
            self.assertEqual(b'abc-123', data)

        async def run_test() -> None:
            read_stream = asyncio.StreamReader()
            await asyncio.gather(run_writer(), run_reader(read_stream), run_pull(read_stream))

        asyncio.run(run_test(), debug=True)

    def test_aio_fd_reader__custom_loop__buffer_reads(self) -> None:
        """Simple read data."""

        async def test_run() -> None:
            expected = b'x' * 300
            loop = asyncio.get_running_loop()
            read_stream = asyncio.StreamReader(loop=loop)
            os.write(self.write_fd, expected)

            # Close is really important.
            os.close(self.write_fd)

            await aio.aio_fd_reader(
                self.read_fd, read_stream, 100, loop,
            )

            data = b''
            read_count = 0
            while not read_stream.at_eof():
                read_count += 1
                data += await read_stream.read(-1)
            self.assertTrue(read_stream.at_eof())
            self.assertEqual(expected, data)
            self.assertEqual(1, read_count)

        asyncio.run(test_run(), debug=True)

    def test_aio_fd_reader__bad_fd(self) -> None:
        """Simple read data."""

        async def test_run() -> None:
            read_stream = asyncio.StreamReader()

            await aio.aio_fd_reader(-1, read_stream, 10)
            # This should raise an OS error, but due to the way OSes closing + reading
            # works, this should correctly trap the OS error.
            res = await read_stream.read(-1)
            self.assertEqual(b'', res)

        asyncio.run(test_run(), debug=True)

    def test_aio_fd_reader__cant_read(self) -> None:
        """Simple read data."""

        async def test_run() -> None:
            mock = unittest.mock.Mock(side_effect=OSError('generated err'))
            with unittest.mock.patch('petronia_common.util.aio.os.read', mock):
                read_stream = asyncio.StreamReader()
                await aio.aio_fd_reader(1, read_stream, 10)
                try:
                    await read_stream.read(-1)
                    self.fail("Did not raise an exception")  # pragma no cover
                except OSError as err:
                    self.assertEqual(('generated err',), err.args)

        asyncio.run(test_run(), debug=True)

    def test_aio_reader__oserr(self) -> None:
        """Simple read data."""

        def read_func() -> Optional[bytes]:
            raise OSError('generated err')

        async def test_run() -> None:
            # Ooh, stream reader, I believe you can get me through the bytes.
            read_stream = asyncio.StreamReader()

            await aio.aio_reader(read_stream, read_func)
            try:
                await read_stream.read(-1)
                self.fail("Did not raise an exception")  # pragma no cover
            except OSError as err:
                self.assertEqual(('generated err',), err.args)

        asyncio.run(test_run(), debug=True)

    def test_aio_reader__eof_error(self) -> None:
        """Test aio_reader with a callback that generates an EOFError."""

        reader_calls = [0]
        data_read = bytearray()

        def my_reader() -> bytes:
            reader_calls[0] += 1
            if reader_calls[0] >= 3:
                raise EOFError('my_reader')
            return b'1'

        async def read_from_stream(stream: asyncio.StreamReader) -> None:
            for _ in range(100):
                data = await stream.read(-1)
                if not data:
                    return
                data_read.extend(data)
            self.fail('attempted read over 100 times.')  # pragma no cover

        async def test_run() -> None:
            read_stream = asyncio.StreamReader()
            self.assertEqual(0, reader_calls[0])
            await asyncio.gather(
                aio.aio_reader(read_stream, my_reader),
                read_from_stream(read_stream),
            )
            self.assertEqual(3, reader_calls[0])
            self.assertEqual(
                b'11',
                bytes(data_read),
            )

        asyncio.run(test_run(), debug=True)
