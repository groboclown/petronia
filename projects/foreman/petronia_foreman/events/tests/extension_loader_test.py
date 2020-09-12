# GENERATED CODE - DO NOT MODIFY
# Created on 2020-09-12T00:48:26.792253

"""
Tests for the extension_loader module.
Extension petronia.core.api.extension_loader, Version 1.0.0
"""

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n
from .. import extension_loader


class LoadExtensionRequestEventTest(unittest.TestCase):
    """
    Tests for LoadExtensionRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOAD_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionRequestEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in LOAD_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOAD_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LoadExtensionRequestEvent'),
            ),

        ),
    ),
]


LOAD_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'Ӷ˴ņɜʫ¯ˢѿνŸʩŘКËҖÕ\x93;đϖ˱ӊͰГʫϝʑýӋ?',
            'minimum_version': [
                -4360023373582889631,
                1033547379438331765,
                4442786774468180680,
            ]
,
            'below_version': [
                -5766234162945031026,
                -3652676443151285860,
                -4137610258528317693,
            ]
,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

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
                res = extension_loader.Arguments.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in ARGUMENTS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.Arguments.parse_data(test_data)
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
            '$': '¯FÒΏǒ˱ѩΔěΆó\x95ԎŶˈǿѠvчԫЅʼϨЂƙȉΝʂѬЖ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -3893270166257178998,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 505460.2531319421,
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
                res = extension_loader.Error.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in ERROR_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.Error.parse_data(test_data)
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
            'identifier': 'ĕȤůU\x9dΏ!HɵÄļʗŦqÆйͽƝҞȜʛɏƲʬєʅUǁͳå',
            'source': 'ÎɔAɓįεѝ˭~Ǐ°ł˅ѝƴˬӀˁŝ³±ЅΕЊĻʙЍ\\Αʷ',
            'message': 'ƅЎAνӵȧ]ɐΏȨҧ½Ҩ΅ĒԥŘԕʈȍʁϧϕΫˏʬ˚έ,C',
            'arguments': [
                {
                    '^': 'float',
                    '$': 476928.40312283125,
                }
            ,
                {
                    '^': 'string',
                    '$': 'ΜδчȪӗϖɼÕÞрƊĦϧ¾ѯZÏҶÂEԆͱĦԜŨȰЊӇϽš',
                }
            ,
                {
                    '^': 'string',
                    '$': '=ӴŔȱƧʥ ΟƱPӍԀƋЫțͺ˩Ȧ©ΆҫЇЮ:ǲʋðŀ¥Ҹ',
                }
            ,
                {
                    '^': 'string',
                    '$': 'ҏҏƕˆ\x9aÿ˞ˉQ',
                }
            ,
                {
                    '^': 'float',
                    '$': 666548.8150825296,
                }
            ,
                {
                    '^': 'int',
                    '$': -7501803884953572861,
                }
            ,
                {
                    '^': 'float',
                    '$': -45039.198462648324,
                }
            ,
                {
                    '^': 'string',
                    '$': '˳˂ŀɕvʲ˟ĖӽӞ˴ԥʨƯɊѴ\x80ԠқЍ-\u0379ϘҺʺƚҜ˳Ϧǜ',
                }
            ,
                {
                    '^': 'string',
                    '$': 'ȧŀiÝöӋ¥ǺƱІӕ/˺ŬӔƢ?\x89XQ»ѐɆԠņɓÞǨ\x86Ԑ',
                }
            ,
                {
                    '^': 'string',
                    '$': ';Кҹ\x83ϭŀƚͳͳӒēѤǡВÓƔ˛ҟȲΟ˃ӭкƴy˶щȢüų',
                }
            ,
            ]
,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ԐŶ',

            'message': '',

            'arguments': [
            ]
,

        },
    ),
]


class LoadExtensionFailedEventTest(unittest.TestCase):
    """
    Tests for LoadExtensionFailedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOAD_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionFailedEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in LOAD_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionFailedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOAD_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LoadExtensionFailedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='LoadExtensionFailedEvent'),
            ),

        ),
    ),
]


