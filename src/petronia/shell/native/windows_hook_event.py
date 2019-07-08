
"""
Ties the Windows hooks into the bus events.

This needs to be one of the last events to
"""

from ...system import event_ids
from ...system import target_ids
from ...system.component import Component, Identifiable
from ...arch.funcs import (
    shell__keyboard_hook, shell__shell_hook, shell__pump_messages, shell__unhook,
    shell__create_global_message_handler, shell__register_window_hook,
    shell__open_start_menu, shell__inject_scancode, shell__lock_workstation,
    shell__is_key_pressed,
    window__create_message_window, monitor__find_monitors, window__send_message,
    SHELL__CANCEL_CALLBACK_CHAIN
)
from ...arch import windows_constants
from ...config import Config, DEFAULT_MODE, MODE_CHANGE_COMMAND
from ...util.hotkey_chain import (
    on_key_hook, ACTION_PENDING, IGNORED,
    STR_VK_MAP, SPECIAL_MODIFIER_CHECK_VKEY_CODES
)
import threading

# for the bits of Windows compatiblity that oozed out of funcs
from ctypes import wintypes, Structure, POINTER
from ctypes import cast as c_cast


class WindowsHookEvent(Identifiable, Component):
    def __init__(self, bus, config):
        Component.__init__(self, bus)
        Identifiable.__init__(self, target_ids.WINDOWS_HOOKS)

        assert isinstance(config, Config)

        self.__config = config
        self.__mode = None
        self.__mode_keys = None
        self.__key_combos = None
        self.__key_hook = None
        self.__shell_hook = None
        self.__hwnd = None
        self.__has_quit = False
        self._reload_hotkeys(None, None, None)

        self._listen(event_ids.CONFIG__UPDATE, target_ids.ANY, self._reload_hotkeys)
        self._listen(event_ids.TELL_WINDOWS__INJECT_KEYS, target_ids.ANY, self._on_inject_keys)

        # noinspection PyUnusedLocal
        def key_callback(vk_code, scan_code, is_key_up, is_injected):
            # print("k {0} {1} {2} {3}".format(
            #     hex(vk_code), hex(scan_code), is_key_up and "Up" or "Dn", is_injected and "Injected" or "Natural"))
            return self._modal_hotkey(vk_code, not is_key_up)

        # noinspection PyUnusedLocal
        def shell_callback(hwnd, message, wparam, lparam):
            self._shell_message(hwnd, wparam, lparam)
            return 0

        # noinspection PyUnusedLocal
        def shell_display_change(hwnd, message, wparam, lparam):
            self._on_display_change()
            return 0

        message_id_callbacks = {
            windows_constants.WM_DISPLAYCHANGE: shell_display_change,
        }

        def on_exit_callback():
            self.__has_quit = True
            self._fire(event_ids.SYSTEM__QUIT, target_ids.BROADCAST, {})

        def message_pumper():
            # These MUST be in the same thread!
            self.__key_hook = shell__keyboard_hook(key_callback)

            message_callback_handler = shell__create_global_message_handler(message_id_callbacks)
            self.__hwnd = window__create_message_window("PyWinShell Hooks", message_callback_handler)
            shell__register_window_hook(self.__hwnd, message_id_callbacks, shell_callback)

            shell__pump_messages(on_exit_callback)

            self.__has_quit = True

        pump_thread = threading.Thread(
            target=message_pumper,
            daemon=True
        )
        pump_thread.start()

        # Send an initial message about the current OS state
        self._on_display_change()

    # noinspection PyUnusedLocal
    def _reload_hotkeys(self, event_id, target_id, event_obj):
        # Needs to be as thread-safe as possible.

        mode_chains = {}
        for mode, combos in self.__config.hotkeys.mode_combos.items():
            self._log_verbose("Registered keyboard mode {0}".format(mode))
            mode_chains[mode] = combos

        if self.__mode not in mode_chains:
            self.__mode = DEFAULT_MODE
        self.__key_combos = mode_chains
        self.__mode_keys = mode_chains[self.__mode]

    def _modal_hotkey(self, vk_code, is_down):
        # HAAAACK
        # Due to issues when the user locks the desktop, the windows key
        # release hook can get lost.  Because of that, we need to test if
        # the windows key is up or down, and send that to the hook.
        specials = {}
        for special_code in SPECIAL_MODIFIER_CHECK_VKEY_CODES:
            specials[special_code] = shell__is_key_pressed(special_code)
        
        if on_key_hook(vk_code, is_down, specials):
            res = self.__key_combos[self.__mode].key_action(vk_code, is_down)
            if res == IGNORED:
                return None
            if res != ACTION_PENDING:
                # Mode change actions need to be done here first.
                # So special handling for mode changes.
                self._log_debug("Running command {0}".format(res))
                if res[0] == MODE_CHANGE_COMMAND:
                    new_mode = res[1].strip()
                    if new_mode in self.__key_combos:
                        old_mode = self.__mode
                        self.__mode = new_mode
                        self.__mode_keys = self.__key_combos[new_mode]
                        self.__mode_keys.reset()
                        self._fire(event_ids.MODE__CHANGE_TO, target_ids.ANY, {
                            'old-mode': old_mode,
                            'new-mode': new_mode,
                        })
                    else:
                        self._log_error("CONFIG: unknown mode {0}".format(new_mode))
                else:
                    self._fire(event_ids.USER__COMMAND, target_ids.BROADCAST, {'command': res})

            # Weird things happen if we block win+L and win+U;
            # specifically, the win key is stuck down.
            # Experiments found that if we don't block the key release,
            # then things won't get stuck.
            if not is_down and (vk_code == 0x5B or vk_code == 0x5C):
                self._log_debug("Not blocking a Win key up")
                return None
            self._log_debug("Returning Cancel Key Forward ({0} {1})".format(hex(vk_code), is_down and "Dn" or "Up"))
            return SHELL__CANCEL_CALLBACK_CHAIN

    def _shell_message(self, source_hwnd, action_id, lparam):
        self._log_debug("shell message {0} {1}".format(hex(action_id), hex(lparam)))
        event_id, event_obj = _gen_shell_event(source_hwnd, action_id, lparam)
        if event_id and event_obj:
            self._fire(event_id, target_ids.BROADCAST, event_obj)

    def _on_display_change(self):
        monitors = monitor__find_monitors()
        # Only the top layout receives this event.
        self._fire(event_ids.OS__RESOLUTION_CHANGED, target_ids.TOP_LAYOUT, {
            'monitors': monitors
        })

    # noinspection PyUnusedLocal,PyMethodMayBeStatic
    def _on_inject_keys(self, event_id, target_id, event_obj):
        key_pairs = event_obj['keys']
        for key, is_key_up in key_pairs:
            if key in STR_VK_MAP:
                scan_code = STR_VK_MAP[key]
            elif key.isdigit():
                scan_code = int(key)
            else:
                raise OSError("Unknown scan code `{0}`".format(key))

            is_key_up = event_obj['is-key-up'].strip().lower()
            keyup = is_key_up in ['up', 'true', 'yes', 'off']
            shell__inject_scancode(scan_code, keyup)

    def close(self):
        try:
            if not self.__has_quit:
                window__send_message(self.__hwnd, windows_constants.WM_QUIT, 0, 0)
            if self.__key_hook:
                shell__unhook(self.__key_hook)
                self.__key_hook = None
            if self.__shell_hook:
                shell__unhook(self.__shell_hook)
                self.__shell_hook = None
        finally:
            super().close()


