"""Shared library libxcb-icccm"""

from typing import List, Sequence, Callable
import ctypes
from petronia_common.util import PetroniaReturnError, StdRet, T
from . import ct_util
from .xcb_library import xcb_types


class LibXcbIcccm:
    __slots__ = (
        '__problems',
        'xcb_icccm_set_wm_class',
        'xcb_icccm_set_wm_name',
    )

    def __init__(self) -> None:
        self.__problems: List[PetroniaReturnError] = []
        xcb_icccm_res = ct_util.load_lib('libxcb-icccm.so.4')
        self._setup_res(xcb_icccm_res)

        self.xcb_icccm_set_wm_class: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbWindow, ctypes.c_uint32, ctypes.c_char_p],
            xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_icccm_res, 'xcb_icccm_set_wm_class',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
            window=xcb_types.XcbWindow,
            class_name_length=ctypes.c_uint32,
            class_name=ctypes.c_char_p,
        )

        self.xcb_icccm_set_wm_name: Callable[
            [
                xcb_types.XcbConnectionP, xcb_types.XcbWindow, xcb_types.XcbAtom,
                ctypes.c_uint8, ctypes.c_uint32, ctypes.c_char_p,
            ],
            xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_icccm_res, 'xcb_icccm_set_wm_name',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
            window=xcb_types.XcbWindow,
            encoding=xcb_types.XcbAtom,
            format=ctypes.c_uint8,
            name_length=ctypes.c_uint32,
            name=ctypes.c_char_p,
        )

    @property
    def problems(self) -> Sequence[PetroniaReturnError]:
        return tuple(self.__problems)

    def _setup_res(self, res: StdRet[T]) -> None:
        if res.has_error:
            self.__problems.append(res.valid_error)


def load_libxcb_icccm() -> StdRet[LibXcbIcccm]:
    """Load the library."""
    ret = LibXcbIcccm()
    if ret.problems:
        return StdRet.pass_error(*ret.problems)
    return StdRet.pass_ok(ret)
