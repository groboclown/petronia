"""Global data store.  Data is assembled based on steps."""

from typing import Sequence, Optional
import ctypes
from petronia_common.util import StdRet, RET_OK_NONE
from .libraries import Libraries
from ..libs import (
    libxcb_types, xcb_atoms, libxcb_consts,
)


PROPERTY_MODE__REPLACE = libxcb_consts.XCB_PROP_MODE_REPLACE
PROPERTY_MODE__PREPEND = libxcb_consts.XCB_PROP_MODE_PREPEND
PROPERTY_MODE__APPEND = libxcb_consts.XCB_PROP_MODE_APPEND
PropertyModeEnum = (PROPERTY_MODE__REPLACE, PROPERTY_MODE__PREPEND, PROPERTY_MODE__APPEND)


class WindowManagerData:
    """Data collected after the connection is the window manager."""
    __slots__ = (
        '__libs',
        '__conn', '__screen', '__default_visual', '__visual',
        '__default_depth', '__default_colormap', '__atoms',
        '__timestamp', '__default_screen',
        '__default_depth_raw', '__selection_atom', '__selection_owner_window',
    )

    def __init__(
            self, *,
            libs: Libraries,
            conn: libxcb_types.XcbConnectionP,
            default_screen: ctypes.c_int,
            screen: libxcb_types.XcbScreenP,
            default_visual: libxcb_types.XcbVisualtypeP,
            visual: libxcb_types.XcbVisualtypeP,
            default_depth_raw: ctypes.c_uint8,
            default_depth: int,
            default_colormap: int,
            timestamp: libxcb_types.XcbTimestamp,
            atoms: xcb_atoms.AtomDef,
            selection_atom: Optional[libxcb_types.XcbAtom],
            selection_owner_window: Optional[libxcb_types.XcbWindow],
    ) -> None:
        self.__libs = libs
        self.__conn = conn
        self.__default_screen = default_screen
        self.__screen = screen
        self.__default_visual = default_visual
        self.__visual = visual
        self.__default_depth_raw = default_depth_raw
        self.__default_depth = default_depth
        self.__default_colormap = default_colormap
        self.__timestamp = timestamp
        self.__atoms = atoms
        self.__selection_atom: Optional[libxcb_types.XcbAtom] = selection_atom
        self.__selection_owner_window: Optional[libxcb_types.XcbWindow] = selection_owner_window

    @property
    def libs(self) -> Libraries:
        return self.__libs

    @property
    def connection(self) -> libxcb_types.XcbConnectionP:
        return self.__conn

    @property
    def screen_root(self) -> libxcb_types.XcbWindow:
        return self.__screen.contents.root

    def change_window_property_uint32(
            self, *,
            mode: ctypes.c_uint8,
            window_id: Optional[libxcb_types.XcbWindow],
            property_atom: libxcb_types.XcbAtom,
            property_type: libxcb_types.XcbAtom,
            ctypes_data: Sequence[ctypes.c_uint32],
    ) -> StdRet[None]:
        """Set the window property to a list of 32 bit values."""
        assert mode in PropertyModeEnum  # nosec  # programmer check.
        data_type = ctypes.c_uint32 * len(ctypes_data)
        prop_data = data_type(ctypes_data)
        self.__libs.xcb.xcb_change_property(
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
            window_id: libxcb_types.XcbWindow,
            value_mask: ctypes.c_uint32,
            value_list: Sequence[ctypes.c_uint32],
    ) -> StdRet[libxcb_types.XcbVoidCookie]:
        data_type = ctypes.c_uint32 * (len(value_list) + 1)
        prop_data = data_type(*value_list, 0)
        res = self.__libs.xcb.xcb_change_window_attributes(
            self.__conn, window_id, value_mask, ctypes.cast(prop_data, ctypes.c_void_p),
        )
        return StdRet.pass_ok(res)
