
from .states import (
    NO_BORDER,
    WorkspaceState,
    TileState,
)
from .events import (
    EVENT_ID_REQUEST_SET_ACTIVE_TILE,
    RequestSetActiveTileEvent,

    EVENT_ID_REQUEST_MOVE_RESIZE_ACTIVE_TILE,
    RequestMoveResizeActiveTileEvent,

    EVENT_ID_REQUEST_SET_VIRTUAL_WORKSPACE,
    RequestSetVirtualWorkspaceEvent,

    EVENT_ID_REQUEST_REMOVE_ACTIVE_TILE,
    RequestRemoveActiveTileEvent,

    EVENT_ID_REQUEST_SET_TILE_BORDER_SIZE,
    RequestSetTileBorderSizeEvent,

    EVENT_ID_ACTIVE_VIRTUAL_WORKSPACE_CHANGED,
    ActiveVirtualWorkspaceChangedEvent,

    EVENT_ID_ACTIVE_TILE_CHANGED,
    ActiveTileChangedEvent,
)
from .....aid.std import (
    EventBus,
    STRING_EMPTY_TUPLE,
)
from .....aid.bootstrap import (
    ANY_VERSION,
    QUEUE_EVENT_NORMAL,
    REQUEST_EVENT_PROTECTION,
    CONSUME_EVENT_PROTECTION,
    NOT_PARTICIPANT,
    register_event,
)
from ....platform.api.defs import ZERO_SCREEN_AREA
from .....base.internal_.internal_extension import petronia_extension


def bootstrap_layout_api(bus: EventBus) -> None:
    register_event(
        bus, EVENT_ID_REQUEST_SET_ACTIVE_TILE, QUEUE_EVENT_NORMAL, REQUEST_EVENT_PROTECTION,
        RequestSetActiveTileEvent, RequestSetActiveTileEvent(NOT_PARTICIPANT)
    )
    register_event(
        bus, EVENT_ID_REQUEST_MOVE_RESIZE_ACTIVE_TILE, QUEUE_EVENT_NORMAL, REQUEST_EVENT_PROTECTION,
        RequestMoveResizeActiveTileEvent, RequestMoveResizeActiveTileEvent(0, 0, 0, 0, 0)
    )
    register_event(
        bus, EVENT_ID_REQUEST_REMOVE_ACTIVE_TILE, QUEUE_EVENT_NORMAL, REQUEST_EVENT_PROTECTION,
        RequestRemoveActiveTileEvent, RequestRemoveActiveTileEvent()
    )
    register_event(
        bus, EVENT_ID_REQUEST_SET_TILE_BORDER_SIZE, QUEUE_EVENT_NORMAL, REQUEST_EVENT_PROTECTION,
        RequestSetTileBorderSizeEvent, RequestSetTileBorderSizeEvent(NO_BORDER)
    )
    register_event(
        bus, EVENT_ID_REQUEST_SET_VIRTUAL_WORKSPACE, QUEUE_EVENT_NORMAL, REQUEST_EVENT_PROTECTION,
        RequestSetVirtualWorkspaceEvent, RequestSetVirtualWorkspaceEvent('')
    )
    register_event(
        bus, EVENT_ID_ACTIVE_VIRTUAL_WORKSPACE_CHANGED, QUEUE_EVENT_NORMAL, CONSUME_EVENT_PROTECTION,
        ActiveVirtualWorkspaceChangedEvent, ActiveVirtualWorkspaceChangedEvent(WorkspaceState(
            '',
            (TileState(NOT_PARTICIPANT, ZERO_SCREEN_AREA, ZERO_SCREEN_AREA, 0, '', STRING_EMPTY_TUPLE),),
            NOT_PARTICIPANT,
        ))
    )
    register_event(
        bus, EVENT_ID_ACTIVE_TILE_CHANGED, QUEUE_EVENT_NORMAL, CONSUME_EVENT_PROTECTION,
        ActiveTileChangedEvent, ActiveTileChangedEvent(TileState(
            NOT_PARTICIPANT, ZERO_SCREEN_AREA, ZERO_SCREEN_AREA, 0, '', STRING_EMPTY_TUPLE
        ))
    )


EXTENSION_METADATA = petronia_extension({
    "name": "core.layout.tile.api",
    "type": "api",
    "version": (1, 0, 0,),
    "depends": ({
        "extension": "core.state.api",
        "minimum": ANY_VERSION,
    },),
})
