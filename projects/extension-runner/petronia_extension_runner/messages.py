"""
Handle error messages.
"""

from typing import Optional
import sys
import threading
import traceback
from petronia_common.util import StdRet, T
from petronia_common.util.error import ExceptionPetroniaReturnError

_PRINT_LOCK = threading.RLock()


def low_println(text: str) -> None:
    """Print text to the console in a safe way."""
    with _PRINT_LOCK:
        sys.stdout.write(text + '\n')
        sys.stdout.flush()


def display_message(res: StdRet[T], message: Optional[str] = None) -> None:
    """Display the messages in the error."""
    with _PRINT_LOCK:
        if message:
            low_println(message)
        for msg in res.error_messages():
            low_println(msg.debug())
        err = res.error
        if isinstance(err, ExceptionPetroniaReturnError):
            traceback.print_exception(
                type(err.exception()), err.exception(), err.exception().__traceback__,
            )
