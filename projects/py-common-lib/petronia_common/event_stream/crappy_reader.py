
"""
Reads streaming event data.
"""

from typing import Callable, BinaryIO, Tuple, Union, Dict, List, Optional, Any
from petronia_common.util import i18n as _
from .defs import RawEvent, to_raw_event_binary, to_raw_event_object
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

    error_buffer = b''
    errors: List[UserMessage] = []
    object_stack: List[Tuple[int, Optional[str], Any]] = [()]
    payload_length = 0
    state = STATE_EXPECTING_START
    key: Optional[str] = None
    buf: Any = None

    # handler for the exceedingly common logic for handling an end-of-value
    # in an object
    def handle_end_of_value(
            value: Union[str, int, float, bool, None, List[Any], Dict[str, Any]],
    ) -> Tuple[int, Optional[str], Any]:
        next_state, key_val, buf_cache = object_stack.pop()
        if next_state == STATE_O_ARRAY_ON_VALUE:
            assert isinstance(buf_cache, List)
            buf_cache.append(value)
            return STATE_O_ARRAY_END_VALUE_SEARCH, None, buf_cache
        elif next_state == STATE_O_DICT_ON_KEY:
            if not isinstance(value, str):
                errors.append(UserMessage(_("Dictionary values can only be strings")))
                return STATE_O_DICT_COLON_SEARCH, '?', buf_cache
            else:
                return STATE_O_DICT_COLON_SEARCH, value, buf_cache
        elif next_state == STATE_O_DICT_ON_VALUE:
            buf_cache[key_val] = value
            return STATE_O_DICT_END_VALUE_SEARCH, None, buf_cache
        elif next_state == STATE_B_ON_EVENT_ID:
            if not isinstance(value, str):
                errors.append(UserMessage(_("event-id must be a string")))
                return STATE_B_BAD_1, None, None
            buf_cache['event-id'] = value
            return STATE_B_AFTER_EVENT_ID, None, buf_cache
        elif next_state == STATE_B_ON_TARGET_ID:
            if not isinstance(value, str):
                errors.append(UserMessage(_("target-id must be a string")))
                return STATE_B_BAD_1, None, None
            buf_cache['target-id'] = value
            return STATE_B_AFTER_TARGET_ID, None, buf_cache
        elif next_state == STATE_B_ON_LENGTH:
            if not isinstance(value, int):
                errors.append(UserMessage(_("blob length must be an integer")))
                return STATE_B_BAD_1, None, None
            nonlocal payload_length
            payload_length = value
            return STATE_B_AFTER_LENGTH, None, buf_cache
        elif next_state == STATE_END_OBJECT:
            return next_state, key_val, buf_cache
        else:
            # Internal error
            raise RuntimeError(f'Invalid event parser state {next_state}')

    def handle_value_separator(
            value_handle: Tuple[int, Optional[str], Any],
            separator: bytes,
    ) -> Tuple[int, Optional[str], Any]:
        # This could be condensed way down based on the conditions leading into this.
        nonlocal payload_length
        next_state, key_val, buf_cache = value_handle
        if next_state == STATE_O_ARRAY_END_VALUE_SEARCH:
            if separator == BINARY_VALUE_SEPARATOR_VAL:
                # move on to the next value
                object_stack.append((STATE_O_ARRAY_ON_VALUE, None, buf_cache,))
                return STATE_O_VALUE_SEARCH, None, None
            elif separator == BINARY_ARRAY_END_VAL:
                # Close off this array
                return handle_end_of_value(buf_cache)
            elif separator in BINARY_WHITESPACE_SET:
                return STATE_O_ARRAY_END_VALUE_SEARCH, None, buf_cache
            # special characters that indicate we can't correctly parse this
            elif separator == BINARY_DICT_END_VAL or separator == BINARY_KEY_VALUE_SEPARATOR_VAL:
                # unrecoverable state
                errors.append(UserMessage(_("Invalid character after a value in an array")))
                return STATE_O_BAD_1, None, None
            else:
                # invalid state; treated as a bad token
                errors.append(UserMessage(_("Invalid character after a value in an array")))
                object_stack.append((STATE_O_ARRAY_ON_VALUE, None, buf_cache,))
                return STATE_O_INVALID_TOKEN, None, None
        elif next_state == STATE_O_DICT_COLON_SEARCH:
            if separator in BINARY_WHITESPACE_SET:
                return STATE_O_DICT_COLON_SEARCH, key_val, buf_cache
            elif separator == BINARY_KEY_VALUE_SEPARATOR_VAL:
                object_stack.append((STATE_O_DICT_ON_VALUE, key_val, buf_cache,))
                return STATE_O_VALUE_SEARCH, None, None
            # special characters that indicate we can't correctly parse this
            elif separator == BINARY_ARRAY_END_VAL:
                # unrecoverable state
                errors.append(UserMessage(_("Invalid character after a key in a dictionary")))
                return STATE_O_BAD_1, None, None
            else:
                # invalid state; treated as a bad token
                errors.append(UserMessage(_("Unrecoverable error for invalid character after a key in a dictionary")))
                object_stack.append((STATE_O_DICT_ON_VALUE, key_val, buf_cache,))
                return STATE_O_INVALID_TOKEN, None, None
        elif next_state == STATE_O_DICT_END_VALUE_SEARCH:
            if separator in BINARY_WHITESPACE_SET:
                return STATE_O_DICT_END_VALUE_SEARCH, None, buf_cache
            elif separator == BINARY_VALUE_SEPARATOR_VAL:
                object_stack.append((STATE_O_DICT_ON_KEY, None, buf_cache,))
                return STATE_O_VALUE_SEARCH, None, None
            elif separator == BINARY_DICT_END_VAL:
                return handle_end_of_value(buf_cache)
            # special characters that indicate we can't correctly parse this
            elif separator == BINARY_ARRAY_END_VAL:
                # unrecoverable state
                errors.append(UserMessage(_("Invalid character after a value in a dictionary")))
                return STATE_O_BAD_1, None, None
            else:
                # invalid state; treated as a bad token
                errors.append(UserMessage(_("Unrecoverable error for invalid character after a value in a dictionary")))
                object_stack.append((STATE_O_DICT_END_VALUE_SEARCH, None, buf_cache,))
                return STATE_O_INVALID_TOKEN, None, None
        elif next_state == STATE_O_DICT_ON_KEY:
            # This should only happen on a {} statement.
            if separator == BINARY_DICT_END_VAL:
                return handle_end_of_value(buf_cache)
            else:
                # Bad input data, like `{]}`
                errors.append(UserMessage(_("Invalid character after a value in a dictionary")))
                return STATE_O_BAD_1, None, None
        elif next_state == STATE_O_ARRAY_ON_VALUE:
            # This should only happen on a [] statement.
            if separator == BINARY_ARRAY_END_VAL:
                return handle_end_of_value(buf_cache)
            else:
                # Bad input data, like `{"": [}`
                errors.append(UserMessage(_("Invalid character after a value in an array")))
                return STATE_O_BAD_1, None, None

        elif next_state == STATE_B_AFTER_EVENT_ID:
            if separator in BINARY_WHITESPACE_SET:
                return STATE_B_AFTER_EVENT_ID, None, buf_cache
            elif separator == BINARY_VALUE_SEPARATOR_VAL:
                object_stack.append((STATE_B_ON_TARGET_ID, None, buf_cache,))
                return STATE_O_VALUE_SEARCH, None, None
            elif separator == BINARY_ARRAY_END_VAL:
                errors.append(UserMessage(_("Invalid character after event value in binary blob")))
                nonlocal payload_length
                payload_length = 0
                return STATE_B_BAD_2, None, None
            else:
                # unrecoverable state
                errors.append(UserMessage(_("Invalid character after event value in binary blob")))
                return STATE_B_BAD_1, None, None
        elif next_state == STATE_B_AFTER_TARGET_ID:
            if separator in BINARY_WHITESPACE_SET:
                return STATE_B_AFTER_TARGET_ID, None, buf_cache
            elif separator == BINARY_VALUE_SEPARATOR_VAL:
                object_stack.append((STATE_B_ON_LENGTH, None, buf_cache,))
                return STATE_O_VALUE_SEARCH, None, None
            elif separator == BINARY_ARRAY_END_VAL:
                errors.append(UserMessage(_("Invalid character after target value in binary blob")))
                payload_length = 0
                return STATE_B_BAD_2, None, None
            else:
                # unrecoverable state
                errors.append(UserMessage(_("Invalid character after target value in binary blob")))
                return STATE_B_BAD_1, None, None
        elif next_state == STATE_B_AFTER_LENGTH:
            if separator in BINARY_WHITESPACE_SET:
                return STATE_B_AFTER_LENGTH, None, buf_cache
            elif separator == BINARY_VALUE_SEPARATOR_VAL:
                if payload_length == 0:
                    # Special case for 0-length payload
                    buf_cache = object_stack.pop()[2]
                    buf_cache['data'] = b''
                    return STATE_B_AFTER_PAYLOAD, None, buf_cache
                return STATE_B_PAYLOAD, None, b''
            elif separator == BINARY_ARRAY_END_VAL:
                errors.append(UserMessage(_("Invalid character after length value in binary blob")))
                payload_length = 0
                return STATE_B_BAD_1, None, None
            else:
                # unrecoverable state
                errors.append(UserMessage(_("Invalid character after length value in binary blob")))
                return STATE_B_BAD_1, None, None
        else:
            # Any other combination is a valid state.
            return next_state, key_val, buf_cache

    # From the Wikipedia page:
    # Byte Count   Codepoint Bits    Byte 1        Byte 2      Byte 3     Byte 4
    #          1                7    0xxxxxxx           -           -          -
    #          2               11    110xxxxx    10xxxxxx           -          -
    #          3               16    1110xxxx    10xxxxxx    10xxxxxx          -
    #          4               21    11110xxx    10xxxxxx    10xxxxxx   10xxxxxx
    # Examples:
    # Character            Code point             UTF-8
    # $  U+0024                     010 0100      00100100                              0x24
    # ¢  U+00A2                000 1010 0010      11000010 10100010                     0xc2 0xa2
    # ह  U+0939          0000 1001 0011 1001      11100000 10100100 10111001            0xe0 0xa4 0xb9
    # €  U+20AC          0010 0000 1010 1100      11100010 10000010 10101100            0xe2 0x82 0xac
    # 한 U+D55C          1101 0101 0101 1100      11101101 10010101 10011100            0xed 0x95 0x9c
    # 𐍈  U+10348  0 0001 0000 0011 0100 1000      11110000 10010000 10001101 10001000   0xf0 0x90 0x8d 0x88

    # This encoding is handled in 6 places in the state, so we simplify the state machine
    # by calling them out.  Eventually, this could be integrated back into the state machine
    # when bugs are worked out, to make it faster.

    def handle_first_string_char(
            read_byte: bytes,
            utf_last_state: int,
            utf_2_of_3_state: int,
            utf_2_of_4_state: int,
    ) -> Tuple[int, Optional[str], Tuple[int, int]]:
        ord_val = ord(read_byte)
        if ord_val & 0x80 == 0:
            # 0xxxxxxx - one byte character
            return -1, chr(ord_val), (0, 0,)
        elif ord_val & 0xe0 == 0xc0:
            # 110xxxxx (10xxxxxx) - two byte character
            return utf_last_state, None, ((ord_val & 0x1f) << 6, 0,)
        elif ord_val & 0xf0 == 0xe0:
            # 1110xxxx (10xxxxxx 10xxxxxx) - three byte character
            return utf_2_of_3_state, None, ((ord_val & 0x0f) << 12, 6,)
        elif ord_val & 0xf8 == 0xf0:
            # 11110xxx (10xxxxxx 10xxxxxx 10xxxxxx) - four byte character
            return utf_2_of_4_state, None, ((ord_val & 0x07) << 18, 12,)
        else:
            # Invalid utf-8 encoding
            return -1, '?', (0, 0,)

    def handle_mid_string_char(
            read_byte: bytes,
            next_byte_state: int,
            current_buf: Any,
    ) -> Tuple[int, Tuple[int, int]]:
        assert isinstance(current_buf, tuple) and len(current_buf) == 2
        ord_val = ord(read_byte)
        if ord_val & 0xc0 == 0x80:
            return next_byte_state, (current_buf[0] + ((ord_val & 0x3f) << current_buf[1]), current_buf[1] - 6,)
        else:
            # Invalid utf-8 encoding
            return -1, (0, 0,)

    def handle_last_string_char(
            read_byte: bytes,
            current_buf: Any,
    ) -> str:
        assert isinstance(current_buf, tuple) and len(current_buf) == 2
        ord_val = ord(read_byte)
        if ord_val & 0xc0 == 0x80:
            return chr(current_buf[0] + (ord_val & 0x3f))
        else:
            # Invalid utf-8 encoding
            return '?'

    # =======================================================================
    # The Big Loop
    while True:
        if state == STATE_END_OBJECT:
            assert isinstance(buf, dict)
            event_id = buf.get('event-id')
            target_id = buf.get('target-id')
            data = buf.get('data')
            if not event_id or not target_id or not isinstance(data, dict):
                errors.append(UserMessage(_("No event-id or target-id or data in event object")))
                return None, as_error(*errors), False
            return to_raw_event_object(event_id, target_id, data), possible_error(messages=errors), False

        c = stream.read(1)
        print(f"+ [{c}]; s:{state}; k:{key}; b:{buf}; os: {object_stack}")

        # ===================================================================
        # Initial state checks.

        if c == b'':
            # End-of-stream.
            if error_buffer:
                return (
                    None,
                    as_error(UserMessage(_("Extra data found in stream before stream was closed"))),
                    True,
                )
            return None, None, True
        if c != BINARY_ZERO_VAL:
            error_buffer = error_buffer[-40:] + c

        if state == STATE_O_BAD_1:
            # Vacuum up all the garbage until the end-of-stream markers.
            # Here, we're looking for the end-of-object marker, '}', before checking the
            # next character, 0
            if c == BINARY_DICT_END_VAL:
                state = STATE_O_BAD_2
            else:
                pass
        elif state == STATE_O_BAD_2:
            if c == BINARY_ZERO_VAL:
                return None, as_error(*errors), False
            elif c == BINARY_DICT_END_VAL:
                # may have a }}\0 ...
                pass
            else:
                # reset to the bad search.
                state = STATE_O_BAD_1

        elif state == STATE_B_BAD_1:
            if c == BINARY_ARRAY_END_VAL:
                state = STATE_B_BAD_2
            else:
                pass
        elif state == STATE_B_BAD_2:
            if c == BINARY_ZERO_VAL:
                return None, as_error(*errors), False
            elif c == BINARY_ARRAY_END_VAL:
                # may have a ]]\0 ...
                pass
            else:
                state = STATE_B_BAD_1

        elif state == STATE_EXPECTING_START:
            if c == BINARY_DICT_START_VAL:
                # Starting an object.  These immediately
                # move on to looking for a key.
                # key = None
                buf = {}
                object_stack.append((STATE_END_OBJECT, None, buf,))
                object_stack.append((STATE_O_DICT_ON_KEY, None, buf,))
                state = STATE_O_VALUE_SEARCH
                # if error_buffer:
                #     errors.append(UserMessage(_('Unexpected data between event objects.')))
                #     error_buffer = b''
            if c == BINARY_ARRAY_START_VAL:
                # Search for a string value.
                buf = {}
                object_stack.append((STATE_END_BLOB, None, buf,))
                object_stack.append((STATE_B_ON_EVENT_ID, None, buf,))
                state = STATE_O_VALUE_SEARCH
                # key = None
                # buf = None
                # if error_buffer:
                #     errors.append(UserMessage(_('Unexpected data between event objects.')))
                #     error_buffer = b''
            elif c != BINARY_ZERO_VAL:
                error_buffer += c
            # c == b'\0' is fine as a separator character.

        # ===================================================================
        # JSON Parsing

        # -------------------------------------------------------------------
        # Value parsing:
        # These are either the dictionary key, dictionary value, or array item.
        # The first part is STATE_O_VALUE_SEARCH, with the last stack value
        # indicating what to do with the value when it's finished being parsed.
        # When the first character of the value is found, that determines the
        # parser to use.
        # Once the value is completed parsing, the stack is popped and interpreted
        # to decide what to do with the parsed value, and what the next state will be.

        elif state == STATE_O_VALUE_SEARCH:
            # if c in BINARY_STRING_QUOTE:
            if c == BINARY_STRING_QUOTE_VAL:
                state = STATE_O_STRING_CHAR
                key = ''
                buf = 0
            # elif c in BINARY_NEGATIVE:
            elif c == BINARY_NEGATIVE_VAL:
                state = STATE_O_NUMBER
                buf = '-'
            elif c == BINARY_POSITIVE_VAL:
                state = STATE_O_NUMBER
                buf = ''
            elif c in BINARY_NUMBER_SET:
                state = STATE_O_NUMBER
                buf = BINARY_NUMBER_MAP[c]
            # elif c in BINARY_DECIMAL:
            elif c == BINARY_DECIMAL_VAL:
                state = STATE_O_FLOAT_DECIMAL
                buf = '0.'
            elif c in BINARY_NULL_TRUE_FALSE_START_SET:
                state = STATE_O_NULL_TRUE_FALSE
                buf = c
            elif c == BINARY_DICT_START_VAL:
                object_stack.append((STATE_O_DICT_ON_KEY, None, {}))
                state = STATE_O_VALUE_SEARCH
            elif c == BINARY_ARRAY_START_VAL:
                object_stack.append((STATE_O_ARRAY_ON_VALUE, None, []))
                state = STATE_O_VALUE_SEARCH
            elif c == BINARY_DICT_END_VAL:
                # expecting a key or value for a key (just saw a ',' ':', or '{').  This is ONLY
                # valid IMMEDIATELY AFTER a '{', to indicate an empty dictionary.
                # However, we'll allow it...
                state, key, buf = handle_value_separator(object_stack.pop(), c)

            elif c == BINARY_ARRAY_END_VAL:
                # expecting a value (just saw a ',' or '[').  This is ONLY valid IMMEDIATELY AFTER
                # a '['
                state, key, buf = handle_value_separator(object_stack.pop(), c)

            elif c in BINARY_WHITESPACE_SET:
                pass

            else:
                # unexpected value
                print(f"Found unexpected data when looking for a value: [{c}]")
                error_buffer += c
                state = STATE_O_INVALID_TOKEN

        # -------------------------------------------------------------------
        # String parsing
        # We do UTF-8 parsing by hand.  Yeah, probably shouldn't.  But we guarantee
        # that we read the " and \" correctly.
        elif state == STATE_O_STRING_CHAR:
            state, ch, buf = handle_first_string_char(
                c, STATE_O_STRING_UTF_BYTE_LAST, STATE_O_STRING_UTF_BYTE_PENULTIMATE, STATE_O_STRING_UTF_BYTE_2_OF_4,
            )
            if state == -1:
                if ch == '"':
                    # End-of-string
                    state, key, buf = handle_end_of_value(key)
                elif ch == '\\':
                    # Start of escaping.
                    # buffer and key remains the same.
                    state = STATE_O_STRING_ESCAPE_CHAR
                else:
                    key += ch
                    state = STATE_O_STRING_CHAR

        elif state == STATE_O_STRING_UTF_BYTE_LAST:
            ch = handle_last_string_char(c, buf)
            if ch == '\\':
                state = STATE_O_STRING_ESCAPE_CHAR
            elif ch == '"':
                # end-of-string
                state, key, buf = handle_end_of_value(key)
            else:
                key += ch
                state = STATE_O_STRING_CHAR

        elif state == STATE_O_STRING_UTF_BYTE_2_OF_4:
            state, buf = handle_mid_string_char(c, STATE_O_STRING_UTF_BYTE_PENULTIMATE, buf)
            if state == -1:
                key += '?'
                state = STATE_O_STRING_CHAR

        elif state == STATE_O_STRING_UTF_BYTE_PENULTIMATE:
            state, buf = handle_mid_string_char(c, STATE_O_STRING_UTF_BYTE_LAST, buf)
            if state == -1:
                key += '?'
                state = STATE_O_STRING_CHAR

        # ...................................................................
        # String escape character sequence
        elif state == STATE_O_STRING_ESCAPE_CHAR:
            state, ch, buf = handle_first_string_char(
                c,
                STATE_O_STRING_ESCAPE_UTF_BYTE_LAST,
                STATE_O_STRING_ESCAPE_UTF_BYTE_PENULTIMATE,
                STATE_O_STRING_ESCAPE_UTF_BYTE_2_OF_4,
            )
            if state == -1:
                if ch == 'u':
                    state = STATE_O_STRING_ESCAPE_UNICODE_CHAR_1
                    buf = []
                else:
                    key += ESCAPED_CHARS_MAP.get(ch, ch)
                    state = STATE_O_STRING_CHAR

        elif state == STATE_O_STRING_ESCAPE_UTF_BYTE_LAST:
            ch = handle_last_string_char(c, buf)
            if ch == 'u':
                state = STATE_O_STRING_ESCAPE_UNICODE_CHAR_1
                buf = []
            else:
                key += ESCAPED_CHARS_MAP.get(ch, ch)
                state = STATE_O_STRING_CHAR

        elif state == STATE_O_STRING_ESCAPE_UTF_BYTE_2_OF_4:
            state, buf = handle_mid_string_char(c, STATE_O_STRING_ESCAPE_UTF_BYTE_PENULTIMATE, buf)
            if state == -1:
                key += '?'
                state = STATE_O_STRING_CHAR

        elif state == STATE_O_STRING_ESCAPE_UTF_BYTE_PENULTIMATE:
            state, buf = handle_mid_string_char(c, STATE_O_STRING_ESCAPE_UTF_BYTE_LAST, buf)
            if state == -1:
                key += '?'
                state = STATE_O_STRING_CHAR

        elif state == STATE_O_STRING_ESCAPE_UNICODE_CHAR_1:
            state, ch, buf = handle_first_string_char(
                c,
                STATE_O_STRING_ESCAPE_UNICODE_CHAR_1_UTF_BYTE_LAST,
                STATE_O_STRING_ESCAPE_UNICODE_CHAR_1_UTF_BYTE_PENULTIMATE,
                STATE_O_STRING_ESCAPE_UNICODE_CHAR_1_UTF_BYTE_2_OF_4,
            )
            if state == -1:
                state = STATE_O_STRING_ESCAPE_UNICODE_CHAR_2
                buf = [HEX_CHARS_MAP.get(ch, 0) << 12, 0]

        elif state == STATE_O_STRING_ESCAPE_UNICODE_CHAR_1_UTF_BYTE_LAST:
            ch = handle_last_string_char(c, buf)
            buf = [HEX_CHARS_MAP.get(ch, 0) << 12, 0]
            state = STATE_O_STRING_ESCAPE_UNICODE_CHAR_2

        elif state == STATE_O_STRING_ESCAPE_UNICODE_CHAR_1_UTF_BYTE_2_OF_4:
            state, buf = handle_mid_string_char(c, STATE_O_STRING_ESCAPE_UNICODE_CHAR_1_UTF_BYTE_PENULTIMATE, buf)
            if state == -1:
                buf = [0, 0]
                state = STATE_O_STRING_ESCAPE_UNICODE_CHAR_2

        elif state == STATE_O_STRING_ESCAPE_UNICODE_CHAR_1_UTF_BYTE_PENULTIMATE:
            state, buf = handle_mid_string_char(c, STATE_O_STRING_ESCAPE_UNICODE_CHAR_1_UTF_BYTE_PENULTIMATE, buf)
            if state == -1:
                buf = [0, 0]
                state = STATE_O_STRING_ESCAPE_UNICODE_CHAR_2

        elif state == STATE_O_STRING_ESCAPE_UNICODE_CHAR_2:
            state, ch, buf_val = handle_first_string_char(
                c,
                STATE_O_STRING_ESCAPE_UNICODE_CHAR_2_UTF_BYTE_LAST,
                STATE_O_STRING_ESCAPE_UNICODE_CHAR_2_UTF_BYTE_PENULTIMATE,
                STATE_O_STRING_ESCAPE_UNICODE_CHAR_2_UTF_BYTE_2_OF_4,
            )
            if state == -1:
                state = STATE_O_STRING_ESCAPE_UNICODE_CHAR_3
                buf[0] += HEX_CHARS_MAP.get(ch, 0) << 8
            else:
                buf[1] = buf_val

        elif state == STATE_O_STRING_ESCAPE_UNICODE_CHAR_2_UTF_BYTE_LAST:
            ch = handle_last_string_char(c, buf[1])
            buf[0] += HEX_CHARS_MAP.get(ch, 0) << 8
            state = STATE_O_STRING_ESCAPE_UNICODE_CHAR_3

        elif state == STATE_O_STRING_ESCAPE_UNICODE_CHAR_2_UTF_BYTE_2_OF_4:
            state, buf_val = handle_mid_string_char(
                c, STATE_O_STRING_ESCAPE_UNICODE_CHAR_2_UTF_BYTE_PENULTIMATE, buf[1],
            )
            if state == -1:
                state = STATE_O_STRING_ESCAPE_UNICODE_CHAR_3
            else:
                buf[1] = buf_val

        elif state == STATE_O_STRING_ESCAPE_UNICODE_CHAR_2_UTF_BYTE_PENULTIMATE:
            state, buf_val = handle_mid_string_char(
                c, STATE_O_STRING_ESCAPE_UNICODE_CHAR_2_UTF_BYTE_LAST, buf[1],
            )
            if state == -1:
                state = STATE_O_STRING_ESCAPE_UNICODE_CHAR_3
            else:
                buf[1] = buf_val

        elif state == STATE_O_STRING_ESCAPE_UNICODE_CHAR_3:
            state, ch, buf_val = handle_first_string_char(
                c,
                STATE_O_STRING_ESCAPE_UNICODE_CHAR_3_UTF_BYTE_LAST,
                STATE_O_STRING_ESCAPE_UNICODE_CHAR_3_UTF_BYTE_PENULTIMATE,
                STATE_O_STRING_ESCAPE_UNICODE_CHAR_3_UTF_BYTE_2_OF_4,
            )
            if state == -1:
                state = STATE_O_STRING_ESCAPE_UNICODE_CHAR_4
                buf[0] += HEX_CHARS_MAP.get(ch, 0) << 4
            else:
                buf[1] = buf_val

        elif state == STATE_O_STRING_ESCAPE_UNICODE_CHAR_3_UTF_BYTE_LAST:
            ch = handle_last_string_char(c, buf[1])
            buf[0] += HEX_CHARS_MAP.get(ch, 0) << 4
            state = STATE_O_STRING_ESCAPE_UNICODE_CHAR_4

        elif state == STATE_O_STRING_ESCAPE_UNICODE_CHAR_3_UTF_BYTE_2_OF_4:
            state, buf_val = handle_mid_string_char(
                c, STATE_O_STRING_ESCAPE_UNICODE_CHAR_3_UTF_BYTE_PENULTIMATE, buf[1],
            )
            if state == -1:
                state = STATE_O_STRING_ESCAPE_UNICODE_CHAR_4
            else:
                buf[1] = buf_val

        elif state == STATE_O_STRING_ESCAPE_UNICODE_CHAR_3_UTF_BYTE_PENULTIMATE:
            state, buf_val = handle_mid_string_char(
                c, STATE_O_STRING_ESCAPE_UNICODE_CHAR_3_UTF_BYTE_LAST, buf[1],
            )
            if state == -1:
                state = STATE_O_STRING_ESCAPE_UNICODE_CHAR_4
            else:
                buf[1] = buf_val

        elif state == STATE_O_STRING_ESCAPE_UNICODE_CHAR_4:
            state, ch, buf_val = handle_first_string_char(
                c,
                STATE_O_STRING_ESCAPE_UNICODE_CHAR_4_UTF_BYTE_LAST,
                STATE_O_STRING_ESCAPE_UNICODE_CHAR_4_UTF_BYTE_PENULTIMATE,
                STATE_O_STRING_ESCAPE_UNICODE_CHAR_4_UTF_BYTE_2_OF_4,
            )
            if state == -1:
                key += chr(buf[0] + HEX_CHARS_MAP.get(ch, 0))
                state = STATE_O_STRING_CHAR
            else:
                buf[1] = buf_val

        elif state == STATE_O_STRING_ESCAPE_UNICODE_CHAR_4_UTF_BYTE_LAST:
            ch = handle_last_string_char(c, buf[1])
            key += chr(buf[0] + HEX_CHARS_MAP.get(ch, 0))
            state = STATE_O_STRING_CHAR

        elif state == STATE_O_STRING_ESCAPE_UNICODE_CHAR_4_UTF_BYTE_2_OF_4:
            state, buf_val = handle_mid_string_char(
                c, STATE_O_STRING_ESCAPE_UNICODE_CHAR_4_UTF_BYTE_PENULTIMATE, buf[1],
            )
            if state == -1:
                key += '?'
                state = STATE_O_STRING_CHAR
            else:
                buf[1] = buf_val

        elif state == STATE_O_STRING_ESCAPE_UNICODE_CHAR_4_UTF_BYTE_PENULTIMATE:
            state, buf_val = handle_mid_string_char(
                c, STATE_O_STRING_ESCAPE_UNICODE_CHAR_4_UTF_BYTE_LAST, buf[1],
            )
            if state == -1:
                key += '?'
                state = STATE_O_STRING_CHAR
            else:
                buf[1] = buf_val

        # -------------------------------------------------------------------
        # Number parsing

        elif state == STATE_O_NUMBER:
            # the whole-number part of the number.
            if c == BINARY_DECIMAL_VAL:
                buf += '.'
                state = STATE_O_FLOAT_DECIMAL
            elif c in BINARY_EXPONENT_SET:
                buf += '.0e'
                state = STATE_O_EXPONENT_FIRST
            elif c in BINARY_NUMBER_SET:
                buf += BINARY_NUMBER_MAP[c]
            elif c in BINARY_END_VALUE_SET:
                # should be able to do a straight 'int(buf)', because we've carefully inspected its contents.
                state, key, buf = handle_value_separator(handle_end_of_value(int(buf)), c)
            else:
                state = STATE_O_INVALID_TOKEN
                error_buffer = buf.encode('utf-8') + c

        elif state == STATE_O_FLOAT_DECIMAL:
            if c in BINARY_EXPONENT_SET:
                buf += '0e'
                state = STATE_O_EXPONENT_FIRST
            elif c in BINARY_NUMBER_SET:
                buf += BINARY_NUMBER_MAP[c]
            elif c in BINARY_END_VALUE_SET:
                # should be able to do a straight 'float(buf)', because we've carefully inspected its contents.
                state, key, buf = handle_value_separator(handle_end_of_value(float(buf)), c)
            else:
                state = STATE_O_INVALID_TOKEN
                error_buffer = buf.encode('utf-8') + c

        elif state == STATE_O_EXPONENT_FIRST:
            if c == BINARY_POSITIVE_VAL:
                buf += '+'
                state = STATE_O_EXPONENT_NUMBER
            elif c == BINARY_NEGATIVE_VAL:
                buf += '-'
                state = STATE_O_EXPONENT_NUMBER
            elif c in BINARY_NUMBER_SET:
                buf += BINARY_NUMBER_MAP[c]
                state = STATE_O_EXPONENT_NUMBER
            elif c in BINARY_END_VALUE_SET:
                # technically, an invalid number format, but we'll allow it.
                buf += '0'
                # should be able to do a straight 'float(buf)', because we've carefully inspected its contents.
                state, key, buf = handle_value_separator(handle_end_of_value(float(buf)), c)
            else:
                state = STATE_O_INVALID_TOKEN
                error_buffer = buf.encode('utf-8') + c

        elif state == STATE_O_EXPONENT_NUMBER:
            if c in BINARY_NUMBER_SET:
                buf += BINARY_NUMBER_MAP[c]
                state = STATE_O_EXPONENT_NUMBER
            elif c in BINARY_END_VALUE_SET:
                # should be able to do a straight 'float(buf)', because we've carefully inspected its contents.
                state, key, buf = handle_value_separator(handle_end_of_value(float(buf)), c)
            else:
                state = STATE_O_INVALID_TOKEN
                error_buffer = buf.encode('utf-8') + c

        # -------------------------------------------------------------------
        # "true", "false", and "null" parsing

        elif state == STATE_O_NULL_TRUE_FALSE:
            # read until an end character, then check if the token is valid.
            # accumulates the 'buf' with a binary string.
            if c in BINARY_END_VALUE_SET:
                if c == BINARY_NULL_STRING:
                    buf = None
                elif c == BINARY_TRUE_STRING:
                    buf = True
                elif c == BINARY_FALSE_STRING:
                    buf = False
                else:
                    # Treat like a None value.
                    errors.append(UserMessage(_("Invalid token in event stream")))
                    buf = None
                state, key, buf = handle_value_separator(handle_end_of_value(float(buf)), c)
            else:
                buf += c

        # -------------------------------------------------------------------
        # Dictionary parsing
        #   - looking for the key:
        #       stack[-1]: (STATE_O_DICT_ON_KEY, None, the dictionary object)
        #       state: STATE_O_VALUE_SEARCH (note that keys should be strings)
        #       buf: None
        #       key: None
        #   - after finding the key:

        elif state == STATE_O_DICT_COLON_SEARCH:
            if c == BINARY_KEY_VALUE_SEPARATOR_VAL:
                object_stack.append((STATE_O_DICT_ON_VALUE, key, buf,))
                state = STATE_O_VALUE_SEARCH
            elif c in BINARY_WHITESPACE_SET:
                pass
            # special characters that indicate we can't correctly parse this
            elif c == BINARY_ARRAY_END_VAL:
                # unrecoverable state
                errors.append(UserMessage(_("Invalid character after a key in a dictionary")))
                state = STATE_O_BAD_1
            else:
                # invalid state; treated as a bad token
                errors.append(UserMessage(_("Unrecoverable error for invalid character after a key in a dictionary")))
                object_stack.append((STATE_O_DICT_ON_VALUE, key, buf,))
                state = STATE_O_INVALID_TOKEN

        elif state == STATE_O_DICT_END_VALUE_SEARCH:
            if c in BINARY_WHITESPACE_SET:
                pass
            elif c == BINARY_VALUE_SEPARATOR_VAL:
                object_stack.append((STATE_O_DICT_ON_KEY, None, buf,))
                state = STATE_O_VALUE_SEARCH
            elif c == BINARY_DICT_END_VAL:
                state, key, buf = handle_end_of_value(buf)
            # special characters that indicate we can't correctly parse this
            elif c == BINARY_ARRAY_END_VAL:
                # unrecoverable state
                errors.append(UserMessage(_("Invalid character after a value in an dictionary")))
                state = STATE_O_BAD_1
            else:
                # invalid state; treated as a bad token
                errors.append(UserMessage(_("Unrecoverable error for invalid character after a value in a dictionary")))
                object_stack.append((STATE_O_DICT_END_VALUE_SEARCH, None, buf,))
                state = STATE_O_INVALID_TOKEN

        # -------------------------------------------------------------------
        # Array parsing

        elif state == STATE_O_ARRAY_END_VALUE_SEARCH:
            if c in BINARY_WHITESPACE_SET:
                pass
            elif c == BINARY_VALUE_SEPARATOR_VAL:
                object_stack.append((STATE_O_ARRAY_ON_VALUE, None, buf,))
                state = STATE_O_VALUE_SEARCH
            elif c == BINARY_ARRAY_END_VAL:
                state, key, buf = handle_end_of_value(buf)
            elif c == BINARY_DICT_END_VAL or c == BINARY_KEY_VALUE_SEPARATOR_VAL:
                # unrecoverable state
                errors.append(UserMessage(_("Invalid character after a value in an array")))
                state = STATE_O_BAD_1
            else:
                # invalid state; treated as a bad token
                errors.append(UserMessage(_("Invalid character after a value in an array")))
                object_stack.append((STATE_O_ARRAY_ON_VALUE, None, buf,))
                state = STATE_O_INVALID_TOKEN

        # -------------------------------------------------------------------
        # Invalid token parsing

        elif state == STATE_O_INVALID_TOKEN:
            if c in BINARY_END_VALUE_SET:
                state, key, buf = handle_end_of_value(None)
            else:
                pass

        # ===================================================================
        # Binary Blob parsing

        elif state == STATE_B_AFTER_EVENT_ID:
            if c in BINARY_WHITESPACE_SET:
                pass
            elif c == BINARY_VALUE_SEPARATOR_VAL:
                object_stack.append((STATE_B_ON_TARGET_ID, None, buf,))
                state = STATE_O_VALUE_SEARCH
            elif c == BINARY_ARRAY_END_VAL:
                errors.append(UserMessage(_("Invalid character after event value in binary blob")))
                state = STATE_B_BAD_2
            else:
                # unrecoverable state
                errors.append(UserMessage(_("Invalid character after event value in binary blob")))
                state = STATE_B_BAD_1
        elif state == STATE_B_AFTER_TARGET_ID:
            if c in BINARY_WHITESPACE_SET:
                pass
            elif c == BINARY_VALUE_SEPARATOR_VAL:
                object_stack.append((STATE_B_ON_LENGTH, None, buf,))
                state = STATE_O_VALUE_SEARCH
            elif c == BINARY_ARRAY_END_VAL:
                errors.append(UserMessage(_("Invalid character after target value in binary blob")))
                state = STATE_B_BAD_2
            else:
                # unrecoverable state
                errors.append(UserMessage(_("Invalid character after target value in binary blob")))
                state = STATE_B_BAD_1

        elif state == STATE_B_AFTER_LENGTH:
            if c in BINARY_WHITESPACE_SET:
                pass
            elif c == BINARY_VALUE_SEPARATOR_VAL:
                if payload_length == 0:
                    buf = object_stack.pop()[2]
                    buf['data'] = b''
                    state = STATE_B_AFTER_PAYLOAD
                else:
                    state = STATE_B_PAYLOAD
                    buf = b''
            elif c == BINARY_ARRAY_END_VAL:
                errors.append(UserMessage(_("Invalid end after payload length in binary blob event")))
                return None, as_error(*errors), False
            else:
                # unrecoverable state
                errors.append(UserMessage(_("Invalid character after length value in binary blob")))
                state = STATE_B_BAD_1

        elif state == STATE_B_PAYLOAD:
            buf += c
            if len(buf) >= payload_length:
                top_buf = object_stack.pop()[2]
                top_buf['data'] = buf
                buf = top_buf
                state = STATE_B_AFTER_PAYLOAD

        elif state == STATE_B_AFTER_PAYLOAD:
            if c == BINARY_ARRAY_END_VAL:
                assert isinstance(buf, dict)
                event_id = buf.get('event-id')
                target_id = buf.get('target-id')
                data = buf.get('data')
                if not event_id or not target_id or not isinstance(data, bytes):
                    errors.append(UserMessage(_("No event-id or target-id or data in event object")))
                    return None, as_error(*errors), False
                return to_raw_event_binary(event_id, target_id, data), possible_error(messages=errors), False

        elif state == STATE_B_ON_EVENT_ID:
            # For input "[]"
            errors.append(UserMessage(_("Invalid binary blob event format")))
            return None, as_error(*errors), False

        else:
            raise RuntimeError(f'Unexpected state {state}')


