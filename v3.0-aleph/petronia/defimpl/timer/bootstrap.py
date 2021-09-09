
"""
Sets up the timer.
"""

from ...aid.bootstrap import (
    EventBus,
    ANY_VERSION,
    create_singleton_identity,
)
from ...aid.lifecycle import (
    create_module_listener_helper,
)
from ...base.internal_.internal_extension import petronia_extension
from ...core.state.api import (
    as_state_change_listener,
    StateStoreUpdatedEvent,
)
from ...core.state.api.events import EVENT_ID_UPDATED_STATE
from .config import (
    TARGET_TIMER_CONFIG,
    DEFAULT_INTERVAL,
    TimerConfig,
)
from .timer import BusTimer


MODULE_ID_TIMER = create_singleton_identity('default.timer')


def start_extension(bus: EventBus) -> None:
    """
    Get the timer started.

    There should only ever be one timer.  It is global, and should never be
    disabled.
    """
    # Set the "active" to false, so that it can start itself up.
    config = TimerConfig(DEFAULT_INTERVAL, False)
    timer = BusTimer(bus, config)

    listener = create_module_listener_helper(bus, MODULE_ID_TIMER, timer.dispose)

    listener.listen(  # type: ignore
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


EXTENSION_METADATA = petronia_extension({
    "name": "default.timer",
    "version": (1, 0, 0),
    'type': 'impl',
    "depends": ({
        'extension': 'core.state.api',
        'minimum': ANY_VERSION,
    },),
    'implements': ({
        "extension": "core.timer.api",
        "minimum": ANY_VERSION,
    },),
})
