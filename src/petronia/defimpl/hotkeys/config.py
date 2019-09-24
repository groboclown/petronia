
"""
Manage the configuration translation to state.

Configuration details:

# master: see the platform.api.user_input master sequence for details.
master: "master key sequence"
append: false  # optional, defaults to false
bind:
    - key: "shift+a"
      action: "bound action name"
      parameters:
        (dictionary of keys/values that are defined by the action)
    ...
"""

from typing import Tuple, Iterable, List, Sequence
from ...aid.simp import (
    create_singleton_identity,
    create_user_error,
    ErrorReport,
)
from ...core.config_persistence.api import (
    PersistType,
    PersistTypeSchema,
    PersistTypeSchemaItem,
    readonly_persistent_schema_copy,
    PERSISTENT_TYPE_SCHEMA_TYPE__STR,
    PERSISTENT_TYPE_SCHEMA_TYPE__BOOL,
    PERSISTENT_TYPE_SCHEMA_TYPE__ANY,
)
from ...core.hotkeys.api import (
    BoundServiceActionData,
)
from .state import (
    HotkeyState,
)

CONFIGURATION_ID_HOTKEYS_CMD = create_singleton_identity('default.hotkeys/setup-configuration')

HOTKEY_CONFIGURATION_SCHEMA: PersistTypeSchema = readonly_persistent_schema_copy({
    'master': PersistTypeSchemaItem(
        "Master key sequence.  Prefix with `seq:` for a key sequence, or `meta:` for a collection of  modifier keys",
        PERSISTENT_TYPE_SCHEMA_TYPE__STR
    ),
    'append': PersistTypeSchemaItem(
        "(optional) if set to `true`, then the existing hotkeys are not cleared out before loading",
        PERSISTENT_TYPE_SCHEMA_TYPE__BOOL
    ),
    'bind': [{
        'key': PersistTypeSchemaItem(
            "Keys pressed, after the master sequence, that trigger this action.",
            PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
        'action': PersistTypeSchemaItem(
            "Action name, as defined by the hotkey binding",
            PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
        'parameters': PersistTypeSchemaItem(
            "Action-specific parameters, as defined by the hotkey binding",
            PERSISTENT_TYPE_SCHEMA_TYPE__ANY
        )
    }]
})


def load_hotkey_configuration(state: HotkeyState, persistent: PersistType) -> Tuple[str, Sequence[ErrorReport]]:
    """
    Updates the hotkey state with the loaded configuration.  Returns the
    master sequence string and the list of discovered configuration issues.

    Note: if there are configuration issues, but the basic form is right
    ("master" + "bind"), then the state is updated while there are config
    problems.

    :param state:
    :param persistent:
    :return:
    """
    # Basic pre-conditions.
    if (
            'master' not in persistent or
            not persistent['master'] or
            not isinstance(persistent['master'], str) or
            'bind' not in persistent or
            not isinstance(persistent['bind'], Iterable)
    ):
        return '', (create_user_error(
            load_hotkey_configuration, "Invalid configuration definition for hotkeys: {p}", p=repr(persistent)
        ),),

    if 'append' not in persistent or persistent['append'] is not True:
        state.clear_hotkeys()

    errors: List[ErrorReport] = []
    for key_def in persistent['bind']:
        if (
            key_def and isinstance(key_def, dict) and
            'key' in key_def and isinstance(key_def['key'], str) and
            'action' in key_def and isinstance(key_def['action'], str)
        ):
            if "parameters" in key_def and isinstance(key_def['parameters'], dict):
                parameters = key_def["parameters"]
            else:
                parameters = {}
            state.add_hotkey(key_def['key'], BoundServiceActionData(key_def['action'], parameters))
        else:
            errors.append(create_user_error(
                load_hotkey_configuration, "Invalid key definition for hotkeys: {p}", p=repr(key_def)
            ))

    return persistent["master"], tuple(errors)
