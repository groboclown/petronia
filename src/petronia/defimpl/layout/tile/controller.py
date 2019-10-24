
"""
General manager for the tiles.  This provides the control methods for
interacting with the splitters and portals tree.
"""

from typing import Sequence, Tuple, Optional
from threading import Lock
from ....aid.std import (
    ComponentId,
)
from ....core.platform.api import (
    ScreenSize, ScreenPosition, ScreenArea,
)
from .root import (
    RootTile,
)
from .portal import (
    Portal,
    PortalWindowInfo,
)
from .splitter import (
    Tile,
)


class AdjustedWindow:
    """Defines how a window moved or resized."""
    __slots__ = ('__cid', '__area',)

    def __init__(self, window_cid: ComponentId, area: ScreenArea) -> None:
        self.__cid = window_cid
        self.__area = area

    @property
    def window_cid(self) -> ComponentId:
        return self.__cid

    @property
    def area(self) -> ScreenArea:
        return self.__area


ADJUSTED_PORTAL_ACTION_REMOVED = 'removed'
ADJUSTED_PORTAL_ACTION_RESIZED = 'resized'
ADJUSTED_PORTAL_ACTION_ADDED = 'added'
ADJUSTED_PORTAL_ACTION_ALL = (
    ADJUSTED_PORTAL_ACTION_REMOVED,
    ADJUSTED_PORTAL_ACTION_RESIZED,
    ADJUSTED_PORTAL_ACTION_ADDED,
)


class AdjustedPortal:
    """Defines a portal and the contained windows that were changed."""
    __slots__ = ('__portal', '__windows', '__action',)

    def __init__(self, action: str, portal: Portal, windows: Sequence[AdjustedWindow]) -> None:
        assert action in ADJUSTED_PORTAL_ACTION_ALL
        self.__action = action
        self.__portal = portal
        self.__windows = tuple(windows)

    @property
    def action(self) -> str:
        return self.__action

    @property
    def portal(self) -> Portal:
        return self.__portal

    @property
    def windows(self) -> Sequence[AdjustedWindow]:
        return self.__windows

    def is_removed(self) -> bool:
        return self.__action == ADJUSTED_PORTAL_ACTION_REMOVED

    def is_resized(self) -> bool:
        return self.__action == ADJUSTED_PORTAL_ACTION_RESIZED

    def is_added(self) -> bool:
        return self.__action == ADJUSTED_PORTAL_ACTION_ADDED


MOVE_WINDOW_DIRECTION_NORTH = 1
MOVE_WINDOW_DIRECTION_SOUTH = 2
MOVE_WINDOW_DIRECTION_EAST = 3
MOVE_WINDOW_DIRECTION_WEST = 4
MOVE_WINDOW_DIRECTION_ALL = (
    MOVE_WINDOW_DIRECTION_NORTH,
    MOVE_WINDOW_DIRECTION_SOUTH,
    MOVE_WINDOW_DIRECTION_EAST,
    MOVE_WINDOW_DIRECTION_WEST,
)



