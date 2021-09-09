
"""
Bootstrap the Wrench theme.
"""

from ....aid.bootstrap import (
    EventBus,
    QUEUE_EVENT_NORMAL,
    register_event,
    ANY_VERSION,
)
from ....base.internal_.internal_extension import petronia_extension


def bootstrap_wrench(bus: EventBus) -> None:
    """
    Setup the theme.
    """
    pass


EXTENSION_METADATA = petronia_extension({
    "name": "default.theme.wrench",
    "version": (1, 0, 0,),

    "type": "impl",
    "implements": ({
       "extension": "core.theme.api",
       "minimum": ANY_VERSION,
    },),
    "depends": ({
        "extension": "core.platform.api",
        "minimum": ANY_VERSION,
    }, {
        "extension": "core.hotkeys.binding",
        "minimum": ANY_VERSION,
    },),
})
