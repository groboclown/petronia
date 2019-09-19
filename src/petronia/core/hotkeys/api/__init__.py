
"""
Standard API for registering hotkeys that perform generate events.

The API acts as a broker between applications that use hotkeys, and the low-
level platform hotkey registration.

The registration will associate a basic key combination to a target ID and
a basic data structure.  The event ID is fixed.
"""

from .bootstrap import bootstrap_hotkeys as start_extension
from .bootstrap import EXTENSION_METADATA

from .events import (
    TARGET_ID_HOTKEYS,

    EVENT_ID_HOTKEY_EVENT_TRIGGERED,
    HotkeyEventTriggeredEvent,
    as_hotkey_event_triggered_listener,
    send_hotkey_event_triggered,

    EVENT_ID_REMOVE_HOTKEY_EVENT,
    RemoveHotkeyEventEvent,
    as_remove_hotkey_event_listener,
    remove_hotkey_event,

    EVENT_ID_REGISTER_HOTKEY_EVENT,
    RegisterHotkeyEventEvent,
    as_register_hotkey_event_listener,
    register_hotkey_event,

    EVENT_ID_SET_MASTER_HOTKEY_SEQUENCE,
    SetMasterHotkeySequenceEvent,
    as_set_master_hotkey_sequence_listener,
    set_master_hotkey_sequence,

    EVENT_ID_HOTKEY_BOUND_SERVICE_ANNOUNCEMENT,
    HotkeyBoundServiceAnnouncementEvent,
    as_hotkey_bound_service_announcement_listener,
    send_hotkey_bound_service_announcement,

    EVENT_ID_HOTKEY_UNBIND_SERVICE_ANNOUNCEMENT,
    HotkeyUnbindServiceAnnouncementEvent,
    as_hotkey_unbind_service_announcement_listener,
    send_hotkey_unbind_service_announcement,
)
from .state import (
    BoundServiceActionData,
    BoundServiceActionSchema,
    HotkeyEventState,
    RegisteredHotkeyEvent,
    STATE_ID_HOTKEY_EVENTS,
    set_hotkey_event_state,
)
