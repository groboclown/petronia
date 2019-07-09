
"""
The state data store.  State created by the system is stored here, for easy querying.  All state
changes must be made through the event bus.
"""

from . import bus
from .bus import set_state
