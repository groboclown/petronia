
"""
Reads low-level streaming event data.
"""

from typing import Callable, BinaryIO, Tuple, List, Dict, Optional, Any
import json
from petronia_common.util import i18n as _
from .defs import RawEvent, RawBinaryReader, to_raw_event_binary, to_raw_event_object
from ..util import PetroniaReturnError, UserMessage, as_error, possible_error


def read_event_stream(
        stream: BinaryIO,
        event_listener: Callable[[RawEvent], bool],
        end_of_stream_listener: Callable[[], None],
        error_listener: Callable[[PetroniaReturnError], bool],
) -> None:
    """
    Reads the events from the stream.  Each read event will be sent to the listener.
    When the stream is closed, the listener will be sent a None object, then not called again
    by this function.  If the listener returns True, then this function will stop reading
    any more events.

    This function will never close the stream by itself.  If an error is encountered while
    reading the event data, the reader will attempt to recover as best as it can, then
    call the listener with an error argument.

    :param error_listener:
    :param end_of_stream_listener:
    :param event_listener:
    :param stream:
    :return:
    """
    while True:
        raw_event, error, eof = parse_raw_event(stream)
        if error:
            # error parsing an event.
            if error_listener(error):
                return
        if raw_event:
            # raw data parsed
            if event_listener(raw_event):
                return
        if eof:
            # End-of-stream
            end_of_stream_listener()
            return


