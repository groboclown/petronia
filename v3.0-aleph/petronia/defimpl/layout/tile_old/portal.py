
"""
Portals, Containers, and Managers, oh my!
"""

from typing import List, Tuple, Sequence, Optional, Iterable
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


class PortalWindowInfo:
    """Information about a window within a portal."""
    __slots__ = ('__cid', '__base_area', '__favor',)

    def __init__(self, cid: ComponentId, base_area: ScreenArea, position_favor: int) -> None:
        assert position_favor in POSITION_FAVOR_ALL
        self.__cid = cid
        self.__base_area = base_area
        self.__favor = position_favor

    @property
    def cid(self) -> ComponentId:
        return self.__cid

    @property
    def base_area(self) -> ScreenArea:
        return self.__base_area

    @property
    def position_favor(self) -> int:
        return self.__favor

    def set_position_favor(self, position_favor: int) -> None:
        assert position_favor in POSITION_FAVOR_ALL
        self.__favor = position_favor

    def __repr__(self) -> str:
        return "PortalWindowInfo(cid={0}, base_area={1}, position_favor={2})".format(
            repr(self.__cid),
            repr(self.__base_area),
            repr(self.__favor)
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

    This is not thread safe.
    """

    __slots__ = (
        '_cid',
        '__name',
        '__matchers',
        '__size',
        '_windows',
        '__window_favor',
        '__current_index',
        '__background_cid',
    )
    _windows: List[PortalWindowInfo]
    _cid: Optional[ComponentId]

    def __init__(
            self,
            name: str,
            initial_size: ScreenArea,
            matchers: Iterable[WindowMatcher],
            default_position: int,
            background: Optional[ComponentId] = None,
    ) -> None:
        assert default_position in POSITION_FAVOR_ALL
        self._cid = None
        self.__name = name
        self.__matchers = tuple(matchers)
        self.__size = initial_size
        self.__window_favor = default_position
        self._windows = []
        self.__current_index = 0
        self.__background_cid = background

    def is_match(self, window: NativeWindowState) -> bool:
        """Is the given window information a match for this portal?"""

        # Matchers are read-only, so no lock is required.
        for m in self.__matchers:
            if m.is_window_property_match(window):
                return True
        return False

    @property
    def default_position(self) -> int:
        return self.__window_favor

    def get_cid(self) -> Optional[ComponentId]:
        return self._cid

    def set_cid(self, cid: ComponentId) -> None:
        # TODO use validation API
        assert self._cid is None
        self._cid = cid

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_background_cid(self) -> Optional[ComponentId]:
        return self.__background_cid

    def set_background_cid(self, cid: Optional[ComponentId]) -> None:
        """Set the background component ID.  This might be a picture, or portal chrome, or any number
        of other things."""
        self.__background_cid = cid

    def add_window(
            self, cid: ComponentId, base_area: ScreenArea, position_favor: Optional[int] = None
    ) -> Tuple[int, ScreenArea]:
        """
        Add the window to the portal's managed list.  This could be
        a chrome or native window component id.  Returns the added window's
        index and new location.  The new window is ONLY marked as being the
        active window if and only if there was no window in the portal previously.
        """
        pf: int = self.__window_favor if position_favor is None else position_favor
        pwi = PortalWindowInfo(cid, base_area, pf)

        index = len(self._windows)
        self._windows.append(pwi)
        assert self._windows[index] == pwi

        # should be true, but just to be sure...
        self.__current_index = self.__current_index % len(self._windows)

        area = get_position(self.__size, base_area, pf)
        return index, area

    def remove_window(self, cid: ComponentId) -> Optional[PortalWindowInfo]:
        """
        Remove the window from the portal's list.  If the window is
        not in the portal's list, then None is returned.  The
        active window will only be adjusted if the removed window was
        the active window.
        """
        for index in range(len(self._windows)):
            if self._windows[index].cid == cid:
                pwi = self._windows[index]
                del self._windows[index]
                if self.__current_index >= index:
                    self.__current_index = max(0, self.__current_index - 1)
                return pwi
        return None

    def get_area(self) -> ScreenArea:
        # A function, not a property, because of the explicit "set_area" call.
        return self.__size

    def resize(self, new_area_size: ScreenArea) -> Sequence[Tuple[ComponentId, ScreenArea]]:
        """
        Set the size of this portal.  The call returns the adjusted size of the owned windows,
        which the caller must use to generate the appropriate native move/resize events.

        :param new_area_size:
        :return:
        """
        prev = self.__size
        self.__size = new_area_size
        adjusted: List[Tuple[ComponentId, ScreenArea]] = []
        for window in self._windows:
            prev_size = get_position(prev, window.base_area, window.position_favor)
            new_size = get_position(new_area_size, window.base_area, window.position_favor)
            if prev_size != new_size:
                adjusted.append((window.cid, new_size,))
        if self.__background_cid:
            adjusted.append((self.__background_cid, new_area_size,))
        return adjusted

    def get_window_at(self, index: int) -> Optional[Tuple[ComponentId, ScreenArea]]:
        """Gets the window cid + size of the requested window index.  The index is
        adjusted to be within the range of windows through absolute value and modulo.
        Only if there are no windows is None returned."""
        if len(self._windows) <= 0:
            return None
        index = abs(index % len(self._windows))
        window = self._windows[index]
        return window.cid, get_position(self.__size, window.base_area, window.position_favor)

    def __getitem__(self, i: int) -> PortalWindowInfo:
        return self._windows[i]

    def get_windows(self) -> Sequence[ComponentId]:
        """
        Return the list of registered window CIDs (either chrome or window).
        Does not include the background window.  The list is in the same index
        order.
        """
        return tuple([w.cid for w in self._windows])

    def __len__(self) -> int:
        return self.get_window_count()

    def get_window_count(self) -> int:
        """The number of internal windows, not counting the background window."""
        return len(self._windows)

    def set_visible_window_index(self, index: int) -> Optional[ComponentId]:
        """
        Sets the window at the given internal index as the now-visible
        window within this portal.  If the index is out of range, it will
        be mapped (through modulo and absolute value) to a valid number.
        """
        if len(self._windows) <= 0:
            return None
        self.__current_index = abs(index % len(self._windows))
        return self._windows[self.__current_index].cid

    def set_visible_window(self, window_cid: ComponentId) -> bool:
        """
        Adjust the internal settings of the portal to think of the
        given window_cid as being active.  Returns True if the cid
        is in this portal, or False if it is not.

        :param window_cid:
        :return:
        """
        for index in range(len(self._windows)):
            if self._windows[index].cid == window_cid:
                self.__current_index = index
                return True
        return False

    def get_visible_window_index(self) -> int:
        """
        Gets the visible window index, or < 0 if there is no window in
        this portal.
        """
        if len(self._windows) <= 0:
            return -1
        return self.__current_index

    def get_visible_window(self) -> Optional[ComponentId]:
        if len(self._windows) <= 0:
            return None
        return self._windows[self.__current_index].cid

    def get_visible_window_info(self) -> Optional[PortalWindowInfo]:
        if len(self._windows) <= 0:
            return None
        return self._windows[self.__current_index]

    def change_visible_window_index(self, delta_index: int) -> Optional[ComponentId]:
        """
        Same as `set_visible_window_index`, but changes the index by
        a number based on the current index.

        :param delta_index:
        :return:
        """
        # Cannot reuse self.set_visible_window_index, because we're using
        # a non-reentrant lock.
        if len(self._windows) <= 0:
            return None
        self.__current_index = abs((self.__current_index + delta_index) % len(self._windows))
        return self._windows[self.__current_index].cid

    def set_visible_window_position_favor(self, position_favor: int) -> Optional[Tuple[ComponentId, ScreenArea]]:
        """
        If there is a visible window, then change its position favor, and return the window CID + the
        new screen area.

        :param position_favor:
        :return:
        """
        if len(self._windows) <= 0:
            return None
        window = self._windows[self.__current_index]
        window.set_position_favor(position_favor)
        return window.cid, get_position(self.__size, window.base_area, position_favor)

    def set_focus(self, has_focus: bool) -> Optional[ComponentId]:
        """
        Set the top window as having the focus, or losing the focus.
        :return:
        """
        if has_focus and len(self._windows) > 0:
            return self._windows[self.__current_index].cid
        return None

    def has_window(self, cid: ComponentId) -> bool:
        for window in self._windows:
            if window.cid == cid:
                return True
        return False

    def __repr__(self) -> str:
        return (
            'Portal(name={name}, size={size}, current={current}, '
            'background={background}, windows={windows})').format(
            name=repr(self.__name),
            size=repr(self.__size),
            current=repr(self.__current_index),
            background=repr(self.__background_cid),
            windows=repr(self._windows)
        )


def get_position(portal_size: ScreenArea, window_size: ScreenArea, position_favor: int) -> ScreenArea:
    """
    Finds the window position based on the portal size, the original window size, and how
    the window favors its position within the portal.

    :param portal_size:
    :param window_size:
    :param position_favor:
    :return:
    """

    assert position_favor in POSITION_FAVOR_ALL
    x = window_size[SCREEN_AREA_X]
    y = window_size[SCREEN_AREA_Y]
    w = window_size[SCREEN_AREA_W]
    h = window_size[SCREEN_AREA_H]

    if (position_favor & POSITION_FAVOR_MASK_RESTRICT_WIDTH) != 0:
        w = min(portal_size[SCREEN_AREA_W], w)
    if (position_favor & POSITION_FAVOR_MASK_RESTRICT_HEIGHT) != 0:
        h = min(portal_size[SCREEN_AREA_H], h)

    if (position_favor & POSITION_FAVOR_MASK_ALIGN_E) != 0:
        x = portal_size[SCREEN_AREA_X]
        if (position_favor & POSITION_FAVOR_MASK_ALIGN_W) != 0:
            w = portal_size[SCREEN_AREA_W]
    elif (position_favor & POSITION_FAVOR_MASK_ALIGN_W) != 0:
        x = portal_size[SCREEN_AREA_X] + portal_size[SCREEN_AREA_W] - w

    if (position_favor & POSITION_FAVOR_MASK_ALIGN_N) != 0:
        y = portal_size[SCREEN_AREA_Y]
        if (position_favor & POSITION_FAVOR_MASK_ALIGN_S) != 0:
            h = portal_size[SCREEN_AREA_H]
    elif (position_favor & POSITION_FAVOR_MASK_ALIGN_S) != 0:
        y = portal_size[SCREEN_AREA_Y] + portal_size[SCREEN_AREA_H] - h

    return x, y, w, h
