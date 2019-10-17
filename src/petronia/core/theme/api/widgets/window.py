
"""
Theme-level widgets, which are a higher-level abstraction on top of the
low-level platform api.
"""

from ....platform.api.defs import (
    TextBiDi,
    TextDisplay,
    TextRotation,
    TextAlignment,
)


class WindowTitle:
    """
    How to show the window's title text.

    TODO this might be part of a dynamic widget, rather than directly
        described by the window itself.
    """

    __slots__ = (
        '__display',
        '__bidi',
        '__alignment',
        '__rotation',
    )

    def __init__(
            self,
            display: TextDisplay,
            bidi: TextBiDi,
            align: TextAlignment,
            rot: TextRotation
    ) -> None:
        self.__display = display
        self.__bidi = bidi
        self.__alignment = align
        self.__rotation = rot
