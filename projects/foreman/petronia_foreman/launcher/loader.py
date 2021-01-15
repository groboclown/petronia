"""Loads the launchers."""


from typing import Mapping
from petronia_common.util import StdRet, readonly_dict
from petronia_common.util import i18n as _
from .abc import AbcLauncherCategory, LauncherFactory
from .cmd import create_cmd_launcher
from .memory import create_memory_launcher
from ..configuration import LauncherConfig
from ..user_message import CATALOG


# This should have a better mechanism for defining the registered launchers,
# but this works for now.  Especially since launchers are currently
# directly built into foreman.
IMPLEMENTATIONS: Mapping[str, LauncherFactory] = readonly_dict({
    # 'docker': ,
    'in-memory': create_memory_launcher,
    # 'sandbox': ,
    'cmd-launcher': create_cmd_launcher,
})


def create_launcher_category(
        launcher_configuration: LauncherConfig,
) -> StdRet[AbcLauncherCategory]:
    """Create the launcher, but only if it is valid."""
    launcher_factory = IMPLEMENTATIONS.get(launcher_configuration.runner)
    if not launcher_factory:
        return StdRet.pass_errmsg(
            CATALOG,
            _('Unknown launcher runner {name}'),
            name=launcher_configuration.runner,
        )
    launcher = launcher_factory(launcher_configuration)
    ret_valid = launcher.is_valid()
    if ret_valid.has_error:
        return ret_valid.forward()
    return StdRet.pass_ok(launcher)
