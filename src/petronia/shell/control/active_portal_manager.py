
from ...config import Config
from ...system.component import Component, Identifiable
from ...system import event_ids
from ...system import target_ids
from ..control.portal import PORTAL_CATEGORY
from ..navigation import create_direction_negotiation_start_event_obj, DIR_PREVIOUS, DIR_NEXT


# noinspection PyUnusedLocal
def active_portal_manager_factory(bus, config, id_manager):
    if config.uses_layout:
        ActivePortalManager(bus, config)


class ActivePortalManager(Identifiable, Component):
    def __init__(self, bus, config):
        Component.__init__(self, bus)
        Identifiable.__init__(self, target_ids.ACTIVE_PORTAL_MANAGER)
        assert isinstance(config, Config)

        self.__config = config

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

        # Because this class owns the list of portals and their aliases, we can have it also take on the
        # responsibility of the window to portal assignment.  This may need to be split out eventually.

        self._listen(event_ids.WINDOW__CREATED, target_ids.ANY, self._on_window_created)

    # noinspection PyUnusedLocal
    def _on_focus_move(self, event_id, target_id, event_obj):
        active = self._find_active_portal_cid()
        if active is not None:
            direction = event_obj['direction']
            self._fire(
                event_ids.DIRECTION_NEGOTIATION__BEGIN, active,
                create_direction_negotiation_start_event_obj(
                    self.cid, direction, 'portal', event_ids.PORTAL__SET_ACTIVE, None, {}
                )
            )

    # noinspection PyUnusedLocal
    def _on_window_zorder_change(self, event_id, target_id, event_obj):
        direction = event_obj['direction']
        active = self._find_active_portal_cid()
        if active is not None:
            self._fire(event_ids.ZORDER__CHANGE_TOP_WINDOW, active, {
                'direction': direction,
            })
        else:
            self._log_verbose("Could not change window z-order; no active portal.")
        # TODO implement
        pass

    # noinspection PyUnusedLocal
    def _on_create_portal_alias(self, event_id, target_id, event_obj):
        if 'portal-cid' in event_obj:
            # print("DEBUG registered alias {0} on portal {1}".format(event_obj['alias'], event_obj['portal-cid']))
            self.__portal_aliases[event_obj['portal-cid']] = event_obj['alias']
        elif self.__active_portal_cid is not None:
            # print("DEBUG registered alias {0} on portal {1}".format(event_obj['alias'], self.__active_portal_cid))
            self.__portal_aliases[event_obj['alias']] = self.__active_portal_cid

    # noinspection PyUnusedLocal
    def _on_focus_portal_alias(self, event_id, target_id, event_obj):
        alias = event_obj['alias']
        if alias in self.__portal_aliases and self.__portal_aliases[alias] in self.__portal_cids:
            self._fire(event_ids.PORTAL__SET_ACTIVE, self.__portal_aliases[alias], {})

    # noinspection PyUnusedLocal
    def _move_portal_window_to_other_portal(self, event_id, target_id, event_obj):
        active = self._find_active_portal_cid()
        if active is not None:
            # This is the temporary movement handler until navigation can handle it better.
            self._log_verbose("Moving active window in {0} {1}".format(
                active, event_obj['direction']
            ))
            direction = event_obj['direction']
            if DIR_NEXT == direction:
                dir_add = 1
            elif DIR_PREVIOUS == direction:
                dir_add = -1
            else:
                # Use the normal movement.  This should be the only line in the
                # "if __active_portal_cid is not None" statement.
                return self._fire(event_id, active, event_obj)

            portals = list(self.__portal_cids)
            portal_count = len(portals)
            try:
                current_index = portals.index(active)
                dest_cid = portals[(portal_count + current_index + dir_add) % portal_count]
            except KeyError:
                if portal_count <= 0:
                    return self._log_warn("No portals registered; cannot move window.")
                dest_cid = portals[0]
            return self._fire(event_ids.PORTAL__MOVE_WINDOW_TO_OTHER_PORTAL, active, {
                'destination-cid': dest_cid
            })
        # else:
        #     print("DEBUG no active portal")

    # noinspection PyUnusedLocal
    def _on_portal_activated(self, event_id, target_id, event_obj):
        self.__active_portal_cid = event_obj['portal-cid']
        self._log_debug("Active manager assigned active portal to {0}".format(self.__active_portal_cid))

    # noinspection PyUnusedLocal
    def _on_object_registered(self, event_id, target_id, event_obj):
        if event_obj['category'] == PORTAL_CATEGORY:
            self.__portal_cids.append(event_obj['cid'])
            self._fire(event_ids.PORTAL__CREATED, event_obj['cid'], event_obj)
            # Note that, if the active portal is None, do NOT set it to active.
            # Bad things happen; specifically the least significant window suddenly becomes
            # active, and all the initial windows are shoved into it.

    # noinspection PyUnusedLocal
    def _on_object_removed(self, event_id, target_id, event_obj):
        try:
            self.__portal_cids.remove(target_id)
            self._log_verbose("Removed registered portal {0}".format(target_id))
            # Ensure the active portal is still accurate
            self._find_active_portal_cid()
            self._fire(event_ids.PORTAL__DESTROYED, target_id, event_obj)
        except KeyError:
            pass
        except ValueError:
            pass

    # noinspection PyUnusedLocal
    def _on_window_created(self, event_id, target_id, event_obj):
        portal_alias = self.__config.applications.get_best_portal_match(
            self.__portal_aliases.keys(), event_obj['window-info'])
        # print("DEBUG matched {1} with {0}".format(event_obj['window-info']['exec_filename'], portal_alias))
        dest_cid = None
        if portal_alias in self.__portal_aliases:
            dest_cid = self.__portal_aliases[portal_alias]
            if dest_cid not in self.__portal_cids:
                dest_cid = None
        if dest_cid is None:
            dest_cid = self._find_active_portal_cid()
            if dest_cid is None:
                self._log_debug("Window added before any portal created.")
                return
        self._fire(event_ids.LAYOUT__ADD_WINDOW, dest_cid, event_obj)

    def _find_active_portal_cid(self):
        ret = self.__active_portal_cid
        if ret is not None:
            # Ensure it exists
            if ret not in self.__portal_cids:
                self.__active_portal_cid = None
                ret = None
        if ret is None:
            if len(self.__portal_cids) > 0:
                ret = self.__portal_cids[0]
                self._fire(event_ids.PORTAL__SET_ACTIVE, ret, {})
            # else:
            #     print("DEBUG no active portal, because there are no known portals.")
        return ret
