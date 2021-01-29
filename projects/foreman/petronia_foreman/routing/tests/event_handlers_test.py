"""Test the module."""

from typing import List, Tuple, Optional, Any
import unittest
from petronia_common.util import PetroniaReturnError
from .. import event_handlers
from ...events import foreman


class ExtensionLoaderTargetTest(unittest.TestCase):
    """Test the ExtensionLoaderTarget class."""

    def test_can_consume__true(self) -> None:
        """Test all the can_consume events."""
        target = event_handlers.ExtensionLoaderTarget(TargetHandlerRuntimeContextImpl())
        for event_id in event_handlers.CONSUMED_EXTENSION_LOADER_EVENT_IDS:
            self.assertTrue(target.can_consume(event_id, 'x', 'y'))

    def test_can_consume__false(self) -> None:
        """Test that an unknown event is reported as not consumed."""
        target = event_handlers.ExtensionLoaderTarget(TargetHandlerRuntimeContextImpl())
        self.assertFalse(target.can_consume('xyz', 'x', 'y'))

    def test_on_error(self) -> None:
        """Ensure on_error calls are handled as expected."""
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.ExtensionLoaderTarget(context)
        error = PetroniaReturnError()

        self.assertFalse(target.on_error(error))

        self.assertEqual(
            [
                ('do_restart', False, error,),
            ],
            context.call_order,
        )

    def test_on_eof(self) -> None:
        """Ensure on_eof calls are handled as expected."""
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.ExtensionLoaderTarget(context)

        target.on_eof()

        self.assertEqual(
            [
                ('do_restart', False, None,),
            ],
            context.call_order,
        )

    def test_consume_unknown_event(self) -> None:
        """Test consuming an unknown event id."""
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.ExtensionLoaderTarget(context)

        self.assertFalse(target.consume_object('unknown', 'source', 'target', {}))

        self.assertEqual([], context.call_order)

    def test_consume_start_launcher(self) -> None:
        """Test consuming a start_launcher event."""
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.ExtensionLoaderTarget(context)

        self.assertFalse(
            target.consume_object(
                foreman.LauncherStartExtensionRequestEvent.FULL_EVENT_NAME, 'source', 'target',
                foreman.LauncherStartExtensionRequestEvent(
                    'the-id', [], [], 'the-launcher', [], None, [],
                ).export_data(),
            )
        )

        self.assertEqual(1, len(context.call_order))
        self.assertEqual('start_extension', context.call_order[0][0])
        self.assertEqual('target', context.call_order[0][1])
        event = context.call_order[0][2]
        self.assertIsInstance(event, foreman.LauncherStartExtensionRequestEvent)
        assert isinstance(event, foreman.LauncherStartExtensionRequestEvent)  # nosec
        # We're not testing event export and parsing.
        self.assertEqual(event.name, 'the-id')

    def test_consume_add_event_listener(self) -> None:
        """Test consuming a start_launcher event."""
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.ExtensionLoaderTarget(context)

        self.assertFalse(
            target.consume_object(
                foreman.ExtensionAddEventListenerEvent.FULL_EVENT_NAME, 'source', 'target',
                foreman.ExtensionAddEventListenerEvent(
                    [],
                ).export_data(),
            )
        )

        self.assertEqual(1, len(context.call_order))
        self.assertEqual('add_event_listener', context.call_order[0][0])
        self.assertEqual('target', context.call_order[0][1])
        event = context.call_order[0][2]
        self.assertIsInstance(event, foreman.ExtensionAddEventListenerEvent)
        assert isinstance(event, foreman.ExtensionAddEventListenerEvent)  # nosec

    def test_consume_remove_event_listener(self) -> None:
        """Test consuming a start_launcher event."""
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.ExtensionLoaderTarget(context)

        self.assertFalse(
            target.consume_object(
                foreman.ExtensionRemoveEventListenerEvent.FULL_EVENT_NAME, 'source', 'target',
                foreman.ExtensionRemoveEventListenerEvent(
                    [],
                ).export_data(),
            )
        )

        self.assertEqual(1, len(context.call_order))
        self.assertEqual('remove_event_listener', context.call_order[0][0])
        self.assertEqual('target', context.call_order[0][1])
        event = context.call_order[0][2]
        self.assertIsInstance(event, foreman.ExtensionRemoveEventListenerEvent)
        assert isinstance(event, foreman.ExtensionRemoveEventListenerEvent)  # nosec


