
"""
Container UI components.  It contains zero or more widgets arranged
according to the container's setup.

Containers themselves do not respond to user input.  If you want an
entire container to respond to, say, mouse clicks, then each child
component will need that added.

For those that come from more standard UI backgrounds, these containers
mix the idea of contained widget layout and holding the widgets.
"""

from typing import Union
from ..defs import (
    Color,
    ScreenUnit,
)


class GridContainer:
    """
    A low-level container that is NxM grid.

    Container UI components.  It contains zero or more widgets arranged
    according to the container's setup.

    This can be used to create toolbars, drop-down menus, dialogs, and other
    elements.  Because a container is not itself a widget, they cannot be
    embedded inside each other.

    Containers use a "grid" layout.  An item inserted into the grid is assumed
    to take up the entire defined area.  Items can take up multiple parts of the
    grid, and they can overlap each other.  Likewise, items will be restricted to
    drawing within the confines of the declared grid size.

    The container size itself is in screen units.
    """
    __slots__ = (
        '__color',
        '__width',
        '__height',
        '__grid_x',
        '__grid_y',
    )

    def __init__(
            self,
            color: Color,
            width: ScreenUnit,
            height: ScreenUnit,
            grid_count_x: int,
            grid_count_y: int
    ) -> None:
        self.__color = color
        self.__width = width
        self.__height = height
        assert grid_count_y >= 0 and grid_count_x >= 0
        self.__grid_x = grid_count_x
        self.__grid_y = grid_count_y

    @property
    def color(self) -> Color:
        return self.__color

    @property
    def width(self) -> ScreenUnit:
        return self.__width

    @property
    def height(self) -> ScreenUnit:
        return self.__height

    @property
    def grid_count_x(self) -> int:
        return self.__grid_x

    @property
    def grid_count_y(self) -> int:
        return self.__grid_y


class FlowContainer:
    """
    A container that has a start and end section, each of which can
    contain any number of widgets.  The widgets will line up one after the
    other.  There is a chance that the two sections will overlap.

    The container can either be vertical or horizontal in orientation.
    """
    __slots__ = (
        '__color',
        '__width',
        '__height',
    )

    def __init__(self, color: Color) -> None:
        self.__color = color

    @property
    def color(self) -> Color:
        return self.__color


Container = Union[GridContainer, FlowContainer]
