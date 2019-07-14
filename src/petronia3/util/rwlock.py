"""Simple reader-writer locks in Python
Many readers can hold the lock XOR one and only one writer.

Source: https://majid.info/blog/a-reader-writer-lock-for-python/
License: public domain.
"""
from typing import Optional
import threading
from ..errors import PetroniaLockTimeoutError

# version = """$Id: rwlock.py,v 1.1 2004/12/22 22:32:00 majid Exp $"""

DEFAULT_TIMEOUT = 30

class RWLock:
    """
    A simple reader-writer lock Several readers can hold the lock
    simultaneously, XOR one writer. Write locks have priority over reads to
    prevent write starvation.
    """

    __timeout: float

    def __init__(self, timeout: Optional[float] = DEFAULT_TIMEOUT) -> None:
        self.__rwlock = 0
        self.__writers_waiting = 0
        self.__monitor = threading.Lock()
        self.__readers_ok = threading.Condition(self.__monitor)
        self.__writers_ok = threading.Condition(self.__monitor)
        self.__timeout = timeout or DEFAULT_TIMEOUT

    def acquire_read(self) -> None:
        """Acquire a read lock. Several threads can hold this typeof lock.
        It is exclusive with write locks."""
        if not self.__monitor.acquire(timeout=self.__timeout):
            raise PetroniaLockTimeoutError()
        while self.__rwlock < 0 or self.__writers_waiting:
            self.__readers_ok.wait()
        self.__rwlock += 1
        self.__monitor.release()

    def acquire_write(self) -> None:
        """Acquire a write lock. Only one thread can hold this lock, and
        only when no read locks are also held."""
        if not self.__monitor.acquire(timeout=self.__timeout):
            raise PetroniaLockTimeoutError()
        while self.__rwlock != 0:
            self.__writers_waiting += 1
            self.__writers_ok.wait()
            self.__writers_waiting -= 1
        self.__rwlock = -1
        self.__monitor.release()

    def promote(self) -> None:
        """Promote an already-acquired read lock to a write lock
        WARNING: it is very easy to deadlock with this method"""
        if not self.__monitor.acquire(timeout=self.__timeout):
            raise PetroniaLockTimeoutError()
        self.__rwlock -= 1
        while self.__rwlock != 0:
            self.__writers_waiting += 1
            self.__writers_ok.wait()
            self.__writers_waiting -= 1
        self.__rwlock = -1
        self.__monitor.release()

    def demote(self) -> None:
        """Demote an already-acquired write lock to a read lock"""
        if not self.__monitor.acquire(timeout=self.__timeout):
            raise PetroniaLockTimeoutError()
        self.__rwlock = 1
        self.__readers_ok.notifyAll()
        self.__monitor.release()

    def release(self) -> None:
        """Release a lock, whether read or write."""
        if not self.__monitor.acquire(timeout=self.__timeout):
            raise PetroniaLockTimeoutError()
        if self.__rwlock < 0:
            self.__rwlock = 0
        else:
            self.__rwlock -= 1
        wake_writers = self.__writers_waiting and self.__rwlock == 0
        wake_readers = self.__writers_waiting == 0
        self.__monitor.release()
        if wake_writers:
            self.__writers_ok.acquire()
            self.__writers_ok.notify()
            self.__writers_ok.release()
        elif wake_readers:
            self.__readers_ok.acquire()
            self.__readers_ok.notifyAll()
            self.__readers_ok.release()
