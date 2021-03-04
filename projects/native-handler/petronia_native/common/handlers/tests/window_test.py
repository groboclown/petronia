"""Test the module."""

import unittest
import unittest.mock
import json
from petronia_common.util import RET_OK_NONE
from petronia_ext_lib.runner import EventRegistryContext
from petronia_ext_lib.events import datastore
from .. import window
from ...events.impl import window as window_events


class WindowHandlerTest(unittest.TestCase):
    """Test the module function and classes."""

    def test_store_active_windows_state(self) -> None:
        """Test the store_active_windows_state function."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        window.store_active_windows_state(context, ('w1', 'w2'))
        context.send_event.assert_called_once()
        args = context.send_event.call_args_list[0].args
        self.assertEqual(
            window_events.ActiveWindowsState.UNIQUE_TARGET_FQN,
            args[0],
        )
        self.assertEqual(
            datastore.StoreDataEvent.UNIQUE_TARGET_FQN,
            args[1],
        )
        event_obj = args[2]
        self.assertIsInstance(event_obj, datastore.StoreDataEvent)
        # mypy required
        assert isinstance(event_obj, datastore.StoreDataEvent)  # nosec
        self.assertEqual(
            json.dumps({
                'active_ids': [{'window_id': 'w1'}, {'window_id': 'w2'}],
            }),
            event_obj.json,
        )
