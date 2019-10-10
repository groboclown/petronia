
"""
Watches the state of a target.
"""

from typing import Generic, Callable, Optional
from threading import RLock
from ...base.bus import (
    EventId,
)
from ...base.participant import (
    ParticipantId,
)
from ...base.util import (
    T,
)
from ...core.state.api import (
    StateStoreUpdatedEvent,
    as_state_change_listener,
)
from .listener_set import (
    ListenerSet
)


class StateWatch(Generic[T]):
    """
    Monitors a published state, and sends notifications
    to an optional listener.
    """

    __slots__ = (
        '__listener', '__state', '__set',
        '__lock',
    )

    def __init__(
            self,
            listeners: ListenerSet,
            target: ParticipantId,
            initial_state: T,
            listener: Optional[Callable[[T], None]] = None
    ) -> None:
        self.__state = initial_state
        self.__listener = listener
        self.__set = False
        self.__lock = RLock()
        listeners.listen(target, as_state_change_listener, self._on_state)  # type: ignore

    def _on_state(
            self, _event_id: EventId, _target_id: ParticipantId,
            event_obj: StateStoreUpdatedEvent[T]
    ) -> None:
        with self.__lock:
            if not self.__set or event_obj.state != self.__state:
                self.__set = True
                self.__state = event_obj.state
                if self.__listener:
                    self.__listener(self.__state)

    def set_listener(self, listener: Optional[Callable[[T], None]]) -> None:
        # This is why we need a re-entrant lock: so that the listener
        # can swap itself out with something else.
        with self.__lock:
            self.__listener = listener
            if listener and self.__set:
                listener(self.__state)

    @property
    def state(self) -> T:
        return self.__state

    @property
    def is_set(self) -> bool:
        return self.__set
