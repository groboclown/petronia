"""Handle message loop and Petronia event interactions."""

from typing import Mapping, Dict, List, Optional, Any, Hashable
import concurrent.futures
from petronia_common.util import (
    StdRet, EMPTY_MAPPING, RET_OK_NONE, join_none_results, join_results, not_none,
)
from petronia_native.common import user_messages
from petronia_native.common.handlers import window
from petronia_native.common.events.impl import window as window_events
from .arch.native_funcs import HWND, RECT, WINDOWS_FUNCTIONS, WPARAM, LPARAM, DWORD
from . import hook_messages, message_loop, message_queue


class WindowsNativeWindow(window.ActiveWindow[HWND]):
    """An active window with Windows data."""
    __slots__ = ()

    def __init__(
            self,
            window_id: str,
            hwnd: HWND,
            state: window_events.WindowState,
    ) -> None:
        window.ActiveWindow.__init__(self, window_id, hwnd, str(hwnd), state)


_CLOSE_WINDOW = 0
_MINIMIZE_WINDOW = 1
_MAXIMIZE_WINDOW = 2
_RESTORE_WINDOW = 3
_SET_POSITION = 4
_SET_STYLE = 5
_SET_GLOBAL = 6
_UPDATE_OS = 7

GLOBAL_SETTING__METRICS_BORDER_WIDTH = 'border-width'
GLOBAL_SETTING__METRICS_PADDED_BORDER_WIDTH = 'padded-border-width'
GLOBAL_SETTING__METRICS_SCROLL_WIDTH = 'scroll-width'
GLOBAL_SETTING__METRICS_SCROLL_HEIGHT = 'scroll-height'
GLOBAL_SETTING__METRICS_CAPTION_WIDTH = 'caption-width'
GLOBAL_SETTING__METRICS_CAPTION_HEIGHT = 'caption-height'
GLOBAL_SETTING__METRICS_CAPTION_FONT = 'caption-font'
GLOBAL_SETTING__METRICS_SMALL_CAPTION_WIDTH = 'small-caption-width'
GLOBAL_SETTING__METRICS_SMALL_CAPTION_HEIGHT = 'small-caption-height'
GLOBAL_SETTING__METRICS_SMALL_CAPTION_FONT = 'small-caption-font'
GLOBAL_SETTING__METRICS_MENU_WIDTH = 'menu-width'
GLOBAL_SETTING__METRICS_MENU_HEIGHT = 'menu-height'
GLOBAL_SETTING__METRICS_MENU_FONT = 'menu-font'
GLOBAL_SETTING__METRICS_STATUS_FONT = 'status-font'
GLOBAL_SETTING__METRICS_MESSAGE_FONT = 'message-font'

DEFAULT_GLOBAL_SETTINGS: Mapping[str, str] = {}
GLOBAL_SETTINGS_DESCRIPTIONS: Mapping[str, str] = {
    GLOBAL_SETTING__METRICS_BORDER_WIDTH: 'The thickness of the sizing border, in pixels.',
    GLOBAL_SETTING__METRICS_PADDED_BORDER_WIDTH: 'The thickness of the padded border, in pixels.',

    # These aren't supported right now.
    # GLOBAL_SETTING__METRICS_SCROLL_WIDTH:
    #     'The width of a standard vertical scroll bar, in pixels.',
    # GLOBAL_SETTING__METRICS_SCROLL_HEIGHT:
    #     'The height of a standard horizontal scroll bar, in pixels.',
    # GLOBAL_SETTING__METRICS_CAPTION_WIDTH: 'The width of caption buttons, in pixels.',
    # GLOBAL_SETTING__METRICS_CAPTION_HEIGHT: 'The height of caption buttons, in pixels.',
    # GLOBAL_SETTING__METRICS_CAPTION_FONT: 'Font description for the caption text.',
    # GLOBAL_SETTING__METRICS_SMALL_CAPTION_WIDTH: 'The width of small caption buttons, in pixels.',
    # GLOBAL_SETTING__METRICS_SMALL_CAPTION_HEIGHT:
    #     'The height of small caption buttons, in pixels.',
    # GLOBAL_SETTING__METRICS_SMALL_CAPTION_FONT: 'Font description for the small caption text.',
    # GLOBAL_SETTING__METRICS_MENU_WIDTH: 'The width of menu-bar buttons, in pixels.',
    # GLOBAL_SETTING__METRICS_MENU_HEIGHT: 'The height of a menu bar, in pixels.',
    # GLOBAL_SETTING__METRICS_MENU_FONT: 'Font description for the menu bar text.',
    # GLOBAL_SETTING__METRICS_STATUS_FONT:
    #     'Font description for text used in status bars and tooltip text.',
    # GLOBAL_SETTING__METRICS_MESSAGE_FONT: 'Font description for message box text',
}

