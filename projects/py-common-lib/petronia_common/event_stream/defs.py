
"""
Type definitions for the event stream.
"""

from typing import Tuple, Dict, Union, Any, cast, Protocol


# RawBinaryReader = Callable[[Optional[int]], bytes]
class RawBinaryReader(Protocol):
    """Function to read binary data, up to a maximum number of bytes per call."""
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
    """Returns the event object data type with the named arguments.
    Makes tuple creation a snap!"""
    return event_id, source_id, target_id, True, object_data


def to_raw_event_binary(
        event_id: str, source_id: str, target_id: str, binary_data_reader: RawBinaryReader,
) -> RawEventBinary:
    """Returns the binary blob event type with named arguments.
    Makes tuple creation a snap!"""
    return event_id, source_id, target_id, False, binary_data_reader


def raw_event_id(raw_event: RawEvent) -> str:
    """Returns the event tuple's event ID."""
    return raw_event[0]


def raw_event_source_id(raw_event: RawEvent) -> str:
    """Returns the event tuple's source ID."""
    return raw_event[1]


def raw_event_target_id(raw_event: RawEvent) -> str:
    """Returns the event tuple's target ID."""
    return raw_event[2]


def is_raw_event_object(raw_event: RawEvent) -> bool:
    """Returns whether the event tuple represents an event object."""
    return raw_event[3] is True


def is_raw_event_binary(raw_event: RawEvent) -> bool:
    """Returns whether the event tuple represents a binary blob."""
    return raw_event[3] is False


def as_raw_event_object_data(raw_event: RawEvent) -> MarshalledEventObject:
    """Performs an assertion (!) that the type is indeed an event object, and returns
    that event object value.  You MUST check that it's an event object before calling this."""
    assert raw_event[3] is True
    return cast(RawEventObject, raw_event)[4]


def as_raw_event_binary_data_reader(raw_event: RawEvent) -> RawBinaryReader:
    """Performs an assertion (!) that the type is indeed a binary blob, and
    returns that blob's reader.  You MUST check that it's a binary blob type before calling."""
    assert raw_event[3] is False
    return cast(RawEventBinary, raw_event)[4]
