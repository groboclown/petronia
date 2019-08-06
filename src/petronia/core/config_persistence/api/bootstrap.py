

"""
Configuration system setup.
"""

from .events import (
    EVENT_ID_PERSIST_CONFIGURATION,
    PersistConfigurationEvent,
)
from ....base import NOT_PARTICIPANT
from ....base.bus import (
    EventBus,
    register_event,
    ExtensionMetadataStruct,
    QUEUE_EVENT_IO,
)
from ...extensions.api import ANY_VERSION

def bootstrap_config_api(bus: EventBus) -> None:
    """Bootstrap all the necessary bits for this extension."""
    register_event(
        bus,
        EVENT_ID_PERSIST_CONFIGURATION,
        QUEUE_EVENT_IO,
        PersistConfigurationEvent,
        PersistConfigurationEvent(NOT_PARTICIPANT)
    )

EXTENSION_METADATA: ExtensionMetadataStruct = {
    "name": "core.config_persistence.api",
    "version": (1, 0, 0,),
    "type": "api",
    "depends": [],
    "defaults": [{
        "extension": "default.config_persistence",
        "minimum": ANY_VERSION,
    }],
    "authors": ["Petronia"],
}
