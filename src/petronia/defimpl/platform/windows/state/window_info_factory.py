
"""
Load information on a HWND.
"""

from typing import Sequence, List, Dict, Mapping, Union, Optional
from typing import cast as t_cast
from threading import RLock
import atexit
from ..arch.native_funcs import (
    HWND, RECT, DWORD,
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
from ..arch.error_codes_common import (
    ERROR_ACCESS_DENIED
)


def create_native_window_state(bus: EventBus, hwnd: HWND, hwnd_i: int) -> Optional[NativeWindowState]:
    """
    Creates the top-level window state.  If this returns None, then
    it's because the HWND is not a top-level window, or access was denied
    when reading information about it.
    """

    # Find out if this is a top-level window.
    if WINDOWS_FUNCTIONS.window.get_owning_window:
        t_top = WINDOWS_FUNCTIONS.window.get_owning_window(hwnd)
        if isinstance(t_top, WindowsErrorMessage):
            # generally either hwnd is a top window, or it was an access denied error.
            if t_top.errno == ERROR_ACCESS_DENIED:
                return None
            log(TRACE, create_native_window_state, 'querying HWND {0} for top window returned {1}', hwnd, t_top)
        else:
            # Not a top-level window.
            # Ignore this window.
            log(DEBUG, create_native_window_state, 'ignored HWND {0} because it is a child of {1}', hwnd, t_top)
            return None

    cid = bus.create_component_id('petronia.defimpl.platform.windows/window')
    log(DEBUG, create_native_window_state, 'Window created: HWND {0} -> Component ID {1}', hwnd, cid)
    new_window_info = mk_window_state(hwnd, cid)
    window_info: NativeWindowState
    if isinstance(new_window_info, WindowsErrorMessage):
        log(
            WARN, create_native_window_state,
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
            style={},
            is_visible=True,
            is_active=False,
            is_focused=False
        )
    else:
        window_info = new_window_info
    return window_info


def hwnd_to_int(hwnd: HWND) -> Optional[int]:
    if hwnd is None:
        return None
    if isinstance(hwnd, int):
        return hwnd
    if hwnd.value is None:
        return None
    return hwnd.value


def dword_to_int(dword: DWORD) -> Optional[int]:
    if dword is None:
        return None
    if isinstance(dword, int):
        return dword
    if dword.value is None:
        return None
    return dword.value


def mk_window_state(
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
    is_visible = False
    if WINDOWS_FUNCTIONS.window.is_visible:
        is_visible = WINDOWS_FUNCTIONS.window.is_visible(hwnd)

    style: Mapping[str, Union[str, float, bool]] = {}
    if is_visible and WINDOWS_FUNCTIONS.window.get_style:
        style = WINDOWS_FUNCTIONS.window.get_style(hwnd)

    title = ''
    if WINDOWS_FUNCTIONS.window.get_title:
        title = WINDOWS_FUNCTIONS.window.get_title(hwnd)

    pid_d = DWORD(-1)
    pid = -1
    if WINDOWS_FUNCTIONS.window.get_process_id:
        pid_d = WINDOWS_FUNCTIONS.window.get_process_id(hwnd)
        pid = dword_to_int(pid_d) or 0

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
        res = WINDOWS_FUNCTIONS.process.get_username_domain_for_pid(pid_d)
        if not isinstance(res, WindowsErrorMessage):
            names['user'] = res[0]
            names['domain'] = res[1]
    if pid >= 0 and WINDOWS_FUNCTIONS.process.get_executable_filename:
        p_file = WINDOWS_FUNCTIONS.process.get_executable_filename(pid_d)
        if p_file and isinstance(p_file, str):
            names['exe'] = p_file
        else:
            names['exe'] = '<unknown> {0}'.format(repr(p_file))

    # WINDOWS_FUNCTIONS.shell.get_window_metrics?  Is that something we should also get?

    return NativeWindowState(
        component_id=cid,
        title=title,
        process_id=pid,
        names=names,
        bordered_rect=bordered_rect,
        client_rect=client_rect,
        style=t_cast(Dict[str, Union[str, float, bool]], style),
        is_visible=is_visible is not False,
        is_active=active_window_hwnd == hwnd,
        is_focused=active_window_hwnd == hwnd
    )
