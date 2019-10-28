
"""
Process the configuration.
"""

from typing import List, Optional, Union
from typing import cast as t_cast
import re
from .....aid.std import (
    ErrorReport,
    ResultWithErrors,
    create_user_error,
)
from .....base.util.simple_type import (
    PersistType,
    PersistTypeSchemaItem,
    readonly_persistent_schema_copy,
    PERSISTENT_TYPE_SCHEMA_TYPE__STR,
    PERSISTENT_TYPE_SCHEMA_TYPE__BOOL,
    PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT,
    PERSISTENT_TYPE_SCHEMA_TYPE__REF,
    PERSISTENT_TYPE_SCHEMA_TYPE__ID,
    PERSISTENT_TYPE_SCHEMA_NAME__SCHEMA,
    collect_errors,
    with_key_as_list,
    list_of_maps,
    optional_str,
    optional_bool,
    optional_int,
    NO_ERRORS,
)
from .....core.platform.api import (
    WindowMatcher,
    WINDOW_MATCH_EXACT,
    WINDOW_MATCH_PART,
    WINDOW_MATCH_GLOB,
    WINDOW_MATCH_REGEX,
    ScreenSize,
)
from .layout import (
    RootTileLayout,
    ScreenTileLayout,
    SplitTileLayout,
    PortalLayout,
)
from .match import (
    MatchWindowToPortal,
)
from .config import (
    TileLayoutConfig,
)
from ..splitter import (
    SPLIT_HORIZONTAL,
    SPLIT_VERTICAL,
)
from ..portal import (
    POSITION_FAVOR_FILL,
    POSITION_FAVOR_N_EDGE,
    POSITION_FAVOR_E_EDGE,
    POSITION_FAVOR_S_EDGE,
    POSITION_FAVOR_W_EDGE,
    POSITION_FAVOR_NE,
    POSITION_FAVOR_SE,
    POSITION_FAVOR_NW,
    POSITION_FAVOR_SW,
    POSITION_FAVOR_RESTRICTED_N_EDGE,
    POSITION_FAVOR_RESTRICTED_E_EDGE,
    POSITION_FAVOR_RESTRICTED_S_EDGE,
    POSITION_FAVOR_RESTRICTED_W_EDGE,
    POSITION_FAVOR_RESTRICTED_NE,
    POSITION_FAVOR_RESTRICTED_SE,
    POSITION_FAVOR_RESTRICTED_NW,
    POSITION_FAVOR_RESTRICTED_SW,
)
from ..consts import (
    MOVE_WINDOW_DIRECTION_NORTH,
    MOVE_WINDOW_DIRECTION_EAST,
    MOVE_WINDOW_DIRECTION_SOUTH,
    MOVE_WINDOW_DIRECTION_WEST,
)

_PORTAL_SCHEMA = {
    'name': PersistTypeSchemaItem(
        "An optional name for the portal, for use with matching or quick focus on key bindings",
        PERSISTENT_TYPE_SCHEMA_TYPE__STR
    ),
    'size': PersistTypeSchemaItem(
        "proportional size of the area",
        PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT
    ),
    'position': PersistTypeSchemaItem(
        "Position for windows inserted into the portal (fill, n, e, s, w, ne, nw, se, sw, and r- variants).",
        PERSISTENT_TYPE_SCHEMA_TYPE__STR
    )
}
DEFAULT_WINDOW_POSITION = 'r-ne'
DEFAULT_WINDOW_POSITION_VALUE = POSITION_FAVOR_RESTRICTED_NE
_SPLIT_SCHEMA = {
    PERSISTENT_TYPE_SCHEMA_NAME__SCHEMA: PersistTypeSchemaItem(
        "split-layout",
        PERSISTENT_TYPE_SCHEMA_TYPE__ID
    ),
    'target': PersistTypeSchemaItem(
        "TRUE if this is where the user-triggered splits will happen",
        PERSISTENT_TYPE_SCHEMA_TYPE__BOOL
    ),
    'name': PersistTypeSchemaItem(
        "An optional name for the portal, for use with matching or quick focus on key bindings",
        PERSISTENT_TYPE_SCHEMA_TYPE__STR
    ),
    'size': PersistTypeSchemaItem(
        "Proportional size of the split, to its siblings",
        PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT
    ),
    'splits': [
        PersistTypeSchemaItem("split-layout", PERSISTENT_TYPE_SCHEMA_TYPE__REF),
        _PORTAL_SCHEMA,
    ],
}
_SCREEN_SCHEMA = {
    'resolution': PersistTypeSchemaItem(
        "screen resolution to match against, in the form WIDTHxHEIGHT (e.g. `1024x768`)",
        PERSISTENT_TYPE_SCHEMA_TYPE__STR
    ),
    'name': PersistTypeSchemaItem(
        "screen name or index to match against", PERSISTENT_TYPE_SCHEMA_TYPE__STR
    ),
    'direction': PersistTypeSchemaItem(
        "Initial split direction.  Deeper splits will alternate.",
        PERSISTENT_TYPE_SCHEMA_TYPE__STR
    ),
    'target': PersistTypeSchemaItem(
        "TRUE if this is where the user-triggered splits will happen",
        PERSISTENT_TYPE_SCHEMA_TYPE__BOOL
    ),
    'splits': [
        _SPLIT_SCHEMA,
        _PORTAL_SCHEMA,
    ],
}
_RESOLUTION_PATTERN = re.compile(r'^\s*(\d+)\s*[Xx,]\s*(\d+)\s*$')

