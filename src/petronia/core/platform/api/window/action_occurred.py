
"""
Native window interactions.
"""

from .....aid.simp import (
    EventId,
    EventBus,
    EventCallback,
    ListenerSetup,
    ComponentId,
    create_singleton_identity,
)
from ..defs import (
    ScreenRect,
)


TARGET_ID_WINDOW_CREATION = create_singleton_identity('core.platform.api/native-window')

# ---------------------------------------------------------------------------
EVENT_ID_NATIVE_WINDOW_CREATED = EventId('core.platform.api native-window-created')


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


def as_native_window_created_listener(
        callback: EventCallback[NativeWindowCreatedEvent]
) -> ListenerSetup[NativeWindowCreatedEvent]:
    return (EVENT_ID_NATIVE_WINDOW_CREATED, callback,)


def send_native_window_created_event(
        bus: EventBus,
        window_id: ComponentId
) -> None:
    bus.trigger(EVENT_ID_NATIVE_WINDOW_CREATED, TARGET_ID_WINDOW_CREATION, NativeWindowCreatedEvent(window_id))


# ---------------------------------------------------------------------------
EVENT_ID_NATIVE_WINDOW_CLOSED = EventId('core.platform.api native-window-closed')


class NativeWindowClosedEvent:
    """
    The window was closed.  The corresponding state is removed.
    """

    __slots__ = ('__forced',)

    def __init__(self, forced: bool) -> None:
        self.__forced = forced

    @property
    def forced(self) -> bool:
        return self.__forced


def as_native_window_closed_listener(
        callback: EventCallback[NativeWindowClosedEvent]
) -> ListenerSetup[NativeWindowClosedEvent]:
    return (EVENT_ID_NATIVE_WINDOW_CLOSED, callback,)


def send_native_window_closed_event(
        bus: EventBus,
        window_id: ComponentId,
        forced: bool
) -> None:
    bus.trigger(EVENT_ID_NATIVE_WINDOW_CLOSED, window_id, NativeWindowClosedEvent(forced))


# ---------------------------------------------------------------------------
EVENT_ID_NATIVE_WINDOW_FLASHED = EventId('core.platform.api native-window-flashed')


class NativeWindowFlashedEvent:
    """
    The window sent a request to alert the user about it.
    """

    __slots__ = ()

    def __init__(self) -> None:
        pass


def as_native_window_flashed_listener(
        callback: EventCallback[NativeWindowFlashedEvent]
) -> ListenerSetup[NativeWindowFlashedEvent]:
    return (EVENT_ID_NATIVE_WINDOW_FLASHED, callback,)


def send_native_window_flashed_event(
        bus: EventBus,
        window_id: ComponentId
) -> None:
    bus.trigger(EVENT_ID_NATIVE_WINDOW_FLASHED, window_id, NativeWindowFlashedEvent())


# ---------------------------------------------------------------------------
EVENT_ID_NATIVE_WINDOW_MOVED = EventId('core.platform.api native-window-moved')


class NativeWindowMovedEvent:
    """
    The window moved or resized or changed visibility.
    """

    __slots__ = (
        '__new_area',
        '__is_visible',
    )

    def __init__(self, new_area: ScreenRect, is_visible: bool) -> None:
        self.__new_area = new_area
        self.__is_visible = is_visible

    @property
    def new_area(self) -> ScreenRect:
        return self.__new_area

    @property
    def is_visible(self) -> bool:
        return self.__is_visible


def as_native_window_moved_listener(
        callback: EventCallback[NativeWindowMovedEvent]
) -> ListenerSetup[NativeWindowMovedEvent]:
    return (EVENT_ID_NATIVE_WINDOW_MOVED, callback,)


def send_native_window_moved_event(
        bus: EventBus,
        window_id: ComponentId,
        area: ScreenRect,
        is_visible: bool
) -> None:
    bus.trigger(EVENT_ID_NATIVE_WINDOW_MOVED, window_id, NativeWindowMovedEvent(area, is_visible))


# ---------------------------------------------------------------------------
EVENT_ID_NATIVE_WINDOW_FOCUSED = EventId('core.platform.api native-window-focused')


class NativeWindowFocusedEvent:
    """
    The window was given focus.
    """

    __slots__ = ()

    def __init__(self) -> None:
        pass


def as_native_window_focused_listener(
        callback: EventCallback[NativeWindowFocusedEvent]
) -> ListenerSetup[NativeWindowFocusedEvent]:
    return (EVENT_ID_NATIVE_WINDOW_FOCUSED, callback,)


def send_native_window_focused_event(
        bus: EventBus,
        window_id: ComponentId
) -> None:
    bus.trigger(EVENT_ID_NATIVE_WINDOW_FOCUSED, window_id, NativeWindowFocusedEvent())
