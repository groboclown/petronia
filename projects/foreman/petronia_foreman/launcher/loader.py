"""Loads the launchers."""


from typing import Dict
from petronia_common.util import StdRet
from petronia_common.util import i18n as _
from .abc import AbcLauncherCategory, LauncherFactory
from ..user_message import CATALOG


IMPLEMENTATIONS: Dict[str, LauncherFactory] = {
    # 'docker': ,
}


def create_launcher_category(
        launcher_category: str, options: Dict[str, str],
) -> StdRet[AbcLauncherCategory]:
    """Create the launcher, but only if it is valid."""
    launcher_factory = IMPLEMENTATIONS.get(launcher_category)
    if not launcher_factory:
        return StdRet.pass_errmsg(
            CATALOG,
            _('Unknown launcher category {name}'),
            name=launcher_category,
        )
    launcher = launcher_factory(options)
    ret_valid = launcher.is_valid()
    if ret_valid.has_error:
        return ret_valid.forward()
    return StdRet.pass_ok(launcher)
