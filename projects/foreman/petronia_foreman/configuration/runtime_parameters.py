"""
Parameters for launchers that are used by foreman to better understand
the use of the launcher.
"""

from configparser import ConfigParser
from typing import Mapping, Dict
from petronia_common.util import readonly_dict

RuntimeLauncherOptions = Mapping[str, str]
RUNNER_OPTION = 'runner'
STOP_TIMEOUT_OPTION = 'stop-timeout'
STOP_TIMEOUT_DEFAULT = 5.0
FOREMAN_OPTIONS = (
    RUNNER_OPTION,
    STOP_TIMEOUT_OPTION,
)


def get_runner(section: str, config: ConfigParser) -> str:
    """Get the launcher factory."""
    return config.get(section, RUNNER_OPTION, fallback='')


def get_stop_timeout(options: RuntimeLauncherOptions) -> float:
    """Get the time to wait after a stop request before forcing the stop."""
    res = options.get(STOP_TIMEOUT_OPTION)
    if not res:
        return STOP_TIMEOUT_DEFAULT
    try:
        return float(res)
    except (ValueError, TypeError):
        return STOP_TIMEOUT_DEFAULT


def get_launcher_options(section: str, config: ConfigParser) -> RuntimeLauncherOptions:
    """Extract the non-foreman options."""
    ret: Dict[str, str] = {}
    for key, value in config.items(section):
        if key not in FOREMAN_OPTIONS and key[0] != '#':
            ret[key] = value
    return readonly_dict(ret)
