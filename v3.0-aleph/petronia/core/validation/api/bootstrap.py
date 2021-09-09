
"""
Validation bootstrap
"""

from ....aid.std import (
    EventBus,
    EventId,
    ParticipantId,
)
from ....aid.bootstrap import (
    ANY_VERSION,
    create_singleton_identity,
)
from ....base.internal_.internal_extension import petronia_extension


def bootstrap_validation(bus: EventBus) -> None:
    pass


EXTENSION_METADATA = petronia_extension({
    "type": "api",
    "name": "core.validation.api",
    "version": (1, 0, 0,),
    "depends": (),
    "defaults": ({
        "extension": "default.validation",
        "minimum": ANY_VERSION,
    },),
})
