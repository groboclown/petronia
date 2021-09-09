
"""
Convert a configuration layout to a formal structure.
"""

from typing import List, Sequence, Tuple, Iterable

from .config import (
    TileLayoutConfig,
    PortalLayout,
    TileLayout,
    MatchWindowToPortal,
    match_layouts_to_screens,
    parse_position,
    DEFAULT_WINDOW_POSITION,
    DEFAULT_WINDOW_POSITION_VALUE,
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
from ....aid.std import i18n as _
from ....aid.std import (
    ErrorReport,
    create_user_error,
)


def convert_config(
        config: TileLayoutConfig, display: VirtualScreenInfo
) -> Tuple[RootTile, int, Iterable[ErrorReport]]:
    """
    Uses the current screen layout to convert the configuration into the
    tile layout.  It also returns which screen index in the root tile is
    the initial focused screen ("primary screen").

    :param config:
    :param display:
    :return:
    """
    screens: List[SplitterTile] = []

    packed_data, errors = match_layouts_to_screens(
        [lay.screens for lay in config.layouts],
        display.blocks
    )
    root_index, screen_assignment = packed_data
    name = '()'
    if 0 <= root_index < len(config.layouts):
        name = config.layouts[root_index].name

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
    if not screens:
        if not errors:
            errors = [create_user_error(
                convert_config, _('no screens defined in {sc}'), sc=repr(config)
            )]
        # TODO should the splitter define the default window position too?
        #   This should be inherited from the parent splitter.
        screens.append(SplitterTile(
            mk_tile_factory((PortalLayout('default', 1, DEFAULT_WINDOW_POSITION),), SPLIT_HORIZONTAL, []),
            display.get_primary().area,
            SPLIT_HORIZONTAL, [1], True
        ))

    return RootTile(name, screens, primary), primary, errors


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
                position = parse_position(layout.default_fill or DEFAULT_WINDOW_POSITION)
                if position is None:
                    position = DEFAULT_WINDOW_POSITION_VALUE

                return Portal(
                    portal_name, size, find_matchers_for_name(portal_name, matchers), position, None
                )
            else:
                return SplitterTile(
                    mk_tile_factory(layout.splits, direction, matchers),
                    size, direction, get_split_children_sizes(layout.splits), layout.is_split_target
                )
        portal_name = str(index)
        # TODO allow for setting up a background.
        return Portal(
            portal_name, size,
            find_matchers_for_name(portal_name, matchers),
            DEFAULT_WINDOW_POSITION_VALUE, None
        )
    return tile_factory
