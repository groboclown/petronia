"""Test the module."""

import unittest
from .. import color
from ..windows_common import RGB, COLORREF


class WinColorTest(unittest.TestCase):
    """Test the functions in the module."""

    def test_color_to_native_rgb(self) -> None:
        """Test the color_to_native_rgb function."""
        res = color.color_to_native_rgb((0xa0, 0x2b, 0x01, 0x3f))
        self.assertEqual(
            res.value,
            COLORREF(RGB(0xa0, 0x2b, 0x01)).value,
        )

    def test_color_rgba_to_native_rgb(self) -> None:
        """Test the color_rgba_to_native_rgb function."""
        # Invalid length
        self.assertIs(color.DEFAULT_COLORREF, color.color_rgba_to_native_rgb(()))
        self.assertIs(color.DEFAULT_COLORREF, color.color_rgba_to_native_rgb((1,)))
        self.assertIs(color.DEFAULT_COLORREF, color.color_rgba_to_native_rgb((1, 2)))

        # Invalid values
        self.assertIs(
            color.color_rgba_to_native_rgb((-1, 1, 1)),
            color.DEFAULT_COLORREF,
        )
        self.assertIs(
            color.color_rgba_to_native_rgb((1, -1, 1)),
            color.DEFAULT_COLORREF,
        )
        self.assertIs(
            color.color_rgba_to_native_rgb((1, 1, -1)),
            color.DEFAULT_COLORREF,
        )
        self.assertIs(
            color.color_rgba_to_native_rgb((0x1f0, 1, 1)),
            color.DEFAULT_COLORREF,
        )
        self.assertIs(
            color.color_rgba_to_native_rgb((1, 0x190, 1)),
            color.DEFAULT_COLORREF,
        )
        self.assertIs(
            color.color_rgba_to_native_rgb((1, 1, 0x190)),
            color.DEFAULT_COLORREF,
        )

        # Valid value with many items.
        self.assertEqual(
            color.color_rgba_to_native_rgb((0xff, 0xab, 0x03, 1, 2, 3, 4, 5)).value,
            COLORREF(RGB(0xff, 0xab, 0x03)).value,
        )
