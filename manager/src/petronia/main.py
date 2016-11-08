
# Future stuff may make this available as a windows shell replacement.
# To register this as the default shell, rather than explorer:
# HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\shell", "YOUR SHELL APPLICATION AND PATH HERE"

# http://stackoverflow.com/questions/2270527/how-to-code-a-new-windows-shell

from .system.bus import Bus
from .system.id_manager import IdManager
from .system.registrar import Registrar
from .system.logger import Logger, LEVEL_DEBUG, LEVEL_VERBOSE, LEVEL_WARN
from .shell.native.windows_hook_event import WindowsHookEvent
from .shell.native.window_mapper import WindowMapper
from .script.read_config import read_user_configuration
from .tests.bus_logger import log_events

import sys


def setup(config_file, layout_name):
    config = read_user_configuration(config_file)
    config.init_options['layout-name'] = layout_name
    config.init_options['config-file'] = config_file
    config.init_options['log-level'] = LEVEL_VERBOSE
    # config.init_options['log-level'] = LEVEL_DEBUG
    bus = Bus()
    id_mgr = IdManager(bus)
    registrar = Registrar(bus, id_mgr, config)
    config.register_components(registrar)

    # Important: Mapper before Hook Event
    WindowMapper(bus, id_mgr, config)

    # Important: Hook Event after Mapper
    WindowsHookEvent(bus, config)

    return bus


def main_setup():
    if len(sys.argv) <= 1:
        print("Usage: arg 1: the user configuration file")
        exit(1)

    layout_name = None
    if len(sys.argv) >= 3:
        layout_name = sys.argv[2]

    setup(sys.argv[1], layout_name)


if __name__ == '__main__':
    main_setup()