class InternalTargetTest(unittest.TestCase):
    """Test the InternalTarget class."""

    def test_can_consume__true(self) -> None:
        """Test all the can_consume events."""
        target = event_handlers.InternalTarget(TargetHandlerRuntimeContextImpl())
        for event_id in event_handlers.CONSUMED_INTERNAL_EVENT_IDS:
            self.assertTrue(target.can_consume(event_id, 'x', 'y'))

    def test_can_consume__false(self) -> None:
        """Test that an unknown event is reported as not consumed."""
        target = event_handlers.InternalTarget(TargetHandlerRuntimeContextImpl())
        self.assertFalse(target.can_consume('xyz', 'x', 'y'))

    def test_on_error(self) -> None:
        """Ensure on_error calls are handled as expected."""
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.InternalTarget(context)
        error = PetroniaReturnError()

        self.assertFalse(target.on_error(error))

        self.assertEqual(
            [
                ('do_restart', False, error,),
            ],
            context.call_order,
        )

    def test_on_eof(self) -> None:
        """Ensure on_eof calls are handled as expected."""
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.InternalTarget(context)

        target.on_eof()

        self.assertEqual(
            [
                ('do_restart', False, None,),
            ],
            context.call_order,
        )

    def test_consume_unknown_event(self) -> None:
        """Test consuming an unknown event id."""
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.InternalTarget(context)

        self.assertFalse(
            target.consume_object(
                'unknown', 'source', 'target', {},
            )
        )

        self.assertEqual([], context.call_order)

    def test_consume_stop(self) -> None:
        """Test consuming a stop event."""
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.InternalTarget(context)

        self.assertFalse(
            target.consume_object(
                foreman.StopEvent.FULL_EVENT_NAME, 'source', 'target',
                foreman.StopEvent().export_data(),
            )
        )

        self.assertEqual(
            [
                ('do_shutdown', None, None,),
            ],
            context.call_order,
        )

    def test_consume_restart(self) -> None:
        """Test consuming a restart event."""
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.InternalTarget(context)

        self.assertFalse(
            target.consume_object(
                foreman.RestartEvent.FULL_EVENT_NAME, 'source', 'target',
                foreman.RestartEvent().export_data(),
            )
        )

        self.assertEqual(
            [
                ('do_restart', True, None,),
            ],
            context.call_order,
        )


class TargetHandlerRuntimeContextImpl(event_handlers.TargetHandlerRuntimeContext):
    """Monitor for the calls."""

    __slots__ = ('call_order',)

    def __init__(self) -> None:
        self.call_order: List[Tuple[str, Any, Any]] = []

    def do_shutdown(self) -> None:
        self.call_order.append(('do_shutdown', None, None))

    def do_restart(self, requested: bool, error: Optional[PetroniaReturnError]) -> None:
        self.call_order.append(('do_restart', requested, error,))

    def start_extension(
            self, source_id: str, target_id: str,
            event: foreman.LauncherStartExtensionRequestEvent,
    ) -> None:
        self.call_order.append(('start_extension', target_id, event,))

    def add_event_listener(
            self, target_id: str, event: foreman.ExtensionAddEventListenerEvent,
    ) -> None:
        self.call_order.append(('add_event_listener', target_id, event,))

    def remove_event_listener(
            self, target_id: str, event: foreman.ExtensionRemoveEventListenerEvent,
    ) -> None:
        self.call_order.append(('remove_event_listener', target_id, event,))
