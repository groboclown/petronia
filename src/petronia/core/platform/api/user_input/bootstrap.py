
"""
Bootstrap the user input.
"""

from .....aid.simp import (
    EventBus,
    set_state,
    STRING_EMPTY_TUPLE,
)
from .....aid.bootstrap import (
    register_event,
    QUEUE_EVENT_NORMAL,
)
from .hotkey import (
    EVENT_ID_HOTKEY_PRESSED,
    HotkeyPressedEvent,

    EVENT_ID_HOTKEY_PROGRESS,
    HotkeyProgressEvent,

    EVENT_ID_HOTKEY_PROGRESS_CANCELLED,
    HotkeyProgressCancelledEvent,
)


def register_user_input_events(bus: EventBus) -> None:
    """
    Register the user input events.
    """
    register_event(
        bus, EVENT_ID_HOTKEY_PRESSED, QUEUE_EVENT_NORMAL,
        HotkeyPressedEvent, HotkeyPressedEvent('')
    )
    register_event(
        bus, EVENT_ID_HOTKEY_PROGRESS, QUEUE_EVENT_NORMAL,
        HotkeyProgressEvent, HotkeyProgressEvent('', STRING_EMPTY_TUPLE)
    )
    register_event(
        bus, EVENT_ID_HOTKEY_PROGRESS_CANCELLED, QUEUE_EVENT_NORMAL,
        HotkeyProgressCancelledEvent, HotkeyProgressCancelledEvent()
    )
