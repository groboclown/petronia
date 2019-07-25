"""
Basic operations.  These are fundamental actions in Python that make the code
much cleaner.
"""

import collections
from typing import Dict, Sequence, Type, Optional
from .memory import K, V, T

def in_or(con: Dict[K, V], key: K, default_value: V) -> V:
    """If the key is in the collection, return the value, otherwise return the
    default_value."""
    if key in con:
        return con[key]
    return default_value

def optional_key(con: Dict[K, V], key: K) -> Optional[V]:
    """If the key is in the collection, return the value, otherwise return
    None."""
    if key in con:
        return con[key]
    return None

def optional_list_key(con: Dict[K, V], key: K, oftype: Optional[Type[T]] = None) -> Optional[Sequence[T]]:
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
        if oftype:
            for one in val:
                if not isinstance(one, oftype):
                    return None
        return tuple(val)
    return None

def optional_typed_key(con: Dict[K, V], key: K, oftype: Type[T]) -> Optional[T]:
    """If the key is in the colleciton, and of the given type, then return the
    value, otherwise None."""
    if key not in con:
        return None
    val = con[key]
    if isinstance(val, oftype):
        return val
    return None
