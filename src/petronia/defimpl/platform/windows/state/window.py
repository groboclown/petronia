
"""
Discover GUI windows.

Converts from low-level information to Petronia, platform agnostic level.

Also, handles event requests to windows.
"""

from typing import Sequence, List, Dict, Optional
from typing import cast as t_cast
from threading import RLock
import atexit
from ..arch.native_funcs import (
    HWND, RECT,
    WINDOWS_FUNCTIONS,
)
from .....aid.std import (
    EventBus,
    EventId,
    ListenerId,
    ComponentId,
    ParticipantId,
    TARGET_WILDCARD,
    log, WARN, DEBUG, TRACE, VERBOSE, INFO,
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

    RequestSetNativeWindowStyleEvent,
    as_request_set_native_window_style_listener,

    send_native_window_closed_event,

    send_native_window_created_event,

    send_native_window_flashed_event,

    send_native_window_focused_event,

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
    window_replaced_message,
    window_replacing_message,
)
from .window_info_factory import (
    create_native_window_state,
    mk_window_state,
    hwnd_to_int,
)
from .actions.restore_windows import restore_windows
from .actions.window_style import set_window_style


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

    # A lock is required because the user request events can be in any thread, even though
    # the Windows events can only come in through one thread.
    lock = RLock()
    listeners: List[ListenerId] = []
    reverse_window_ids: Dict[ComponentId, HWND] = {}
    active_windows: Dict[int, NativeWindowState] = {}
    original_state: Dict[int, NativeWindowState] = {}

    # Always, always, always actions windows to their original state at exit.
    atexit.register(restore_windows, reverse_window_ids, original_state)

    def add_window_info(hwnd: HWND, hwnd_i: int) -> Optional[NativeWindowState]:
        window_state = create_native_window_state(bus, hwnd, hwnd_i)
        if not window_state:
            return None

        with lock:
            if hwnd_i in active_windows:
                # The remove was never received.  Trigger that.
                on_window_destroyed(hwnd)
                # Keep the original state, though.
            active_windows[hwnd_i] = window_state
            if hwnd_i not in original_state:
                if window_state.bordered_rect.width != 0 and window_state.bordered_rect.height != 0:
                    log(
                        VERBOSE, add_window_info, "Found new visible top window {0} -> cid {1} {3} ({2})",
                        hwnd_i, window_state.component_id[1], window_state.names.get('exe'), window_state.bordered_rect
                    )
                    original_state[hwnd_i] = window_state
            reverse_window_ids[window_state.component_id] = hwnd
        return window_state

    def on_window_created(hwnd: HWND) -> None:
        hwnd_i = hwnd_to_int(hwnd)
        if hwnd_i is None:
            return
        with lock:
            new_window_info = add_window_info(hwnd, hwnd_i)
            if not new_window_info:
                log(DEBUG, on_window_created, "Ignored window created event for {0}", hwnd)
                return
            reverse_window_ids[new_window_info.component_id] = hwnd

            # Note: Send the creation notice must be done before the
            # state is set.  State setting is a normal priority, while
            # creation is high, so that the creator can then listen for
            # state after receiving the window created event.
            send_native_window_created_event(bus, new_window_info.component_id, new_window_info)
            set_active_windows_state(bus, active_windows.values())

    def on_window_destroyed(hwnd: HWND) -> None:
        hwnd_i = hwnd_to_int(hwnd)
        if hwnd_i is None:
            return
        with lock:
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
            if hwnd_i in original_state:
                del original_state[hwnd_i]

    def on_window_focused(hwnd: HWND) -> None:
        hwnd_i = hwnd_to_int(hwnd)
        if hwnd_i is None:
            return
        with lock:
            if hwnd_i not in active_windows:
                winfo = add_window_info(hwnd, hwnd_i)
                if not winfo:
                    log(DEBUG, on_window_focused, "Ignored window focused event for {0}", hwnd)
                    return
                assert hwnd_i in active_windows
            window_info = active_windows[hwnd_i]
            log(DEBUG, on_window_focused, 'Window focused: {0}', window_info.component_id)
            update_active_window(hwnd_i, active_windows)
            send_native_window_focused_event(bus, window_info.component_id)
            set_active_windows_state(bus, active_windows.values())

    def on_window_moved(hwnd: HWND, _pos: Optional[RECT] = None) -> None:
        hwnd_i = hwnd_to_int(hwnd)
        if hwnd_i is None:
            return
        with lock:
            if hwnd_i not in active_windows:
                winfo = add_window_info(hwnd, hwnd_i)
                if not winfo:
                    log(DEBUG, on_window_moved, "Ignored window moved event for {0}", hwnd)
                    return
                assert hwnd_i in active_windows
            window_info = active_windows[hwnd_i]
            log(DEBUG, on_window_focused, 'Window moved: {0}', window_info.component_id)
            screen_rect: ScreenRect
            new_window_info = mk_window_state(hwnd, window_info.component_id)
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
        hwnd_i = hwnd_to_int(hwnd)
        if hwnd_i is None:
            return
        with lock:
            if hwnd_i not in active_windows:
                winfo = add_window_info(hwnd, hwnd_i)
                if not winfo:
                    log(DEBUG, on_window_flash, "Ignored window flashed event for {0}", hwnd)
                    return
                assert hwnd_i in active_windows
            window_info = active_windows[hwnd_i]
            log(DEBUG, on_window_focused, 'Window flashed: {0}', window_info.component_id)
            send_native_window_flashed_event(bus, window_info.component_id)
            # Nothing to update with window state.

    def on_window_replace(new_window: HWND, old_window: HWND) -> None:
        n_hwnd_i = hwnd_to_int(new_window)
        o_hwnd_i = hwnd_to_int(old_window)
        if n_hwnd_i is None or o_hwnd_i is None:
            return
        with lock:
            if o_hwnd_i not in active_windows:
                if n_hwnd_i not in active_windows:
                    # the old window wasn't marked as active, so act like it's new.
                    on_window_created(new_window)
                    assert n_hwnd_i in active_windows
                    return
                # Already registered the new window, and the old one isn't around,
                # so there's nothing to do.
                return
            if n_hwnd_i in active_windows:
                # Incorrectly marked this as a new window.
                log(
                    WARN, on_window_replace,
                    "Marked {0} as a new window, when it should have been a replacement for {1}",
                    new_window, old_window
                )
                return
            # Else, swap-a-roni
            active = active_windows[o_hwnd_i]
            del active_windows[o_hwnd_i]
            active_windows[n_hwnd_i] = active
            reverse_window_ids[active.component_id] = new_window
            if o_hwnd_i in original_state:
                o_state = original_state[o_hwnd_i]
                del original_state[o_hwnd_i]
                original_state[n_hwnd_i] = o_state
            else:
                # Weird state... shouldn't happen, but...
                log(
                    WARN, on_window_replace,
                    "Unexpected state: old window {0} known, was replaced with {1}, but the old window does "
                    "not have an original state",
                    old_window, new_window
                )
                original_state[n_hwnd_i] = active

    def on_request_move(
            _event_id: EventId, target_id: ParticipantId,
            event: RequestMoveNativeWindowEvent
    ) -> None:
        with lock:
            log(WARN, on_request_move, 'Picked up a request to move a window.')
            if target_id in reverse_window_ids and WINDOWS_FUNCTIONS.window.move_resize:
                # For target to be in the list, it must be of the right type.
                hwnd = reverse_window_ids[t_cast(ComponentId, target_id)]
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
                # TODO does this need to explicitly trigger a state change, or does the
                #   corresponding event get triggered?

    def on_request_close(
            _event_id: EventId, target_id: ParticipantId,
            _event: RequestCloseNativeWindowEvent
    ) -> None:
        with lock:
            if target_id in reverse_window_ids and WINDOWS_FUNCTIONS.window.close:
                # For target to be in the list, it must be of the right type.
                hwnd = reverse_window_ids[t_cast(ComponentId, target_id)]
                res = WINDOWS_FUNCTIONS.window.close(hwnd)
                if isinstance(res, WindowsErrorMessage):
                    log(
                        WARN, on_request_close,
                        'Failed to close window {0} ({1}): {2}',
                        target_id, hwnd, res
                    )
                # TODO does this need to explicitly trigger a state change, or does the
                #   corresponding event get triggered?

    def on_request_focus(
            _event_id: EventId, target_id: ParticipantId,
            _event: RequestFocusNativeWindowEvent
    ) -> None:
        log(WARN, on_request_move, 'Picked up a request to focus a window.')
        with lock:
            if target_id in reverse_window_ids and WINDOWS_FUNCTIONS.window.activate:
                hwnd = reverse_window_ids[t_cast(ComponentId, target_id)]
                res = WINDOWS_FUNCTIONS.window.activate(hwnd)
                if isinstance(res, WindowsErrorMessage):
                    log(
                        WARN, on_request_close,
                        'Failed to focus window {0} ({1}): {2}',
                        target_id, hwnd, res
                    )
                # if event.raise_to_top:
                #     WINDOWS_FUNCTIONS.window. ...
                #     which call to make?
                # TODO does this need to explicitly trigger a state change, or does the
                #   corresponding event get triggered?

    def on_request_style(
            _event_id: EventId, target_id: ParticipantId,
            event: RequestSetNativeWindowStyleEvent
    ) -> None:
        with lock:
            if target_id in reverse_window_ids:
                hwnd = reverse_window_ids[target_id]  # type: ignore
                set_window_style(hwnd, event.style)
                # TODO does this need to explicitly trigger a state change, or does the
                #   corresponding event get triggered?

    hooks.add_message_handler(window_created_message(on_window_created))
    hooks.add_message_handler(window_destroyed_message(on_window_destroyed))
    hooks.add_message_handler(window_activated_message(on_window_focused))
    hooks.add_message_handler(window_rude_activated_message(on_window_focused))
    hooks.add_message_handler(window_minimized_message(on_window_moved))
    hooks.add_message_handler(window_monitor_changed_message(on_window_moved))
    hooks.add_message_handler(window_flash_message(on_window_flash))
    hooks.add_message_handler(window_replacing_message(on_window_replace))
    hooks.add_message_handler(window_replaced_message(on_window_replace))

    listeners.extend((
        bus.add_listener(TARGET_WILDCARD, as_request_move_native_window_listener, on_request_move),
        bus.add_listener(TARGET_WILDCARD, as_request_focus_native_window_listener, on_request_focus),
        bus.add_listener(TARGET_WILDCARD, as_request_close_native_window_listener, on_request_close),
        bus.add_listener(TARGET_WILDCARD, as_request_set_native_window_style_listener, on_request_style),
    ))

    # Set the initial state.
    if WINDOWS_FUNCTIONS.window.find_handles:
        for g_hwnd in WINDOWS_FUNCTIONS.window.find_handles():
            # This calls EnumWindows under the covers, which is supposed to return
            # just the top-level windows.  However, it reports many top-level
            # windows for programs that have just a single displayed window.
            # Need to understand what's going on better.
            g_hwnd_i = hwnd_to_int(g_hwnd)
            if g_hwnd_i is not None:
                add_window_info(g_hwnd, g_hwnd_i)
    set_active_windows_state(bus, active_windows.values())
    log(
        TRACE, bootstrap_window_discovery, 'Initial window state: {0}', active_windows.values()
    )

    return listeners


def update_active_window(active_hwnd: int, active_windows: Dict[int, NativeWindowState]) -> None:
    for key, val in active_windows.items():
        active_windows[key] = NativeWindowState(
            component_id=val.component_id,
            title=val.title,
            process_id=val.process_id,
            names=val.names,
            bordered_rect=val.bordered_rect,
            client_rect=val.client_rect,
            style=val.style,
            is_visible=val.is_visible,
            is_active=key == active_hwnd,
            is_focused=key == active_hwnd
        )
