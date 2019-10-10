
"""
Process the configuration.
"""

from typing import List, Dict, Iterable, Mapping, Optional, Union
from typing import cast as t_cast
from .....aid.std import (
    ErrorReport,
    ResultWithErrors,
    create_user_error,
    readonly_dict,
)
from .....base.util.simple_type import (
    PersistType,
    PersistTypeSchema,
    PersistTypeSchemaItem,
    readonly_persistent_schema_copy,
    PERSISTENT_TYPE_SCHEMA_TYPE__STR,
    PERSISTENT_TYPE_SCHEMA_TYPE__BOOL,
    PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT,
    PERSISTENT_TYPE_SCHEMA_TYPE__REF,
    PERSISTENT_TYPE_SCHEMA_TYPE__ID,
    PERSISTENT_TYPE_SCHEMA_NAME__SCHEMA,
    collect_errors,
    with_key_as_dict,
    with_key_as_list,
    required_dict,
    list_of_maps,
)
from .....core.platform.api import (
    WindowMatcher,
    WINDOW_MATCH_EXACT,
    WINDOW_MATCH_PART,
    WINDOW_MATCH_GLOB,
    WINDOW_MATCH_REGEX,
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

_PORTAL_SCHEMA = {
    'name': PersistTypeSchemaItem(
        "An optional name for the portal, for use with matching or quick focus on key bindings",
        PERSISTENT_TYPE_SCHEMA_TYPE__STR
    ),
}
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
        PersistTypeSchemaItem("split-layout", PERSISTENT_TYPE_SCHEMA_TYPE__REF),
        _PORTAL_SCHEMA,
    ],
}

_KEY_MATCH_WINDOWS = 'match-windows'
_KEY_LAYOUTS = 'layouts'
_KEY_SCREENS = 'screens'
TILE_LAYOUT_CONFIG_SCHEMA = readonly_persistent_schema_copy({
    _KEY_MATCH_WINDOWS: [{
        'portal': PersistTypeSchemaItem(
            "name of the portal that the window will go into by default", PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
        'position': PersistTypeSchemaItem(
            "corner to align the window (ne, se, nw, sw), or not set if it is resized",
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
    }],
    _KEY_LAYOUTS: [{
        _KEY_SCREENS: [{
            'layout': _SCREEN_SCHEMA,
        }]
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

    layout_data_list = with_key_as_list(
        data, _KEY_LAYOUTS,
        lambda: create_user_error(parse_config, '{key} must be a list', key=_KEY_LAYOUTS)
    )
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
                    parse_config, '{s} in each {l} must be a list', s=_KEY_SCREENS, l=_KEY_LAYOUTS
                )
            ))
            if screen_list_data:
                layout_screens: List[ScreenTileLayout] = []
                for screen_data in list_of_maps(
                    screen_list_data, errors,
                    lambda i: create_user_error(
                        parse_config, '{s} #{i} in {l} must be a key-value set', s=_KEY_SCREENS, i=i, l=_KEY_LAYOUTS
                    )
                ):
                    screen = collect_errors(errors, parse_screen(screen_data))
                    if screen:
                        layout_screens.append(screen)
                layouts.append(RootTileLayout(layout_screens))
            else:
                top = collect_errors(errors, parse_screen(t_cast(PersistType, data[_KEY_LAYOUTS])))
                if top:
                    floating_screens.append(top)
        layouts.append(RootTileLayout(floating_screens))

    return TileLayoutConfig(layouts, matchers), errors


def parse_match_window_to_portal(data: PersistType) -> ResultWithErrors[Optional[MatchWindowToPortal]]:
    pass


def parse_match_windows(data: PersistType) -> ResultWithErrors[Optional[WindowMatcher]]:
    pass


def parse_screen(data: PersistType) -> ResultWithErrors[Optional[ScreenTileLayout]]:
    pass


def parse_tile(data: PersistType) -> ResultWithErrors[Union[SplitTileLayout, PortalLayout, None]]:
    pass


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
