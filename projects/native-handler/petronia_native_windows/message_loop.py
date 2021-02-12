"""
The handler for the Windows message loop.

This code must strictly follow the guidelines of
https://docs.microsoft.com/en-us/windows/win32/winmsg/using-messages-and-message-queues

This code is also designed to be testable.
"""

from typing import Optional
import threading

# The code has a global constant for maintaining the running loops.  At shutdown time,
# they must all be cleaned up correctly.

THREAD_STATE__NOT_STARTED = 0
THREAD_STATE__THREAD_INITIALIZING = 1
THREAD_STATE__THREAD_STARTED = 2
THREAD_STATE__THREAD_LOOPING = 3
THREAD_STATE__THREAD_STOPPING = 4
THREAD_STATE__THREAD_STOPPED = 5


class MessageLoopThreadData:
    """All the data associated with a running message loop thread."""
    __slots__ = ('_thread', '_state', '_lock')

    def __init__(self) -> None:
        self._lock = threading.RLock()
        self._thread: Optional[threading.Thread] = None
