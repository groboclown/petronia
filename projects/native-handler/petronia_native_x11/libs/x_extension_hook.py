"""extension setup handler."""

from petronia_common.util import StdRet
from .handler import Hooks


def setup(hooks: Hooks) -> StdRet[None]:
    """Set up the extensions."""

    # check for each needed extension
    #  - xtest
    #  - shape
    #  - xfixes

    pass
