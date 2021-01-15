#!/bin/env /usr/bin/python3

"""
Runs the CI build.  This should be as simple as possible while being useful.
"""

from typing import List, Tuple
import os
import sys
import shutil
import subprocess


def build_std_project_dir(root_project_dir: str, project_dir: str) -> int:
    top_package_names: List[str] = []
    mypy_args: List[str] = ['--warn-unused-configs', '--no-incremental']
    for name in os.listdir(project_dir):
        fqn = os.path.join(project_dir, name)
        if '.' not in name and name[0] != '_' and os.path.isdir(fqn):
            top_package_names.append(name)
            mypy_args.append('--package')
            mypy_args.append(name)

    extra_path: List[str] = []
    if project_dir.endswith('-tests'):
        # special case for top-level testing projects that require cross-project path.
        for dirname in os.listdir(root_project_dir):
            fqn = os.path.join(root_project_dir, dirname)
            if fqn not in extra_path and os.path.isdir(fqn):
                extra_path.append(fqn)


    print("")
    print("----------------------------------------------------------------------")
    print("Type Checking...")
    mypy_code = run_python_cmd(
        project_dir,
        [os.path.abspath(os.path.join(root_project_dir, 'py-common-lib'))],
        'mypy',
        mypy_args,
        True,
    )
    if mypy_code != 0:
        # If mypy fails, there's little point in running anything else.
        print(f"MyPy exited with {mypy_code}")
        return mypy_code

    print("")
    print("----------------------------------------------------------------------")
    print("Linting...")
    lint_code = run_python_cmd(
        project_dir,
        [
            os.path.abspath(os.path.join(root_project_dir, 'py-common-lib')),
            os.path.abspath(os.path.join(root_project_dir, 'extension-tools')),
            *extra_path,
        ],
        'pylint',
        [
            '--load-plugins',
            'petronia_extension_tools.pylint_plugins.trailing_commas',
            *top_package_names,
        ],
        True,
    )

    if lint_code != 0:
        print(f"Linting exited with {lint_code}")
        # Let unit test run, even if linting failed.

    print("")
    print("----------------------------------------------------------------------")
    print("Unit Testing...")
    test_code = run_python_cmd(
        project_dir,
        [
            os.path.abspath(os.path.join(root_project_dir, 'py-common-lib')),
            *extra_path,
        ],
        'coverage',
        [
            'run', '--source', '.', '--timid',
            # We are daring...
            '--branch',
            '-m', 'unittest', 'discover', '-s', '.', '-p', '*_test.py',
        ],
        True,
    )
    if test_code != 0:
        print(f"Unit test exited with {test_code}")

    report_code = run_python_cmd(
        project_dir,
        [],
        'coverage',
        ['report', '-m', '--fail-under', '99'],
        True,
    )
    if report_code != 0:
        print(f"Code coverage exited with {report_code}")

    return lint_code + test_code + report_code


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
    python_cmd = sys.executable
    cmd = [
        shutil.which(python_cmd),
        # "-X", "dev",
        # "-bb",
        "-m", module,
        *args,
    ]
    # print("Running " + str(cmd))
    result = subprocess.run(
        cmd,
        cwd=cwd,
        env=env,
    )
    if fail_on_nonzero:
        return result.returncode
    return 0


PRIORITY_PROJECTS = ('py-common-lib', 'extension-tools',)
IGNORED_PROJECT_DIRS = ('py-stubs',)


def get_std_project_dirs(project_dir: str) -> List[Tuple[str, str]]:
    """All the project directories, in prioritized order"""
    ret: List[Tuple[str, str]] = []
    contents = os.listdir(project_dir)
    root_dir = os.path.abspath(project_dir)
    if 'mypy.ini' in contents:
        # This is a single directory to build.
        return [(os.path.dirname(root_dir), root_dir)]
    ordered_search: List[str] = list(PRIORITY_PROJECTS)
    for name in contents:
        if name not in ordered_search and name not in IGNORED_PROJECT_DIRS:
            ordered_search.append(name)
    for name in ordered_search:
        fqn = os.path.join(root_dir, name)
        if os.path.isdir(fqn):
            ret.append((root_dir, fqn))
    return ret


def main(root_project_dir: str, child_projects: List[str]) -> int:
    """Static + Dynamic Checks on the code."""
    total_code = 0
    print("======================================================================")
    print("======================================================================")
    print("Standard Build Projects")
    print("")
    for project_dir, std_project_dir in get_std_project_dirs(root_project_dir):
        project_name = os.path.basename(std_project_dir)
        if child_projects and project_name not in child_projects:
            continue
        print("======================================================================")
        print(f":: {project_name} ::")
        partial_code = build_std_project_dir(project_dir, std_project_dir)
        if partial_code != 0:
            print(f":: {project_name} failed: {partial_code} ::")
        total_code += partial_code

    print("")
    print("_._._._._._._._._._._.__._._._._._._._._._._._._._._._._._._._._._._")
    print(f"Final build result: {'PASS' if total_code <= 0 else 'FAIL'} ({total_code})")
    return total_code


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: build.py (dir of `projects`) [child dirs]")
        sys.exit(1)
    sys.exit(main(sys.argv[1], sys.argv[2:]))
