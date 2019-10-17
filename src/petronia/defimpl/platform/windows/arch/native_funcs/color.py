
"""
Converts between Petronia colors and native color values.
"""

from typing import Dict, Sequence
from ......core.platform.api import (
    ColorRGBA,
    ColorStr,
    Color,
)
from .windows_common import (
    RGB, COLORREF,
)


def to_rgb(color: Color) -> COLORREF:
    if isinstance(color, str):
        return color_rgba_to_rgb(str_to_rgba(color))
    if isinstance(color, Sequence) and not isinstance(color, str):
        return color_rgba_to_rgb(color)
    return color_rgba_to_rgb(DEFAULT_COLOR)


def color_rgba_to_rgb(color: Sequence[int]) -> COLORREF:
    assert (
            len(color) >= 3 and
            0 <= color[0] <= 0xff and
            0 <= color[1] <= 0xff and
            0 <= color[2] <= 0xff
    )
    # Note that this is 0xbbggrr
    return COLORREF(RGB(color[0], color[1], color[2]))


DEFAULT_COLOR = (0x80, 0x80, 0x80, 0xff,)
COLOR_NAME_MAP: Dict[str, ColorRGBA] = {
    'red':     (0xff, 0x00, 0x00, 0xff,),
    'green':   (0xff, 0xff, 0x00, 0xff,),
    'blue':    (0x00, 0x00, 0xff, 0xff,),
    'white':   (0xff, 0xff, 0xff, 0xff,),
    'black':   (0x00, 0x00, 0x00, 0xff,),

    # TODO
}


def str_to_rgba(color: ColorStr) -> ColorRGBA:
    color = color.strip().lower()
    if not color:
        return DEFAULT_COLOR
    try:
        if color[0] == '#':
            if len(color) == 4:
                return (
                    int(color[1] + color[1], 16),
                    int(color[2] + color[2], 16),
                    int(color[3] + color[3], 16),
                    0xff,
                )
            if len(color) == 5:
                return (
                    int(color[1] + color[1], 16),
                    int(color[2] + color[2], 16),
                    int(color[3] + color[3], 16),
                    int(color[4] + color[4], 16),
                )
            if len(color) == 7:
                return (
                    int(color[1:3], 16),
                    int(color[3:5], 16),
                    int(color[5:6], 16),
                    0xff,
                )
            if len(color) == 9:
                return (
                    int(color[1:3], 16),
                    int(color[3:5], 16),
                    int(color[5:6], 16),
                    int(color[6:8], 16),
                )
        return COLOR_NAME_MAP[color]
    except ValueError:
        return DEFAULT_COLOR
