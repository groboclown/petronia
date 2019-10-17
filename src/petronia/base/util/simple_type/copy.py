
"""
Copy creation of the simple type.
"""

from typing import Dict, Mapping, Iterable, Union, overload
from typing import cast as t_cast
from .defs import (
    PersistType,
    PersistTypeSchema,
    PersistTypeSchemaItem,
    GenericPersistType,
    GenericPersistSchema,
)
from ..memory import (
    readonly_dict,
    T,
)


@overload
def readonly_persistent_copy(src: PersistType) -> PersistType:
    ...


@overload
def readonly_persistent_copy(src: Mapping[str, object]) -> PersistType:
    ...


def readonly_persistent_copy(src: Union[Mapping[str, object], PersistType]) -> PersistType:
    return t_cast(PersistType, _readonly_generic_type(t_cast(PersistType, src)))


def _readonly_generic_type(src: GenericPersistType[T]) -> GenericPersistType[T]:
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


@overload
def readonly_persistent_schema_copy(src: PersistTypeSchema) -> PersistTypeSchema:
    ...


@overload
def readonly_persistent_schema_copy(src: Mapping[str, object]) -> PersistTypeSchema:
    ...


def readonly_persistent_schema_copy(src: Union[PersistTypeSchema, Mapping[str, object]]) -> PersistTypeSchema:
    return t_cast(PersistTypeSchema, _readonly_generic_schema(t_cast(PersistTypeSchema, src)))


def _readonly_generic_schema(src: GenericPersistSchema[T]) -> GenericPersistSchema[T]:
    if isinstance(src, PersistTypeSchemaItem):
        return src
    if isinstance(src, Mapping):
        ret: Dict[str, T] = {}
        for key, val in src.items():
            ret[key] = t_cast(T, _readonly_generic_schema(t_cast(GenericPersistSchema[T], val)))
        return readonly_dict(ret)
    if isinstance(src, str):
        return src
    if isinstance(src, Iterable):
        return tuple([t_cast(T, _readonly_generic_schema(t_cast(GenericPersistSchema[T], val))) for val in src])

    raise ValueError('unsupported persistent schema type: {0} ({1})'.format(type(src), repr(src)))
