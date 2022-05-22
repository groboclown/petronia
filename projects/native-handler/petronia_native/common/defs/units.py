
"""
Units for display sizes.
"""

from typing import Tuple, NewType, Any, cast

# Pixels according to the screen size measurement.
ScreenUnit = NewType('ScreenUnit', int)
ZERO_SCREEN_UNIT = cast(ScreenUnit, 0)

# x, y
ScreenPosition = Tuple[ScreenUnit, ScreenUnit]
SCREEN_POSITION_X = 0
SCREEN_POSITION_Y = 1

ZERO_SCREEN_POSITION: ScreenPosition = (ZERO_SCREEN_UNIT, ZERO_SCREEN_UNIT,)

# w, h
ScreenSize = Tuple[ScreenUnit, ScreenUnit]
SCREEN_SIZE_WIDTH = 0
SCREEN_SIZE_HEIGHT = 1
SCREEN_SIZE_W = SCREEN_SIZE_WIDTH
SCREEN_SIZE_H = SCREEN_SIZE_HEIGHT

ZERO_SCREEN_SIZE: ScreenSize = (ZERO_SCREEN_UNIT, ZERO_SCREEN_UNIT,)

# x, y, w, h
ScreenArea = Tuple[ScreenUnit, ScreenUnit, ScreenUnit, ScreenUnit]
SCREEN_AREA_X = 0
SCREEN_AREA_Y = 1
SCREEN_AREA_WIDTH = 2
SCREEN_AREA_HEIGHT = 3
SCREEN_AREA_W = SCREEN_AREA_WIDTH
SCREEN_AREA_H = SCREEN_AREA_HEIGHT

ZERO_SCREEN_AREA: ScreenArea = (
    ZERO_SCREEN_UNIT, ZERO_SCREEN_UNIT, ZERO_SCREEN_UNIT, ZERO_SCREEN_UNIT,
)

# For native screen dimensions...
MonitorUnit = NewType('MonitorUnit', int)
ZERO_MONITOR_UNIT = cast(MonitorUnit, 0)

# identifier, x, y
MonitorPosition = Tuple[int, MonitorUnit, MonitorUnit]
MONITOR_POSITION_MONITOR_IDENTIFIER = 0
MONITOR_POSITION_X = 1
MONITOR_POSITION_Y = 2

# width, height
MonitorSize = Tuple[MonitorUnit, MonitorUnit]
MONITOR_SIZE_WIDTH = 0
MONITOR_SIZE_HEIGHT = 1
MONITOR_SIZE_W = MONITOR_SIZE_WIDTH
MONITOR_SIZE_H = MONITOR_SIZE_HEIGHT

# x, y, width, height
MonitorArea = Tuple[int, MonitorUnit, MonitorUnit, MonitorUnit, MonitorUnit]
MONITOR_AREA_MONITOR_INDEX = 0
MONITOR_AREA_X = 1
MONITOR_AREA_Y = 2
MONITOR_AREA_WIDTH = 3
MONITOR_AREA_HEIGHT = 4
MONITOR_AREA_W = MONITOR_AREA_WIDTH
MONITOR_AREA_H = MONITOR_AREA_HEIGHT


class ScreenRect:  # pylint:disable=too-many-instance-attributes
    """Rectangle display on the screen."""
    __slots__ = ('__x', '__y', '__width', '__height', '__left', '__right', '__top', '__bottom',)

    def __init__(  # pylint:disable=too-many-arguments, invalid-name
            self, *,
            x: ScreenUnit, y: ScreenUnit, width: ScreenUnit, height: ScreenUnit,
            left: ScreenUnit, right: ScreenUnit, top: ScreenUnit, bottom: ScreenUnit,
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
    def x(self) -> ScreenUnit:  # pylint:disable=invalid-name
        """x position"""
        return self.__x

    @property
    def y(self) -> ScreenUnit:  # pylint:disable=invalid-name
        """y position"""
        return self.__y

    @property
    def width(self) -> ScreenUnit:
        """width"""
        return self.__width

    @property
    def height(self) -> ScreenUnit:
        """height"""
        return self.__height

    @property
    def left(self) -> ScreenUnit:
        """left"""
        return self.__left

    @property
    def right(self) -> ScreenUnit:
        """right"""
        return self.__right

    @property
    def top(self) -> ScreenUnit:
        """top"""
        return self.__top

    @property
    def bottom(self) -> ScreenUnit:
        """bottom"""
        return self.__bottom

    def get_area(self) -> ScreenArea:
        """get as an area"""
        return self.__x, self.__y, self.__width, self.__height

    @staticmethod
    def from_border(
            left: int,
            right: int,
            top: int,
            bottom: int,
    ) -> 'ScreenRect':
        """Create a ScreenRect from the border position."""
        return ScreenRect(
            x=cast(ScreenUnit, left), y=cast(ScreenUnit, top),
            width=cast(ScreenUnit, right - left + 1), height=cast(ScreenUnit, bottom - top + 1),
            left=cast(ScreenUnit, left), right=cast(ScreenUnit, right),
            top=cast(ScreenUnit, top), bottom=cast(ScreenUnit, bottom),
        )

    def __repr__(self) -> str:
        return f'ScreenRect(x={self.__x}, y={self.__y}, w={self.__width}, h={self.__height})'

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ScreenRect):
            return False
        return (
            self.__x == other.x
            and self.__y == other.y
            and self.__width == other.width
            and self.__height == other.height
            # the other values SHOULD be constructed the same.
        )

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return self.__x + self.__y + self.__width + self.__height


