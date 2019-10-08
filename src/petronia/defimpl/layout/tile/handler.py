
"""
The intermediary between the EventBus events and the tile controller.
"""

from typing import Iterable
from ....aid.std import (
    EventBus,
    EventId,
    ParticipantId,
    StateStoreUpdatedEvent,
    as_state_change_listener,
    ListenerSet,
    StateWatch,
)
from ....core.platform.api import (
    NativeWindowFocusedEvent,
    as_native_window_focused_listener,
    NativeWindowFlashedEvent,
    as_native_window_flashed_listener,
    TARGET_ID_WINDOW_CREATION,
    NativeWindowCreatedEvent,
    as_native_window_created_listener,
    NativeWindowClosedEvent,
    as_native_window_closed_listener,

    send_request_move_native_window_event,
    send_request_focus_native_window_event,
    send_request_close_native_window_event,

    WindowMatcher,

    ScreenState,
    STATE_ID_SCREENS,
)
from .config.layout import (
    match_layouts_to_screens,
    RootTileLayout,
)
from .controller import (
    TileController,
)


def startup_tile_event_handler(
        bus: EventBus,
        default_layout: RootTileLayout,
        listeners: ListenerSet
) -> None:
    """

    :param bus:
    :param default_layout:
    :param listeners:
    :return:
    """
    pass


class TileEventHandler:
    """
    Handle the tile events, and send the right ones.
    """

    __slots__ = (
        '__bus',
        '__ctrl',
        '__layouts',
        '__listeners',
        '__disposed',
    )

    def __init__(
            self, bus: EventBus,
            layouts: Iterable[RootTileLayout],
            listeners: ListenerSet
    ):
        self.__bus = bus
        #self.__ctrl =
        self.__listeners = listeners
        self.__disposed = False

        listeners.listen(
            TARGET_ID_WINDOW_CREATION, as_native_window_created_listener, self._on_window_created
        )
        listeners.listen(STATE_ID_SCREENS, as_state_change_listener, self._on_screen_state_changed)  # type: ignore

    def _on_screen_state_changed(
            self,
            event_id: EventId,
            target_id: ParticipantId,
            event_obj: StateStoreUpdatedEvent[ScreenState]
    ) -> None:
        # TODO find the new layout that matches the screens.
        raise NotImplementedError()

    def _on_window_created(
            self,
            event_id: EventId,
            target_id: ParticipantId,
            event_obj: NativeWindowCreatedEvent
    ) -> None:
        raise NotImplementedError()