def _gen_shell_event(source_hwnd, action_id, lparam):
    if action_id in _ACTION_ID_HANDLERS:
        event_obj = {
            'source_hwnd': source_hwnd,
            'action-id': action_id,
        }
        _ACTION_ID_HANDLERS[action_id](event_obj, lparam)
        return _ACTION_ID_EVENT_IDS[action_id], event_obj
    return None, None


def _populate_event__window_handle(event_obj, lparam):
    event_obj['target_hwnd'] = lparam


class SHELLHOOKINFO(Structure):
    _fields_ = [
        ("hwnd", wintypes.HWND),
        ("rc", wintypes.RECT),
    ]


def _populate_event__window_minimized(event_obj, lparam):
    info = c_cast(lparam, POINTER(SHELLHOOKINFO))
    event_obj['target_hwnd'] = info.contents.hwnd


# noinspection PyUnusedLocal
def _populate_event__app_command(event_obj, lparam):
    # Don't need the horribly complex parsing of lparam now.
    pass


# noinspection PyUnusedLocal
def _populate_event__noop(event_obj, lparam):
    pass


# Deep windows knowledge crept outside the "arch" directory.
# See https://msdn.microsoft.com/en-us/library/windows/desktop/ms644991(v=vs.85).aspx
# wparam -> lparam meanings
HSHELL_WINDOWCREATED = 1  # -> A handle to the window being created.
HSHELL_WINDOWDESTROYED = 2  # -> A handle to the top-level window being destroyed.
HSHELL_ACTIVATESHELLWINDOW = 3  # -> Not used.  (shell window focused)
HSHELL_WINDOWACTIVATED = 4  # -> A handle to the activated window. (window focused)
HSHELL_GETMINRECT = 5  # -> A pointer to a SHELLHOOKINFO structure. (window minimized)
HSHELL_REDRAW = 6  # -> A handle to the window that needs to be redrawn.
HSHELL_TASKMAN = 7  # -> Can be ignored.
HSHELL_LANGUAGE = 8  # -> ???
HSHELL_SYSMENU = 9  # -> ???
HSHELL_ENDTASK = 10  # -> A handle to the window that should be forced to exit.
HSHELL_ACCESSIBILITYSTATE = 11  # -> ???
HSHELL_WINDOWREPLACED = 13  # A handle to the window being replaced.
HSHELL_WINDOWREPLACING = 14  # -> A handle to the window replacing the top-level window.
HSHELL_MONITORCHANGED = 16  # -> A handle to the window that moved to a different monitor.
HSHELL_HIGHBIT = 0x8000  # used to augment an existing message
HSHELL_RUDEAPPACTIVATED = 0x8004  # -> A handle to the activated window; treat as WINDOWACTIVATED.
HSHELL_FLASH = 0x8006  # -> A handle to the window that needs to be flashed.  One message per flash
HSHELL_APPCOMMAND = 12  # -> The APPCOMMAND which has been unhandled by the application
# or other hooks. See WM_APPCOMMAND and use the GET_APPCOMMAND_LPARAM macro to retrieve this parameter.
# We get shell message "0x35" and "0x36".  Don't know what these are.
HSHELL_UNKNOWN_35 = 0x35
HSHELL_UNKNOWN_36 = 0x36


