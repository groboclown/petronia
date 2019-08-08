
"""General type definitions."""

from .action import (
    RespondsToAction,
)
from .color import (
    ColorRGBA,
    ColorStr,
    Color,
)
from .text import (
    TextFragment,
    TextDisplay,
    Text,

    TEXT_ORIENTATION_LTR,
    TEXT_ORIENTATION_RTL,
    TEXT_ORIENTATION_TTB,
    TEXT_ORIENTATION_LTR_ROTATE_TOP,
    TEXT_ORIENTATION_LTR_ROTATE_BOTTOM,
    TEXT_ORIENTATION_RTL_ROTATE_TOP,
    TEXT_ORIENTATION_RTL_ROTATE_BOTTOM,
    TEXT_ORIENTATIONS,
)
from .units import (
    FontQUnit,
    ScreenUnit,

    ScreenPosition,
    SCREEN_POSITION_X,
    SCREEN_POSITION_Y,

    ScreenSize,
    SCREEN_SIZE_WIDTH,
    SCREEN_SIZE_W,
    SCREEN_SIZE_HEIGHT,
    SCREEN_SIZE_H,

    ScreenArea,
    SCREEN_AREA_X,
    SCREEN_AREA_Y,
    SCREEN_AREA_WIDTH,
    SCREEN_AREA_W,
    SCREEN_AREA_HEIGHT,
    SCREEN_AREA_H,
)
