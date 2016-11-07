
from . import event_ids
from . import target_ids
from .bus import Bus
from .marshalable import Marshalable
import weakref
import atexit


class Component(object):
    """
    A component that interacts in the shell.
    """

    def __init__(self, bus):
        assert isinstance(bus, Bus)
        self.__bus = bus
        self.__listeners = []
        weakref.finalize(self, _cleanup_listeners, self.__bus, self.__listeners)
        atexit.register(self.close)

        self._listen(event_ids.SYSTEM__QUIT, target_ids.ANY, self.__on_close)

    def close(self):
        self._remove_all_listeners()
        self._log_verbose("closed component {0}".format(self))

    def _listen(self, event_id, target_id, callback):
        # TODO There is weirdness here - registering the same callback
        # for different events causes the previous ones to be unregistered.
        """

        :param event_id:
        :param target_id:
        :param callback:
        :return:
        """
        self.__listeners.append((event_id, target_id, callback))
        self.__bus.add_listener(event_id, target_id, callback)

    def _remove_listener(self, event_id, target_id, callback):
        self.__bus.remove_listener(event_id, target_id, callback)
        for i in range(len(self.__listeners)):
            eid, tid, value = self.__listeners[i]
            if eid == event_id and tid == target_id and value == callback:
                del self.__listeners[i]
                return

    def _remove_all_listeners(self):
        _cleanup_listeners(self.__bus, self.__listeners)

    def _fire(self, event_id, target_id, event_obj):
        self.__bus.fire(event_id, target_id, event_obj)

    def _log_debug(self, message, exception=None):
        self._log(event_ids.LOG__DEBUG, message, exception)

    def _log_verbose(self, message, exception=None):
        self._log(event_ids.LOG__VERBOSE, message, exception)

    def _log_info(self, message, exception=None):
        self._log(event_ids.LOG__INFO, message, exception)

    def _log_warn(self, message, exception=None):
        self._log(event_ids.LOG__WARN, message, exception)

    def _log_error(self, message, exception=None):
        self._log(event_ids.LOG__ERROR, message, exception)

    def _log_fatal(self, message, exception=None):
        self._log(event_ids.LOG__FATAL, message, exception)

    def _log(self, event_id, message, exception=None):
        self._fire(event_id, target_ids.LOGGER, {
            "message": "({0}) {1}".format(self._get_log_src(), message),
            "error": exception,
        })

    def _get_log_src(self):
        return str(self)

    @property
    def _bus(self):
        return self.__bus

    # noinspection PyUnusedLocal
    def __on_close(self, event_id, target_id, event_obj):
        self.close()


def _cleanup_listeners(bus, listeners):
    assert isinstance(bus, Bus)
    assert isinstance(listeners, list)
    for event_id, target_id, listener in listeners:
        bus.remove_listener(event_id, target_id, listener)
    listeners.clear()


class MarshalableComponent(Component, Marshalable):
    def __init__(self, bus):
        Component.__init__(self, bus)
        self._listen(event_ids.MARSHAL__SAVE, target_ids.BROADCAST, lambda e, t, o: self._fire(
            event_ids.MARSHAL__SAVE_TO, target_ids.MARSHALLER, {'text': self.marshal()}))


class Identifiable(object):
    def __init__(self, cid):
        assert isinstance(self, Component)

        self.__cid = cid

    def close(self):
        cid = self.cid
        print("DEBUG Identifiable close() call for {0}".format(cid))
        assert isinstance(self, Component)
        self._fire(event_ids.REGISTRAR__OBJECT_REMOVED, cid, {
            'cid': cid,
            'type': type(self)
        })
        Component.close(self)

    def _get_log_src(self):
        return self.cid

    @property
    def cid(self):
        return self.__cid

    def __str__(self):
        return "{0} ({0})".format(self.cid, type(self))
