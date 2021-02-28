# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-28T02:46:12.016194+00:00

"""
Tests for the timer module.
Extension petronia.core.api.timer, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import timer

class HeartbeatEventTest(unittest.TestCase):
    """
    Tests for HeartbeatEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in HEARTBEAT_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = timer.HeartbeatEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = {
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                }
                actual = list(res.valid_error.messages())
                # The parsing returns at least one of the problems, but not necessarily all.
                self.assertTrue(len(actual) >= 1, repr(expected))
                self.assertTrue(expected.issuperset(actual), repr(expected))

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in HEARTBEAT_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = timer.HeartbeatEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


HEARTBEAT_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='sent_on', name='HeartbeatEvent'),
            ),

        ),
    ),

]


HEARTBEAT_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'sent_on': '20210228:024611.953345:+0000',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sent_on': '20210228:024611.953385:+0000',

        },
    ),
]

class HeartbeatIntervalStateTest(unittest.TestCase):
    """
    Tests for HeartbeatIntervalState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in HEARTBEAT_INTERVAL_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = timer.HeartbeatIntervalState.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = {
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                }
                actual = list(res.valid_error.messages())
                # The parsing returns at least one of the problems, but not necessarily all.
                self.assertTrue(len(actual) >= 1, repr(expected))
                self.assertTrue(expected.issuperset(actual), repr(expected))

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in HEARTBEAT_INTERVAL_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = timer.HeartbeatIntervalState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


HEARTBEAT_INTERVAL_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='seconds', name='HeartbeatIntervalState'),
            ),

        ),
    ),

]


HEARTBEAT_INTERVAL_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'seconds': 349604.2115839956,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'seconds': 887460.2689976706,

        },
    ),
]
