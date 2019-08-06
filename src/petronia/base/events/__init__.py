
"""
Core events for the Petronia system.

There are interdepndencies between this module and the bus module, so care is
taken to split this out to prevent cycles, with the intent that the end user
would have the primary events imported separately from the bus.
"""

from ..internal_.bus_events import (
    EventListenerAddedEvent,
    as_listener_added_listener,

    register_event,
)
from ..internal_.dispose_events import (
    DisposeCompleteEvent,
    as_dispose_complete_listener,
    send_dispose_complete_event,

    RequestDisposeEvent,
    as_request_dispose_listener,
    send_request_dispose_event,
)
from .component_events import (
    ComponentCreatedEvent,
    as_component_created_listener,

    RequestNewComponentEvent,
    as_request_new_component_listener,
    send_request_new_component,
)
from .participant_events import (
    ParticipantStartedEvent,
    as_participant_started_listener,
    send_participant_started_event,
)
from .system_events import (
    SystemStartedEvent,
    as_system_started_listener,
)
