
# mypy: allow-any-expr
# mypy: allow-any-explicit
# mypy: allow-any-generics

"""
Constructs the Pythonified representation of the object.
"""

from typing import Any, Dict, Mapping, List, Tuple, Iterable, Type
from ..memory import T


def add_repr(cz: Type[T]) -> Type[T]:
    cz.__repr__ = classmethod(repr_value)  # type: ignore
    return cz


def repr_value(value: Any) -> str:
    """Creates a python repr-like string for a serializable class instance."""
    return _repr_value(value, {})


def _repr_value(value: Any, refs: Dict[int, str]) -> str:
    """
    Uses the same algorithm of the serialization, but generates a Python-looking repr
    value.
    """
    if (
            value is None or
            isinstance(value, (str, int, float, bool))
    ):
        return repr(value)

    value_id = id(value)
    if value_id in refs:
        return refs[value_id]

    if isinstance(value, type):
        return repr(value)

    # dict check before iterable check.
    if isinstance(value, Mapping):
        keyvals: Dict[str, str] = {}
        for key, val in value.items():
            try:
                keyvals[_repr_value(key, refs)] = _repr_value(val, refs)
            except ValueError as err:
                raise ValueError(
                    'key {0} value {1} not serializable'.format(key, val),
                    (value, err.args[1])
                )
        ret = repr(keyvals)
        refs[value_id] = ret
        return ret

    if hasattr(value, '__slots__') and hasattr(value, '__class__'):
        # Internal value
        cname = value.__module__ + '.' + value.__class__.__name__
        ret = '{0}('.format(cname)
        first = True
        for key in dir(value):
            if key.startswith('_') or key.endswith('_'):
                continue
            val = getattr(value, key)
            if not callable(val) or isinstance(val, type):
                if first:
                    first = False
                else:
                    ret += ', '
                try:
                    ret += '{0}={1}'.format(key, _repr_value(val, refs))
                except ValueError as err:
                    raise ValueError(
                        'property {0} with value {1} not serializable'.format(key, val),
                        (value, err.args[1])
                    )
        ret += ')'
        refs[value_id] = ret
        return ret

    if isinstance(value, Iterable):
        contents: List[str] = []
        for val in value:
            try:
                contents.append(_repr_value(val, refs))
            except ValueError as err:
                raise ValueError(
                    'element {0} not serializable'.format(val),
                    (value, err.args[1])
                )
        if isinstance(value, tuple):
            ret = repr(tuple(contents))
        else:
            ret = repr(contents)
        refs[value_id] = ret
        return ret

    raise ValueError('not of a serializable type', value)
