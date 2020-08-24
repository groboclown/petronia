
"""
Launch the executable process.
"""

from typing import List, Tuple
import os
import tempfile
from petronia_common.extension.config.extension_schema import ExtensionRuntime
from petronia_common.util import StdRet
from petronia_common.util import i18n as _
from .process import ManagedProcess
from .popen_win import run_launcher_windows
from .popen_posix import run_launcher_posix
from ..configuration.foreman import ForemanConfig
from ..configuration.platform import PlatformSettings, CATEGORY__WINDOWS, CATEGORY__LINUX


async def run_launcher(
        identity: str,
        extension_runtime: ExtensionRuntime,
        foreman_config: ForemanConfig,
        platform: PlatformSettings,
) -> StdRet[ManagedProcess]:
    """Launch the process."""
    ret_launcher_config = foreman_config.get_launcher(extension_runtime.launcher)
    if ret_launcher_config.has_error:
        return ret_launcher_config.forward()
    launcher_config = ret_launcher_config.result

    if platform.category == CATEGORY__WINDOWS:
        return await run_launcher_windows(
            identity, launcher_config, platform,
            extension_runtime.requested_permissions,
        )
    if platform.category == CATEGORY__LINUX:
        return await run_launcher_posix(
            identity, launcher_config, platform,
            extension_runtime.requested_permissions,
        )
    return StdRet.pass_errmsg(
        _('Unsupported launch platform {name}'),
        name=platform.name,
    )


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
