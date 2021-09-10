"""Test the module."""

from typing import Tuple, Sequence, Any, cast
import unittest
import unittest.mock
import json
from petronia_common.util import StdRet, RET_OK_NONE, not_none, i18n
from petronia_ext_lib.runner import EventRegistryContext
from petronia_ext_lib.events import logging
from .. import json_store_handler, shared_state
from ..events.impl import datastore


class StoreHandlerTest(unittest.TestCase):
    """Test the module functions and classes"""

    def test_register_post_data_listener__errors(self) -> None:
        """Test register_delete_data_listener when it encounters errors."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = StdRet.pass_errmsg('c1', i18n('m1'))
        context.register_event_parser.return_value = StdRet.pass_errmsg('c2', i18n('m2'))
        context.register_target.return_value = StdRet.pass_errmsg('c3', i18n('m3'))
        res = json_store_handler.register_json_store_data_listener(context)
        self.assertIsNotNone(res.error)
        self.assertEqual(
            ['m1', 'm2', 'm3'],
            [m.debug() for m in res.error_messages()],
        )

    def test_post_event__does_not_exist(self) -> None:
        """Test receiving an event when the data doesn't exist."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        shared_state.clear_data()
        handler = json_store_handler.StoreDataHandler(context)
        handler.on_event(
            's:1', 't', datastore.StoreDataRequestEvent(json.dumps({'a': 1})),
        )
        # No such data, so a data removed is sent.
        context.send_event.assert_called_once()
        vargs, kwargs = cast(Tuple[Any, Any], not_none(context.send_event.call_args))
        self.assertEqual(3, len(vargs))
        self.assertEqual({}, kwargs)
        self.assertEqual(datastore.DeleteDataRequestEvent.UNIQUE_TARGET_FQN, vargs[0])
        self.assertEqual('s:1', vargs[1])
        self.assertIsInstance(vargs[2], datastore.DataUpdatedEvent)
        self.assertEqual({'s:1'}, set(shared_state.stored_data_ids()))
        self.assertEqual(
            not_none(shared_state.get_json_data('s:1'))[0],
            cast(datastore.DataUpdatedEvent, vargs[2]).json,
        )
        self.assertEqual(
            not_none(shared_state.get_json_data('s:1'))[1],
            cast(datastore.DataUpdatedEvent, vargs[2]).changed,
        )

    def test_post_event__bad_data(self) -> None:
        """Test receiving an event when the data doesn't exist."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        shared_state.clear_data()
        handler = json_store_handler.StoreDataHandler(context)
        handler.on_event(
            's:1', 't', datastore.StoreDataRequestEvent('['),
        )
        # No such data, so a data removed is sent.
        context.send_event.assert_called_once()
        vargs, kwargs = cast(Tuple[Any, Any], not_none(context.send_event.call_args))
        self.assertEqual(3, len(vargs))
        self.assertEqual({}, kwargs)
        self.assertEqual(datastore.StoreDataRequestEvent.UNIQUE_TARGET_FQN, vargs[0])
        self.assertEqual(logging.SystemErrorEvent.UNIQUE_TARGET_FQN, vargs[1])
        self.assertIsInstance(vargs[2], logging.SystemErrorEvent)
        self.assertEqual(set(), set(shared_state.stored_data_ids()))

    def test_post_event__exists(self) -> None:
        """Test receiving an event when the data exists."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.configure_mock(**{
            'send_event.return_value': RET_OK_NONE,
        })
        shared_state.clear_data()
        shared_state.store_json_data('s:1', json.dumps({'x': 'y'}))
        shared_state.store_json_data('s:2', 'my-data-2')
        handler = json_store_handler.StoreDataHandler(context)
        handler.on_event(
            's:1', 't', datastore.StoreDataRequestEvent(json.dumps({'a': 1})),
        )
        context.send_event.assert_called_once()
        vargs, kwargs = cast(Tuple[Sequence[Any], Any], not_none(context.send_event.call_args))
        self.assertEqual(3, len(vargs))
        self.assertEqual({}, kwargs)
        self.assertEqual(datastore.SendStateRequestEvent.UNIQUE_TARGET_FQN, vargs[0])
        self.assertEqual('s:1', vargs[1])
        self.assertIsInstance(vargs[2], datastore.DataUpdatedEvent)
        self.assertEqual(
            not_none(shared_state.get_json_data('s:1'))[0],
            cast(datastore.DataUpdatedEvent, vargs[2]).json,
        )
        self.assertEqual({'s:1', 's:2'}, set(shared_state.stored_data_ids()))
