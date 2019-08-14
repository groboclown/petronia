
"""
Special logic for handling shutdown events.

On shutdown requests, waits for either a no-event quiet period or a total
timeout.  If either is surpassed, then a halt is sent out.
"""

import time
import threading
from typing import Optional
from ....aid.simp import (
    ParticipantId,
    log,
    VERBOSE,
    DEBUG,
    TRACE,
    EventBus,
    EventCallback,
    EventId,
    ListenerId,
)
from ....aid.bootstrap import (
    ListenerSetup,
    EVENT_WILDCARD,
    TARGET_WILDCARD,
)
from ....aid.state_swap import StateSwapController
from ....base.events.system_events import (
    TARGET_ID_SYSTEM,

    SystemHaltedEvent,
    EVENT_ID_SYSTEM_HALTED,
)
from ....core.shutdown.api.events import (
    TARGET_ID_SYSTEM_SHUTDOWN,

    RequestSystemShutdownEvent,
    as_request_system_shutdown_listener,

    SystemShutdownEvent,
    EVENT_ID_SYSTEM_SHUTDOWN,

    EVENT_ID_REQUEST_CANCEL_SYSTEM_SHUTDOWN,

    SystemShutdownCancelledEvent,
    EVENT_ID_SYSTEM_SHUTDOWN_CANCELLED,

    SystemShutdownFinalizeEvent,
    EVENT_ID_SYSTEM_SHUTDOWN_FINALIZE,
)
from ....core.timer.api.events import EVENT_ID_TIMER

# TODO use the Timer helper
# TODO add configuration state listeners for the timeout values.


def setup_shutdown_handler(
        bus: EventBus,
        cancel_quiet_timeout: float, cancel_global_timeout: float,
        finalize_quiet_timeout: float, finalize_global_timeout: float
) -> None:
    """
    Sets up the shutdown state chain.
    """
    controller = StateSwapController()
    _WaitForShutdown(bus, controller)
    _CancellableShutdown(bus, controller, cancel_quiet_timeout, cancel_global_timeout)
    _FinalizeShutdown(bus, controller, finalize_quiet_timeout, finalize_global_timeout)
    controller.switch_state(_STATE_WAIT_FOR_SHUTDOWN)



_STATE_WAIT_FOR_SHUTDOWN = 'normal'
class _WaitForShutdown:
    """
    State while waiting for a shutdown request to happen.
    """
    __slots__ = (
        '__bus', '__controller', '_listener',
    )
    _listener: Optional[ListenerId]

    def __init__(self, bus: EventBus, controller: StateSwapController) -> None:
        self.__bus = bus
        self.__controller = controller
        self._listener = None

        controller.add_state(
            _STATE_WAIT_FOR_SHUTDOWN,
            self._on_setup,
            self._on_stop
        )

    def _on_setup(self) -> None:
        if self._listener:
            # bad state
            return
        log(VERBOSE, setup_shutdown_handler, 'Awating shutdown request.')
        self._listener = self.__bus.add_listener(
            TARGET_ID_SYSTEM_SHUTDOWN,
            as_request_system_shutdown_listener,
            self._on_request_shutdown
        )

    def _on_stop(self) -> None:
        listener = self._listener
        self._listener = None
        if listener:
            log(DEBUG, _WaitForShutdown, 'Stopping.')
            self.__bus.remove_listener(listener)

    def _on_request_shutdown(
            self,
            event_id: EventId, target_id: ParticipantId, event_obj: RequestSystemShutdownEvent # pylint: disable=unused-argument
    ) -> None:
        log(DEBUG, _WaitForShutdown, 'Switching to cancellable shutdown state.')
        self.__bus.trigger(
            EVENT_ID_SYSTEM_SHUTDOWN,
            TARGET_ID_SYSTEM_SHUTDOWN,
            SystemShutdownEvent()
        )
        self.__controller.switch_state(_STATE_CAN_BE_CANCELLED)