_ACTION_ID_HANDLERS = {
    HSHELL_WINDOWCREATED: _populate_event__window_handle,
    HSHELL_WINDOWDESTROYED: _populate_event__window_handle,
    HSHELL_ACTIVATESHELLWINDOW: _populate_event__noop,
    HSHELL_WINDOWACTIVATED: _populate_event__window_handle,
    HSHELL_GETMINRECT: _populate_event__window_minimized,
    HSHELL_REDRAW: _populate_event__window_handle,
    HSHELL_TASKMAN: _populate_event__noop,
    HSHELL_LANGUAGE: _populate_event__noop,
    HSHELL_SYSMENU: _populate_event__noop,
    HSHELL_ENDTASK: _populate_event__window_handle,
    # HSHELL_ACCESSIBILITYSTATE: _populate_event__noop,
    HSHELL_WINDOWREPLACED: _populate_event__window_handle,
    HSHELL_WINDOWREPLACING: _populate_event__window_handle,
    HSHELL_MONITORCHANGED: _populate_event__window_handle,
    HSHELL_RUDEAPPACTIVATED: _populate_event__window_handle,
    HSHELL_FLASH: _populate_event__window_handle,
    HSHELL_APPCOMMAND: _populate_event__app_command,
    HSHELL_UNKNOWN_35: _populate_event__noop,
    HSHELL_UNKNOWN_36: _populate_event__noop,
}
_ACTION_ID_EVENT_IDS = {
    HSHELL_WINDOWCREATED: event_ids.OS__WINDOW_CREATED,
    HSHELL_WINDOWDESTROYED: event_ids.OS__WINDOW_DESTROYED,
    HSHELL_ACTIVATESHELLWINDOW: event_ids.OS__SHELL_WINDOW_FOCUSED,
    HSHELL_WINDOWACTIVATED: event_ids.OS__WINDOW_FOCUSED,
    HSHELL_GETMINRECT: event_ids.OS__WINDOW_MINIMIZED,
    HSHELL_REDRAW: event_ids.OS__WINDOW_REDRAW,
    HSHELL_TASKMAN: event_ids.OS__TASK_MANAGER_FOCUSED,
    HSHELL_LANGUAGE: event_ids.OS__LANGUAGE,
    HSHELL_SYSMENU: event_ids.OS__SYS_MENU,
    HSHELL_ENDTASK: event_ids.OS__WINDOW_FORCED_END,
    # HSHELL_ACCESSIBILITYSTATE: event_ids.OS__ACCESSIBILITY_STATE,
    HSHELL_WINDOWREPLACED: event_ids.OS__WINDOW_REPLACED,
    HSHELL_WINDOWREPLACING: event_ids.OS__WINDOW_REPLACING,
    HSHELL_MONITORCHANGED: event_ids.OS__WINDOW_MONITOR_CHANGED,
    HSHELL_RUDEAPPACTIVATED: event_ids.OS__WINDOW_FOCUSED,
    HSHELL_FLASH: event_ids.OS__WINDOW_FLASH,
    HSHELL_APPCOMMAND: event_ids.OS__APP_COMMAND,
    HSHELL_UNKNOWN_35: event_ids.OS__WINDOW_FOCUSED,
    HSHELL_UNKNOWN_36: event_ids.OS__WINDOW_FOCUSED,
}
