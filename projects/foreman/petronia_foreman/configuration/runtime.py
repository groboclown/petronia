
"""
The Launcher mapping configuration.

There exists one of these for each runtime configuration type.
"""

from configparser import ConfigParser
from petronia_common.util import StdRet, RET_OK_NONE
from petronia_common.util import i18n as _
from . import runtime_parameters
from ..constants import TRANSLATION_CATALOG as CATALOG


class RuntimeConfig:
    """Configuration for all the runtime launchers.

    A launcher is a well-defined name used by extensions to indicate how it should be launched.
    The launcher configuration defines a process to run.

    At boot time, the foreman process will run the hard-coded "extension-loader" launcher and
    whichever native launcher is appropriate for the platform.  The launchers must connect
    themselves to the communication with the foreman to receive and send events.

    Reusable launchers only start one launcher per permission set, so that it will contain
    multiple running extensions.
    """
    __slots__ = ('__launcher_name', '__runner', '__options',)

    def __init__(self, launcher_name: str, configuration: ConfigParser) -> None:
        self.__launcher_name = launcher_name
        self.__runner = runtime_parameters.get_runner(launcher_name, configuration)
        self.__options = runtime_parameters.get_launcher_options(launcher_name, configuration)

    @property
    def runtime_name(self) -> str:
        """The name of the launcher, as defined in the petronia ini section title."""
        return self.__launcher_name

    @property
    def runner(self) -> str:
        """The name of the runner defined in the ini file."""
        return self.__runner

    @property
    def options(self) -> runtime_parameters.RuntimeLauncherOptions:
        """Additional options defined for the runtime launcher."""
        return self.__options

    def get_option(self, key: str) -> StdRet[str]:
        """Get the option, or an error if it isn't registered."""
        if key not in self.options:
            return StdRet.pass_errmsg(
                CATALOG,
                _('runtime {name} does not have required option `{key}` set'),
                name=self.runtime_name,
                key=key,
            )
        ret = self.options.get(key)
        return StdRet.pass_ok(str(ret))

    def validate(self) -> StdRet[None]:
        """Check if the configuration is valid."""
        if not self.runner:
            return StdRet.pass_errmsg(
                CATALOG,
                _("`runner` not specified for launcher {name}"),
                name=self.runtime_name,
            )
        return RET_OK_NONE