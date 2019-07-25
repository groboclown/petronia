
"""
Sets up the timer.
"""

import time
import threading
from typing import Optional, Callable, Sequence
from petronia3.extensions.timer.api.events import (
    EVENT_ID_TIMER, GLOBAL_TIMER_EVENT,
    TARGET_TIMER,
    TimerEvent,
)
from petronia3.system.logging import log, NOTICE
from petronia3.system.bus import (
    EventBus,
    EventId,
    register_event,
    QUEUE_EVENT_NORMAL,
)
from petronia3.system.participant import ParticipantId
from petronia3.extensions.state import (
    as_state_change_listener,
    StateStoreUpdatedEvent,
)
from .config import (
    TARGET_TIMER_CONFIG,
    DEFAULT_INTERVAL,
    TimerConfig,
    set_timer_config
)


EXTENSION_DEPENDENCIES: Sequence[str] = tuple()

def start_extension(bus: EventBus) -> None:
    """
    Get the timer started.

    There should only ever be one timer.  It is global, and should never be
    disabled.
    """
    register_event(
        bus,
        EVENT_ID_TIMER,
        QUEUE_EVENT_NORMAL,
        TimerEvent,
        GLOBAL_TIMER_EVENT
    )
    # Set the "active" to false, so that it can start itself up.
    config = TimerConfig(DEFAULT_INTERVAL, False)
    timer = BusTimer(bus, config)
    bus.add_listener(
        TARGET_TIMER_CONFIG,
        as_state_change_listener,
        timer.on_config_change
    )
    set_timer_config(bus, config)


class BusTimer:
    """
    The timer event firing object.  Shouldn't be used directly.  Instead, use
    the `bootstrap_timer` function.

    Made "public" for unit test ease.
    """
    __slots__ = ('_config', '_bus', '_running', '_thread', 'sleeper', 'mk_thread')
    _thread: Optional[threading.Thread]

    def __init__(self, bus: EventBus, config: TimerConfig):
        self._running = False
        self._config = config
        self._bus = bus
        self._thread = None
        self.sleeper = time.sleep
        self.mk_thread = _create_timer_thread

    @property
    def is_running(self) -> bool:
        """Is the timer thread running?"""
        return self._running

    def on_config_change(
            self,
            eid: EventId, tid: ParticipantId, # pylint: disable=unused-argument
            update_event: StateStoreUpdatedEvent[TimerConfig]
    ) -> None:
        """Event notification of a configuration change."""
        new_config = update_event.state
        activate = not self._config.active and new_config.active
        self._config = new_config
        if activate and not self._running:
            # Note: sleeping during a non-io event is a big no-no.
            # if self._thread:
            #     self._thread.join(0.1)
            mk_thread: Callable[[Callable[[], None]], threading.Thread] = self.mk_thread
            self._thread = mk_thread(self.run)
            self._thread.start()

    def run(self) -> None:
        """Run the timer in a thread."""
        self._running = True
        last_time = time.time()
        try:
            while self._config.active:
                # Wait for the interval since the last sleep started.
                now_time = time.time()
                sleep_time = self._config.interval_seconds - (now_time - last_time)
                last_time = now_time
                if sleep_time > 0:
                    self.sleeper(sleep_time)
                else:
                    # May want to extend the interval time automatically.
                    log(
                        NOTICE, 'system.timer',
                        'Timer interval exceeded by {0} seconds', -sleep_time
                    )
                if self._config.active:
                    self._bus.trigger(EVENT_ID_TIMER, TARGET_TIMER, GLOBAL_TIMER_EVENT)
        finally:
            self._running = False


def _create_timer_thread_fn(callback: Callable[[], None]) -> threading.Thread:
    return threading.Thread(name='timer-event-generator', daemon=True, target=callback)

_create_timer_thread: Callable[[Callable[[], None]], threading.Thread] = _create_timer_thread_fn
