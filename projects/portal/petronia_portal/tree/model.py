"""The split / portal tree model.  This is business logic built on top of the data model
defined in the extension definition."""

from typing import Sequence, List, Tuple, Optional
import math
from petronia_common.util import EMPTY_TUPLE
from ..state import petronia_portal as portal_state
from ..events import window as window_event


class KnownWindow:
    """A window stored in the layout.  Windows have a defined target_id, a possible
    assigned position within the portal"""
    __slots__ = (
        '_target_id', '_fit', 'pos_x', 'pos_y', 'pos_w', 'pos_h',
        '_original_state', 'managed'
    )

    def __init__(
            self,
            target_id: str, fit: Optional[portal_state.WindowPortalFit],
            managed: bool,
            window_state: window_event.WindowState,
    ) -> None:
        self._target_id = target_id
        self._fit = fit
        self._original_state = window_state
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
    def native_state(self) -> window_event.WindowState:
        """Get the state of the window as reported by the native extension."""
        return self._original_state

    def update_native_state(self, new_state: window_event.WindowState) -> None:
        """Update the window's state when the native extension reports an update."""
        self._original_state = new_state

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
            self.native_state.location.width,
            nw_x, width, fit.justify_horizontal, fit.fit_horizontal,
        )
        new_y, new_height = adjust_position(
            self.native_state.location.height,
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


class Portal(Tile):
    """Leaf node in the tree.  Contains windows.  Not thread safe."""
    __slots__ = (
        '_window_order',
        '_position',
        '_state',
        '__index'
    )
    _PORTAL_COUNT = 0

    def __init__(self, window_order: Sequence[KnownWindow], state: portal_state.Portal) -> None:
        Tile.__init__(self)
        self._window_order = list(window_order)
        self._state = state
        self.rel_size = state.size
        self.__index = Portal._PORTAL_COUNT
        Portal._PORTAL_COUNT += 1

    @property
    def portal_id(self) -> int:
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

    def remove_window(self, window_id: str) -> bool:
        """Remove the window with the given target id.  Returns True if the window was in
        the portal, and False if not."""
        new_order: List[KnownWindow] = []
        found = False
        for window in self._window_order:
            if window.target_id == window_id:
                found = True
            else:
                new_order.append(window)
        self._window_order = new_order
        return found

    def add_windows(
            self, windows: Sequence[KnownWindow], first: bool,
    ) -> Sequence[KnownWindow]:
        """Add the given windows into this portal.  If `first` is True, then this is added
        at the start of the list, otherwise it is added to the end of the list.

        Returns the list of windows that changed position."""
        if first:
            self._window_order = [*windows, *self._window_order]
        else:
            self._window_order.extend(windows)

        return self._update_window_position(windows)

    def _update_window_position(self, windows: Sequence[KnownWindow]) -> Sequence[KnownWindow]:
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


class TileContainer(Tile):
    """A layout that has multiple containers or portals within it."""
    __slots__ = ('_children', '_is_block')

    def __init__(self, is_block: bool) -> None:
        Tile.__init__(self)
        self._is_block = is_block
        self._children: List[Tile] = []

    @property
    def covers_screen_block(self) -> bool:
        """True if this split covers an entire screen block."""
        return self._is_block

    def get_children(self) -> Sequence[Tile]:
        """Get all the children of this split."""
        return tuple(self._children)

    def add_child(self, child: Tile, front: bool, equally_sized: bool) -> Sequence[KnownWindow]:
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
        return ()


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

    def update_position(
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
            setter = get_vert_size
            total_space = new_width

        rel_portion = total_space / rel_sum

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
