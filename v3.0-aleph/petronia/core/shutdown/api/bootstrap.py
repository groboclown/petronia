
"""
Setup the extension.
"""

from ....base.bus import (
    EventBus,
    register_event,
    QUEUE_EVENT_NORMAL,
)
from ....base.events.bus import (
    PRODUCE_EVENT_PROTECTION, CONSUME_EVENT_PROTECTION,
)
from ....base.internal_.internal_extension import petronia_extension

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
        bus, EVENT_ID_REQUEST_SYSTEM_SHUTDOWN, QUEUE_EVENT_NORMAL, PRODUCE_EVENT_PROTECTION,
        RequestSystemShutdownEvent, RequestSystemShutdownEvent()
    )
    register_event(
        bus, EVENT_ID_REQUEST_CANCEL_SYSTEM_SHUTDOWN, QUEUE_EVENT_NORMAL, PRODUCE_EVENT_PROTECTION,
        RequestCancelSystemShutdownEvent, RequestCancelSystemShutdownEvent()
    )
    register_event(
        bus, EVENT_ID_SYSTEM_SHUTDOWN, QUEUE_EVENT_NORMAL, CONSUME_EVENT_PROTECTION,
        SystemShutdownEvent, SystemShutdownEvent()
    )
    register_event(
        bus, EVENT_ID_SYSTEM_SHUTDOWN_CANCELLED, QUEUE_EVENT_NORMAL, CONSUME_EVENT_PROTECTION,
        SystemShutdownCancelledEvent, SystemShutdownCancelledEvent()
    )
    register_event(
        bus, EVENT_ID_SYSTEM_SHUTDOWN_FINALIZE, QUEUE_EVENT_NORMAL, CONSUME_EVENT_PROTECTION,
        SystemShutdownFinalizeEvent, SystemShutdownFinalizeEvent()
    )


EXTENSION_METADATA = petronia_extension({
    "name": "core.shutdown.api",
    "version": (1, 0, 0,),
    "type": "api",
    "depends": (),
    "defaults": ({
        "extension": "default.shutdown.timer",
        "minimum": ANY_VERSION,
    },),
    "authors": ("Petronia",),
    "license": ("MIT",),
})
