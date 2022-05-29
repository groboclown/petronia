"""Xcb API usage and interface."""

from typing import Sequence, Optional, Any
import ctypes
from petronia_common.util import StdRet, RET_OK_NONE
from .xcb import xcb_native as nat
from .xcb.xcb_atoms import AtomDef


class Freeable:
    """A pointer that might be able to be freed."""
    __slots__ = ('__val',)

    def __init__(self, val: Any) -> None:
        self.__val = val

    def free(self, lib: nat.LibXcb) -> None:
        if self.__val is not None:
            lib.free(self.__val)
            self.__val = None


PROPERTY_MODE__REPLACE = nat.XCB_PROP_MODE_REPLACE
PROPERTY_MODE__PREPEND = nat.XCB_PROP_MODE_PREPEND
PROPERTY_MODE__APPEND = nat.XCB_PROP_MODE_APPEND
PropertyModeEnum = (PROPERTY_MODE__REPLACE, PROPERTY_MODE__PREPEND, PROPERTY_MODE__APPEND)


class XcbApi:
    """Interface with standard XCB stuff."""
    __slots__ = (
        '__lib', '__conn', '__screen', '__visual',
        '__default_depth', '__default_colormap',
        '__cursor_context', '__timestamp', '__atoms',
        '__selection_atom', '__selection_owner_window',
    )

    def __init__(
            self, *,
            lib: nat.LibXcb,
            conn: nat.XcbConnectionP,
            screen: nat.XcbScreenP,
            visual: nat.XcbVisualtypeP,
            default_depth: int,
            default_colormap: int,
            cursor_context: nat.XcbCursorContextP,
            atoms: AtomDef,
            selection_atom: nat.XcbAtom,
            selection_owner_window: nat.XcbWindow,
            timestamp: nat.XcbTimestamp,
    ) -> None:
        self.__lib = lib
        self.__conn = conn
        self.__screen = screen
        self.__visual = visual
        self.__default_depth = default_depth
        self.__default_colormap = default_colormap
        self.__cursor_context = cursor_context
        self.__atoms = atoms
        self.__selection_atom = selection_atom
        self.__selection_owner_window = selection_owner_window
        self.__timestamp = timestamp

    @property
    def atoms(self) -> AtomDef:
        """The registered atoms."""
        return self.__atoms

    @property
    def screen_root(self) -> nat.XcbWindow:
        """The screen root window."""
        return self.__screen.contents.root

    def change_window_property_uint32(
            self, *,
            mode: ctypes.c_uint8,
            window_id: Optional[nat.XcbWindow],
            property_atom: nat.XcbAtom,
            property_type: nat.XcbAtom,
            ctypes_data: Sequence[ctypes.c_uint32],
    ) -> StdRet[None]:
        """Set the window property to a list of 32 bit values."""
        assert mode in PropertyModeEnum  # nosec  # programmer check.
        data_type = ctypes.c_uint32 * len(ctypes_data)
        prop_data = data_type(ctypes_data)
        self.__lib.xcb_change_property(
            self.__conn, mode,
            window_id or self.__screen.contents.root,
            property_atom, property_type,
            ctypes.c_uint8(32),  # because uint32
            ctypes.c_uint32(len(ctypes_data)),
            ctypes.cast(prop_data, ctypes.c_void_p),
        )
        return RET_OK_NONE

    def change_window_attributes(
            self, *,
            window_id: nat.XcbWindow,
            value_mask: ctypes.c_uint32,
            value_list: Sequence[ctypes.c_uint32],
    ) -> StdRet[nat.XcbVoidCookie]:
        data_type = ctypes.c_uint32 * (len(value_list) + 1)
        prop_data = data_type(*value_list, 0)
        res = self.__lib.xcb_change_window_attributes(
            self.__conn, window_id, value_mask, ctypes.cast(prop_data, ctypes.c_void_p),
        )
        return StdRet.pass_ok(res)

    def query_tree(self, base_window_id: nat.XcbWindow) -> StdRet[nat.XcbQueryTreeCookie]:
        """Request to get the window's tree of windows."""
        res = self.__lib.xcb_query_tree_unchecked(self.__conn, base_window_id)
        return StdRet.pass_ok(res)

    def reparent_window(
            self, *,
            window_id: nat.XcbWindow,
            new_parent_id: nat.XcbWindow,
            new_x: int, new_y: int,
    ) -> StdRet[None]:
        self.__lib.xcb_reparent_window(
            self.__conn, window_id, new_parent_id,
            ctypes.c_int16(new_x), ctypes.c_int16(new_y),
        )
        return RET_OK_NONE

    def disconnect_xcb_cursor(self) -> StdRet[None]:
        """Shutdown xcb.  Only shutdown hooks should call this."""
        self.__lib.xcb_cursor_context_free(self.__cursor_context)
        return RET_OK_NONE

    def disconnect_xcb(self) -> StdRet[None]:
        """Shutdown xcb connection."""
        # work around an issue with focus on shutdown
        #     xcb_set_input_focus(conn, XCB_INPUT_FOCUS_POINTER_ROOT,
        #             XCB_NONE, timestamp)
        #     xcb_aux_sync(conn)

        # xcb_disconnect(conn)
        self.__lib.xcb_set_input_focus(
            self.__conn, nat.XCB_INPUT_FOCUS_POINTER_ROOT, nat.XCB_NONE, self.__timestamp,
        )
        self.__lib.xcb_aux_sync(self.__conn)
        self.__lib.xcb_disconnect(self.__conn)
        return RET_OK_NONE


class EventCallback:
    """A pluggable callback when events are received.  Allows different systems to
    tie themselves into the event loop."""

    def event_map(self) -> Optional[Sequence[int]]:
        """optional list of event IDs handled by this callback.  If given, then
        the handle will only be called for these event IDs.  If not given, then it
        will be called for all event IDs not already handled by other callbacks with
        an event map containing that ID."""
        raise NotImplemented

    def handle(self) -> StdRet[bool]:
        """Returns True if the event is fully handled, or False if it should be continued
        to look up in other handlers."""
        raise NotImplemented
