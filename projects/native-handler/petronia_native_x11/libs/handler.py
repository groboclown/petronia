"""Standard calls for handlers used by x11 window manager."""

from typing import List, Callable
from petronia_common.util import StdRet
from .api import XcbApi


class Hooks:
    """Registered hooks for the handler."""
    __slots__ = (
        '__initializers',
    )

    def __init__(
            self, *,
            initializers: List[Callable[[XcbApi], StdRet[None]]]
    ) -> None:
        self.__initializers = initializers

    def add_initializer(self, callback: Callable[[XcbApi], StdRet[None]]) -> None:
        """Add an initializer for the hook."""
        self.__initializers.append(callback)


class HookManager:
    """Manages working with hooks"""
    __slots__ = (
        '__initializers',
    )

    def __init__(self) -> None:
        self.__initializers: List[Callable[[XcbApi], StdRet[None]]] = []

    def for_hook(self) -> Hooks:
        """Create the hook interface."""
        return Hooks(
            initializers=self.__initializers,
        )
