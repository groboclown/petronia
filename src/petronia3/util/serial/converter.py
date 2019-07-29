
# mypy: allow-any-expr
# mypy: allow-any-explicit
# mypy: allow-any-generics

"""
Simple json serialization and de-serialization tool.
"""

import json
import collections
import importlib
from typing import Any, Dict, Union, Sequence, List, Tuple
from ...errors import (
    PetroniaValueNotSerializable,
    PetroniaSerializationFormatError,
)

SerialBasic = Union[str, int, float, bool, None]
SerialRef = Tuple[int]
SerialValue = Union[SerialBasic, SerialRef]

SerialKeyValue = Tuple[SerialValue, SerialValue]
SerialTyped = Dict[str, Union[
    SerialValue, Sequence[SerialKeyValue], Sequence[SerialValue]
]]


def serialize_to_json(value: Any) -> str:
    refs: Dict[int, SerialTyped] = {}
    serializable = serialize_value(value, refs)

    return json.dumps({
        'data': serializable,
        'refs': refs,
    })


def deserialize_from_json(value: str) -> Any:
    decoded = json.loads(value)
    return deserialize_value(decoded['data'], decoded['refs'], {})


def serialize_value(value: Any, refs: Dict[int, SerialTyped]) -> SerialValue:
    """
    Attempt to serialize the value.  Any non-trivial value is stuffed into the
    `refs` structure, and a reference to it is returned.
    """
    if (
            value is None or
            isinstance(value, (str, int, float, bool))
    ):
        return value

    value_id = id(value)
    # References are stored as a single value array.
    # At this point, the return value is a non-basic value, which means it's a
    # reference value.
    ret = (value_id,)
    if value_id in refs:
        return ret

    # dict check before iterable check.
    if isinstance(value, dict):
        keyvals: List[SerialKeyValue] = []
        for key, val in value.items():
            keyvals.append((
                serialize_value(key, refs),
                serialize_value(val, refs),
            ))
        refs[value_id] = {'type': 'dict', 'keyval': keyvals}
        return ret

    if hasattr(value, '__slots__') and hasattr(value, '__class__'):
        # Internal value
        variables: List[SerialKeyValue] = []
        for key in dir(value.__slots__):
            val = getattr(ret, key)
            if not callable(val):
                variables.append((
                    key,
                    serialize_value(val, refs),
                ))
        refs[value_id] = {
            'type': 'internal',
            'class': getattr(value, '__class__').name,
            'contents': variables,
        }
        return ret

    if isinstance(value, collections.Iterable):
        contents: List[SerialValue] = []
        for val in value:
            contents.append(serialize_value(val, refs))
        refs[value_id] = {
            'type': 'list',
            'contents': contents,
        }
        return ret

    raise PetroniaValueNotSerializable('not of a serializable type', value)


def deserialize_value(
        value: SerialValue, refs: Dict[int, SerialTyped], seen: Dict[int, Any]
) -> Any:
    if (
            value is None or
            isinstance(value, (str, int, float, bool))
    ):
        return value

    if (
            not isinstance(value, collections.Iterable) or
            len(value) != 1 or
            not isinstance(value[0], int)
    ):
        raise PetroniaSerializationFormatError('expected [int], found {0}'.format(type(value)))

    value_id = value[0]
    if value_id in seen:
        return seen[value_id]

    if value_id not in refs:
        raise PetroniaSerializationFormatError('no reference to {0}'.format(value_id))

    vtype = refs[value_id]
    if not isinstance(vtype, dict):
        raise PetroniaSerializationFormatError('invalid reference format')

    if 'type' not in vtype:
        raise PetroniaSerializationFormatError('invalid format')

    value_type = vtype['type']
    if value_type == 'dict':
        if 'keyval' not in vtype or not isinstance(vtype['keyval'], collections.Iterable):
            raise PetroniaSerializationFormatError('invalid dictionary format')
        retdict: Dict[Any, Any] = {}
        for keyval in vtype['keyval']:
            if not isinstance(keyval, collections.Iterable) or len(keyval) != 2:
                raise PetroniaSerializationFormatError('invalid dictionary format')
            key = deserialize_value(keyval[0], refs, seen)
            val = deserialize_value(keyval[1], refs, seen)
            retdict[key] = val
        seen[value_id] = retdict
        return retdict
    if value_type == 'list':
        if 'contents' not in vtype or not isinstance(vtype['contents'], collections.Iterable):
            raise PetroniaSerializationFormatError('invalid list format')
        retlist: List[Any] = []
        for val in vtype['contents']:
            retlist.append(deserialize_value(val, refs, seen))
        seen[value_id] = retlist
        return retlist
    if value_type == 'internal':
        args: Dict[str, Any] = {}
        if 'class' not in vtype and not isinstance(vtype['class'], str):
            raise PetroniaSerializationFormatError('invalid class format')

        for keyval in vtype['keyval']:
            if (
                    not isinstance(keyval, collections.Iterable) or
                    len(keyval) != 2 or
                    not isinstance(keyval[0], str)
            ):
                raise PetroniaSerializationFormatError('invalid class format')
            args[keyval[0]] = deserialize_value(keyval[1], refs, seen)
        retinst = create_instance(vtype['class'], args)
        seen[value_id] = retinst
        return retinst
    else:
        raise PetroniaSerializationFormatError('invalid type {0}'.format(value_type))


def create_instance(classname: str, key_values: Dict[str, Any]) -> Any:
    parts = classname.split('.')
    module_name = '.'.join(parts[:-1])
    attr_name = parts[-1]
    if module_name == '':
        raise PetroniaSerializationFormatError('class names must be in a module')
    mod = importlib.import_module(module_name)
    if not hasattr(mod, attr_name):
        raise PetroniaSerializationFormatError(
            'no such class {0} in module {1}'.format(attr_name, module_name)
        )
    clz = getattr(mod, attr_name)
    return clz(**key_values)
