

"""
API for the event bus system.
"""

from ..internal_.bus_types import (
    EventBus, EventCallback,
    EventId, ListenerId,
    ListenerRegistrar, ListenerSetup,
    QueuePriority,

    # These probably should move to some other module.
    ExtensionCompatibilityStruct,
    ExtensionMetadataStruct,
    ExtensionVersionStruct,
)
from ..internal_.bus_constants import (
    EVENT_WILDCARD, TARGET_WILDCARD,

    NOT_LISTENER,

    QUEUE_EVENT_HIGH, QUEUE_EVENT_NORMAL, QUEUE_EVENT_IO,
    QUEUE_EVENT_TYPES,
)
from ..internal_.bus_events import (
    # Note the extremely limited set of things that are made easily available.
    EventListenerAddedEvent,
    as_listener_added_listener,

    register_event,
)
