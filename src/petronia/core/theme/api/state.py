
"""
State definitions of the theme.  This is for the theme itself, and not for the
generated windows.  Those are handled individually by extensions that want to
create them.
"""

from typing import Iterable, Sequence
from ...platform.api import NativeWindowState
from .chrome import ThemeChrome
from .match import WindowMatcher


class WindowMatchChrome:
    __slots__ = (
        '__match', '__chrome',
    )

    def __init__(self, match: WindowMatcher, chrome: ThemeChrome) -> None:
        self.__match = match
        self.__chrome = chrome

    @property
    def match(self) -> WindowMatcher:
        return self.__match

    @property
    def chrome(self) -> ThemeChrome:
        return self.__chrome


class ThemeState:
    __slots__ = (
        '__default', '__matchers',
    )

    def __init__(self, default_chrome: ThemeChrome, matchers: Iterable[WindowMatchChrome]) -> None:
        self.__default = default_chrome
        self.__matchers = tuple(matchers)

    @property
    def default_chrome(self) -> ThemeChrome:
        return self.__default

    @property
    def matchers(self) -> Sequence[WindowMatchChrome]:
        return self.__matchers

    def match_window_properties(self, info: NativeWindowState) -> ThemeChrome:
        for m in self.__matchers:
            if m.match.is_window_property_match(info):
                return m.chrome
        return self.__default