# Standard Styles:  See https://docs.microsoft.com/en-us/windows/win32/winmsg/window-styles
WINDOW_META__STYLE_BORDER = 'has-border'
WINDOW_META__STYLE_TITLE = 'has-title'
WINDOW_META__STYLE_HSCROLL = 'has-hscroll'
WINDOW_META__STYLE_MAX_BUTTON = 'has-maximize-button'
WINDOW_META__STYLE_MIN_BUTTON = 'has-minimize-button'
WINDOW_META__STYLE_SIZE_BORDER = 'has-size-border'
WINDOW_META__STYLE_SYSMENU = 'has-sysmenu'
WINDOW_META__STYLE_VSCROLL = 'has-vscroll'
WINDOW_META__STYLE_FORCE_TASKBAR = 'force-on-taskbar'

WINDOW_META_STYLES: Mapping[str, str] = {
    # See windows_constants WS_STYLE_BIT_MAP and WS_EX_STYLE_BIT_MAP
    WINDOW_META__STYLE_BORDER: 'border',
    WINDOW_META__STYLE_TITLE: 'dialog-frame',
    WINDOW_META__STYLE_HSCROLL: 'hscroll',
    WINDOW_META__STYLE_MAX_BUTTON: 'maximize-button',
    WINDOW_META__STYLE_MIN_BUTTON: 'minimize-button',
    WINDOW_META__STYLE_SIZE_BORDER: 'size-border',
    WINDOW_META__STYLE_SYSMENU: 'sysmenu-button',
    WINDOW_META__STYLE_VSCROLL: 'vscroll',
    WINDOW_META__STYLE_FORCE_TASKBAR: 'app-window',
}

WINDOW_META__PROGRAM = 'executable'
WINDOW_META__PID = 'pid'
WINDOW_META__WINDOW_CLASS_NAME = 'class'
WINDOW_META__WINDOW_MODULE_FILENAME = 'module-filename'
WINDOW_META__WINDOW_TITLE = 'title'
WINDOW_META__OWNER = 'owner'

WINDOW_META_DESCRIPTIONS: Mapping[str, str] = {
    WINDOW_META__STYLE_BORDER: 'The window has a thin-line border.',
    WINDOW_META__STYLE_SIZE_BORDER:
        'The window has a thick border that can be used for resizing the window with the mouse',
    WINDOW_META__STYLE_TITLE:
        f'The window is a dialog frame.  Include {WINDOW_META__STYLE_BORDER} to make it a'
        f'normal window with a title bar.',
    WINDOW_META__STYLE_MIN_BUTTON:
        f'The window has a minimize button.  Include both {WINDOW_META__STYLE_BORDER} and '
        f'{WINDOW_META__STYLE_TITLE} to make it show up.  It cannot be used if the window has '
        f'the context-help style is also set, which is not settable.',
    WINDOW_META__STYLE_MAX_BUTTON:
        f'The window has a maximize and restore button.  Include both {WINDOW_META__STYLE_BORDER} '
        f'and {WINDOW_META__STYLE_TITLE} to make it show up.  It cannot be used if window has '
        f'the context-help style is also set, which is not settable.',
    WINDOW_META__STYLE_SYSMENU:
        f'The window has a sysmenu button.  Include both {WINDOW_META__STYLE_BORDER} and '
        f'{WINDOW_META__STYLE_TITLE} to make it show up.',
    WINDOW_META__STYLE_HSCROLL: 'The window has a horizontal scroll bar.',
    WINDOW_META__STYLE_VSCROLL: 'The window has a vertical scroll bar.',
    WINDOW_META__STYLE_FORCE_TASKBAR:
        'When the window is visible, it is always shown in the taskbar.',
    WINDOW_META__PROGRAM: 'Program that launched the window.',
    WINDOW_META__PID: 'Process ID for the owning program.',
    WINDOW_META__WINDOW_CLASS_NAME: 'Underlying class name for the window.',
    WINDOW_META__WINDOW_TITLE: 'Display title for the window.',
    WINDOW_META__OWNER: 'The user and domain that the process runs under.',
}

