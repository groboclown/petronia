
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
    TextBiDi,
    TEXT_BIDI_LTR,
    TEXT_BIDI_RTL,

    TextFragment,
    TextDisplay,
    Text,
)
from .image import (
    Image,
    ImageTransform,
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

    NativeScreenUnit,

    NativeScreenPosition,
    NATIVE_SCREEN_POSITION_X,
    NATIVE_SCREEN_POSITION_Y,

    NativeScreenSize,
    NATIVE_SCREEN_SIZE_WIDTH,
    NATIVE_SCREEN_SIZE_W,
    NATIVE_SCREEN_SIZE_HEIGHT,
    NATIVE_SCREEN_SIZE_H,

    NativeScreenArea,
    NATIVE_SCREEN_AREA_X,
    NATIVE_SCREEN_AREA_Y,
    NATIVE_SCREEN_AREA_WIDTH,
    NATIVE_SCREEN_AREA_W,
    NATIVE_SCREEN_AREA_HEIGHT,
    NATIVE_SCREEN_AREA_H,

    ScreenRect,
    EMPTY_SCREEN_RECT,
)
from .position import (
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

    ImageRelativeVerticalAlign,
    IMAGE_RELATIVE_VERTICAL_TOP,
    IMAGE_RELATIVE_VERTICAL_CENTER,
    IMAGE_RELATIVE_VERTICAL_BASELINE,
    IMAGE_RELATIVE_VERTICAL_BOTTOM,
    IMAGE_RELATIVE_VERTICAL_ALL,

    ImageRelativePosition,
    IMAGE_RELATIVE_POSITION_N,
    IMAGE_RELATIVE_POSITION_S,
    IMAGE_RELATIVE_POSITION_E,
    IMAGE_RELATIVE_POSITION_W,
    IMAGE_RELATIVE_POSITION_CENTER,
    IMAGE_RELATIVE_POSITION_ALL,

    ImageRelativeZOrder,
    IMAGE_RELATIVE_Z_ORDER_HARD,
    IMAGE_RELATIVE_Z_ORDER_FRONT,
    IMAGE_RELATIVE_Z_ORDER_BACK,
    IMAGE_RELATIVE_Z_ORDER_ALL,

    ImageRelativeTextPosition,
)
from .screen import (
    ScreenHandle,
    NativeScreenInfo,
    VirtualScreenArea,
    VirtualScreenInfo,
)
