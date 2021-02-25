"""Test the module."""

from typing import cast
import unittest
from .. import virtual_screen, defs
# from ..events.impl import monitor


class VirtualScreenBlockTest(unittest.TestCase):
    """Test the VirtualScreenBlock class."""

    def test_screen_to_monitor__out_of_bounds_both(self) -> None:
        """Test the screen_to_monitor function"""
        block = virtual_screen.VirtualScreenBlock(
            _mk_monitor_area(1, 0, 0, 200, 300),
            _mk_screen_area(-5, -7, 2, 3),
            0,
        )
        self.assertIsNone(block.screen_to_monitor(_mk_screen_pos(2, 3)))
        self.assertIsNone(block.screen_to_monitor(_mk_screen_pos(-3, -4)))

    def test_screen_to_monitor__out_of_bounds_x(self) -> None:
        """Test the screen_to_monitor function"""
        block = virtual_screen.VirtualScreenBlock(
            _mk_monitor_area(1, 0, 0, 200, 300),
            _mk_screen_area(-5, -7, 2, 3),
            0,
        )
        res = block.screen_to_monitor(_mk_screen_pos(2, -6))
        self.assertIsNone(res)

    def test_screen_to_monitor__out_of_bounds_y(self) -> None:
        """Test the screen_to_monitor function"""
        block = virtual_screen.VirtualScreenBlock(
            _mk_monitor_area(1, 0, 0, 200, 300),
            _mk_screen_area(-5, -7, 2, 3),
            0,
        )
        res = block.screen_to_monitor(_mk_screen_pos(-4, 3))
        self.assertIsNone(res)

    def test_screen_to_monitor__in_bounds_1(self) -> None:
        """Test the screen_to_monitor function"""
        # identity mapping
        block = virtual_screen.VirtualScreenBlock(
            _mk_monitor_area(1, 0, 0, 200, 300),
            _mk_screen_area(0, 0, 200, 300),
            0,
        )
        self.assertEqual(
            (1, 0, 0),
            block.screen_to_monitor(_mk_screen_pos(0, 0)),
        )
        self.assertEqual(
            (1, 199, 299),
            block.screen_to_monitor(_mk_screen_pos(199, 299)),
        )

    def test_screen_to_monitor__in_bounds_2(self) -> None:
        """Test the screen_to_monitor function"""
        # translation mapping
        block = virtual_screen.VirtualScreenBlock(
            _mk_monitor_area(1, 5, 7, 200, 300),
            _mk_screen_area(11, 12, 200, 300),
            0,
        )
        self.assertEqual(
            (1, 5, 7),
            block.screen_to_monitor(_mk_screen_pos(11, 12)),
        )
        self.assertEqual(
            (1, 204, 306),
            block.screen_to_monitor(_mk_screen_pos(210, 311)),
        )

    def test_screen_to_monitor__in_bounds_3(self) -> None:
        """Test the screen_to_monitor function"""
        # non-integer resize
        block = virtual_screen.VirtualScreenBlock(
            _mk_monitor_area(1, 0, 0, 200, 300),
            _mk_screen_area(0, 0, 300, 400),
            0,
        )
        self.assertEqual(
            (1, 0, 0),
            block.screen_to_monitor(_mk_screen_pos(0, 0)),
        )
        self.assertEqual(
            (1, 199, 299),
            block.screen_to_monitor(_mk_screen_pos(299, 399)),
        )


# def _mk_monitor(
#         identifier: int,
#         width: int, height: int,
#         dpi_x: int = 96, dpi_y: int = 96,
# ) -> monitor.Monitor:
#     return monitor.Monitor(
#         identifier=identifier,
#         description=f'm-{identifier}',
#         real_pixel_width=width,
#         real_pixel_height=height,
#         dpi_x=dpi_x, dpi_y=dpi_y,
#         supports_rotation=False,
#     )


def _mk_monitor_area(  # pylint:disable=invalid-name
        identifier: int, x: int, y: int, w: int, h: int,
) -> defs.MonitorArea:
    return (
        identifier,
        cast(defs.MonitorUnit, x),
        cast(defs.MonitorUnit, y),
        cast(defs.MonitorUnit, w),
        cast(defs.MonitorUnit, h),
    )


def _mk_screen_area(  # pylint:disable=invalid-name
        x: int, y: int, w: int, h: int,
) -> defs.ScreenArea:
    return (
        cast(defs.ScreenUnit, x),
        cast(defs.ScreenUnit, y),
        cast(defs.ScreenUnit, w),
        cast(defs.ScreenUnit, h),
    )


def _mk_screen_pos(  # pylint:disable=invalid-name
        x: int, y: int,
) -> defs.ScreenPosition:
    return (
        cast(defs.ScreenUnit, x),
        cast(defs.ScreenUnit, y),
    )
