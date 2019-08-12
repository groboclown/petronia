
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
)
from ....aid.bootstrap import (
    ExtensionMetadataStruct,
    ListenerSetup,
    ANY_VERSION,
)
from ....core.state.api import (
    StateStoreUpdatedEvent,
    as_state_change_listener,
)

def bootstrap_config_file(bus: EventBus) -> None:
    _StateListener(bus)


class _StateListener:
    __slots__ = ('_listener', '__bus',)
    _listener: Optional[ListenerId]

    def __init__(self, bus: EventBus) -> None:
        self.__bus = bus
        self._listener = bus.add_listener(
            STATE_ID_PLATFORM_EXTENSION_CONFIGURATION_STATE,
            _as_ssuepec_listener,
            self._on_state_change
        )

    def _on_state_change(
            self,
            event_id: EventId, target_id: ParticipantId, # pylint: disable=unused-argument
            event_obj: StateStoreUpdatedEvent[PlatformExtensionConfigurationState]
    ) -> None:
        paths = event_obj.state.ordered_search_path
        if paths and self._listener:
            self.__bus.remove_listener(self._listener)
            self._listener = None
            handle_config_paths(self.__bus, paths)


def _as_ssuepec_listener(
        callback: EventCallback[StateStoreUpdatedEvent[PlatformExtensionConfigurationState]]
) -> ListenerSetup[StateStoreUpdatedEvent[PlatformExtensionConfigurationState]]:
    return as_state_change_listener(callback)


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
