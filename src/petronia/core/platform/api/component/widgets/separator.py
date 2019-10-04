
"""
Insert a visual separator.  Some platforms may allow for the user to move it.
"""

from typing import Optional
from ......base import create_singleton_identity
from ...defs import (
    FontQUnit,
    Color,
    RespondsToAction,
)

COMPONENT_ID_CREATE_SEPARATOR = create_singleton_identity('core.platform.api/separator')


class SeparatorWidget:
    """
    Simple, no-data separator.  The precise display is up to the platform; the
    platform will determine whether the separator is vertical or horizontal
    based on the container's orientation.
    """

    __slots__ = (
        '__padding', '__fg', '__bg', '__responds_to',

    )

    def __init__(
            self,
            padding: FontQUnit, fg: Color, bg: Optional[Color],
            responds_to: Optional[RespondsToAction] = None
    ) -> None:
        self.__padding = padding
        self.__fg = fg
        self.__bg = bg
        self.__responds_to = responds_to

    @property
    def padding(self) -> FontQUnit:
        return self.__padding

    @property
    def fg(self) -> Color:
        return self.__fg

    @property
    def bg(self) -> Optional[Color]:
        return self.__bg

    @property
    def responds_to(self) -> Optional[RespondsToAction]:
        """All the actions that this widget should send out events when they
        occur."""
        return self.__responds_to
