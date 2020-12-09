# GENERATED CODE - DO NOT MODIFY
# Created on 2020-12-09T16:48:34.351237

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
            'name': 'CϠĊɲȧ}ƘƥҐ΅κʿǜεɨӣΨ˰żѢӷÂqʤЩΈҐˁΰϺ',
            'version': [
                -1547678704677543636,
                -6059403810384912251,
                7038513709525959070,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'version': [
                -1830538676653236472,
                4070698145491815085,
                -5081615011842654051,
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
            '$': '!ԥü«)ŰƇå˄u˜ǅςӯЧҶқƆǺȔǯϬʨԕҍƈʣӄśź',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -7231496112483454738,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 279437.23614555784,
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
            'identifier': 'έИȥÓ5ʪΧҾǱĳƽȸϰςMʚжŗԐь\u0380ȦɿåͰUǏ"',
            'source': '#ҕϖϜȷѵǊЉӷĠϩ˙œƌˎƖʨʣϸÍɍʃӹΠyʪˬӼˣɓ',
            'message': 'ʀ',
            'arguments': [
                {
                    '^': 'int',
                    '$': -1378500780716315259,
                },
                {
                    '^': 'int',
                    '$': 6120054104441134655,
                },
                {
                    '^': 'float',
                    '$': 714962.1963244844,
                },
                {
                    '^': 'int',
                    '$': 2713009596034014013,
                },
                {
                    '^': 'string',
                    '$': 'ЪëƬɧ±ήӖΰ˰ӋAӔѤɉ\u038bȅт³ҟǼΪΊƆřй\x7fɣˠԜ\u0382',
                },
                {
                    '^': 'int',
                    '$': -7039747232408124860,
                },
                {
                    '^': 'int',
                    '$': -1320997273877512163,
                },
                {
                    '^': 'float',
                    '$': 558883.3165222898,
                },
                {
                    '^': 'int',
                    '$': 8626089165590055021,
                },
                {
                    '^': 'float',
                    '$': 543595.1234326789,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': '¸ң',

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
            'name': "ӣҝ'ʑǛчԓԢɍΘˌ˵²дέжƧ7ŲМϚΆ\x85˞ʖ¡ҴʙǥѾ",
            'error': {
                'identifier': 'ŷŏʭĖрGɒДößǩʩҰǕ\x93UȁԋĠϝқ\x81\x94ʈ¨aѳѫƾƠ',
                'source': 'ӋǄȧρȚɋԓʼλԒ',
                'message': '˜ӄƺΎêҲУęϹԗǒŪҗĀΝϰϮ$hɲʏÝǴ˳ƣϽÌ϶\x9c˝',
                'arguments': [
                    {
                            '^': 'string',
                            '$': 'ӷĆȪÏš˂!Ӯϋ©ӵ\x87Üñśiʤѭ´δѣҝƅ¿ϣ˥ҖêÊʀ',
                        },
                    {
                            '^': 'float',
                            '$': 94793.5726478956,
                        },
                    {
                            '^': 'string',
                            '$': 'ƧŊѱÌêˆЈ\u038dˀņә\x97ЙġɊ»°ŚʐӲӁӔǔƨʽζɿɜώγ',
                        },
                    {
                            '^': 'string',
                            '$': 'ȅĂʈɷȒ\x81ÜϺʙǮȚ¾ϭǐĺґŖʍÅΫÔǏ\x91ʅѕʞжɻЂϑ',
                        },
                    {
                            '^': 'int',
                            '$': 7722776559076386274,
                        },
                    {
                            '^': 'float',
                            '$': 854706.1977929808,
                        },
                    {
                            '^': 'string',
                            '$': 'ԐĳƈʙŢϐѡʨ÷ԗĴĈѓCǔ˦ҐѼĠӤʿЧΰ˙å\x9c1ʋǐɦ',
                        },
                    {
                            '^': 'int',
                            '$': -5453005965396985524,
                        },
                    {
                            '^': 'int',
                            '$': -7652937309229147629,
                        },
                    {
                            '^': 'int',
                            '$': 7184445393395813553,
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
                'identifier': 'ƨԫ',
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
            'name': 'гÑŹƳЅɎңǩ#ǱʺǄџӥҺӜӎȯεԮфπЍўиѰțЫ϶ѣ',
            'version': [
                2185839783490568260,
                -2478404773937612567,
                -2486479501063143095,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'version': [
                2774353745970532701,
                -2072639386327653867,
                -1105949364786168277,
            ],

        },
    ),
]
