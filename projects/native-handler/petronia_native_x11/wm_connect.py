"""Connects to the X server and establishes the connection
as the window manager."""

from typing import List, Sequence, Callable, Optional, Any
import ctypes
from petronia_common.util import T, StdRet, RET_OK_NONE
from petronia_common.util import i18n as _
from petronia_native.common import user_messages
from .api import XcbApi
from .event_handler import setup_event_listener_with_screen, EventHandlerLoop
from .xcb import xcb_native as nat
from .xcb.xcb_atoms import AtomDef, initialize_atoms
from .c_util import as_py_int, as_uint8, as_uint16

_PETRONIA_CHAR_P = ctypes.c_char_p(b'petronia')
_PETRONIA_CI_CHAR_P = ctypes.c_char_p(b'petronia\0petronia')
_WM_S_CHAR_P = ctypes.c_char_p(b'WM_S')
_SELECTION_OWNER_WINDOW_CHAR_P = ctypes.c_char_p(b'Petronia WM_Sn selection owner window')


class WmConnectionData:
    """Data holder to pass the large amounts of data around."""
    __slots__ = (
        'lib',
        'conn', 'screen', 'default_visual', 'visual',
        'default_depth', 'default_colormap', 'atoms',
        'cursor_context', 'timestamp', 'default_screen',
        'default_depth_raw', 'selection_atom', 'selection_owner_window',
        'pending_events', 'no_focus_window', 'graphics_context',
    )

    def __init__(self) -> None:
        self.lib = nat.LibXcb()
        self.conn: Optional[nat.XcbConnectionP] = None
        self.default_screen = ctypes.c_int(0)
        self.screen: Optional[nat.XcbScreenP] = None
        self.default_visual: Optional[nat.XcbVisualtypeP] = None
        self.visual: Optional[nat.XcbVisualtypeP] = None
        self.default_depth_raw = ctypes.c_uint8(0)
        self.default_depth: int = 0
        self.default_colormap: int = 0
        self.cursor_context: Optional[nat.XcbCursorContextP] = None
        self.timestamp = nat.XcbTimestamp(0)
        self.atoms: Optional[AtomDef] = None
        self.selection_atom: Optional[nat.XcbAtom] = None
        self.selection_owner_window: Optional[nat.XcbWindow] = None
        self.pending_events: List[nat.XcbGenericEventP] = []
        self.no_focus_window: Optional[nat.XcbWindow] = None
        self.graphics_context: Optional[nat.XcbGContext] = None

    def close(self, res: StdRet[T]) -> StdRet:
        """Close any open connections."""
        for event in self.pending_events:
            # Each pending event must be freed up.
            self.lib.free(event)
        self.pending_events.clear()

        if res.has_error:
            return res.forward()
        return RET_OK_NONE

    def create_api(self) -> XcbApi:
        """Turn this into an API."""
        return XcbApi(
            lib=self.lib,
            conn=_req(self.conn),
            screen=_req(self.screen),
            visual=_req(self.visual),
            default_depth=self.default_depth,
            default_colormap=self.default_colormap,
            cursor_context=_req(self.cursor_context),
            atoms=_req(self.atoms),
            selection_atom=_req(self.selection_atom),
            selection_owner_window=_req(self.selection_owner_window),
            timestamp=self.timestamp,
        )


class WMRet:
    """Return values from the window manager connection."""
    __slots__ = ('xcb', 'event_loop', 'shutdown')

    def __init__(self, xcb: XcbApi, loop: EventHandlerLoop) -> None:
        self.xcb = xcb
        self.event_loop = loop
        self.shutdown: List[Callable[[XcbApi], StdRet[None]]] = []


