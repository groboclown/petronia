
"""
Sets up the extension.
"""

from .timer import setup_shutdown_handler
from ....aid.simp import (
    EventBus,
)
from ....aid.bootstrap import (
    ANY_VERSION,
    ExtensionMetadataStruct,
)

def bootstrap_shutdown_timer(bus: EventBus) -> None:
    # This is the default time.  Configuration allows changing it.
    setup_shutdown_handler(bus, 5, 120, 5, 120)


EXTENSION_METADATA: ExtensionMetadataStruct = {
    "type": "impl",
    "depends": [],
    "implements": [{
        "extension": "core.shutdown.api",
        "minimum": ANY_VERSION,
    }],
    "authors": ["Petronia"],
}
