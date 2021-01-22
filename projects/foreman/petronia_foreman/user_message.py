
"""
Display a message to the user.

As Foreman is the main process that the end-user runs, it needs the
ability to send messages to the user.
"""

from typing import Dict, Iterable, Optional
import os
import sys
import threading
import gettext
import traceback
from petronia_common.util import PetroniaReturnError, I18n, UserMessage, UserMessageData
from petronia_common.util.error import ExceptionPetroniaReturnError
from .configuration.platform import PlatformSettings
from .constants import TRANSLATION_CATALOG

CATALOG = TRANSLATION_CATALOG

_TRANSLATIONS: Dict[str, gettext.NullTranslations] = {}
_LOCK = threading.RLock()


def low_println(text: str) -> None:
    """Low-level print.  Used for proper output."""
    with _LOCK:
        sys.stdout.write(text + '\n')
        sys.stdout.flush()


def display(catalog: str, message: I18n, **kwargs: UserMessageData) -> None:
    """Display a message."""
    low_println(translate(catalog, message, **kwargs))


def local_display(message: I18n, **kwargs: UserMessageData) -> None:
    """Display a message using the local catalog."""
    display(CATALOG, message, **kwargs)


def display_message(message: UserMessage) -> None:
    """Display a message.  The catalog of the message is ignored."""
    display(message.catalog, message.message, **message.arguments)


def display_error(err: PetroniaReturnError, debug: bool = False) -> None:
    """Display an error"""
    with _LOCK:
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
    if catalog in _TRANSLATIONS:
        return _TRANSLATIONS[catalog].gettext(message).format(**kwargs)
    return message.format(**kwargs)


def load_translation(
        settings: PlatformSettings,
        locale_names: Optional[Iterable[str]] = None,
) -> None:
    """Use the platform-specific settings to find the translation directory.
    The locales are not in the platform on purpose."""
    _TRANSLATIONS.clear()
    data_dir = settings.find_data_dir('translations')
    if not data_dir:
        low_println("No translations directory found.")
        return
    domain_list_file = os.path.join(data_dir, 'catalog.list')
    if os.path.isfile(domain_list_file):
        with open(domain_list_file, 'r') as f_obj:
            for line in f_obj.readlines():
                catalog = line.strip()
                try:
                    translation = gettext.translation(
                        catalog, data_dir, languages=locale_names,
                    )
                    _TRANSLATIONS[catalog] = translation
                except FileNotFoundError:
                    low_println(
                        f"Could not find translation file for {catalog} in {data_dir}"
                        f" ({locale_names and locale_names or 'system locale)'}"
                    )
                    # Keep going.
    else:
        low_println(f"No file {domain_list_file} found.  Not loading translations.")
