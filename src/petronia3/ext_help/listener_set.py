
"""
Event bus proxy support.

This handles proper lifecycle support with the event bus.
"""

from typing import List
from threading import Lock
from ..system.bus import (
    EventBus, ListenerId, EventCallback,
    ListenerRegistrator,
)
from ..system.participant import ParticipantId
from ..util.memory import T

class ListenerSet:
    """
    Lifecycle support for managing listeners.

    One of these should be created for each component.

    This is thread-safe.
    """

    __slots__ = ('_bus', '_listener_ids', '_lock')

    _listener_ids: List[ListenerId]

    def __init__(self, bus: EventBus) -> None:
        self._bus = bus
        self._listener_ids = []
        self._lock = Lock()

    def listen(
            self,
            target_id: ParticipantId,
            listener_setup: ListenerRegistrator[T],
            callback: EventCallback[T]
    ) -> ListenerId:
        """
        Register a new listener.
        """
        with self._lock:
            listener_id = self._bus.add_listener(target_id, listener_setup, callback)
            self._listener_ids.append(listener_id)
            return listener_id

    def remove_listener(self, listener_id: ListenerId) -> None:
        """
        Stop listening to the given ID.
        """
        with self._lock:
            try:
                index = self._listener_ids.index(listener_id)
                del self._listener_ids[index]
                self._bus.remove_listener(listener_id)
            except ValueError:
                # The listener_id is not known by our listen list.
                pass

    def dispose(self) -> None:
        """
        De-register all the active listeners.
        """
        with self._lock:
            for listener_id in self._listener_ids:
                self._bus.remove_listener(listener_id)
