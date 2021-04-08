
"""
Constants for the event bus.
"""

from .bus_types import (
    EventId, ListenerId, QueuePriority,
    EventProtectionModel,
)
from .identity_types import create_singleton_identity


EVENT_WILDCARD = EventId('*')
TARGET_WILDCARD = create_singleton_identity('*')

NOT_LISTENER = ListenerId(0)

QUEUE_EVENT_HIGH = QueuePriority('high')
QUEUE_EVENT_NORMAL = QueuePriority('normal')
QUEUE_EVENT_IO = QueuePriority('io')

QUEUE_EVENT_TYPES = (
    QUEUE_EVENT_HIGH,
    QUEUE_EVENT_NORMAL,
    QUEUE_EVENT_IO,
)

GLOBAL_EVENT_PROTECTION = EventProtectionModel(True, True)
INTERNAL_EVENT_PROTECTION = EventProtectionModel(False, False)
PRODUCE_EVENT_PROTECTION = EventProtectionModel(True, False)
CONSUME_EVENT_PROTECTION = EventProtectionModel(False, True)

# Aliases
REQUEST_EVENT_PROTECTION = PRODUCE_EVENT_PROTECTION
RESPONSE_EVENT_PROTECTION = CONSUME_EVENT_PROTECTION
