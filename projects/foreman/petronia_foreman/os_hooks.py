"""
Low-level hooks for connecting events to call-backs.
"""
from typing import Callable, Optional
import faulthandler
import signal

SHUTDOWN_SIGNALS = ('SIGINT', 'SIGTERM', 'CTRL_C_EVENT')
RESTART_SIGNALS = ('SIGBREAK', 'SIGHUP', 'CTRL_BREAK_EVENT')
KILL_SIGNALS = ('SIGKILL',)


class OsHooks:
    """
    Connects signals and other external events from the OS to the foreman process.
    This should only be for low-level processing that the initial executable must handle,
    and not things that the native handler should instead handle.  This is a fine line,
    and best judgement should be used.

    This does not do the StdRet stuff, because it should all be handled internally.
    """

    __slots__ = ('__log_fd', '__on_shutdown', '__on_restart', '__on_kill', '__state')

    def __init__(self) -> None:
        self.__state = 0
        self.__log_fd: Optional[int] = None
        self.__on_shutdown: Optional[Callable[[], None]] = None
        self.__on_restart: Optional[Callable[[], None]] = None
        self.__on_kill: Optional[Callable[[], None]] = None

    def register_root_fd(self, root_log_fd: Optional[int]) -> None:
        """Register the root FD.  Can only be done before start."""
        self._ensure_not_started()
        self.__log_fd = root_log_fd

    def register_on_shutdown(self, callback: Optional[Callable[[], None]]) -> None:
        """Register the handler for when a nice shutdown request comes in."""
        self.__on_shutdown = callback

    def register_on_restart(self, callback: Optional[Callable[[], None]]) -> None:
        """Register the handler for when a restart request comes in."""
        self.__on_restart = callback

    def start(self) -> None:
        """Start the connections."""
        self._ensure_not_started()
        self.__state = 1
        if self.__log_fd is not None:
            faulthandler.enable(self.__log_fd, all_threads=True)

        if self.__on_shutdown:
            def shutdown_callback() -> None:
                # print("On shutdown")
                if self.__on_shutdown:
                    self.__on_shutdown()

            for signal_name in SHUTDOWN_SIGNALS:
                OsHooks._set_signal(signal_name, shutdown_callback)

        if self.__on_restart:
            def restart_callback() -> None:
                # print("On restart")
                if self.__on_restart:
                    self.__on_restart()

            for signal_name in RESTART_SIGNALS:
                OsHooks._set_signal(signal_name, restart_callback)

        if self.__on_kill:
            def kill_callback() -> None:
                # print("On kill")
                if self.__on_kill:
                    # pylint is complaining that this isn't callable.  Don't know why.
                    self.__on_kill()  # pylint: disable=not-callable

            for signal_name in KILL_SIGNALS:
                OsHooks._set_signal(signal_name, kill_callback)

    @staticmethod
    def _set_signal(
            signal_name: str,
            handler: Callable[[], None],
    ) -> None:
        if hasattr(signal, signal_name):
            try:
                signal.signal(getattr(signal, signal_name), lambda x, y: handler())
                # print(f"Set signal {signal_name}")
            except ValueError:
                # Not available on this platform
                pass

    def stop(self) -> None:
        """Stop the connections."""
        if self.__state != 1:
            # safe to call multiple times.
            return
        if self.__log_fd and faulthandler.is_enabled():
            faulthandler.disable()
        self.__state = 2

    def _ensure_not_started(self) -> None:
        if self.__state != 0:
            raise AttributeError('can only be run before started')
