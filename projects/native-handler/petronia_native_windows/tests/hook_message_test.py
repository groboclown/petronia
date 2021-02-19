"""Test the module."""

from typing import List, Tuple
from typing import cast as t_cast
import unittest
import ctypes
from petronia_native.common.defs.units import OsScreenRect
from .. import hook_messages
from ..arch import windows_constants
from ..arch.native_funcs.windows_common import HWND, LPARAM, WPARAM, RECT


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

        is_shell, _msg_id, cbk = hook_messages.display_changed_message(callback)
        self.assertFalse(is_shell)
        self.assertTrue(
            cbk(HWND_1, 2, WPARAM_2, LPARAM_3)
        )
        self.assertEqual([True], called)

    def test_system_settings_changed_message(self) -> None:
        """system_settings_changed_message"""

        called: List[WPARAM] = []

        def callback(wparam: WPARAM) -> None:
            called.append(wparam)

        is_shell, _msg_id, cbk = hook_messages.system_settings_changed_message(callback)
        self.assertFalse(is_shell)
        self.assertTrue(
            cbk(HWND_1, 2, WPARAM_2, LPARAM_3)
        )
        self.assertEqual([WPARAM_2], called)

    def test_device_changed_message(self) -> None:
        """device_changed_message"""

        called: List[WPARAM] = []

        def callback(wparam: WPARAM) -> None:
            called.append(wparam)

        is_shell, _msg_id, cbk = hook_messages.device_changed_message(callback)
        self.assertFalse(is_shell)
        self.assertTrue(
            cbk(HWND_1, 2, WPARAM_2, LPARAM_3)
        )
        self.assertEqual([WPARAM_2], called)

    def test_window_minimized_message(self) -> None:
        """window_minimized_message"""

        called: List[Tuple[HWND, OsScreenRect]] = []

        def callback(hwnd: HWND, rect: RECT) -> None:
            called.append((hwnd, OsScreenRect.from_border(
                rect.left, rect.right, rect.top, rect.bottom,  # type: ignore
            )))

        is_shell, _msg_id, cbk = hook_messages.window_minimized_message(callback)
        self.assertTrue(is_shell)

        rect_val = hook_messages.SHELLHOOKINFO()
        rect_val.hwnd = HWND_1
        rect_val.rc.left = 1
        rect_val.rc.right = 2
        rect_val.rc.top = 3
        rect_val.rc.bottom = 4

        self.assertTrue(
            cbk(
                HWND_1, 2, WPARAM_2,
                t_cast(LPARAM, ctypes.byref(rect_val)),
            )
        )
        self.assertEqual(
            [(HWND_1, OsScreenRect.from_border(1, 2, 3, 4))],
            called,
        )

    def test_window_created_message(self) -> None:
        """window_created_message"""

        called: List[HWND] = []

        def callback(wparam: HWND) -> None:
            called.append(wparam)

        is_shell, _msg_id, cbk = hook_messages.window_created_message(callback)
        self.assertTrue(is_shell)
        self.assertTrue(
            cbk(HWND_1, 2, WPARAM_2, LPARAM_3)
        )
        self.assertEqual([LPARAM_3], called)

    def test_window_destroyed_message(self) -> None:
        """window_destroyed_message"""

        called: List[HWND] = []

        def callback(wparam: HWND) -> None:
            called.append(wparam)

        is_shell, _msg_id, cbk = hook_messages.window_destroyed_message(callback)
        self.assertTrue(is_shell)
        self.assertTrue(
            cbk(HWND_1, 2, WPARAM_2, LPARAM_3)
        )
        self.assertEqual([LPARAM_3], called)

    def test_shell_window_focused_message(self) -> None:
        """shell_window_focused_message"""

        called: List[HWND] = []

        def callback(wparam: HWND) -> None:
            called.append(wparam)

        is_shell, _msg_id, cbk = hook_messages.shell_window_focused_message(callback)
        self.assertTrue(is_shell)
        self.assertTrue(
            cbk(HWND_1, 2, WPARAM_2, LPARAM_3)
        )
        self.assertEqual([LPARAM_3], called)

    def test_window_activated_message(self) -> None:
        """window_activated_message"""

        called: List[HWND] = []

        def callback(wparam: HWND) -> None:
            called.append(wparam)

        is_shell, _msg_id, cbk = hook_messages.window_activated_message(callback)
        self.assertTrue(is_shell)
        self.assertTrue(
            cbk(HWND_1, 2, WPARAM_2, LPARAM_3)
        )
        self.assertEqual([LPARAM_3], called)

    def test_window_rude_activated_message(self) -> None:
        """window_rude_activated_message"""

        called: List[HWND] = []

        def callback(wparam: HWND) -> None:
            called.append(wparam)

        is_shell, _msg_id, cbk = hook_messages.window_rude_activated_message(callback)
        self.assertTrue(is_shell)
        self.assertTrue(
            cbk(HWND_1, 2, WPARAM_2, LPARAM_3)
        )
        self.assertEqual([LPARAM_3], called)

    def test_redraw_message(self) -> None:
        """redraw_message"""

        called: List[HWND] = []

        def callback(wparam: HWND) -> None:
            called.append(wparam)

        is_shell, _msg_id, cbk = hook_messages.redraw_message(callback)
        self.assertTrue(is_shell)
        self.assertTrue(
            cbk(HWND_1, 2, WPARAM_2, LPARAM_3)
        )
        self.assertEqual([LPARAM_3], called)

    def test_forced_exit_message(self) -> None:
        """forced_exit_message"""

        called: List[HWND] = []

        def callback(wparam: HWND) -> None:
            called.append(wparam)

        is_shell, _msg_id, cbk = hook_messages.forced_exit_message(callback)
        self.assertTrue(is_shell)
        self.assertTrue(
            cbk(HWND_1, 2, WPARAM_2, LPARAM_3)
        )
        self.assertEqual([LPARAM_3], called)

    def test_window_monitor_changed_message(self) -> None:
        """window_monitor_changed_message"""

        called: List[HWND] = []

        def callback(wparam: HWND) -> None:
            called.append(wparam)

        is_shell, _msg_id, cbk = hook_messages.window_monitor_changed_message(callback)
        self.assertTrue(is_shell)
        self.assertTrue(
            cbk(HWND_1, 2, WPARAM_2, LPARAM_3)
        )
        self.assertEqual([LPARAM_3], called)

    def test_window_flash_message(self) -> None:
        """window_monitor_changed_message"""

        called: List[HWND] = []

        def callback(wparam: HWND) -> bool:
            called.append(wparam)
            return False

        is_shell, _msg_id, cbk = hook_messages.window_flash_message(callback)
        self.assertTrue(is_shell)
        self.assertFalse(
            cbk(HWND_1, 2, WPARAM_2, LPARAM_3)
        )
        self.assertEqual([LPARAM_3], called)

    def test_window_replacing_message(self) -> None:
        """window_replacing_message"""

        called: List[Tuple[HWND, HWND]] = []

        def callback(new: HWND, old: HWND) -> None:
            called.append((new, old))

        is_shell, _msg_id, cbk = hook_messages.window_replacing_message(callback)
        self.assertTrue(is_shell)
        self.assertTrue(
            cbk(HWND_1, 2, WPARAM_2, LPARAM_3)
        )
        self.assertEqual([(LPARAM_3, HWND_1)], called)

    def test_window_replaced_message(self) -> None:
        """window_replaced_message"""

        called: List[Tuple[HWND, HWND]] = []

        def callback(new: HWND, old: HWND) -> None:
            called.append((new, old))

        is_shell, _msg_id, cbk = hook_messages.window_replaced_message(callback)
        self.assertTrue(is_shell)
        self.assertTrue(
            cbk(HWND_1, 2, WPARAM_2, LPARAM_3)
        )
        self.assertEqual([(LPARAM_3, HWND_1)], called)

    def test_system_power_state_changed(self) -> None:
        """window_replaced_message"""

        called: List[bool] = []

        def callback(entering_suspend: bool) -> None:
            called.append(entering_suspend)

        is_shell, _msg_id, cbk = hook_messages.system_power_state_changed(callback)
        self.assertTrue(is_shell)
        # Only check the return code once.
        self.assertTrue(
            cbk(HWND_1, 2, t_cast(WPARAM, windows_constants.PBT_APMRESUMESUSPEND), LPARAM_3)
        )
        self.assertEqual([False], called)
        called.clear()
        cbk(HWND_1, 2, t_cast(WPARAM, windows_constants.PBT_APMSUSPEND), LPARAM_3)
        self.assertEqual([True], called)
        called.clear()
        cbk(HWND_1, 2, t_cast(WPARAM, windows_constants.PBT_APMRESUMEAUTOMATIC), LPARAM_3)
        self.assertEqual([], called)
        called.clear()
        cbk(HWND_1, 2, t_cast(WPARAM, windows_constants.PBT_APMPOWERSTATUSCHANGE), LPARAM_3)
        self.assertEqual([], called)

    def test_taskman_message(self) -> None:
        """taskman_message"""

        called: List[Tuple[HWND, WPARAM]] = []

        def callback(hwnd: HWND, wparam: WPARAM) -> None:
            called.append((hwnd, wparam))

        is_shell, _msg_id, cbk = hook_messages.taskman_message(callback)
        self.assertTrue(is_shell)
        self.assertTrue(
            cbk(HWND_1, 2, WPARAM_2, LPARAM_3)
        )
        self.assertEqual([(LPARAM_3, WPARAM_2)], called)
