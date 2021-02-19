"""Test the module."""

from typing import List, Tuple, cast
import unittest
from petronia_native.common.defs import OsScreenRect
from .. import window_state
from ..windows_common import RECT, GUITHREADINFO, HWND, LONG
from ...windows_constants import (
    GUI_CARETBLINKING, GUI_INMENUMODE, GUI_INMOVESIZE, GUI_POPUPMENUMODE, GUI_SYSTEMMENUMODE,
)


class WindowStateTest(unittest.TestCase):
    """Test the functions and classes in the module."""

    def test_convert_rect(self) -> None:
        """Test converting a windows RECT to an Os rect."""
        rect = RECT()
        rect.top = LONG(10)
        rect.bottom = LONG(20)
        rect.left = LONG(100)
        rect.right = LONG(200)
        os_rect = window_state.convert_rect(rect)
        self.assertEqual(
            OsScreenRect(
                x=100, y=10, width=100, height=10, left=100, right=200, top=10, bottom=20,
            ),
            os_rect,
        )

    def test_window_state(self) -> None:
        """Test the window state construction function + class."""
        hwnd1 = cast(HWND, 1)
        hwnd2 = cast(HWND, 2)
        hwnd3 = cast(HWND, 3)
        hwnd4 = cast(HWND, 4)
        hwnd5 = cast(HWND, 5)
        hwnd6 = cast(HWND, 6)
        rect = OsScreenRect(
            x=100, y=10, width=100, height=10, left=100, right=200, top=10, bottom=20,
        )

        flag_data: List[Tuple[int, List[str]]] = [
            (0, []),
            (GUI_CARETBLINKING, ['caret-blinking']),
            (GUI_INMENUMODE, ['in-menu-mode']),
            (GUI_INMOVESIZE, ['in-move-size']),
            (GUI_POPUPMENUMODE, ['popup-menu-mode']),
            (GUI_SYSTEMMENUMODE, ['in-system-menu-mode']),
        ]

        for flag, flag_names in flag_data:
            with self.subTest(str(flag_data)):
                info = GUITHREADINFO()
                info.flags = flag
                info.hwndActive = hwnd1
                info.hwndFocus = hwnd2
                info.hwndCapture = hwnd3
                info.hwndMenuOwner = hwnd4
                info.hwndMoveSize = hwnd5
                info.hwndCaret = hwnd6
                info.rcCaret.top = 10
                info.rcCaret.bottom = 20
                info.rcCaret.left = 100
                info.rcCaret.right = 200

                state = window_state.create_windows_window_state(info)
                self.assertEqual(
                    set(flag_names),
                    set(state.flags),
                )
                self.assertEqual(
                    hwnd1,
                    state.active,
                )
                self.assertEqual(
                    hwnd2,
                    state.focus,
                )
                self.assertEqual(
                    hwnd3,
                    state.capture,
                )
                self.assertEqual(
                    hwnd4,
                    state.menu_owner,
                )
                self.assertEqual(
                    hwnd5,
                    state.move_size,
                )
                self.assertEqual(
                    hwnd6,
                    state.caret,
                )
                self.assertEqual(
                    rect,
                    state.caret_rect,
                )
