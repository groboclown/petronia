"""Test the module."""

from typing import Tuple, Any, cast
import unittest
import unittest.mock
from petronia_common.util import StdRet, RET_OK_NONE, not_none, i18n
from petronia_ext_lib.runner import EventRegistryContext
from .. import json_delete_handler, shared_state
from ..events.impl import datastore


class DeleteHandlerTest(unittest.TestCase):
    """Test the module functions and classes"""

    def test_register_delete_data_listener__errors(self) -> None:
        """Test register_delete_data_listener when it encounters errors."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = StdRet.pass_errmsg('c1', i18n('m1'))
        context.register_event_parser.return_value = StdRet.pass_errmsg('c2', i18n('m2'))
        context.register_target.return_value = StdRet.pass_errmsg('c3', i18n('m3'))
        res = json_delete_handler.register_json_delete_data_listener(context)
        self.assertIsNotNone(res.error)
        self.assertEqual(
            ['m1', 'm2', 'm3'],
            [m.debug() for m in res.error_messages()],
        )

    def test_delete_event__does_not_exist(self) -> None:
        """Test receiving an event when the data doesn't exist."""
        context = unittest.mock.Mock(EventRegistryContext())
        shared_state.clear_data()
        handler = json_delete_handler.DeleteDataHandler(context)
        handler.on_event(
            's1', 't', datastore.DeleteDataRequestEvent(),
        )
        # No such data, so no events sent.
        context.assert_not_called()
        self.assertEqual(set(), set(shared_state.stored_data_ids()))

    def test_delete_event__exists(self) -> None:
        """Test receiving an event when the data exists."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.configure_mock(**{
            'send_event.return_value': RET_OK_NONE,
        })
        shared_state.clear_data()
        shared_state.store_json_data('s:1', 'my-data')
        shared_state.store_json_data('s:2', 'my-data-2')
        handler = json_delete_handler.DeleteDataHandler(context)
        handler.on_event(
            's:1', 't', datastore.DeleteDataRequestEvent(),
        )
        context.send_event.assert_called_once()
        vargs, kwargs = cast(Tuple[Any, Any], not_none(context.send_event.call_args))
        self.assertEqual(3, len(vargs))
        self.assertEqual({}, kwargs)
        self.assertEqual(datastore.DeleteDataRequestEvent.UNIQUE_TARGET_FQN, vargs[0])
        self.assertEqual('s:1', vargs[1])
        self.assertIsInstance(vargs[2], datastore.DataRemovedEvent)
        self.assertEqual({'s:2'}, set(shared_state.stored_data_ids()))
