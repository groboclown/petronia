
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

    if int_arg < 0:
        return StdRet.pass_errmsg(
            _('Argument is not a valid file descriptor value: {arg}'),
            arg=argument,
        )

    if platform.system() == 'Windows':
        # On Windows, the file handle is passed in, not the fd.
        import msvcrt  # pylint: disable=import-outside-toplevel,import-error  # pragma no cover
        try:  # pragma no cover
            int_arg = msvcrt.open_osfhandle(int_arg, 0)  # pragma no cover
        except OSError as err:  # pragma no cover
            return StdRet.pass_errmsg(  # pragma no cover
                _('Invalid file handle {arg}: {err}'), arg=argument, err=err,
            )
    # No other way to tell if the file descriptor is valid.
    return StdRet.pass_ok(int_arg)
