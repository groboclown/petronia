"""Test the module"""

import unittest
from petronia_common.event_stream.tests.shared import create_read_stream, SimpleBinaryWriter
from .. import single_threaded, EventObjectParser, EventBinaryTarget, EventObjectTarget
from ...events import logging


class SingleThreadedTest(unittest.TestCase):
    """Test the functions and classes in the module."""

    def test_register_event__duplicate(self) -> None:
        """Test register_event, running it twice to get a duplicate problem."""
        context = single_threaded.SingleThreadedEventRegistryContext(
            create_read_stream(b''), SimpleBinaryWriter(), None,
        )
        res = context.register_event_parser(
            logging.SystemErrorEvent.FULL_EVENT_NAME,
            logging.SystemErrorEvent.parse_data,
        )
        self.assertIsNone(res.error)
        res = context.register_event(
            logging.SystemErrorEvent.FULL_EVENT_NAME,
            EventObjectParser(logging.SystemErrorEvent.parse_data),
        )
        self.assertIsNone(res.error)
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
        context = single_threaded.SingleThreadedEventRegistryContext(
            create_read_stream(b''), SimpleBinaryWriter(), None,
        )
        res = context.register_binary_target(
            'e1', 't1', EventBinaryTarget(),
        )
        self.assertEqual(
            [],
            [m.debug() for m in res.error_messages()],
        )

    def test_register_target(self) -> None:
        """Test the register_target method."""
        context = single_threaded.SingleThreadedEventRegistryContext(
            create_read_stream(b''), SimpleBinaryWriter(), None,
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
                'register_target: validation error',
                'event ID e1 does not have a registered parser',
             ],
            [m.debug() for m in res.error_messages()],
        )

        # Register with an unregistered event parser, and the timer is given.
        res = context.register_target('e1', None, EventObjectTarget(), timeout=2.0)
        self.assertEqual(
            [
                'register_target: validation error',
                'event ID e1 does not have a registered parser',
                "only targets that don't time out are supported.",
            ],
            [m.debug() for m in res.error_messages()],
        )

        # Register with a registered event parser, and the timer is given.
        res = context.register_target('e', None, EventObjectTarget(), timeout=2.0)
        self.assertEqual(
            [
                'register_target: validation error',
                "only targets that don't time out are supported.",
            ],
            [m.debug() for m in res.error_messages()],
        )

        # Register with a registered event parser, and no timer is given.
        res = context.register_target('e', None, EventObjectTarget())
        self.assertIsNone(res.error)

        # Register with a registered event parser that already has a registration
        res = context.register_target('e', None, EventObjectTarget())
        self.assertEqual(
            [
                'register_target: validation error',
                'a target handler for event "e", target "None" is already registered',
            ],
            [m.debug() for m in res.error_messages()],
        )
