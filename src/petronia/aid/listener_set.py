
"""
Event bus proxy support.

This handles proper lifecycle support with the event bus.
"""

from typing import List, Tuple
from threading import Lock
from ..base import (
    EventBus, ListenerId, EventCallback, ParticipantId,
)
from ..base.bus import ListenerRegistrator
from ..base.util import T
from ..core.hotkeys.api import (
    BoundServiceActionSchema,
    send_hotkey_bound_service_announcement,
    send_hotkey_unbind_service_announcement,
)


class ListenerSet:
    """
    Lifecycle support for managing listeners.

    One of these should be created for each component.

    This is thread-safe.
    """

    __slots__ = ('_bus', '_listener_ids', '_lock', '_bound_hotkeys')

    _listener_ids: List[ListenerId]
    _bound_hotkeys: List[Tuple[ParticipantId, str]]

    def __init__(self, bus: EventBus) -> None:
        self._bus = bus
        self._listener_ids = []
        self._bound_hotkeys = []
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

    def bind_hotkey(self, binding: BoundServiceActionSchema) -> None:
        send_hotkey_bound_service_announcement(self._bus, binding)
        with self._lock:
            self._bound_hotkeys.append((binding.service, binding.action,))

    def dispose(self) -> None:
        """
        De-register all the active listeners.
        """
        with self._lock:
            for service, action in self._bound_hotkeys:
                send_hotkey_unbind_service_announcement(self._bus, service, action)
            for listener_id in self._listener_ids:
                self._bus.remove_listener(listener_id)
            self._listener_ids.clear()
            self._bound_hotkeys.clear()
