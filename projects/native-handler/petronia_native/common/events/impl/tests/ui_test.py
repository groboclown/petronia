# GENERATED CODE - DO NOT MODIFY

"""
Tests for the ui module.
Extension petronia.core.api.native.ui, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

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
            'locale': 'ІąЭӅ',
            'format': 'ӤƔЉԩʼ\u0380ѓҗѽz˱Ļѯјȉ3ʏдћŢǪ͵Ǔ7Ԅȋ˂Ӯȕâ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale': 'Ɛ',

            'format': 'ȝ',

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
            'identifier': 8169017,
            'mouse_buttons': [
                3660461504220348046,
                -1158302147379922736,
                -1842220351355844075,
                -1476231485407829188,
                8567970357046981628,
                -6658247164923184127,
                7109310148680576664,
                6430984091574674059,
                2837901638984408733,
                -8103093797135407023,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 6558793,

            'mouse_buttons': [
                1293558003487294325,
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
            'identifier': 5504415,
            'text': 'Ô_ĭŴҕƾĠŧďɺǬɸѵŤŖʓͼòͻƳɋƢțȲˮyaҔӨh',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 3913791,

            'text': '',

        },
    ),
]
