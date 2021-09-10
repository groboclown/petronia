"""Test the module."""

from typing import Tuple, Sequence, Any, cast
import unittest
import unittest.mock
import io
from petronia_common.event_stream import convert_reader_to_raw
from petronia_common.util import StdRet, RET_OK_NONE, not_none, i18n
from petronia_ext_lib.runner import EventRegistryContext
from .. import bin_fetch_handler, shared_state
from ..events.impl import binarystore


class PostHandlerTest(unittest.TestCase):
    """Test the module functions and classes"""

    def test_register_post_data_listener__errors(self) -> None:
        """Test register_delete_data_listener when it encounters errors."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = StdRet.pass_errmsg('c1', i18n('m1'))
        context.register_event_parser.return_value = StdRet.pass_errmsg('c2', i18n('m2'))
        context.register_target.return_value = StdRet.pass_errmsg('c3', i18n('m3'))
        res = bin_fetch_handler.register_bin_fetch_data_listener(context)
        self.assertIsNotNone(res.error)
        self.assertEqual(
            ['m1', 'm2', 'm2', 'm3', 'm3'],
            [m.debug() for m in res.error_messages()],
        )

    def test_post_event__does_not_exist(self) -> None:  # pylint: disable=no-self-use
        """Test receiving an event when the data doesn't exist."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        shared_state.clear_data()
        handler = bin_fetch_handler.SendDataHandler(context)
        handler.on_event(
            'sx', 't', binarystore.SendDataRequestEvent('s:1'),
        )
        # No such data, so a data removed is sent.
        context.send_event.assert_not_called()

    def test_post_event__exists(self) -> None:
        """Test receiving an event when the data exists."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.configure_mock(**{
            'send_event.return_value': RET_OK_NONE,
        })
        shared_state.clear_data()
        self.assertIsNone(shared_state.add_pending(
            's:1', shared_state.PendingStoreData('image/png'),
        ))
        shared_state.store_binary_data(
            's:1', 4, convert_reader_to_raw(io.BytesIO(b'1234')),
        )
        self.assertIsNone(shared_state.add_pending(
            's:2', shared_state.PendingStoreData('image/png'),
        ))
        shared_state.store_binary_data(
            's:2', 6, convert_reader_to_raw(io.BytesIO(b'123456')),
        )
        handler = bin_fetch_handler.SendDataHandler(context)
        context.send_binary_event_stream.return_value = RET_OK_NONE
        handler.on_event(
            'sx', 't', binarystore.SendDataRequestEvent('s:1'),
        )
        context.send_binary_event_stream.assert_called_once()
        vargs, kwargs = cast(
            Tuple[Sequence[Any], Any], not_none(context.send_binary_event_stream.call_args),
        )
        self.assertEqual(5, len(vargs))
        self.assertEqual({}, kwargs)
        self.assertEqual(binarystore.SendDataRequestEvent.UNIQUE_TARGET_FQN, vargs[0])
        self.assertEqual('s:1', vargs[1])
        self.assertEqual(vargs[2], binarystore.BinaryDataEvent.FULL_EVENT_NAME)
        self.assertEqual(vargs[3], 4)
        self.assertTrue(callable(vargs[4]))
        # This file is closed by the time it's read here...
        # self.assertEqual(vargs[4](), b'1234')  # mypy ignore
        self.assertEqual({'s:1', 's:2'}, set(shared_state.known_data_ids()))

    def tearDown(self) -> None:
        """Make sure the temporary files are cleaned up"""
        shared_state.clear_data()
