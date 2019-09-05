
"""
Bootstrap
"""

from typing import Optional
from .handle_config_paths import handle_config_paths
from ..general import (
    PlatformExtensionConfigurationState,
    STATE_ID_PLATFORM_EXTENSION_CONFIGURATION_STATE,
)
from ....aid.simp import (
    EventBus,
    ListenerId,
    ParticipantId,
    EventId,
    EventCallback,
    log, TRACE, DEBUG, VERBOSE,
)
from ....aid.bootstrap import (
    create_singleton_identity,
    ExtensionMetadataStruct,
    ListenerSetup,
    ANY_VERSION,
)
from ....aid.lifecycle import create_one_and_done
from ....core.state.api import (
    EVENT_ID_UPDATE_STATE_REQUEST,
    StateStoreUpdatedEvent,
    as_state_change_listener,
)


TARGET_ID_CONFIGURATION_FILE_READER = create_singleton_identity('petronia.default.configuration.file')


def bootstrap_config_file(bus: EventBus) -> None:
    """Setup the extension."""

    def on_config_state_change(
            _event_id: EventId, _target_id: ParticipantId,  # pylint: disable=unused-argument
            event_obj: StateStoreUpdatedEvent[PlatformExtensionConfigurationState]
    ) -> None:
        paths = event_obj.state.ordered_search_path
        if paths:
            handle_config_paths(bus, paths)

    # The configuration only needs to run once.

    create_one_and_done(
        bus, TARGET_ID_CONFIGURATION_FILE_READER,
        EVENT_ID_UPDATE_STATE_REQUEST,
        as_state_change_listener, on_config_state_change,
        is_application=True, is_standalone=True
    )


EXTENSION_METADATA: ExtensionMetadataStruct = {
    "type": "standalone",
    "depends": [
        {
            "extension": "core.state.api",
            "minimum": ANY_VERSION,
        },
    ],

    "name": "default.configuration.file",
    "version": (1, 0, 0,),
    "authors": ["Petronia"],
}
