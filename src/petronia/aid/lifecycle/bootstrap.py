
"""
Helps module-based bootstrap implementations.
"""

from typing import Callable, Optional
from .dispose import setup_dispose_handler
from ..std.listener_set import ListenerSet
from ...base import (
    SingletonId,
    ComponentId,
    EventBus,
)


def create_module_listener_helper(
        bus: EventBus,
        mid: SingletonId,
        on_dispose: Optional[Callable[[], None]] = None
) -> ListenerSet:
    """
    Creates a helper to register module listeners.  This is configured to
    include de-registering the module when it is requested to be disposed.
    """
    ret = ListenerSet(bus)

    def disposer() -> None:
        if on_dispose:
            on_dispose()
        ret.dispose()

    setup_dispose_handler(bus, mid, disposer, False)
    return ret


def create_component_listener_helper(
        bus: EventBus,
        cid: ComponentId,
        on_dispose: Optional[Callable[[], None]] = None
) -> ListenerSet:
    """
    Creates a helper to register component listeners.
    """
    ret = ListenerSet(bus)

    def disposer() -> None:
        if on_dispose:
            on_dispose()
        ret.dispose()

    setup_dispose_handler(bus, cid, disposer, True)
    return ret
