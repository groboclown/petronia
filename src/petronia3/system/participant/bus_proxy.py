
"""
Event bus proxy support.

This handles proper lifecycle support with the event bus.
"""

from typing import List
from ..bus import (
    TypeSafeEventBus, ListenerId, TypeSafeEventCallback,
    EventId,
)
from ..participant import ParticipantId
from ...util.memory import T

class Bus:
    """
    Lifecycle support for interacting with the event bus.

    One of these should be created for each component.
    """

    __slots__ = ('__bus', '__listener_ids')

    __listener_ids: List[ListenerId]

    def __init__(self, bus: TypeSafeEventBus) -> None:
        self.__bus = bus
        self.__listener_ids = []

    def listen(
            self,
            event_id: EventId, target_id: ParticipantId,
            callback: TypeSafeEventCallback[T]
    ) -> ListenerId:
        listener_id = self.__bus.add_listener(event_id, target_id, callback)
        self.__listener_ids.append(listener_id)
        return listener_id

    def listen_to_component(
        self
    ) -> None:
        """
        Listens to events for a specific component.  If
        that component is deregistered, the listener is automatically
        removed.
        """
        pass
