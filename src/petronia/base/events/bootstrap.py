
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

    EVENT_ID_ERROR,
    ErrorEvent,
    ErrorReport,
    ERROR_CATEGORY_USER,
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
    EventId, QueuePriority, EventProtectionModel,
)
from ..internal_.bus_constants import (
    QUEUE_EVENT_IO,
    QUEUE_EVENT_NORMAL,
    QUEUE_EVENT_HIGH,
    GLOBAL_EVENT_PROTECTION,
    CONSUME_EVENT_PROTECTION,
    PRODUCE_EVENT_PROTECTION,
)
from ..internal_.identity_types import NOT_PARTICIPANT
from ..util.memory import T, EMPTY_MAPPING

# Order of arguments to the RegisterEventEvent constructor
# event_id: EventId, priority: QueuePriority, public_produce: bool, public_consume: bool,
# event_class: Type[T], example: T
EventDefinition = Tuple[EventId, QueuePriority, EventProtectionModel, Type[T], T]


def bootstrap_core_events() -> Sequence[EventDefinition[Any]]:  # type: ignore
    """
    List all the core events along with details of how they should be
    registered.
    """
    return (
        (
            EVENT_ID_EVENT_LISTENER_ADDED,
            QUEUE_EVENT_NORMAL, CONSUME_EVENT_PROTECTION,
            EventListenerAddedEvent,
            EventListenerAddedEvent(EVENT_ID_EVENT_LISTENER_ADDED, NOT_PARTICIPANT),
        ),
        (
            EVENT_ID_REGISTER_EVENT,
            QUEUE_EVENT_HIGH, PRODUCE_EVENT_PROTECTION,
            RegisterEventEvent,
            RegisterEventEvent(
                EVENT_ID_DISPOSE_COMPLETE, QUEUE_EVENT_IO, GLOBAL_EVENT_PROTECTION,
                DisposeCompleteEvent, DisposeCompleteEvent(NOT_PARTICIPANT)
            ),
        ),
        (
            EVENT_ID_DISPOSE_COMPLETE,
            QUEUE_EVENT_NORMAL, GLOBAL_EVENT_PROTECTION,
            DisposeCompleteEvent,
            DisposeCompleteEvent(NOT_PARTICIPANT),
        ),
        (
            EVENT_ID_REQUEST_DISPOSE,
            QUEUE_EVENT_NORMAL, GLOBAL_EVENT_PROTECTION,
            RequestDisposeEvent,
            RequestDisposeEvent(NOT_PARTICIPANT),
        ),
        (
            EVENT_ID_COMPONENT_CREATED,
            QUEUE_EVENT_NORMAL, GLOBAL_EVENT_PROTECTION,
            ComponentCreatedEvent,
            ComponentCreatedEvent(NOT_PARTICIPANT, 1),
        ),
        (
            EVENT_ID_COMPONENT_CREATION_FAILED,
            QUEUE_EVENT_NORMAL, GLOBAL_EVENT_PROTECTION,
            ComponentCreationFailedEvent,
            ComponentCreationFailedEvent('x', 1, 'x', {}),
        ),
        (
            EVENT_ID_REQUEST_NEW_COMPONENT,
            QUEUE_EVENT_NORMAL, GLOBAL_EVENT_PROTECTION,
            RequestNewComponentEvent,
            RequestNewComponentEvent(object(), NOT_PARTICIPANT, 1),
        ),
        (
            EVENT_ID_PARTICIPANT_STARTED,
            QUEUE_EVENT_NORMAL, GLOBAL_EVENT_PROTECTION,
            ParticipantStartedEvent,
            ParticipantStartedEvent(NOT_PARTICIPANT),
        ),
        (
            EVENT_ID_SYSTEM_STARTED,
            QUEUE_EVENT_NORMAL, CONSUME_EVENT_PROTECTION,
            SystemStartedEvent,
            SystemStartedEvent(),
        ),
        (
            EVENT_ID_SYSTEM_HALTED,
            QUEUE_EVENT_NORMAL, CONSUME_EVENT_PROTECTION,
            SystemHaltedEvent,
            SystemHaltedEvent()
        ),
        (
            EVENT_ID_ERROR,
            QUEUE_EVENT_HIGH, GLOBAL_EVENT_PROTECTION,
            ErrorEvent,
            ErrorEvent(ErrorReport('', ERROR_CATEGORY_USER, '', EMPTY_MAPPING))  # type: ignore
        ),
    )
