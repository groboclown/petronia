
from ..shell.view.portal_chrome import portal_chrome_factory


def get_factory(component_settings):
    def portal_chrome_factory_gen(bus, config, id_manager):
        portal_chrome_factory(bus, config, id_manager, component_settings)

    return portal_chrome_factory_gen
