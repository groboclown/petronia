
"""
Persistence of the configuration.
"""

from .events import (
    PersistConfigurationEvent,
    as_persist_configuration_listener,
    send_persist_configuration,
)

from .persist_types import (
    PersistentConfigurationState,
    PersistType,
    PersistTypeSchemaItem,
    PersistTypeSchema,

    PERSISTENT_TYPE_SCHEMA_TYPE__BOOL,
    PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT,
    PERSISTENT_TYPE_SCHEMA_TYPE__STR,
    PERSISTENT_TYPE_SCHEMA_TYPE__ANY,

    readonly_persistent_copy,
    readonly_persistent_schema_copy,
)

from .bootstrap import bootstrap_config_api as start_extension
from .bootstrap import EXTENSION_METADATA
