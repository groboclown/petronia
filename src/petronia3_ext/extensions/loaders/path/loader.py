
"""
Simple directory path loading.  This supports local development modules or
local unzipped downloads.
"""

import os
import importlib
import importlib.util
import importlib.machinery
from typing import Sequence, List, Optional
from petronia3.util.memory import EMPTY_TUPLE
from ...defs import (
    DiscoveredExtension,
    ExtensionLoader,
    ExtensionVersion,
    SecureExtensionVersion,
    SECURE_ANY_VERSION_SEQ,
    INSECURE_ANY_VERSION_SEQ,
    NO_VERSIONS,
)
from ...util.spec import get_extension_from_module_spec
from ...sandbox import SandboxPermission, create_sandbox_module_loader


class PathExtensionLoader(ExtensionLoader):
    """
    Simple extension loader using a list of paths where Python files are
    located.  They are all lumped together into a single search, and versions
    are ignored.

    If permissions is non-None, then the paths are considered insecure, and
    run in a sandbox with only the granted permissions.  If permissions is
    None, then the paths are considered to be secure, and are run in-memory
    with the current extension loader.
    """
    __slots__ = ('__finder', '_paths', '__secure', '_permissions')
    _paths: Sequence[str]
    _permissions: Sequence[SandboxPermission]

    def __init__(
            self, paths: Sequence[str], permissions: Optional[Sequence[SandboxPermission]]
    ) -> None:
        self.__finder = importlib.machinery.PathFinder()
        self.__secure = permissions is None
        if permissions:
            self._permissions = tuple(permissions)
        else:
            self._permissions = EMPTY_TUPLE
        allowed_paths: List[str] = []
        for path in paths:
            if os.path.isdir(path):
                allowed_paths.append(path)
        self._paths = tuple(allowed_paths)

    def find_versions(self, name: str) -> Sequence[SecureExtensionVersion]:
        # If this is not secure, then we should not load the
        # module into memory.
        if self.__secure:
            mod_spec = self.__finder.find_spec(fullname=name, path=self._paths)
            if mod_spec is not None:
                if self.__secure:
                    return SECURE_ANY_VERSION_SEQ
                return INSECURE_ANY_VERSION_SEQ
            return NO_VERSIONS
        else:
            # Not 100% guaranteed to mean the extension exists, but it's
            # "good enough" for now.
            expect_file = name.replace('.', os.path.sep) + '.py'
            for path in self._paths:
                if os.path.isfile(os.path.join(path, expect_file)):
                    return INSECURE_ANY_VERSION_SEQ
            return NO_VERSIONS


    def find_extension(
            self,
            only_secure: bool,
            name: str,
            version: ExtensionVersion
    ) -> Optional[DiscoveredExtension]:
        if not self.__secure and only_secure:
            # This is not a secure extension loader, but only secure
            # extensions are requested.
            return None

        if self.__secure:
            mod_spec = self.__finder.find_spec(fullname=name, path=self._paths)
            if mod_spec is None:
                return None
            return get_extension_from_module_spec(name, (True, version,), mod_spec, None)

        loader = create_sandbox_module_loader(self._paths, self._permissions)
        # Need to figure out how to find the extension metadata in this situation.
        raise NotImplementedError()
