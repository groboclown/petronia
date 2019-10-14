
"""
The general container type.
"""

from typing import List, Sequence, Tuple, Iterable, Callable, Optional, Union
from ....aid.std import (
    ComponentId,
)
from ....core.platform.api import (
    ScreenUnit,
    ScreenArea,
    SCREEN_AREA_X,
    SCREEN_AREA_Y,
    SCREEN_AREA_HEIGHT,
    SCREEN_AREA_WIDTH,
)
from .portal import Portal


Tile = Union[Portal, 'SplitterTile']
TileFactory = Callable[[int, ScreenArea], Tile]


SPLIT_VERTICAL = 0
SPLIT_HORIZONTAL = 1
SPLIT_ALL = (
    SPLIT_VERTICAL,
    SPLIT_HORIZONTAL,
)


class SplitterTile:
    """
    A container of 1 or more portals, so called because it manages the
    splitting of the portals.

    The splits are proportions of the size of the portals within the
    container's area. A "1" value for each split means that every portal
    is close to the same size (may have 1 pixel rounding difference).

    If a child tile has size "0", then it starts where the previous tile left
    off (or at the top if there was no previous one), and fills the rest of
    the split.  The following tile continue as if the size "0" wasn't
    present.  This allows for a tile to overlap others.

    Splitters must have at least 1 child.  That means the leaf of the splitter
    tree must be only portals.
    """

    __slots__ = (
        '_children',
        '__size',
        '__splits',
        '__factory',
        '__active_index',
        '__direction',
        '__is_split_target',
    )
    _children: List[Tile]

    def __init__(
            self,
            factory: TileFactory,
            size: ScreenArea,
            direction: int,
            splits: Iterable[int],
            is_split_target: bool
    ) -> None:
        assert direction in SPLIT_ALL
        assert splits
        self.__direction = direction
        self.__size = size
        self.__factory = factory
        self.__splits = tuple(splits)
        self._children = []
        self.__active_index = 0
        self.__is_split_target = is_split_target
        total = 0
        for s in self.__splits:
            total += s
        # Avoid a divide by zero.
        factor = _split_dir_size(size, direction) // max(total, 1)
        last = 0
        for i in range(len(self.__splits)):
            is_last = i >= len(self.__splits) - 1
            prop = self.__splits[i]
            if prop <= 0:
                sub_area = _split_dir_pos(size, last, -1, direction, is_last)[0]
            else:
                sub_area, last = _split_dir_pos(size, last, factor * prop, direction, is_last)
            self._children.append(factory(i, sub_area))
        assert len(self._children) > 0

    def get_active_split_target(self) -> Optional[Tile]:
        """
        Depth-first analysis to find the split target at or
        closest to the active portal.
        :return:
        """
        active = self._children[self.__active_index]
        if not isinstance(active, Portal):
            tgt = active.get_active_split_target()
            if tgt:
                return tgt
        if self.__is_split_target:
            return self
        return None

    def get_active_split_target_path(self) -> Optional[Sequence[int]]:
        """
        Find the index-based path to the split target.  If it returns
        an empty sequence, then this split is the active split.  If
        it returns None, then there is no active split in this.

        :return:
        """
        active = self._children[self.__active_index]
        if not isinstance(active, Portal):
            path = active.get_active_split_target_path()
            if path is not None:
                ret = [self.__active_index]
                ret.extend(path)
                return ret
        if self.__is_split_target:
            return []
        return None

    def get_active_portal(self) -> Optional[Portal]:
        """
        Find the active portal within this splitter.

        :return:
        """
        child = self._children[self.__active_index]
        if isinstance(child, Portal):
            return child
        return child.get_active_portal()

    def get_active_portal_path(self) -> Sequence[int]:
        """
        Return the index path from this splitter down to the active
        portal.

        :return:
        """
        ret = [self.__active_index]
        active = self._children[self.__active_index]
        if not isinstance(active, Portal):
            path = active.get_active_split_target_path()
            if path:
                ret.extend(path)
        return ret

    def get_portals(self) -> Sequence[Portal]:
        """
        Find all contained portals, including within all child splits.
        :return:
        """
        ret: List[Portal] = []
        for child in self._children:
            if isinstance(child, Portal):
                ret.append(child)
            else:
                ret.extend(child.get_portals())
        return ret

    def set_active_split(self, pos: int) -> Optional[ComponentId]:
        """

        :param pos:
        :return: the cid of the now-active portal's
        """
        if len(self._children) <= 0:
            # TODO disable the active split.
            return None
        raise NotImplementedError()

    def change_active_split(self, adjustment: int) -> Optional[ComponentId]:
        """

        :param adjustment:
        :return: the cid of the now-active portal's
        """
        return self.set_active_split(self.__active_index + adjustment)

    def add_split(self, proportion: int) -> None:
        # Set the active index to the newly added split.
        # This allows add -> remove to be essentially a no-op.
        self.__active_index = -1
        raise NotImplementedError()

    def remove_active_split(self) -> Sequence[ComponentId]:
        """
        Remove the active split.  If there is only one tile left, the request is
        passed to that child.  If that child is a portal, then the request is
        ignored.

        :return: list of all child windows that were in the active split.
            It's the caller's responsibility to move those to new splits or
            to otherwise manage their new state.
        """
        if len(self._children) <= 0:
            return ()
        self.__active_index -= 1
        raise NotImplementedError()

    def increase_active_split_factor(self, active_increase: int) -> None:
        """
        Resizes the split by a given amount.  If the amount is negative, then the
        split size is reduced by that amount.  However, a split size cannot be less
        than 1, so if that happens, then the other splits are all increased by the
        corresponding number.

        :return:
        """
        raise NotImplementedError()

    def get_area(self) -> ScreenArea:
        return self.__size

    def resize(self, new_area: ScreenArea) -> None:
        raise NotImplementedError()

    def get_children(self) -> Sequence[Tile]:
        return tuple(self._children)

    def get_child(self, index: int) -> Tile:
        return self._children[abs(index % len(self._children))]

    def __getitem__(self, item: int) -> Tile:
        return self.get_child(item)

    def count(self) -> int:
        return len(self._children)

    def __len__(self) -> int:
        return self.count()

    def __repr__(self) -> str:
        return (
            'SplitterTile(size={size}, '
            'active={active}, direction={direction}, is_split_target={target}, splits={splits}, children={kids})'
        ).format(
            size=repr(self.__size),
            active=repr(self.__active_index),
            direction=repr(self.__direction),
            target=repr(self.__is_split_target),
            splits=repr(self.__splits),
            kids=repr(self._children)
        )


