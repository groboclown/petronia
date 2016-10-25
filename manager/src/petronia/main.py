
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
from .util import worker_thread
from .script.read_config import read_user_configuration
from .tests.bus_logger import log_events

import sys


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Usage: arg 1: the user configuration file")
        exit(1)

    config = read_user_configuration(sys.argv[1])
    bus = Bus()
    Logger(bus, LEVEL_VERBOSE)
    # log_events(bus)
    id_mgr = IdManager(bus)
    cmd_handler = CommandHandler(bus, config)
    registrar = Registrar(bus, id_mgr, config)
    for reg_objects in (layout_factories(), portal_factories()):
        for category, factory in reg_objects.items():
            registrar.register_category_factory(category, factory)
    if config.uses_layout:
        RootLayout(bus, config, id_mgr)
        LayoutManagementController(bus, id_mgr)
        ActivePortalManager(bus)

    # Important: Mapper before Hook Event
    wm = WindowMapper(bus, id_mgr, config)

    # Important: Hook Event first
    whe = WindowsHookEvent(bus, config)

    if config.uses_layout:
        RenderSelectedPanels(bus, config)
        RenderActivePortal(bus, config)

    sys.stdin.read(1)

    worker_thread.stop_all_threads()
    exit()
