
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

def bootstrap_platform_api(bus: EventBus) -> None:
    """
    Register all the events.
    """
    pass


EXTENSION_METADATA: ExtensionMetadataStruct = {
    "name": "core.platform.api",
    "version": (1, 0, 0,),
    "type": "api",
    "depends": [],
    "defaults": [{
        "extension": "default.platform",
        "minimum": ANY_VERSION,
    }],
    "authors": ["Petronia"],
}
