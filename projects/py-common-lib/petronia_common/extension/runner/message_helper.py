"""Helper functions for creating the standardized message and error types.
Many of these functions are hampered from being a generic form due to the
per-extension way of defining the event data.
"""

from typing import List, Tuple, Iterable, Set, Literal, Union, cast
import datetime
import collections.abc
from petronia_common.util.message import (
    UserMessage, ListUserMessageData, STANDARD_PETRONIA_CATALOG,
)

LocaleMessageArgumentType = Union[
    List[bool],
    bool,
    List[float],
    List[datetime.datetime],
    datetime.datetime,
    int,
    float,
    str,
    List[int],
    List[str],
]
LocaleMessageArgumentTypeName = Literal[
    'string', 'int', 'float', 'bool', 'datetime',
    'string_list', 'int_list', 'float_list', 'bool_list', 'datetime_list',
]
STRING_LOCALE_ARGUMENT_TYPE: LocaleMessageArgumentTypeName = 'string'
STRING_LIST_LOCALE_ARGUMENT_TYPE: LocaleMessageArgumentTypeName = 'string_list'
INT_LOCALE_ARGUMENT_TYPE: LocaleMessageArgumentTypeName = 'int'
INT_LIST_LOCALE_ARGUMENT_TYPE: LocaleMessageArgumentTypeName = 'int_list'
FLOAT_LOCALE_ARGUMENT_TYPE: LocaleMessageArgumentTypeName = 'float'
FLOAT_LIST_LOCALE_ARGUMENT_TYPE: LocaleMessageArgumentTypeName = 'float_list'
BOOL_LOCALE_ARGUMENT_TYPE: LocaleMessageArgumentTypeName = 'bool'
BOOL_LIST_LOCALE_ARGUMENT_TYPE: LocaleMessageArgumentTypeName = 'bool_list'
DATETIME_LOCALE_ARGUMENT_TYPE: LocaleMessageArgumentTypeName = 'datetime'
DATETIME_LIST_LOCALE_ARGUMENT_TYPE: LocaleMessageArgumentTypeName = 'datetime_list'


ErrorCategoryType = Literal[
    'file', 'os', 'configuration', 'network', 'access-restriction',
    'invalid-user-action', 'internal',
]
FILE_ERROR_CATEGORY: ErrorCategoryType = 'file'
OS_ERROR_CATEGORY: ErrorCategoryType = 'os'
CONFIGURATION_ERROR_CATEGORY: ErrorCategoryType = 'configuration'
NETWORK_ERROR_CATEGORY: ErrorCategoryType = 'network'
ACCESS_RESTRICTION_ERROR_CATEGORY: ErrorCategoryType = 'access-restriction'
INVALID_USER_ACTION_ERROR_CATEGORY: ErrorCategoryType = 'invalid-user-action'
INTERNAL_ERROR_CATEGORY: ErrorCategoryType = 'internal'


def join_message_text(
        messages: Iterable[UserMessage],
) -> str:
    """Join the user messages together."""
    return '; '.join([m.message for m in messages])


def get_message_catalog(messages: Iterable[UserMessage]) -> str:
    """Get the message catalog for the collection of messages."""
    catalog = STANDARD_PETRONIA_CATALOG
    for message in messages:
        catalog = message.catalog
    return catalog


