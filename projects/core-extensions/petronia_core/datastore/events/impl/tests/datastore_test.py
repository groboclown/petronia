# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-09T22:29:00.144263+00:00

"""
Tests for the datastore module.
Extension petronia.core.api.datastore, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import datastore


class StoreDataEventTest(unittest.TestCase):
    """
    Tests for StoreDataEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in STORE_DATA_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = datastore.StoreDataEvent.parse_data(test_data)
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
        for test_name, test_data in STORE_DATA_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = datastore.StoreDataEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


STORE_DATA_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='json', name='StoreDataEvent'),
            ),

        ),
    ),

]


STORE_DATA_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'json': 'kΐԦĮȸϴԅˇԨΣ\u038bхƪɸ\x90ΎΊ1\u0378ɿǗӈOӞǏзPċΑ\xad',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'json': '.\u0380',

        },
    ),
]


class DeleteDataEventTest(unittest.TestCase):
    """
    Tests for DeleteDataEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in DELETE_DATA_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = datastore.DeleteDataEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


DELETE_DATA_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]


class SendStateEventTest(unittest.TestCase):
    """
    Tests for SendStateEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SEND_STATE_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = datastore.SendStateEvent.parse_data(test_data)
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
        for test_name, test_data in SEND_STATE_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = datastore.SendStateEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SEND_STATE_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='store_id', name='SendStateEvent'),
            ),

        ),
    ),

]


SEND_STATE_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'store_id': 'Iơȭ\x93tΧύεȰǔŧŞGȦ\x98ˮњǊΓǀEþ\x92ťϰ\u038b˩ɇϰđ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'store_id': 'Ľ0ŕɈǼ',

        },
    ),
]


class DataUpdateEventTest(unittest.TestCase):
    """
    Tests for DataUpdateEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in DATA_UPDATE_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = datastore.DataUpdateEvent.parse_data(test_data)
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
        for test_name, test_data in DATA_UPDATE_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = datastore.DataUpdateEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


DATA_UPDATE_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='changed', name='DataUpdateEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='json', name='DataUpdateEvent'),
            ),

        ),
    ),

]


DATA_UPDATE_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'changed': '20210209:222900.075614:+0000',
            'json': 'ˍЉмBǔʿɓ\x90˫ҜŮԮɹĩѤýX˒\x90ŨĭǗªԍ˷ɣ)ŷū˧',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'changed': '20210209:222900.075653:+0000',

            'json': 'ǸЖ',

        },
    ),
]


class DataRemovedEventTest(unittest.TestCase):
    """
    Tests for DataRemovedEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in DATA_REMOVED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = datastore.DataRemovedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


DATA_REMOVED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]