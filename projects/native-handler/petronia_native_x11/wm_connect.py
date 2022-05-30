"""Connect to the X server, become a window manager, and grab the screen."""

from typing import List, Optional, Callable, Any
import ctypes
from petronia_common.util import StdRet, RET_OK_NONE, T
from petronia_common.util import i18n as _
from petronia_native.common import user_messages
from petronia_native_x11 import common_data
from .libs import (
    libxcb, libxcb_types, libxcb_consts,
    xcb_atoms, libcairo_consts, libxcb_icccm, ct_util,
)


_PETRONIA_CHAR_P = ctypes.c_char_p(b'petronia')
_PETRONIA_CI_CHAR_P = ctypes.c_char_p(b'petronia\0petronia')
_WM_S_CHAR_P = ctypes.c_char_p(b'WM_S')
_SELECTION_OWNER_WINDOW_CHAR_P = ctypes.c_char_p(b'Petronia WM_Sn selection owner window')


def connect_as_wm(libs: common_data.Libraries) -> StdRet[common_data.WindowManagerData]:
    cxt = WindowManagerDataBuilder(libs)

    return _ordered_res(
        lambda: cxt.close(),

        lambda: _connect(cxt),
        lambda: _with_screen(cxt),
        lambda: _with_visual(
            cxt=cxt,
            use_argb_visual=libs.config.get_config().connection.use_argb_visual,
        ),
        lambda: _with_atoms(cxt),
        lambda: _test_cairo_surface(cxt),
        lambda: _with_timestamp(cxt),
        lambda: _acquire_wm_sn(
            cxt=cxt,
            replace_existing=libs.config.get_config().connection.replace_existing_wm,
        ),
        lambda: _become_window_manager(cxt),
        lambda: _grab_server(cxt),
        lambda: _prefetch_maximum_request_length(cxt),
    ).then(lambda x: cxt.build())


class WindowManagerDataBuilder:
    """Data holder to pass the large amounts of data around."""
    __slots__ = (
        'lib',
        'conn', 'screen', 'default_visual', 'visual',
        'default_depth', 'default_colormap', 'atoms',
        'timestamp', 'default_screen',
        'default_depth_raw', 'selection_atom', 'selection_owner_window',
    )

    def __init__(self, lib: common_data.Libraries) -> None:
        self.lib = lib
        self.conn: Optional[libxcb_types.XcbConnectionP] = None
        self.default_screen = ctypes.c_int(0)
        self.screen: Optional[libxcb_types.XcbScreenP] = None
        self.default_visual: Optional[libxcb_types.XcbVisualtypeP] = None
        self.visual: Optional[libxcb_types.XcbVisualtypeP] = None
        self.default_depth_raw = ctypes.c_uint8(0)
        self.default_depth: int = 0
        self.default_colormap: int = 0
        self.timestamp = libxcb_types.XcbTimestamp(0)
        self.atoms: Optional[xcb_atoms.AtomDef] = None
        self.selection_atom: Optional[libxcb_types.XcbAtom] = None
        self.selection_owner_window: Optional[libxcb_types.XcbWindow] = None

    def close(self) -> None:
        """Close any open connections."""
        if self.conn:
            self.lib.xcb.xcb_ungrab_server(self.conn)
            self.lib.xcb.xcb_disconnect(self.conn)
            self.conn = None

    def build(self) -> StdRet[common_data.WindowManagerData]:
        return StdRet.pass_ok(common_data.WindowManagerData(
            libs=self.lib,
            conn=self.conn,
            default_screen=self.default_screen,
            screen=self.screen,
            default_visual=self.default_visual,
            visual=self.visual,
            default_depth_raw=self.default_depth_raw,
            default_depth=self.default_depth,
            default_colormap=self.default_colormap,
            timestamp=self.timestamp,
            atoms=self.atoms,
            selection_atom=self.selection_atom,
            selection_owner_window=self.selection_owner_window,
        ))


