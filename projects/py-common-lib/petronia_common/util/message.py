
"""
Localizable message.

The most common use case:

>>> from petronia_common.util import i18n as _
>>> from petronia_common.util import UserMessage as UM
>>> # I18N: a simple message
>>> report_message(UM(_('my message {x}={y}'), x=1, y=4))

"""

from typing import Iterable, Mapping, Union, Optional, NewType
from datetime import datetime, time, date


SimpleUserMessageData = Union[str, int, float, bool, datetime, time, date, None, BaseException]
UserMessageData = Union[
    SimpleUserMessageData,
    Iterable[SimpleUserMessageData],
    Mapping[str, SimpleUserMessageData],
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

    __slots__ = ('__message', '__args', '__hash')

    def __init__(self, message: I18n, **arguments: UserMessageData) -> None:
        self.__message = message
        # Note that, because the arguments are passed as key-values, this is not a dictionary that the
        # end-user can modify.  To conserve memory and speed up the processing, the original mapping is stored.
        self.__args = arguments
        # Only compute the hash when we need to.
        self.__hash: Optional[int] = None

    @property
    def message(self) -> I18n:
        return self.__message

    @property
    def arguments(self) -> Mapping[str, UserMessageData]:
        return dict(self.__args)

    def debug(self) -> str:
        """Return a "debug" version of the user message, meaning that it isn't translated."""
        return self.__message.format(**self.__args)

    def __repr__(self) -> str:
        return 'UserMessage({0}, {1})'.format(
            repr(self.__message),
            ', '.join(['{0}={1}'.format(k, repr(v)) for k, v in self.__args.items()])
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, UserMessage):
            return False
        return other.__message == self.__message and other.__args == self.__args

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        if self.__hash is None:
            # "dict" is un-hashable.
            # Note that the hash does not need to be 100% unique; just enough
            # to bucket it well in a set or dict.
            my_hash = hash(self.__message) << 6
            for key in self.__args.keys():
                my_hash += hash(key)
            self.__hash = my_hash
        return self.__hash
