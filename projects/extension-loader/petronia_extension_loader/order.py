"""
Finds the load order.

This must take care to handle the dependency diamond scenario:

      D
     /  \\
    B   C
     \\ /
      A

If A depends on B & C, but B & C each depend on D, then the load order must
be D, (B + C), A, where B and C can load in parallel once D is loaded.
"""

from typing import Iterable, Sequence, List, Dict, Mapping, Set, Optional
from petronia_common.extension.config import (
    ApiExtensionMetadata, ImplExtensionMetadata, ProtocolExtensionMetadata,
)
from petronia_common.extension.config.extension_schema import ExtensionDependency
from petronia_common.util import StdRet, UserMessage, join_errors, RET_OK_NONE, not_none
from petronia_common.util import i18n as _
from .search import find_best_extension, find_dependencies
from .defs import ExtensionInfo, TRANSLATION_CATALOG


class ExtensionDependencyOrder:
    """A container for an extension information and all of the extensions
    that depend upon it to be loaded, and all the extensions it requires to
    be loaded first.  This only stores the immediate dependencies and
    requirements."""
    __slots__ = ('depends_on', 'required_by', 'ext')

    def __init__(
            self,
            ext: ExtensionInfo,
            depends_on: List[ExtensionInfo],
            required_by: List[ExtensionInfo],
    ) -> None:
        self.ext = ext
        self.depends_on = list(depends_on)
        self.required_by = required_by

    def is_root(self) -> bool:
        """Is this a root dependency?"""
        return len(self.depends_on) <= 0

    def get_ext_dependencies(self) -> List[ExtensionDependency]:
        """Get the metadata's defined extension dependencies."""
        metadata = self.ext.metadata
        ret = list(metadata.depends_on)
        if isinstance(metadata, ImplExtensionMetadata):
            ret.extend(metadata.implements)
        return ret

    def get_everything_requiring(
            self, world: Mapping[str, 'ExtensionDependencyOrder'],
    ) -> Iterable[ExtensionInfo]:
        """Get all the extensions that depend upon this extension."""
        required_by: Dict[str, ExtensionInfo] = {}
        stack: List[ExtensionDependencyOrder] = [self]
        found: Set[str] = set()

        while stack:
            order = not_none(stack.pop())
            for requires in order.required_by:
                if requires.name in found:
                    continue
                found.add(requires.name)
                req_order = world.get(requires.name)
                if req_order:
                    required_by[requires.name] = requires
                    stack.append(req_order)
        return required_by.values()

    def can_run(self, loaded_extensions: Iterable[ExtensionInfo]) -> bool:
        """Can this dependency run yet?  Only runnable if the depends are all loaded."""

        # Early out check.
        if self.is_root():
            return True
        remaining = {
            ext.name
            for ext in self.depends_on
        }

        for ext in loaded_extensions:
            if ext.name in remaining:
                remaining.remove(ext.name)
                # Early out check.
                if not remaining:
                    return True

        # At this point, because of the early-out check + initial root check,
        # this can only mean there are more remaining items.
        return False


