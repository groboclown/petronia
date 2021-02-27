"""Test the module"""

from typing import List, Tuple, Optional, cast
import unittest
from petronia_common.util import StdRet
from petronia_native.common.defs import OsScreenSize
from .. import windows_vs
from ..arch.native_funcs import WINDOWS_FUNCTIONS
from ..arch.native_funcs.windows_common import HFONT, HWND, HDC, WindowsReturnError


class WindowsVSTest(unittest.TestCase):
    """Test the module classes and functions."""

    def setUp(self) -> None:
        self._orig_get_text_size = WINDOWS_FUNCTIONS.window.get_text_size

    def tearDown(self) -> None:
        WINDOWS_FUNCTIONS.window.get_text_size = self._orig_get_text_size

    def test_get_text_size__not_set(self) -> None:
        """Test get_text_size without the underlying function set."""
        WINDOWS_FUNCTIONS.window.get_text_size = None

        hwnd1 = cast(HWND, 1)
        hfont2 = cast(HFONT, 2)
        res = windows_vs.get_text_size(hwnd1, hfont2, 2)
        self.assertIsNone(res)

    def test_get_text_size__set__returns_error(self) -> None:
        """Test the get_text_size function."""

        called_args: List[Tuple[HFONT, str, Optional[HWND], Optional[HDC]]] = []

        def callback(
                font: HFONT, text_sample: str, hwnd: Optional[HWND], hdc: Optional[HDC],
        ) -> StdRet[OsScreenSize]:
            called_args.append((font, text_sample, hwnd, hdc))
            return WindowsReturnError.stdret('get_text_size', 15100)

        WINDOWS_FUNCTIONS.window.get_text_size = callback

        hwnd1 = cast(HWND, 1)
        hfont2 = cast(HFONT, 2)
        res = windows_vs.get_text_size(hwnd1, hfont2, 2)
        self.assertIsNone(res)
        self.assertEqual(
            [(hfont2, 'mm', hwnd1, None)],
            called_args,
        )
