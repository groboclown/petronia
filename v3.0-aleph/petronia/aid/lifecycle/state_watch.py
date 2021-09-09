
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

    This allows for swapping out in a thread-safe way the listener.  A common pattern
    is to have the initial listener wait for the first-time state set to act as a gating
    block before starting up the extension.

    It also allows for encapsulating the state information, so that an extension can
    listen to a state without needing to know the state id.
    """

    __slots__ = (
        '_listener', '_state', '_set',
        '_lock',
    )

    def __init__(
            self,
            listeners: ListenerSet,
            target: ParticipantId,
            initial_state: T,
            listener: Optional[Callable[[T], None]] = None
    ) -> None:
        self._state = initial_state
        self._listener = listener
        self._set = False
        self._lock = RLock()

        # This puts an instance of this watcher into the listener set, which
        # means this object will stay around as long as the listener set does.
        listeners.listen(target, as_state_change_listener, self._on_state)  # type: ignore

    def _on_state(
            self, _event_id: EventId, _target_id: ParticipantId,
            event_obj: StateStoreUpdatedEvent[T]
    ) -> None:
        with self._lock:
            # print("DEBUG state watch received state update for {0}; is set? {1};".format(_target_id, self._set))
            if not self._set or event_obj.state != self._state:
                self._set = True
                self._state = event_obj.state
                if self._listener:
                    self._listener(self._state)

    def set_listener(self, listener: Optional[Callable[[T], None]]) -> None:
        # This is why we need a re-entrant lock: so that the listener
        # can swap itself out with something else.
        with self._lock:
            self._listener = listener
            if listener and self._set:
                listener(self._state)

    @property
    def state(self) -> T:
        return self._state

    @property
    def is_set(self) -> bool:
        return self._set
