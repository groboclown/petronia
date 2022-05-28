"""Petronia UI setup handler."""

from petronia_common.util import StdRet
from .hook_manager import Hooks


class PetroniaUiApi:
    """The API for accessing the graphics context."""


def setup_petronia_ui(hooks: Hooks) -> StdRet[PetroniaUiApi]:
    """Set up the graphics context."""

    # desktop / wallpaper setup

    return StdRet.pass_ok(PetroniaUiApi())
