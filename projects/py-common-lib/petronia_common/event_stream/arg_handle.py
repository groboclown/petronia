
"""
Tools to help get the file descriptor from the argument list.  The program must define which
argument is passed the handle, and this tool will return the correct handle.
"""

from typing import BinaryIO
import os
import platform
from ..util import StdRet
from ..util import i18n as _
from ..util import STANDARD_PETRONIA_CATALOG as STDC


def get_fd_from_argument(argument: str) -> StdRet[int]:
    """Get the file descriptor from the command-line argument."""
    try:
        int_arg = int(argument)
    except ValueError:
        return StdRet.pass_errmsg(
            STDC, _('Argument is not a file descriptor type: {arg}'),
            arg=argument,
        )

    if int_arg < 0:
        return StdRet.pass_errmsg(
            STDC, _('Argument is not a valid file descriptor value: {arg}'),
            arg=argument,
        )

    if platform.system() == 'Windows':
        # On Windows, the file handle is passed in, not the fd.
        import msvcrt  # pylint: disable=import-outside-toplevel,import-error  # pragma no cover
        try:  # pragma no cover
            int_arg = msvcrt.open_osfhandle(int_arg, 0)  # pragma no cover
        except OSError as err:  # pragma no cover
            return StdRet.pass_errmsg(  # pragma no cover
                STDC, _('Invalid file handle {arg}: {err}'), arg=argument, err=err,
            )
    # No other way to tell if the file descriptor is valid.
    return StdRet.pass_ok(int_arg)


class FdWriter:
    """BinaryWriter over an FD IO binary writer."""
    __slots__ = ('__writer',)

    def __init__(self, writer: BinaryIO) -> None:
        self.__writer = writer

    def write(self, data: bytes) -> None:
        """Perform the write operation."""
        self.__writer.write(data)
        # We must have the IO flush the data, because we
        # have no guarantee that the close() function will
        # be called.
        self.__writer.flush()

    def close(self) -> None:
        """Close the underlying stream."""
        self.__writer.close()


def get_fd_writer(file_descriptor: int) -> FdWriter:
    """Get the BinaryWriter compatible object for the file descriptor."""
    return FdWriter(os.fdopen(file_descriptor, 'wb'))


def get_fd_reader(file_descriptor: int) -> BinaryIO:
    """Get the BinaryReader compatible object for the file descriptor."""
    return os.fdopen(file_descriptor, 'rb')
