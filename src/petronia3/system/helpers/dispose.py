
"""
Helpers for disposing components.
"""

from ..bus import (
    TypeSafeEventCallback, TypeSafeEventBus,
    EventId, ListenerSetup,
    TARGET_WILDCARD,
)
from ..participant import (
    ParticipantId,
)
from ...validation import (
    assert_formatted,
)

EVENT_ID_REQUEST_DISPOSE = EventId('participant request-dispose')
EVENT_ID_DISPOSE_COMPLETE = EventId('participant dispose-complete')

class RequestDisposeEvent:
    """
    Request for a participant to dispose itself.
    """

    __slots__ = ('_target_id',)

    def __init__(self, target_id: ParticipantId) -> None:
        self._target_id = target_id

    @property
    def target_id(self) -> ParticipantId:
        """The participant that is requested to dispose itself."""
        return self._target_id


class DisposeCompleteEvent:
    """
    Notification that a dispose completed.
    """

    __slots__ = ('_disposed_id',)

    def __init__(self, disposed_id: ParticipantId) -> None:
        self._disposed_id = disposed_id

    @property
    def disposed_id(self) -> ParticipantId:
        """The participant that completed disposal."""
        return self._disposed_id


def as_request_dispose_listener(
        listener: TypeSafeEventCallback[RequestDisposeEvent]
) -> ListenerSetup[RequestDisposeEvent]:
    """Describe the listener's events in a type-safe way."""
    return (EVENT_ID_REQUEST_DISPOSE, listener,)


def send_request_dispose_event(bus: TypeSafeEventBus, to_dispose_id: ParticipantId) -> None:
    """Reqest that a participant be disposed."""
    assert_formatted(
        to_dispose_id != TARGET_WILDCARD,
        'RequestDisposeEvent',
        'disposed ID cannot be a wildcard',
        'requested {0}', to_dispose_id
    )
    bus.trigger(EVENT_ID_REQUEST_DISPOSE, to_dispose_id, RequestDisposeEvent(to_dispose_id))


def as_dispose_complete_listener(
        listener: TypeSafeEventCallback[DisposeCompleteEvent]
) -> ListenerSetup[DisposeCompleteEvent]:
    """Add a listener for dispose completion events."""
    return (EVENT_ID_DISPOSE_COMPLETE, listener,)


def send_dispose_complete_event(bus: TypeSafeEventBus, disposed_id: ParticipantId) -> None:
    """Notify listeners that a participant was disposed."""
    assert_formatted(
        disposed_id != TARGET_WILDCARD,
        'RequestDisposeEvent',
        'disposed ID cannot be a wildcard',
        'requested {0}', disposed_id
    )
    bus.trigger(EVENT_ID_DISPOSE_COMPLETE, disposed_id, DisposeCompleteEvent(disposed_id))
