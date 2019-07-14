
"""
Participant Identity.

Dynamically created participants ("components") must call the
`create_participant_identity()` method to create the next available ID.
Singletons must use a hard-coded identity.

At the moment, IDs are numbers.  Dynamic identities are positive and singletons
are negative.  A zero identity indicates an error.
"""

from typing import NewType
from threading import Lock
from ...errors import PetroniaLockTimeoutError

# All participants use this typed value.
# The type of the value might change over time.
ParticipantId = NewType('ParticipantId', int)

NOT_PARTICIPANT = ParticipantId(0)

def is_valid_participant_identity(pid: ParticipantId) -> bool:
    """Is this a valid participant identity?"""
    return isinstance(pid, int) and pid != 0

def is_valid_singleton_identity(pid: ParticipantId) -> bool:
    """Is this a valid participant identity for a singleton to have?"""
    return isinstance(pid, int) and pid < 0

def is_valid_component_identity(pid: ParticipantId) -> bool:
    """Is this a valid participant identity for a component to have?"""
    return isinstance(pid, int) and pid > 0


_NEXT_ID = 1
_IDENTITY_LOCK = Lock()
_LOCK_TIMEOUT = 300

def create_participant_identity() -> ParticipantId:
    """
    Create a new unique identity for a new participant.

    This function is thread-safe, because it accesses memory
    which is global across all threads.
    """
    global _NEXT_ID # pylint: disable=global-statement
    if not _IDENTITY_LOCK.acquire(timeout=_LOCK_TIMEOUT):
        raise PetroniaLockTimeoutError()
    try:
        ret = _NEXT_ID
        _NEXT_ID += 1
    finally:
        _IDENTITY_LOCK.release()
    return ParticipantId(ret)
