
"""
Units for display sizes.
"""

from typing import Tuple

# Pixels according to the screen size measurement.
ScreenUnit = int

# x, y
ScreenPosition = Tuple[ScreenUnit, ScreenUnit]
SCREEN_POSITION_X = 0
SCREEN_POSITION_Y = 1

# w, h
ScreenSize = Tuple[ScreenUnit, ScreenUnit]
SCREEN_SIZE_WIDTH = 0
SCREEN_SIZE_HEIGHT = 1
SCREEN_SIZE_W = SCREEN_SIZE_WIDTH
SCREEN_SIZE_H = SCREEN_SIZE_HEIGHT

# x, y, w, h
ScreenArea = Tuple[ScreenUnit, ScreenUnit, ScreenUnit, ScreenUnit]
SCREEN_AREA_X = 0
SCREEN_AREA_Y = 1
SCREEN_AREA_WIDTH = 2
SCREEN_AREA_HEIGHT = 3
SCREEN_AREA_W = SCREEN_AREA_WIDTH
SCREEN_AREA_H = SCREEN_AREA_HEIGHT

# Quarter font unit.
FontQUnit = int


class ScreenRect:
    """Rectangle display on the screen."""
    __slots__ = ('__x', '__y', '__width', '__height', '__left', '__right', '__top', '__bottom',)

    def __init__(
            self,
            x: int, y: int, width: int, height: int,
            left: int, right: int, top: int, bottom: int
    ) -> None:
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__left = left
        self.__right = right
        self.__top = top
        self.__bottom = bottom

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    @property
    def left(self) -> int:
        return self.__left

    @property
    def right(self) -> int:
        return self.__right

    @property
    def top(self) -> int:
        return self.__top

    @property
    def bottom(self) -> int:
        return self.__bottom
