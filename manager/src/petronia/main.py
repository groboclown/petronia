
# Future stuff may make this available as a windows shell replacement.
# To register this as the default shell, rather than explorer:
# HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\shell", "YOUR SHELL APPLICATION AND PATH HERE"

# http://stackoverflow.com/questions/2270527/how-to-code-a-new-windows-shell

from petronia.system.bus import Bus
from petronia.system.id_manager import IdManager
from petronia.system.registrar import Registrar
from petronia.shell.control.command_handler import CommandHandler
from petronia.shell.control.layout_management import LayoutManagementController
from petronia.shell.control.root_layout import RootLayout
from petronia.shell.control.split_layout import get_object_factories as layout_factories
from petronia.shell.control.portal import get_object_factories as portal_factories
from petronia.shell.control.active_portal_manager import ActivePortalManager
from petronia.shell.native.windows_hook_event import WindowsHookEvent
from petronia.shell.native.window_mapper import WindowMapper
from petronia.shell.view.render_selected_layout import RenderSelectedPanels
from petronia.shell.view.render_active_portal import RenderActivePortal
from petronia.util import worker_thread
from .tests.bus_logger import log_events

import sys
import importlib


if __name__ == '__main__':
    config_module = None
    if len(sys.argv) > 1:
        mod_name = sys.argv[1]
        if mod_name.endswith('.py'):
            mod_name = mod_name[:-3]
        mod_name = mod_name.replace('\\', '/').replace('/', '.')
        print("Importing configuration {0}".format(mod_name))
        config_module = importlib.import_module(mod_name)
    if config_module is None or not(hasattr(config_module, 'load_config')) or not callable(config_module.load_config):
        raise Exception("Argument 1 must be a Python file that provides the 'load_config' method.")
    # Temporary hard-coded setup until the config loading is working right.
    config = config_module.load_config()
    bus = Bus()
    log_events(bus)
    id_mgr = IdManager(bus)
    cmd_handler = CommandHandler(bus, config)
    registrar = Registrar(bus, id_mgr, config)
    for reg_objects in (layout_factories(), portal_factories()):
        for category, factory in reg_objects.items():
            registrar.register_category_factory(category, factory)
    root_layout = RootLayout(bus, config, id_mgr)
    layout_manager = LayoutManagementController(bus, id_mgr)
    apm = ActivePortalManager(bus)

    # Important: Mapper before Hook Event
    wm = WindowMapper(bus, id_mgr, config)

    # Important: Hook Event first
    whe = WindowsHookEvent(bus, config)
    rsp = RenderSelectedPanels(bus, config)
    rap = RenderActivePortal(bus, config)

    sys.stdin.read(1)

    worker_thread.stop_all_threads()
    exit()
