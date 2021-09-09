
"""
Listener-based events.

Added here only for the use case to support event bus implementations.
"""

from ...internal_.bus_events import (
    TARGET_EVENT_BUS,
    TARGET_EVENT_REGISTRY,

    EVENT_ID_EVENT_LISTENER_ADDED,
    EventListenerAddedEvent,
    as_listener_added_listener,

    EVENT_ID_REGISTER_EVENT,
    RegisterEventEvent,
    as_register_event_listener,
)
from ...internal_.bus_types import (
    EventProtectionModel,
)
from ...internal_.bus_constants import (
    GLOBAL_EVENT_PROTECTION,
    INTERNAL_EVENT_PROTECTION,
    PRODUCE_EVENT_PROTECTION,
    CONSUME_EVENT_PROTECTION,
    REQUEST_EVENT_PROTECTION,
    RESPONSE_EVENT_PROTECTION,
)
