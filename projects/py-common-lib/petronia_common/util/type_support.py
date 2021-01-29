
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


def not_none(val: Optional[T_co]) -> T_co:
    """Return the value as non-none.  Should only be used when the interweaving of
    the code logic of the shows that the value cannot be none, but MyPy analysis
    indicates that, at some future point, changes to the code could invalidate this
    assumption."""
    if val is None:
        raise ValueError('value assumed not None but is None')
    return val
