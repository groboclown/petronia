
"""
Loads the extension.
"""

from typing import Sequence, List, Iterable, Collection
from petronia3.system.bus import EventBus
from petronia3.errors import (
    PetroniaExtensionError,
    PetroniaExtensionInitializationError,
)
from .defs import (
    LoadedExtension,
    ExtensionLoader,
    ExtensionCompatibility,
    ANY_VERSION,
)
from .ext_finder import (
    find_extensions,
)

def load_additional_extension(
        extension: str,
        loader: ExtensionLoader,
        bus: EventBus,
        loaded: Collection[LoadedExtension]
) -> Sequence[LoadedExtension]:
    """
    Load another extension into the system, using the best fitting version
    based on the already loaded extensions.

    Will raise exceptions on load issues.
    """
    compat = [ExtensionCompatibility(extension, ANY_VERSION, None)]
    for ext in loaded:
        compat.append(ExtensionCompatibility(ext.name, ext.version, None))
    to_load = find_extensions(compat, loader, False)
    ret: List[LoadedExtension] = []
    for disc in to_load:
        if disc.name in loaded:
            # Already loaded
            continue
        try:
            disc.module_loader(bus)
            ret.append(LoadedExtension(
                disc.name, disc.is_secure, disc.version
            ))
        except PetroniaExtensionError:
            raise
        except BaseException as err: # pylint: disable=broad-except
            raise PetroniaExtensionInitializationError(
                disc.name,
                map(lambda x: x.name, ret), # type: ignore
                err
            )
    return ret



def load_extensions(
        extensions: Iterable[ExtensionCompatibility],
        loader: ExtensionLoader,
        bus: EventBus,
        only_secure: bool
) -> Sequence[LoadedExtension]:
    """
    Load the best fitting extensions.

    Will raise exceptions on load issues.
    """
    to_load = find_extensions(extensions, loader, only_secure)
    ret: List[LoadedExtension] = []
    for ext in to_load:
        try:
            ext.module_loader(bus)
            ret.append(LoadedExtension(
                ext.name, ext.is_secure, ext.version
            ))
        except PetroniaExtensionError:
            raise
        except BaseException as err: # pylint: disable=broad-except
            raise PetroniaExtensionInitializationError(
                ext.name,
                map(lambda x: x.name, ret), # type: ignore
                err
            )
    return ret
