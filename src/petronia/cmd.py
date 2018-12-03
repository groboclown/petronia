
# Same as `main.py`, but waits for user input.
# Allows for a "graceful" exit if the quit key isn't working.

from petronia.util import worker_thread

import sys

def start(arguments=None):
    from petronia import main
    bus = main.main_setup(arguments)


def stop():
    worker_thread.stop_all_threads()
    sys.exit(0)


def start_wait_stop(arguments):
    start(arguments)
    sys.stdin.read(1)
    stop()


if __name__ == '__main__':
    start_wait_stop(sys.argv)
