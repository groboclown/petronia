
"""
The dressing around a window.

There's the border description (sides + corners), each of which can have mouse
interaction for moving or resizing windows.  What does the mouse action do?
It will need to be configurable (the layout needs to handle the interaction;
it triggers an event).

Borders themselves can have dynamic content.  The title and icon for the
window, sure, and the maximize/minimize/close buttons, yes, but why not
the CPU and memory usage of the program?  The executable that launched the
window?  This is all under the perview of the layout, but can be extended
by other extensions.  Say, an extension that adds the CPU usage.

Each corner and edge that's drawable generates a new component that can
have widgets attached to it.  Some of the basic things you'd expect are
defined by the basic theme.
"""

from typing import Mapping, Optional, Union
from ...platform.api.defs import (
    Color,
)


class ThemeBorderSide:
    """
    Description of how to draw a border.  Borders that are not specified
    are not drawn.  Any widget added to a border will be placed between the
    window contents and the border.
    """
    __slots__ = (
        '__width',
        '__color',
        '__cursor',
        '__allow_drag',
    )

    def __init__(
            self, width: int, color: Color,
            cursor: str,
            allow_drag: bool
    ) -> None:
        self.__width = width
        self.__color = color
        self.__cursor = cursor
        self.__allow_drag = allow_drag

    @property
    def width(self) -> int:
        return self.__width

    @property
    def color(self) -> Color:
        return self.__color

    @property
    def cursor(self) -> str:
        return self.__cursor

    @property
    def allow_drag(self) -> bool:
        return self.__allow_drag


class ThemeBorder:
    __slots__ = (
        '__n', '__e', '__s', '__w',
        '__ne', '__nw', '__se', '__sw',
    )

    def __init__(
            self,
            n: Optional[ThemeBorderSide],
            e: Optional[ThemeBorderSide],
            s: Optional[ThemeBorderSide],
            w: Optional[ThemeBorderSide],
            ne: Optional[ThemeBorderSide],
            nw: Optional[ThemeBorderSide],
            se: Optional[ThemeBorderSide],
            sw: Optional[ThemeBorderSide]
    ) -> None:
        self.__n = n
        self.__e = e
        self.__s = s
        self.__w = w
        self.__ne = ne
        self.__nw = nw
        self.__se = se
        self.__sw = sw

    @property
    def n(self) -> Optional[ThemeBorderSide]:
        return self.__n

    @property
    def e(self) -> Optional[ThemeBorderSide]:
        return self.__e

    @property
    def s(self) -> Optional[ThemeBorderSide]:
        return self.__s

    @property
    def w(self) -> Optional[ThemeBorderSide]:
        return self.__w

    @property
    def ne(self) -> Optional[ThemeBorderSide]:
        return self.__ne

    @property
    def nw(self) -> Optional[ThemeBorderSide]:
        return self.__nw

    @property
    def se(self) -> Optional[ThemeBorderSide]:
        return self.__se

    @property
    def sw(self) -> Optional[ThemeBorderSide]:
        return self.__sw


class ThemeChrome:
    __slots__ = (
        '__border',
        '__style',
    )

    def __init__(
            self,
            border: ThemeBorder,
            style: Mapping[str, Union[str, bool, float]]
    ) -> None:
        self.__border = border
        self.__style = style

    @property
    def border(self) -> ThemeBorder:
        return self.__border

    @property
    def style(self) -> Mapping[str, Union[str, bool, float]]:
        return self.__style
