
"""
Timer heartbeat event api.
"""


from .events import (
    TimerEvent,
    as_timer_listener,
)

from .bootstrap import start_extension, EXTENSION_DEPENDENCIES
