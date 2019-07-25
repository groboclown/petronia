
"""
Timer configuration.
"""

from petronia3.system.bus import EventBus
from petronia3.system.participant import create_singleton_identity

TARGET_TIMER_CONFIG = create_singleton_identity('core.timer.impl config')
DEFAULT_INTERVAL = 1.2

class TimerConfig:
    def __init__(self, interval_seconds: float, active: bool) -> None:
        raise NotImplementedError()

    @property
    def active(self) -> bool:
        raise NotImplementedError()

    @property
    def interval_seconds(self) -> float:
        raise NotImplementedError()

def set_timer_config(bus: EventBus, config: TimerConfig) -> None:
    raise NotImplementedError()
