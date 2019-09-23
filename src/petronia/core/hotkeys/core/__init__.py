"""
Petronia Core Hotkey Handlers.

Defines the hotkey action types for core actions the user may want to perform.

Extracted into a separate extension, because some of these core extensions
must be loaded before the hotkey registration can load.
"""

from .bootstrap import bootstrap_core_handlers as start_extension
from .bootstrap import EXTENSION_METADATA
