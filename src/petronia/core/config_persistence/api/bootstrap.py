

"""
Configuration system setup.
"""

from .events import (
    EVENT_ID_PERSIST_CONFIGURATION,
    PersistConfigurationEvent,
)
from ....aid.bootstrap import (
    EventBus,
    register_event,
    QUEUE_EVENT_IO,
    NOT_PARTICIPANT,
    GLOBAL_EVENT_PROTECTION,
    ANY_VERSION,
)
from ....base.internal_.internal_extension import petronia_extension


def bootstrap_config_api(bus: EventBus) -> None:
    """Bootstrap all the necessary bits for this extension."""
    register_event(
        bus, EVENT_ID_PERSIST_CONFIGURATION, QUEUE_EVENT_IO, GLOBAL_EVENT_PROTECTION,
        PersistConfigurationEvent, PersistConfigurationEvent(NOT_PARTICIPANT)
    )


EXTENSION_METADATA = petronia_extension({
    "name": "core.config_persistence.api",
    "version": (1, 0, 0,),
    "type": "api",
    "depends": [],
    "defaults": [{
        "extension": "default.config_persistence",
        "minimum": ANY_VERSION,
    }],
})
