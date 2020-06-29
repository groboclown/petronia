
"""
Standard threading.
"""

from typing import Optional, Callable, Union
import threading
from ...base.logging import (
    logerr, ERROR,
)
from ...base.util.pthread import create_loop_thread as mk_lt
from ...base.util.pthread import create_single_pass_thread as mk_spt
from ...base import EventBus
from ...core.shutdown.api import send_system_shutdown_request


def create_single_pass_thread(
        bus: EventBus,
        name: str,
        daemon: bool,
        runner: Callable[[], None],
        error_reporter: Optional[Callable[[BaseException], None]] = None
) -> threading.Thread:
    if not error_reporter:
        error_reporter = _mk_error_reporter(name)
    return mk_spt(name, daemon, runner, error_reporter, _mk_keyboard_listener(bus))


def create_loop_thread(
        bus: EventBus,
        name: str,
        daemon: bool,
        runner: Callable[[], None],
        is_active: Callable[[], bool],
        error_handler: Union[bool, Callable[[BaseException], bool]]
) -> threading.Thread:
    err: Callable[[BaseException], bool]
    if isinstance(error_handler, bool):
        err = _mk_error_handler(name, error_handler)
    else:
        err = error_handler
    return mk_lt(name, daemon, runner, is_active, err, _mk_keyboard_handler(bus))


def _mk_keyboard_listener(bus: EventBus) -> Callable[[], None]:
    def ret() -> None:
        send_system_shutdown_request(bus)
    return ret


def _mk_keyboard_handler(bus: EventBus) -> Callable[[], bool]:
    def ret() -> bool:
        send_system_shutdown_request(bus)
        return True
    return ret


def _mk_error_reporter(name: str) -> Callable[[BaseException], None]:
    def ret(err: BaseException) -> None:
        if _is_reportable_error(err):
            logerr(ERROR, name, err, 'Encountered unexpected problem.')
    return ret


def _mk_error_handler(
        name: str, fail_on_error: bool
) -> Callable[[BaseException], bool]:
    def ret(err: BaseException) -> bool:
        if _is_reportable_error(err):
            logerr(ERROR, name, err, 'Encountered unexpected problem.')
        return fail_on_error
    return ret


def _is_reportable_error(err: BaseException) -> bool:
    return (
        not isinstance(err, SystemExit)
        and not isinstance(err, KeyboardInterrupt)
    )
