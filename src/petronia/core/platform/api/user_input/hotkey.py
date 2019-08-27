
"""
Events related to registering hotkeys and getting the state of them.

Hotkeys at the platform level are very low level.  It's simply a list of
hotkey expressions, like `shift+m` or `super+f1`.  The platform implementation
manages the conversion of that string into platform-specific key codes.  When
a hotkey sequence is detected by the platform, that original hotkey string
is sent out as an event.  The target for the event is a singleton hotkey target.

Because of the low-level nature of platform hotkeys, they cannot be directly
updated through user configuration.  Instead, some other API must be configured
to use them.  For example, the `core.hotkeys.api`.
"""

from typing import Iterable, Sequence
from .....aid.simp import (
    EventId,
    EventBus,
    set_state,
)
from .....aid.bootstrap import (
    create_singleton_identity,
)

# ---------------------------------------------------------------------------
CONFIGURATION_ID_HOTKEYS = create_singleton_identity('core.platform.api/hotkey-config')


class HotkeyConfig:
    """Requested configuration for the hotkeys.  If the configuration is
    allowed, the HotkeyState is sent out with the update.  If there was a
    problem, then an error is reported."""
    __slots__ = ('__hotkeys', '__master')

    def __init__(self, master_sequence: str, hotkeys: Iterable[str]) -> None:
        self.__master = master_sequence
        self.__hotkeys = tuple(hotkeys)

    @property
    def master_sequence(self) -> str:
        """The key sequence that must be pressed before any of the hotkeys.
        This does not affect the hotkey names returned in the pressed event."""
        return self.__master

    @property
    def hotkeys(self) -> Sequence[str]:
        """All registered hotkeys, as the configuration named them."""
        return self.__hotkeys


def set_hotkey_config(bus: EventBus, master_sequence: str, hotkeys: Iterable[str]) -> None:
    set_state(
        bus, CONFIGURATION_ID_HOTKEYS,
        HotkeyConfig, HotkeyConfig(master_sequence, hotkeys)
    )


# ---------------------------------------------------------------------------
STATE_ID_HOTKEYS = create_singleton_identity('core.platform.api/hotkey-state')


class HotkeyState:
    """The state of the current hotkeys.  Extracted from the hotkey configuration."""
    __slots__ = ('__hotkeys', '__master')

    def __init__(self, master_sequence: str, hotkeys: Iterable[str]) -> None:
        self.__master = master_sequence
        self.__hotkeys = tuple(hotkeys)

    @property
    def master_sequence(self) -> str:
        """The key sequence that must be pressed before any of the hotkeys.
        This does not affect the hotkey names returned in the pressed event."""
        return self.__master

    @property
    def hotkeys(self) -> Sequence[str]:
        """All registered hotkeys, as the configuration named them."""
        return self.__hotkeys


def set_hotkey_state(bus: EventBus, master_sequence: str, hotkeys: Iterable[str]) -> None:
    set_state(
        bus, STATE_ID_HOTKEYS,
        HotkeyState, HotkeyState(master_sequence, hotkeys)
    )


# ---------------------------------------------------------------------------
TARGET_ID_HOTKEY = create_singleton_identity('core.platform.api/hotkey')
EVENT_ID_HOTKEY_PRESSED = EventId('core.platform.api hotkey-pressed')


class HotkeyPressedEvent:
    """A hotkey sequence was detected as pressed by the user."""
    __slots__ = ('__name',)

    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        """Name of the pressed hotkey."""
        return self.__name
