
"""Tests for the event writer module."""

import unittest
import io
import re
from .util import ConstSizeChanger
from .. import writer, consts
from ...util.error import PetroniaReturnError
from ...util.message import i18n, UserMessage


class WriterTest(unittest.TestCase):
    """Tests the event writer code."""
    def setUp(self) -> None:
        self.size_changer = ConstSizeChanger()

    def tearDown(self) -> None:
        self.size_changer.tear_down()

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
        """Runs packet writing when reading from a data function."""
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
        """Ensures that if the stream size doesn't match what is read from the
        packet data source, the correct number of bytes are output, and that
        an error is returned."""
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
        """Ensures that if the stream size doesn't match what is passed in an
        argument, then a packet isn't generated and an error is returned."""
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
        """Ensures that invalid unicode characters generate an appropriate error"""
        out = io.BytesIO()
        res = writer.write_binary_event_to_stream(
            out, '\ud800', 'src1', 'tgt1', 0, b'',
        )
        self.assertEqual(b'', out.getvalue())
        self.assertFalse(res.ok)
        self._assert_unicode_error(res.valid_error, 'event-id')

    def test_write_binary_event_to_stream__source_unicode(self) -> None:
        """Ensures that invalid unicode characters generate an appropriate error"""
        out = io.BytesIO()
        res = writer.write_binary_event_to_stream(
            out, 'evt1', '\ud800', 'tgt1', 0, b'',
        )
        self.assertEqual(b'', out.getvalue())
        self.assertFalse(res.ok)
        self._assert_unicode_error(res.valid_error, 'source-id')

    def test_write_binary_event_to_stream__target_unicode(self) -> None:
        """Ensures that invalid unicode characters generate an appropriate error"""
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
        self.assertEqual(
            [expected_id.replace('-', '_'), 'exception'],
            list(messages[0].arguments.keys()),
        )
        self.assertIsInstance(messages[0].arguments['exception'], UnicodeEncodeError)

    def test_write_binary_event_to_stream__size_constraints_all(self) -> None:
        """Checks that invalid size constraints generates the right error messages."""
        out = io.BytesIO()
        res = writer.write_binary_event_to_stream(
            out, '', '', '', consts.MAX_BLOB_SIZE + 1, b'01234567890',
        )
        self.assertEqual(b'', out.getvalue())
        self.assertFalse(res.ok)
        messages = res.valid_error.messages()
        self.assertEqual((
            UserMessage(
                i18n(
                    '{src}: validation error: event-id length must be within [{id_min}, {id_max}]',
                ),
                src='write_binary_event_to_stream', id_min=1, id_max=10, b_min=0, b_max=10,
            ),
            UserMessage(
                i18n(
                    '{src}: validation error: source-id length must be within [{id_min}, {id_max}]',
                ),
                src='write_binary_event_to_stream', id_min=1, id_max=10, b_min=0, b_max=10,
            ),
            UserMessage(
                i18n(
                    '{src}: validation error: target-id length must be within [{id_min}, {id_max}]',
                ),
                src='write_binary_event_to_stream', id_min=1, id_max=10, b_min=0, b_max=10,
            ),
            UserMessage(
                i18n(
                    '{src}: validation error: binary event '
                    'data size must be within [{b_min}, {b_max}]',
                ),
                src='write_binary_event_to_stream', id_min=1, id_max=10, b_min=0, b_max=10,
            ),
        ), messages)

    def test_write_object_event_to_stream_1(self) -> None:
        """Ensures that the standard write-to-stream for a normal object packet works."""
        out = io.BytesIO()
        res = writer.write_object_event_to_stream(
            out,
            'evt1',
            'src1',
            'tgt1',
            {"x": "y"},
        )
        self.assertIsNotNone(res)
        self.assertTrue(res.ok)
        self.assertIsNone(res.value)
        self.assertEqual(
            b'\0\0[e\0\x04evt1s\0\x04src1t\0\x04tgt1{\0\x09{"x":"y"}',
            out.getvalue(),
        )

    def test_write_object_event_to_stream__json_dump_problem(self) -> None:
        """Ensures that problems during dumping json objects are caught."""
        out = io.BytesIO()
        res = writer.write_object_event_to_stream(
            out, '\ud800', 'src1', 'tgt1', {"x": re.compile('x').match('x')},
        )
        self.assertEqual(b'', out.getvalue())
        self.assertFalse(res.ok)
        messages = res.valid_error.messages()
        self.assertEqual(1, len(messages))
        self.assertEqual('event object data cannot be marshalled: {exception}', messages[0].message)
        self.assertEqual(['exception'], list(messages[0].arguments.keys()))
        self.assertIsInstance(messages[0].arguments['exception'], TypeError)

    def test_write_object_event_to_stream__event_unicode(self) -> None:
        """Ensures that invalid unicode characters generate an appropriate error"""
        out = io.BytesIO()
        res = writer.write_object_event_to_stream(
            out, '\ud800', 'src1', 'tgt1', {},
        )
        self.assertEqual(b'', out.getvalue())
        self.assertFalse(res.ok)
        self._assert_unicode_error(res.valid_error, 'event-id')

    def test_write_object_event_to_stream__source_unicode(self) -> None:
        """Ensures that invalid unicode characters generate an appropriate error"""
        out = io.BytesIO()
        res = writer.write_object_event_to_stream(
            out, 'evt1', '\ud800', 'tgt1', {},
        )
        self.assertEqual(b'', out.getvalue())
        self.assertFalse(res.ok)
        self._assert_unicode_error(res.valid_error, 'source-id')

    def test_write_object_event_to_stream__target_unicode(self) -> None:
        """Ensures that invalid unicode characters generate an appropriate error"""
        out = io.BytesIO()
        res = writer.write_object_event_to_stream(
            out, 'evt1', 'src1', '\ud800', {},
        )
        self.assertEqual(b'', out.getvalue())
        self.assertFalse(res.ok)
        self._assert_unicode_error(res.valid_error, 'target-id')

    def test_write_object_event_to_stream__size_constraints_all(self) -> None:
        """Ensures that, when writing an object stream whose values go beyond the
        size limits, correct errors are reported."""
        out = io.BytesIO()
        res = writer.write_object_event_to_stream(
            out, '', '', '', {"012345678901234567890123456": "012345678901234567890123456"},
        )
        self.assertEqual(b'', out.getvalue())
        self.assertFalse(res.ok)
        messages = res.valid_error.messages()
        self.assertEqual((
            UserMessage(
                i18n(
                    '{src}: validation error: event-id length must be within [{id_min}, {id_max}]',
                ),
                src='write_binary_event_to_stream', id_min=1, id_max=10, b_min=2, b_max=60,
            ),
            UserMessage(
                i18n(
                    '{src}: validation error: source-id '
                    'length must be within [{id_min}, {id_max}]',
                ),
                src='write_binary_event_to_stream', id_min=1, id_max=10, b_min=2, b_max=60,
            ),
            UserMessage(
                i18n(
                    '{src}: validation error: target-id length '
                    'must be within [{id_min}, {id_max}]',
                ),
                src='write_binary_event_to_stream', id_min=1, id_max=10, b_min=2, b_max=60,
            ),
            UserMessage(
                i18n(
                    '{src}: validation error: event object data '
                    'size must be within [{b_min}, {b_max}]',
                ),
                src='write_binary_event_to_stream', id_min=1, id_max=10, b_min=2, b_max=60,
            ),
        ), messages)


def io_reader(buff: bytes) -> writer.RawBinaryReader:
    """Simple binary reader implementation"""
    inp = io.BytesIO(buff)

    def reader(max_read_count: int = -1) -> bytes:
        return inp.read(max_read_count)

    return reader
