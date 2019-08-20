
"""
Hotkey action registration.
"""

from ....aid.simp import (
    EventId,
    EventBus,
    ParticipantId,
    EventCallback,
)
from ....aid.bootstrap import (
    ListenerSetup,
    create_singleton_identity,
)
from ....core.config_persistence.api import PersistType


TARGET_ID_HOTKEYS = create_singleton_identity('core.hotkeys.api')



EVENT_ID_SET_MASTER_HOTKEY_SEQUENCE = EventId('core.hotkeys.api/master')

class SetMasterHotkeySequenceEvent:
    """
    Set the master hotkey sequence.  This may be rejected by the underlying platform.
    """
    __slots__ = ('__sequence',)
    def __init__(self, master_sequence: str) -> None:
        self.__sequence = master_sequence

    @property
    def master_sequence(self) -> str:
        return self.__sequence

def set_master_hotkey_sequence(bus: EventBus, master_sequence: str) -> None:
    bus.trigger(
        EVENT_ID_SET_MASTER_HOTKEY_SEQUENCE, TARGET_ID_HOTKEYS,
        SetMasterHotkeySequenceEvent(master_sequence)
    )

def as_set_master_hotkey_sequence_listener(
        callback: EventCallback[SetMasterHotkeySequenceEvent]
) -> ListenerSetup[SetMasterHotkeySequenceEvent]:
    return (EVENT_ID_SET_MASTER_HOTKEY_SEQUENCE, callback)



EVENT_ID_REGISTER_HOTKEY_EVENT = EventId('core.hotkeys.api/register')

class RegisterHotkeyEventEvent:
    """
    Register a hotkey to trigger an event.  The hotkey itself does not include
    the master sequence.
    """
    __slots__ = ('__hotkey', '__target_id', '__data',)

    def __init__(self, target_id: ParticipantId, hotkey: str, data: PersistType) -> None:
        self.__hotkey = hotkey
        self.__target_id = target_id
        self.__data = data

    @property
    def target_id(self) -> ParticipantId:
        return self.__target_id

    @property
    def hotkey(self) -> str:
        return self.__hotkey

    @property
    def data(self) -> PersistType:
        return self.__data

def register_hotkey_event(
        bus: EventBus, target_id: ParticipantId, hotkey: str, data: PersistType
) -> None:
    bus.trigger(
        EVENT_ID_REGISTER_HOTKEY_EVENT, TARGET_ID_HOTKEYS,
        RegisterHotkeyEventEvent(target_id, hotkey, data)
    )

def as_register_hotkey_event_listener(
        callback: EventCallback[RegisterHotkeyEventEvent]
) -> ListenerSetup[RegisterHotkeyEventEvent]:
    return (EVENT_ID_REGISTER_HOTKEY_EVENT, callback)



EVENT_ID_REMOVE_HOTKEY_EVENT = EventId('core.hotkeys.api/remove')

class RemoveHotkeyEventEvent:
    """
    Remove a registered hotkey.
    """
    __slots__ = ('__hotkey', '__target_id',)

    def __init__(self, target_id: ParticipantId, hotkey: str) -> None:
        self.__hotkey = hotkey
        self.__target_id = target_id

    @property
    def target_id(self) -> ParticipantId:
        return self.__target_id

    @property
    def hotkey(self) -> str:
        return self.__hotkey

def remove_hotkey_event(bus: EventBus, target_id: ParticipantId, hotkey: str) -> None:
    bus.trigger(
        EVENT_ID_REMOVE_HOTKEY_EVENT, TARGET_ID_HOTKEYS,
        RemoveHotkeyEventEvent(target_id, hotkey)
    )

def as_remove_hotkey_event_listener(
        callback: EventCallback[RemoveHotkeyEventEvent]
) -> ListenerSetup[RemoveHotkeyEventEvent]:
    return (EVENT_ID_REMOVE_HOTKEY_EVENT, callback)



EVENT_ID_HOTKEY_EVENT_TRIGGERED = EventId('core.hotkeys.api/trigger')

class HotkeyEventTriggeredEvent:
    """
    Notification that a hotkey event activated.
    """
    __slots__ = ('__data',)
    def __init__(self, data: PersistType) -> None:
        self.__data = data

    @property
    def data(self) -> PersistType:
        return self.__data

def send_hotkey_event_triggered(
        bus: EventBus, target_id: ParticipantId, data: PersistType
) -> None:
    bus.trigger(EVENT_ID_HOTKEY_EVENT_TRIGGERED, target_id, HotkeyEventTriggeredEvent(data))

def as_hotkey_event_triggered_listener(
        callback: EventCallback[HotkeyEventTriggeredEvent]
) -> ListenerSetup[HotkeyEventTriggeredEvent]:
    return (EVENT_ID_HOTKEY_EVENT_TRIGGERED, callback)
