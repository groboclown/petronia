
from typing import Optional
import os
import platform
from petronia_common.util import i18n as _
from petronia_common.util import StdRet, with_message, no_error


def get_config_file(config_arg: Optional[str]) -> StdRet[str]:
    if config_arg is not None:
        if os.path.isfile(config_arg):
            return no_error(config_arg)
        return with_message(_('Cannot find configuration file {name}'), name=config_arg)

    # OS dependent detection of install location.
    if platform.system() in ('linux', 'Linux', 'posix', 'Posix'):
        return discover_linux_config_file()

    if platform.system() in ('windows', 'Windows',):
        return discover_windows_config_file()

    return with_message(_(
        'Petronia does not support your platform ({platform}).'
    ), platform=platform.system())


def discover_linux_config_file() -> StdRet[str]:
    raise NotImplementedError()


def discover_windows_config_file() -> StdRet[str]:
    raise NotImplementedError()
