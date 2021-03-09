"""Test the module"""

import unittest
import unittest.mock
from petronia_common.util import RET_OK_NONE
from .. import registration
from ...runner import EventRegistryContext
from ...events import extension_loader


class RegistrationTest(unittest.TestCase):
    """Test the functions in the module."""

    def test_send_register_listeners(self) -> None:
        """Test the function."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        res = registration.send_register_listeners(context, 'my-ext', [
            ('e1', 't1'), (None, 't2'), ('e3', None), (None, None),
        ])
        self.assertIs(RET_OK_NONE, res)
        calls = context.send_event.call_args_list
        self.assertEqual(1, len(calls))
        self.assertEqual(
            calls[0].args[0],
            'my-ext',
        )
        self.assertEqual(
            calls[0].args[1],
            extension_loader.RegisterExtensionListenersEvent.UNIQUE_TARGET_FQN,
        )
        event_obj = calls[0].args[2]
        assert isinstance(  # nosec  # mypy required
            event_obj,
            extension_loader.RegisterExtensionListenersEvent,
        )
        self.assertEqual(
            event_obj.export_data(),
            {'events': [
                {'event_id': 'e1', 'target_id': 't1'},
                {'target_id': 't2'},
                {'event_id': 'e3'},
                {},
            ]},
        )

    def test_send_remove_listeners(self) -> None:
        """Test the function."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        res = registration.send_remove_listeners(context, 'my-ext', [
            ('e1', 't1'), (None, 't2'), ('e3', None), (None, None),
        ])
        self.assertIs(RET_OK_NONE, res)
        calls = context.send_event.call_args_list
        self.assertEqual(1, len(calls))
        self.assertEqual(
            calls[0].args[0],
            'my-ext',
        )
        self.assertEqual(
            calls[0].args[1],
            extension_loader.RemoveExtensionListenersEvent.UNIQUE_TARGET_FQN,
        )
        event_obj = calls[0].args[2]
        assert isinstance(  # nosec  # mypy required
            event_obj,
            extension_loader.RemoveExtensionListenersEvent,
        )
        self.assertEqual(
            event_obj.export_data(),
            {'events': [
                {'event_id': 'e1', 'target_id': 't1'},
                {'target_id': 't2'},
                {'event_id': 'e3'},
                {},
            ]},
        )
