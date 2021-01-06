"""
Helper for running a native program.
"""

from typing import Tuple, Sequence, Dict
import os
import sys
import shlex
from petronia_common.util import StdRet


ENV__LIBRARY_PATH = 'LD_LIBRARY_PATH'


def get_native_exec_args(
        exec_with_args: str,
) -> StdRet[Tuple[Sequence[str], Dict[str, str]]]:
    """Construct the base executable command list and environment variables."""

    # Some Python launchers tweak the library path.
    # https://pyinstaller.readthedocs.io/en/stable/runtime-information.html
    env = os.environ.copy()  # make a copy of the environment
    if sys.platform != 'win32' and getattr(sys, 'frozen', False):
        # We are running in a bundle where the library path is important.
        lp_orig = env.get(ENV__LIBRARY_PATH + '_ORIG')
        if lp_orig is not None:
            env[ENV__LIBRARY_PATH] = lp_orig  # restore the original, unmodified value
        elif ENV__LIBRARY_PATH in env:
            # This happens when LD_LIBRARY_PATH was not set.
            # Remove the env var as a last resort:
            del env[ENV__LIBRARY_PATH]

    # This isn't 100% correct for Windows escaping, but for our purposes, we can at
    # least have the same behavior on path splitting in the ini files.
    cmd = shlex.split(exec_with_args, comments=True, posix=True)

    return StdRet.pass_ok((cmd, env))
