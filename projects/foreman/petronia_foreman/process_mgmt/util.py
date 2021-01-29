
"""Shared utilities."""

from typing import Mapping, Sequence, List
import os
from ..configuration import platform


def create_cmd(
        command: Sequence[str],
        temp_dir: str, other_params: Mapping[str, str],
        child_fd: int,
) -> Sequence[str]:
    """Create the command argument and the temporary directories."""
    params = {
        '${' + key.upper() + '}': value
        for key, value in other_params.items()
    }
    params['${DATA_PATH'] = os.path.pathsep.join(platform.data_paths)
    params['${CONFIG_PATH}'] = os.path.pathsep.join(platform.configuration_paths)
    params['${TEMP_DIR}'] = os.path.abspath(temp_dir)
    params['${WRITE_FD}'] = str(child_fd)

    ret_cmd: List[str] = []
    for cmd_part in command:
        for key, value in params.items():
            if key in cmd_part:
                cmd_part = cmd_part.replace(key, value)
        ret_cmd.append(cmd_part)
    return ret_cmd
