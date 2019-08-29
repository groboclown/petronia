
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
)
from .image import (
    Image,
    ImageLocation,
    ImageRaw,
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

    ScreenRect,
)
from .alignment import (
    TextBiDi,
    TEXT_BIDI_LTR,
    TEXT_BIDI_RTL,

    TextRotation,
    TEXT_ROTATE_HORIZ,
    TEXT_ROTATE_90_CLOCKWISE,
    TEXT_ROTATE_90_COUNTER_CLOCKWISE,
    TEXT_ROTATE_ALL,

    TextAlignment,
    TEXT_ALIGN_UPPER_LEFT,
    TEXT_ALIGN_UPPER_RIGHT,
    TEXT_ALIGN_BOTTOM_LEFT,
    TEXT_ALIGN_BOTTOM_RIGHT,
    TEXT_ALIGN_CENTER_LEFT,
    TEXT_ALIGN_CENTER_RIGHT,
    TEXT_ALIGN_UPPER_CENTER,
    TEXT_ALIGN_BOTTOM_CENTER,
    TEXT_ALIGN_CENTER_CENTER,
    TEXT_ALIGN_ALL,
)
from .screen import (
    ScreenHandle,
    NativeScreenInfo,
)