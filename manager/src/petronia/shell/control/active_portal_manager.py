
from ...system.component import Component, Identifiable
from ...system import event_ids
from ...system import target_ids
from ..control.portal import PORTAL_CATEGORY
from ..navigation import create_direction_negotiation_start_event_obj, DIR_PREVIOUS, DIR_NEXT


class ActivePortalManager(Identifiable, Component):
    def __init__(self, bus):
        Component.__init__(self, bus)
        Identifiable.__init__(self, target_ids.ACTIVE_PORTAL_MANAGER)

        # This is a temporary measure to handle some window movement, until the real navigation is
        # fixed and working.
        # Maybe it'll be permanent; and because I'm putting it here early, it'll probably end up being
        # permanent.
        self.__portal_cids = []
        self._listen(event_ids.REGISTRAR__OBJECT_REGISTERED, target_ids.ANY, self._on_object_registered)
        self._listen(event_ids.REGISTRAR__OBJECT_REMOVED, target_ids.ANY, self._on_object_removed)

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
            # This is the temporary movement handler until navigation can handle it better.
            print("DEBUG Moving active window in {0} {1}".format(self.__active_portal_cid, event_obj['direction']))
            direction = event_obj['direction']
            if DIR_NEXT == direction:
                dir_add = 1
            elif DIR_PREVIOUS == direction:
                dir_add = -1
            else:
                # Use the normal movement.  This should be the only line in the
                # "if __active_portal_cid is not None" statement.
                return self._fire(event_id, self.__active_portal_cid, event_obj)

            portals = list(self.__portal_cids)
            portal_count = len(portals)
            try:
                current_index = portals.index(self.__active_portal_cid)
                dest_cid = portals[(portal_count + current_index + dir_add) % portal_count]
            except KeyError:
                if portal_count <= 0:
                    return self._log_warn("No portals registered; cannot move window.")
                dest_cid = portals[0]
            return self._fire(event_ids.PORTAL__MOVE_WINDOW_TO_OTHER_PORTAL, self.__active_portal_cid, {
                'destination-cid': dest_cid
            })
        else:
            print("DEBUG no active portal")

    # noinspection PyUnusedLocal
    def _on_portal_activated(self, event_id, target_id, event_obj):
        self.__active_portal_cid = event_obj['portal-cid']
        self._log_debug("Active manager assigned active portal to {0}".format(self.__active_portal_cid))

    # noinspection PyUnusedLocal
    def _on_object_registered(self, event_id, target_id, event_obj):
        if event_obj['category'] == PORTAL_CATEGORY:
            self.__portal_cids.append(event_obj['cid'])

    # noinspection PyUnusedLocal
    def _on_object_removed(self, event_id, target_id, event_obj):
        try:
            self.__portal_cids.remove(event_obj['cid'])
        except KeyError:
            pass
        except ValueError:
            pass
