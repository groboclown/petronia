"""Dbus handler."""

from petronia_common.util import StdRet, RET_OK_NONE
from .hook_manager import Hooks


class DbusApi:
    """API stuff for dbus."""
    __slots__ = ()


def setup_dbus(hooks: Hooks) -> StdRet[DbusApi]:
    """Set up dbus."""
    return StdRet.pass_ok(DbusApi())
