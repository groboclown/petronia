
"""
Non-Platform specific extensions to the base Petronia system.

Some of these are classified as "extensions" because the base system does not
need them to run.  However, they are so integral to many other extensions that
they may well be considered essential.
"""

# Import the commonly used sub-parts for easy use by other parts of the
# system.

from .shutdown.api import (
    as_system_shutdown_listener,
    SystemShutdownEvent,
)

from .state.api import (
    StateStoreUpdatedEvent,
    as_state_change_listener,
    set_state,
)

from .timer.api import (
    as_timer_listener,
    TimerEvent,
)

from ..base.events import (
    ComponentCreatedEvent,
    as_component_created_listener,

    DisposeCompleteEvent,
    as_dispose_complete_listener,
    send_dispose_complete_event,

    RequestDisposeEvent,
    as_request_dispose_listener,
    send_request_dispose_event,

    RequestNewComponentEvent,
    as_request_new_component_listener,
    send_request_new_component,

    as_system_started_listener,
)
