
# Future stuff may make this available as a windows shell replacement.
# To register this as the default shell, rather than explorer:
# HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\shell", "YOUR SHELL APPLICATION AND PATH HERE"

# http://stackoverflow.com/questions/2270527/how-to-code-a-new-windows-shell

from .system.bus import Bus
from .system.id_manager import IdManager
from .system.registrar import Registrar
from .system.logger import Logger, LEVEL_DEBUG, LEVEL_VERBOSE, LEVEL_ERROR
from .shell.control.command_handler import CommandHandler
from .shell.control.layout_management import LayoutManagementController
from .shell.control.root_layout import RootLayout
from .shell.control.split_layout import get_object_factories as layout_factories
from .shell.control.portal import get_object_factories as portal_factories
from .shell.control.active_portal_manager import ActivePortalManager
from .shell.native.windows_hook_event import WindowsHookEvent
from .shell.native.window_mapper import WindowMapper
from .shell.view.render_selected_layout import RenderSelectedPanels
from .shell.view.render_active_portal import RenderActivePortal
from .shell.view.render_text import get_object_factories as render_text_factories
from .script.read_config import read_user_configuration
from .tests.bus_logger import log_events

import sys


def setup(config_file):
    config = read_user_configuration(config_file)
    bus = Bus()
    Logger(bus, LEVEL_VERBOSE)
    id_mgr = IdManager(bus)
    CommandHandler(bus, config)
    registrar = Registrar(bus, id_mgr, config)

    # TODO this factory declaration needs to be extensible.
    for reg_objects in (layout_factories(), portal_factories(), render_text_factories()):
        for category, factory in reg_objects.items():
            registrar.register_category_factory(category, factory)

    if config.uses_layout:
        RootLayout(bus, config, id_mgr)
        LayoutManagementController(bus, id_mgr)
        ActivePortalManager(bus, config)

    # Important: Mapper before Hook Event
    WindowMapper(bus, id_mgr, config)

    # Important: Hook Event after Mapper
    WindowsHookEvent(bus, config)

    if config.uses_layout:
        RenderSelectedPanels(bus, config)
        RenderActivePortal(bus, config)

    return bus


def main_setup():
    if len(sys.argv) <= 1:
        print("Usage: arg 1: the user configuration file")
        exit(1)

    setup(sys.argv[1])


if __name__ == '__main__':
    main_setup()
