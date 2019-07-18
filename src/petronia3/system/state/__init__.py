
"""
The state data store.  State created by the system is stored here, for easy querying.  All state
changes must be made through the event bus.
"""

from .events import (
    set_state,
    as_state_change_listener,
)
