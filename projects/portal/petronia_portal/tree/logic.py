"""Logic for actions between portals, splits, and windows."""

from typing import Sequence, Tuple, Dict, Optional
from petronia_common.util import EMPTY_TUPLE
from . import model, navigation
from ..state import petronia_portal as portal_state
from ..state import screen as screen_state
from ..events import window as window_event


class OptimizedTileTree:
    """The whole tile tree, with optimizations for performance.  This is not thread safe."""
    __slots__ = ('__root', '__portals_by_id', '__windows_by_id')

    def __init__(self) -> None:
        initial_portal = model.Portal(EMPTY_TUPLE, portal_state.Portal(
                1, portal_state.WindowPortalFit('left', 'top', 'fit', 'fit'),
                0, 0, 0, 0, [],
            ))
        self.__root = OptimizedTileTree.create_default_root(initial_portal)
        self.__portals_by_id = {initial_portal.portal_id: initial_portal}
        self.__windows_by_id: Dict[str, model.KnownWindow] = {}

    def get_window_by_id(self, window_id: str) -> Optional[model.KnownWindow]:
        """Get the window with the given ID, if it exists."""
        return self.__windows_by_id.get(window_id)

    def get_portal_by_id(self, portal_id: int) -> Optional[model.Portal]:
        """Get the portal with the given ID, if it exists."""
        return self.__portals_by_id.get(portal_id)

    def register_window(
            self,
            target_id: str, fit: Optional[portal_state.WindowPortalFit],
            window_state: window_event.WindowState
    ) -> Optional[model.KnownWindow]:
        """Add the window to the tile tree registration.  If it should be managed, then
        a follow-up call should be made to `move_window`."""
        if self.get_window_by_id(target_id) is not None:
            # It was already registered.
            return None
        window = model.KnownWindow(target_id, fit, False, window_state)
        self.__windows_by_id[target_id] = window
        return window

    def move_window_to_portal_id(
            self, window_id: str, target_portal_id: int, make_first: bool,
    ) -> Sequence[model.KnownWindow]:
        """Move the window to the target portal.  If the window is associated with a different
        portal, then it is first removed from that portal.  If the window was not registered
        to the tree, then nothing happens.

        Returns windows that have changed size and/or position.
        """
        window = self.get_window_by_id(window_id)
        target_portal = self.get_portal_by_id(target_portal_id)
        if not window or not target_portal or not window.managed:
            return EMPTY_TUPLE

        source_portal = self.get_portal_by_id(window.owning_portal_id)
        if source_portal:
            source_portal.remove_window(window_id)
            # if that call returned True, then it was removed.  Is there anything
            # in that source portal that would require a change to other contained
            # windows?
        return target_portal.add_windows((window,), make_first)

    def remove_window(self, window_id: str, destroyed: bool) -> Sequence[model.KnownWindow]:
        """Remove the window from the tree because it was destroyed.  If it is marked as destroyed,
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

    def change_screen_layout(
            self,
            screens: Sequence[Tuple[
                screen_state.VirtualScreenBlock,
                portal_state.LayoutSplit,
            ]],
    ) -> Sequence[model.KnownWindow]:
        """Change the portal layouts based on the new screen blocks.

        Returns windows that have changed size and/or position.
        """
        return self.__root.on_screen_change([
            (
                block.nw_x_pixel, block.nw_y_pixel, block.width, block.height,
                BlockHandler(split).callback,
            )
            for block, split in screens
        ])

    @staticmethod
    def create_default_root(initial_portal: model.Portal) -> model.RootContainer:
        """Create the default top-level split."""

        def child_callback(
                block: model.ScreenBlockSplit, windows: Dict[str, model.KnownWindow],
        ) -> Sequence[model.KnownWindow]:
            initial_portal.add_windows(windows.values(), False)
            windows.clear()

            split = model.SimpleSplit(True)
            split.add_child(initial_portal, True, True)

            block.add_child(split, True, True)

            return initial_portal.update_position(0, 0, 0, 0)

        root_split = model.RootContainer()
        root_split.on_screen_change(
            (
                (0, 0, 0, 0, child_callback),
            ),
        )
        return root_split


def split_portal(
        root: model.RootContainer,
        active_portal_id: int,
        add_before: bool,
        new_direction: bool,
) -> Sequence[model.KnownWindow]:
    """Split the active portal into two portals.

    Returns windows that have changed size and/or position.
    """


def join_portals(
        root: model.RootContainer,
        active_portal_id: int,
        join_before: bool,
) -> Sequence[model.KnownWindow]:
    """Join the active portal with an adjacent one.

    Returns windows that have changed size and/or position.
    """


def find_portal_target(
        root: model.RootContainer,
        source_portal_id: int,
        target: str,
) -> int:
    """Finds the target portal based on the target, which can be a direction or
    a portal id.  If the target portal can't be found, then the source portal is returned.
    """


class BlockHandler:
    """Handles generating the portals and splits within a screen block."""
    __slots__ = ('block_config',)

    def __init__(self, block_config: portal_state.LayoutSplit) -> None:
        self.block_config = block_config

    def callback(
            self, block: model.ScreenBlockSplit, remaining_windows: Dict[str, model.KnownWindow],
    ) -> Sequence[model.KnownWindow]:
        """Screen change callback."""
