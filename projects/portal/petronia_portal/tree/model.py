"""The split / portal tree model.  This is business logic built on top of the data model
defined in the extension definition."""
from abc import ABC
from typing import Sequence, List, Tuple, Iterable, Dict, Callable, Optional
import math
from petronia_common.util import EMPTY_TUPLE
from ..state import petronia_portal as portal_state
from ..events import window as window_event


class KnownWindow:
    """A window stored in the layout.  Windows have a defined target_id, a possible
    assigned position within the portal"""
    __slots__ = (
        '_target_id', '_fit', 'pos_x', 'pos_y', 'pos_w', 'pos_h',
        '_managed_state', 'managed', 'owning_portal_id', '_unmanaged_state',
    )

    def __init__(
            self,
            target_id: str, fit: Optional[portal_state.WindowPortalFit],
            managed: bool,
            window_state: window_event.WindowState,
    ) -> None:
        self._target_id = target_id
        self._fit = fit
        self._managed_state = window_state
        self._unmanaged_state = window_state
        self.owning_portal_id = -1
        self.managed = managed
        self.pos_x = window_state.location.x
        self.pos_y = window_state.location.y
        self.pos_w = window_state.location.width
        self.pos_h = window_state.location.height

    @property
    def target_id(self) -> str:
        """The window's target_id"""
        return self._target_id

    @property
    def unmanaged_native_state(self) -> window_event.WindowState:
        """Get the state of the window as reported by the native extension, before its managed."""
        return self._unmanaged_state

    @property
    def managed_native_state(self) -> window_event.WindowState:
        """Get the state of the window as reported by the native extension."""
        return self._managed_state

    def update_native_state(self, new_state: window_event.WindowState) -> None:
        """Update the window's state when the native extension reports an update."""
        # Note: this does NOT update the position or size variables!
        if self.managed:
            self._managed_state = new_state
        else:
            self._unmanaged_state = new_state

    def update_position(
            self, nw_x: int, nw_y: int, width: int, height: int,
            default_fit: portal_state.WindowPortalFit,
    ) -> bool:
        """Update the current position, and return True if changed."""
        if not self.managed:
            # Petronia does not manage this window within a portal.
            return False

        fit = self._fit or default_fit

        new_x, new_width = adjust_position(
            self.unmanaged_native_state.location.width,
            nw_x, width, fit.justify_horizontal, fit.fit_horizontal,
        )
        new_y, new_height = adjust_position(
            self.unmanaged_native_state.location.height,
            nw_y, height, fit.justify_vertical, fit.fit_vertical,
        )

        if (
            new_x == self.pos_x and
            new_y == self.pos_y and
            new_width == self.pos_w and
            new_height == self.pos_h
        ):
            return False
        self.pos_x = new_x
        self.pos_y = new_y
        self.pos_w = new_width
        self.pos_h = new_height
        return True


class Tile:
    """Abstract parent of the portal / split."""
    __slots__ = ('__pos_x', '__pos_y', '__pos_w', '__pos_h', 'rel_size')

    def __init__(self) -> None:
        self.__pos_x = 0
        self.__pos_y = 0
        self.__pos_w = 0
        self.__pos_h = 0
        self.rel_size = 1

    @property
    def pos_x(self) -> int:
        """X position of this tile"""
        return self.__pos_x

    @property
    def pos_y(self) -> int:
        """Y position of this tile"""
        return self.__pos_y

    @property
    def width(self) -> int:
        """Width of this tile"""
        return self.__pos_w

    @property
    def height(self) -> int:
        """Height of this tile"""
        return self.__pos_h

    def update_position(
            self, new_x: int, new_y: int, new_width: int, new_height: int,
    ) -> Sequence[KnownWindow]:
        """Update this tile with the new position.  Should be overridden by implementations.

        Returns all the windows that had their positions changed."""
        self.__pos_x = new_x
        self.__pos_y = new_y
        self.__pos_w = new_width
        self.__pos_h = new_height
        return EMPTY_TUPLE

    def get_minimum_size(self) -> Tuple[int, int]:
        """Get the minimum size for this tile."""
        raise NotImplementedError

    def get_contained_windows(self) -> Dict[str, KnownWindow]:
        """Return all windows contained in this tile."""
        raise NotImplementedError