def connect_as_window_manager(
        *,
        on_server_init: Sequence[Callable[[XcbApi], StdRet[None]]],
        use_argb_visual: bool = True,
        replace_existing_wm: bool = False,
) -> StdRet[WMRet]:
    """Connect to the X server and attempt to become the window manager."""

    # TODO setup the event thread and use that to capture events?

    cxt = WmConnectionData()
    no_res = _with_connection(cxt)
    if no_res.has_error:
        return cxt.close(no_res)

    no_res = _with_visual(cxt=cxt, use_argb_visual=use_argb_visual)
    if no_res.has_error:
        return cxt.close(no_res)

    no_res = _with_atoms(cxt)
    if no_res.has_error:
        return cxt.close(no_res)

    no_res = _with_cursor_context(cxt)
    if no_res.has_error:
        return cxt.close(no_res)

    no_res = _with_extension_prefetch(cxt)
    if no_res.has_error:
        return cxt.close(no_res)

    no_res = _test_cairo_surface(cxt)
    if no_res.has_error:
        return cxt.close(no_res)

    no_res = _with_timestamp(cxt)
    if no_res.has_error:
        return cxt.close(no_res)

    no_res = _acquire_wm_sn(cxt, replace_existing_wm)
    if no_res.has_error:
        return cxt.close(no_res)

    # Start a bunch of actions once we've grabbed the server.
    cxt.lib.xcb_grab_server(_req(cxt.conn))

    no_res = _become_window_manager(cxt)
    if no_res.has_error:
        return cxt.close(no_res)

    cxt.lib.xcb_prefetch_maximum_request_length(_req(cxt.conn))

    no_res = _create_no_focus_window(cxt)
    if no_res.has_error:
        return cxt.close(no_res)

    xcb_api = cxt.create_api()

    for callback in on_server_init:
        no_res = callback(xcb_api)
        if no_res.has_error:
            return cxt.close(no_res)

    no_res = setup_event_listener_with_screen(xcb_api)
    if no_res.has_error:
        return cxt.close(no_res)

    cxt.lib.xcb_ungrab_server(_req(cxt.conn))

    event_loop = EventHandlerLoop(
        api=xcb_api,
        xcb=cxt.lib,
        conn=cxt.conn,

        # TODO replace with a real handler
        on_error=lambda x: user_messages.low_traceback(x),

        # TODO allow configuring queue wait time?
    )
    event_loop.add_missed_events(cxt.pending_events)
    ret = WMRet(xcb_api, event_loop)

    ret.shutdown.extend([
        _on_shutdown_cursor,
        _on_shutdown_xcb,
    ])

    return StdRet.pass_ok(ret)


def _with_connection(cxt: WmConnectionData) -> StdRet[None]:
    _debug("Connecting")
    if cxt.conn:
        return StdRet.pass_errmsg(
            user_messages.TRANSLATION_CATALOG,
            _('already connected to server'),
        )

    _debug("connecting to default screen")
    cxt.conn = cxt.lib.xcb_connect(nat.NULL__c_char_p, ctypes.byref(cxt.default_screen))
    _debug("check if connection has error ({conn})", conn=cxt.conn)
    error_code = cxt.lib.xcb_connection_has_error(_req(cxt.conn))
    _debug("error code {code}", code=error_code)
    if error_code != 0:
        return StdRet.pass_errmsg(
            user_messages.TRANSLATION_CATALOG,
            _('cannot open X11 display (error {error_code}'),
            error_code=repr(error_code),
        )
    return RET_OK_NONE


def _with_visual(*, cxt: WmConnectionData, use_argb_visual: bool) -> StdRet[None]:
    """Get the screen + visual + colormap.  Requires a connection."""
    _debug("get screen")
    conn = _req(cxt.conn)
    screen = cxt.lib.xcb_aux_get_screen(conn, cxt.default_screen)
    cxt.screen = screen
    cxt.default_visual = _find_visual(cxt.lib, screen, screen.contents.root_visual)

    _debug("get visual")
    cxt.visual = None
    if use_argb_visual:
        cxt.visual = _find_argb_visual(cxt.lib, cxt.screen)
    if not cxt.visual:
        cxt.visual = cxt.default_visual
    visual = _req(cxt.visual)

    _debug("get visual depth")
    depth_res = _find_visual_depth(
        cxt.lib, screen, visual.contents.visual_id,
    )
    if depth_res.has_error:
        return depth_res.forward()
    cxt.default_depth_raw = depth_res.value
    cxt.default_depth = as_py_int(cxt.default_depth_raw)
    _debug("visual depth: {default_depth}", default_depth=cxt.default_depth)

    cxt.default_colormap = as_py_int(screen.contents.default_colormap)
    if cxt.default_depth_raw != screen.contents.root_depth:
        # Need to create a color map since we aren't using the default depth
        _debug("Generating new colormap due to depth difference")
        cxt.default_colormap = cxt.lib.xcb_generate_id(_req(cxt.conn))
        cxt.lib.xcb_create_colormap(
            conn, nat.XCB_COLORMAP_ALLOC_NONE,
            cxt.default_colormap, screen.contents.root,
            cxt.visual.contents.visual_id,
        )

    return RET_OK_NONE


