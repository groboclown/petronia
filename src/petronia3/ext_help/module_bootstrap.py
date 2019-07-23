
"""
Helps module-based bootstrap implementations.
"""

from typing import Callable, Optional
from .listener_set import ListenerSet
from ..system.participant import SingletonId
from ..system.bus import (
    EventBus,
)
from ..system.events import (
    send_dispose_complete_event,
    as_request_dispose_listener,
)


def create_module_listener_helper(
        bus: EventBus,
        mid: SingletonId,
        on_dispose: Optional[Callable[[], None]] = None
) -> ListenerSet:
    """
    Creates a helper to register module listeners.  This is configured to
    include de-regstiering the module when it is requested to be disposed.
    """
    ret = ListenerSet(bus)
    ret.listen(
        mid,
        as_request_dispose_listener,
        lambda eid, tid, eobj: _on_module_disposed(bus, mid, ret, on_dispose)
    )
    return ret


def _on_module_disposed(
        bus: EventBus,
        mid: SingletonId,
        lset: ListenerSet,
        on_dispose: Optional[Callable[[], None]]
) -> None:
    lset.dispose()
    if on_dispose:
        on_dispose()
    send_dispose_complete_event(bus, mid)
