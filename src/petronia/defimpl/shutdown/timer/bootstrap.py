
"""
Sets up the extension.
"""

from ....base.bus import (
    EventBus,
    ExtensionMetadataStruct,
)
from .timer import ShutdownTimer
from ....aid.bootstrap import ANY_VERSION

def bootstrap_shutdown_timer(bus: EventBus) -> None:
    # TODO allow for configuring the timer.
    ShutdownTimer(bus, 120, 5)

EXTENSION_METADATA: ExtensionMetadataStruct = {
    "type": "impl",
    "depends": [],
    "implements": [{
        "extension": "core.shutdown.api",
        "minimum": ANY_VERSION,
    }],
    "authors": ["Petronia"],
}
