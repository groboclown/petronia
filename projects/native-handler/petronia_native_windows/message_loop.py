"""
The application loop for a winapi notification aware program.

This is the big, critical section of the code that needs to be highly optimized
and working really right, according to Windows rules, otherwise we end up with
a sluggish computer that acts weird and needs a reboot to clean up.
"""

# pylint is confused by optional fields that are callable.
# pylint:disable=not-callable


from typing import Dict, Tuple, Sequence, Optional, Callable
from typing import cast as t_cast
import threading
import atexit
import traceback
from petronia_common.util import StdRet, RET_OK_NONE
from petronia_common.util import i18n as _
from petronia_native.common import log, user_messages
from .arch import windows_constants
from .arch.native_funcs import (
    WINDOWS_FUNCTIONS,
    SHELL__CANCEL_CALLBACK_CHAIN,
    HWND, HHOOK, UINT, WPARAM, LPARAM,
    MessageCallback,
)
from .hook_messages import MessageEntry, get_message_id_from_custom_user_message


_Hook = Callable[[], UINT]

THREAD_STATE__NOT_STARTED = 0
THREAD_STATE__THREAD_INITIALIZING = 1
THREAD_STATE__THREAD_STARTED = 2
THREAD_STATE__THREAD_LOOPING = 3
THREAD_STATE__DISPOSING = 4
THREAD_STATE__THREAD_STOPPING = 5
THREAD_STATE__THREAD_STOPPED = 6