_STATE_CAN_BE_CANCELLED = 'cancellable'
class _CancellableShutdown:
    """
    State while the shutdown can be cancelled.
    """
    __slots__ = (
        '__bus', '__controller', '__quiet_timeout', '__global_timeout',
        '_listener', '__next_quiet_expires', '__next_global_expires',
    )
    _listener: Optional[ListenerId]

    def __init__(
            self, bus: EventBus, controller: StateSwapController,
            quiet_timeout: float, global_timeout: float
    ) -> None:
        self.__bus = bus
        self.__controller = controller
        self.__quiet_timeout = quiet_timeout
        self.__global_timeout = global_timeout
        self.__next_quiet_expires = 0.0
        self.__next_global_expires = 0.0
        self._listener = None

        controller.add_state(
            _STATE_CAN_BE_CANCELLED,
            self._on_setup,
            self._on_stop,
        )

    def _on_setup(self) -> None:
        # Wait for a quiet period.  This means listen to all events.
        if self._listener:
            # Bad state...
            return
        log(VERBOSE, setup_shutdown_handler, 'Starting shutdown phase.  User can still cancel the process.')
        self._listener = self.__bus.add_listener(
            TARGET_WILDCARD,
            _as_any_listener,
            self._on_any_event
        )
        now = time.time()
        self.__next_quiet_expires = now + self.__quiet_timeout
        self.__next_global_expires = now + self.__global_timeout

    def _on_stop(self) -> None:
        log(DEBUG, _CancellableShutdown, 'Stopping.')
        listener = self._listener
        self._listener = None
        if listener:
            self.__bus.remove_listener(listener)

    def _on_any_event(
            self, event_id: EventId,
            target_id: ParticipantId, event_obj: object # pylint: disable=unused-argument
    ) -> None:
        if not self._listener:
            # Not active, so don't do anything.
            return
        now = time.time()
        if event_id == EVENT_ID_SYSTEM_HALTED:
            # Something else halted the system.
            self.__controller.dispose()
            return
        if event_id == EVENT_ID_REQUEST_CANCEL_SYSTEM_SHUTDOWN:
            # Shutdown was cancelled
            self.__bus.trigger(
                EVENT_ID_SYSTEM_SHUTDOWN_CANCELLED,
                TARGET_ID_SYSTEM,
                SystemShutdownCancelledEvent()
            )
            log(DEBUG, _CancellableShutdown, 'Encountered shutdown cancel request.  Switching back to normal wait mode.')
            self.__controller.switch_state(_STATE_WAIT_FOR_SHUTDOWN)
            return
        if event_id == EVENT_ID_SYSTEM_SHUTDOWN_CANCELLED:
            # Shutdown was cancelled by something else.
            log(DEBUG, _CancellableShutdown, 'Encountered shutdown cancel.  Switching back to normal wait mode.')
            self.__controller.switch_state(_STATE_WAIT_FOR_SHUTDOWN)
            return

        # Time analysis
        if event_id != EVENT_ID_TIMER:
            # A non-timer event, so it counts towards the non-quiet period.
            self.__next_quiet_expires = now + self.__quiet_timeout

        log(
            TRACE,
            _CancellableShutdown,
            'Encountered an event during cancelable state.  Now: {0}, quiet timeout: {1}, global timeout: {2}',
            now, self.__next_quiet_expires, self.__next_global_expires
        )
        if now >= self.__next_quiet_expires or now >= self.__next_global_expires:
            self.__bus.trigger(
                EVENT_ID_SYSTEM_SHUTDOWN_FINALIZE,
                TARGET_ID_SYSTEM_SHUTDOWN,
                SystemShutdownFinalizeEvent())
            self.__controller.switch_state(_STATE_SHUTDOWN_FINALIZE)


