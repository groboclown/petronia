#!/bin/env /usr/bin/python3

"""
Runs the CI build.  This should be as simple as possible while being useful.
"""

from typing import Dict, List, Tuple, Set
import os
import sys
import shutil
import subprocess

# Bump back up after initial good build.
# MINIMUM_COVERAGE_PERCENT = 99
MINIMUM_COVERAGE_PERCENT = 75

SPECIAL_EXTENDED_PATHS = {
    'py-common-lib': [],
    'foreman': ['py-common-lib', 'py-extension-lib'],  # see the to-do document.
    'py-extension-lib': ['py-common-lib'],
    'other': ['py-common-lib', 'py-extension-lib'],
}

OS_PREFIX = (
    '.win-' if sys.platform == 'win32' else
    '.linux-' if sys.platform in ('linux', 'linux2') else
    '.osx-'
)

IGNORED_OS_NAMES = (
    ('_x11', '_wayland', '_osx') if sys.platform == 'win32' else
    ('_windows', '_osx') if sys.platform in ('linux', 'linux2') else
    ('_windows', '_x11', '_wayland')
)


def is_project_dir_item_included(fqn: str, name: str) -> bool:
    """Is the project directory's item (found by os.listdir) included in package search?"""
    if len(name) <= 0 or '.' in name or name[0] == '_':
        return False
    for ignored in IGNORED_OS_NAMES:
        if name.endswith(ignored):
            return False
    return os.path.isdir(fqn)


def build_std_project_dir(root_project_dir: str, project_dir: str) -> List[str]:
    setup_project_for_platform(project_dir)
    top_package_names: List[str] = []
    mypy_args: List[str] = ['--warn-unused-configs', '--no-incremental']
    lint_dirs: List[str] = []
    for name in os.listdir(project_dir):
        fqn = os.path.join(project_dir, name)
        if is_project_dir_item_included(fqn, name):
            top_package_names.append(name)
            mypy_args.append('--package')
            mypy_args.append(name)
            lint_dirs.append(fqn)
    # print(f"   checking packages {', '.join(top_package_names)}")

    extra_path: List[str] = []
    if project_dir.endswith('-tests'):
        # special case for top-level testing projects that require cross-project path.
        for dirname in os.listdir(root_project_dir):
            fqn = os.path.join(root_project_dir, dirname)
            if fqn not in extra_path and os.path.isdir(fqn):
                extra_path.append(fqn)
    elif os.path.dirname(project_dir) in SPECIAL_EXTENDED_PATHS:
        extra_path.extend([
            os.path.join(root_project_dir, p)
            for p in SPECIAL_EXTENDED_PATHS[os.path.dirname(project_dir)]
        ])
    else:
        extra_path.extend([
            os.path.join(root_project_dir, p)
            for p in SPECIAL_EXTENDED_PATHS['other']
        ])

    print("")
    print("----------------------------------------------------------------------")
    print("Type Checking...")
    mypy_code = run_python_cmd(
        project_dir,
        extra_path,
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
        extra_path,
        'pylint',
        [
            # New to pylint 2.7.2: petronia_extension_tools has a plugin that runs while the lint
            # is running on the same project.  In that case, we need to explicitly add the
            # directory to the sys path.  This needs to happen even if extension tools is already on
            # the PYTHONPATH.  So now we just use this instead of putting it on the path.
            f'--init-hook=sys.path.append("'
            f'{os.path.abspath(os.path.join(root_project_dir, "extension-tools"))}'
            f'")',

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

    # Discovery can only have a single start search directory,
    # so break this up into multiple runs.

    # This means we need to have coverage append, but don't bring in
    # old coverage numbers from before this run.
    if os.path.isfile(os.path.join(project_dir, '.coverage')):
        os.unlink(os.path.join(project_dir, '.coverage'))
    test_code = 0
    for start_pkg_name in top_package_names:
        test_code += run_python_cmd(
            project_dir,
            [
                *extra_path,
            ],
            'coverage',
            [
                'run', '--append', '--timid',
                '--source', ','.join(top_package_names),
                # We are daring...
                '--branch',
                '-m', 'unittest', 'discover', '--buffer',
                '--top-level-directory', project_dir,
                '--start-directory', start_pkg_name,
                '-p', '*_test.py',
            ],
            True,
        )
    if test_code != 0:
        print(f"Unit test FAILED: exit code {test_code}")
        failed.append('unit tests')
    else:
        print("Unit tests PASS")

    # This encounters the error:
    # AttributeError: 'Coverage' object has no attribute 'get_json_data'
    # So programmatic access is used instead.
    report_code = run_python_cmd(
        project_dir,
        [],
        'coverage',
        ['report', '-m', '--fail-under', str(MINIMUM_COVERAGE_PERCENT)],
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
    root_compiled_dir = os.path.join(project_dir, 'compiled')
    compiled_dir = os.path.join(root_compiled_dir, 'translations')
    if os.path.isdir(root_compiled_dir):
        shutil.rmtree(root_compiled_dir, ignore_errors=True)
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
    # print(f"Running {cmd}")
    # print(f" - cwd: {cwd}")
    # print(f" - path: {env}")
    result = subprocess.run(
        cmd,
        cwd=cwd,
        env=env,
    )
    if fail_on_nonzero:
        return result.returncode
    return 0


PROJECT_BUILD_FILES = (
    '.coveragerc', 'mypy.ini', 'pylintrc',
)


def setup_project_for_platform(project_dir: str) -> None:
    """Setup a project directory for running a build, changing the structure
    based on the platform-specific config files."""
    replaced = False
    for build_file in PROJECT_BUILD_FILES:
        os_build_file = os.path.join(project_dir, OS_PREFIX + build_file)
        if os.path.isfile(os_build_file):
            real_file = os.path.join(project_dir, build_file)
            if os.path.isfile(real_file):
                os.unlink(real_file)
            shutil.copy(os_build_file, real_file)
            replaced = True
    if replaced:
        print(f"(Prepared project's build environment for {sys.platform})")


PRIORITY_PROJECTS = ('py-common-lib', 'extension-tools', 'py-extension-lib')
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


def normalize_child_project_names(child_projects: List[str]) -> List[str]:
    """Normalize the names; if it's a directory, strip off all the stuff but the name."""
    ret: List[str] = []
    for name in child_projects:
        while name[-1] == '/':
            name = name[:-1]
        if os.path.isdir(name):
            ret.append(os.path.basename(name))
        else:
            ret.append(name)
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
        normalize_child_project_names(sys.argv[1:]),
    ))
