"""Shared library libxcb-randr"""

from typing import List, Sequence, Callable
import ctypes
from petronia_common.util import PetroniaReturnError, StdRet, T
from . import ct_util
from .libxcb import xcb


class LibXcbRandr:
    __slots__ = (
        '__problems',
        'xcb_randr_id',
    )

    def __init__(self) -> None:
        self.__problems: List[PetroniaReturnError] = []
        xcb_randr_res = ct_util.load_lib('libxcb-randr.so.0')
        self._setup_res(xcb_randr_res)

        self.xcb_randr_id = ct_util.as_library_extern(
            self.__problems, xcb_randr_res, 'xcb_randr_id',
            xcb_native.XcbExtensionP,
        )

    @property
    def problems(self) -> Sequence[PetroniaReturnError]:
        return tuple(self.__problems)

    def _setup_res(self, res: StdRet[T]) -> None:
        if res.has_error:
            self.__problems.append(res.valid_error)


def load_libxcb_util() -> StdRet[LibXcbUtil]:
    """Load the library."""
    ret = LibXcbUtil()
    if ret.problems:
        return StdRet.pass_error(*ret.problems)
    return StdRet.pass_ok(ret)
