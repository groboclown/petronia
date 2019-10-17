
from .bus import Bus
from .id_manager import IdManager
from .registrar import Registrar
from ..config import Config


class ApplicationContext(object):
    """
    The whole application.
    """
    def __init__(self, bus=None, id_manager=None, registry=None, config=None):
        if bus is None:
            bus = Bus()
        assert isinstance(bus, Bus)
        if id_manager is None:
            id_manager = IdManager(bus)
        assert isinstance(id_manager, IdManager)
        if registry is None:
            registry = Registrar(bus, id_manager)
        assert isinstance(registry, Registrar)
        assert isinstance(config, Config)

        self.__bus = bus
        self.__id_manager = id_manager
        self.__registry = registry
        self.__config = config

    @property
    def bus(self):
        return self.__bus

    @property
    def registry(self):
        return self.__registry

    @property
    def config(self):
        return self.__config
