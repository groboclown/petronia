"""Creates a generic Error object."""

from typing import List, Iterable, Sequence, Callable, Optional, Union, Literal, TypeVar, cast
from petronia_common.util import StdRet, UserMessage, T, V, K, PetroniaReturnError
from .localizable_message import (
    LocaleMessageArgumentTypeName,
    LocaleMessageArgumentType,
    create_localizable_message,
)

# We need an extra one of these to get things to work.
Z = TypeVar('Z')  # pylint: disable=invalid-name


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


def create_error_data(  # pylint:disable=too-many-arguments
        error_factory: Callable[
            [str, List[str], Optional[str], List[K]],
            Z,
        ],
        localizable_message_factory: Callable[
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
        error: Union[StdRet, PetroniaReturnError, UserMessage, Iterable[UserMessage]],
        categories: List[ErrorCategoryType],
        identifier: str,
        source: Optional[str] = None,
) -> Optional[Z]:
    """Create the error typed value form the factories, if the StdRet is an error."""
    messages: Sequence[UserMessage]
    if isinstance(error, StdRet):
        messages = error.error_messages()
    elif isinstance(error, PetroniaReturnError):
        messages = error.messages()
    elif isinstance(error, UserMessage):
        messages = (error,)
    else:
        # isinstance(error, collections.abc.Iterable)
        messages = list(error)
    return create_error_message_data(
        error_factory, localizable_message_factory, argument_factory, argument_value_factory,
        messages,
        categories, identifier, source,
    )


def create_error_message_data(  # pylint:disable=too-many-arguments
        error_factory: Callable[
            [str, List[str], Optional[str], List[K]],
            Z,
        ],
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
        messages: Sequence[UserMessage],
        categories: List[ErrorCategoryType],
        identifier: str,
        source: Optional[str] = None,
) -> Optional[Z]:
    """Create the error typed value form the factories, if there are any user messages."""
    if not messages:
        return None
    return error_factory(
        identifier, cast(List[str], categories), source,
        [
            create_localizable_message(
                message_factory, argument_factory, argument_value_factory, m,
            )
            for m in messages
        ],
    )
