"""Test the module."""

import unittest
import unittest.mock
from petronia_common.util import RET_OK_NONE
from petronia_ext_lib.runner import EventRegistryContext, EventObjectTarget
from ..events.impl import hotkey_binding as hotkey_binding_event
from ..events.ext import hotkey as native_hotkey_event
from .. import bind_handler, shared_state


class BindHandlerTest(unittest.TestCase):
    """Test the module's functions and classes."""

    def setUp(self) -> None:
        shared_state.clear_data()

    def test_register_bind_handlers(self) -> None:
        """Test register_bind_handlers"""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        context.register_event_parser.return_value = RET_OK_NONE
        context.register_target.return_value = RET_OK_NONE
        res = bind_handler.register_bind_handlers(context)
        self.assertIsNone(res.error)

    def test_hotkey_pressed_callback(self) -> None:
        """Test create_on_hotkey_pressed_callback and the returned callback."""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        shared_state.set_master_sequence('meta', ['rwin'])
        bound_event = hotkey_binding_event.BoundEvent(
            't1', [],
        )
        shared_state.set_bound_key(['a', 'b'], None, bound_event)
        res = bind_handler.create_on_hotkey_pressed_callback(context)
        res(['a'])
        context.send_event.assert_not_called()
        res(['a', 'b'])
        context.send_event.assert_called_once()
        args = context.send_event.call_args.args
        self.assertEqual(len(args), 3)
        self.assertEqual(args[0], hotkey_binding_event.HotkeyFiredEvent.UNIQUE_TARGET_FQN)
        self.assertEqual(args[1], 't1')
        self.assertIsInstance(args[2], hotkey_binding_event.HotkeyFiredEvent)
        event = args[2]
        assert isinstance(event, hotkey_binding_event.HotkeyFiredEvent)  # nosec  # for mypy
        self.assertIs(event.event, bound_event)

    def test_extension_event_register(self) -> None:
        """Test the ExtensionEventRegisterEventTarget class"""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        target = bind_handler.ExtensionEventRegisterEventTarget(context)
        self.assertFalse(target.on_context_event(
            context, 's1', 't1', hotkey_binding_event.ExtensionEventRegisterEvent(
                'n1', 'd1', 't1', [],
            ),
        ))
        events = shared_state.get_extension_events()
        self.assertEqual(1, len(events))
        self.assertEqual('n1', events[0].name)
        context.send_event.assert_called_once()

    def test_set_master_sequence_request(self) -> None:
        """Test the SetMasterSequenceRequestEventTarget class"""
        context = unittest.mock.Mock(EventRegistryContext())
        context.send_event.return_value = RET_OK_NONE
        context.register_target.return_value = RET_OK_NONE
        target = bind_handler.SetMasterSequenceRequestEventTarget(context)
        self.assertFalse(target.on_context_event(
            context, 's1', 't1', hotkey_binding_event.SetMasterSequenceRequestEvent(
                'abc', ['rwin', 'ralt'], None,
            ),
        ))
        calls = context.method_calls
        self.assertEqual(3, len(calls))
        register_success_target = calls[0]
        self.assertEqual('register_target', register_success_target[0])
        self.assertEqual(
            native_hotkey_event.SetHotkeyBindingsSuccessEvent.FULL_EVENT_NAME,
            register_success_target.args[0],
        )
        success_target = register_success_target.args[2]
        self.assertIsInstance(success_target, EventObjectTarget)
        assert isinstance(success_target, EventObjectTarget)  # nosec  # for mypy

        register_failure_target = calls[1]
        self.assertEqual('register_target', register_failure_target[0])
        self.assertEqual(
            native_hotkey_event.SetHotkeyBindingsFailedEvent.FULL_EVENT_NAME,
            register_failure_target.args[0],
        )
        failure_target = register_failure_target.args[2]
        self.assertIsInstance(failure_target, EventObjectTarget)
        assert isinstance(failure_target, EventObjectTarget)  # nosec  # for mypy

        send_event_target = calls[2]
        self.assertEqual('send_event', send_event_target[0])
        self.assertEqual(
            native_hotkey_event.SetHotkeyBindingsEvent.UNIQUE_TARGET_FQN,
            send_event_target.args[1],
        )
        bind_event = send_event_target.args[2]
        self.assertIsInstance(bind_event, native_hotkey_event.SetHotkeyBindingsEvent)
        assert isinstance(  # nosec  # for mypy
            bind_event, native_hotkey_event.SetHotkeyBindingsEvent,
        )
        self.assertEqual('abc', bind_event.master.sequence_type)
        self.assertEqual(['rwin', 'ralt'], bind_event.master.sequence)

        # Now try out the callbacks.
        context.reset_mock()
        context.send_event.return_value = RET_OK_NONE

        # Due to the use of the decision chain, only one will trigger an event.
        success_target.on_event('s1', 't1', native_hotkey_event.SetHotkeyBindingsSuccessEvent(
            bind_event.request,
        ))
        calls = context.method_calls
        self.assertEqual(2, len(calls))
        self.assertEqual(calls[0][0], 'send_event')
        self.assertEqual(calls[1][0], 'send_event')
        self.assertEqual('abc', shared_state.get_master_sequence().sequence_type)
        self.assertEqual(['rwin', 'ralt'], shared_state.get_master_sequence().sequence)
