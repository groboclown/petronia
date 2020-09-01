
"""Test the arg_handle module."""

import unittest
import platform
from .. import arg_handle


class ArgHandleTest(unittest.TestCase):
    """Test the arg_handle functions."""

    def setUp(self) -> None:
        self.valid_fd = 2
        if platform.system() == 'Windows':
            import _winapi  # pylint: disable=C0415,E0401  # pragma no cover
            read_handle, write_handle = _winapi.CreatePipe(None, 0)  # pragma no cover
            _winapi.CloseHandle(read_handle)  # pragma no cover
            self.valid_fd = write_handle  # pragma no cover

    def tearDown(self) -> None:
        if platform.system() == 'Windows' and self.valid_fd:
            import _winapi  # pylint: disable=C0415,E0401  # pragma no cover
            _winapi.CloseHandle(self.valid_fd)  # pragma no cover

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
        ret = arg_handle.get_fd_from_argument(str(self.valid_fd))
        self.assertTrue(ret.ok)
        # Can't do a 1-for-1 check on the ret, because windows can return a different value.
