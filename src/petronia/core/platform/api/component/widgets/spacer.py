
"""
A widget that adds an arbitrary space between one side of a component and
another.  Only the first spacer is generally used.
"""
from ......base import create_singleton_identity
from ...defs import Color

COMPONENT_ID_CREATE_SPACER = create_singleton_identity('core.platform.api/spacer')


class SpacerWidget:
    """
    A simple widget with no data.  It injects an alignment space
    between widgets.  The first of these widgets will change the
    alignment, and subsequent ones within the same container will
    be just an additional amount of screen space.
    """
    __slots__ = (
        '__color',
    )

    def __init__(self, color: Color) -> None:
        self.__color = color

    @property
    def color(self) -> Color:
        return self.__color