def get_load_order(  # pylint:disable=too-many-locals,too-many-nested-blocks,too-many-branches
        extensions: Iterable[ExtensionInfo], installed: Iterable[ExtensionInfo],
) -> StdRet[Sequence[ExtensionDependencyOrder]]:
    """This gathers all the dependent extensions needed to be loaded.  If an implementation
    must be added because the API is requested to be loaded but the implementation of that
    API is not explicitly listed, then it is added.

    The order is intended to be in a format that allows for parallel loading of the
    extensions.

    This ignores cycles in the dependency ordering.

    Note: THIS DOES NOT ENSURE THAT ONE AND ONLY ONE API IMPLEMENTATION IS LOADED.
    """

    # This ends up performing a topological sort, so that API and implementations can be handled
    # nicely.

    errors: List[UserMessage] = []

    visited: Dict[str, bool] = {}
    order: Dict[str, ExtensionDependencyOrder] = {}
    # APIs requested to be loaded...
    apis: Dict[str, ApiExtensionMetadata] = {}
    # The API -> implementation name for explicitly discovered ones.
    implementations: Dict[str, str] = {}
    visit_list: List[ExtensionInfo] = list(extensions)

    # First pass: discover all extensions that need to be loaded.

    while visit_list:
        ext = not_none(visit_list.pop())
        visited[ext.name] = True

        # Enforce the has-dependency check.
        mtd = ext.metadata
        if mtd.extension_type == 'api' and isinstance(mtd, ApiExtensionMetadata):
            apis[ext.name] = mtd
        elif mtd.extension_type == 'impl' and isinstance(mtd, ImplExtensionMetadata):
            for impl_dependency in mtd.implements:
                implementations[impl_dependency.name] = ext.name

        found_dependencies, not_found_dependencies = find_dependencies(ext, installed)
        for dep in not_found_dependencies:
            errors.append(UserMessage(
                TRANSLATION_CATALOG,
                _(
                    'extension {name} depends on not-found extension {dep} '
                    '[>={min_version}, <{max_version}]'
                ),
                name=ext.name,
                dep=dep.name,
                min_version=dep.minimum_version,
                max_version=dep.below_version,
            ))

        for dep_info in found_dependencies:
            if dep_info.name not in visited:
                visit_list.append(dep_info)

        # Put this in the return list.
        # reverse_order.append(ext)
        order[ext.name] = ExtensionDependencyOrder(ext, [], [])

        if not visit_list:
            # End of visiting the list of extensions.  There may be API implementations
            # that need loading.
            for api_name, api in apis.items():
                if api_name not in implementations:
                    # We have a listed API, but no implementation found yet.
                    impl_dep = api.default_implementation
                    if impl_dep:
                        best = find_best_extension(
                            impl_dep.name,
                            impl_dep.minimum_version,
                            impl_dep.below_version,
                            installed,
                        )
                        if not best:
                            errors.append(UserMessage(
                                TRANSLATION_CATALOG,
                                _(
                                    'No implementation declared for API extension {name}, '
                                    'and default extension {default} not installed'
                                ),
                                name=api_name,
                                default=impl_dep.name,
                            ))
                        else:
                            visit_list.append(best)
                    else:
                        # There's cruft left over.
                        errors.append(UserMessage(
                            TRANSLATION_CATALOG,
                            _('No implementation declared for API extension {name}'),
                            name=api_name,
                        ))
            # Re-visit the list, now with no APIs to load.
            # If the visit list is empty at this point, then there's nothing left to load.
            apis.clear()
    if errors:
        return StdRet.pass_error(join_errors(*errors))

    # reverse_order.reverse()
    # return StdRet.pass_ok(reverse_order)

    # Second pass: populate the dependencies and requirements.
    ret: List[ExtensionDependencyOrder] = []
    for ext_order in order.values():
        for ext_dep in ext_order.get_ext_dependencies():
            dep_order = order[ext_dep.name]
            ext_order.depends_on.append(dep_order.ext)
            dep_order.required_by.append(ext_order.ext)
            if dep_order not in ret:
                ret.append(dep_order)

        ret.append(ext_order)
    return StdRet.pass_ok(ret)


