
"""
Timer heartbeat event api.
"""


from .events import (
    TimerEvent,
    as_timer_listener,
    TARGET_TIMER,
)

from .bootstrap import bootstrap_timer_api as start_extension
from .bootstrap import EXTENSION_METADATA