def _connect(cxt: WindowManagerDataBuilder) -> StdRet[None]:
    # Sets:
    #   +cxt.conn
    _debug("Connecting")
    assert not cxt.conn  # nosec  # programmer error

    _debug("connecting to default screen")
    conn = cxt.lib.xcb.xcb_connect(
        ct_util.NULL__c_char_p, ctypes.byref(cxt.default_screen),
    )
    cxt.conn = conn
    _debug("check if connection has error ({conn})", conn=conn)
    error_code = cxt.lib.xcb.xcb_connection_has_error(conn)
    _debug("error code {code}", code=error_code)
    if error_code != 0:
        return StdRet.pass_errmsg(
            user_messages.TRANSLATION_CATALOG,
            _('cannot open X11 display (error {error_code}'),
            error_code=repr(error_code),
        )
    return RET_OK_NONE


def _with_screen(cxt: WindowManagerDataBuilder) -> StdRet[None]:
    # Requires:
    #   -cxt.conn
    # Sets:
    #   +cxt.screen

    _debug("get screen")
    conn = _req(cxt.conn)
    if cxt.lib.has_xcb_util():
        # Full feature way
        cxt.screen = cxt.lib.xcb_util.xcb_aux_get_screen(conn, cxt.default_screen)
    else:
        # Works
        cxt.screen = cxt.lib.xcb.xcb_setup_roots_iterator(
            cxt.lib.xcb.xcb_get_setup(conn),
        ).data
    screen = _req(cxt.screen)
    cxt.default_visual = _find_visual(cxt.lib.xcb, screen, screen.contents.root_visual)

    return RET_OK_NONE


def _with_visual(*, cxt: WindowManagerDataBuilder, use_argb_visual: bool) -> StdRet[None]:
    # Requires:
    #   -cxt.conn
    # Sets:
    #   +cxt.default_visual
    #   +cxt.visual
    #   +cxt.default_depth_raw
    #   +cxt.default_depth
    #   +cxt.default_colormap

    conn = _req(cxt.conn)
    screen = _req(cxt.screen)

    _debug("get visual")
    cxt.default_visual = _find_visual(cxt.lib.xcb, screen, screen.contents.root_visual)

    if use_argb_visual:
        cxt.visual = _find_argb_visual(cxt.lib.xcb, screen)
    if not cxt.visual:
        cxt.visual = cxt.default_visual
    visual = _req(cxt.visual)

    _debug("get visual depth")
    depth_res = _find_visual_depth(
        cxt.lib.xcb, screen, visual.contents.visual_id,
    )
    if depth_res.has_error:
        return depth_res.forward()
    cxt.default_depth_raw = depth_res.value
    cxt.default_depth = ct_util.as_py_int(cxt.default_depth_raw)
    _debug("visual depth: {default_depth}", default_depth=cxt.default_depth)

    cxt.default_colormap = ct_util.as_py_int(screen.contents.default_colormap)
    if cxt.default_depth_raw != screen.contents.root_depth:
        # Need to create a color map since we aren't using the default depth
        _debug("Generating new colormap due to depth difference")
        cxt.default_colormap = cxt.lib.xcb.xcb_generate_id(_req(cxt.conn))
        cxt.lib.xcb.xcb_create_colormap(
            conn, libxcb_consts.XCB_COLORMAP_ALLOC_NONE__c,
            cxt.default_colormap, screen.contents.root,
            cxt.visual.contents.visual_id,
        )

    return RET_OK_NONE


def _with_atoms(cxt: WindowManagerDataBuilder) -> StdRet[None]:
    # Requires:
    #   -cxt.conn
    # Sets:
    #   +cxt.atoms
    _debug('Getting atoms')
    atom_res = xcb_atoms.initialize_atoms(cxt.lib.xcb, cxt.lib.clib, _req(cxt.conn))
    if atom_res.has_error:
        return atom_res.forward()
    cxt.atoms = atom_res.result
    return RET_OK_NONE


def _find_visual(
        lib: libxcb.LibXcb,
        screen: libxcb_types.XcbScreenP, visual: libxcb_types.XcbVisualid,
) -> libxcb_types.XcbVisualtypeP:
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
    return libxcb_types.XcbVisualtypeP()


def _find_argb_visual(
        lib: libxcb.LibXcb,
        screen: libxcb_types.XcbScreenP,
) -> libxcb_types.XcbVisualtypeP:
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
    _debug(" - not found; returning null")
    return libxcb_types.XcbVisualtypeP()


