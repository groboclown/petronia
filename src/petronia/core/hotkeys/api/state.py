
"""
The current state of the registered hotkeys.
"""

from typing import Sequence
from ....aid.simp import (
    ParticipantId,
)
from ....aid.bootstrap import (
    create_singleton_identity,
)
from ....core.config_persistence.api import PersistType


STATE_ID_HOTKEY_EVENTS = create_singleton_identity('core.hotkeys.api/state')

class RegisteredHotkeyEvent:
    """An internal state representation of the registered hotkey data."""
    __slots__ = ('__hotkey', '__target_id', '__data',)
    def __init__(self, hotkey: str, target_id: ParticipantId, data: PersistType) -> None:
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


class HotkeyEventState:
    """
    All the registered hotkey events.
    """
    __slots__ = ('__reg',)
    def __init__(self, registered: Sequence[RegisteredHotkeyEvent]) -> None:
        self.__reg = registered

    @property
    def registered(self) -> Sequence[RegisteredHotkeyEvent]:
        return self.__reg
