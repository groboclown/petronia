
"""
Standard API for the state.
"""

from .events import (
    StateStoreUpdatedEvent,
    as_state_change_listener,

    set_state,
)

from .bootstrap import bootstrap_state_store_api as start_extension
from .bootstrap import STATE_STORE_MODULE_ID as MODULE_ID
# No dependencies.
