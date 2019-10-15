

from ....aid.bootstrap import (
    EventBus,
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

    EVENT_ID_REQUEST_SHIFT_LAYOUT_FOCUS,
    RequestShiftLayoutFocusEvent,

    EVENT_ID_REQUEST_SET_FOCUSED_WINDOW_VISIBILITY,
    RequestSetFocusedWindowVisibilityEvent,
)


def bootstrap_layout_api(bus: EventBus) -> None:
    register_event(
        bus, EVENT_ID_LAYOUT_CHANGED, QUEUE_EVENT_NORMAL,
        LayoutChangedEvent, LayoutChangedEvent()
    )
    register_event(
        bus, EVENT_ID_REQUEST_MOVE_RESIZE_FOCUSED_WINDOW, QUEUE_EVENT_NORMAL,
        RequestMoveResizeFocusedWindowEvent, RequestMoveResizeFocusedWindowEvent(0, 0, 0, 0, 0)
    )
    register_event(
        bus, EVENT_ID_REQUEST_SHIFT_LAYOUT_FOCUS, QUEUE_EVENT_NORMAL,
        RequestShiftLayoutFocusEvent, RequestShiftLayoutFocusEvent('', 0)
    )
    register_event(
        bus, EVENT_ID_REQUEST_SET_FOCUSED_WINDOW_VISIBILITY, QUEUE_EVENT_NORMAL,
        RequestSetFocusedWindowVisibilityEvent, RequestSetFocusedWindowVisibilityEvent(False)
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