class Portal(Tile):
    """Leaf node in the tree.  Contains windows.  Not thread safe."""
    __slots__ = (
        '_window_order',
        '_position',
        '_state',
        '__index',
        'minimum_size',
    )
    _PORTAL_COUNT = 0

    def __init__(self, window_order: Sequence[KnownWindow], state: portal_state.Portal) -> None:
        Tile.__init__(self)
        self._window_order = list(window_order)
        self._state = state
        self.rel_size = state.size
        self.__index = Portal._PORTAL_COUNT
        self.minimum_size = (
            state.padding_left + state.padding_right + 10,
            state.padding_top + state.padding_bottom + 10,
        )
        Portal._PORTAL_COUNT += 1

    @property
    def portal_id(self) -> int:
        """Get this portal ID"""
        return self.__index

    @property
    def window_order(self) -> Sequence[KnownWindow]:
        """Get the order of window target_ids.  Index 0 is the top-most window."""
        return tuple(self._window_order)

    @property
    def primary_alias(self) -> str:
        """Get the primary name for the portal.  This should be static and not
        change due to outside events.."""
        return self._state.portal_aliases[0]

    def get_minimum_size(self) -> Tuple[int, int]:
        """Get the minimum size for this portal."""
        return self.minimum_size

    def has_window_id(self, window_id: str) -> bool:
        """Does this portal have the window with the given target_id?"""
        for window in self._window_order:
            if window.target_id == window_id:
                return True
        return False

    def has_portal_alias(self, alias: str) -> bool:
        """Is this portal known by the given alias?"""
        return alias in self._state.portal_aliases

    def update_position(
            self, new_x: int, new_y: int, new_width: int, new_height: int,
    ) -> Sequence[KnownWindow]:
        Tile.update_position(self, new_x, new_y, new_width, new_height)
        return self._update_window_position(self._window_order)

    def rotate_windows_forward(self) -> Sequence[KnownWindow]:
        """Rotate the order of the windows, and return the new order."""
        if len(self._window_order) > 1:
            # This only makes sense to run if there is more than 1 window.
            first = self._window_order[0]
            del self._window_order[0]
            self._window_order.append(first)
        return tuple(self._window_order)

    def rotate_windows_backward(self) -> Sequence[KnownWindow]:
        """Rotate the order of the windows, and return the new order."""
        if len(self._window_order) > 1:
            # This only makes sense to run if there is more than 1 window.
            last = self._window_order[-1]
            del self._window_order[-1]
            self._window_order.insert(0, last)
        return tuple(self._window_order)

    def remove_window(self, window_id: str) -> Optional[KnownWindow]:
        """Remove the window with the given target id.  Returns True if the window was in
        the portal, and False if not."""
        new_order: List[KnownWindow] = []
        found: Optional[KnownWindow] = None
        for window in self._window_order:
            if window.target_id == window_id:
                found = window
                window.owning_portal_id = -1
            else:
                new_order.append(window)
        self._window_order = new_order
        return found

    def add_windows(
            self, windows: Iterable[KnownWindow], first: bool,
    ) -> Sequence[KnownWindow]:
        """Add the given windows into this portal.  If `first` is True, then this is added
        at the start of the list, otherwise it is added to the end of the list.

        Returns the list of windows that changed position."""
        if first:
            self._window_order = [*windows, *self._window_order]
        else:
            self._window_order.extend(windows)

        for window in windows:
            window.owning_portal_id = self.portal_id

        return self._update_window_position(windows)

    def get_contained_windows(self) -> Dict[str, KnownWindow]:
        return {
            w.target_id: w
            for w in self._window_order
        }

    def _update_window_position(self, windows: Iterable[KnownWindow]) -> Sequence[KnownWindow]:
        """Update each window in the arguments, and return those whose position has changed."""
        changed: List[KnownWindow] = []

        window_x = self.pos_x + self._state.padding_left
        window_y = self.pos_y + self._state.padding_top
        window_w = max(0, self.width - self._state.padding_left - self._state.padding_right)
        window_h = max(0, self.height - self._state.padding_top - self._state.padding_bottom)

        for window in windows:
            if window.update_position(
                    window_x, window_y, window_h, window_w, self._state.preferred_location,
            ):
                changed.append(window)

        return changed


class TileIterator(Tile, ABC):
    """A tile that contains other tiles that can be fetched."""

    def get_children(self) -> Sequence[Tile]:
        """Get all the children contained."""
        raise NotImplementedError