CUSTOM_MESSAGE_ID__WINDOW_HANDLES = 12


class WindowsNativeHandler(window.AbstractWindowHandler[WindowsNativeWindow, HWND]):
    """Windows native handler for Petronia events."""

    __slots__ = ('__executor', '__queue', '__loop')

    def __init__(self, executor: Optional[concurrent.futures.ThreadPoolExecutor] = None) -> None:
        window.AbstractWindowHandler.__init__(
            self,
            DEFAULT_GLOBAL_SETTINGS, GLOBAL_SETTINGS_DESCRIPTIONS, WINDOW_META_DESCRIPTIONS,
        )
        self.__executor = executor or concurrent.futures.ThreadPoolExecutor(1)
        self.__queue: Optional[message_queue.UserMessageQueue] = None
        self.__loop: Optional[message_loop.WindowsMessageLoop] = None

    def hash_native_id(self, native_id: HWND) -> Hashable:
        return str(native_id.value)

    def close(self) -> None:
        window.AbstractWindowHandler.close(self)
        self.__queue = None
        self.__loop = None
        self.__executor.shutdown()

    def register_messages(self, loop: message_loop.WindowsMessageLoop) -> None:
        """Register this handler with the loop."""

        # Queue allows for injecting messages into the message loop for interacting
        # with Windows API.  These should spend minimal time in the message loop.
        self.__queue = message_queue.UserMessageQueue(loop, CUSTOM_MESSAGE_ID__WINDOW_HANDLES)
        self.__queue.add_handler(_CLOSE_WINDOW, WindowsNativeHandler._queue_close_window)
        self.__queue.add_handler(_MINIMIZE_WINDOW, WindowsNativeHandler._queue_minimize_window)
        self.__queue.add_handler(_MAXIMIZE_WINDOW, WindowsNativeHandler._queue_maximize_window)
        self.__queue.add_handler(_RESTORE_WINDOW, WindowsNativeHandler._queue_restore_window)
        self.__queue.add_handler(_SET_POSITION, self._queue_set_position_window)
        self.__queue.add_handler(_SET_STYLE, WindowsNativeHandler._queue_set_window_style)
        self.__queue.add_handler(_SET_GLOBAL, self._queue_set_global_style)
        self.__queue.add_handler(_UPDATE_OS, self._queue_load_os_settings)

        loop.add_message_handler(
            hook_messages.window_minimized_message(self.on_window_minimized_message)
        )
        loop.add_message_handler(
            hook_messages.window_created_message(self.on_window_created_message)
        )
        loop.add_message_handler(
            hook_messages.window_destroyed_message(self.on_window_destroyed_message)
        )
        loop.add_message_handler(
            hook_messages.shell_window_focused_message(self.on_shell_window_focused_message)
        )
        loop.add_message_handler(
            hook_messages.window_activated_message(self.on_window_activated_message)
        )
        loop.add_message_handler(
            hook_messages.window_rude_activated_message(self.on_window_activated_message)
        )
        loop.add_message_handler(
            hook_messages.forced_exit_message(self.on_forced_exit_message)
        )
        loop.add_message_handler(
            hook_messages.window_flash_message(self.on_window_flash_message)
        )
        loop.add_message_handler(
            hook_messages.window_replacing_message(self.on_window_replace_message)
        )
        loop.add_message_handler(
            hook_messages.window_replaced_message(self.on_window_replace_message)
        )

    def initialize_system_state(self) -> StdRet[None]:
        """Setup the internal and datastore storage to reflect the current Windows OS state.
        This will trigger the loading inside the message loop."""
        if not self.__loop:
            return RET_OK_NONE
        return join_none_results(
            self.__loop.send_custom_message_to_self(
                CUSTOM_MESSAGE_ID__WINDOW_HANDLES,
                WPARAM(0), LPARAM(0),
            )
        )

    def on_window_minimized_message(self, hwnd: HWND, size: RECT) -> None:
        """Handle the window_minimized_message loop message"""
        wnd = self.get_window_by_native(hwnd)
        if wnd:
            wnd.state.minimized = True
            wnd.state.location.x = size.left.value
            wnd.state.location.y = size.top.value
            wnd.state.location.width = size.right.value - size.left.value
            wnd.state.location.height = size.bottom.value - size.top.value
            self.__executor.submit(self._in_exec_update_window_state, wnd)
        # else log?

    def on_window_created_message(self, hwnd: HWND) -> None:
        """Handle the window_created_message loop message"""
        wnd = self.get_window_by_native(hwnd)
        if wnd:
            # log?  This window is already registered.
            return
        wnd = self._mk_window_state(hwnd)
        # This is inside the message loop, so we can investigate the data.
        user_messages.report_send_receive_problems(update_window_state(hwnd, wnd.state))
        self.__executor.submit(self._in_exec_create_window_state, wnd)

        # If we want to keep track of the window position and other aspects to the changes
        # in this newly created window, then this should call SetWinEventHook to attach
        # this message loop to the PID of the window's process.

    def on_window_destroyed_message(self, hwnd: HWND) -> None:
        """Handle the window_destroyed_message loop message"""
        self.__executor.submit(self._in_exec_destroy_window_state, hwnd, 'closed')

        # If the SetWinEventHook was called, then it needs to be unhooked here if this
        # is the last window for the PID.

    def on_shell_window_focused_message(self, hwnd: HWND) -> None:
        """Handle the shell_window_focused_message loop message"""
        # FIXME the parent class needs better focus management.
        # Specifically, marking the old window as not having focus.

    def on_window_activated_message(self, hwnd: HWND) -> None:
        """Handle the window_activated_message and window_rude_activated_message loop message"""
        # The title can change too?
        # FIXME what needs to be updated on this window?

    def on_forced_exit_message(self, hwnd: HWND) -> None:
        """Handle the forced_exit_message loop message"""
        self.__executor.submit(self._in_exec_destroy_window_state, hwnd, 'forced')

        # If the SetWinEventHook was called, then it needs to be unhooked here if this
        # is the last window for the PID.

    def on_window_flash_message(self, hwnd: HWND) -> None:
        """Handle the window_flash_message loop message"""
        self.__executor.submit(self._in_exec_window_flashed, hwnd)

    def on_window_replace_message(self, new_hwnd: HWND, old_hwnd: HWND) -> None:
        """Handle the window_replacing_message and window_replaced_message loop messages."""
        old_window = self.get_window_by_native(old_hwnd)
        if old_window:
            new_window = WindowsNativeWindow(old_window.window_id, new_hwnd, old_window.state)
            self.replace_native_id(old_window, new_window)

    def on_set_window_position_request(  # pylint:disable=arguments-differ
            self, wnd: WindowsNativeWindow, new_location: window_events.ScreenDimension,
    ) -> StdRet[None]:
        if self.__queue:
            return self.__queue.queue_message(
                _SET_POSITION, (wnd, new_location),
            )
        return RET_OK_NONE

    def on_close_window_request(  # pylint:disable=arguments-differ
            self, wnd: WindowsNativeWindow,
    ) -> StdRet[None]:
        if self.__queue:
            return self.__queue.queue_message(
                _CLOSE_WINDOW, wnd,
            )
        return RET_OK_NONE

    def on_minimize_window_request(  # pylint:disable=arguments-differ
            self, wnd: WindowsNativeWindow,
    ) -> StdRet[None]:
        if self.__queue:
            return self.__queue.queue_message(
                _MINIMIZE_WINDOW, wnd,
            )
        return RET_OK_NONE

    def on_maximize_window_request(  # pylint:disable=arguments-differ
            self, wnd: WindowsNativeWindow,
    ) -> StdRet[None]:
        if self.__queue:
            return self.__queue.queue_message(
                _MAXIMIZE_WINDOW, wnd,
            )
        return RET_OK_NONE

    def on_restore_window_request(  # pylint:disable=arguments-differ
            self, wnd: WindowsNativeWindow,
    ) -> StdRet[None]:
        if self.__queue:
            return self.__queue.queue_message(
                _RESTORE_WINDOW, wnd,
            )
        return RET_OK_NONE

    def on_set_window_settings(  # pylint:disable=arguments-differ
            self, wnd: WindowsNativeWindow, settings: Mapping[str, str],
    ) -> StdRet[None]:
        if self.__queue:
            return self.__queue.queue_message(
                _SET_STYLE, (wnd, settings),
            )
        return RET_OK_NONE

    def on_set_global_settings(self, settings: Mapping[str, str]) -> StdRet[None]:
        # Pass this signal on to the message queue.
        if self.__queue:
            return self.__queue.queue_message(_SET_GLOBAL, settings)
        return RET_OK_NONE

    @staticmethod
    def _queue_close_window(arg: Any) -> None:
        """Send the close window signal to a window.  Run from within the message loop."""
        # This is an internal function, so the assertions are just for debugging / developer
        # aid.
        if WINDOWS_FUNCTIONS.window.close:
            assert isinstance(arg, WindowsNativeWindow)  # nosec

            # This call will just ask another window to close itself.  If it actually closes, then
            # that will be triggered as a separate message that this handler can respond to.
            user_messages.report_send_receive_problems(
                WINDOWS_FUNCTIONS.window.close(arg.native_id)  # pylint:disable=not-callable
            )

    @staticmethod
    def _queue_minimize_window(arg: Any) -> None:
        """Send the minimize window signal to a window.  Run from within the message loop."""
        # This is an internal function, so the assertions are just for debugging / developer
        # aid.
        if WINDOWS_FUNCTIONS.window.minimize:
            assert isinstance(arg, WindowsNativeWindow)  # nosec
            user_messages.report_send_receive_problems(
                WINDOWS_FUNCTIONS.window.minimize(arg.native_id)  # pylint:disable=not-callable
            )

    @staticmethod
    def _queue_maximize_window(arg: Any) -> None:
        """Send the maximize window signal to a window.  Run from within the message loop."""
        # This is an internal function, so the assertions are just for debugging / developer
        # aid.
        if WINDOWS_FUNCTIONS.window.maximize:
            assert isinstance(arg, WindowsNativeWindow)  # nosec
            user_messages.report_send_receive_problems(
                WINDOWS_FUNCTIONS.window.maximize(arg.native_id)  # pylint:disable=not-callable
            )

    @staticmethod
    def _queue_restore_window(arg: Any) -> None:
        """Send the restore window signal to a window.  Run from within the message loop."""
        # This is an internal function, so the assertions are just for debugging / developer
        # aid.
        if WINDOWS_FUNCTIONS.window.restore:
            assert isinstance(arg, WindowsNativeWindow)  # nosec
            user_messages.report_send_receive_problems(
                WINDOWS_FUNCTIONS.window.restore(arg.native_id)  # pylint:disable=not-callable
            )

    @staticmethod
    def _queue_set_position_window(arg: Any) -> None:
        """Send the move/resize signal to a window.  Run from within the message loop."""
        # This is an internal function, so the assertions are just for debugging / developer
        # aid.
        if WINDOWS_FUNCTIONS.window.move_resize:
            assert isinstance(arg, tuple)  # nosec
            wnd, new_location = arg
            assert isinstance(wnd, WindowsNativeWindow)  # nosec
            assert isinstance(new_location, window_events.ScreenDimension)  # nosec

            success = WINDOWS_FUNCTIONS.window.move_resize(  # pylint:disable=not-callable
                wnd.native_id,
                new_location.x, new_location.y, new_location.width, new_location.height,
                True,
            )
            if success:
                # TODO change the position state in the datastore.
                # I don't think this will trigger another Windows message that would then
                # perform this operation.
                pass

    @staticmethod
    def _queue_set_window_style(arg: Any) -> None:
        """Perform style window setting.  Run from within the message loop."""
        # This is an internal function, so the assertions are just for debugging / developer
        # aid.
        if WINDOWS_FUNCTIONS.window.set_style:
            assert isinstance(arg, tuple)  # nosec
            wnd, settings = arg
            assert isinstance(wnd, WindowsNativeWindow)  # nosec
            assert isinstance(settings, dict)  # nosec
            style: Dict[str, bool] = {}
            for key, val in settings.items():
                bool_val = _parse_bool(val)
                if bool_val is not None and key in WINDOW_META_STYLES:
                    style[WINDOW_META_STYLES[key]] = bool_val

            res = WINDOWS_FUNCTIONS.window.set_style(wnd.native_id, style)  # pylint:disable=not-callable
            if res.ok:
                # TODO: change the settings in the datastore
                pass

    def _queue_set_global_style(self, arg: Any) -> None:
        """Perform global style setting.  Run from within the message loop."""
        # This is an internal function, so the assertions are just for debugging / developer
        # aid.
        if WINDOWS_FUNCTIONS.shell.set_border_size:
            assert isinstance(arg, dict)  # nosec
            border_width = _get_int(GLOBAL_SETTING__METRICS_BORDER_WIDTH, arg, -1)
            padded_border_width = _get_int(GLOBAL_SETTING__METRICS_BORDER_WIDTH, arg, 4)
            if border_width >= 0:
                user_messages.report_send_receive_problems(
                    WINDOWS_FUNCTIONS.shell.set_border_size(  # pylint:disable=not-callable
                        border_width, padded_border_width,
                    )
                )
            new_settings_res = WindowsNativeHandler._load_global_settings()
            user_messages.report_send_receive_problems(new_settings_res)
            if new_settings_res.ok:
                self.__executor.submit(
                    self._in_exec_update_global_settings,
                    new_settings_res.result,
                )

    def _queue_load_os_settings(self, _arg: Any) -> None:
        """Load up the OS settings."""
        global_settings_res = self._load_global_settings()
        if global_settings_res.has_error:
            user_messages.report_send_receive_problems(global_settings_res)
        else:
            self.__executor.submit(
                self._in_exec_update_global_settings, global_settings_res.result,
            )
        window_states_res = self._load_window_states()
        if window_states_res.has_error:
            user_messages.report_send_receive_problems(window_states_res)
        else:
            for window_state in window_states_res.result:
                self.__executor.submit(self.update_window_state, window_state)

    def _in_exec_update_global_settings(self, settings: Mapping[str, str]) -> None:
        user_messages.report_send_receive_problems(
            self.update_global_settings(settings)
        )

    def _in_exec_update_window_states(self, window_states: List[WindowsNativeWindow]) -> None:
        for window_state in window_states:
            if self.get_window_by_id(window_state.window_id):
                user_messages.report_send_receive_problems(
                    self.update_window_state(window_state)
                )
            else:
                user_messages.report_send_receive_problems(
                    self.window_created(window_state)
                )

    def _in_exec_update_window_state(self, window_state: WindowsNativeWindow) -> None:
        user_messages.report_send_receive_problems(
            self.update_window_state(window_state)
        )

    def _in_exec_create_window_state(self, window_state: WindowsNativeWindow) -> None:
        user_messages.report_send_receive_problems(
            self.window_created(window_state)
        )

    def _in_exec_destroy_window_state(self, hwnd: HWND, reason: str) -> None:
        user_messages.report_send_receive_problems(
            self.window_destroyed(hwnd, reason)
        )

    def _in_exec_window_flashed(self, hwnd: HWND) -> None:
        user_messages.report_send_receive_problems(
            self.window_flashing(hwnd)
        )

    @staticmethod
    def _load_global_settings() -> StdRet[Mapping[str, str]]:
        """Read all the global OS settings, and update the state.
        This should be run from the windows message loop."""
        if WINDOWS_FUNCTIONS.shell.get_window_metrics:
            metrics = WINDOWS_FUNCTIONS.shell.get_window_metrics()  # pylint:disable=not-callable
            if metrics.has_error:
                return metrics.forward()
            return StdRet.pass_ok({
                GLOBAL_SETTING__METRICS_BORDER_WIDTH:
                    str(metrics.result.border_width),
                GLOBAL_SETTING__METRICS_PADDED_BORDER_WIDTH:
                    str(metrics.result.padded_border_width),
                GLOBAL_SETTING__METRICS_SCROLL_WIDTH:
                    str(metrics.result.scroll_width),
                GLOBAL_SETTING__METRICS_SCROLL_HEIGHT:
                    str(metrics.result.scroll_height),
                GLOBAL_SETTING__METRICS_CAPTION_WIDTH:
                    str(metrics.result.caption_width),
                GLOBAL_SETTING__METRICS_CAPTION_HEIGHT:
                    str(metrics.result.caption_height),

                # TODO font metrics struct to string
                GLOBAL_SETTING__METRICS_CAPTION_FONT: '',

                GLOBAL_SETTING__METRICS_SMALL_CAPTION_WIDTH:
                    str(metrics.result.sm_caption_width),
                GLOBAL_SETTING__METRICS_SMALL_CAPTION_HEIGHT:
                    str(metrics.result.sm_caption_height),

                # TODO font metrics struct to string
                # GLOBAL_SETTING__METRICS_SMALL_CAPTION_FONT: '',

                GLOBAL_SETTING__METRICS_MENU_WIDTH:
                    str(metrics.result.menu_width),
                GLOBAL_SETTING__METRICS_MENU_HEIGHT:
                    str(metrics.result.menu_height),

                # TODO font metrics struct to string
                # GLOBAL_SETTING__METRICS_MENU_FONT: '',

                # TODO font metrics struct to string
                # GLOBAL_SETTING__METRICS_STATUS_FONT: '',

                # TODO font metrics struct to string
                # GLOBAL_SETTING__METRICS_MESSAGE_FONT: '',
            })
        return StdRet.pass_ok(EMPTY_MAPPING)

    def _load_window_states(self) -> StdRet[List[WindowsNativeWindow]]:
        """Read in all the OS Windows and their states.  Should be done in the message loop."""
        active_windows: Dict[HWND, WindowsNativeWindow] = {
            wnd.native_id: wnd
            for wnd in self.get_active_windows()
        }
        res: List[StdRet[None]] = []

        focused_hwnd: Optional[HWND] = None
        if WINDOWS_FUNCTIONS.window.get_active_window:
            focused_hwnd = WINDOWS_FUNCTIONS.window.get_active_window()  # pylint:disable=not-callable
        if WINDOWS_FUNCTIONS.window.find_handles:
            handles = WINDOWS_FUNCTIONS.window.find_handles()  # pylint:disable=not-callable
            for handle in handles:
                wnd = active_windows.get(handle)
                if not wnd:
                    wnd = self._mk_window_state(handle)
                    active_windows[handle] = wnd
                if focused_hwnd == handle:
                    wnd.state.focus = 0
                    wnd.state.active = True
                res.append(update_window_state(wnd.native_id, wnd.state))
        return join_results(
            lambda x: list(active_windows.values()),
            *res
        )

    def _mk_window_state(self, hwnd: HWND) -> WindowsNativeWindow:
        return WindowsNativeWindow(
            self.create_next_window_id(),
            hwnd,
            window_events.WindowState(
                False, -1, None,
                window_events.ScreenDimension(0, 0, 0, 0),
                False, [],
            ),
        )


