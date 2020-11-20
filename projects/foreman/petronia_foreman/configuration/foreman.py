
"""
Structural definition for the contents of the Foreman configuration.


"""

from typing import Dict, List, Optional
from configparser import ConfigParser
from petronia_common.util import StdRet, RET_OK_NONE, collect_errors_from
from petronia_common.util import i18n as _
from .launcher import LauncherConfig
from ..user_message import CATALOG


class ForemanConfig:
    """
    The Foreman Process configuration.

    This contains:
        - The "launcher" types.  Each launcher type describes a method for setting up and
            running a particular extension type.
    """
    __slots__ = ('_launcher_mapper', '_root_log_file')

    def __init__(self) -> None:
        self._launcher_mapper: Dict[str, LauncherConfig] = {}
        self._root_log_file: Optional[str] = None

    def get_root_log_file(self) -> Optional[str]:
        """Get the root log file for the basics of foreman."""
        return self._root_log_file

    def load_config(self, *configs: ConfigParser) -> StdRet[None]:
        """Load the configurations.
        These are ordered in priority order - least important is first.
        """
        self._launcher_mapper.clear()

        for config in configs:
            for section_name in config.sections():
                inner_section_name = section_name.lower()
                self._launcher_mapper[inner_section_name] = LauncherConfig(
                    section_name, config,
                )

        errs = collect_errors_from(
            [launcher.validate() for launcher in self._launcher_mapper.values()],
        )
        if errs:
            return StdRet.pass_error(errs)

        return RET_OK_NONE

    def get_registered_launcher_config_names(self) -> List[str]:
        """Get all registered launcher configuration names."""
        return list(self._launcher_mapper.keys())

    def get_launcher_config(self, name: str) -> StdRet[LauncherConfig]:
        """Fetch the boot launcher configurations."""
        if name not in self._launcher_mapper:
            return StdRet.pass_errmsg(
                CATALOG,
                _('No launcher named {name}.'),
                name=name,
            )
        ret = self._launcher_mapper[name]
        valid = ret.validate()
        if not valid:
            return valid.forward()
        return StdRet.pass_ok(ret)
