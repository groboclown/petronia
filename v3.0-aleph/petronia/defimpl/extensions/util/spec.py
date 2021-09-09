
# This is dealing with introspection of unknown things.
# mypy: allow-any-expr
# mypy: allow-any-explicit
# mypy: allow-any-generics

"""
Loads module information from a module specification.
"""

import importlib.machinery
from typing import Dict, Optional, Any
from ....errors import (
    PetroniaInternalError,
)
from ....base import (
    log,
    logerr,
    ERROR,
    NOTICE,
    TRACE,
    DEBUG,
)
from .inspect_mod import (
    get_module_loader,
    get_internal_module_metadata,
)
from ..defs import (
    DiscoveredExtension,
    SecureExtensionVersion,
)


def get_extension_from_module_spec(
        extension: str,
        version: SecureExtensionVersion,
        mod_spec: importlib.machinery.ModuleSpec,
        description: Optional[Dict[str, Any]]
) -> Optional[DiscoveredExtension]:
    """
    Create a discovered extension object from a module.
    """
    if not mod_spec.loader:
        raise PetroniaInternalError('`loader` not defined on module specification')

    try:
        log(TRACE, get_extension_from_module_spec, 'Loading {0} from spec', mod_spec)
        mod = importlib.util.module_from_spec(mod_spec)

        # MyPy doesn't see the "exec_module" on the loader, but it's there.
        log(TRACE, get_extension_from_module_spec, 'Initializing module')
        mod_spec.loader.exec_module(mod)  # type: ignore

        if not description:
            log(TRACE, get_extension_from_module_spec, 'Finding metadata for module')
            description = get_internal_module_metadata(mod)
            if not description:
                log(
                    NOTICE,
                    get_extension_from_module_spec,
                    'module {0} does not define its own metadata; cannot use it',
                    mod
                )
                return None
            log(TRACE, get_extension_from_module_spec, 'Found metadata for module')

        loader = get_module_loader(mod)
        if not loader:
            log(
                NOTICE,
                get_extension_from_module_spec,
                'module {0} does not define a valid loader; cannot use it',
                mod
            )
            return None

        log(DEBUG, get_extension_from_module_spec, 'Loaded module as extension {0}', extension)
        return DiscoveredExtension(extension, version, description, loader)
    except Exception as err: # pylint: disable=broad-except
        logerr(
            ERROR,
            get_extension_from_module_spec,
            err,
            'problem loading module {0}'.format(mod_spec)
        )
        return None
