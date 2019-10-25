
"""
The general container type.
"""

from typing import List, Sequence, Tuple, Iterable, Callable, Optional, Union
from typing import cast as t_cast
import math
from ....aid.std import (
    ComponentId,
    EMPTY_LIST
)
from ....core.platform.api import (
    ScreenUnit,
    ScreenArea,
    SCREEN_AREA_X,
    SCREEN_AREA_Y,
    SCREEN_AREA_HEIGHT,
    SCREEN_AREA_WIDTH,
    WindowMatcher,
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

    # TODO add a higher-level interface for a "layout tile", which knows how
    #   to place the portals inside it.  This puts more of the responsibility on the
    #   layout to figure out what navigation directions mean.

    __slots__ = (
        '_children',
        '__area',
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
        self.__area = size
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

    @property
    def is_split_target(self) -> bool:
        return self.__is_split_target

    def get_area(self) -> ScreenArea:
        return self.__area

    def get_portal_in_direction(self, direction: int, start_index: int) -> Tuple[List[int], int]:
        """
        Finds the next portal `direction` count away from the start index.
        This assumes that the current split is the expected axis of movement.

        The `direction` being positive means increasing the index from the start,
        and negative means decreasing the index from the start.  This may need
        to look inside child splits to get the next portal.
        If the direction is more than the split contains, then it returns as the
        second number the remaining direction count to continue in that direction,
        but for a parent to figure out.

        Returns the path to the next portal, relative to this splitter, and the
        remaining direction.
        """

        # Complex example that needs to be accounted for:
        # This split:
        #  +---------+--------+----------+------------------+
        #  |         |        |          |                  |
        #  |         |  B1a   | B1b      |                  |
        #  |         |        |          |                  |
        #  |   A     +--------+----------+      C           |
        #  |         |                   |                  |
        #  |         |       B2          |                  |
        #  |         |                   |                  |
        #  +---------+-------------------+------------------+

        # Start on A, move left 3 over to C.  In this case, let's say that B1b is the last B/B1 active portal.
        # 1. A, the start, is a portal.
        # 2. Move left 1 (2 remaining).  This is B.  However, B is a split with 2 children, B1 and B2.
        #    B indicates that B1 is active.  Because B is a split, its internal direction
        #    is up/down (not left/right), so it must be taken into account its own children.
        #    * B1 is also a split, so it's in the same left/right direction we care about, so
        #      it must be recursively descended.  Because the parent is moving left/right,
        #      we can't take into account B1's active state.
        #    * B1's left-most child (because we're moving left-to-right) is B1a.
        #    * We're on B1, looking at child B1a, with 2 more left moves to make.  Recurse.
        #           a. B1a, the start, is a portal.
        #           b. Move left 1 (1 remaining).  This is B1b.  B1b is a portal, so continue looking 1 more time.
        #           c. Move left 1 (0 remaining).  This is outside the bounds of the split, so it's a miss.
        #              We're done looking, so return the last index found (1), along with the remaining
        #              moves (0) plus the missed move (1).
        # 4. Recursion into B1 tells us that there's more work to do (remaining moves = 1 > 0).  So continue the
        #    move left, based on the "current" split of B.
        # 5. Move left 1 (0 moves left).  This is C.  C is a portal.
        #    Remaining moves is 0, so return with C (path is (2)).

        # Another example:
        # Start on A, move left 2 over to B1b.  In this case, let's say that B1b is the last B/B1 active portal.
        # 1. A, the start, is a portal.
        # 2. Move left 1 (1 remaining).  This is B.  However, B is a split with 2 children, B1 and B2.
        #    B indicates that B1 is active.  Because B is a split, its internal direction
        #    is up/down (not left/right), so it must be taken into account its own children.
        #    * B1 is also a split, so it's in the same left/right direction we care about, so
        #      it must be recursively descended.  Because the parent is moving left/right,
        #      we can't take into account B1's active state.
        #    * B1's left-most child (because we're moving left-to-right) is B1a.
        #    * We're on B1, looking at child B1a, with 1 more left move to make.  Recurse.
        #           a. B1a, the start, is a portal.
        #           b. Move left 1 (0 remaining).  This is B1b.  B1b is a portal.
        #              With 0 remaining on a portal, this is the destination.  So return
        #              the last index found (1) along with the remaining moves (0).
        # 3. Recursion into B1 tells us that there's no more work to do (remaining moves == 0).
        #    So return this path into B > B1 + the recursion result (path (1)), which is the path (1, 0, 1).

        # Another example:
        # Start on A, move left 3 over to C.  In this case, let's say that B2 is the last B active portal.
        # 1. A, the start, is a portal.
        # 2. Move left 1 (1 remaining).  This is B.  However, B is a split with 2 children, B1 and B2.
        #    B indicates that B2 is active.  Because B is a split, its internal direction
        #    is up/down (not left/right), so it must be taken into account its own children.
        #    * B2 is a portal, so act as though B > B2 is a single step.
        #    * There is another move left, so continue from B.
        # 3. Move left 1 (1 remaining).  This is C.  C is a portal.
        # 4. Move left 1 (0 remaining).  This is outside the bounds of the split, so it's a miss.
        #    We're done looking, so return the last index found (2), along with the remaining moves(0) plus
        #    the missed move (1).

        # Side note:
        # * If the last index was a split, and there's more moves to make which will take us outside the
        #   bounds of the split (a miss), then return the deep path in that split.  This is in case the
        #   request was for going to the end of the screen, and there's no wrap-around.

        kid_len = len(self._children)
        assert 0 <= start_index < kid_len, 'start_index out of range'
        if direction == 0:
            return [start_index], 0
        incr = 1
        if direction < 0:
            incr = -1
            direction = -direction

        # FIXME this code is almost right, but because of the above analysis, this code should be
        #   re-written to better match that analysis.

        # Increase direction count by 1.  This is because the first pass in the
        # loop below will find what the starting index is, before the move.
        direction += 1

        next_index = start_index
        while True:
            child = self._children[next_index]
            if not isinstance(child, Portal):
                # child == a split
                # This is a split, which means that it's in the wrong direction
                # from what we want.  This inner split's active child is the
                # thing we will move a direction against.  Note that the movement
                # is based on this intermediary's active child, which generally means
                # the previously active child.
                active_child_index = child.get_active_child_index()
                split = child[active_child_index]
                if not isinstance(split, Portal):
                    # Need to move this direction step on this deep split.
                    # It starts at the beginning of the deep split, not its active
                    if incr < 0:
                        # start at end
                        split_index = split.count() - 1
                    # subtract 1 from direction, to account for the original increase by 1.
                    split_path, direction = split.get_portal_in_direction((direction - 1) * incr, split_index)
                    if direction == 0:
                        # This is what we want...
                        return [next_index, *split_path], 0
                    if direction < 0:
                        assert incr < 0
                        direction = -direction
                # Else this child split's active child is a portal, which means we can treat this
                # child split the same as we treat a portal.  The one caveat is if it's the
                # destination for the direction, in which case the returned path must be
                # for the deep path.
                elif direction == 1:
                    # The final destination is this inner portal.
                    return [next_index, child.get_active_child_index()], 0
                # else it's a portal, and the next movement (because direction > 1)

            # else, it's a portal, which means that it can be used as a
            # stop in the direction.
            direction -= 1
            if direction <= 0 or not 0 <= (next_index + incr) < kid_len:
                # Do not increase the next position if there's no more direction,
                # or if it will take the loop outside the bounds.
                break
            next_index += incr

        return [next_index], direction * incr

    def get_active_child(self) -> Tile:
        return self._children[self.__active_index]

    def get_active_child_index(self) -> int:
        return self.__active_index

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

    def set_active_split(self, pos: int) -> None:
        # Note: always at least 1 child
        self.__active_index = abs(pos % len(self._children))

    def set_active_split_path(self, path: Sequence[int]) -> None:
        path_len = len(path)
        if path_len > 0:
            self.set_active_split(path[0])
            if path_len > 1:
                child = self._children[self.__active_index]
                if not isinstance(child, Portal):
                    child.set_active_split_path(path[1:])

    def set_active_window(self, cid: ComponentId) -> Sequence[int]:
        for child_index in range(len(self._children)):
            child = self._children[child_index]
            if isinstance(child, Portal):
                if child.set_visible_window(cid):
                    # found the destination
                    self.__active_index = child_index
                    return child_index,
                return t_cast(Sequence[int], EMPTY_LIST)
            found = child.set_active_window(cid)
            if found:
                self.__active_index = child_index
                return (child_index, *found)
        return t_cast(Sequence[int], EMPTY_LIST)

    def change_active_split(self, adjustment: int) -> None:
        """

        :param adjustment:
        :return: the cid of the now-active portal's
        """
        self.set_active_split(self.__active_index + adjustment)

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

        #size = blah
        #portal = Portal('', size, t_cast(Iterable[WindowMatcher], EMPTY_LIST))

        #self.__active_index = -1
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
        #if len(self._children) <= 0:
        #    return ()
        #self.__active_index -= 1
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
            'active={active}, direction={direction}, is_split_target={target}, splits={splits}, children={kids})'
        ).format(
            size=repr(self.__area),
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
