
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
from .state import (
    BoundServiceActionData,
    BoundServiceActionSchema,
)


TARGET_ID_HOTKEYS = create_singleton_identity('core.hotkeys.api')


# ---------------------------------------------------------------------------

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
    return (EVENT_ID_SET_MASTER_HOTKEY_SEQUENCE, callback,)


# ---------------------------------------------------------------------------

EVENT_ID_REGISTER_HOTKEY_EVENT = EventId('core.hotkeys.api/register')


class RegisterHotkeyEventEvent:
    """
    Register a hotkey to trigger an event.  The hotkey itself does not include
    the master sequence.  The event will be targeted to the service that
    registered the schema bound to the action type.
    """
    __slots__ = ('__hotkey', '__data',)

    def __init__(self, hotkey: str, data: BoundServiceActionData) -> None:
        self.__hotkey = hotkey
        self.__data = data

    @property
    def hotkey(self) -> str:
        return self.__hotkey

    @property
    def data(self) -> BoundServiceActionData:
        return self.__data


def register_hotkey_event(
        bus: EventBus, target_id: ParticipantId, hotkey: str, data: BoundServiceActionData
) -> None:
    bus.trigger(
        EVENT_ID_REGISTER_HOTKEY_EVENT, TARGET_ID_HOTKEYS,
        RegisterHotkeyEventEvent(hotkey, data)
    )


def as_register_hotkey_event_listener(
        callback: EventCallback[RegisterHotkeyEventEvent]
) -> ListenerSetup[RegisterHotkeyEventEvent]:
    return (EVENT_ID_REGISTER_HOTKEY_EVENT, callback,)


# ---------------------------------------------------------------------------

EVENT_ID_REMOVE_HOTKEY_EVENT = EventId('core.hotkeys.api/remove')


class RemoveHotkeyEventEvent:
    """
    Remove a registered hotkey.
    """
    __slots__ = ('__hotkey',)

    def __init__(self, hotkey: str) -> None:
        self.__hotkey = hotkey

    @property
    def hotkey(self) -> str:
        return self.__hotkey


def remove_hotkey_event(bus: EventBus, hotkey: str) -> None:
    bus.trigger(
        EVENT_ID_REMOVE_HOTKEY_EVENT, TARGET_ID_HOTKEYS,
        RemoveHotkeyEventEvent(hotkey)
    )


def as_remove_hotkey_event_listener(
        callback: EventCallback[RemoveHotkeyEventEvent]
) -> ListenerSetup[RemoveHotkeyEventEvent]:
    return (EVENT_ID_REMOVE_HOTKEY_EVENT, callback,)


# ---------------------------------------------------------------------------

EVENT_ID_HOTKEY_EVENT_TRIGGERED = EventId('core.hotkeys.api/trigger')


class HotkeyEventTriggeredEvent:
    """
    Notification that a hotkey event activated.
    """
    __slots__ = ('__data',)

    def __init__(self, data: BoundServiceActionData) -> None:
        self.__data = data

    @property
    def data(self) -> BoundServiceActionData:
        return self.__data


def send_hotkey_event_triggered(
        bus: EventBus, target_id: ParticipantId, data: BoundServiceActionData
) -> None:
    bus.trigger(EVENT_ID_HOTKEY_EVENT_TRIGGERED, target_id, HotkeyEventTriggeredEvent(data))


def as_hotkey_event_triggered_listener(
        callback: EventCallback[HotkeyEventTriggeredEvent]
) -> ListenerSetup[HotkeyEventTriggeredEvent]:
    return (EVENT_ID_HOTKEY_EVENT_TRIGGERED, callback,)


# ---------------------------------------------------------------------------

EVENT_ID_HOTKEY_BOUND_SERVICE_ANNOUNCEMENT = EventId('core.hotkeys.api/announce')


class HotkeyBoundServiceAnnouncementEvent:
    """
    Notification that a service can be bound to a hotkey, and a description
    of the expected values in the binding.
    """
    __slots__ = ('__schema',)

    def __init__(self, schema: BoundServiceActionSchema) -> None:
        self.__schema = schema

    @property
    def schema(self) -> BoundServiceActionSchema:
        return self.__schema


def send_hotkey_bound_service_announcement(
        bus: EventBus, schema: BoundServiceActionSchema
) -> None:
    bus.trigger(
        EVENT_ID_HOTKEY_EVENT_TRIGGERED, TARGET_ID_HOTKEYS,
        HotkeyBoundServiceAnnouncementEvent(schema)
    )


def as_hotkey_bound_service_announcement_listener(
        callback: EventCallback[HotkeyBoundServiceAnnouncementEvent]
) -> ListenerSetup[HotkeyBoundServiceAnnouncementEvent]:
    return (EVENT_ID_HOTKEY_BOUND_SERVICE_ANNOUNCEMENT, callback,)


# ---------------------------------------------------------------------------

EVENT_ID_HOTKEY_UNBIND_SERVICE_ANNOUNCEMENT = EventId('core.hotkeys.api/revoke-announce')


class HotkeyUnbindServiceAnnouncementEvent:
    """
    Notification that a service can be bound to a hotkey, and a description
    of the expected values in the binding.
    """
    __slots__ = ('__service', '__action')

    def __init__(self, service: ParticipantId, action: str) -> None:
        self.__service = service
        self.__action = action

    @property
    def service(self) -> ParticipantId:
        return self.__service

    @property
    def action(self) -> str:
        return self.__action


def send_hotkey_unbind_service_announcement(
        bus: EventBus, service: ParticipantId, action: str
) -> None:
    bus.trigger(
        EVENT_ID_HOTKEY_EVENT_TRIGGERED, TARGET_ID_HOTKEYS,
        HotkeyUnbindServiceAnnouncementEvent(service, action)
    )


def as_hotkey_unbind_service_announcement_listener(
        callback: EventCallback[HotkeyUnbindServiceAnnouncementEvent]
) -> ListenerSetup[HotkeyUnbindServiceAnnouncementEvent]:
    return (EVENT_ID_HOTKEY_BOUND_SERVICE_ANNOUNCEMENT, callback,)