def parse_raw_event(stream: BinaryIO) -> Tuple[Optional[RawEvent], Optional[PetroniaReturnError], bool]:
    """
    For performance, the parsing is smashed up into a single method, written to remove as many sub-if
    statements as possible.

    :param stream:
    :return: the raw event, if read; the errors in parsing, if read; whether it was an end-of-stream.
    """

    # STREAM = (anything) (PACKET_SEPARATOR) (EVENT_PACKET)
    # PACKET_SEPARATOR = 0x00 0x00 0x91
    # EVENT_PACKET = (EVENT_ID_STRING) (TARGET_ID_STRING) (DATA_CONTENTS)
    # EVENT_ID_STRING = 0x65 (STRING) ; 'e'
    # TARGET_ID_STRING = 0x74 (STRING) ; 't'
    # DATA_CONTENTS = (JSON_CONTENTS) or (BINARY_CONTENTS)
    # JSON_CONTENTS = 0x7b (STRING) ; '{'
    # BINARY_CONTENTS = 0x5b (BLOB) ; '['
    # STRING = (size octet 1) (size octet 2) (size number of octets)
    # BLOB = (size octect 1) (size octet 2) (size octet 3) (size octet 4) (size number of octets)

    error_messages: List[UserMessage] = []
    event_id_remaining = 0
    event_id = b''
    decoded_event_id = ''
    target_id_remaining = 0
    target_id = b''
    decoded_target_id = ''
    data_contents_length = 0
    data_contents = b''
    state = STATE_INIT

    # Should use this to read, but that means blocking any other parser
    # until the caller has finished reading this.  That leads to a bad situation.
    def as_reader_func(count: int) -> RawBinaryReader:
        remaining = [count]

        def reader_func(max_count: Optional[int] = -1) -> bytes:
            if remaining[0] <= 0:
                return b''
            if max_count <= 0 or max_count >= remaining[0]:
                expected_read_count = remaining[0]
            else:
                expected_read_count = max_count
            ret = stream.read(expected_read_count)
            remaining[0] = max(0, remaining[0] - len(ret))
            return ret

        return reader_func

    while True:
        c = stream.read(1)
        if c == b'':
            # End-of-stream reached.
            if state != STATE_INIT:
                # We've read some of the stream.
                error_messages.append(UserMessage(
                    _("Reached end-of-stream before packet end ({state})"),
                    state=state,
                ))
                return (
                    None,
                    as_error(*error_messages),
                    True,
                )
            return None, None, True

        # ===================================================================
        # Start of Packet Search
        if state == STATE_INIT:
            if c == BINARY_PACKET_MARKER_1:
                state = STATE_EXPECTING_MARKER_2
                print("1")
            # else - ignore; we remain in the init state
        elif state == STATE_EXPECTING_MARKER_2:
            if c == BINARY_PACKET_MARKER_2:
                state = STATE_EXPECTING_MARKER_3
                print("2")
            else:
                # didn't see the marker.
                return None, None, False

        elif state == STATE_EXPECTING_MARKER_3:
            if c == BINARY_PACKET_MARKER_3:
                state = STATE_EVENT_ID_EXPECTING_MARKER
                print("3")
            else:
                # didn't see the marker.
                return None, None, False

        elif state == STATE_EVENT_ID_EXPECTING_MARKER:
            if c == BINARY_EVENT_ID_MARKER:
                state = STATE_EVENT_ID_SIZE_1
                print("4")
            else:
                # didn't see the marker.  At this point, it's no longer
                # okay to just assume there's line noise.
                return None, as_error(UserMessage(_("Unexpected data in the event stream"))), False

        # ===================================================================
        # Event ID
        elif state == STATE_EVENT_ID_SIZE_1:
            event_id_remaining = ord(c) << 8
            state = STATE_EVENT_ID_SIZE_2

        elif state == STATE_EVENT_ID_SIZE_2:
            event_id_remaining += ord(c)
            if event_id_remaining <= 0:
                # Invalid size.
                # However, we'll keep reading.
                error_messages.append(UserMessage(
                    _("event-id must have a length in the range [1, {m}]"),
                    m=MAX_ID_SIZE,
                ))
                # Note that we skip the event id content reading.
                state = STATE_TARGET_ID_EXPECTING_MARKER
            elif event_id_remaining > MAX_ID_SIZE:
                # Invalid size.
                # However, we'll keep reading.
                error_messages.append(UserMessage(
                    _("event-id must have a length in the range [1, {m}]"),
                    m=MAX_ID_SIZE,
                ))
                state = STATE_INVALID_EVENT_ID_CONTENTS
            else:
                state = STATE_EVENT_ID_CONTENTS

        elif state == STATE_EVENT_ID_CONTENTS:
            event_id += c
            event_id_remaining -= 1
            if event_id_remaining <= 0:
                try:
                    decoded_event_id = event_id.decode("utf-8")
                except UnicodeDecodeError as e:
                    # On decode error, keep going.  We need to parse
                    # the whole packet regardless of this error.
                    error_messages.append(UserMessage(_("event-id included invalid UTF-8 encoding"), e=str(e)))

                state = STATE_TARGET_ID_EXPECTING_MARKER

        elif state == STATE_INVALID_EVENT_ID_CONTENTS:
            # read in the data, but don't keep it.
            event_id_remaining -= 1
            if event_id_remaining <= 0:
                state = STATE_TARGET_ID_EXPECTING_MARKER

        # ===================================================================
        # Target ID

        elif state == STATE_TARGET_ID_EXPECTING_MARKER:
            if c == BINARY_TARGET_ID_MARKER:
                state = STATE_TARGET_ID_SIZE_1
            else:
                # didn't see the marker.  At this point, it's no longer
                # okay to just assume there's line noise.
                # Ignore the other error messages, as they are meaningless here.
                return None, as_error(UserMessage(_("Unexpected data in the event stream"))), False

        elif state == STATE_TARGET_ID_SIZE_1:
            target_id_remaining = ord(c) << 8
            state = STATE_TARGET_ID_SIZE_2

        elif state == STATE_TARGET_ID_SIZE_2:
            target_id_remaining += ord(c)
            if target_id_remaining <= 0:
                # Invalid size.
                # However, we'll keep reading.
                error_messages.append(UserMessage(
                    _("target-id must have a length in the range [1, {m}]"),
                    m=MAX_ID_SIZE,
                ))
                # Note that we skip the target id content reading.
                state = STATE_CONTENT_TYPE_EXPECTING_MARKER
            elif target_id_remaining > MAX_ID_SIZE:
                # Invalid size.
                # However, we'll keep reading.
                error_messages.append(UserMessage(
                    _("target-id must have a length in the range [1, {m}]"),
                    m=MAX_ID_SIZE,
                ))
                state = STATE_INVALID_TARGET_ID_CONTENTS
            else:
                state = STATE_TARGET_ID_CONTENTS

        elif state == STATE_TARGET_ID_CONTENTS:
            target_id += c
            target_id_remaining -= 1
            if target_id_remaining <= 0:
                try:
                    decoded_target_id = target_id.decode("utf-8")
                except UnicodeDecodeError as e:
                    # On decode error, keep going.  We need to parse
                    # the whole packet regardless of this error.
                    error_messages.append(UserMessage(_("target-id included invalid UTF-8 encoding"), e=str(e)))

                state = STATE_CONTENT_TYPE_EXPECTING_MARKER

        elif state == STATE_INVALID_TARGET_ID_CONTENTS:
            # read the data, but don't keep it
            target_id_remaining -= 1
            if target_id_remaining <= 0:
                state = STATE_CONTENT_TYPE_EXPECTING_MARKER

        # ===================================================================
        # Content Type Detection

        elif state == STATE_CONTENT_TYPE_EXPECTING_MARKER:
            if c == BINARY_JSON_CONTENTS_MARKER:
                state = STATE_JSON_SIZE_1
            elif c == BINARY_BLOB_CONTENTS_MARKER:
                state = STATE_BLOB_SIZE_1
            else:
                # didn't see the marker.  At this point, it's no longer
                # okay to just assume there's line noise.
                # Ignore the other errors, as they are meaningless now.
                return None, as_error(UserMessage(_("Unexpected data in the event stream"))), False

        # ===================================================================
        # Json Reading

        elif state == STATE_JSON_SIZE_1:
            data_contents_length = ord(c) << 8
            state = STATE_JSON_SIZE_2

        elif state == STATE_JSON_SIZE_2:
            data_contents_length += ord(c)
            if data_contents_length <= 0:
                # Invalid size.
                error_messages.append(UserMessage(
                    _("json data must have a length in the range [1, {m}]"),
                    m=MAX_JSON_SIZE,
                ))
                # Because this is the end of the packet, we'll stop here.
                return (
                    None,
                    possible_error(messages=error_messages),
                    False,
                )
            elif data_contents_length > MAX_JSON_SIZE:
                # Invalid size.
                # But we'll keep reading.
                error_messages.append(UserMessage(
                    _("json data must have a length in the range [1, {m}]"),
                    m=MAX_JSON_SIZE,
                ))
                state = STATE_INVALID_JSON_CONTENTS
            else:
                state = STATE_JSON_CONTENTS

        elif state == STATE_JSON_CONTENTS:
            data_contents += c
            data_contents_length -= 1
            if data_contents_length <= 0:
                event_data: Optional[Dict[str, Any]]
                try:
                    event_data = json.loads(data_contents)
                except UnicodeDecodeError as e:
                    event_data = None
                    error_messages.append(UserMessage(
                        _("Event streaming data included incorrectly encoded UTF-8 values: {e}"),
                        e=str(e),
                    ))
                except json.decoder.JSONDecodeError as e:
                    event_data = None
                    error_messages.append(UserMessage(
                        _("Event streaming data included badly formatted JSON data: {e}"),
                        e=str(e),
                    ))
                if not isinstance(event_data, dict):
                    error_messages.append(UserMessage(_("Event data was not sent as JSON dictionary")))
                if error_messages and event_data:
                    return (
                        None,
                        as_error(*error_messages),
                        False,
                    )
                return (
                    to_raw_event_object(decoded_event_id, decoded_target_id, event_data),
                    None,
                    False,
                )

        elif state == STATE_INVALID_JSON_CONTENTS:
            # Read the data, but don't keep it.
            data_contents_length -= 1
            if data_contents_length <= 0:
                return (
                    None,
                    as_error(*error_messages),
                    False,
                )

        # ===================================================================
        # Binary Blob Reading

        elif state == STATE_BLOB_SIZE_1:
            data_contents_length = ord(c) << 16
            state = STATE_BLOB_SIZE_2

        elif state == STATE_BLOB_SIZE_2:
            data_contents_length += ord(c) << 8
            state = STATE_BLOB_SIZE_3

        elif state == STATE_BLOB_SIZE_3:
            data_contents_length += ord(c)
            if data_contents_length <= 0:
                # This size is acceptable.
                if error_messages:
                    return (
                        None,
                        as_error(*error_messages),
                        False,
                    )
                return (
                    to_raw_event_binary(decoded_event_id, decoded_target_id, _empty_reader),
                    None,
                    False,
                )
            elif data_contents_length > MAX_BLOB_SIZE:
                # Invalid size.
                # However, we'll still read it.
                error_messages.append(UserMessage(
                    _("binary blob data must have a length in the range [1, {m}]"),
                    m=MAX_BLOB_SIZE,
                ))
                state = STATE_INVALID_BLOB_CONTENTS
            else:
                state = STATE_BLOB_CONTENTS

        elif state == STATE_BLOB_CONTENTS:
            data_contents += c
            data_contents_length -= 1
            if data_contents_length <= 0:
                if error_messages:
                    return (
                        None,
                        as_error(*error_messages),
                        False,
                    )
                return (
                    to_raw_event_binary(decoded_event_id, decoded_target_id, _static_reader(data_contents)),
                    None,
                    False,
                )

        elif state == STATE_INVALID_BLOB_CONTENTS:
            # Read the data, but don't keep it.
            data_contents_length -= 1
            if data_contents_length <= 0:
                return (
                    None,
                    as_error(*error_messages),
                    False,
                )

        # ===================================================================
        else:
            raise RuntimeError(f'invalid state {state}')


