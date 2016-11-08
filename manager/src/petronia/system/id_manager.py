
from .component import Component, Identifiable
from . import event_ids
from . import target_ids


class IdManager(Identifiable, Component):
    """
    Manages the allocation of new identifiers.
    """
    def __init__(self, bus):
        Component.__init__(self, bus)
        Identifiable.__init__(self, target_ids.ID_MANAGER)

        self.__categories = {}
        self.__user_allocated = set()

        self._listen(event_ids.BUS__USER_GENERATED_ID, target_ids.ANY, lambda e, t, o: self.mark_allocated(o['cid']))

    def allocate(self, category):
        """

        :param category: how to categorize the identifier.  Has no implicit meaning.
        :return: the allocated CID
        """
        assert isinstance(category, str)
        if category not in self.__categories:
            self.__categories[category] = 0
        raw_cid = self.__categories[category]
        self.__categories[category] += 1
        ret = "{0}_{1}".format(category, raw_cid)
        self._fire(event_ids.REGISTRAR__ID_ALLOCATED, target_ids.BROADCAST, {'cid': ret})
        return ret

    def mark_allocated(self, cid):
        assert isinstance(cid, str)
        self.__user_allocated.add(cid)


class Parent(object):
    """
    A parent object that has a list of children.  It uses an IdManager to
    create the child IDs.
    """
    def __init__(self, id_manager, parent_cid=None):
        assert isinstance(self, Identifiable)
        assert isinstance(id_manager, IdManager)

        self.__id_manager = id_manager
        self.__parent_cid = parent_cid
        self.__child_cid_data = {}
        self.__ordered_child_cids = []  # ordered list of cids

    def _create_child(self, category, arguments, child_listeners, directed_events):
        """

        :param category: the kind of child to create; used by the registrar to
            create the actual object.
        :param child_listeners: dictionary of event ID to listener.
        :param directed_events: event objects (must include the key "event_id")
            that will be sent to the constructed child after it is created
            by the registrar.
        :return: CID of the created child.
        """
        assert isinstance(category, str)
        assert child_listeners is None or isinstance(child_listeners, dict)
        assert isinstance(arguments, dict)

        arguments['parent-cid'] = self.cid

        child_cid = self.__id_manager.allocate(category)
        # Add listeners before firing registration event
        self.__ordered_child_cids.append(child_cid)
        self.__child_cid_data[child_cid] = {}
        self.__child_cid_data[child_cid]['listeners'] = []
        if child_listeners is not None:
            for event_id, listener in child_listeners.items():
                self._child_listen(event_id, child_cid, listener)
        self._child_listen(event_ids.REGISTRAR__OBJECT_REMOVED, child_cid, self._on_child_removed)
        self._fire(event_ids.REGISTRAR__REGISTER_OBJECT, target_ids.REGISTRAR, {
            'cid': child_cid,
            'category': category,
            'arguments': arguments,
            'registration-events': directed_events,
        })
        return child_cid

    # noinspection PyUnusedLocal
    def _on_child_removed(self, event_id, target_id, event_obj):
        self.__remove_child_data(target_id)

    def _remove_child(self, child_cid):
        if child_cid in self.__child_cid_data:
            # TODO send close event to the child
            self._log_warn("TODO no close event sent to child")
            self.__remove_child_data(child_cid)
        else:
            self._log_warn("INTERNAL ERROR Cannot remove; no such child: {0}".format(child_cid))

    def __remove_child_data(self, child_cid):
        if child_cid in self.__child_cid_data:
            for event_id, target_id, listener in self.__child_cid_data[child_cid]['listeners']:
                self._remove_listener(event_id, target_id, listener)
            del self.__child_cid_data[child_cid]
            if child_cid in self.__ordered_child_cids:
                self.__ordered_child_cids.remove(child_cid)
            # print("DEBUG removed child {2} for {0}; {1} children left ({3})".format(
            #     self.cid, self._child_count, child_cid, self._child_cids
            # ))
            if len(self.__child_cid_data) <= 0:
                self._on_last_child_removed()
        else:
            self._log_warn("INTERNAL ERROR Cannot remove; no such child: {0}".format(child_cid))

    def _child_listen(self, event_id, child_cid, listener):
        if child_cid not in self.__child_cid_data:
            self._log_warn("INTERNAL ERROR Cannot listen; no such child: {0}".format(child_cid))
        else:
            self.__child_cid_data[child_cid]['listeners'].append((event_id, child_cid, listener))
            self._listen(event_id, child_cid, listener)

    def _on_last_child_removed(self):
        pass

    def _get_child_data(self, child_cid, key):
        assert 'listeners' != key
        if child_cid in self.__child_cid_data and key in self.__child_cid_data[child_cid]:
            return self.__child_cid_data[child_cid][key]
        return None

    def _set_child_data(self, child_cid, key, data):
        assert 'listeners' != key
        if child_cid in self.__child_cid_data:
            self.__child_cid_data[child_cid][key] = data

    @property
    def _has_children(self):
        return len(self.__ordered_child_cids) > 0

    @property
    def _child_count(self):
        return len(self.__ordered_child_cids)

    @property
    def _child_cids(self):
        return list(self.__ordered_child_cids)

    @property
    def parent_cid(self):
        return self.__parent_cid

    @property
    def has_parent(self):
        return self.__parent_cid is not None
