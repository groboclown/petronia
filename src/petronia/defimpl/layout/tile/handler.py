
# mypy: allow-any-expr
# mypy: allow-any-explicit

"""
The intermediary between the EventBus events and the tile controller.
"""

from typing import Iterable, Any
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
    VirtualScreenInfo,
)
from .config import (
    TileLayoutConfig,
    CONFIG_ID_TILE_LAYOUT,
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

    # Use the wait-for-initialization startup pattern.

    tile_config = StateWatch(listeners, CONFIG_ID_TILE_LAYOUT, TileLayoutConfig([], {}))
    screen_state = StateWatch(listeners, STATE_ID_SCREENS, ScreenState(VirtualScreenInfo([])))

    def on_state_change(val: Any) -> None:
        if tile_config.is_set and screen_state.is_set:
            # Boot up the tile event handler.
            TileEventHandler(bus, listeners, tile_config, screen_state)

    tile_config.set_listener(on_state_change)
    screen_state.set_listener(on_state_change)


class TileEventHandler:
    """
    Handle the tile events, and send the right ones.
    """

    __slots__ = (
        '__bus',
        '__listeners',
        '__ctrl',
        '__config',
        '__screens',
    )

    def __init__(
            self, bus: EventBus,
            listeners: ListenerSet,
            tile_config: StateWatch[TileLayoutConfig],
            screen_state: StateWatch[ScreenState]
    ):
        self.__bus = bus
        #self.__ctrl =
        self.__listeners = listeners
        self.__config = tile_config.state
        self.__screens = screen_state.state

        screen_state.set_listener(self._on_screen_state_changed)
        listeners.listen(
            TARGET_ID_WINDOW_CREATION, as_native_window_created_listener, self._on_window_created
        )

    def _on_screen_state_changed(self, state: ScreenState) -> None:
        # TODO find the new layout that matches the screens.
        raise NotImplementedError()

    def _on_tile_config_changed(self, config: TileLayoutConfig) -> None:
        # TODO found out the new layout that matches the screens.
        raise NotImplementedError()

    def _on_window_created(
            self,
            event_id: EventId,
            target_id: ParticipantId,
            event_obj: NativeWindowCreatedEvent
    ) -> None:
        raise NotImplementedError()
