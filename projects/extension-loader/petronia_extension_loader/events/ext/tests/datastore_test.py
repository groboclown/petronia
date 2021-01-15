# GENERATED CODE - DO NOT MODIFY
# Created on 2021-01-15T16:34:25.482427

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
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

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
                dict(field_name='destination', name='StoreDataEvent'),
            ),
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
            'destination': 'ʹyēØԂLúĄўԪD±ёǔѡɊșƼӘ\u03a2ϛϱҭĆɃ!ȐŽʐ¿',
            'json': 'ϐϵсӚ˻Ґ\x89ǃȮʗƜѤǘÀƏûҋȽ_ЉԆǡƕђĮԪąϹǉ¸',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'destination': '',

            'json': '',

        },
    ),
]


class DeleteDataEventTest(unittest.TestCase):
    """
    Tests for DeleteDataEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in DELETE_DATA_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = datastore.DeleteDataEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in DELETE_DATA_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = datastore.DeleteDataEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


DELETE_DATA_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='destination', name='DeleteDataEvent'),
            ),

        ),
    ),

]


DELETE_DATA_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'destination': 'ӱҒəʾΎ¿ƁѮϖ˥ĞҶˠͱĳ×WбȻʹ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'destination': '',

        },
    ),
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
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

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
                dict(field_name='destination', name='SendStateEvent'),
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
            'destination': "іІʛ\\ӈ\u0383.ćʊįȿҡϸŭůЌpͱЄŎϚ@ҍº¬'ŨIͲɦ",
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'destination': '',

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
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

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
            'changed': 'YYYYMMDD:hhmmss.sss:Z',
            'json': 'ŧȮĆEҎϢʜǛԍǖΎĊǕ»ԁɤÎÄʖҔӣȈȰćǃϋǆͿǬӂ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'changed': 'YYYYMMDD:hhmmss.sss:Z',

            'json': '',

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