BINARY_DICT_START_VAL = b'{'
BINARY_DICT_END_VAL = b'}'
BINARY_ARRAY_START_VAL = b'['
BINARY_ARRAY_END_VAL = b']'
BINARY_VALUE_SEPARATOR_VAL = b','
BINARY_KEY_VALUE_SEPARATOR_VAL = b':'
BINARY_STRING_QUOTE_VAL = b'"'
BINARY_NEGATIVE_VAL = b'-'
BINARY_POSITIVE_VAL = b'+'
BINARY_NUMBER_SET = b'0123456789'
BINARY_ZERO_VAL = b'\0'
BINARY_NUMBER_MAP = {
    b'0': '0',
    b'1': '1',
    b'2': '2',
    b'3': '3',
    b'4': '4',
    b'5': '5',
    b'6': '6',
    b'7': '7',
    b'8': '8',
    b'9': '9',
}
BINARY_DECIMAL_VAL = b'.'
BINARY_EXPONENT_SET = b'eE'
BINARY_NULL_TRUE_FALSE_START_SET = b'ntf'
BINARY_TRUE_STRING = b'true'
BINARY_FALSE_STRING = b'false'
BINARY_NULL_STRING = b'null'
BINARY_WHITESPACE_SET = b'\x09\x0a\x0b\x0c\x0d\x20\x85\xa0'
# Does not support full UTF-8 whitespace character set, because this is a simplified parser.
# U+0009  character tabulation
# U+000A  line feed
# U+000B  line tabulation
# U+000C  form feed
# U+000D  carriage return
# U+0020  space
# U+0085  next line
# U+00A0  no-break space
# U+1680  ogham space mark
# U+180E  mongolian vowel separator
# U+2000  en quad
# U+2001  em quad
# U+2002  en space
# U+2003  em space
# U+2004  three-per-em space
# U+2005  four-per-em space
# U+2006  six-per-em space
# U+2007  figure space
# U+2008  punctuation space
# U+2009  thin space
# U+200A  hair space
# U+200B  zero width space
# U+200C  zero width non-joiner
# U+200D  zero width joiner
# U+2028  line separator
# U+2029  paragraph separator
# U+202F  narrow no-break space
# U+205F  medium mathematical space
# U+2060  word joiner
# U+3000  ideographic space
# U+FEFF  zero width non-breaking space

