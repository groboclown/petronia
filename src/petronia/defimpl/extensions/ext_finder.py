
"""
Finds the extension and its dependencies.

The details of this are in the document folder.
"""

from typing import Sequence, List, Tuple, Dict, Set, Optional, Iterable
from ...errors import (
    PetroniaExtensionNotFound,
    PetroniaNoCompatibleExtensionFound,
)
from ...base import (
    TRACE, DEBUG, log
)
from .defs import (
    SecureExtensionVersion,
    ExtensionLoader,
    ExtensionCompatibility,
    DiscoveredExtension,
    compare_version,
    ANY_VERSION,
    SECURE_ANY_VERSION,
    INSECURE_ANY_VERSION,
)


class DependencyCache:
    """Cache of dependencies."""
    __slots__ = ('versions', 'discovered', 'loader', 'only_secure',)
    versions: Dict[str, List[SecureExtensionVersion]]
    discovered: Dict[str, Dict[SecureExtensionVersion, Optional[DiscoveredExtension]]]

    def __init__(
            self,
            loader: ExtensionLoader,
            only_secure: bool
    ) -> None:
        self.only_secure = only_secure
        self.loader = loader
        self.versions = {}
        self.discovered = {}

    def get_versions_for(self, name: str) -> Sequence[SecureExtensionVersion]:
        """Get the cached versions, or load the cache, for the extension name."""
        if name not in self.versions:
            self.versions[name] = []
            for version in self.loader.find_versions(name):
                assert isinstance(version[0], bool), name
                assert isinstance(version[1], tuple), name
                if not self.only_secure or version[0]:
                    self.versions[name].append(version)
        return tuple(self.versions[name])

    def get_compatible_versions_for(
            self, ext: ExtensionCompatibility
    ) -> Sequence[SecureExtensionVersion]:
        """
        Get all versions compatible with the argument.
        """
        compats: List[SecureExtensionVersion] = []
        versions = self.get_versions_for(ext.name)
        for version in versions:
            if not self.only_secure or version[0]:
                if ext.is_compatible_with(version[1]):
                    compats.append(version)
        return compats

    def get_discovered_version(
            self,
            name: str,
            version: SecureExtensionVersion
    ) -> Optional[DiscoveredExtension]:
        """Get the discovered extension (if it exists).  It correctly checks
        for ANY_VERSION in either the request or the available extensions."""
        if self.only_secure and not version[0]:
            # Only secure versions are allowed, and the requested version isn't secure.
            return None
        if name not in self.discovered:
            self.discovered[name] = {}
        desc = self.discovered[name]

        # Because we maintain a "None" value in the discovered list,
        # we don't go through the effort of retrying an extension that is known
        # to not exist.
        if version not in desc:
            desc[version] = self.loader.find_extension(self.only_secure, name, version[1])
        if desc[version]:
            return desc[version]

        # This most likely has an edge case issue.

        # Check for any version being registered.
        if SECURE_ANY_VERSION not in desc:
            desc[SECURE_ANY_VERSION] = self.loader.find_extension(
                self.only_secure, name, version[1]
            )
        if SECURE_ANY_VERSION in desc and desc[SECURE_ANY_VERSION] is not None:
            return desc[SECURE_ANY_VERSION]

        if not self.only_secure:
            if INSECURE_ANY_VERSION not in desc:
                desc[INSECURE_ANY_VERSION] = self.loader.find_extension(
                    self.only_secure, name, version[1]
                )
            if INSECURE_ANY_VERSION in desc and desc[INSECURE_ANY_VERSION] is not None:
                return desc[INSECURE_ANY_VERSION]

        # Check if the user is requesting any version.
        if version[1] is ANY_VERSION:
            versions = self.get_versions_for(name)
            highest = _find_highest_version(versions, self.only_secure or version[0])
            if highest:
                if highest not in desc:
                    desc[highest] = self.loader.find_extension(self.only_secure, name, highest[1])
                return desc[highest]

        return None


