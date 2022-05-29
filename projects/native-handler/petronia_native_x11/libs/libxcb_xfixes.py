"""Shared library libxcb-xfixes"""

from typing import List, Sequence, Callable
import ctypes
from petronia_common.util import PetroniaReturnError, StdRet, T
from . import ct_util
from .libxcb import xcb


class LibXcbXFixes:
    """Shared library libxcb-xfixes"""
    __slots__ = (
        '__problems',
        'xcb_xfixes_id',
    )

    def __init__(self) -> None:
        self.__problems: List[PetroniaReturnError] = []
        xcb_xfixes_res = ct_util.load_lib('libxcb-xfixes.so.0')
        self._setup_res(xcb_xfixes_res)

        self.xcb_xfixes_id = ct_util.as_library_extern(
            self.__problems, xcb_xfixes_res, 'xcb_xfixes_id',
            xcb_native.XcbExtensionP,
        )

    @property
    def problems(self) -> Sequence[PetroniaReturnError]:
        return tuple(self.__problems)

    def _setup_res(self, res: StdRet[T]) -> None:
        if res.has_error:
            self.__problems.append(res.valid_error)


def load_libxcb_xfixes() -> StdRet[LibXcbXFixes]:
    """Load the library."""
    ret = LibXcbXFixes()
    if ret.problems:
        return StdRet.pass_error(*ret.problems)
    return StdRet.pass_ok(ret)
