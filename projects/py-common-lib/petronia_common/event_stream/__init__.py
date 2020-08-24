
"""
Common code for handling raw event data streams.
"""

from .reader import read_event_stream
from .writer import write_binary_event_to_stream, write_object_event_to_stream, BinaryWriter
from .consts import BROADCAST_EVENT_TARGET_ID
from .defs import (
    RawEvent,
    RawEventObject,
    RawBinaryReader,
    RawEventBinary,
    raw_event_id,
    raw_event_target_id,
    raw_event_source_id,
    raw_event_binary_size,
    as_raw_event_binary_data_reader,
    as_raw_event_object_data,
    is_raw_event_binary,
    is_raw_event_object,
    MarshalledEventObject,
    to_raw_event_object,
    to_raw_event_binary,
)
from .forwarder import EventForwarderTarget, EventForwarder
