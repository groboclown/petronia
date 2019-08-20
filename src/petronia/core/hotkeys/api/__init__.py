
"""
Standard API for registering hotkeys that perform generate events.

The registration will associate a basic key combination to a target ID and
a basic data structure.  The event ID is fixed.
"""

from .bootstrap import bootstrap_hotkeys as start_extension
from .bootstrap import EXTENSION_METADATA
