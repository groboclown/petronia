"""
Sets up the runner.
"""

from typing import Dict, List, Tuple, Optional, Any
import os
import sys
import tempfile
import shutil
import atexit
from petronia_common.util import StdRet, load_structured_file

HANDLER_ID = '<unset>'
USER_CONFIG_PATH: List[str] = []
DATA_PATH: List[str] = []
TEMP_DIR = os.curdir
EXTENSION_NAME = '<unset>'
ENTRYPOINT_NAME = 'extension_entrypoint'


def initialize(  # pylint:disable=keyword-arg-before-vararg
        handler_id: Optional[str] = None,
        user_config_path: Optional[str] = None,
        data_path: Optional[str] = None,
        temp_dir: Optional[str] = None,
        extension_name: Optional[str] = None,
        config_file: Optional[str] = None,
        *others: str,
) -> StdRet[Tuple[List[str], Dict[str, Any]]]:
    """Initialize the user settings.  Can be called multiple times."""

    # Load the configuration file.
    config: Dict[str, Any] = {}
    if config_file:
        config_res = load_structured_file(config_file)
        if config_res.has_error:
            return config_res.forward()
        loaded_config = config_res.result
        if isinstance(loaded_config, dict):
            config = loaded_config
        else:
            # The load structured file returns either a dictionary or a sequence.
            config_list = list(loaded_config)
            if len(config_list) > 0 and isinstance(config_list[0], dict):
                config = config_list[0]

    global HANDLER_ID, TEMP_DIR, EXTENSION_NAME  # pylint:disable=global-statement
    HANDLER_ID = handler_id or '<unset>'
    if temp_dir and os.path.isdir(temp_dir):
        TEMP_DIR = temp_dir
    else:
        TEMP_DIR = tempfile.mkdtemp()
        atexit.register(shutil.rmtree, TEMP_DIR, ignore_errors=True)
    EXTENSION_NAME = extension_name or '<unset>'

    USER_CONFIG_PATH.clear()
    USER_CONFIG_PATH.extend((user_config_path or os.curdir).split(os.pathsep))

    DATA_PATH.clear()
    DATA_PATH.extend((data_path or os.curdir).split(os.pathsep))

    return StdRet.pass_ok((list(others), config))


def get_module_name() -> str:
    """Get the Python module name.  See the __init__ file for the standard."""
    return EXTENSION_NAME


def get_entrypoint_name() -> str:
    """Get the name of the function that acts as the entrypoint for the extension in the module."""
    return ENTRYPOINT_NAME


def get_python_path() -> List[str]:
    """Get the Python path used for loading Python modules."""
    return list(sys.path)
