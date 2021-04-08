
"""
Start up the layout.
"""

from ....aid.std import (
    EventBus,
)
from ....aid.bootstrap import (
    create_singleton_identity,
    ANY_VERSION,
)
from ....aid.lifecycle import (
    create_module_listener_helper,
)
from ....base.internal_.internal_extension import petronia_extension
from .consts import (
    MODULE_ID,
)
from .handler import (
    startup_tile_event_handler,
)


def bootstrap_layout(bus: EventBus) -> None:
    listeners = create_module_listener_helper(bus, MODULE_ID)
    startup_tile_event_handler(bus, listeners)


EXTENSION_METADATA = petronia_extension({
    "name": "default.layout.tile",
    "version": (1, 0, 0,),

    "type": "impl",
    "implements": ({
        "extension": "core.layout.api",
        "minimum": ANY_VERSION,
    },),
    "depends": ({
        "extension": "core.platform.api",
        "minimum": ANY_VERSION,
    }, {
        "extension": "core.state.api",
        "minimum": ANY_VERSION,
    }, {
        "extension": "core.theme.api",
        "minimum": ANY_VERSION,
    }, {
        "extension": "core.layout.binding",
        "minimum": ANY_VERSION,
    },),
})
