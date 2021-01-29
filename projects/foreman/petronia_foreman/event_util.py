"""Event utility functions"""

from typing import Iterable, List, Optional, cast
from petronia_common.util import UserMessage, PetroniaReturnError, not_none
from petronia_common.util import i18n as _
from petronia_common.extension.runner import message_helper
from .events import foreman
from .user_message import TRANSLATION_CATALOG


def create_std_ret_errors(
        res: PetroniaReturnError,
        categories: Iterable[message_helper.ErrorCategoryType],
        source: Optional[str] = foreman.EXTENSION_NAME,
        corrective_action_msg: Optional[UserMessage] = None,
) -> List[foreman.Error]:
    """Turn the StdRet error into an error event value."""
    category_list = list(categories)
    corrective_action = create_optional_message(corrective_action_msg)
    ret: List[foreman.Error] = []
    for message in res.messages():
        ret.append(foreman.Error(
            identifier=message.message,
            categories=cast(List[str], category_list),
            source=source,
            corrective_action=corrective_action,
            error_message=create_message(message),
        ))
    return ret


def create_top_std_ret_error(
        res: PetroniaReturnError,
        categories: Iterable[message_helper.ErrorCategoryType],
        source: Optional[str] = foreman.EXTENSION_NAME,
        corrective_action_msg: Optional[UserMessage] = None,
) -> foreman.Error:
    """Create the error for the top message in the return."""
    errors = create_std_ret_errors(
        res, categories, source, corrective_action_msg=corrective_action_msg,
    )
    if not errors:
        return create_error(
            'unknown-error',
            categories,
            UserMessage(TRANSLATION_CATALOG, _('unknown error')),
        )
    return errors[0]


def create_error(
        identifier: str,
        categories: Iterable[message_helper.ErrorCategoryType],
        message: UserMessage,
        corrective_action_msg: Optional[UserMessage] = None,
        source: Optional[str] = None,
) -> foreman.Error:
    """Create the error object used in error events."""
    corrective_action = create_optional_message(corrective_action_msg)
    return foreman.Error(
        identifier=identifier,
        categories=list(categories),
        source=source,
        corrective_action=corrective_action,
        error_message=create_message(message),
    )


def create_optional_message(message: Optional[UserMessage]) -> Optional[foreman.LocalizableMessage]:
    """Transform a message object into a localizable event value."""
    if not message:
        return None
    return foreman.LocalizableMessage(
        message.catalog,
        message.message,
        [
            foreman.MessageArgument(
                key,
                foreman.MessageArgumentValue(type_name, value)
            )
            for key, type_name, value in message_helper.get_message_arguments(message)
        ],
    )


def create_message(message: UserMessage) -> foreman.LocalizableMessage:
    """Transform a message object into a localizable event value."""
    return not_none(create_optional_message(message))