LOAD_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ĦƯ\x85ǲɊӞÇȣǗƺӭɢǓ\x92ԟŨ\x8eϜëӉŢʺӶɪξԐ8ѻƂÃ',
            'error': {
                'identifier': 'Ά¡џϺđǣҁǂŭΗŹʁ˯ԩΧ\x8fȍċϣԪӤƆÐğĢԟ×\x8bʵΖ',
                'source': 'ôƕİŃ9Ņӳƹɩƻ;ńļӋQӆǇǳȺ>ΡÖӘǍȾ4Yȿʹу',
                'message': 'Ƣюϯ¾íjʭɠWѕԤĝǇɺԟәϓˌхŵ1ϷRwFЕϗÞ\x94Ω',
                'arguments': [
                    {
                            '^': 'int',
                            '$': -749564859744196047,
                        }
                ,
                    {
                            '^': 'int',
                            '$': -3913830451489875360,
                        }
                ,
                    {
                            '^': 'string',
                            '$': 'ΩâӠӻЇǡξyΚȦҏТЛŠȤэϧҡέˋҵ΄ß>МΒ\x93\u0383ʶӸ',
                        }
                ,
                    {
                            '^': 'string',
                            '$': 'ŭ˄ЭǘҮˠԞ2ʭҥԛȈεĀķϡӬɒƂ҉lǕʛ©јϵ\u0378ԇØș',
                        }
                ,
                    {
                            '^': 'float',
                            '$': 248673.65662097355,
                        }
                ,
                    {
                            '^': 'float',
                            '$': 831226.1943663137,
                        }
                ,
                    {
                            '^': 'int',
                            '$': 407408548735676289,
                        }
                ,
                    {
                            '^': 'int',
                            '$': 1973797822714269011,
                        }
                ,
                    {
                            '^': 'string',
                            '$': 'ǓyѢƥʯӘРӗƯҠȗЦȣϐĢ˒ȿɧíтӍć˜˅˃άˤŇҽΕ',
                        }
                ,
                    {
                            '^': 'string',
                            '$': 'ɋԟƑΕÎƞЗŴʵˆѶöƪґԪѐЏҸƪҞɮӯ:ҾǫҳŭȌͰƧ',
                        }
                ,
                ]
            ,
            }
,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'error': {
                'identifier': 'Ӱѩ',
                'message': '',
                'arguments': [
                ]
            ,
            }
,

        },
    ),
]


class LoadExtensionSuccessEventTest(unittest.TestCase):
    """
    Tests for LoadExtensionSuccessEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOAD_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in LOAD_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOAD_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LoadExtensionSuccessEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='LoadExtensionSuccessEvent'),
            ),

        ),
    ),
]


LOAD_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ӕļŕѯȒҨʘĲ˭ІȇèЬԧҝѩǝʆ2AȐCҐϯɿįƁ_ńĜ',
            'version': [
                9159544360547727303,
                4706394943715670626,
                -2207790503921499075,
            ]
,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'version': [
                7889452569038934681,
                -3968203277909246431,
                -6045972214720431613,
            ]
,

        },
    ),
]


class LauncherLoadExtensionEventTest(unittest.TestCase):
    """
    Tests for LauncherLoadExtensionEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LAUNCHER_LOAD_EXTENSION_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LauncherLoadExtensionEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in LAUNCHER_LOAD_EXTENSION_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LauncherLoadExtensionEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LAUNCHER_LOAD_EXTENSION_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LauncherLoadExtensionEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='LauncherLoadExtensionEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='location', name='LauncherLoadExtensionEvent'),
            ),

        ),
    ),
]


LAUNCHER_LOAD_EXTENSION_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ӥҫȖǬǉΖʘӣ2ЮǞȉÏзˤɩΓԨô@ÅaҲAϯФņ½ϛ²',
            'version': [
                4685711411218915491,
                1206114826023772405,
                9086077766017284427,
            ]
,
            'location': 'ƞԒӮͺĹϪŹԘ¸Ѯ˴;ȡԎЊʱ\u0382ĹїÖ˷ŀżЇőΫÊσҺȬ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '',

            'version': [
                -6568451061909471174,
                -5508021563565742727,
                -7150071704611164460,
            ]
,

            'location': '',

        },
    ),
]
