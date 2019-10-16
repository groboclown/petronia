
"""
Validation bootstrap
"""

from ...aid.std import (
    EventBus,
    EventId,
    ParticipantId,
)
from ...aid.bootstrap import (
    ANY_VERSION,
    create_singleton_identity,
)
from ...base.internal_.internal_extension import petronia_extension


def bootstrap_validation(bus: EventBus) -> None:
    pass


EXTENSION_METADATA = petronia_extension({
    "type": "impl",
    "name": "default.validation",
    "version": (1, 0, 0,),
    "implements": ({
       "extension": "core.validation.api",
       "minimum": ANY_VERSION,
    },),
    "depends": (),
})
