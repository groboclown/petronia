
"""
Localizable message.

The most common use case:

In a utility method for the module, define:

>>> from petronia_common.util import UserMessage, UserMessageData, I18n
>>> CATALOG = 'my-catalog'
>>> def UM(message: I18n, **arguments: UserMessageData) -> UserMessage:
>>>    return UserMessage(CATALOG, message, **arguments)

Then, in the code, define:
>>> from petronia_common.util import i18n as _
>>> report_message(UM(_('my message {x}={y}'), x=1, y=4))

"""

from typing import Iterable, Mapping, Union, Optional, NewType
from datetime import datetime, time, date


STANDARD_PETRONIA_CATALOG = 'petronia'

SimpleUserMessageData = Union[str, int, float, bool, datetime, time, date, None, BaseException]
# Iterables must be of a unified type.
ListUserMessageData = Union[
    Iterable[str],
    Iterable[int],
    Iterable[float],
    Iterable[bool],
    Iterable[datetime],
    Iterable[time],
    Iterable[date],
]
UserMessageData = Union[
    SimpleUserMessageData,
    Mapping[str, SimpleUserMessageData],
    ListUserMessageData,
]
I18n = NewType('I18n', str)


def i18n(message: str) -> I18n:
    """
    Localization message string function, for message extraction.  This should generally be
    imported `as _` so that the localization helper tool can do its magic.

    :param message:
    :return:
    """
    return I18n(message)


class UserMessage:
    """
    A message that can be displayed to the end-user.
    """

    __slots__ = ('__catalog', '__message', '__args', '__hash')

    def __init__(self, catalog: str, message: I18n, **arguments: UserMessageData) -> None:
        self.__catalog = catalog
        self.__message = message
        # Note that, because the arguments are passed as key-values, this is not
        # a dictionary that the end-user can modify.  To conserve memory and speed up the
        # processing, the original mapping is stored.
        self.__args = arguments
        # Only compute the hash when we need to.
        self.__hash: Optional[int] = None

    @property
    def catalog(self) -> str:
        """The catalog that owns the message for purposes of localization."""
        return self.__catalog

    @property
    def message(self) -> I18n:
        """The message text, which should be localized."""
        return self.__message

    @property
    def arguments(self) -> Mapping[str, UserMessageData]:
        """The programmatic arguments for the message."""
        return dict(self.__args)

    def debug(self) -> str:
        """Return a "debug" version of the user message, meaning that it isn't translated."""
        return self.__message.format(**self.__args)

    def __repr__(self) -> str:
        msg = repr(self.__message)
        parts = ', '.join([f'{k}={repr(v)}' for k, v in self.__args.items()])
        return f'UserMessage({msg}, {parts})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, UserMessage):
            return False
        return (
            other.catalog == self.__catalog
            and other.message == self.__message
            and other.arguments == self.__args
        )

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        if self.__hash is None:
            # "dict" is un-hashable.
            # Note that the hash does not need to be 100% unique; just enough
            # to bucket it well in a set or dict.
            my_hash = (hash(self.__message) << 6) + (hash(self.__catalog) << 3)
            for key in self.__args:
                my_hash += hash(key)
            self.__hash = my_hash
        return self.__hash
