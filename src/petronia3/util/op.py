"""
Basic operations
"""

from typing import Dict, Optional
from .memory import K, V

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
