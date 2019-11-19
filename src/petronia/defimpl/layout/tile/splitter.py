
"""
The general container type.
"""

import math
from typing import List, Sequence, Tuple, Iterable, Callable, Optional, Union

from .portal import Portal
from ....aid.std import (
    ComponentId
)
from ....core.platform.api import (
    ScreenUnit,
    ScreenArea,
    SCREEN_AREA_X,
    SCREEN_AREA_Y,
    SCREEN_AREA_HEIGHT,
    SCREEN_AREA_WIDTH,
)

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

    # TODO add a higher-level interface for a "layout tile", which knows how
    #   to place the portals inside it.  This puts more of the responsibility on the
    #   layout to figure out what navigation directions mean.

    __slots__ = (
        '_children',
        '__area',
        '__splits',
        '__factory',
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
        self.__area = size
        self.__factory = factory
        self.__splits = tuple(splits)
        self._children = []
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

    @property
    def direction(self) -> int:
        return self.__direction

    def is_vertical(self) -> bool:
        return self.__direction == SPLIT_VERTICAL

    def is_horizontal(self) -> bool:
        return self.__direction == SPLIT_HORIZONTAL

    @property
    def is_split_target(self) -> bool:
        return self.__is_split_target

    def get_area(self) -> ScreenArea:
        return self.__area

    def get_active_split_target(self, active_path: Sequence[int]) -> Optional[Tile]:
        """
        Depth-first analysis to find the split target at or
        closest to the active portal.
        :return:
        """
        active_index = 0
        if active_path:
            active_index = abs(active_path[0] % len(self._children))
        active = self._children[active_index]
        if not isinstance(active, Portal):
            tgt = active.get_active_split_target(active_path[1:])
            if tgt:
                return tgt
        if self.__is_split_target:
            return self
        return None

    def get_portals(self) -> Iterable[Portal]:
        """
        Find all contained portals, including within all child splits.
        :return:
        """
        for child in self._children:
            if isinstance(child, Portal):
                yield child
            else:
                for kid in child.get_portals():
                    yield kid

    def get_portals_with_paths(self) -> Iterable[Tuple[Portal, Sequence[int]]]:
        for child_index in range(len(self._children)):
            child = self._children[child_index]
            if isinstance(child, Portal):
                yield child, [child_index]
            else:
                for portal, path in child.get_portals_with_paths():
                    yield portal, [child_index, *path]

    def add_split(self, percent_size: int) -> Tuple[Portal, Sequence[Tuple[ComponentId, ScreenArea]]]:
        """
        Add a new split with a new portal.  This new portal will be made active.
        If any other split is resized to accommodate the new portal, their
        contained windows will be returned to allow the caller to invoke the
        proper resize call.
        """

        # TODO allow setting the relative position of the new split - should it
        #   be above the current split, at the front of the rest, at the end?
        #   So many options for the user.
        # TODO allow better control over the size of the new portal.

        # 1. Collect the size information of the existing splits.
        # 2. Calculate the size of the new portal based on the percent_size and existing splits.
        # 3. Insert the portal into the list, and make it active.
        # 4. Recalculate the split sizes.
        # 5. Send the splits down to the child splits, and collect the adjusted window sizes.

        # Set the active index to the newly added split.
        # This allows add -> remove to be essentially a no-op.

        # size = blah
        # portal = Portal('', size, t_cast(Iterable[WindowMatcher], EMPTY_LIST))

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
        # if len(self._children) <= 0:
        #     return ()
        raise NotImplementedError()

    def resize_active_split(self, increase: ScreenUnit) -> None:
        """
        Resizes the active split by the given number of "pixels".
        Note that once the split is created, all sizes are in pixel sizes,
        not in the proportion.

        :return:
        """
        raise NotImplementedError()

    def resize(self, new_area: ScreenArea) -> List[Tuple[ComponentId, ScreenArea]]:
        """
        Resize the whole split.  This will attempt to keep the same proportions between
        the splits.
        """
        orig_length = _split_dir_size(self.__area, self.__direction)
        new_length = _split_dir_size(new_area, self.__direction)
        scale = new_length / orig_length
        last_pos = 0
        ret: List[Tuple[ComponentId, ScreenArea]] = []
        for child_index in range(len(self._children)):
            child = self._children[child_index]
            old_size = child.get_area()
            old_child_length = _split_dir_size(old_size, self.__direction)
            new_child_length = old_child_length * scale
            new_child_area, last_pos = _split_dir_pos(
                new_area, last_pos, math.floor(new_child_length), self.__direction,
                child_index >= len(self._children) - 1
            )
            ret.extend(child.resize(new_child_area))
        return ret

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
            'direction={direction}, is_split_target={target}, splits={splits}, children={kids})'
        ).format(
            size=repr(self.__area),
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
