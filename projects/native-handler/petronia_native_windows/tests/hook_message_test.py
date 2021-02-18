"""Test the module."""

from typing import List, Tuple
from typing import cast as t_cast
import unittest
import ctypes
from .. import hook_messages
from ..arch.native_funcs.windows_common import HWND, LPARAM, WPARAM, RECT, LPVOID
from petronia_native.common.defs.units import OsScreenRect


HWND_1 = t_cast(HWND, 1)
WPARAM_2 = t_cast(WPARAM, 2)
LPARAM_3 = t_cast(LPARAM, 3)


class HookMessageTest(unittest.TestCase):
    """Tests the functions.

    The really correct way to test this is by registering a message, start up a message loop,
    then inject that message into the loop.  However, that's ... difficult at best.

    Instead, this will test out the handler that wraps the callback.
    """

    def test_display_changed_message(self) -> None:
        """display_changed_message"""

        called: List[bool] = []

        def callback() -> None:
            called.append(True)

        is_shell, _msg_id, cb = hook_messages.display_changed_message(callback)
        self.assertFalse(is_shell)
        cb(HWND_1, 2, WPARAM_2, LPARAM_3)
        self.assertEqual([True], called)

    def test_system_settings_changed_message(self) -> None:
        """system_settings_changed_message"""

        called: List[WPARAM] = []

        def callback(wparam: WPARAM) -> None:
            called.append(wparam)

        is_shell, _msg_id, cb = hook_messages.system_settings_changed_message(callback)
        self.assertFalse(is_shell)
        cb(HWND_1, 2, WPARAM_2, LPARAM_3)
        self.assertEqual([WPARAM_2], called)

    def test_device_changed_message(self) -> None:
        """device_changed_message"""

        called: List[WPARAM] = []

        def callback(wparam: WPARAM) -> None:
            called.append(wparam)

        is_shell, _msg_id, cb = hook_messages.device_changed_message(callback)
        self.assertFalse(is_shell)
        cb(HWND_1, 2, WPARAM_2, LPARAM_3)
        self.assertEqual([WPARAM_2], called)

    def test_window_minimized_message(self) -> None:
        """window_minimized_message"""

        called: List[Tuple[HWND, OsScreenRect]] = []

        def callback(hwnd: HWND, rect: RECT) -> None:
            called.append((hwnd, OsScreenRect.from_border(
                rect.left, rect.right, rect.top, rect.bottom,  # type: ignore
            )))

        is_shell, _msg_id, cb = hook_messages.window_minimized_message(callback)
        self.assertTrue(is_shell)

        rect_val = hook_messages.SHELLHOOKINFO()
        rect_val.hwnd = HWND_1
        rect_val.rc.left = 1
        rect_val.rc.right = 2
        rect_val.rc.top = 3
        rect_val.rc.bottom = 4

        cb(
            HWND_1, 2, WPARAM_2,
            t_cast(LPARAM, ctypes.byref(rect_val)),
        )
        self.assertEqual(
            [(HWND_1, OsScreenRect.from_border(1, 2, 3, 4))],
            called,
        )
