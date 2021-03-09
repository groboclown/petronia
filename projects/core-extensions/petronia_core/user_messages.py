"""User message helpers."""

from typing import Any
import sys
import traceback
from petronia_common.util import StdRet
from petronia_common.util.error import ExceptionPetroniaReturnError

TRANSLATION_CATALOG = 'petronia_core'


def report_send_receive_problems(extension: str, res: StdRet[Any]) -> None:
    """Report a problem on send / receive.  These can't be sent via normal
    error logging by the nature of them, and we don't want to just throw away
    the error.

    This can be called as a wrapper around calls that send or receive.  It will handle
    possible problems in a "nice" way."""

    # Lock isn't used, because this is expected to already be within a lock.

    if res.has_error:
        sys.stderr.write('\n'.join([
            f'[{extension} ERROR] {m.debug()}'
            for m in res.error_messages()
        ]) + '\n')
        problem = res.error
        if isinstance(problem, ExceptionPetroniaReturnError):
            traceback.print_exception(
                type(problem.exception()), problem.exception(), problem.exception().__traceback__,
                file=sys.stderr,
            )