def _with_atoms(cxt: WmConnectionData) -> StdRet[None]:
    """Initialize the atoms."""
    atom_res = initialize_atoms(cxt.lib, _req(cxt.conn))
    if atom_res.has_error:
        return atom_res.forward()
    cxt.atoms = atom_res.result
    return RET_OK_NONE


def _with_cursor_context(cxt: WmConnectionData) -> StdRet[None]:
    """Initialize the cursor context."""
    conn = _req(cxt.conn)
    screen = _req(cxt.screen)
    cxt.cursor_context = nat.XcbCursorContextP()
    int_res = cxt.lib.xcb_cursor_context_new(conn, screen, ctypes.byref(cxt.cursor_context))
    if as_py_int(int_res) < 0:
        return StdRet.pass_errmsg(
            user_messages.TRANSLATION_CATALOG,
            _('xcb-cursor failed initialization'),
        )
    return RET_OK_NONE


def _with_extension_prefetch(cxt: WmConnectionData) -> StdRet[None]:
    """Prefetch the extensions"""
    conn = _req(cxt.conn)
    cxt.lib.xcb_prefetch_extension_data(conn, cxt.lib.xcb_big_requests_id)
    cxt.lib.xcb_prefetch_extension_data(conn, cxt.lib.xcb_test_id)
    cxt.lib.xcb_prefetch_extension_data(conn, cxt.lib.xcb_randr_id)
    cxt.lib.xcb_prefetch_extension_data(conn, cxt.lib.xcb_xinerama_id)
    return RET_OK_NONE


def _find_visual(
        lib: nat.LibXcb,
        screen: nat.XcbScreenP, visual: nat.XcbVisualid,
) -> nat.XcbVisualtypeP:
    """Find the visual type for the screen."""
    _debug("getting allowed screen depths")
    depth_iter = lib.xcb_screen_allowed_depths_iterator(screen)
    if depth_iter.data:
        while depth_iter.rem != 0:
            # _debug("Getting depth visuals")
            visual_iter = lib.xcb_depth_visuals_iterator(depth_iter.data)
            while visual_iter.rem != 0:
                # _debug("Found visual id {vid}", vid=repr(visual_iter.data.contents.visual_id))
                if visual_iter.data.contents.visual_id == visual:
                    return visual_iter.data
                # _debug("Getting next visual type")
                lib.xcb_visualtype_next(ctypes.byref(visual_iter))
            # _debug("getting next depth")
            lib.xcb_depth_next(ctypes.byref(depth_iter))
    return nat.XcbVisualtypeP()


def _find_argb_visual(
        lib: nat.LibXcb,
        screen: nat.XcbScreenP,
) -> nat.XcbVisualtypeP:
    """Find a visual for the screen with alpha-red-blue-green color depth."""
    _debug("finding argb visual")
    depth_iter = lib.xcb_screen_allowed_depths_iterator(screen)
    if depth_iter.data:
        while depth_iter.rem != 0:
            # _debug(" - checking depth {dep}", dep=depth_iter.data.contents.depth)
            if depth_iter.data.contents.depth == 32:
                # Get the first visual.
                visual_iter = lib.xcb_depth_visuals_iterator(depth_iter.data)
                if visual_iter.rem != 0:
                    return visual_iter.data
            # _debug(" - moving to next depth")
            # byref may not do the conversion right...
            ptr = ctypes.pointer(depth_iter)
            lib.xcb_depth_next(ptr)
    # _debug(" - not found; returning null")
    return nat.XcbVisualtypeP()


def _find_visual_depth(
        lib: nat.LibXcb,
        screen: nat.XcbScreenP,
        visual_id: nat.XcbVisualid,
) -> StdRet[int]:
    """Find the pixel depth (number of bits per pixel) for the visual."""
    _debug("finding visual depth")
    depth_iter = lib.xcb_screen_allowed_depths_iterator(screen)
    if depth_iter.data:
        while depth_iter.rem != 0:
            # _debug(" - checking depth {dep}", dep=depth_iter.data.contents.depth)
            visual_iter = lib.xcb_depth_visuals_iterator(depth_iter.data)
            while visual_iter.rem != 0:
                # _debug(" - checking visual {vid}", vid=visual_iter.data.contents.visual_id)
                if visual_id == visual_iter.data.contents.visual_id:
                    # officially returns a c_uint8, but Python auto-translates that to an int.
                    return StdRet.pass_ok(as_py_int(depth_iter.data.contents.depth))
                lib.xcb_visualtype_next(ctypes.byref(visual_iter))
            lib.xcb_depth_next(ctypes.byref(depth_iter))
    return StdRet.pass_errmsg(
        user_messages.TRANSLATION_CATALOG,
        _("could not find a visual's depth")
    )


