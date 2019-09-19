
"""
Manage the configuration translation to state.

Configuration details:

# master: see the platform.api.user_input master sequence for details.
master: "master key sequence"
keys:
    "key+sequence":
        action: "bound action name"
        parameters:
            (dictionary of keys/values that are defined by the action)
    ...
"""

from typing import Tuple
from ...aid.simp import (
    create_singleton_identity,
    log, WARN,
)
from ...core.config_persistence.api import (
    PersistType,
)
from ...core.hotkeys.api import (
    BoundServiceActionData,
)
from .state import (
    HotkeyState,
)

CONFIGURATION_ID_HOTKEYS_CMD = create_singleton_identity('default.hotkeys/setup-configuration')


def load_hotkey_configuration(state: HotkeyState, persistent: PersistType) -> Tuple[str, bool]:
    # Basic pre-conditions.
    if (
            "master" not in persistent or
            not persistent["master"] or
            not isinstance(persistent["master"], str) or
            "keys" not in persistent or
            not isinstance(persistent["keys"], dict)
    ):
        return "", False,

    for key, settings in persistent["keys"]:
        if (
                key and isinstance(key, str) and
                settings and isinstance(settings, dict) and
                "action" in settings and
                isinstance(settings["action"], str)
        ):
            if "parameters" in settings and isinstance(settings['parameters'], dict):
                parameters = settings["parameters"]
            else:
                parameters = {}
            state.add_hotkey(key, BoundServiceActionData(settings["action"], parameters))
        else:
            log(
                WARN, load_hotkey_configuration,
                "Incorrect settings for key '%d'; settings must include an "
                "'action' value, and optionally a 'parameters' structure; found %s",
                key, repr(settings)
            )
    return persistent["master"], True
