
"""Windows-Based POpen, to allow proper pipe sharing with the child process.
"""

from typing import Mapping, Sequence, Iterable, Callable, Optional, Any
import os
import shlex
import platform
import asyncio
import subprocess
from petronia_common.util import StdRet
from petronia_common.util import i18n as _
from petronia_common.util.aio import aio_fd_reader
from .process import ManagedProcess
from .util import create_cmd_and_dirs
from ..configuration.launcher import LauncherConfig
from ..configuration.platform import PlatformSettings
from ..user_message import CATALOG

if platform.system() == 'Windows':
    import msvcrt  # pylint: disable=import-error
    import _winapi  # pylint: disable=import-error

    async def run_launcher_windows(
            identity: str,
            launcher_cmd_option_key: str,
            launcher_config: LauncherConfig,
            platform_settings: PlatformSettings,
            _requested_permissions: Mapping[str, Sequence[str]],
    ) -> StdRet[ManagedProcess]:
        """Run a launcher program from Windows.  Launchers run by Windows will be passed the
        Windows file handle, not the file descriptor, because that's meaningless as Windows goes."""

        current_proc = _winapi.GetCurrentProcess()

        # rx pipe is for the parent to receive data.
        #   The write-end of this pipe is used by the child process.
        # tx pipe is for the parent to send data.
        #   The read-end of this pipe is used by the child process.
        h_rx_read, h_rx_write = _winapi.CreatePipe(None, 0)
        h_tx_read, h_tx_write = _winapi.CreatePipe(None, 0)

        child_h_rx_write = _winapi.DuplicateHandle(
            current_proc, h_rx_write, current_proc, 0, True,
            _winapi.DUPLICATE_SAME_ACCESS,
        )
        child_h_tx_read = _winapi.DuplicateHandle(
            current_proc, h_tx_read, current_proc, 0, True,
            _winapi.DUPLICATE_SAME_ACCESS,
        )

        command = launcher_config.get_option(launcher_cmd_option_key)
        if command.has_error:
            return command.forward()
        cmd, temp_dirs = create_cmd_and_dirs(
            command.result, platform_settings, int(child_h_rx_write),
        )
        split_cmd = split_windows_cmd(cmd)
        env = os.environ.copy()
        try:
            # print("[DEBUG] Running windows command {0}".format(split_cmd))
            # h_proc, h_thread, pid, tid = _winapi.CreateProcess(
            #         split_cmd[0], ' '.join(split_cmd[1:])
            #         None, None, False, 0, env, launcher_config.run_dir, None
            # )
            # _winapi.CloseHandle(h_thread)
            proc = subprocess.Popen(
                split_cmd,
                close_fds=False,  # Important to inherit just the explicitly shared handles.
                stdin=msvcrt.open_osfhandle(child_h_tx_read, 0),
                text=False,
                env=env,
            )
            # The parent process needs to close the child's end of the pipes.
            _close_handles(child_h_rx_write, child_h_tx_read)

            ret = ManagedWinProcess(identity, proc, h_rx_read, h_tx_write, temp_dirs)
            # await ret.watch_process()
            return StdRet.pass_ok(ret)
        except BaseException as err:
            _close_handles(h_rx_read, child_h_rx_write, h_rx_read, child_h_tx_read)
            return StdRet.pass_errmsg(
                CATALOG,
                _('Failed to create process for {cmd}: {err}'),
                cmd=cmd,
                err=err,
            )


    def split_windows_cmd(full: str) -> Sequence[str]:
        """Split the command line into arguments, specific for Windows"""
        # Just kind of do the thing, even though it's not really right.
        return shlex.split(full, posix=False)


    class ManagedWinProcess(ManagedProcess):
        """Windows managed process"""

        __slots__ = (
            '__proc', '__reader', '__read_fd', '__h_read', '__h_write', '__write_fd', '__exit_code',
        )

        def __init__(
                self,
                ident: str,
                proc: subprocess.Popen,
                h_rx_read: Any,
                h_tx_write: Any,
                temp_files: Iterable[str],
        ) -> None:
            self.__write_fd = msvcrt.open_osfhandle(h_tx_write, 0)
            self.__proc = proc
            self.__exit_code: Optional[int] = None
            self.__h_read = h_rx_read
            self.__h_write = h_tx_write
            self.__read_fd = msvcrt.open_osfhandle(h_rx_read, 0)
            self.__reader = asyncio.StreamReader()
            ManagedProcess.__init__(self, ident, self.__reader, temp_files)

        def stop(self) -> None:
            if self.__exit_code is None:
                self.__proc.terminate()

        def write(self, data: bytes) -> None:
            os.write(self.__write_fd, data)

        def close_writer(self) -> None:
            _close_handles(self.__h_write)
            self.__h_write = None

        async def watch_process(self, on_exit_cb: Callable[[int], None]) -> None:
            if self.__exit_code is None:
                async def proc_wait() -> None:
                    try:
                        self.__exit_code = self.__proc.wait()
                    finally:
                        # Note that the file descriptors are just internal aliases for the handles,
                        # so they don't need to be closed.
                        _close_handles(self.__h_write, self.__h_read)
                        self.__h_write = None
                        self.__h_read = None
                        on_exit_cb(-1 if self.__exit_code is None else self.__exit_code)

                await asyncio.gather(
                    # Note: the buffer size must be big enough to allow for reading pending data
                    # before the stream is closed.
                    aio_fd_reader(self.__read_fd, self.__reader, 2 ** 16),
                    proc_wait(),
                )
            else:
                on_exit_cb(self.__exit_code)

    def _close_handles(*handles: Any) -> None:
        for handle in handles:
            if handle is not None:
                _winapi.CloseHandle(handle)


else:
    async def run_launcher_windows(
            identity: str,
            launcher_cmd_option_key: str,
            launcher_config: LauncherConfig,
            platform_settings: PlatformSettings,
            _requested_permissions: Mapping[str, Sequence[str]],
    ) -> StdRet[ManagedProcess]:
        return StdRet.pass_errmsg(
            CATALOG,
            _('Not running under Windows.'),
        )
