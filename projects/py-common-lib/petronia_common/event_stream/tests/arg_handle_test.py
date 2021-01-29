
"""Test the arg_handle module."""

import unittest
import os
import platform
import tempfile
import shutil
from .. import arg_handle


class ArgHandleTest(unittest.TestCase):
    """Test the arg_handle functions."""

    def setUp(self) -> None:
        self.tempdir = tempfile.mkdtemp()
        self.valid_write_fd = 2  # sys.stderr.fileno()

        # OS specific stuff.
        if hasattr(os, 'O_BINARY'):
            self.o_binary = int(getattr(os, 'O_BINARY'))  # pragma no cover
        else:
            self.o_binary = 0  # pragma no cover
        if platform.system() == 'Windows':
            import _winapi  # pylint: disable=C0415,E0401  # pragma no cover
            read_handle, write_handle = _winapi.CreatePipe(None, 0)  # pragma no cover
            _winapi.CloseHandle(read_handle)  # pragma no cover
            self.valid_write_fd = write_handle  # pragma no cover

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir, ignore_errors=True)
        if platform.system() == 'Windows' and self.valid_write_fd:
            import _winapi  # pylint: disable=C0415,E0401  # pragma no cover
            _winapi.CloseHandle(self.valid_write_fd)  # pragma no cover

    def test_get_fd_from_argument__not_int(self) -> None:
        """Test where the argument is not an integer."""
        ret = arg_handle.get_fd_from_argument("x")
        self.assertTrue(ret.has_error)

    def test_get_fd_from_argument__neg(self) -> None:
        """Test where the argument is a negative integer."""
        ret = arg_handle.get_fd_from_argument("-100")
        self.assertTrue(ret.has_error)

    def test_get_fd_from_argument__int(self) -> None:
        """Test where argument is an integer.
        Special care must be taken for Windows environments."""
        ret = arg_handle.get_fd_from_argument(str(self.valid_write_fd))
        self.assertTrue(ret.ok)
        # Can't do a 1-for-1 check on the ret, because windows can return a different value.

    def test_get_fd_writer__close(self) -> None:
        """Test creating a writer from an fd.  Ensures calling close multiple
        times works."""
        test_file = os.path.join(self.tempdir, 'write-file.txt')
        file_descriptor = os.open(test_file, os.O_CREAT | os.O_WRONLY | self.o_binary)
        try:
            writer = arg_handle.get_fd_writer(file_descriptor)
            writer.write(b'test writing some data')
            writer.close()
            writer.close()
        finally:
            try:
                os.close(file_descriptor)
            except OSError:
                pass

        with open(test_file, 'rb') as fhl:
            self.assertEqual(b'test writing some data', fhl.read())

    def test_get_fd_writer__no_close(self) -> None:
        """Test creating a writer from an fd, without calling close on it."""
        test_file = os.path.join(self.tempdir, 'write-file.txt')
        file_descriptor = os.open(test_file, os.O_CREAT | os.O_WRONLY | self.o_binary)
        try:
            writer = arg_handle.get_fd_writer(file_descriptor)
            writer.write(b'test writing some more data')
        finally:
            os.close(file_descriptor)

        with open(test_file, 'rb') as fhl:
            self.assertEqual(b'test writing some more data', fhl.read())

    def test_get_fd_reader(self) -> None:
        """Test creating a reader from an fd."""

        test_file = os.path.join(self.tempdir, 'read-file.txt')
        with open(test_file, 'wb') as fhl:
            fhl.write(b'data to read')

        file_descriptor = os.open(test_file, os.O_RDONLY | self.o_binary)
        try:
            reader = arg_handle.get_fd_reader(file_descriptor)
            data = reader.read()
        finally:
            os.close(file_descriptor)

        self.assertEqual(b'data to read', data)
