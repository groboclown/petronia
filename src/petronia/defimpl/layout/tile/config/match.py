
"""
Configuration to match windows to named portals.
"""

from typing import Optional
from .....core.platform.api import (
    WindowMatcher,
)


class MatchWindowToPortal:
    """
    Matches a window to a portal through the different named aspects of the
    window and the portal.
    """

    __slots__ = (
        '__window_matcher',
        '__portal_name',
        '__position',
    )

    def __init__(
            self,
            window_matcher: WindowMatcher,
            portal_name: str,
            position: Optional[str]
    ) -> None:
        self.__window_matcher = window_matcher
        self.__portal_name = portal_name
        self.__position = position

    @property
    def window_matcher(self) -> WindowMatcher:
        return self.__window_matcher

    @property
    def portal_name(self) -> str:
        return self.__portal_name

    @property
    def position(self) -> Optional[str]:
        return self.__position
