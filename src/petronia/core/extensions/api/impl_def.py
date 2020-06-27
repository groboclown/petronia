
"""
Definitions for implementations.

Because the extension loader implementation has very special requirements for
boot-time loading, this provides the standard definition for these requirements.
"""

from typing import Iterable, Callable
from .defs import LoadedExtension
from ....base.bus import EventBus
from ....core.platform.preboot import SandboxPath


class ExtensionLoaderSetup:
    """Definitions that need to be passed to the extension loader."""
    __slots__ = (
        'secure_paths', 'sandbox_paths', 'secure_zip_dirs', 'sandbox_zip_dirs',
        'preloaded_extensions', 'initial_extension_groups',
        'cache_dir',
    )

    def __init__(
            self,
            secure_paths: Iterable[str],
            sandbox_paths: Iterable[SandboxPath],
            secure_zip_dirs: Iterable[str],
            sandbox_zip_dirs: Iterable[SandboxPath],
            preloaded_extensions: Iterable[LoadedExtension],
            initial_extension_groups: Iterable[Iterable[str]],
            cache_dir: str
    ) -> None:
        self.secure_paths = secure_paths
        self.sandbox_paths = sandbox_paths
        self.secure_zip_dirs = secure_zip_dirs
        self.sandbox_zip_dirs = sandbox_zip_dirs
        self.preloaded_extensions = preloaded_extensions
        self.initial_extension_groups = initial_extension_groups
        self.cache_dir = cache_dir


EXTENSION_LOADER_MODULE_BOOTSTRAP_FUNCTION_NAME = 'bootstrap_extension_loader'
ExtensionLoaderBootstrapFunction = Callable[[EventBus, ExtensionLoaderSetup], None]
