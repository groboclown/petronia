
"""
Decorations around a native window.  Defined as widgets for each side and
corner around the window.
"""

from typing import Iterable, Optional
from ..defs import RespondsToAction
from .....base import (
    create_singleton_identity,
    ComponentId,
)
from .widgets import Widget

COMPONENT_ID_CREATE_CHROME = create_singleton_identity('core.platform.api/chrome')


class Chrome:
    """
    Describes the chrome outline of a window.
    """
    __slots__ = ('__owner', '__n', '__e', '__s', '__w', '__ne', '__nw', '__se', '__sw')

    def __init__(
            self,
            owning_window_id: ComponentId,
            n: Optional[Widget], e: Optional[Widget], s: Optional[Widget], w: Optional[Widget],
            ne: Optional[Widget], nw: Optional[Widget], se: Optional[Widget], sw: Optional[Widget]
    ) -> None:
        self.__owner = owning_window_id
        self.__n = n
        self.__e = e
        self.__s = s
        self.__w = w
        self.__ne = ne
        self.__nw = nw
        self.__se = se
        self.__sw = sw

    @property
    def owning_window_id(self) -> ComponentId:
        return self.__owner

    @property
    def n(self) -> Optional[Widget]:
        return self.__n

    @property
    def e(self) -> Optional[Widget]:
        return self.__e

    @property
    def s(self) -> Optional[Widget]:
        return self.__s

    @property
    def w(self) -> Optional[Widget]:
        return self.__w

    @property
    def ne(self) -> Optional[Widget]:
        return self.__ne

    @property
    def nw(self) -> Optional[Widget]:
        return self.__nw

    @property
    def se(self) -> Optional[Widget]:
        return self.__se

    @property
    def sw(self) -> Optional[Widget]:
        return self.__sw
