
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
    return DictLoader(config_name, d, logger)


class DictLoader(object):
    def __init__(self, config_name, d, logger):
        if not isinstance(d, dict):
            raise ConfigLoadException([config_name], "Configuration must be a dictionary")
        self.config_name = config_name
        self.d = d
        self.logger = logger

    def load_config(self):
        section = [self.config_name]
        if 'version' in self.d:
            v = self.d['version']
            if v == 1:
                return v1.load_config(section, self.d, self.logger)
        raise ConfigLoadException(section, "Unknown configuration file version")