class TileContainer(TileIterator, ABC):
    """A layout that has multiple containers or portals within it."""
    __slots__ = ('_children', '_is_block')

    def __init__(self, is_block: bool) -> None:
        TileIterator.__init__(self)
        self._is_block = is_block
        self._children: List[Tile] = []

    @property
    def covers_screen_block(self) -> bool:
        """True if this split covers an entire screen block."""
        return self._is_block

    def get_children(self) -> Sequence[Tile]:
        """Get all the children of this split."""
        return tuple(self._children)

    def get_contained_windows(self) -> Dict[str, KnownWindow]:
        ret: Dict[str, KnownWindow] = {}
        for chd in self._children:
            ret.update(chd.get_contained_windows())
        return ret

    def add_child(self, child: Tile, front: bool, _equally_sized: bool) -> Sequence[KnownWindow]:
        """Add a new child into this split, optionally at the start.
        If equally_sized is True, then the child's relative size is ignored and instead it is set
        to 1/(total child count) relative size.
        """
        if front:
            self._children.insert(0, child)
        else:
            self._children.append(child)
        return self.update_position(self.pos_x, self.pos_y, self.width, self.height)

    def remove_child(self, tile: Tile) -> Sequence[KnownWindow]:
        """Remove the given child.  Returns the windows whose size has changed."""
        if tile in self._children:
            self._children.remove(tile)
            return self.update_position(self.pos_x, self.pos_y, self.width, self.height)
        return EMPTY_TUPLE

    def change_child_size(
            self, child_index: int, delta_x: int, delta_y: int,
    ) -> Tuple[Sequence[KnownWindow], int, int]:
        """Adjust the size of the child at the given index by the delta_x, delta_y amounts.
        If, due to sizing restrictions, the child cannot grow by the full delta amount, then
        the remaining amount is returned.  This returns:

        (windows whose size has changed, remaining delta x, remaining delta y)
        """
        raise NotImplementedError


class ScreenBlockSplit(TileContainer):
    """A tile container that covers a screen block."""
    __slots__ = ()

    def __init__(self, screen_x: int, screen_y: int, screen_w: int, screen_h: int) -> None:
        TileContainer.__init__(self, True)
        # Due to the overridden function, must call the deep parent's update function.
        Tile.update_position(
            self, screen_x, screen_y, screen_w, screen_h,
        )

    def update_position(
            self, new_x: int, new_y: int, new_width: int, new_height: int,
    ) -> Sequence[KnownWindow]:
        # The screen block can't be resized.
        raise ValueError('Cannot change the screen block size.')

    def add_child(self, child: Tile, front: bool, equally_sized: bool) -> Sequence[KnownWindow]:
        if len(self.get_children()) != 0:
            raise ValueError('a screen block can contain at most 1 child.')
        self._children.append(child)
        return child.update_position(self.pos_x, self.pos_y, self.width, self.height)

    def get_minimum_size(self) -> Tuple[int, int]:
        # Screen blocks cannot change size.
        return self.width, self.height

    def change_child_size(
            self, child_index: int, delta_x: int, delta_y: int,
    ) -> Tuple[Sequence[KnownWindow], int, int]:
        # Pass this down to the contained child.  However, screen blocks themselves
        # don't allow additional x/y adjustments for themselves, so this always returns
        # additional 0 delta.
        children = self.get_children()
        if children:
            child = children[0]
            if isinstance(child, TileContainer):
                res = child.change_child_size(0, delta_x, delta_y)
                return res[0], 0, 0
        return EMPTY_TUPLE, 0, 0


class RootContainer(TileIterator):
    """The root of the container tree."""

    __slots__ = ('_blocks',)

    def __init__(self, blocks: Iterable[ScreenBlockSplit]) -> None:
        TileIterator.__init__(self)
        self._blocks = tuple(blocks)

    def get_children(self) -> Sequence[Tile]:
        return self._blocks

    def get_contained_windows(self) -> Dict[str, KnownWindow]:
        ret: Dict[str, KnownWindow] = {}
        for chd in self.get_children():
            ret.update(chd.get_contained_windows())
        return ret

    def get_minimum_size(self) -> Tuple[int, int]:
        # Kind of meaningless here.
        return 0, 0


