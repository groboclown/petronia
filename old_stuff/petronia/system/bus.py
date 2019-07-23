
from collections import defaultdict

import datetime
import weakref

from . import event_ids
from . import target_ids
from ..util.worker_thread import WorkerThread
from ..util.rwlock import RWLock
import traceback


# TODO: "now" should be two different workers; "same"
# should mean run in the current worker, but at the end, and "now"
# should mean run right now, and don't be put in a queue.


# Note: explicitly not a "component" to prevent madness.
# Internal logging through the LOG events is unusable because of the
# chance for infinite recursion.
class Bus(object):
    """
    Simple message bus.  Keeps the connection between components
    loose.
    """

    def __init__(self, worker_factory=WorkerThread):
        self.__listeners = defaultdict(weakref.WeakSet)
        self.__listener_lock = RWLock()

        self.__workers = {}
        for worker_name in event_ids.EVENT_THREAD_NAMES:
            if worker_name != event_ids.EVENT_THREAD__NOW:
                self.__workers[worker_name] = worker_factory(worker_name)

    def add_listener(self, event_id, target_id, callback):
        """
        Note that each callback is registered exactly once
        internally, so a remove will remove it, even if the
        listener was added multiple times.

        If the callback ever leaves scope and is cleaned up,
        it will no longer receive listen events, due to the
        callback being stored in a weak reference in the bus.

        :param event_id:
        :param target_id:
        :param callback: callback takes 3 arguments: event id, target, event object.
        :return:
        """
        assert callback is not None and callable(callback)
        assert isinstance(event_id, str)
        assert isinstance(target_id, str)

        self.fire(event_ids.BUS__LISTENER_ADDED, target_ids.BROADCAST, {
            'listen-event_id': event_id,
            'listen-target_id': target_id,
        })

        key = self.__event_target_key(event_id, target_id)

        self.__listener_lock.acquire_write()
        try:
            self.__listeners[key].add(callback)
        finally:
            self.__listener_lock.release()

    def remove_listener(self, event_id, target_id, callback):
        key = self.__event_target_key(event_id, target_id)
        self.__listener_lock.acquire_write()
        try:
            event_listeners = self.__listeners[key]
            try:
                event_listeners.remove(callback)
            except KeyError:
                # can happen even if the callback seems to be in the list,
                # but isn't any longer due to a weak reference.
                pass
        finally:
            self.__listener_lock.release()
        self.fire(event_ids.BUS__LISTENER_REMOVED, target_ids.BROADCAST, {})

    def fire(self, event_id, target_id, event_obj):
        if event_id in event_ids.EVENT_ID_TO_THREAD:
            worker_name = event_ids.EVENT_ID_TO_THREAD[event_id]
            if worker_name == event_ids.EVENT_THREAD__NOW:
                self.__fire_now(event_id, target_id, event_obj)
            else:
                self.__fire_later(
                    self.__workers[event_ids.EVENT_ID_TO_THREAD[event_id]], event_id, target_id, event_obj)
        else:
            print("<<BUS ERROR invalid event id {0}>>".format(event_id))
            # This can causes recursion!
            # self.fire(event_ids.LOG__ERROR, target_ids.ANY, {"message": "invalid event id {0}".format(event_id)})

    def __fire_later(self, worker, event_id, target_id, event_obj):
        self.__normalize_event(event_id, target_id, event_obj)
        listeners = self.__get_listeners_for(event_id, target_id)

        # Add in the extra event information for possible queue compacting
        if not worker.queue({
            'op': lambda: _fire_listeners(listeners, event_id, target_id, event_obj),
            'event_id': event_id,
            'target_id': target_id,
            'event_obj': event_obj
        }):
            print("<<BUS ERROR: Not a valid event object {0}>>".format(event_obj))

    def __fire_now(self, event_id, target_id, event_obj):
        event_obj = self.__normalize_event(event_id, target_id, event_obj)
        _fire_listeners(self.__get_listeners_for(event_id, target_id), event_id, target_id, event_obj)

    @staticmethod
    def __normalize_event(event_id, target_id, event_obj):
        assert isinstance(event_id, str), "event_id not a str: {0}".format(event_id)
        assert isinstance(target_id, str), "target_id not a str: {0}".format(target_id)
        assert isinstance(event_obj, dict), "event_obj not a dict: {0} ({1})".format(event_obj, type(event_obj))

        # Make a copy of the event object.  This is for safety, as some things
        # may directly pass the parent event object here, and this would unfortunately
        # alter that event object before other listeners can use it.
        ret = dict(event_obj)
        ret['target_id'] = target_id
        ret['event_id'] = event_id
        ret['when'] = datetime.datetime.now()
        return ret

    def __get_listeners_for(self, event_id, target_id):
        # Use a set of keys to invisibly remove duplicates.
        keys = {
            self.__event_target_key(event_id, target_id),
            self.__event_target_key(event_ids.ALL, target_id),
            self.__event_target_key(event_id, target_ids.BROADCAST),
            self.__event_target_key(event_ids.ALL, target_ids.BROADCAST),
        }

        ret = set()
        self.__listener_lock.acquire_read()
        try:
            for key in keys:
                event_listeners = self.__listeners[key]
                ret.update(event_listeners)
        finally:
            self.__listener_lock.release()
        return ret

    @staticmethod
    def __event_target_key(event_id, target_id):
        return event_id + chr(2) + target_id


def _fire_listeners(listeners, event_id, target_id, event_obj):
    for listener in listeners:
        try:
            listener(event_id, target_id, event_obj)
        except BaseException as e:
            print("<<EVENT ERROR: ({0}) Failed to run listener {1}: {2} ({3})>>".format(event_id, listener, e, type(e)))
            traceback.print_exc()
            # Gulp!
        except:
            print("<<EVENT ERROR: ({0}) Failed to run listener {0}>>".format(event_id, listener))
            traceback.print_exc()
            raise


class SingleThreadedBus(Bus):
    """
    Used for unit testing.
    """
    def __init__(self):
        Bus.__init__(self, NonThreadedWorker)


class NonThreadedWorker(object):
    def __init__(self, name):
        pass

    # noinspection PyMethodMayBeStatic
    def queue(self, action):
        if isinstance(action, dict) and 'op' in action and callable(action['op']):
            if 'vargs' not in action:
                action['vargs'] = []
            elif not (isinstance(action['vargs'], list) or isinstance(action['vargs'], tuple)):
                action['vargs'] = []
            if 'kargs' not in action:
                action['kargs'] = {}
            elif not isinstance(action['kargs'], dict):
                action['kargs'] = {}
        action['op'](*action['vargs'], **action['kargs'])
        return True

    def stop(self):
        pass
