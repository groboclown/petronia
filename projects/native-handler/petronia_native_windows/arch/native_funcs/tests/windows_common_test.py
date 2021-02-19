"""Slam these tests into this module."""

import unittest
from .. import windows_common


class WindowsErrorMessageTest(unittest.TestCase):
    """Test the WindowsErrorMessage class."""

    def test_with_error(self) -> None:
        """Provide the error in the call."""
        err = windows_common.WindowsErrorMessage('func', 4)
        self.assertEqual('func', err.called_function)
        self.assertEqual(4, err.errno)
        self.assertEqual(
            "WindowsErrorMessage(called='func', errno=4)",
            repr(err),
        )

    def test_without_error(self) -> None:
        """Provide the error in the call."""
        err = windows_common.WindowsErrorMessage('func')
        self.assertEqual('func', err.called_function)
        # Don't know what the real error is; probably 0, but just in case...
