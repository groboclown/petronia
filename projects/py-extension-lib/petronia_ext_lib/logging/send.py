"""Send log events."""

from typing import List
from petronia_common.util import PetroniaReturnError, StdRet, RET_OK_NONE
from ..events import logging
from ..runner import EventRegistryContext
from ..standard.error import create_error_data, ErrorCategoryType


def send_system_error(
        context: EventRegistryContext,
        source_id: str,
        system_error: PetroniaReturnError,
        categories: List[ErrorCategoryType],
        identifier: str,
) -> StdRet[None]:
    """Send a system error log message."""
    error = create_error_data(
        logging.Error,
        logging.LocalizableMessage,
        logging.MessageArgument,
        logging.MessageArgumentValue,
        system_error,
        list(categories),
        identifier,
    )
    if not error:
        return RET_OK_NONE
    return context.send_event(
        source_id,
        logging.SystemErrorEvent.UNIQUE_TARGET_FQN,
        logging.SystemErrorEvent(error),
    )
