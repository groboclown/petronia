
"""
Worker Threads
"""

from typing import List, Optional, Any, Dict, Callable
import threading
import queue
import traceback
from .rwlock import RWLock
#from ..validation import assert_state
from .memory import EMPTY_DICT, EMPTY_LIST


def stop_all_threads() -> None:
    """
    Stop all worker threads.
    """
    # Create a copy of the queues, so we don't get
    # into a weird state mid-processing
    for qqq in list(_RUNNING_THREAD_QUEUES):
        qqq.put_nowait(_STOP_ACTION)


ErrorHandler = Callable[[str, BaseException], None]


class _WorkAction:
    """Small holder for worker actions."""
    __slots__ = ('opr', 'vargs', 'kvargs')
    def __init__(
            self,
            opr: Optional[Callable],
            vargs: List[Any], kvargs: Dict[str, Any]
    ) -> None:
        self.opr = opr
        self.vargs = vargs
        self.kvargs = kvargs

    def run(self) -> bool:
        """Run the operation."""
        if self.opr is None:
            return False
        else:
            self.opr(*self.vargs, **self.kvargs)
            return True


class WorkerThread:
    """
    The worker thread class.  Creating a worker thread automatically registers it
    to the global set of threads.
    """

    # Should be subscript [_WorkAction], but this causes a runtime error
    # ('type' object is not subscriptable)
    __q: queue.Queue # type: ignore
    __error_handler: ErrorHandler

    def __init__(
            self,
            cid: str, daemon: bool = False,
            error_handler: Optional[ErrorHandler] = None
    ) -> None:
        assert error_handler is None or callable(error_handler)
        self.__thread = threading.Thread(
            target=lambda: self._run(), # pylint: disable=unnecessary-lambda
            daemon=daemon
        )
        self.__cid = cid
        self.__thread.name = "Worker {0}".format(cid)

        # ignored type: see mypy #708
        self.__error_handler = error_handler or default_error_handler # type: ignore

        self.__state = 0
        self.__q = queue.Queue()
        self.__state_lock = RWLock()
        self.__thread.start()

    def queue(
            self,
            callback: Callable, # type: ignore
            vargs: Optional[List[Any]] = None, kargs: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        Adds an item to the end of the worker's queue.  It does not inspect the state of the
        worker thread, so if the worker is stopped in any way, this will be silently ignored.

        :param callback Function: callable function, invoked when the worker gets to it.
        """
        assert callable(callback)
        self.__q.put_nowait(_WorkAction(
            callback, vargs or EMPTY_LIST, kargs or EMPTY_DICT
        ))

    def join(self, timeout: Optional[float] = None) -> None:
        """
        Waits for the worker thread to stop running, up to the timeout, regardless of the
        state of the worker.

        :param timeout: seconds to timeout waiting for the worker thread to finish.
        """
        self.__thread.join(timeout)

    def complete(self) -> None:
        """
        Sends a signal to the worker thread to stop running after the queue is finished.
        Any additional items added to the queue after this point will be silently ignored.
        """
        self.__q.put_nowait(_STOP_ACTION)

    def close(self) -> None:
        """
        Signal the worker thread to stop listening to its queue, and turn off access to
        the queue.  The worker will NOT complete pending items in the queue.
        """
        self.__state_lock.acquire_read()
        try:
            if self.__state < 2:
                self.__state_lock.promote()
                self.__state = 2
                # Force the queue to wake up
                self.__q.put_nowait(_NOOP_ACTION)
        finally:
            self.__state_lock.release()

    def _run(self) -> None:
        total = 0
        _RUNNING_THREAD_QUEUES.append(self.__q)
        try:
            self.__state_lock.acquire_read()
            try:
                if self.__state != 0:
                    raise Exception('thread should be in not-started state')
                self.__state_lock.promote()
                self.__state = 1
            finally:
                self.__state_lock.release()

            while True:
                # Check the state at the loop start.
                self.__state_lock.acquire_read()
                try:
                    if self.__state >= 2:
                        break
                finally:
                    self.__state_lock.release()
                action: _WorkAction = self.__q.get()
                try:
                    total += 1
                    if not action.run():
                        self.close()
                except BaseException as err: # pylint: disable=broad-except
                    # See mypy #702
                    self.__error_handler(self.__cid, err) # type: ignore
        finally:
            # No lock on this, because it's not a read then write.
            self.__state = 3
            if self.__q in _RUNNING_THREAD_QUEUES:
                _RUNNING_THREAD_QUEUES.remove(self.__q)


def default_error_handler(cid: str, err: BaseException) -> None:
    """
    Default error handler.  Just prints the problem to the console.
    """
    print("<<ERROR Worker Thread {0} action failed: {1}>>".format(cid, err))
    traceback.print_exception(etype=type(err), value=err, tb=err.__traceback__)

# [_WorkAction]
_RUNNING_THREAD_QUEUES: List[queue.Queue] = []
_STOP_ACTION = _WorkAction(None, EMPTY_LIST, EMPTY_DICT) # type: ignore
_NOOP_ACTION = _WorkAction(lambda: 0, EMPTY_LIST, EMPTY_DICT) # type: ignore
