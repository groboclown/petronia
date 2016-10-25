
from ...config import Config
from ...system import event_ids
from ...system import target_ids
from ...system.component import MarshalableComponent, Identifiable
from ...system.id_manager import Parent


class Tile(Parent, Identifiable, MarshalableComponent):
    """
    Base class for the layouts and portals.
    """
    def __init__(self, cid, bus, config, id_manager, parent_cid):
        MarshalableComponent.__init__(self, bus)
        Identifiable.__init__(self, cid)
        Parent.__init__(self, id_manager, parent_cid)

        assert isinstance(config, Config)

        self.__config = config
        self.__size = None

        self._listen(event_ids.LAYOUT__SET_RECTANGLE, cid, self._on_resize)
        self._listen(event_ids.LAYOUT__ADD_WINDOW, cid, self._on_add_window)
        self._listen(event_ids.LAYOUT__REMOVE_OBJECT, cid, self._on_remove_self)

        self._listen(event_ids.DIRECTION_NEGOTIATION__BEGIN, cid, self._on_direction_negotiation_begin)
        self._listen(event_ids.DIRECTION_NEGOTIATION__DISCOVER, cid, self._on_direction_negotiation_discover)
        self._listen(event_ids.DIRECTION_NEGOTIATION__DESCEND, cid, self._on_direction_negotiation_descend)
        self._listen(event_ids.DIRECTION_NEGOTIATION__TARGET, cid, self._on_direction_negotiation_target)

    # noinspection PyUnusedLocal
    def _on_resize(self, event_id, target_id, event_obj):
        self.__size = {
            'x': event_obj['x'],
            'y': event_obj['y'],
            'width': event_obj['width'],
            'height': event_obj['height'],
        }
        self._do_layout()

    def _on_add_window(self, event_id, target_id, event_obj):
        raise NotImplementedError()

    def _on_remove_self(self, event_id, target_id, event_obj):
        # New parent for orphaned children is 'window-parent'
        self._fire(event_ids.REGISTRAR__OBJECT_REMOVED, target_ids.REGISTRAR, {})

    def _on_direction_negotiation_begin(self, event_id, target_id, event_obj):
        raise NotImplementedError()

    def _on_direction_negotiation_discover(self, event_id, target_id, event_obj):
        raise NotImplementedError()

    def _on_direction_negotiation_descend(self, event_id, target_id, event_obj):
        raise NotImplementedError()

    # noinspection PyUnusedLocal
    def _on_direction_negotiation_target(self, event_id, target_id, event_obj):
        print("DEBUG negotiation target {0}".format(self.cid))
        event_obj['chained-event-obj']['destination-cid'] = self.cid
        self._negotiation_complete(event_obj)
        target = event_obj['chained-event-target']
        if target is None:
            target = self.cid
        self._fire(event_obj['chained-event-id'], target, event_obj['chained-event-obj'])

    def _do_layout(self):
        raise NotImplementedError()

    @property
    def config(self):
        return self.__config

    @property
    def size(self):
        return self.__size

    def _fire_negotiation_discover(self, event_obj, is_origin_cid=False):
        # Always sent to the parent.
        dest_obj = dict(event_obj)
        if is_origin_cid:
            dest_obj['origin-portal-cid'] = self.cid
        dest_obj['previous-cid'] = self.cid
        self._fire(event_ids.DIRECTION_NEGOTIATION__DISCOVER, self.parent_cid, dest_obj)

    def _fire_negotiation_descend(self, child_cid, event_obj):
        dest_obj = dict(event_obj)
        dest_obj['previous-cid'] = self.cid
        self._fire(event_ids.DIRECTION_NEGOTIATION__DESCEND, child_cid, dest_obj)

    def _negotiation_complete(self, event_obj):
        self._fire(event_ids.DIRECTION_NEGOTIATION__COMPLETE, event_obj['source-cid'], {
            'negotiated-target-cid': self.cid,
            'negotiated-target-parent-cid': self.parent_cid,
            'chained-event-id': event_obj['chained-event-id'],
            'chained-event-target': event_obj['chained-event-target'],
            'chained-event-obj': event_obj['chained-event-obj']
        })