_STATE_SHUTDOWN_FINALIZE = 'finalize'
class _FinalizeShutdown:
    """
    State while the final shutdown is happening, which can't be cancelled.
    Because the finalizer runs while things stop, such as the timer thread,
    this must use its own thread to mark the time.
    """
    __slots__ = (
        '__bus', '__controller', '__quiet_timeout', '__global_timeout',
        '_listener', '__next_quiet_expires', '__next_global_expires',
        '_thread',
    )
    _listener: Optional[ListenerId]
    _thread: Optional[threading.Thread]

    def __init__(
            self, bus: EventBus, controller: StateSwapController,
            quiet_timeout: float, global_timeout: float
    ) -> None:
        self.__bus = bus
        self.__controller = controller
        self.__quiet_timeout = quiet_timeout
        self.__global_timeout = global_timeout
        self.__next_quiet_expires = 0.0
        self.__next_global_expires = 0.0
        self._listener = None
        self._thread = None

        controller.add_state(
            _STATE_SHUTDOWN_FINALIZE,
            self._on_setup,
            self._on_stop,
        )

    def _on_setup(self) -> None:
        # Wait for a quiet period.  This means listen to all events.
        if self._listener:
            # Bad state...
            return
        log(VERBOSE, setup_shutdown_handler, 'Cancel period passed.  Committing to system shutdown.')
        self._listener = self.__bus.add_listener(
            TARGET_WILDCARD,
            _as_any_listener,
            self._on_any_event
        )
        self._thread = threading.Thread(
            name='Shutdown Timer',
            target=self._timer_thread,
            daemon=True
        )
        now = time.time()
        self.__next_quiet_expires = now + self.__quiet_timeout
        self.__next_global_expires = now + self.__global_timeout
        self._thread.start()

    def _on_stop(self) -> None:
        listener = self._listener
        thread = self._thread
        self._listener = None
        self._thread = None
        if listener:
            self.__bus.remove_listener(listener)
        if thread:
            thread.join()

    def _timer_thread(self) -> None:
        while self._listener:
            now = time.time()
            if self.__check_timeout(now):
                log(DEBUG, _FinalizeShutdown, 'Timer thread stopping due to timeout.')
                return
            # Sleep until a timer expires.
            # This timer can only increase, so this sleep will be the minimal time
            # required to sleep.
            wakeup = min(self.__next_global_expires, self.__next_quiet_expires) - now
            log(TRACE, _FinalizeShutdown, 'Timer thread waiting for {0} seconds', wakeup)
            time.sleep(wakeup)

    def _on_any_event(
            self, event_id: EventId,
            target_id: ParticipantId, event_obj: object # pylint: disable=unused-argument
    ) -> None:
        if not self._listener:
            # Not active, so don't do anything.
            return
        now = time.time()
        if event_id == EVENT_ID_SYSTEM_HALTED:
            # Something else halted the system.
            self.__controller.dispose()
            return

        # Time analysis
        if event_id != EVENT_ID_TIMER:
            # A non-timer event, so it counts towards the non-quiet period.
            self.__next_quiet_expires = now + self.__quiet_timeout

        self.__check_timeout(now)

    def __check_timeout(self, now: float) -> bool:
        if now >= self.__next_quiet_expires or now >= self.__next_global_expires:
            log(TRACE, _FinalizeShutdown, 'timeout exceeded; halting system.')
            self.__controller.dispose()
            self.__bus.trigger(
                EVENT_ID_SYSTEM_HALTED,
                TARGET_ID_SYSTEM,
                SystemHaltedEvent()
            )
            return True
        log(
            TRACE, _FinalizeShutdown,
            'Still waiting for shutdown time.  now: {0}, quiet expires: {1}, global expires: {2}',
            now, self.__next_quiet_expires, self.__next_global_expires
        )
        return False



def _as_any_listener(
        callback: EventCallback[object]
) -> ListenerSetup[object]:
    return (EVENT_WILDCARD, callback,)