_ExtensionVersion = Tuple[str, SecureExtensionVersion]
_VersionMap = Dict[str, SecureExtensionVersion]
_AllowedVersionsMap = Dict[str, Set[SecureExtensionVersion]]


def find_extensions(
        extensions: Iterable[ExtensionCompatibility],
        loader: ExtensionLoader,
        only_secure: bool
) -> Sequence[DiscoveredExtension]:
    """
    Finds a compatible extension and all of its dependencies.  Returns the
    found extension.  Will raise a PetroniaExtensionLoadError on any problems.

    This does not do any checking for already loaded extensions.  Those must
    be excluded after calling here.
    """

    log(
        DEBUG,
        find_extensions,
        "Finding extension dependencies for {0}",
        extensions
    )

    cache = DependencyCache(loader, only_secure)

    # 1. Set `H` to an empty stack. Set `C` to an empty map which will map an extension
    #    name to a version.  Set `A` to the children groups of the root node (each group is the
    #    collection of versions to choose for a single extension).  Set `C'` to a null value.

    match: _VersionMap = {}
    order: List[str] = []

    # C'
    override_match: Optional[_VersionMap] = None
    override_order: List[str] = []

    # H - stack entry: #0 == A, #1 == C
    # 2. Push a copy of `C` and `A` onto the stack `H`.
    search_stack: List[Tuple[_AllowedVersionsMap, _VersionMap, List[str]]] = [
        (_find_all_compatible(cache, extensions), dict(match), list(order),)
    ]

    # 3. If `H` is empty, then we're done searching
    while search_stack:
        # 4. Pop the top item from `H` and assign the popped values to `C`
        # (map), and `A` (remaining children groups).
        remaining_groups, match, order = search_stack.pop()

        log(
            TRACE,
            find_extensions,
            "Start search loop iteration\n"
            " - remaining groups: {0}\n"
            " - current match: {1}\n"
            " - load order: {2}",
            remaining_groups, match, order
        )

        # 5. If `C'` is not null, then assign `C` to `C'` (not a copy!), then
        # set `C'` to null.
        if override_match is not None:
            match = override_match
            override_match = None
            order = override_order
            override_order = []
            log(
                TRACE,
                find_extensions,
                " - override with match {0}; order {1}",
                match, order
            )

        # (6 + 7 implies a loop over the remaining groups)
        # 7. Remove a group from `A` and assign it to `N`.
        # 8. Set `P` to the list of versions in `N`.
        log(TRACE, find_extensions, "Looping over groups.")
        loop_groups = dict(remaining_groups)
        for group_extension, group_versions in loop_groups.items():
            # 7. Remove a group from `A` and assign it to `N`.
            del remaining_groups[group_extension]
            log(
                TRACE, find_extensions,
                "Trying group {0} versions {1}",
                group_extension, group_versions
            )

            # (9 + 10 implies a loop over group versions)
            loop_group_continue = False
            loop_group_break = False
            while group_versions:
                # 10. Use `f` to remove an item from `P` and assign it to `Q`.
                highest = _find_highest_version(group_versions, only_secure)
                if highest:
                    group_versions.remove(highest)
                    log(
                        TRACE, find_extensions,
                        "Trying next highest vesrion {0}",
                        highest
                    )
                else:
                    # 9. If `P` is empty, then no version could be selected, and this is
                    # an invalid path.  Go back to 3.
                    log(TRACE, find_extensions, "No more versions to try.")
                    loop_group_break = True
                    break

                if group_extension in match:
                    # 11. If there is a `N` in `C` with the same version as
                    # `Q`, then it's already been added to the list, so go
                    # back to 6.
                    if _match_version_is(match[group_extension], highest):
                        # GOTO 6...
                        log(TRACE, find_extensions, "Already added this to our match list.")
                        loop_group_continue = True
                        break

                    # 12. If there is an `N` in `C` with a different version
                    # than `Q`, then it's a conflict.  Go back to 9.
                    log(TRACE, find_extensions, "Metch conflict.  Trying another one.")
                else:
                    # 13. We now have a choice for `N`.  Set `N` in `C` with
                    # version `Q`.  Go back to 2.
                    log(
                        TRACE, find_extensions,
                        "Going to try {0} at version {1}",
                        group_extension, highest
                    )
                    match[group_extension] = highest
                    order.insert(0, group_extension)
                    new_remaining_groups = _find_dependency_compatiblity(
                        cache, group_extension, highest
                    )
                    new_remaining_groups.update(remaining_groups)
                    search_stack.append((
                        new_remaining_groups,
                        dict(match),
                        list(order),
                    ))
                    loop_group_break = True
                    break

            # (11 ... go back to 6)
            if loop_group_continue:
                continue

            # (13 ... go back to 2)
            if loop_group_break:
                break

        # 6. If `A` is empty, then this node was successfully searched.
        # Set `C'` to `C` (not a copy!) and go back to 3.
        override_match = match
        override_order = order

    # (3...) if `C` contains all the direct child extension names of the root node,
    # then there is a match; otherwise no compatible search could be made.
    matched_names = set(match.keys())
    required_names = set(map(lambda x: x.name, extensions)) # type: ignore
    found_required_names = required_names.intersection(matched_names)
    log(
        TRACE, find_extensions,
        "Completed search.\n"
        " - Matched: {0}\n"
        " - Required to load: {1}\n"
        " - Found required: {2}",
        match, extensions, found_required_names
    )
    if found_required_names != required_names:
        # TODO may need a different exception.
        raise PetroniaNoCompatibleExtensionFound(
            ', '.join(required_names.difference(found_required_names)),
            found_required_names
        )

    # match is now the right list of dependencies and versions...
    # and order is in reverse order.
    order.reverse()
    ret: List[DiscoveredExtension] = []
    for name in order:
        disc = cache.get_discovered_version(name, match[name])
        assert disc is not None
        ret.append(disc)
    log(DEBUG, find_extensions, "Final load order: {0}", ret)
    return ret


