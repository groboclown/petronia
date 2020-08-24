
"""
Display a message to the user.
"""

from typing import List
import gettext
from .configuration.platform import PlatformSettings
from petronia_common.util import PetroniaReturnError, I18n, UserMessage, UserMessageData


def display(message: I18n, **kwargs: UserMessageData) -> None:
    """Display a message."""
    print(translate(message, **kwargs))


def display_message(message: UserMessage) -> None:
    """Display a message."""
    display(message.message, **message.arguments)


def display_error(err: PetroniaReturnError) -> None:
    """Display an error"""
    for message in err.messages():
        display_message(message)


def translate(message: I18n, **kwargs: UserMessageData) -> str:
    """Translate the message + data to a string the user can read."""
    return gettext.dgettext('messages', message).format(**kwargs)


def load_translation(settings: PlatformSettings) -> None:
    """Use the platform-specific settings to find the translation directory."""
