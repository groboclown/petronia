
"""
Type definitions for the event stream.
"""

from typing import Tuple, Dict, Union, Any, cast, Protocol


# RawBinaryReader = Callable[[Optional[int]], bytes]
class RawBinaryReader(Protocol):
    def __call__(self, max_read_count: int = -1) -> bytes: ...


# What it should be ...
# MarshalledEventObjectData = Union[
#     str, int, float, None,
#     Sequence['MarshalledEventObjectData'], Dict[str, 'MarshalledEventObjectData'],
# ]
# MarshalledEventObject = Dict[str, MarshalledEventObjectData]
# What non-cyclic type definitions require...  sigh.
MarshalledEventObject = Dict[str, Any]
RawEventObject = Tuple[str, str, str, bool, MarshalledEventObject]
RawEventBinary = Tuple[str, str, str, bool, RawBinaryReader]
RawEvent = Union[RawEventObject, RawEventBinary]


def to_raw_event_object(
        event_id: str, source_id: str, target_id: str, object_data: MarshalledEventObject,
) -> RawEventObject:
    return event_id, source_id, target_id, True, object_data


def to_raw_event_binary(
        event_id: str, source_id: str, target_id: str, binary_data_reader: RawBinaryReader,
) -> RawEventBinary:
    return event_id, source_id, target_id, False, binary_data_reader


def raw_event_id(raw_event: RawEvent) -> str:
    return raw_event[0]


def raw_event_source_id(raw_event: RawEvent) -> str:
    return raw_event[1]


def raw_event_target_id(raw_event: RawEvent) -> str:
    return raw_event[2]


def is_raw_event_object(raw_event: RawEvent) -> bool:
    return raw_event[3] is True


def is_raw_event_binary(raw_event: RawEvent) -> bool:
    return raw_event[3] is False


def as_raw_event_object_data(raw_event: RawEvent) -> MarshalledEventObject:
    assert raw_event[3] is True
    return cast(RawEventObject, raw_event)[4]


def as_raw_event_binary_data_reader(raw_event: RawEvent) -> RawBinaryReader:
    assert raw_event[3] is False
    return cast(RawEventBinary, raw_event)[4]
