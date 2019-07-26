
"""
Finds the extension and its dependencies.

This is a kind of
[Constraint Satisfaction Problem](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem)

For this discussion, I'll call extensions by a capital letter, with a version
number beside it.  Version ranges in Petronia only allow for an absolute
minimum and an optional open maximum, but for this discussion I'll refer to
exact values in the form `A[0,1,2]` to mean either A0, A1, or A2 as acceptable
choices.

The usual case is a simple directed acyclic graph, where extension A depends
on extension B and so on.  The difficulty comes with supporting a range of
versions, and different versions have conflicting requirements.

Here's an example of the complexity.

* A1 depends on B[1,2] and C[1,2]
* B1 depends on D[1,2]
* B2 depends on D2 and E1
* C1 depends on D1
* C2 depends on D2 and E2

A1 cannot depend on both B2 and C2 at the same time, because they conflict on
E1 and E2.  So the algorithm can choose either B1+C1+D1 or B1+C2+D2+E2.  The
algorithm will prefer higher versions over lower versions.  However, there are
situations where no choice is overall "higher" than others.
"""

from typing import Sequence, List, Tuple, Dict, Set, Union, Optional, Iterable
from petronia3.errors import (
    PetroniaExtensionNotFound,
    PetroniaCyclicExtensionDependency,
    PetroniaNoCompatibleExtensionFound,
)
from petronia3.util.memory import STRING_EMPTY_TUPLE
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
    __slots__ = ('versions', 'discovered', 'loader', 'only_secure')
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


# This web has inter-depdencies crossing, which isn't right.  See the
# notes below.  That is to say, THIS STRUCTURE DOESN'T WORK.
DependencyWeb = Dict[str, Dict[SecureExtensionVersion, 'DependencyTree']]

class DependencyTree:
    """
    The tree of dependent versions for an extension.
    """
    __slots__ = ('ext', 'deps',)
    def __init__(self, ext: DiscoveredExtension, deps: DependencyWeb) -> None:
        self.ext = ext
        self.deps = deps


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

    # The request asks to find the highest version of each dependency,
    # but only for the necessary dependencies.  This requires searching
    # a web of dependencies to first find the ones that work, then
    # to find the highest version of those.

    # This requires a recursive check into each dependency to find its
    # versions and each of those's dependencies.  Dependencies with
    # no versions are culled from the tree of possibilities.

    # Because zip support (and thus versioning) isn't supported yet,
    # any extension with more than one version causes an error.  Once zips are
    # supported, this will need to be properly implemented.

    compatible_versions: Dict[str, Set[SecureExtensionVersion]] = {}
    web: DependencyWeb = {}
    cache = DependencyCache(loader, only_secure)

    # Depth-first search
    visiting: Set[str] = set()
    visited: Set[str] = set()
    stack: List[Tuple[int, str]] = []

    for ext in extensions:
        trees = _find_compatible_trees(ext, web, cache)
        compatible_versions[ext.name] = set(trees.keys())
        stack.append((0, ext.name,))

    # At this point, the web is fully formed for the extent that
    # we care about the input extension compatibility list.

    order: List[str] = []

    # The "compatible_verions" list maintains the list of current
    # compatible versions that are left available.  If any entry is
    # both in the order list and empty in the compatible_versions,
    # then there is a conflict.  This is NOT CORRECT BEHAVIOR FOR ZIPS
    # because one combination of versions may not work while another
    # combination does.  The "compatible_versions" ONLY WORKS for
    # combination of sub-tree children, not as a global tree thing.

    while stack:
        # "visit" method.
        state, ext_name = stack.pop()
        if state == 0:
            if ext_name in visited:
                continue
            if ext_name in visiting:
                raise PetroniaCyclicExtensionDependency(
                    ext_name,
                    tuple(visiting),
                    STRING_EMPTY_TUPLE
                )
            visiting.add(ext_name)

            # Perform the primary visit operation

            # Yeah, this isn't right.
            if ext_name not in compatible_versions:
                compatible_versions[ext_name] = set(web[ext_name].keys())
            elif ext_name in web:
                compatible_versions[ext_name].intersection_update(web[ext_name].keys())

            # Visit outself again, in the second half, after
            # visiting all the children.
            stack.append((1, ext_name,))

            # Visit all the children.
            ext_found = False
            for version, tree in web[ext_name].items():
                if version in compatible_versions[ext_name]:
                    ext_found = True
                    for dep_name in tree.deps.keys():
                        stack.append((0, dep_name,))
            if not ext_found:
                raise PetroniaNoCompatibleExtensionFound(
                    ext_name,
                    tuple(visiting.union(visited))
                )
        elif state == 1:
            # Finished visiting node.
            visiting.remove(ext_name)
            visited.add(ext_name)
            order.insert(0, ext_name)

    order.reverse()
    ret: List[DiscoveredExtension] = []
    for ext_name in order:
        highest = _find_highest_version(compatible_versions[ext_name], only_secure)
        if not highest:
            raise PetroniaNoCompatibleExtensionFound(
                ext_name,
                tuple(visited)
            )
        disc = cache.get_discovered_version(ext_name, highest)
        if not disc:
            raise PetroniaNoCompatibleExtensionFound(
                ext_name,
                tuple(visited)
            )
        ret.append(disc)

    return ret


