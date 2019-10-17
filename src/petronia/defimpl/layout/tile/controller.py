
"""
General manager for the tiles.  This provides the control methods for
interacting with the splitters and portals tree.
"""

from typing import Dict, Sequence, Tuple, Optional
from threading import Lock
from ....aid.std import (
    ComponentId,
)
from .root import (
    RootTile,
)
from .portal import (
    Portal,
)
from .splitter import (
    Tile,
)


class TileController:
    """
    Outside controller for the tiles.
    """

    __slots__ = ('__root', '__active_path', '_named_portals', '__lock')
    _named_portals: Dict[str, Sequence[int]]

    def __init__(self, root: RootTile) -> None:
        self.__root = root
        self.__active_path = root.get_active_index()
        self.__lock = Lock()
        self._named_portals = {}

    def add_window_to_named_portal(self, name: str, window_cid: ComponentId) -> Portal:
        """Put the window into the portal with the given name, or into the named portal path,
        or into the active portal.  This does not generate the necessary events, but it returns
        the position the window will take.  The window must not already be added."""
        with self.__lock:
            portal = self.get_named_portal(name)
            window_index = portal.add_window(window_cid)
            portal.set_visible_window_index(window_index)
        return portal

    def remove_window(self, window_cid: ComponentId) -> Optional[Portal]:
        """Remove the window from the tree, usually because it's been deleted."""
        with self.__lock:
            for portal in self.__root.get_portals():
                if portal.remove_window(window_cid):
                    return portal
            return None

    def set_active_portal_name(self, name: str) -> None:
        """Set a named path to the currently active portal."""
        raise NotImplementedError()

    def focus_named_portal(self, name: str) -> ComponentId:
        """Set the named path as active and return its visible window cid."""
        raise NotImplementedError()

    def active_portal_window_switch(self, direction: int) -> None:
        """
        Switch the active window within the active portal by the given number of
        windows (negative for reverse direction).

        :param direction:
        :return:
        """
        raise NotImplementedError()

    def remove_active_split(self) -> None:
        raise NotImplementedError()

    def add_active_split(self) -> None:
        raise NotImplementedError()

    def resize_active_split(self, pixel_count: int) -> None:
        raise NotImplementedError()

    def move_active_window(self, direction: int, count: int, wrap: bool) -> None:
        """
        Move the active window to a different portal in the given direction.

        :param direction:
        :param count:
        :param wrap:
        :return:
        """
        raise NotImplementedError()

    def get_named_portal(self, name: str) -> Portal:
        """Find the portal with the given name, or the named path,
        or the active portal."""
        with self.__lock:
            for portal in self.__root.get_portals():
                if portal.name == name:
                    return portal
            if name in self._named_portals:
                val, path = self._tile_at(self._named_portals[name])
                if isinstance(val, Portal):
                    return val
            return self.__root.get_active_portal()

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
