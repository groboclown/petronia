
"""
Portals, Containers, and Managers, oh my!
"""

from typing import List, Sequence, Optional, Iterable
from ....aid.std import (
    EventBus,
    ComponentId,
)
from ....core.platform.api import (
    ScreenUnit,
    ScreenArea,
    NativeWindowState,
    WindowMatcher,
)


class Portal:
    """
    Manages zero or more windows within a small area.

    The portal object acts as an intermediary between the layout and the
    owning windows.  The capturing of platform events is done at the higher
    level, as well as the management of the portal position.

    The portal could be optimized to have a single bit of chrome for the area,
    but that won't work for non-sizable windows.  And the theme / platform
    doesn't support that.

    The optional "background" window is shown if no window exists within the
    portal.  It is not returned from the normal "window" functions.
    """

    __slots__ = (
        '__bus',
        '__name',
        '__matchers',
        '__size',
        '__position_favor',
        '_window_cids',
        '__current_index',
        '__background_cid',
    )
    _window_cids: List[ComponentId]

    def __init__(
            self,
            bus: EventBus,
            name: str,
            initial_size: ScreenArea,
            matchers: Iterable[WindowMatcher],
            background: Optional[ComponentId]
    ) -> None:
        self.__bus = bus
        self.__name = name
        self.__matchers = tuple(matchers)
        self.__size = initial_size
        self._window_cids = []
        self.__current_index = 0
        self.__background_cid = background

    def is_match(self, window: NativeWindowState) -> bool:
        """Is the given window information a match for this portal?"""
        for m in self.__matchers:
            if m.is_window_property_match(window):
                return True
        return False

    @property
    def name(self) -> str:
        return self.__name

    @property
    def background_cid(self) -> Optional[ComponentId]:
        return self.__background_cid

    @property
    def area(self) -> ScreenArea:
        return self.__size

    def add_window(self, cid: ComponentId) -> int:
        """
        Add the window to the portal's managed list.  This could be
        a chrome or native window component id.  Returns the added window's
        index.
        """
        raise NotImplementedError()

    def remove_window(self, cid: ComponentId) -> bool:
        """
        Remove the window from the portal's list.  If the window is
        not in the portal's list, then False is returned.
        """
        raise NotImplementedError()

    def set_area(self, new_area_size: ScreenArea) -> None:
        """
        Set the size of this portal.  The implementation passes this
        change on to the child windows.

        :param new_area_size:
        :return:
        """
        raise NotImplementedError()

    def __getitem__(self, i: int) -> ComponentId:
        return self._window_cids[i]

    def get_windows(self) -> Sequence[ComponentId]:
        """
        Return the list of registered window CIDs (either chrome or window).
        Does not include the background window.
        """
        return tuple(self._window_cids)

    def __len__(self) -> int:
        return self.get_window_count()

    def get_window_count(self) -> int:
        """The number of internal windows, not counting the background window."""
        return len(self._window_cids)

    def set_visible_window_index(self, index: int) -> None:
        """
        Sets the window at the given internal index as the now-visible
        window within this portal.  If the index is out of range, it will
        be mapped (through modulo and absolute value) to a valid number.
        """
        if len(self._window_cids) <= 0:
            return
        raise NotImplementedError()

    def change_visible_window_index(self, delta_index: int) -> None:
        """
        Same as `set_visible_window_index`, but changes the index by
        a number based on the current index.

        :param delta_index:
        :return:
        """
        self.set_visible_window_index(self.__current_index + delta_index)

    def set_focus(self, has_focus: bool) -> None:
        """
        Set the top window as having the focus, or losing the focus.
        :return:
        """
        raise NotImplementedError()
