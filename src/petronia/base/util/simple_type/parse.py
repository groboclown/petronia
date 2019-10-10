
"""
Helper functions to parse the data, usually user configuration data, into
other data structures.
"""

from typing import Callable, List, Mapping, Iterable, Optional, Union
from typing import cast as t_cast
from .defs import (
    PersistType,
    GenericPersistType,
)
from ..memory import T, K, EMPTY_LIST
from ...events.system_events import (
    ErrorReport,
    ResultWithErrors,
)

NO_ERRORS = t_cast(Iterable[ErrorReport], EMPTY_LIST)


def as_persist(m: GenericPersistType[T]) -> PersistType:
    """Convert the mapping to a persist type."""
    if not isinstance(m, Mapping):
        raise ValueError('must be a mapping')
    return t_cast(PersistType, m)


def collect_errors(errors: List[ErrorReport], res: ResultWithErrors[T]) -> T:
    """Collect the reported errors into the error list, and return the result value."""
    errors.extend(res[1])
    return res[0]


def required_dict(
        errors: List[ErrorReport], value: Union[PersistType, GenericPersistType[T]],
        handler: Callable[[PersistType], ResultWithErrors[Optional[K]]],
        error_handler: Optional[Callable[[], ErrorReport]] = None
) -> Optional[K]:
    """
    Unifies a common checking pattern into a single call.  If `value` is not
    a mapping, then the optional `error_handler` is invoked and None is returned.
    Otherwise, the handler is run and the errors returned are collected.

    The error handler is usually a simple lambda to create the error message.

    :param errors:
    :param value:
    :param handler:
    :param error_handler:
    :return:
    """
    if not isinstance(value, Mapping):
        if error_handler:
            errors.append(error_handler())
        return None
    return collect_errors(errors, handler(as_persist(value)))


def with_key_as_dict(
        value: Union[PersistType, GenericPersistType[T]], key: str,
        error_handler: Optional[Callable[[], ErrorReport]] = None
) -> ResultWithErrors[Optional[PersistType]]:
    if isinstance(value, Mapping) and key in value:
        v_key = value[key]
        if isinstance(v_key, Mapping):
            return t_cast(PersistType, v_key), NO_ERRORS
        elif error_handler:
            return None, (error_handler(),)
        else:
            return None, NO_ERRORS
    return None, NO_ERRORS


def with_key_as_list(
        value: Union[PersistType, GenericPersistType[T]], key: str,
        error_handler: Optional[Callable[[], ErrorReport]] = None
) -> ResultWithErrors[Optional[List[PersistType]]]:
    if isinstance(value, Mapping) and key in value:
        v_key = value[key]
        if isinstance(v_key, Iterable):
            return [t_cast(PersistType, v) for v in v_key], NO_ERRORS
        elif error_handler:
            return None, (error_handler(),)
        else:
            return None, NO_ERRORS
    return None, NO_ERRORS


def list_of_maps(
        values: Iterable[object], errors: List[ErrorReport], error_handler: Callable[[int], ErrorReport]
) -> Iterable[PersistType]:
    i = 0
    for item in values:
        if not isinstance(item, Mapping):
            errors.append(error_handler(i))
        else:
            yield item
        i += 1


def is_key_true(value: Union[PersistType, GenericPersistType[T]], key: str) -> bool:
    """Test if the key is explicitly in the value and that the value for that key is explicitly the boolean True."""
    if isinstance(value, Mapping) and key in value and value[key] is True:
        return True
    return False


def is_key_false(value: Union[PersistType, GenericPersistType[T]], key: str) -> bool:
    """Test if the key is explicitly in the value and that the value for that key is explicitly the boolean False."""
    if isinstance(value, Mapping) and key in value and value[key] is False:
        return True
    return False
