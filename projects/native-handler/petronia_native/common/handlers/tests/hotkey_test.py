"""Test the module"""

import unittest
import unittest.mock
import json
from petronia_common.util import StdRet, i18n, RET_OK_NONE, not_none
from petronia_ext_lib.runner import EventRegistryContext
from petronia_ext_lib.events import datastore
from .. import hotkey
from ...events.impl import hotkey as hotkey_event


class HotkeyTest(unittest.TestCase):
    """Test the module classes and functions."""

    def test_send_hotkey_pressed(self) -> None:
        """Test calling out to send_hotkey_pressed"""
        context = unittest.mock.Mock(EventRegistryContext())
        hotkey.send_hotkey_pressed(context, ['x'])
        context.send_event.assert_called()
        self.assertEqual(
            (
                hotkey_event.HotkeyPressedEvent.UNIQUE_TARGET_FQN,
                hotkey_event.HotkeyPressedEvent.UNIQUE_TARGET_FQN,
            ),
            context.send_event.call_args[0][0:2],
        )
        event = context.send_event.call_args[0][2]
        self.assertIsInstance(event, hotkey_event.HotkeyPressedEvent)
        assert isinstance(event, hotkey_event.HotkeyPressedEvent)  # nosec  # mypy required
        self.assertEqual(['x'], event.hotkey.keys)

    def test_register_hotkey_listeners__bad_parser(self) -> None:
        """Test register_hotkey_listeners, with a failed parser registration."""
        context = unittest.mock.Mock(EventRegistryContext())
        handler = unittest.mock.Mock(hotkey.HotkeyHandler())
        bad_res: StdRet[None] = StdRet.pass_errmsg('c', i18n('m'))
        context.register_event_parser.return_value = bad_res
        res = hotkey.register_hotkey_listeners(context, handler)
        self.assertIs(bad_res, res)
        context.register_event_parser.assert_called_once()

    def test_register_hotkey_listeners__ok(self) -> None:
        """Test register_hotkey_listeners, with a failed parser registration."""
        context = unittest.mock.Mock(EventRegistryContext())
        handler = unittest.mock.Mock(hotkey.HotkeyHandler())
        context.register_event_parser.return_value = RET_OK_NONE
        context.register_target.return_value = RET_OK_NONE
        res = hotkey.register_hotkey_listeners(context, handler)
        self.assertIs(RET_OK_NONE, res)
        context.register_event_parser.assert_called_once()
        context.register_target.assert_called_once()

    def test_handler_bindings__on_event__closed(self) -> None:
        """Test out HotkeyBindingsTarget.on_event when the target is closed."""

        context = unittest.mock.Mock(EventRegistryContext())
        handler = unittest.mock.Mock(hotkey.HotkeyHandler())
        target = hotkey.HotkeyBindingsTarget(context, handler)
        target.on_close()
        self.assertTrue(
            target.on_event('s', 't', hotkey_event.SetHotkeyBindingsEvent(
                1, hotkey_event.MasterHotkeySequence('m', []), [],
            ))
        )
        handler.set_hotkey_bindings.assert_not_called()
        context.send_event.assert_not_called()

    def test_handler_bindings__on_event__errors(self) -> None:
        """Test out HotkeyBindingsTarget.on_event when the target is closed."""

        context = unittest.mock.Mock(EventRegistryContext())
        handler = unittest.mock.Mock(hotkey.HotkeyHandler())
        problems = hotkey.BoundKeyProblems()
        problems.master_problem = StdRet.pass_errmsg('c', i18n('m'))
        problems.sequence_problems['a'] = RET_OK_NONE
        problems.sequence_problems['x'] = StdRet.pass_errmsg('c', i18n('x'))
        handler.set_hotkey_bindings.return_value = problems
        context.send_event.return_value = RET_OK_NONE
        target = hotkey.HotkeyBindingsTarget(context, handler)
        self.assertFalse(
            target.on_event('s', 't', hotkey_event.SetHotkeyBindingsEvent(
                1, hotkey_event.MasterHotkeySequence('m', []), [],
            ))
        )
        handler.set_hotkey_bindings.assert_called_once()
        context.send_event.assert_called_once()
        self.assertEqual(
            (
                hotkey_event.SetHotkeyBindingsEvent.UNIQUE_TARGET_FQN,
                's',
            ),
            context.send_event.call_args[0][0:2],
        )
        event = context.send_event.call_args[0][2]
        self.assertIsInstance(event, hotkey_event.SetHotkeyBindingsFailedEvent)
        assert isinstance(  # nosec  # mypy required
            event, hotkey_event.SetHotkeyBindingsFailedEvent,
        )
        self.assertIsNotNone(event.master_problem)
        self.assertEqual(
            {'sequence_type': 'm', 'sequence': []},
            not_none(event.master_problem).master.export_data(),
        )

    def test_handler_bindings__on_event__ok(self) -> None:
        """Test out HotkeyBindingsTarget.on_event when the target is closed."""

        context = unittest.mock.Mock(EventRegistryContext())
        handler = unittest.mock.Mock(hotkey.HotkeyHandler())
        handler.set_hotkey_bindings.return_value = hotkey.BoundKeyProblems()
        context.send_event.return_value = RET_OK_NONE
        target = hotkey.HotkeyBindingsTarget(context, handler)
        self.assertFalse(
            target.on_event('s', 't', hotkey_event.SetHotkeyBindingsEvent(
                1, hotkey_event.MasterHotkeySequence('m', []), [],
            ))
        )
        handler.set_hotkey_bindings.assert_called_once()
        context.send_event.assert_called()

        # Should have sent a "success" and a "set state" event.
        self.assertEqual(2, len(context.send_event.mock_calls))

        self.assertEqual(
            (
                hotkey_event.SetHotkeyBindingsEvent.UNIQUE_TARGET_FQN,
                's',
            ),
            context.send_event.mock_calls[0].args[0:2],
        )
        event = context.send_event.mock_calls[0].args[2]
        self.assertIsInstance(event, hotkey_event.SetHotkeyBindingsSuccessEvent)

        self.assertEqual(
            (
                hotkey_event.HotkeyBindingsState.UNIQUE_TARGET_FQN,
                datastore.StoreDataEvent.UNIQUE_TARGET_FQN,
            ),
            context.send_event.mock_calls[1].args[0:2],
        )
        event = context.send_event.mock_calls[1].args[2]
        self.assertIsInstance(event, datastore.StoreDataEvent)
        assert isinstance(event, datastore.StoreDataEvent)  # nosec  # mypy required
        self.assertEqual(
            json.loads(event.json),
            {'master': {'sequence': [], 'sequence_type': 'm'}, 'bound': []},
        )
