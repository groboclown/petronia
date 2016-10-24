
from petronia.util.rwlock import RWLock
import threading
import queue
import traceback


_STOP_THREAD_NOTICE = "STOP"
_RUNNING_THREAD_QUEUES = []


def stop_all_threads():
    # Create a copy of the queues, so we don't get
    # into a weird state mid-processing
    for q in list(_RUNNING_THREAD_QUEUES):
        q.put_nowait(_STOP_THREAD_NOTICE)


class WorkerThread(object):
    def __init__(self, cid, daemon=True):
        self.__thread = threading.Thread(
            target=lambda: self._run(),
            daemon=daemon
        )
        self.__thread.name = "Worker {0}".format(cid)
        self.__state = 0
        self.__q = queue.Queue()
        self.__state_lock = RWLock()
        self.__thread.start()

    def queue(self, obj):
        if isinstance(obj, dict) and 'op' in obj and callable(obj['op']):
            if 'vargs' not in obj:
                obj['vargs'] = []
            elif not (isinstance(obj['vargs'], list) or isinstance(obj['vargs'], tuple)):
                obj['vargs'] = []
            if 'kargs' not in obj:
                obj['kargs'] = {}
            elif not isinstance(obj['kargs'], dict):
                obj['kargs'] = {}
            self.__q.put_nowait(obj)
            return True
        return False

    def stop(self, timeout=None):
        if threading.current_thread() == self.__thread:
            self.close()
        else:
            return self.__thread.join(timeout)

    def close(self):
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
                if self.__state != 0:
                    # TODO correct exception
                    raise Exception("Already started")
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
                    except BaseException as e:
                        # TODO log the error better
                        print("<<ERROR Worker Thread action failed: {0}>>".format(e))
                        traceback.print_exc(e)
        finally:
            # No lock on this, because it's not a read then write.
            self.__state = 3
            if self.__q in _RUNNING_THREAD_QUEUES:
                _RUNNING_THREAD_QUEUES.remove(self.__q)
