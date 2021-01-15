
"""Shared utilities."""

from typing import Tuple, Sequence, List
import os
import tempfile
from petronia_foreman.configuration import PlatformSettings


def create_cmd_and_dirs(
        command: Sequence[str],
        platform: PlatformSettings,
        child_fd: int,
) -> Tuple[Sequence[str], List[str]]:
    """Create the command argument and the temporary directories."""
    temp_dirs: List[str] = []
    ret_cmd: List[str] = []
    for cmd_part in command:
        if '${TEMP_DIR}' in cmd_part:
            temp_dirs.append(tempfile.mkdtemp())
            cmd_part = cmd_part.replace('${TEMP_DIR}', temp_dirs[0])
        if '${DATA_PATH}' in cmd_part:
            cmd_part = cmd_part.replace(
                '${DATA_PATH}',
                os.path.pathsep.join(platform.data_paths)
            )
        if '${CONFIG_PATH}' in cmd_part:
            cmd_part = cmd_part.replace(
                '${CONFIG_PATH}',
                os.path.pathsep.join(platform.config_paths)
            )
        if '${WRITE_FD}' in cmd_part:
            cmd_part = cmd_part.replace('${WRITE_FD}', str(child_fd))
        ret_cmd.append(cmd_part)
    return ret_cmd, temp_dirs
