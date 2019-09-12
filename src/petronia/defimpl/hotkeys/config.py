
"""
Manage the configuration translation to state.
"""

from ...aid.simp import (
    create_singleton_identity
)
from ...core.config_persistence.api import (
    PersistentConfigurationState,
    PersistType,
)
from .cmd import (
    Cmd,
)

CONFIGURATION_ID_HOTKEYS_CMD = create_singleton_identity('default.hotkeys/setup-configuration')

