
"""
Color definitions
"""

from typing import Tuple, Mapping, Union

# A 0-255 value scheme of colors.
ColorRGBA = Tuple[int, int, int, int]
COLOR_RGBA_RED_INDEX = 0
COLOR_RGBA_GREEN_INDEX = 1
COLOR_RGBA_BLUE_INDEX = 2
COLOR_RGBA_ALPHA_INDEX = 3

# A color string is a string definition.  The interpretation of the color
# text is up to the platform.  However, the standard web colors
# (#rrggbb, #rrggbbaa) should be supported.
ColorStr = str

Color = Union[ColorStr, ColorRGBA]


DEFAULT_COLOR: ColorRGBA = (0x80, 0x80, 0x80, 0xff,)
COLOR_NAME_MAP: Mapping[str, ColorRGBA] = {
    'red':     (0xff, 0x00, 0x00, 0xff,),
    'green':   (0xff, 0xff, 0x00, 0xff,),
    'blue':    (0x00, 0x00, 0xff, 0xff,),
    'white':   (0xff, 0xff, 0xff, 0xff,),
    'black':   (0x00, 0x00, 0x00, 0xff,),

    # add more colors here.
}


def color_to_rgba(color: Color) -> ColorRGBA:
    """Converts a color value to an RGBA value."""
    if isinstance(color, ColorStr):
        return color_str_to_rgba(color)
    return color


def color_str_to_rgba(color: ColorStr) -> ColorRGBA:  # pylint:disable=too-many-return-statements
    """Convert a color string into a tuple of colors."""
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
    except (ValueError, KeyError):
        return DEFAULT_COLOR
