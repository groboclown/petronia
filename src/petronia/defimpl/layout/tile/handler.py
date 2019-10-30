
# mypy: allow-any-expr
# mypy: allow-any-explicit

"""
The intermediary between the EventBus events and the tile controller.
"""

from typing import Tuple, Iterable, Sequence, Any
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
    log, WARN, INFO, DEBUG,
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
from ....core.hotkeys.api import (
    as_hotkey_event_triggered_listener,
    HotkeyEventTriggeredEvent,
)
from ....base.util.simple_type import (
    PersistType,
)
from .consts import (
    MODULE_ID,
    PORTAL_COMPONENT_CATEGORY,
)
from .hotkeys import (
    HOTKEY_ACTION_FILL_PORTAL,
    HOTKEY_SCHEMA_FILL_PORTAL,
    HOTKEY_SCHEMA_FILL_PORTAL__FILL,

    HOTKEY_ACTION_NAME_PORTAL,
    HOTKEY_SCHEMA_NAME_PORTAL,
    HOTKEY_SCHEMA_NAME_PORTAL__NAME,

    HOTKEY_ACTION_ADD_PORTAL,
    HOTKEY_SCHEMA_ADD_PORTAL,

    HOTKEY_ACTION_REMOVE_PORTAL,
    HOTKEY_SCHEMA_REMOVE_PORTAL,

    HOTKEY_ACTION_MOVE_WINDOW,
    HOTKEY_SCHEMA_MOVE_WINDOW,
    HOTKEY_SCHEMA_MOVE_WINDOW__NAME,
    HOTKEY_SCHEMA_MOVE_WINDOW__DIRECTION,
)
from .config import (
    TileLayoutConfig,
    CONFIG_ID_TILE_LAYOUT,
    MatchWindowToPortal,
    parse_config,
    parse_position,
    parse_direction,
)
from .controller import (
    TileController,
    AdjustedPortal,
    ADJUSTED_PORTAL_ACTION_REMOVED,
    ADJUSTED_PORTAL_ACTION_RESIZED,
)
from .convert_config import (
    convert_config,
)
from .portal import (
    Portal,
)


# TODO add in Tiling State updates.


