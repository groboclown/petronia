
"""
A hotkey handler, which acts as a broker between services and the
low-level platform hotkey events.
"""

from .bootstrap import bootstrap_hotkey_broker as start_extension
from .bootstrap import EXTENSION_METADATA
