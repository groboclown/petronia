
"""
Basic events generated by layouts.

Layouts define how native windows arrange themselves on the screen.  They can
also control hidden / shown states of the native windows.

Layouts perform the control through several mechanisms:

* Direct movement and minimize / maximize / etc of the native windows.
* (This needs to be worked out better)
    * They "tag" each window to associate it with a "tile" state.
    * They manage tile states.  A window can be associated with zero or one tile, and a tile can be associated
        with zero to many windows.
    * virtual screens are a side-effect of tile tags + layout managed windows?
    * Need to work out tag collections, associations with tiles, and virtual screens.  That is non-obvious
        at the moment.

"""

from .bootstrap import bootstrap_layout_api as start_extension
from .bootstrap import EXTENSION_METADATA

from .events import (
    TARGET_ID_LAYOUT,
    EVENT_ID_LAYOUT_CHANGED,
    LayoutChangedEvent,
    as_layout_changed_listener,
    send_layout_changed_event,

    EVENT_ID_REQUEST_MOVE_RESIZE_FOCUSED_WINDOW,
    RequestMoveResizeFocusedWindowEvent,
    as_request_move_resize_focused_window_listener,
    send_request_move_resize_focused_window_event,

    EVENT_ID_REQUEST_SHIFT_LAYOUT_FOCUS,
    RequestShiftLayoutFocusEvent,
    as_request_shift_layout_focus_listener,
    send_request_shift_layout_focus_event,

    EVENT_ID_REQUEST_SET_FOCUSED_WINDOW_VISIBILITY,
    RequestSetFocusedWindowVisibilityEvent,
    as_request_set_focused_window_visibility_listener,
    send_request_set_window_visibility_event,
)

from .tile_state import (
    STATE_ID_TILE,
    TileState,
    AllTileState,
    set_tile_states,
    create_tile_state_watch,
    send_tile_created_event,
    add_tile_created_listener,
)
