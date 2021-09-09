
"""
Special hotkeys just for this layout.
"""

from ....core.hotkeys.api import (
    BoundServiceActionSchema,
)
from ....base.util.simple_type import (
    PersistTypeSchemaItem,
    readonly_persistent_schema_copy,
    PERSISTENT_TYPE_SCHEMA_TYPE__STR,
    PERSISTENT_TYPE_SCHEMA_NAME__DOC,
)
from .consts import (
    MODULE_ID,
)


HOTKEY_ACTION_FILL_PORTAL = 'set-window-position'
HOTKEY_SCHEMA_FILL_PORTAL__FILL = 'position'
HOTKEY_SCHEMA_FILL_PORTAL = BoundServiceActionSchema(
    MODULE_ID, HOTKEY_ACTION_FILL_PORTAL, readonly_persistent_schema_copy({
        PERSISTENT_TYPE_SCHEMA_NAME__DOC: PersistTypeSchemaItem(
            "Allows to, on the fly, change how the active window sizes itself within the portal.",
            PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
        HOTKEY_SCHEMA_FILL_PORTAL__FILL: PersistTypeSchemaItem(
            "The same value for the matcher is used here (n, s, e, w, ne, nw, se, sw, and the `r-` variants).",
            PERSISTENT_TYPE_SCHEMA_TYPE__STR
        )
    })
)


HOTKEY_ACTION_NAME_PORTAL = 'name-portal'
HOTKEY_SCHEMA_NAME_PORTAL__NAME = 'name'
HOTKEY_SCHEMA_NAME_PORTAL = BoundServiceActionSchema(
    MODULE_ID, HOTKEY_ACTION_NAME_PORTAL, readonly_persistent_schema_copy({
        PERSISTENT_TYPE_SCHEMA_NAME__DOC: PersistTypeSchemaItem(
            """
            Gives the active portal a name, so that other hotkeys can reference it.  This is useful to, on the fly,
            change the destination for a common collection of hotkeys.  For example, you can name a portal
            'run', then have a series of hotkeys to move a window to 'run', and quickly move the focus to 'run',
            then have an accompanying series of hotkeys for 'edit', to enable quick navigation between the two.
            """,
            PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
        HOTKEY_SCHEMA_NAME_PORTAL__NAME: PersistTypeSchemaItem(
            "The new name for the portal.",
            PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
    })
)


HOTKEY_ACTION_ADD_PORTAL = 'add-portal'
HOTKEY_SCHEMA_ADD_PORTAL = BoundServiceActionSchema(
    MODULE_ID, HOTKEY_ACTION_ADD_PORTAL, readonly_persistent_schema_copy({
        PERSISTENT_TYPE_SCHEMA_NAME__DOC: PersistTypeSchemaItem(
            "Creates a new portal where windows can be added.",
            PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
    })
)


HOTKEY_ACTION_REMOVE_PORTAL = 'remove-portal'
HOTKEY_SCHEMA_REMOVE_PORTAL = BoundServiceActionSchema(
    MODULE_ID, HOTKEY_ACTION_REMOVE_PORTAL, readonly_persistent_schema_copy({
        PERSISTENT_TYPE_SCHEMA_NAME__DOC: PersistTypeSchemaItem(
            "Removes the active portal, unless it's the last portal in a split.",
            PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
    })
)


HOTKEY_ACTION_MOVE_WINDOW = 'move-window-to-portal'
HOTKEY_SCHEMA_MOVE_WINDOW__DIRECTION = 'direction'
HOTKEY_SCHEMA_MOVE_WINDOW__NAME = 'name'
HOTKEY_SCHEMA_MOVE_WINDOW = BoundServiceActionSchema(
    MODULE_ID, HOTKEY_ACTION_MOVE_WINDOW, readonly_persistent_schema_copy({
        PERSISTENT_TYPE_SCHEMA_NAME__DOC: PersistTypeSchemaItem(
            "Moves a window to an adjacent or named portal.",
            PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
        HOTKEY_SCHEMA_MOVE_WINDOW__DIRECTION: PersistTypeSchemaItem(
            "The direction to move the window - one of `n`, `s`, `e`, or `w`.",
            PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
        HOTKEY_SCHEMA_MOVE_WINDOW__NAME: PersistTypeSchemaItem(
            """Portal name to move the window into.  If this is not given, or the portal with the given name is not
            found, then `direction` is used.""",
            PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
    })
)
