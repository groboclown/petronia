
"""
End-user configuration of the theme.
"""

from typing import List, Tuple, Dict, Iterable
from ....aid.std import (
    create_user_error,
    ErrorReport,
)
from ...platform.api import (
    WindowMatcher,
)
from ....base.util.simple_type import (
    PersistTypeSchema,
    PersistTypeSchemaItem,
    PersistType,

    readonly_persistent_copy,
    readonly_persistent_schema_copy,

    PERSISTENT_TYPE_SCHEMA_TYPE__BOOL,
    PERSISTENT_TYPE_SCHEMA_TYPE__ANY,
    PERSISTENT_TYPE_SCHEMA_TYPE__STR,
    PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT,
)
from .chrome import (
    ThemeBorderSide,
    ThemeBorder,
    ThemeChrome,
)
from .state import (
    WindowMatchChrome,
    ThemeState,
)

_CHROME_SCHEMA = {
    "border": [{
        "pos": PersistTypeSchemaItem(
            "n, e, w, s, ne, nw, se, or sw",
            PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
        "width": PersistTypeSchemaItem(
            "border width",
            PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT
        ),
        "color": PersistTypeSchemaItem(
            "border color",
            PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
        "cursor": PersistTypeSchemaItem(
            "named cursor icon to display when over the border (platform specific)",
            PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
        "draggable": PersistTypeSchemaItem(
            "allow dragging the mouse over this part of the border",
            PERSISTENT_TYPE_SCHEMA_TYPE__BOOL
        ),
    }],
    "style": [{
        "key": PersistTypeSchemaItem(
            "Platform-specific style key",
            PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
        "value": PersistTypeSchemaItem(
            "Value for the style key",
            PERSISTENT_TYPE_SCHEMA_TYPE__ANY
        ),
    }],
}

THEME_CONFIG_SCHEMA = readonly_persistent_schema_copy({
    "chrome": {
        "default": _CHROME_SCHEMA,
        "window": [{
            "matches": [{
                "key": PersistTypeSchemaItem(
                    "Key from the set of window descriptions, whose value will be matched",
                    PERSISTENT_TYPE_SCHEMA_TYPE__STR
                ),
                "exactly": PersistTypeSchemaItem(
                    "Exact text to match the key's value against",
                    PERSISTENT_TYPE_SCHEMA_TYPE__STR
                ),
                "partial": PersistTypeSchemaItem(
                    "Exact text to match the key's value against",
                    PERSISTENT_TYPE_SCHEMA_TYPE__STR
                ),
                "regex": PersistTypeSchemaItem(
                    "Regular expression matching the value",
                    PERSISTENT_TYPE_SCHEMA_TYPE__STR
                ),
                "glob": PersistTypeSchemaItem(
                    "Glob ('*' and '?') expression matching the value",
                    PERSISTENT_TYPE_SCHEMA_TYPE__STR
                ),
            }],
            "chrome": _CHROME_SCHEMA,
        }],
    },
})


def convert_config_to_state(config: PersistType) -> Tuple[ThemeState, List[ErrorReport]]:
    raise NotImplementedError()


def convert_config_to_chrome(config: PersistType) -> Tuple[ThemeChrome, List[ErrorReport]]:
    raise NotImplementedError()
