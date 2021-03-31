"""Logic for actions between portals, splits, and windows."""

from typing import Sequence, Tuple, Dict
from petronia_common.util import EMPTY_TUPLE
from . import model
from ..state import petronia_portal as portal_state
from ..state import screen as screen_state


def add_window(
        config: portal_state.ConfigurationState,
        root: model.RootContainer,
        window: model.KnownWindow,
) -> Sequence[model.KnownWindow]:
    """Add a new window into the existing tree.  Either it was created or became managed.

    Returns windows that have changed size and/or position.
    """


def remove_window(
        root: model.RootContainer,
        window: model.KnownWindow,
) -> Sequence[model.KnownWindow]:
    """Remove the window from the existing tree.  Either it was destroyed or became unmanaged.

    Returns windows that have changed size and/or position.
    """


def move_window(
        root: model.RootContainer,
        window: model.KnownWindow,
        target: str,
) -> Sequence[model.KnownWindow]:
    """Move a window from one portal to another.

    Returns windows that have changed size and/or position.
    """
    target_portal_id = find_portal_target(root, window.owning_portal_id, target)
    if target_portal_id == window.owning_portal_id or target_portal_id < 0:
        # Did not change contained portal.
        return EMPTY_TUPLE
    raise NotImplementedError


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


def change_screen_layout(
        root: model.RootContainer,
        screens: Sequence[Tuple[
            screen_state.VirtualScreenBlock,
            portal_state.LayoutSplit,
        ]],
) -> Sequence[model.KnownWindow]:
    """Change the portal layouts based on the new screen blocks.

    Returns windows that have changed size and/or position.
    """
    return root.on_screen_change([
        (
            block.nw_x_pixel, block.nw_y_pixel, block.width, block.height,
            BlockHandler(split).callback,
        )
        for block, split in screens
    ])


class BlockHandler:
    """Handles generating the portals and splits within a screen block."""
    __slots__ = ('block_config',)

    def __init__(self, block_config: portal_state.LayoutSplit) -> None:
        self.block_config = block_config

    def callback(
            self, block: model.ScreenBlockSplit, remaining_windows: Dict[str, model.KnownWindow],
    ) -> Sequence[model.KnownWindow]:
        """Screen change callback."""
