
"""
Native Windows definitions that extend the platform API.
"""

from typing import Optional
import math
from .windows_common import (
    HMONITOR,
)
from ......core.platform.api import (
    NativeScreenInfo,
    NativeScreenUnit,
    ScreenUnit,
)


class WindowsMonitor:
    """Windows-specific information on a monitor.  It includes DPI and scaling
    information for more accurate placement."""
    __slots__ = (
        '__handle',
        '__info',
        '__dpi_x',
        '__dpi_y',
        '__scale',
        '__straight_scale',
    )

    def __init__(
            self,
            monitor_handle: HMONITOR, screen_index: int,
            monitor_left: int, monitor_right: int, monitor_top: int, monitor_bottom: int,
            work_left: int, work_right: int, work_top: int, work_bottom: int,
            name: Optional[str], is_primary: bool,
            dpi_x: int, dpi_y: int, scale_factor: int
    ):
        self.__handle = monitor_handle
        self.__info = NativeScreenInfo(
            # Disguise the handle as something else
            handle=str(monitor_handle),
            screen_index=screen_index,
            screen_size=(
                monitor_left, monitor_top,
                monitor_right - monitor_left + 1,
                monitor_bottom - monitor_top + 1
            ),
            work_area=(
                work_left, work_top,
                work_right - work_left + 1,
                work_bottom - work_top + 1
            ),
            name=name or str(screen_index),
            is_primary=is_primary
        )

        self.__dpi_x = dpi_x
        self.__dpi_y = dpi_y

        self.__scale = scale_factor
        if scale_factor % 100 == 0:
            self.__straight_scale = scale_factor // 100
        else:
            self.__straight_scale = 0


    @property
    def handle(self) -> HMONITOR:
        return self.__handle

    @property
    def info(self) -> NativeScreenInfo:
        return self.__info

    @property
    def dpi_x(self) -> int:
        return self.__dpi_x

    @property
    def dpi_y(self) -> int:
        return self.__dpi_y

    @property
    def scale_factor(self) -> int:
        """* 100 scaling factor."""
        return self.__scale

    def scale_x(self, x: NativeScreenUnit) -> ScreenUnit:
        if self.__straight_scale > 0:
            return x * self.__straight_scale
        return math.floor((self.__scale * x) / 100)

    def scale_y(self, y: NativeScreenUnit) -> ScreenUnit:
        if self.__straight_scale > 0:
            return y * self.__straight_scale
        return math.floor((self.__scale * y) / 100)
