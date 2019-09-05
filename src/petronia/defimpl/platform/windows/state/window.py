
"""
Discover GUI windows.

Converts from low-level information to Petronia, platform agnostic level.

Also, handles event requests to windows.
"""

from typing import Sequence, List, Dict, Union, Optional
from ..arch.native_funcs import (
    HWND, RECT, DWORD,
    WINDOWS_FUNCTIONS,
)
from .....aid.simp import (
    EventBus,
    EventId,
    ListenerId,
    ComponentId,
    ParticipantId,
    TARGET_WILDCARD,
    log, WARN, DEBUG, TRACE, VERBOSE, INFO,
)
from .....core.platform.api.defs import (
    ScreenRect, EMPTY_SCREEN_RECT,
    SCREEN_AREA_X, SCREEN_AREA_Y, SCREEN_AREA_W, SCREEN_AREA_H,
)
from .....core.platform.api.window import (
    RequestCloseNativeWindowEvent,
    as_request_close_native_window_listener,

    RequestFocusNativeWindowEvent,
    as_request_focus_native_window_listener,

    RequestMoveNativeWindowEvent,
    as_request_move_native_window_listener,

    send_native_window_closed_event,

    send_native_window_created_event,

    NativeWindowFlashedEvent,
    send_native_window_flashed_event,

    NativeWindowFocusedEvent,
    send_native_window_focused_event,

    NativeWindowMovedEvent,
    send_native_window_moved_event,

    NativeWindowState,
    set_active_windows_state,
)
from ..connect import (
    WindowsHookEvent,
    WindowsErrorMessage,
    from_user_to_native_screen,
)
from ..connect.messages import (
    window_activated_message,
    window_created_message,
    window_destroyed_message,
    window_flash_message,
    window_minimized_message,
    window_monitor_changed_message,
    window_rude_activated_message,
)


