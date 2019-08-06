
"""
Events for all participants to use.
"""

from ..internal_.bus_types import (
    EventBus, EventId, EventCallback,
    ListenerSetup,
)
from ..internal_.identity_types import ParticipantId
from ..internal_.bus_constants import TARGET_WILDCARD

# Note: not "core"
EVENT_ID_PARTICIPANT_STARTED = EventId('petronia.participant started')


class ParticipantStartedEvent:
    """
    Event to indicate that a participant finished initializing itself and is
    ready to begin normal operation.  This should happen after configuration.
    """
    __slots__ = ('_pid')
    def __init__(self, pid: ParticipantId) -> None:
        self._pid = pid

    @property
    def pid(self) -> ParticipantId:
        """The participant ID that has started."""
        return self._pid

def as_participant_started_listener(
        callback: EventCallback[ParticipantStartedEvent]
) -> ListenerSetup[ParticipantStartedEvent]:
    return (EVENT_ID_PARTICIPANT_STARTED, callback,)

def send_participant_started_event(
        bus: EventBus,
        pid: ParticipantId
) -> None:
    bus.trigger(
        EVENT_ID_PARTICIPANT_STARTED, TARGET_WILDCARD,
        ParticipantStartedEvent(pid)
    )
