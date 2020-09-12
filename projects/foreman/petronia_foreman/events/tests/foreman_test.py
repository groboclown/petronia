# GENERATED CODE - DO NOT MODIFY
# Created on 2020-09-12T00:48:26.876580

"""
Tests for the foreman module.
Extension petronia.core.api.foreman, Version 1.0.0
"""

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n
from .. import foreman


class StartLauncherStartedEventTest(unittest.TestCase):
    """
    Tests for StartLauncherStartedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in START_LAUNCHER_STARTED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncherStartedEvent.parse_data(test_data)
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
        for test_name, test_data in START_LAUNCHER_STARTED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncherStartedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


START_LAUNCHER_STARTED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='StartLauncherStartedEvent'),
            ),

        ),
    ),
]


START_LAUNCHER_STARTED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'identifier': 'Ԣϭ\x82ЎƦ΄ųҴƓӳпʆ҅іЖ˩қƻЙѡĪϲѶԕӱāтȃˤΞ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'pʂ(',

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
                res = foreman.Arguments.parse_data(test_data)
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
                res = foreman.Arguments.parse_data(test_data)
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
            '$': 'ǴjʸÛőʉ˅\u0380ʄOдП\u03a2ҌȬǅΠΒ҆ǵĐ{ϱȆҗ\x92ƛʣΐϤ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -4013633526741164055,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 411136.7764225202,
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
                res = foreman.Error.parse_data(test_data)
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
                res = foreman.Error.parse_data(test_data)
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
            'identifier': 'ƔĒ\u038bƊȺ˵лѝζsǵŜӟȷЋėǣȆ',
            'source': 'ŻfЀƓɉÑʏɫʒȬƐУϢȽƋαǅ\x91ȄӮԟïѧ´ɟϩӀύǺȹ',
            'message': "ѱ ӳǾǛƬĮϹʯΎŚӃҎǓѕƫԏɋ'ҥшpŀȣϡΕ¨¹Ǻʡ",
            'arguments': [
                {
                    '^': 'int',
                    '$': 553995510409484413,
                }
            ,
                {
                    '^': 'int',
                    '$': -512990035585230890,
                }
            ,
                {
                    '^': 'string',
                    '$': 'ïǖѯÕҺϣΎͱӣϱȷʥóĨȏ×>µƱ˦Ɖó˳Ķ˦ŭŻΛʕҰ',
                }
            ,
                {
                    '^': 'string',
                    '$': "ώ˰Рďɿ<o˼'É҅ɄƨŤ\x96ņӈϨĹэ]ģϾɀǕ¼.`Ϊͳ",
                }
            ,
                {
                    '^': 'string',
                    '$': '\x88ĵɷџɝѦͶɅQˡҎçøŁѼȽλɏЗЛ͵ſšȞ˅ɜцʶϒǑ',
                }
            ,
                {
                    '^': 'int',
                    '$': -4789444646417768851,
                }
            ,
                {
                    '^': 'int',
                    '$': 4064366934951204000,
                }
            ,
                {
                    '^': 'string',
                    '$': 'ΞгҥĖњɱѲԏȒӌAĠэԍҶşʃј\u0381rӷ\x92ȬˀͲјɲʎƜS',
                }
            ,
                {
                    '^': 'string',
                    '$': 'Ğģθ˅\xad҇ɒ˚Ñԣŀϣ˳C#Оҳ˥ñ¾Н\u0379ư\x80ʓŶӚҋrɰ',
                }
            ,
                {
                    '^': 'float',
                    '$': 983110.1374687601,
                }
            ,
            ]
,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ƢΕ',

            'message': '',

            'arguments': [
            ]
,

        },
    ),
]


class StartLauncherFailedEventTest(unittest.TestCase):
    """
    Tests for StartLauncherFailedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in START_LAUNCHER_FAILED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncherFailedEvent.parse_data(test_data)
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
        for test_name, test_data in START_LAUNCHER_FAILED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncherFailedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


START_LAUNCHER_FAILED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='StartLauncherFailedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='StartLauncherFailedEvent'),
            ),

        ),
    ),
]


START_LAUNCHER_FAILED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'identifier': 'ґŤԖΪѧŀӈÇƻҤģ°¿ˀϔɗ/ώŋƇńOʾ·ʓӇáԖԤӸ',
            'error': {
                'identifier': 'hȅЍ@ːЂcuʁ`јΟ\x93ԖʹȣƍɾӎǅĨ\u0378ɵǯÔҖƧҁŹǽ',
                'source': 'ѕǄȽñ˻ѲOҶŘК²ԒuŏμqЯƎ˹ſ\x93ұ҉ʥCғŦ\x81ˁɸ',
                'message': '\u0380бѻыjSʁʏ\x93юģɊ˞Άԥζʞʭ˼ěζҲʌȈɂѾƶ\x8eĿԍ',
                'arguments': [
                    {
                            '^': 'float',
                            '$': 988961.83247281,
                        }
                ,
                    {
                            '^': 'string',
                            '$': 'ίӾυԤʲ\u0379ʄPºʼѯЦŮùŻļђѹΤϣҏɱƋӳĹϦѽǖңŶ',
                        }
                ,
                    {
                            '^': 'string',
                            '$': 'GҴЁʚɍΙǶυϻ\u038dƧŮȗ˽ĠqҏѸϣ\xadͿВυȡԇ\x8aӠͱзɐ',
                        }
                ,
                    {
                            '^': 'float',
                            '$': 696758.7360558043,
                        }
                ,
                    {
                            '^': 'int',
                            '$': 8078009312230612889,
                        }
                ,
                    {
                            '^': 'string',
                            '$': '˒çƒʬЕǝʊɇϺƃԐú҂ҕҌīȵȖҩы;ȚĽӀπɋƓĳǢǲ',
                        }
                ,
                    {
                            '^': 'string',
                            '$': "ďȕԨĭђɢȃ\u0380ҖͶĜʘ'ɑǵЦȕàÝԉӘƘԝǳʗƋӞŐѶŬ",
                        }
                ,
                    {
                            '^': 'string',
                            '$': 'ӹԡҊ͵ʂȏƘȿXɎԧӭЁҳɱʠȹ˻кҚзӖ\x95Қҏʯ.Ɲыҹ',
                        }
                ,
                    {
                            '^': 'int',
                            '$': -4448778829915806600,
                        }
                ,
                    {
                            '^': 'int',
                            '$': -4221209443019937202,
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

            'identifier': '',

            'error': {
                'identifier': 'юǨ',
                'message': '',
                'arguments': [
                ]
            ,
            }
,

        },
    ),
]
