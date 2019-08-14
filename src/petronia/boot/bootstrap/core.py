
"""
Load all the core petronia API modules.
"""

from typing import Sequence, List
from ...base import (
    EventBus,
)
from ...base.util import (
    EMPTY_TUPLE,
)
from ...errors import PetroniaExtensionNotFound
from ...core.extensions.api import (
    ANY_VERSION,
    LoadedExtension,
)
from ...defimpl.extensions.loaders import CoreExtensionLoader

_ORDERED_CORE_EXTENSIONS = (
    # The absolute bare minimum stuff necessary to get petronia
    # loaded.  More than this causes the default implementations
    # to load, which may need state before boot time.
    'core.shutdown.api',
    'core.state.api',
    'core.extensions.api',
    'core.config_persistence.api',
    'core.timer.api',

    # This must be loaded after the initial list of extensions.
    #'core.platform.api',
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