BINARY_END_VALUE_SET = (
        BINARY_ARRAY_END_VAL +
        BINARY_DICT_END_VAL +
        BINARY_VALUE_SEPARATOR_VAL +
        BINARY_WHITESPACE_SET
)

ESCAPED_CHARS_MAP = {
    'b': '\b',  # backspace
    'f': '\f',  # form feed
    'n': '\n',  # line feed
    'r': '\r',  # carriage return
    't': '\t',  # tab
    # \u is very different.
    # everything else is just the character itself.
}
HEX_CHARS_MAP = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'A': 10,
    'b': 11,
    'B': 11,
    'c': 12,
    'C': 12,
    'd': 13,
    'D': 13,
    'e': 14,
    'E': 14,
    'f': 15,
    'F': 15,
}

STATE_EXPECTING_START = 0
STATE_END_OBJECT = 1
STATE_END_BLOB = 2

STATE_O_BAD_1 = 3
STATE_O_BAD_2 = 4
STATE_B_BAD_1 = 5
STATE_B_BAD_2 = 6

STATE_B_ON_EVENT_ID = 100
STATE_B_AFTER_EVENT_ID = 101
STATE_B_ON_TARGET_ID = 102
STATE_B_AFTER_TARGET_ID = 103
STATE_B_ON_LENGTH = 104
STATE_B_AFTER_LENGTH = 105
STATE_B_PAYLOAD = 106
STATE_B_AFTER_PAYLOAD = 107

