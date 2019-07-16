
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
