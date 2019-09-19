
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

from typing import Sequence, Dict
from .....aid.simp import (
    EventId,
    EventBus,
    EventCallback,
    SingletonId,
    set_state,
)
from .....aid.bootstrap import (
    create_singleton_identity,
    ListenerSetup,
)

# ---------------------------------------------------------------------------
CONFIGURATION_ID_HOTKEYS: SingletonId = create_singleton_identity('core.platform.api/hotkey-config')


class HotkeyConfig:
    """Requested configuration for the hotkeys.  If the configuration is
    allowed, the HotkeyState is sent out with the update.  If there was a
    problem, then an error is reported.

    The hotkeys are a mapping from the key combo to the hotkey label, because
    hotkey combos must be unique.
    """
    __slots__ = ('__hotkeys', '__master')

    def __init__(self, master_sequence: str, hotkeys: Dict[str, str]) -> None:
        self.__master = master_sequence
        self.__hotkeys = dict(hotkeys)

    @property
    def master_sequence(self) -> str:
        """The key sequence that must be pressed before any of the hotkeys.
        This does not affect the hotkey names returned in the pressed event."""
        return self.__master

    @property
    def hotkeys(self) -> Dict[str, str]:
        """All registered hotkeys, as the configuration named them."""
        return self.__hotkeys


def set_hotkey_config(bus: EventBus, master_sequence: str, hotkeys: Dict[str, str]) -> None:
    set_state(
        bus, CONFIGURATION_ID_HOTKEYS,
        HotkeyConfig, HotkeyConfig(master_sequence, hotkeys)
    )


# ---------------------------------------------------------------------------
STATE_ID_HOTKEYS = create_singleton_identity('core.platform.api/hotkey-state')


class HotkeyState:
    """The state of the current hotkeys.  Extracted from the hotkey configuration."""
    __slots__ = ('__hotkeys', '__master')

    def __init__(self, master_sequence: str, hotkeys: Dict[str, str]) -> None:
        self.__master = master_sequence
        self.__hotkeys = dict(hotkeys)

    @property
    def master_sequence(self) -> str:
        """The key sequence that must be pressed before any of the hotkeys.
        This does not affect the hotkey names returned in the pressed event."""
        return self.__master

    @property
    def hotkeys(self) -> Dict[str, str]:
        """All registered hotkeys, as the configuration named them."""
        return self.__hotkeys


def set_hotkey_state(bus: EventBus, master_sequence: str, hotkeys: Dict[str, str]) -> None:
    set_state(
        bus, STATE_ID_HOTKEYS,
        HotkeyState, HotkeyState(master_sequence, hotkeys)
    )


# ---------------------------------------------------------------------------
TARGET_ID_PLATFORM_HOTKEY = create_singleton_identity('core.platform.api/hotkey')
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


def send_hotkey_pressed_event(bus: EventBus, hotkey_name: str) -> None:
    bus.trigger(EVENT_ID_HOTKEY_PRESSED, TARGET_ID_PLATFORM_HOTKEY, HotkeyPressedEvent(hotkey_name))


def as_hotkey_pressed_listener(
        callback: EventCallback[HotkeyPressedEvent]
) -> ListenerSetup[HotkeyPressedEvent]:
    return (EVENT_ID_HOTKEY_PRESSED, callback,)


# ---------------------------------------------------------------------------
EVENT_ID_HOTKEY_PROGRESS = EventId('core.platform.api hotkey-progress')


class HotkeyProgressEvent:
    """
    A hotkey sequence is being processed.

    For limited use; specifically, a helper tool to display your progress in
    entering a hotkey combo, and listing different next-key options, and what
    they will do.
    """
    __slots__ = ('__keys', '__actions')

    def __init__(self, keys: Sequence[str], actions: Sequence[str]) -> None:
        self.__keys = tuple(keys)
        self.__actions = tuple(actions)

    @property
    def keys(self) -> Sequence[str]:
        """List of keys in the sequence pressed already."""
        return self.__keys

    @property
    def actions(self) -> Sequence[str]:
        """List of potential actions that could follow this up."""
        return self.__actions


def send_hotkey_progress_event(bus: EventBus, keys: Sequence[str], actions: Sequence[str]) -> None:
    bus.trigger(EVENT_ID_HOTKEY_PROGRESS, TARGET_ID_PLATFORM_HOTKEY, HotkeyProgressEvent(keys, actions))


def as_hotkey_progress_listener(
        callback: EventCallback[HotkeyProgressEvent]
) -> ListenerSetup[HotkeyProgressEvent]:
    return (EVENT_ID_HOTKEY_PROGRESS, callback,)


# ---------------------------------------------------------------------------
EVENT_ID_HOTKEY_PROGRESS_CANCELLED = EventId('core.platform.api hotkey-progress-cancelled')


class HotkeyProgressCancelledEvent:
    """
    A hotkey sequence that was processed, is now cancelled.

    For limited use; specifically, a helper tool to display your progress in
    entering a hotkey combo, and listing different next-key options, and what
    they will do.
    """
    __slots__ = ()

    def __init__(self) -> None:
        pass


def send_hotkey_progress_cancelled_event(bus: EventBus) -> None:
    bus.trigger(EVENT_ID_HOTKEY_PROGRESS_CANCELLED, TARGET_ID_PLATFORM_HOTKEY, HotkeyProgressCancelledEvent())


def as_hotkey_progress_cancelled_listener(
        callback: EventCallback[HotkeyProgressCancelledEvent]
) -> ListenerSetup[HotkeyProgressCancelledEvent]:
    return (EVENT_ID_HOTKEY_PROGRESS_CANCELLED, callback,)
