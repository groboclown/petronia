"""Logic for actions between portals, splits, and windows."""

from typing import Sequence, Tuple, List, Iterable, Set, Dict, Callable, Optional
from petronia_common.util import EMPTY_TUPLE
from . import model, navigation
from ..state import petronia_portal as portal_state
from ..state import screen as screen_state
from ..events import window as window_event


class OptimizedTileTree:
    """The whole tile tree, with optimizations for performance.  This is not thread safe."""
    __slots__ = ('__root', '__portals_by_id', '__windows_by_id', '__screen_uninitialized')

    def __init__(self) -> None:
        self.__screen_uninitialized = True
        initial_portal = OptimizedTileTree.create_default_portal()
        self.__root = OptimizedTileTree.create_default_root(initial_portal)
        self.__portals_by_id = {initial_portal.portal_id: initial_portal}
        self.__windows_by_id: Dict[str, model.KnownWindow] = {}

    def is_initialized(self) -> bool:
        """Is the tree initialized with a screen?"""
        return not self.__screen_uninitialized

    def get_window_by_id(self, window_id: str) -> Optional[model.KnownWindow]:
        """Get the window with the given ID, if it exists."""
        return self.__windows_by_id.get(window_id)

    def get_known_windows(self) -> Iterable[model.KnownWindow]:
        """Get all known windows, both managed and unmanaged."""
        return tuple(self.__windows_by_id.values())

    def get_portal_by_id(self, portal_id: int) -> Optional[model.Portal]:
        """Get the portal with the given ID, if it exists."""
        return self.__portals_by_id.get(portal_id)

    def get_portal_by_alias(self, portal_alias: str) -> Optional[model.Portal]:
        """Get the portal with the given alias, if it exists."""
        if self.__screen_uninitialized:
            return None
        for portal in self.__portals_by_id.values():
            if portal.has_portal_alias(portal_alias):
                return portal
        return None

    def get_default_portal(self) -> model.Portal:
        """Find the default portal.  Portals named 'default' are used first, then the portal with
        the lowest ID."""
        # Developer check; this should always be true.
        assert len(self.__portals_by_id) > 0  # nosec
        lowest_id: Optional[model.Portal] = None
        for portal in self.__portals_by_id.values():
            if portal.has_portal_alias('default'):
                return portal
            if lowest_id is None or portal.portal_id < lowest_id.portal_id:
                lowest_id = portal

        # should be guaranteed due to how block always has a portal.
        assert lowest_id is not None  # nosec

        return lowest_id

    def register_window(
            self,
            target_id: str, fit: Optional[portal_state.WindowPortalFit],
            window_state: window_event.WindowState,
    ) -> Optional[model.KnownWindow]:
        """Add the window to the tile tree registration."""
        if self.get_window_by_id(target_id) is not None:
            # It was already registered.
            return None
        window = model.KnownWindow(target_id, fit, False, window_state)
        self.__windows_by_id[target_id] = window
        return window

    def move_window_to_portal_id(
            self, window_id: str, target_portal_id: int, make_first: bool,
            manage: bool,
    ) -> Sequence[model.KnownWindow]:
        """Move the window to the target portal.  If the window is associated with a different
        portal, then it is first removed from that portal.  If the window was not registered
        to the tree, then it is re-added into the tree only if manage is True.  If the screen is
        not initialized yet, then it will be registered.

        Returns windows that have changed size and/or position.
        """
        window = self.get_window_by_id(window_id)
        target_portal = self.get_portal_by_id(target_portal_id)
        if (
                not window
                or not target_portal
                or (not manage and not window.managed)
                or window.owning_portal_id == target_portal_id
        ):
            return EMPTY_TUPLE

        window.managed = True

        source_portal = self.get_portal_by_id(window.owning_portal_id)
        if source_portal:
            source_portal.remove_window(window_id)
            # if that call returned True, then it was removed.  Is there anything
            # in that source portal that would require a change to other contained
            # windows?
        return target_portal.add_windows((window,), make_first)

    def remove_window(self, window_id: str, destroyed: bool) -> Sequence[model.KnownWindow]:
        """Remove the window from the tree because it was destroyed or unmanaged.
        If it is marked as destroyed,
        it will not be in the list of returned windows, otherwise the window will be restored
        to its pre-managed size and returned in the list.

        Returns windows that have changed size and/or position.
        """
        window = self.get_window_by_id(window_id)
        if not window:
            return EMPTY_TUPLE
        owning_portal = self.get_portal_by_id(window.owning_portal_id)
        if owning_portal:
            # window was managed.
            removed_window = owning_portal.remove_window(window_id)
            assert removed_window is not None  # nosec  # this should never happen.
        if destroyed:
            del self.__windows_by_id[window_id]
            return EMPTY_TUPLE

        # Not destroyed, so it's now unmanaged.
        if not window.managed:
            # Already unmanaged.
            return EMPTY_TUPLE
        window.managed = False
        original_location = window.unmanaged_native_state.location
        window.pos_x = original_location.x
        window.pos_y = original_location.y
        window.pos_w = original_location.width
        window.pos_h = original_location.height
        return [window]

    def change_screen_layout(  # pylint:disable=too-many-locals
            self,
            screens: Sequence[Tuple[
                screen_state.VirtualScreenBlock,
                portal_state.LayoutSplit,
            ]],
            get_assigned_windows: Callable[
                [portal_state.Portal, Sequence[model.KnownWindow]],
                Iterable[model.KnownWindow],
            ],
    ) -> Sequence[model.KnownWindow]:
        """Change the portal layouts based on the new screen blocks.

        The get_assigned_windows callback should return the windows that the given
        portal should contain.

        Returns windows that have changed size and/or position.
        """
        if len(screens) <= 0:
            # Do not change.  This is a terrible scenario, and probably means a bug.
            return []
        self.__screen_uninitialized = False
        print("[PORTAL] screen layout changing")
        self.__portals_by_id.clear()
        blocks: List[model.ScreenBlockSplit] = []

        changed_windows: List[model.KnownWindow] = []
        remaining_windows: List[model.KnownWindow] = []
        for window in self.__windows_by_id.values():
            if window.managed:
                remaining_windows.append(window)

        for screen_block, layout_split in screens:
            block_split = model.ScreenBlockSplit(
                screen_block.nw_x_pixel, screen_block.nw_y_pixel,
                screen_block.width, screen_block.height,
            )
            blocks.append(block_split)
            screen_stack: List[Tuple[model.TileContainer, portal_state.SplitContent]] = []
            primary_split = _add_children_to_stack(screen_stack, block_split, layout_split)
            found_splits: List[model.SimpleSplit] = [primary_split]

            while screen_stack:
                next_tuple = screen_stack.pop(0)
                assert next_tuple is not None  # nosec  # ensured because of while stack.
                parent_container, content_def = next_tuple
                content_value = content_def.value
                if isinstance(content_value, portal_state.Portal):
                    contained_windows = tuple(get_assigned_windows(
                        content_value, remaining_windows,
                    ))
                    changed_windows.extend(contained_windows)
                    for cws in contained_windows:
                        remaining_windows.remove(cws)
                    portal = model.Portal(contained_windows, content_value)
                    self.__portals_by_id[portal.portal_id] = portal
                    parent_container.add_child(portal, False, False)
                elif isinstance(content_value, portal_state.LayoutSplit):
                    child_split = _add_children_to_stack(
                        screen_stack, parent_container, content_value,
                    )
                    found_splits.append(child_split)

            # Ensure all simple splits have at least one child.
            for child_split in found_splits:
                if len(child_split.get_children()) <= 0:
                    # Incorrectly defined child.  Need to add a portal.
                    print('[PORTAL] bad config; missing portal on a split.')
                    portal = OptimizedTileTree.create_default_portal()
                    self.__portals_by_id[portal.portal_id] = portal
                    child_split.add_child(portal, False, False)

        self.__root = model.RootContainer(blocks)

        if remaining_windows:
            changed_windows.extend(self.get_default_portal().add_windows(remaining_windows, False))

        # Ensure the developer logic is valid.
        assert len(self.__portals_by_id) > 0  # nosec

        print('[PORTAL] Updated layout tree:')
        tile_stack: List[Tuple[str, model.Tile]] = [(' *', self.__root)]
        while tile_stack:
            next_indent, next_tile = tile_stack.pop(0)
            size_text = (
                f'({next_tile.pos_x}, {next_tile.pos_y}) x '
                f'({next_tile.width}, {next_tile.height})'
            )
            if isinstance(next_tile, model.TileIterator):
                print(f'{next_indent} > {repr(next_tile)} {size_text}')
                for child in next_tile.get_children():
                    tile_stack.append((next_indent + '*', child))
            else:
                print(f'{next_indent} = {size_text}')
                for wnd in next_tile.get_contained_windows():
                    print(f'{next_indent} . {repr(wnd)}')

        return changed_windows

    def get_target_portal(self, source_portal_id: int, direction: str) -> int:
        """Finds the target portal ID.  If a non-direction is given, it's interpreted as
        a portal alias, and if that is not found, a -1 is returned.  If a direction is given,
        then a best attempt is made to find the destination, which may be the source portal.
        If the source portal is not known, then -1 is returned."""
        source_portal = self.get_portal_by_id(source_portal_id)
        if not source_portal:
            return -1
        source_path = navigation.get_path_for_portal_id(self.__root, source_portal_id)
        drn = direction.strip().lower()
        wrap = navigation.WRAP_MODE__NONE
        ret: Optional[model.Portal]
        if drn.startswith('wrap-screen-'):
            drn = drn[12:]
            wrap = navigation.WRAP_MODE__SCREEN
        elif drn.startswith('wrap-block-'):
            drn = drn[11:]
            wrap = navigation.WRAP_MODE__BLOCK
        if drn in ('forward', 'forwards', 'next'):
            ret_path = navigation.navigate_next(self.__root, source_path, wrap)
            target_portal = ret_path[0][1]
            # dev check; should always be true
            assert isinstance(target_portal, model.Portal)  # nosec
            ret = target_portal
        elif drn in ('backward', 'backwards', 'previous', 'prev'):
            ret_path = navigation.navigate_previous(self.__root, source_path, wrap)
            target_portal = ret_path[0][1]
            # dev check; should always be true
            assert isinstance(target_portal, model.Portal)  # nosec
            ret = target_portal
        elif drn in ('north', 'up'):
            ret = navigation.navigate_up(self.__root, source_path, wrap)
        elif drn in ('south', 'down'):
            ret = navigation.navigate_down(self.__root, source_path, wrap)
        elif drn in ('west', 'left'):
            ret = navigation.navigate_left(self.__root, source_path, wrap)
        elif drn in ('east', 'right'):
            ret = navigation.navigate_right(self.__root, source_path, wrap)
        else:
            # Not a known direction; choose aliases.
            ret = self.get_portal_by_alias(direction)
            if ret:
                return ret.portal_id
            # If searching by alias, then this can fail to find something.
            return -1
        if ret is not None:
            # This should always be true.
            return ret.portal_id

        # Nothing found, so use the source.
        return source_portal_id

    @staticmethod
    def create_default_portal() -> model.Portal:
        """Create a default portal object."""
        return model.Portal(EMPTY_TUPLE, portal_state.Portal(
                1, portal_state.WindowPortalFit('left', 'top', 'fit', 'fit'),
                0, 0, 0, 0, [],
            ))

    @staticmethod
    def create_default_root(initial_portal: model.Portal) -> model.RootContainer:
        """Create the default top-level split."""

        screen_block = model.ScreenBlockSplit(0, 0, 0, 0)

        split = model.SimpleSplit(True)
        split.add_child(initial_portal, True, True)
        screen_block.add_child(split, True, True)

        initial_portal.update_position(0, 0, 0, 0)

        root_split = model.RootContainer([screen_block])
        return root_split

    def change_portal_size(
            self, portal_id: int, delta_x: int, delta_y: int,
    ) -> Sequence[model.KnownWindow]:
        """Change the given portal's size in the x/y directions."""

        # First, the trivial case.
        if delta_x == 0 and delta_y == 0:
            return EMPTY_TUPLE

        # This needs to search up the tree.  The adjustment direction may cause the parent
        # split to change size.  This can't change a screen block or the direct split inside
        # the screen block.

        portal_path = navigation.get_path_for_portal_id(self.__root, portal_id)

        # element 0 == block index, element 1 == split inside the block.  If length of the
        # path is <= 2, then it's a portal that can't be resized.  Or length 0 means the
        # id wasn't found.
        if len(portal_path) <= 2:
            return EMPTY_TUPLE

        changed_windows: Set[model.KnownWindow] = set()

        # Edge case possibilities here:
        #   * A portal is contained in a single-child split (meaning the portal is all alone).
        #     Here, the portal can't change relative size within the split, so instead the split
        #     must be expanded within its parent.
        #   * A portal expands in size, which causes the neighbors to shrink, but the neighbors
        #     are already at the smallest allowed size, so the contained split must grow.

        path_len = len(portal_path)
        parent_path_index = 1
        while parent_path_index < path_len and (delta_x != 0 or delta_y != 0):
            child_index, _child_item = portal_path[parent_path_index + 1]
            _parent_index, parent_split = portal_path[parent_path_index]
            if isinstance(parent_split, model.TileContainer):
                adjusted_windows, delta_x, delta_y = parent_split.change_child_size(
                    child_index, delta_x, delta_y,
                )
                changed_windows.update(adjusted_windows)

            parent_path_index += 1

        return tuple(changed_windows)

    def split_portal(
            self,
            active_portal_id: int,
            _add_before: bool,
            _new_direction: bool,
    ) -> Sequence[model.KnownWindow]:
        """Split the active portal into two portals.

        Returns windows that have changed size and/or position.
        """
        print(f"[PORTAL NOT IMPLEMENTED] split {active_portal_id} in half")
        return []

    def join_portals(
            self,
            active_portal_id: int,
            _join_before: bool,
    ) -> Sequence[model.KnownWindow]:
        """Join the active portal with an adjacent one.

        Returns windows that have changed size and/or position.
        """
        print(f"[PORTAL NOT IMPLEMENTED] join {active_portal_id}")
        return []

    def refit_window_in_portal(
            self, window_id: str, fit: portal_state.WindowPortalFit,
    ) -> Sequence[model.KnownWindow]:
        """Change the fit attribute of the window ID."""
        raise NotImplementedError


def _add_children_to_stack(
        stack: List[Tuple[model.TileContainer, portal_state.SplitContent]],
        parent: model.TileContainer,
        current: portal_state.LayoutSplit,
) -> model.SimpleSplit:
    """Handle the adding the current node to its parent, and adding the children of
    the current node into the stack.  This includes updating the relative size of the
    layouts to work right when added into the current node."""
    current_split = model.SimpleSplit(current.direction == model.DIRECITON_HORIZONTAL)
    current_split.rel_size = current.size
    parent.add_child(current_split, False, False)

    # At this point, the current_split size is set.  This allows changing the
    # relative size of the children to now be a pixel-perfect size.
    current_split.predict_children_sizes(current.contents)

    for content in current.contents:
        stack.append((current_split, content))

    return current_split
