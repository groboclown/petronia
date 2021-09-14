"""Test the module."""

import unittest

from petronia_common.util import not_none
from .. import window_handler
from ..arch.native_funcs import HWND, WINDOWS_FUNCTIONS


class WindowHandlerTest(unittest.TestCase):
    """Test the windows implementation."""

    def test__mk_window_state(self) -> None:
        """Test the _mk_window_state function."""

        # Use a real HWND value returned by the win32 API, as opposed to trying to
        # create one which may not be right.
        assert WINDOWS_FUNCTIONS.window.find_handles is not None  # nosec
        windows = WINDOWS_FUNCTIONS.window.find_handles()
        self.assertTrue(len(windows) > 0)
        handler = AccessibleWindowHandler()
        hwnd = windows[0]
        nwn = handler.internal__mk_window_state(hwnd)
        self.assertIs(hwnd, nwn.native_id)


class AccessibleWindowHandler(window_handler.WindowsNativeHandler):
    """Testable version of the WindowsNativeHandler class"""

    def internal__mk_window_state(self, hwnd: HWND) -> window_handler.WindowsNativeWindow:
        """return _mk_window_state"""
        return not_none(self._mk_window_state(hwnd))
