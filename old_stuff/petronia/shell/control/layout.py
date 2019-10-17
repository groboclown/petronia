
from .tile import Tile
from ..navigation import PORTAL_TYPE
from ...system import event_ids
from ...config import LayoutConfig


class Layout(Tile):
    def __init__(self, cid, bus, config, id_manager, parent_cid):
        """

        :param cid:
        :param bus:
        :param config:
        :param id_manager:
        """
        Tile.__init__(self, cid, bus, config, id_manager, parent_cid)

    def _add_child_portal(self, size, layout_def, events):
        """
        Add a portal child.

        :param size:
        :param events:
        :return:
        """
        return self.__add_child_obj(PORTAL_TYPE, layout_def, size, events)

    def _add_child_layout(self, layout_def, size, events):
        """
        Add a layout child.

        :param layout_def:
        :param size:
        :param events:
        :return:
        """
        assert isinstance(layout_def, LayoutConfig)
        return self.__add_child_obj(layout_def.category, layout_def, size, events)

    def __add_child_obj(self, category, layout_def, size, events):
        assert layout_def is None or isinstance(layout_def, LayoutConfig)
        arguments = {
            'layout-def': layout_def,
        }
        if size is not None:
            events.append({
                'event-id': event_ids.LAYOUT__SET_RECTANGLE,
                'x': size['x'],
                'y': size['y'],
                'width': size['width'],
                'height': size['height'],
            })
        child_cid = self._create_child(category, arguments, self._create_child_listeners(category), events)
        self._set_child_data(child_cid, 'type', category)
        self._set_child_data(child_cid, 'layout-def', layout_def)
        return child_cid

    def _get_child_layout(self, child_cid):
        ret = self._get_child_data(child_cid, 'layout-def')
        assert ret is None or isinstance(ret, LayoutConfig)
        return ret

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def _create_child_listeners(self, category):
        """
        Add additional listeners for an added child's events.

        :param category: category of the added child.
        :return: list of listeners (see _create_child for a description)
        """
        return None

    def _on_remove_self(self, event_id, target_id, event_obj):
        for child_cid in self._child_cids:
            # print("DEBUG {0} requesting removal of child {1}".format(self.cid, child_cid))
            self._fire(event_ids.LAYOUT__REMOVE_OBJECT, child_cid, {
                'window-parent': self.parent_cid,
            })
        # Wait for the children to be removed before closing self.

    def _on_last_child_removed(self):
        # Immediately terminate this object.
        # print("DEBUG {0} last child removed; closing".format(self.cid))
        self.close()

    def _on_direction_negotiation_descend(self, event_id, target_id, event_obj):
        if event_obj['destination-type'] == PORTAL_TYPE:
            self._on_direction_negotiation_descend__portal(event_obj)
        else:
            # Just use self as the target
            self._negotiation_complete(event_obj)

    def _on_direction_negotiation_descend__portal(self, event_obj):
        raise NotImplementedError()

    def _on_direction_negotiation_discover(self, event_id, target_id, event_obj):
        raise NotImplementedError()

    def _on_direction_negotiation_begin(self, event_id, target_id, event_obj):
        # For layouts, we need to discover the next place to send it to.
        # It does, however, need to be aware of whether "self" is an acceptable
        # target, based on the event id or the origin cid; in both these cases,
        # the "self" is not acceptable.  For the most part, a layout should never
        # be the source of a negotiation, but things happen.
        self._log_warn("Layout {0} set as direction negotiation source".format(self.cid))
        dest_obj = dict(event_obj)
        dest_obj['origin-portal-cid'] = self.cid
        self._on_direction_negotiation_discover(event_id, target_id, event_obj)

    def _on_add_window(self, event_id, target_id, event_obj):
        # This should not be the target for the window; it needs to be passed to a portal
        window_info = event_obj['window-info']

        child_cid = self._find_child_cid_for_window(window_info, [
            event_obj['origin-portal-cid'], event_obj['previous-cid']
        ])
        if child_cid is None:
            return
        dest_obj = dict(event_obj)
        dest_obj['previous-cid'] = self.cid
        self._fire(event_id, child_cid, dest_obj)

    def _do_layout(self):
        for child_cid in self._child_cids:
            self._fire(event_ids.LAYOUT__SET_RECTANGLE, child_cid, dict(self.size))

    def _find_child_cid_for_window(self, window_info, lowest_priority_cids=None):
        if lowest_priority_cids is None:
            lowest_priority_cids = tuple()
        assert isinstance(lowest_priority_cids, list) or isinstance(lowest_priority_cids, tuple)

        if not self._has_children:
            self._log_fatal("No destination for window {0} (source {1])".format(
                window_info, lowest_priority_cids
            ))
            return None

        # First, try children who are not in the lowest priority set,
        child_ids = self._child_cids
        for child_cid in child_ids:
            if child_cid not in lowest_priority_cids:
                layout_def = self._get_child_layout(child_cid)
                layout_name = layout_def is None and child_cid or layout_def.name
                if self.config.applications.is_contained_in(layout_name, window_info):
                    return child_cid

        # *Still* no match.  Try main layout child
        for child_cid in child_ids:
            layout_def = self._get_child_layout(child_cid)
            if layout_def and layout_def.is_main_layout_sibling:
                return child_cid

        # Did not match a layout that wants the window.
        # Next, try the children that are not lowest priority.
        for child_cid in child_ids:
            if child_cid not in lowest_priority_cids:
                return child_cid

        # I give up.  Just use the first child.
        return child_ids[0]
