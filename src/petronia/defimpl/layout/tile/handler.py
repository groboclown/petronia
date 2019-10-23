
# mypy: allow-any-expr
# mypy: allow-any-explicit

"""
The intermediary between the EventBus events and the tile controller.
"""

from typing import Tuple, Iterable, Optional, Any
from typing import cast as t_cast

from ....aid.std import (
    EventBus,
    EventId,
    ParticipantId,
    ComponentId,
    ListenerSet,
    StateWatch,
    report_error,
    TARGET_WILDCARD,
    readonly_dict,
    log, INFO, DEBUG,
)
from ....core.config_persistence.api import PersistentConfigurationState
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
    send_request_set_native_window_visibility_event,

    ScreenState,
    STATE_ID_SCREENS,
    VirtualScreenInfo,
    VirtualScreenArea,
    ScreenArea,

    STATE_ID_ACTIVE_WINDOWS,
    AllActiveWindowsState,
    NativeWindowState,
)
from ....core.layout.api import (
    TARGET_ID_LAYOUT,
    send_layout_changed_event,
    RequestMoveResizeFocusedWindowEvent,
    as_request_move_resize_focused_window_listener,
    RequestShiftLayoutFocusEvent,
    as_request_shift_layout_focus_listener,
    RequestSetFocusedWindowVisibilityEvent,
    as_request_set_focused_window_visibility_listener,
)
from .config import (
    TileLayoutConfig,
    CONFIG_ID_TILE_LAYOUT,
    MatchWindowToPortal,
    parse_config,
)
from .controller import (
    TileController,
)
from .convert_config import (
    convert_config,
)
from .portal import (
    Portal,
    POSITION_FAVOR_FILL,
    POSITION_FAVOR_N_EDGE,
    POSITION_FAVOR_E_EDGE,
    POSITION_FAVOR_S_EDGE,
    POSITION_FAVOR_W_EDGE,
    POSITION_FAVOR_NE,
    POSITION_FAVOR_SE,
    POSITION_FAVOR_NW,
    POSITION_FAVOR_SW,
    POSITION_FAVOR_RESTRICTED_N_EDGE,
    POSITION_FAVOR_RESTRICTED_E_EDGE,
    POSITION_FAVOR_RESTRICTED_S_EDGE,
    POSITION_FAVOR_RESTRICTED_W_EDGE,
    POSITION_FAVOR_RESTRICTED_NE,
    POSITION_FAVOR_RESTRICTED_SE,
    POSITION_FAVOR_RESTRICTED_NW,
    POSITION_FAVOR_RESTRICTED_SW,
)


PORTAL_FAVOR_MAP = readonly_dict({
    "fill": POSITION_FAVOR_FILL,

    "n": POSITION_FAVOR_N_EDGE,
    "e": POSITION_FAVOR_E_EDGE,
    "s": POSITION_FAVOR_S_EDGE,
    "w": POSITION_FAVOR_W_EDGE,

    "n-r": POSITION_FAVOR_RESTRICTED_N_EDGE,
    "e-r": POSITION_FAVOR_RESTRICTED_E_EDGE,
    "s-r": POSITION_FAVOR_RESTRICTED_S_EDGE,
    "w-r": POSITION_FAVOR_RESTRICTED_W_EDGE,

    "ne": POSITION_FAVOR_NE,
    "nw": POSITION_FAVOR_NW,
    "se": POSITION_FAVOR_SE,
    "sw": POSITION_FAVOR_SW,

    "ne-r": POSITION_FAVOR_RESTRICTED_NE,
    "nw-r": POSITION_FAVOR_RESTRICTED_NW,
    "se-r": POSITION_FAVOR_RESTRICTED_SE,
    "sw-r": POSITION_FAVOR_RESTRICTED_SW,

})