def _find_compatible_trees(
        compat: ExtensionCompatibility,
        complete_web: DependencyWeb,
        cache: DependencyCache
) -> Dict[SecureExtensionVersion, DependencyTree]:
    ret: Dict[SecureExtensionVersion, DependencyTree] = {}
    for dep in cache.get_compatible_versions_for(compat):
        disc = cache.get_discovered_version(compat.name, dep)
        if disc:
            ret[dep] = _find_dependency_tree(disc, complete_web, cache)
    return ret


def _find_dependency_tree(
        extension: DiscoveredExtension,
        complete_web: DependencyWeb,
        cache: DependencyCache
) -> DependencyTree:
    """
    Find the complete tree of dependencies.  This will fill up the
    `complete_web` structure as it searches.  It returns a dependency
    tree for each valid compatible version.

    Any discovered cycles will raise the corresponding error.
    """
    visiting: Set[Tuple[str, SecureExtensionVersion]] = set()
    stack: List[Tuple[int, DiscoveredExtension]] = [(0, extension,)]

    while stack:
        state, next_ext = stack.pop()
        if state == 0:
            # Load up the children after the current node.
            stack.append((1, next_ext,))
            for child in next_ext.depends_on:
                found = False
                for dep in cache.get_compatible_versions_for(child):
                    disc = cache.get_discovered_version(child.name, dep)
                    if disc:
                        vtg = (child.name, dep,)
                        if vtg in visiting:
                            raise PetroniaCyclicExtensionDependency(
                                child.name,
                                map(lambda x: x[0], visiting), # type: ignore
                                STRING_EMPTY_TUPLE
                            )
                        visiting.add(vtg)
                        found = True
                        stack.append((0, disc))
                if not found:
                    raise PetroniaExtensionNotFound(
                        child.name,
                        STRING_EMPTY_TUPLE
                    )
        elif state == 1:
            vtg = (next_ext.name, next_ext.secure_version,)
            visiting.remove(vtg)
            deps: DependencyWeb = {}
            for child in next_ext.depends_on:
                for dep in cache.get_compatible_versions_for(child):
                    if child.name not in deps:
                        deps[child.name] = {}
                    deps[child.name][dep] = complete_web[child.name][dep]
            if next_ext.name not in complete_web:
                complete_web[next_ext.name] = {}
            complete_web[next_ext.name][next_ext.secure_version] = DependencyTree(next_ext, deps)

    return complete_web[extension.name][extension.secure_version]


def _find_highest_version(
        versions: Union[Sequence[SecureExtensionVersion], Set[SecureExtensionVersion]],
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
