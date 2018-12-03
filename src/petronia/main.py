
# Future stuff may make this available as a windows shell replacement.
# To register this as the default shell, rather than explorer:
# HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\shell", "YOUR SHELL APPLICATION AND PATH HERE"

# http://stackoverflow.com/questions/2270527/how-to-code-a-new-windows-shell

from petronia.system.bus import Bus
from petronia.system.id_manager import IdManager
from petronia.system.registrar import Registrar
from petronia.system.logger import Logger, LEVEL_DEBUG, LEVEL_VERBOSE, LEVEL_WARN
from petronia.shell.native.windows_hook_event import WindowsHookEvent
from petronia.shell.native.window_mapper import WindowMapper
from petronia.script.read_config import read_user_configuration
from petronia.tests.bus_logger import log_events
from petronia.script.script_logger import create_stdout_logger
from petronia.version import VERSION

import sys
import os
import argparse


def setup(config_file, layout_name):
    config = read_user_configuration(config_file, create_stdout_logger())
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


def main_setup(args=None):
    if args is None:
        args = sys.argv
    parser = argparse.ArgumentParser()
    parser.description = "Window tiling manager for Windows."
    parser.add_argument(
        "-l", "--layout",
        help="Initial layout.  If not given, the layout named `default' is used.")
    parser.add_argument(
        "-v", "--version",
        help="Show the version and quit.",
        action="store_true"
    )
    parser.add_argument(
        "-e", "--extensions",
        help="Directory where the user extensions are stored.  Defaults to environment variable %%PETRONIA_USER_DIR%%"
    )
    parser.add_argument(
        "configfile",
        help="Configuration file for setting up the display.  Supported formats are: yaml, json, and py.")

    # argparse doesn't allow for the "-v" by itself.
    for arg in args[1:]:
        if arg == '-v' or arg == '--version':
            parser.exit(message="Petronia v{0}\nRunning Python {1}".format(VERSION, sys.version))

    args = parser.parse_args()

    if args.version:
        parser.exit(message="Petronia v{0}\nRunning Python {1}".format(VERSION, sys.version))

    if args.extensions:
        if os.path.isdir(args.extensions):
            sys.path.append(args.extensions)
        else:
            print("User extensions directory ({0}) does not exist. Skipping.".format(args.extensions))
    elif 'PETRONIA_USER_DIR' in os.environ:
        if os.path.isdir(os.environ['PETRONIA_USER_DIR']):
            sys.path.append(os.environ['PETRONIA_USER_DIR'])
        else:
            print("User extensions directory from environment ({0}) does not exist.  Skipping.".format(
                os.environ['PETRONIA_USER_DIR']))

    if not args.configfile or not os.path.isfile(args.configfile):
        parser.error("Missing configuration file.  Use `-h' to see the full usage.")

    setup(args.configfile, args.layout)


if __name__ == '__main__':
    main_setup(sys.argv)
