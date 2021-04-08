
"""
The events around the shutdown phase of the system lifecycle.  See the
architecture document for details about this.

This is an extension API because there may be different ways to implement
the shutdown UI aspects and the is-shutdown-complete detection.

This must tie into the SystemHaltedEvent.
"""

from ....base import create_singleton_identity
from ....base.bus import (
    EventId,
    EventBus,
    EventCallback,
    ListenerSetup,
)

TARGET_ID_SYSTEM_SHUTDOWN = create_singleton_identity('core.shutdown.api')


# ---------------------------------------------------------------------------

EVENT_ID_REQUEST_SYSTEM_SHUTDOWN = EventId('core.shutdown.api request-shutdown')


class RequestSystemShutdownEvent:
    """
    Request that the Petronia system stop running.  When the system is ready
    to shut down, the SystemShutdownEvent is triggered by the event bus.
    """
    __slots__ = ()


def as_request_system_shutdown_listener(
    callback: EventCallback[RequestSystemShutdownEvent]
) -> ListenerSetup[RequestSystemShutdownEvent]:
    return (EVENT_ID_REQUEST_SYSTEM_SHUTDOWN, callback,)

def send_system_shutdown_request(bus: EventBus) -> None:
    bus.trigger(
        EVENT_ID_REQUEST_SYSTEM_SHUTDOWN, TARGET_ID_SYSTEM_SHUTDOWN, RequestSystemShutdownEvent()
    )


# ---------------------------------------------------------------------------

EVENT_ID_SYSTEM_SHUTDOWN = EventId('core.shutdown.api system-shutting-down')

class SystemShutdownEvent:
    """
    The system has started the shutdown phase.  The system will decide when to
    shut everything off.
    """
    __slots__ = ()

def as_system_shutdown_listener(
    callback: EventCallback[SystemShutdownEvent]
) -> ListenerSetup[SystemShutdownEvent]:
    return (EVENT_ID_SYSTEM_SHUTDOWN, callback,)


# ---------------------------------------------------------------------------

EVENT_ID_REQUEST_CANCEL_SYSTEM_SHUTDOWN = EventId('core.shutdown.api request-cancel-shutdown')

class RequestCancelSystemShutdownEvent:
    """
    A request to stop the shutdown.
    """
    __slots__ = ()

def send_cancel_system_shutdown_request(bus: EventBus) -> None:
    bus.trigger(
        EVENT_ID_REQUEST_CANCEL_SYSTEM_SHUTDOWN, TARGET_ID_SYSTEM_SHUTDOWN,
        RequestCancelSystemShutdownEvent()
    )


# ---------------------------------------------------------------------------

EVENT_ID_SYSTEM_SHUTDOWN_CANCELLED = EventId('core.shutdown.api shutdown-cancelled')

class SystemShutdownCancelledEvent:
    """
    The system shutdown is cancelled, and the system is back to normal operation.
    """
    __slots__ = ()

def as_system_shutdown_cancelled_listener(
        callback: EventCallback[SystemShutdownCancelledEvent]
) -> ListenerSetup[SystemShutdownCancelledEvent]:
    return (EVENT_ID_SYSTEM_SHUTDOWN_CANCELLED, callback,)


# ---------------------------------------------------------------------------

EVENT_ID_SYSTEM_SHUTDOWN_FINALIZE = EventId('core.shutdown.api system-shut-down-finalize')

class SystemShutdownFinalizeEvent:
    """
    The system has finished the application shutdown phase, and it can no
    longer be cancelled.  At this point, system services must shutdown, and
    after a quiet period, the system will send a HALT event.
    """
    __slots__ = ()

def as_system_shutdown_finalize_listener(
    callback: EventCallback[SystemShutdownFinalizeEvent]
) -> ListenerSetup[SystemShutdownFinalizeEvent]:
    return (EVENT_ID_SYSTEM_SHUTDOWN_FINALIZE, callback,)
