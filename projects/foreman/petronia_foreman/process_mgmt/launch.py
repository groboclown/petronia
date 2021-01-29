
"""
Launch the executable process.
"""

from typing import Sequence, Mapping
from petronia_common.extension.config.extension_schema import ExtensionRuntime
from petronia_common.util import StdRet
from petronia_common.util import i18n as _
from .popen_posix import run_launcher_posix
from .popen_win import run_launcher_windows
from .process import ManagedProcess
from ..configuration import platform
from ..user_message import CATALOG


def run_launcher(
        identity: str,
        params: Mapping[str, str], temp_dir: str,
        extension_runtime: ExtensionRuntime,
        command: Sequence[str], env: Mapping[str, str],
) -> StdRet[ManagedProcess]:
    """Launch the process."""
    if platform.os_category == platform.CATEGORY__WINDOWS:
        return run_launcher_windows(
            identity, command, env, params, temp_dir,
            extension_runtime.requested_permissions,
        )
    if platform.os_category in (platform.CATEGORY__LINUX, platform.CATEGORY__OSX):
        return run_launcher_posix(
            identity, command, env, params, temp_dir,
            extension_runtime.requested_permissions,
        )
    return StdRet.pass_errmsg(
        CATALOG,
        _('Unsupported launch platform {name}'),
        name=platform.platform_name,
    )
