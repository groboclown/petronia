
"""
Details on finding and loading the right platform.  This does not add the
platform to the event bus, because that requires the extensions loader, but
the extensions loader has dependencies on aspects of the platform.
"""

import os
import sys
import importlib
from types import ModuleType
from petronia3.errors import PetroniaPlatformNotSupported
from petronia3.system.bus import EventBus
from petronia3.extensions.platform.preboot import (
    DiscoveryFunction,
    DISCOVERY_FUNCTION_NAME,
    RUN_SYSTEM_FUNCTION_NAME,
    PREBOOT_MODULE_NAME,
)


def get_base_platform_module() -> ModuleType:
    """
    Find the module that implements the basic bootstrap implementation.
    """
    plat = sys.platform
    if plat == 'linux' or os.name == 'posix':
        return importlib.import_module('petronia3_root.platform.posix')
    if plat == 'win32':
        return importlib.import_module('petronia3_root.platform.windows')
    raise PetroniaPlatformNotSupported(plat)


def get_user_platform_module(name: str) -> ModuleType:
    """Get the module defined by the user as the preboot platform."""
    return importlib.import_module(name)


def get_platform_discovery_function(base_mod: ModuleType) -> DiscoveryFunction:
    """
    Get the discovery function for the current base platform.
    """
    if not hasattr(base_mod, PREBOOT_MODULE_NAME):
        mod = importlib.import_module(base_mod.__name__ + '.' + PREBOOT_MODULE_NAME)
    else:
        mod = getattr(base_mod, PREBOOT_MODULE_NAME)
    if not hasattr(mod, DISCOVERY_FUNCTION_NAME): # type: ignore
        # TODO better error
        raise Exception('preboot platform {0} does not supply {1}'.format(
            mod.__name__,
            DISCOVERY_FUNCTION_NAME
        ))
    ret = getattr(mod, DISCOVERY_FUNCTION_NAME) # type: ignore
    if not callable(ret): # type: ignore
        # TODO better error
        raise Exception('preboot platform {0} does not supply valid {1}'.format(
            mod.__name__,
            DISCOVERY_FUNCTION_NAME
        ))
    # could inspect it...  But we won't (right now)
    return ret # type: ignore


def run_platform_main(bus: EventBus, base_mod: ModuleType) -> int:
    """Run the platform's run loop."""
    if not hasattr(base_mod, PREBOOT_MODULE_NAME):
        mod = importlib.import_module(base_mod.__name__ + '.' + PREBOOT_MODULE_NAME)
    else:
        mod = getattr(base_mod, PREBOOT_MODULE_NAME)
    if not hasattr(mod, RUN_SYSTEM_FUNCTION_NAME): # type: ignore
        # TODO better error
        raise Exception('preboot platform {0} does not supply {1}'.format(
            mod.__name__,
            RUN_SYSTEM_FUNCTION_NAME
        ))
    ret = getattr(mod, RUN_SYSTEM_FUNCTION_NAME) # type: ignore
    if not callable(ret): # type: ignore
        # TODO better error
        raise Exception('preboot platform {0} does not supply {1}'.format(
            mod.__name__,
            RUN_SYSTEM_FUNCTION_NAME
        ))
    # could inspect it...  But we won't (right now)
    return ret(bus) # type: ignore
