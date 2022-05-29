"""Shared library cairo"""

from typing import List, Sequence, Callable
import ctypes
from petronia_common.util import PetroniaReturnError, StdRet, T
from . import ct_util
from . import libcairo_types
from .xcb_library import xcb_types


class LibCairo:
    """Shared library cairo"""
    __slots__ = (
        '__problems',
        'cairo_xcb_surface_create', 'cairo_surface_status',
        'cairo_status_to_string', 'cairo_surface_finish',
        'cairo_surface_destroy',
    )

    def __init__(self) -> None:
        self.__problems: List[PetroniaReturnError] = []
        cairo_res = ct_util.load_lib('libcairo.so.2')
        self._setup_res(cairo_res)

        self.cairo_xcb_surface_create: Callable[
            [
                xcb_types.XcbConnectionP, xcb_types.XcbDrawable,
                xcb_types.XcbVisualtypeP, ctypes.c_int, ctypes.c_int,
            ],
            libcairo_types.CairoSurfaceP,
        ] = ct_util.as_typed_call(
            self.__problems, cairo_res, 'cairo_xcb_surface_create',
            returns=libcairo_types.CairoSurfaceP,
            connection=xcb_types.XcbConnectionP,
            drawable=xcb_types.XcbDrawable,
            visual=xcb_types.XcbVisualtypeP,
            width=ctypes.c_int,
            height=ctypes.c_int,
        )

        self.cairo_surface_status: Callable[
            [libcairo_types.CairoSurfaceP], libcairo_types.CairoStatus,
        ] = ct_util.as_typed_call(
            self.__problems, cairo_res, 'cairo_surface_status',
            returns=libcairo_types.CairoStatus,
            surface=libcairo_types.CairoSurfaceP,
        )

        self.cairo_status_to_string: Callable[
            [libcairo_types.CairoStatus], ctypes.c_char_p,
        ] = ct_util.as_typed_call(
            self.__problems, cairo_res, 'cairo_status_to_string',
            returns=ctypes.c_char_p,
            status=libcairo_types.CairoStatus,
        )

        self.cairo_surface_finish: Callable[
            [libcairo_types.CairoSurfaceP], None
        ] = ct_util.as_typed_call(
            self.__problems, cairo_res, 'cairo_surface_finish',
            returns=None,
            surface=libcairo_types.CairoSurfaceP,
        )

        self.cairo_surface_destroy: Callable[
            [libcairo_types.CairoSurfaceP], None
        ] = ct_util.as_typed_call(
            self.__problems, cairo_res, 'cairo_surface_destroy',
            returns=None,
            surface=libcairo_types.CairoSurfaceP,
        )

    @property
    def problems(self) -> Sequence[PetroniaReturnError]:
        return tuple(self.__problems)

    def _setup_res(self, res: StdRet[T]) -> None:
        if res.has_error:
            self.__problems.append(res.valid_error)


def load_libcairo() -> StdRet[LibCairo]:
    """Load the library."""
    ret = LibCairo()
    if ret.problems:
        return StdRet.pass_error(*ret.problems)
    return StdRet.pass_ok(ret)
