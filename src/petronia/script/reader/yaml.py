
import os
from ...util import yaml
from .dict_builder import build_config_loader_from_dict, ConfigLoadException


def load_yaml(config_file, logger):
    file_name = os.path.abspath(config_file)

    try:
        with open(file_name, 'r') as inp:
            contents = yaml.load(inp)
            return build_config_loader_from_dict(config_file, contents, logger)
    except ConfigLoadException as e:
        logger.error('Problem loading configuration file {0}'.format(config_file), e)
        return None
