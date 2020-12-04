"""Test the module."""

from typing import List, Tuple, Optional, Any
import unittest
from concurrent.futures import ThreadPoolExecutor
from petronia_common.util import PetroniaReturnError
from petronia_common.event_stream import (
    to_raw_event_object,
)
from .. import event_handlers
from ...events import foreman


class ExtensionLoaderTargetTest(unittest.TestCase):
    """Test the ExtensionLoaderTarget class."""

    def test_can_consume__true(self) -> None:
        """Test all the can_consume events."""
        target = event_handlers.ExtensionLoaderTarget(
            TargetHandlerRuntimeContextImpl(), ThreadPoolExecutor(),
        )
        for event_id in event_handlers.CONSUMED_EXTENSION_LOADER_EVENT_IDS:
            self.assertTrue(target.can_consume(event_id, 'x', 'y'))

    def test_can_consume__false(self) -> None:
        """Test that an unknown event is reported as not consumed."""
        target = event_handlers.ExtensionLoaderTarget(
            TargetHandlerRuntimeContextImpl(), ThreadPoolExecutor(),
        )
        self.assertFalse(target.can_consume('xyz', 'x', 'y'))

    def test_on_error(self) -> None:
        """Ensure on_error calls are handled as expected."""
        executor = ThreadPoolExecutor()
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.ExtensionLoaderTarget(context, executor)
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
        executor = ThreadPoolExecutor()
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.ExtensionLoaderTarget(context, executor)

        target.on_eof()

        self.assertEqual(
            [
                ('do_restart', False, None,),
            ],
            context.call_order,
        )

    def test_consume_unknown_event(self) -> None:
        """Test consuming an unknown event id."""
        executor = ThreadPoolExecutor()
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.ExtensionLoaderTarget(context, executor)

        self.assertFalse(
            target.consume(to_raw_event_object(
                'unknown', 'source', 'target', {},
            ))
        )

        self.assertEqual([], context.call_order)

    def test_consume_start_launcher(self) -> None:
        """Test consuming a start_launcher event."""
        executor = ThreadPoolExecutor()
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.ExtensionLoaderTarget(context, executor)

        self.assertFalse(
            target.consume(to_raw_event_object(
                foreman.StartLauncherRequestEvent.FULL_EVENT_NAME, 'source', 'target',
                foreman.StartLauncherRequestEvent(
                    'the-id', 'the-launcher', [],
                ).export_data(),
            ))
        )

        self.assertEqual(1, len(context.call_order))
        self.assertEqual('start_launcher', context.call_order[0][0])
        self.assertIsNone(context.call_order[0][1])
        event = context.call_order[0][2]
        self.assertIsInstance(event, foreman.StartLauncherRequestEvent)
        assert isinstance(event, foreman.StartLauncherRequestEvent)  # mypy requirement
        # We're not testing event export and parsing.
        self.assertEqual(event.launcher, 'the-launcher')

    def test_consume_load_extension(self) -> None:
        """Test consuming a start_launcher event."""
        executor = ThreadPoolExecutor()
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.ExtensionLoaderTarget(context, executor)

        self.assertFalse(
            target.consume(to_raw_event_object(
                foreman.LauncherLoadExtensionRequestEvent.FULL_EVENT_NAME, 'source', 'target',
                foreman.LauncherLoadExtensionRequestEvent(
                    'the-name', [1, 2, 3], 'the-location',
                ).export_data(),
            ))
        )

        self.assertEqual(1, len(context.call_order))
        self.assertEqual('load_extension', context.call_order[0][0])
        self.assertEqual('target', context.call_order[0][1])
        event = context.call_order[0][2]
        self.assertIsInstance(event, foreman.LauncherLoadExtensionRequestEvent)
        assert isinstance(event, foreman.LauncherLoadExtensionRequestEvent)  # mypy requirement
        # We're not testing event export and parsing.
        self.assertEqual(event.name, 'the-name')

    def test_consume_add_event_listener(self) -> None:
        """Test consuming a start_launcher event."""
        executor = ThreadPoolExecutor()
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.ExtensionLoaderTarget(context, executor)

        self.assertFalse(
            target.consume(to_raw_event_object(
                foreman.ExtensionAddEventListenerEvent.FULL_EVENT_NAME, 'source', 'target',
                foreman.ExtensionAddEventListenerEvent(
                    'extension-name', [],
                ).export_data(),
            ))
        )

        self.assertEqual(1, len(context.call_order))
        self.assertEqual('add_event_listener', context.call_order[0][0])
        self.assertEqual('target', context.call_order[0][1])
        event = context.call_order[0][2]
        self.assertIsInstance(event, foreman.ExtensionAddEventListenerEvent)
        assert isinstance(event, foreman.ExtensionAddEventListenerEvent)  # mypy requirement
        # We're not testing event export and parsing.
        self.assertEqual(event.extension_name, 'extension-name')

    def test_consume_remove_event_listener(self) -> None:
        """Test consuming a start_launcher event."""
        executor = ThreadPoolExecutor()
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.ExtensionLoaderTarget(context, executor)

        self.assertFalse(
            target.consume(to_raw_event_object(
                foreman.ExtensionRemoveEventListenerEvent.FULL_EVENT_NAME, 'source', 'target',
                foreman.ExtensionRemoveEventListenerEvent(
                    'extension-name', [],
                ).export_data(),
            ))
        )

        self.assertEqual(1, len(context.call_order))
        self.assertEqual('remove_event_listener', context.call_order[0][0])
        self.assertEqual('target', context.call_order[0][1])
        event = context.call_order[0][2]
        self.assertIsInstance(event, foreman.ExtensionRemoveEventListenerEvent)
        assert isinstance(event, foreman.ExtensionRemoveEventListenerEvent)  # mypy requirement
        # We're not testing event export and parsing.
        self.assertEqual(event.extension_name, 'extension-name')


