
"""
General Windows hook event handler.

Implementations will need to work with the WindowHandleMapper class.
"""

from typing import Dict, Optional, Callable
from typing import cast as t_cast
import threading

from ..arch.native_funcs.windows_common import WindowsErrorMessage
from ..arch import windows_constants
from ..arch.native_funcs import (
    WINDOWS_FUNCTIONS,
    SHELL__CANCEL_CALLBACK_CHAIN,
    HWND, HHOOK, UINT, WPARAM, LPARAM,
    MessageCallback,
)
from .messages import MessageEntry

_Hook = Callable[[], UINT]


class WindowsHookEvent:
    """
    Connects to the important windows shell events,
    and directs those to callback functions.
    """

    __slots__ = (
        '_key_hook', '_shell_hook',
        '_hwnd', '__start_state',
        '_window_message_map', '_key_handler',
        '_shell_message_map',
        '_shell_handler',
    )
    _hwnd: Optional[HWND]
    _key_hook: Optional[HHOOK]
    _shell_hook: Optional[HHOOK]
    _window_message_map: Dict[int, MessageCallback]
    _shell_message_map: Dict[int, MessageCallback]
    _key_handler: Optional[Callable[[int, bool, bool], bool]]

    def __init__(self) -> None:
        self._key_hook = None
        self._shell_hook = None
        self._hwnd = None
        self.__start_state = 0
        self._window_message_map = {}
        self._shell_message_map = {}
        self._key_handler = None

    def set_key_handler(self, callback: Callable[[int, bool, bool], bool]) -> None:
        """
        Sets the key handler.
        :param callback: arguments: (VK_CODE, is_key_up, is_key_injected)
        :return: None
        """
        self._key_handler = callback

    def add_message_handler(self, message: MessageEntry) -> None:
        if message[0]:
            # It's a shell message
            self._shell_message_map[message[1]] = message[2]
        else:
            self._window_message_map[message[1]] = message[2]

    def start(self, on_exit: Callable[[], None]) -> None:
        def key_handler(vk_code: int, _scan_code: int, is_key_up: bool, is_injected: bool) -> Optional[str]:
            print("[key] xxx {1}".format(vk_code, 'up' if is_key_up else 'dn'))
            if self._key_handler:
                if self._key_handler(vk_code, is_key_up, is_injected):
                    return SHELL__CANCEL_CALLBACK_CHAIN
            return None

        def shell_handler(source_hwnd: HWND, message: int, wparam: WPARAM, lparam: LPARAM) -> bool:
            print("[shell] {1}".format(source_hwnd, message))
            if message in self._window_message_map:
                return self._window_message_map[message](source_hwnd, message, wparam, lparam)
            return True

        def shell_hook_handler(message: int, wparam: WPARAM, lparam: LPARAM) -> Optional[str]:
            print("[hshell] {0} {1}".format(message, wparam))
            if message in self._shell_message_map:
                if self._shell_message_map[message](
                        self._hwnd or windows_constants.HWND_TOP,
                        message,
                        wparam, lparam
                ):
                    return SHELL__CANCEL_CALLBACK_CHAIN
            return None

        def message_pumper() -> None:
            print("In the message pumper")
            assert self.__start_state == 0
            self.__start_state = 1

            # These MUST be in the same thread!
            if WINDOWS_FUNCTIONS.shell.keyboard_hook:
                hook = WINDOWS_FUNCTIONS.shell.keyboard_hook(key_handler)
                if isinstance(hook, WindowsErrorMessage):
                    print("Failed to register key handler: " + repr(hook))
                else:
                    self._key_hook = hook
                    print("Registered keyboard hook " + repr(self._key_hook))
            if WINDOWS_FUNCTIONS.shell.shell_hook:
                hook = WINDOWS_FUNCTIONS.shell.shell_hook(shell_hook_handler)
                if isinstance(hook, WindowsErrorMessage):
                    print("Failed to register shell handler: " + repr(hook))
                else:
                    self._shell_hook = hook
                    print("Registered shell hook " + repr(self._shell_hook))

            if (
                    WINDOWS_FUNCTIONS.shell.create_global_message_handler and
                    WINDOWS_FUNCTIONS.window.create_message_window and
                    WINDOWS_FUNCTIONS.shell.register_window_hook and
                    WINDOWS_FUNCTIONS.shell.pump_messages
            ):
                message_callback_handler = WINDOWS_FUNCTIONS.shell.create_global_message_handler(
                    self._window_message_map
                )
                hwnd = WINDOWS_FUNCTIONS.window.create_message_window(
                    "PyWinShell Hooks", message_callback_handler
                )
                if isinstance(hwnd, WindowsErrorMessage):
                    # TODO better logging
                    print("Error creating message window: " + repr(hwnd))
                    return
                self._hwnd = hwnd
                if self._hwnd:
                    print("Registering window hook " + repr(self._hwnd))
                    msg = WINDOWS_FUNCTIONS.shell.register_window_hook(
                        self._hwnd, self._window_message_map, shell_handler
                    )
                    if isinstance(msg, WindowsErrorMessage):
                        print("Failed to register window hook: " + repr(msg))
                    else:
                        print("Register window hook message id: " + repr(msg))

                print("Pumping messages...")
                WINDOWS_FUNCTIONS.shell.pump_messages(on_exit)
            else:
                print("Basic functions not defined")

            print("Stopping the message pumper")
            self.__start_state = 2

        print("Starting the message pumper")
        pump_thread = threading.Thread(
            target=message_pumper,
            daemon=True
        )
        pump_thread.start()

    def dispose(self) -> None:
        if self.__start_state == 1 and WINDOWS_FUNCTIONS.window.send_message and self._hwnd:
            WINDOWS_FUNCTIONS.window.send_message(
                self._hwnd, UINT(windows_constants.WM_QUIT), t_cast(WPARAM, 0), t_cast(LPARAM, 0)
            )
        if self._key_hook and WINDOWS_FUNCTIONS.shell.unhook:
            WINDOWS_FUNCTIONS.shell.unhook(self._key_hook)
            self._key_hook = None
        if self._shell_hook and WINDOWS_FUNCTIONS.shell.unhook:
            WINDOWS_FUNCTIONS.shell.unhook(self._shell_hook)
            self._shell_hook = None
