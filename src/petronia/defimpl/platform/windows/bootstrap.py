
"""
Start up the Windows system.
"""

from typing import Optional
import sys
from ....aid.std import (
    EventBus,
    PetroniaPlatformNotSupported,
)
from ....aid.bootstrap import (
    ExtensionMetadataStruct,
    ANY_VERSION,
)
from ....core.shutdown.api import send_system_shutdown_request
from .state import (
    bootstrap_hotkeys,
    bootstrap_display_detection,
    bootstrap_window_discovery,
)
import atexit


def bootstrap_windows_platform(bus: EventBus) -> None:
    import platform
    try:
        from . import connect

        # DEBUG CODE...
        hotkeys = {
            'f1': 'Pressed Super+f1',
            'ctrl+f1': 'Pressed Super+Ctrl+f1'
        }
        hook = connect.WindowsHookEvent()
        bootstrap_hotkeys(
            bus, hook,
            ('meta:super', hotkeys,)
        )

        bootstrap_display_detection(bus, hook)
        bootstrap_window_discovery(bus, hook)
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
