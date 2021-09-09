
# mypy: allow-any-expr
# mypy: allow-any-explicit
# mypy: allow-any-generics

"""
Simple json serialization and de-serialization tool.
"""

from typing import Any, Dict, Union, Sequence, List, Tuple, Iterable, Mapping
import json
import importlib
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

_REFERENCE_KEY = 'R'
_DATA_KEY = 'D'


def serialize_to_json(value: Any) -> str:
    """
    Transform the value into a custom serialized JSON formatted string.

    The only object types allowed are data types that provide either public
    value members or property members, whose values are taken as named
    arguments to the constructor.
    """
    refs: Dict[int, SerialTyped] = {}
    serializable = serialize_value(value, refs)

    return json.dumps(
        {
            _DATA_KEY: serializable,
            _REFERENCE_KEY: refs,
        },

        # Make the most compact format possible.
        indent=None,
        separators=(',', ':',),

        # We construct the data such that there is no circular reference,
        # so this extra logic isn't necessary and increases performance.
        check_circular=False
    )


def deserialize_from_json(value: str) -> Any:
    """
    Deserialize the custom JSON formatted string into a value.
    """
    decoded = json.loads(value)
    if (
            not isinstance(decoded, dict) or
            _DATA_KEY not in decoded or
            # not isinstance(
            #   decoded[_DATA_KEY],
            #   (str, int, float, bool, None, collections.Iterable)
            # ) or
            _REFERENCE_KEY not in decoded or
            not isinstance(decoded[_REFERENCE_KEY], dict)
    ):
        raise PetroniaSerializationFormatError('invalid serialized format')
    return deserialize_value(decoded[_DATA_KEY], decoded[_REFERENCE_KEY], {})


_TYPE_KEY = 't'
_VALUE_LIST_KEY = 'k'
_CLASSNAME_KEY = 'c'
_DICT_TYPE = 'd'
_LIST_TYPE = 'l'
_TYPE_TYPE = 't'
_INTERNAL_CLASS_TYPE = 'z'


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

    if isinstance(value, type):
        cname = value.__module__ + '.' + value.__name__
        refs[value_id] = {
            _TYPE_KEY: _TYPE_TYPE,
            _CLASSNAME_KEY: cname,
        }
        return ret

    # dict check before iterable check.
    if isinstance(value, Mapping):
        keyvals: List[SerialKeyValue] = []
        for key, val in value.items():
            keyvals.append((
                serialize_value(key, refs),
                serialize_value(val, refs),
            ))
        refs[value_id] = {_TYPE_KEY: _DICT_TYPE, _VALUE_LIST_KEY: keyvals}
        return ret

    if hasattr(value, '__slots__') and hasattr(value, '__class__'):
        # Internal value
        cname = value.__module__ + '.' + value.__class__.__name__
        variables: List[SerialKeyValue] = []
        for key in dir(value):
            if key.startswith('_') or key.endswith('_'):
                continue
            val = getattr(value, key)
            if not callable(val) or isinstance(val, type):
                variables.append((
                    key,
                    serialize_value(val, refs),
                ))
            # else:
            #     print("Internal {0} of {1} is a {2}".format(key, value, type(val)))
        refs[value_id] = {
            _TYPE_KEY: _INTERNAL_CLASS_TYPE,
            _CLASSNAME_KEY: cname,
            _VALUE_LIST_KEY: variables,
        }
        return ret

    if isinstance(value, Iterable):
        contents: List[SerialValue] = []
        for val in value:
            contents.append(serialize_value(val, refs))
        refs[value_id] = {
            _TYPE_KEY: _LIST_TYPE,
            _VALUE_LIST_KEY: contents,
        }
        return ret

    raise PetroniaValueNotSerializable('not of a serializable type', value)


