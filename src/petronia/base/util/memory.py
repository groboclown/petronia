
"""
Memory-based helpers.

Used to either profile memory or help reduce memory.
"""

from typing import TypeVar, Tuple, Generic, Optional


# singleton empty collections.  DO NOT MODIFY THEM.
# Note that the typing is ignored, so that they can take the place of anything.
EMPTY_DICT = dict() # type: ignore
EMPTY_LIST = list() # type: ignore
EMPTY_TUPLE = tuple() # type: ignore

STRING_EMPTY_TUPLE: Tuple[str] = EMPTY_TUPLE # type: ignore

# For generics
T = TypeVar('T') # pylint: disable=invalid-name
K = TypeVar('K') # pylint: disable=invalid-name
V = TypeVar('V') # pylint: disable=invalid-name

class ValueHolder(Generic[T]):
    """Holds a piece of data tha can be delayed in its setup until later.
    Used for passing to a child object that can assign the value at some
    later time."""
    __slots__ = ('value',)

    def __init__(self, val: Optional[T]) -> None:
        self.value = val
