
"""
The root tile of the tile tree, which means it directly contains
one splitter per screen.
"""

from typing import Iterable, Sequence, List, Optional
from ....aid.std import ComponentId
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

    __slots__ = ('__screens', '__active_index',)

    def __init__(self, screens: Iterable[SplitterTile]) -> None:
        assert screens
        self.__screens = tuple(screens)
        self.__active_index = 0

    def set_active_index(self, index: int) -> None:
        """
        Sets the active screen index.  If the index is out of range, it will
        be wrapped (via modulo and absolute value) to a valid index.

        :param index:
        :return:
        """
        self.__active_index = abs(index % len(self.__screens))

    def get_active_index(self) -> int:
        return self.__active_index

    def get_active_portal_path(self) -> Sequence[int]:
        ret = [self.__active_index]
        ret.extend(self.__screens[self.__active_index].get_active_portal_path())
        return ret

    def get_active_portal(self) -> Portal:
        ret = self.__screens[self.__active_index].get_active_portal()
        if ret is None:
            # TODO use validation logic stuff...
            raise ValueError('Should always have one active portal')
        return ret

    def get_portals(self) -> Sequence[Portal]:
        ret: List[Portal] = []
        for screen in self.__screens:
            ret.extend(screen.get_portals())
        return ret

    def get_active_split_target(self) -> Optional[Tile]:
        raise NotImplementedError()

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
        return "RootTile(active={0}, screens={1})".format(self.__active_index, self.__screens)
