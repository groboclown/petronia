"""Shared library xcb_util"""

from typing import List, Sequence, Callable
import ctypes
from petronia_common.util import PetroniaReturnError, StdRet, T
from . import ct_util
from .libxcb import xcb as nat


class LibXcbUtil:
    """Shared library xcb_util"""
    __slots__ = (
        '__problems',
        'xcb_aux_get_screen',
        'xcb_atom_name_by_screen',
        'xcb_aux_sync',
    )

    def __init__(self) -> None:
        self.__problems: List[PetroniaReturnError] = []
        xcb_util_res = ct_util.load_lib('libxcb-util.so.1')
        self._setup_res(xcb_util_res)

        self.xcb_aux_get_screen: Callable[
            [nat.XcbConnectionP, ctypes.c_int], nat.XcbScreenP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_util_res, 'xcb_aux_get_screen',
            returns=nat.XcbScreenP,
            connection=nat.XcbConnectionP,
            screen_number=ctypes.c_int,
        )

        self.xcb_atom_name_by_screen: Callable[
            [ctypes.c_char_p, ctypes.c_uint8], ctypes.c_char_p,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_util_res, 'xcb_atom_name_by_screen',
            returns=ctypes.c_char_p,
            base=ctypes.c_char_p,
            screen=ctypes.c_uint8,
        )

        self.xcb_aux_sync: Callable[
            [nat.XcbConnectionP], None
        ] = ct_util.as_typed_call(
            self.__problems, xcb_util_res, 'xcb_aux_sync',
            returns=None,
            connection=nat.XcbConnectionP,
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
