
from typing import List, Callable, Optional, Generic
from threading import Lock
from .std import create_loop_thread
from ...base.bus import EventBus
from ...base.errors import PetroniaLockTimeoutError
from ...base.util.memory import T


class ThreadedExecutor(Generic[T]):
    """
    Maintains a list of items to run, in order, inside a separate thread.
    The execution runs a registered callback, which is called over each item
    added.  The execution is guaranteed to be single threaded for each item
    added.

    You should add the call to `stop()` in the shutdown handler.
    """
    __slots__ = ('_queue', '__thread', '__active', '__lock', '__timeout', '__callback', '__drain')
    _queue: List[T]

    def __init__(
            self,
            bus: EventBus,
            name: str,
            daemon: bool,
            callback: Callable[[T], None],
            error_handler: Callable[[BaseException], bool],
            poll_timeout_seconds: float = 0.5
    ) -> None:
        self._queue = []
        self.__lock = Lock()
        self.__active = True
        self.__drain = False
        self.__timeout = poll_timeout_seconds
        self.__callback = callback
        self.__thread = create_loop_thread(
            bus, name, daemon,
            self._check_queue,
            self.is_active,
            error_handler
        )
        self.__thread.start()

    def is_active(self) -> bool:
        """Active state means that a request to stop has not yet been called."""
        return self.__active

    def is_alive(self) -> bool:
        """Alive state means that the underlying thread is still running."""
        return self.__thread.is_alive()

    def is_draining(self) -> bool:
        """Draining state means that the queue is no longer accepting more
        items, and will stop when the list of remaining items has emptied."""
        return self.__active and self.__drain

    def begin_drain(self) -> None:
        """Starts the draining.  After this, no more items will be added."""
        self.__drain = True

    def stop(self, timeout_wait: Optional[float]) -> bool:
        """Signal the looping thread to stop, and return True if the thread is stopped.
        Use a negative timeout to not join with the thread."""
        self.__active = False
        if not self.__thread.is_alive():
            return True
        if timeout_wait is None or timeout_wait > 0:
            self.__thread.join(timeout_wait)
        return not self.__thread.is_alive()

    def add_execution(self, handled_item: T, timeout: Optional[float] = None) -> None:
        """
        Add a new item to the queue for execution.  If the timeout occurs
        while waiting for the opportunity to add the item to the queue,
        then a PetroniaLockTimeoutError occurs.  If the timeout is None,
        then the internal executor timeout is used.
        """
        if not self.__active:
            raise RuntimeError('called add_execution after stop')
        if self.__drain:
            raise RuntimeError('called add_execution after begin_drain')
        if timeout is None:
            timeout = self.__timeout
        if not self.__lock.acquire(timeout=timeout):
            raise PetroniaLockTimeoutError()
        try:
            self._queue.append(handled_item)
        finally:
            self.__lock.release()

    def _check_queue(self) -> None:
        if not self.__active:
            return

        next_item: List[T] = []

        if not self.__lock.acquire(timeout=self.__timeout):
            return
        try:
            if len(self._queue) > 0:
                next_item.append(self._queue[0])
                self._queue = self._queue[1:]
            if self.__drain and len(self._queue) <= 0:
                self.__active = False
        finally:
            self.__lock.release()

        if next_item:
            self.__callback(next_item[0])
