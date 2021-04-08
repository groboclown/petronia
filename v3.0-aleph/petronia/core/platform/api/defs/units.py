
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

ZERO_SCREEN_POSITION: ScreenPosition = (0, 0,)

# w, h
ScreenSize = Tuple[ScreenUnit, ScreenUnit]
SCREEN_SIZE_WIDTH = 0
SCREEN_SIZE_HEIGHT = 1
SCREEN_SIZE_W = SCREEN_SIZE_WIDTH
SCREEN_SIZE_H = SCREEN_SIZE_HEIGHT

ZERO_SCREEN_SIZE: ScreenSize = (0, 0,)

# x, y, w, h
ScreenArea = Tuple[ScreenUnit, ScreenUnit, ScreenUnit, ScreenUnit]
SCREEN_AREA_X = 0
SCREEN_AREA_Y = 1
SCREEN_AREA_WIDTH = 2
SCREEN_AREA_HEIGHT = 3
SCREEN_AREA_W = SCREEN_AREA_WIDTH
SCREEN_AREA_H = SCREEN_AREA_HEIGHT

ZERO_SCREEN_AREA: ScreenArea = (0, 0, 0, 0,)

# Quarter font unit.
FontQUnit = int

# For native screen dimensions...
NativeScreenUnit = int

# x, y
NativeScreenPosition = Tuple[NativeScreenUnit, NativeScreenUnit]
NATIVE_SCREEN_POSITION_X = 0
NATIVE_SCREEN_POSITION_Y = 1

# width, height
NativeScreenSize = Tuple[NativeScreenUnit, NativeScreenUnit]
NATIVE_SCREEN_SIZE_WIDTH = 0
NATIVE_SCREEN_SIZE_HEIGHT = 1
NATIVE_SCREEN_SIZE_W = NATIVE_SCREEN_SIZE_WIDTH
NATIVE_SCREEN_SIZE_H = NATIVE_SCREEN_SIZE_HEIGHT

# x, y, width, height
NativeScreenArea = Tuple[NativeScreenUnit, NativeScreenUnit, NativeScreenUnit, NativeScreenUnit]
NATIVE_SCREEN_AREA_X = 0
NATIVE_SCREEN_AREA_Y = 1
NATIVE_SCREEN_AREA_WIDTH = 2
NATIVE_SCREEN_AREA_HEIGHT = 3
NATIVE_SCREEN_AREA_W = NATIVE_SCREEN_AREA_WIDTH
NATIVE_SCREEN_AREA_H = NATIVE_SCREEN_AREA_HEIGHT


class ScreenRect:
    """Rectangle display on the screen."""
    __slots__ = ('__x', '__y', '__width', '__height', '__left', '__right', '__top', '__bottom',)

    def __init__(
            self,
            x: ScreenUnit, y: ScreenUnit, width: ScreenUnit, height: ScreenUnit,
            left: ScreenUnit, right: ScreenUnit, top: ScreenUnit, bottom: ScreenUnit
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
    def x(self) -> ScreenUnit:
        return self.__x

    @property
    def y(self) -> ScreenUnit:
        return self.__y

    @property
    def width(self) -> ScreenUnit:
        return self.__width

    @property
    def height(self) -> ScreenUnit:
        return self.__height

    @property
    def left(self) -> ScreenUnit:
        return self.__left

    @property
    def right(self) -> ScreenUnit:
        return self.__right

    @property
    def top(self) -> ScreenUnit:
        return self.__top

    @property
    def bottom(self) -> ScreenUnit:
        return self.__bottom

    def copy(self) -> 'ScreenRect':
        return ScreenRect(
            x=self.__x,
            y=self.__y,
            width=self.__width,
            height=self.__height,
            left=self.__left,
            right=self.__right,
            top=self.__top,
            bottom=self.__bottom
        )
    
    def get_area(self) -> ScreenArea:
        return self.__x, self.__y, self.__width, self.__height

    def __repr__(self) -> str:
        return 'ScreenRect(x={0}, y={1}, w={2}, h={3})'.format(
            self.__x, self.__y, self.__width, self.__height
        )


EMPTY_SCREEN_RECT = ScreenRect(0, 0, 0, 0, 0, 0, 0, 0)
