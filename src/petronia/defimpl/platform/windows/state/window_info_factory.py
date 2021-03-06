
"""
Load information on a HWND.
"""

from typing import Dict, Mapping, Tuple, Union, Optional
from typing import cast as t_cast
from ..arch.error_codes_common import (
    ERROR_ACCESS_DENIED
)
from ..arch.native_funcs import (
    HWND, DWORD,
    WINDOWS_FUNCTIONS,
)
from ..connect import (
    WindowsErrorMessage,
)
from .....aid.std import (
    EventBus,
    ComponentId,
    log, WARN, DEBUG, TRACE, VERBOSE, )
from .....core.platform.api.defs import (
    ScreenRect, EMPTY_SCREEN_RECT,
)
from .....core.platform.api.window import (
    NativeWindowState,
)


_CURRENT_PROCESS: Optional[Tuple[DWORD, str, str]] = None


def create_native_window_state(bus: EventBus, hwnd: HWND, _hwnd_i: int) -> Optional[NativeWindowState]:
    """
    Creates the top-level window state.  If this returns None, then
    it's because the HWND is not a top-level window, or access was denied
    when reading information about it.
    """

    if hwnd == 0 or hwnd is None:
        # Special handle for the desktop that we won't be able to investigate.
        log(VERBOSE, create_native_window_state, 'Cannot find information on window HWND 0')
        return None

    global _CURRENT_PROCESS
    if (
            _CURRENT_PROCESS is None and
            WINDOWS_FUNCTIONS.process.get_current_pid and
            WINDOWS_FUNCTIONS.process.get_current_username_domain
    ):
        current_pid = WINDOWS_FUNCTIONS.process.get_current_pid()
        raw_current_username_domain = WINDOWS_FUNCTIONS.process.get_current_username_domain()
        if isinstance(raw_current_username_domain, WindowsErrorMessage):
            current_username_domain = ('', '')
        else:
            current_username_domain = raw_current_username_domain
        _CURRENT_PROCESS = (current_pid, *current_username_domain)

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
        return None
    else:
        window_info = new_window_info

    # Extra filters ...

    if not window_info.is_visible:
        log(
            DEBUG, create_native_window_state,
            'Skipping non-GUI window {0}: {1}',
            hwnd, window_info
        )
        return None

    if _CURRENT_PROCESS and _CURRENT_PROCESS[0] == window_info.process_id:
        # Do not load window states for the current window.  Those are handled elsewhere.
        return None
    if (
            _CURRENT_PROCESS and
            (window_info.get_name('user') != _CURRENT_PROCESS[1] or
            window_info.get_name('domain') != _CURRENT_PROCESS[2])
    ):
        log(
            DEBUG, create_native_window_state,
            "ignoring window with pid {0}, class {1} from other user {2}@{3} (current user is {4}@{5}",
            window_info.process_id, window_info.get_name('class'),
            window_info.get_name('user'), window_info.get_name('domain'),
            _CURRENT_PROCESS[1], _CURRENT_PROCESS[2]
        )
        if window_info.get_name('class') == 'PuTTY':
            log(
                WARN, create_native_window_state,
                "PUTTY ignoring window; detected {0}\\{1}, have {2}\\{3}",
                window_info.get_name('domain'),
                window_info.get_name('user'),
                _CURRENT_PROCESS[2], _CURRENT_PROCESS[1]
            )
        return None

    # Maybe add this later?
    # if class_name is None or class_name.startswith(PETRONIA_CREATED_WINDOW__CLASS_PREFIX):
    #     self._log_debug("Ignoring self-managed window with class {0}".format(class_name))
    #     return None

    log(
        DEBUG, create_native_window_state,
        "Found window {0}", window_info
    )
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