def bootstrap_window_discovery(bus: EventBus, hooks: WindowsHookEvent) -> Sequence[ListenerId]:
    """
    Startup the window code.  NOte that this does not need to be aware of
    windows created by the GUI code, because those windows still need to
    be managed.  The GUI window itself will have its own ID, and the
    component will be a different ID.

    :param bus:
    :param hooks:
    :return:
    """

    listeners: List[ListenerId] = []
    reverse_window_ids: Dict[ComponentId, HWND] = {}
    active_windows: Dict[int, NativeWindowState] = {}

    def add_window_info(hwnd: HWND, hwnd_i: int) -> NativeWindowState:
        if hwnd_i in active_windows:
            # The remove was never received.  Trigger that.
            on_window_destroyed(hwnd)
        cid = bus.create_component_id('petronia.defimpl.platform.windows/window')
        log(DEBUG, on_window_created, 'Window created: HWND {0} -> Component ID {1}', hwnd, cid)
        new_window_info = mk_window_info(hwnd, cid)
        window_info: NativeWindowState
        if isinstance(new_window_info, WindowsErrorMessage):
            log(
                INFO, on_window_created,
                'Failed to get information for window {0}: {1}',
                hwnd, new_window_info
            )
            # Need *something* there...
            window_info = NativeWindowState(
                component_id=cid,
                title='',
                process_id=-1,
                names={},
                bordered_rect=EMPTY_SCREEN_RECT,
                client_rect=EMPTY_SCREEN_RECT,
                is_visible=True,
                is_active=False,
                is_focused=False
            )
        else:
            window_info = new_window_info
        active_windows[hwnd_i] = window_info
        return window_info

    def on_window_created(hwnd: HWND) -> None:
        hwnd_i = _hwnd_to_int(hwnd)
        if hwnd_i is None:
            return
        new_window_info = add_window_info(hwnd, hwnd_i)
        reverse_window_ids[new_window_info.component_id] = hwnd
        send_native_window_created_event(bus, new_window_info.component_id)
        set_active_windows_state(bus, active_windows.values())

    def on_window_destroyed(hwnd: HWND) -> None:
        hwnd_i = _hwnd_to_int(hwnd)
        if hwnd_i is None:
            return
        if hwnd_i in active_windows:
            window_info = active_windows[hwnd_i]
            log(
                DEBUG, on_window_destroyed,
                'Window closed: HWND {0} -> Component ID {1}', hwnd, window_info.component_id
            )
            del active_windows[hwnd_i]
            if window_info.component_id in reverse_window_ids:
                del reverse_window_ids[window_info.component_id]
            else:
                log(WARN, on_window_destroyed, 'Component ID for window {0} not known', hwnd)
            # Is there some other way to tell if it's been forced?
            send_native_window_closed_event(bus, window_info.component_id, False)
            set_active_windows_state(bus, active_windows.values())

    def on_window_focused(hwnd: HWND) -> None:
        hwnd_i = _hwnd_to_int(hwnd)
        if hwnd_i is None:
            return
        if hwnd_i not in active_windows:
            on_window_created(hwnd)
            assert hwnd_i in active_windows
        window_info = active_windows[hwnd_i]
        log(DEBUG, on_window_focused, 'Window focused: {0}', window_info.component_id)
        update_active_window(hwnd_i, active_windows)
        send_native_window_focused_event(bus, window_info.component_id)
        set_active_windows_state(bus, active_windows.values())

    def on_window_moved(hwnd: HWND, _pos: Optional[RECT] = None) -> None:
        hwnd_i = _hwnd_to_int(hwnd)
        if hwnd_i is None:
            return
        if hwnd_i not in active_windows:
            on_window_created(hwnd)
            assert hwnd_i in active_windows
        window_info = active_windows[hwnd_i]
        log(DEBUG, on_window_focused, 'Window moved: {0}', window_info.component_id)
        screen_rect: ScreenRect
        new_window_info = mk_window_info(hwnd, window_info.component_id)
        if isinstance(new_window_info, WindowsErrorMessage):
            log(
                INFO, on_request_move,
                'Failed to get information on window {0}: {1}', hwnd, new_window_info
            )
            # Keep the old one...
        else:
            window_info = new_window_info
            active_windows[hwnd_i] = window_info
        send_native_window_moved_event(
            bus, window_info.component_id,
            window_info.bordered_rect, window_info.is_visible
        )
        set_active_windows_state(bus, active_windows.values())

    def on_window_flash(hwnd: HWND) -> None:
        hwnd_i = _hwnd_to_int(hwnd)
        if hwnd_i is None:
            return
        if hwnd_i not in active_windows:
            on_window_created(hwnd)
            assert hwnd_i in active_windows
        window_info = active_windows[hwnd_i]
        log(DEBUG, on_window_focused, 'Window flashed: {0}', window_info.component_id)
        send_native_window_flashed_event(bus, window_info.component_id)
        # Nothing to update with window state.

    def on_request_move(
            target_id: ParticipantId, _event_id: EventId,
            event: RequestMoveNativeWindowEvent
    ) -> None:
        if isinstance(target_id, ComponentId) and target_id in reverse_window_ids:
            hwnd = reverse_window_ids[target_id]
            area = event.area
            x, y = from_user_to_native_screen(area[SCREEN_AREA_X], area[SCREEN_AREA_Y])
            w, h = from_user_to_native_screen(area[SCREEN_AREA_W], area[SCREEN_AREA_H])
            log(
                VERBOSE, on_request_move, 'Moving window {0} -> HWND {1} to {2} -> {3}',
                target_id, hwnd, area, (x, y, w, h,)
            )
            res = WINDOWS_FUNCTIONS.window.move_resize(
                hwnd,
                x, y, w, h,
                True
            )
            if isinstance(res, WindowsErrorMessage):
                log(
                    WARN, on_request_close,
                    'Failed to move window {0} ({1}): {2}',
                    target_id, hwnd, res
                )

    def on_request_close(
            target_id: ParticipantId, _event_id: EventId,
            _event: RequestCloseNativeWindowEvent
    ) -> None:
        if isinstance(target_id, ComponentId) and target_id in reverse_window_ids:
            hwnd = reverse_window_ids[target_id]
            res = WINDOWS_FUNCTIONS.window.close(hwnd)
            if isinstance(res, WindowsErrorMessage):
                log(
                    WARN, on_request_close,
                    'Failed to close window {0} ({1}): {2}',
                    target_id, hwnd, res
                )

    def on_request_focus(
            target_id: ParticipantId, _event_id: EventId,
            _event: RequestFocusNativeWindowEvent
    ) -> None:
        if isinstance(target_id, ComponentId) and target_id in reverse_window_ids:
            hwnd = reverse_window_ids[target_id]
            res = WINDOWS_FUNCTIONS.window.activate(hwnd)
            if isinstance(res, WindowsErrorMessage):
                log(
                    WARN, on_request_close,
                    'Failed to focus window {0} ({1}): {2}',
                    target_id, hwnd, res
                )
            # if event.raise_to_top:
            #     WINDOWS_FUNCTIONS.window. ...

    hooks.add_message_handler(window_created_message(on_window_created))
    hooks.add_message_handler(window_destroyed_message(on_window_destroyed))
    hooks.add_message_handler(window_activated_message(on_window_focused))
    hooks.add_message_handler(window_rude_activated_message(on_window_focused))
    hooks.add_message_handler(window_minimized_message(on_window_moved))
    hooks.add_message_handler(window_monitor_changed_message(on_window_moved))
    hooks.add_message_handler(window_flash_message(on_window_flash))

    listeners.extend((
        bus.add_listener(TARGET_WILDCARD, as_request_move_native_window_listener, on_request_move),
        bus.add_listener(TARGET_WILDCARD, as_request_focus_native_window_listener, on_request_focus),
        bus.add_listener(TARGET_WILDCARD, as_request_close_native_window_listener, on_request_close),
    ))

    # Set the initial state.
    if WINDOWS_FUNCTIONS.window.find_handles:
        for g_hwnd in WINDOWS_FUNCTIONS.window.find_handles():
            g_hwnd_i = _hwnd_to_int(g_hwnd)
            if g_hwnd_i is not None:
                add_window_info(g_hwnd, g_hwnd_i)
    set_active_windows_state(bus, active_windows.values())
    log(
        TRACE, bootstrap_window_discovery, 'Initial window state: {0}', active_windows.values()
    )

    return listeners


