
"""
Start up the layout.
"""

from ....aid.std import (
    EventBus,
)
from ....aid.bootstrap import (
    QUEUE_EVENT_NORMAL,
    register_event,
    ANY_VERSION,
)
from ....aid.lifecycle import (
    create_module_listener_helper,
)
from ....base.internal_.internal_extension import petronia_extension


def bootstrap_layout(bus: EventBus) -> None:
    # TODO register platform listeners

    # TODO register configuration listener

    # TODO register initial state

    # TODO register hotkey types and action listeners

    pass


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
        "extension": "core.hotkeys.api",
        "minimum": ANY_VERSION,
    },),
})
