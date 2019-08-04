
"""
Load all the core petronia API modules.
"""

from typing import Sequence, List
from petronia3.system.bus import EventBus
from petronia3.errors import PetroniaExtensionNotFound
from petronia3.extensions.extensions.api import (
    ANY_VERSION,
    LoadedExtension,
)
from petronia3.util.memory import EMPTY_TUPLE
from petronia3_ext.extensions.loaders import CoreExtensionLoader

_ORDERED_CORE_EXTENSIONS = (
    'core.shutdown.api',
    'core.state.api',
    'core.extensions.api',
    'core.config_persistence.api',
    'core.timer.api',
    'core.platform.api',
)

def load_core_extensions(
        bus: EventBus
) -> Sequence[LoadedExtension]:
    """
    Load the usual required core modules.  This must be the first set of
    extensions loaded by the system.
    """
    loader = CoreExtensionLoader()
    ret: List[LoadedExtension] = []
    for name in _ORDERED_CORE_EXTENSIONS:
        disc = loader.find_extension(True, name, ANY_VERSION)
        if not disc:
            raise PetroniaExtensionNotFound(
                name,
                EMPTY_TUPLE # type: ignore
            )
        disc.module_loader(bus)
        ret.append(LoadedExtension(name, disc.is_secure, disc.version))
    return tuple(ret)
