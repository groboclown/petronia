
# mypy: allow-any-expr
# mypy: allow-any-explicit

"""
A specific lifecycle for an event listener that, once triggered, is finished
with all actions.
"""

from typing import List, Optional, Any
from threading import Lock
from ..simp import (
    EventBus,
    ParticipantId,
    ListenerId,
    EventId,
    send_dispose_complete_event,
    T,
    ValueHolder,
    EventCallback,
)
from ..bootstrap import (
    as_request_dispose_listener,
    as_system_shutdown_finalize_listener,
    as_system_shutdown_listener,
    TARGET_ID_SYSTEM_SHUTDOWN,
    ListenerRegistrator,
)


def create_one_and_done(
        bus: EventBus,
        source_id: ParticipantId,
        target_id: ParticipantId,
        registrator: ListenerRegistrator[T],
        callback: EventCallback[T],
        is_application: bool = True,
        is_standalone: bool = False
) -> None:
    """
    Create the full lifecycle handler for the event that, when triggered,
    is no longer listened to.
    """
    listeners: List[ListenerId] = []
    lock = Lock()
    disposed = ValueHolder(False)

    def dispose(_event_id: EventId, _target: ParticipantId, _event_obj: Any):
        with lock:
            if not disposed.value:
                disposed.value = True
                for listener in listeners:
                    bus.remove_listener(listener)
                listeners.clear()
                if is_standalone:
                    send_dispose_complete_event(bus, source_id)

    def listener_func(event_id: EventId, target: ParticipantId, event_obj: T):
        dispose(event_id, target, event_obj)
        callback(event_id, target, event_obj)

    listeners.append(bus.add_listener(target_id, registrator, listener_func))
    listeners.append(bus.add_listener(source_id, as_request_dispose_listener, dispose))
    if is_application:
        listeners.append(bus.add_listener(TARGET_ID_SYSTEM_SHUTDOWN, as_system_shutdown_listener, dispose))
    else:
        listeners.append(bus.add_listener(TARGET_ID_SYSTEM_SHUTDOWN, as_system_shutdown_finalize_listener, dispose))
