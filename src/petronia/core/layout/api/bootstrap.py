

from ....aid.simp import (
    EventBus,
)
from ....aid.bootstrap import (
    QUEUE_EVENT_NORMAL,
    ExtensionMetadataStruct,
    register_event,
    ANY_VERSION,
)
from .events import (
    EVENT_ID_LAYOUT_CHANGED,
    LayoutChangedEvent,

    EVENT_ID_REQUEST_MOVE_RESIZE_FOCUSED_WINDOW,
    RequestMoveResizeFocusedWindowEvent,
)


def bootstrap_layout_api(bus: EventBus) -> None:
    register_event(
        bus, EVENT_ID_LAYOUT_CHANGED, QUEUE_EVENT_NORMAL,
        LayoutChangedEvent, LayoutChangedEvent()
    )
    register_event(
        bus, EVENT_ID_REQUEST_MOVE_RESIZE_FOCUSED_WINDOW, QUEUE_EVENT_NORMAL,
        RequestMoveResizeFocusedWindowEvent, RequestMoveResizeFocusedWindowEvent(0, 0, 0, 0)
    )


EXTENSION_METADATA: ExtensionMetadataStruct = {
    "name": "core.layout.api",
    "version": (1, 0, 0,),

    "type": "api",
    "depends": [],
    "defaults": [
        {
            "extension": "default.layout.tile",
            "minimum": ANY_VERSION,
        }
    ],
    "authors": ["Petronia"],
}
