
"""
Initialize the extension.
"""

from ...aid.std import (
    EventId,
    EventBus,
    ParticipantId,
    as_state_change_listener,
    StateStoreUpdatedEvent,
    report_error,
    log, VERBOSE, INFO,
)
from ...aid.bootstrap import (
    create_singleton_identity,
    ANY_VERSION,
)
from ...aid.lifecycle import create_module_listener_helper
from ...base.internal_.internal_extension import petronia_extension
from ...core.hotkeys.api import (
    TARGET_ID_HOTKEYS,

    SetMasterHotkeySequenceEvent,
    as_set_master_hotkey_sequence_listener,

    RegisterHotkeyEventEvent,
    as_register_hotkey_event_listener,

    RemoveHotkeyEventEvent,
    as_remove_hotkey_event_listener,

    HotkeyBoundServiceAnnouncementEvent,
    as_hotkey_bound_service_announcement_listener,

    send_hotkey_event_triggered,
    set_hotkey_event_state,
)
from ...core.config_persistence.api import (
    PersistentConfigurationState,
)
from ...core.platform.api.user_input.hotkey import (
    TARGET_ID_PLATFORM_HOTKEY,
    set_hotkey_config,
    HotkeyPressedEvent,
    as_hotkey_pressed_listener,
)
from .config import (
    CONFIGURATION_ID_HOTKEYS_CMD,
    load_hotkey_configuration,
)
from .state import (
    HotkeyState,
)

MODULE_ID = create_singleton_identity('default.hotkeys')
EXTENSION_METADATA = petronia_extension({
    'type': 'impl',
    "implements": ({
        "extension": "core.hotkeys.api",
        "minimum": ANY_VERSION,
    },),
    'depends': (),
    'name': 'default.hotkeys',
    'version': (1, 0, 0,),
})


def bootstrap_hotkey_broker(bus: EventBus) -> None:
    handler = Handler(bus)
    helper = create_module_listener_helper(bus, MODULE_ID)
    helper.listen(  # type: ignore
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
    helper.listen(
        TARGET_ID_HOTKEYS, as_hotkey_bound_service_announcement_listener,
        handler.bound_service
    )
    helper.listen(
        TARGET_ID_PLATFORM_HOTKEY, as_hotkey_pressed_listener,
        handler.hotkey_pressed
    )


class Handler:
    __slots__ = ('__bus', '__state', '__master')

    def __init__(self, bus: EventBus):
        self.__bus = bus
        self.__state = HotkeyState()
        self.__master = ""

    def on_config_load(
            self,
            _event_id: EventId, _target_id: ParticipantId,
            state: StateStoreUpdatedEvent[PersistentConfigurationState]
    ) -> None:
        master, problems = load_hotkey_configuration(self.__state, state.state.persistent)
        if problems:
            for problem in problems:
                report_error(self.__bus, problem)
        elif master:
            self.__master = master
            self._send_hotkey_setup()

    def bound_service(
            self,
            _event_id: EventId, _target_id: ParticipantId,
            event: HotkeyBoundServiceAnnouncementEvent
    ) -> None:
        self.__state.add_announced(event.schema)
        self._send_hotkey_setup()

    def set_master_sequence(
            self,
            _event_id: EventId, _target_id: ParticipantId,
            event: SetMasterHotkeySequenceEvent
    ) -> None:
        self.__master = event.master_sequence
        self._send_hotkey_setup()

    def register_hotkey(
            self,
            _event_id: EventId, _target_id: ParticipantId,
            event: RegisterHotkeyEventEvent
    ) -> None:
        self.__state.add_hotkey(event.hotkey, event.data)
        self._send_hotkey_setup()

    def remove_hotkey(
            self,
            _event_id: EventId, _target_id: ParticipantId,
            event: RemoveHotkeyEventEvent
    ) -> None:
        self.__state.remove_hotkey(event.hotkey)
        self._send_hotkey_setup()

    def hotkey_pressed(
            self,
            _event_id: EventId, _target_id: ParticipantId,
            event: HotkeyPressedEvent
    ) -> None:
        binding = self.__state.get_hotkey_event(event.name)
        log(
            INFO, Handler.hotkey_pressed,
            'Encountered hotkey "{0}", bound to {1}',
            event.name, binding
        )
        if binding is not None:
            send_hotkey_event_triggered(self.__bus, binding[1].service, binding[0].data)

    def _send_hotkey_setup(self) -> None:
        if self.__master:
            # Only broadcast the key config if we have a configuration.
            set_hotkey_config(self.__bus, self.__master, self.__state.get_platform_keys())
        set_hotkey_event_state(self.__bus, self.__state.get_state())
