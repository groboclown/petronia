"""
Basic operations.  These are fundamental actions in Python that make the code
much cleaner.
"""

import collections
from typing import Dict, Sequence, Tuple, Union, Optional
from .memory import K, V, T

def in_or(con: Dict[K, V], key: K, default_value: V) -> V:
    """If the key is in the collection, return the value, otherwise return the
    default_value."""
    if key in con:
        return con[key]
    return default_value


def optional_key(
        con: Dict[K, V], key: K,
        oftype: Optional[Union[type, Tuple[Union[type, Tuple[V, ...]], ...]]] = None
) -> Optional[V]:
    """If the key is in the collection, return the value, otherwise return
    None.  If `oftype` is non-None, then the value will only be returned if it
    is of the expected type."""
    if key in con:
        val = con[key]
        if not oftype or isinstance(val, oftype):
            return val
    return None


def optional_list_key(
        con: Dict[K, V], key: K,
        oftype: Optional[Union[type, Tuple[Union[type, Tuple[T, ...]], ...]]] = None
) -> Optional[Sequence[T]]:
    """If the key is in the collection, and the value is an iterable like
    structure, then the sequence value is returned, otherwise None.
    Strings not wrapped in a list are not returned."""
    if key not in con:
        return None
    val = con[key]
    if isinstance(val, collections.Sequence):
        if oftype:
            for one in val:
                if not isinstance(one, oftype):
                    return None
        return val
    if not isinstance(val, str) and hasattr(type(val), '__iter__'):
        # val is iterable.
        if oftype:
            for one in val: # type: ignore
                if not isinstance(one, oftype):
                    return None
        return tuple(val) # type: ignore
    return None
