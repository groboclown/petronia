
"""
Definition for components that use a configuration part.
"""

from typing import Dict, Mapping, Iterable, Sequence, Union
from typing import cast as t_cast
from ....base.util import T, readonly_dict


# Supported persistent types...
_PrimitivePersistType = Union[str, float, bool, None]
_GenericPersistType = Union[
    _PrimitivePersistType,
    Mapping[str, T],
    Iterable[T]
]
# FIXME Any way to make this a tree with cycles?
PersistType = Mapping[str, _GenericPersistType[
    _GenericPersistType[
        _GenericPersistType[
            _GenericPersistType[
                _GenericPersistType[
                    _GenericPersistType[
                        _GenericPersistType[
                            _GenericPersistType[
                                _PrimitivePersistType
                            ]
                        ]
                    ]
                ]
            ]
        ]
    ]
]]


class PersistTypeSchemaItem:
    __slots__ = ('__type_name', '__description',)

    def __init__(self, description: str, type_name: str) -> None:
        assert description
        assert type_name in PERSISTENT_TYPE_SCHEMA_TYPES
        self.__description = description
        self.__type_name = type_name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def type_name(self) -> str:
        return self.__type_name


# Dict: a dictionary of regex keys whose schema value match against regex matching keys values.
# Sequence: it expects a list containing any number of items, but each one must match
# up to one of the schemas in this list.
_GenericPersistSchema = Union[PersistTypeSchemaItem, Mapping[str, T], Sequence[T]]
PersistTypeSchema = Mapping[str, _GenericPersistSchema[
    _GenericPersistSchema[
        _GenericPersistSchema[
            _GenericPersistSchema[
                _GenericPersistSchema[
                    _GenericPersistSchema[
                        _GenericPersistSchema[
                            _GenericPersistSchema[
                                PersistTypeSchemaItem
                            ]
                        ]
                    ]
                ]
            ]
        ]
    ]
]]
PERSISTENT_TYPE_SCHEMA_TYPE__STR = 'str'
PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT = 'float'
PERSISTENT_TYPE_SCHEMA_TYPE__BOOL = 'bool'
PERSISTENT_TYPE_SCHEMA_TYPE__ANY = 'any'
PERSISTENT_TYPE_SCHEMA_TYPES = (
    PERSISTENT_TYPE_SCHEMA_TYPE__STR,
    PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT,
    PERSISTENT_TYPE_SCHEMA_TYPE__BOOL,
    PERSISTENT_TYPE_SCHEMA_TYPE__ANY,
)


def readonly_persistent_copy(src: PersistType) -> PersistType:
    return t_cast(PersistType, _readonly_generic_type(src))


def _readonly_generic_type(src: _GenericPersistType[T]) -> _GenericPersistType[T]:
    if (
            src is None or
            isinstance(src, str) or
            isinstance(src, int) or
            isinstance(src, float) or
            isinstance(src, bool)
    ):
        return src

    if isinstance(src, Mapping):
        ret: Dict[str, T] = {}
        for key, val in src.items():
            ret[key] = _readonly_generic_type(val)  # type: ignore
        return readonly_dict(ret)
    if isinstance(src, Iterable):
        return tuple([_readonly_generic_type(val) for val in src])  # type: ignore

    raise ValueError('unsupported persistent type: {0} ({1})'.format(type(src), repr(src)))


def readonly_persistent_schema_copy(src: PersistTypeSchema) -> PersistTypeSchema:
    return t_cast(PersistTypeSchema, _readonly_generic_schema(src))


def _readonly_generic_schema(src: _GenericPersistSchema[T]) -> _GenericPersistSchema[T]:
    if isinstance(src, PersistTypeSchemaItem):
        return src
    if isinstance(src, Mapping):
        ret: Dict[str, T] = {}
        for key, val in src.items():
            ret[key] = t_cast(T, _readonly_generic_schema(t_cast(_GenericPersistSchema[T], val)))
        return readonly_dict(ret)
    if isinstance(src, Iterable):
        return tuple([t_cast(T, _readonly_generic_schema(t_cast(_GenericPersistSchema[T], val))) for val in src])

    raise ValueError('unsupported persistent schema type: {0} ({1})'.format(type(src), repr(src)))


class PersistentConfigurationState:
    """
    A "state" value that contains values that were read from a configuration,
    and that can potentially be written back to configuration.
    """
    __slots__ = ('__persistent',)

    def __init__(self, persistent: PersistType) -> None:
        self.__persistent = readonly_persistent_copy(persistent)

    @property
    def persistent(self) -> PersistType:
        """
        Because of the nature of events, the returned value shouldn't be edited, as that
        will have unexpected consequences.
        """
        return self.__persistent
