"""Handles chained events.  These are event handlers that rely on:

1. After one event type is received, another event is sent, a follow-up event is registered,
    and the received event listener is removed.
2. A group of events are possible to be received (say, success or failure).  If one is received,
    all listeners in the group should be removed.  The listeners in the group represent a
    "decision".

Timeouts for the chain are already handled by the registry module.
"""

from typing import Callable
from petronia_common.util import ValueHolder, T
from .registry import EventObjectTarget


class DecisionHandlerProxy(EventObjectTarget[T]):
    """Handles a decision call.  This shares an "active" value, which, when set to True,
    causes the handlers with the same state value to be removed from the processing.
    The handler proxy takes in a handler callback function, which takes the source ID
    and target ID and event object.  It returns True if the handler function correctly
    handled the event and "made a decision", or it returns False if the event wasn't
    what it was looking for, and the decision processing can continue."""
    __slots__ = ('_active', '_handler',)

    def __init__(self, handler: Callable[[str, str, T], bool], active: ValueHolder[bool]) -> None:
        self._active = active
        self._handler = handler

    def on_event(self, source: str, target: str, event: T) -> bool:
        if not self._active.value:
            # No longer active, so remove this handler.
            return True
        self._active.value = not self._handler(source, target, event)
        return not self._active.value
