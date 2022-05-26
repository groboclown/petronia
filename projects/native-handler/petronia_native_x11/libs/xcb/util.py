"""ctypes utility functions."""
from types import TracebackType
from typing import Callable, Generic, Type, Union, Optional
import ctypes
import contextlib
from petronia_common.util import T

CtypeInt = Union[
    int,
    ctypes.c_int, ctypes.c_int8, ctypes.c_int16, ctypes.c_int32,
    ctypes.c_uint, ctypes.c_uint8, ctypes.c_uint16, ctypes.c_uint32,
    ctypes.c_byte, ctypes.c_ubyte,
]


def as_int(val: CtypeInt) -> int:
    """Convert a ctype integer value into a python int."""
    if isinstance(val, int):
        return val
    return val.value


def as_uint8(val: CtypeInt) -> ctypes.c_uint8:
    """convert a c_int into a c_uint8"""
    return ctypes.c_uint8(as_int(val))


def as_uint16(val: CtypeInt) -> ctypes.c_uint16:
    """convert a c_int into a c_uint8"""
    return ctypes.c_uint16(as_int(val))


class EnterExit(Generic[T]):
    __slots__ = ('__value', '__on_exit')

    def __init__(self, value: T, on_exit: Callable[[T], Optional[bool]]) -> None:
        self.__value: Optional[T] = value
        self.__on_exit = on_exit

    def __enter__(self) -> T:
        """Return `self` upon entering the runtime context."""
        if self.__value is None:
            raise ValueError('already exited')
        return self.__value

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        """Raise any exception triggered within the runtime context."""
        if self.__value is not None:
            try:
                return self.__on_exit(self.__value)
            finally:
                self.__value = None
        return None