def _test_cairo_surface(cxt: WmConnectionData) -> StdRet[None]:
    """Test creation of a new surface."""
    # create the 1x1 pixmap
    conn = _req(cxt.conn)
    pixmap: nat.XcbPixmap = cxt.lib.xcb_generate_id(conn)
    cxt.lib.xcb_create_pixmap(
        conn, cxt.default_depth_raw, pixmap, _req(cxt.screen).contents.root,
        ctypes.c_uint16(1), ctypes.c_uint16(1),
    )
    try:
        # Create the 1x1 surface
        surface = cxt.lib.cairo_xcb_surface_create(
            conn, pixmap, _req(cxt.visual),
            ctypes.c_int(1), ctypes.c_int(1),
        )
        status = cxt.lib.cairo_surface_status(surface)
        if status != nat.CAIRO_STATUS_SUCCESS:
            return StdRet.pass_errmsg(
                user_messages.TRANSLATION_CATALOG,
                _('Could not set up display; cairo surface status {status}: {status_str}'),
                status=repr(status),
                status_str=repr(cxt.lib.cairo_status_to_string(status)),
            )

        # free the surface
        cxt.lib.cairo_surface_finish(surface)
        cxt.lib.cairo_surface_destroy(surface)
    finally:
        # free the pixmap
        cxt.lib.xcb_free_pixmap(_req(cxt.conn), pixmap)
    return RET_OK_NONE


def _set_xwindow_name(
        lib: nat.LibXcb, conn: nat.XcbConnectionP,
        win: nat.XcbWindow, name: ctypes.c_char_p,
) -> None:
    """Set the static name of the window."""
    lib.xcb_icccm_set_wm_name(
        conn, win, nat.XCB_ATOM_STRING, ctypes.c_uint8(8),
        ctypes.c_uint32(ctypes.sizeof(name) - 1), name,
    )


def _set_xwindow_petronia_class_instance(
        lib: nat.LibXcb, conn: nat.XcbConnectionP,
        win: nat.XcbWindow,
) -> None:
    """Set the class / instance for the petronia ownership."""
    lib.xcb_icccm_set_wm_class(
        conn, win, ctypes.c_uint32(ctypes.sizeof(_PETRONIA_CI_CHAR_P)), _PETRONIA_CI_CHAR_P,
    )


