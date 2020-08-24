
"""Shared utilities."""

from typing import Tuple, List
import os
import tempfile
from petronia_foreman.configuration import PlatformSettings


def create_cmd_and_dirs(
        command: str,
        platform: PlatformSettings,
        child_fd: int,
) -> Tuple[str, List[str]]:
    """Create the command argument and the temporary directories."""
    temp_dirs: List[str] = []
    if '${TEMP_DIR}' in command:
        temp_dirs.append(tempfile.mkdtemp())
        command = command.replace('${TEMP_DIR}', temp_dirs[0])
    if '${DATA_PATH}' in command:
        command = command.replace(
            '${DATA_PATHS}',
            os.path.pathsep.join(platform.data_paths)
        )
    if '${CONFIG_PATH}' in command:
        command = command.replace(
            '${DATA_PATHS}',
            os.path.pathsep.join(platform.config_paths)
        )
    if '${WRITE_FD}' in command:
        command = command.replace('${WRITE_FD}', str(child_fd))
    return command, temp_dirs
