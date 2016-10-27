
from .layout import Layout
from .portal import PORTAL_CATEGORY
from ...system import event_ids
from ...config import LayoutConfig, ChildSplitConfig, ORIENTATION_HORIZONTAL, ORIENTATION_VERTICAL, ORIENTATION_CENTER
from ..navigation import *

SPLIT_LAYOUT_CATEGORY = 'split-layout'


def get_object_factories():
    return {
        SPLIT_LAYOUT_CATEGORY: split_layout_factory,
    }


_RAW_SIZE = {'x': 0, 'y': 0, 'width': 1, 'height': 1}

_MOVE_PARENT_DIR = -2

_ORIENT_DIRS = {
    ORIENTATION_HORIZONTAL: {
        DIR_NORTH: _MOVE_PARENT_DIR,
        DIR_SOUTH: _MOVE_PARENT_DIR,
        DIR_EAST: 1,
        DIR_WEST: -1,
        DIR_PREVIOUS: -1,
        DIR_NEXT: 1,
    },
    ORIENTATION_VERTICAL: {
        DIR_NORTH: -1,
        DIR_SOUTH: 1,
        DIR_EAST: _MOVE_PARENT_DIR,
        DIR_WEST: _MOVE_PARENT_DIR,
        DIR_PREVIOUS: -1,
        DIR_NEXT: 1,
    }
}


def split_layout_factory(cid, arguments, bus, id_manager, config):
    parent_cid = arguments['parent-cid']
    layout_def = arguments['layout-def']
    return SplitLayout(cid, bus, config, id_manager, parent_cid, layout_def)