class WindowsMessageLoop:  # pylint:disable=too-many-instance-attributes
    """
    Connects to the important windows shell events,
    and directs those to callback functions.
    """

    __slots__ = (
        '_key_hook', '_shell_hook',
        '_hwnd', '__state',
        '_window_message_map', '_key_handler',
        '_shell_message_map',
        '_shell_handler',
        '_message_callback_handler',
        '_on_exit',
        '_thread',
    )

    def __init__(self) -> None:
        self._key_hook: Optional[HHOOK] = None
        self._shell_hook: Optional[HHOOK] = None
        self._hwnd: Optional[HWND] = None
        self.__state = THREAD_STATE__NOT_STARTED
        self._window_message_map: Dict[int, MessageCallback] = {}
        self._shell_message_map: Dict[int, MessageCallback] = {}
        self._key_handler: Optional[
            Callable[[int, int, bool, bool], Tuple[bool, Sequence[Tuple[int, bool]]]]
        ] = None
        self._on_exit: Callable[[], None] = default_on_exit
        self._thread: Optional[threading.Thread] = None

    @property
    def hwnd(self) -> Optional[HWND]:
        """Get the running message window's HWND."""
        return self._hwnd

    def send_custom_message_to_self(
            self, custom_message_id: int, wparam: WPARAM, lparam: LPARAM,
    ) -> StdRet[None]:
        """Send a message to the running message window's HWND."""
        message = UINT(get_message_id_from_custom_user_message(custom_message_id))
        if self._hwnd and WINDOWS_FUNCTIONS.window.send_message:
            print(f'Sending custom message to self: {message}')
            res = WINDOWS_FUNCTIONS.window.send_message(self._hwnd, message, wparam, lparam)
            if res.has_error:
                return res.forward()
            return RET_OK_NONE
        print(f'Could not send message to self: no send message or no hwnd {self._hwnd}')
        return StdRet.pass_errmsg(
            user_messages.TRANSLATION_CATALOG,
            _('not running or not SendMessage implemented'),
        )

    def set_key_handler(
            self, callback: Callable[
                [int, int, bool, bool], Tuple[bool, Sequence[Tuple[int, bool]]],
            ]
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

    def set_on_exit_callback(self, callback: Callable[[], None]) -> None:
        """Set the on-exit message loop callback."""
        self._on_exit = callback

    def add_message_handler(self, message: MessageEntry) -> None:
        """Add a message handler, generated by hook_messages"""
        if message[0]:
            # It's a shell message
            self._shell_message_map[message[1]] = message[2]
        else:
            self._window_message_map[message[1]] = message[2]

    def is_running(self) -> bool:
        """Is the thread running?"""
        return self.__state == THREAD_STATE__THREAD_LOOPING

    def is_alive(self) -> bool:
        """Is the thread running?"""
        return self._thread is not None and self._thread.is_alive()

    def start(self) -> None:
        """Start the event monitoring thread."""
        if self.__state != THREAD_STATE__NOT_STARTED:
            log.info("message pumper already started.")
            return

        log.info("message_pumper: Starting the Windows message pumper thread.")
        self._thread = threading.Thread(
            target=self._message_pumper,
            daemon=True,
        )
        self.__state = THREAD_STATE__THREAD_INITIALIZING
        self._thread.start()
        atexit.register(self.dispose)

    def dispose(self, timeout: float = -1.0) -> None:
        """Close all the connections."""
        if self.__state == THREAD_STATE__DISPOSING:
            # Already triggered dispose...
            log.info('dispose: stopping re-entrance of dispose call.')
            return
        log.info(
            "dispose: Stopping the Windows message pumper thread (state = {state}).",
            state=self.__state,
        )
        if self.__state == THREAD_STATE__THREAD_LOOPING:
            self.__state = THREAD_STATE__DISPOSING
        if self._hwnd and WINDOWS_FUNCTIONS.window.close:  # pragma no cover
            log.trace("dispose: Sending close message to self {h:04x}.", h=self._hwnd)
            close_res = WINDOWS_FUNCTIONS.window.close(self._hwnd)
            if close_res.has_error:
                log.error(
                    "dispose: Failed to close self: {errors}",
                    errors=[m.debug() for m in close_res.error_messages()],
                )
        if (  # pragma no cover
                self.__state in (THREAD_STATE__THREAD_LOOPING, THREAD_STATE__DISPOSING)
                and WINDOWS_FUNCTIONS.window.send_message and self._hwnd
        ):
            log.info('dispose: Sending shutdown to window message consumer {h:04x}.', h=self._hwnd)
            send_res = WINDOWS_FUNCTIONS.window.send_message(
                self._hwnd, UINT(windows_constants.WM_QUIT), t_cast(WPARAM, 0), t_cast(LPARAM, 0),
            )
            if send_res.has_error:
                log.error(
                    "dispose: Failed to send quit message to self: {errors}",
                    errors=[m.debug() for m in send_res.error_messages()],
                )
            else:
                log.trace('dispose: Send message returned {code}', code=send_res.value)
        else:
            log.trace('dispose: skipped shutdown due to state {state}', state=self.__state)

        # This seems to not be encountered, but is here to ensure the message loop
        # stops correctly.
        if self._thread and self._thread.is_alive():  # pragma no cover
            log.trace('dispose: joining thread timing out after {t} seconds', t=timeout)
            self._thread.join(None if timeout <= 0 else timeout)  # pragma no cover

        # Must be called before unsetting _hwnd
        self._unhook()
        self.__state = THREAD_STATE__THREAD_STOPPED
        self._hwnd = None
        self._thread = None

    def __hook(self) -> StdRet[None]:
        """Creates the message window, and hooks all the listeners to the window.
        This must be done inside the message loop, which is why it's a private method."""

        if (
            WINDOWS_FUNCTIONS.shell.create_global_message_handler is None
            or WINDOWS_FUNCTIONS.window.create_message_window is None
            or WINDOWS_FUNCTIONS.shell.register_window_hook is None
        ):
            return RET_OK_NONE

        if WINDOWS_FUNCTIONS.shell.keyboard_hook:  # pragma no cover
            hook_res = WINDOWS_FUNCTIONS.shell.keyboard_hook(self.message_key_handler)
            if hook_res.has_error:
                log.error(
                    "registration: Failed to register key handler: {errors}",
                    errors=[m.debug() for m in hook_res.error_messages()],
                )
            else:
                self._key_hook = hook_res.result
                log.trace("registration: Registered keyboard hook {hook}", hook=hook_res.result)

        message_callback_handler = WINDOWS_FUNCTIONS.shell.create_global_message_handler(
            self._window_message_map,
        )
        hwnd_res = WINDOWS_FUNCTIONS.window.create_message_window(
            "PyWinShell Hooks", message_callback_handler,
        )
        if hwnd_res.has_error:  # pragma no cover
            log.error(  # pragma no cover
                "registration: Error creating message window: {errors}; cannot continue.",
                errors=[m.debug() for m in hwnd_res.error_messages()],
            )
            # Note: we do still continue here, because there's state stuff that needs to
            # happen.
        self._hwnd = hwnd_res.value

        if self._hwnd:  # pragma no cover
            log.trace("registration: Registering window hook {hwnd:04x}", hwnd=self._hwnd)
            msg_res = WINDOWS_FUNCTIONS.shell.register_window_hook(
                self._hwnd, self._window_message_map, self.message_shell_handler,
            )
            if msg_res.has_error:
                log.error(
                    "registration: Failed to register window hook: {errs}; cannot continue",
                    errs=[m.debug() for m in msg_res.error_messages()],
                )

            if WINDOWS_FUNCTIONS.shell.register_session_notification:
                sess_res = WINDOWS_FUNCTIONS.shell.register_session_notification(
                    self._hwnd, False,
                )
                if sess_res.has_error:
                    log.error(
                        "registration: Failed to register for session notifications: {errs}",
                        errs=[m.debug() for m in sess_res.error_messages()],
                    )
        return RET_OK_NONE

    def _unhook(self) -> None:
        if self._key_hook and WINDOWS_FUNCTIONS.shell.unhook:  # pragma no cover
            WINDOWS_FUNCTIONS.shell.unhook(self._key_hook)
            self._key_hook = None
        if self._shell_hook and WINDOWS_FUNCTIONS.shell.unhook:  # pragma no cover
            WINDOWS_FUNCTIONS.shell.unhook(self._shell_hook)
            self._shell_hook = None
        if (  # pragma no cover
                self._hwnd and WINDOWS_FUNCTIONS.shell.unregister_session_notification
        ):
            user_messages.report_send_receive_problems(
                WINDOWS_FUNCTIONS.shell.unregister_session_notification(self._hwnd)
            )

    def _message_pumper(self) -> None:
        # This runs in a background thread.
        # If this doesn't stop during shutdown, then an exception
        # is reported to the console.  This indicates that the quit
        # event message queue either didn't run soon enough, or it
        # was never triggered.

        # This shouldn't happen, but just to be sure, because it being wrong could be
        # catastrophic to a system.
        if (  # pragma no cover
            self._hwnd is not None
            or self.__state != THREAD_STATE__THREAD_INITIALIZING
        ):
            raise ValueError('already running (or finished running)')  # pragma no cover
        self.__state = THREAD_STATE__THREAD_STARTED

        try:
            log.trace('message_pump: In the message pumper')

            # Message window creation + hook registration MUST be in the same thread!
            # So this registration can only happen right before the loop starts.

            res = self.__hook()
            if res.has_error:
                # Can't continue
                self.__state = THREAD_STATE__THREAD_STOPPING
                return

            if (
                self._hwnd
                and WINDOWS_FUNCTIONS.shell.pump_messages
            ):
                log.debug("message_pump: Pumping messages on hwnd 0x{hwnd:04x}", hwnd=self._hwnd)

                # Thread sort-of-safety thing here...
                # It's hard to duplicate, so we skip it.  It's an added comfort thing that
                # could potentially still cause problems because of the lack of locks.
                if self.__state != THREAD_STATE__THREAD_STARTED:  # pragma no cover
                    log.error(  # pragma no cover
                        'weird state while starting the thread: {state}', state=self.__state,
                    )
                    self.__state = THREAD_STATE__THREAD_STOPPING  # pragma no cover
                    self.dispose()  # pragma no cover
                    return  # pragma no cover

                self.__state = THREAD_STATE__THREAD_LOOPING
                WINDOWS_FUNCTIONS.shell.pump_messages(self._on_exit)
                log.debug("message_pump: Pump messages ended.")
            else:  # pragma no cover
                log.error(  # pragma no cover
                    "message_pump: Basic platform functions not defined; cannot continue"
                )
        except BaseException as err:  # pylint:disable=broad-except  # pragma no cover
            log.error(  # pragma no cover
                "message_pump: generated unexpected exception {err}", err=err,
            )
            traceback.print_exception(type(err), err, err.__traceback__)  # pragma no cover

        self._unhook()
        log.info('message_pump: Stopping the Windows message pumper')
        self.__state = THREAD_STATE__THREAD_STOPPING

    def message_key_handler(
            self,
            vk_code: int, scan_code: int, is_key_up: bool, is_injected: bool,
    ) -> Optional[str]:
        """Key handler, called inside the message pumper."""
        # print(f"[key] {vk_to_names(vk_code)} {vk_code} {'up' if is_key_up else 'dn'}")
        if self._key_handler:
            res = self._key_handler(vk_code, scan_code, is_key_up, is_injected)
            if WINDOWS_FUNCTIONS.shell.inject_input_vks and res[1]:
                if not WINDOWS_FUNCTIONS.shell.inject_input_vks(res[1]):
                    print(" - injection of {0} failed".format(res[1]))
                # Injection may cause a problem, but that's ignored.
            if res[0]:
                # print(" - cancelling callback chain for key")
                return SHELL__CANCEL_CALLBACK_CHAIN
            # else:
            #     print(" - passing on key")
        return None

    def message_shell_handler(
            self,
            source_hwnd: HWND, message: int, wparam: WPARAM, lparam: LPARAM,
    ) -> bool:
        """Shell message handler, called from within the message pumper."""
        # Shell window messages use the WPARAM to specify the kind of shell event.
        # See https://docs.microsoft.com/en-us/windows/win32/api/winuser/
        # nf-winuser-registershellhookwindow
        wparam_msg = t_cast(int, wparam)
        if wparam_msg in self._shell_message_map:
            log.trace(
                'shell: {source}: {message} ({wparam})',
                source=source_hwnd,
                message=message,
                wparam=wparam,
            )
            return self._shell_message_map[wparam_msg](source_hwnd, message, wparam, lparam)
        log.trace(
            'shell: 0x{wparam_msg:08x} not handled '
            '({message:08x} / {wparam:08x} / {lparam:08x})',
            wparam_msg=wparam_msg,
            message=message,
            wparam=wparam,
            lparam=lparam,
        )
        return True


def default_on_exit() -> None:
    """The default on-exit handler. Does nothing."""
