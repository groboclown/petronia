
"""
Participants in the Petronia system must include subclasses
of some of the included types.
"""

from .identity import (
    ParticipantId,
    ComponentId,
    SingletonId,
    NOT_PARTICIPANT,

    is_valid_component_identity,
    is_valid_participant_identity,
    is_valid_singleton_identity,

    create_component_identity,
    create_singleton_identity,
)

# These are not explicitly exported,
# because of inter-depndencies with the event bus.
#from .events import (
#    RequestDisposeEvent,
#    DisposeCompleteEvent,
#    as_request_dispose_listener,
#    as_dispose_complete_listener,
#    send_dispose_complete_event,
#    send_request_dispose_event,
#)
