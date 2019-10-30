
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

    def get_portal_in_split_direction(
            self, split_direction: int, direction_count: int, start_index: int
    ) -> Tuple[List[int], int]:
        if self.__direction == split_direction:
            return self.get_portal_in_direction(direction_count, start_index, True)
        active_child = self._children[self.__active_index]
        if isinstance(active_child, Portal):
            return [self.__active_index], direction_count
        path, remainder = active_child.get_portal_in_direction(direction_count, start_index, True)
        return [self.__active_index, *path], remainder

    def get_portal_in_direction(self, direction: int, start_index: int, first: bool) -> Tuple[List[int], int]:
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

        # Another example:
        # The first call is made by an outside program to find the left-by-1 window for the split, and
        # the active portal is B1b.
        # 1. The caller first calls get_active_child_index() to find the start index, which is B.
        # 2. This method is invoked with the start index, direction is -1 (left), and `first` is True.
        # 3. B, the start, is a split, and because it's a direct child, its split direction is the
        #    opposite of the original requested direction.  So the active child is checked, which is B1 (0).
        #    B1 is a split, so it must be recursed.  Because `first` is True, B1's active child is
        #    used, rather than the right-most.
        # 4. B1 is called with direction -1, start B1b (1) and `first` is True.
        # 5. B1's start is B1b, which is a Portal.
        # 6. Move left 1 (remaining direction is 0).  This gives us B1a as the active location, which is a Portal.
        # 7. Remaining direction is 0, so this is the value.  Return the index (B1a) and the remaining direction (0).
        # 8. Outer split receives a remaining direction of 0, so it returns its path (B) + the split's
        #    path (B1) + the response path (B1a).

        # Side note:
        # * If the last index was a split, and there's more moves to make which will take us outside the
        #   bounds of the split (a miss), then return the deep path in that split.  This is in case the
        #   request was for going to the end of the screen, and there's no wrap-around.

        # print("DEBUG move {0}, {1}, {2} on {3}".format(direction, start_index, first, self))

        kid_len = len(self._children)
        assert 0 <= start_index < kid_len, 'start_index out of range'
        if direction == 0:
            # Special degenerate case.  This helps with the recursion scenario.
            # print("Degenerate return {0}, 0".format(start_index))
            return [start_index], 0
        incr = 1
        if direction < 0:
            incr = -1
            direction = -direction

        current_index = start_index
        current_path = [current_index]
        while True:
            # print("Loop: dir={0}, incr={1}, curr={2}, path={3}".format(
            #     direction, incr, current_index, current_path
            # ))
            # Find the current location.
            child = self._children[current_index]
            if not isinstance(child, Portal):
                # The current location is a split.
                # Due to the alternating vertical / horizontal nature of splits, we will treat this
                # split based on what its active child is.
                split_index = child.get_active_child_index()
                split = child[split_index]
                if isinstance(split, Portal):
                    # Switch the path to treat the current child as a portal.
                    current_path = [current_index, split_index]
                    # print("  - split -> portal :: {0}".format(current_path))
                else:
                    # Split -> Split, so we need to move inside the lower split.
                    if first:
                        # Handle the special case where we're entering a split node as the very first
                        # thing we're discovering.
                        split_move_index = split.get_active_child_index()
                        # print(" - split -> split(first:{0})".format(split_move_index))
                    elif incr < 0:
                        # moving backwards, so use the last child.
                        split_move_index = split.count() - 1
                        # print(" - split -> split(backwards:{0})".format(split_move_index))
                    else:
                        # moving forwards, so use the first child.
                        split_move_index = 0
                        # print(" - split -> split(forwards:0)")
                    # Now recurse into the split so it can handle the movement.
                    next_path, next_direction = split.get_portal_in_direction(direction * incr, split_move_index, first)
                    # This is the moved-to location + remaining direction, relative to that inner split.
                    # So now it needs to be translated into this split's child location.
                    # But this is just like saying that a movement step just happened, we have
                    # that position, and now we need another movement step for this split.
                    direction = abs(next_direction)
                    current_path = [current_index, split_index, *next_path]
                    # print(" - move in split -> split returned dir={0}, path={1}".format(direction, current_path))

            # Else it's a portal, and it just needs a movement.

            # Start the movement.
            next_index = current_index + incr
            if direction == 0 or not 0 <= next_index < kid_len:
                # Movement will go outside the bounds, so return the
                # most recent valid path + remaining direction.
                # print(" - finished: {0}, {1}".format(current_path, direction * incr))
                return current_path, direction * incr
            # Next index is valid.  Use it.
            current_index = next_index
            current_path = [current_index]
            # Update direction
            direction -= 1
            # Make sure we're not considered first anymore
            first = False

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
