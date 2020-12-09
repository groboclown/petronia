"""
Helpers for launching a Python interpreter as the executable.
"""

from typing import List, Sequence, Tuple, Dict
import os
import sys
import shlex
from petronia_common.util import StdRet
from ...configuration.platform import detect_install_dir

ENV__PYTHONPATH = 'PYTHONPATH'


def get_python_exec_args(
        module_name: str,
        additional_module_paths: Sequence[str],
        reuse_current_path: bool,
) -> StdRet[Tuple[str, Dict[str, str]]]:
    """Get the argument list and environment variables for running the given python
    module.  If running the module requires additional, module-specific arguments,
    then those are also added."""

    # When a normal Python script runs, sys.executable is the path to the program that
    # was executed, namely, the Python interpreter. In a frozen app, sys.executable is
    # also the path to the program that was executed, but that is not Python; it is the
    # bootloader in either the one-file app or the executable in the one-folder app.

    exec_args = shlex.join((sys.executable, '-m', module_name))
    env = os.environ.copy()

    py_path: List[str]
    if reuse_current_path:
        py_path = list(sys.path)
        install_dir = detect_install_dir()
        if install_dir not in py_path:
            py_path.append(install_dir)
    else:
        py_path = []
    for mod_path in additional_module_paths:
        if mod_path not in py_path:
            py_path.append(mod_path)

    env[ENV__PYTHONPATH] = os.path.pathsep.join(py_path)

    return StdRet.pass_ok((exec_args, env))