def startup_tile_event_handler(
        bus: EventBus,
        listeners: ListenerSet
) -> None:
    """

    :param bus:
    :param listeners:
    :return:
    """

    # Use the wait-for-initialization startup pattern.

    tile_config = StateWatch(listeners, CONFIG_ID_TILE_LAYOUT, PersistentConfigurationState({}))
    screen_state = StateWatch(listeners, STATE_ID_SCREENS, ScreenState(VirtualScreenInfo([
        VirtualScreenArea('', (0, 0, 0, 0,), True)
    ])))
    windows = StateWatch(listeners, STATE_ID_ACTIVE_WINDOWS, AllActiveWindowsState([]))

    def on_state_change(_val: Any) -> None:
        print("tile config? {0}; screen? {1}; windows? {2}".format(
            tile_config.is_set, screen_state.is_set, windows.is_set
        ))
        if tile_config.is_set and screen_state.is_set and windows.is_set:
            # Boot up the tile event handler.
            TileEventHandler(bus, listeners, tile_config, screen_state, windows)

    tile_config.set_listener(on_state_change)
    screen_state.set_listener(on_state_change)
    windows.set_listener(on_state_change)


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
        '__windows',
    )

    def __init__(
            self, bus: EventBus,
            listeners: ListenerSet,
            tile_config: StateWatch[PersistentConfigurationState],
            screen_state: StateWatch[ScreenState],
            windows: StateWatch[AllActiveWindowsState]
    ):
        self.__bus = bus
        self.__listeners = listeners
        self.__config = parse_config_data(bus, tile_config.state)
        self.__screens = screen_state.state
        self.__windows = windows.state

        listeners.listen(
            TARGET_ID_LAYOUT, as_request_set_focused_window_visibility_listener, self._req_window_visibility
        )
        listeners.listen(
            TARGET_ID_LAYOUT, as_request_shift_layout_focus_listener, self._req_shift_focus
        )
        listeners.listen(
            TARGET_ID_LAYOUT, as_request_move_resize_focused_window_listener, self._req_resize
        )
        screen_state.set_listener(self._on_screen_state_changed)
        tile_config.set_listener(self._on_tile_config_changed)
        windows.set_listener(self._on_windows_changed)
        self.__ctrl = do_layout(bus, self.__config, screen_state.state, windows.state)
        listeners.listen(
            TARGET_ID_WINDOW_CREATION, as_native_window_created_listener, self._on_window_created
        )
        listeners.listen(
            TARGET_WILDCARD, as_native_window_closed_listener, self._on_window_destroyed
        )
        listeners.listen(
            TARGET_WILDCARD, as_native_window_focused_listener, self._on_window_focused
        )

    # -----------------------------------------------------------------------
    # User Requests
    def _req_window_visibility(
            self,
            _event_id: EventId,
            _target_id: ParticipantId,
            event_obj: RequestSetFocusedWindowVisibilityEvent
    ) -> None:
        # Change the window to be minimized or restored.
        active_window = self.__ctrl.get_active_window()
        if active_window:
            send_request_set_native_window_visibility_event(
                self.__bus, active_window, event_obj.visible
            )

    def _req_shift_focus(
            self,
            _event_id: EventId,
            _target_id: ParticipantId,
            event_obj: RequestShiftLayoutFocusEvent
    ) -> None:
        """
        Changes the currently focused portal.  Uses the `name` to indicate
        the direction, and `index` to indicate the amount of move.  The direction names
        recognized are 'n', 's', 'e', and 'w'.  An index of 0 will be interpreted as a 1
        (this is due to the way Petronia handles the index if it isn't specified).

        FIXME add an option to move focus to a named portal.

        FIXME add an option to move the active window to a different portal.

        """
        action = (event_obj.name or '').lower()
        if action.find(':') > 0:
            # Named portal.
            portal_name = action[action.find(':') + 1:]
            pass
        if action.startswith('move-focus-'):
            direction = action[11:]
            # TODO check layout for wrap mode.
            dest_portal, new_active_cid = self.__ctrl.move_portal_focus(direction, event_obj.index, True)
            # TODO if the portal has chrome, send a notice that it's active.
            if new_active_cid:
                send_request_focus_native_window_event(self.__bus, new_active_cid, True)
            return
        if action.startswith('move-window-'):
            direction = action[12:]
            pass

    def _req_resize(
            self,
            _event_id: EventId,
            _target_id: ParticipantId,
            event_obj: RequestMoveResizeFocusedWindowEvent
    ) -> None:
        """
        Adjusts the size and position of the active portal, if possible.
        Only one of `dx` and `dy`, or `dw` and `dh` need be specified; the layout will
        use the correct one for the owning split's direction.
        Moving a portal (dx or dy) means resizing the sibling tiles so the active portal
        keeps its ame size.
        The `dz` has a special meaning - it flips the active window within the portal.
        """
        # if dw isn't given, try dh.
        resize = event_obj.dw or event_obj.dh
        if resize != 0:
            self.__ctrl.resize_active_split(resize)
        # if dx isn't given, try dy.
        move = event_obj.dx or event_obj.dy
        if move != 0:
            self.__ctrl.move_active_split(move)
        if event_obj.dz != 0:
            self.__ctrl.active_portal_window_switch(event_obj.dz)

    # -----------------------------------------------------------------------
    # State Change Events
    def _on_screen_state_changed(self, state: ScreenState) -> None:
        self.__screens = state
        self.__ctrl = do_layout(self.__bus, self.__config, self.__screens, self.__windows)

    def _on_tile_config_changed(self, config: PersistentConfigurationState) -> None:
        self.__config = parse_config_data(self.__bus, config)
        self.__ctrl = do_layout(self.__bus, self.__config, self.__screens, self.__windows)

    def _on_windows_changed(self, windows: AllActiveWindowsState) -> None:
        self.__windows = windows
        # No need to search the windows for changes, because that's
        # handled in the create + destroy.

    # -----------------------------------------------------------------------
    # Native Platform Events
    def _on_window_created(
            self,
            _event_id: EventId,
            _target_id: ParticipantId,
            event_obj: NativeWindowCreatedEvent
    ) -> None:
        assign_window_to_portal(self.__bus, self.__ctrl, event_obj.info, self.__config.matchers)

    def _on_window_destroyed(
            self,
            _event_id: EventId,
            target_id: ParticipantId,
            _event_obj: NativeWindowClosedEvent
    ) -> None:
        # Remove the window from that portal.
        if isinstance(target_id, tuple):
            self.__ctrl.remove_window(t_cast(ComponentId, target_id))

    def _on_window_focused(
            self,
            _event_id: EventId,
            target_id: ParticipantId,
            _event_obj: NativeWindowFocusedEvent
    ) -> None:
        if isinstance(target_id, tuple):
            self.__ctrl.on_window_focused(t_cast(ComponentId, target_id))