def _empty_reader(_max_count: Optional[int] = -1) -> bytes:
    return b''


def _static_reader(data: bytes) -> RawBinaryReader:
    pos = [0]
    data_len = len(data)

    def reader_func(max_count: Optional[int] = -1) -> bytes:
        start = pos[0]
        if start >= data_len:
            return b''
        end = min(data_len, start + max_count)
        pos[0] = end
        return data[start:end]

    return reader_func


BINARY_PACKET_MARKER_1 = b'\0'
BINARY_PACKET_MARKER_2 = b'\0'
BINARY_PACKET_MARKER_3 = b'['
BINARY_EVENT_ID_MARKER = b'e'
BINARY_TARGET_ID_MARKER = b't'
BINARY_JSON_CONTENTS_MARKER = b'{'
BINARY_BLOB_CONTENTS_MARKER = b'['

MAX_ID_SIZE = 2047
MAX_JSON_SIZE = 65535
MAX_BLOB_SIZE = 10485760


STATE_INIT = 0

STATE_EXPECTING_MARKER_2 = 2
STATE_EXPECTING_MARKER_3 = 3

STATE_EVENT_ID_EXPECTING_MARKER = 10
STATE_EVENT_ID_SIZE_1 = 11
STATE_EVENT_ID_SIZE_2 = 12
STATE_EVENT_ID_CONTENTS = 13
STATE_INVALID_EVENT_ID_CONTENTS = 101

STATE_TARGET_ID_EXPECTING_MARKER = 20
STATE_TARGET_ID_SIZE_1 = 21
STATE_TARGET_ID_SIZE_2 = 22
STATE_TARGET_ID_CONTENTS = 23
STATE_INVALID_TARGET_ID_CONTENTS = 102

STATE_CONTENT_TYPE_EXPECTING_MARKER = 30
STATE_JSON_SIZE_1 = 31
STATE_JSON_SIZE_2 = 32
STATE_JSON_CONTENTS = 33
STATE_INVALID_JSON_CONTENTS = 103
STATE_BLOB_SIZE_1 = 34
STATE_BLOB_SIZE_2 = 35
STATE_BLOB_SIZE_3 = 36
STATE_BLOB_CONTENTS = 38
STATE_INVALID_BLOB_CONTENTS = 104
