"""Test the module"""

from typing import cast
import unittest.mock
from .. import monitor_screen
from ... import defs


class MonitorScreenTest(unittest.TestCase):
    """Test classes and functions in the module."""

    def test_create_monitor_state(self) -> None:
        """Test create_monitor_state"""
        res = monitor_screen.create_monitor_state(
            1, 'desc',
            (cast(defs.MonitorUnit, 2), cast(defs.MonitorUnit, 3)),
            6, 7, True,
        )
        self.assertEqual(1, res.identifier)
        self.assertEqual('desc', res.description)
        self.assertEqual(2, res.real_pixel_width)
        self.assertEqual(3, res.real_pixel_height)
        self.assertEqual(6, res.dpi_x)
        self.assertEqual(7, res.dpi_y)
        self.assertEqual(True, res.supports_rotation)
