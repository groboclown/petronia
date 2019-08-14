
"""
Find the configuration files to load.
"""

import os
from typing import Iterable, Set, List, Callable

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
    Find all extension configuration files, recursing into sub-directories if
    requested.
    """
    seen_dirs: Set[str] = set()
    ret: List[str] = []
    for path in paths:
        if recurse:
            for dirpath, _, filenames in os.walk(path, followlinks=True):
                if dirpath in seen_dirs:
                    continue
                seen_dirs.add(dirpath)
                for fnm in filenames:
                    _check_name(dirpath, fnm, name_matcher, ret)
        else:
            for fnm in os.listdir(path):
                _check_name(path, fnm, name_matcher, ret)
    return tuple(ret)


def _check_name(
        path: str, fnm: str, name_matcher: Callable[[str], bool], found: List[str]
) -> None:
    if name_matcher(fnm):
        filename = os.path.join(path, fnm)
        found.append(filename)
