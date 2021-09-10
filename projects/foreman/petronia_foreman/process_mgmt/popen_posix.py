
"""The process handler."""

from typing import Iterable, Sequence, Mapping, Callable, Optional, BinaryIO
import os
import subprocess  # nosec
from petronia_common.util import StdRet, StreamReadState, select_reader
from petronia_common.util import i18n as _
from .process import ManagedProcess
from .util import create_cmd
from ..configuration.platform import platform_name
from ..constants import TRANSLATION_CATALOG as CATALOG


try:
    import fcntl  # pylint: disable=import-error

    GLOBAL_READERS = StreamReadState(lambda x: None)
    GLOBAL_READERS.start_read_loop_thread(select_reader)

    def run_launcher_posix(  # pylint: disable=too-many-locals
            identity: str,
            command: Sequence[str],
            env: Mapping[str, str],
            command_params: Mapping[str, str],
            temp_dir: str,
            _requested_permissions: Mapping[str, Sequence[str]],
    ) -> StdRet[ManagedProcess]:
        """Runs the launcher on a POSIX platform."""
        # rx pipe is for the parent to receive data.
        #   The write-end of this pipe is used by the child process.
        # tx pipe is for the parent to send data.
        #   The read-end of this pipe is used by the child process.
        rx_read, rx_write = os.pipe()
        tx_read, tx_write = os.pipe()
        cmd = create_cmd(
            command, temp_dir, rx_write, identity, command_params,
        )
        try:
            # Must close pipe input if child will block waiting for end
            # Can also be closed in a preexec_fn passed to subprocess.Popen
            fcntl.fcntl(rx_read, fcntl.F_SETFD, fcntl.FD_CLOEXEC)

            # Yes, this is using Popen.  Arguments are somewhat loaded in from
            # the user, but these are explicit split arguments without shell access.
            # This helps restrict the security issues present with this.
            process = subprocess.Popen(  # pylint: disable=no-member,consider-using-with  # nosec
                args=cmd,
                env=env,
                stdin=tx_read,
                text=False,
                pass_fds=(rx_write,),
            )
            # Parent closes the write.
            os.close(rx_write)
            # os.close(tx_read)

            return StdRet.pass_ok(ManagedPosixProcess(
                identity, process, rx_read,
                os.fdopen(tx_write, 'wb'), [temp_dir],
            ))
        except OSError as err:
            return StdRet.pass_errmsg(
                CATALOG,
                _('Failed to launch [{cmd}]: {err}'),
                cmd='] ['.join(cmd),
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
                process: subprocess.Popen,
                reader_fd: int,
                writer: BinaryIO,
                temp_files: Iterable[str],
        ) -> None:
            stream = GLOBAL_READERS.add_fd(reader_fd)
            ManagedProcess.__init__(self, ident, stream, temp_files)
            self.__process = process
            self.__exit_code: Optional[int] = None
            self.__writer = writer

        def write(self, data: bytes) -> None:
            self.__writer.write(data)
            # Ensure the data is not buffered.  That can lead to events being
            # delayed on sending.
            self.__writer.flush()

        def close_writer(self) -> None:
            self.__writer.close()

        def stop(self) -> None:
            """Stop the running process."""
            self.__process.kill()

        def wait_for_stop(self, timeout: float) -> bool:
            if self.__exit_code is None:
                try:
                    self.__process.wait(timeout)
                    # Ensure everything is closed off.
                    self.watch_process(lambda x: None)
                    return True
                except subprocess.TimeoutExpired:
                    return False
            return True

        def watch_process(self, on_exit_cb: Callable[[int], None]) -> None:
            """Watch the process."""
            if self.__exit_code is None:
                self.__exit_code = self.__process.wait()
                self._close()
            on_exit_cb(self.__exit_code)


except ModuleNotFoundError:
    def run_launcher_posix(  # pylint:disable=unused-argument,too-many-arguments
            identity: str,  # pylint:disable=unused-argument
            command: Sequence[str],  # pylint:disable=unused-argument
            env: Mapping[str, str],  # pylint:disable=unused-argument
            command_params: Mapping[str, str],  # pylint:disable=unused-argument
            temp_dir: str,  # pylint:disable=unused-argument
            _requested_permissions: Mapping[str, Sequence[str]],
    ) -> StdRet[ManagedProcess]:
        """Runs the launcher on a POSIX platform."""
        return StdRet.pass_errmsg(
            CATALOG,
            _('Platform {platform} not supported.'),
            platform=platform_name,
        )
