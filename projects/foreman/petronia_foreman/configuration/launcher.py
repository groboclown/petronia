
"""
The Launcher mapping configuration.

There exists one of these for each launch configuration type.
"""

from typing import Dict
from configparser import ConfigParser
from petronia_common.util import StdRet, RET_OK_NONE
from petronia_common.util import i18n as _
from ..user_message import CATALOG


class LauncherConfig:
    """Configuration for all the launchers.

    A launcher is a well-defined name used by extensions to indicate how it should be launched.
    The launcher configuration defines a process to run.

    At boot time, the foreman process will run the hard-coded "extension-loader" launcher and
    whichever native launcher is appropriate for the platform.  The launchers must connect
    themselves to the communication with the foreman to receive and send events.

    Reusable launchers only start one launcher per permission set, so that it will contain
    multiple running extensions.
    """
    __slots__ = ('launcher_name', 'runner', 'options',)

    def __init__(self, launcher_name: str, configuration: ConfigParser) -> None:
        self.launcher_name = launcher_name
        self.runner = configuration.get(launcher_name, 'runner', fallback='')
        self.options: Dict[str, str] = {}
        for name, value in configuration.items(launcher_name):
            self.options[name] = value

    def get_option(self, key: str) -> StdRet[str]:
        """Get the option, or an error if it isn't registered."""
        if key not in self.options:
            return StdRet.pass_errmsg(
                CATALOG,
                _('launcher {name} does not have required option `{key}` set'),
                name=self.launcher_name,
                key=key,
            )
        ret = self.options.get(key)
        assert isinstance(ret, str)
        return StdRet.pass_ok(ret)

    def validate(self) -> StdRet[None]:
        """Check if the configuration is valid."""
        if not self.runner:
            return StdRet.pass_errmsg(
                CATALOG,
                _("`runner` not specified for launcher {name}"),
                name=self.launcher_name,
            )
        return RET_OK_NONE
