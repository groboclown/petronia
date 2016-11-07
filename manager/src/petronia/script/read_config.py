
import os
import importlib
import traceback
from ..config import Config, HotKeyConfig, DEFAULT_MODE

_LOADED_MODULES = {}
_MODULE_NAMES = []


def read_user_configuration(config_file):
    """

    :param config_file: the name of the configuration file to load.
    :return: the user configuration.  Will not be None, will be of type Config.
    :rtype: Config
    """

    config_module = _load_module(config_file)
    if config_module is None:
        # Errors already reported
        config = None
    elif not(hasattr(config_module, 'load_config')) or not callable(config_module.load_config):
        # TODO Better error logging
        print("CONFIG ERROR: Problem loading {0} - it does not provide the function `load_config()`".format(
            config_file))
        config = None
    else:
        try:
            config = config_module.load_config()
            if not isinstance(config, Config):
                # TODO Better error logging
                print("CONFIG ERROR: {0} provided `load_config()`, but it did not return a Config type.".format(
                    config_file))
                config = None
        except BaseException as e:
            # TODO Better error logging
            print("CONFIG ERROR: Problem loading {0}".format(config_file))
            traceback.print_exc(e)
            config = None

    if config is None:
        config = _create_default_config()
    assert isinstance(config, Config)
    return config


def _load_module(config_file):
    file_name = os.path.abspath(config_file)

    # This doesn't work right...
    # if file_name in _LOADED_MODULES:
    #     config_module = _LOADED_MODULES[file_name]
    #     try:
    #         importlib.reload(config_module)
    #         return config_module
    #     except BaseException as e:
    #         print("CONFIG ERROR: Problem reloading {0}".format(config_file))
    #         traceback.print_exc(e)
    #         return None

    index = 0
    module_name = "user_config_mod0"
    while module_name in _MODULE_NAMES:
        index += 1
        module_name = "user_config_mod{0}".format(index)
    try:
        spec = importlib.util.spec_from_file_location(module_name, file_name)
        config_module = importlib.util.module_from_spec(spec)
        if config_module is not None:
            spec.loader.exec_module(config_module)
            _LOADED_MODULES[file_name] = config_module
        else:
            print("CONFIG ERROR: Unknown problem loading module {0} from {1}".format(module_name, file_name))
        return config_module
    except BaseException as e:
        # TODO Better error logging
        print("CONFIG ERROR: Problem loading {0}".format(config_file))
        traceback.print_exc(e)
        return None


def _create_default_config():
    # We need a way to kill the application, even if the config isn't loaded right.

    # Need to be able to stop the program.
    hotkeys = HotKeyConfig()
    hotkeys.parse_hotkey_mode_keys(
        DEFAULT_MODE,
        [
            "win+f4 => quit",
        ]
    )

    return Config(hotkeys=hotkeys)
