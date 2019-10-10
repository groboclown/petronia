
"""
Persistence of the configuration.
"""

from .events import (
    PersistConfigurationEvent,
    as_persist_configuration_listener,
    send_persist_configuration,
)
from .persist_types import PersistentConfigurationState

from .bootstrap import bootstrap_config_api as start_extension
from .bootstrap import EXTENSION_METADATA
