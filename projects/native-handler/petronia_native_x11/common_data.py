"""Global data store.  Data is assembled based on steps."""

from typing import Callable, Optional
from petronia_common.util import StdRet, collect_errors_from, UserMessage, T
from .libs import (
    libxcb, libcairo, libc, libxcb_cursor, libxcb_icccm, libxcb_randr, libxcb_shape,
    libxcb_util, libxcb_xfixes, libxcb_xinerama, libxcb_xtest,
)


class Libraries:
    """Boot-time common data."""
    __slots__ = (
        '__xcb', '__cairo', '__clib',
        '__xcb_cursor', '__xcb_icccm', '__xcb_randr', '__xcb_shape',
        '__xcb_util', '__xcb_xfixes', '__xcb_xinerama', '__xcb_xtest',
    )

    def __init__(
            self, *,

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
    def xcb(self) -> libxcb.LibXcb:
        """libxcb library"""
        return self.__xcb

    @property
    def cairo(self) -> libcairo.LibCairo:
        return self.__cairo

    @property
    def clib(self) -> libc.LibC:
        return self.__clib

    @staticmethod
    def create(
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


class WindowManagerData:
    """Data collected after the connection is the window manager."""
    __slots__ = (
        '__libs',
        '__conn', '__screen', '__default_visual', '__visual',
        '__default_depth', '__default_colormap', '__atoms',
        '__cursor_context', '__timestamp', '__default_screen',
        '__default_depth_raw', '__selection_atom', '__selection_owner_window',
        '__no_focus_window', '__graphics_context',
    )


class CommonData:
    """Common data used throughout all the parts after setup is complete."""
