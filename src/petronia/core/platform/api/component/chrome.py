
"""
Decorations around a native window.  Defined as widgets for each side and
corner around the window.  The chrome itself does not react to user input,
but the attached widgets can.
"""

from typing import Optional
from .....base import (
    create_singleton_identity,
    ComponentId,
)
from .widgets import Widget

COMPONENT_ID_CREATE_CHROME = create_singleton_identity('core.platform.api/chrome')


class Chrome:
    """
    Describes the chrome outline of a window.

    To add the chrome to a window, you must trigger the
    RequestCreateChromeWrapperEvent.  This will cause the platform to add the
    new chrome around the window, and requests to the window will affect the
    chrome.

    To add widgets to the chrome, you must first provide a new component ID for
    the area for the widget to live, then send standard widget creation lifecycle
    calls, using the chrome's border area as the parent.
    """
    __slots__ = ('__owner', '__n', '__e', '__s', '__w', '__ne', '__nw', '__se', '__sw')

    def __init__(
            self,
            owning_window_id: ComponentId,
            n: Optional[ComponentId] = None, e: Optional[ComponentId] = None,
            s: Optional[ComponentId] = None, w: Optional[ComponentId] = None,
            ne: Optional[ComponentId] = None, nw: Optional[ComponentId] = None,
            se: Optional[ComponentId] = None, sw: Optional[ComponentId] = None
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
    def n(self) -> Optional[ComponentId]:
        return self.__n

    @property
    def e(self) -> Optional[ComponentId]:
        return self.__e

    @property
    def s(self) -> Optional[ComponentId]:
        return self.__s

    @property
    def w(self) -> Optional[ComponentId]:
        return self.__w

    @property
    def ne(self) -> Optional[ComponentId]:
        return self.__ne

    @property
    def nw(self) -> Optional[ComponentId]:
        return self.__nw

    @property
    def se(self) -> Optional[ComponentId]:
        return self.__se

    @property
    def sw(self) -> Optional[ComponentId]:
        return self.__sw
