
from ....aid.simp import (
    EventBus,
    EventId,
    ParticipantId,
)
from ....aid.bootstrap import (
    ANY_VERSION,
    ExtensionMetadataStruct,
    create_singleton_identity,
)


def bootstrap_validation(bus: EventBus) -> None:
    pass


EXTENSION_METADATA: ExtensionMetadataStruct = {
    "type": "api",
    "name": "core.validation.api",
    "version": (1, 0, 0,),
    "depends": [],
    "authors": ["Petronia"],
}