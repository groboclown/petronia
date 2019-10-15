

from ....aid.bootstrap import (
    EventBus,
    QUEUE_EVENT_NORMAL,
    register_event,
    ANY_VERSION,
    CONSUME_EVENT_PROTECTION,
    REQUEST_EVENT_PROTECTION,
)
from ....base.internal_.internal_extension import petronia_extension
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
        bus, EVENT_ID_LAYOUT_CHANGED, QUEUE_EVENT_NORMAL, CONSUME_EVENT_PROTECTION,
        LayoutChangedEvent, LayoutChangedEvent()
    )
    register_event(
        bus, EVENT_ID_REQUEST_MOVE_RESIZE_FOCUSED_WINDOW, QUEUE_EVENT_NORMAL, REQUEST_EVENT_PROTECTION,
        RequestMoveResizeFocusedWindowEvent, RequestMoveResizeFocusedWindowEvent(0, 0, 0, 0, 0)
    )
    register_event(
        bus, EVENT_ID_REQUEST_SHIFT_LAYOUT_FOCUS, QUEUE_EVENT_NORMAL, REQUEST_EVENT_PROTECTION,
        RequestShiftLayoutFocusEvent, RequestShiftLayoutFocusEvent('', 0)
    )
    register_event(
        bus, EVENT_ID_REQUEST_SET_FOCUSED_WINDOW_VISIBILITY, QUEUE_EVENT_NORMAL, REQUEST_EVENT_PROTECTION,
        RequestSetFocusedWindowVisibilityEvent, RequestSetFocusedWindowVisibilityEvent(False)
    )


EXTENSION_METADATA = petronia_extension({
    "name": "core.layout.api",
    "version": (1, 0, 0,),

    "type": "api",
    "depends": (),
    "defaults": ({
        "extension": "default.layout.tile",
        "minimum": ANY_VERSION,
    },),
})
