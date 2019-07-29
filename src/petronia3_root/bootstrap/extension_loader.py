
"""
Create the extension loader.
"""

import os
from typing import List, Tuple, Iterable, Optional
from petronia3.system.bus import EventBus
from petronia3.system.security import SandboxPermission
from petronia3.extensions.extensions import LoadedExtension
from petronia3.extensions.platform.preboot import DiscoveryData
from petronia3_ext.extensions.bootstrap import bootstrap_extension_loader as _bootstrap_extension_loader
from petronia3_ext.extensions.create_loader import create_extension_loader as _mk_ext_loader
from .args import UserArguments

def bootstrap_extension_extension(
        bus: EventBus, data: DiscoveryData,
        args: UserArguments,
        already_loaded_extensions: Iterable[LoadedExtension]
) -> None:
    """
    Create the extension loader and register it to the event bus.
    """
    local: List[Tuple[str, Optional[Iterable[SandboxPermission]]]] = []
    zips: List[Tuple[str, Optional[Iterable[SandboxPermission]]]] = []
    for path in data.ext_paths.secure_paths:
        local.append((path, None,))
    for spath in data.ext_paths.sandbox_paths:
        local.append((spath[0], spath[1],))
    for path in data.ext_paths.secure_zip_dirs:
        zips.append((path, None,))
    for spath in data.ext_paths.sandbox_zip_dirs:
        zips.append((spath[0], spath[1],))
    cache_dir = os.path.join(data.temp_dir, 'extension-cache')
    if not os.path.isdir(cache_dir):
        os.mkdir(cache_dir)
    loader = _mk_ext_loader(
        cache_dir,
        local, zips
    )
    _bootstrap_extension_loader(
        bus,
        already_loaded_extensions,

        # If at least one of these require "only secure", then that's the way
        # it will be.
        args.only_secure or data.only_secure,

        loader
    )
