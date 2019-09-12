
"""
Initialize the extension.
"""

from typing import Sequence, Set, List, Tuple, Iterable, Optional
from ...aid.simp import (
    EventId,
    EventBus, EventCallback,
    ParticipantId,
    T,
    log,
    TRACE,
    as_state_change_listener,
    StateStoreUpdatedEvent,
)
from ...aid.bootstrap import (
    create_singleton_identity,
    ListenerSetup,
    ExtensionMetadataStruct,
    ANY_VERSION,
)
from ...aid.module_bootstrap import create_module_listener_helper
from ...core.hotkeys.api import (
    TARGET_ID_HOTKEYS,

    SetMasterHotkeySequenceEvent,
    as_set_master_hotkey_sequence_listener,

    RegisterHotkeyEventEvent,
    as_register_hotkey_event_listener,

    RemoveHotkeyEventEvent,
    as_remove_hotkey_event_listener,
)
from ...core.config_persistence.api import (
    PersistentConfigurationState,
)
from .config import (
    CONFIGURATION_ID_HOTKEYS_CMD,
)

MODULE_ID = create_singleton_identity('default.hotkey.cmd')
EXTENSION_METADATA: ExtensionMetadataStruct = {
    'type': 'impl',
    "implements": [{
        "extension": "core.hotkeys/api",
        "version": ANY_VERSION,
    }],
    'depends': [],
    'name': 'default.hotkeys.cmd',
    'version': (1, 0, 0,),
    'authors': ['Petronia'],
}


def bootstrap_hotkey_broker(bus: EventBus) -> None:
    handler = Handler(bus)
    helper = create_module_listener_helper(bus, MODULE_ID)
    helper.listen(
        CONFIGURATION_ID_HOTKEYS_CMD, as_state_change_listener,
        handler.on_config_load
    )
    helper.listen(
        TARGET_ID_HOTKEYS, as_set_master_hotkey_sequence_listener,
        handler.set_master_sequence
    )
    helper.listen(
        TARGET_ID_HOTKEYS, as_register_hotkey_event_listener,
        handler.register_hotkey
    )
    helper.listen(
        TARGET_ID_HOTKEYS, as_remove_hotkey_event_listener,
        handler.remove_hotkey
    )


class Handler:
    __slots__ = ('__bus',)

    def __init__(self, bus: EventBus):
        self.__bus = bus

    def on_config_load(
            self,
            _event_id: EventId, _target_id: ParticipantId,
            state: StateStoreUpdatedEvent[PersistentConfigurationState]
    ) -> None:
        pass

    def set_master_sequence(
            self,
            _event_id: EventId, _target_id: ParticipantId,
            event: SetMasterHotkeySequenceEvent
    ) -> None:
        pass

    def register_hotkey(
            self,
            _event_id: EventId, _target_id: ParticipantId,
            event: RegisterHotkeyEventEvent
    ) -> None:
        pass

    def remove_hotkey(
            self,
            _event_id: EventId, _target_id: ParticipantId,
            event: RemoveHotkeyEventEvent
    ) -> None:
        pass
