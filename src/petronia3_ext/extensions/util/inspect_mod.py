
"""
Inspect a module for compliance with the API requirements.
"""

from typing import Dict, Optional, Any
from types import ModuleType
from inspect import signature
from petronia3.system.bus import EventBus
from petronia3.system.logging import (
    log,
    NOTICE,
)
from ..defs import ModuleLoader

def get_module_loader(mod: ModuleType) -> Optional[ModuleLoader]:
    """
    Checks if the module is a valid startable type.
    """
    if not hasattr(mod, 'start_extension'):
        return None
    starter = getattr(mod, 'start_extension')
    if not callable(starter):
        log(
            NOTICE,
            get_module_loader,
            'module {0} is not runnable extension; '
            'provided `start_extension` is not a function, but {1}',
            mod.name,
            starter
        )
        return None
    sig = signature(starter)
    if sig.return_annotation is not None:
        log(
            NOTICE,
            get_module_loader,
            'module {0} is not runnable extension; '
            'provided `start_extension` must have signature `(bus: EventBus) -> None`, found {1}',
            mod.name,
            sig
        )
        return None
    ordered_argument_names = tuple(sig.parameters)
    if len(ordered_argument_names) != 1:
        log(
            NOTICE,
            get_module_loader,
            'module {0} is not runnable extension; '
            'provided `start_extension` must have signature `(bus: EventBus) -> None`, found {1}',
            mod.name,
            sig
        )
        return None
    arg_name = ordered_argument_names[0]
    param = sig.parameters[arg_name]
    param_type = param.annotation
    if param_type != EventBus:
        log(
            NOTICE,
            get_module_loader,
            'module {0} is not runnable extension; '
            'provided `start_extension` must have signature `(bus: EventBus) -> None`, found {1}',
            mod.name,
            sig
        )
        return None
    return starter


def get_internal_module_metadata(mod: ModuleType) -> Optional[Dict[str, Any]]:
    """
    Get the internally defined metadata for the module.
    """
    if not hasattr(mod, 'EXTENSION_METADATA'):
        return None
    desc = getattr(mod, 'EXTENSION_METADATA')
    if not isinstance(desc, dict):
        return None
    for key in desc.keys():
        if not isinstance(key, str):
            return None
    return desc
