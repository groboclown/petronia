
"""
Sets up the platform API.
"""

from ....aid.bootstrap import (
    EventBus,
)
from ....base.internal_.internal_extension import petronia_extension
from ...extensions.api import ANY_VERSION
from .component.bootstrap import (
    register_component_events,
)
from .user_input.bootstrap import (
    register_user_input_events,
)
from .window.bootstrap import (
    register_window_events,
)


def bootstrap_platform_api(bus: EventBus) -> None:
    """
    Register all the events.
    """
    register_component_events(bus)
    register_user_input_events(bus)
    register_window_events(bus)


EXTENSION_METADATA = petronia_extension({
    "name": "core.platform.api",
    "version": (1, 0, 0,),
    "type": "api",
    "depends": ({
        "extension": "core.state.api",
        "minimum": ANY_VERSION,
    },),
    "defaults": ({
        # A non-existent plugin.  Because platform must be included in the
        # bootstrap phase, a real platform that implements this API must also
        # be included, so that this doesn't generate a boot-up error.
        "extension": "default.platform",
        "minimum": ANY_VERSION,
    },),
})
