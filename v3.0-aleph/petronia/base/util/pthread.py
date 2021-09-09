
"""
Utility for spawning a thread.

Petronia uses threads prevent the dynamic nature of event processing from
blocking the execution.  It also allows for timers.

However, there are many nuances to the way Petronia interacts with the system
in well defined ways that require special attention.
"""

from typing import Callable, Optional
from threading import Thread
from ..logging import (
    log, logerr, TRACE, DEBUG,
)


def create_single_pass_thread(
        name: str,
        daemon: bool,
        runner: Callable[[], None],
        error_reporter: Callable[[BaseException], None],
        keyboard_interrupt_handler: Optional[Callable[[], None]] = None
) -> Thread:
    """
    Creates a thread (which must have `start()` called to start it).
    It will run the `runner` once then exit.
    """
    def callback() -> None:
        try:
            runner()
        except KeyboardInterrupt as err:
            if keyboard_interrupt_handler:
                keyboard_interrupt_handler()
            else:
                error_reporter(err)
        except SystemExit:
            # Exit immediately.
            pass
        except BaseException as err:  # pylint: disable=broad-except
            error_reporter(err)
    return Thread(name=name, daemon=daemon, target=callback)


def create_loop_thread(
        name: str,
        daemon: bool,
        runner: Callable[[], None],
        is_active: Callable[[], bool],
        error_handler: Callable[[BaseException], bool],
        keyboard_interrupt_handler: Optional[Callable[[], bool]] = None
) -> Thread:
    """
    Executes the `runner` inside a loop until one of several conditions
    happens:
        * The `is_active` call returns False
        * A SystemExit happens.
        * A KeyboardInterrupt happens, and `keyboard_interrupt_handler` returns True.
        * Some other exception happens, and the `error_handler` returns True for that error.
    """
    def callback() -> None:
        log(DEBUG, create_loop_thread, "Start thread {0}", name)
        while is_active():
            log(TRACE, create_loop_thread, "Running thread {0}", name)
            try:
                runner()
            except KeyboardInterrupt as err:
                log(DEBUG, create_loop_thread, "Ctrl-C in thread {0}", name)
                if keyboard_interrupt_handler:
                    if keyboard_interrupt_handler():
                        log(TRACE, create_loop_thread, "... which caused the loop to exit.")
                        return
                elif error_handler(err):
                    log(TRACE, create_loop_thread, "... which caused the loop to exit (from error handler).")
                    return
            except SystemExit:
                # Exit immediately.
                log(DEBUG, create_loop_thread, "System exit for thread {0}", name)
                return
            except BaseException as err:  # pylint: disable=broad-except
                logerr(DEBUG, create_loop_thread, err, "Error in thread {0}", name)
                if error_handler(err):
                    log(TRACE, create_loop_thread, "... which caused the loop to exit")
                    return
    return Thread(name=name, daemon=daemon, target=callback)
