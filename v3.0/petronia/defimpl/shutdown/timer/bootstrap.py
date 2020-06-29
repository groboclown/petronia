
"""
Sets up the extension.
"""

from .timer import setup_shutdown_handler
from ....aid.bootstrap import (
    EventBus,
    ANY_VERSION,
)
from ....base.internal_.internal_extension import petronia_extension


def bootstrap_shutdown_timer(bus: EventBus) -> None:
    # This is the default time.  Configuration allows changing it.
    setup_shutdown_handler(bus, 5, 120, 5, 120)


EXTENSION_METADATA = petronia_extension({
    "name": "default.shutdown.timer",
    "version": (1, 0, 0),
    "type": "impl",
    "depends": (),
    "implements": ({
        "extension": "core.shutdown.api",
        "minimum": ANY_VERSION,
    },),
})
