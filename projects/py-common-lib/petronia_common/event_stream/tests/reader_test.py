
from typing import List, Tuple, Optional, Union, Dict, Any
import unittest
import io
import json
from .util import CallbackCollector, ConstSizeChanger
from .. import reader
from .. import consts
from ..defs import (
    RawEvent, is_raw_event_binary, is_raw_event_object,
    raw_event_source_id, raw_event_target_id, raw_event_id,
    as_raw_event_object_data, as_raw_event_binary_data_reader,
)
from ...util import UserMessage, i18n


ExpectedEvent = Tuple[str, str, str, Union[bytes, Dict[str, Any]]]


class ParseRawEventTest(unittest.TestCase):
    def setUp(self) -> None:
        self.size_changer = ConstSizeChanger()

    def tearDown(self) -> None:
        self.size_changer.tear_down()

    def test_setup(self) -> None:
        # Ensure the assumptions in the constants, plus the assignments above, match up.

        # + 2 for the extra length bytes
        self.assertEqual(consts.MAX_JSON_SIZE + 3, len(TOO_BIG_JSON_BIN))
        self.assertEqual(consts.MAX_JSON_SIZE + 2, len(BIGGEST_JSON_BIN))
        self.assertEqual(consts.MAX_ID_SIZE + 3, len(TOO_BIG_ID_BIN))
        self.assertEqual(consts.MAX_ID_SIZE + 2, len(BIGGEST_ID_BIN))

        self.assertEqual(consts.MAX_BLOB_SIZE + 1, len(TOO_BIG_BLOB))
        self.assertEqual(consts.MAX_BLOB_SIZE, len(BIGGEST_BLOB))

    def test_data(self) -> None:
        for name, byte_data, expected, left_over in PARSE_DATA:
            with self.subTest(name=name):
                # print(f"Parsing [{repr(byte_data)}]")
                stream = io.BytesIO(byte_data)
                actual = reader.parse_raw_event(reader.MarkedStreamReader(stream))
                # print(f" - {actual}")
                self.assert_raw_event_equal(expected[0], actual[0])
                if not expected[1]:
                    self.assertIsNone(actual[1])
                else:
                    self.assertIsNotNone(actual[1])
                    # mypy requirement
                    assert actual[1] is not None
                    self.assertEqual(
                        list(actual[1].messages()),
                        expected[1],
                    )

                self.assertEqual(actual[2], expected[2])
                self.assertEqual(stream.read(), left_over)

    def test_read_event_stream__2_packets(self) -> None:
        byte_data = (
            PACKET_MARKER +
            b'e' + as_bin_str('event-1') +
            b's' + as_bin_str('source-1') +
            b't' + as_bin_str('target-1') +
            b'[\0\0\1x' +
            PACKET_MARKER +
            b'e' + as_bin_str('event-2') +
            b's' + as_bin_str('source-2') +
            b't' + as_bin_str('target-2') +
            b'[\0\0\1y'
        )
        collector = CallbackCollector()
        collector.execute(byte_data)
        event1 = collector.next_as_raw_event(self)
        self.assert_raw_event_equal(
            ("event-1", "source-1", "target-1", b'x'),
            event1,
        )
        event2 = collector.next_as_raw_event(self)
        self.assert_raw_event_equal(
            ("event-2", "source-2", "target-2", b'y'),
            event2,
        )
        collector.next_as_eof(self)

    def test_read_event_stream__2_packets_listener_stop(self) -> None:
        byte_data = (
            PACKET_MARKER +
            b'e' + as_bin_str('event-1') +
            b's' + as_bin_str('source-1') +
            b't' + as_bin_str('target-1') +
            b'[\0\0\1x' +
            PACKET_MARKER +
            b'e' + as_bin_str('event-2') +
            b's' + as_bin_str('source-2') +
            b't' + as_bin_str('target-2') +
            b'[\0\0\1y'
        )
        collector = CallbackCollector()
        collector.event_responses.append(True)
        collector.execute(byte_data)
        event1 = collector.next_as_raw_event(self)
        self.assert_raw_event_equal(
            ("event-1", "source-1", "target-1", b'x'),
            event1,
        )
        collector.is_empty()

    def test_read_event_stream__error(self) -> None:
        byte_data = PACKET_MARKER + b'x'
        collector = CallbackCollector()
        collector.execute(byte_data)
        error = collector.next_as_error(self)
        self.assertEqual(
            "(UserMessage('Reached end-of-stream during packet read', ),)",
            repr(error.messages())
        )

    def test_read_event_stream__error_callback_problem(self) -> None:
        # Note: due to the aggressive, parsing algorithm, the byte stream will
        # skip a packet marker if less than 3 bytes are used after the packet marker.
        byte_data = PACKET_MARKER + b'xyz' + PACKET_MARKER + b'abc' + PACKET_MARKER + b'123'
        collector = CallbackCollector()
        collector.error_responses.extend([False, True, False])
        collector.execute(byte_data)
        error1 = collector.next_as_error(self)
        self.assertEqual(
            "(UserMessage('Unexpected data in the event stream', ),)",
            repr(error1.messages())
        )
        error2 = collector.next_as_error(self)
        self.assertEqual(
            "(UserMessage('Unexpected data in the event stream', ),)",
            repr(error2.messages())
        )
        self.assertTrue(collector.is_empty())

    def test_out_of_order_packet_read(self) -> None:
        # This also tests long data reads.

        # Ensure the blob size allows for large blob reads.
        consts.MAX_BLOB_SIZE = self.size_changer.max_blob

        # Need to generate a packet that exceeds the length necessary to trigger
        # a pipe reader.
        # That, along with the way the collector works, the pipe reader won't
        # be called to read the data.  That should trigger the runtime error.
        byte_data = (
            PACKET_MARKER +
            b'e' + BIGGEST_ID_BIN +
            b's' + BIGGEST_ID_BIN +
            b't' + BIGGEST_ID_BIN +
            b'['
        )
        # we'll generate 1 mb of data + 1 byte.  1mb = 1048576 bytes; 1048576 = 0x100000
        byte_data += b'\x10\0\x01' + (b' ' * 1048576) + b'x'
        # Now add in a second packet, to trigger the out-of-order read error.
        byte_data += (
            PACKET_MARKER +
            b'e' + BIGGEST_ID_BIN +
            b's' + BIGGEST_ID_BIN +
            b't' + BIGGEST_ID_BIN +
            b'{' + BIGGEST_JSON_BIN
        )
        collector = CallbackCollector()
        try:
            collector.execute(byte_data)
            self.fail('Did not generate error.')  # pragma: no cover
        except RuntimeError as e:
            self.assertEqual('Illegal out-of-order event stream read', str(e))

    def test_get_empty_reader(self) -> None:
        stream = reader.MarkedStreamReader(io.BytesIO(b'12'))
        reader_callback = reader.get_reader(stream, 0)
        self.assertEqual(b'', reader_callback())

    def test_get_static_reader(self) -> None:
        stream = reader.MarkedStreamReader(io.BytesIO(b'123'))
        reader_callback = reader.get_reader(stream, 2)
        self.assertEqual(b'1', reader_callback(1))
        self.assertEqual(b'2', reader_callback(1))
        self.assertEqual(b'', reader_callback(1))

    def test_piped_reader(self) -> None:
        stream = reader.MarkedStreamReader(io.BytesIO(b'123'))
        reader_callback = reader.piped_reader(stream, 2)
        self.assertEqual(b'1', reader_callback(1))
        self.assertEqual(b'2', reader_callback(1))
        self.assertEqual(b'', reader_callback(1))

    def assert_raw_event_equal(self, expected: Optional[ExpectedEvent], actual: Optional[RawEvent]) -> None:
        if expected is None:
            self.assertIsNone(actual)
            return
        self.assertIsNotNone(actual)
        # mypy requirement
        assert actual is not None
        self.assertEqual(expected[0], raw_event_id(actual))
        self.assertEqual(expected[1], raw_event_source_id(actual))
        self.assertEqual(expected[2], raw_event_target_id(actual))
        if isinstance(expected[3], bytes):
            # binary
            self.assertTrue(is_raw_event_binary(actual))
            self.assertFalse(is_raw_event_object(actual))
            data_reader = as_raw_event_binary_data_reader(actual)
            self.assertEqual(expected[3], data_reader(-1))
        else:
            # json
            self.assertTrue(is_raw_event_object(actual))
            self.assertFalse(is_raw_event_binary(actual))
            self.assertEqual(expected[3], as_raw_event_object_data(actual))


