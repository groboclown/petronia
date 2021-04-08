
"""
An object that grants access to a queue implementation along with simple
insights and control.
"""

from typing import Sequence
from .basic_event_bus import (
    BasicEventCallback,
    BasicEventCallbackArguments,
)
from ....base.bus import (
    QueuePriority,
)


class BusQueueManager:
    """
    An ABC that provides a bus queue function (QueueFunction) and simple
    information and control.  This helps allow for a more robust shutdown
    implementation from the system.
    """

    def queue_function(
            self,
            priority: QueuePriority,
            listeners: Sequence[BasicEventCallback],
            arguments: BasicEventCallbackArguments
    ) -> None:
        """Conforms to the QueueFunction prototype."""
        raise NotImplementedError()

    def current_event_count(self) -> int:
        """Number of event listeners queued to run or actively running."""
        raise NotImplementedError()

    def stop(self, timeout_seconds: float = 120) -> None:
        """Stop all running threads.  Will wait up to the timeout seconds
        for the threads to stop.  Whether this timeout is total timeout
        or per thread is dependent upon the implementation."""
        raise NotImplementedError()