def _split_dir_size(area: ScreenArea, direction: int) -> ScreenUnit:
    if direction == SPLIT_HORIZONTAL:
        return area[SCREEN_AREA_WIDTH]
    return area[SCREEN_AREA_HEIGHT]


def _split_dir_pos(
        area: ScreenArea, prev_end: ScreenUnit, size: ScreenUnit, direction: int,
        is_last: bool
) -> Tuple[ScreenArea, ScreenUnit]:
    """
    Creates a screen area in the direction for the given size.  This limits
    the returned area to be within the area argument, but does not guarantee
    that the returned area has any size.

    :param area:
    :param prev_end:
    :param size:
    :param direction:
    :return: tuple of (sub area size, end position for returned area)
    """
    if direction == SPLIT_HORIZONTAL:
        mpos = area[SCREEN_AREA_X] + area[SCREEN_AREA_WIDTH]
        start = min(mpos, area[SCREEN_AREA_X] + prev_end)
        if size <= 0 or is_last:
            end = mpos
            size = end - start
        else:
            end = min(mpos, area[SCREEN_AREA_X] + prev_end + size)
        return (
            (
                start, area[SCREEN_AREA_Y], size, area[SCREEN_AREA_HEIGHT],
            ),
            end,
        )
    mpos = area[SCREEN_AREA_Y] + area[SCREEN_AREA_HEIGHT]
    start = min(mpos, area[SCREEN_AREA_Y] + prev_end)
    if size <= 0 or is_last:
        end = mpos
        size = end - start
    else:
        end = min(mpos, area[SCREEN_AREA_Y] + prev_end + size)
    return (
        (
            area[SCREEN_AREA_X], start, area[SCREEN_AREA_WIDTH], size,
        ),
        end,
    )
