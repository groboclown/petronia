"""Standard calls for handlers used by x11 window manager."""

from typing import List, Sequence, Callable
from petronia_common.util import StdRet
from .api import XcbApi, EventCallback


class Hooks:
    """Registered hooks for the handler."""
    __slots__ = (
        '__screen_initializers',
        '__pre_event_initializers',
        '__event_hooks',
        '__shutdown',
    )

    def __init__(
            self, *,
            screen_initializers: List[Callable[[XcbApi], StdRet[None]]],
            pre_event_initializers: List[Callable[[XcbApi], StdRet[None]]],
            event_hooks: List[EventCallback],
            shutdown: List[Callable[[XcbApi, float], StdRet[None]]],
    ) -> None:
        self.__screen_initializers = screen_initializers
        self.__pre_event_initializers = pre_event_initializers
        self.__event_hooks = event_hooks
        self.__shutdown = shutdown

    def add_screen_initializer(self, callback: Callable[[XcbApi], StdRet[None]]) -> None:
        """Add an initializer for the hook."""
        self.__screen_initializers.append(callback)

    def add_pre_event_initializer(self, callback: Callable[[XcbApi], StdRet[None]]) -> None:
        """Add an initializer for the hook."""
        self.__pre_event_initializers.append(callback)

    def add_event_callback(self, callback: EventCallback) -> None:
        """Add an event callback."""
        self.__event_hooks.append(callback)

    def add_shutdown(self, callback: Callable[[XcbApi, float], StdRet[None]]) -> None:
        """Add a shutdown hook."""
        self.__shutdown.append(callback)


class HookManager:
    """Manages working with hooks"""
    __slots__ = (
        '__screen_initializers',
        '__pre_event_initializers',
        '__event_hooks',
        '__shutdown',
    )

    def __init__(self) -> None:
        self.__screen_initializers: List[Callable[[XcbApi], StdRet[None]]] = []
        self.__shutdown: List[Callable[[XcbApi, float], StdRet[None]]] = []
        self.__pre_event_initializers: List[Callable[[XcbApi], StdRet[None]]] = []
        self.__event_hooks: List[EventCallback] = []

    def for_hook(self) -> Hooks:
        """Create the hook interface."""
        return Hooks(
            screen_initializers=self.__screen_initializers,
            pre_event_initializers=self.__pre_event_initializers,
            event_hooks=self.__event_hooks,
            shutdown=self.__shutdown,
        )

    @property
    def screen_initializers(self) -> Sequence[Callable[[XcbApi], StdRet[None]]]:
        """Get the initializers"""
        return tuple(self.__screen_initializers)

    @property
    def pre_event_initializers(self) -> Sequence[Callable[[XcbApi], StdRet[None]]]:
        """Get the initializers"""
        return tuple(self.__pre_event_initializers)

    @property
    def shutdown(self) -> Sequence[Callable[[XcbApi, float], StdRet[None]]]:
        """Get the shutdown hooks"""
        return tuple(self.__shutdown)