def _hwnd_to_int(hwnd: HWND) -> Optional[int]:
    if hwnd is None:
        return None
    if isinstance(hwnd, int):
        return hwnd
    if hwnd.value is None:
        return None
    return hwnd.value


def _dword_to_int(dword: DWORD) -> Optional[int]:
    if dword is None:
        return None
    if isinstance(dword, int):
        return dword
    if dword.value is None:
        return None
    return dword.value


def mk_window_info(
        hwnd: HWND,
        cid: ComponentId
) -> Union[NativeWindowState, WindowsErrorMessage]:
    bordered_rect: ScreenRect
    if WINDOWS_FUNCTIONS.window.border_rectangle:
        rect = WINDOWS_FUNCTIONS.window.border_rectangle(hwnd)
        if isinstance(rect, WindowsErrorMessage):
            return rect
        bordered_rect = rect
    else:
        bordered_rect = EMPTY_SCREEN_RECT
    client_rect: ScreenRect
    if WINDOWS_FUNCTIONS.window.client_rectangle:
        # This returns coordinates where 0,0 is always the top/left value.
        # So it needs to be converted.
        rect = WINDOWS_FUNCTIONS.window.client_rectangle(hwnd)
        if isinstance(rect, WindowsErrorMessage):
            return rect
        client_rect = ScreenRect(
            rect.x + bordered_rect.x, rect.y + bordered_rect.y,
            rect.width, rect.height,
            rect.left + bordered_rect.left, rect.right + bordered_rect.right,
            rect.top + bordered_rect.top, rect.bottom + bordered_rect.bottom
        )
    else:
        client_rect = EMPTY_SCREEN_RECT

    active_window_hwnd: Optional[HWND] = None
    if WINDOWS_FUNCTIONS.window.get_active_window:
        # Can't tell outside the handling thread which window is the proper
        # active, and which has focus.  This can only tell us which is the
        # foreground window.
        active_window_hwnd = WINDOWS_FUNCTIONS.window.get_active_window()
    is_visible = WINDOWS_FUNCTIONS.window.is_visible(hwnd)

    title = ''
    if WINDOWS_FUNCTIONS.window.get_title:
        title = WINDOWS_FUNCTIONS.window.get_title(hwnd)

    pid = -1
    if WINDOWS_FUNCTIONS.window.get_process_id:
        pid = _dword_to_int(WINDOWS_FUNCTIONS.window.get_process_id(hwnd))

    names: Dict[str, str] = {}
    if WINDOWS_FUNCTIONS.window.get_class_name:
        cls_name = WINDOWS_FUNCTIONS.window.get_class_name(hwnd)
        if cls_name and isinstance(cls_name, str):
            names['class'] = cls_name
    if WINDOWS_FUNCTIONS.window.get_module_filename:
        mod_name = WINDOWS_FUNCTIONS.window.get_module_filename(hwnd)
        if mod_name and isinstance(mod_name, str):
            names['module'] = mod_name
    if pid >= 0 and WINDOWS_FUNCTIONS.process.get_username_domain_for_pid:
        res = WINDOWS_FUNCTIONS.process.get_username_domain_for_pid(pid)
        if not isinstance(res, WindowsErrorMessage):
            names['user'] = res[0]
            names['domain'] = res[1]
    if pid >= 0 and WINDOWS_FUNCTIONS.process.get_executable_filename:
        p_file = WINDOWS_FUNCTIONS.process.get_executable_filename(pid)
        if p_file and isinstance(p_file, str):
            names['exe'] = p_file

    # WINDOWS_FUNCTIONS.shell.get_window_metrics?  Is that something we should also get?

    return NativeWindowState(
        component_id=cid,
        title=title,
        process_id=pid,
        names=names,
        bordered_rect=bordered_rect,
        client_rect=client_rect,
        is_visible=is_visible is not False,
        is_active=active_window_hwnd == hwnd,
        is_focused=active_window_hwnd == hwnd
    )


def update_active_window(active_hwnd: int, active_windows: Dict[int, NativeWindowState]) -> None:
    for key, val in active_windows.items():
        active_windows[key] = NativeWindowState(
            component_id=val.component_id,
            title=val.title,
            process_id=val.process_id,
            names=val.names,
            bordered_rect=val.bordered_rect,
            client_rect=val.client_rect,
            is_visible=val.is_visible,
            is_active=key == active_hwnd,
            is_focused=key == active_hwnd
        )
