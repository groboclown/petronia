
"""
Color definitions
"""

from typing import Tuple, Union

# A 0-255 value scheme of colors.
ColorRGBA = Tuple[int, int, int, int]

# A color string is a string definition.  The interpretation of the color
# text is up to the platform.  However, the standard web colors
# (#rrggbb, #rrggbbaa) should be supported.
ColorStr = str

Color = Union[ColorStr, ColorRGBA]
