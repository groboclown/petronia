
"""
Sets up the timer.
"""

from petronia3.extensions.timer.api.events import (
    EVENT_ID_TIMER, GLOBAL_TIMER_EVENT,
    TimerEvent,
)
from petronia3.system.bus import (
    EventBus,
    register_event,
    ExtensionMetadataStruct,
    QUEUE_EVENT_NORMAL,
)
from petronia3.extensions.extensions.api import ANY_VERSION
from petronia3.extensions.state.api import (
    as_state_change_listener,
)
from .config import (
    TARGET_TIMER_CONFIG,
    DEFAULT_INTERVAL,
    TimerConfig,
    set_timer_config
)
from .timer import BusTimer


def start_extension(bus: EventBus) -> None:
    """
    Get the timer started.

    There should only ever be one timer.  It is global, and should never be
    disabled.
    """
    register_event(
        bus,
        EVENT_ID_TIMER,
        QUEUE_EVENT_NORMAL,
        TimerEvent,
        GLOBAL_TIMER_EVENT
    )
    # Set the "active" to false, so that it can start itself up.
    config = TimerConfig(DEFAULT_INTERVAL, False)
    timer = BusTimer(bus, config)
    bus.add_listener( # type: ignore
        TARGET_TIMER_CONFIG,
        as_state_change_listener,
        timer.on_config_change
    )
    set_timer_config(bus, config)


EXTENSION_METADATA: ExtensionMetadataStruct = {
    'type': 'impl',
    'implements': {
        "name": "core.timer.api",
        "version": ANY_VERSION,
    },
    "authors": ["Petronia"],
}
