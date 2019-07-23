

"""
Configuration system setup.
"""

from .events import (
    EVENT_ID_PERSIST_CONFIGURATION,
    PersistConfigurationEvent,
)
from ....system.bus import (
    EventBus,
    register_event,
    QUEUE_EVENT_IO,
)
from ....system.participant import NOT_PARTICIPANT

def bootstrap_config(bus: EventBus) -> None:
    register_event(
        bus,
        EVENT_ID_PERSIST_CONFIGURATION,
        QUEUE_EVENT_IO,
        PersistConfigurationEvent,
        PersistConfigurationEvent(NOT_PARTICIPANT)
    )
