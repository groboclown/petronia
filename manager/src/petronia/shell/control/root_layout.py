from .layout import Layout
from ...system import event_ids
from ...system import target_ids
from ...config import LayoutConfig
from ..navigation import *
import threading


_DIRECTION_INDEX = {
    DIR_NORTH: -1,
    DIR_SOUTH: 1,
    DIR_WEST: -1,
    DIR_EAST: 1,
    DIR_PREVIOUS: -1,
    DIR_NEXT: 1,
}


class RootLayout(Layout):
    """
    The root layout needs considerable locking when dealing with the layout.
    """

    def __init__(self, bus, config, id_manager):
        Layout.__init__(self, target_ids.TOP_LAYOUT, bus, config, id_manager, None)

        # When the root layout is computing
        self.__in_layout_mode = True
        self.__layout_name = None
        self.__windows_pending_assignment_by_cid = {}
        self.__monitors = None

        self._listen(event_ids.WINDOW__CREATED, target_ids.ANY, self._on_new_window_created)
        self._listen(event_ids.OS__RESOLUTION_CHANGED, target_ids.BROADCAST, self._on_resolution_changed)
        self._listen(event_ids.PORTAL__WINDOW_MOVED_TO_OTHER_PORTAL, target_ids.ANY, self._on_window_move_request)
        self._listen(event_ids.LAYOUT__ROOT_LAYOUT_CREATE, target_ids.TOP_LAYOUT, self._on_root_create_layout)
        self._listen(event_ids.LAYOUT__SWITCH_TO, target_ids.TOP_LAYOUT, self._on_workflow_layout_switch)

        self.__layout_lock = threading.RLock()

    def _on_resolution_changed(self, event_id, target_id, event_obj):
        with self.__layout_lock:
            self.__monitors = event_obj['monitors']
            self._on_workflow_layout_switch(event_id, target_id, {'layout-name': self.__layout_name})

    # noinspection PyUnusedLocal
    def _on_new_window_created(self, event_id, target_id, event_obj):
        window_cid = event_obj['window-cid']
        window_info = event_obj['window-info']
        with self.__layout_lock:
            if self.__in_layout_mode or not self._has_children:
                self._log_debug("RootLayout recorded window {0} for later movement".format(window_cid))
                self.__windows_pending_assignment_by_cid[window_cid] = window_info
                return

        # Find the location for the window.
        child_cid = self._find_child_cid_for_window(window_info)
        if child_cid is None:
            # No children, which shouldn't be possible, but still...
            self._log_warn("Window {0} could not be assigned to any layout".format(window_cid))
            self.__windows_pending_assignment_by_cid[window_cid] = window_info
        else:
            self._log_debug("Assigning window {0} to cid {1}".format(window_cid, child_cid))
            self._fire(event_ids.LAYOUT__ADD_WINDOW, child_cid, {
                'window-cid': window_cid,
                'window-info': window_info,
                'origin-portal-cid': 'origin-portal-cid' in event_obj and event_obj['origin-portal-cid'] or None,
                'previous-cid': self.cid,
            })

    # noinspection PyUnusedLocal
    def _on_window_move_request(self, event_id, target_id, event_obj):
        # A window was assigned to a portal.  Remove from our list of pending.
        window_cid = event_obj['window-cid']
        # window_info = event_obj['window-info']
        with self.__layout_lock:
            if window_cid in self.__windows_pending_assignment_by_cid:
                del self.__windows_pending_assignment_by_cid[window_cid]

    # noinspection PyUnusedLocal
    def _on_workflow_layout_switch(self, event_id, target_id, event_obj):
        # Remove all children.  When the last is removed, that will trigger
        # _on_last_child_removed, which will rebuild the layout.
        with self.__layout_lock:
            self.__layout_name = event_obj['layout-name']
            if self._has_children:
                self._log_verbose("Delaying workflow layout switch - need to clear out children first")
                for child_cid in self._child_cids:
                    self._fire(event_ids.LAYOUT__REMOVE_OBJECT, child_cid, {
                        'window-parent': target_ids.TOP_LAYOUT,
                    })
            else:
                # directly setup the layout
                self._on_root_create_layout(event_id, target_id, event_obj)

    # noinspection PyUnusedLocal
    def _on_root_create_layout(self, event_id, target_id, event_obj):
        """
        The big kahuna.  This populates the layouts according to the screen resolution and the user configuration.

        :param event_id:
        :param target_id:
        :param event_obj:
        :return:
        """
        self._log_verbose("============================= Root create layout =============================")
        with self.__layout_lock:
            if self.__monitors is None:
                self._log_error("Called 'root_create_layout' before a resolution changed event generated.  " +
                                "Setup order is probably wrong.")
                # TODO could generate a new event to trigger the windows_hook_event to regenerate the monitor setup
                # event.
                return
            self.__in_layout_mode = True
            workgroup = self.config.get_workgroup_for_display(self.__monitors)
            top_layouts = workgroup.get_layout_group(self.__layout_name)
            if len(top_layouts) == len(self.__monitors):
                self._log_debug("RootLayout: One layout per monitor")
                windows_by_layout = []
                for layout_config in top_layouts:
                    assert isinstance(layout_config, LayoutConfig)
                    layout_windows = []
                    if layout_config.include_initial_windows:
                        # copy of the list so that we can remove from it while iterating.
                        for window_info in list(self.__windows_pending_assignment_by_cid.values()):
                            if self.config.applications.is_contained_in(layout_config.name, window_info):
                                layout_windows.append(window_info)
                                del self.__windows_pending_assignment_by_cid[window_info['cid']]
                    windows_by_layout.append(layout_windows)
                # Any leftovers are going in the first layout that accepts initial windows
                for layout_config in top_layouts:
                    if layout_config.include_initial_windows:
                        for window_info in self.__windows_pending_assignment_by_cid.values():
                            windows_by_layout[0].append(window_info)
                        self.__windows_pending_assignment_by_cid = {}
                if len(self.__windows_pending_assignment_by_cid) > 0:
                    self._log_warn("Orphaned windows: {0}".format(self.__windows_pending_assignment_by_cid.keys()))

                for i in range(len(top_layouts)):
                    layout = top_layouts[i]
                    monitor = self.__monitors[i]
                    size = {
                        'x': monitor['left'],
                        'y': monitor['top'],
                        'width': monitor['right'] - monitor['left'],
                        'height': monitor['bottom'] - monitor['top'],
                    }
                    events = []
                    for window_info in windows_by_layout[i]:
                        events.append({
                            'event-id': event_ids.LAYOUT__ADD_WINDOW,
                            'window-cid': window_info['cid'],
                            'window-info': window_info,
                            'origin-portal-cid': None,
                            'previous-cid': self.cid,
                        })
                    child_cid = self._add_child_layout(layout, size, events)
                    self._log_debug("Child layout {0} assigned {1} windows".format(child_cid, len(windows_by_layout)))
                    self._set_child_data(child_cid, 'monitor', size)

            # elif len(top_layouts) == 1:
            else:
                # We only support 1 layout for everything, or 1 layout per monitor.
                # Other combinations are just too tricky (for now).
                if len(top_layouts) != 1:
                    self._log_warn("Layout group {0} has {1} layouts, but there are {2} monitors".format(
                        self.__layout_name, len(top_layouts), len(self.__monitors)
                    ))
                self._log_debug("One layout for all the monitors")
                size = {'x': 100000, 'y': 100000, 'width': 0, 'height': 0}
                for monitor in self.__monitors:
                    size['x'] = min(size['x'], monitor['left'])
                    size['y'] = min(size['y'], monitor['top'])
                    size['width'] = max(size['width'], monitor['right'])
                    size['height'] = max(size['height'], monitor['bottom'])
                events = []
                for window_cid, window_info in self.__windows_pending_assignment_by_cid.items():
                    events.append({
                        'event_id': event_ids.LAYOUT__ADD_WINDOW,
                        'window-cid': window_cid,
                        'window-info': window_info,
                        'origin-portal-cid': None,
                        'previous-cid': self.cid,
                    })
                child_cid = self._add_child_layout(top_layouts[0], size, events)
                self._set_child_data(child_cid, 'monitor', size)

            self.__in_layout_mode = False

    def _on_last_child_removed(self):
        self._on_root_create_layout(None, None, None)

    def _on_direction_negotiation_discover(self, event_id, target_id, event_obj):
        print("DEBUG Root discover")

        # This is really complex when dealing with multi-monitor situations (think
        # 5 monitors stacked like:
        #
        #     M2    M3
        #  M4    M1     M5
        #
        # For now, just loop through the layouts in a reasonable manner.

        index_change = 1
        if 'direction' in event_obj:
            if DIR_PARENT == event_obj['direction']:
                # use the first child
                return self._on_direction_negotiation_descend__portal(event_obj)
            if event_obj['direction'] in _DIRECTION_INDEX:
                index_change = _DIRECTION_INDEX[event_obj['direction']]

        previous_cid = event_obj['previous-cid']
        try:
            previous_child_index = self._child_cids.index(previous_cid)
        except ValueError:
            # Don't know where it's from.  Just use a good match.
            self._log_warn("Unknown child cid {0} for root layout".format(previous_cid))
            return self._on_direction_negotiation_descend__portal(event_obj)

        # Rotate through the child indicies
        next_child_index = (previous_child_index + index_change + self._child_count) % self._child_count
        print("DEBUG root rotating movement from index {0} to {1}".format(previous_child_index, next_child_index))

        return self._fire_negotiation_descend(self._child_cids[next_child_index], event_obj)

    def _on_direction_negotiation_descend__portal(self, event_obj):
        print("DEBUG Root descend portal")
        # Just find the first valid child.
        for child_cid in self._child_cids:
            if child_cid != event_obj['previous-cid']:
                print("DEBUG root descending into first non-previous child {0}".format(child_cid))
                return self._fire_negotiation_descend(child_cid, event_obj)
        if self._child_count > 0:
            # Just reuse the first one.
            print("DEBUG root descending into first child {0}".format(self._child_cids[0]))
            return self._fire_negotiation_descend(self._child_cids[0], event_obj)
        # Whoops.  Use the origin.
        self._log_warn("Could not find a child of the root node.  Sending movement back to the origin")
        self._fire_negotiation_descend(event_obj['origin-portal-cid'], event_obj)

    def _do_layout(self):
        # Very special layout operation.
        # In fact, it's so special (very monitor specific), that we don't
        # actually do anything.
        self._log_verbose("RootLayout ignoring do_layout request")
