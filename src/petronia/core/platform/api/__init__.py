
"""
API that the platform components must implement.

This defines what is expected from the platform runtime implementation.
"""

from .bootstrap import bootstrap_platform_api as start_extension
from .bootstrap import EXTENSION_METADATA


from .defs import (
    RespondsToAction,

    ColorRGBA,
    ColorStr,
    Color,

    TextFragment,
    TextDisplay,
    Text,

    Image,
    ImageLocation,
    ImageRaw,

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

    ScreenHandle,
    NativeScreenInfo,
)
from .window.state import (
    NativeWindowState,
)
