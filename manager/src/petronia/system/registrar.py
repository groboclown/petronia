
from .component import Component, Identifiable
from .id_manager import IdManager
from . import event_ids
from . import target_ids
from ..config import Config


class Registrar(Identifiable, Component):
    def __init__(self, bus, id_manager, config):
        Component.__init__(self, bus)
        Identifiable.__init__(self, target_ids.REGISTRAR)
        assert isinstance(id_manager, IdManager)
        assert isinstance(config, Config)

        self.__category_factories = {}

        # Only here because you can't create a child object
        # without the id manager, and this avoids passing the
        # 2 objects.
        self.__id_manager = id_manager

        self.__config = config

        self._listen(event_ids.REGISTRAR__REGISTER_OBJECT, target_ids.REGISTRAR, self._on_register_object)

    def register_category_factory(self, category, factory):
        """

        :param category: category of object to construct
        :param factory: callable that takes 4 arguments: (cid, arguments, bus, id_manager, config),
            where "arguments" is a dictionary of string keys to values.
        :return: None
        """
        assert isinstance(category, str)
        assert callable(factory)
        if category in self.__category_factories:
            self._log_warn("already registered category factory {0}".format(category))
        self.__category_factories[category] = factory

    # noinspection PyUnusedLocal
    def _on_register_object(self, event_id, target_id, event_obj):
        cid = event_obj['cid']
        category = event_obj['category']
        registration_events = event_obj['registration-events']
        arguments = event_obj['arguments']
        obj = self._create_object(category, cid, arguments)
        if obj is not None:
            self._fire(event_ids.REGISTRAR__OBJECT_REGISTERED, cid, {
                'cid': obj.cid,
                'category': category,
                'arguments': arguments,
            })
            if registration_events is not None:
                for event in registration_events:
                    self._fire(event['event-id'], obj.cid, event)

    def _create_object(self, category, cid, arguments):
        try:
            if category in self.__category_factories:
                obj = self.__category_factories[category](cid, arguments, self._bus, self.__id_manager, self.__config)
                assert obj is None or isinstance(obj, Identifiable)
                return obj
            self._log_error("No such registered category {0}".format(category))
        except BaseException as e:
            self._log_error("Failed creating category {0} cid {1}".format(category, cid), e)
        return None


class StatefulRegistrar(Registrar):
    def __init__(self, bus, id_manager, config):
        super().__init__(bus, id_manager, config)

        self.__created_objects = {}

    @property
    def created_objects_by_cid(self):
        return self.__created_objects

    def _create_object(self, category, cid, arguments):
        ret = super()._create_object(category, cid, arguments)
        self.__created_objects[cid] = ret
        return ret