def _find_all_compatible(
        cache: DependencyCache,
        compats: Iterable[ExtensionCompatibility]
) -> _AllowedVersionsMap:
    ret: _AllowedVersionsMap = {}
    for compat in compats:
        ret[compat.name] = set(cache.get_compatible_versions_for(compat))
    return ret


def _find_highest_version(
        versions: Iterable[SecureExtensionVersion],
        only_secure: bool
) -> Optional[SecureExtensionVersion]:
    highest: Optional[SecureExtensionVersion] = None
    for ver in versions:
        if not only_secure or ver[0]:
            if ver[1] is ANY_VERSION:
                return ver
            if highest is None:
                highest = ver
            elif compare_version(ver[1], highest[1]) > 0:
                highest = ver
    return highest

def _find_dependency_compatiblity(
        cache: DependencyCache,
        name: str,
        version: SecureExtensionVersion
) -> _AllowedVersionsMap:
    disc = cache.get_discovered_version(name, version)
    if disc is None:
        raise PetroniaExtensionNotFound(name, [])
    assert disc is not None, "{0} {1}".format(name, version)
    ret = _find_all_compatible(cache, disc.depends_on)
    for imp in disc.implements:
        ret[imp.name] = set(cache.get_compatible_versions_for(imp))
    return ret

def _deep_copy(inp: _VersionMap) -> _VersionMap:
    return dict(inp)

def _match_version_is(
        match_version: SecureExtensionVersion, highest: SecureExtensionVersion
) -> bool:
    if SECURE_ANY_VERSION in (match_version, highest):
        return True
    if INSECURE_ANY_VERSION in (match_version, highest):
        return True
    return match_version == highest
