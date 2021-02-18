"""Test the color functions."""

import unittest
from .. import color


class ColorTest(unittest.TestCase):
    """Test the module functions."""

    def test_color_to_rgba(self) -> None:
        """Test color_to_rgba."""

        # No conversion
        self.assertIs(
            color.COLOR_NAME_MAP['red'],
            color.color_to_rgba(color.COLOR_NAME_MAP['red']),
        )

        # String conversion
        self.assertIs(
            color.DEFAULT_COLOR,
            color.color_to_rgba(''),
        )

    def test_color_str_to_rgba(self) -> None:
        """Test color_str_to_rgba"""

        # Unset color.
        self.assertIs(
            color.DEFAULT_COLOR,
            color.color_str_to_rgba(''),
        )

        # 3-nybble hex.
        self.assertEqual(
            (0xaa, 0x11, 0x33, 0xff),
            color.color_str_to_rgba('#a13'),
        )

        # 4-nybble hex
        self.assertEqual(
            (0xaa, 0x11, 0x33, 0x00),
            color.color_str_to_rgba('#a130'),
        )

        # 6-nybble hex
        self.assertEqual(
            (0x3a, 0x02, 0x4b, 0xff),
            color.color_str_to_rgba('#3a024b'),
        )

        # 8-nybble hex
        self.assertEqual(
            (0x3a, 0x02, 0x4b, 0xe0),
            color.color_str_to_rgba('#3a024be0'),
        )

        # Known color name
        self.assertIs(
            color.COLOR_NAME_MAP['blue'],
            color.color_str_to_rgba('blue'),
        )

        # Unknown color
        self.assertIs(
            color.DEFAULT_COLOR,
            color.color_str_to_rgba('not a color name'),
        )

        # Invalid hex length
        self.assertIs(
            color.DEFAULT_COLOR,
            color.color_str_to_rgba('#a'),
        )
