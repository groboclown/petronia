
"""
Display a message to the user.

As Foreman is the main process that the end-user runs, it needs the
ability to send messages to the user.
"""

import os
import sys
import gettext
import traceback
from petronia_common.util import PetroniaReturnError, I18n, UserMessage, UserMessageData
from petronia_common.util.error import ExceptionPetroniaReturnError
from .configuration.platform import PlatformSettings
from .constants import TRANSLATION_CATALOG

CATALOG = TRANSLATION_CATALOG


def display(catalog: str, message: I18n, **kwargs: UserMessageData) -> None:
    """Display a message."""
    print(translate(catalog, message, **kwargs))


def local_display(message: I18n, **kwargs: UserMessageData) -> None:
    """Display a message using the local catalog."""
    display(CATALOG, message, **kwargs)


def display_message(message: UserMessage) -> None:
    """Display a message.  The catalog of the message is ignored."""
    display(message.catalog, message.message, **message.arguments)


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


def translate(catalog: str, message: I18n, **kwargs: UserMessageData) -> str:
    """Translate the message + data to a string the user can read."""
    return gettext.dgettext(catalog, message).format(**kwargs)


def load_translation(_settings: PlatformSettings) -> None:
    """Use the platform-specific settings to find the translation directory."""
    data_dir = _settings.find_data_dir('translations')
    if not data_dir:
        print("No translations directory found.")
        return
    domain_list_file = os.path.join(data_dir, 'catalog.list')
    if os.path.isfile(domain_list_file):
        with open(domain_list_file, 'r') as f_obj:
            for line in f_obj.readlines():
                gettext.bindtextdomain(line, data_dir)
    else:
        print(f"No file {domain_list_file} found.  Not loading translations.")
