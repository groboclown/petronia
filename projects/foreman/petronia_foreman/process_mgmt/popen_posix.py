
"""The process handler."""

from typing import Iterable, Sequence, Mapping, Callable, Optional
import asyncio
import os
import shlex
import subprocess
import fcntl
from petronia_common.event_stream import BinaryWriter
from petronia_common.util import StdRet
from petronia_common.util import i18n as _
from petronia_common.util.aio import FdStreamReader
from .process import ManagedProcess
from .util import create_cmd_and_dirs
from ..configuration import LauncherConfig, PlatformSettings


async def run_launcher_posix(
        identity: str,
        launcher_config: LauncherConfig,
        platform: PlatformSettings,
        _requested_permissions: Mapping[str, Sequence[str]],
) -> StdRet[ManagedProcess]:
    pipe_read, pipe_write = os.pipe()
    cmd, temp_dirs = create_cmd_and_dirs(launcher_config.command, platform, pipe_write)
    cmd_parts = shlex.split(cmd)
    try:
        # Must close pipe input if child will block waiting for end
        # Can also be closed in a preexec_fn passed to subprocess.Popen
        fcntl.fcntl(pipe_read, fcntl.F_SETFD, fcntl.FD_CLOEXEC)
        process = await asyncio.subprocess.create_subprocess_exec(
            cmd_parts[0], *cmd_parts[1:],
            stdin=subprocess.PIPE,
            text=False,
            pass_fds=(pipe_write,),
        )
        # Parent closes the write.
        os.close(pipe_write)
        return StdRet.pass_ok(ManagedPosixProcess(
            identity, process, FdStreamReader(pipe_read),
            process.stdin, temp_dirs,
        ))
    except OSError as err:
        return StdRet.pass_errmsg(
            _('Failed to launch [{cmd}]: {err}'),
            cmd='] ['.join(cmd_parts),
            err=err,
        )


class ManagedPosixProcess(ManagedProcess):
    """The process handler."""
    __slots__ = ('__process', '__exit_code')

    def __init__(
            self,
            ident: str,
            process: asyncio.subprocess.Process,
            reader: asyncio.StreamReader,
            writer: BinaryWriter,
            temp_files: Iterable[str],
    ) -> None:
        ManagedProcess.__init__(self, ident, reader, writer, temp_files)
        self.__process = process
        self.__exit_code: Optional[int] = None

    def stop(self) -> None:
        """Stop the running process."""
        self.__process.kill()

    async def watch_process(self, on_exit_cb: Callable[[int], None]) -> None:
        """Watch the process."""
        if self.__exit_code is None:
            self.__exit_code = await self.__process.wait()
            self._close()
        on_exit_cb(self.__exit_code)
