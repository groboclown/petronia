
"""
RECT type.
"""

from ...arch.native_funcs.windows_common import (
    RECT, LONG,
)
from ......core.platform.api import (
    ScreenArea,
    SCREEN_AREA_H, SCREEN_AREA_W, SCREEN_AREA_X, SCREEN_AREA_Y,

    ScreenSize,
    SCREEN_SIZE_H, SCREEN_SIZE_W,

    ScreenRect,
)


def rect_to_screen_area(rect: RECT) -> ScreenArea:
    """Convert a RECT to a ScreenArea"""
    # ScreenArea = Tuple[ScreenUnit, ScreenUnit, ScreenUnit, ScreenUnit]
    return (
        rect.left.value,
        rect.top.value,
        (rect.right.value - rect.left.value),
        (rect.bottom.value - rect.top.value),
    )


def screen_area_to_rect(area: ScreenArea) -> RECT:
    """Convert a ScreenArea to a RECT."""
    rect = RECT()
    rect.left = LONG(area[SCREEN_AREA_X])
    rect.top = LONG(area[SCREEN_AREA_Y])
    rect.right = LONG(area[SCREEN_AREA_X] + area[SCREEN_AREA_W])
    rect.bottom = LONG(area[SCREEN_AREA_Y] + area[SCREEN_AREA_H])
    return rect


def rect_to_screen_size(rect: RECT) -> ScreenSize:
    """One-way conversion from a RECT to a ScreenSize."""
    return (
        (rect.right.value - rect.left.value),
        (rect.bottom.value - rect.top.value),
    )


def rect_to_screen_rect(rect: RECT) -> ScreenRect:
    """Convert a RECT to a ScreenRect"""
    return ScreenRect(
        left=rect.left.value,
        right=rect.right.value,
        top=rect.top.value,
        bottom=rect.bottom.value,

        x=rect.left.value,
        y=rect.top.value,
        width=(rect.right.value - rect.left.value),
        height=(rect.bottom.value - rect.top.value)
    )


def screen_rect_to_rect(screen: ScreenRect) -> RECT:
    rect = RECT()
    rect.left = LONG(screen.left)
    rect.right = LONG(screen.right)
    rect.top = LONG(screen.top)
    rect.bottom = LONG(screen.bottom)
    return rect
