
from typing import List, Tuple, Optional, Any
import unittest
import io
from ..crappy_reader import parse_raw_event
from ..defs import RawEvent, to_raw_event_binary, to_raw_event_object
from ...util import PetroniaReturnError, UserMessage, i18n, as_error


class ParseRawEventTest(unittest.TestCase):

    def test_data(self) -> None:
        i = 0
        for byte_data, expected, left_over in PARSE_DATA:
            with self.subTest(index=i):
                print(f"Parsing [{byte_data}]")
                stream = io.BytesIO(byte_data)
                actual = parse_raw_event(stream)
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
            i += 1


def _msg(message: str, **args: Any) -> UserMessage:
    # no alias for i18n as _ here, because we don't want test strings in the message catalog.
    return UserMessage(i18n(message), **args)


PARSE_DATA: List[Tuple[bytes, Tuple[Optional[RawEvent], List[UserMessage], bool], bytes]] = [
    (  # 0
        b'',
        (None, [], True),
        b'',
    ),
    (  # 1
        b'\0',
        (None, [], True),
        b'',
    ),
    (  # 2
        b'{}{',
        (None, [_msg("No event-id or target-id or data in event object")], False),
        b'{',
    ),
    (  # 3
        b'{{}: ""}{',
        (None, [
            _msg("Dictionary values can only be strings"),
            _msg("No event-id or target-id or data in event object"),
        ], False),
        b'{',
    ),
    (  # 4
        b'{[]: ""}\0{',
        (None, [
            _msg("Dictionary values can only be strings"),
            _msg("No event-id or target-id or data in event object"),
        ], False),
        b'\0{',
    ),
    (  # 5
        b'{"": {}',
        (None, [_msg("Extra data found in stream before stream was closed")], True),
        b'',
    ),
    (  # 6
        # This is a really weird scenario, which is because it's corrupted data.
        # TODO We may want to handle this with recovery...
        b'{"": [}\0{',
        (None, [_msg("Extra data found in stream before stream was closed")], True),
        b'',
    ),
    (  # 7
        b'{]}\0{',
        (None, [_msg("Invalid character after a value in a dictionary")], False),
        b'{',
    ),
    (  # 8
        b'{]\0',
        (None, [_msg("Extra data found in stream before stream was closed")], True),
        b'',
    ),
    (  # 9
        b'{"event-id": "x", "target-id": "y", "data": {}}',
        (to_raw_event_object("x", "y", {}), [], False),
        b'',
    ),
    (  # 10
        b'{"event-id": "x", "target-id": "y", "data": {"t": []}}',
        (to_raw_event_object("x", "y", {"t": []}), [], False),
        b'',
    ),
    (  # 11
        b'\0\0{  "event-id"  : "x"   , "target-id"   : "y"  , "data"  :  {  "t"  :  [  1,  2,  3  ]  }  }',
        (to_raw_event_object("x", "y", {"t": [1, 2, 3]}), [], False),
        b'',
    ),
    (  # 12
        b'{"event-id":"x","target-id":"y","data":{"t":[1,2,3]}}',
        (to_raw_event_object("x", "y", {"t": [1, 2, 3]}), [], False),
        b'',
    ),
    (  # 13
        b'{"event-id":"x","target-id":"y","data":{"t":"\xc2\xa2"}}',
        (to_raw_event_object("x", "y", {"t": "\xa2"}), [], False),
        b'',
    ),
    (  # 14
        b'{"event-id":"x","target-id":"y","data":{"t":"\xe0\xa4\xb9"}}',
        (to_raw_event_object("x", "y", {"t": chr(0x939)}), [], False),
        b'',
    ),
    (  # 15
        b'{"event-id":"x","target-id":"y","data":{"t":"\xe2\x82\xac"}}',
        (to_raw_event_object("x", "y", {"t": chr(0x20ac)}), [], False),
        b'',
    ),
    (  # 16
        b'{"event-id":"x","target-id":"y","data":{"t":"\xed\x95\x9c"}}',
        (to_raw_event_object("x", "y", {"t": chr(0xd55c)}), [], False),
        b'',
    ),
    (  # 17
        b'{"event-id":"x","target-id":"y","data":{"t":"\xf0\x90\x8d\x88"}}',
        (to_raw_event_object("x", "y", {"t": chr(0x10348)}), [], False),
        b'',
    ),
    (  # 18
        b'["x","y",0,]',
        (to_raw_event_binary("x", "y", b''), [], False),
        b'',
    ),
    (  # 19
        b'[    "x"   ,    "y"   ,    0    ,  ]',
        (to_raw_event_binary("x", "y", b''), [], False),
        b'',
    ),
    (  # 20
        b'["x","y",2,\xff\xf1]',
        (to_raw_event_binary("x", "y", b'\xff\xf1'), [], False),
        b'',
    ),
    (  # 21
        b'["x","y",2,\xff\xf1 ]\0{',
        (to_raw_event_binary("x", "y", b'\xff\xf1'), [], False),
        b'\0{',
    ),
    (  # 22
        b'[]\0{',
        (None, [_msg('Invalid binary blob event format')], False),
        b'{',
    ),
    (  # 23
        b'[{}]\0{',
        (None, [_msg("event-id must be a string")], False),
        b'{',
    ),
    (  # 24
        b'[{',
        (None, [_msg('Extra data found in stream before stream was closed')], True),
        b'',
    ),
    (  # 25
        b'[{}\0',
        (None, [_msg('Extra data found in stream before stream was closed')], True),
        b'',
    ),
    (  # 26
        # TODO this is a very bad formatted event.  We don't handle the end-of-event
        #   attempt correctly here.
        b'[{]\0\0',
        (None, [_msg('Extra data found in stream before stream was closed')], True),
        b'',
    ),
    (  # 27
        b'[""]\0{',
        (None, [_msg('Invalid character after event value in binary blob')], False),
        b'{',
    ),
    (  # 28
        b'["x", "y"]\0\0',
        (None, [_msg('Invalid character after target value in binary blob')], False),
        b'\0',
    ),
    (  # 29
        b'["x", "y", 1]\0{',
        (None, [_msg('Extra data found in stream before stream was closed')], True),
        b'',
    ),
    (  # 30
        # TODO this shows a bug in the end-of-array parsing.
        b'[]',
        (None, [_msg('Extra data found in stream before stream was closed')], True),
        b''
    )
]
