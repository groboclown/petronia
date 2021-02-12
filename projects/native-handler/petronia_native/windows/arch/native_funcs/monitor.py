
"""
Native Windows definitions that extend the platform API.
"""

# mypy requirement
import sys
assert sys.platform == 'win32'  # nosec

from typing import Sequence, Optional, cast
import math
from .windows_common import (
    HMONITOR,
)
from ....common import defs
from ....common.events.impl.monitor import Monitors as MonitorStruct


_MONITOR_INDEX = [-999999]
_MIN_MONITOR_INDEX = -999999
_MAX_MONITOR_INDEX = 9999999


class WindowsMonitor:
    """Windows-specific information on a monitor.  It includes DPI and scaling
    information for more accurate placement."""
    __slots__ = (
        '__handle',
        '__info',
        '__scale',
        '__straight_scale',
        '__index',
        '__work_area',
        '__is_primary',
    )

    def __init__(  # pylint:disable=too-many-arguments,too-many-locals
            self,
            monitor_handle: HMONITOR, monitor_index: int,
            monitor_left: int, monitor_right: int, monitor_top: int, monitor_bottom: int,
            work_left: int, work_right: int, work_top: int, work_bottom: int,
            name: Optional[str], is_primary: bool,
            dpi_x: int, dpi_y: int, scale_factor: int,
    ) -> None:
        identifier = _MONITOR_INDEX[0]
        _MONITOR_INDEX[0] += 1
        if _MONITOR_INDEX[0] > _MAX_MONITOR_INDEX:
            _MONITOR_INDEX[0] = _MIN_MONITOR_INDEX
        self.__handle = monitor_handle
        self.__info = MonitorStruct(
            identifier=identifier,

            # Should be something better...
            description=f'{name or str(monitor_index)} - {str(monitor_handle)}',

            real_pixel_width=monitor_right - monitor_left,
            real_pixel_height=monitor_bottom - monitor_top,

            dpi_x=max(1, dpi_x),
            dpi_y=max(1, dpi_y),

            supports_rotation=False,
        )

        # The "straight_scale" allows for faster computations where
        # a floating point division operation isn't necessary.
        self.__scale = scale_factor
        if scale_factor % 100 == 0:
            self.__straight_scale = scale_factor // 100
        else:
            self.__straight_scale = 0

        self.__index = monitor_index
        self.__is_primary = is_primary
        self.__work_area: defs.MonitorArea = (
            monitor_index,
            cast(defs.MonitorUnit, work_left), cast(defs.MonitorUnit, work_top),
            cast(defs.MonitorUnit, work_right - work_left + 1),
            cast(defs.MonitorUnit, work_bottom - work_top + 1),
        )

    @property
    def handle(self) -> HMONITOR:
        """The monitor's handle."""
        return self.__handle

    @property
    def info(self) -> MonitorStruct:
        """The shared monitor structure."""
        return self.__info

    @property
    def scale_factor(self) -> int:
        """* 100 scaling factor.  Greater than 100 means a single screen pixel unit
        covers multiple monitor pixel units, and less than 100 means that a screen pixel unit
        is a subdivision of a single monitor pixel."""
        return self.__scale

    def transform_pixel_to_screen(
            self,
            monitor_virtual_position: defs.ScreenArea,
            monitor_position: defs.MonitorPosition,
    ) -> defs.ScreenPosition:
        """Transform the monitor x,y position into a screen position, given the
        monitor's virtual space."""

    def scale_x(self, x: defs.MonitorUnit) -> defs.ScreenUnit:  # pylint:disable=invalid-name
        """Transform the x monitor pixel to a screen pixel.  Note that the screen pixel will
        assume the x is relative to position (0, 0)."""
        if self.__straight_scale > 0:
            return cast(defs.ScreenUnit, x // self.__straight_scale)
        return cast(defs.ScreenUnit, math.floor(x * 100 / self.__scale))

    def scale_y(self, y: defs.MonitorUnit) -> defs.ScreenUnit:  # pylint:disable=invalid-name
        """Transform the y monitor pixel to a screen pixel.  Note that the screen pixel will
        assume the y is relative to position (0, 0)."""
        if self.__straight_scale > 0:
            return cast(defs.ScreenUnit, y // self.__straight_scale)
        return cast(defs.ScreenUnit, math.floor(y * 100 / self.__scale))


def are_monitors_different(
        first: Sequence[WindowsMonitor], second: Sequence[WindowsMonitor],
) -> bool:
    """Are the monitors different?"""
    if len(first) != len(second):
        return True
    last = len(first)
    for i in range(last):
        if (
            first[i].info.real_pixel_width != second[i].info.real_pixel_width
            or first[i].info.real_pixel_height != second[i].info.real_pixel_height
            or first[i].info.dpi_x != second[i].info.dpi_x
            or first[i].info.dpi_y != second[i].info.dpi_y
        ):
            return True
    return False
