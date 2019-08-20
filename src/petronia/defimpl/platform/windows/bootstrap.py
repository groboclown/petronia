
"""
Start up the Windows system.
"""

import sys
from ....aid.simp import (
    EventBus,
    PetroniaPlatformNotSupported,
)
from ....aid.bootstrap import (
    ExtensionMetadataStruct,
    ANY_VERSION,
)

def bootstrap_windows_platform(bus: EventBus) -> None:
    try:
        import platform
        from . import arch
    except:
        raise PetroniaPlatformNotSupported(
            '{0} {1}'.format(sys.platform, platform.architecture()[0])
        )


EXTENSION_METADATA: ExtensionMetadataStruct = {
    "name": "default.platform.windows",
    "version": (1, 0, 0,),
    "type": "impl",
    "implements": [{
        "extension": "core.platform.api",
        "minimum": ANY_VERSION,
    }],
    "depends": [{
        "extension": "core.state.api",
        "minimum": ANY_VERSION,
    }],
    "authors": ["Petronia"],
}
