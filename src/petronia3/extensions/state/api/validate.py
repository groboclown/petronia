
from ....system.participant import (
    ParticipantId,
    is_valid_participant_identity,
)
from ....validation import assert_formatted

def validate_state_id(state_id: ParticipantId) -> None:
    """Ensure the state_id conforms to the standard."""

    assert_formatted(
        is_valid_participant_identity(state_id),

        'StateStore',
        'invalid state id format',
        'id {0}', state_id
    )
