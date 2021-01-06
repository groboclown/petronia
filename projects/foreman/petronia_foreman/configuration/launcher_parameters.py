"""
Parameters for launchers that are used by foreman to better understand
the use of the launcher.
"""
from configparser import ConfigParser
from typing import Mapping, Dict, Optional
from petronia_common.util import readonly_dict


LauncherOptions = Mapping[str, str]
BOOT_CHANNEL_OPTION = 'boot-channel'
RUNNER_OPTION = 'runner'
IS_BOOT_LAUNCHER_OPTION = '#is-boot-launcher'
IS_BOOT_LAUNCHER_VALUE = 'yes'
STOP_TIMEOUT_OPTION = 'stop-timeout'
STOP_TIMEOUT_DEFAULT = 5.0
FOREMAN_OPTIONS = (
    BOOT_CHANNEL_OPTION,
    RUNNER_OPTION,
    STOP_TIMEOUT_OPTION,
)


def get_boot_channel(section: str, config: ConfigParser) -> Optional[str]:
    """Get the specified boot channel for the launcher.  Launchers
    that do not have this are not bootable."""
    return config.get(section, BOOT_CHANNEL_OPTION, fallback='') or None


def get_runner(section: str, config: ConfigParser) -> str:
    """Get the launcher factory."""
    return config.get(section, RUNNER_OPTION, fallback='')


def is_boot_launcher(options: LauncherOptions) -> bool:
    """According to the options, is this a boot launcher?"""
    return options.get(IS_BOOT_LAUNCHER_OPTION) == IS_BOOT_LAUNCHER_VALUE


def get_stop_timeout(options: LauncherOptions) -> float:
    """Get the time to wait after a stop request before forcing the stop."""
    res = options.get(STOP_TIMEOUT_OPTION)
    if not res:
        return STOP_TIMEOUT_DEFAULT
    try:
        return float(res)
    except (ValueError, TypeError):
        return STOP_TIMEOUT_DEFAULT


def get_launcher_options(section: str, config: ConfigParser) -> LauncherOptions:
    """Extract the non-foreman options."""
    ret: Dict[str, str] = {}
    for key, value in config.items(section):
        if key not in FOREMAN_OPTIONS and key[0] != '#':
            ret[key] = value
        elif key == BOOT_CHANNEL_OPTION:
            ret[IS_BOOT_LAUNCHER_OPTION] = IS_BOOT_LAUNCHER_VALUE
    return readonly_dict(ret)
