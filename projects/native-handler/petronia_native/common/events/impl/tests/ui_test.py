# GENERATED CODE - DO NOT MODIFY

"""
Tests for the ui module.
Extension petronia.core.api.native.ui, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import ui


class RegisterImageDetailsEventTest(unittest.TestCase):
    """
    Tests for RegisterImageDetailsEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_IMAGE_DETAILS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = ui.RegisterImageDetailsEvent.parse_data(test_data)
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
        for test_name, test_data in REGISTER_IMAGE_DETAILS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = ui.RegisterImageDetailsEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTER_IMAGE_DETAILS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='locale', name='RegisterImageDetailsEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='format', name='RegisterImageDetailsEvent'),
            ),

        ),
    ),

]


REGISTER_IMAGE_DETAILS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'locale': 'CÉѸёɿΜԈǢϝȻ',
            'format': 'tƇҁІǹa¹ȴʿ\x94\x8fŗȗѨʀҖґ҃ĚǼɇŻӂër\x9b',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale': 'ʤ',

            'format': 'ѕ',

        },
    ),
]


class UiPanelClickedEventTest(unittest.TestCase):
    """
    Tests for UiPanelClickedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in UI_PANEL_CLICKED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = ui.UiPanelClickedEvent.parse_data(test_data)
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
        for test_name, test_data in UI_PANEL_CLICKED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = ui.UiPanelClickedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


UI_PANEL_CLICKED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='UiPanelClickedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='mouse_buttons', name='UiPanelClickedEvent'),
            ),

        ),
    ),

]


UI_PANEL_CLICKED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'identifier': 9465619,
            'mouse_buttons': [
                3032669418832288113,
                4952137317265817904,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 8621521,

            'mouse_buttons': [
                4148457379822190157,
            ],

        },
    ),
]


class UiTextFieldUpdateEventTest(unittest.TestCase):
    """
    Tests for UiTextFieldUpdateEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in UI_TEXT_FIELD_UPDATE_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = ui.UiTextFieldUpdateEvent.parse_data(test_data)
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
        for test_name, test_data in UI_TEXT_FIELD_UPDATE_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = ui.UiTextFieldUpdateEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


UI_TEXT_FIELD_UPDATE_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='UiTextFieldUpdateEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='text', name='UiTextFieldUpdateEvent'),
            ),

        ),
    ),

]


UI_TEXT_FIELD_UPDATE_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'identifier': 866596,
            'text': '҆į҅ƤȻǷӢĸ1ĶΕ4\x95ÐʕәξĄͿЏ\u0381ɸĭ\x8fĲȶʞԛʗÌ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 4093397,

            'text': '',

        },
    ),
]
