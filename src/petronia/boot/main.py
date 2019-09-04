
"""
The main execution for Petronia.
"""

from typing import Sequence
import threading
from traceback import print_exception
from .bootstrap.args import parse_args
from .bootstrap.all import bootstrap_petronia, run_petronia


def main(args: Sequence[str]) -> int:
    """
    Entry for the program.
    """
    try:
        user_args = parse_args(args)
        bus = bootstrap_petronia(user_args)
        return run_petronia(bus, user_args)
    except BaseException as err: # pylint: disable=broad-except
        print_exception(err.__class__, err, err.__traceback__)
        from ..base.util.worker_thread import stop_all_threads
        stop_all_threads()
        for thread in threading.enumerate():
            if thread != threading.current_thread() and thread.isAlive():
                print("Thread {0} still alive".format(thread.name))
        print("Exiting Petronia with error.")
        return 1
