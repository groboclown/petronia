
"""
Generic participant API.
"""

from ..internal_.identity_types import (
    ParticipantId,
    SingletonId,
    ComponentId,

    NOT_PARTICIPANT,

    create_singleton_identity,

    is_valid_component_identity,
    is_valid_participant_identity,
    is_valid_singleton_identity,
)
