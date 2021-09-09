
"""
Sets up the timer.
"""

import time
from typing import Optional, Callable
from ...core.timer.api.events import (
    send_timer_event,
)
from ...base import (
    EventBus,
    EventId,
    ParticipantId,

    log,
    DEBUG,
    INFO,
)
from ...core.state.api import (
    StateStoreUpdatedEvent,
)
from .config import (
    TimerConfig,
)
from ...aid.thread import (
    Thread,
    create_loop_thread,
)


class BusTimer:
    """
    The timer event firing object.  Shouldn't be used directly.  Instead, use
    the `bootstrap_timer` function.

    Made "public" for unit test ease.
    """
    __slots__ = (
        '_config', '_bus', '_running', '_thread', 'sleeper',
        'mk_thread', '_last_time',
        '_disposed',
    )
    _thread: Optional[Thread]

    def __init__(self, bus: EventBus, config: TimerConfig):
        self._running = False
        self._config = config
        self._bus = bus
        self._thread = None
        self.sleeper = time.sleep
        self.mk_thread = _create_timer_thread
        self._last_time = -1.0
        self._disposed = False

    def dispose(self) -> None:
        if not self._disposed:
            self._disposed = True
            self._config = TimerConfig(self._config.interval_seconds, False)

    @property
    def is_running(self) -> bool:
        """Is the timer thread running?"""
        return self._thread is not None and self._thread.is_alive()

    def on_config_change(
            self,
            _eid: EventId, _tid: ParticipantId,
            update_event: StateStoreUpdatedEvent[TimerConfig]
    ) -> None:
        """Event notification of a configuration change."""
        if self._disposed:
            return
        new_config = update_event.state
        activate = not self._config.active and new_config.active
        self._config = new_config
        if activate and not self._running:
            # Note: sleeping during a non-io event is a big no-no.
            # if self._thread:
            #     self._thread.join(0.1)
            self._last_time = -1.0
            mk_thread: CreateThreadType = self.mk_thread
            self._thread = mk_thread(self._bus, self.is_config_active, self.run_in_loop)
            self._thread.start()
            log(
                INFO, BusTimer,
                'Starting timer heartbeat event, firing every {0} seconds',
                self._config.interval_seconds
            )

    def is_config_active(self) -> bool:
        return not self._disposed and self._config.active

    def run_in_loop(self) -> None:
        if not self.is_config_active():
            return

        # Wait for the interval since the last sleep started.
        now_time = time.time()
        if self._last_time < 0:
            self._last_time = now_time
        sleep_time = self._config.interval_seconds - (now_time - self._last_time)
        self._last_time = now_time
        if sleep_time > 0:
            self.sleeper(sleep_time)
        else:
            # May want to extend the interval time automatically.
            log(
                DEBUG, 'system.timer',
                'Timer interval exceeded by {0} seconds', -sleep_time
            )
        if self._config.active:
            send_timer_event(self._bus)


def _create_timer_thread_fn(
        bus: EventBus,
        is_active: Callable[[], bool],
        callback: Callable[[], None]
) -> Thread:
    return create_loop_thread(
        bus,
        'timer-event-generator',
        True,
        callback,
        is_active,
        True
    )


CreateThreadType = Callable[
    [EventBus, Callable[[], bool], Callable[[], None]], Thread
]
_create_timer_thread: CreateThreadType = _create_timer_thread_fn
