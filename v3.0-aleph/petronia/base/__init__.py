
"""
Minimal components that make up Petronia.  Everything else allows for creation
of a UI on top of this loose event system.
"""

from .bus import (
    EventBus,
    EventCallback,
    EventId,
    ListenerId,

    EVENT_WILDCARD,
    TARGET_WILDCARD,
)

from .errors import (
    PetroniaError
)

from .participant import (
    ComponentId,
    ParticipantId,
    SingletonId,
    create_singleton_identity,

    is_valid_participant_identity,
    is_valid_singleton_identity,
    is_valid_component_identity,

    NOT_PARTICIPANT,
)

from .events import (
    RequestDisposeEvent,
    as_request_dispose_listener,
    send_dispose_complete_event,
    send_request_dispose_event,
)

from .logging import (
    log, logerr,

    TRACE,
    DEBUG,
    VERBOSE,
    INFO,
    NOTICE,
    WARN,
    DEPRECATED,
    ERROR,
    FATAL,
)
