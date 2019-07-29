
"""
Configuration for the timer.
"""

from ....system.participant import (
    create_singleton_identity,
)


TARGET_TIMER_CONFIG = create_singleton_identity('core.timer.api config')

DEFAULT_INTERVAL = 1.2

CONFIG_INTERVAL_SECONDS = 'interval-seconds'