EMPTY_SCREEN_RECT = ScreenRect(
    x=ZERO_SCREEN_UNIT, y=ZERO_SCREEN_UNIT, width=ZERO_SCREEN_UNIT, height=ZERO_SCREEN_UNIT,
    left=ZERO_SCREEN_UNIT, right=ZERO_SCREEN_UNIT, top=ZERO_SCREEN_UNIT, bottom=ZERO_SCREEN_UNIT,
)


OsScreenPosition = Tuple[int, int]
OS_SCREEN_POSITION_X = 0
OS_SCREEN_POSITION_Y = 1


OsScreenSize = Tuple[int, int]
OS_SCREEN_SIZE_WIDTH = 0
OS_SCREEN_SIZE_HEIGHT = 1


class OsScreenRect:  # pylint:disable=too-many-arguments,too-many-instance-attributes
    """Native screen sizes for a rectangular region on the screen.
    This may be in a scaled space or native monitor pixels; that's up to
    the native rendering tools to decide.

    Use of this structure should be kept entirely internal."""
    __slots__ = ('__x', '__y', '__width', '__height', '__top', '__bottom', '__left', '__right')

    def __init__(
            self, *,
            x: int = 0,  # pylint:disable=invalid-name
            y: int = 0,  # pylint:disable=invalid-name
            width: int = 0,
            height: int = 0,
            left: int = 0,
            right: int = 0,
            top: int = 0,
            bottom: int = 0,
    ) -> None:
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__top = top
        self.__bottom = bottom
        self.__left = left
        self.__right = right

    @property
    def x(self) -> int:  # pylint:disable=invalid-name
        """upper-left x position"""
        return self.__x

    @property
    def y(self) -> int:  # pylint:disable=invalid-name
        """upper-left y position"""
        return self.__y

    @property
    def width(self) -> int:
        """number of pixels wide (x-axis)"""
        return self.__width

    @property
    def height(self) -> int:
        """number of pixels high (y-axis)"""
        return self.__height

    @property
    def left(self) -> int:
        """left-side coordinate"""
        return self.__left

    @property
    def right(self) -> int:
        """right-side coordinate"""
        return self.__right

    @property
    def top(self) -> int:
        """top-side coordinate"""
        return self.__top

    @property
    def bottom(self) -> int:
        """bottom-side coordinate"""
        return self.__bottom

    @staticmethod
    def from_coordinates(x1: int, y1: int, x2: int, y2: int) -> 'OsScreenRect':  # pylint:disable=invalid-name
        """Creates a structure based on (x, y) -> (x, y) screen coordinates."""
        min_x = min(x1, x2)
        min_y = min(y1, y2)
        max_x = max(x1, x2)
        max_y = max(y1, y2)
        return OsScreenRect(
            x=min_x, y=min_y, width=max_x - min_x,  height=max_y - min_y,
            left=min_x, right=max_x, top=min_y, bottom=max_y,
        )

    @staticmethod
    def from_size(x: int, y: int, width: int, height: int) -> 'OsScreenRect':  # pylint:disable=invalid-name
        """Creates a structure based on the upper-left corner + size.
        This will always make a visible rectangle; the smallest it can be is 1x1."""
        r_w = max(1, width)
        r_h = max(1, height)
        return OsScreenRect(
            x=x, y=y, width=r_w, height=r_h,
            left=x, right=x + r_w, top=y, bottom=y + r_h,
        )

    @staticmethod
    def from_border(left: int, right: int, top: int, bottom: int) -> 'OsScreenRect':
        """Creates a structure based on the border positions."""
        # This is based on experiments from returned values on Windows.
        return OsScreenRect(
            x=left,
            y=top,
            width=right - left,
            height=bottom - top,
            left=left,
            right=right,
            top=top,
            bottom=bottom,
        )

    def __repr__(self) -> str:
        return (
            f'OsScreenRect('
            f'left={self.left}, right={self.right}, top={self.top}, bottom={self.bottom}'
            # f', x={self.x}, y={self.y}, w={self.width}, h={self.height}'
            f')'
        )

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, OsScreenRect):
            return False
        return (
            self.__x == other.x
            and self.__y == other.y
            and self.__width == other.width
            and self.__height == other.height
            # The others should be the same if this was constructed correctly.
        )

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)
