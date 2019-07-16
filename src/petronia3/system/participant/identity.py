
"""
Participant Identity.

Dynamically created participants ("components") must call the
`create_participant_identity()` method to create the next available ID.
Singletons must use a hard-coded identity.

At the moment, IDs are numbers.  Dynamic identities are positive and singletons
are negative.  A zero identity indicates an error.
"""

from typing import NewType, Union, Tuple
from threading import Lock
from ...errors import PetroniaLockTimeoutError

# All participants use these typed values.
# The type of the value might change over time, so type tests should use
# the functions in this file.

ComponentId = NewType('ComponentId', Tuple[str, int])
SingletonId = NewType('SingletonId', str)
ParticipantId = Union[ComponentId, SingletonId]

NOT_PARTICIPANT = ComponentId(('', 0,))

def is_valid_participant_identity(pid: ParticipantId) -> bool:
    """Is this a valid participant identity?"""
    return (
        is_valid_component_identity(pid) or
        is_valid_singleton_identity(pid)
    )

def is_valid_singleton_identity(pid: ParticipantId) -> bool:
    """Is this a valid participant identity for a singleton to have?"""
    return isinstance(pid, str) and len(pid) > 0

def is_valid_component_identity(pid: ParticipantId) -> bool:
    """Is this a valid participant identity for a component to have?"""
    return (
        isinstance(pid, tuple) and
        len(pid) == 2 and
        isinstance(pid[0], str) and
        isinstance(pid[1], int) and
        pid[1] > 0
    )


_NEXT_ID = 1
_IDENTITY_LOCK = Lock()
_LOCK_TIMEOUT = 300

def create_component_identity(category: str) -> ComponentId:
    """
    Create a new unique identity for a new participant.

    This function is thread-safe, because it accesses memory
    which is global across all threads.
    """
    assert category
    assert isinstance(category, str)

    global _NEXT_ID # pylint: disable=global-statement
    if not _IDENTITY_LOCK.acquire(timeout=_LOCK_TIMEOUT):
        raise PetroniaLockTimeoutError()
    try:
        ret = _NEXT_ID
        _NEXT_ID += 1
    finally:
        _IDENTITY_LOCK.release()
    return ComponentId((category, ret,))


def create_singleton_identity(category: str) -> SingletonId:
    """
    Create a new singleton identity.  Singleton identities must
    be unique by category, so it is up to the caller to ensure that
    it does not conflict with any other existing singletons.
    """
    return SingletonId(category)
