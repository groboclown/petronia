
"""
Sets up the platform API.
"""

from ....system.bus import (
    EventBus,
    register_event,
    ExtensionMetadataStruct,
    QUEUE_EVENT_NORMAL,
)

def bootstrap_platform_api(bus: EventBus) -> None:
    """
    Register all the events.
    """
    pass


EXTENSION_METADATA: ExtensionMetadataStruct = {
    "type": "api",
    "depends": [],
    "authors": ["Petronia"],
}