def do_layout(
        bus: EventBus, config: TileLayoutConfig, screens: ScreenState,
        windows: AllActiveWindowsState
) -> TileController:
    root, primary_index, errors = convert_config(config, screens.screens)
    for err in errors:
        report_error(bus, err)
    log(
        INFO, do_layout,
        'Using layout "{0}" (primary screen: {1})', root.name, primary_index
    )
    log(
        DEBUG, do_layout,
        'layout={0}', repr(root)
    )
    ctrl = TileController(root)
    for window in windows.windows:
        assign_window_to_portal(bus, ctrl, window, config.matchers)
    send_layout_changed_event(bus)
    return ctrl


def assign_window_to_portal(
        bus: EventBus, ctrl: TileController, window: NativeWindowState, matchers: Iterable[MatchWindowToPortal]
) -> None:
    portal, position = match_window_to_portal(ctrl, window, matchers)
    area = get_window_position(window, portal, position)
    send_request_move_native_window_event(
        bus, window.component_id, area
    )
    #print("DEBUG -- would have moved window {0} to portal {1} / area {2}".format(
    #    window, portal, area
    #))


def match_window_to_portal(
        ctrl: TileController, window: NativeWindowState, matchers: Iterable[MatchWindowToPortal]
) -> Tuple[Portal, str]:
    portal = ctrl.get_active_portal()
    position = "fill"
    for matcher in matchers:
        if matcher.is_window_property_match(window):
            portal = ctrl.get_named_portal(matcher.portal_name or '')
            position = matcher.position or "fill"
            break
    return portal, position.lower()


def get_window_position(window: NativeWindowState, portal: Portal, position: Optional[str]) -> ScreenArea:
    favor = PORTAL_FAVOR_MAP.get(position or '') or POSITION_FAVOR_FILL
    return portal.get_window_position(window.bordered_rect.get_area(), favor)


def parse_config_data(bus: EventBus, config: PersistentConfigurationState) -> TileLayoutConfig:
    res, errors = parse_config(config.persistent)
    for err in errors:
        report_error(bus, err)
    return res