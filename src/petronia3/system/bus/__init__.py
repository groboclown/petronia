
"""
API supporting the event bus.
"""

from .event_bus import (
    # Force an explicit request to use the raw event bus.
    # EventBus,

    EventCallback,
    ListenerId,

    QUEUE_EVENT_IO,
    QUEUE_EVENT_NORMAL,
    QUEUE_EVENT_NOW,

    NOT_LISTENER,

    EVENT_WILDCARD,
    TARGET_WILDCARD,
)
from .event_registry import (
    EventRegistry,
    EventId,
)
from .typesafe_types import (
    TypeSafeEventCallback,
    ListenerRegistrator,
    ListenerSetup,
)
from .typesafe import (
    TypeSafeEventBus,
)
from .events import (
    register_event,
    
    EventListenerAddedEvent,
    as_listener_added_listener,
)
