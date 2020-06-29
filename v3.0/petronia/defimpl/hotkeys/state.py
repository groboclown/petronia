
"""
Hotkey state.
"""

from typing import Dict, List, Sequence, Tuple, Optional
from threading import Lock
from ...aid.std import i18n as _
from ...aid.std import (
    ErrorReport,
    create_user_error,
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
    _key_data_map: Dict[str, Tuple[RegisteredHotkeyEvent, BoundServiceActionSchema]]

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
            all_keys: List[RegisteredHotkeyEvent] = (
                [x for x in self._unbound_keys.values()] +
                [x[0] for x in self._key_data_map.values()]
            )
            return HotkeyEventState(all_keys, tuple(self._announced))

    def get_platform_keys(self) -> Dict[str, str]:
        keys: Dict[str, str] = {}
        with self.__lock:
            for key in self._key_data_map.keys():
                keys[key] = key
        return keys

    def add_announced(self, announced: BoundServiceActionSchema) -> Sequence[ErrorReport]:
        with self.__lock:
            ret: List[ErrorReport] = []
            removed: List[str] = []
            for idx in range(len(self._announced)):
                if _schema_src_match(self._announced[idx], announced):
                    self._announced[idx] = announced
                    for key, event in self._key_data_map.items():
                        if not _is_valid_schema_data(announced, event[0].data):
                            ret.append(create_user_error(
                                HotkeyState,
                                _(
                                    'Service {service} hotkey action {action} does not match '
                                    'requested hotkey {hotkey}: {data}'
                                ),
                                service=announced.service,
                                action=announced.action,
                                hotkey=key,
                                data=repr(event[0].data)
                            ))
                            removed.append(key)
                            self._unbound_keys[key] = event[0]
                    for key in removed:
                        del self._key_data_map[key]
                    return ret

            self._announced.append(announced)
            for key, raw in self._unbound_keys.items():
                if _event_schema_match(raw, announced):
                    if _is_valid_schema_data(announced, raw.data):
                        self._key_data_map[key] = (raw, announced,)
                        removed.append(key)
                    else:
                        ret.append(create_user_error(
                            HotkeyState,
                            _(
                                'Service {service} hotkey action {action} does not match '
                                'requested hotkey {hotkey}: {data}'
                            ),
                            service=announced.service,
                            action=announced.action,
                            hotkey=key,
                            data=repr(raw.data)
                        ))
            for key in removed:
                del self._unbound_keys[key]
            return ret

    def remove_announced(self, announced: BoundServiceActionSchema) -> bool:
        with self.__lock:
            if announced not in self._announced:
                return False
            self._announced.remove(announced)
            removed: List[str] = []
            for key, binding in self._key_data_map.items():
                if _event_schema_match(binding[0], announced):
                    removed.append(key)
                    self._unbound_keys[key] = binding[0]
            for key in removed:
                del self._key_data_map[key]
            return True

    def add_hotkey(self, hotkey_sequence: str, data: BoundServiceActionData) -> Sequence[ErrorReport]:
        ret: List[ErrorReport] = []
        event = RegisteredHotkeyEvent(hotkey_sequence, data)
        with self.__lock:
            # First, see if it's been registered and if it's valid.
            for announced in self._announced:
                if _event_schema_match(event, announced):
                    if not _is_valid_schema_data(announced, event.data):
                        ret.append(create_user_error(
                            HotkeyState,
                            _(
                                'Service {service} hotkey action {action} does not match '
                                'requested hotkey {hotkey}: {data}'
                            ),
                            service=announced.service,
                            action=announced.action,
                            hotkey=hotkey_sequence,
                            data=repr(event.data)
                        ))
                        self._unbound_keys[hotkey_sequence] = event
                    else:
                        self._key_data_map[hotkey_sequence] = (event, announced,)
                    return ret
            # Nothing declares this kind of event yet.
            self._unbound_keys[hotkey_sequence] = event
        return ret

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

    def clear_hotkeys(self) -> None:
        with self.__lock:
            self._key_data_map.clear()

    def get_hotkey_event(
            self, hotkey_sequence: str
    ) -> Optional[Tuple[RegisteredHotkeyEvent, BoundServiceActionSchema]]:
        with self.__lock:
            return self._key_data_map.get(hotkey_sequence, None)


def _schema_src_match(first: BoundServiceActionSchema, second: BoundServiceActionSchema) -> bool:
    return first.service == second.service and first.action == second.action


def _event_schema_match(event: RegisteredHotkeyEvent, schema: BoundServiceActionSchema) -> bool:
    return event.data.action == schema.action


def _is_valid_schema_data(_schema: BoundServiceActionSchema, _data: BoundServiceActionData) -> bool:
    # TODO check the schema for validity.
    return True
