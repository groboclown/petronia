"""Basic definitions shared across systems."""

from . import units
from .units import (
    OsScreenPosition,
    OsScreenSize,
    OsScreenRect,
    MonitorUnit,
    MonitorSize,
    MonitorArea,
    MonitorPosition,
    ScreenUnit,
    ScreenSize,
    ScreenArea,
    ScreenRect,
    ScreenPosition,

    ZERO_MONITOR_UNIT,

    MONITOR_POSITION_X, MONITOR_POSITION_Y, MONITOR_POSITION_MONITOR_IDENTIFIER,

    MONITOR_SIZE_W, MONITOR_SIZE_H, MONITOR_SIZE_WIDTH, MONITOR_SIZE_HEIGHT,

    MONITOR_AREA_MONITOR_INDEX, MONITOR_AREA_X, MONITOR_AREA_Y,
    MONITOR_AREA_W, MONITOR_AREA_H, MONITOR_AREA_WIDTH, MONITOR_AREA_HEIGHT,

    ZERO_SCREEN_UNIT,

    SCREEN_POSITION_X, SCREEN_POSITION_Y,

    SCREEN_AREA_X, SCREEN_AREA_Y,
    SCREEN_AREA_W, SCREEN_AREA_H, SCREEN_AREA_WIDTH, SCREEN_AREA_HEIGHT,

    OS_SCREEN_SIZE_WIDTH,
    OS_SCREEN_SIZE_HEIGHT,

    OS_SCREEN_POSITION_X,
    OS_SCREEN_POSITION_Y,
)

from . import color
from .color import (
    ColorRGBA,
    ColorStr,
    Color,
    DEFAULT_COLOR,
    color_str_to_rgba,
    color_to_rgba,
)
