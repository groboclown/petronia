
"""
Loads the extension.
"""

from typing import Sequence, List, Iterable, Collection, Set
from ...base import (
    EventBus,
    INFO, TRACE, log
)
from ...errors import (
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


def load_additional_extensions(
        extensions: Iterable[str],
        loader: ExtensionLoader,
        bus: EventBus,
        loaded: Collection[LoadedExtension]
) -> Sequence[LoadedExtension]:
    """
    Load another extension into the system, using the best fitting version
    based on the already loaded extensions.

    Will raise exceptions on load issues.
    """
    compat: List[ExtensionCompatibility] = []
    loaded_names: Set[str] = set()
    for ext_name in extensions:
        compat.append(ExtensionCompatibility(ext_name, ANY_VERSION, None))
    for ext in loaded:
        loaded_names.add(ext.name)
        compat.append(ExtensionCompatibility(ext.name, ext.version, None))
    to_load = find_extensions(compat, loader, False)
    ret: List[LoadedExtension] = []
    for disc in to_load:
        if disc.name in loaded_names:
            # Already loaded
            continue
        try:
            log(
                INFO, load_additional_extensions,
                "Loading extension {0} v{1}",
                disc.name, disc.version
            )
            log(
                TRACE, load_additional_extensions,
                "Extension loader: {0}",
                disc.module_loader
            )
            disc.module_loader(bus)
            ret.append(LoadedExtension(
                disc.name, disc.is_secure, disc.version
            ))
            loaded_names.add(disc.name)
        except PetroniaExtensionError:
            raise
        except BaseException as err:  # pylint: disable=broad-except
            raise PetroniaExtensionInitializationError(
                disc.name,
                [ext.name for ext in ret],
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
            log(
                INFO, load_extensions,
                "Loading extension {0} v{1}",
                ext.name, ext.version
            )
            ext.module_loader(bus)
            ret.append(LoadedExtension(
                ext.name, ext.is_secure, ext.version
            ))
        except PetroniaExtensionError:
            raise
        except BaseException as err:  # pylint: disable=broad-except
            raise PetroniaExtensionInitializationError(
                ext.name,
                map(lambda x: x.name, ret),  # type: ignore
                err
            )
    return ret
