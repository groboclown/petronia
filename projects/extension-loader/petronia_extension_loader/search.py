"""
Searches for extensions.
"""

from typing import Sequence, Iterable, List, Tuple, Optional
from petronia_common.extension.config import (
    ExtensionVersion, ExtensionDependency, ImplExtensionMetadata,
)
from petronia_common.util import StdRet
from .defs import ExtensionInfo


def get_extensions_to_load(
        requested: Iterable[ExtensionInfo],
        installed: Iterable[ExtensionInfo],
) -> StdRet[Sequence[ExtensionInfo]]:
    """From the requested extensions, find the dependencies and implementations and
    order them appropriately.  Dependencies must be loaded before the extension
    itself."""
    raise NotImplementedError()


def find_dependencies(
        info: ExtensionInfo,
        installed_extensions: Iterable[ExtensionInfo],
) -> Tuple[Sequence[ExtensionInfo], Iterable[ExtensionDependency]]:
    """Given an extension name with optional version information, find the extension
    and its best-matching direct dependencies.
    This does not perform implementation matching."""
    found: List[ExtensionInfo] = []
    not_found: List[ExtensionDependency] = []
    metadata = info.metadata
    for dep in metadata.depends_on:
        best = find_best_extension(
            dep.name, dep.minimum_version, dep.below_version, installed_extensions,
        )
        if best:
            found.append(best)
        else:
            not_found.append(dep)

    if isinstance(metadata, ImplExtensionMetadata):
        for impl in metadata.implements:
            best = find_best_extension(
                impl.name, impl.minimum_version, impl.below_version, installed_extensions,
            )
            if best:
                found.append(best)
            else:
                not_found.append(impl)

    return found, not_found


def find_best_extension(
        name: str,
        min_version: Optional[ExtensionVersion],
        max_version: Optional[ExtensionVersion],
        installed_extensions: Iterable[ExtensionInfo],
) -> Optional[ExtensionInfo]:
    """Find the highest version of this extension that's within the given parameters.
    If no match is found, then None is returned."""
    best: Optional[ExtensionInfo] = None

    for ext in installed_extensions:
        if ext.name != name:
            continue
        if min_version and is_version_before(ext.version, min_version):
            continue
        if max_version and is_version_after(ext.version, max_version):
            continue
        if not best or is_version_after(ext.version, best.version):
            best = ext

    return best


def is_version_after(first: ExtensionVersion, second: ExtensionVersion) -> bool:
    """Is the first argument a higher number (e.g. more recent) that the second?"""
    if first[0] > second[0]:
        return True
    if first[0] == second[0]:
        if first[1] > second[1]:
            return True
        if first[1] == second[1]:
            if first[2] > second[2]:
                return True
    return False


def is_version_before(first: ExtensionVersion, second: ExtensionVersion) -> bool:
    """Is the first version value before (smaller) than the second?"""
    if first[0] < second[0]:
        return True
    if first[0] == second[0]:
        if first[1] < second[1]:
            return True
        if first[1] == second[1]:
            if first[2] < second[2]:
                return True
    return False
