
"""
Type Support functions.
"""

from typing import Optional, Iterable, List
from .memory import T_co


def without_none(vals: Iterable[Optional[T_co]]) -> List[T_co]:
    """Return the values as non-None."""
    ret: List[T_co] = []
    for val in vals:
        if val is not None:
            ret.append(val)
    return ret
