"""Basic definitions shared across systems."""

from . import units
from .units import (
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
