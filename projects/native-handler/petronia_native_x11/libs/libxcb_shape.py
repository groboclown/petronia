"""Shared library libxcb-shape"""

from typing import List, Sequence, Callable
import ctypes
from petronia_common.util import PetroniaReturnError, StdRet, T
from . import ct_util
from .libxcb import xcb


class LibXcbShape:
    """Shared library libxcb-shape"""
    __slots__ = (
        '__problems',
        'xcb_shape_id',
    )

    def __init__(self) -> None:
        self.__problems: List[PetroniaReturnError] = []
        xcb_shape_res = ct_util.load_lib('libxcb-shape.so.0')
        self._setup_res(xcb_shape_res)

        self.xcb_shape_id = ct_util.as_library_extern(
            self.__problems, xcb_shape_res, 'xcb_shape_id',
            xcb_native.XcbExtensionP,
        )

    @property
    def problems(self) -> Sequence[PetroniaReturnError]:
        return tuple(self.__problems)

    def _setup_res(self, res: StdRet[T]) -> None:
        if res.has_error:
            self.__problems.append(res.valid_error)


def load_libxcb_shape() -> StdRet[LibXcbShape]:
    """Load the library."""
    ret = LibXcbShape()
    if ret.problems:
        return StdRet.pass_error(*ret.problems)
    return StdRet.pass_ok(ret)
