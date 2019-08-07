
"""
Define all the core events.  This is used by setup routines to create all the
initial events in the system before the system is up and running.
"""

from typing import Sequence, Tuple, Type, Any
from .component_events import (
    EVENT_ID_COMPONENT_CREATED,
    ComponentCreatedEvent,

    EVENT_ID_REQUEST_NEW_COMPONENT,
    RequestNewComponentEvent,

    EVENT_ID_COMPONENT_CREATION_FAILED,
    ComponentCreationFailedEvent,
)
from .system_events import (
    EVENT_ID_SYSTEM_STARTED,
    SystemStartedEvent,

    EVENT_ID_SYSTEM_HALTED,
    SystemHaltedEvent,
)
from .participant_events import (
    EVENT_ID_PARTICIPANT_STARTED,
    ParticipantStartedEvent,
)
from ..internal_.bus_events import (
    EVENT_ID_EVENT_LISTENER_ADDED,
    EventListenerAddedEvent,

    EVENT_ID_REGISTER_EVENT,
    RegisterEventEvent,
)
from ..internal_.dispose_events import (
    EVENT_ID_DISPOSE_COMPLETE,
    DisposeCompleteEvent,

    EVENT_ID_REQUEST_DISPOSE,
    RequestDisposeEvent,
)
from ..internal_.bus_types import (
    EventId, QueuePriority
)
from ..internal_.bus_constants import (
    QUEUE_EVENT_IO,
    QUEUE_EVENT_NORMAL,
    QUEUE_EVENT_HIGH,
)
from ..internal_.identity_types import NOT_PARTICIPANT
from ..util.memory import T

EventDefinition = Tuple[EventId, QueuePriority, Type[T], T]

def bootstrap_core_events() -> Sequence[EventDefinition[Any]]: # type: ignore
    """
    List all the core events along with details of how they should be
    registered.
    """
    return (
        (
            EVENT_ID_EVENT_LISTENER_ADDED,
            QUEUE_EVENT_NORMAL,
            EventListenerAddedEvent,
            EventListenerAddedEvent(EVENT_ID_EVENT_LISTENER_ADDED, NOT_PARTICIPANT),
        ),
        (
            EVENT_ID_REGISTER_EVENT,
            QUEUE_EVENT_HIGH,
            RegisterEventEvent,
            RegisterEventEvent(
                EVENT_ID_DISPOSE_COMPLETE, QUEUE_EVENT_IO,
                DisposeCompleteEvent, DisposeCompleteEvent(NOT_PARTICIPANT)
            ),
        ),
        (
            EVENT_ID_DISPOSE_COMPLETE,
            QUEUE_EVENT_NORMAL,
            DisposeCompleteEvent,
            DisposeCompleteEvent(NOT_PARTICIPANT),
        ),
        (
            EVENT_ID_REQUEST_DISPOSE,
            QUEUE_EVENT_NORMAL,
            RequestDisposeEvent,
            RequestDisposeEvent(NOT_PARTICIPANT),
        ),
        (
            EVENT_ID_COMPONENT_CREATED,
            QUEUE_EVENT_NORMAL,
            ComponentCreatedEvent,
            ComponentCreatedEvent(NOT_PARTICIPANT, 1),
        ),
        (
            EVENT_ID_COMPONENT_CREATION_FAILED,
            QUEUE_EVENT_NORMAL,
            ComponentCreationFailedEvent,
            ComponentCreationFailedEvent('x', 1, 'x', {}),
        ),
        (
            EVENT_ID_REQUEST_NEW_COMPONENT,
            QUEUE_EVENT_NORMAL,
            RequestNewComponentEvent,
            RequestNewComponentEvent(object(), NOT_PARTICIPANT, 1),
        ),
        (
            EVENT_ID_PARTICIPANT_STARTED,
            QUEUE_EVENT_NORMAL,
            ParticipantStartedEvent,
            ParticipantStartedEvent(NOT_PARTICIPANT),
        ),
        (
            EVENT_ID_SYSTEM_STARTED,
            QUEUE_EVENT_NORMAL,
            SystemStartedEvent,
            SystemStartedEvent(),
        ),
        (
            EVENT_ID_SYSTEM_HALTED,
            QUEUE_EVENT_NORMAL,
            SystemHaltedEvent,
            SystemHaltedEvent()
        ),
    )
