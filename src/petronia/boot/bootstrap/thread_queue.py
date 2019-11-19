
# mypy: allow-any-expr
# mypy: allow-any-explicit
# mypy: allow-any-generics

"""
Core thread queue handler.
"""

from typing import Sequence, Tuple, List, Any
from threading import Lock
from ...base.bus import (
    QUEUE_EVENT_IO,
    QUEUE_EVENT_NORMAL,
    QUEUE_EVENT_HIGH,

    QueuePriority,
    EventId,
    EventCallback,
)
from ...base import (
    ParticipantId,

    log,
    ERROR,
    DEBUG,
    TRACE,
)
from ...base.util import WorkerThread
from ...defimpl.bus.local.bus_queue import (
    BusQueueManager,
    BasicEventCallback,
    BasicEventCallbackArguments,
)


_EventRequest = Tuple[EventCallback[Any], Tuple[EventId, ParticipantId, object]]


class CoreActionHandler(BusQueueManager):
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
        '__lock', '__next_io_thread', '__count',
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
        self.__count = 0
        self.__lock = Lock()

    def current_event_count(self) -> int:
        """Number of events queued to run or actively running."""
        with self.__lock:
            return self.__count

    def stop(self, timeout_seconds: float = 120) -> None:
        """Stop all running threads."""
        self._main_thread.complete()
        for thread in self._io_threads:
            thread.complete()
        self._main_thread.join(timeout_seconds)
        for thread in self._io_threads:
            thread.join(timeout_seconds)

    def queue_function(
            self,
            priority: QueuePriority,
            listeners: Sequence[BasicEventCallback],
            arguments: BasicEventCallbackArguments
    ) -> None:
        """
        Handle adding a listener request to the thread pool.
        """
        with self.__lock:
            if priority == QUEUE_EVENT_IO:
                # Run each listener in its own thread.
                for listener in listeners:
                    self.__count += 1
                    thread_index = self.__next_io_thread
                    self.__next_io_thread = (self.__next_io_thread + 1) % len(self._io_threads)
                    self._io_threads[thread_index].queue(listener, arguments)
            elif priority == QUEUE_EVENT_NORMAL:
                for listener in listeners:
                    self.__count += 1
                    self._main_events.append((listener, arguments,))
                    log(
                        TRACE, CoreActionHandler.queue_function,
                        'Queued listener.  Normal queue size: {0}',
                        len(self._main_events)
                    )
                self._main_thread.queue(self._main_handler)
            elif priority == QUEUE_EVENT_HIGH:
                for listener in listeners:
                    self.__count += 1
                    self._priority_events.append((listener, arguments,))
                    log(
                        TRACE, CoreActionHandler.queue_function,
                        'Queued listener.  Priority queue size: {0}',
                        len(self._priority_events)
                    )
                self._main_thread.queue(self._main_handler)
            log(
                DEBUG, CoreActionHandler,
                'Active event count: {0} (queued events)', self.__count
            )

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
            remaining = False
            with self.__lock:
                log(
                    TRACE, CoreActionHandler._main_handler,
                    'In main handler pull event loop.  Priority events: {0}, regular: {1}',
                    len(self._priority_events), len(self._main_events)
                )
                if self._priority_events:
                    log(
                        TRACE, CoreActionHandler._main_handler,
                        'Pulling priority event'
                    )
                    hand = self._priority_events[0]
                    del self._priority_events[0]
                    remaining = True
                elif self._main_events:
                    log(
                        TRACE, CoreActionHandler._main_handler,
                        'Pulling regular event'
                    )
                    hand = self._main_events[0]
                    del self._main_events[0]
                    remaining = True
            if hand:
                self._run_handler(hand)

    def _run_handler(self, req: _EventRequest) -> None:
        log(
            TRACE, CoreActionHandler._run_handler,
            'Running event {0}', req
        )
        try:
            req[0](req[1][0], req[1][1], req[1][2])
        except SystemExit:
            # Let everything else handle it.
            raise
        except BaseException as err: # pylint: disable=broad-except
            self._error_handler('Failed running {0}'.format(req[1]), err)
        finally:
            with self.__lock:
                self.__count -= 1
                log(
                    DEBUG, CoreActionHandler,
                    'Active event count: {0} (processed)',
                    self.__count
                )
