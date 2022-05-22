"""Test the module."""

from typing import Optional
import unittest
import io
from petronia_common.event_stream import convert_reader_to_raw
from .. import shared_state


class SharedStateTest(unittest.TestCase):
    """Test the functions in the module."""

    def test_get_store_data(self) -> None:
        """Test the store_data function."""
        shared_state.clear_data()
        self.assertIsNone(shared_state.add_pending(
            'd1', shared_state.PendingStoreData('image/png'),
        ))
        res1 = shared_state.store_binary_data(
            'd1', 6, convert_reader_to_raw(io.BytesIO(b'123456')),
        )
        self.assertIsNone(res1.error)
        self.assertIsNotNone(res1.value)
        self.assertIsNone(shared_state.add_pending(
            'd2', shared_state.PendingStoreData('image/png'),
        ))
        res2 = shared_state.store_binary_data(
            'd2', 2, convert_reader_to_raw(io.BytesIO(b'12')),
        )
        self.assertIsNone(res2.error)
        self.assertIsNotNone(res2.value)
        self.assertEqual({'d1', 'd2'}, set(shared_state.known_data_ids()))
        self.assertIsNone(shared_state.get_data('d0'))
        self.assertIs(res1.value, shared_state.get_data('d1'))
        self.assertIs(res2.value, shared_state.get_data('d2'))
        self.assertEqual(b'123456', _read_data(res1.result))
        self.assertEqual(b'12', _read_data(res2.result))

        # Updating data is not allowed
        res1a = shared_state.store_binary_data(
            'd1', 1, convert_reader_to_raw(io.BytesIO(b'1')),
        )
        self.assertIsNone(res1a.error)
        self.assertIsNone(res1a.value)
        self.assertEqual({'d1', 'd2'}, set(shared_state.known_data_ids()))
        self.assertIs(res1.value, shared_state.get_data('d1'))
        self.assertEqual(b'123456', _read_data(res1.result))

    def tearDown(self) -> None:
        """Make sure the temporary files are cleaned up"""
        shared_state.clear_data()


def _read_data(data: Optional[shared_state.StoredData]) -> bytes:
    assert data is not None  # nosec  # to make things easier for us.
    with open(data.filename, 'rb') as f:
        return f.read(data.size)
