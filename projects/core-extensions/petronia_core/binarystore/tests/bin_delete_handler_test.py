"""Test the module."""

from typing import Tuple, Any, cast
import unittest
import unittest.mock
import io
from petronia_common.event_stream import convert_reader_to_raw
from petronia_common.util import StdRet, RET_OK_NONE, not_none, i18n
from petronia_ext_lib.runner import EventRegistryContext
from .. import bin_delete_handler, shared_state
from ..events.impl import binarystore


class DeleteHandlerTest(unittest.TestCase):
    """Test the module functions and classes"""

    def test_register_delete_data_listener__errors(self) -> None:
        """Test register_delete_data_listener when it encounters errors."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = StdRet.pass_errmsg('c1', i18n('m1'))
        context.register_event_parser.return_value = StdRet.pass_errmsg('c2', i18n('m2'))
        context.register_target.return_value = StdRet.pass_errmsg('c3', i18n('m3'))
        res = bin_delete_handler.register_bin_delete_data_listener(context)
        self.assertIsNotNone(res.error)
        self.assertEqual(
            ['m1', 'm2', 'm3'],
            [m.debug() for m in res.error_messages()],
        )

    def test_delete_event__exists(self) -> None:
        """Test receiving an event when the data exists."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.configure_mock(**{
            'send_event.return_value': RET_OK_NONE,
        })
        shared_state.clear_data()
        shared_state.add_pending('s:1', shared_state.PendingStoreData('image/jpeg'))
        shared_state.add_pending('s:2', shared_state.PendingStoreData('image/jpeg'))
        shared_state.store_binary_data(
            's:1', 5, convert_reader_to_raw(io.BytesIO(b'12345')),
        )
        shared_state.store_binary_data(
            's:2', 6, convert_reader_to_raw(io.BytesIO(b'123456')),
        )
        handler = bin_delete_handler.DeleteDataHandler(context)
        handler.on_event(
            's:1', 't', binarystore.DeleteDataRequestEvent(),
        )
        context.send_event.assert_called_once()
        vargs, kwargs = cast(Tuple[Any, Any], not_none(context.send_event.call_args))
        self.assertEqual(3, len(vargs))
        self.assertEqual({}, kwargs)
        self.assertEqual(binarystore.DeleteDataRequestEvent.UNIQUE_TARGET_FQN, vargs[0])
        self.assertEqual('s:1', vargs[1])
        self.assertIsInstance(vargs[2], binarystore.DataDescriptionEvent)
        self.assertEqual({'s:1', 's:2'}, set(shared_state.known_data_ids()))
        self.assertEqual({'s:2'}, set(shared_state.active_data_ids()))

    def tearDown(self) -> None:
        """Make sure the temporary files are cleaned up"""
        shared_state.clear_data()
