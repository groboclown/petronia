"""Test the module"""


import unittest
import unittest.mock
import time
from petronia_common.event_stream.tests.shared import create_read_stream, SimpleBinaryWriter
from petronia_common.util import PetroniaReturnError
from .. import lookup, EventObjectParser, EventBinaryTarget, EventObjectTarget
from ...events import logging


class LookupTest(unittest.TestCase):
    """Test the functions and classes in the module."""

    def test_register_event__duplicate(self) -> None:
        """Test register_event, running it twice to get a duplicate problem."""
        context = lookup.LookupEventRegistryContext(
            create_read_stream(b''), SimpleBinaryWriter(), None, None,
        )
        res = context.register_event_parser(
            logging.SystemErrorEvent.FULL_EVENT_NAME,
            logging.SystemErrorEvent.parse_data,
        )
        self.assertIsNone(res.error)

        # Exact same item should not generate an error...
        res = context.register_event(
            logging.SystemErrorEvent.FULL_EVENT_NAME,
            EventObjectParser(logging.SystemErrorEvent.parse_data),
        )
        self.assertIsNone(res.error)

        # A different parser should generate an error
        res = context.register_event(
            logging.SystemErrorEvent.FULL_EVENT_NAME,
            EventObjectParser(logging.LogEvent.parse_data),
        )
        self.assertEqual(
            [f'parser for event {logging.SystemErrorEvent.FULL_EVENT_NAME} already registered'],
            [m.debug() for m in res.error_messages()],
        )

    def test_register_binary_target(self) -> None:
        """Test the register_binary_target method"""
        context = lookup.LookupEventRegistryContext(
            create_read_stream(b''), SimpleBinaryWriter(), None, None,
        )
        res = context.register_binary_target(
            'e1', 't1', EventBinaryTarget(),
        )
        self.assertIsNone(res.error)
        res = context.register_binary_target(
            'e2', 't1', EventBinaryTarget(), None, 1.0,
        )
        self.assertIsNone(res.error)
        res = context.register_binary_target(
            'e1', 't2', EventBinaryTarget(),
        )
        self.assertEqual(
            ['a target handler for binary event e1 is already registered'],
            [m.debug() for m in res.error_messages()],
        )

    def test_register_target(self) -> None:
        """Test the register_target method."""
        context = lookup.LookupEventRegistryContext(
            create_read_stream(b''), SimpleBinaryWriter(), None, None,
        )
        res = context.register_event_parser(
            'e',
            logging.SystemErrorEvent.parse_data,
        )
        self.assertIsNone(res.error)

        # Register with an unregistered event parser.
        res = context.register_target('e1', None, EventObjectTarget())
        self.assertEqual(
            [
                'event ID e1 does not have a registered parser',
            ],
            [m.debug() for m in res.error_messages()],
        )

        # Register with an unregistered event parser, and the timer is given.
        res = context.register_target('e1', None, EventObjectTarget(), timeout=2.0)
        self.assertEqual(
            [
                'event ID e1 does not have a registered parser',
            ],
            [m.debug() for m in res.error_messages()],
        )

        # Register with a registered event parser, and the timer is given.
        res = context.register_target('e', None, EventObjectTarget(), timeout=2.0)
        self.assertIsNone(res.error)

        # Register with a registered event parser + handler, and no timer is given.
        res = context.register_target('e', None, EventObjectTarget())
        self.assertIsNone(res.error)

    def test_timeout(self) -> None:
        """Test timeout handling."""
        target1 = unittest.mock.Mock(EventObjectTarget())
        target1.on_event.return_value = False
        target2 = unittest.mock.Mock(EventObjectTarget())
        target2.on_event.return_value = False
        target3 = unittest.mock.Mock(EventObjectTarget())
        target3.on_event.return_value = False
        target4 = unittest.mock.Mock(EventObjectTarget())
        target4.on_event.return_value = False
        target5 = unittest.mock.Mock(EventObjectTarget())
        target5.on_event.return_value = False
        target6 = unittest.mock.Mock(EventBinaryTarget())
        target6.on_event.return_value = False
        target7 = unittest.mock.Mock(EventBinaryTarget())
        target7.on_event.return_value = False
        context = TestableLookupEventRegistryContext(
            create_read_stream(b''), SimpleBinaryWriter(), None, None,
        )
        res = context.register_event_parser(
            'e',
            logging.SystemErrorEvent.parse_data,
        )
        self.assertIsNone(res.error)

        res = context.register_target('e', None, target1, timeout=0.001)
        self.assertIsNone(res.error)
        res = context.register_target('e', None, target2, timeout=0.001)
        self.assertIsNone(res.error)
        res = context.register_target('e', 'x', target3, timeout=0.001)
        self.assertIsNone(res.error)
        res = context.register_target('e', 'x', target4, timeout=100.0)
        self.assertIsNone(res.error)
        res = context.register_target('e', 'y', target5, timeout=-1)
        self.assertIsNone(res.error)
        res = context.register_binary_target('e1', 'x', target6, timeout=0.001)
        self.assertIsNone(res.error)
        res = context.register_binary_target('e2', None, target7, timeout=-1)
        self.assertIsNone(res.error)

        time.sleep(0.1)

        context.inner__handle_timeouts()

        target1.on_close.assert_called()
        target2.on_close.assert_called()
        target3.on_close.assert_called()
        target4.on_close.assert_not_called()
        target5.on_close.assert_not_called()
        target6.on_close.assert_called()
        target7.on_close.assert_not_called()

    def test_end_of_stream(self) -> None:
        """Test end-of-stream handling."""
        target1 = unittest.mock.Mock(EventObjectTarget())
        target1.on_event.return_value = False
        target2 = unittest.mock.Mock(EventObjectTarget())
        target2.on_event.return_value = False
        target3 = unittest.mock.Mock(EventObjectTarget())
        target3.on_event.return_value = False
        target4 = unittest.mock.Mock(EventObjectTarget())
        target4.on_event.return_value = False
        target5 = unittest.mock.Mock(EventObjectTarget())
        target5.on_event.return_value = False
        target6 = unittest.mock.Mock(EventBinaryTarget())
        target6.on_event.return_value = False
        target7 = unittest.mock.Mock(EventBinaryTarget())
        target7.on_event.return_value = False
        context = TestableLookupEventRegistryContext(
            create_read_stream(b''), SimpleBinaryWriter(), None, None,
        )
        res = context.register_event_parser(
            'e',
            logging.SystemErrorEvent.parse_data,
        )
        self.assertIsNone(res.error)

        res = context.register_target('e', None, target1, timeout=0.001)
        self.assertIsNone(res.error)
        res = context.register_target('e', None, target2, timeout=0.001)
        self.assertIsNone(res.error)
        res = context.register_target('e', 'x', target3, timeout=0.001)
        self.assertIsNone(res.error)
        res = context.register_target('e', 'x', target4, timeout=100.0)
        self.assertIsNone(res.error)
        res = context.register_target('e', 'y', target5, timeout=-1)
        self.assertIsNone(res.error)
        res = context.register_binary_target('e1', 'x', target6, timeout=0.001)
        self.assertIsNone(res.error)
        res = context.register_binary_target('e2', None, target7, timeout=-1)
        self.assertIsNone(res.error)

        # Input stream is empty, but we'll also stop the reading before we do any reading.
        context.stop_reader()
        context.process_reader('x')

        target1.on_close.assert_called()
        target2.on_close.assert_called()
        target3.on_close.assert_called()
        target4.on_close.assert_called()
        target5.on_close.assert_called()
        target6.on_close.assert_called()
        target7.on_close.assert_called()


class TestableLookupEventRegistryContext(lookup.LookupEventRegistryContext):
    """A testable version."""

    def inner__eof_listener(self) -> None:
        """Inner access"""
        self._eof_listener()

    def inner__error_listener(self, error: PetroniaReturnError) -> bool:
        """inner access"""
        return self._error_listener(error)

    def inner__handle_timeouts(self) -> None:
        """inner access"""
        self._handle_timeouts()
