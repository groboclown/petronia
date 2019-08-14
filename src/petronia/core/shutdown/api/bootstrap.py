
"""
Setup the extension.
"""

from ....base.bus import (
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

    EVENT_ID_SYSTEM_SHUTDOWN_FINALIZE,
    SystemShutdownFinalizeEvent,
)
from ...extensions.api import ANY_VERSION


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
        SystemShutdownCancelledEvent, SystemShutdownCancelledEvent()
    )
    register_event(
        bus, EVENT_ID_SYSTEM_SHUTDOWN_FINALIZE, QUEUE_EVENT_NORMAL,
        SystemShutdownFinalizeEvent, SystemShutdownFinalizeEvent()
    )


EXTENSION_METADATA: ExtensionMetadataStruct = {
    "name": "core.shutdown.api",
    "version": (1, 0, 0,),
    "type": "api",
    "depends": [],
    "defaults": [{
        "extension": "default.shutdown.timer",
        "minimum": ANY_VERSION,
    }],
    "authors": ["Petronia"],
}
