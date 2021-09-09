
"""
API defining states and events for extensions that handle the generation and
location of tiles on the screen.  "Tiles" is used here in a generic way; it
can refer to the regions of the screen on a tiling windowing system or just
the location of a window.

The tiles can have an associated virtual workspace.  This allows for having
different tiles for different "screens".

The tiles do not concern themselves with which windows are in the tile,
or how the tile decorates itself.  However, the tiles *do* contain information
regarding usable versus visible size, which is intended for decoration
purposes.  Windows within a tile should use the `usable_area`.

Tiles have the following traits:
    * (x,y) screen location for the NW corner of the tile.
    * (height, width) size of the tile.  This covers the entire tile,
      including any border added by the layout window extension.
    * z-index.  Relative height between tiles.  Each tile has its own z-index.
      Lower z-index tiles are drawn on top of higher z-index tiles.
    * Workspace ID.  This is the virtual workspace the tile lives in.
    * Tags.  A set of lower-cased user-supplied tags for the tile.  This can
      be used to auto-associate windows with a tile.

Implementations must:
    * Listen on `as_request_new_tile_listener` with CID `TARGET_ID_LAYOUT_TILE`
      for requests to create a new tile.
    * If the `as_request_new_tile_listener` callback triggers a tile creation,
      then the `send_tile_created_event` must be called, and also the
      `send_component_created_event` to the requester.
    * If a tile is created due to implicit layout actions and not from a
      request event, then call `send_tile_created_event`.
    * Listen on `as_request_dispose_component_listener` for each active
      tile.
    * If a tile is removed, then the `send_component_disposed` event is
      sent.
    * Any change to the internal tile state must generate a state change to
      the LayoutTileState and the TileState.
    * If the workspace state or active workspace changes, or if a tile is
      created or deleted, then LayoutTileState state change is sent.
    * Listen on `as_request_move_resize_focused_window_listener` with
      target ID `TARGET_ID_LAYOUT_TILE`.
    * Listen on `as_request_set_active_tile_listener` with target ID
      `TARGET_ID_LAYOUT_TILE`.
    * Listen on `as_request_remove_active_tile_listener` with target ID
      `TARGET_ID_LAYOUT_TILE`.
    * Listen on `as_request_set_virtual_screen_listener` with target ID
      `TARGET_ID_LAYOUT_TILE`.
    * Listen on `as_request_set_global_tile_border_size_listener` with
    * Listen on `as_request_set_tile_border_size_listener` for all tiles and
      for target ID `TARGET_ID_LAYOUT_TILE` (which adjusts the global tile
      borders, for all non-explicitly set border tiles).
    * On virtual workspace changing, the `send_active_virtual_workspace_changed`
      event is sent, followed by a `send_active_tile_changed` for the previously
      active tile on the switched-to workspace.
    * On active tile change, a `send_active_tile_changed` must be sent.
"""

from .bootstrap import bootstrap_layout_api as start_extension
from .bootstrap import EXTENSION_METADATA

from .states import (
    LayoutTileState,
    TileState,
    WorkspaceState,
    BorderSize,

    STATE_ID_LAYOUT_TILE,
    NO_BORDER,

    set_tile_state,
    create_tile_state_watch,
    send_tile_created_event,
    add_tile_created_listener,
    set_layout_tile_state,
    create_layout_tile_state_watch,
)
from .events import (
    TARGET_ID_LAYOUT_TILE,

    as_request_new_tile_listener,
    add_request_new_tile_listener,
    send_request_new_tile,

    EVENT_ID_REQUEST_MOVE_RESIZE_ACTIVE_TILE,
    RequestMoveResizeActiveTileEvent,
    as_request_move_resize_focused_window_listener,
    add_request_move_resize_focused_window_listener,
    send_request_move_resize_active_tile_event,

    EVENT_ID_REQUEST_SET_ACTIVE_TILE,
    RequestSetActiveTileEvent,
    as_request_set_active_tile_listener,
    add_request_set_active_tile_listener,
    send_request_set_active_tile_event,

    EVENT_ID_REQUEST_SET_TILE_BORDER_SIZE,
    RequestSetTileBorderSizeEvent,
    as_request_set_tile_border_size_listener,
    send_request_set_tile_border_size_event,
    as_request_set_global_tile_border_size_listener,
    add_request_set_global_active_tile_listener,
    send_request_set_global_tile_border_size_event,

    EVENT_ID_REQUEST_REMOVE_ACTIVE_TILE,
    RequestRemoveActiveTileEvent,
    as_request_remove_active_tile_listener,
    add_request_remove_active_tile_listener,
    send_request_remove_active_tile,

    EVENT_ID_REQUEST_SET_VIRTUAL_WORKSPACE,
    RequestSetVirtualWorkspaceEvent,
    as_request_set_virtual_workspace_listener,
    add_request_set_virtual_workspace_listener,
    send_request_set_virtual_workspace_event,

    EVENT_ID_ACTIVE_VIRTUAL_WORKSPACE_CHANGED,
    ActiveVirtualWorkspaceChangedEvent,
    as_active_virtual_workspace_changed_listener,
    add_active_virtual_workspace_changed_listener,
    send_active_virtual_workspace_changed_event
)
