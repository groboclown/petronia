"""ctypes utility functions."""

from typing import List, Callable, Generic, Type, Union, Optional, Any
from typing import cast as t_cast
import threading
import ctypes
import warnings
import contextlib
from petronia_common.util import StdRet, PetroniaReturnError, T, UserMessage
from petronia_common.util import i18n as _
from petronia_common.util.error import SimplePetroniaReturnError
from petronia_native.common import user_messages


CtypeInt = Union[
    int,
    ctypes.c_int, ctypes.c_int8, ctypes.c_int16, ctypes.c_int32,
    ctypes.c_uint, ctypes.c_uint8, ctypes.c_uint16, ctypes.c_uint32,
    ctypes.c_byte, ctypes.c_ubyte, ctypes.c_size_t,
]

NULL = ctypes.c_void_p(None)
NULL__c_char_p = ctypes.cast(NULL, ctypes.POINTER(ctypes.c_char))
NULL__uint = ctypes.cast(NULL, ctypes.POINTER(ctypes.c_uint))
NULL__int = ctypes.cast(NULL, ctypes.POINTER(ctypes.c_int))


def as_py_int(val: CtypeInt) -> int:
    """Convert a ctype integer value into a python int."""
    if isinstance(val, int):
        return val
    return val.value


def as_uint8(val: CtypeInt) -> ctypes.c_uint8:
    """convert an int type into a c_uint8"""
    return ctypes.c_uint8(as_py_int(val))


def as_uint16(val: CtypeInt) -> ctypes.c_uint16:
    """convert an int type into a c_uint16"""
    return ctypes.c_uint16(as_py_int(val))


def as_uint32(val: CtypeInt) -> ctypes.c_uint16:
    """convert an in type into a c_uint32"""
    return ctypes.c_uint16(as_py_int(val))


def as_uint(val: CtypeInt) -> ctypes.c_uint:
    """convert an int type into a c_uint"""
    return ctypes.c_uint(as_py_int(val))


def as_uint32_list(*items: ctypes.c_uint32) -> ctypes.c_void_p:
    """Create an array of c_uint32 values"""
    ret_type = ctypes.c_uint32 * len(items)
    ret_val = ret_type(*items)
    return ctypes.cast(ret_val, ctypes.c_void_p)


def as_int32_list(*items: ctypes.c_int32) -> ctypes.c_void_p:
    """Create an array of c_uint32 values"""
    ret_type = ctypes.c_int32 * len(items)
    ret_val = ret_type(*items)
    return ctypes.cast(ret_val, ctypes.c_void_p)


def as_xint32_list(*items: Union[ctypes.c_uint32, ctypes.c_int32]) -> ctypes.c_void_p:
    """Create an array of c_uint32 values"""
    ret_type = ctypes.c_int32 * len(items)
    ret_val = ret_type(*items)
    return ctypes.cast(ret_val, ctypes.c_void_p)


def as_null(src_type: Type[T]) -> T:
    """Create a NULL alias for the given type; must be a pointer."""
    return ctypes.cast(NULL, src_type)


def as_typed_call(
        problems: List[PetroniaReturnError],
        lib: StdRet[ctypes.CDLL], function: str,
        *,
        returns: Type[T],
        **kwargs: Type[Any],
) -> Callable[..., T]:
    """Return the native library method as a typed callable.

    The naming of the arguments adds a bit of self-documenting to the library extraction."""
    if lib.has_error:
        # Don't double report an error
        return _func_not_found
    if hasattr(lib.value, function):
        ret = getattr(lib.value, function)
        ret.restype = returns
        # The kwargs keys() and values() and items() are ordered to match the input.
        ret.argtypes = tuple(kwargs.values())
        return ret
    problems.append(SimplePetroniaReturnError(UserMessage(
        user_messages.TRANSLATION_CATALOG,
        _('Library {lib} has no such function {function}'),
        lib=repr(lib.value),
        function=function,
    )))
    return _func_not_found


def _func_not_found() -> None:
    raise Exception('Function not found in shared library')


def as_library_extern(
        problems: List[PetroniaReturnError],
        lib: StdRet[ctypes.CDLL], extern_name: str,
        extern_ptr_type: Type[T],
) -> T:  # types: ctypes.POINTER(T)
    """Return a pointer to a static variable from the library."""
    if lib.has_error:
        # Don't double report an error
        return t_cast(extern_ptr_type, NULL)
    if lib.ok and hasattr(lib.value, extern_name):
        ret = getattr(lib.value, extern_name)
        return t_cast(extern_ptr_type, ctypes.byref(ret))
    problems.append(SimplePetroniaReturnError(UserMessage(
        user_messages.TRANSLATION_CATALOG,
        _('Library {lib} has no such static extern {name}'),
        lib=repr(lib.value),
        name=extern_name,
    )))
    return t_cast(extern_ptr_type, NULL)


def load_lib(name: str) -> StdRet[ctypes.CDLL]:
    """Load a native library in a safe way."""
    try:
        return StdRet.pass_ok(ctypes.cdll.LoadLibrary(name))
    except OSError as err:
        return StdRet.pass_exception(
            user_messages.TRANSLATION_CATALOG,
            _('Could not load native library {name}; is it installed?'),
            exception=err,
            name=name,
        )


class Closable(Generic[T]):
    """Wrapper object for a value that can be closed"""
    # This can be subclassed, so slots does not work here.
    # __slots__ = ('__value', '__closer', '__origin', '__lock')

    def __init__(
            self,
            value: T,
            closer: Callable[[T], None],
            lock: Optional[Union[threading.Lock, threading.RLock]] = None,
    ) -> None:
        if value is None:
            raise ValueError('cannot use a None value')  # programmer error
        self.__value: Optional[T] = value
        self.__closer: Optional[Callable[[T], None]] = closer
        self.__lock = lock or NOOP_CONTEXT
        try:
            raise Exception(f'Did not close value {value}')
        except Exception as err:
            self.__origin = err
        assert self.__origin is not None  # nosec  # for mypy

    @property
    def optional(self) -> Optional[T]:
        """A possibly None value, if it was already closed."""
        return self.__value

    def is_closed(self) -> bool:
        """Is this value closed?"""
        return self.__value is None

    def is_available(self) -> bool:
        """Is this value not closed?"""
        return self.__value is not None

    def __bool__(self) -> bool:
        return self.__value is not None

    @property
    def value(self) -> T:
        """Get the value.  Raises an error if already closed."""
        with self.__lock:
            if self.__value is None:
                raise ValueError('already closed value')  # programmer error
            return self.__value

    def close(self) -> None:
        """Explicitly close the value.  Not doing so and allowing the value to be garbage
        collected later generates a warning.  Multiple calls to close is okay."""
        with self.__lock:
            if self.__value is not None:
                assert self.__closer is not None  # nosec  # for mypy
                try:
                    self.__closer(self.__value)
                finally:
                    self.__value = None
                    self.__closer = None

    def __del__(self) -> None:
        if self.__value is not None:
            warnings.warn(
                message=self.__origin.args[0],
                stacklevel=2,
                source=self.__origin,
            )
            self.close()


class NoOpContextManager(contextlib.AbstractContextManager):
    """Does nothing."""
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return None


NOOP_CONTEXT = NoOpContextManager()
