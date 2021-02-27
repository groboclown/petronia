"""Handles a generic way to create the LocalizableMessage structure from common Petronia
types."""

from typing import List, Tuple, Callable, Union, Literal, cast
import collections.abc
import datetime
from petronia_common.util import T, V, K, tznow
from petronia_common.util.message import UserMessage, UserMessageData, ListUserMessageData


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


def create_localizable_message(
        message_factory: Callable[
            [str, str, List[V]],
            K,
        ],
        argument_factory: Callable[
            [str, T],
            V,
        ],
        argument_value_factory: Callable[
            [LocaleMessageArgumentTypeName, LocaleMessageArgumentType], T,
        ],
        message: UserMessage,
) -> K:
    """Creates a message from the standard UserMessage, typed for the event.
    The 'factories' passed in as arguments should just be the constructors
    for those objects."""
    return message_factory(
        message.catalog,
        message.message,
        [
            create_message_argument(argument_factory, argument_value_factory, key, value)
            for key, value in message.arguments.items()
        ],
    )


def create_message_argument(
        argument_factory: Callable[
            [str, T],
            V,
        ],
        argument_value_factory: Callable[
            [LocaleMessageArgumentTypeName, LocaleMessageArgumentType], T,
        ],
        key: str, value: UserMessageData,
) -> V:
    """Creates a message-argument, typed for the event."""
    type_name, typed_value = create_message_argument_value(value)
    return argument_factory(key, argument_value_factory(type_name, typed_value))


def create_message_argument_value(  # pylint:disable=too-many-return-statements
        arg_value: UserMessageData,
) -> Tuple[LocaleMessageArgumentTypeName, LocaleMessageArgumentType]:
    """Examine the data value to find the best matching type and value."""
    if arg_value is None:
        # not directly supported
        return STRING_LOCALE_ARGUMENT_TYPE, '<null>'
    if isinstance(arg_value, str):
        # str is iterable but must be handled carefully.
        return STRING_LOCALE_ARGUMENT_TYPE, arg_value
    if isinstance(arg_value, dict):
        # not directly translatable...
        # sort the keys, so that it's repeatable and easier for end users to read.
        return STRING_LIST_LOCALE_ARGUMENT_TYPE, [
            f'{key}={repr(val)}'
            for key, val in sorted(list(arg_value.items()), key=lambda x: str(x[0]))
        ]
    if isinstance(arg_value, collections.abc.Iterable):
        return _get_list_message_arguments(arg_value)
    if isinstance(arg_value, bool):
        return BOOL_LOCALE_ARGUMENT_TYPE, arg_value
    if isinstance(arg_value, int):
        return INT_LOCALE_ARGUMENT_TYPE, arg_value
    if isinstance(arg_value, float):
        return FLOAT_LOCALE_ARGUMENT_TYPE, arg_value
    if isinstance(arg_value, datetime.datetime):
        return DATETIME_LOCALE_ARGUMENT_TYPE, arg_value
    if isinstance(arg_value, datetime.time):
        now = tznow()
        return DATETIME_LOCALE_ARGUMENT_TYPE, datetime.datetime(
            year=now.year, month=now.month, day=now.day,
            hour=arg_value.hour, minute=arg_value.minute,
            second=arg_value.second, microsecond=arg_value.microsecond,
            tzinfo=arg_value.tzinfo,
        )
    if isinstance(arg_value, datetime.date):
        return DATETIME_LOCALE_ARGUMENT_TYPE, datetime.datetime(
            year=arg_value.year, month=arg_value.month, day=arg_value.day,
            tzinfo=datetime.timezone.utc,
        )

    # Shouldn't happen, but don't error out.
    return STRING_LOCALE_ARGUMENT_TYPE, str(arg_value)


def _get_list_message_arguments(  # pylint:disable=too-many-return-statements
        arg_values: ListUserMessageData,
) -> Tuple[LocaleMessageArgumentTypeName, LocaleMessageArgumentType]:
    values = list(arg_values)
    if len(values) <= 0:
        # No way to identify the type, but it doesn't really matter.
        return STRING_LIST_LOCALE_ARGUMENT_TYPE, cast(List[str], values)

    # Assume that the first value reflects all the types of the list.
    val0 = values[0]
    if isinstance(val0, str):
        return STRING_LIST_LOCALE_ARGUMENT_TYPE, cast(List[str], values)
    if isinstance(val0, bool):
        return BOOL_LIST_LOCALE_ARGUMENT_TYPE, cast(List[bool], values)
    if isinstance(val0, int):
        return INT_LIST_LOCALE_ARGUMENT_TYPE, cast(List[int], values)
    if isinstance(val0, float):
        return FLOAT_LIST_LOCALE_ARGUMENT_TYPE, cast(List[float], values)
    if isinstance(val0, datetime.datetime):
        return DATETIME_LIST_LOCALE_ARGUMENT_TYPE, cast(List[datetime.datetime], values)
    if isinstance(val0, datetime.time):
        now = tznow()
        return DATETIME_LIST_LOCALE_ARGUMENT_TYPE, [
            datetime.datetime(
                year=now.year, month=now.month, day=now.day,
                hour=arg_value.hour, minute=arg_value.minute, second=arg_value.second,
                microsecond=arg_value.microsecond,
                tzinfo=arg_value.tzinfo,
            )
            for arg_value in cast(List[datetime.time], values)
        ]
    if isinstance(val0, datetime.date):
        return DATETIME_LIST_LOCALE_ARGUMENT_TYPE, [
            datetime.datetime(
                arg_value.year, arg_value.month, arg_value.day,
                tzinfo=datetime.timezone.utc,
            )
            for arg_value in cast(List[datetime.date], values)
        ]

    # Should not be possible, but allow.
    return STRING_LIST_LOCALE_ARGUMENT_TYPE, [
        str(val)
        for val in values
    ]