def deserialize_value(
        value: SerialValue, refs: Dict[str, SerialTyped], seen: Dict[int, Any]
) -> Any:
    """
    Turn the serialized, simplified construct into a value.
    """
    if (
            value is None or
            isinstance(value, (str, int, float, bool))
    ):
        return value

    if (
            not isinstance(value, Iterable) or
            len(tuple(value)) != 1 or
            not isinstance(value[0], int)
    ):
        raise PetroniaSerializationFormatError('expected [int], found {0}'.format(type(value)))

    value_id = value[0]
    if value_id in seen:
        return seen[value_id]

    value_id_str = str(value_id)
    if value_id_str not in refs:
        # raise PetroniaSerializationFormatError('no reference to {0}'.format(value_id))
        raise PetroniaSerializationFormatError(
            'no reference to {0}; known refs are {1}'.format(value_id, refs.keys())
        )

    vtype = refs[value_id_str]
    if not isinstance(vtype, dict):
        raise PetroniaSerializationFormatError('invalid reference format')

    if _TYPE_KEY not in vtype:
        raise PetroniaSerializationFormatError('invalid format')

    value_type = vtype[_TYPE_KEY]
    if value_type == _TYPE_TYPE:
        if _CLASSNAME_KEY not in vtype or not isinstance(vtype[_CLASSNAME_KEY], str):
            raise PetroniaSerializationFormatError('invalid type dictionary format')
        clz = find_type(vtype[_CLASSNAME_KEY])
        seen[value_id] = clz
        return clz

    if value_type == _DICT_TYPE:
        if (
                _VALUE_LIST_KEY not in vtype or
                not isinstance(vtype[_VALUE_LIST_KEY], Iterable)
        ):
            raise PetroniaSerializationFormatError('invalid dictionary format')
        retdict: Dict[Any, Any] = {}
        for keyval in vtype[_VALUE_LIST_KEY]:
            if not isinstance(keyval, Iterable) or len(tuple(keyval)) != 2:
                raise PetroniaSerializationFormatError('invalid dictionary format')
            kv = tuple(keyval)
            key = deserialize_value(kv[0], refs, seen)
            val = deserialize_value(kv[1], refs, seen)
            retdict[key] = val
        seen[value_id] = retdict
        return retdict

    if value_type == _LIST_TYPE:
        if (
                _VALUE_LIST_KEY not in vtype or
                not isinstance(vtype[_VALUE_LIST_KEY], Iterable)
        ):
            raise PetroniaSerializationFormatError('invalid list format')
        retlist: List[Any] = []
        for val in vtype[_VALUE_LIST_KEY]:
            retlist.append(deserialize_value(val, refs, seen))
        # For memory purposes, make sure this is a tuple.
        # This also allows the various internal types, like ComponentId,
        # work correctly.
        rettuple = tuple(retlist)
        seen[value_id] = rettuple
        return rettuple

    if value_type == _INTERNAL_CLASS_TYPE:
        args: Dict[str, Any] = {}
        if (
                _CLASSNAME_KEY not in vtype or
                not isinstance(vtype[_CLASSNAME_KEY], str) or
                _VALUE_LIST_KEY not in vtype or
                not isinstance(vtype[_VALUE_LIST_KEY], Iterable)
        ):
            raise PetroniaSerializationFormatError('invalid class format')

        for keyval in vtype[_VALUE_LIST_KEY]:
            if (
                    not isinstance(keyval, Iterable) or
                    len(tuple(keyval)) != 2 or
                    not isinstance(keyval[0], str)
            ):
                raise PetroniaSerializationFormatError('invalid class format')
            kv = tuple(keyval)
            args[kv[0]] = deserialize_value(kv[1], refs, seen)
        retinst = create_instance(vtype[_CLASSNAME_KEY], args)
        seen[value_id] = retinst
        return retinst
    else:
        raise PetroniaSerializationFormatError('invalid type {0}'.format(value_type))


def create_instance(classname: str, key_values: Dict[str, Any]) -> Any:
    """
    Using simple rules, turn the class name and key values into a new class
    instance.
    """
    clz = find_type(classname)
    return clz(**key_values)


def find_type(classname: str) -> type:
    parts = classname.split('.')
    module_name = '.'.join(parts[:-1])
    attr_name = parts[-1]
    if module_name == '':
        raise PetroniaSerializationFormatError('class names must be in a module')
    mod = importlib.import_module(module_name)
    if not hasattr(mod, attr_name):
        print("Failed to find '{0}' in '{1}'".format(attr_name, module_name))
        print(dir(mod))
        raise PetroniaSerializationFormatError(
            'no such class "{0}" in module "{1}"'.format(attr_name, module_name)
        )
    clz = getattr(mod, attr_name)
    if not isinstance(clz, type):
        raise PetroniaSerializationFormatError(
            'no such class "{0}" in module "{1}"'.format(attr_name, module_name)
        )
    return clz
