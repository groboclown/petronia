
"""
Setup for the API extension.
"""

from .events import (
    EVENT_ID_EXTENSION_LOADED,
    EVENT_ID_REQUEST_LOAD_EXTENSION,
    ExtensionLoadedEvent,
    RequestLoadExtensionEvent,
)
from .defs import LoadedExtension
from ....base.bus import (
    EventBus, register_event,
    ExtensionMetadataStruct,
    QUEUE_EVENT_NORMAL,
)
from ....base import create_singleton_identity
from ....base.events.bus import (
    REQUEST_EVENT_PROTECTION, RESPONSE_EVENT_PROTECTION,
)
from ....core.extensions.api import ANY_VERSION


MODULE_ID = create_singleton_identity('core.extensions.api')


def bootstrap_extensions_api(bus: EventBus) -> None:
    """Register all events."""
    register_event(
        bus, EVENT_ID_REQUEST_LOAD_EXTENSION, QUEUE_EVENT_NORMAL,
        REQUEST_EVENT_PROTECTION,
        RequestLoadExtensionEvent,
        RequestLoadExtensionEvent('x')
    )
    register_event(
        bus, EVENT_ID_EXTENSION_LOADED, QUEUE_EVENT_NORMAL,
        RESPONSE_EVENT_PROTECTION,
        ExtensionLoadedEvent,
        ExtensionLoadedEvent(LoadedExtension('x', True, (1, 0, 0,)), [])
    )


EXTENSION_METADATA: ExtensionMetadataStruct = {
    "name": "core.extensions.api",
    "version": (1, 0, 0,),
    "type": "api",
    "depends": [
        {
            # extensions publish a state.
            "extension": "core.state.api",
            "minimum": ANY_VERSION,
        }
    ],
    "defaults": [{
        "extension": "defimpl.extensions",
        "minimum": ANY_VERSION,
    }],
    "authors": ["Petronia"],
}