def get_message_arguments(  # pylint:disable=too-many-branches
        *messages: UserMessage,
) -> List[Tuple[str, LocaleMessageArgumentTypeName, LocaleMessageArgumentType]]:
    """Constructs the message argument values, in the form of argument name,
    argument type name, and argument value.
    """
    found: Set[str] = set()
    ret: List[Tuple[str, LocaleMessageArgumentTypeName, LocaleMessageArgumentType]] = []

    for message in messages:
        for arg_name, arg_value in message.arguments.items():
            if arg_name in found:
                # Skip it, so there isn't a naming collision problem.
                continue
            found.add(arg_name)
            if arg_value is None:
                # not directly supported
                ret.append((arg_name, STRING_LOCALE_ARGUMENT_TYPE, '<null>'))
            elif isinstance(arg_value, str):
                # str is iterable but must be handled carefully.
                ret.append((arg_name, STRING_LOCALE_ARGUMENT_TYPE, arg_value))
            elif isinstance(arg_value, dict):
                # not directly translatable...
                ret.append((arg_name, STRING_LIST_LOCALE_ARGUMENT_TYPE, [
                    f'{key}={repr(val)}'
                    for key, val in sorted(list(arg_value.items()), key=lambda x: str(x[0]))
                ]))
            elif isinstance(arg_value, collections.abc.Iterable):
                ret.append(_get_list_message_arguments(arg_name, arg_value))
            elif isinstance(arg_value, bool):
                ret.append((arg_name, BOOL_LOCALE_ARGUMENT_TYPE, arg_value))
            elif isinstance(arg_value, int):
                ret.append((arg_name, INT_LOCALE_ARGUMENT_TYPE, arg_value))
            elif isinstance(arg_value, float):
                ret.append((arg_name, FLOAT_LOCALE_ARGUMENT_TYPE, arg_value))
            elif isinstance(arg_value, datetime.datetime):
                ret.append((arg_name, DATETIME_LOCALE_ARGUMENT_TYPE, arg_value))
            elif isinstance(arg_value, datetime.time):
                now = datetime.datetime.now()
                ret.append((arg_name, DATETIME_LOCALE_ARGUMENT_TYPE, datetime.datetime(
                    now.year, now.month, now.day,
                    arg_value.hour, arg_value.minute, arg_value.second, arg_value.microsecond,
                )))
            elif isinstance(arg_value, datetime.date):
                ret.append((arg_name, DATETIME_LOCALE_ARGUMENT_TYPE, datetime.datetime(
                    arg_value.year, arg_value.month, arg_value.day,
                )))
            else:
                # Shouldn't happen, but don't error out.
                ret.append((arg_name, STRING_LOCALE_ARGUMENT_TYPE, str(arg_value)))
    return ret


def _get_list_message_arguments(  # pylint:disable=too-many-return-statements
        name: str,
        arg_values: ListUserMessageData,
) -> Tuple[str, LocaleMessageArgumentTypeName, LocaleMessageArgumentType]:
    values = list(arg_values)
    if len(values) <= 0:
        # No way to identify the type, but it doesn't really matter.
        return name, STRING_LIST_LOCALE_ARGUMENT_TYPE, cast(List[str], values)

    # Assume that the first value reflects all the types of the list.
    val0 = values[0]
    if isinstance(val0, str):
        return name, STRING_LIST_LOCALE_ARGUMENT_TYPE, cast(List[str], values)
    if isinstance(val0, bool):
        return name, BOOL_LIST_LOCALE_ARGUMENT_TYPE, cast(List[bool], values)
    if isinstance(val0, int):
        return name, INT_LIST_LOCALE_ARGUMENT_TYPE, cast(List[int], values)
    if isinstance(val0, float):
        return name, FLOAT_LIST_LOCALE_ARGUMENT_TYPE, cast(List[float], values)
    if isinstance(val0, datetime.datetime):
        return name, DATETIME_LIST_LOCALE_ARGUMENT_TYPE, cast(List[datetime.datetime], values)
    if isinstance(val0, datetime.time):
        now = datetime.datetime.now()
        return name, DATETIME_LIST_LOCALE_ARGUMENT_TYPE, [
            datetime.datetime(
                now.year, now.month, now.day,
                arg_value.hour, arg_value.minute, arg_value.second, arg_value.microsecond,
            )
            for arg_value in cast(List[datetime.time], values)
        ]
    if isinstance(val0, datetime.date):
        return name, DATETIME_LIST_LOCALE_ARGUMENT_TYPE, [
            datetime.datetime(
                arg_value.year, arg_value.month, arg_value.day,
            )
            for arg_value in cast(List[datetime.date], values)
        ]

    # Should not be possible, but allow.
    return name, STRING_LIST_LOCALE_ARGUMENT_TYPE, [
        str(val)
        for val in values
    ]
