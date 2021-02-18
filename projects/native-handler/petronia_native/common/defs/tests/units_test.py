"""Test the module"""

from typing import cast as t_cast
import unittest
from .. import units


class UnitsTest(unittest.TestCase):
    """Test module functions."""

    def test_screen_rect(self) -> None:
        """Test the ScreenRect structure."""

        # Note: this is an invalid rectangle construction, in terms
        # of business logic, but for testing purposes it's fine.
        rect = units.ScreenRect(
            t_cast(units.ScreenUnit, 1),
            t_cast(units.ScreenUnit, 2),
            t_cast(units.ScreenUnit, 3),
            t_cast(units.ScreenUnit, 4),
            t_cast(units.ScreenUnit, 5),
            t_cast(units.ScreenUnit, 6),
            t_cast(units.ScreenUnit, 7),
            t_cast(units.ScreenUnit, 8),
        )
        self.assertEqual(1, rect.x)
        self.assertEqual(2, rect.y)
        self.assertEqual(3, rect.width)
        self.assertEqual(4, rect.height)
        self.assertEqual(5, rect.left)
        self.assertEqual(6, rect.right)
        self.assertEqual(7, rect.top)
        self.assertEqual(8, rect.bottom)

        self.assertTrue(rect.__eq__(rect))
        self.assertFalse(rect.__ne__(rect))
        self.assertFalse(rect.__eq__('x'))

        # try in a hash...
        hashed_values = {rect: 1}
        self.assertIs(1, hashed_values[rect])

        rect2 = units.ScreenRect.from_border(1, 2, 3, 4)
        self.assertFalse(rect.__eq__(rect2))
        self.assertTrue(rect.__ne__(rect2))
        self.assertFalse(rect2.__eq__(rect))
        self.assertTrue(rect2.__ne__(rect))
        self.assertEqual(1, rect2.x)
        self.assertEqual(1, rect2.left)
        self.assertEqual(2, rect2.width)
        self.assertEqual(2, rect2.right)
        self.assertEqual(3, rect2.y)
        self.assertEqual(3, rect2.top)
        self.assertEqual(4, rect2.bottom)
        self.assertEqual(2, rect2.height)
        self.assertEqual((1, 3, 2, 2), rect2.get_area())
        self.assertEqual(
            'ScreenRect(x=1, y=3, w=2, h=2)',
            repr(rect2),
        )

    def test_os_screen_rect(self) -> None:
        """Test the OsScreenRect structure."""
        rect1 = units.OsScreenRect.from_coordinates(1, 20, 10, 199)
        rect2 = units.OsScreenRect.from_border(1, 10, 20, 199)
        rect3 = units.OsScreenRect.from_size(1, 20, 10, 180)
        rect_list = (rect1, rect2, rect3)
        for i in range(len(rect_list)):  # pylint:disable=consider-using-enumerate
            rect = rect_list[i]
            with self.subTest(str(i)):
                self.assertEqual(1, rect.x)
                self.assertEqual(1, rect.left)
                self.assertEqual(20, rect.y)
                self.assertEqual(20, rect.top)
                self.assertEqual(10, rect.right)
                self.assertEqual(199, rect.bottom)
                self.assertEqual(10, rect.width)
                self.assertEqual(180, rect.height)

        self.assertTrue(rect1.__eq__(rect1))
        self.assertFalse(rect1.__ne__(rect1))
        self.assertTrue(rect1.__eq__(rect2))
        self.assertFalse(rect1.__eq__('x'))
