
"""
Sets up the platform API.
"""

from ....base.bus import (
    EventBus,
    register_event,
    ExtensionMetadataStruct,
    QUEUE_EVENT_NORMAL,
)
from ...extensions.api import ANY_VERSION
from .user_input.bootstrap import (
    register_user_input_events,
)
from .window.bootstrap import (
    register_window_events,
)


def bootstrap_platform_api(bus: EventBus) -> None:
    """
    Register all the events.
    """
    register_user_input_events(bus)
    register_window_events(bus)


EXTENSION_METADATA: ExtensionMetadataStruct = {
    "name": "core.platform.api",
    "version": (1, 0, 0,),
    "type": "api",
    "depends": [{
        "extension": "core.state.api",
        "minimum": ANY_VERSION,
    }],
    "defaults": [{
        # A non-existent plugin.  Because platform must be included in the
        # bootstrap phase, a real platform that implements this API must also
        # be included, so that this doesn't generate a boot-up error.
        "extension": "default.platform",
        "minimum": ANY_VERSION,
    }],
    "authors": ["Petronia"],
}
