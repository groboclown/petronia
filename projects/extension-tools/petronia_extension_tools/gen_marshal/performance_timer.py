"""Performs timing for performance purposes."""

import time


class PerfTimer:
    """A simple, reusable timer."""
    __slots__ = ('__start',)

    def __init__(self) -> None:
        self.__start = time.time()

    def start(self) -> None:
        """Restart the timer."""
        self.__start = time.time()

    def report(self, source: str) -> None:
        """Report the time usage.  Also, restarts the timer."""
        now = time.time()
        print(f"[performance] {source} {now - self.__start}")
        self.start()
