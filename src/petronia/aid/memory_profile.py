
# mypy: allow-any-expr
# mypy: allow-any-explicit
# mypy: allow-any-generics

"""
Memory profiling helpers.

TODO use pympler instead (https://github.com/pympler/pympler)
"""

from typing import List, Set, Any
from types import FunctionType, MethodType
from collections.abc import Mapping, Iterable
from sys import getsizeof as shallow_getsizeof


def deep_getsizeof(obj: Any) -> int:
    """
    Deeply inspects any Python object for its data usage.

    :param o:
    :return:
    """

    stack: List[Any] = [obj]
    seen: Set[int] = set()
    total = 0

    while stack:
        n_obj = stack.pop()
        if id(n_obj) in seen:
            continue
        seen.add(id(n_obj))
        if isinstance(n_obj, (str, int, float, bool, bytes,)):
            total += shallow_getsizeof(n_obj)
        elif isinstance(n_obj, Mapping):
            for key, val in n_obj.items():
                stack.append(key)
                stack.append(val)
            total += shallow_getsizeof(n_obj)
        elif isinstance(n_obj, Iterable):
            for val in n_obj:
                stack.append(val)
            total += shallow_getsizeof(n_obj)
        elif hasattr(n_obj, '__slots__'):
            # TODO this needs to look up the class tree...
            for key in getattr(n_obj, '__slots__'):
                stack.append(getattr(n_obj, key))
            total += shallow_getsizeof(n_obj)
        else:
            # Don't know a good way to extract data values out of an object...
            # So this isn't accurate.
            total += shallow_getsizeof(n_obj)
    return total