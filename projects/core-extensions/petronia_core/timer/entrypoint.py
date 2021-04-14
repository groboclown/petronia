"""Timer Entrypoint."""

from typing import Sequence, Dict, Any
import threading
import time
from petronia_common.event_stream import BinaryReader, BinaryWriter
from petronia_common.util import StdRet, RET_OK_NONE, tznow
from petronia_ext_lib.runner import LookupEventRegistryContext, EventRegistryContext
from .events.impl import timer as timer_event
from .state import timer as timer_state
from ..user_messages import report_send_receive_problems


def extension_entrypoint(
        reader: BinaryReader,
        writer: BinaryWriter,
        _config: Dict[str, Any],
        _args: Sequence[str],
) -> StdRet[None]:
    """Standardized entrypoint."""
    # Timer runs in the background, so it needs a proper thread-safe handler.
    context = LookupEventRegistryContext(reader, writer, None, None)
    tick_thread = TimerTick(context)
    context.register_eof_target(tick_thread.join)

    # Needs to load up the config

    # Needs to add in state change listeners.

    tick_thread.start()
    context.process_reader(timer_state.EXTENSION_NAME)

    return RET_OK_NONE


INTERVAL_TIME = [1.0]


def set_interval_seconds(seconds: float) -> None:
    """Set the interval time, in seconds, between timer ticks."""
    INTERVAL_TIME[0] = seconds


def get_interval_seconds() -> float:
    """Get the interval time, in seconds."""
    return INTERVAL_TIME[0]


class TimerTick:
    """The timer."""

    __slots__ = ('context', 'thread', 'alive')

    def __init__(self, context: EventRegistryContext) -> None:
        self.context = context
        self.alive = True
        self.thread = threading.Thread(
            name='timer-tick',
            target=self._run,
            daemon=True,
        )

    def start(self) -> None:
        """Start the thread."""
        self.thread.start()

    def join(self) -> None:
        """Stop the thread."""
        self.alive = False
        self.thread.join()

    def _run(self) -> None:
        while self.alive:
            # print(f'sleeping for {get_interval_seconds()} seconds')
            time.sleep(get_interval_seconds())
            if self.alive:
                # print('sending event')
                report_send_receive_problems(
                    'timer',
                    self.context.send_event(
                        timer_event.HeartbeatEvent.UNIQUE_TARGET_FQN,
                        timer_event.HeartbeatEvent.UNIQUE_TARGET_FQN,
                        timer_event.HeartbeatEvent(tznow()),
                    ),
                )
