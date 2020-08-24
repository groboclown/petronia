
"""
Reads the configuration file, and puts the data into the correct objects.
"""

from typing import Optional
import configparser
from petronia_common.util import StdRet
from .platform import PlatformSettings
from .foreman import ForemanConfig
from .find_file import get_config_file


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

    return StdRet.pass_ok(ret)
