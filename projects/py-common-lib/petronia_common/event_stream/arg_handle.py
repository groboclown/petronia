
"""
Tools to help get the file descriptor from the argument list.  The program must define which
argument is passed the handle, and this tool will return the correct handle.
"""

import platform
from ..util import StdRet
from ..util import i18n as _


def get_fd_from_argument(argument: str) -> StdRet[int]:
    """Get the file descriptor from the command-line argument."""
    try:
        int_arg = int(argument)
    except ValueError:
        return StdRet.pass_errmsg(
            _('Argument is not a file descriptor type: {arg}'),
            arg=argument,
        )

    if platform.system() == 'Windows':
        # On Windows, the file handle is passed in, not the fd.
        import msvcrt
        return StdRet.pass_ok(msvcrt.open_osfhandle(int_arg, 0))
    return StdRet.pass_ok(int_arg)
