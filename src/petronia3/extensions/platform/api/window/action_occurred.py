
"""
Native window interactions.
"""

from .....system.bus import EventId
from .....system.participant import (
    ComponentId,
)


EVENT_ID_WINDOW_CREATED = EventId('core.platform.api native-window-created')

class NativeWindowCreatedEvent:
    """
    A new window was created.  Its state is stored with the window_id.
    Behavior such as the window moving or gaining focus are associated with
    state changes for the window.
    """
    __slots__ = ('__id',)

    def __init__(
            self,
            window_id: ComponentId
    ) -> None:
        self.__id = window_id

    @property
    def window_id(self) -> ComponentId:
        return self.__id



EVENT_ID_NATIVE_WINDOW_CLOSED = EventId('core.platform.api native-window-closed')

class NativeWindowClosedEvent:
    """
    The window was closed.  The corresponding state is removed.
    """

    __slots__ = ('__id', '__forced')

    def __init__(self, window_id: ComponentId, forced: bool) -> None:
        self.__id = window_id
        self.__forced = forced

    @property
    def window_id(self) -> ComponentId:
        return self.__id

    @property
    def forced(self) -> bool:
        return self.__forced