STATE_O_ARRAY_ON_VALUE = 202
STATE_O_DICT_ON_KEY = 203
STATE_O_DICT_COLON_SEARCH = 204
STATE_O_VALUE_SEARCH = 205
STATE_O_NUMBER = 206
STATE_O_FLOAT_DECIMAL = 207
STATE_O_NULL_TRUE_FALSE = 208
STATE_O_DICT_END_VALUE_SEARCH = 211
STATE_O_ARRAY_END_VALUE_SEARCH = 212
STATE_O_DICT_ON_VALUE = 213
STATE_O_INVALID_TOKEN = 214
STATE_O_EXPONENT_FIRST = 215
STATE_O_EXPONENT_NUMBER = 216

STATE_O_STRING_CHAR = 240
STATE_O_STRING_UTF_BYTE_2_OF_4 = 241
STATE_O_STRING_UTF_BYTE_PENULTIMATE = 242
STATE_O_STRING_UTF_BYTE_LAST = 243

STATE_O_STRING_ESCAPE_CHAR = 245
STATE_O_STRING_ESCAPE_UTF_BYTE_2_OF_4 = 246
STATE_O_STRING_ESCAPE_UTF_BYTE_PENULTIMATE = 247
STATE_O_STRING_ESCAPE_UTF_BYTE_LAST = 248