_KEY_MATCH_WINDOWS = 'match-windows'
_KEY_LAYOUTS = 'layouts'
_KEY_SCREENS = 'screens'
TILE_LAYOUT_CONFIG_SCHEMA = readonly_persistent_schema_copy({
    _KEY_MATCH_WINDOWS: [{
        'portal': PersistTypeSchemaItem(
            "name of the portal that the window will go into by default", PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
        'position': PersistTypeSchemaItem(
            """corner to align the window (fill, ne, se, nw, sw, n, e, s, w, and r- variants),
            or not set if it is resized""",
            PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
        'key': PersistTypeSchemaItem(
            "window property key to match", PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
        'match': PersistTypeSchemaItem(
            "text to match against the window property key value", PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
        'type': PersistTypeSchemaItem(
            "type of matching to use: glob (default), partial, exact, or regex",
            PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
        'matchers': [{
            'key': PersistTypeSchemaItem(
                "window property key to match", PERSISTENT_TYPE_SCHEMA_TYPE__STR
            ),
            'match': PersistTypeSchemaItem(
                "text to match against the window property key value", PERSISTENT_TYPE_SCHEMA_TYPE__STR
            ),
            'type': PersistTypeSchemaItem(
                "type of matching to use: glob (default), partial, exact, or regex",
                PERSISTENT_TYPE_SCHEMA_TYPE__STR
            ),
        }]
    }],
    _KEY_LAYOUTS: [{
        'name': PersistTypeSchemaItem(
            "layout name, for logging purposes", PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
        _KEY_SCREENS: [_SCREEN_SCHEMA],
    }, _SCREEN_SCHEMA]
})


def parse_config(data: PersistType) -> ResultWithErrors[TileLayoutConfig]:
    layouts: List[RootTileLayout] = []
    matchers: List[MatchWindowToPortal] = []
    errors: List[ErrorReport] = []

    match_window_data_list = collect_errors(errors, with_key_as_list(
        data, _KEY_MATCH_WINDOWS,
        lambda: create_user_error(parse_config, '{key} must be a list of key-value set', key=_KEY_MATCH_WINDOWS)
    ))
    if match_window_data_list:
        for matcher_data in list_of_maps(
                match_window_data_list, errors,
                lambda i: create_user_error(
                    parse_config, '{key} #{i} must be a key-value set', key=_KEY_MATCH_WINDOWS, i=i
                )
        ):
            matcher = collect_errors(errors, parse_match_window_to_portal(t_cast(PersistType, matcher_data)))
            if matcher:
                matchers.append(matcher)

    layout_data_list = collect_errors(errors, with_key_as_list(
        data, _KEY_LAYOUTS,
        lambda: create_user_error(parse_config, '{key} must be a list', key=_KEY_LAYOUTS)
    ))
    if layout_data_list:
        floating_screens: List[ScreenTileLayout] = []
        for layout_data in list_of_maps(
                layout_data_list, errors,
                lambda i: create_user_error(
                    parse_config, '{key} #{i} must be a key-value set', key=_KEY_LAYOUTS, i=i
                )
        ):
            screen_list_data = collect_errors(errors, with_key_as_list(
                layout_data, _KEY_SCREENS,
                lambda: create_user_error(
                    parse_config, '{s} in each {la} must be a list', s=_KEY_SCREENS, la=_KEY_LAYOUTS
                )
            ))
            if screen_list_data:
                name = str(layout_data.get("name", str(len(layouts))))
                layout_screens: List[ScreenTileLayout] = []
                for screen_data in list_of_maps(
                    screen_list_data, errors,
                    lambda i: create_user_error(
                        parse_config, '{s} #{i} in {la} must be a key-value set', s=_KEY_SCREENS, i=i, la=_KEY_LAYOUTS
                    )
                ):
                    screen = collect_errors(errors, parse_screen(screen_data))
                    if screen:
                        layout_screens.append(screen)
                layouts.append(RootTileLayout(name, layout_screens))
            else:
                top = collect_errors(errors, parse_screen(t_cast(PersistType, layout_data)))
                if top:
                    floating_screens.append(top)
        if len(floating_screens) > 0:
            layouts.append(RootTileLayout('top', floating_screens))

    return TileLayoutConfig(layouts, matchers), errors


def parse_match_window_to_portal(data: PersistType) -> ResultWithErrors[Optional[MatchWindowToPortal]]:
    errors: List[ErrorReport] = []
    portal = collect_errors(errors, optional_str(
        data, 'portal', lambda: create_user_error(
            parse_config, '{k1} key {k2} must be a string', k1=_KEY_MATCH_WINDOWS, k2='portal'
        )
    ))
    position = collect_errors(errors, optional_str(
        data, 'position', lambda: create_user_error(
            parse_config, '{k1} key {k2} must be a string', k1=_KEY_MATCH_WINDOWS, k2='position'
        )
    ))
    matchers: List[WindowMatcher] = []
    matcher = collect_errors(errors, parse_window_matcher(data))
    if matcher:
        matchers.append(matcher)
    matcher_list_data = collect_errors(errors, with_key_as_list(
        data, 'matchers',
        lambda: create_user_error(create_matcher, '{m} must be a list of key-value sets', m='matchers')
    ))
    if matcher_list_data:
        # TODO should this should have an "and" wrapper around all these matchers?
        #  Or should "and" be an owning key for the parser?

        for matcher_data in list_of_maps(
            matcher_list_data, errors,
            lambda i: create_user_error(create_matcher, '{m} #{i} must be a key-value set', m='matchers', i=i)
        ):
            matcher = collect_errors(errors, parse_window_matcher(matcher_data))
            if matcher:
                matchers.append(matcher)
    return MatchWindowToPortal(matchers, portal, position), errors


def parse_window_matcher(data: PersistType) -> ResultWithErrors[Optional[WindowMatcher]]:
    errors: List[ErrorReport] = []
    key = collect_errors(errors, optional_str(
        data, 'key', lambda: create_user_error(
            parse_config, '{k1} key {k2} must be a string', k1=_KEY_MATCH_WINDOWS, k2='key'
        )
    ))
    match = collect_errors(errors, optional_str(
        data, 'match', lambda: create_user_error(
            parse_config, '{k1} key {k2} must be a string', k1=_KEY_MATCH_WINDOWS, k2='match'
        )
    ))
    m_type = collect_errors(errors, optional_str(
        data, 'type', lambda: create_user_error(
            parse_config, '{k1} key {k2} must be a string', k1=_KEY_MATCH_WINDOWS, k2='type'
        )
    ))
    if key and match and m_type:
        return create_matcher(key, match, m_type)
    if key or match or m_type:
        return None, (create_user_error(create_matcher, 'Must provide all of "key", "match", and "type"'),)
    return None, NO_ERRORS


def parse_screen(data: PersistType) -> ResultWithErrors[Optional[ScreenTileLayout]]:
    """
    """
    errors: List[ErrorReport] = []
    splits = collect_errors(errors, parse_splits(data))
    if not splits:
        splits.append(PortalLayout('default', 1, DEFAULT_WINDOW_POSITION))

    resolution = collect_errors(errors, optional_str(
        data, 'resolution', lambda: create_user_error(parse_config, 'resolution must be a string')
    ))
    name = collect_errors(errors, optional_str(
        data, 'name', lambda: create_user_error(parse_config, 'name must be a string')
    ))
    direction = collect_errors(errors, optional_str(
        data, 'direction', lambda: create_user_error(parse_config, 'direction must be a string')
    ))
    # target = optional_bool(data, 'target', lambda: create_user_error(parse_config, 'target must be true or false'))
    size: ScreenSize = (0, 0,)
    if resolution:
        mc = _RESOLUTION_PATTERN.match(resolution)
        if mc:
            size = (int(mc.group(1)), int(mc.group(2)),)
        else:
            errors.append(create_user_error(parse_config, "resolution must be in the form 'width x height"))
    if direction in ("left-right", "horiz", "horizontal", "e-w", "w-e",):
        direction_int = SPLIT_HORIZONTAL
    elif direction in ('top-down', 'vertical', 'n-s', 's-n', None):
        direction_int = SPLIT_VERTICAL
    else:
        errors.append(create_user_error(
            parse_config,
            'direction must be "vertical" or "horizontal" but found "{direction}"; defaulting to vertical',
            direction=direction
        ))
        direction_int = SPLIT_VERTICAL
    # if target is None:
    #     target = False
    ret = ScreenTileLayout(name, direction_int, False, size)
    ret.layout.extend(splits)
    return ret, errors


def parse_tile(data: PersistType) -> ResultWithErrors[Union[SplitTileLayout, PortalLayout, None]]:
    """
    Read the recursive tile layout.
    """
    errors: List[ErrorReport] = []
    name = collect_errors(errors, optional_str(
        data, 'name', lambda: create_user_error(parse_config, 'name must be a string')
    ))
    splits = collect_errors(errors, parse_splits(data))
    if not splits:
        size = 1
        size_data = collect_errors(errors, optional_int(
            data, 'size', lambda: create_user_error(parse_config, 'size must be a number')
        ))
        position = collect_errors(errors, optional_str(
            data, 'position', lambda: create_user_error(parse_config, 'position must be a string')
        ))
        if size_data is not None and size_data > 0:
            size = size_data
        return PortalLayout(name or 'default', size, position or DEFAULT_WINDOW_POSITION), errors

    target = collect_errors(errors, optional_bool(
        data, 'target', lambda: create_user_error(parse_config, 'target must be true or false')
    ))
    if target is None:
        target = False
    size_data = collect_errors(errors, optional_int(
        data, 'size', lambda: create_user_error(parse_config, 'size must be a number')
    ))
    if size_data is None or size_data <= 0:
        size = 1
    else:
        size = size_data
    return SplitTileLayout(name, size, splits, target), errors


def parse_splits(data: PersistType) -> ResultWithErrors[List[Union[SplitTileLayout, PortalLayout]]]:
    errors: List[ErrorReport] = []
    splits: List[Union[SplitTileLayout, PortalLayout]] = []
    split_list_data = collect_errors(errors, with_key_as_list(
        data, 'splits',
        lambda: create_user_error(parse_config, 'splits must be a list of key-value sets')
    ))
    if split_list_data:
        for split_data in list_of_maps(split_list_data, errors, lambda i: create_user_error(
                parse_config, 'split #{i} must be a key-value set', i=i
        )):
            tile = collect_errors(errors, parse_tile(split_data))
            if tile:
                splits.append(tile)
    return splits, errors


MATCH_KIND_GLOB = 'glob'
MATCH_KIND_REGEX = 'regex'
MATCH_KIND_PART = 'partial'
MATCH_KIND_EXACT = 'exact'
MATCH_KIND_ALL = (
    MATCH_KIND_GLOB,
    MATCH_KIND_REGEX,
    MATCH_KIND_PART,
    MATCH_KIND_EXACT,
)


def create_matcher(
        key: str,
        matches: str,
        kind: str
) -> ResultWithErrors[WindowMatcher]:
    """Create the WindowMatcher instance based on this configuration."""
    kind = kind.lower()
    errors: List[ErrorReport] = []
    if kind == MATCH_KIND_EXACT:
        kind_id = WINDOW_MATCH_EXACT
    elif kind == MATCH_KIND_PART:
        kind_id = WINDOW_MATCH_PART
    elif kind == MATCH_KIND_REGEX:
        kind_id = WINDOW_MATCH_REGEX
    elif kind == MATCH_KIND_GLOB:
        kind_id = WINDOW_MATCH_GLOB
    else:
        # Default kind...
        kind_id = WINDOW_MATCH_GLOB
        errors.append(create_user_error(create_matcher, 'Unknown window matcher kind `{kind}`', kind=kind))

    return WindowMatcher(key, matches, kind_id), errors


_POSITION_MAP = {
    'fill': POSITION_FAVOR_FILL,
    'n': POSITION_FAVOR_N_EDGE,
    'e': POSITION_FAVOR_E_EDGE,
    's': POSITION_FAVOR_S_EDGE,
    'w': POSITION_FAVOR_W_EDGE,
    'ne': POSITION_FAVOR_NE,
    'se': POSITION_FAVOR_SE,
    'nw': POSITION_FAVOR_NW,
    'sw': POSITION_FAVOR_SW,
    'r-n': POSITION_FAVOR_RESTRICTED_N_EDGE,
    'r-e': POSITION_FAVOR_RESTRICTED_E_EDGE,
    'r-s': POSITION_FAVOR_RESTRICTED_S_EDGE,
    'r-w': POSITION_FAVOR_RESTRICTED_W_EDGE,
    'r-ne': POSITION_FAVOR_RESTRICTED_NE,
    'r-se': POSITION_FAVOR_RESTRICTED_SE,
    'r-nw': POSITION_FAVOR_RESTRICTED_NW,
    'r-sw': POSITION_FAVOR_RESTRICTED_SW,
    'n-r': POSITION_FAVOR_RESTRICTED_N_EDGE,
    'e-r': POSITION_FAVOR_RESTRICTED_E_EDGE,
    's-r': POSITION_FAVOR_RESTRICTED_S_EDGE,
    'w-r': POSITION_FAVOR_RESTRICTED_W_EDGE,
    'ne-r': POSITION_FAVOR_RESTRICTED_NE,
    'se-r': POSITION_FAVOR_RESTRICTED_SE,
    'nw-r': POSITION_FAVOR_RESTRICTED_NW,
    'sw-r': POSITION_FAVOR_RESTRICTED_SW,
}


def parse_position(position: Optional[str]) -> Optional[int]:
    """
    Convert the position text value to a correct value.

    :param position:
    :return:
    """
    if not position:
        return None
    position = position.strip().lower()
    if position in _POSITION_MAP:
        return _POSITION_MAP[position]
    return None


_MOVE_MAP = {
    'l': MOVE_WINDOW_DIRECTION_WEST,
    'left': MOVE_WINDOW_DIRECTION_WEST,
    'w': MOVE_WINDOW_DIRECTION_WEST,
    'west': MOVE_WINDOW_DIRECTION_WEST,
    'r': MOVE_WINDOW_DIRECTION_EAST,
    'right': MOVE_WINDOW_DIRECTION_EAST,
    'e': MOVE_WINDOW_DIRECTION_EAST,
    'east': MOVE_WINDOW_DIRECTION_EAST,
    't': MOVE_WINDOW_DIRECTION_NORTH,
    'top': MOVE_WINDOW_DIRECTION_NORTH,
    'up': MOVE_WINDOW_DIRECTION_NORTH,
    'u': MOVE_WINDOW_DIRECTION_NORTH,
    'n': MOVE_WINDOW_DIRECTION_NORTH,
    'north': MOVE_WINDOW_DIRECTION_NORTH,
    'b': MOVE_WINDOW_DIRECTION_SOUTH,
    'bottom': MOVE_WINDOW_DIRECTION_SOUTH,
    'down': MOVE_WINDOW_DIRECTION_SOUTH,
    'd': MOVE_WINDOW_DIRECTION_SOUTH,
    's': MOVE_WINDOW_DIRECTION_SOUTH,
    'south': MOVE_WINDOW_DIRECTION_SOUTH,
}


def parse_direction(direction: Optional[str]) -> Optional[int]:
    if not direction:
        return None
    direction = direction.strip().lower()
    if direction in _MOVE_MAP:
        return _MOVE_MAP[direction]
    return None
