"""User message helpers."""

from typing import Optional, Any
import sys
import traceback
import threading
from petronia_common.util import StdRet
from petronia_common.util.error import ExceptionPetroniaReturnError

TRANSLATION_CATALOG = 'petronia_native'

_PRINT_LOCK = threading.RLock()


def report_send_receive_problems(res: StdRet[Any]) -> None:
    """Report a problem on send / receive.  These can't be sent via normal
    error logging by the nature of them, and we don't want to just throw away
    the error.

    This can be called as a wrapper around calls that send or receive.  It will handle
    possible problems in a "nice" way."""

    # Lock isn't used, because this is expected to already be within a lock.

    if res.has_error:
        sys.stderr.write('\n'.join([
            f'[native-handler ERROR] {m.debug()}'
            for m in res.error_messages()
        ]) + '\n')
        problem = res.error
        if isinstance(problem, ExceptionPetroniaReturnError):
            traceback.print_exception(
                type(problem.exception()), problem.exception(), problem.exception().__traceback__,
                file=sys.stderr,
            )


def low_println(text: str) -> None:
    """Print text to the console in a safe way."""
    with _PRINT_LOCK:
        sys.stdout.write(text + '\n')
        sys.stdout.flush()


def low_traceback(err: BaseException) -> None:
    """Print a traceback in a safe way."""
    with _PRINT_LOCK:
        traceback.print_exception(type(err), err, err.__traceback__, file=sys.stdout)


def display_message(res: StdRet[Any], message: Optional[str] = None) -> None:
    """Display the messages in the error."""
    with _PRINT_LOCK:
        if message:
            low_println(message)
        for msg in res.error_messages():
            low_println(msg.debug())
        err = res.error
        if isinstance(err, ExceptionPetroniaReturnError):
            low_traceback(err.exception())
