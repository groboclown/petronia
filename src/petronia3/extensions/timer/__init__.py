
"""
Fires events at regular intervals.
"""


from .config import (
    TimerConfig,
    create_timer_config_from_persistence,
    set_timer_config,
)

from .events import (
    TimerEvent,
    as_timer_listener,
)