def _parse_bool(val: str) -> Optional[bool]:
    val = val.strip().lower()
    if val in (
            'true', 'yes', 'ok', 'enable', 'enabled', 'active', 'activate', 'activated', 'on', '1',
    ):
        return True
    if val in (
            'false', 'no', 'disable', 'disabled', 'deactivate', 'deactivated', 'off', '0',
    ):
        return False
    return None


def _get_int(key: str, struct: Mapping[str, str], default: int) -> int:
    if key in struct:
        try:
            return int(struct[key])
        except ValueError:
            pass
    return default


def update_window_state(  # pylint:disable=too-many-branches
        hwnd: HWND, state: window_events.WindowState,
) -> StdRet[None]:
    """Load the window state data.  Should be called from the Windows message loop."""
    res: List[StdRet[None]] = []
    meta: Dict[str, str] = {
        m.key: m.value
        for m in state.meta
    }
    if WINDOWS_FUNCTIONS.window.border_rectangle:
        rect_res = WINDOWS_FUNCTIONS.window.border_rectangle(  # pylint:disable=not-callable
            hwnd,
        )
        res.append(rect_res.forward())
        if rect_res.ok:
            state.location.x = rect_res.result.x
            state.location.y = rect_res.result.y
            state.location.width = rect_res.result.width
            state.location.height = rect_res.result.height
    if WINDOWS_FUNCTIONS.window.get_style:
        style = WINDOWS_FUNCTIONS.window.get_style(  # pylint:disable=not-callable
            hwnd,
        )
        meta.update({
            key: 'true' if style.get(WINDOW_META_STYLES[key], False) else 'false'
            for key in WINDOW_META_STYLES  # keys()
        })
    pid: DWORD = DWORD(0)
    if WINDOWS_FUNCTIONS.window.get_process_id:
        pid = WINDOWS_FUNCTIONS.window.get_process_id(  # pylint:disable=not-callable
            hwnd,
        )
        meta[WINDOW_META__PID] = str(pid)
    if WINDOWS_FUNCTIONS.window.get_class_name:
        name_res = WINDOWS_FUNCTIONS.window.get_class_name(  # pylint:disable=not-callable
            hwnd,
        )
        if name_res.ok:
            meta[WINDOW_META__WINDOW_CLASS_NAME] = name_res.result
        else:
            res.append(name_res.forward())
    if WINDOWS_FUNCTIONS.window.get_module_filename:
        name_res = WINDOWS_FUNCTIONS.window.get_module_filename(  # pylint:disable=not-callable
            hwnd,
        )
        if name_res.ok:
            meta[WINDOW_META__WINDOW_MODULE_FILENAME] = name_res.result
        else:
            res.append(name_res.forward())
    if WINDOWS_FUNCTIONS.window.get_title:
        meta[WINDOW_META__WINDOW_TITLE] = WINDOWS_FUNCTIONS.window.get_title(  # pylint:disable=not-callable
            hwnd,
        )
    if WINDOWS_FUNCTIONS.process.get_username_domain_for_pid and pid != 0:
        user_domain_res = WINDOWS_FUNCTIONS.process.get_username_domain_for_pid(  # pylint:disable=not-callable
            pid,
        )
        if user_domain_res.ok:
            meta[WINDOW_META__OWNER] = f'{user_domain_res.result[0]}/{user_domain_res.result[1]}'
        else:
            res.append(user_domain_res.forward())  # pylint:disable=not-callable
    if WINDOWS_FUNCTIONS.process.get_executable_filename and pid != 0:
        exec_fn_res = WINDOWS_FUNCTIONS.process.get_executable_filename(pid)  # pylint:disable=not-callable
        if exec_fn_res.ok and exec_fn_res.value:
            meta[WINDOW_META__PROGRAM] = not_none(exec_fn_res.value)
        else:
            res.append(exec_fn_res.forward())

    return join_none_results(*res)