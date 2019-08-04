
"""
Creates the managed queue instance.
"""

from petronia3.extensions.platform.preboot import (
    EventQueueModel,
)

from petronia3_ext.bus.local.bus_queue import (
    BusQueueManager,
)

from .thread_queue import CoreActionHandler


class RootEventQueueModel(EventQueueModel):
    """
    API that can be provided by the queue model.
    """
    __slots__ = ('io_thread_count',)

    def __init__(self, io_thread_count: int) -> None:
        self.io_thread_count = io_thread_count


DEFAULT_IO_THREAD_COUNT = 4


def create_managed_queue(queue_model: EventQueueModel) -> BusQueueManager:
    """
    Create the managed queue based on the model.  This can be used to create
    the event bus and handle shutdown requests.
    """
    io_thread_count = DEFAULT_IO_THREAD_COUNT
    if isinstance(queue_model, RootEventQueueModel):
        io_thread_count = queue_model.io_thread_count

    return CoreActionHandler(io_thread_count)
