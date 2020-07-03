
import unittest
import io
from .. import writer, consts
from ...util.error import PetroniaReturnError
from ...util.message import i18n, UserMessage


class WriterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.max_id = consts.MAX_ID_SIZE
        self.max_json = consts.MAX_JSON_SIZE
        self.max_blob = consts.MAX_BLOB_SIZE
        consts.MAX_ID_SIZE = 10
        consts.MAX_JSON_SIZE = 60
        consts.MAX_BLOB_SIZE = 10

    def tearDown(self) -> None:
        consts.MAX_ID_SIZE = self.max_id
        consts.MAX_JSON_SIZE = self.max_json
        consts.MAX_BLOB_SIZE = self.max_blob

    def test_write_binary_event_to_stream_1(self) -> None:
        """in-memory standard write."""
        out = io.BytesIO()
        res = writer.write_binary_event_to_stream(
            out,
            'evt1',
            'src1',
            'tgt1',
            2,
            b'ab',
        )
        self.assertIsNotNone(res)
        self.assertTrue(res.ok)
        self.assertIsNone(res.value)
        self.assertEqual(
            b'\0\0[e\0\x04evt1s\0\x04src1t\0\x04tgt1[\0\0\x02ab',
            out.getvalue(),
        )

    def test_write_binary_event_to_stream__from_func(self) -> None:
        out = io.BytesIO()
        res = writer.write_binary_event_to_stream(
            out, 'evt1', 'src1', 'tgt1', 10, io_reader(b'0123456789'),
        )
        self.assertIsNotNone(res)
        self.assertTrue(res.ok)
        self.assertIsNone(res.value)
        self.assertEqual(
            b'\0\0[e\0\x04evt1s\0\x04src1t\0\x04tgt1[\0\0\x0a0123456789',
            out.getvalue(),
        )

    def test_write_binary_event_to_stream__from_func_too_few(self) -> None:
        out = io.BytesIO()
        res = writer.write_binary_event_to_stream(
            out, 'evt1', 'src1', 'tgt1', 10, io_reader(b'0123'),
        )
        self.assertIsNotNone(res)
        self.assertFalse(res.ok)
        self.assertIsNone(res.value)
        self.assertEqual(
            b'\0\0[e\0\x04evt1s\0\x04src1t\0\x04tgt1[\0\0\x0a0123      ',
            out.getvalue(),
        )
        self.assertEqual(
            (UserMessage(i18n('binary blob data less than requested size')),),
            res.valid_error.messages(),
        )

    def test_write_binary_event_to_stream__size_mismatch(self) -> None:
        out = io.BytesIO()
        res = writer.write_binary_event_to_stream(
            out, 'evt1', 'src1', 'tgt1', 5, b'',
        )
        self.assertEqual(b'', out.getvalue())
        self.assertFalse(res.ok)
        self.assertEqual(
            (UserMessage(
                i18n('binary_blob has {real_size} bytes, but requested {expected_size}'),
                real_size=0,
                expected_size=5,
            ),),
            res.valid_error.messages(),
        )

    def test_write_binary_event_to_stream__event_unicode(self) -> None:
        out = io.BytesIO()
        res = writer.write_binary_event_to_stream(
            out, '\ud800', 'src1', 'tgt1', 0, b'',
        )
        self.assertEqual(b'', out.getvalue())
        self.assertFalse(res.ok)
        self._assert_unicode_error(res.valid_error, 'event-id')

    def test_write_binary_event_to_stream__source_unicode(self) -> None:
        out = io.BytesIO()
        res = writer.write_binary_event_to_stream(
            out, 'evt1', '\ud800', 'tgt1', 0, b'',
        )
        self.assertEqual(b'', out.getvalue())
        self.assertFalse(res.ok)
        self._assert_unicode_error(res.valid_error, 'source-id')

    def test_write_binary_event_to_stream__target_unicode(self) -> None:
        out = io.BytesIO()
        res = writer.write_binary_event_to_stream(
            out, 'evt1', 'src1', '\ud800', 0, b'',
        )
        self.assertEqual(b'', out.getvalue())
        self.assertFalse(res.ok)
        self._assert_unicode_error(res.valid_error, 'target-id')

    def _assert_unicode_error(self, error: PetroniaReturnError, expected_id: str) -> None:
        messages = error.messages()
        self.assertEqual(1, len(messages))
        self.assertEqual(expected_id + ' UTF-8 encoding problem: {exception}', messages[0].message)
        self.assertEqual([expected_id.replace('-', '_'), 'exception'], list(messages[0].arguments.keys()))
        self.assertIsInstance(messages[0].arguments['exception'], UnicodeEncodeError)

    def test_write_binary_event_to_stream__size_constraints_all(self) -> None:
        out = io.BytesIO()
        res = writer.write_binary_event_to_stream(
            out, '', '', '', consts.MAX_BLOB_SIZE + 1, b'01234567890',
        )
        self.assertEqual(b'', out.getvalue())
        self.assertFalse(res.ok)
        messages = res.valid_error.messages()
        self.assertEqual((
            UserMessage(
                i18n('{src}: validation error: event-id length must be within [{id_min}, {id_max}]'),
                src='write_binary_event_to_stream', id_min=1, id_max=10, b_min=0, b_max=10
            ),
            UserMessage(
                i18n('{src}: validation error: source-id length must be within [{id_min}, {id_max}]'),
                src='write_binary_event_to_stream', id_min=1, id_max=10, b_min=0, b_max=10
            ),
            UserMessage(
                i18n('{src}: validation error: target-id length must be within [{id_min}, {id_max}]'),
                src='write_binary_event_to_stream', id_min=1, id_max=10, b_min=0, b_max=10
            ),
            UserMessage(
                i18n('{src}: validation error: binary event data size must be within [{b_min}, {b_max}]'),
                src='write_binary_event_to_stream', id_min=1, id_max=10, b_min=0, b_max=10
            ),
        ), messages)


def io_reader(buff: bytes) -> writer.RawBinaryReader:
    inp = io.BytesIO(buff)

    def reader(max_read_count: int = -1) -> bytes:
        return inp.read(max_read_count)

    return reader