class TileController:
    """
    Outside controller for the tiles.  Does not interact with the bus.
    """

    __slots__ = ('__root', '__active_path', '__lock')

    def __init__(self, root: RootTile) -> None:
        self.__root = root
        self.__active_path = root.get_active_index()
        self.__lock = Lock()

    def add_window_to_named_portal(
            self, name: str, window_cid: ComponentId, base_window_area: ScreenArea, position_favor: int
    ) -> Tuple[Portal, ScreenArea]:
        """Put the window into the portal with the given name, or into the named portal path,
        or into the active portal.  This does not generate the necessary events, but it returns
        the position the window will take.  The window must not already be added."""
        with self.__lock:
            portal = self.get_named_portal(name)
            window_index, area = portal.add_window(window_cid, base_window_area, position_favor)
            portal.set_visible_window_index(window_index)
        return portal, area

    def remove_window(self, window_cid: ComponentId) -> Optional[Portal]:
        """Remove the window from the tree, usually because it's been deleted."""
        with self.__lock:
            for portal in self.__root.get_portals():
                if portal.remove_window(window_cid):
                    return portal
            return None

    def set_active_portal_name(self, name: str) -> None:
        """Set a named path to the currently active portal."""
        with self.__lock:
            portal = self.__root.get_active_portal()
            portal.set_name(name)

    def focus_named_portal(self, name: str) -> Optional[Portal]:
        """Set the given named path as active and return the focused portal, if any.  If
        the name isn't assigned to a portal or a path, then None is returned."""
        with self.__lock:
            for portal, path in self.__root.get_portals_with_paths():
                if portal.get_name() == name:
                    self.__root.set_active_index_path(path)
                    return portal
        return None

    def on_window_focused(self, window: ComponentId) -> None:
        """Inform the owning portal that the given window is now focused.  Used
        to keep internal state synchronized with the native UI state."""
        with self.__lock:
            self.__root.set_active_window(window)

    def active_portal_window_switch(self, direction: int) -> Optional[Tuple[Portal, ComponentId]]:
        """
        Switch the active window within the active portal by the given number of
        windows (negative for reverse direction).

        :param direction:
        :return: the portal containing the window, and the newly active window.
        """
        with self.__lock:
            portal = self.__root.get_active_portal()
            window = portal.change_visible_window_index(direction)
            if window:
                return portal, window
        return None

    def remove_active_split(self) -> Tuple[Sequence[PortalWindowInfo], Sequence[AdjustedPortal]]:
        """
        Remove the currently active portal from its owning split.  The contained windows will
        need to be moved, and the owning split may adjust its sizes to accommodate the adjusted
        size.

        :return: the windows in the removed portal that are now parent-less, and
            portals that were adjusted with the change (does not include the parent-less windows).
        """
        raise NotImplementedError()

    def add_active_split(self) -> Sequence[AdjustedPortal]:
        """
        Adds a new portal in the nearest target split to the active portal.  The splits
        and portals may have their position adjusted.

        :return: the portals that were adjusted by the change.
        """
        raise NotImplementedError()

    def resize_active_split(self, pixel_count: int) -> Sequence[AdjustedPortal]:
        """
        Resize the active split child, in the direction of this split.

        In general, it prioritizes east and south growth or shrinkage.
        """
        raise NotImplementedError()

    def move_active_split(self, pixel_count: int) -> Sequence[AdjustedPortal]:
        """
        Moves the active split by growing or shrinking the sibling splits
        around it.
        """
        raise NotImplementedError()

    def move_active_window(self, direction: int, count: int, wrap: bool) -> Sequence[AdjustedPortal]:
        """
        Move the active window to a different portal in the given direction.

        :param direction:
        :param count:
        :param wrap:
        :return:
        """
        # assert direction in MOVE_WINDOW_DIRECTION_ALL
        raise NotImplementedError()

    def get_named_portal(self, name: str) -> Portal:
        """Find the portal with the given name, or the named path,
        or the active portal."""
        with self.__lock:
            for portal in self.__root.get_portals():
                if portal.get_name() == name:
                    return portal
            return self.get_active_portal()

    def get_active_portal(self) -> Portal:
        return self.__root.get_active_portal()

    def get_active_window(self) -> Optional[ComponentId]:
        portal = self.__root.get_active_portal()
        return portal.get_visible_window()

    def move_portal_focus(self, direction: str, amount: int, wrap: bool) -> Tuple[Portal, Optional[ComponentId]]:
        """

        :param direction: one of 'n', 's', 'e', or 'w'.  Default is 'e'.
        :param amount:
        :param wrap:
        :return:
        """
        raise NotImplementedError()

    def _left(self, path: Sequence[int], wrap: bool) -> Tuple[Portal, Sequence[int]]:
        """The tile that is 'left' from the currently active tile."""
        raise NotImplementedError()

    def _right(self, path: Sequence[int], wrap: bool) -> Tuple[Portal, Sequence[int]]:
        raise NotImplementedError()

    def _up(self, path: Sequence[int], wrap: bool) -> Tuple[Portal, Sequence[int]]:
        raise NotImplementedError()

    def _down(self, path: Sequence[int], wrap: bool) -> Tuple[Portal, Sequence[int]]:
        raise NotImplementedError()

    def _tile_at(self, path: Sequence[int]) -> Tuple[Tile, Sequence[int]]:
        """
        Must be called from within a lock.
        """
        if not path:
            raise ValueError('path must have at least 1 entry')
        child: Tile = self.__root.get_child(path[0])
        followed = [path[0]]
        remaining = list(path[1:])
        while remaining:
            if isinstance(child, Portal):
                return child, followed
            index = remaining.pop()
            child = child.get_child(index)
            followed.append(index)
        return child, followed
