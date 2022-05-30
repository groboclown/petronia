"""Global data store.  Data is assembled based on steps."""

from typing import Sequence, Callable, Optional
import threading
import ctypes
from petronia_common.util import StdRet, collect_errors_from, UserMessage, T, RET_OK_NONE
from petronia_ext_lib.runner import LookupEventRegistryContext
from .configuration import ConfigurationStore
from .libs import (
    libxcb, libcairo, libc, libxcb_cursor, libxcb_icccm, libxcb_randr, libxcb_shape,
    libxcb_util, libxcb_xfixes, libxcb_xinerama, libxcb_xtest, libxcb_types, xcb_atoms,
    libxcb_consts,
)


class Libraries:
    """Boot-time common data."""
    __slots__ = (
        '__xcb', '__cairo', '__clib',
        '__xcb_cursor', '__xcb_icccm', '__xcb_randr', '__xcb_shape',
        '__xcb_util', '__xcb_xfixes', '__xcb_xinerama', '__xcb_xtest',
        '__context', '__config',
    )

    def __init__(
            self, *,
            context: LookupEventRegistryContext,
            config: ConfigurationStore,

            # Required libraries
            xcb: libxcb.LibXcb,
            cairo: libcairo.LibCairo,
            clib: libc.LibC,

            # Optional libraries
            xcb_cursor: Optional[libxcb_cursor.LibXcbCursor],
            xcb_icccm: Optional[libxcb_icccm.LibXcbIcccm],
            xcb_randr: Optional[libxcb_randr.LibXcbRandr],
            xcb_shape: Optional[libxcb_shape.LibXcbShape],
            xcb_util: Optional[libxcb_util.LibXcbUtil],
            xcb_xfixes: Optional[libxcb_xfixes.LibXcbXFixes],
            xcb_xinerama: Optional[libxcb_xinerama.LibXcbXinerama],
            xcb_xtest: Optional[libxcb_xtest.LibXcbXTest],
    ) -> None:
        self.__context = context
        self.__config = config
        self.__xcb = xcb
        self.__cairo = cairo
        self.__clib = clib
        self.__xcb_cursor = xcb_cursor
        self.__xcb_icccm = xcb_icccm
        self.__xcb_randr = xcb_randr
        self.__xcb_shape = xcb_shape
        self.__xcb_util = xcb_util
        self.__xcb_xfixes = xcb_xfixes
        self.__xcb_xinerama = xcb_xinerama
        self.__xcb_xtest = xcb_xtest

    @property
    def context(self) -> LookupEventRegistryContext:
        return self.__context

    @property
    def config(self) -> ConfigurationStore:
        return self.__config

    @property
    def xcb(self) -> libxcb.LibXcb:
        """libxcb library"""
        return self.__xcb

    @property
    def cairo(self) -> libcairo.LibCairo:
        return self.__cairo

    @property
    def clib(self) -> libc.LibC:
        return self.__clib

    def has_xcb_util(self) -> bool:
        """libxcb-util library"""
        return self.__xcb_util is not None

    @property
    def xcb_util(self) -> libxcb_util.LibXcbUtil:
        """libxcb-util library"""
        assert self.__xcb_util is not None  # nosec  # should have called has_ first.
        return self.__xcb_util

    def has_xcb_icccm(self) -> bool:
        return self.__xcb_icccm is not None

    @property
    def xcb_icccm(self) -> libxcb_icccm.LibXcbIcccm:
        assert self.__xcb_icccm is not None  # nosec  # should have called has_ first.
        return self.__xcb_icccm

    @staticmethod
    def create(
            *,
            context: LookupEventRegistryContext,
            config: ConfigurationStore,
            warning_report: Optional[Callable[[UserMessage], None]] = None,
    ) -> StdRet['Libraries']:
        """Create a new boot-time common data."""
        # These libraries absolutely have to exist.
        xcb_res = libxcb.load_libxcb()
        cairo_res = libcairo.load_libcairo()
        clib_res = libc.load_libc()
        err = collect_errors_from(xcb_res, cairo_res, clib_res)
        if err:
            return StdRet.pass_error(err)

        # Optional stuff
        def opt(res: StdRet[T]) -> Optional[T]:
            if res.has_error:
                for message in res.valid_error.messages():
                    warning_report(message)
                return None
            return res.result

        return StdRet.pass_ok(Libraries(
            context=context,
            config=config,
            xcb=xcb_res.result,
            cairo=cairo_res.result,
            clib=clib_res.result,
            xcb_cursor=opt(libxcb_cursor.load_libxcb_cursor()),
            xcb_icccm=opt(libxcb_icccm.load_libxcb_icccm()),
            xcb_randr=opt(libxcb_randr.load_libxcb_util()),
            xcb_shape=opt(libxcb_shape.load_libxcb_shape()),
            xcb_util=opt(libxcb_util.load_libxcb_util()),
            xcb_xfixes=opt(libxcb_xfixes.load_libxcb_xfixes()),
            xcb_xinerama=opt(libxcb_xinerama.load_libxcb_xinerama()),
            xcb_xtest=opt(libxcb_xtest.load_libxcb_util()),
        ))


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


class CommonData:
    """Common data used throughout all the parts after setup is complete."""
    __slots__ = (
        '__wm',
    )

    def __init__(
            self,
            wm_data: WindowManagerData,
    ) -> None:
        self.__wm = wm_data

    @property
    def context(self) -> LookupEventRegistryContext:
        return self.__wm.libs.context

    @property
    def config(self) -> ConfigurationStore:
        return self.__wm.libs.config

    @property
    def xcb(self) -> libxcb.LibXcb:
        """libxcb library"""
        return self.__wm.libs.xcb

    @property
    def cairo(self) -> libcairo.LibCairo:
        return self.__wm.libs.cairo

    @property
    def clib(self) -> libc.LibC:
        return self.__wm.libs.clib

    def has_xcb_util(self) -> bool:
        """libxcb-util library"""
        return self.__wm.libs.has_xcb_util()

    @property
    def xcb_util(self) -> libxcb_util.LibXcbUtil:
        """libxcb-util library"""
        return self.__wm.libs.xcb_util

    def has_xcb_icccm(self) -> bool:
        return self.__wm.libs.has_xcb_icccm()

    @property
    def xcb_icccm(self) -> libxcb_icccm.LibXcbIcccm:
        return self.__wm.libs.xcb_icccm

    def freeable(
            self,
            value,  # types: ctypes.pointer[T]
            lock: Optional[threading.Lock] = None,
    ) -> libc.Pointer[T]:
        """Make the value free-able"""
        return self.__wm.libs.clib.freeable(value, lock)

    @property
    def connection(self) -> libxcb_types.XcbConnectionP:
        return self.__wm.connection
