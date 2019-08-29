
"""
Start up the Windows system.
"""

from typing import Optional
import sys
from ....aid.simp import (
    EventBus,
    PetroniaPlatformNotSupported,
)
from ....aid.bootstrap import (
    ExtensionMetadataStruct,
    ANY_VERSION,
)
from ....core.shutdown.api import send_system_shutdown_request
import atexit


def bootstrap_windows_platform(bus: EventBus) -> None:
    import platform
    try:
        from . import connect

        # DEBUG CODE...
        hook = connect.WindowsHookEvent()
        hook.start(lambda: send_system_shutdown_request(bus))
        atexit.register(hook.dispose)
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