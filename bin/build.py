#!/bin/env /usr/bin/python3

"""
Runs the CI build.  This should be extremely simple.
"""

from typing import List
import os
import sys
import platform
import subprocess


def build_std_project_dir(root_project_dir: str, project_dir: str) -> int:
    top_package_names: List[str] = []
    mypy_args: List[str] = ['--warn-unused-configs', '--no-incremental']
    for name in os.listdir(project_dir):
        fqn = os.path.join(project_dir, name)
        if '.' not in name and os.path.isdir(fqn):
            top_package_names.append(name)
            mypy_args.append('--package')
            mypy_args.append(name)

    print("")
    print("----------------------------------------------------------------------")
    print("Type Checking...")
    code = run_python_cmd(
        project_dir,
        [os.path.abspath(os.path.join(root_project_dir, 'py-common-lib'))],
        'mypy',
        mypy_args,
        True,
    )
    if code != 0:
        print(f"MyPy exited with {code}")
        return code

    print("")
    print("----------------------------------------------------------------------")
    print("Linting...")
    code = run_python_cmd(
        project_dir,
        [
            os.path.abspath(os.path.join(root_project_dir, 'py-common-lib')),
            os.path.abspath(os.path.join(root_project_dir, 'extension-tools')),
        ],
        'pylint',
        [
            '--load-plugins',
            'petronia_extension_tools.pylint_plugins.trailing_commas',
            *top_package_names,
        ],
        True,
    )

    if code != 0:
        print(f"Linting exited with {code}")
        # For now, lint exit code is ignored.
        # return code

    print("")
    print("----------------------------------------------------------------------")
    print("Unit Testing...")
    code = run_python_cmd(
        project_dir,
        [os.path.abspath(os.path.join(root_project_dir, 'py-common-lib'))],
        'coverage',
        ['run', '--source', '.', '-m', 'unittest', 'discover', '-s', '.', '-p', '*_test.py'],
        True,
    )
    # Don't care about code coverage report stats exit code?
    report_exit_code = run_python_cmd(
        project_dir,
        [],
        'coverage',
        ['report', '-m'],
        True,
    )
    if code != 0:
        print(f"Unit test exited with {code}")
        return code
    return 0


def run_python_cmd(
        cwd: str,
        extra_py_path: List[str],
        module: str,
        args: List[str],
        fail_on_nonzero: bool,
) -> int:
    env = dict(os.environ)
    if 'PYTHONPATH' in env:
        env['PYTHONPATH'] = os.path.pathsep.join([*extra_py_path, env['PYTHONPATH']])
    else:
        env['PYTHONPATH'] = os.path.pathsep.join(extra_py_path)
    python_cmd = 'python3'
    if platform.system() == 'Windows':
        python_cmd = 'python'
    cmd = [
        python_cmd,
        "-m", module,
        *args,
    ]
    result = subprocess.run(
        cmd,
        cwd=cwd,
        env=env,
    )
    if fail_on_nonzero:
        return result.returncode
    return 0


PRIORITY_PROJECTS = ('py-common-lib', 'extension-tools',)
IGNORED_PROJECT_DIRS = ()


def get_std_project_dirs(project_dir: str) -> List[str]:
    """All the project directories, in prioritized order"""
    ret: List[str] = []
    contents = os.listdir(project_dir)
    ordered_search: List[str] = list(PRIORITY_PROJECTS)
    for name in contents:
        if name not in ordered_search and name not in IGNORED_PROJECT_DIRS:
            ordered_search.append(name)
    for name in ordered_search:
        fqn = os.path.abspath(os.path.join(project_dir, name))
        if os.path.isdir(fqn):
            ret.append(fqn)
    return ret


def main(root_project_dir: str) -> int:
    """Static + Dynamic Checks on the code."""
    total_code = 0
    print("======================================================================")
    print("======================================================================")
    print("Standard Build Projects")
    print("")
    for std_project_dir in get_std_project_dirs(root_project_dir):
        print("======================================================================")
        project_name = os.path.basename(std_project_dir)
        print(f":: {project_name} ::")
        partial_code = build_std_project_dir(root_project_dir, std_project_dir)
        if partial_code != 0:
            print(f":: {project_name} failed: {partial_code} ::")
        total_code += partial_code

    return total_code


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: build.py (dir of `projects`)")
        sys.exit(1)
    sys.exit(main(sys.argv[1]))
