
"""
Configuration to match windows to named portals.
"""

from typing import Sequence, Iterable, Optional
from .....core.platform.api import (
    WindowMatcher,
)


class MatchWindowToPortal:
    """
    Matches a window to a portal through the different named aspects of the
    window and the portal.  It also defines whether the window is resized or
    not.
    """

    __slots__ = (
        '__window_matchers',
        '__portal_name',
        '__position',
    )

    def __init__(
            self,
            window_matchers: Iterable[WindowMatcher],
            portal_name: Optional[str],
            position: Optional[str]
    ) -> None:
        self.__window_matchers = tuple(window_matchers)
        self.__portal_name = portal_name
        self.__position = position

    @property
    def window_matchers(self) -> Sequence[WindowMatcher]:
        return self.__window_matchers

    @property
    def portal_name(self) -> Optional[str]:
        """
        name of the portal into which the window is placed.

        :return:
        """
        return self.__portal_name

    @property
    def position(self) -> Optional[str]:
        """
        Valid values:
            ne, nw, sw, se:
                Don't resize the window, and align it to a corner.
                E corners aligns the E side of the window with the E edge of the portal,
                and so with the W corners.

            n, s, e, w:
                Align the specified edge with the same edge of the window,
                and resize the window along that edge.  i.e. `n` will cause
                the window to be resized the full width of the portal, but will not be
                resized along the vertical, so that the n edge of the window is aligned with
                the n edge of the portal, and the window takes up the whole n edge.

            None:
                The window is resized to fit the portal

        :return:
        """
        return self.__position
