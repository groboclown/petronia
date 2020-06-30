
from typing import List, Tuple, Optional, Any
import unittest
import io
import json
from .. import reader
from ..defs import RawEvent, to_raw_event_binary, to_raw_event_object
from ...util import PetroniaReturnError, UserMessage, i18n, as_error


class ParseRawEventTest(unittest.TestCase):
    def setUp(self) -> None:
        self.max_id = reader.MAX_ID_SIZE
        self.max_json = reader.MAX_JSON_SIZE
        self.max_blob = reader.MAX_BLOB_SIZE
        reader.MAX_ID_SIZE = 10
        reader.MAX_JSON_SIZE = 60
        reader.MAX_BLOB_SIZE = 10

    def tearDown(self) -> None:
        reader.MAX_ID_SIZE = self.max_id
        reader.MAX_JSON_SIZE = self.max_json
        reader.MAX_BLOB_SIZE = self.max_blob

    def test_setup(self) -> None:
        # + 2 for the extra length bytes
        self.assertEqual(reader.MAX_JSON_SIZE + 3, len(TOO_BIG_JSON_BIN))
        self.assertEqual(reader.MAX_JSON_SIZE + 2, len(BIGGEST_JSON_BIN))
        self.assertEqual(reader.MAX_ID_SIZE + 3, len(TOO_BIG_ID_BIN))
        self.assertEqual(reader.MAX_ID_SIZE + 2, len(BIGGEST_ID_BIN))

        self.assertEqual(reader.MAX_BLOB_SIZE + 1, len(TOO_BIG_BLOB))
        self.assertEqual(reader.MAX_BLOB_SIZE, len(BIGGEST_BLOB))

    def test_data(self) -> None:
        for name, byte_data, expected, left_over in PARSE_DATA:
            with self.subTest(name=name):
                print(f"Parsing [{byte_data}]")
                stream = io.BytesIO(byte_data)
                actual = reader.parse_raw_event(stream)
                print(f" - {actual}")
                self.assertEqual(actual[0], expected[0])
                if not expected[1]:
                    self.assertIsNone(actual[1])
                else:
                    self.assertEqual(
                        list(actual[1].messages()),
                        expected[1],
                    )
                self.assertEqual(actual[2], expected[2])
                self.assertEqual(stream.read(), left_over)


TOO_BIG_JSON_SRC = {"01234567890123456789012345": "012345678901234567890123456"}
TOO_BIG_JSON = json.dumps(TOO_BIG_JSON_SRC)
BIGGEST_JSON_SRC = {"01234567890123456789012345": "01234567890123456789012345"}
BIGGEST_JSON = json.dumps(BIGGEST_JSON_SRC)
TOO_BIG_BLOB = b'012345678x9'
TOO_BIG_BLOB_BIN = b'\0\0\0\x0b' + TOO_BIG_BLOB
BIGGEST_BLOB = b'012345678x'
BIGGEST_BLOB_BIN = b'\0\0\0\x0a' + BIGGEST_BLOB
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
TOO_BIG_JSON_BIN = as_bin_str(TOO_BIG_JSON)
BIGGEST_JSON_BIN = as_bin_str(BIGGEST_JSON)

PARSE_DATA: List[Tuple[str, bytes, Tuple[Optional[RawEvent], List[UserMessage], bool], bytes]] = [
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
        'garbage before marker, and post-marker data',
        # 0x00 0x00 0x91
        b'abc\0\0[e\0\x01at\0\x01b[\0\0\0\0x',
        (to_raw_event_binary("a", "b", b''), [], False),
        b'x',
    ),
    (
        'too big event-id',
        b'\0\0[e' + TOO_BIG_ID_BIN + b't' + BIGGEST_ID_BIN + b'{' + BIGGEST_JSON_BIN + b'x',
        (None, [_m('event-id must have a length in the range [1, {m}]', m=10)], False),
        b'x',
    ),
    (
        'too big target-id',
        b'\0\0[e' + BIGGEST_ID_BIN + b't' + TOO_BIG_ID_BIN + b'{' + BIGGEST_JSON_BIN + b'x',
        (None, [_m('target-id must have a length in the range [1, {m}]', m=10)], False),
        b'x',
    ),
    (
        'too big json',
        b'\0\0[e' + BIGGEST_ID_BIN + b't' + BIGGEST_ID_BIN + b'{' + TOO_BIG_JSON_BIN + b'x',
        (None, [_m('json data must have a length in the range [1, {m}]', m=60)], False),
        b'x',
    ),
    (
        'too big binary',
        b'\0\0[e' + BIGGEST_ID_BIN + b't' + BIGGEST_ID_BIN + b'[' + TOO_BIG_BLOB_BIN + b'x',
        (None, [_m('binary blob data must have a length in the range [1, {m}]', m=10)], False),
        b'x',
    ),
]