def _acquire_wm_sn(
        cxt: WmConnectionData,
        replace_existing: bool,
) -> StdRet[None]:
    """Acquire the WM_Sn
    As per https://tronche.com/gui/x/icccm/sec-4.html#s-4.3
    the window manager must obtain the WM_S(n), where n is the screen number.

    Returns the owner window, atom
    """
    lib = cxt.lib
    conn = _req(cxt.conn)
    screen = _req(cxt.screen)
    default_screen = _req(cxt.default_screen)
    timestamp = _req(cxt.timestamp)
    atoms = _req(cxt.atoms)

    owner_window = lib.xcb_generate_id(conn)
    lib.xcb_create_window(
        conn, screen.contents.root_depth, owner_window, screen.contents.root,
        # x, y, width, height, border-width
        ctypes.c_int16(-1), ctypes.c_int16(-1), ctypes.c_uint16(1), ctypes.c_uint16(1),
        ctypes.c_uint16(0),
        nat.XCB_COPY_FROM_PARENT, screen.contents.root_visual,
        ctypes.c_int32(0), nat.NULL,
    )
    _set_xwindow_petronia_class_instance(lib, conn, owner_window)
    _set_xwindow_name(lib, conn, owner_window, _SELECTION_OWNER_WINDOW_CHAR_P)

    atom_name = lib.xcb_atom_name_by_screen(_WM_S_CHAR_P, as_uint8(default_screen))
    if not atom_name:
        return StdRet.pass_errmsg(
            user_messages.TRANSLATION_CATALOG,
            _('Failed to allocate window manager; WM_Sn atom name failure')
        )
    atom_q = lib.xcb_intern_atom_unchecked(
        conn, ctypes.c_uint8(0), as_uint16(lib.strlen(atom_name)), atom_name,
    )
    lib.free(atom_name)
    atom_r = lib.xcb_intern_atom_reply(conn, atom_q, nat.NULL_XcbGenericErrorPP)
    if not atom_r:
        return StdRet.pass_errmsg(
            user_messages.TRANSLATION_CATALOG,
            _('Failed to allocate window manager; WM_Sn atom name fetch failure')
        )
    atom: nat.XcbAtom = atom_r.contents.atom
    lib.free(atom_r)

    # If the selection is already owned, try to capture it.
    get_sel_reply = lib.xcb_get_selection_owner_reply(
        conn,
        lib.xcb_get_selection_owner(conn, atom), nat.NULL_XcbGenericErrorPP,
    )
    if not get_sel_reply:
        return StdRet.pass_errmsg(
            user_messages.TRANSLATION_CATALOG,
            _('Failed to allocate window manager; get selection owner for WM_Sn failed'),
        )
    if not replace_existing and as_py_int(get_sel_reply.contents.owner) != as_py_int(nat.XCB_NONE):
        return StdRet.pass_errmsg(
            user_messages.TRANSLATION_CATALOG,
            _('Failed to allocate window manager; another window manager is running ({owner})'),
            owner=repr(get_sel_reply.contents.owner),
            rep=repr(replace_existing),
        )

    lib.xcb_set_selection_owner(conn, owner_window, atom, timestamp)
    if get_sel_reply.contents.owner != nat.XCB_NONE:
        # Wait for the old owner
        while True:
            geometry_reply = lib.xcb_get_geometry_reply(
                conn, lib.xcb_get_geometry(conn, get_sel_reply.contents.owner),
                nat.NULL_XcbGenericErrorPP,
            )
            if geometry_reply:
                lib.free(geometry_reply)
            else:
                break
    lib.free(get_sel_reply)

    # custom event to announce that this connection is the new owner.
    ev = nat.XcbClientMessageEvent()
    # lib.memset(
    #     ctypes.cast(ctypes.byref(ev), ctypes.c_void_p),
    #     ctypes.c_uint8(0), as_uint(ctypes.sizeof(ev)),
    # )
    ev.response_type = nat.XCB_CLIENT_MESSAGE
    ev.window = screen.contents.root
    ev.format = 32
    ev.type = atoms.MANAGER
    ev.data.data32[0] = timestamp
    ev.data.data32[1] = atom
    ev.data.data32[2] = owner_window
    ev.data.data32[3] = 0
    ev.data.data32[4] = 0
    lib.xcb_send_event(
        conn, ctypes.c_uint8(0), screen.contents.root,
        ctypes.c_uint32(0xFFFFFF), ctypes.cast(ctypes.byref(ev), ctypes.c_char_p),
    )

    cxt.selection_atom = atom
    cxt.selection_owner_window = owner_window

    return RET_OK_NONE


_PropertyDataType = ctypes.c_uint32 * 1


def _with_timestamp(cxt: WmConnectionData) -> StdRet[None]:
    """Get a timestamp from the X server. Each one of the pending events is an
    event that was fetched but not handled; they must all be freed."""
    lib = cxt.lib
    conn = _req(cxt.conn)
    screen = _req(cxt.screen)

    lib.xcb_grab_server(conn)
    property_data = _PropertyDataType(nat.XCB_EVENT_MASK_PROPERTY_CHANGE__u32)
    lib.xcb_change_window_attributes(
        conn, screen.contents.root, nat.XCB_CW_EVENT_MASK_uint32,
        ctypes.cast(ctypes.byref(property_data), ctypes.c_void_p),
    )
    lib.xcb_change_property(
        conn, nat.XCB_PROP_MODE_APPEND, screen.contents.root,
        nat.XCB_ATOM_RESOURCE_MANAGER, nat.XCB_ATOM_STRING,
        ctypes.c_uint8(8), ctypes.c_uint32(0), nat.NULL__c_char_p,
    )
    property_data = _PropertyDataType(0)
    lib.xcb_change_window_attributes(
        conn, screen.contents.root,
        nat.XCB_CW_EVENT_MASK_uint32,
        ctypes.cast(ctypes.byref(property_data), ctypes.c_void_p),
    )
    lib.xcb_ungrab_server(conn)
    lib.xcb_flush(conn)

    # wait for the event.
    pending_events: List[nat.XcbGenericEventP] = []
    while True:
        event = lib.xcb_wait_for_event(conn)
        if not event:
            # what to do here?
            return StdRet.pass_errmsg(
                user_messages.TRANSLATION_CATALOG,
                _('No more events from X server'),
            )

        if nat.LibXcb.is_xcb_event_response_type(event, nat.XCB_PROPERTY_NOTIFY):
            notify_evt = ctypes.cast(event, nat.XcbPropertyNotifyEventP)
            cxt.timestamp = notify_evt.contents.time
            lib.free(event)
            return RET_OK_NONE
        # Each one of these will need to be freed.
        pending_events.append(event)


