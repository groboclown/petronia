"""API for working with xcb"""

from typing import Tuple, Callable, Optional, Any
from petronia_common.util import StdRet


def _not_implemented() -> Any:
    raise NotImplemented('not implemented')


class UIFunctions:
    """Basic X11 UI interaction functions."""
    __slots__ = (
        'connect',
    )

    def __init__(self) -> None:
        self.connect: Callable[
            [], StdRet[None],
        ] = lambda: _not_implemented()


class LibFunctions:
    __slots__ = (
        '__ui',
    )

    def __init__(self) -> None:
        self.__ui = UIFunctions()

    @property
    def ui(self) -> UIFunctions:
        """UI function interfaces"""
        return self.__ui
