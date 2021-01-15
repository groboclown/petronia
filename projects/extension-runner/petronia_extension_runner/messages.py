"""
Handle error messages.
"""

from typing import Optional
import traceback
from petronia_common.util import StdRet, T
from petronia_common.util.error import ExceptionPetroniaReturnError


def display_message(res: StdRet[T], message: Optional[str] = None) -> None:
    """Display the messages in the error."""
    if message:
        print(message)
    for msg in res.error_messages():
        print(msg.debug())
    err = res.error
    if isinstance(err, ExceptionPetroniaReturnError):
        traceback.print_exception(
            type(err.exception()), err.exception(), err.exception().__traceback__,
        )
