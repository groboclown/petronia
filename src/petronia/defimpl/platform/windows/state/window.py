
"""
Discover GUI windows.

Converts from low-level information to Petronia, platform agnostic level.

Also, handles event requests to windows.
"""

from typing import Sequence, List, Dict, Optional
from ..arch.native_funcs import (
    HWND, RECT,
    WINDOWS_FUNCTIONS,
)
from ..arch.native_funcs.window_state import convert_rect
from .....aid.simp import (
    EventBus,
    EventId,
    ListenerId,
    ComponentId,
    ParticipantId,
    TARGET_WILDCARD,
    log, WARN, DEBUG, VERBOSE,
)
from .....core.platform.api.defs import (
    ScreenRect,
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
)
from ..connect import (
    WindowsHookEvent,
    WindowsErrorMessage,
    get_monitors,
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
    active_window_ids: Dict[int, ComponentId] = {}
    reverse_window_ids: Dict[ComponentId, HWND] = {}

    def on_window_created(hwnd: HWND) -> None:
        hwnd_i = _hwnd_to_int(hwnd)
        if hwnd_i is None:
            return
        if hwnd_i in active_window_ids:
            # The remove was never received.  Trigger that.
            on_window_destroyed(hwnd)
        cid = bus.create_component_id('petronia.defimpl.platform.windows/window')
        log(DEBUG, on_window_created, 'Window created: HWND {0} -> Component ID {1}', hwnd, cid)
        active_window_ids[hwnd_i] = cid
        reverse_window_ids[cid] = hwnd
        send_native_window_created_event(bus, cid)

    def on_window_destroyed(hwnd: HWND) -> None:
        hwnd_i = _hwnd_to_int(hwnd)
        if hwnd_i is None:
            return
        if hwnd_i in active_window_ids:
            cid = active_window_ids[hwnd_i]
            log(DEBUG, on_window_destroyed, 'Window closed: HWND {0} -> Component ID {1}', hwnd, cid)
            del active_window_ids[hwnd_i]
            if cid in reverse_window_ids:
                del reverse_window_ids[cid]
            else:
                log(WARN, on_window_destroyed, 'Component ID for window {0} not known', hwnd)
            # Is there some other way to tell if it's been forced?
            send_native_window_closed_event(bus, cid, False)

    def on_window_focused(hwnd: HWND) -> None:
        hwnd_i = _hwnd_to_int(hwnd)
        if hwnd_i is None:
            return
        if hwnd_i not in active_window_ids:
            on_window_created(hwnd)
            assert hwnd_i in active_window_ids
        cid = active_window_ids[hwnd_i]
        log(DEBUG, on_window_focused, 'Window focused: {0}', cid)
        send_native_window_focused_event(bus, cid)

    def on_window_moved(hwnd: HWND, pos: Optional[RECT] = None) -> None:
        hwnd_i = _hwnd_to_int(hwnd)
        if hwnd_i is None:
            return
        if hwnd_i not in active_window_ids:
            on_window_created(hwnd)
            assert hwnd_i in active_window_ids
        cid = active_window_ids[hwnd_i]
        log(DEBUG, on_window_focused, 'Window moved: {0}', cid)
        screen_rect: ScreenRect
        if not pos:
            if WINDOWS_FUNCTIONS.window.client_rectangle:
                client_rect = WINDOWS_FUNCTIONS.window.client_rectangle(hwnd)
                if isinstance(client_rect, WindowsErrorMessage):
                    log(WARN, on_window_moved, 'Could not find client position for window {0}: {1}', hwnd, client_rect)
                    return
                screen_rect = client_rect
            else:
                log(WARN, on_window_moved, 'Could not find client position for window {0}: not implemented', hwnd)
                return
        else:
            screen_rect = convert_rect(pos)
        is_visible = WINDOWS_FUNCTIONS.window.is_visible(hwnd)
        send_native_window_moved_event(bus, cid, screen_rect, is_visible)

    def on_window_flash(hwnd: HWND) -> None:
        hwnd_i = _hwnd_to_int(hwnd)
        if hwnd_i is None:
            return
        if hwnd_i not in active_window_ids:
            on_window_created(hwnd)
            assert hwnd_i in active_window_ids
        cid = active_window_ids[hwnd_i]
        log(DEBUG, on_window_focused, 'Window flashed: {0}', cid)
        send_native_window_flashed_event(bus, cid)

    def on_request_move(
            target_id: ParticipantId, event_id: EventId,
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
            target_id: ParticipantId, event_id: EventId,
            event: RequestCloseNativeWindowEvent
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
            target_id: ParticipantId, event_id: EventId,
            event: RequestFocusNativeWindowEvent
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
            #     WINDOWS_FUNCTIONS.window.

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
    return listeners


def _hwnd_to_int(hwnd: HWND) -> Optional[int]:
    if hwnd is None:
        return None
    if isinstance(hwnd, int):
        return hwnd
    if hwnd.value is None:
        return None
    return hwnd.value
