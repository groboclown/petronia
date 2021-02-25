"""Event utility functions"""

from typing import Iterable, Optional, Union
from petronia_common.util import StdRet, UserMessage, PetroniaReturnError
from petronia_ext_lib.standard.error import ErrorCategoryType, create_error_data
from .events import foreman


def create_std_ret_errors(
        error: Union[StdRet, PetroniaReturnError, UserMessage, Iterable[UserMessage]],
        identifier: str,
        categories: Iterable[ErrorCategoryType],
        source: Optional[str] = foreman.EXTENSION_NAME,
) -> Optional[foreman.Error]:
    """Turn the StdRet error into an error event value."""
    category_list = list(categories)
    return create_error_data(
        error_factory=foreman.Error,
        localizable_message_factory=foreman.LocalizableMessage,
        argument_factory=foreman.MessageArgument,
        argument_value_factory=foreman.MessageArgumentValue,
        identifier=identifier,
        categories=list(category_list),
        source=source,
        error=error,
    )
