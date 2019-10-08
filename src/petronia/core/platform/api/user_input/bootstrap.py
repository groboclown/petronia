
"""
Bootstrap the user input.
"""

from .....aid.std import (
    EventBus,
    STRING_EMPTY_TUPLE,
)
from .....aid.bootstrap import (
    register_event,
    QUEUE_EVENT_NORMAL,
    QUEUE_EVENT_HIGH,
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
    # Hotkey events have high priority, because we want the key responsiveness
    # to be quick.
    register_event(
        bus, EVENT_ID_HOTKEY_PRESSED, QUEUE_EVENT_HIGH,
        HotkeyPressedEvent, HotkeyPressedEvent('')
    )
    register_event(
        bus, EVENT_ID_HOTKEY_PROGRESS, QUEUE_EVENT_HIGH,
        HotkeyProgressEvent, HotkeyProgressEvent('', STRING_EMPTY_TUPLE)
    )
    register_event(
        bus, EVENT_ID_HOTKEY_PROGRESS_CANCELLED, QUEUE_EVENT_HIGH,
        HotkeyProgressCancelledEvent, HotkeyProgressCancelledEvent()
    )