class InternalTargetTest(unittest.TestCase):
    """Test the InternalTarget class."""

    def test_can_consume__true(self) -> None:
        """Test all the can_consume events."""
        target = event_handlers.InternalTarget(
            TargetHandlerRuntimeContextImpl(), ThreadPoolExecutor(),
        )
        for event_id in event_handlers.CONSUMED_INTERNAL_EVENT_IDS:
            self.assertTrue(target.can_consume(event_id, 'x', 'y'))

    def test_can_consume__false(self) -> None:
        """Test that an unknown event is reported as not consumed."""
        target = event_handlers.InternalTarget(
            TargetHandlerRuntimeContextImpl(), ThreadPoolExecutor()
        )
        self.assertFalse(target.can_consume('xyz', 'x', 'y'))

    def test_on_error(self) -> None:
        """Ensure on_error calls are handled as expected."""
        executor = ThreadPoolExecutor()
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.InternalTarget(context, executor)
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
        executor = ThreadPoolExecutor()
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.InternalTarget(context, executor)

        target.on_eof()

        self.assertEqual(
            [
                ('do_restart', False, None,),
            ],
            context.call_order,
        )

    def test_consume_unknown_event(self) -> None:
        """Test consuming an unknown event id."""
        executor = ThreadPoolExecutor()
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.InternalTarget(context, executor)

        self.assertFalse(
            target.consume(to_raw_event_object(
                'unknown', 'source', 'target', {},
            ))
        )

        self.assertEqual([], context.call_order)

    def test_consume_stop(self) -> None:
        """Test consuming a stop event."""
        executor = ThreadPoolExecutor()
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.InternalTarget(context, executor)

        self.assertFalse(
            target.consume(to_raw_event_object(
                foreman.StopEvent.FULL_EVENT_NAME, 'source', 'target',
                foreman.StopEvent().export_data(),
            ))
        )

        self.assertEqual(
            [
                ('do_shutdown', None, None,),
            ],
            context.call_order,
        )

    def test_consume_restart(self) -> None:
        """Test consuming a restart event."""
        executor = ThreadPoolExecutor()
        context = TargetHandlerRuntimeContextImpl()
        target = event_handlers.InternalTarget(context, executor)

        self.assertFalse(
            target.consume(to_raw_event_object(
                foreman.RestartEvent.FULL_EVENT_NAME, 'source', 'target',
                foreman.RestartEvent().export_data(),
            ))
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

    def start_launcher(
            self, source_id: str, event: foreman.StartLauncherRequestEvent,
    ) -> None:
        self.call_order.append(('start_launcher', None, event,))

    def load_extension(
            self, source_id: str, target_id: str, event: foreman.LauncherLoadExtensionRequestEvent,
    ) -> None:
        self.call_order.append(('load_extension', target_id, event,))

    def add_event_listener(
            self, target_id: str, event: foreman.ExtensionAddEventListenerEvent,
    ) -> None:
        self.call_order.append(('add_event_listener', target_id, event,))

    def remove_event_listener(
            self, target_id: str, event: foreman.ExtensionRemoveEventListenerEvent,
    ) -> None:
        self.call_order.append(('remove_event_listener', target_id, event,))
