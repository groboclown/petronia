
"""
Reads low-level streaming event data.
"""

from typing import Callable, BinaryIO, Tuple, List, Dict, Optional, Any
import json
from petronia_common.util import i18n as _
from .defs import RawEvent, RawBinaryReader, to_raw_event_binary, to_raw_event_object
from ..util import PetroniaReturnError, UserMessage, possible_error, join_errors


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
    marked_stream = MarkedStreamReader(stream)
    while True:
        raw_event, error, eof = parse_raw_event(marked_stream)
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


class MarkedStreamReader:
    """Special stream reader class to prevent multiple execution paths from
    walking over the stream.  This allows it to be shared while ensuring correct
    read order.
    """
    __slots__ = ('__last_mark', '__stream', '__current')

    def __init__(self, stream: BinaryIO) -> None:
        self.__last_mark = 0
        self.__current = [0]
        self.__stream = stream

    def fork(self, count: int) -> 'MarkedStreamReader':
        ret = MarkedStreamReader(self.__stream)
        ret.__current = self.__current
        ret.__last_mark = self.__last_mark
        # Before this reads again, the forked one needs to read COUNT bytes.
        # And mask the size to limit how big the numbers get.
        self.__last_mark = (count + self.__last_mark) & 0xffffffff
        return ret

    def marked_read(self, count: int) -> bytes:
        if self.__last_mark != self.__current[0]:
            raise RuntimeError('Illegal out-of-order event stream read')
        self.__last_mark = (count + self.__last_mark) & 0xffffffff
        self.__current[0] = self.__last_mark
        return self.__stream.read(count)


