"""
Low-level hooks for connecting events to call-backs.
"""

from typing import Callable, Optional
import faulthandler
import signal


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
        assert self.__state == 0, 'can only be run before started'
        self.__log_fd = root_log_fd

    def register_on_shutdown(self, callback: Optional[Callable[[], None]]) -> None:
        """Register the handler for when a nice shutdown request comes in."""
        self.__on_shutdown = callback

    def start(self) -> None:
        """Start the connections."""
        assert self.__state == 0, 'can only be run before started'
        self.__state = 1
        if self.__log_fd is not None:
            faulthandler.enable(self.__log_fd, all_threads=True)

    def stop(self) -> None:
        """Stop the connections."""
        if self.__state != 1:
            # safe to call multiple times.
            return
        if self.__log_fd and faulthandler.is_enabled():
            faulthandler.disable()
        self.__state = 2
