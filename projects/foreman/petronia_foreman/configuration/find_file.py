
"""
Finds configuration files based on passed in values or system defaults.

These can be OS dependent for the defaults, and must follow OS-specific guidelines.
"""

from typing import Optional
import os
import platform
from petronia_common.util import i18n as _
from petronia_common.util import StdRet


def get_config_file(config_arg: Optional[str]) -> StdRet[str]:
    """
    Find the root configuration file.

    :param config_arg:
    :return:
    """
    if config_arg is not None:
        if os.path.isfile(config_arg):
            return StdRet.pass_ok(config_arg)
        return StdRet.pass_errmsg(_('Cannot find configuration file {name}'), name=config_arg)

    # OS dependent detection of install location.
    if platform.system() in ('linux', 'Linux', 'posix', 'Posix'):
        return discover_linux_config_file()

    if platform.system() in ('windows', 'Windows',):
        return discover_windows_config_file()

    return StdRet.pass_errmsg(_(
        'Petronia does not support your platform ({platform}).'
    ), platform=platform.system())


def discover_linux_config_file() -> StdRet[str]:
    """
    Find the default root configuration file for Linux systems.

    :return:
    """
    raise NotImplementedError()


def discover_windows_config_file() -> StdRet[str]:
    """
    Find the default root configuration file for Windows systems.

    :return:
    """
    raise NotImplementedError()
