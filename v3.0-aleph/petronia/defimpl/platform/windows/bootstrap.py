
"""
Start up the Windows system.
"""

import sys
import atexit
from ....aid.std import (
    EventBus,
    PetroniaPlatformNotSupported,
    create_singleton_identity,
)
from ....aid.bootstrap import (
    ANY_VERSION,
)
from ....aid.lifecycle import create_module_listener_helper
from ....base.internal_.internal_extension import petronia_extension
from ....core.shutdown.api import send_system_shutdown_request
from .state import (
    bootstrap_hotkeys,
    bootstrap_display_detection,
    bootstrap_window_discovery,
)

MODULE_ID = create_singleton_identity('default.platform.windows')


def bootstrap_windows_platform(bus: EventBus) -> None:
    import platform
    try:
        from . import connect

        hook = connect.WindowsHookEvent()
        listeners = create_module_listener_helper(bus, MODULE_ID, hook.dispose)

        bootstrap_hotkeys(
            bus, hook, listeners,
            ('meta:super', {},)
        )
        bootstrap_display_detection(bus, listeners, hook)
        bootstrap_window_discovery(bus, listeners, hook)

        hook.start(lambda: send_system_shutdown_request(bus))
        atexit.register(hook.dispose)
    except BaseException as err:
        print(err)
        raise PetroniaPlatformNotSupported(
            '{0} {1}'.format(sys.platform, platform.architecture()[0])
        )


EXTENSION_METADATA = petronia_extension({
    "name": "default.platform.windows",
    "version": (1, 0, 0,),
    "type": "impl",
    "implements": ({
        "extension": "core.platform.api",
        "minimum": ANY_VERSION,
    },),
    "depends": ({
        "extension": "core.state.api",
        "minimum": ANY_VERSION,
    },),
})