TOO_BIG_JSON_SRC = {"01234567890123456789012345": "012345678901234567890123456"}
TOO_BIG_JSON = json.dumps(TOO_BIG_JSON_SRC)
BIGGEST_JSON_SRC = {"01234567890123456789012345": "01234567890123456789012345"}
BIGGEST_JSON = json.dumps(BIGGEST_JSON_SRC)
TOO_BIG_BLOB = b'012345678x9'
TOO_BIG_BLOB_BIN = b'\0\0\x0b' + TOO_BIG_BLOB
BIGGEST_BLOB = b'012345678x'
BIGGEST_BLOB_BIN = b'\0\0\x0a' + BIGGEST_BLOB
TOO_BIG_ID = '01234567890'
BIGGEST_ID = '0123456789'
UTF_8_2_BYTE = 'x-' + chr(0xa2) + '-x'  # encodes to b'"x-\xc2\xa2-x"
UTF_8_3_BYTE_1 = 'x-' + chr(0x939) + '-x'  # encodes to b'"x-\xe0\xa4\xb9-x"
UTF_8_3_BYTE_2 = 'x-' + chr(0x20ac) + '-x'  # encodes to b'"x-\xe2\x82\xac-x"
UTF_8_3_BYTE_3 = 'x-' + chr(0xd55c) + '-x'  # encodes to b'"x-\xed\x95\x9c-x"
UTF_8_4_BYTE = 'x-' + chr(0x10348) + '-x'  # encodes to b'"x-\xf0\x90\x8d\x88-x"