def _find_visual_depth(
        lib: libxcb.LibXcb,
        screen: libxcb_types.XcbScreenP,
        visual_id: libxcb_types.XcbVisualid,
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
                    return StdRet.pass_ok(ct_util.as_py_int(depth_iter.data.contents.depth))
                lib.xcb_visualtype_next(ctypes.byref(visual_iter))
            lib.xcb_depth_next(ctypes.byref(depth_iter))
    return StdRet.pass_errmsg(
        user_messages.TRANSLATION_CATALOG,
        _("could not find a visual's depth")
    )


def _test_cairo_surface(cxt: WindowManagerDataBuilder) -> StdRet[None]:
    """Test creation of a new surface."""
    _debug("test cairo surface")
    # create the 1x1 pixmap
    conn = _req(cxt.conn)
    screen = _req(cxt.screen)
    pixmap: libxcb_types.XcbPixmap = cxt.lib.xcb.xcb_generate_id(conn)
    cxt.lib.xcb.xcb_create_pixmap(
        conn, cxt.default_depth_raw, pixmap, screen.contents.root,
        ctypes.c_uint16(1), ctypes.c_uint16(1),
    )
    try:
        # Create the 1x1 surface
        surface = cxt.lib.cairo.cairo_xcb_surface_create(
            conn, pixmap, _req(cxt.visual),
            ctypes.c_int(1), ctypes.c_int(1),
        )
        status = cxt.lib.cairo.cairo_surface_status(surface)
        if status != libcairo_consts.CAIRO_STATUS_SUCCESS:
            return StdRet.pass_errmsg(
                user_messages.TRANSLATION_CATALOG,
                _('Could not set up display; cairo surface status {status}: {status_str}'),
                status=repr(status),
                status_str=repr(cxt.lib.cairo.cairo_status_to_string(status)),
            )

        # free the surface
        cxt.lib.cairo.cairo_surface_finish(surface)
        cxt.lib.cairo.cairo_surface_destroy(surface)
    finally:
        # free the pixmap
        cxt.lib.xcb.xcb_free_pixmap(cxt.conn, pixmap)
    return RET_OK_NONE


def _set_xwindow_name(
        lib: libxcb_icccm.LibXcbIcccm, conn: libxcb_types.XcbConnectionP,
        win: libxcb_types.XcbWindow, name: ctypes.c_char_p,
) -> None:
    """Set the static name of the window."""
    lib.xcb_icccm_set_wm_name(
        conn, win, libxcb_consts.XCB_ATOM_STRING__c, ctypes.c_uint8(8),
        ctypes.c_uint32(ctypes.sizeof(name) - 1), name,
    )


def _set_xwindow_petronia_class_instance(
        lib: libxcb_icccm.LibXcbIcccm, conn: libxcb_types.XcbConnectionP,
        win: libxcb_types.XcbWindow,
) -> None:
    """Set the class / instance for the petronia ownership."""
    lib.xcb_icccm_set_wm_class(
        conn, win, ctypes.c_uint32(ctypes.sizeof(_PETRONIA_CI_CHAR_P)), _PETRONIA_CI_CHAR_P,
    )


def _acquire_wm_sn(
        cxt: WindowManagerDataBuilder,
        replace_existing: bool,
) -> StdRet[None]:
    """Acquire the WM_Sn
    As per https://tronche.com/gui/x/icccm/sec-4.html#s-4.3
    the window manager must obtain the WM_S(n), where n is the screen number.
    """
    _debug("acquiring WM_Sn")
    if not cxt.lib.has_xcb_util():
        # No api available to do this.
        _debug("Can't acquire WM_Sn via the API.")
        return RET_OK_NONE

    lib = cxt.lib.xcb
    conn = _req(cxt.conn)
    screen = _req(cxt.screen)
    default_screen = _req(cxt.default_screen)
    timestamp = _req(cxt.timestamp)
    atoms = _req(cxt.atoms)

    _debug(" - create window")
    owner_window = lib.xcb_generate_id(conn)
    lib.xcb_create_window(
        conn, screen.contents.root_depth, owner_window, screen.contents.root,
        # x, y, width, height, border-width
        ctypes.c_int16(-1), ctypes.c_int16(-1), ctypes.c_uint16(1), ctypes.c_uint16(1),
        ctypes.c_uint16(0),
        libxcb_consts.XCB_COPY_FROM_PARENT, screen.contents.root_visual,
        ctypes.c_int32(0), ct_util.NULL,
    )
    if cxt.lib.has_xcb_icccm():
        _debug(" - set class and name")
        _set_xwindow_petronia_class_instance(cxt.lib.xcb_icccm, conn, owner_window)
        _set_xwindow_name(cxt.lib.xcb_icccm, conn, owner_window, _SELECTION_OWNER_WINDOW_CHAR_P)

    _debug(" - getting the atom name for the WM_Sn")
    atom_name = cxt.lib.xcb_util.xcb_atom_name_by_screen(
        _WM_S_CHAR_P, ct_util.as_uint8(default_screen),
    )
    if not atom_name:
        return StdRet.pass_errmsg(
            user_messages.TRANSLATION_CATALOG,
            _('Failed to allocate window manager; WM_Sn atom name failure')
        )
    _debug(f" - fetching the atom named {atom_name}")
    atom_q = lib.xcb_intern_atom_unchecked(
        conn, ctypes.c_uint8(0),
        ct_util.as_uint16(cxt.lib.clib.strlen(atom_name)), atom_name,
    )
    # Python is being helpful and returning the ctypes.c_char_p as a bytearray instead.
    #   ... for some implementations.
    if isinstance(atom_name, ctypes.c_char_p):
        _debug(f" - freeing the atom name {repr(atom_name)}")
        cxt.lib.clib.force_free(atom_name)
    _debug(" - getting the atom reply")
    atom_r = lib.xcb_intern_atom_reply(conn, atom_q, libxcb_consts.NULL__XcbGenericErrorPP)
    if not atom_r:
        return StdRet.pass_errmsg(
            user_messages.TRANSLATION_CATALOG,
            _('Failed to allocate window manager; WM_Sn atom name fetch failure')
        )
    atom: libxcb_types.XcbAtom = atom_r.contents.atom
    _debug(" - freeing the atom reply")
    cxt.lib.clib.force_free(atom_r)

    # If the selection is already owned, try to capture it.
    _debug(" - getting the selection owner")
    get_sel_reply = lib.xcb_get_selection_owner_reply(
        conn,
        lib.xcb_get_selection_owner(conn, atom), libxcb_consts.NULL__XcbGenericErrorPP,
    )
    if not get_sel_reply:
        return StdRet.pass_errmsg(
            user_messages.TRANSLATION_CATALOG,
            _('Failed to allocate window manager; get selection owner for WM_Sn failed'),
        )
    if (
            not replace_existing
            and ct_util.as_py_int(get_sel_reply.contents.owner)
            != ct_util.as_py_int(libxcb_consts.XCB_NONE)
    ):
        return StdRet.pass_errmsg(
            user_messages.TRANSLATION_CATALOG,
            _('Failed to allocate window manager; another window manager is running ({owner})'),
            owner=repr(get_sel_reply.contents.owner),
            rep=repr(replace_existing),
        )

    _debug(" - setting selection owner to the new window")
    lib.xcb_set_selection_owner(conn, owner_window, atom, timestamp)
    old_owner = get_sel_reply.contents.owner
    _debug(" - freeing the selection owner reply")
    cxt.lib.clib.force_free(get_sel_reply)
    if old_owner != libxcb_consts.XCB_NONE:
        # Wait for the old owner
        while True:
            _debug(" - getting the old owner")
            geometry_reply = lib.xcb_get_geometry_reply(
                conn, lib.xcb_get_geometry(conn, old_owner),
                libxcb_consts.NULL__XcbGenericErrorPP,
            )
            if geometry_reply:
                _debug(" - still exists; freeing the old owner reply")
                cxt.lib.clib.force_free(geometry_reply)
            else:
                break

    # custom event to announce that this connection is the new owner.
    _debug(" - announce this is the new owner")
    ev = libxcb_types.XcbClientMessageEvent()
    # lib.memset(
    #     ctypes.cast(ctypes.byref(ev), ctypes.c_void_p),
    #     ctypes.c_uint8(0), as_uint(ctypes.sizeof(ev)),
    # )
    ev.response_type = libxcb_consts.XCB_CLIENT_MESSAGE
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


def _with_timestamp(cxt: WindowManagerDataBuilder) -> StdRet[None]:
    """Get a timestamp from the X server. Each one of the pending events is an
    event that was fetched but not handled; they must all be freed."""
    lib = cxt.lib.xcb
    conn = _req(cxt.conn)
    screen = _req(cxt.screen)

    lib.xcb_grab_server(conn)
    property_data = _PropertyDataType(libxcb_consts.XCB_EVENT_MASK_PROPERTY_CHANGE__c)
    lib.xcb_change_window_attributes(
        conn, screen.contents.root, libxcb_consts.XCB_CW_EVENT_MASK__c,
        ctypes.cast(ctypes.byref(property_data), ctypes.c_void_p),
    )
    lib.xcb_change_property(
        conn, libxcb_consts.XCB_PROP_MODE_APPEND, screen.contents.root,
        libxcb_consts.XCB_ATOM_RESOURCE_MANAGER__c, libxcb_consts.XCB_ATOM_STRING__c,
        ctypes.c_uint8(8), ctypes.c_uint32(0), ct_util.NULL__c_char_p,
    )
    property_data = _PropertyDataType(0)
    lib.xcb_change_window_attributes(
        conn, screen.contents.root,
        libxcb_consts.XCB_CW_EVENT_MASK__c,
        ctypes.cast(ctypes.byref(property_data), ctypes.c_void_p),
    )
    lib.xcb_ungrab_server(conn)
    lib.xcb_flush(conn)

    # wait for the event.
    pending_events: List[libxcb_types.XcbGenericEventP] = []
    while True:
        event = lib.xcb_wait_for_event(conn)
        if not event:
            # what to do here?
            return StdRet.pass_errmsg(
                user_messages.TRANSLATION_CATALOG,
                _('No more events from X server'),
            )

        if libxcb.LibXcb.is_xcb_event_response_type(event, libxcb_consts.XCB_PROPERTY_NOTIFY):
            notify_evt = ctypes.cast(event, libxcb_types.XcbPropertyNotifyEventP)
            cxt.timestamp = notify_evt.contents.time
            cxt.lib.clib.force_free(event)
            return RET_OK_NONE
        # Each one of these will need to be freed.
        pending_events.append(event)


def _become_window_manager(cxt: WindowManagerDataBuilder) -> StdRet[None]:
    """Perform xcb_change_window_attributes_checked to become the new window manager"""
    conn = _req(cxt.conn)
    screen = _req(cxt.screen)

    select_input_val = libxcb_consts.XCB_EVENT_MASK_SUBSTRUCTURE_REDIRECT__c
    cookie = cxt.lib.xcb.xcb_change_window_attributes_checked(
        conn, screen.contents.root, libxcb_consts.XCB_CW_EVENT_MASK__c,
        ctypes.cast(ctypes.byref(select_input_val), ctypes.c_void_p),
    )
    err = cxt.lib.xcb.xcb_request_check(conn, cookie)
    if err:
        return StdRet.pass_errmsg(
            user_messages.TRANSLATION_CATALOG,
            _('Cannot select substructure redirect; e.g. another window manager is running'),
        )
    return RET_OK_NONE


def _grab_server(cxt: WindowManagerDataBuilder) -> StdRet[None]:
    # Start a bunch of actions once we've grabbed the server.
    cxt.lib.xcb.xcb_grab_server(_req(cxt.conn))
    return RET_OK_NONE


def _prefetch_maximum_request_length(cxt: WindowManagerDataBuilder) -> StdRet[None]:
    cxt.lib.xcb.xcb_prefetch_maximum_request_length(_req(cxt.conn))
    return RET_OK_NONE


def _req(val: Optional[T]) -> T:
    """Require that the value is not None."""
    if val is None:
        raise ValueError()
    return val


def _ordered_res(
        on_failure: Callable[[], None],
        *order: Callable[[], StdRet[None]],
) -> StdRet[None]:
    """Call each item in order.  If any one of them fails, exit at that point."""
    for callback in order:
        res = callback()
        if res.has_error:
            on_failure()
            return res.forward()
    return RET_OK_NONE


def _debug(message: str, **kwargs: Any) -> None:
    """Debug print."""
    user_messages.low_println(message.format(**kwargs))
