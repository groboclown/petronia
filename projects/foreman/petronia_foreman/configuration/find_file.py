
"""
Finds configuration files based on passed in values or system defaults.

These can be OS dependent for the defaults, and must follow OS-specific guidelines.
"""

from typing import List, Iterable, Optional
import os
from petronia_common.util import i18n as _
from petronia_common.util import StdRet
from . import platform
from ..constants import TRANSLATION_CATALOG as CATALOG


DEFAULT_PETRONIA_CONFIG_FILE_NAMES = (
    os.path.join('petronia.ini'),
    os.path.join('.petronia.ini'),
)

BOOT_EXTENSION_SEARCH_DIRS = (
    os.curdir,
    'boot-extensions',
)


def get_config_file(config_arg: Optional[str]) -> StdRet[str]:
    """
    Find the root configuration file.

    :param config_arg:
    :return:
    """
    if config_arg is not None:
        if os.path.isfile(config_arg):
            return StdRet.pass_ok(config_arg)
        return discover_config_file_in([config_arg])
    return discover_config_file_in(platform.configuration_paths)


def discover_config_file_in(search_path: Iterable[Optional[str]]) -> StdRet[str]:
    """Find the configuration file within the search path."""
    searched: List[str] = []
    for path in search_path:
        if not path:
            continue
        for sub_file in DEFAULT_PETRONIA_CONFIG_FILE_NAMES:
            petronia_file = os.path.join(path, sub_file)
            if os.path.isfile(petronia_file):
                return StdRet.pass_ok(petronia_file)
            searched.append(petronia_file)

    return StdRet.pass_errmsg(
        CATALOG,
        _('Could not find configuration file "petronia.ini" in any of {searched}'),
        searched='; '.join(searched),
    )


def get_boot_extension_file(
        filename: str,
        additional_boot_extension_dir: Optional[str] = None,
) -> StdRet[str]:
    """Discover the location of the boot extension file."""
    extension_dirs = list(BOOT_EXTENSION_SEARCH_DIRS)
    if additional_boot_extension_dir:
        extension_dirs.append(additional_boot_extension_dir)
    fqn = platform.find_data_file(filename, *extension_dirs)
    if fqn:
        return StdRet.pass_ok(fqn)
    return StdRet.pass_errmsg(
        CATALOG,
        _('could not find boot extension file {name}; searched in {path}'),
        path=', '.join(platform.data_paths), name=filename,
    )
