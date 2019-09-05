
"""
Handle the finding, parsing, and sending of all the configurations.
"""

from typing import Iterable
from .find_configs import find_extension_config_files
from .load_config import load_config_file
from .send_configs import send_config
from ....aid.simp import (
    EventBus,
)


def handle_config_paths(bus: EventBus, paths: Iterable[str]) -> None:
    """
    Handle finding all the configuration files, parsing them, and sending them
    to the right target.
    """
    for config_file in find_extension_config_files(paths, True):
        for config in load_config_file(config_file):
            send_config(bus, config)
