"""Test the module."""

from typing import cast
import unittest
from petronia_native.common import defs
from .. import monitor
from ..windows_common import HMONITOR


class WindowsMonitorTest(unittest.TestCase):
    """Test the class and support functions."""

    def test_constructor(self) -> None:
        """Test the basic construction."""
        m_handle = cast(HMONITOR, 1)
        mtr = monitor.WindowsMonitor(
            monitor_handle=m_handle,
            monitor_index=0,
            monitor_left=2,
            monitor_right=32,
            monitor_top=3,
            monitor_bottom=43,
            work_left=10,
            work_right=50,
            work_top=100,
            work_bottom=122,
            vd_left=12,
            vd_right=52,
            vd_top=102,
            vd_bottom=124,
            name='m1',
            is_primary=False,
            dpi_x=96,
            dpi_y=97,
            scale_factor=12,
        )
        self.assertEqual(m_handle, mtr.handle)
        self.assertEqual(12, mtr.scale_factor)
        self.assertEqual(10, mtr.work_area[defs.MONITOR_AREA_X])
        self.assertEqual(100, mtr.work_area[defs.MONITOR_AREA_Y])
        self.assertEqual(40, mtr.work_area[defs.MONITOR_AREA_W])
        self.assertEqual(22, mtr.work_area[defs.MONITOR_AREA_H])
        self.assertEqual(12, mtr.virtual_desktop_area.left)
        self.assertEqual(52, mtr.virtual_desktop_area.right)
        self.assertEqual(102, mtr.virtual_desktop_area.top)
        self.assertEqual(124, mtr.virtual_desktop_area.bottom)
        self.assertEqual(96, mtr.info.dpi_x)
        self.assertEqual(97, mtr.info.dpi_y)
        self.assertEqual(30, mtr.info.real_pixel_width)
        self.assertEqual(40, mtr.info.real_pixel_height)
        self.assertRegex(mtr.info.description, r'^m1 - \d+$')
        self.assertEqual(False, mtr.info.supports_rotation)

        # Just throwing this here because it's a simple test that doesn't need excessive setup.
        self.assertTrue(mtr.is_in_virtual_desktop_area(12, 102))
        self.assertFalse(mtr.is_in_virtual_desktop_area(52, 124))

    def test_scale_factor__mod_100(self) -> None:
        """Test the basic construction."""
        mtr = monitor.WindowsMonitor(
            monitor_handle=cast(HMONITOR, 1), monitor_index=0,
            monitor_left=2, monitor_right=32, monitor_top=3, monitor_bottom=43,
            work_left=10, work_right=50, work_top=100, work_bottom=122,
            vd_left=12, vd_right=52, vd_top=102, vd_bottom=124,
            name='m1', is_primary=False,
            dpi_x=96, dpi_y=97,
            scale_factor=200,
        )
        self.assertEqual(
            2,
            mtr.scale_x(cast(defs.MonitorUnit, 4)),
        )
        self.assertEqual(
            2,
            mtr.scale_y(cast(defs.MonitorUnit, 4)),
        )

    def test_scale_factor__not_mod_100(self) -> None:
        """Test the basic construction."""
        mtr = monitor.WindowsMonitor(
            monitor_handle=cast(HMONITOR, 1), monitor_index=0,
            monitor_left=2, monitor_right=32, monitor_top=3, monitor_bottom=43,
            work_left=10, work_right=50, work_top=100, work_bottom=122,
            vd_left=12, vd_right=52, vd_top=102, vd_bottom=124,
            name='m1', is_primary=False,
            dpi_x=96, dpi_y=97,
            scale_factor=150,
        )
        self.assertEqual(
            66,
            mtr.scale_x(cast(defs.MonitorUnit, 100)),
        )
        self.assertEqual(
            66,
            mtr.scale_y(cast(defs.MonitorUnit, 100)),
        )

    def test_are_monitors_different(self) -> None:
        """test the function."""
        mtr1a = monitor.WindowsMonitor(
            monitor_handle=cast(HMONITOR, 1), monitor_index=0,
            monitor_left=2, monitor_right=32, monitor_top=3, monitor_bottom=43,
            work_left=10, work_right=50, work_top=100, work_bottom=122,
            vd_left=12, vd_right=52, vd_top=102, vd_bottom=124,
            name='m1a', is_primary=False,
            dpi_x=96, dpi_y=97,
            scale_factor=150,
        )
        mtr1b = monitor.WindowsMonitor(
            monitor_handle=cast(HMONITOR, 2), monitor_index=1,
            monitor_left=2, monitor_right=32, monitor_top=3, monitor_bottom=43,
            work_left=10, work_right=50, work_top=100, work_bottom=122,
            vd_left=12, vd_right=52, vd_top=102, vd_bottom=124,
            name='m1b', is_primary=False,
            dpi_x=96, dpi_y=97,
            scale_factor=150,
        )
        mtr2a = monitor.WindowsMonitor(
            monitor_handle=cast(HMONITOR, 3), monitor_index=2,
            monitor_left=2000, monitor_right=32000, monitor_top=3000, monitor_bottom=43000,
            work_left=10000, work_right=50000, work_top=100000, work_bottom=122000,
            vd_left=12, vd_right=52, vd_top=102, vd_bottom=124,
            name='m2a', is_primary=False,
            dpi_x=96, dpi_y=97,
            scale_factor=150,
        )
        mtr2b = monitor.WindowsMonitor(
            monitor_handle=cast(HMONITOR, 4), monitor_index=2,
            monitor_left=2000, monitor_right=32000, monitor_top=3000, monitor_bottom=43000,
            work_left=10000, work_right=50000, work_top=100000, work_bottom=122000,
            vd_left=12, vd_right=52, vd_top=102, vd_bottom=124,
            name='m2b', is_primary=False,
            dpi_x=96, dpi_y=97,
            scale_factor=150,
        )
        self.assertFalse(
            monitor.are_monitors_different([], [])
        )
        self.assertFalse(
            monitor.are_monitors_different([mtr1a], [mtr1a])
        )
        self.assertFalse(
            monitor.are_monitors_different([mtr1a], [mtr1b])
        )
        self.assertFalse(
            monitor.are_monitors_different([mtr1a, mtr2a], [mtr1a, mtr2a])
        )
        self.assertFalse(
            monitor.are_monitors_different([mtr1a, mtr2a], [mtr1b, mtr2b])
        )
        self.assertTrue(
            monitor.are_monitors_different([], [mtr1a])
        )
        self.assertTrue(
            monitor.are_monitors_different([mtr1a], [mtr2a])
        )
        self.assertTrue(
            monitor.are_monitors_different([mtr1a, mtr1b], [mtr1a])
        )
        self.assertTrue(
            monitor.are_monitors_different([mtr2a, mtr1a], [mtr1a, mtr2a])
        )
