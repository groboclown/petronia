"""Run events on heartbeats."""

from typing import Iterable, List, Callable, Optional
import threading
from ..events import timer as timer_event
from ..runner import ContextEventObjectTarget, EventRegistryContext


class OnHeartbeatListener(ContextEventObjectTarget[timer_event.HeartbeatEvent]):
    """Runs context-aware callbacks on a heartbeat.  If a callback returns True,
    then it is removed from the callbacks list.  If the list of callbacks is empty,
    this will remain listening.  It must be explicitly closed to stop listening."""
    __slots__ = ('__callbacks', '__lock')

    def __init__(
            self, context: EventRegistryContext,
            callbacks: Optional[Iterable[Callable[[EventRegistryContext], bool]]],
    ) -> None:
        ContextEventObjectTarget.__init__(self, context)
        self.__lock = threading.Lock()
        self.__callbacks: List[Callable[[EventRegistryContext], bool]] = []
        if callbacks:
            self.__callbacks.extend(callbacks)

    def add_callback(self, callback: Callable[[EventRegistryContext], bool]) -> None:
        """Add the callback to the list."""
        with self.__lock:
            self.__callbacks.append(callback)

    def on_context_event(
            self, context: EventRegistryContext, source: str, target: str,
            event: timer_event.HeartbeatEvent,
    ) -> bool:
        with self.__lock:
            new_callbacks: List[Callable[[EventRegistryContext], bool]] = []
            for callback in self.__callbacks:
                if not callback(context):
                    new_callbacks.append(callback)
            self.__callbacks = new_callbacks
        return False
