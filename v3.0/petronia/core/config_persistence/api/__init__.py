
"""
User Configuration Sub-System.

Configuration in Petronia is much more than some files.  It takes advantage of
the state storage mechanism and applies readers and persistence on top of it.

The internal participant configuration is handled through states. However,
whereas states are *pushed* from the owner to the system for announcing the
changes, the configuration is pushed from the configuration reader to the
component (backwards of states).

This configuration extension handles the different ways to read state and
persist it back.  Passing the configuration is done through the state system.
"""

from .events import (
    PersistConfigurationEvent,
    as_persist_configuration_listener,
    send_persist_configuration,
)
from .persist_types import PersistentConfigurationState

from .bootstrap import bootstrap_config_api as start_extension
from .bootstrap import EXTENSION_METADATA
