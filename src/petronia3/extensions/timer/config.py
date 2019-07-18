
"""
Configuration for the timer.
"""

from typing import Tuple
from ...system.participant import (
    create_singleton_identity,
    ParticipantId,
)
from ...system.bus import TypeSafeEventBus
from ...system.state import set_state
from ...config.component import (
    PersistableState,
    PersistType,
)

TARGET_TIMER_CONFIG = create_singleton_identity('global-timer config')

DEFAULT_INTERVAL = 1.2

CONFIG_INTERVAL_SECONDS = 'interval-seconds'

class TimerConfig(PersistableState):
    """
    Configuration for the timer.
    """
    __slots__ = ('__interval', '__active')

    def __init__(self, interval_seconds: float, active: bool) -> None:
        self.__interval = interval_seconds
        self.__active = active

    @property
    def interval_seconds(self) -> float:
        return self.__interval

    @property
    def active(self) -> bool:
        return self.__active

    def persist(self) -> PersistType:
        # "active" is a transient property.
        return { CONFIG_INTERVAL_SECONDS: self.__interval }


def set_timer_config(bus: TypeSafeEventBus, config: TimerConfig) -> None:
    set_state(bus, TARGET_TIMER_CONFIG, TimerConfig, config)


def create_timer_config_from_persistence(config: PersistType) -> Tuple[ParticipantId, PersistableState]:
    """config.component.ConfigStateLoader type"""
    if CONFIG_INTERVAL_SECONDS in config:
        interval = config[CONFIG_INTERVAL_SECONDS]
        if isinstance(interval, float) or isinstance(interval, int):
            return (TARGET_TIMER_CONFIG, TimerConfig(float(interval), True))
    return (TARGET_TIMER_CONFIG, TimerConfig(DEFAULT_INTERVAL, True))