STATE_O_STRING_ESCAPE_UNICODE_CHAR_1 = 250
STATE_O_STRING_ESCAPE_UNICODE_CHAR_1_UTF_BYTE_2_OF_4 = 251
STATE_O_STRING_ESCAPE_UNICODE_CHAR_1_UTF_BYTE_PENULTIMATE = 252
STATE_O_STRING_ESCAPE_UNICODE_CHAR_1_UTF_BYTE_LAST = 253

STATE_O_STRING_ESCAPE_UNICODE_CHAR_2 = 255
STATE_O_STRING_ESCAPE_UNICODE_CHAR_2_UTF_BYTE_2_OF_4 = 256
STATE_O_STRING_ESCAPE_UNICODE_CHAR_2_UTF_BYTE_PENULTIMATE = 257
STATE_O_STRING_ESCAPE_UNICODE_CHAR_2_UTF_BYTE_LAST = 258

STATE_O_STRING_ESCAPE_UNICODE_CHAR_3 = 260
STATE_O_STRING_ESCAPE_UNICODE_CHAR_3_UTF_BYTE_2_OF_4 = 261
STATE_O_STRING_ESCAPE_UNICODE_CHAR_3_UTF_BYTE_PENULTIMATE = 262
STATE_O_STRING_ESCAPE_UNICODE_CHAR_3_UTF_BYTE_LAST = 263

STATE_O_STRING_ESCAPE_UNICODE_CHAR_4 = 265
STATE_O_STRING_ESCAPE_UNICODE_CHAR_4_UTF_BYTE_2_OF_4 = 266
STATE_O_STRING_ESCAPE_UNICODE_CHAR_4_UTF_BYTE_PENULTIMATE = 267
STATE_O_STRING_ESCAPE_UNICODE_CHAR_4_UTF_BYTE_LAST = 268
