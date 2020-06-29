
import os
from .module import load_module
from .yaml import load_yaml
from .json import load_json

_REGISTRY = {
    '.py': load_module,
    '.json': load_json,
    '.yml': load_yaml,
    '.yaml': load_yaml,
}


def parse_config(filename, logger):
    core, ext = os.path.splitext(filename)
    if ext in _REGISTRY:
        return _REGISTRY[ext](filename, logger)
    else:
        logger.error("CONFIG ERROR: unknown config file type: {0}".format(filename))
        return None
