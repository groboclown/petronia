
"""
Logging configuration state.
"""

from typing import Dict, Mapping
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

class LogConfiguration:
    """
    The configuration of the logger.
    """
    __slots__ = ('_category_levels',)

    def __init__(self, category_levels: Dict[str, LogLevel]) -> None:
        self._category_levels = readonly_dict(category_levels)

    @property
    def category_levels(self) -> Mapping[str, LogLevel]:
        """
        The current mapping of category log levels.

        Each key is the category prefix, which is mapped to the minimal
        log level to be displayed; anything below that level is not shown.
        """
        return self._category_levels


def as_log_configuration_listener(
        callback: EventCallback[StateStoreUpdatedEvent[LogConfiguration]]
) -> ListenerSetup[StateStoreUpdatedEvent[LogConfiguration]]:
    """ListenerRegistrar setup."""
    return as_state_change_listener(callback)

def send_log_configuration(
        bus: EventBus, logger_config_id: ParticipantId, config: LogConfiguration
) -> None:
    """
    Request a configuration change to the logger.
    """
    set_state(bus, logger_config_id, LogConfiguration, config)
