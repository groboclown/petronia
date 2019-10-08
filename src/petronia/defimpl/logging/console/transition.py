
"""
The log state transition handler.
"""

from typing import Dict, Tuple, Optional
from threading import Lock
from ....aid.std import (
    EventBus,
    EventId,
    ParticipantId,
    ListenerId,
    LogHandlerId,
    LogLevel,
    add_log_handler,
    remove_log_handler,
    StateStoreUpdatedEvent,
)
from ..configuration import (
    LogState,
    LogConfiguration,
    as_log_configuration_listener,
    set_log_state,
)
from .handler import standard_log_message
from .ident import (
    TARGET_ID_CONSOLE_LOGGER_CONFIG,
    TARGET_ID_CONSOLE_LOGGER_STATE,
)


class LogStateTransitionHandler:
    """
    Handles the transition of a configuration request on the
    log handler.
    """
    __slots__ = ('_listeners', '_bus', '_cc_listener', '_lock',)
    _listeners: Dict[str, Tuple[LogLevel, LogHandlerId]]
    _cc_listener: Optional[ListenerId]
    _bus: Optional[EventBus]

    def __init__(self, bus: EventBus) -> None:
        self._lock = Lock()
        self._bus = bus
        self._listeners = {}
        self._cc_listener = bus.add_listener(
            TARGET_ID_CONSOLE_LOGGER_CONFIG,
            as_log_configuration_listener,
            self._on_config_change
        )

    def dispose(self) -> None:
        """Dispose of this component.  Completely idempotent."""
        with self._lock:
            if self._bus and self._cc_listener:
                self._bus.remove_listener(self._cc_listener)
                self._cc_listener = None
                self._bus = None
            for llh in self._listeners.values():
                remove_log_handler(llh[1])
            self._listeners.clear()

    def _generate_state(self) -> LogState:
        # Must be in a lock.
        lsm: Dict[str, LogLevel] = {}
        for cat, llh in self._listeners.items():
            lsm[cat] = llh[0]
        return LogState(lsm)

    def _on_config_change(
            self,
            _event_id: EventId, _target_id: ParticipantId,  # pylint: disable=unused-argument
            event_obj: StateStoreUpdatedEvent[LogConfiguration]
    ) -> None:
        with self._lock:
            different = False
            active_cats = set(self._listeners.keys())
            for cat, level in event_obj.state.category_levels.items():
                if cat in self._listeners:
                    curr_level, listener = self._listeners[cat]
                    if curr_level != level:
                        remove_log_handler(listener)
                        lid = add_log_handler(level, cat, standard_log_message)
                        self._listeners[cat] = (level, lid,)
                        different = True
                    # else it's the same.
                    active_cats.remove(cat)
                else:
                    # New listener
                    lid = add_log_handler(level, cat, standard_log_message)
                    self._listeners[cat] = (level, lid,)
                    different = True
            if active_cats:
                # There are categories that need to be removed.
                for cat in active_cats:
                    listener = self._listeners[cat][1]
                    remove_log_handler(listener)
                    del self._listeners[cat]
                different = True

            if different and self._bus:
                new_state = self._generate_state()
                set_log_state(self._bus, TARGET_ID_CONSOLE_LOGGER_STATE, new_state)
