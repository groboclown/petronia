"""Shared library libxcb-xinerama"""

from typing import List, Sequence, Callable
import ctypes
from petronia_common.util import PetroniaReturnError, StdRet, T
from . import ct_util
from .xcb_library import xcb_types


class LibXcbXinerama:
    """Shared library libxcb-xinerama"""
    __slots__ = (
        '__problems',
        'xcb_xinerama_id',
    )

    def __init__(self) -> None:
        self.__problems: List[PetroniaReturnError] = []
        xcb_xinerama_res = ct_util.load_lib('libxcb-xinerama.so.0')
        self._setup_res(xcb_xinerama_res)

        self.xcb_xinerama_id = ct_util.as_library_extern(
            self.__problems, xcb_xinerama_res, 'xcb_xinerama_id',
            xcb_types.XcbExtensionP,
        )

    @property
    def problems(self) -> Sequence[PetroniaReturnError]:
        return tuple(self.__problems)

    def _setup_res(self, res: StdRet[T]) -> None:
        if res.has_error:
            self.__problems.append(res.valid_error)


def load_libxcb_xinerama() -> StdRet[LibXcbXinerama]:
    """Load the library."""
    ret = LibXcbXinerama()
    if ret.problems:
        return StdRet.pass_error(*ret.problems)
    return StdRet.pass_ok(ret)
