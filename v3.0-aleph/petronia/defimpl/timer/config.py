
"""
Timer configuration.
"""

from ...base import (
    EventBus,
    create_singleton_identity,
)
from ...core.state.api import set_state

TARGET_TIMER_CONFIG = create_singleton_identity('core.timer.impl config')
DEFAULT_INTERVAL = 1.2


class TimerConfig:
    __slots__ = ('_interval_seconds', '_active')

    def __init__(self, interval_seconds: float, active: bool) -> None:
        self._interval_seconds = interval_seconds
        self._active = active

    @property
    def active(self) -> bool:
        return self._active

    @property
    def interval_seconds(self) -> float:
        return self._interval_seconds


def set_timer_config(bus: EventBus, config: TimerConfig) -> None:
    set_state(bus, TARGET_TIMER_CONFIG, TimerConfig, config)
