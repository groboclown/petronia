
from ...system.component import Component, Identifiable
from ...system import event_ids
from ...system import target_ids
from ..navigation import create_direction_negotiation_start_event_obj


class ActivePortalManager(Identifiable, Component):
    def __init__(self, bus):
        Component.__init__(self, bus)
        Identifiable.__init__(self, target_ids.ACTIVE_PORTAL_MANAGER)

        self.__active_portal_cid = None
        self.__portal_aliases = {}

        self._listen(event_ids.FOCUS__MOVE, target_ids.ACTIVE_PORTAL_MANAGER, self._on_focus_move)
        self._listen(event_ids.ZORDER__WINDOW_SHOWN_CHANGE, target_ids.ACTIVE_PORTAL_MANAGER,
                     self._on_window_zorder_change)
        self._listen(event_ids.PORTAL__CREATE_ALIAS, target_ids.ACTIVE_PORTAL_MANAGER,
                     self._on_create_portal_alias)
        self._listen(event_ids.FOCUS__PORTAL_ALIAS, target_ids.ACTIVE_PORTAL_MANAGER,
                     self._on_focus_portal_alias)
        self._listen(event_ids.PORTAL__MOVE_WINDOW_TO_OTHER_PORTAL, target_ids.ACTIVE_PORTAL_MANAGER,
                     self._move_portal_window_to_other_portal)
        self._listen(event_ids.PORTAL__ACTIVATED, target_ids.ANY, self._on_portal_activated)

    # noinspection PyUnusedLocal
    def _on_focus_move(self, event_id, target_id, event_obj):
        if self.__active_portal_cid is not None:
            direction = event_obj['direction']
            self._fire(
                event_ids.DIRECTION_NEGOTIATION__BEGIN, self.__active_portal_cid,
                create_direction_negotiation_start_event_obj(
                    self.cid, direction, 'portal', event_ids.PORTAL__SET_ACTIVE, None, {}
                )
            )

    # noinspection PyUnusedLocal
    def _on_window_zorder_change(self, event_id, target_id, event_obj):
        direction = event_obj
        # TODO implement
        pass

    # noinspection PyUnusedLocal
    def _on_create_portal_alias(self, event_id, target_id, event_obj):
        if self.__active_portal_cid is not None:
            self.__portal_aliases[event_obj['alias']] = self.__active_portal_cid

    # noinspection PyUnusedLocal
    def _on_focus_portal_alias(self, event_id, target_id, event_obj):
        alias = event_obj['alias']
        if alias in self.__portal_aliases:
            self._fire(event_ids.PORTAL__SET_ACTIVE, self.__portal_aliases[alias], {})

    # noinspection PyUnusedLocal
    def _move_portal_window_to_other_portal(self, event_id, target_id, event_obj):
        if self.__active_portal_cid is not None:
            self._fire(event_id, self.__active_portal_cid, event_obj)

    # noinspection PyUnusedLocal
    def _on_portal_activated(self, event_id, target_id, event_obj):
        self.__active_portal_cid = event_obj['portal-cid']
        self._log_debug("Active manager assigned active portal to {0}".format(self.__active_portal_cid))
