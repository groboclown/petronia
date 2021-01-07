# GENERATED CODE - DO NOT MODIFY
# Created on 2021-01-06T22:34:11.874522

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
            'name': 'Ƹ\x89ǥŮǀ˗ʀѣˑ˹įˣӴļ"˷ȐƬГSν®\x98ǍƊϧϛ@Ϭ˂',
            'version': [
                8018821894621825810,
                -6710700099905994474,
                -2222516726524812804,
            ],
            'configuration': 'ńǒο¯ӗȽ{ÒԔϤĀiԢӳЉэρ¡ɷǎǹ^СǞňƁΘʢRԅ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'version': [
                -5101280693351625029,
                979305257215600226,
                -1410558039497985087,
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
            '$': 'ЈɎζӤɟˍĂ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 1567446284116520850,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 977757.7954746413,
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
            'identifier': 'ʌκӘĘ\x84ɓΘϒÌ\x8aдδĦǘǮʳʆƦĉȲʚţęŚϠŨ˃ɿϘҤ',
            'source': 'ȟɴbϦҨǼΏd˕űťJѢɸԃʛȮԢԪeİϫғːñǖЀƈТι',
            'message': 'ƌԤƣʢӿΝΠȌӴԦ\x94ƨΥɾ˖ϏȾȗņǫƒl˨œ[ȧśЉiϕ',
            'arguments': [
                {
                    '^': 'string',
                    '$': 'Gӑϥη\x88ʯɔĬь°ЊӭÀЈĝȦïЬŠʷЕ˔ǯʅͱ˅Ԋȩ˴˩',
                },
                {
                    '^': 'float',
                    '$': 493237.95150016865,
                },
                {
                    '^': 'int',
                    '$': -4091778641683636554,
                },
                {
                    '^': 'float',
                    '$': 85330.61789166852,
                },
                {
                    '^': 'string',
                    '$': ']¡ƓӎĽńѝ¡ȝԤȚΉƥȒ\x93ÑҖŵŵВƜͻǀÕʫ˰JŃȷϱ',
                },
                {
                    '^': 'int',
                    '$': -8261920892881076769,
                },
                {
                    '^': 'string',
                    '$': 'ɼͷђуĩȜϠƄҧΗĦɽÆȎ˩ϮŴʸʥι˰ϤŪӀŔ´ћoΪ<',
                },
                {
                    '^': 'int',
                    '$': 3829620567941786335,
                },
                {
                    '^': 'string',
                    '$': 'ɳūŰɋԂÉ\x88ȶȋūƚŲwĈùАϿhEØŶѮɶҚѱŵȤŹҤD',
                },
                {
                    '^': 'string',
                    '$': 'ǂı\x9aĝϳǻ\x96sɵǪʽ=Ҿ¨ȝē˾ːψğӇAq\x93ʪA˴·Γ˅',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': '{ɂ',

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
            'name': 'Ӿјө«ЗȴѸbiƌƘƪʬěȟƾΐΟӃ\u03a2ǽӑgŝơϷëʺȵƨ',
            'error': {
                'identifier': 'Ï˰ÌѫǮrªХ\u0382ȻtЏN҅ÇĴ÷˔ԩɱǐ\x96ĖЏƂѿƭяйɤ',
                'source': 'ӗɡōƥùчвęÁóѓƠгԑƔӗȁΪţ˩˄pʷĹѱVƝ˧\u0380B',
                'message': 'ɯũͽäȬtЌŹŖȰÚěȾ\x93ȗȼƋ˙\x9cIƞ¬žăɝӶŭ\x98žÕ',
                'arguments': [
                    {
                            '^': 'int',
                            '$': -2708341223201293328,
                        },
                    {
                            '^': 'int',
                            '$': -1036223426466156378,
                        },
                    {
                            '^': 'string',
                            '$': 'ɪяБfȏʋǁĭԌbčȍǦџiǐΎʗ\x88ūÇӢ½žǅҰƅУǹО',
                        },
                    {
                            '^': 'float',
                            '$': 471030.0154960223,
                        },
                    {
                            '^': 'float',
                            '$': 261572.41578085476,
                        },
                    {
                            '^': 'int',
                            '$': 8105563550088467111,
                        },
                    {
                            '^': 'int',
                            '$': -8557896234259823383,
                        },
                    {
                            '^': 'float',
                            '$': 7693.748038352976,
                        },
                    {
                            '^': 'string',
                            '$': 'ʕѾ\x83ǱғԦǫԢƿƚԋqдʤŽю\u038b¡˱ӴǡȐ˺ӠɯʋЄϋƁн',
                        },
                    {
                            '^': 'string',
                            '$': 'ӝÁˊNēϪƥԥɚĠŐşʂӺƔʎ¦ʵҿʣԘƂÝєԨҴӹɚ|ɽ',
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
                'identifier': 'ԫɐ',
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
            'name': 'ϱ˰ϑЭıƆΊӮ&ǒʟɱ%\x83ЋǩѿΞʔĵŔǲϾʿƙӨhλӱŅ',
            'version': [
                6429080362264810064,
                3362455976477999060,
                -2565313541366122533,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'version': [
                -4853801517052146876,
                6518825725971702484,
                -1309740175943164732,
            ],

        },
    ),
]
