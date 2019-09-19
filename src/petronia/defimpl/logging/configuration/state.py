
"""
Log state.
"""

from typing import Mapping
from ....aid.simp import (
    EventBus,
    EventCallback,
    ParticipantId,
    LogLevel,
    readonly_dict,
    set_state,
    as_state_change_listener,
    StateStoreUpdatedEvent,
)
from ....aid.bootstrap import (
    ListenerSetup,
)


class LogState:
    """
    The active state of the logger.
    """
    __slots__ = ('_category_levels',)

    def __init__(self, category_levels: Mapping[str, LogLevel]) -> None:
        self._category_levels = readonly_dict(category_levels)

    @property
    def category_levels(self) -> Mapping[str, LogLevel]:
        """
        The current mapping of category log levels.

        Each key is the category prefix, which is mapped to the minimal
        log level to be displayed; anything below that level is not shown.
        """
        return self._category_levels


def as_log_state_listener(
        callback: EventCallback[StateStoreUpdatedEvent[LogState]]
) -> ListenerSetup[StateStoreUpdatedEvent[LogState]]:
    """ListenerRegistrar setup."""
    return as_state_change_listener(callback)


def set_log_state(
        bus: EventBus, log_state_id: ParticipantId, state: LogState
) -> None:
    """
    Announce a log state update.
    """
    set_state(bus, log_state_id, LogState, state)
