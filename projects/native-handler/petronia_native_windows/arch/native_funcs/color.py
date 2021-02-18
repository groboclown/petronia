
"""
Converts between Petronia colors and native color values.
"""

from typing import Sequence
from petronia_native.common.defs import (
    Color,
    color_to_rgba,
)
from .windows_common import (
    RGB, COLORREF,
)


def color_to_native_rgb(color: Color) -> COLORREF:
    """Convert a def's Color value into a COLORREF."""
    return color_rgba_to_native_rgb(color_to_rgba(color))


def color_rgba_to_native_rgb(color: Sequence[int]) -> COLORREF:
    """Convert an RGBA format int list into a COLORREF."""
    if (
            len(color) >= 3
            and 0 <= color[0] <= 0xff
            and 0 <= color[1] <= 0xff
            and 0 <= color[2] <= 0xff
    ):
        # Note that this is 0xbbggrr
        return COLORREF(RGB(color[0], color[1], color[2]))
    return DEFAULT_COLORREF


DEFAULT_COLORREF = COLORREF(RGB(0x80, 0x80, 0x80))
