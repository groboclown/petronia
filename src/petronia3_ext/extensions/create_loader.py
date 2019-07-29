
"""
Setup the loader for the extensions.  This requires adding in additional dependent extensions.
"""

from typing import Iterable, List, Tuple, Optional
from petronia3.system.security import SandboxPermission
from .caches import DirectoryExtensionCache
from .loaders import (
    ExtensionLoader,
    CoreExtensionLoader,
    PathExtensionLoader,
    ZipExtensionLoader,
    CompositeExtensionLoader,
)

def create_core_loader() -> ExtensionLoader:
    """
    Create an extension loader that only loads extensions that are defined
    in the Python path.  All of these loaded extensions are assumed to be
    okay to load and run in the main (loose permissions) execution thread.
    """
    return CoreExtensionLoader()

def create_extension_loader(
        cache_dir: str,
        local_search_dirs: Iterable[Tuple[str, Optional[Iterable[SandboxPermission]]]],
        zip_dirs: Iterable[Tuple[str, Optional[Iterable[SandboxPermission]]]]
) -> ExtensionLoader:
    """
    Creates the loader for the extensions.
    """
    loaders: List[ExtensionLoader] = [
        create_core_loader()
    ]
    cache = DirectoryExtensionCache(cache_dir)
    for dirname, permissions in local_search_dirs:
        if permissions is not None:
            loaders.append(PathExtensionLoader((dirname,), tuple(permissions)))
        else:
            loaders.append(PathExtensionLoader((dirname,), None))
    for dirname, permissions in zip_dirs:
        if permissions is not None:
            loaders.append(ZipExtensionLoader(cache, (dirname,), tuple(permissions)))
        else:
            loaders.append(ZipExtensionLoader(cache, (dirname,), None))
    return CompositeExtensionLoader(loaders)
