"""Test the module."""

import unittest
from petronia_common.util import UserMessage, i18n
from petronia_common.util.error import SimplePetroniaReturnError
from .. import router_context


class RouterContextTest(unittest.TestCase):
    """Test the class and functions in the module."""

    def test_launcher_id_as_target_id(self) -> None:
        """Tests for launcher_id_as_target_id."""
        self.assertEqual(
            router_context.LAUNCHER_TARGET_PREFIX + 'lau1',
            router_context.launcher_id_as_target_id('lau1'),
        )

    def test_target_id_as_launcher_id(self) -> None:
        """Combined tests for target_id_as_launcher_id."""
        self.assertEqual(
            'abc',
            router_context.target_id_as_launcher_id(router_context.LAUNCHER_TARGET_PREFIX + 'abc'),
        )
        self.assertIsNone(
            router_context.target_id_as_launcher_id('abc')
        )
        self.assertIsNone(
            router_context.target_id_as_launcher_id('')
        )

    def test_create_handler_id(self) -> None:
        """Test the create_handler_id function."""
        self.assertEqual(
            'cat1:lau1:ext1',
            router_context.create_handler_id('cat1', 'lau1', 'ext1'),
        )

    def test_create_event_error__no_messages(self) -> None:
        """Create an event error with no messages."""
        res = router_context.create_event_error(
            'id1', None, SimplePetroniaReturnError(),
        )
        self.assertEqual('id1', res.identifier)
        self.assertIsNone(res.source)
        self.assertEqual('', res.message)
        self.assertEqual(0, len(res.arguments))

    def test_create_event_error__one_message(self) -> None:
        """Create an event error with one message."""
        res = router_context.create_event_error(
            'id1', None, SimplePetroniaReturnError(
                UserMessage('x', i18n('m1 {m2}'), m2='abc'),
            ),
        )
        self.assertEqual('id1', res.identifier)
        self.assertIsNone(res.source)
        self.assertEqual('m1 {m2}', res.message)
        self.assertEqual(1, len(res.arguments))
        self.assertEqual('m2', res.arguments[0].name)
        self.assertEqual('abc', res.arguments[0].value)

    def test_create_event_error__two_messages(self) -> None:
        """Create an event error with two messages, including complex arg type."""
        res = router_context.create_event_error(
            'id1', None, SimplePetroniaReturnError(
                UserMessage('x', i18n('m1 {m2}'), m2='abc'),
                UserMessage('x', i18n('a1 {a2}'), a2=['abc', 1, True]),
            ),
        )
        self.assertEqual('id1', res.identifier)
        self.assertIsNone(res.source)
        self.assertEqual('m1 {m2}; a1 {a2}', res.message)
        self.assertEqual(2, len(res.arguments))
        self.assertEqual('m2', res.arguments[0].name)
        self.assertEqual('abc', res.arguments[0].value)
        self.assertEqual('a2', res.arguments[1].name)
        self.assertEqual("['abc', 1, True]", res.arguments[1].value)
