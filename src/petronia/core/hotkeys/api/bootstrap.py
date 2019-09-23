
# mypy: allow-any-expr
# mypy: allow-any-generics

"""
Startup the extension.
"""

from ....aid.simp import (
    EventBus,
    EMPTY_DICT,
    EMPTY_MAPPING,
    EMPTY_TUPLE,
)
from ....aid.bootstrap import (
    register_event,
    ExtensionMetadataStruct,
    ANY_VERSION,
    QUEUE_EVENT_NORMAL,
    NOT_PARTICIPANT,
)
from ...state.api import set_state
from .events import (
    EVENT_ID_HOTKEY_EVENT_TRIGGERED,
    HotkeyEventTriggeredEvent,
    BoundServiceActionData,

    EVENT_ID_REGISTER_HOTKEY_EVENT,
    RegisterHotkeyEventEvent,

    EVENT_ID_REMOVE_HOTKEY_EVENT,
    RemoveHotkeyEventEvent,

    EVENT_ID_SET_MASTER_HOTKEY_SEQUENCE,
    SetMasterHotkeySequenceEvent,

    EVENT_ID_HOTKEY_BOUND_SERVICE_ANNOUNCEMENT,
    HotkeyBoundServiceAnnouncementEvent,
    BoundServiceActionSchema,

    EVENT_ID_HOTKEY_UNBIND_SERVICE_ANNOUNCEMENT,
    HotkeyUnbindServiceAnnouncementEvent,
)
from .state import (
    STATE_ID_HOTKEY_EVENTS,
    HotkeyEventState,
)


def bootstrap_hotkeys(bus: EventBus) -> None:
    """Register all the events and everything."""
    register_event(
        bus, EVENT_ID_HOTKEY_EVENT_TRIGGERED, QUEUE_EVENT_NORMAL,
        HotkeyEventTriggeredEvent, HotkeyEventTriggeredEvent(BoundServiceActionData('', EMPTY_MAPPING))
    )
    register_event(
        bus, EVENT_ID_REGISTER_HOTKEY_EVENT, QUEUE_EVENT_NORMAL,
        RegisterHotkeyEventEvent, RegisterHotkeyEventEvent('', BoundServiceActionData('', EMPTY_MAPPING))
    )
    register_event(
        bus, EVENT_ID_REMOVE_HOTKEY_EVENT, QUEUE_EVENT_NORMAL,
        RemoveHotkeyEventEvent, RemoveHotkeyEventEvent('')
    )
    register_event(
        bus, EVENT_ID_SET_MASTER_HOTKEY_SEQUENCE, QUEUE_EVENT_NORMAL,
        SetMasterHotkeySequenceEvent, SetMasterHotkeySequenceEvent('')
    )
    register_event(
        bus, EVENT_ID_HOTKEY_BOUND_SERVICE_ANNOUNCEMENT, QUEUE_EVENT_NORMAL,
        HotkeyBoundServiceAnnouncementEvent, HotkeyBoundServiceAnnouncementEvent(
            BoundServiceActionSchema(NOT_PARTICIPANT, '', {})
        )
    )
    register_event(
        bus, EVENT_ID_HOTKEY_UNBIND_SERVICE_ANNOUNCEMENT, QUEUE_EVENT_NORMAL,
        HotkeyUnbindServiceAnnouncementEvent, HotkeyUnbindServiceAnnouncementEvent(
            NOT_PARTICIPANT, ''
        )
    )
    set_state(
        bus, STATE_ID_HOTKEY_EVENTS,
        HotkeyEventState, HotkeyEventState(EMPTY_TUPLE, EMPTY_TUPLE)
    )


EXTENSION_METADATA: ExtensionMetadataStruct = {
    "type": "api",
    "default": [{
        "extension": "defimpl.hotkeys",
        "version": ANY_VERSION,
    }],
    "depends": [{
        "extension": "core.platform.api",
        "version": ANY_VERSION,
    }, {
        "extension": "core.state.api",
        "version": ANY_VERSION,
    }],

    "name": "core.hotkeys.api",
    "version": (1, 0, 0,),
    "authors": ["Petronia"],
}
