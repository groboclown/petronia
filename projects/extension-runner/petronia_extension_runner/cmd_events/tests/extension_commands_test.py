# GENERATED CODE - DO NOT MODIFY
# Created on 2021-01-15T16:34:27.737965

"""
Tests for the extension_commands module.
Extension petronia.internal.extension_commands, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import extension_commands


class InternalLoadExtensionRequestEventTest(unittest.TestCase):
    """
    Tests for InternalLoadExtensionRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in INTERNAL_LOAD_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_commands.InternalLoadExtensionRequestEvent.parse_data(test_data)
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
        for test_name, test_data in INTERNAL_LOAD_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_commands.InternalLoadExtensionRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


INTERNAL_LOAD_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='InternalLoadExtensionRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='InternalLoadExtensionRequestEvent'),
            ),

        ),
    ),

]


INTERNAL_LOAD_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': '5ԫŇuƍǑťΞŰˆǎŅÜ΅gʢ¼ӊ\x9c0ğĚ\x82Ƒ¨Ć˃˷ΫQ',
            'version': [
                4509812538886567135,
                -5087558354815545952,
                -6387185572479180272,
            ],
            'configuration': 'уą˸ӞçɠÂҥǢԧƶŉʷƍˇАýԓD±Ɂӹ҅ęГҟЏӆΕü',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'version': [
                -9890852903842284,
                274303629691791636,
                897624813119763548,
            ],

        },
    ),
]


class ArgumentsTest(unittest.TestCase):
    """
    Tests for Arguments
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ARGUMENTS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_commands.Arguments.parse_data(test_data)
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
        for test_name, test_data in ARGUMENTS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_commands.Arguments.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ARGUMENTS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [


]


ARGUMENTS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    (
        'string',
        {
            '^': 'string',
            '$': 'ʫΝǸφиŵʷэƬˏʅèRϋÄσ˶ːǯĎŶ¼ҫˏîľƀыԦѕ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -3934785988125258950,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 77931.76404607086,
        },
    ),
]


class ErrorTest(unittest.TestCase):
    """
    Tests for Error
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ERROR_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_commands.Error.parse_data(test_data)
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
        for test_name, test_data in ERROR_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_commands.Error.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ERROR_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='Error'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='message', name='Error'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='arguments', name='Error'),
            ),

        ),
    ),

]


ERROR_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'identifier': 'ˡŀαӣͳȽǹҤ±ӏюѭԀ¢Ҟ\x9cǎƦˑϠĎĶћ˃ΑÜŦЊĨǋ',
            'source': "¡Ψûĭ?¼ĆȲƦϹѮӾōϓɜ'ԐXˀʡ\x9bуЀǥŐЋҞҴèő",
            'message': 'РǆǂӚȘӞ8È\xa0ŀԊǂ',
            'arguments': [
                {
                    '^': 'int',
                    '$': -1523059265658080928,
                },
                {
                    '^': 'float',
                    '$': 860275.1213698324,
                },
                {
                    '^': 'string',
                    '$': 'ˉȫ\x90ŠϗĒŐ\x83åѺяȗˍӔɭѰ҆ĲђɒЩ½ëξCϣÜ',
                },
                {
                    '^': 'string',
                    '$': 'đԀʩˀжлÁƸҕ',
                },
                {
                    '^': 'int',
                    '$': 6146805326921402486,
                },
                {
                    '^': 'int',
                    '$': -6337447883506796619,
                },
                {
                    '^': 'int',
                    '$': 709001188447194605,
                },
                {
                    '^': 'float',
                    '$': 879279.0292388418,
                },
                {
                    '^': 'int',
                    '$': -5265700809393927922,
                },
                {
                    '^': 'float',
                    '$': 882035.1512986738,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ƅх',

            'message': '',

            'arguments': [
            ],

        },
    ),
]


class InternalLoadExtensionFailedEventTest(unittest.TestCase):
    """
    Tests for InternalLoadExtensionFailedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in INTERNAL_LOAD_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_commands.InternalLoadExtensionFailedEvent.parse_data(test_data)
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
        for test_name, test_data in INTERNAL_LOAD_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_commands.InternalLoadExtensionFailedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


INTERNAL_LOAD_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='InternalLoadExtensionFailedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='InternalLoadExtensionFailedEvent'),
            ),

        ),
    ),

]


INTERNAL_LOAD_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'υǍϘ@ϟАȡE±ɩØʮÜŎņǽͱ1γRӣˬıΈѰђӬѣßʏ',
            'error': {
                'identifier': 'ЯHǴĚҍӡʶ˵Ŭ˲Н\u0383ҝŲˈØȅǖ˅ԍӧĮËǈғаÁѡðτ',
                'source': 'ӓƥЙ\x82ҴÎѸßˇЏ\x8aʐɌϕȏVӈӗӯ΄yƭÚʑʄ6оɍ\x87ʇ',
                'message': 'ō',
                'arguments': [
                    {
                            '^': 'string',
                            '$': 'ĺ\x8bʒԛΑɕ+ҫȎÓʸԐ͵ƢĞńʲ\u03a2ŃɵγΦǡƭҴȽҲ´Ϲđ',
                        },
                    {
                            '^': 'int',
                            '$': -3898661815678940508,
                        },
                    {
                            '^': 'float',
                            '$': 665247.5960571573,
                        },
                    {
                            '^': 'int',
                            '$': 4507562236503627181,
                        },
                    {
                            '^': 'int',
                            '$': 7407533774478646895,
                        },
                    {
                            '^': 'float',
                            '$': 103785.3686792774,
                        },
                    {
                            '^': 'string',
                            '$': 'Ȁ\u038bĽțţɺĬʕäˣÑҡιȀΗƳҝĳˢɍӥĒӠ0ώӼŉˇϷЩ',
                        },
                    {
                            '^': 'float',
                            '$': 354034.66481980286,
                        },
                    {
                            '^': 'int',
                            '$': -7593554730319371991,
                        },
                    {
                            '^': 'float',
                            '$': -46752.35232171636,
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'error': {
                'identifier': 'ǡù',
                'message': '',
                'arguments': [
                ],
            },

        },
    ),
]


class InternalLoadExtensionSuccessEventTest(unittest.TestCase):
    """
    Tests for InternalLoadExtensionSuccessEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in INTERNAL_LOAD_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_commands.InternalLoadExtensionSuccessEvent.parse_data(test_data)
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
        for test_name, test_data in INTERNAL_LOAD_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_commands.InternalLoadExtensionSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


INTERNAL_LOAD_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='InternalLoadExtensionSuccessEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='InternalLoadExtensionSuccessEvent'),
            ),

        ),
    ),

]


INTERNAL_LOAD_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'úӂƅÄϹUƞ-ӋȒŉЛϝύȍӘĥēıԠΒӎɽΧϧrɬτƈ˸',
            'version': [
                -6401909756506181151,
                7735542812717158882,
                1542745283374339258,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'version': [
                -4161671410595026905,
                7036297239267835056,
                -5198887316741281454,
            ],

        },
    ),
]
