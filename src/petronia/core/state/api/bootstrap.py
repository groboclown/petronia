
"""
EventBus interaction for the global state.
"""

from .events import (
    EVENT_ID_UPDATE_STATE_REQUEST,
    StateStoreUpdateRequestEvent,

    EVENT_ID_UPDATED_STATE,
    StateStoreUpdatedEvent,
)
from ....base import (
    NOT_PARTICIPANT,
    create_singleton_identity,
)
from ....base.bus import (
    register_event,
    EventBus,
    ExtensionMetadataStruct,
    QUEUE_EVENT_NORMAL,
)
from ...extensions.api import ANY_VERSION


STATE_STORE_MODULE_ID = create_singleton_identity('core.state.api')


def bootstrap_state_store_api(bus: EventBus) -> None:
    """Register all state store events."""
    register_event(
        bus,
        EVENT_ID_UPDATE_STATE_REQUEST,
        QUEUE_EVENT_NORMAL,
        StateStoreUpdateRequestEvent,
        StateStoreUpdateRequestEvent(NOT_PARTICIPANT, object, object()) # type: ignore
    )
    register_event(
        bus,
        EVENT_ID_UPDATED_STATE,
        QUEUE_EVENT_NORMAL,
        StateStoreUpdatedEvent,
        StateStoreUpdatedEvent(NOT_PARTICIPANT, object, object(), object()) # type: ignore
    )


EXTENSION_METADATA: ExtensionMetadataStruct = {
    "name": "core.state.api",
    "version": (1, 0, 0,),
    "type": "api",
    "depends": [],
    "defaults": [{
        "extension": "default.state",
        "minimum": ANY_VERSION,
    }],
    "authors": ["Petronia"],
}
