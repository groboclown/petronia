
"""
Sets up the extension.
"""

from ....base.bus import (
    EventBus,
    ExtensionMetadataStruct,
)
from .timer import ShutdownTimer

def bootstrap_shutdown_timer(bus: EventBus) -> None:
    # TODO allow for configuring the timer.
    ShutdownTimer(bus, 120, 5)

EXTENSION_METADATA: ExtensionMetadataStruct = {
    "type": "impl",
    "depends": [],
    "authors": ["Petronia"],
}