def as_bin_str(data: str) -> bytes:
    ret = b''
    raw_data = data.encode('utf-8')
    count = len(raw_data)
    ret += bytes(bytearray(((count >> 8) & 0xff,)))
    ret += bytes(bytearray((count & 0xff,)))
    ret += raw_data
    return ret


def _m(message: str, **args: Any) -> UserMessage:
    # no alias for i18n as _ here, because we don't want test strings in the message catalog.
    return UserMessage(i18n(message), **args)


TOO_BIG_ID_BIN = as_bin_str(TOO_BIG_ID)
BIGGEST_ID_BIN = as_bin_str(BIGGEST_ID)
UTF_8_2_BYTE_BIN = as_bin_str(UTF_8_2_BYTE)
UTF_8_3_BYTE_1_BIN = as_bin_str(UTF_8_3_BYTE_1)
UTF_8_3_BYTE_2_BIN = as_bin_str(UTF_8_3_BYTE_2)
UTF_8_3_BYTE_3_BIN = as_bin_str(UTF_8_3_BYTE_3)
UTF_8_4_BYTE_BIN = as_bin_str(UTF_8_4_BYTE)
BAD_UTF_8_BIN = b'\0\x02\xff\xfe'
TOO_BIG_JSON_BIN = as_bin_str(TOO_BIG_JSON)
BIGGEST_JSON_BIN = as_bin_str(BIGGEST_JSON)
PACKET_MARKER = b'\0\0['

