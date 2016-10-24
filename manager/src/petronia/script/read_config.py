
import importlib
from ..config import Config


def read_user_configuration(config_file):
    mod_name = config_file
    if mod_name.endswith('.py'):
        mod_name = mod_name[:-3]
    mod_name = mod_name.replace('\\', '/').replace('/', '.')
    # print("Importing configuration {0}".format(mod_name))
    config_module = importlib.import_module(mod_name)
    if config_module is None or not(hasattr(config_module, 'load_config')) or not callable(config_module.load_config):
        raise Exception("Argument 1 must be a Python file that provides the 'load_config' method.")

    config = config_module.load_config()
    assert isinstance(config, Config)
    return config
