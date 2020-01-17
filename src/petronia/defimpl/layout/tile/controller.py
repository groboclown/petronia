
"""
General manager for the tile.  This provides the control methods for
interacting with the splitters and portals tree.
"""

from typing import Sequence, Tuple, Iterable, Optional
from typing import cast as t_cast
from threading import Lock
from .consts import (
    MOVE_WINDOW_DIRECTION_NORTH,
    MOVE_WINDOW_DIRECTION_EAST,
    MOVE_WINDOW_DIRECTION_SOUTH,
    MOVE_WINDOW_DIRECTION_WEST,
)
from .navigation import Navigator
from .portal import (
    Portal,
    PortalWindowInfo,
)
from .root import (
    RootTile,
)
from .splitter import (
    Tile,
)
from ....aid.std import (
    ComponentId,
    EMPTY_TUPLE,
)
from ....core.platform.api import (
    ScreenArea,
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


class TileController:
    """
    Outside controller for the tile.  Does not interact with the bus.
    """

    __slots__ = ('__root', '__navigation', '__lock')

    def __init__(self, root: RootTile, active_window_cid: Optional[ComponentId]) -> None:
        self.__root = root
        self.__navigation = Navigator(
            active_window_cid, root.get_portals_with_paths(),
            root.wrap_x, root.wrap_y
        )
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
            portal = self.__navigation.get_active_portal()
            portal.set_name(name)

    def focus_named_portal(self, name: str) -> Optional[Portal]:
        """Set the given named path as active and return the focused portal, if any.  If
        the name isn't assigned to a portal or a path, then None is returned."""
        with self.__lock:
            portal_and_path = self.__navigation.make_active_choice(lambda p: p.get_name() == name)
        if portal_and_path:
            return portal_and_path[0]
        return None

    def on_window_focused(self, window: ComponentId) -> None:
        """Inform the owning portal that the given window is now focused.  Used
        to keep internal state synchronized with the native UI state."""
        with self.__lock:
            with self.__lock:
                self.__navigation.make_active_choice(lambda p: p.has_window(window))

    def active_portal_window_switch(self, direction: int) -> Optional[Tuple[Portal, ComponentId]]:
        """
        Switch the active window within the active portal by the given number of
        windows (negative for reverse direction).

        :param direction:
        :return: the portal containing the window, and the newly active window.
        """
        with self.__lock:
            portal = self.__navigation.get_active_portal()
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

        # Must create a new navigation
        # self.__navigation = new Navigation(...)

        raise NotImplementedError()

    def add_active_split(self, new_portal_id: ComponentId) -> Tuple[Portal, Sequence[AdjustedPortal]]:
        """
        Adds a new portal in the nearest target split to the active portal.  The splits
        and portals may have their position adjusted.

        :return: the portals that were adjusted by the change.
        """

        # Must create a new navigation
        # self.__navigation = new Navigation(...)

        raise NotImplementedError()

    def resize_active_split(self, pixel_count: int) -> Sequence[AdjustedPortal]:
        """
        Resize the active split child, in the direction of this split.

        In general, it prioritizes east and south growth or shrinkage.
        """

        # Must create a new navigation
        # self.__navigation = new Navigation(...)

        raise NotImplementedError()

    def move_active_split(self, pixel_count: int) -> Sequence[AdjustedPortal]:
        """
        Moves the active split by growing or shrinking the sibling splits
        around it.
        """

        # Must create a new navigation
        # self.__navigation = new Navigation(...)

        raise NotImplementedError()

    def move_active_window(
            self, direction: int, count: int
    ) -> Tuple[Portal, Portal, Optional[ComponentId], Sequence[AdjustedPortal]]:
        """
        Move the active window to a different portal in the given direction.  The
        returned destination portal will internally be marked as active.

        :param direction:
        :param count:
        :return: source portal (no longer active), destination portal (now active),
            now-active window CID, moved portal windows.
        """

        # This is done as a portal move focus, while also capturing the initial focused window.
        src_portal = self.__navigation.get_active_portal()
        window_info = src_portal.get_visible_window_info()
        if not window_info:
            # No-Op
            return src_portal, src_portal, None, t_cast(Sequence[AdjustedPortal], EMPTY_TUPLE)
        _, tgt_portal, _ = self.move_portal_focus(direction, count)
        if tgt_portal == src_portal:
            # No-Op
            return src_portal, src_portal, window_info.cid, t_cast(Sequence[AdjustedPortal], EMPTY_TUPLE)

        src_portal.remove_window(window_info.cid)
        _, area = tgt_portal.add_window(window_info.cid, window_info.base_area, window_info.position_favor)

        return (
            src_portal, tgt_portal, window_info.cid,
            (
                AdjustedPortal(ADJUSTED_PORTAL_ACTION_RESIZED, tgt_portal, (
                    AdjustedWindow(window_info.cid, area),
                )),
            ),
        )

    def get_named_portal(self, name: str) -> Portal:
        """Find the portal with the given name, or the named path,
        or the active portal."""
        with self.__lock:
            for portal in self.__root.get_portals():
                if portal.get_name() == name:
                    return portal
            return self.get_active_portal()

    def get_active_portal(self) -> Portal:
        return self.__navigation.get_active_portal()

    def get_active_window(self) -> Optional[ComponentId]:
        portal = self.__navigation.get_active_portal()
        return portal.get_visible_window()

    def get_portals(self) -> Iterable[Portal]:
        return self.__root.get_portals()

    def move_portal_focus(
            self, direction: int, amount: int
    ) -> Tuple[Portal, Portal, Optional[ComponentId]]:
        """

        :param direction: direction to move focus
        :param amount: number of portals to move in the direction
        :return: source portal (no longer focused), new focused portal, and the window that now has the focus.
        """
        src_portal = self.__navigation.get_active_portal()
        # Yeah, having the loop outside the if statement is inefficient, but this is run "rarely" (e.g. based
        # on user typing something, not in a tight loop that's running for a long period of time).
        tgt_portal_and_path: Optional[Tuple[Portal, Sequence[int]]] = None
        for _i in range(amount):
            if direction == MOVE_WINDOW_DIRECTION_NORTH:
                next_tgt_portal_and_path = self.__navigation.move_north()
            elif direction == MOVE_WINDOW_DIRECTION_EAST:
                next_tgt_portal_and_path = self.__navigation.move_east()
            elif direction == MOVE_WINDOW_DIRECTION_SOUTH:
                next_tgt_portal_and_path = self.__navigation.move_south()
            elif direction == MOVE_WINDOW_DIRECTION_WEST:
                next_tgt_portal_and_path = self.__navigation.move_west()
            else:
                raise ValueError('invalid direction number {0}'.format(direction))
            if not next_tgt_portal_and_path:
                # reached the end.
                break
            tgt_portal_and_path = next_tgt_portal_and_path
        if not tgt_portal_and_path:
            # No-Op
            return src_portal, src_portal, None
        focus_window = tgt_portal_and_path[0].get_visible_window()
        return src_portal, tgt_portal_and_path[0], focus_window

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
            index = remaining[0]
            remaining = remaining[1:]
            child = child.get_child(index)
            followed.append(index)
        return child, followed

    def _active_portal_path(self) -> Tuple[Portal, Sequence[int]]:
        """Helper for tests."""
        return self.__navigation.get_active_portal_and_path()
