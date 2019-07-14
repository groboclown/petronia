
"""
EventBus attachment for the disposer.
"""

from ..bus import (
    TypeSafeEventBus,
    EventRegistry,
)

EVENT_ID_DISPOSER_REQUEST_DISPOSE = 'disposer request-dispose'
EVENT_ID_DISPOSER_DISPOSED = 'disposer disposed'
