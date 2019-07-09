"""
Worker Threads
"""

import threading
import queue
import traceback
from .rwlock import RWLock
from ..errors import assert_state

_STOP_THREAD_NOTICE = "STOP"
_RUNNING_THREAD_QUEUES = []

def stop_all_threads():
    """
    Stop all worker threads.
    """
    # Create a copy of the queues, so we don't get
    # into a weird state mid-processing
    for qqq in list(_RUNNING_THREAD_QUEUES):
        qqq.put_nowait(_STOP_THREAD_NOTICE)


class WorkerThread:
    """
    The worker thread class.  Creating a worker thread automatically registers it
    to the global set of threads.
    """
    def __init__(self, cid: str, daemon: bool = False, error_handler=None):
        assert error_handler is None or callable(error_handler)
        self.__thread = threading.Thread(
            target=lambda: self._run(), # pylint: disable=unnecessary-lambda
            daemon=daemon
        )
        self.__cid = cid
        self.__thread.name = "Worker {0}".format(cid)
        self.__error_handler = error_handler or default_error_handler
        self.__state = 0
        self.__q = queue.Queue()
        self.__state_lock = RWLock()
        self.__thread.start()

    def queue(self, callback, vargs: list or tuple or None = None, kargs: dict or None = None):
        """
        Adds an item to the end of the worker's queue.  It does not inspect the state of the
        worker thread, so if the worker is stopped in any way, this will be silently ignored.

        :param callback Function: callable function, invoked when the worker gets to it.
        """
        if not callable(callback):
            return False
        self.__q.put_nowait({
            'op': callback,
            'vargs': vargs or [],
            'kargs': kargs or {},
        })
        return True

    def join(self, timeout: float or int or None = None):
        """
        Waits for the worker thread to stop running, up to the timeout, regardless of the
        state of the worker.

        :param timeout: seconds to timeout waiting for the worker thread to finish.
        """
        self.__thread.join(timeout)

    def complete(self):
        """
        Sends a signal to the worker thread to stop running after the queue is finished.
        Any additional items added to the queue after this point will be silently ignored.
        """
        self.__q.put_nowait(_STOP_THREAD_NOTICE)

    def close(self):
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
                self.__q.put_nowait({'op': lambda: 0, 'vargs': [], 'kargs': {}})
        finally:
            self.__state_lock.release()

    def _run(self):
        total = 0
        _RUNNING_THREAD_QUEUES.append(self.__q)
        try:
            self.__state_lock.acquire_read()
            try:
                assert_state(
                    self.__state == 0,
                    'WorkerThread',
                    'thread should not be started'
                )
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
                action = self.__q.get()
                if action == _STOP_THREAD_NOTICE:
                    self.close()
                elif action is not None:
                    try:
                        total += 1
                        action['op'](*action['vargs'], **action['kargs'])
                    except BaseException as err: # pylint: disable=broad-except
                        self.__error_handler(self.__cid, err)
        finally:
            # No lock on this, because it's not a read then write.
            self.__state = 3
            if self.__q in _RUNNING_THREAD_QUEUES:
                _RUNNING_THREAD_QUEUES.remove(self.__q)


def default_error_handler(cid: str, err: Exception):
    """
    Default error handler.  Just prints the problem to the console.
    """
    print("<<ERROR Worker Thread {0} action failed: {1}>>".format(cid, err))
    traceback.print_exception(err, err, err)
