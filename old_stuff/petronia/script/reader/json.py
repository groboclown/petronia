
import os
import json
from .dict_builder import build_config_loader_from_dict, ConfigLoadException


def load_json(config_file, logger):
    file_name = os.path.abspath(config_file)

    try:
        with open(file_name, 'r') as inp:
            contents = json.load(inp)
            return build_config_loader_from_dict(config_file, contents, logger)
    except ConfigLoadException as e:
        logger.error('Problem loading configuration file {0}'.format(config_file), e)
        return None
