
"""
Portals, Containers, and Managers, oh my!
"""

from typing import List, Sequence, Optional, Iterable
from ....aid.std import (
    ComponentId,
)
from ....core.platform.api import (
    ScreenArea,
    NativeWindowState,
    WindowMatcher,
    SCREEN_AREA_X,
    SCREEN_AREA_Y,
    SCREEN_AREA_W,
    SCREEN_AREA_H,
)


# If it's restricted, then the size cannot go beyond the bound.
POSITION_FAVOR_MASK_RESTRICT_WIDTH = 0X01
POSITION_FAVOR_MASK_RESTRICT_HEIGHT = 0X02
POSITION_FAVOR_MASK_RESTRICT_AREA = POSITION_FAVOR_MASK_RESTRICT_WIDTH | POSITION_FAVOR_MASK_RESTRICT_HEIGHT
POSITION_FAVOR_MASK_ALIGN_N = 0X04
POSITION_FAVOR_MASK_ALIGN_S = 0X08
POSITION_FAVOR_MASK_ALIGN_E = 0X10
POSITION_FAVOR_MASK_ALIGN_W = 0X20
POSITION_FAVOR_FILL = (
        POSITION_FAVOR_MASK_ALIGN_N | POSITION_FAVOR_MASK_ALIGN_E |
        POSITION_FAVOR_MASK_ALIGN_E | POSITION_FAVOR_MASK_ALIGN_W
)
POSITION_FAVOR_N_EDGE = POSITION_FAVOR_MASK_ALIGN_N | POSITION_FAVOR_MASK_ALIGN_E | POSITION_FAVOR_MASK_ALIGN_W
POSITION_FAVOR_E_EDGE = POSITION_FAVOR_MASK_ALIGN_E | POSITION_FAVOR_MASK_ALIGN_N | POSITION_FAVOR_MASK_ALIGN_S
POSITION_FAVOR_S_EDGE = POSITION_FAVOR_MASK_ALIGN_S | POSITION_FAVOR_MASK_ALIGN_E | POSITION_FAVOR_MASK_ALIGN_W
POSITION_FAVOR_W_EDGE = POSITION_FAVOR_MASK_ALIGN_W | POSITION_FAVOR_MASK_ALIGN_N | POSITION_FAVOR_MASK_ALIGN_S
POSITION_FAVOR_NE = POSITION_FAVOR_MASK_ALIGN_N | POSITION_FAVOR_MASK_ALIGN_E
POSITION_FAVOR_NW = POSITION_FAVOR_MASK_ALIGN_N | POSITION_FAVOR_MASK_ALIGN_W
POSITION_FAVOR_SE = POSITION_FAVOR_MASK_ALIGN_S | POSITION_FAVOR_MASK_ALIGN_E
POSITION_FAVOR_SW = POSITION_FAVOR_MASK_ALIGN_S | POSITION_FAVOR_MASK_ALIGN_W
POSITION_FAVOR_RESTRICTED_N_EDGE = POSITION_FAVOR_N_EDGE | POSITION_FAVOR_MASK_RESTRICT_HEIGHT
POSITION_FAVOR_RESTRICTED_S_EDGE = POSITION_FAVOR_S_EDGE | POSITION_FAVOR_MASK_RESTRICT_HEIGHT
POSITION_FAVOR_RESTRICTED_E_EDGE = POSITION_FAVOR_E_EDGE | POSITION_FAVOR_MASK_RESTRICT_WIDTH
POSITION_FAVOR_RESTRICTED_W_EDGE = POSITION_FAVOR_W_EDGE | POSITION_FAVOR_MASK_RESTRICT_WIDTH
POSITION_FAVOR_RESTRICTED_NE = POSITION_FAVOR_NE | POSITION_FAVOR_MASK_RESTRICT_AREA
POSITION_FAVOR_RESTRICTED_NW = POSITION_FAVOR_NW | POSITION_FAVOR_MASK_RESTRICT_AREA
POSITION_FAVOR_RESTRICTED_SE = POSITION_FAVOR_SE | POSITION_FAVOR_MASK_RESTRICT_AREA
POSITION_FAVOR_RESTRICTED_SW = POSITION_FAVOR_SW | POSITION_FAVOR_MASK_RESTRICT_AREA
POSITION_FAVOR_ALL = (
    POSITION_FAVOR_FILL,
    POSITION_FAVOR_N_EDGE,
    POSITION_FAVOR_E_EDGE,
    POSITION_FAVOR_S_EDGE,
    POSITION_FAVOR_W_EDGE,
    POSITION_FAVOR_NE,
    POSITION_FAVOR_SE,
    POSITION_FAVOR_NW,
    POSITION_FAVOR_SW,
    POSITION_FAVOR_RESTRICTED_N_EDGE,
    POSITION_FAVOR_RESTRICTED_E_EDGE,
    POSITION_FAVOR_RESTRICTED_S_EDGE,
    POSITION_FAVOR_RESTRICTED_W_EDGE,
    POSITION_FAVOR_RESTRICTED_NE,
    POSITION_FAVOR_RESTRICTED_SE,
    POSITION_FAVOR_RESTRICTED_NW,
    POSITION_FAVOR_RESTRICTED_SW,
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
        '__name',
        '__matchers',
        '__size',
        '_window_cids',
        '__current_index',
        '__background_cid',
    )
    _window_cids: List[ComponentId]

    def __init__(
            self,
            name: str,
            initial_size: ScreenArea,
            matchers: Iterable[WindowMatcher],
            background: Optional[ComponentId] = None,
    ) -> None:
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

    def get_area(self) -> ScreenArea:
        # A function, not a property, because of the explicit "set_area" call.
        return self.__size

    def set_area(self, new_area_size: ScreenArea) -> None:
        """
        Set the size of this portal.  The implementation passes this
        change on to the child windows.

        :param new_area_size:
        :return:
        """
        raise NotImplementedError()

    def get_window_position(self, window_size: ScreenArea, position_favor: int) -> ScreenArea:
        assert position_favor in POSITION_FAVOR_ALL
        x = window_size[SCREEN_AREA_X]
        y = window_size[SCREEN_AREA_Y]
        w = window_size[SCREEN_AREA_W]
        h = window_size[SCREEN_AREA_H]

        if (position_favor & POSITION_FAVOR_MASK_RESTRICT_WIDTH) != 0:
            w = min(self.__size[SCREEN_AREA_W], w)
        if (position_favor & POSITION_FAVOR_MASK_RESTRICT_HEIGHT) != 0:
            h = min(self.__size[SCREEN_AREA_H], h)

        if (position_favor & POSITION_FAVOR_MASK_ALIGN_E) != 0:
            x = self.__size[SCREEN_AREA_X]
            if (position_favor & POSITION_FAVOR_MASK_ALIGN_W) != 0:
                w = self.__size[SCREEN_AREA_W]
        elif (position_favor & POSITION_FAVOR_MASK_ALIGN_W) != 0:
            x = self.__size[SCREEN_AREA_X] + self.__size[SCREEN_AREA_W] - w

        if (position_favor & POSITION_FAVOR_MASK_ALIGN_N) != 0:
            y = self.__size[SCREEN_AREA_Y]
            if (position_favor & POSITION_FAVOR_MASK_ALIGN_S) != 0:
                h = self.__size[SCREEN_AREA_H]
        elif (position_favor & POSITION_FAVOR_MASK_ALIGN_S) != 0:
            y = self.__size[SCREEN_AREA_Y] + self.__size[SCREEN_AREA_H] - h

        return x, y, w, h

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

    def __repr__(self) -> str:
        return (
            'Portal(name={name}, size={size}, current={current}, '
            'background={background}, windows={windows})').format(
            name=repr(self.__name),
            size=repr(self.__size),
            current=repr(self.__current_index),
            background=repr(self.__background_cid),
            windows=repr(self._window_cids)
        )
