
"""
A widget that adds an arbitrary space between one side of a component and
another.  Only the first spacer is generally used.
"""

from typing import Optional
from ......base import create_singleton_identity
from ...defs import (
    Color,
    RespondsToAction,
)

COMPONENT_ID_CREATE_SPACER = create_singleton_identity('core.platform.api/spacer')


class SpacerWidget:
    """
    A simple widget with no data.  It injects an alignment space
    between widgets.  The first of these widgets will change the
    alignment, and subsequent ones within the same container will
    be just an additional amount of screen space.
    """
    __slots__ = (
        '__color', '__responds_to',
    )

    def __init__(self, color: Color, responds_to: Optional[RespondsToAction] = None) -> None:
        self.__color = color
        self.__responds_to = responds_to

    @property
    def color(self) -> Color:
        return self.__color

    @property
    def responds_to(self) -> Optional[RespondsToAction]:
        return self.__responds_to
