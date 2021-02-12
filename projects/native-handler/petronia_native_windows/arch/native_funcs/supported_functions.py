
"""
All supported windows functions, mapped to Python types.
"""

from typing import Callable, Sequence, Iterable, Tuple, Dict, Union, Optional
from petronia_common.util import T
from petronia_native.common.defs.units import OsScreenSize
from petronia_native.common.defs import (
    OsScreenRect,
    Color,
)
from .windows_common import (
    HWND, DWORD, c_int,
    UINT, WPARAM, LPARAM,
    HDC, HFONT, HHOOK, ANIMATIONINFO,
    MessageCallback, NativeMessageCallback,
    WindowsErrorMessage,
)
from .window_state import WindowsWindowState
from .window_metrics import WindowMetrics
from .process_metrics import ProcessMetrics
from .monitor import WindowsMonitor

PaintCallback = Callable[[HWND, HDC], T]


class WindowFunctions:  # pylint:disable=too-many-instance-attributes
    """
    Simple mapping of functions.
    These can all be replaced.
    """

    __slots__ = (
        'find_handles',
        'enum_window_handles',
        'find_handle_for_class_title',
        'find_handle_for_child_class_title',
        'get_title',
        'is_visible',
        'get_process_id',
        'get_class_name',
        'get_module_filename',
        'get_thread_window_handles',
        'get_child_window_handles',
        'get_owning_window',
        'border_rectangle',
        'client_rectangle',
        'move_resize',
        'redraw',
        'repaint',
        'wait_gui_thread_idle',
        'send_message',
        'post_message',
        'close',
        'maximize',
        'minimize',
        'restore',
        'get_visibility_states',
        'draw_border_outline',
        'set_position',
        'set_layered_attributes',
        'get_active_window',
        'activate',
        'create_message_window',
        'create_display_window',
        'get_font_for_description',
        'get_text_size',
        'do_paint',
        'do_draw',
        'set_style',
        'has_style',
        'get_style',
        'create_borderless_window',
    )
    find_handles: Optional[Callable[[], Sequence[HWND]]]
    enum_window_handles: Optional[Callable[[Callable[[HWND], bool]], None]]
    find_handle_for_class_title: Optional[Callable[[str, str], Optional[HWND]]]
    find_handle_for_child_class_title: Optional[
        Callable[[HWND, Optional[HWND], str, str], Optional[HWND]]
    ]
    get_title: Optional[Callable[[HWND], str]]
    is_visible: Optional[Callable[[HWND], bool]]
    get_process_id: Optional[Callable[[HWND], DWORD]]
    get_class_name: Optional[Callable[[HWND], Union[WindowsErrorMessage, str]]]
    get_module_filename: Optional[Callable[[HWND], Union[WindowsErrorMessage, str]]]
    get_thread_window_handles: Optional[Callable[[DWORD], Sequence[HWND]]]
    get_child_window_handles: Optional[Callable[[HWND], Sequence[HWND]]]
    get_owning_window: Optional[Callable[[HWND], Union[WindowsErrorMessage, HWND]]]
    border_rectangle: Optional[Callable[[HWND], Union[WindowsErrorMessage, OsScreenRect]]]
    client_rectangle: Optional[Callable[[HWND], Union[WindowsErrorMessage, OsScreenRect]]]
    move_resize: Optional[Callable[[HWND, int, int, int, int, Optional[bool]], bool]]
    redraw: Optional[Callable[[HWND, Optional[bool]], bool]]
    repaint: Optional[Callable[[HWND], Optional[WindowsErrorMessage]]]
    wait_gui_thread_idle: Optional[Callable[[HWND, Optional[int]], Optional[WindowsErrorMessage]]]
    send_message: Optional[
        Callable[[HWND, UINT, WPARAM, LPARAM], Union[WindowsErrorMessage, LPARAM]]
    ]
    post_message: Optional[Callable[[HWND, UINT, WPARAM, LPARAM], Optional[WindowsErrorMessage]]]
    close: Optional[Callable[[HWND], Optional[WindowsErrorMessage]]]
    maximize: Optional[Callable[[HWND], Optional[WindowsErrorMessage]]]
    minimize: Optional[Callable[[HWND], Optional[WindowsErrorMessage]]]
    restore: Optional[Callable[[HWND], Optional[WindowsErrorMessage]]]
    get_visibility_states: Optional[Callable[[HWND], Sequence[str]]]
    draw_border_outline: Optional[Callable[
        [OsScreenRect, Color, int, Optional[int], Optional[int], Optional[HWND]],
        None
    ]]
    set_position: Optional[Callable[
        [HWND, Union[HWND, str], OsScreenRect, Iterable[str]],
        Optional[WindowsErrorMessage]
    ]]
    set_layered_attributes: Optional[Callable[[HWND, Color], Optional[WindowsErrorMessage]]]
    get_active_window: Optional[Callable[[], Optional[HWND]]]
    activate: Optional[Callable[[HWND], Optional[WindowsErrorMessage]]]
    create_message_window: Optional[
        Callable[[str, NativeMessageCallback], Union[HWND, WindowsErrorMessage]]
    ]
    create_display_window: Optional[Callable[
        [str, str, MessageCallback, Iterable[str]],
        Union[HWND, WindowsErrorMessage]
    ]]
    get_font_for_description: Optional[
        Callable[[str, Optional[HWND], Optional[HDC]], Optional[HFONT]]
    ]
    get_text_size: Optional[Callable[
        [HFONT, str, Optional[HWND], Optional[HDC]],
        Union[OsScreenSize, WindowsErrorMessage],
    ]]
    do_paint: Optional[Callable[[HWND, PaintCallback[T]], Union[T, WindowsErrorMessage]]]
    do_draw: Optional[Callable[[HWND, PaintCallback[T]], Union[T, WindowsErrorMessage]]]
    set_style: Optional[
        Callable[[HWND, Dict[str, bool]], Union[WindowsErrorMessage, Dict[str, bool]]]
    ]
    has_style: Optional[Callable[[HWND, str], bool]]
    get_style: Optional[Callable[[HWND], Dict[str, bool]]]
    create_borderless_window: Optional[Callable[
        [str, str, MessageCallback, Dict[int, MessageCallback], Optional[bool], Optional[bool]],
        Union[HWND, WindowsErrorMessage]
    ]]

    def __init__(self) -> None:
        self.find_handles = None
        self.enum_window_handles = None
        self.find_handle_for_class_title = None
        self.find_handle_for_child_class_title = None
        self.get_title = None
        self.is_visible = None
        self.get_process_id = None
        self.get_class_name = None
        self.get_module_filename = None
        self.get_thread_window_handles = None
        self.get_child_window_handles = None
        self.border_rectangle = None
        self.client_rectangle = None
        self.move_resize = None
        self.redraw = None
        self.repaint = None
        self.wait_gui_thread_idle = None
        self.send_message = None
        self.post_message = None
        self.close = None
        self.maximize = None
        self.minimize = None
        self.restore = None
        self.get_visibility_states = None
        self.draw_border_outline = None
        self.set_position = None
        self.set_layered_attributes = None
        self.get_active_window = None
        self.activate = None
        self.create_message_window = None
        self.create_display_window = None
        self.get_font_for_description = None
        self.get_text_size = None
        self.do_paint = None
        self.do_draw = None
        self.set_style = None
        self.has_style = None
        self.get_style = None
        self.create_borderless_window = None


