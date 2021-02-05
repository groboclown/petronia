"""Loads the launchers."""


from typing import Dict
from petronia_common.util import StdRet
from petronia_common.util import i18n as _
from .abc import AbcLauncherCategory, RuntimeFactory
from .cmd import create_cmd_launcher
from .memory import create_memory_launcher
from ..configuration import RuntimeConfig
from ..user_message import CATALOG

# Extensions with a runtime launcher equal to this string
# are marker extension files, and are intended instead to
# be loaded through the boot mechanism.
INTERNAL_EXTENSION_RUNTIME = '<internal>'


# This should have a better mechanism for defining the registered launchers,
# but this works for now.  Especially since launchers are currently
# directly built into foreman.
# For safety purposes, this should be a Mapping, but for unit test purposes it's a dict.
# IMPLEMENTATIONS: Mapping[str, RuntimeFactory] = readonly_dict({
IMPLEMENTATIONS: Dict[str, RuntimeFactory] = {
    # 'docker': ,
    'in-memory': create_memory_launcher,
    # 'sandbox': ,
    'cmd-launcher': create_cmd_launcher,
}
# )


def create_launcher_category(
        runtime_configuration: RuntimeConfig,
) -> StdRet[AbcLauncherCategory]:
    """Create the launcher, but only if it is valid."""
    launcher_factory = IMPLEMENTATIONS.get(runtime_configuration.runner)
    if not launcher_factory:
        return StdRet.pass_errmsg(
            CATALOG,
            _('Unknown runner {name}'),
            name=runtime_configuration.runner,
        )
    launcher = launcher_factory(runtime_configuration)
    ret_valid = launcher.is_valid()
    if ret_valid.has_error:
        return ret_valid.forward()
    return StdRet.pass_ok(launcher)
