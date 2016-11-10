
# Same as `main.py`, but waits for user input.
# Allows for a "graceful" exit if the quit key isn't working.

from petronia.util import worker_thread

import sys


if __name__ == '__main__':
    from . import main
    bus = main.main_setup()

    sys.stdin.read(1)

    worker_thread.stop_all_threads()
    sys.exit(0)
