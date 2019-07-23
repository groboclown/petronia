
"""
Constants for the event bus.
"""

from .bus_types import EventId, ListenerId, QueuePriority
from .identity_types import create_singleton_identity


EVENT_WILDCARD = EventId('*')
TARGET_WILDCARD = create_singleton_identity('*')

NOT_LISTENER = ListenerId(0)

QUEUE_EVENT_NOW = QueuePriority('now')
QUEUE_EVENT_NORMAL = QueuePriority('normal')
QUEUE_EVENT_IO = QueuePriority('io')

QUEUE_EVENT_TYPES = (
    QUEUE_EVENT_NOW,
    QUEUE_EVENT_NORMAL,
    QUEUE_EVENT_IO,
)
