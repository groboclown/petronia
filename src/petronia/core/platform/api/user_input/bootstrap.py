
"""
Bootstrap the user input.
"""

from .....aid.simp import (
    EventBus,
    set_state,
)
from .....aid.bootstrap import (
    register_event,
    QUEUE_EVENT_NORMAL,
)
from .hotkey import (
    EVENT_ID_HOTKEY_PRESSED,
    HotkeyPressedEvent,
)


def register_user_input_events(bus: EventBus) -> None:
    """
    Register the user input events.
    """
    register_event(
        bus, EVENT_ID_HOTKEY_PRESSED, QUEUE_EVENT_NORMAL,
        HotkeyPressedEvent, HotkeyPressedEvent('')
    )