def _become_window_manager(cxt: WmConnectionData) -> StdRet[None]:
    """Perform xcb_change_window_attributes_checked to become the new window manager"""
    conn = _req(cxt.conn)
    screen = _req(cxt.screen)

    select_input_val = nat.XCB_EVENT_MASK_SUBSTRUCTURE_REDIRECT__u32
    cookie = cxt.lib.xcb_change_window_attributes_checked(
        conn, screen.contents.root, nat.XCB_CW_EVENT_MASK_uint32,
        ctypes.cast(ctypes.byref(select_input_val), ctypes.c_void_p),
    )
    err = cxt.lib.xcb_request_check(conn, cookie)
    if err:
        return StdRet.pass_errmsg(
            user_messages.TRANSLATION_CATALOG,
            _('Cannot select substructure redirect; e.g. another window manager is running'),
        )
    return RET_OK_NONE


def _create_no_focus_window(cxt: WmConnectionData) -> StdRet[None]:
    """Create a window to capture events when nothing else has focus.

    This also grabs a default GC with the default depth."""
    conn = _req(cxt.conn)
    screen = _req(cxt.screen)
    visual = _req(cxt.visual)

    no_focus_window = cxt.lib.xcb_generate_id(conn)
    cxt.no_focus_window = no_focus_window
    gc = cxt.lib.xcb_generate_id(conn)
    cxt.graphics_context = gc

    value_list_type = ctypes.c_uint32 * 4
    cxt.lib.xcb_create_window(
        # connection, depth, wid, parent
        conn, cxt.default_depth_raw, no_focus_window, screen.contents.root,

        # x, y, width, height, border_width
        ctypes.c_int16(-1), ctypes.c_int16(-1), ctypes.c_uint16(1), ctypes.c_uint16(1),
        ctypes.c_uint16(0),

        # class, visual
        nat.XCB_COPY_FROM_PARENT, visual.contents.visual_id,

        # value mask
        ctypes.c_int32(
                nat.XCB_CW_BACK_PIXEL | nat.XCB_CW_BORDER_PIXEL
                | nat.XCB_CW_OVERRIDE_REDIRECT | nat.XCB_CW_COLORMAP
        ),

        # value list
        ctypes.cast(
            value_list_type(
                screen.contents.white_pixel,
                screen.contents.black_pixel,
                1,
                cxt.default_colormap,
            ),
            ctypes.c_void_p,
        ),
    )
    _set_xwindow_petronia_class_instance(cxt.lib, conn, no_focus_window)
    _set_xwindow_name(cxt.lib, conn, no_focus_window, ctypes.c_char_p(b'Petronia Non Focus'))
    cxt.lib.xcb_map_window(conn, no_focus_window)
    gc_val_list_type = ctypes.c_uint32 * 2
    cxt.lib.xcb_create_gc(
        conn, gc, no_focus_window,
        nat.XCB_GC_FOREGROUND | nat.XCB_GC_BACKGROUND,
        ctypes.cast(
            gc_val_list_type(screen.contents.black_pixel, screen.contents.white_pixel),
            ctypes.c_void_p,
        ),
    )

    return RET_OK_NONE


def _on_shutdown_cursor(xcb: XcbApi, timeout: float) -> StdRet[None]:
    """Shutdown the cursor allocations."""
    xcb.disconnect_xcb_cursor()
    return RET_OK_NONE


def _on_shutdown_xcb(xcb: XcbApi, timeout: float) -> StdRet[None]:
    """Shutdown xcb"""
    xcb.disconnect_xcb()
    return RET_OK_NONE


def _req(val: Optional[T]) -> T:
    """Require that the value is not None."""
    if val is None:
        raise ValueError()
    return val


def _debug(message: str, **kwargs: Any) -> None:
    """Debug print."""
    user_messages.low_println(message.format(**kwargs))
