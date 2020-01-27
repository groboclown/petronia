
"""
The root tile of the tile tree, which means it directly contains
one splitter per screen.
"""

from typing import List, Tuple, Iterable, Sequence
from .portal import Portal
from .splitter import SplitterTile, Tile


class RootTile:
    """
    The top-level tile, which contains one splitter per screen.  This means
    that, with this configuration, windows cannot cross screen boundaries.

    If the screen resolution changes, or the number of monitors changes, then
    the root tile will need to be destroyed and a new one takes its place.
    The manager may make a best guess on placement of windows in the new
    resolution, but that, by its nature, will be hard to do.
    """

    __slots__ = ('__screens', '__name', '__wrap_x', '__wrap_y')

    def __init__(self, name: str, screens: Iterable[SplitterTile], _primary: int) -> None:
        assert screens
        self.__name = name
        self.__screens = tuple(screens)
        self.__wrap_x = False
        self.__wrap_y = False

    @property
    def name(self) -> str:
        return self.__name

    @property
    def wrap_x(self) -> bool:
        return self.__wrap_x

    @property
    def wrap_y(self) -> bool:
        return self.__wrap_y

    def get_portals(self) -> Iterable[Portal]:
        """Note that this is a generator...  So that an early exit will not need
        to loop through everything."""
        for screen in self.__screens:
            for portal in screen.get_portals():
                yield portal

    def get_portals_with_paths(self) -> Iterable[Tuple[Portal, Sequence[int]]]:
        for screen_index in range(len(self.__screens)):
            screen = self.__screens[screen_index]
            for portal, path in screen.get_portals_with_paths():
                yield portal, [screen_index, *path]

    def get_split_target(self, active_path: Sequence[int]) -> Tuple[SplitterTile, Sequence[int]]:
        """
        Find the active split target.  This is done by finding the active portal, and walking
        up the splits to the first one that is a target.  If none are targets, then the
        portal's direct parent is returned.
        :return:
        """

        assert active_path
        path = list(active_path)
        splits: List[SplitterTile] = []
        kids: Sequence[Tile] = self.__screens
        index = 0
        while index < len(path):
            part = kids[path[index]]
            if isinstance(part, Portal):
                path = path[0:index + 1]
                break
            kids = part.get_children()
            splits.append(part)

        # Then, find the closest split target to the end.
        for index in range(len(splits) - 1, -1, -1):
            if splits[index].is_split_target:
                return splits[index], path[0:index + 1]
        # No target found
        return splits[-1], path

    def count(self) -> int:
        return len(self.__screens)

    def __len__(self) -> int:
        return self.count()

    def get_child(self, index: int) -> SplitterTile:
        return self.__screens[abs(index % len(self.__screens))]

    def __getitem__(self, item: int) -> SplitterTile:
        return self.get_child(item)

    def get_children(self) -> Sequence[SplitterTile]:
        return self.__screens

    def __repr__(self) -> str:
        return "RootTile(screens={0})".format(self.__screens)
