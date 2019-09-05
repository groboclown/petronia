
"""
Bootstrap
"""

from .handle_config_paths import handle_config_paths
from ..general import (
    PlatformExtensionConfigurationState,
    STATE_ID_PLATFORM_EXTENSION_CONFIGURATION_STATE,
)
from ....aid.simp import (
    EventBus,
    ParticipantId,
    EventId,
    log, TRACE, DEBUG, VERBOSE,
)
from ....aid.bootstrap import (
    ExtensionMetadataStruct,
    ANY_VERSION,
)
from ....aid.lifecycle import create_one_and_done
from ....core.state.api import (
    EVENT_ID_UPDATED_STATE,
    StateStoreUpdatedEvent,
    as_state_change_listener,
)


def bootstrap_config_file(bus: EventBus) -> None:
    """Setup the extension."""

    def on_config_state_change(
            _event_id: EventId, _target_id: ParticipantId,  # pylint: disable=unused-argument
            event_obj: StateStoreUpdatedEvent[PlatformExtensionConfigurationState]
    ) -> None:
        paths = event_obj.state.ordered_search_path
        # print("DEBUG config file startup: " + repr(paths) + " - " + repr(_target_id))
        if paths:
            handle_config_paths(bus, paths)

    # The configuration only needs to run once.

    create_one_and_done(
        bus, STATE_ID_PLATFORM_EXTENSION_CONFIGURATION_STATE,
        STATE_ID_PLATFORM_EXTENSION_CONFIGURATION_STATE,
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
