
"""
The current state of the registered hotkeys.
"""

from typing import Sequence
from ....aid.simp import (
    ParticipantId,
    EventBus,
    set_state,
)
from ....aid.bootstrap import (
    create_singleton_identity,
)
from ....core.config_persistence.api import (
    PersistType,
    PersistTypeSchema,
    readonly_persistent_copy,
    readonly_persistent_schema_copy,
)


STATE_ID_HOTKEY_EVENTS = create_singleton_identity('core.hotkeys.api/state')


class BoundServiceActionData:
    """
    Information bound to a hotkey, to specify parameters to the service
    that listens.
    """
    __slots__ = (
        '__action',
        '__parameters',
    )

    def __init__(self, action: str, parameters: PersistType) -> None:
        self.__action = action
        self.__parameters = readonly_persistent_copy(parameters)

    @property
    def action(self) -> str:
        return self.__action

    @property
    def parameters(self) -> PersistType:
        return self.__parameters


class BoundServiceActionSchema:
    """
    Advertised service action and its expected information.
    """
    __slots__ = (
        '__service',
        '__action',
        '__parameters',
    )

    def __init__(self, service: ParticipantId, action: str, parameters: PersistTypeSchema) -> None:
        self.__service = service
        self.__action = action
        self.__parameters = readonly_persistent_schema_copy(parameters)

    @property
    def service(self) -> ParticipantId:
        return self.__service

    @property
    def action(self) -> str:
        return self.__action

    @property
    def parameters(self) -> PersistType:
        return self.__parameters

    def __eq__(self, other) -> bool:
        if not isinstance(other, BoundServiceActionSchema):
            return False
        return (
                self.service == other.service and
                self.action == other.action and
                self.parameters == other.parameters
        )


class RegisteredHotkeyEvent:
    """An internal state representation of the registered hotkey data.  The target for the hotkey
    is the bound service action schema's service."""
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


class HotkeyEventState:
    """
    All the registered hotkey events.
    """
    __slots__ = ('__reg', '__adv',)

    def __init__(
            self,
            registered: Sequence[RegisteredHotkeyEvent],
            announced: Sequence[BoundServiceActionSchema]
    ) -> None:
        self.__reg = tuple(registered)
        self.__adv = tuple(announced)

    @property
    def registered(self) -> Sequence[RegisteredHotkeyEvent]:
        """All registered hotkeys with a correctly bound action."""
        return self.__reg

    @property
    def announced(self) -> Sequence[BoundServiceActionSchema]:
        """All announced services and their actions which can have a hotkey binding."""
        return self.__adv


def set_hotkey_event_state(bus: EventBus, state: HotkeyEventState) -> None:
    set_state(bus, STATE_ID_HOTKEY_EVENTS, HotkeyEventState, state)
