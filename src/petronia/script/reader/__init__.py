
import os
from .module import load_module
from .yaml import load_yaml

_REGISTRY = {
    '.py': load_module,
    '.yml': load_yaml,
    '.yaml': load_yaml,
}


def parse_confg(filename, logger):
    core, ext = os.path.splitext(filename)
    if ext in _REGISTRY:
        return _REGISTRY[ext](filename, logger)
    else:
        logger.error("CONFIG ERROR: unknown config file type: {0}".format(filename))
        return None
