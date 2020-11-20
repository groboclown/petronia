
"""
Display a message to the user.

As Foreman is the main process that the end-user runs, it needs the
ability to send messages to the user.
"""

import sys
import gettext
import traceback
from petronia_common.util import PetroniaReturnError, I18n, UserMessage, UserMessageData
from petronia_common.util.error import ExceptionPetroniaReturnError
from .configuration.platform import PlatformSettings
from .constants import TRANSLATION_CATALOG

CATALOG = TRANSLATION_CATALOG


def display(message: I18n, **kwargs: UserMessageData) -> None:
    """Display a message."""
    print(translate(message, **kwargs))


def display_message(message: UserMessage) -> None:
    """Display a message.  The catalog of the message is ignored."""
    display(message.message, **message.arguments)


def display_error(err: PetroniaReturnError, debug: bool = False) -> None:
    """Display an error"""
    for message in err.messages():
        display_message(message)
    if debug and isinstance(err, ExceptionPetroniaReturnError):
        exception = err.exception()
        traceback.print_exception(
            type(exception),
            exception,
            exception.__traceback__,
            file=sys.stdout,
        )


def translate(message: I18n, **kwargs: UserMessageData) -> str:
    """Translate the message + data to a string the user can read."""
    return gettext.dgettext('messages', message).format(**kwargs)


def load_translation(_settings: PlatformSettings) -> None:
    """Use the platform-specific settings to find the translation directory."""
    raise NotImplementedError()
