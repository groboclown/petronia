
"""The process handler."""

from typing import Iterable, Sequence, Mapping, Callable, Optional, BinaryIO
import asyncio
import os
import shlex
from petronia_common.util import StdRet
from petronia_common.util import i18n as _
from .process import ManagedProcess
from .util import create_cmd_and_dirs
from ..configuration import LauncherConfig, PlatformSettings
from ..user_message import CATALOG


try:
    import fcntl  # pylint: disable=import-error


    async def run_launcher_posix(  # pylint: disable=too-many-locals
            identity: str,
            launcher_cmd_option_key: str,
            launcher_config: LauncherConfig,
            platform: PlatformSettings,
            _requested_permissions: Mapping[str, Sequence[str]],
    ) -> StdRet[ManagedProcess]:
        """Runs the launcher on a POSIX platform."""
        # rx pipe is for the parent to receive data.
        #   The write-end of this pipe is used by the child process.
        # tx pipe is for the parent to send data.
        #   The read-end of this pipe is used by the child process.
        rx_read, rx_write = os.pipe()
        tx_read, tx_write = os.pipe()
        command = launcher_config.get_option(launcher_cmd_option_key)
        if command.has_error:
            return command.forward()
        cmd, temp_dirs = create_cmd_and_dirs(
            command.result, platform, rx_write,
        )
        cmd_parts = shlex.split(cmd)
        try:
            # Must close pipe input if child will block waiting for end
            # Can also be closed in a preexec_fn passed to subprocess.Popen
            fcntl.fcntl(rx_read, fcntl.F_SETFD, fcntl.FD_CLOEXEC)
            process = await asyncio.subprocess.create_subprocess_exec(  # pylint: disable=no-member
                cmd_parts[0], *cmd_parts[1:],
                stdin=tx_read,
                text=False,
                pass_fds=(rx_write,),
            )
            # Parent closes the write.
            os.close(rx_write)
            # os.close(tx_read)

            # Create the reader in the loop.
            stream_reader = asyncio.StreamReader()
            reader_protocol = asyncio.StreamReaderProtocol(stream_reader)
            await asyncio.get_event_loop().connect_read_pipe(
                lambda: reader_protocol,
                os.fdopen(rx_read),
            )

            return StdRet.pass_ok(ManagedPosixProcess(
                identity, process, stream_reader,
                os.fdopen(tx_write, 'wb'), temp_dirs,
            ))
        except OSError as err:
            return StdRet.pass_errmsg(
                CATALOG,
                _('Failed to launch [{cmd}]: {err}'),
                cmd='] ['.join(cmd_parts),
                err=err,
            )


    def make_fd_nonblocking(file_desc: int) -> None:
        """Make the file descriptor non-blocking."""
        flags = fcntl.fcntl(file_desc, fcntl.F_GETFL, 0)
        fcntl.fcntl(file_desc, fcntl.F_SETFL, flags | os.O_NONBLOCK)  # pylint: disable=no-member


    class ManagedPosixProcess(ManagedProcess):
        """The process handler."""

        __slots__ = ('__process', '__writer', '__exit_code')

        def __init__(  # pylint: disable=too-many-arguments
                self,
                ident: str,
                process,  # type: asyncio.subprocess.Process
                reader: asyncio.StreamReader,
                writer: BinaryIO,
                temp_files: Iterable[str],
        ) -> None:
            ManagedProcess.__init__(self, ident, reader, temp_files)
            self.__process = process
            self.__exit_code: Optional[int] = None
            self.__writer = writer

        def write(self, data: bytes) -> None:
            self.__writer.write(data)

        def close_writer(self) -> None:
            self.__writer.close()

        def stop(self) -> None:
            """Stop the running process."""
            self.__process.kill()

        async def watch_process(self, on_exit_cb: Callable[[int], None]) -> None:
            """Watch the process."""
            if self.__exit_code is None:
                self.__exit_code = await self.__process.wait()
                self._close()
            on_exit_cb(self.__exit_code)


except ModuleNotFoundError:
    async def run_launcher_posix(  # pylint: disable=unused-argument,too-many-arguments
            identity: str,
            launcher_cmd_option_key: str,
            launcher_config: LauncherConfig,
            platform: PlatformSettings,
            _requested_permissions: Mapping[str, Sequence[str]],
    ) -> StdRet[ManagedProcess]:
        """Runs the launcher on a POSIX platform."""
        return StdRet.pass_errmsg(
            CATALOG,
            _('Platform {platform} not supported.'),
            platform=platform.name,
        )
