
"""
The root tile of the tile tree, which means it directly contains
one splitter per screen.
"""

from typing import List, Tuple, Iterable, Sequence
from typing import cast as t_cast
from ....aid.std import ComponentId, EMPTY_LIST
from .portal import Portal
from .splitter import SplitterTile, Tile, SPLIT_HORIZONTAL


class RootTile:
    """
    The top-level tile, which contains one splitter per screen.  This means
    that, with this configuration, windows cannot cross screen boundaries.

    If the screen resolution changes, or the number of monitors changes, then
    the root tile will need to be destroyed and a new one takes its place.
    The manager may make a best guess on placement of windows in the new
    resolution, but that, by its nature, will be hard to do.
    """

    __slots__ = ('__screens', '__active_index', '__name',)

    def __init__(self, name: str, screens: Iterable[SplitterTile], primary: int = 0) -> None:
        assert screens
        self.__name = name
        self.__screens = tuple(screens)
        self.__active_index = max(0, min(primary, len(self.__screens) - 1))

    @property
    def name(self) -> str:
        return self.__name

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

    def set_active_index_path(self, path: Sequence[int]) -> None:
        path_len = len(path)
        if path_len > 0:
            # Note: always have at least 1 screen.
            self.set_active_index(path[0])
            if path_len > 1:
                self.__screens[self.__active_index].set_active_split_path(path[1:])

    def get_active_portal_path(self) -> Sequence[int]:
        ret = [self.__active_index]
        ret.extend(self.__screens[self.__active_index].get_active_portal_path())
        return ret

    def get_active_portal(self) -> Portal:
        ret = self.__screens[self.__active_index].get_active_portal()
        if ret is None:
            # TODO use validation logic stuff instead...
            raise ValueError('Should always have one active portal')
        return ret

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

    def get_portal_in_split_direction(
            self, split_direction: int, direction_count: int, wrap: bool
    ) -> Sequence[int]:
        # split direction for screens is always considered horizontal.
        # TODO changing this requires knowing relative locations between screens.
        active = self.__active_index

        count = direction_count
        path = self.get_active_portal_path()
        if split_direction == SPLIT_HORIZONTAL:
            # print("Finding direction {0} relative to active potal {1}".format(split_direction, path))
            # Move includes moving between screens.
            current = self.__screens[active].get_active_child_index()
            while count != 0:
                # print(" - moving {0} from active {1}.{2}".format(count, active, current))
                # Move the active
                path, count = self.__screens[active].get_portal_in_split_direction(
                    split_direction, count, current
                )
                path = [active, *path]
                # print(" - move returned path {0} with remaining count {1}".format(path, count))
                if count > 0:
                    if not wrap and active + 1 >= len(self.__screens):
                        # print(" - no wrap caused terminate with path {0} and remaining count {1}".format(
                        #     path, count
                        # ))
                        return path
                    active = (active + 1) % len(self.__screens)
                    current = 0
                elif count < 0:
                    if not wrap and active - 1 < 0:
                        # print(" - no wrap caused terminate with path {0} and remaining count {1}".format(
                        #     path, count
                        # ))
                        return path
                    active = (active - 1) % len(self.__screens)
                    current = self.__screens[active].count() - 1
            # print(" - loop terminated with path {0}".format(path))
            return path
        else:
            # stay on the same active.
            screen = self.__screens[active]
            current = screen.get_active_child_index()
            while count != 0:
                path, count = screen.get_portal_in_split_direction(split_direction, count, current)
                path = [active, *path]
                if count > 0:
                    if not wrap:
                        return path
                    current = 0
                elif count < 0:
                    if not wrap:
                        return path
                    current = screen.count() - 1
            return path

    def get_active_split_target(self) -> Tuple[SplitterTile, Sequence[int]]:
        """
        Find the active split target.  This is done by finding the active portal, and walking
        up the splits to the first one that is a target.  If none are targets, then the
        portal's direct parent is returned.
        :return:
        """

        # First, find the paths that lead up to the active portal.
        path = self.get_active_portal_path()
        assert path
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

    def set_active_window(self, cid: ComponentId) -> Sequence[int]:
        """
        Helper method to assign the currently active window path.

        :param cid:
        :return:
        """
        for screen_index in range(len(self.__screens)):
            found = self.__screens[screen_index].set_active_window(cid)
            if found:
                self.__active_index = screen_index
                return [screen_index, *found]
        return t_cast(Sequence[int], EMPTY_LIST)

    def __repr__(self) -> str:
        return "RootTile(active={0}, screens={1})".format(self.__active_index, self.__screens)
