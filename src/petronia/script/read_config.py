
import traceback
from ..config import Config, HotKeyConfig, DEFAULT_MODE
from . import reader

_LOADED_MODULES = {}
_MODULE_NAMES = []


def read_user_configuration(config_file, logger):
    """

    :param config_file: the name of the configuration file to load.
    :return: the user configuration.  Will not be None, will be of type Config.
    :rtype: Config
    """

    config_module = reader.parse_config(config_file, logger)
    if config_module is None:
        # Errors already reported
        config = None
    elif not(hasattr(config_module, 'load_config')) or not callable(config_module.load_config):
        logger.error("CONFIG ERROR: Problem loading {0} - it does not provide the function `load_config()`".format(
            config_file))
        config = None
    else:
        try:
            config = config_module.load_config()
            if not isinstance(config, Config):
                logger.error("CONFIG ERROR: {0} provided `load_config()`, but it did not return a Config type.".format(
                    config_file))
                config = None
        except BaseException as e:
            logger.error("CONFIG ERROR: Problem loading {0}".format(config_file))
            traceback.print_exception(e, e, e)
            config = None

    if config is None:
        config = _create_default_config()
    assert isinstance(config, Config)
    config.init_options['config-file'] = config_file
    return config


def _create_default_config():
    # We need a way to kill the application, even if the config isn't loaded right.

    # Need to be able to stop the program.
    hotkeys = HotKeyConfig()
    hotkeys.parse_hotkey_mode_keys(
        DEFAULT_MODE,
        {
            "win+f4": ["quit"],
        }
    )

    return Config(hotkeys=hotkeys)
