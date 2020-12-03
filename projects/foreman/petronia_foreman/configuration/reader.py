
"""
Reads the configuration file, and puts the data into the correct objects.
"""

from typing import Optional
import configparser
from petronia_common.util import StdRet
from petronia_common.util import i18n as _
from .platform import PlatformSettings
from .foreman import ForemanConfig
from .find_file import get_config_file
from ..constants import TRANSLATION_CATALOG


def read_configuration_file(
        filename: Optional[str], platform: PlatformSettings,
) -> StdRet[ForemanConfig]:
    """
    Parses the configuration file into the configuration.  If the filename is
    not provided, then the default file is searched for (using OS dependent
    path defaults).  If no configuration can be found, then the internal default
    values are returned.

    :param platform:
    :param filename:
    :return:
    """
    config_file = get_config_file(filename, platform)
    if config_file.has_error:
        return config_file.forward()

    parser = configparser.ConfigParser()
    parser.read(config_file.result)

    ret = ForemanConfig()
    res = ret.load_config(parser)
    if res.has_error:
        return res.forward()

    if not ret.get_boot_config().boot_order:
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            _(
                'No boot-order defined in the foreman configuration, so foreman cannot start.  '
                'Did you install Petronia correctly?  Please check the instructions again.  '
                'Petronia expects a file named petronia.ini in an OS-specific location.'
            ),
        )

    return StdRet.pass_ok(ret)