class SplitLayout(Layout):
    def __init__(self, cid, bus, config, id_manager, parent_cid, layout_config):
        assert isinstance(layout_config, LayoutConfig)
        assert layout_config.orientation in _ORIENT_DIRS
        Layout.__init__(self, cid, bus, config, id_manager, parent_cid)

        self.__layout_config = layout_config

        splits = layout_config.child_splits
        if splits is None or len(splits) <= 0:
            self._log_debug("Split definition {0} has no child splits; assuming 1 child portal".format(
                layout_config.name))
            splits = [None]

        # Create a child for each split
        for split in splits:
            if split is None:
                split = ChildSplitConfig(1, None)
            if split.layout_def is None or PORTAL_CATEGORY == split.layout_def.category:
                child_cid = self._add_child_portal(_RAW_SIZE, [])
                self._log_debug("Split {0} ({1}) child {2} assigned to portal {3}".format(
                    self.cid, layout_config.name, self._child_count, child_cid
                ))
                self._set_child_data(child_cid, 'split', split)
            else:
                child_cid = self._add_child_layout(split.layout_def, _RAW_SIZE, [])
                self._log_debug("Split {0} ({1}) child {2} assigned to layout {3} ({4})".format(
                    self.cid, layout_config.name, self._child_count, child_cid, split.layout_def.name
                ))
                self._set_child_data(child_cid, 'split', split)

    def _on_direction_negotiation_descend__portal(self, event_obj):
        # print("DEBUG negotiation descend for portal; {0}".format(self.cid))
        # Came from a parent.  Find the first available child.
        dest_type = event_obj['destination-type']
        child_cids = self._child_cids

        if dest_type != PORTAL_TYPE:
            self._log_debug("Descended to layout, which is an acceptable target.  Ending.")
            return self._fire_negotiation_target(self.cid, event_obj)

        if len(child_cids) <= 0:
            # No children.
            # Just end it already
            self._log_debug("Split with no children cannot go deeper, so using self as target.")
            return self._fire_negotiation_target(self.cid, event_obj)

        self._log_debug("Redirecting movement to the first child".format(child_cids[0]))
        self._fire_negotiation_descend(child_cids[0], event_obj)

    def _on_direction_negotiation_discover(self, event_id, target_id, event_obj):
        # print("DEBUG negotiation discover {0}".format(self.cid))
        self.__direction_negotiate(event_obj, True)

    def __direction_negotiate(self, event_obj, can_visit_parent):
        direction = event_obj['direction']
        dest_type = event_obj['destination-type']
        previous_cid = event_obj['previous-cid']
        origin_cid = event_obj['origin-portal-cid']

        if direction == DIR_PARENT:
            if can_visit_parent:
                # We're done.
                self._log_verbose("Navigate to parent as final destination")
                return self._fire_negotiation_target(self.parent_cid, event_obj)

            if dest_type == PORTAL_TYPE:
                # Can't really do anything else.  Looks like a mistake?
                self._log_warn("Attempted to navigate to a parent while descending to a portal ({0})".format(event_obj))
                # Redirect to the origin.  Going back to the previous cid would probably
                # just keep us making the same boo-boo, because that was where the code lives that got us
                # into this mess to begin with.
                return self._fire_negotiation_target(origin_cid, event_obj)

            # The parent can't be visited, and the destination isn't supposed to be a portal.
            # So we're the target.`
            self._log_verbose("Navigate to self, as the parent, as the final destination")
            return self._fire_negotiation_target(self.cid, event_obj)

        if direction not in _ORIENT_DIRS[self.__layout_config.orientation]:
            # Bad direction that we can't handle
            # Note that this is after "parent", which isn't in the list.
            self._log_error("Unknown direction {0} for orientation {1}".format(
                direction, self.__layout_config.orientation))

            # Just end it already
            if dest_type == PORTAL_TYPE:
                # redirect to origin
                self._log_verbose("Redirect to origin from the bad direction")
                self._fire_negotiation_target(origin_cid, event_obj)
            # just use self
            self._log_verbose("Redirect to self from the bad direction")
            return self._fire_negotiation_target(self.cid, event_obj)

        index_change = _ORIENT_DIRS[self.__layout_config.orientation][direction]
        # print("DEBUG {0}: Rotating in {1} direction".format(self.cid, index_change))
        # print("DEBUG  -- children: {0}".format(self._child_cids))

        # Determine if we can handle this direction, based on our orientation.
        if _MOVE_PARENT_DIR == index_change:
            # move to the parent
            self._log_verbose("Cannot move in direction for this split, telling parent to handle it")
            return self._fire_negotiation_discover(event_obj)

        # We came from a child, so discover the child's index.
        child_cids = self._child_cids
        child_count = len(child_cids)
        try:
            source_pos = child_cids.index(previous_cid)
        except ValueError:
            if child_count <= 0:
                # No children.
                # Just end it already
                if dest_type == PORTAL_TYPE:
                    # redirect to origin
                    self._log_verbose("Split with no children cannot redirect to a child portal,"+
                                      " so pushing back to origin")
                    self._fire_negotiation_target(origin_cid, event_obj)
                # just use self
                self._log_verbose("Split with no children cannot go deeper, so using self as target.")
                return self._fire_negotiation_target(self.cid, event_obj)

            # just choose something
            self._log_verbose("Split can't find previous child cid as a child, so just choosing one.")
            source_pos = 0

        # Rotate through the children indices.
        next_pos = (source_pos + index_change + child_count) % child_count

        # Go down into the children
        self._log_verbose("Redirecting movement to the next child index {0}".format(next_pos))
        self._fire_negotiation_descend(child_cids[next_pos], event_obj)

    def _fire_negotiation_target(self, target_cid, event_obj):
        if target_cid == self.cid:
            return self._on_direction_negotiation_target(event_ids.DIRECTION_NEGOTIATION__TARGET, self.cid, event_obj)
        self._fire(event_ids.DIRECTION_NEGOTIATION__TARGET, target_cid, event_obj)

    def _do_layout(self):
        if ORIENTATION_CENTER == self.__layout_config.orientation:
            super()._do_layout()
            return

        dyn_min = 'y'
        dyn_max = 'height'
        static_min = 'x'
        static_max = 'width'
        if self.__layout_config.orientation == ORIENTATION_HORIZONTAL:
            static_min = 'y'
            static_max = 'height'
            dyn_min = 'x'
            dyn_max = 'width'

        static_min_pos = self.size[static_min]
        static_max_pos = self.size[static_max]
        start_pos = self.size[dyn_min]
        max_pos = self.size[dyn_max]
        diff_pos = max_pos - start_pos

        # First, calculate the number of split steps
        step_count = 0
        for child_cid in self._child_cids:
            step_count += self._get_split(child_cid).size

        step_pos = 0
        current_dyn = start_pos
        # print("DEBUG Splitting {0} (base size ({1},{2})x({3},{4})".format(
        #     self.cid, static_min_pos, static_max_pos, start_pos, max_pos
        # ))
        for child_cid in self._child_cids:
            split = self._get_split(child_cid)
            if split.size <= 0:
                # Floating child.
                self._fire(event_ids.LAYOUT__SET_RECTANGLE, child_cid, self.size)
                continue
            next_step = step_pos + split.size
            next_dyn = current_dyn + ((split.size * diff_pos) // step_count)
            if next_step >= step_count:
                # last child, make it full size
                # Remember, this is a width or height, not a final pixels position.
                next_dyn = max_pos - current_dyn
            # print("DEBUG - child {0}@{1} ({2},{3}) ({4} steps)".format(
            #     child_cid, step_pos, current_dyn, next_dyn, split.size))
            size = {
                static_min: static_min_pos,
                static_max: static_max_pos,
                dyn_min: current_dyn,
                dyn_max: next_dyn
            }
            self._fire(event_ids.LAYOUT__SET_RECTANGLE, child_cid, size)
            step_pos = next_step
            current_dyn = next_dyn

    def _get_split(self, child_cid):
        ret = self._get_child_data(child_cid, 'split')
        assert isinstance(ret, ChildSplitConfig)
        return ret
