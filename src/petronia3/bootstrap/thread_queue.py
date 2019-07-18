
"""
Core thread queue handler.
"""

from typing import Sequence, Tuple, List
from threading import Lock
from ..system.bus.event_bus import (
    QUEUE_EVENT_IO,
    QUEUE_EVENT_NORMAL,
    QUEUE_EVENT_NOW,

    QueuePriority,
    EventId,
    EventCallback,
)
from ..system.participant import (
    ParticipantId,
)
from ..system.logging import (
    log,
    ERROR,
)
from ..util import WorkerThread

_EventRequest = Tuple[EventCallback, Tuple[EventId, ParticipantId, object]]

class CoreActionHandler:
    """
    Uses a collection of worker threads to handle the requests.
    All non-io events are handled in the same event queue.  The
    I/O events, because they can block each other, are sent to
    a set of worker threads.

    Use this as a queuer by referencing the bound method
    `queuer`.
    """
    __slots__ = (
        '_io_threads', '_main_thread',
        '_main_events', '_priority_events',
        '__lock', '__next_io_thread'
    )
    _io_threads: List[WorkerThread]
    _main_events: List[_EventRequest]
    _priority_events: List[_EventRequest]

    def __init__(self, io_thread_count: int) -> None:
        self._io_threads = []
        assert io_thread_count > 0
        for i in range(io_thread_count):
            self._io_threads.append(WorkerThread(
                'io_event ' + str(i), False, self._error_handler
            ))
        self._main_thread = WorkerThread('main_event', False, self._error_handler)
        self._main_events = []
        self._priority_events = []
        self.__next_io_thread = 0
        self.__lock = Lock()

    def stop(self, timeout: float = 100) -> None:
        """Stop all running threads."""
        self._main_thread.complete()
        for thread in self._io_threads:
            thread.complete()
        self._main_thread.join(timeout)
        for thread in self._io_threads:
            thread.join(timeout)

    def queuer(
            self,
            priority: QueuePriority,
            listeners: Sequence[EventCallback],
            arguments: Tuple[EventId, ParticipantId, object]
    ) -> None:
        """
        Handle adding a listener request to the thread pool.
        """
        with self.__lock:
            if priority == QUEUE_EVENT_IO:
                # Run each listener in its own thread.
                for listener in listeners:
                    thread_index = self.__next_io_thread
                    self.__next_io_thread = (self.__next_io_thread + 1) % len(self._io_threads)
                    self._io_threads[thread_index].queue(listener, arguments)
            elif priority == QUEUE_EVENT_NORMAL:
                for listener in listeners:
                    self._main_events.append((listener, arguments,))
                self._main_thread.queue(self._main_handler)
            elif priority == QUEUE_EVENT_NOW:
                for listener in listeners:
                    self._priority_events.append((listener, arguments,))
                self._main_thread.queue(self._main_handler)

    def _error_handler(self, msg: str, err: BaseException) -> None:
        log(ERROR, 'EventQueue', msg + ': {0}', err)

    def _main_handler(self) -> None:
        # Loop through all the pending events.
        # All events in the priority list take priority over the
        # normal events.  Could use a priority queue, but, meh,
        # this is easy.
        remaining = True
        while remaining:
            hand = None
            with self.__lock:
                if self._priority_events:
                    hand = self._priority_events[0]
                    del self._priority_events[0]
                    remaining = True
                elif self._main_events:
                    hand = self._main_events[0]
                    del self._main_events[0]
            if hand:
                hand[0](hand[1][0], hand[1][1], hand[1][2])
