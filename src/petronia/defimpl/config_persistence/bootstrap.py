
"""
Bootstrap the extension.
"""

from ...aid.simp import (
    EventBus,
)
from ...aid.bootstrap import (
    ExtensionMetadataStruct,
    ANY_VERSION,
)


def bootstrap_config_persistence(bus: EventBus) -> None:
    """Doesn't do anything yet."""


EXTENSION_METADATA: ExtensionMetadataStruct = {
    "type": "impl",
    "implements": [{
        "extension": "core.config_persistence.api",
        "minimum": ANY_VERSION,
    }],
    "depends": [],

    "name": "default.config_persistence",
    "version": (1, 0, 0,),
    "authors": ["Petronia"],
}