class PaintFunctions:
    """
    Simple mapping of functions.
    These can all be replaced.
    """

    __slots__ = (
        'draw_rect',
        'draw_text',
        'draw_outline_text',
    )
    draw_rect: Optional[Callable[[HDC, OsScreenRect, Color], Optional[WindowsErrorMessage]]]
    draw_text: Optional[Callable[
        [HDC, HFONT, str, int, int, int, int, Optional[Color], Optional[Color]],
        Optional[WindowsErrorMessage],
    ]]
    draw_outline_text: Optional[Callable[
        [HDC, HFONT, str, int, int, int, Color, Color, Optional[Color]],
        Optional[WindowsErrorMessage],
    ]]

    def __init__(self) -> None:
        self.draw_rect = None
        self.draw_text = None
        self.draw_outline_text = None


class ShellFunctions:  # pylint:disable=too-many-instance-attributes
    """
    Simple mapping of functions.
    These can all be replaced.
    """

    __slots__ = (
        'get_task_bar_window_handles',
        'is_key_pressed',
        'keyboard_hook',
        'shell_hook',
        'unhook',
        'register_window_hook',
        'create_global_message_handler',
        'inject_scancode',
        'lock_workstation',
        'pump_messages',
        'system_parameters_info',
        'open_start_menu',
        'find_notification_icons',
        'get_window_metrics',
        'set_window_metrics',
        'set_border_size',
    )
    get_task_bar_window_handles: Optional[Callable[[], Sequence[HWND]]]
    is_key_pressed: Optional[Callable[[c_int], bool]]
    keyboard_hook: Optional[Callable[
        [Callable[[int, int, bool, bool], Optional[str]]],
        Union[HHOOK, WindowsErrorMessage]
    ]]
    shell_hook: Optional[Callable[
        [Callable[[int, WPARAM, LPARAM], Optional[str]]], Union[HHOOK, WindowsErrorMessage],
    ]]
    unhook: Optional[Callable[[HHOOK], None]]
    inject_scancode: Optional[Callable[[int, bool], bool]]
    lock_workstation: Optional[Callable[[], bool]]
    register_window_hook: Optional[Callable[
        [HWND, Optional[Dict[int, MessageCallback]], Optional[MessageCallback]],
        Union[int, WindowsErrorMessage],
    ]]
    create_global_message_handler: Optional[
        Callable[[Dict[int, MessageCallback]], NativeMessageCallback]
    ]
    pump_messages: Optional[Callable[[Callable[[], None]], None]]
    system_parameters_info: Optional[Callable[
        [Dict[str, Union[int, bool, ANIMATIONINFO]]],
        Optional[Dict[str, Union[int, bool, ANIMATIONINFO, WindowsErrorMessage]]],
    ]]
    open_start_menu: Optional[Callable[[bool], Optional[WindowsErrorMessage]]]
    find_notification_icons: Optional[Callable[[], Sequence[HWND]]]
    get_window_metrics: Optional[Callable[[], Union[WindowMetrics, WindowsErrorMessage]]]
    set_window_metrics: Optional[Callable[[WindowMetrics], Optional[WindowsErrorMessage]]]
    set_border_size: Optional[Callable[[int, int], Optional[WindowsErrorMessage]]]

    def __init__(self) -> None:
        self.get_task_bar_window_handles = None
        self.is_key_pressed = None
        self.keyboard_hook = None
        self.shell_hook = None
        self.register_window_hook = None
        self.create_global_message_handler = None
        self.unhook = None
        self.inject_scancode = None
        self.lock_workstation = None
        self.pump_messages = None
        self.system_parameters_info = None
        self.open_start_menu = None
        self.find_notification_icons = None
        self.get_window_metrics = None
        self.set_window_metrics = None
        self.set_border_size = None


