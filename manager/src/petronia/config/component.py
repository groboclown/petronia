"""
Manages the user configuration.
"""

from .base_config import BaseConfig


class ComponentConfig(BaseConfig):
    """
    Registers all the different parts of the system to load.  Only runs
    once at startup time (cannot be reloaded).
    """
    def __init__(self, singletons=None, extensions=None):
        """

        :param singletons: list of factories that initiate themselves and install a single component
            into the system.
        :param extensions: dictionary of component type keys linked to the component factory.
        """
        # Perform import here to avoid circular imports.
        from ..system.extensions.component_factory_registry import get_base_extension_factories
        from ..system.extensions.singleton_factory_registry import get_base_singleton_factories

        self.__extensions = dict(get_base_extension_factories())
        if extensions is not None:
            for category, factory in extensions:
                assert isinstance(category, str)
                assert callable(factory)
                self.__extensions[category] = factory

        self.__singletons = list(get_base_singleton_factories())
        if singletons is not None:
            for singleton in singletons:
                assert callable(singleton)
                self.__singletons.append(singleton)

    def register_extensions(self, registrar):
        # Perform Registry import here to avoid circular imports.
        from ..system.registrar import Registrar
        assert isinstance(registrar, Registrar)
        for category, factory in self.__extensions.items():
            registrar.register_category_factory(category, factory)

    def activate_singletons(self, registrar):
        # Perform Registry import here to avoid circular imports.
        from ..system.registrar import Registrar
        assert isinstance(registrar, Registrar)
        for factory in self.__singletons:
            registrar.activate_singleton(factory)
