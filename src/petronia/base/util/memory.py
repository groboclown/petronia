
"""
Memory-based helpers.

Used to either profile memory or help reduce memory.
"""

from typing import TypeVar, Tuple, Generic, Optional, Dict, Mapping, Any


# singleton empty collections.  DO NOT MODIFY THEM.
# Note that the typing is ignored, so that they can take the place of anything.
EMPTY_DICT = dict()  # type: ignore
EMPTY_LIST = list()  # type: ignore
EMPTY_TUPLE = tuple()  # type: ignore

EMPTY_MAPPING: Mapping[Any, Any] = EMPTY_DICT  # type: ignore
STRING_EMPTY_TUPLE: Tuple[str] = EMPTY_TUPLE  # type: ignore

# For generics
T = TypeVar('T') # pylint: disable=invalid-name
K = TypeVar('K') # pylint: disable=invalid-name
V = TypeVar('V') # pylint: disable=invalid-name


class ValueHolder(Generic[T]):
    """Holds a piece of data tha can be delayed in its setup until later.
    Used for passing to a child object that can assign the value at some
    later time."""
    __slots__ = ('value',)

    def __init__(self, val: T) -> None:
        self.value = val


class DelayedValueHolder(Generic[T]):
    """Holds a piece of data tha can be delayed in its setup until later.
    Used for passing to a child object that can assign the value at some
    later time."""
    __slots__ = ('value',)

    def __init__(self, val: Optional[T] = None) -> None:
        self.value = val


def readonly_dict(inp: Mapping[K, V]) -> Mapping[K, V]:
    """Create a (shallow) read-only copy of the dictionary."""
    if isinstance(inp, _ReadOnlyDict):
        return inp
    return _ReadOnlyDict(inp) # type: ignore


class _ReadOnlyDict(Dict[K, V], Generic[K, V]):
    """A read-only dictionary."""
    def __readonly__(self, *args, **kwargs): # type: ignore
        raise RuntimeError("Cannot modify ReadOnlyDict")

    __setitem__ = __readonly__ # type: ignore
    __delitem__ = __readonly__ # type: ignore
    pop = __readonly__ # type: ignore
    popitem = __readonly__ # type: ignore
    clear = __readonly__ # type: ignore
    update = __readonly__ # type: ignore
    setdefault = __readonly__ # type: ignore
    del __readonly__