class MonitorFunctions:
    """
    Simple mapping of functions.
    These can all be replaced.
    """

    __slots__ = (
        'find_monitors',
        'set_native_dpi_awareness'
    )
    find_monitors: Optional[Callable[[], Sequence[WindowsMonitor]]]
    set_native_dpi_awareness: Optional[Callable[[], Optional[WindowsErrorMessage]]]

    def __init__(self) -> None:
        self.find_monitors = None
        self.set_native_dpi_awareness = None


class ProcessFunctions:  # pylint:disable=too-many-instance-attributes
    """
    Simple mapping of functions.
    These can all be replaced.
    """

    __slots__ = (
        'get_exit_code',
        'get_window_state',
        'get_current_pid',
        'get_username_domain_for_pid',
        'get_current_username_domain',
        'get_executable_filename',
        'get_all_pids',
        'load_all_process_details',
        'get_all_service_information',
    )
    get_exit_code: Optional[Callable[[DWORD], Optional[int]]]
    get_window_state: Optional[Callable[[DWORD], Union[WindowsWindowState, WindowsErrorMessage]]]
    get_current_pid: Optional[Callable[[], DWORD]]
    get_username_domain_for_pid: Optional[
        Callable[[DWORD], Union[Tuple[str, str], WindowsErrorMessage]]
    ]
    get_current_username_domain: Optional[
        Callable[[], Union[Tuple[str, str], WindowsErrorMessage]]
    ]
    get_executable_filename: Optional[Callable[[DWORD], Union[WindowsErrorMessage, str, None]]]
    get_all_pids: Optional[Callable[[], Union[WindowsErrorMessage, Sequence[DWORD]]]]
    load_all_process_details: Optional[Callable[[], Sequence[Dict[str, str]]]]
    get_all_service_information: Optional[
        Callable[[], Union[WindowsErrorMessage, Sequence[ProcessMetrics]]]
    ]

    def __init__(self) -> None:
        self.get_exit_code = None
        self.get_window_state = None
        self.get_current_pid = None
        self.get_username_domain_for_pid = None
        self.get_current_username_domain = None
        self.get_executable_filename = None
        self.get_all_pids = None
        self.load_all_process_details = None
        self.get_all_service_information = None


class Functions:
    """
    Simple mapping of functions.
    These can all be replaced.
    """

    __slots__ = (
        '__window',
        '__paint',
        '__shell',
        '__monitor',
        '__process',
    )

    def __init__(self) -> None:
        self.__window = WindowFunctions()
        self.__paint = PaintFunctions()
        self.__shell = ShellFunctions()
        self.__monitor = MonitorFunctions()
        self.__process = ProcessFunctions()

    @property
    def window(self) -> WindowFunctions:
        """Get the window related functions"""
        return self.__window

    @property
    def paint(self) -> PaintFunctions:
        """Get the painting related functions"""
        return self.__paint

    @property
    def shell(self) -> ShellFunctions:
        """Get the Windows Shell related functions"""
        return self.__shell

    @property
    def monitor(self) -> MonitorFunctions:
        """Get the monitor related functions"""
        return self.__monitor

    @property
    def process(self) -> ProcessFunctions:
        """Get the process related functions."""
        return self.__process
