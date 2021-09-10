"""Test the module."""

from typing import Tuple, Any, cast
import unittest
import unittest.mock
import io
from petronia_common.event_stream import convert_reader_to_raw
from petronia_common.util import StdRet, RET_OK_NONE, not_none, i18n
from petronia_ext_lib.runner import EventRegistryContext
from .. import bin_store_handler, shared_state
from ..events.impl import binarystore


class StoreHandlerTest(unittest.TestCase):
    """Test the module functions and classes"""

    def test_register_post_data_listener__errors(self) -> None:
        """Test register_delete_data_listener when it encounters errors."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = StdRet.pass_errmsg('c1', i18n('m1'))
        context.register_event_parser.return_value = StdRet.pass_errmsg('c2', i18n('m2'))
        context.register_target.return_value = StdRet.pass_errmsg('c3', i18n('m3'))
        context.register_binary_target.return_value = StdRet.pass_errmsg('c4', i18n('m4'))
        res = bin_store_handler.register_bin_store_data_listener(context)
        self.assertIsNotNone(res.error)
        self.assertEqual(
            ['m1', 'm2', 'm3', 'm4'],
            [m.debug() for m in res.error_messages()],
        )

    def test_post_event__does_not_pending(self) -> None:
        """Test receiving an event when data isn't in a pending state."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        shared_state.clear_data()
        handler = bin_store_handler.StoreDataHandler(context)
        handler.on_event(
            's:1', 't',
            6, convert_reader_to_raw(io.BytesIO(b'1234566')),
        )
        # No such data, so a data removed is sent.
        context.send_event.assert_called_once()
        vargs, kwargs = cast(Tuple[Any, Any], not_none(context.send_event.call_args))
        self.assertEqual(3, len(vargs))
        self.assertEqual({}, kwargs)
        self.assertEqual(binarystore.StoreDataRequestEvent.UNIQUE_TARGET_FQN, vargs[0])
        self.assertEqual('s:1', vargs[1])
        self.assertIsInstance(vargs[2], binarystore.DataDescriptionEvent)
        self.assertEqual(set(), set(shared_state.known_data_ids()))

    def test_post_event__pending(self) -> None:
        """Test receiving an event when the data is in a pending state."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        shared_state.clear_data()
        shared_state.add_pending('s:1', shared_state.PendingStoreData('image/png'))
        handler = bin_store_handler.StoreDataHandler(context)
        handler.on_event(
            's:1', 't',
            6, convert_reader_to_raw(io.BytesIO(b'1234566')),
        )
        self.assertIsNotNone(shared_state.get_data('s:1'))
        # Data is added, so a data description event is sent.
        context.send_event.assert_called_once()
        vargs, kwargs = cast(Tuple[Any, Any], not_none(context.send_event.call_args))
        self.assertEqual(3, len(vargs))
        self.assertEqual({}, kwargs)
        self.assertEqual(binarystore.StoreDataRequestEvent.UNIQUE_TARGET_FQN, vargs[0])
        self.assertEqual('s:1', vargs[1])
        self.assertIsInstance(vargs[2], binarystore.DataDescriptionEvent)

    def tearDown(self) -> None:
        """Make sure the temporary files are cleaned up"""
        shared_state.clear_data()