def parse_raw_event(
        stream: MarkedStreamReader
) -> Tuple[Optional[RawEvent], Optional[PetroniaReturnError], bool]:
    """
    For performance, the parsing is smashed up into a single method, written to remove as many sub-if
    statements as possible.

    :param stream:
    :return: the raw event, if read; the errors in parsing, if read; whether it was an end-of-stream.
    """

    # See the documentation for details about the stream packet format.
    # STREAM = (anything) (PACKET_SEPARATOR) (EVENT_PACKET)
    # PACKET_SEPARATOR = 0x00 0x00 0x91
    # EVENT_PACKET = (EVENT_ID_STRING) (SOURCE_ID_STRING) (TARGET_ID_STRING) (DATA_CONTENTS)
    # EVENT_ID_STRING = 0x65 (STRING) ; 'e'
    # SOURCE_ID_STRING = 0x73 (STRING) ; 's'
    # TARGET_ID_STRING = 0x74 (STRING) ; 't'
    # DATA_CONTENTS = (JSON_CONTENTS) or (BINARY_CONTENTS)
    # JSON_CONTENTS = 0x7b (STRING) ; '{'
    # BINARY_CONTENTS = 0x5b (BLOB) ; '['
    # STRING = (size octet 1) (size octet 2) (size number of octets)
    # BLOB = (size octet 1) (size octet 2) (size octet 3) (size number of octets)

    error_messages: List[UserMessage] = []
    state = STATE_INIT

    while True:
        # A general state loop, looking for the packet start.
        # To be fully resilient to errors, we could maintain a buffer of read data,
        # and on error, go back and look for the marker.  But that seems like overkill.
        c = stream.marked_read(1)
        if c == EMPTY_BINARY:
            # End-of-stream reached.
            if state != STATE_INIT:
                # We've read some of the stream.
                error_messages.append(UserMessage(
                    _("Reached end-of-stream before packet start"),
                    state=state,
                ))
                return None, join_errors(*error_messages), True
            return None, None, True

        # ===================================================================
        # Start of Packet Search
        elif state == STATE_INIT:
            if c == BINARY_PACKET_MARKER_1:
                state = STATE_EXPECTING_MARKER_2
            # else - ignore; we remain in the init state
        elif state == STATE_EXPECTING_MARKER_2:
            if c == BINARY_PACKET_MARKER_2:
                state = STATE_EXPECTING_MARKER_3
            else:
                # didn't see the marker.
                return None, None, False

        elif state == STATE_EXPECTING_MARKER_3:
            if c == BINARY_PACKET_MARKER_3:
                # Move on to packet parsing.
                state = STATE_EVENT_ID_EXPECTING_MARKER
                break
            else:
                # didn't see the marker.
                return None, None, False

        else:
            raise RuntimeError('Invalid state')

    assert state == STATE_EVENT_ID_EXPECTING_MARKER

    def read_stream(count: int) -> Tuple[Optional[PetroniaReturnError], bytes]:
        read_data = b''
        while count > 0:
            next_data = stream.marked_read(count)
            if next_data == EMPTY_BINARY:
                error_messages.append(UserMessage(_("Reached end-of-stream during packet read")))
                return join_errors(*error_messages), read_data
            count -= len(next_data)
            read_data += next_data
        return None, read_data

    def advance_stream(count: int) -> Optional[PetroniaReturnError]:
        while count > 0:
            # Because this is throwing away data, don't read in too much at once.
            next_data = stream.marked_read(min(65535, count))
            if next_data == EMPTY_BINARY:
                error_messages.append(UserMessage(_("Reached end-of-stream during packet read")))
                return join_errors(*error_messages)
            count -= len(next_data)
        return None

    # =======================================================================
    # Event ID parsing.
    # Start by reading the marker + 2 length bytes.
    ret_err, c = read_stream(3)
    if ret_err:
        return None, ret_err, True
    if c[0] != BINARY_EVENT_ID_MARKER_INT:
        # didn't see the marker.  At this point, it's no longer
        # okay to just assume there's line noise.
        return None, join_errors(UserMessage(_("Unexpected data in the event stream"))), False

    decoded_event_id = ''
    event_id_remaining = (c[1] << 8) + c[2]
    if event_id_remaining <= 0:
        # Invalid size.
        # However, we'll keep reading.
        error_messages.append(UserMessage(
            _("event-id must have a length in the range [1, {m}]"),
            m=MAX_ID_SIZE,
        ))
    elif event_id_remaining > MAX_ID_SIZE:
        # Invalid size.
        # However, we'll keep reading.
        error_messages.append(UserMessage(
            _("event-id must have a length in the range [1, {m}]"),
            m=MAX_ID_SIZE,
        ))
        ret_err = advance_stream(event_id_remaining)
        if ret_err:
            return None, ret_err, True
    else:
        ret_err, c = read_stream(event_id_remaining)
        if ret_err:
            return None, ret_err, True
        try:
            decoded_event_id = c.decode("utf-8")
        except UnicodeDecodeError as e:
            # On decode error, keep going.  We need to parse
            # the whole packet regardless of this error.
            error_messages.append(UserMessage(_("event-id included invalid UTF-8 encoding"), e=str(e)))

    # =======================================================================
    # Source ID
    # Start by reading the marker + 2 length bytes.
    decoded_source_id = ''
    ret_err, c = read_stream(3)
    if ret_err:
        return None, ret_err, True
    if c[0] != BINARY_SOURCE_ID_MARKER_INT:
        # didn't see the marker.  At this point, it's no longer
        # okay to just assume there's line noise.
        # Ignore the other error messages, as they are meaningless here.
        return None, join_errors(UserMessage(_("Unexpected data in the event stream"))), False

    source_id_remaining = (c[1] << 8) + c[2]
    if source_id_remaining <= 0:
        # Invalid size.
        # However, we'll keep reading.
        error_messages.append(UserMessage(
            _("source-id must have a length in the range [1, {m}]"),
            m=MAX_ID_SIZE,
        ))
    elif source_id_remaining > MAX_ID_SIZE:
        # Invalid size.
        # However, we'll keep reading.
        error_messages.append(UserMessage(
            _("source-id must have a length in the range [1, {m}]"),
            m=MAX_ID_SIZE,
        ))
        ret_err = advance_stream(source_id_remaining)
        if ret_err:
            return None, ret_err, True
    else:
        ret_err, c = read_stream(source_id_remaining)
        if ret_err:
            return None, ret_err, True
        try:
            decoded_source_id = c.decode("utf-8")
        except UnicodeDecodeError as e:
            # On decode error, keep going.  We need to parse
            # the whole packet regardless of this error.
            error_messages.append(UserMessage(_("source-id included invalid UTF-8 encoding"), e=str(e)))

    # =======================================================================
    # Target ID
    # Start by reading the marker + 2 length bytes.
    decoded_target_id = ''
    ret_err, c = read_stream(3)
    if ret_err:
        return None, ret_err, True
    if c[0] != BINARY_TARGET_ID_MARKER_INT:
        # didn't see the marker.  At this point, it's no longer
        # okay to just assume there's line noise.
        # Ignore the other error messages, as they are meaningless here.
        return None, join_errors(UserMessage(_("Unexpected data in the event stream"))), False

    target_id_remaining = (c[1] << 8) + c[2]
    if target_id_remaining <= 0:
        # Invalid size.
        # However, we'll keep reading.
        error_messages.append(UserMessage(
            _("target-id must have a length in the range [1, {m}]"),
            m=MAX_ID_SIZE,
        ))
    elif target_id_remaining > MAX_ID_SIZE:
        # Invalid size.
        # However, we'll keep reading.
        error_messages.append(UserMessage(
            _("target-id must have a length in the range [1, {m}]"),
            m=MAX_ID_SIZE,
        ))
        ret_err = advance_stream(target_id_remaining)
        if ret_err:
            return None, ret_err, True
    else:
        ret_err, c = read_stream(target_id_remaining)
        if ret_err:
            return None, ret_err, True
        try:
            decoded_target_id = c.decode("utf-8")
        except UnicodeDecodeError as e:
            # On decode error, keep going.  We need to parse
            # the whole packet regardless of this error.
            error_messages.append(UserMessage(_("target-id included invalid UTF-8 encoding"), e=str(e)))

    # =======================================================================
    # Content Type Detection
    # Start by reading the marker by itself
    # Reading 1 byte, so easy reading...
    c = stream.marked_read(1)
    if c == EMPTY_BINARY:
        error_messages.append(UserMessage(_("Reached end-of-stream during packet read")))
        return None, join_errors(*error_messages), True
    elif c == BINARY_JSON_CONTENTS_MARKER:
        # ===================================================================
        # Json Reading

        # Read in the size first...
        ret_err, c = read_stream(2)
        if ret_err:
            return None, ret_err, True
        data_contents_length = (c[0] << 8) + c[1]
        if data_contents_length <= 0:
            # Invalid size.
            error_messages.append(UserMessage(
                _("json data must have a length in the range [2, {m}]"),
                m=MAX_JSON_SIZE,
            ))
            # Because this is the end of the packet, we'll stop here.
            return None, possible_error(messages=error_messages), False
        elif data_contents_length > MAX_JSON_SIZE:
            # Invalid size.
            # But we'll keep reading.
            error_messages.append(UserMessage(
                _("json data must have a length in the range [1, {m}]"),
                m=MAX_JSON_SIZE,
            ))
            ret_err = advance_stream(data_contents_length)
            if ret_err:
                return None, ret_err, True
            return None, possible_error(messages=error_messages), False
        ret_err, c = read_stream(data_contents_length)
        if ret_err:
            return None, ret_err, True

        event_data: Optional[Dict[str, Any]]
        try:
            event_data = json.loads(c)
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
        if error_messages:
            return None, join_errors(*error_messages), False
        # MyPy assertion guaranteeing the if-block above.
        assert isinstance(event_data, dict)
        return (
            to_raw_event_object(decoded_event_id, decoded_source_id, decoded_target_id, event_data),
            None,
            False,
        )

    elif c == BINARY_BLOB_CONTENTS_MARKER:
        # ===================================================================
        # Blob Reading

        # read in the size first
        ret_err, c = read_stream(3)
        if ret_err:
            return None, ret_err, True
        data_contents_length = (c[0] << 16) + (c[1] << 8) + c[2]
        if data_contents_length <= 0:
            # This size is acceptable.
            # Note that we can't pass this on to invalid state,
            # because the error message, if any, needs to be
            # returned, without a next-byte read.
            if error_messages:
                return None, join_errors(*error_messages), False
            return (
                # Just hard-code the empty reader here.
                to_raw_event_binary(decoded_event_id, decoded_source_id, decoded_target_id, empty_reader),
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
            ret_err = advance_stream(data_contents_length)
            if ret_err:
                return None, ret_err, True
            return None, join_errors(*error_messages), False
        else:
            # Read all the blob contents through a reader, to take
            # advantage of possible memory savings.

            # This returns immediately, so we don't need to keep
            # track of the marks loaded by the get_reader call.
            return (
                to_raw_event_binary(
                    decoded_event_id, decoded_source_id, decoded_target_id,
                    get_reader(stream, data_contents_length),
                ),
                None,
                False,
            )

    else:
        # ===================================================================
        # Invalid Packet Data

        # didn't see a valid marker.  At this point, it's no longer
        # okay to just assume there's line noise.
        # Ignore the other errors, as they are meaningless now.
        return None, join_errors(UserMessage(_("Unexpected data in the event stream"))), False


def get_reader(marked_stream: MarkedStreamReader, data_size: int) -> RawBinaryReader:
    if data_size <= 0:
        return empty_reader

    # In-memory pipe
    if data_size < MEMORY_READER_SIZE:
        return static_reader(marked_stream.marked_read(data_size))

    # This is very, very unsafe in the general case.
    #   A poorly written application could fetch the object,
    #   and keep it around, unread, while the next event is
    #   processed.  The stream is "marked" with a number,
    #   to tell if the stream is ever read by something else.

    # If it turns out this becomes a problem, then an alternate method,
    #   like a disk cache, may be necessary.

    return piped_reader(marked_stream=marked_stream.fork(data_size), data_size=data_size)


# noinspection PyUnusedLocal
def empty_reader(max_read_count: int = -1) -> bytes:
    return EMPTY_BINARY


def static_reader(data: bytes) -> RawBinaryReader:
    # A memory conservative version of a reader.
    # It loads the initial data entirely in memory, but then
    # removes it after it's been read.
    remainder = [data, len(data)]

    def reader_func(max_read_count: int = -1) -> bytes:
        remaining_length: int = remainder[1]  # type: ignore
        if remaining_length <= 0:
            return EMPTY_BINARY
        end: int
        if max_read_count <= 0:
            end = remaining_length
        else:
            end = min(remaining_length, max_read_count)
        remaining_data: bytes = remainder[0]  # type: ignore
        ret: bytes = remaining_data[:end]
        remaining_data = remaining_data[end:]
        remainder[0] = remaining_data
        remainder[1] = len(remaining_data)
        return ret

    return reader_func


def piped_reader(marked_stream: MarkedStreamReader, data_size: int) -> RawBinaryReader:
    context: List[int] = [data_size]

    def reader_func(max_read_count: int = -1) -> bytes:
        if context[0] <= 0:
            return EMPTY_BINARY
        if max_read_count <= 0 or max_read_count >= context[0]:
            expected_read_count = context[0]
        else:
            expected_read_count = max_read_count
        ret = marked_stream.marked_read(expected_read_count)
        context[0] = max(0, context[0] - len(ret))
        return ret

    return reader_func


BINARY_PACKET_MARKER_1 = b'\0'
BINARY_PACKET_MARKER_2 = b'\0'
BINARY_PACKET_MARKER_3 = b'['
BINARY_EVENT_ID_MARKER_INT = ord('e')
BINARY_SOURCE_ID_MARKER_INT = ord('s')
BINARY_TARGET_ID_MARKER_INT = ord('t')
BINARY_JSON_CONTENTS_MARKER = b'{'
BINARY_BLOB_CONTENTS_MARKER = b'['
EMPTY_BINARY = b''

MAX_ID_SIZE = 2047
MAX_JSON_SIZE = 65535
MAX_BLOB_SIZE = 10485760

MEMORY_READER_SIZE = 1024 * 1024


STATE_INIT = 0

STATE_EXPECTING_MARKER_2 = 2
STATE_EXPECTING_MARKER_3 = 3

STATE_EVENT_ID_EXPECTING_MARKER = 10