PARSE_DATA: List[Tuple[str, bytes, Tuple[Optional[ExpectedEvent], List[UserMessage], bool], bytes]] = [
    (
        'no data',
        b'',
        (None, [], True),
        b''
    ),
    (
        'no marker',
        b'abc-abc',
        (None, [], True),
        b''
    ),
    (
        'partial marker 1',
        b'abc\0abc',
        (None, [], False),
        b'bc'
    ),
    (
        'partial marker 2',
        b'abc\0\0abc',
        (None, [], False),
        b'bc'
    ),
    (
        'partial marker then EOF',
        b'\0',
        (None, [_m('Reached end-of-stream before packet start', state=2)], True),
        b''
    ),

    # ===== Event ID errors
    (
        'EOF during event + size read',
        # 0x00 0x00 0x91
        b'abc' + PACKET_MARKER + b'e\0',
        (None, [_m('Reached end-of-stream during packet read')], True),
        b'',
    ),
    (
        'Invalid event id size - 0',
        # 0x00 0x00 0x91
        b'abc' + PACKET_MARKER + b'e\0\0s\0\x01bt\0\x01c[\0\0\0',
        (None, [_m('event-id must have a length in the range [{n}, {x}]', n=1, x=10)], False),
        b'',
    ),
    (
        'EOF during event data read, when size is too big',
        b'abc' + PACKET_MARKER + b'e\xff\xffa',
        (None, [
            _m('event-id must have a length in the range [{n}, {x}]', n=1, x=10),
            _m('Reached end-of-stream during packet read'),
        ], True),
        b'',
    ),
    (
        'EOF during event data read',
        # 0x00 0x00 0x91
        b'abc' + PACKET_MARKER + b'e\0\x02a',
        (None, [_m('Reached end-of-stream during packet read')], True),
        b'',
    ),
    (
        'Unicode error in event id',
        # 0x00 0x00 0x91
        b'abc' + PACKET_MARKER + b'e' + BAD_UTF_8_BIN + b's\0\x01bt\0\x01c[\0\0\0',
        (None, [_m(
            'event-id included invalid UTF-8 encoding',
            e="'utf-8' codec can't decode byte 0xff in position 0: invalid start byte",
        )], False),
        b'',
    ),

    # ===== Source ID errors
    (
        'Wrong source marker',
        b'abc' + PACKET_MARKER + b'e\0\x01ab\0\x01c',
        (None, [_m('Unexpected data in the event stream')], False),
        b'c',
    ),
    (
        'EOF during source + size read',
        b'abc' + PACKET_MARKER + b'e\0\x01as\0',
        (None, [_m('Reached end-of-stream during packet read')], True),
        b'',
    ),
    (
        'Invalid source id size - 0',
        b'abc' + PACKET_MARKER + b'e\0\x01as\0\0t\0\x01c[\0\0\0',
        (None, [_m('source-id must have a length in the range [{n}, {x}]', n=1, x=10)], False),
        b'',
    ),
    (
        'EOF during source data read, when size is too big',
        b'abc' + PACKET_MARKER + b'e\0\x01as\xff\xffa',
        (None, [
            _m('source-id must have a length in the range [{n}, {x}]', n=1, x=10),
            _m('Reached end-of-stream during packet read'),
        ], True),
        b'',
    ),
    (
        'EOF during source data read',
        # 0x00 0x00 0x91
        b'abc' + PACKET_MARKER + b'e\0\x01as\0\x02b',
        (None, [_m('Reached end-of-stream during packet read')], True),
        b'',
    ),
    (
        'Unicode error in source id',
        # 0x00 0x00 0x91
        b'abc' + PACKET_MARKER + b'e\0\x01as' + BAD_UTF_8_BIN + b't\0\x01c[\0\0\0',
        (None, [_m(
            'source-id included invalid UTF-8 encoding',
            e="'utf-8' codec can't decode byte 0xff in position 0: invalid start byte",
        )], False),
        b'',
    ),

    # ===== Target ID errors
    (
        'Wrong target marker',
        b'abc' + PACKET_MARKER + b'e\0\x01as\0\x01bx\0\x01cf',
        (None, [_m('Unexpected data in the event stream')], False),
        b'cf',
    ),
    (
        'EOF during target + size read',
        b'abc' + PACKET_MARKER + b'e\0\x01as\0\x01bt\0',
        (None, [_m('Reached end-of-stream during packet read')], True),
        b'',
    ),
    (
        'Invalid target id size - 0',
        b'abc' + PACKET_MARKER + b'e\0\x01as\0\x01bt\0\0[\0\0\0',
        (None, [_m('target-id must have a length in the range [{n}, {x}]', n=1, x=10)], False),
        b'',
    ),
    (
        'EOF during target data read, when size is too big',
        b'abc' + PACKET_MARKER + b'e\0\x01as\0\x01bt\xff\xffa',
        (None, [
            _m('target-id must have a length in the range [{n}, {x}]', n=1, x=10),
            _m('Reached end-of-stream during packet read'),
        ], True),
        b'',
    ),
    (
        'EOF during target data read',
        # 0x00 0x00 0x91
        b'abc' + PACKET_MARKER + b'e\0\x01as\0\x01at\0\x02b',
        (None, [_m('Reached end-of-stream during packet read')], True),
        b'',
    ),
    (
        'Unicode error in source id',
        # 0x00 0x00 0x91
        b'abc' + PACKET_MARKER + b'e\0\x01as\0\x01bt' + BAD_UTF_8_BIN + b'[\0\0\0',
        (None, [_m(
            'target-id included invalid UTF-8 encoding',
            e="'utf-8' codec can't decode byte 0xff in position 0: invalid start byte",
        )], False),
        b'',
    ),

    # ======== packet data
    (
        'EOF at packet data marker',
        # 0x00 0x00 0x91
        b'abc' + PACKET_MARKER + b'e\0\x01as\0\x01bt\0\x01c',
        (None, [_m('Reached end-of-stream during packet read')], True),
        b'',
    ),
    (
        'EOF at JSON packet size read',
        # 0x00 0x00 0x91
        b'abc' + PACKET_MARKER + b'e\0\x01as\0\x01bt\0\x01c{\0',
        (None, [_m('Reached end-of-stream during packet read')], True),
        b'',
    ),
    (
        'EOF at blob packet size read',
        # 0x00 0x00 0x91
        b'abc' + PACKET_MARKER + b'e\0\x01as\0\x01bt\0\x01c[\0',
        (None, [_m('Reached end-of-stream during packet read')], True),
        b'',
    ),
    (
        'garbage before marker, and post-marker data',
        # 0x00 0x00 0x91
        b'abc' + PACKET_MARKER + b'e\0\x01as\0\x01bt\0\x01c[\0\0\0x',
        (("a", "b", "c", b''), [], False),
        b'x',
    ),
    (
        'biggest object data allowed',
        (
            PACKET_MARKER +
            b'e' + BIGGEST_ID_BIN +
            b's' + BIGGEST_ID_BIN +
            b't' + BIGGEST_ID_BIN +
            b'{' + BIGGEST_JSON_BIN
        ),
        ((BIGGEST_ID, BIGGEST_ID, BIGGEST_ID, BIGGEST_JSON_SRC), [], False),
        b'',
    ),
    (
        'Too small JSON size',
        b'abc' + PACKET_MARKER + b'e\0\x01as\0\x01bt\0\x01c{\0\0x',
        (None, [_m('json data must have a length in the range [{n}, {x}]', n=2, x=60)], False),
        b'x',
    ),
    (
        'EOF during too small JSON size',
        b'abc' + PACKET_MARKER + b'e\0\x01as\0\x01bt\0\x01c{\0\1',
        (None, [
            _m('json data must have a length in the range [{n}, {x}]', n=2, x=60),
            _m('Reached end-of-stream during packet read'),
        ], True),
        b'',
    ),
    (
        'EOF during JSON read',
        b'abc' + PACKET_MARKER + b'e\0\x01as\0\x01bt\0\x01c{\0\x05x',
        (None, [_m('Reached end-of-stream during packet read')], True),
        b'',
    ),
    (
        'EOF during too-big JSON read',
        b'abc' + PACKET_MARKER + b'e\0\x01as\0\x01bt\0\x01c{\xff\xffx',
        (None, [
            _m('json data must have a length in the range [{n}, {x}]', n=2, x=60),
            _m('Reached end-of-stream during packet read'),
        ], True),
        b'',
    ),
    (
        'bad json',
        PACKET_MARKER + b'e\0\x01as\0\x01bt\0\x01c{\0\x02{[',
        (None, [
            _m(
                'Event streaming data included badly formatted JSON data: {e}',
                e='Expecting property name enclosed in double quotes: line 1 column 2 (char 1)',
            ),
            _m('Event data was not sent as JSON dictionary'),
        ], False),
        b'',
    ),
    (
        'utf json error',
        PACKET_MARKER + b'e\0\x01as\0\x01bt\0\x01c{\0\x09{"\xff\xfe":""}',
        (None, [
            _m(
                'Event streaming data included incorrectly encoded UTF-8 values: {e}',
                e="'utf-8' codec can't decode byte 0xff in position 2: invalid start byte",
            ),
            _m('Event data was not sent as JSON dictionary'),
        ], False),
        b'',
    ),
    (
        'too big event-id',
        (
            PACKET_MARKER +
            b'e' + TOO_BIG_ID_BIN +
            b's' + BIGGEST_ID_BIN +
            b't' + BIGGEST_ID_BIN +
            b'{' + BIGGEST_JSON_BIN +
            b'x'
        ),
        (None, [_m('event-id must have a length in the range [{n}, {x}]', n=1, x=10)], False),
        b'x',
    ),
    (
        'too big source-id',
        (
            PACKET_MARKER +
            b'e' + BIGGEST_ID_BIN +
            b's' + TOO_BIG_ID_BIN +
            b't' + BIGGEST_ID_BIN +
            b'{' + BIGGEST_JSON_BIN +
            b'x'
        ),
        (None, [_m('source-id must have a length in the range [{n}, {x}]', n=1, x=10)], False),
        b'x',
    ),
    (
        'too big target-id',
        (
            PACKET_MARKER +
            b'e' + BIGGEST_ID_BIN +
            b's' + BIGGEST_ID_BIN +
            b't' + TOO_BIG_ID_BIN +
            b'{' + BIGGEST_JSON_BIN +
            b'x'
        ),
        (None, [_m('target-id must have a length in the range [{n}, {x}]', n=1, x=10)], False),
        b'x',
    ),
    (
        'too big json',
        (
            PACKET_MARKER +
            b'e' + BIGGEST_ID_BIN +
            b's' + BIGGEST_ID_BIN +
            b't' + BIGGEST_ID_BIN +
            b'{' + TOO_BIG_JSON_BIN +
            b'x'
        ),
        (None, [_m('json data must have a length in the range [{n}, {x}]', n=2, x=60)], False),
        b'x',
    ),
    (
        'too big binary',
        (
            PACKET_MARKER +
            b'e' + UTF_8_3_BYTE_2_BIN +
            b's' + UTF_8_3_BYTE_3_BIN +
            b't' + UTF_8_2_BYTE_BIN +
            b'[' + TOO_BIG_BLOB_BIN +
            b'x'
        ),
        (None, [_m('binary blob data must have a length in the range [{n}, {x}]', n=0, x=10)], False),
        b'x',
    ),
    (
        'EOF during too big binary read',
        (
            PACKET_MARKER +
            b'e' + UTF_8_4_BYTE_BIN +
            b's' + UTF_8_3_BYTE_1_BIN +
            b't' + UTF_8_3_BYTE_2_BIN +
            b'[\xff\xff\xffx'
        ),
        (None, [
            _m('binary blob data must have a length in the range [{n}, {x}]', n=0, x=10),
            _m('Reached end-of-stream during packet read'),
        ], True),
        b'',
    ),
    (
        'Unrecognized packet data format marker',
        PACKET_MARKER + b'e\0\x01as\0\x01bt\0\x01c!x',
        (None, [_m('Unexpected data in the event stream')], False),
        b'x',
    ),
]
