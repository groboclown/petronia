
from .....aid.bootstrap import (
    EventBus,
    register_event,
    QUEUE_EVENT_NORMAL,
    CONSUME_EVENT_PROTECTION,
    REQUEST_EVENT_PROTECTION,
    NOT_PARTICIPANT,
    ANY_VERSION,
)
from .events import (
    EVENT_ID_REQUEST_ASSIGN_WINDOW_TO_TILE,
    RequestAssignWindowToTileEvent,

    EVENT_ID_REQUEST_SET_NEXT_WINDOW_ACTIVE,
    RequestSetNextWindowActiveEvent,

    EVENT_ID_REQUEST_SET_WINDOW_VISIBILITY,
    RequestSetWindowVisibility,

    EVENT_ID_REQUEST_CHANGE_WINDOW_SETTINGS,
    RequestChangeWindowSettings,
)
from .....base.internal_.internal_extension import petronia_extension


def bootstrap_layout_window_api(bus: EventBus) -> None:
    register_event(
        bus, EVENT_ID_REQUEST_ASSIGN_WINDOW_TO_TILE, QUEUE_EVENT_NORMAL, REQUEST_EVENT_PROTECTION,
        RequestAssignWindowToTileEvent, RequestAssignWindowToTileEvent(
            NOT_PARTICIPANT, NOT_PARTICIPANT, 0, '', False
        )
    )
    register_event(
        bus, EVENT_ID_REQUEST_SET_NEXT_WINDOW_ACTIVE, QUEUE_EVENT_NORMAL, REQUEST_EVENT_PROTECTION,
        RequestSetNextWindowActiveEvent, RequestSetNextWindowActiveEvent(1)
    )
    register_event(
        bus, EVENT_ID_REQUEST_SET_WINDOW_VISIBILITY, QUEUE_EVENT_NORMAL, REQUEST_EVENT_PROTECTION,
        RequestSetWindowVisibility, RequestSetWindowVisibility(None, False)
    )
    register_event(
        bus, EVENT_ID_REQUEST_CHANGE_WINDOW_SETTINGS, QUEUE_EVENT_NORMAL, REQUEST_EVENT_PROTECTION,
        RequestChangeWindowSettings, RequestChangeWindowSettings(None, 0, '', False)
    )


EXTENSION_METADATA = petronia_extension({
    "name": "core.layout.window.api",
    "type": "api",
    "version": (1, 0, 0,),
    "depends": ({
        "extension": "core.state.api",
        "minimum": ANY_VERSION,
    },),
})
