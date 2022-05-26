"""Generated list of atoms."""

from typing import Sequence, Dict, List, Tuple
import ctypes

from petronia_common.util import StdRet
from . import xcb_native


class AtomDef:
    __slots__ = ('_vals',)

    def __init__(self, vals: Dict[str, xcb_native.XcbAtom]) -> None:
        self._vals = vals

    def __getattr__(self, item: str) -> xcb_native.XcbAtom:
        """Fetch the value, if known.  Otherwise, raises a key error."""
        return self._vals[item]


def initialize_atoms(
        lib: xcb_native.LibXcb,
        conn: xcb_native.XcbConnectionP,
) -> StdRet[AtomDef]:
    """Initialize the atom list."""
    refs: Dict[str, xcb_native.XcbAtom] = {}

    cookies: List[Tuple[bytes, xcb_native.XcbInternAtomCookie]] = []

    # Make the request first
    for name in _ATOM_NAMES:
        chars = ctypes.c_char_p(name)
        cookie = lib.xcb_intern_atom_unchecked(
            conn, ctypes.c_uint8(0), ctypes.c_uint16(len(name) - 1), chars,
        )
        cookies.append((name, cookie))

    # Then check responses
    for name, cookie in cookies:
        reply = lib.xcb_intern_atom_reply(conn, cookie, ctypes.cast(xcb_native.NULL, xcb_native.XcbGenericErrorPP))
        if not reply:
            # Error occurred; get the next atom.
            continue
        try:
            atom = reply.contents.atom
            name_str = name.decode('utf-8')
        finally:
            lib.free(reply)

        refs[name_str] = atom
        # Strip off leading '_' because of python naming.
        while name_str.startswith('_'):
            name_str = name_str[1:]
        if name_str not in refs:
            refs[name_str] = atom

    return StdRet.pass_ok(AtomDef(refs))


_ATOM_NAMES: Sequence[bytes] = (
    # Taken from xcb-util-wm-0.4.1, ewmh/atomlist.m4
    b"_NET_SUPPORTED",
    b"_NET_CLIENT_LIST",
    b"_NET_CLIENT_LIST_STACKING",
    b"_NET_NUMBER_OF_DESKTOPS",
    b"_NET_DESKTOP_GEOMETRY",
    b"_NET_DESKTOP_VIEWPORT",
    b"_NET_CURRENT_DESKTOP",
    b"_NET_DESKTOP_NAMES",
    b"_NET_ACTIVE_WINDOW",
    b"_NET_WORKAREA",
    b"_NET_SUPPORTING_WM_CHECK",
    b"_NET_VIRTUAL_ROOTS",
    b"_NET_DESKTOP_LAYOUT",
    b"_NET_SHOWING_DESKTOP",
    b"_NET_CLOSE_WINDOW",
    b"_NET_MOVERESIZE_WINDOW",
    b"_NET_WM_MOVERESIZE",
    b"_NET_RESTACK_WINDOW",
    b"_NET_REQUEST_FRAME_EXTENTS",
    b"_NET_WM_NAME",
    b"_NET_WM_VISIBLE_NAME",
    b"_NET_WM_ICON_NAME",
    b"_NET_WM_VISIBLE_ICON_NAME",
    b"_NET_WM_DESKTOP",
    b"_NET_WM_WINDOW_TYPE",
    b"_NET_WM_STATE",
    b"_NET_WM_ALLOWED_ACTIONS",
    b"_NET_WM_STRUT",
    b"_NET_WM_STRUT_PARTIAL",
    b"_NET_WM_ICON_GEOMETRY",
    b"_NET_WM_ICON",
    b"_NET_WM_PID",
    b"_NET_WM_HANDLED_ICONS",
    b"_NET_WM_USER_TIME",
    b"_NET_WM_USER_TIME_WINDOW",
    b"_NET_FRAME_EXTENTS",
    b"_NET_WM_PING",
    b"_NET_WM_SYNC_REQUEST",
    b"_NET_WM_SYNC_REQUEST_COUNTER",
    b"_NET_WM_FULLSCREEN_MONITORS",
    b"_NET_WM_FULL_PLACEMENT",
    b"UTF8_STRING",
    b"WM_PROTOCOLS",
    b"MANAGER",
    b"_NET_WM_WINDOW_TYPE_DESKTOP",
    b"_NET_WM_WINDOW_TYPE_DOCK",
    b"_NET_WM_WINDOW_TYPE_TOOLBAR",
    b"_NET_WM_WINDOW_TYPE_MENU",
    b"_NET_WM_WINDOW_TYPE_UTILITY",
    b"_NET_WM_WINDOW_TYPE_SPLASH",
    b"_NET_WM_WINDOW_TYPE_DIALOG",
    b"_NET_WM_WINDOW_TYPE_DROPDOWN_MENU",
    b"_NET_WM_WINDOW_TYPE_POPUP_MENU",
    b"_NET_WM_WINDOW_TYPE_TOOLTIP",
    b"_NET_WM_WINDOW_TYPE_NOTIFICATION",
    b"_NET_WM_WINDOW_TYPE_COMBO",
    b"_NET_WM_WINDOW_TYPE_DND",
    b"_NET_WM_WINDOW_TYPE_NORMAL",
    b"_NET_WM_STATE_MODAL",
    b"_NET_WM_STATE_STICKY",
    b"_NET_WM_STATE_MAXIMIZED_VERT",
    b"_NET_WM_STATE_MAXIMIZED_HORZ",
    b"_NET_WM_STATE_SHADED",
    b"_NET_WM_STATE_SKIP_TASKBAR",
    b"_NET_WM_STATE_SKIP_PAGER",
    b"_NET_WM_STATE_HIDDEN",
    b"_NET_WM_STATE_FULLSCREEN",
    b"_NET_WM_STATE_ABOVE",
    b"_NET_WM_STATE_BELOW",
    b"_NET_WM_STATE_DEMANDS_ATTENTION",
    b"_NET_WM_ACTION_MOVE",
    b"_NET_WM_ACTION_RESIZE",
    b"_NET_WM_ACTION_MINIMIZE",
    b"_NET_WM_ACTION_SHADE",
    b"_NET_WM_ACTION_STICK",
    b"_NET_WM_ACTION_MAXIMIZE_HORZ",
    b"_NET_WM_ACTION_MAXIMIZE_VERT",
    b"_NET_WM_ACTION_FULLSCREEN",
    b"_NET_WM_ACTION_CHANGE_DESKTOP",
    b"_NET_WM_ACTION_CLOSE",
    b"_NET_WM_ACTION_ABOVE",
    b"_NET_WM_ACTION_BELOW",
)
