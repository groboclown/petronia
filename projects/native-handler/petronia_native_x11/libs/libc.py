"""Standard C library."""

from typing import Sequence, List, Callable, Generic, Union, Optional, Any
import ctypes
import threading
import warnings
from petronia_common.util import PetroniaReturnError, StdRet, T, V
from . import ct_util


class Pointer(ct_util.Closable[V], Generic[V]):
    @property
    def contents(self) -> Optional[V]:
        if self.value:
            return self.value
        return None


class RealPointer(Pointer):   # types: RealPointer(Pointer[ctypes.pointer[V]], Generic[V])
    @property
    def contents(self) -> Optional[V]:
        """Like .contents..."""
        if self.value:
            return self.value.contents
        return None


class LibC:
    """Standard C library"""
    __slots__ = (
        '__problems',
        '_free',
        'strlen',
        '_memset',
    )

    def __init__(self) -> None:
        self.__problems: List[PetroniaReturnError] = []
        c_res = ct_util.load_lib('libxcb-util.so.1')
        self._setup_res(c_res)

        self._free: Callable[
            [ctypes.POINTER], None,
        ] = ct_util.as_typed_call(
            self.__problems, c_res, 'free',
            returns=None,
            ptr=ctypes.c_void_p,
        )

        self.strlen: Callable[
            [ctypes.c_char_p], ctypes.c_size_t,
        ] = ct_util.as_typed_call(
            self.__problems, c_res, 'strlen',
            returns=ctypes.c_size_t,
            string=ctypes.c_char_p,
        )

        # pointer, value, size
        self._memset: Callable[
            [ctypes.POINTER, ctypes.c_uint8, ctypes.c_uint], None,
        ] = ct_util.as_typed_call(
            self.__problems, c_res, 'memset',
            returns=None,
            pointer=ctypes.c_void_p,
            byte_value=ctypes.c_uint8,
            size=ctypes.c_size_t,
        )

    @property
    def problems(self) -> Sequence[PetroniaReturnError]:
        return tuple(self.__problems)

    def _setup_res(self, res: StdRet[T]) -> None:
        if res.has_error:
            self.__problems.append(res.valid_error)

    def force_free(self, ptr: Any) -> None:
        """Force the memory to be freed.  Use carefully."""
        self._free(ctypes.cast(ptr, ctypes.c_void_p))

    def freeable(
            self,
            ptr,  # types: ctypes.pointer[T]
            lock: Optional[Union[threading.Lock, threading.RLock]] = None,
    ) -> Pointer[T]:
        """Wrap the pointer in a closable type, to ensure its memory gets freed."""
        if not ptr:
            raise ValueError('pointers must be tested for non-null outside this call.')
        if isinstance(ptr, ctypes.c_void_p):
            return Pointer(ptr, self._free, lock)
        if (
                # built-in pointer types
                isinstance(ptr, (ctypes.c_char_p, ctypes.c_wchar_p))

                # constructed pointer
                or (isinstance(ptr, object) and ptr.__class__.__name__.startswith('LP_'))
        ):
            return RealPointer(ptr, self.force_free, lock)
        elif isinstance(ptr, (bytes, str, bytearray, ctypes.Array)):
            warnings.warn(
                f"Incorrectly assumed {type(ptr)} is a freeable pointer",
                stacklevel=2,
            )
            return Pointer(ptr, lambda x: None, lock)
        raise ValueError(f'Not a pointer: {ptr} ({type(ptr)})')  # programmer error


def load_libc() -> StdRet[LibC]:
    """Load the library."""
    ret = LibC()
    if ret.problems:
        return StdRet.pass_error(*ret.problems)
    return StdRet.pass_ok(ret)