def startup_tile_event_handler(
        bus: EventBus,
        listeners: ListenerSet
) -> None:
    """

    :param bus:
    :param listeners:
    :return:
    """

    listeners.bind_hotkey(HOTKEY_SCHEMA_FILL_PORTAL)
    listeners.bind_hotkey(HOTKEY_SCHEMA_NAME_PORTAL)
    listeners.bind_hotkey(HOTKEY_SCHEMA_ADD_PORTAL)
    listeners.bind_hotkey(HOTKEY_SCHEMA_REMOVE_PORTAL)
    listeners.bind_hotkey(HOTKEY_SCHEMA_MOVE_WINDOW)

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
        listeners.listen(
            MODULE_ID, as_hotkey_event_triggered_listener, self._req_hotkey
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
        """
        name = (event_obj.name or '').lower()
        count = min(1, event_obj.index)
        src_portal = self.__ctrl.get_active_portal()
        dest_portal = self.__ctrl.get_named_portal(name)
        if dest_portal == src_portal:
            # Might be a direction.  Try that.
            direction = parse_direction(name)
            if direction is None:
                # then it was a named portal that is the current portal, or an unknown direction,
                # or a non-existent portal.  In any case, it's a no-op.
                return
            # TODO check layout for wrap mode.
            src_portal, dest_portal, new_active_cid = self.__ctrl.move_portal_focus(direction, count, True)
        else:
            new_active_cid = dest_portal.get_visible_window()
        # TODO update portal state to indicate that a different portal is active.
        if new_active_cid:
            send_request_focus_native_window_event(self.__bus, new_active_cid, True)

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
        # TODO gather the windows + portals that changed, and send events to perform resizes.
        #   Portals will be important so that, if there's per-portal chrome, it can be resized.
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

    def _req_hotkey(
            self,
            _event_id: EventId,
            _target_id: ParticipantId,
            event_obj: HotkeyEventTriggeredEvent
    ) -> None:
        if event_obj.data.action == HOTKEY_ACTION_FILL_PORTAL:
            active_portal = self.__ctrl.get_active_portal()
            window_fill = event_obj.data.parameters.get(HOTKEY_SCHEMA_FILL_PORTAL__FILL, None)
            if not isinstance(window_fill, str) or window_fill is not None:
                log(WARN, TileEventHandler, 'Invalid position parameter `{0}` type; must be a string', window_fill)
                return
            favor = parse_position(window_fill)
            if favor is None:
                log(WARN, TileEventHandler, 'Invalid position parameter `{0}` value', window_fill)
                return
            res = active_portal.set_visible_window_position_favor(favor)
            if res:
                window_cid, area = res
                send_request_move_native_window_event(self.__bus, window_cid, area)
            else:
                log(DEBUG, TileEventHandler, 'No active window for request to set the position favor')
            return
        if event_obj.data.action == HOTKEY_ACTION_NAME_PORTAL:
            portal_name = event_obj.data.parameters.get(HOTKEY_SCHEMA_NAME_PORTAL__NAME, None)
            if portal_name is None or not isinstance(portal_name, str):
                log(WARN, TileEventHandler, 'Invalid portal name parameter `{0}` type', portal_name)
                return
            self.__ctrl.set_active_portal_name(portal_name)
            return
        if event_obj.data.action == HOTKEY_ACTION_ADD_PORTAL:
            # TODO update portal state
            new_portal, adjusted = self.__ctrl.add_active_split(
                self.__bus.create_component_id(PORTAL_COMPONENT_CATEGORY)
            )
            self.__adjust_portals(adjusted)
            return
        if event_obj.data.action == HOTKEY_ACTION_REMOVE_PORTAL:
            # FIXME
            raise NotImplementedError()
        if event_obj.data.action == HOTKEY_ACTION_MOVE_WINDOW:
            self._move_window(event_obj.data.parameters)
            return

    def _move_window(self, parameters: PersistType) -> None:
        active_portal = self.__ctrl.get_active_portal()
        active_window = active_portal.get_visible_window_info()
        if not active_window:
            return
        # TODO Send state updates
        if HOTKEY_SCHEMA_MOVE_WINDOW__NAME in parameters:
            name = parameters[HOTKEY_SCHEMA_MOVE_WINDOW__NAME]
            if isinstance(name, str):
                dest = self.__ctrl.get_named_portal(name)
                if dest:
                    active_portal.remove_window(active_window.cid)
                    _index, area = dest.add_window(
                        active_window.cid, active_window.base_area, active_window.position_favor
                    )
                    send_request_move_native_window_event(self.__bus, active_window.cid, area)
                    send_request_focus_native_window_event(self.__bus, active_window.cid, True)
                    return
        if HOTKEY_SCHEMA_MOVE_WINDOW__DIRECTION in parameters:
            direction_raw = parameters[HOTKEY_SCHEMA_MOVE_WINDOW__DIRECTION]
            if isinstance(direction_raw, str):
                # TODO add count and wrap to parameters.
                direction = parse_direction(direction_raw)
                if direction is not None:
                    src_portal, dest_portal, moved_window_cid, moved_windows = self.__ctrl.move_active_window(
                        direction, 1, False
                    )
                    for moved in moved_windows:
                        for window in moved.windows:
                            send_request_move_native_window_event(
                                self.__bus, window.window_cid, window.area
                            )
                    if moved_window_cid:
                        send_request_focus_native_window_event(self.__bus, moved_window_cid, True)
                    # TODO send update to portal state.

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

    # -----------------------------------------------------------------------
    # Internal state management
    def __adjust_portals(self, adjusted: Sequence[AdjustedPortal]) -> None:
        # TODO return the new portal state, or some other means of updating it.
        for portal in adjusted:
            if portal.action == ADJUSTED_PORTAL_ACTION_RESIZED:
                for window in portal.windows:
                    send_request_move_native_window_event(
                        self.__bus, window.window_cid, window.area
                    )

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
    portal, position_str = match_window_to_portal(ctrl, window, matchers)
    position = parse_position(position_str)
    _index, area = portal.add_window(window.component_id, window.bordered_rect.get_area(), position)
    send_request_move_native_window_event(
        bus, window.component_id, area
    )


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


def parse_config_data(bus: EventBus, config: PersistentConfigurationState) -> TileLayoutConfig:
    res, errors = parse_config(config.persistent)
    for err in errors:
        report_error(bus, err)
    return res
