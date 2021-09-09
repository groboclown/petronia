
"""
Bootstrap the extension.
"""

from ...aid.bootstrap import (
    EventBus,
    ANY_VERSION,
)
from ...base.internal_.internal_extension import petronia_extension


def bootstrap_config_persistence(_bus: EventBus) -> None:
    """Doesn't do anything yet."""


EXTENSION_METADATA = petronia_extension({
    "type": "impl",
    "implements": ({
        "extension": "core.config_persistence.api",
        "minimum": ANY_VERSION,
    },),
    "depends": (),

    "name": "default.config_persistence",
    "version": (1, 0, 0,),
})
