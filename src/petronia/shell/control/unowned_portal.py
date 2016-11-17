
from ...system import event_ids
from ...system import target_ids
from ...system.component import Component, Identifiable


# noinspection PyUnusedLocal
def unowned_portal_factory(bus, config, id_manager):
    UnownedPortal(bus)


class UnownedPortal(Identifiable, Component):
    """
    A hidden layout type.  This will own any window that should not belong to the tiled
    management.

    This allows windows to respond to user requests that otherwise require a portal.
    """
    def __init__(self, bus):
        Component.__init__(self, bus)
        Identifiable.__init__(self, target_ids.UNOWNED_WINDOW_PORTAL)

        self.__windows = {}
        self.__window_listeners = {}
        self.__last_flashing_window_cid = None

        self._listen(event_ids.WINDOW__FLASHING, target_ids.ANY, self._on_any_window_flashing)
        self._listen(event_ids.FOCUS__SWITCH_TO_LAST_FLASHING_WINDOW, target_ids.ANY, self._on_switch_flashing_window)
        self._listen(
            event_ids.LAYOUT__WINDOW_PUT_OUTSIDE_MANAGEMENT,
            target_ids.UNOWNED_WINDOW_PORTAL,
            self._on_move_window_here)

    # noinspection PyUnusedLocal
    def _on_any_window_flashing(self, event_id, target_id, event_obj):
        info = self._get_window_info(target_id)
        if info is not None:
            self.__last_flashing_window_cid = target_id
        else:
            self.__last_flashing_window_cid = None

    # noinspection PyUnusedLocal
    def _on_move_window_here(self, event_id, target_id, event_obj):
        window_cid = event_obj['window-cid']
        if self._get_window_info(window_cid) is not None:
            return
        window_info = event_obj['window-info']
        self.__windows[window_cid] = window_info
        listeners = {
            event_ids.WINDOW__CLOSED: self._on_window_closed,
        }
        for key, listener in listeners.items():
            self._listen(key, window_cid, listener)

    # noinspection PyUnusedLocal
    def _on_window_closed(self, event_id, target_id, event_obj):
        if target_id in self.__windows:
            del self.__windows[target_id]
        if target_id in self.__window_listeners:
            listeners = self.__window_listeners[target_id]
            del self.__window_listeners[target_id]
            for key, listener in listeners.items():
                self._remove_listener(key, target_id, listener)

    # noinspection PyUnusedLocal
    def _on_switch_flashing_window(self, event_id, target_id, event_obj):
        if self.__last_flashing_window_cid is not None and self.__last_flashing_window_cid in self.__windows:
            self._log_debug("Switching to last flashing window {0}".format(
                self.__windows[self.__last_flashing_window_cid]))
            self._fire(event_ids.ZORDER__SET_WINDOW_ON_TOP, self.__last_flashing_window_cid, {})

    def _get_window_info(self, window_cid):
        if window_cid in self.__windows:
            return self.__windows[window_cid]
        return None
