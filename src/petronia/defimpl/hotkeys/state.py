
"""
Hotkey state.
"""

from typing import Dict, List, Optional
from threading import Lock
from ...aid.simp import (
    ParticipantId,
    log, WARN,
)
from ...core.hotkeys.api import (
    BoundServiceActionSchema,
    BoundServiceActionData,
    HotkeyEventState,
    RegisteredHotkeyEvent,
)


class HotkeyState:
    """
    Maintains the internal state of the hotkey registration, and the binding
    to the announced services.

    Hotkeys can be bound to an unannounced service, but until the
    service+action are bound, it will not be sent.
    """
    __slots__ = (
        '__key_count', '__lock',
        '_key_data_map', '_hotkey_id_map', '_announced', '_unbound_keys',
    )

    # Map the the hotkey sequence string to the internal key ID.
    _hotkey_id_map: Dict[str, str]

    # Map the key ID (as registered to the platform hotkey) to the event.
    _key_data_map: Dict[str, RegisteredHotkeyEvent]

    _announced: List[BoundServiceActionSchema]
    _unbound_keys: Dict[str, RegisteredHotkeyEvent]

    def __init__(self) -> None:
        self.__key_count = 0
        self.__lock = Lock()
        self._key_data_map = {}
        self._announced = []
        self._unbound_keys = {}

    def get_state(self) -> HotkeyEventState:
        with self.__lock:
            all_keys = list(self._unbound_keys.values()) + list(self._key_data_map.values())
            return HotkeyEventState(all_keys, tuple(self._announced))

    def add_announced(self, announced: BoundServiceActionSchema) -> None:
        with self.__lock:
            removed: List[str] = []
            for idx in range(len(self._announced)):
                if _schema_src_match(self._announced[idx], announced):
                    self._announced[idx] = announced
                    for key, event in self._key_data_map:
                        if not _is_valid_schema_data(announced, event.data):
                            log(
                                WARN, HotkeyState,
                                'Service {0} hotkey action {1} does not match requested hotkey {2}: {3}',
                                announced.service, announced.action, key, event.data
                            )
                            removed.append(key)
                            self._unbound_keys[key] = event
                    for key in removed:
                        del self._key_data_map[key]
                    return

            self._announced.append(announced)
            for key, event in self._unbound_keys.items():
                if _event_schema_match(event, announced):
                    if _is_valid_schema_data(announced, event.data):
                        self._key_data_map[key] = event
                        removed.append(key)
                    else:
                        log(
                            WARN, HotkeyState,
                            'Service {0} hotkey action {1} does not match requested hotkey {2}: {3}',
                            announced.service, announced.action, key, event.data
                        )
            for key in removed:
                del self._unbound_keys[key]

    def remove_announced(self, announced: BoundServiceActionSchema) -> bool:
        with self.__lock:
            if announced not in self._announced:
                return False
            self._announced.remove(announced)
            removed: List[str] = []
            for key, event in self._key_data_map.items():
                if _event_schema_match(event, announced):
                    removed.append(key)
                    self._unbound_keys[key] = event
            for key in removed:
                del self._key_data_map[key]
            return True

    def add_hotkey(self, target_id: ParticipantId, hotkey_sequence: str, data: BoundServiceActionData) -> None:
        event = RegisteredHotkeyEvent(hotkey_sequence, target_id, data)
        with self.__lock:
            # First, see if it's been registered and if it's valid.
            for announced in self._announced:
                if _event_schema_match(event, announced):
                    if not _is_valid_schema_data(announced, event.data):
                        log(
                            WARN, HotkeyState,
                            'Service {0} hotkey action {1} does not match requested hotkey {2}: {3}',
                            announced.service, announced.action, hotkey_sequence, event.data
                        )
                        self._unbound_keys[hotkey_sequence] = event
                    else:
                        self._key_data_map[hotkey_sequence] = event
                    return
            # Nothing declares this kind of event yet.
            self._unbound_keys[hotkey_sequence] = event

    def remove_hotkey(self, hotkey_sequence: str) -> bool:
        ret = False
        with self.__lock:
            if hotkey_sequence in self._key_data_map:
                del self._key_data_map[hotkey_sequence]
                ret = True
            if hotkey_sequence in self._unbound_keys:
                del self._unbound_keys[hotkey_sequence]
                ret = True
        return ret

    def get_hotkey_event(self, hotkey_sequence: str) -> Optional[RegisteredHotkeyEvent]:
        with self.__lock:
            return self._key_data_map.get(hotkey_sequence, None)


def _schema_src_match(first: BoundServiceActionSchema, second: BoundServiceActionSchema) -> bool:
    return first.service == second.service and first.action == second.action


def _event_schema_match(event: RegisteredHotkeyEvent, schema: BoundServiceActionSchema) -> bool:
    return event.target_id == schema.service and event.data.action == schema.action


def _is_valid_schema_data(schema: BoundServiceActionSchema, data: BoundServiceActionData) -> bool:
    # TODO check the schema for validity.
    return True
