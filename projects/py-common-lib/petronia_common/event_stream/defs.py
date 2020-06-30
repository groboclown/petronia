
"""
Type definitions for the event stream.
"""

from typing import Tuple, Dict, Union, Any, Callable, Optional, cast


RawEventObject = Tuple[str, str, bool, Dict[str, Any]]
RawBinaryReader = Callable[[Optional[int]], bytes]
RawEventBinary = Tuple[str, str, bool, RawBinaryReader]
RawEvent = Union[RawEventObject, RawEventBinary]


def to_raw_event_object(event_id: str, target_id: str, object_data: Dict[str, Any]) -> RawEventObject:
    return event_id, target_id, True, object_data


def to_raw_event_binary(event_id: str, target_id: str, binary_data_reader: RawBinaryReader) -> RawEventBinary:
    return event_id, target_id, False, binary_data_reader


def raw_event_id(raw_event: RawEvent) -> str:
    return raw_event[0]


def raw_event_target_id(raw_event: RawEvent) -> str:
    return raw_event[1]


def is_raw_event_object(raw_event: RawEvent) -> bool:
    return raw_event[2] is True


def is_raw_event_binary(raw_event: RawEvent) -> bool:
    return raw_event[2] is False


def as_raw_event_object_data(raw_event: RawEvent) -> Dict[str, Any]:
    assert raw_event[2] is True
    return cast(RawEventObject, raw_event)[3]


def as_raw_event_binary_data_reader(raw_event: RawEvent) -> RawBinaryReader:
    assert raw_event[2] is False
    return cast(RawEventBinary, raw_event)[3]
