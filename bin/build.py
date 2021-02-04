#!/bin/env /usr/bin/python3

"""
Runs the CI build.  This should be as simple as possible while being useful.
"""

from typing import Dict, List, Tuple, Set
import os
import sys
import shutil
import subprocess


def build_std_project_dir(root_project_dir: str, project_dir: str) -> List[str]:
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
        print(f"MyPy FAILED: exit code {mypy_code}")
        return ['mypy']
    print("MyPy PASSED")

    failed: List[str] = []

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
        print(f"Linting FAILED: exit code {lint_code}")
        failed.append('lint')
        # Let unit test run, even if linting failed.
    else:
        print("Linting PASSED")

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
        print(f"Unit test FAILED: exit code {test_code}")
        failed.append('unit tests')
    else:
        print("Unit tests PASS")

    report_code = run_python_cmd(
        project_dir,
        [],
        'coverage',
        ['report', '-m', '--fail-under', '99'],
        True,
    )
    if report_code != 0:
        print(f"Code coverage FAILED: exit code {report_code}")
        failed.append('insufficient code coverage from unit tests')
    else:
        print("Code coverage PASSED")

    print("")
    print("----------------------------------------------------------------------")
    print("Bandit Security Checks...")
    sec_code = run_python_cmd(
        project_dir,
        [],
        'bandit.cli.main',
        ['-r', project_dir],
        True,
    )
    if sec_code != 0:
        print(f"Bandit security check FAILED: exit code {sec_code}")
        failed.append('security inspections')
    else:
        print("Bandit security check PASSED")

    return failed


def build_l10n_project_dir(_root_project_dir: str, project_dir: str) -> List[str]:
    """Compile the .pot files into .mo files."""

    source_dir = os.path.join(project_dir, 'translations')
    compiled_dir = os.path.join(project_dir, 'compiled')
    if os.path.isdir(compiled_dir):
        shutil.rmtree(compiled_dir, ignore_errors=True)
    os.makedirs(compiled_dir, exist_ok=True)

    # project name -> list of (locale, po file)
    project_locales: Dict[str, List[Tuple[str, str]]] = {}

    failures: List[str] = []

    for locale_name in os.listdir(source_dir):
        lcm_dir = os.path.join(source_dir, locale_name, 'LC_MESSAGES')
        if not os.path.isdir(lcm_dir):
            continue
        for po_file in os.listdir(lcm_dir):
            po_fqn = os.path.join(lcm_dir, po_file)
            if not os.path.isfile(po_fqn) or not po_file.endswith('.po'):
                continue
            project_name = po_file[:-3]
            if project_name not in project_locales:
                project_locales[project_name] = []
            project_locales[project_name].append((locale_name, po_fqn))
    for project_name, locale_files in project_locales.items():
        print("")
        print("----------------------------------------------------------------------")
        print(f"Compile {project_name} ...")
        for locale_name, po_fqn in locale_files:
            print(f"  - {locale_name}")
            os.makedirs(os.path.join(compiled_dir, locale_name, 'LC_MESSAGES'), exist_ok=True)
            exit_code = run_python_cmd(
                project_dir, [],
                'babel.messages.frontend',
                [
                    'compile',
                    f'--domain={project_name}',
                    f'--directory={compiled_dir}',
                    f'--locale={locale_name}',
                    f'--input-file={po_fqn}',
                    '--use-fuzzy',
                    '--statistics',
                ],
                True,
            )
            if exit_code != 0:
                failures.append(f'{project_name} localization files for {locale_name}')
    # Petronia uses a special catalog file, too...
    with open(os.path.join(compiled_dir, 'catalog.list'), 'w') as f:
        f.write('\n'.join(project_locales.keys()))

    return failures


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
TRANSLATION_PROJECTS = ('l10n',)


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
    total_failures: List[str] = []
    print("======================================================================")
    print("======================================================================")
    print("Standard Build Projects")
    print("")
    remaining_projects: Set[str] = set(child_projects)
    for project_dir, std_project_dir in get_std_project_dirs(root_project_dir):
        project_name = os.path.basename(std_project_dir)
        if child_projects and project_name not in child_projects:
            continue
        if child_projects:
            remaining_projects.remove(project_name)
        print("======================================================================")
        print(f":: {project_name} ::")
        if project_name in TRANSLATION_PROJECTS:
            partial_code = build_l10n_project_dir(project_dir, std_project_dir)
        else:
            partial_code = build_std_project_dir(project_dir, std_project_dir)
        if partial_code:
            print(f":: {project_name} failed: {partial_code} ::")
        total_failures.extend([
            f'{project_name}: {part}'
            for part in partial_code
        ])

    for project_name in remaining_projects:
        print("======================================================================")
        print(f":: {project_name} ::")
        print(f":: {project_name} failed: Does Not Exist ::")
        total_failures.append(f'{project_name}: does not exist')

    print("")
    print("_._._._._._._._._._._.__._._._._._._._._._._._._._._._._._._._._._._")
    print(f"Final build result: {'FAIL' if total_failures else 'PASS'}")
    if total_failures:
        print(f'  FAILED ' + ('\n  FAILED '.join(total_failures)))
    return len(total_failures)


if __name__ == '__main__':
    sys.exit(main(
        os.path.join(os.path.dirname(sys.argv[0]), os.path.pardir, 'projects'),
        sys.argv[1:],
    ))
