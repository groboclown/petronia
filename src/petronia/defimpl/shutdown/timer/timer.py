
"""
Special logic for handling shutdown events.

On shutdown requests, waits for either a no-event quiet period or a total
timeout.  If either is surpassed, then a halt is sent out.
"""

import time
import threading
from typing import Optional
from ....base import (
    ParticipantId,
    log,
    VERBOSE,
)
from ....base.bus import (
    EventBus,
    EventCallback,
    EventId,
    ListenerId,
    ListenerSetup,
    EVENT_WILDCARD,
    TARGET_WILDCARD,
)
from ....base.events.system_events import (
    TARGET_ID_SYSTEM,

    SystemHaltedEvent,
    EVENT_ID_SYSTEM_HALTED,
)
from ....core.shutdown.api.events import (
    RequestSystemShutdownEvent,
    EVENT_ID_REQUEST_SYSTEM_SHUTDOWN,

    SystemShutdownEvent,
    EVENT_ID_SYSTEM_SHUTDOWN,

    EVENT_ID_REQUEST_CANCEL_SYSTEM_SHUTDOWN,

    SystemShutdownCancelledEvent,
    EVENT_ID_SYSTEM_SHUTDOWN_CANCELLED,

    SystemShutdownFinalizeEvent,
    EVENT_ID_SYSTEM_SHUTDOWN_FINALIZE,
)

# TODO switch to the StateSwitcher helper
# TODO use the Timer helper
# TODO add in EVENT_ID_SYSTEM_SHUTDOWN_FINALIZE support.


class ShutdownTimer:
    """
    Maintains a state related to shutdown.

    After a quiet period of no events, this will send a halt.

    This allows for oscellating between on and off state if something calls
    shutdown cancel.
    """
    __slots__ = (
        '_bus',
        '_quiet_period',
        '_shutdown_started',
        '_last_event_time',
        '_total_wait_time',
        '_final_shutdown_time',
        '_thread',
        '_active',
        '_any_listener',
        '_request_shutdown_listener',
        '_lock',
    )

    _any_listener: Optional[ListenerId]
    _request_shutdown_listener: Optional[ListenerId]
    _thread: Optional[threading.Thread]

    def __init__(
            self,
            bus: EventBus,
            total_wait_seconds: float,
            quiet_period_seconds: float,
    ) -> None:
        self._bus = bus
        self._lock = threading.Lock()
        self._total_wait_time = total_wait_seconds
        self._quiet_period = quiet_period_seconds

        self._last_event_time = 0.0
        self._final_shutdown_time = 0.0
        self._active = True
        self._any_listener = None
        self._thread = None
        self._request_shutdown_listener = None

        self.setup_shutdown_request_listener()


    def setup_shutdown_request_listener(self) -> None:
        with self._lock:
            if self._request_shutdown_listener:
                # Already setup
                return
            self.__internal_stop_sl()
            self._request_shutdown_listener = self._bus.add_listener(
                TARGET_ID_SYSTEM, _as_request_shutdown_listener,
                self.on_shutdown_request
            )

    def __internal_stop_sl(self) -> None:
        self._active = False
        if self._any_listener:
            self._bus.remove_listener(self._any_listener)
            self._any_listener = None

    def stop_shutdown_listener(self) -> None:
        with self._lock:
            self.__internal_stop_sl()


    def on_shutdown_request(
            self,
            event_id: EventId, # pylint: disable=unused-argument
            target_id: ParticipantId, # pylint: disable=unused-argument
            event_obj: RequestSystemShutdownEvent # pylint: disable=unused-argument
    ) -> None:
        """
        Waiting for shutdown request phase.
        """
        with self._lock:
            if not self._request_shutdown_listener:
                # Not in a shutdown listen state.
                return
            self._last_event_time = time.time()
            self._final_shutdown_time = self._last_event_time + self._total_wait_time
            self._active = True

            self._bus.trigger(
                EVENT_ID_SYSTEM_SHUTDOWN,
                TARGET_ID_SYSTEM,
                SystemShutdownEvent()
            )

            # Listen to any event in order to bump up the quient time sleep.
            self._any_listener = self._bus.add_listener(
                TARGET_WILDCARD, _as_any_listener, self.on_any_event
            )

            self._thread = threading.Thread(
                name='Detect Shutdown',
                target=self.time_runner,
                daemon=True
            )


    def on_any_event(
            self,
            event_id: EventId, target_id: ParticipantId,
            event_obj: object # pylint: disable=unused-argument
    ) -> None:
        """
        Waiting for halt scenario phase.

        Listener for any event.  When it happens, the last event time is bumped up.
        """
        log(
            VERBOSE, ShutdownTimer,
            'Event after shutdown: {0} to {1}',
            event_id, target_id
        )
        if event_id == EVENT_ID_SYSTEM_HALTED:
            # Something else halted the system.
            self.stop_shutdown_listener()
        elif event_id == EVENT_ID_REQUEST_CANCEL_SYSTEM_SHUTDOWN:
            # Shutdown was cancelled
            self.setup_shutdown_request_listener()
            self._bus.trigger(
                EVENT_ID_SYSTEM_SHUTDOWN_CANCELLED,
                TARGET_ID_SYSTEM,
                SystemShutdownCancelledEvent()
            )
        elif event_id == EVENT_ID_SYSTEM_SHUTDOWN_CANCELLED:
            # Shutdown was cancelled
            self.setup_shutdown_request_listener()
        else:
            self._last_event_time = time.time()


    def time_runner(self) -> None:
        """
        Thread runner that wakes up at intervals decided by the quiet period
        to see if the queue should be stopped yet.
        """
        while True:
            now = time.time()
            with self._lock:
                if not self._active or threading.current_thread() != self._thread:
                    return
                # Find the timeout that happens first.
                wakeup = min(
                    self._final_shutdown_time,
                    self._last_event_time + self._quiet_period
                )
                if now < wakeup:
                    # Already passed the time to wake up.  Time to send the halt.
                    self._bus.trigger(
                        EVENT_ID_SYSTEM_HALTED,
                        TARGET_ID_SYSTEM,
                        SystemHaltedEvent()
                    )
                    self._active = False
                    return
            time.sleep(wakeup - now)


def _as_any_listener(
        callback: EventCallback[object]
) -> ListenerSetup[object]:
    return (EVENT_WILDCARD, callback,)

def _as_request_shutdown_listener(
        callback: EventCallback[RequestSystemShutdownEvent]
) -> ListenerSetup[RequestSystemShutdownEvent]:
    return (EVENT_ID_REQUEST_SYSTEM_SHUTDOWN, callback,)
