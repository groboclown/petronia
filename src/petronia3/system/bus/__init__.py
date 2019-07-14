
"""
API supporting the event bus.
"""

from .bus import (
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
from .event import (
    EventRegistry,
    EventId,
)
from .typesafe import (
    TypeSafeEventBus,
    TypeSafeEventCallback,
)
