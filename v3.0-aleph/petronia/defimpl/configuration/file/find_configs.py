
"""
Find the configuration files to load.
"""

import os
from typing import Iterable, Set, List, Callable
from ....aid.std import (
    log, VERBOSE,
)

_EXT_EXTENSIONS = ('.json', '.yaml', '.yml',)


def find_extension_config_files(
        paths: Iterable[str],
        recurse: bool = False
) -> Iterable[str]:
    """
    Find all configuration files for the extensions.
    """
    return find_files(
        paths,
        lambda filename: os.path.splitext(filename)[1] in _EXT_EXTENSIONS,
        recurse=recurse
    )


def find_files(
        paths: Iterable[str],
        name_matcher: Callable[[str], bool],
        recurse: bool = False
) -> Iterable[str]:
    """
    Find all extension configuration files, searching each sub-directory if
    requested.
    """
    seen_dirs: Set[str] = set()
    ret: List[str] = []
    for path in paths:
        if recurse:
            for dir_path, _, filenames in os.walk(path, followlinks=True):
                if dir_path in seen_dirs:
                    continue
                seen_dirs.add(dir_path)
                for fnm in filenames:
                    _check_name(dir_path, fnm, name_matcher, ret)
        else:
            for fnm in os.listdir(path):
                _check_name(path, fnm, name_matcher, ret)
    log(VERBOSE, find_files, 'Found config files {0}', ret)
    return tuple(ret)


def _check_name(
        path: str, fnm: str, name_matcher: Callable[[str], bool], found: List[str]
) -> None:
    if name_matcher(fnm):
        filename = os.path.join(path, fnm)
        found.append(filename)
