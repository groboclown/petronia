"""Graphics context setup handler."""

from petronia_common.util import StdRet
from .hook_manager import Hooks


class GraphicsContextApi:
    """The API for accessing the graphics context."""


def setup_grapics_context(hooks: Hooks) -> StdRet[GraphicsContextApi]:
    """Set up the graphics context."""

    # generate graphics context

    # desktop / wallpaper setup

    return StdRet.pass_ok(GraphicsContextApi())
