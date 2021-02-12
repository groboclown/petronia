"""
The application loop for a winapi notification aware program.
"""

from typing import Dict, Tuple, Sequence, Optional, Callable
from typing import cast as t_cast
import threading

from .arch.native_funcs.windows_common import WindowsErrorMessage
from .arch import windows_constants
from .arch.native_funcs import (
    WINDOWS_FUNCTIONS,
    SHELL__CANCEL_CALLBACK_CHAIN,
    HWND, HHOOK, UINT, WPARAM, LPARAM,
    MessageCallback,
)
from .hook_messages import MessageEntry
from ..common import log


_Hook = Callable[[], UINT]


class WindowsHookPumper:
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
        '_message_callback_handler',
    )
    _hwnd: Optional[HWND]
    _key_hook: Optional[HHOOK]
    _shell_hook: Optional[HHOOK]
    _window_message_map: Dict[int, MessageCallback]
    _shell_message_map: Dict[int, MessageCallback]
    _key_handler: Optional[Callable[[int, int, bool, bool], Tuple[bool, Sequence[Tuple[int, bool]]]]]

    def __init__(self) -> None:
        self._key_hook = None
        self._shell_hook = None
        self._hwnd = None
        self.__start_state = 0
        self._window_message_map = {}
        self._shell_message_map = {}
        self._key_handler = None

    def set_key_handler(
            self, callback: Callable[[int, int, bool, bool], Tuple[bool, Sequence[Tuple[int, bool]]]]
    ) -> None:
        """
        Sets the key handler.
        :param callback: arguments: (VK_CODE, scan_code, is_key_up, is_key_injected).
            Returns a tuple of
            (bool - true if cancel propagation of key, false if let it go through,
            list of (scancode, is_key_up) injected keys).
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
        def key_handler(vk_code: int, scan_code: int, is_key_up: bool, is_injected: bool) -> Optional[str]:
            # print("[key] xxx {1}".format(vk_code, 'up' if is_key_up else 'dn', vk_to_names(vk_code)))
            # print("[key] {2} {1}".format(vk_code, 'up' if is_key_up else 'dn', vk_to_names(vk_code)))
            if self._key_handler:
                res = self._key_handler(vk_code, scan_code, is_key_up, is_injected)
                if WINDOWS_FUNCTIONS.shell.inject_scancode and res[1]:
                    for inject_scancode, inject_is_up in res[1]:
                        # print(" - injecting {0} {1}".format(inject_scancode, inject_is_up))
                        WINDOWS_FUNCTIONS.shell.inject_scancode(inject_scancode, inject_is_up)
                if res[0]:
                    # print(" - cancelling callback chain for key")
                    return SHELL__CANCEL_CALLBACK_CHAIN
                # else:
                #     print(" - passing on key")
            return None

        def shell_handler(source_hwnd: HWND, message: int, wparam: WPARAM, lparam: LPARAM) -> bool:
            # Shell window messages use the WPARAM to specify the kind of shell event.
            # See https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-registershellhookwindow
            wparam_msg = t_cast(int, wparam)
            if wparam_msg in self._shell_message_map:
                log.debug(
                    'shell: {source}: {message} ({wparam}: {wparam_msg})',
                    source=source_hwnd,
                    message=message,
                    wparam=wparam,
                    wparam_msg=self._shell_message_map.get(wparam_msg),
                )
                return self._shell_message_map[wparam_msg](source_hwnd, message, wparam, lparam)
            log.debug(
                'shell: 0x{wparam_msg:08x} not handled '
                '({message:08x} / {wparam:08x} / {lparam:08x})',
                wparam_msg=wparam_msg,
                message=message,
                wparam=wparam,
                lparam=lparam,
            )
            return True

        def shell_hook_handler(message: int, wparam: WPARAM, lparam: LPARAM) -> Optional[str]:
            log.debug('shell hook: {message} / {wparam}', message=message, wparam=wparam)
            if message in self._shell_message_map:
                if self._shell_message_map[message](
                        self._hwnd or windows_constants.HWND_TOP,
                        message,
                        wparam, lparam
                ):
                    return SHELL__CANCEL_CALLBACK_CHAIN
            return None

        def message_pumper() -> None:
            # This runs in a background thread.
            # If this doesn't stop during shutdown, then an exception
            # is reported to the console.  This indicates that the quit
            # event message queue either didn't run soon enough, or it
            # was never triggered.

            log.trace('message_pump: In the message pumper')
            assert self.__start_state == 0
            self.__start_state = 1

            # These MUST be in the same thread!
            if WINDOWS_FUNCTIONS.shell.keyboard_hook:
                hook = WINDOWS_FUNCTIONS.shell.keyboard_hook(key_handler)
                if isinstance(hook, WindowsErrorMessage):
                    log.error("message_pump: Failed to register key handler: {hook}", hook=hook)
                else:
                    self._key_hook = hook
                    log.trace("message_pump: Registered keyboard hook {hook}", hook=hook)

            if WINDOWS_FUNCTIONS.shell.shell_hook:
                hook = WINDOWS_FUNCTIONS.shell.shell_hook(shell_hook_handler)
                if isinstance(hook, WindowsErrorMessage):
                    # This is expected until the crazy work-around is implemented.
                    # The crazy work around is to register a DLL to handle this, and have
                    # the DLL be loaded into the shell process.  The DLL also needs both a
                    # x86 and x64 version.
                    # https://stackoverflow.com/questions/61413733/setwindowshookex-method-fails-with-code-1428-dll-injection
                    log.debug(
                        "message_pump: Expected Failure registering shell handler: {hook}",
                        hook=hook,
                    )
                else:
                    self._shell_hook = hook
                    log.error("message_pump: Registered shell hook {hook}", hook=hook)

            if (
                    WINDOWS_FUNCTIONS.shell.create_global_message_handler
                    and WINDOWS_FUNCTIONS.window.create_message_window
                    and WINDOWS_FUNCTIONS.shell.register_window_hook
                    and WINDOWS_FUNCTIONS.shell.pump_messages
            ):
                message_callback_handler = WINDOWS_FUNCTIONS.shell.create_global_message_handler(
                    self._window_message_map,
                )
                hwnd = WINDOWS_FUNCTIONS.window.create_message_window(
                    "PyWinShell Hooks", message_callback_handler,
                )
                if isinstance(hwnd, WindowsErrorMessage):
                    log.error(
                        "message_pump: Error creating message window: {hwnd}; cannot continue.",
                        hwnd=hwnd,
                    )
                    return
                self._hwnd = hwnd
                if self._hwnd:
                    log.trace("message_pump: Registering window hook {hwnd}", hwnd=self._hwnd)
                    msg = WINDOWS_FUNCTIONS.shell.register_window_hook(
                        self._hwnd, self._window_message_map, shell_handler
                    )
                    if isinstance(msg, WindowsErrorMessage):
                        log.error(
                            "message_pump: Failed to register window hook: {msg}; cannot continue",
                            msg=msg,
                        )
                    else:
                        log.trace("message_pump: Register window hook message id: {mesg}", mesg=msg)

                log.debug("message_pump: Pumping messages...")
                WINDOWS_FUNCTIONS.shell.pump_messages(on_exit)
            else:
                log.error("message_pump: Basic platform functions not defined; cannot continue")

            log.info('message_pump: Stopping the Windows message pumper')
            self.__start_state = 2

        log.info("message_pumper: Starting the Windows message pumper thread")
        pump_thread = threading.Thread(
            target=message_pumper,
            daemon=True
        )
        pump_thread.start()

    def dispose(self) -> None:
        if self._hwnd and WINDOWS_FUNCTIONS.window.close:
            WINDOWS_FUNCTIONS.window.close(self._hwnd)
        if self.__start_state == 1 and WINDOWS_FUNCTIONS.window.send_message and self._hwnd:
            log.info('dispose: Sending shutdown to window message consumer.')
            WINDOWS_FUNCTIONS.window.send_message(
                self._hwnd, UINT(windows_constants.WM_QUIT), t_cast(WPARAM, 0), t_cast(LPARAM, 0)
            )
        if self._key_hook and WINDOWS_FUNCTIONS.shell.unhook:
            WINDOWS_FUNCTIONS.shell.unhook(self._key_hook)
            self._key_hook = None
        if self._shell_hook and WINDOWS_FUNCTIONS.shell.unhook:
            WINDOWS_FUNCTIONS.shell.unhook(self._shell_hook)
            self._shell_hook = None
