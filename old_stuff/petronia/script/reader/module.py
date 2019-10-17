
import os
from importlib.util import spec_from_file_location
from importlib.util import module_from_spec

_LOADED_MODULES = {}
_MODULE_NAMES = []


def load_module(config_file, logger):
    file_name = os.path.abspath(config_file)

    index = 0
    module_name = "user_config_mod0"
    while module_name in _MODULE_NAMES:
        index += 1
        module_name = "user_config_mod{0}".format(index)
    try:
        spec = spec_from_file_location(module_name, file_name)
        config_module = module_from_spec(spec)
        if config_module is not None:
            spec.loader.exec_module(config_module)
            _LOADED_MODULES[file_name] = config_module
        else:
            logger.error("CONFIG ERROR: Unknown problem loading module {0} from {1}".format(module_name, file_name))
        return config_module
    except BaseException as e:
        logger.error("CONFIG ERROR: Problem loading {0}".format(config_file), e)
        return None
