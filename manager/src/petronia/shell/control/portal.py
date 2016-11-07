
from .tile import Tile
from ..navigation import PORTAL_TYPE, create_direction_negotiation_start_event_obj
from ...system import event_ids
from ...system import target_ids


PORTAL_CATEGORY = PORTAL_TYPE


def get_object_factories():
    return {
        PORTAL_CATEGORY: portal_factory,
    }


def portal_factory(cid, arguments, bus, id_manager, config):
    parent_cid = arguments['parent-cid']
    ret = Portal(cid, bus, config, id_manager, parent_cid)
    if 'layout-def' in arguments:
        layout_def = arguments['layout-def']
        bus.fire(event_ids.PORTAL__CREATE_ALIAS, target_ids.ACTIVE_PORTAL_MANAGER, {
             'alias': layout_def.name,
             'portal-cid': cid,
        })
    return ret


class Portal(Tile):
    def __init__(self, cid, bus, config, id_manager, parent_cid):
        Tile.__init__(self, cid, bus, config, id_manager, parent_cid)

        self.__windows = []
        self.__window_listeners = {}
        self.__top_window_index = None
        self.__active = False

        self._listen(event_ids.PORTAL__MOVE_WINDOW_HERE, target_ids.ANY, self._on_move_window_here)
        self._listen(event_ids.ZORDER__CHANGE_TOP_WINDOW, cid, self._on_window_zorder_change)
        self._listen(event_ids.FOCUS__SET_FIRST_WINDOW_FOCUSED, cid, self._on_set_first_window_focused)
        self._listen(event_ids.PORTAL__MOVE_WINDOW_TO_OTHER_PORTAL, cid, self._on_move_window_to_other_portal)
        self._listen(event_ids.PORTAL__MOVE_WINDOW_TO_DESTINATION, cid, self._on_move_window_to_destination)
        self._listen(event_ids.PORTAL__SET_ACTIVE, cid, self._on_portal_becomes_active)
        self._listen(event_ids.PORTAL__ACTIVATED, target_ids.ANY, self._on_portal_activated)

    # noinspection PyUnusedLocal
    def _on_move_window_here(self, event_id, target_id, event_obj):
        event_obj['make-focused'] = True
        self._on_add_window(event_id, target_id, event_obj)

    def _on_add_window(self, event_id, target_id, event_obj):
        window_cid = event_obj['window-cid']
        window_index = self._get_window_index(window_cid)
        if target_id != self.cid and window_index >= 0:
            # Remove the window
            self._log_debug("Removing window {0} from portal {1}, moving to {2}".format(
                window_cid, self.cid, target_id))
            del self.__windows[window_index]
            if window_cid in self.__window_listeners:
                for event_id, listener in self.__window_listeners[window_cid].items():
                    self._remove_listener(event_id, window_cid, listener)
                del self.__window_listeners[window_cid]
        elif target_id == self.cid and window_index < 0:
            # Take on the new window
            self._log_debug("Moving widow {0} to portal {2} from {1}".format(
                window_cid, self.cid, target_id))
            window_info = event_obj['window-info']
            self.__windows.append(window_info)
            window_rect = self._get_window_rect()
            window_rect['make-focused'] = 'make-focused' in event_obj and event_obj['make-focused'] or False
            self._fire(event_ids.LAYOUT__SET_RECTANGLE, window_cid, window_rect)

            def this_window_activated(e, t, o):
                self._on_window_becomes_active(e, t, o)

            def this_window_redraw(e, t, o):
                self._on_window_redraw(e, t, o)

            self._listen(event_ids.WINDOW__FOCUSED, window_cid, this_window_activated)
            self._listen(event_ids.WINDOW__REDRAW, window_cid, this_window_redraw)
            self.__window_listeners[window_cid] = {
                event_ids.WINDOW__FOCUSED: this_window_activated,
                event_ids.WINDOW__REDRAW: this_window_redraw,
            }
            if 'make-focused' in event_obj and event_obj['make-focused']:
                self._fire(event_ids.PORTAL__SET_ACTIVE, self.cid, {})

    def _on_portal_becomes_active(self, event_id, target_id, event_obj):
        self._on_set_first_window_focused(event_id, target_id, event_obj)
        if not self.__active:
            self.__active = True
            self._fire(event_ids.PORTAL__ACTIVATED, target_ids.BROADCAST, {
                'portal-cid': self.cid,
                'portal-size': self.size,
                'portal-active': True,
            })

    def _on_window_zorder_change(self, event_id, target_id, event_obj):
        raise NotImplementedError()

    # noinspection PyUnusedLocal
    def _on_set_first_window_focused(self, event_id, target_id, event_obj):
        # Make our top window activated
        if len(self.__windows) <= 0:
            self._log_info("Cannot activate window in portal {0}: no registered windows".format(self.cid))
            return

        if self.__top_window_index is None or self.__top_window_index >= len(self.__windows):
            self.__top_window_index = 0

        self._fire(event_ids.TELL_WINDOWS__FOCUS_WINDOW, self.__windows[self.__top_window_index]['cid'], {})

    # noinspection PyUnusedLocal
    def _on_move_window_to_other_portal(self, event_id, target_id, event_obj):
        dest_window_info = None
        if self.__top_window_index is not None and self.__top_window_index < len(self.__windows):
            dest_window_info = self.__windows[self.__top_window_index]
        if dest_window_info is not None:
            if 'destination-cid' in event_obj:
                # Allow for direct action, rather than going through negotiation.
                self._fire(event_ids.PORTAL__MOVE_WINDOW_HERE, event_obj['destination-cid'], {
                    'window-cid': dest_window_info['cid'],
                    'window-info': dest_window_info,
                })
            else:
                self._fire(
                    event_ids.DIRECTION_NEGOTIATION__BEGIN, self.cid, create_direction_negotiation_start_event_obj(
                    self.cid, event_obj['direction'], PORTAL_TYPE, event_ids.PORTAL__MOVE_WINDOW_TO_DESTINATION,
                        self.cid, {
                            'window-cid': dest_window_info['cid'],
                            'window-info': dest_window_info,
                        }
                ))
        else:
            self._log_verbose("Could not move a window from portal {0}, as it has no windows.".format(self.cid))

    # noinspection PyUnusedLocal
    def _on_move_window_to_destination(self, event_id, target_id, event_obj):
        destination = event_obj['destination-cid']
        self._fire(event_ids.PORTAL__MOVE_WINDOW_HERE, destination, event_obj)

    # noinspection PyUnusedLocal
    def _on_window_becomes_active(self, event_id, target_id, event_obj):
        # TODO should lock on the __windows event.
        window_index = self._get_window_index(target_id)
        if window_index >= 0:
            self.__top_window_index = window_index
            if not self.__active:
                self.__active = True
                self._fire(event_ids.PORTAL__ACTIVATED, target_ids.BROADCAST, {
                    'portal-cid': self.cid,
                    'portal-size': self.size,
                    'portal-active': True,
                })
            return
        self._log_info("Portal {0} listened to 'window becomes active' for window {1}, but it isn't owned".format(
            self.cid, target_id
        ))

    # noinspection PyUnusedLocal
    def _on_window_redraw(self, event_id, target_id, event_obj):
        self._fire(event_ids.PORTAL__REDRAW, target_ids.BROADCAST, {
            'portal-cid': self.cid,
            'portal-size': self.size,
            'portal-active': self.__active,
        })

    # noinspection PyUnusedLocal
    def _on_portal_activated(self, event_id, target_id, event_obj):
        if event_obj['portal-cid'] != self.cid:
            if self.__active:
                self.__active = False
                self._fire(event_ids.PORTAL__DEACTIVATED, target_ids.BROADCAST, {
                    'portal-cid': self.cid,
                    'portal-size': self.size,
                    'portal-active': False,
                })

    def _on_direction_negotiation_discover(self, event_id, target_id, event_obj):
        # The parent passed down the request to "discover" the next location (it could
        # not have come from a child, because we don't have children), but this should
        # have instead been a "descend" event.  We'll still accept it, to keep errors
        # from going crazy, but we'll also report it.
        self._log_error("Internal Boo-Boo; portal was sent 'discover' event instead of 'descend'")
        self._on_direction_negotiation_target(event_id, target_id, event_obj)

    def _on_direction_negotiation_begin(self, event_id, target_id, event_obj):
        # Portals only go up
        self._fire_negotiation_discover(event_obj, True)

    def _on_direction_negotiation_descend(self, event_id, target_id, event_obj):
        # Expected to look at self and decedents; guess we're it.
        self._on_direction_negotiation_target(event_id, target_id, event_obj)

    def _on_remove_self(self, event_id, target_id, event_obj):
        dest_cid = self.parent_cid
        if 'window-parent' in event_obj:
            dest_cid = event_obj['window-parent']
        for window_info in self.__windows:
            self._fire(event_ids.PORTAL__MOVE_WINDOW_TO_OTHER_PORTAL, dest_cid, {
                'window-cid': window_info['cid'],
                'window-info': window_info,
            })
        # Immediately close; do not wait for the events.
        self.close()

    def _do_layout(self):
        window_rect = self._get_window_rect()
        for window_info in self.__windows:
            window_cid = window_info['cid']
            self._fire(event_ids.LAYOUT__SET_RECTANGLE, window_cid, window_rect)

    def _get_window_index(self, window_cid):
        for index in range(len(self.__windows)):
            if self.__windows[index]['cid'] == window_cid:
                return index
        return -1

    def _get_window_rect(self):
        border = self.config.chrome.portal_chrome_border
        if self.__active:
            border = self.config.chrome.portal_chrome_active_border
        return {
            'x': self.size['x'] + border['left'],
            'width': self.size['width'] - border['left'] - border['right'],
            'y': self.size['y'] + border['top'],
            'height': self.size['height'] - border['top'] - border['bottom'],
        }
