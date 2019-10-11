
"""
Convert a configuration layout to a formal structure.
"""

from typing import List, Sequence, Tuple

from .config import (
    TileLayoutConfig,
    PortalLayout,
    TileLayout,
    MatchWindowToPortal,
    match_layouts_to_screens,
)
from .root import (
    RootTile,
)
from .portal import (
    Portal,
)
from .splitter import (
    SplitterTile,
    TileFactory,
    Tile,
    SPLIT_VERTICAL,
    SPLIT_HORIZONTAL,
)
from ....core.platform.api import (
    VirtualScreenInfo,
    ScreenArea,
    WindowMatcher,
)


def convert_config(config: TileLayoutConfig, display: VirtualScreenInfo) -> Tuple[RootTile, int]:
    """
    Uses the current screen layout to convert the configuration into the
    tile layout.  It also returns which screen index in the root tile is
    the initial focused screen ("primary screen").

    :param config:
    :param display:
    :return:
    """
    screens: List[SplitterTile] = []

    screen_assignment = match_layouts_to_screens(
        [lay.screens for lay in config.layouts],
        display.blocks
    )

    primary = 0
    index = 0
    for spl, scn in screen_assignment:
        split = SplitterTile(
            mk_tile_factory(spl.layout, spl.direction, config.matchers),
            scn.area,
            spl.direction,
            get_split_children_sizes(spl.layout),
            False
        )
        if spl.primary:
            primary = index
        screens.append(split)
        index += 1

    return RootTile(screens), primary


def get_split_children_sizes(children: Sequence[TileLayout]) -> List[int]:
    ret: List[int] = []
    for kid in children:
        ret.append(kid.size)
    return ret


def find_matchers_for_name(portal_name: str, matchers: Sequence[MatchWindowToPortal]) -> List[WindowMatcher]:
    ret: List[WindowMatcher] = []
    for match in matchers:
        if match.portal_name == portal_name:
            ret.extend(match.window_matchers)
    return ret


def mk_tile_factory(
        children: Sequence[TileLayout], parent_direction: int, matchers: Sequence[MatchWindowToPortal]
) -> TileFactory:
    direction = SPLIT_VERTICAL if parent_direction == SPLIT_HORIZONTAL else SPLIT_HORIZONTAL

    def tile_factory(index: int, size: ScreenArea) -> Tile:
        if 0 <= index < len(children):
            layout = children[index]
            if isinstance(layout, PortalLayout):
                portal_name = layout.name or str(index)
                return Portal(portal_name, size, find_matchers_for_name(portal_name, matchers), None)
            else:
                return SplitterTile(
                    mk_tile_factory(layout.splits, direction, matchers),
                    size, direction, get_split_children_sizes(layout.splits), layout.is_split_target
                )
        portal_name = str(index)
        # TODO allow for setting up a background.
        return Portal(portal_name, size, find_matchers_for_name(portal_name, matchers), None)
    return tile_factory
