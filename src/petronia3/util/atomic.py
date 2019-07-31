
"""
Lock-safe wrappers around basic operations.
"""

from threading import Lock

class AtomicInt:
    """A thread-safe counter."""
    __slots__ = ('__counter', '__lock',)
    def __init__(self, start: int = 0):
        self.__counter = start
        self.__lock = Lock()

    def get_then_incr(self, increase: int = 1) -> int:
        """Return the current value, and increment the internal value."""
        with self.__lock:
            ret = self.__counter
            self.__counter += increase
        return ret

    def incr_then_get(self, increase: int = 1) -> int:
        """Increment the internal value, and return that updated value."""
        with self.__lock:
            self.__counter += increase
            ret = self.__counter
        return ret
