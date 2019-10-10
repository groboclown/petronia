
"""
Definitions for matching window properties.
"""

from typing import Pattern, Tuple, Optional
import re
from .state import NativeWindowState
from .....aid.std import (
    create_user_error,
    ErrorReport,
)


WINDOW_MATCH_EXACT = 0
WINDOW_MATCH_PART = 1
WINDOW_MATCH_GLOB = 2
WINDOW_MATCH_REGEX = 3
WINDOW_MATCHES = (
    WINDOW_MATCH_EXACT,
    WINDOW_MATCH_PART,
    WINDOW_MATCH_GLOB,
    WINDOW_MATCH_REGEX,
)


class WindowMatcher:
    """
    Standard mechanism for matching a window property set
    value.
    """
    __slots__ = (
        '__key', '__match', '__kind', '__re', '__problem'
    )

    def __init__(self, key: str, match: str, kind: int) -> None:
        assert kind in WINDOW_MATCHES
        self.__key = key
        self.__kind = kind
        self.__re, self.__match, self.__problem = _get_re(match, kind)

    @property
    def key(self) -> str:
        return self.__key

    @property
    def match(self) -> Optional[str]:
        return self.__match

    @property
    def kind(self) -> int:
        return self.__kind

    def is_window_property_match(self, info: NativeWindowState) -> bool:
        """Does the property in the info object match this given value?"""
        if self.__key not in info.names:
            return False
        val = info.names[self.__key]
        if self.__re:
            return self.__re.match(val) is not None
        if self.__kind == WINDOW_MATCH_PART and self.__match:
            return self.__match in val.lower()
        return self.__match == val


def _get_re(match: str, kind: int) -> Tuple[Optional[Pattern[str]], Optional[str], Optional[ErrorReport]]:
    if kind == WINDOW_MATCH_REGEX:
        try:
            return re.compile(match, re.IGNORECASE), None, None,
        except ValueError or TypeError as e:
            return (None, match.lower(), create_user_error(
                WindowMatcher,
                'invalid regular expression {error}',
                error=e
            ))
    if kind == WINDOW_MATCH_GLOB:
        mt = re.escape(match).replace('\\*', '.*?').replace('\\?', '.')
        return re.compile(mt, re.IGNORECASE), None, None
    prob = (
        create_user_error(WindowMatcher, 'Invalid `kind` value {kind}', kind=kind)
        if kind not in WINDOW_MATCHES
        else None
    )
    if kind == WINDOW_MATCH_PART:
        match = match.lower()
    return None, match, prob
