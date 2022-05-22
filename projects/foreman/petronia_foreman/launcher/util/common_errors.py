"""Common error messages."""

from petronia_common.util import StdRet, T
from petronia_common.util import i18n as _
from ...constants import TRANSLATION_CATALOG


def launcher_already_registered(handler_id: str) -> StdRet[T]:
    """Generate an error when the extension handler ID has already been registered."""
    return StdRet.pass_errmsg(
        TRANSLATION_CATALOG,
        _('already registered extension with id {name}'),
        name=handler_id,
    )


def launcher_not_loaded(handler_id: str) -> StdRet[T]:
    """Generate an error when the extension handler ID has not been registered."""
    return StdRet.pass_errmsg(
        TRANSLATION_CATALOG,
        _('extension with id {name} not registered'),
        name=handler_id,
    )


def launcher_category_not_initialized() -> StdRet[T]:
    """Generate an error for when the launcher category is asked to start a launcher but the
    category hasn't been initialized yet."""
    return StdRet.pass_errmsg(
        TRANSLATION_CATALOG,
        _('Launcher category not initialized'),
    )


def launcher_stopped() -> StdRet[T]:
    """Generate an error for when the launcher has already been stopped."""
    return StdRet.pass_errmsg(
        TRANSLATION_CATALOG,
        _('Launcher already stopped'),
    )