class LoadList:
    """
    Maintains a list of pending-to-load extensions that, when loaded, will trigger
    other extensions to load.  If one of them fails to load, then its dependency chain
    will likewise fail.

    This must take care to have deep dependencies be loaded before surface dependencies.

    This class is not thread safe.
    """
    # Any dependency must be in the pending list.
    __slots__ = ('__pending', '__loaded', '__loading',)

    def __init__(self) -> None:
        self.__pending: Dict[str, ExtensionDependencyOrder] = {}
        self.__loaded: Dict[str, ExtensionInfo] = {}
        self.__loading: Dict[str, ExtensionDependencyOrder] = {}

    def mark_loading(self, name: str) -> None:
        """Mark an extension as starting the load process.  It will be excluded from
        queries asking for what's next to load.  This should only be called when
        the extension name is listed in the ready-to-run list."""
        # Assertions are for internal state logic.  If any of these are wrong,
        # then the __pending[name] get will raise an exception anyway.
        assert name not in self.__loading, 'incorrect usage; already loading ' + name  # nosec
        assert name not in self.__loaded, 'incorrect usage; already loaded ' + name  # nosec
        assert name in self.__pending, 'incorrect usage; never added to pending ' + name  # nosec
        order = self.__pending[name]
        del self.__pending[name]
        self.__loading[name] = order

    def mark_loaded(self, name: str) -> StdRet[None]:
        """
        Mark an extension as loaded.  This will put that extension into
        the list of loaded extensions (so it won't be reloaded).  If the
        extension is in any state other than loading, then this will return
        a failure.
        """
        ext = self.__loading.get(name)
        if not ext:
            return StdRet.pass_errmsg(
                TRANSLATION_CATALOG,
                _('Extension {name} is not in loading state, so it should not be marked as loaded'),
                name=name,
            )
        del self.__loading[name]
        self.__loaded[name] = ext.ext
        return RET_OK_NONE

    def mark_failed(self, name: str) -> StdRet[Iterable[ExtensionInfo]]:
        """
        Mark an extension as having failed to load, or a dependency has failed to load.  This
        returns the extensions that should be loaded immediately after that extension has,
        which should then be triggered to fail.
        """
        order = self.__loading.get(name)
        if not order:
            order = self.__pending.get(name)
        if not order:
            return StdRet.pass_errmsg(
                TRANSLATION_CATALOG,
                _('Extension {name} is not in loading state, so it should not be marked as loaded'),
                name=name,
            )
        del self.__loading[name]

        # The failed loading extension must never be required by anything in the
        # loading or loaded state.  So this only needs to check the pending list.
        # Likewise, it can never depend on itself.
        return StdRet.pass_ok(order.get_everything_requiring(self.__pending))

    def get_ready_to_load(self) -> Iterable[ExtensionInfo]:
        """Get the extensions that are ready to be loaded, because all the dependencies
        have finished loading."""
        ret: List[ExtensionInfo] = []
        for order in self.__pending.values():
            if order.can_run(self.__loaded.values()):
                ret.append(order.ext)
        return ret

    def get_loaded(self) -> Iterable[ExtensionInfo]:
        """Get all extensions that have loaded."""
        return tuple(self.__loaded.values())

    def is_loaded(self, name: str) -> bool:
        """Is an extension with this name already loaded?"""
        return name in self.__loaded

    def get_loaded_info(self, name: str) -> Optional[ExtensionInfo]:
        """Get the loaded extension information, or None if not loaded."""
        return self.__loaded.get(name)

    def is_loading(self, name: str) -> bool:
        """Is an extension with this name marked as in the process of loading?"""
        return name in self.__loading

    def is_pending(self, name: str) -> bool:
        """Is an extension with this name marked as needing to be loaded?"""
        return name in self.__pending

    def get_loading_extension(self, name: str) -> Optional[ExtensionInfo]:
        """Find the extension info for the extension marked as loading.  If it
        is not loading or unknown, then None is returned."""
        ret = self.__loading.get(name)
        if ret:
            return ret.ext
        return None

    def add_one_pending(
            self, order: ExtensionDependencyOrder,
    ) -> bool:
        """Add the extension and its dependencies to the pending list.  If the
        extension has already been loaded, then this returns False.  API
        extensions are not explicitly loaded, but instead are just added
        to the loaded list."""
        if (
                self.is_loaded(order.ext.name)
                or self.is_loading(order.ext.name)
                or self.is_pending(order.ext.name)
        ):
            return False
        if isinstance(order.ext.metadata, (ApiExtensionMetadata, ProtocolExtensionMetadata)):
            self.__loaded[order.ext.name] = order.ext
        else:
            self.__pending[order.ext.name] = order
        return True


def add_pending_extensions(
        loader: LoadList,
        extensions: Iterable[ExtensionInfo], installed: Iterable[ExtensionInfo],
) -> StdRet[None]:
    """Uses the get_load_order to find the complete list of extensions to load."""
    load_order_list = get_load_order(extensions, installed)
    if load_order_list.has_error:
        return load_order_list.forward()
    for load_order in load_order_list.result:
        loader.add_one_pending(load_order)
    return RET_OK_NONE
