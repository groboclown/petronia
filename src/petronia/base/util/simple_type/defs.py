
"""
Type definitions for the simple type.
"""

from typing import Mapping, Iterable, Union
from ..memory import T


# Supported persistent types...
_PrimitivePersistType = Union[str, float, bool, None]
GenericPersistType = Union[
    _PrimitivePersistType,
    Mapping[str, T],
    Iterable[T]
]
PersistType = Mapping[str, GenericPersistType[
    GenericPersistType[
        GenericPersistType[
            GenericPersistType[
                GenericPersistType[
                    GenericPersistType[
                        GenericPersistType[
                            GenericPersistType[
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
    """
    A description of a schema item.  For `id` and `ref` types,
    the `description` must be the ID.
    """
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
GenericPersistSchema = Union[PersistTypeSchemaItem, Mapping[str, T], Iterable[T]]
PersistTypeSchema = Mapping[str, GenericPersistSchema[
    GenericPersistSchema[
        GenericPersistSchema[
            GenericPersistSchema[
                GenericPersistSchema[
                    GenericPersistSchema[
                        GenericPersistSchema[
                            GenericPersistSchema[
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
PERSISTENT_TYPE_SCHEMA_TYPE__REF = 'ref'
PERSISTENT_TYPE_SCHEMA_TYPE__ID = 'id'
PERSISTENT_TYPE_SCHEMA_NAME__SCHEMA = '__schema'
PERSISTENT_TYPE_SCHEMA_NAME__DOC = '__doc'
PERSISTENT_TYPE_SCHEMA_TYPES = (
    PERSISTENT_TYPE_SCHEMA_TYPE__STR,
    PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT,
    PERSISTENT_TYPE_SCHEMA_TYPE__BOOL,
    PERSISTENT_TYPE_SCHEMA_TYPE__ANY,
    PERSISTENT_TYPE_SCHEMA_TYPE__REF,
    PERSISTENT_TYPE_SCHEMA_TYPE__ID,
)
