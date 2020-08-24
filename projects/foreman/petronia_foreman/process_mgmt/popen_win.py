
"""Windows-Based POpen, to allow proper pipe sharing with the child process.
"""

from typing import Mapping, Tuple, Sequence, Iterable, Callable, Optional, Any
import os
import asyncio
import shlex
import platform
import subprocess
from petronia_common.event_stream import BinaryWriter
from petronia_common.util import StdRet
from petronia_common.util import i18n as _
from petronia_common.util.aio import FdStreamReader
from .process import ManagedProcess
from .util import create_cmd_and_dirs
from ..configuration.launcher import LauncherConfig
from ..configuration.platform import PlatformSettings

if platform.system() == 'Windows':
    import msvcrt
    import _winapi

    async def run_launcher_windows(
            identity: str,
            launcher_config: LauncherConfig,
            platform_settings: PlatformSettings,
            _requested_permissions: Mapping[str, Sequence[str]],
    ) -> StdRet[ManagedProcess]:
        """Run a launcher program from Windows.  Launchers run by Windows will be passed the
        Windows file handle, not the file descriptor, because that's meaningless as Windows goes."""

        current_proc = _winapi.GetCurrentProcess()
        h_read, h_write = _winapi.CreatePipe(None, 0)
        # The write-end of the pipe is used by the child process, the read-end by the parent.
        child_h_write = _winapi.DuplicateHandle(
            current_proc, h_write, current_proc, 0, True,
            _winapi.DUPLICATE_SAME_ACCESS,
        )
        cmd, temp_dirs = create_cmd_and_dirs(
            launcher_config.command, platform_settings, int(child_h_write),
        )
        split_cmd = split_windows_cmd(cmd)
        env = os.environ.copy()
        try:
            # h_proc, h_thread, pid, tid = _winapi.CreateProcess(
            #         split_cmd[0], ' '.join(split_cmd[1:])
            #         None, None, False, 0, env, launcher_config.run_dir, None
            # )
            # _winapi.CloseHandle(h_thread)
            proc = subprocess.Popen(
                split_cmd,
                close_fds=False,  # Important to inherit just the explicitly shared handles.
                stdin=subprocess.PIPE,
                text=False,
            )
            # The parent process needs to close the write-end of the pipe.
            _winapi.CloseHandle(child_h_write)
            return StdRet.pass_ok(ManagedWinProcess(
                identity, proc, h_read, h_write,
                temp_dirs,
            ))
        except BaseException as err:
            _winapi.CloseHandle(h_read)
            _winapi.CloseHandle(h_write)
            return StdRet.pass_errmsg(
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

        __slots__ = ('__proc', '__h_read', '__h_write', '__exit_code')

        def __init__(
                self,
                ident: str,
                proc: subprocess.Popen,
                h_read: Any,
                h_write: Any,
                temp_files: Iterable[str],
        ) -> None:
            read_fd = msvcrt.open_osfhandle(h_read, 0)
            reader = FdStreamReader(read_fd)
            ManagedProcess.__init__(self, ident, reader, proc.stdin, temp_files)
            self.__proc = proc
            self.__exit_code: Optional[int] = None
            self.__h_read = h_read
            self.__h_write = h_write

        def stop(self) -> None:
            if self.__exit_code is None:
                self.__proc.terminate()

        async def watch_process(self, on_exit_cb: Callable[[int], None]) -> None:
            if self.__exit_code is None:
                # msecs = _winapi.INFINITE
                # else:
                #    msecs = max(0, int(timeout * 1000 + 0.5))
                # res = _winapi.WaitForSingleObject(int(self.__h_proc), msecs)
                # if res == _winapi.WAIT_OBJECT_0:
                #     self.__exit_code = _winapi.GetExitCodeProcess(self.__h_proc)
                #     _close_handles(self.__h_write, self.__h_proc)
                #     self._close()
                # else:
                #     # ???  Shouldn't happen with an indefinite wait.
                #     self.__exit_code = -1
                #     _winapi.TerminateProcess(int(self.__h_proc), 1)
                #     _close_handles(self.__h_write, self.__h_proc)
                #     self._close()
                self.__exit_code = self.__proc.wait()
            on_exit_cb(self.__exit_code)

    def _close_handles(*handles: Any):
        for handle in handles:
            _winapi.CloseHandle(handle)


else:
    async def run_launcher_windows(
            _identity: str,
            _launcher_config: LauncherConfig,
            _platform: PlatformSettings,
            _requested_permissions: Mapping[str, Sequence[str]],
    ) -> StdRet[ManagedProcess]:
        return StdRet.pass_errmsg(_('Not running under Windows.'))
