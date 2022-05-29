"""Shared library xcb-cursor"""

from typing import List, Sequence, Callable
import ctypes
from petronia_common.util import PetroniaReturnError, StdRet, T
from . import ct_util
from . import libxcb_cursor_types
from .xcb_library import xcb_types


class LibXcbCursor:
    """Shared library xcb-cursor"""
    __slots__ = (
        '__problems',
        'xcb_cursor_context_new',
        'xcb_cursor_context_free',
    )

    def __init__(self) -> None:
        self.__problems: List[PetroniaReturnError] = []
        xcb_cursor_res = ct_util.load_lib('libxcb-cursor.so.0')
        self._setup_res(xcb_cursor_res)

        self.xcb_cursor_context_new: Callable[
            [
                xcb_types.XcbConnectionP, xcb_types.XcbScreenP,
                libxcb_cursor_types.XcbCursorContextPP,
            ], ctypes.c_int,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_cursor_res, 'xcb_cursor_context_new',
            returns=ctypes.c_int,
            connection=xcb_types.XcbConnectionP,
            screen=xcb_types.XcbScreenP,
            ctx=libxcb_cursor_types.XcbCursorContextPP,
        )

        self.xcb_cursor_context_free: Callable[
            [libxcb_cursor_types.XcbCursorContextP], None,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_cursor_res, 'xcb_cursor_context_free',
            returns=None,
            ctx=libxcb_cursor_types.XcbCursorContextPP,
        )

    @property
    def problems(self) -> Sequence[PetroniaReturnError]:
        return tuple(self.__problems)

    def _setup_res(self, res: StdRet[T]) -> None:
        if res.has_error:
            self.__problems.append(res.valid_error)


def load_libxcb_cursor() -> StdRet[LibXcbCursor]:
    """Load the library."""
    ret = LibXcbCursor()
    if ret.problems:
        return StdRet.pass_error(*ret.problems)
    return StdRet.pass_ok(ret)
