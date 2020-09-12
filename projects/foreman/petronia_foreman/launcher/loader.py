"""Loads the launchers."""


from typing import Dict
from petronia_common.util import StdRet, RET_OK_NONE
from petronia_common.util import i18n as _
from .abc import AbcLauncher, LauncherFactory


IMPLEMENTATIONS: Dict[str, LauncherFactory] = {
    # 'docker': ,
}


def create_launcher(launcher_impl: str, options: Dict[str, str]) -> StdRet[AbcLauncher]:
    """Create the launcher, but only if it is valid."""
    launcher_factory = IMPLEMENTATIONS.get(launcher_impl)
    if not launcher_factory:
        return StdRet.pass_errmsg(
            _('Unknown launcher implementation {name}'),
            name=launcher_impl,
        )
    launcher = launcher_factory(options)
    ret_valid = launcher.is_valid()
    if ret_valid.has_error:
        return ret_valid.forward()
    return StdRet.pass_ok(launcher)


def is_valid(launcher_impl: str, options: Dict[str, str]) -> StdRet[None]:
    """Check if the launcher + configuration is valid."""
    launcher = create_launcher(launcher_impl, options)
    if launcher.has_error:
        return launcher.forward()
    return RET_OK_NONE
