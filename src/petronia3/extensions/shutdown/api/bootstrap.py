
"""
Setup the extension.
"""

from ....system.bus import (
    EventBus,
    register_event,
    ExtensionMetadataStruct,
    QUEUE_EVENT_NORMAL,
)
from .events import (
    EVENT_ID_REQUEST_SYSTEM_SHUTDOWN,
    RequestSystemShutdownEvent,

    EVENT_ID_REQUEST_CANCEL_SYSTEM_SHUTDOWN,
    RequestCancelSystemShutdownEvent,

    EVENT_ID_SYSTEM_SHUTDOWN,
    SystemShutdownEvent,

    EVENT_ID_SYSTEM_SHUTDOWN_CANCELLED,
    SystemShutdownCancelledEvent,
)

def bootstrap_shutdown_api(bus: EventBus) -> None:
    """
    Register all the events.
    """
    register_event(
        bus, EVENT_ID_REQUEST_SYSTEM_SHUTDOWN, QUEUE_EVENT_NORMAL,
        RequestSystemShutdownEvent, RequestSystemShutdownEvent()
    )
    register_event(
        bus, EVENT_ID_REQUEST_CANCEL_SYSTEM_SHUTDOWN, QUEUE_EVENT_NORMAL,
        RequestCancelSystemShutdownEvent, RequestCancelSystemShutdownEvent()
    )
    register_event(
        bus, EVENT_ID_SYSTEM_SHUTDOWN, QUEUE_EVENT_NORMAL,
        SystemShutdownEvent, SystemShutdownEvent()
    )
    register_event(
        bus, EVENT_ID_SYSTEM_SHUTDOWN_CANCELLED, QUEUE_EVENT_NORMAL,
        SystemShutdownCancelledEvent, RequestSystemShutdownEvent()
    )


EXTENSION_METADATA: ExtensionMetadataStruct = {
    "type": "api",
    "depends": [],
    "authors": ["Petronia"],
}