class SimpleSplit(TileContainer):
    """A portion of the screen that is split into other splits or portals."""
    __slots__ = ('_is_horiz',)

    def __init__(self, horizontal: bool) -> None:
        TileContainer.__init__(self, False)
        self._children: List[Tile] = []
        self._is_horiz = horizontal

    @property
    def horizontal(self) -> bool:
        """Is this split where children are aligned horizontal to each other?"""
        return self._is_horiz

    @property
    def vertical(self) -> bool:
        """Is this split where children are aligned vertically to each other?"""
        return not self._is_horiz

    def add_child(self, child: Tile, front: bool, equally_sized: bool) -> Sequence[KnownWindow]:
        """Add a new child into this split, optionally at the start.
        If equally_sized is True, then the child's relative size is ignored and instead it is set
        to 1/(total child count) relative size.
        """
        if equally_sized:
            # Adjust the rel_size of the new child based on the existing relative size.
            # The computation we're looking at is:
            # (sum(existing) + X) / (count(existing) + 1) = length
            # (due to the update_position setting the rel_size to the virtual pixel size)
            # So, the rel_size we're looking for is:
            # (length * (count(existing) + 1)) - sum(existing)
            total_length = self.width if self.horizontal else self.height
            sum_existing = sum([t.rel_size for t in self._children])
            count_existing = len(self._children)
            child.rel_size = (total_length * (count_existing + 1)) - sum_existing

        return TileContainer.add_child(self, child, front, equally_sized)

    def get_minimum_size(self) -> Tuple[int, int]:
        sum_x = 0
        sum_y = 0
        for child in self.get_children():
            min_x, min_y = child.get_minimum_size()
            sum_x += min_x
            sum_y += min_y
        return sum_x, sum_y

    def change_child_size(  # pylint:disable=too-many-locals,too-many-branches,too-many-statements
            self, child_index: int, delta_x: int, delta_y: int,
    ) -> Tuple[Sequence[KnownWindow], int, int]:
        # Keep this split's size the same, but adjust the children's size.
        children = self.get_children()
        child_count = len(children)
        if child_count <= 1 or child_index < 0 or child_index >= child_count:
            # Can't adjust at this point.
            return EMPTY_TUPLE, delta_x, delta_y

        # This is a zero-sum game.  The adjustment goes into the child, then split the difference
        # (applied negatively) to the children, with the remainder going to the next child or
        # previous child (if no next child).  Children have a minimum size; if that's exceeded,
        # remainder is passed in the return.

        # If the child is asked to be shrunk, then this will always return a 0 on that
        # axis, even if the child can't shrink below the threshold (because the other children
        # should be able to grow to recover the lost space).

        adjusted_windows: List[KnownWindow] = []

        get_primary: Callable[[int, int], int]
        get_secondary: Callable[[int, int], int]
        get_x: Callable[[int, int], int]
        get_y: Callable[[int, int], int]

        if self.horizontal:
            primary_delta_dir = delta_x
            primary_self_length = self.width
            get_primary = get_first
            secondary_delta_dir = delta_y
            secondary_self_length = self.height
            get_secondary = get_second
            get_x = get_first
            get_y = get_second
        else:
            primary_delta_dir = delta_y
            primary_self_length = self.height
            get_primary = get_second
            secondary_delta_dir = delta_x
            secondary_self_length = self.width
            get_secondary = get_first
            get_x = get_second
            get_y = get_first

        adjusted_child = children[child_index]

        # Note: Adjust secondary delta on ALL children.
        adjusted_secondary_length = secondary_self_length + secondary_delta_dir
        if secondary_delta_dir < 0:
            # Shrink; ensure the children can be shrunk that far...
            for child in children:
                adjusted_secondary_length = max(
                    adjusted_secondary_length,
                    get_secondary(*child.get_minimum_size()),
                )

        if primary_delta_dir < 0:
            # shrink the child and grow all the other children.
            min_primary = get_primary(*adjusted_child.get_minimum_size())
            child_primary_length = get_primary(adjusted_child.width, adjusted_child.height)
            adjusted_primary_length = max(min_primary, child_primary_length + primary_delta_dir)
            adjusted_primary_delta = adjusted_primary_length - child_primary_length
            # Children count is at least 2
            assert child_count > 1  # nosec
            per_child_adjustment = adjusted_primary_delta // (child_count - 1)
            # For rounding errors...
            final_child_adj = primary_delta_dir - (per_child_adjustment * (child_count - 2))
            next_primary_pos = get_primary(self.pos_x, self.pos_y)
            secondary_pos = get_secondary(self.pos_x, self.pos_y)
            for i in range(child_count):
                child = children[i]
                if i == child_index:
                    child_len = adjusted_primary_length
                else:
                    if i == 0:
                        child_len = get_primary(child.width, child.height) - final_child_adj
                    else:
                        child_len = (
                                get_primary(child.width, child.height) - per_child_adjustment
                        )
                child.rel_size = child_len
                next_primary_pos += child_len
                adjusted_windows.extend(child.update_position(
                    get_x(next_primary_pos, secondary_pos),
                    get_y(next_primary_pos, secondary_pos),
                    get_x(child_len, adjusted_secondary_length),
                    get_y(child_len, adjusted_secondary_length),
                ))
            return (
                adjusted_windows,
                get_x(adjusted_primary_delta - primary_delta_dir, adjusted_secondary_length),
                get_y(adjusted_primary_delta - primary_delta_dir, adjusted_secondary_length),
            )

        if primary_delta_dir > 0:
            # grow the child and shrink all the other children.
            # Get the expected new size of the primary child, and scan through the other children
            # to see if they end up shrinking too far.
            child_primary_length = get_primary(adjusted_child.width, adjusted_child.height)
            adjusted_child_primary_len = min(
                primary_self_length, child_primary_length + primary_delta_dir,
            )
            min_children_len = [
                get_primary(*ch.get_minimum_size())
                for ch in children
            ]
            children_len: List[int] = [
                get_primary(ch.width, ch.height)
                for ch in children
            ]
            remaining_adjustment = child_primary_length - adjusted_child_primary_len
            changed = True
            while changed and remaining_adjustment > 0:
                can_adjust_count = 0
                for i in range(child_count):
                    if i != child_index and children_len[i] > min_children_len[i]:
                        can_adjust_count += 1
                if can_adjust_count <= 0:
                    break
                adjustment = remaining_adjustment // can_adjust_count
                for i in range(child_count):
                    if remaining_adjustment <= 0:
                        break
                    if i != child_index and children_len[i] > min_children_len[i]:
                        changed = True
                        if adjustment <= 0:
                            # Remainder handling.
                            remaining_adjustment -= 1
                            children_len[i] -= 1
                        else:
                            children_len[i] -= adjustment
                            remaining_adjustment -= adjustment

            if remaining_adjustment > 0:
                adjusted_child_primary_len = min(
                    child_primary_length, adjusted_child_primary_len - remaining_adjustment,
                )
                remaining_adjustment = adjusted_child_primary_len - child_primary_length
            children_len[child_index] = adjusted_child_primary_len
            next_primary_pos = get_primary(self.pos_x, self.pos_y)
            secondary_pos = get_secondary(self.pos_x, self.pos_y)
            for i in range(child_count):
                child = children[i]
                adjusted_windows.extend(child.update_position(
                    get_x(next_primary_pos, secondary_pos),
                    get_y(next_primary_pos, secondary_pos),
                    get_x(children_len[i], adjusted_secondary_length),
                    get_y(children_len[i], adjusted_secondary_length),
                ))
                next_primary_pos += children_len[i]
            return (
                adjusted_windows,
                get_x(remaining_adjustment, adjusted_secondary_length),
                get_y(remaining_adjustment, adjusted_secondary_length),
            )

        if adjusted_secondary_length != secondary_self_length:
            # else no primary adjustment made this this one;
            # pass the delta secondary to ALL the children.

            for child in children:
                adjusted_windows.extend(child.update_position(
                    child.pos_x, child.pos_y,
                    get_x(child.width, adjusted_secondary_length),
                    get_y(child.height, adjusted_secondary_length),
                ))
            adjusted_second_delta = (
                    (secondary_self_length - secondary_delta_dir) - adjusted_secondary_length
            )

            return (
                adjusted_windows,
                get_x(primary_delta_dir, adjusted_second_delta),
                get_y(primary_delta_dir, adjusted_second_delta),
            )

        # Else no adjustments necessary.  Should already be handled above, though.
        return EMPTY_TUPLE, 0, 0  # pragma no cover

    def update_position(  # pylint:disable=too-many-locals
            self, new_x: int, new_y: int, new_width: int, new_height: int,
    ) -> Sequence[KnownWindow]:
        Tile.update_position(self, new_x, new_y, new_width, new_height)

        # Figure out how to measure out the children, based on their current relative size.
        # After this runs, the relative size will change to the absolute size (this allows
        # for adjusting the split sizes by pixels).
        # The absolute sizes are the portion of the sum of the relative sizes.

        rel_sum = sum([t.rel_size for t in self._children])

        setter = set_vert_size
        start_pos = new_y
        total_space = new_height

        if self.horizontal:
            setter = set_horiz_size
            total_space = new_width

        rel_portion = max(total_space, 1) / max(rel_sum, 1)

        next_pos = 0
        child_count = len(self._children)
        last_child_index = child_count - 1
        changed_windows: List[KnownWindow] = []
        for child_index in range(child_count):
            child = self._children[child_index]
            if child.rel_size <= 0 or child_index == last_child_index:
                # rel_size <= 0: the child takes up the rest of the space, but overlaps the next
                #   child.
                # last child: The last child takes up the rest of the space; this prevents rounding
                #                 # errors for creeping in and skipping valuable pixels.
                taken_space = total_space - next_pos
                changed_windows.extend(setter(child, next_pos + start_pos, total_space - next_pos))
            else:
                taken_space = math.floor(child.rel_size * rel_portion)
                changed_windows.extend(setter(child, next_pos + start_pos, taken_space))
                next_pos += taken_space
            child.rel_size = taken_space
        return changed_windows


