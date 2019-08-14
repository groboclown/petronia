
"""
Sets up the timer.
"""

from ...base.bus import (
    EventBus,
    ExtensionMetadataStruct,
)
from ...core.extensions.api import ANY_VERSION
from ...core.state.api import (
    as_state_change_listener,
    StateStoreUpdatedEvent,
)
from ...core.state.api.events import EVENT_ID_UPDATED_STATE
from .config import (
    TARGET_TIMER_CONFIG,
    DEFAULT_INTERVAL,
    TimerConfig,
    set_timer_config,
)
from .timer import BusTimer


def start_extension(bus: EventBus) -> None:
    """
    Get the timer started.

    There should only ever be one timer.  It is global, and should never be
    disabled.
    """
    # Set the "active" to false, so that it can start itself up.
    config = TimerConfig(DEFAULT_INTERVAL, False)
    timer = BusTimer(bus, config)
    bus.add_listener( # type: ignore
        TARGET_TIMER_CONFIG,
        as_state_change_listener,
        timer.on_config_change
    )
    # This implicitly requires a state API implementation to be
    # loaded at boot time.  As the timer is a critical, core component
    # that everything depends upon, we can't expect the state to be
    # loaded first.  Therefore, the config is directly set here.
    # set_timer_config(bus, TimerConfig(DEFAULT_INTERVAL, True))
    timer.on_config_change(
        EVENT_ID_UPDATED_STATE,
        TARGET_TIMER_CONFIG,
        StateStoreUpdatedEvent(
            TARGET_TIMER_CONFIG, TimerConfig,
            TimerConfig(DEFAULT_INTERVAL, True),
            None
        )
    )


EXTENSION_METADATA: ExtensionMetadataStruct = {
    'type': 'impl',
    "depends": [{
        'extension': 'core.state.api',
        'minimum': ANY_VERSION,
    }],
    'implements': [{
        "extension": "core.timer.api",
        "minimum": ANY_VERSION,
    }],
    "authors": ["Petronia"],
}
