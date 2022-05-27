"""Standard calls for handlers used by x11 window manager."""

from typing import List, Sequence, Callable
from petronia_common.util import StdRet
from .api import XcbApi


class Hooks:
    """Registered hooks for the handler."""
    __slots__ = (
        '__initializers',
        '__shutdown',
        '__event_hooks',
    )

    def __init__(
            self, *,
            initializers: List[Callable[[XcbApi], StdRet[None]]],
            shutdown: List[Callable[[XcbApi, float], StdRet[None]]],
    ) -> None:
        self.__initializers = initializers
        self.__shutdown = shutdown

    def add_initializer(self, callback: Callable[[XcbApi], StdRet[None]]) -> None:
        """Add an initializer for the hook."""
        self.__initializers.append(callback)

    def add_shutdown(self, callback: Callable[[XcbApi, float], StdRet[None]]) -> None:
        """Add a shutdown hook."""
        self.__shutdown.append(callback)


class HookManager:
    """Manages working with hooks"""
    __slots__ = (
        '__initializers',
        '__shutdown',
    )

    def __init__(self) -> None:
        self.__initializers: List[Callable[[XcbApi], StdRet[None]]] = []
        self.__shutdown: List[Callable[[XcbApi, float], StdRet[None]]] = []

    def for_hook(self) -> Hooks:
        """Create the hook interface."""
        return Hooks(
            initializers=self.__initializers,
            shutdown=self.__shutdown,
        )

    @property
    def initializers(self) -> Sequence[Callable[[XcbApi], StdRet[None]]]:
        """Get the initializers"""
        return tuple(self.__initializers)

    @property
    def shutdown(self) -> Sequence[Callable[[XcbApi, float], StdRet[None]]]:
        """Get the shutdown hooks"""
        return tuple(self.__shutdown)
