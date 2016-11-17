
from .exceptions import ConfigLoadException
from . import v1


def build_config_loader_from_dict(config_name, d, logger):
    """
    Allows building a configuration from a dictionary structure.
    This way, you can use any kind of these data format file types to load
    the configuration.

    :param config_name:
    :param d:
    :param logger:
    :return:
    """
    section = [config_name]
    if not isinstance(d, dict):
        raise ConfigLoadException(section, "Configuration must be a dictionary")
    if 'version' in d:
        v = d['version']
        if v == 1:
            return v1.load_config(section, d, logger)
    raise ConfigLoadException(section, "Unknown configuration file version")
