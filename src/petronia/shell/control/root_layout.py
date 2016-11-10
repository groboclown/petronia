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


def root_layout_factory(bus, config, id_manager):
    if config.uses_layout:
        layout_name = None
        if 'layout-name' in config.init_options:
            layout_name = config.init_options['layout-name']
        RootLayout(bus, config, id_manager, layout_name)


class RootLayout(Layout):
    """
    The root layout needs considerable locking when dealing with the layout.
    """

    def __init__(self, bus, config, id_manager, initial_layout_name=None):
        Layout.__init__(self, target_ids.TOP_LAYOUT, bus, config, id_manager, None)

        # When the root layout is computing
        self.__layout_name = initial_layout_name
        self.__monitors = None

        self.__layout_lock = threading.RLock()

        self._listen(event_ids.OS__RESOLUTION_CHANGED, target_ids.ANY, self._on_resolution_changed)
        self._listen(event_ids.LAYOUT__ROOT_LAYOUT_CREATE, target_ids.TOP_LAYOUT, self._on_root_create_layout)
        self._listen(event_ids.LAYOUT__SWITCH_TO, target_ids.TOP_LAYOUT, self._on_workflow_layout_switch)
        self._listen(event_ids.CONFIG__UPDATE, target_ids.ANY, self._on_config_update)

    def _on_resolution_changed(self, event_id, target_id, event_obj):
        self._log_verbose("Monitor resolution changed")
        with self.__layout_lock:
            self.__monitors = event_obj['monitors']
            self._on_workflow_layout_switch(event_id, target_id, {'layout-name': self.__layout_name})

    # noinspection PyUnusedLocal
    def _on_config_update(self, event_id, target_id, event_obj):
        self._on_workflow_layout_switch(event_id, target_id, {'layout-name': self.__layout_name})

    # noinspection PyUnusedLocal
    def _on_workflow_layout_switch(self, event_id, target_id, event_obj):
        # Even if the requested layout is the same as the current layout,
        # still perform the change.  If the user had changed around the layout manually,
        # the layout may need adjustment.  Also, this will reset the windows to their
        # original position.
        self._log_verbose("Switching Layout")

        # Remove all children.  When the last is removed, that will trigger
        # _on_last_child_removed, which will rebuild the layout.
        with self.__layout_lock:
            self.__layout_name = event_obj['layout-name']
            if self._has_children:
                self._log_verbose("Delaying workflow layout switch - need to clear out children first")
                for child_cid in self._child_cids:
                    self._log_verbose("Requesting removal of child {0}".format(child_cid))
                    self._fire(event_ids.LAYOUT__REMOVE_OBJECT, child_cid, {
                        'window-parent': target_ids.TOP_LAYOUT,
                    })
                # Because those removals happen in a NOW event, we can see
                # if we can initiate the layout.
                # However, let's just be formal about it. Especially in case
                # the associated event thread changes.
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
            workgroup = self.config.get_workgroup_for_display(self.__monitors)
            top_layouts = workgroup.get_layout_group(self.__layout_name)
            if len(top_layouts) == len(self.__monitors):
                self._log_debug("RootLayout: One layout per monitor")
                for i in range(len(top_layouts)):
                    layout = top_layouts[i]
                    assert isinstance(layout, LayoutConfig)
                    monitor = self.__monitors[i]
                    size = {
                        'x': monitor['left'],
                        'y': monitor['top'],
                        'width': monitor['right'] - monitor['left'],
                        'height': monitor['bottom'] - monitor['top'],
                    }
                    events = []
                    child_cid = self._add_child_layout(layout, size, events)
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
                child_cid = self._add_child_layout(top_layouts[0], size, events)
                self._set_child_data(child_cid, 'monitor', size)

            # Re-allocate all the open windows to their correct portals.
            self._fire(event_ids.PORTAL__SET_ACTIVE, target_ids.ACTIVE_PORTAL_MANAGER, {
                # TODO replace this magic "default" keyword.  At least make it a
                # constant and well-documented value.
                'alias': 'main'
            })
            self._fire(event_ids.LAYOUT__RESEND_WINDOW_CREATED_EVENTS, target_ids.WINDOW_MAPPER, {})

    def _on_last_child_removed(self):
        self._log_verbose("Last root child removed; going on to create the layout.")
        self._on_root_create_layout(None, None, None)

    def _on_direction_negotiation_discover(self, event_id, target_id, event_obj):
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
        self._log_verbose("Root rotating movement from index {0} to {1}".format(previous_child_index, next_child_index))

        return self._fire_negotiation_descend(self._child_cids[next_child_index], event_obj)

    def _on_direction_negotiation_descend__portal(self, event_obj):
        # Just find the first valid child.
        for child_cid in self._child_cids:
            if child_cid != event_obj['previous-cid']:
                return self._fire_negotiation_descend(child_cid, event_obj)
        if self._child_count > 0:
            # Just reuse the first one.
            return self._fire_negotiation_descend(self._child_cids[0], event_obj)
        # Whoops.  Use the origin.
        self._log_warn("Could not find a child of the root node.  Sending movement back to the origin")
        self._fire_negotiation_descend(event_obj['origin-portal-cid'], event_obj)

    def _do_layout(self):
        # Very special layout operation.
        # In fact, it's so special (very monitor specific), that we don't
        # actually do anything.
        self._log_verbose("RootLayout ignoring do_layout request")
