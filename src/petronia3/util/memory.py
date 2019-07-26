
"""
Memory-based helpers.

Used to either profile memory or help reduce memory.
"""

from typing import TypeVar, Tuple


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
