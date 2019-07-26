
"""
Setup for the API extension.
"""

from ....system.bus import EventBus, register_event
from ....system.participant import create_singleton_identity


MODULE_ID = create_singleton_identity('core.extensions.api')
EXTENSION_DEPENDENCIES = ('core.state.api',)

def bootstrap_extensions_api(bus: EventBus) -> None:
    """Register all events."""
    pass
