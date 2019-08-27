
"""
Native window interactions.  The target for these events is the window
component ID.
"""

from .....base import (
    EventId,
    ComponentId,
)


# ---------------------------------------------------------------------------
EVENT_ID_REQUEST_MOVE_NATIVE_WINDOW = EventId('core.platform.api move-native-window')


class RequestMoveNativeWindowEvent:
    """
    Request to move or resize a window.  A value of < 0 means that it
    shouldn't change.
    """
    __slots__ = ('__window_id', '__x', '__y', '__w', '__h',)

    def __init__(
            self, window_id: ComponentId,
            new_x: int, new_y: int, new_width: int, new_height: int
    ) -> None:
        self.__window_id = window_id
        self.__x = new_x
        self.__y = new_y
        self.__w = new_width
        self.__h = new_height

    @property
    def window_id(self) -> ComponentId:
        return self.__window_id

    @property
    def new_x(self) -> int:
        return self.__x

    @property
    def new_y(self) -> int:
        return self.__y

    @property
    def new_width(self) -> int:
        return self.__w

    @property
    def new_height(self) -> int:
        return self.__h


# ---------------------------------------------------------------------------
EVENT_ID_REQUEST_FOCUS_NATIVE_WINDOW = EventId('core.platform.api focus-native-window')


class RequestFocusNativeWindowEvent:
    """
    Set the window as focused and optionally raised to top.  Some platforms
    may ignore the raise-to-top value.
    """

    __slots__ = ('__window_id', '__raise',)

    def __init__(self, window_id: ComponentId, raise_to_top: bool) -> None:
        self.__window_id = window_id
        self.__raise = raise_to_top

    @property
    def window_id(self) -> ComponentId:
        return self.__window_id

    @property
    def raise_to_top(self) -> bool:
        return self.__raise



EVENT_ID_REQUEST_CLOSE_NATIVE_WINDOW = EventId('core.platform.api close-native-window')

class RequestCloseNativeWindowEvent:
    """
    Send a request to close a window.
    """

    __slots__ = ('__window_id', '__force',)

    def __init__(self, window_id: ComponentId, force: bool) -> None:
        self.__window_id = window_id
        self.__force = force

    @property
    def window_id(self) -> ComponentId:
        return self.__window_id

    @property
    def force(self) -> bool:
        return self.__force
