"""Event loop handler."""

from petronia_common.util import StdRet
from .handler import Hooks


def setup(hooks: Hooks) -> StdRet[None]:
    """Set up the events."""
    pass
