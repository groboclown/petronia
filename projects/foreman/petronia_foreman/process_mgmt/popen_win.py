
"""Windows-Based POpen, to allow proper pipe sharing with the child process.
"""

from typing import Mapping, Sequence, Iterable, Callable, Optional, Any
import os
import sys
import subprocess
import threading
from petronia_common.util import StdRet, StreamedBinaryReader, single_reader_loop
from petronia_common.util import i18n as _
from .process import ManagedProcess
from .util import create_cmd
from ..user_message import CATALOG


if sys.platform == 'win32':
    try:
        import msvcrt  # pylint: disable=import-error
        import _winapi  # pylint: disable=import-error
        import ctypes
        import ctypes.wintypes  # pylint: disable=import-error

        kernel32 = ctypes.windll.kernel32  # pylint: disable=import-error

        # See https://docs.microsoft.com/en-us/windows/win32/fileio/cancelioex-func
        CancelIoEx = kernel32.CancelIoEx
        HWND = ctypes.wintypes.HWND

        def run_launcher_windows(  # pylint: disable=too-many-locals
                identity: str,
                command: Sequence[str],
                env: Mapping[str, str],
                command_params: Mapping[str, str],
                temp_dir: str,
                _requested_permissions: Mapping[str, Sequence[str]],
        ) -> StdRet[ManagedProcess]:
            """Run a launcher program from Windows.  Launchers run by Windows will be passed the
            Windows file handle, not the file descriptor, because that's meaningless as
            Windows goes."""

            current_proc = _winapi.GetCurrentProcess()

            # rx pipe is for the parent to receive data.
            #   The write-end of this pipe is used by the child process.
            # tx pipe is for the parent to send data.
            #   The read-end of this pipe is used by the child process.
            h_rx_read, h_rx_write = _winapi.CreatePipe(None, 0)
            h_tx_read, h_tx_write = _winapi.CreatePipe(None, 0)
            print(f"Created pipe 1 handles: read {h_rx_read}, write {h_rx_write}")
            print(f"Created pipe 2 handles: read {h_tx_read}, write {h_tx_write}")

            child_h_rx_write = _winapi.DuplicateHandle(
                current_proc, h_rx_write, current_proc, 0, True,
                _winapi.DUPLICATE_SAME_ACCESS,
            )
            child_h_tx_read = _winapi.DuplicateHandle(
                current_proc, h_tx_read, current_proc, 0, True,
                _winapi.DUPLICATE_SAME_ACCESS,
            )

            split_cmd = create_cmd(
                command, temp_dir, int(child_h_rx_write), identity, command_params,
            )
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

                ret = ManagedWinProcess(identity, proc, h_rx_read, h_tx_write, [temp_dir])
                # await ret.watch_process()
                return StdRet.pass_ok(ret)
            except Exception as err2:  # pylint: disable=broad-except
                _close_handles(h_rx_read, child_h_rx_write, h_tx_write, child_h_tx_read)
                return StdRet.pass_errmsg(
                    CATALOG,
                    _('Failed to create process for {cmd}: {err}'),
                    cmd=split_cmd,
                    err=err2,
                )


        class ManagedWinProcess(ManagedProcess):  # pylint: disable=too-many-instance-attributes
            """Windows managed process"""

            __slots__ = (
                '__proc', '__h_read', '__h_write', '__write_fd', '__exit_code',
                '__read_thread', '__read_stream', '__read_io',
            )

            def __init__(  # pylint: disable=too-many-arguments
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
                self.__read_stream = StreamedBinaryReader()
                # Need to keep track of the fd for internal Python management.
                self.__read_io = os.fdopen(msvcrt.open_osfhandle(h_rx_read, 0), 'rb')
                self.__read_thread = threading.Thread(
                    target=single_reader_loop,
                    args=(self.__read_io, self.__read_stream,),
                    daemon=True,
                )
                print("Starting managed process reader thread")
                self.__read_thread.start()
                ManagedProcess.__init__(
                    self, ident,
                    self.__read_stream,
                    temp_files,
                )

            def stop(self) -> None:
                if self.__exit_code is None:
                    self.__proc.terminate()

            def wait_for_stop(self, timeout: float) -> bool:
                if self.__exit_code is None:
                    try:
                        self.__proc.wait(timeout)
                        return True
                    except subprocess.TimeoutExpired:
                        return False
                return True

            def write(self, data: bytes) -> None:
                os.write(self.__write_fd, data)

            def close_writer(self) -> None:
                _close_handles(self.__h_write)
                self.__h_write = None

            def watch_process(self, on_exit_cb: Callable[[int], None]) -> None:
                if self.__exit_code is None:
                    try:
                        print("Waiting for process to end")
                        self.__exit_code = self.__proc.wait()
                        print(f"process ended with {self.__exit_code}")
                    finally:
                        # Note that the file descriptors are just internal aliases for the handles,
                        # so they don't need to be closed.
                        print("Closing handles")
                        _close_handles(self.__h_write, self.__h_read)
                        self.__h_write = None
                        self.__h_read = None
                        print("Waiting on read thread for process to stop.")
                        self.__read_thread.join()
                        self.__read_stream.feed_eof()
                        print("Calling on-exit callback")
                        on_exit_cb(-1 if self.__exit_code is None else self.__exit_code)
                        # Python required cleanup
                        try:
                            self.__read_io.close()
                        except OSError:
                            pass
                else:
                    on_exit_cb(self.__exit_code)

        def _close_handles(*handles: Any) -> None:
            for handle in handles:
                if handle is not None:
                    print(f"Calling cancel i/o {handle}")
                    CancelIoEx(handle, None)
                    print(f"Calling close handle on {handle}")
                    _winapi.CloseHandle(handle)
                    print(f"Close handle {handle} completed")
    except ModuleNotFoundError as err:
        raise Exception('Trying to run as Windows without Windows libraries.') from err

else:
    def run_launcher_windows(
            identity: str,  # pylint: disable=unused-argument
            command: Sequence[str],  # pylint: disable=unused-argument
            env: Mapping[str, str],  # pylint: disable=unused-argument
            command_params: Mapping[str, str],  # pylint: disable=unused-argument
            temp_dir: str,  # pylint: disable=unused-argument
            _requested_permissions: Mapping[str, Sequence[str]],
    ) -> StdRet[ManagedProcess]:
        """Run a launcher program from Windows.  Launchers run by Windows will be passed the
        Windows file handle, not the file descriptor, because that's meaningless as Windows goes."""

        return StdRet.pass_errmsg(
            CATALOG,
            _('Not running under Windows.'),
        )