JUSTIFY__FRONT = 0
JUSTIFY__CENTER = 1
JUSTIFY__BACK = 2
JUSTIFY__DEFAULT = JUSTIFY__FRONT
JUSTIFY__MAP = {
    'center': JUSTIFY__CENTER,
    'left': JUSTIFY__FRONT,
    'top': JUSTIFY__FRONT,
    'right': JUSTIFY__BACK,
    'bottom': JUSTIFY__BACK,
}


def adjust_position(
        native_length: int,
        portal_pos: int, portal_length: int,
        justify: str, fit: str,
) -> Tuple[int, int]:
    """Adjust the position and length based on the justification and fit.
    Returns pos, length."""
    # shrink, stretch, (fit), none
    justify_type = JUSTIFY__MAP.get(justify.strip().lower(), JUSTIFY__DEFAULT)
    fit_type = fit.strip().lower()

    if fit_type == 'shrink':
        if native_length >= portal_length:
            # Shrink the length to match the portal.
            return portal_pos, portal_length
        # Keep the same length, but adjust according to justification.
        # Fall through to that code.
    elif fit_type == 'stretch':
        if native_length <= portal_length:
            # stretch the length to match the portal.
            return portal_pos, portal_length
        # Keep the same length, but adjust according to justification
        # Fall through to that code.
    elif fit_type == 'none':
        # Keep the same length, but adjust according to justification
        # Fall through to that code.
        pass
    else:
        # Default is "fit"
        return portal_pos, portal_length

    # Adjust the size based on the justification.
    if justify_type == JUSTIFY__FRONT:
        return portal_pos, native_length
    if justify_type == JUSTIFY__BACK:
        return portal_pos + portal_length - native_length, native_length
    # center
    return portal_pos + (portal_length // 2) - (native_length // 2), native_length


def get_horiz_size(tile: Tile) -> Tuple[int, int]:
    """Get the current 'size' of the tile along the horizontal axis."""
    return tile.pos_x, tile.width


def get_vert_size(tile: Tile) -> Tuple[int, int]:
    """Get the current 'size' of the tile along the vertical axis."""
    return tile.pos_y, tile.height


def set_horiz_size(tile: Tile, pos: int, length: int) -> Sequence[KnownWindow]:
    """Set the size of the tile along the horizontal axis."""
    return tile.update_position(
        pos, tile.pos_y, length, tile.height,
    )


def set_vert_size(tile: Tile, pos: int, length: int) -> Sequence[KnownWindow]:
    """Set the size of the tile along the vertical axis."""
    return tile.update_position(
        tile.pos_x, pos, tile.width, length,
    )


def get_first(first: int, _second: int) -> int:
    """Return the first value."""
    return first


def get_second(_first: int, second: int) -> int:
    """Return the second value."""
    return second
