
"""
The primary timeout object.
"""

import time
from typing import Callable, Optional
from threading import Thread
from ...base.util import ValueHolder


def timeout_after(
        timeout_seconds: float,
        callback: ValueHolder[Callable[[], None]],
        sleep_call: Optional[Callable[[float], None]] = None
) -> None:
    """
    Launches a thread that will trigger the timeout call, only if the
    callback is still set.
    """
    sleeper: Callable[[float], None]
    if sleep_call:
        sleeper = sleep_call
    else:
        sleeper = time.sleep
    def runner() -> None:
        sleeper(timeout_seconds)
        to_call = callback.value
        if to_call:
            to_call()

    Thread(
        name='timeout after {0}'.format(timeout_seconds),
        daemon=True,
        target=runner
    ).start()
