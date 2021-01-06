"""Common error messages."""

from petronia_common.util import StdRet, T
from petronia_common.util import i18n as _
from ...constants import TRANSLATION_CATALOG


def no_such_launcher_id(launcher_id: str) -> StdRet[T]:
    """Generate an error when the launcher ID is not registered."""
    return StdRet.pass_errmsg(
        TRANSLATION_CATALOG,
        _('No registered launcher {launcher_id}'),
        launcher_id=launcher_id,
    )


def launcher_already_registered(launcher_id: str) -> StdRet[T]:
    """Generate an error when the launcher ID has already been registered."""
    return StdRet.pass_errmsg(
        TRANSLATION_CATALOG,
        _('already registered launcher id {name}'),
        name=launcher_id,
    )


def launcher_category_not_initialized() -> StdRet[T]:
    """Generate an error for when the launcher category is asked to start a launcher but the
    category hasn't been initialized yet."""
    return StdRet.pass_errmsg(
        TRANSLATION_CATALOG,
        _('Launcher category not initialized'),
    )


def started_extension_from_boot_launcher(launcher_id: str) -> StdRet[T]:
    """Generate an error due to trying to start an extension from a boot launcher."""
    return StdRet.pass_errmsg(
        TRANSLATION_CATALOG,
        _('cannot load an extension in a boot launcher ({launcher_id}).'),
        launcher_id=launcher_id,
    )
