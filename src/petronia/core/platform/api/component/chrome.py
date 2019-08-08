
"""
Decorations around a native window.  This includes a possible title bar.
"""

from typing import Iterable, Optional
from ..defs import RespondsToAction
from .....base import (
    create_singleton_identity,
    ComponentId,
)

COMPONENT_ID_CREATE_CHROME = create_singleton_identity('core.platform.api/chrome')


class Chrome:
    """
    Describes the chrome outline of a window.

    It splits the chrome into five sections, each can be defined
    independently of the others.  The toolbars are added after creation
    of the chrome.

    * n, s: The horizontally-oriented toolbars specific to this window.
    * e, w: The vertically-oriented toolbars.  If both horizontal and vertical
        toolbars are defined, then the vertical bars are "tucked inside" the
        horizontal ones - the horizontal spans across the entire horizontal
        width, while the vertical ones are inside the border + horizontal
        bars.
    * border: the border styling has a default theme style, but this can be
        altered.  This also allows for setting the "grab" and "move"
        response events.  The border movement is not controlled by the theme
        or platform.
    """
    __slots__ = ('__owner', '__n', '__e', '__s', '__w', '__border',)

    def __init__(
            self,
            owning_window_id: ComponentId,
            border_style: Optional[str] = None,
            border_responds_to: Optional[Iterable[RespondsToAction]] = None
    ) -> None:
        pass
