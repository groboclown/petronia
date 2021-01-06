"""
Helpers for launching a Python interpreter as the executable.
"""

from typing import List, Sequence, Tuple, Dict
import os
import sys
from petronia_common.util import StdRet
from ...configuration.platform import detect_install_dir

ENV__PYTHONPATH = 'PYTHONPATH'


def get_python_exec_args(
        module_name: str,
        additional_module_paths: Sequence[str],
        reuse_current_path: bool,
) -> StdRet[Tuple[Sequence[str], Dict[str, str]]]:
    """Get the argument list and environment variables for running the given python
    module.  If running the module requires additional, module-specific arguments,
    then those are also added."""

    # When a normal Python script runs, sys.executable is the path to the program that
    # was executed, namely, the Python interpreter. In a frozen app, sys.executable is
    # also the path to the program that was executed, but that is not Python; it is the
    # bootloader in either the one-file app or the executable in the one-folder app.

    exec_args = (sys.executable, '-m', module_name)
    env = os.environ.copy()

    py_path: List[str] = []
    if reuse_current_path:
        # Keep original invoked path as first in all cases.
        for value in sys.path:
            path_value = os.path.abspath(value)
            if path_value not in py_path:
                py_path.append(path_value)
        install_dir = os.path.abspath(detect_install_dir())
        if install_dir not in py_path:
            py_path.append(install_dir)

    # Mod path is always after the invoked path, so it can't override built-in
    # python / petronia stuff.
    for mod_path in additional_module_paths:
        path_value = os.path.abspath(mod_path)
        if path_value not in py_path:
            py_path.append(path_value)

    env[ENV__PYTHONPATH] = os.path.pathsep.join(py_path)

    return StdRet.pass_ok((exec_args, env))
