"""
Handles the embedded-json-data type.  Indeed, it has type-safe accessors
for general JSON actions.

The parsing is loose, in order to better support end-user configurations.
"""

from typing import Mapping, Sequence, Iterable, Tuple, Union, Optional, Any
import json
import collections.abc
from petronia_common.util import StdRet, RET_OK_NONE
from petronia_common.util import i18n as _

StructuredDataType = Union[None, Sequence[Any], Mapping[str, Any], int, float, str, bool]
StructuredPath = Sequence[str]


def embedded_json_data(data: Optional[str]) -> StdRet[StructuredDataType]:
    """Convert the json data into a json object.  If the returned value
    is an error, then the caller should augment it with the source of the
    problem; this error only reports the low-level JSON trouble."""
    if not data:
        return RET_OK_NONE

    try:
        return StdRet.pass_ok(json.loads(data))
    except json.JSONDecodeError as err:
        return StdRet.pass_exception(
            _('invalid embedded JSON data'),
            err,
        )


def as_structured(value: Any) -> StructuredDataType:
    """Convert the value into a structured data type."""
    if isinstance(
            value, (collections.abc.Sequence, collections.abc.Mapping, int, float, str, bool),
    ):
        return value
    return None


def json_str(data: StructuredDataType) -> Optional[str]:
    """Converts this data into a string.  If it isn't a
    string, it returns None."""
    if isinstance(data, str):
        return data
    if isinstance(data, (float, int, bool)):
        return str(data)
    return None


def json_int(data: StructuredDataType) -> Optional[int]:
    """Converts this data into an int, in a way that's reasonable.
    Strings, floats, and ints will be mangled into an int, if possible."""

    if isinstance(data, int):
        # Note: this implicitly handles bool, too.
        return data
    if isinstance(data, float):
        return int(data)
    if isinstance(data, str):
        radix = 10
        if len(data) > 2 and data[0] == '0' and data[1] in _RADIX_MAP:
            radix = _RADIX_MAP[data[1]]
            data = data[2:]
        try:
            return int(data, radix)
        except ValueError:
            return None
    return None


def json_float(data: StructuredDataType) -> Optional[float]:
    """Converts this data into a float, in a way that's reasonable."""
    if isinstance(data, float):
        return data
    if isinstance(data, int):
        # Note: this implicitly handles bool, too
        return float(data)
    if isinstance(data, str):
        try:
            return float(data)
        except ValueError:
            return None
    return None


def json_bool(data: StructuredDataType) -> Optional[bool]:
    """Converts this data into a boolean value, in a way that's reasonable."""
    if isinstance(data, bool):
        return data
    if isinstance(data, (int, float)):
        return int(data) != 0
    if isinstance(data, str):
        return _BOOL_TRUE.get(data.lower(), False)
    return None


def json_map(data: StructuredDataType) -> Optional[Mapping[str, Any]]:
    """Converts this data into a dictionary / map."""
    if isinstance(data, collections.abc.Mapping):
        return data
    return None


def json_array(data: StructuredDataType) -> Optional[Sequence[Any]]:
    """Converts this data into an array.  Strings are explicitly returned as None."""
    if isinstance(data, (str, collections.abc.Mapping)):
        return None
    if isinstance(data, collections.abc.Iterable):
        return tuple(data)
    return None


def json_iter_array(
        parent_path: StructuredPath, seq: Sequence[Any],
) -> Iterable[Tuple[StructuredPath, StructuredDataType]]:
    """Allows for easy iteration over a sequence to include the path for each element."""
    index = 0
    for item in seq:
        yield (*parent_path, str(index)), as_structured(item)
        index += 1


def json_iter_map(
        parent_path: StructuredPath, map_value: Mapping[str, Any],
) -> Iterable[Tuple[StructuredPath, str, StructuredDataType]]:
    """Allows for easy iteration over a mapping to include the path for each element."""
    for key, value in map_value.items():
        yield (*parent_path, key), key, as_structured(value)


def json_map_value_options(
        map_value: Mapping[str, Any], key: Union[str, Sequence[str]],
) -> Optional[Tuple[str, StructuredDataType]]:
    """Check the map for any of the given key values, case insensitive.  This expects
    the input key or keys to be lower-cased."""
    keys: Sequence[str]
    if isinstance(key, str):
        keys = (key.lower(),)
    else:
        keys = key
    for map_key, value in map_value.items():
        if map_key.lower() in keys:
            return map_key, as_structured(value)
    return None


def json_map_str(
        parent_path: StructuredPath,
        map_value: Mapping[str, Any],
        key: Union[str, Sequence[str]],
) -> Tuple[StructuredPath, Optional[str]]:
    """Get the path + item for the key in the mapping."""
    opt = json_map_value_options(map_value, key)
    if opt is None:
        return parent_path, None
    return (*parent_path, opt[0]), json_str(opt[1])


def json_map_int(
        parent_path: StructuredPath,
        map_value: Mapping[str, Any],
        key: Union[str, Sequence[str]],
) -> Tuple[StructuredPath, Optional[int]]:
    """Get the path + item for the key in the mapping."""
    opt = json_map_value_options(map_value, key)
    if opt is None:
        return parent_path, None
    return (*parent_path, opt[0]), json_int(opt[1])


def json_map_float(
        parent_path: StructuredPath,
        map_value: Mapping[str, Any],
        key: Union[str, Sequence[str]],
) -> Tuple[StructuredPath, Optional[float]]:
    """Get the path + item for the key in the mapping."""
    opt = json_map_value_options(map_value, key)
    if opt is None:
        return parent_path, None
    return (*parent_path, opt[0]), json_float(opt[1])


def json_map_bool(
        parent_path: StructuredPath,
        map_value: Mapping[str, Any],
        key: Union[str, Sequence[str]],
) -> Tuple[StructuredPath, Optional[bool]]:
    """Get the path + item for the key in the mapping."""
    opt = json_map_value_options(map_value, key)
    if opt is None:
        return parent_path, None
    return (*parent_path, opt[0]), json_bool(opt[1])


def json_map_array(
        parent_path: StructuredPath,
        map_value: Mapping[str, Any],
        key: Union[str, Sequence[str]],
) -> Tuple[StructuredPath, Optional[Sequence[Any]]]:
    """Get the path + item for the key in the mapping."""
    opt = json_map_value_options(map_value, key)
    if opt is None:
        return parent_path, None
    return (*parent_path, opt[0]), json_array(opt[1])


def json_map_map(
        parent_path: StructuredPath,
        map_value: Mapping[str, Any],
        key: Union[str, Sequence[str]],
) -> Tuple[StructuredPath, Optional[Mapping[str, Any]]]:
    """Get the path + item for the key in the mapping."""
    opt = json_map_value_options(map_value, key)
    if opt is None:
        return parent_path, None
    return (*parent_path, opt[0]), json_map(opt[1])


_RADIX_MAP = {
    'b': 2,
    'B': 2,
    'o': 8,
    'O': 8,
    'x': 16,
    'X': 16,
}


_BOOL_TRUE = {
    'on': True,
    'yes': True,
    'ok': True,
    'valid': True,
    '1': True,
    'true': True,
    'confirmed': True,
    'affirmative': True,
    'active': True,
}
