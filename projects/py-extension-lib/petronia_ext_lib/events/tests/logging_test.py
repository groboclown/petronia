# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-12T16:51:00.400522+00:00

"""
Tests for the logging module.
Extension petronia.core.protocol.logging, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import logging

class MessageArgumentValueTest(unittest.TestCase):
    """
    Tests for MessageArgumentValue
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MESSAGE_ARGUMENT_VALUE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.MessageArgumentValue.parse_data(test_data)
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
        for test_name, test_data in MESSAGE_ARGUMENT_VALUE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.MessageArgumentValue.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


MESSAGE_ARGUMENT_VALUE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [


]


MESSAGE_ARGUMENT_VALUE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    (
        'string',
        {
            '^': 'string',
            '$': 'ѸЦԅЏϡɯʨɒԕÇǏ͵ƍǬѹϴŘȎ\x9cͺXʓǑϸÃ¯Ӯϗď˗',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 2439031559603752175,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': -30345.94935793616,
        },
    ),

    (
        'bool',
        {
            '^': 'bool',
            '$': True,
        },
    ),

    (
        'datetime',
        {
            '^': 'datetime',
            '$': '20210212:165100.293235:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                '˻ΘĽԤŦƑœǼȑ\u0383ҭŻӊКĹÔŝȴɈҚ\xa0\x99ОѿǓӇ:оҙŔ',
                '\x8eхĦГПĳеѽʼ\x83ĢûҷȞЩ͵ϡōҾΩźԑĢϸɁϗӸ)Ϩȱ',
                'ϱŦȩ ʰȜԬцӆʔȞʭϜʀнҞҫňɬŦēЉİќŻɍӬɍˋɊ',
                'ǾƽbϴǯȭӑҟųɲǼͻɨѢӻoű:Ѧņ£őĪНѽfȼρŵ\x85',
                'ȘЂŪҗțҵ˂¥iϿǇҗАҽƩ·ŒȅġʑƯҩķJô&ҒŪįˊ',
                'ſȟȷ5зɤɦɰǋ\x8aġϩӢԑŇȔɘΐӸѯɓƏʼ\x93ϴͽ)ǔ\x99º',
                'ÕÚϋХ)јҭîӶ˧ʀҖċфхǾdѳϷѨύěʹƏďϚωǜB4',
                'ѪҗÆµ\x9f˸ЦǰӔǉɱ\x8eѨʶͶȄiУɼıɯĥҿѯҤӇʏΒɼþ',
                'ǮưτӀƙ.Ԧӏδвx:\x85ʚҋˈˊũřѼîӆŕ\x9e\u0383šǴʻħќ',
                'x˴ӻψĢɝӕǽИԞƈŶƧȱʊқБÌ\x80Í1ˢҹƏZǐҧѢɘʞ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -715094822339612768,
                -4888218585370211685,
                348159011746777221,
                5279485412771762274,
                -1545654168351229395,
                -4376047052237839138,
                -4563220332038798279,
                7297375675144549858,
                1778738678773365946,
                6378813273811989971,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                496298.3060561562,
                677543.3306584362,
                -78886.38804301346,
                525452.6954633384,
                965634.4141698726,
                381829.36131416593,
                221582.2256734055,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                False,
                False,
                True,
                False,
                False,
                False,
                False,
                True,
                True,
                True,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210212:165100.294030:+0000',
                '20210212:165100.294043:+0000',
                '20210212:165100.294050:+0000',
                '20210212:165100.294056:+0000',
            ],
        },
    ),
]

class MessageArgumentTest(unittest.TestCase):
    """
    Tests for MessageArgument
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MESSAGE_ARGUMENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.MessageArgument.parse_data(test_data)
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
        for test_name, test_data in MESSAGE_ARGUMENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.MessageArgument.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


MESSAGE_ARGUMENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='MessageArgument'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='value', name='MessageArgument'),
            ),

        ),
    ),

]


MESSAGE_ARGUMENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ǵɓҎˋǞӛˇųΧҍҐǜćʥýʑ˺ğҊˣȯǲfϘřǕWcˎϽ',
            'value': {
                '^': 'bool_list',
                '$': [
                    True,
                    True,
                    False,
                    True,
                    False,
                    False,
                    False,
                    True,
                    True,
                    True,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ơ',

            'value': {
                '^': 'datetime',
                '$': '20210212:165100.293012:+0000',
            },

        },
    ),
]

class LocalizableMessageTest(unittest.TestCase):
    """
    Tests for LocalizableMessage
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOCALIZABLE_MESSAGE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.LocalizableMessage.parse_data(test_data)
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
        for test_name, test_data in LOCALIZABLE_MESSAGE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.LocalizableMessage.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOCALIZABLE_MESSAGE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='catalog', name='LocalizableMessage'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='message', name='LocalizableMessage'),
            ),

        ),
    ),

]


LOCALIZABLE_MESSAGE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'catalog': 'ÚƱϑ®ά\u0379ŝ\u03a2Ϳʌ;=ƞӽɯԖѠǀǱûӶѿΟɏǂ҉ҍљЩƫ',
            'message': 'ƚǯϵҦӼĤĀϡþĹԤɶŪθгƀÿżъԐʔ\u0379ϠƢΪ1ǌέϛʰ',
            'arguments': [
                {
                    'name': 'ϥЭ^ӢΪQұʡҿǈЇȍşƮйƖėƘɰ˗ͺĉӾӫʑԏΘĳʲҶ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        False,
                                        False,
                                        False,
                                        True,
                                        False,
                                        False,
                                        True,
                                        False,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ĹΖʁ\x86Ŧ\xadǯŤʸĽŠl}!ĚQϥщӿɹWӎeĳô÷Ӂ;ɡǼ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210212:165100.291008:+0000',
                                        '20210212:165100.291025:+0000',
                                        '20210212:165100.291032:+0000',
                                        '20210212:165100.291038:+0000',
                                        '20210212:165100.291044:+0000',
                                        '20210212:165100.291050:+0000',
                                        '20210212:165100.291055:+0000',
                                        '20210212:165100.291061:+0000',
                                        '20210212:165100.291066:+0000',
                                        '20210212:165100.291072:+0000',
                                    ],
                        },
                },
                {
                    'name': 'öˇԫĔУ\x9aйԄ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ϝʙĿĀɮӺΝůϴ"li¬ɤфϘŕΆҪԈѴԉКԮЖԩǽҚΡΠ',
                    'value': {
                            '^': 'string',
                            '$': 'ʽȈːљ(әʰϢȵȫӋǡз˚Ζȉǡ¥\x92ɰәҮЗԤыЂҍΗԘЅ',
                        },
                },
                {
                    'name': 'ҕɥӱoШЅнѺã^fҠ˹ƒͽБҐǓƉԗȏπЃɖΣԭ˅Ŀþϰ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        3864.955700352948,
                                        948958.7509111017,
                                        324305.7905350823,
                                        375169.96313708206,
                                        470499.50657992414,
                                        921391.2988980195,
                                        572287.4203511655,
                                        -21838.78543248483,
                                        -8766.01722027133,
                                        532895.0127527094,
                                    ],
                        },
                },
                {
                    'name': 'lΈʫɀ2ĎčʆϨқŕÂƐɑɬȝυӴТʞ\x91\x9d',
                    'value': {
                            '^': 'float',
                            '$': 961660.5787975825,
                        },
                },
                {
                    'name': 'ɩŻѕ8ʕɹś<ǳ˓г˥Τҁбзï~ŔbЧ&Ɉ\x89³ϝ,˭ϕ\x85',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        81729.94276798062,
                                        115272.6559058491,
                                        -74909.69992117409,
                                        200763.512304727,
                                        604213.890249515,
                                        355802.17661502166,
                                        911276.9150143167,
                                        996467.3131515821,
                                        657313.635384842,
                                        312319.1026839825,
                                    ],
                        },
                },
                {
                    'name': 'ʱȌçӂŷ¹ǹΙ҈Ԓ',
                    'value': {
                            '^': 'float',
                            '$': -56350.35559166819,
                        },
                },
                {
                    'name': 'ϦʫɶСΩԏƌũɧзˀПǍ;фВӒѥɄƃѯź\x8d',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        296184.38459082105,
                                        635040.9423904376,
                                        709174.2240825708,
                                        4508.8220640047075,
                                        976795.740542558,
                                        865651.304457877,
                                        579230.5019777265,
                                        288581.3978940529,
                                        -40554.007763968606,
                                        329416.2738108158,
                                    ],
                        },
                },
                {
                    'name': 'ĉЃāǛɭԙԡ?ƛPԬΣĺeɓȰԙȫǐĎɆˊǂɪ¢úҞάĕɠ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210212:165100.292533:+0000',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ЫĢ',

            'message': 'Ĝ',

        },
    ),
]

class LogEventTest(unittest.TestCase):
    """
    Tests for LogEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOG_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.LogEvent.parse_data(test_data)
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
        for test_name, test_data in LOG_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.LogEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOG_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='scope', name='LogEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='messages', name='LogEvent'),
            ),

        ),
    ),

]


LOG_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'scope': 'warning',
            'messages': [
                {
                    'catalog': 'ɈʚѨѺӖ\x91ĴƯΰœІЍ\x8aǩ҆ßƂɼҽȑԏЗԉҝ{ЄųЌȡҘ',
                    'message': 'Ĳ˓ҮƂͱ\x98\x89ϻԁ\x81ǌԁЎӖγť˳§\x7fƭӘUɤmңˤɃЕğҮ',
                    'arguments': [
                            {
                                        'name': 'ҚШͱǅˮ!Ȣ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            866285.7370109593,
                                                                            -86547.74560256391,
                                                                            69878.79576897959,
                                                                            994869.2863973854,
                                                                            666435.0755842379,
                                                                            -4654.592795548,
                                                                            452043.5865785888,
                                                                            53774.69327039519,
                                                                            414834.82656370907,
                                                                            802962.8777652927,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'wŪÆʭzɲŐˉĭҳƬЁnѬɜԓш:\x8eɅШāǇʰʜɪ}ͽԝɊ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8602352847834856565,
                                                                            1583134289656978681,
                                                                            -8826450522600586976,
                                                                            8671387660528245539,
                                                                            8411905177303496296,
                                                                            -9149261458799165798,
                                                                            625587522272740642,
                                                                            9181986225325217206,
                                                                            1468624616642980731,
                                                                            873360206529566152,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӲΓƁΒХjɟϜȐӛҙ˂ҋȭԦǺκĤ\x8cɇÒЀŒ˒бҷγ˒ΟЇ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165100.264828:+0000',
                                                                            '20210212:165100.264865:+0000',
                                                                            '20210212:165100.264875:+0000',
                                                                            '20210212:165100.264882:+0000',
                                                                            '20210212:165100.264888:+0000',
                                                                            '20210212:165100.264894:+0000',
                                                                            '20210212:165100.264900:+0000',
                                                                            '20210212:165100.264906:+0000',
                                                                            '20210212:165100.264912:+0000',
                                                                            '20210212:165100.264918:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʄƸǬʤȈǖϧƓХƐŇϭĂ˪кɖҜ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165100.265158:+0000',
                                                                            '20210212:165100.265172:+0000',
                                                                            '20210212:165100.265179:+0000',
                                                                            '20210212:165100.265186:+0000',
                                                                            '20210212:165100.265192:+0000',
                                                                            '20210212:165100.265198:+0000',
                                                                            '20210212:165100.265204:+0000',
                                                                            '20210212:165100.265210:+0000',
                                                                            '20210212:165100.265216:+0000',
                                                                            '20210212:165100.265222:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'UĪ!ˬɬϑǘύɠP˖ĳ˥ԎţyˀċқÇxИĶΓѴ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165100.265463:+0000',
                                                                            '20210212:165100.265476:+0000',
                                                                            '20210212:165100.265483:+0000',
                                                                            '20210212:165100.265490:+0000',
                                                                            '20210212:165100.265496:+0000',
                                                                            '20210212:165100.265502:+0000',
                                                                            '20210212:165100.265507:+0000',
                                                                            '20210212:165100.265513:+0000',
                                                                            '20210212:165100.265519:+0000',
                                                                            '20210212:165100.265525:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8aϨ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7316329661474181567,
                                                    },
                                    },
                            {
                                        'name': 'ŜǳȤʪűɠĨћ#ÅƴКƢɸѿȠʈҺϋЖˎȫÍ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            984538.3673338862,
                                                                            174505.36542499793,
                                                                            745009.5536265954,
                                                                            527740.0381942402,
                                                                            937484.4992054856,
                                                                            91960.05371850033,
                                                                            -70175.16985885454,
                                                                            314553.24931447126,
                                                                            -603.8042644026573,
                                                                            504409.8962671282,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѢDѝԪɩѼĪȣӱʙ/ʷɫψƌȆƜʓ_ŀÖ0ĩάԪЂ\x8dɢŚӚ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165100.266212:+0000',
                                                    },
                                    },
                            {
                                        'name': '®ѣ҃ǮƮȾƋΕɡȍŃȨӒÑ˟іĿΕÚҥʋȾӺθΕйӥӽēʉ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7737805136644827789,
                                                    },
                                    },
                            {
                                        'name': 'ɰOͼƱЦ\x95ԟ)ttįpl\x8dɶТǦȠɬŁҍӫфԐӕnɩЛιɽ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165100.266512:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '2ӽѺҴ\x80ǄѮ·ǈD˟űϬȒKѿўʽňŕӒϹàϭȑx΄ҏāʄ',
                    'message': 'өӏȬ҇Ȃ\x99ԡԏҀĊźȽъͳʕɦȫ#Н˂ʕǊņҎКӛԝʦȌĲ',
                    'arguments': [
                            {
                                        'name': '©\x82ӤŖÍ@ϖПë˸éDҢԑƊ2ΎԭԧƸϖΊɃ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƔҙШғȂ҉ѧªƛԀȦξƬ-Ӓˉ\x9fŖǽĬƔǃӘΦʾgБ\x8e˙Ȫ',
                                                                            "G\x98ҬEÞ'ϕӠơ5EzҞԑŖϜkӝiǼӂŠļɊԏϩÚ6Ǵѯ",
                                                                            'ҫȣȆ\x8alӅ^wɕEıˇЖЋ\x88Ŏ,.ȵʮϸӽQѺțЕíŅӆЏ',
                                                                            'ĝөЅƎʋҗȆʔΣԮӲʳΖϟϵɢϢŤË6ѶĺЬŵäʨƲЫҲº',
                                                                            'ҩĒ?aҨ˖ԈЄ²ɹ˓ŧʮøɻȠЬʶåȭƅҗґүҖКÏ¸_ɿ',
                                                                            'ϓϸΩӠƻΕԊʮǵзȑmϺǁ³Ƒɯ*ÕͷԤƗЋţʦø΅Ҵȱѵ',
                                                                            'ЧȻȖŷvȾɳɧ5ΩӀÏ&AԇϒǸӤЉƎϰªðϵ\u038dƶҜʉǝʝ',
                                                                            "ZƲӣŔѵƂŭÈıЖǛɌyɞęʢʚȡǩǚī'ƨʟҐЪȄ\x93Ľ1",
                                                                            '±ʢņ°uÛƚӈӮǡϋӷĪ\x85ȶӒŔʳ!ӦřɠÁŭɔòȣæѕȜ',
                                                                            'ϼÈńʚȰjȝ8aϪĴ|ƘΛґÇŐϐѦźʟϥńϣ¿!ηӳ¤Э',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'șǖҷύϓȇͿRʧɥȣˍǺΧ;š',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ƶ¼ˀӈƻԨũ˃ǢҢƚӕŘ¬ȁωƂɢĎҏͼ0ɳEȑБͻ²ϪŃ',
                                                                            'ōΈĤňɥɊYƌƀΆѴ\x8bYУɄϕӠϜǞòɒǆ˔ßʌȒӥ˔Ю˲',
                                                                            'ʺxˢbƯҁԔɖΌ¼з³Ł˼Ŧ\x97ЙҋǎӲкѰƣʨɯɍӗsϙЊ',
                                                                            '϶ҧƳσ[ѯϑΨ\u0381ɡŷͺŰГлľЖ±ЇÄāȊϝͷƓԚØӁɻԊ',
                                                                            'әˍΤˬɿȤП£ͶƅȠϻƧяǘșҥȃɞзɄÀңУǯʛơʿˢĄ',
                                                                            'ƛ{ʁWκҘ˂ӖδvƓƓƊ˜ӴѣfûӰHɻϱpͽȳƍӁȁƌx',
                                                                            '¾ЙĐϧѫŞϚԮǕϿ˕nͻ\x83ӺƊƲģăϝǵӓǙȹȇɁπƢũІ',
                                                                            '¬sYɢΐ®гȸĳϲԁɟ)҃ǵRυȰč˽ƚϼѻǹüѪϛČ˹Θ',
                                                                            'ĮӣЙɸӹùȚƛȏȃʐϒӵʥǟ[ԗǾʶƐÓĢʱģЖӮȓҙɞų',
                                                                            'ͳёFȁȉӐ˽Ţм˵Ũȗ҂_ȌΝȮԫӃfΈӏŴѪʱʷ˕_Ɉϟ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Źˈ6ȐȚ¬ЋǛҗӛʁəԫŒŤеϠȐϪȰѕģ;ѦΊҒťУhÑ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ОŅϢàГ·ϭϑŞΦ2ĄӠлȐʇӕÕțēƮҋƉąƼϽș;ºĹ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165100.268049:+0000',
                                                                            '20210212:165100.268063:+0000',
                                                                            '20210212:165100.268070:+0000',
                                                                            '20210212:165100.268076:+0000',
                                                                            '20210212:165100.268081:+0000',
                                                                            '20210212:165100.268087:+0000',
                                                                            '20210212:165100.268093:+0000',
                                                                            '20210212:165100.268098:+0000',
                                                                            '20210212:165100.268104:+0000',
                                                                            '20210212:165100.268110:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÔїˬƼбж<ȣʫΦȉГˑˬɻԍ˥ҾɼʃʴєҊµνϊğΘ҅d',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8158177330832147487,
                                                                            -4618684033451355026,
                                                                            3813537249228356234,
                                                                            2732670572749754698,
                                                                            3952221533384224632,
                                                                            -6715932587141749683,
                                                                            2304803025157876715,
                                                                            -8417583986141991794,
                                                                            -6674654304356230203,
                                                                            9200502793540566113,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÊΏƎϖŴǣϠҾњ:ɑ˚ãɄÏūӨǂ6ɪ˛ȇ¬ʑKʏ˛ӑ$Ɉ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2872491607454948089,
                                                                            5245655537644331348,
                                                                            3997778862200928416,
                                                                            -3180394546344363453,
                                                                            3008041667659568631,
                                                                            -5878783948583509047,
                                                                            4066453920326920159,
                                                                            511118677243443222,
                                                                            -7410180058783985349,
                                                                            3624291441787558461,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȼ҃ɼӆƲЙ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            378420.75396095496,
                                                                            120519.30117818044,
                                                                            735876.6059277975,
                                                                            71148.27835856524,
                                                                            -35887.23196335627,
                                                                            713104.7552924764,
                                                                            818559.1095930449,
                                                                            -34558.657911547554,
                                                                            567345.3112780426,
                                                                            492602.39418895927,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƊτΕϲŁƥOŜц',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ŭ8ʟʨǺ\x88&ɢʙ#ҙ¾ĬɎҀŻț-ǂɔFÐ˂',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӗǍЌΊϗ\u03a2éЯƗʥϰƺŉęċѝLγ˴ҼӼξūʧÍ˨ˣŢŒѓ',
                                                    },
                                    },
                            {
                                        'name': 'ӜʧĩюκƇӎśɪЎȆ¥ěê&ǋȖȗҸʩĎwĽͺ1ʏɷÃʤȅ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            198583.36562511796,
                                                                            882970.9427800596,
                                                                            582329.6413544276,
                                                                            343573.74258570967,
                                                                            131888.52392847772,
                                                                            315925.2565244829,
                                                                            -24975.808378238507,
                                                                            163205.7486966817,
                                                                            306356.79933342314,
                                                                            425547.65403686685,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҼʻüƔΓҀƳҚàɧƹѤɳȾ\x8dȚ^ȁĊǨǾźӌҜӶȖыū˂ʧ',
                    'message': 'ΕΉқÑȨϤǽ\x95Ŋʆǭ˶ƶї҃ЯX©юЦN²\xadԍЌΝĀѺĎɄ',
                    'arguments': [
                            {
                                        'name': 'ÈΑ÷уԊӀɯʎϩĵԖđǕȢҘVӡȉӲŔǟˡƗʄƝŎοƺќˤ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8477593873874880395,
                                                    },
                                    },
                            {
                                        'name': 'ҥAë',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            614919891645310629,
                                                                            5597093834014977616,
                                                                            -5783313423904132518,
                                                                            -8615252697332409448,
                                                                            3713655882124634505,
                                                                            5284522963315470877,
                                                                            -3545833097374507504,
                                                                            -3916269979875763955,
                                                                            6508849074747704012,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƀʿUŜǶŁҭŒž',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 716227143149221965,
                                                    },
                                    },
                            {
                                        'name': 'ǉƵħĻÐǘʴƵΟСʜʄɍσαҊεӨ΄ȜŜѷЗѱ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            840309.8956902607,
                                                                            488949.0496220869,
                                                                            846028.5501195609,
                                                                            836932.2005160472,
                                                                            -4658.645632002706,
                                                                            931694.8722396292,
                                                                            73584.77940812297,
                                                                            993812.2187348176,
                                                                            771443.5131394269,
                                                                            210080.87868348998,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'θʝͷѷ1БіЎĖʧϻ˷оmōɢɶƖԫϭ%өӢ¤ɠƎЄryԡ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȓ҇ǉňǃɅҪůҟҤπς\x81ÉҰΈʽʭѿƿɞŀȑĞɁĠʹ˥Uƺ',
                                                                            'ŃȤЊLϷƅğˮDΈKБʎҸӋTͿϠдΪȴ^ˆś{ǙӀΡæ͵',
                                                                            '~ѤɳÃԠ\x98Æ\x98ΰӔƖŁΣ\u0378Ѡƍ\x91ǭΞʶǙơ^ɿЯɽΙ."ǯ',
                                                                            'Ⱦȿʧ}ɵ¸˜ЍƜ˘ȴίŜ«Fɴ©ǤˣǓ³ĮѭɅÃǾĸòʕɨ',
                                                                            'ÜȆѪфÙӠϣÕқǮҩɘ\x95χӟ˖ŃԖјˤϲЯƝˀƽȬǊдǶϙ',
                                                                            'ʻ\xa0Íҫ˜øеӜ˒ˊӀ\x8eǫνϐġÌʦ{BȕɂǙѵαǆɅkϬʩ',
                                                                            'ȭʳŜљ_ǭ1ǛЋɵȒӨȝɇԀ\u0381˪ǢњԞ˙ѱΤΐ҅Ƃӗęΐǡ',
                                                                            'ϔȚǐ RӆчΛҠƖ˽Ȥͷ)ȚԟʖӁЪÿmқϒʥYɠѕĂΞɂ',
                                                                            'źѲΰѮрѨяʬǌҢЖа҇ƥӨÞԓΑҒõʔqˎǜƠԌvӐ\x98O',
                                                                            'ΥŲɘĈ\u038bΜΜƒԝƵҔ\u0380.aħҒȔƁϞ.ǝ»\u0379ʋƟԙҼҍϟȵ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӗ\u0378ҫA7ɂҮι®\x89ЈȜýȠȗɭӳʏʌċĤƒƤϮӚӰƇτǆ¿',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƶ˳аŔ˩ĿȘȻüɖ ӹԍȹӆҘnɼƐҽΰѧҭˁԚҦÏɹɌϻ',
                                                    },
                                    },
                            {
                                        'name': '\x9dυӚΒЉĺcÛ˵ˡǝPϡĄ^Ǝ²',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            684077.6396047581,
                                                                            858429.6174895962,
                                                                            980735.647683467,
                                                                            74377.83478408787,
                                                                            377653.7373998211,
                                                                            695272.1815108097,
                                                                            713198.6299200571,
                                                                            662635.7983142457,
                                                                            135520.2830069507,
                                                                            856393.8622961652,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˷0żЬďЍoɫƀȪǱԬ.ɛ¹',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӶΖ΄ǳ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -9086514756917096308,
                                                                            854770016835890859,
                                                                            -8568793793409485295,
                                                                            -1201240687571361163,
                                                                            2723381194186159374,
                                                                            -7769634834294527473,
                                                                            -3070582857021611806,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'sδһӹè˽ͶϠ1ΨФϦ²ϙα÷ӈĔðȄòƓїˠԁĶŞӼҾш',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԖйʔĲ§ьȹӁйǲ}ȡмЬͻӚqФ˖ѡǦƶВѹғʪͳʀ҄D',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ħĨˁȸ{ӚʽѵΤȻɴЕǓʽҌѷɃǉƾļȒBψ˼\x88εȹӾ¾о',
                    'message': 'ҔӈЇӗǏɠǯĢCɍ˔ӿ4ӼcΆ ȯώƥ;ԮψŠҺǪŮІÅƁ',
                    'arguments': [
                            {
                                        'name': 'ȓːȨȨɄħè˸ÈʩԦωсҖɛnʁҪĹ\x82ÙƩɵʛʍ÷aù²υ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165100.272362:+0000',
                                                                            '20210212:165100.272376:+0000',
                                                                            '20210212:165100.272383:+0000',
                                                                            '20210212:165100.272389:+0000',
                                                                            '20210212:165100.272395:+0000',
                                                                            '20210212:165100.272401:+0000',
                                                                            '20210212:165100.272406:+0000',
                                                                            '20210212:165100.272412:+0000',
                                                                            '20210212:165100.272418:+0000',
                                                                            '20210212:165100.272423:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˂ƮɇͰʻìŐʄěΞSɨ0\x94јcӪӹϷ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2535153217114476257,
                                                    },
                                    },
                            {
                                        'name': 'ǞƸ+Ξ±ɥŵϪʿѳϲź4˩Ĭԡ¾ȸȳmĐȞĿѝӭЪǖǀÛԕ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '0ӁkĽȚƭ\x80Xҵɩʟ˺\x92ϑͿȩ`āǖоӠ˵ͲʚюџÒȫįȅ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɍӟHƅ{ʌѭΐԌʍʿb0ϒƷʨżӹƽ҈юͰȚԖŀҍ˒øPг',
                                                                            '<˼ϔűӇǊīùԊʣǨвϪԮсɓЎºӈǌ\u0378Ũ˘ȷ˞dϧϟӘą',
                                                                            'ÚɳƫͶхΑ҆мęIҳĚε˵ĭǉz#ҡȝÜ\x9fδ1ЗŅʱʹӕ;',
                                                                            'Ѝ[θҫԊΛȬ˒ЧŗΜӘˈ\x8aʯśΐŦҒÕѦϞɫƭ=ƗіϻǷư',
                                                                            '¤ǈțĀǊ˗ȁǙϛӁòõ\x87\x96ŗ"њӿЬӿҼ¤ѿ\x9eΡΎðƧΚƭ',
                                                                            'űŲɽÑι]ÌɁӾÂƫŧЃăө˱ƍЖƫίİā҇ϡɜ҇əϡʼӞ',
                                                                            'ĸӯņùη?Ȍԅ˾ĞH˰ČµЙΌēыЍҚȎì»ʈԥƎ/˷Ԍ\x8a',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӷϥƗмƗuњrƽ\x7fЇɶȟˇȩӲ\x95ͼʝ\u038dˇϥNɅѮƒåˤуУ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165100.273728:+0000',
                                                                            '20210212:165100.273747:+0000',
                                                                            '20210212:165100.273754:+0000',
                                                                            '20210212:165100.273760:+0000',
                                                                            '20210212:165100.273766:+0000',
                                                                            '20210212:165100.273772:+0000',
                                                                            '20210212:165100.273777:+0000',
                                                                            '20210212:165100.273783:+0000',
                                                                            '20210212:165100.273789:+0000',
                                                                            '20210212:165100.273795:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Έɸ\x9aɖàѡϺΫǫȄǨŦӄ2щǴ:Ԭ\u0380ɇɐȨɓӌѧ\u0379ʿśɄǤ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 365831.1620191696,
                                                    },
                                    },
                            {
                                        'name': 'ӽŇȷä',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "VУ'ˈȀыbǩ¢\x90ĺâ˘ԑџāЅĈџȹƽʛtӜɺӧτÙʝӎ",
                                                    },
                                    },
                            {
                                        'name': 'ǪыƴɽǮҤ\x83',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'кήΩŚʈȲњΣҲΞĈɻʻ¶έ˒ȎQԇ˻ˡňƍҹɪϾӗı\xadË',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԐĘOϝ\x9fāͱԡ1Oȍ˸ȮϟЊΟTҬϪμσìāȪˊͰǯèʕԁ',
                                                    },
                                    },
                            {
                                        'name': 'ăÂţȗÅҴңäϮħр\xadęǬ\x8bŏѪώźƓ,ұЖà˧Ӹ΅ƖώɊ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƨǃА)łŀ£5ӓΕĝ˟Ѻä{ӑɨˢǷˆţϊƾ˜ȧIȶҠ\x93ә',
                    'message': 'ѪͷɌǬ¶˙҉ʜmƳƁԋʐĹÞǘµьɐʚśρéǽΊӸżÖҲπ',
                    'arguments': [
                            {
                                        'name': 'Zė˸\u0382˺ɲѵƲίɓ˸Į˷ӵɶ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9062891273745691820,
                                                    },
                                    },
                            {
                                        'name': 'ЯSþӼȻѬ˽ǁʺ&ѯœɍӰӳĎԋͰӾʦХʃƷÂҏ$ԞӞʼ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165100.275217:+0000',
                                                                            '20210212:165100.275231:+0000',
                                                                            '20210212:165100.275238:+0000',
                                                                            '20210212:165100.275244:+0000',
                                                                            '20210212:165100.275250:+0000',
                                                                            '20210212:165100.275256:+0000',
                                                                            '20210212:165100.275262:+0000',
                                                                            '20210212:165100.275267:+0000',
                                                                            '20210212:165100.275273:+0000',
                                                                            '20210212:165100.275279:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0378ˇШȼ˰ŗ\x99mϺʇқʽɊǉÓΈqʻč\x89ȠƻϪĀ¨˞œϨƭɮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165100.275501:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӠLʞǮŕȎԘʼȅӒԏÓƒ6ҧŒ9Ⱥɋ©',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1017449799388637821,
                                                                            -2877135115989727422,
                                                                            -853777703289880189,
                                                                            2159374855190805223,
                                                                            1081571708457341148,
                                                                            992760289398782606,
                                                                            -5320675460631030672,
                                                                            7607250444386402453,
                                                                            -2900521370929477612,
                                                                            2376913875746081069,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '΅νΞԅ˽ǯӋ½Ӆ¯ųÈӮїȈƞήԭɟȭɾ˯žҞ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 839296.5251833078,
                                                    },
                                    },
                            {
                                        'name': '\u0380ǑȂ΄ű¼JҌУЏŇԠϵ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\u0383āΜ®ѸǕғϜҚǒɶ$\xadǲȥȷͳў˄ǹȬÖǗÝĉЪ˟ήyȐ',
                                                                            '&ƲњϥшԚ˻¡˹я\x86ȴˊļƗЦĸGѷEȦͺѹļÜӘȹǢÌɖ',
                                                                            'ЎƠȨǅ}ΈԜĉͽζǎ\u0378ғӏ»҅ҟõľ¸łēūѲÐΉԈӬžø',
                                                                            'ʍ\x9eǫʳԠԧsÌБƔјƃƷƁʂȯШӭηͶ΄íÔŽͻԢĎưĔϹ',
                                                                            'ʂ˽ӞÌ\x98ſǐԘȉѽҧЖąģѦÀї\u0382ˁŜʳǀǲ,¤žʩǖ½ǳ',
                                                                            'ӝѧɤлϹЭƅёԭÿӶƼZSȇӱHhRӺôѤ\xa0ɒЛԟӀƖǢż',
                                                                            'ӲʎпИЮ\x85ϗҦ÷ӥұΪ˥m˷˥ԚҫͻҢƞȓøȿœуǓ¢ĈĖ',
                                                                            'Еɛʆσj\x94ËҸǄŜɭIǎϜȘŧԀǉԇǠ\x9bȁҡ·ɒɧљёʹǙ',
                                                                            'ǱϓеȯЧtÏӒВȒвǷŞžüiĲӃŶ\x9eǸљʉǏiхƷƍԠˀ',
                                                                            'ɾӴ7ӲɔşØϴsΣԟƼӌ¤ӌфТҾкЎ\x88ɿϬ˂ŎӍӌӛƖȩ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŦѠҺșÒϬϹҭ^˄ĔЄʟʊś¬ԮˮƔƫƱσɿϡɌ¼ŭy«ҝ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŤНѶ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʐƹ˰ȍë\x8aͺpԦ!ůҔαϪιŌв~ԐӌÌŜƩƻмЪrѪϓǻ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165100.276834:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӠѼ˜ӧũ¥йӝ¾\x99ɩΡъҙŋıΚʑϯ҇ʦϳϞƕʺµơєƎΣ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            829280.2144025828,
                                                                            892676.4027844454,
                                                                            955170.9463362042,
                                                                            880366.0337752919,
                                                                            934544.5904199453,
                                                                            103936.48973459989,
                                                                            65666.41083158835,
                                                                            -10797.951990600879,
                                                                            921797.7254421184,
                                                                            120340.62504577049,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǹԀһ҅ӱΑşǴЅȟɶоίȚŪĴŖɥĖ¥ůϧȎϳǤӊÝΙ=ɬ',
                    'message': '0ʽCͻʤϰƙc5ǆÂӨʍǯɳӘысɥĭƚʛsʐԎ˦ѻԭHб',
                    'arguments': [
                            {
                                        'name': 'ΖƟҹѵƂēǣʫƏŽʋŐҢ-ɍʼȿϰßӜѭÁοɣăɐȃʚѺ\x80',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Φԓǐȓ˅Ơǜ˾ȰԭōȾϜÅȟɅ@ǜуЦ!ӵԠéΝσùʭ×ó',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƊϪȺƺ¬ǧϾďΝƘҮыъʘ˫Ŵιśǋē¿ŭÔ!ǵɓʗŗțǷ',
                                                                            'Ϳ\x86ɫєʍïϱȳĚˮ;ρϨAҽʣϟĊȞÞΒ˛Ԕ\x85ϭÙ˳ɵҽ˦',
                                                                            'ǲ2ӢˏеļŤ7˘ϯųĖ˦ÉҠɶɵʕϒΒȼмБͶȷʠČKċǫ',
                                                                            'ǨȿΝҖŌѠϩ˼щŏĈψ\x91ōõҷ\x9d¯ƙϔЈϲȥўĞǆȩŸ[˟',
                                                                            'ĹҠ·˗Ćӷƙϯж',
                                                                            'ùɿ8¿āѦɐҶϝЮķɍeЁΌĲΆÕϨ˓ƚǓƌȄʌºőJ¶Ҡ',
                                                                            'ɉΦĊɦμӞі¿¹ѴȰMӉяѵ¼ȬȑŎÛбϯљµƎϠƹѽӹp',
                                                                            'ZώЅҼ²˦sΏ˒Ԛ>ѥҩӞ~Biь˝ĀĦǧΰΨʈĝˆ4юŵ',
                                                                            '˰ѨҙћԒҹнɧ$\xa0Η˰çǯϖԧθƷǬѺƢȩƮÆ\x99ːͳ¿ıѣ',
                                                                            'ьбҠƶJЃҥƁȡˠѦȉVɯÑӜӰѬϲʾʪΙӻûȮİҊſϯ˻',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ĺʻжó˳İ]<ǜІɹϧҘԠjɑѣɯ҃ΉϬɊɵrŎɕϞйӁќ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            230264.64270800463,
                                                                            253056.03090153163,
                                                                            751699.6834885658,
                                                                            342725.8350396169,
                                                                            188547.95741672354,
                                                                            377124.59514365863,
                                                                            30607.207014276253,
                                                                            405723.5464388134,
                                                                            522111.6688533074,
                                                                            895964.8446226761,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʅˋāǊÿǋӄƋƋѼ˥ǺɚȘ˙ƅçHԅɈΖɘ\x86˴Ŕʜèʺşţ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϱÕҥԈʏҤƶȲʺΓПԃɻϝǆԙ¢ʹǼō',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165100.278616:+0000',
                                                                            '20210212:165100.278629:+0000',
                                                                            '20210212:165100.278637:+0000',
                                                                            '20210212:165100.278643:+0000',
                                                                            '20210212:165100.278649:+0000',
                                                                            '20210212:165100.278655:+0000',
                                                                            '20210212:165100.278661:+0000',
                                                                            '20210212:165100.278666:+0000',
                                                                            '20210212:165100.278672:+0000',
                                                                            '20210212:165100.278678:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'шˣԓɪHǓÙҼûǾ҆Ϟ´ˉĂ Мѷʷӎ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            945143.2741710012,
                                                                            637821.1520805707,
                                                                            403724.5811984875,
                                                                            278070.03612165904,
                                                                            731709.5932118077,
                                                                            507520.47136407206,
                                                                            968614.0260087932,
                                                                            -53110.65445354692,
                                                                            142624.36171147466,
                                                                            742550.9744617551,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'СԉɘɚɻėҊҧɥǵӶϙ»ѳЊůЫ˂ΠѮɑщƆǮШįʵĭӣI',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ąōɷ\u0378¡QѵʹͿѧȋƍƊ\u0379Ʃŉ˔ҴȯȊƌξͻ˦ŉΡӨЗQˌ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165100.279358:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˤŕTȰİԊŀȔрΘУĻƮԡłʹˍѹƃʲпӖ˝б҆\u0381',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 633421.4567470084,
                                                    },
                                    },
                            {
                                        'name': 'âӚşӄϧŇΠζυ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ЭŗѬÚцТ˾ϰ҅ÖԡəИоãѼԊʵϵКʐ,ɮ¯ѸёΖοßж',
                                                                            'ώѸQφǥYƏН}ӘmΣ+ˌ҆ˢͿƛĺіЦĝÉ%ȇƺÙ\x7fӲ\u038d',
                                                                            'ѨΑѼŇ˯Ŀ˵ŜH\x8bZȹ\u038dǮϚЃ¦\xa0ʞΏЗΆȿƯʓEoĩϱϱ',
                                                                            'ƈǟĕ!Ʋȓ\x91ˣԋŭϳΘȥҘȜ´aČȌбťϯэəӃ\x84ǜʇĳј',
                                                                            'ˀӍͰĆˍԟȖȟƈӾĳbĸΰȬҰƨRɛΦ\u0383Ėɕ^ԄβкŠ˂3',
                                                                            'ǎɴΫɇŰӆ#ҰŖÍǵȮԓ:˸ӯЖǸĈF˴ѻʞ\x88ԅŊҊοŁ˖',
                                                                            'Ŗʱϫ\u038dɾЗªņɯʞ\x99əьƷǣȐƽӇʱƁѵдҪĹƀϦҁͼɁΨ',
                                                                            'Vʁnǀҳ\x9fțԝʒӛӎє¡ԧЊįɻҜҨ˻æ=Ѯǻ®˓;ɐӣª',
                                                                            'ЯtǐӶćŴɽŇЍýĺǉ\x81ËͳȃƪʂӹњМб¹ˀ\x92ǁ҉ÌӔР',
                                                                            '¨ɋξǋϚɝΈҏΐѳȢǞȕǩǠʈВŊѼӘ=ϘɆʸÈɺϦӆѝȤ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΦϲËçΤŒҨ\x85\u0380ЉҳgǲɼѰ>ϵʋΖ°ƙп҉ŅӠϨm˜ԟĕ',
                    'message': 'YϮƇЧȪ»ӜǠûξȈ˳óɱԔĵȪтɳǊʄɄŽďѿ\x9eâ!ʽŹ',
                    'arguments': [
                            {
                                        'name': 'ĕӔҙŜЀ˰ƥͼuɺĕÞАБӘԩ˷ӵµ\x8cȟѿƔǴơγeĞҷҪ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4294629087006492465,
                                                    },
                                    },
                            {
                                        'name': 'ѧøрΫǞǸƝˌĻƌɆŦgÞǴԦUԋǁҼɇɻşÙγrҭ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            234484.89916474425,
                                                                            415317.7621788399,
                                                                            647924.7494004086,
                                                                            559804.5169575807,
                                                                            -64156.44897289716,
                                                                            858988.7461492857,
                                                                            918165.3553483335,
                                                                            886130.2582614712,
                                                                            476670.4401150859,
                                                                            697832.3084001034,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԚДũѢǄƋ˺ӏ;ѾͻΟ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˋӜ\x85ͺңͰĿЩӴÖʹҋľžíåѪ@βº§ŴİЍƣq\x9eĳÞʬ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1009606290414586140,
                                                    },
                                    },
                            {
                                        'name': 'ϢӮѨЧŌƤΨǞɅӃwқѼҹ\u0378ӭɔϲЪȋԓ˞\u0381ÛȄӶɃ˅ӵÜ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҐɓάΕ½ӕųĽơ\u0378ʃĭ[ěǐўѮķ+\x98ҕȦѫƍ\x83Ȝß½ώȅ',
                                                                            'υàʆЏΑМЈȣқӜҝɨƙǥ÷ӍĖѻʡȂǿȟԔǏγÉʤЉ˂ǝ',
                                                                            'Юҏάү\u0379ЉЈΣǩϝǵǠӦŹɱɔ;DќƴϯäȆӦϔÊ2ЛĖ\x88',
                                                                            'ǒЯ{ЕƑџUˍЊϤǨȊςЭϋXИŁЛɋԡёɰ(ƽɋ\x90ľÛȠ',
                                                                            'ψҫƭϤґ˱ӜͺΗȕ˔Ůύԧ΄\x99ËƭĀԝ0ȅȎPΏ"ãʝƨÍ',
                                                                            '˯ĪʎÿĈΕ˒ɛМ´\x9bÐʵҗßĴȏϨƙƭϐňϔў7ŰłҗΦʷ',
                                                                            'ɶÉҎ¢Ҭ¨ɝWԗгƱǟӭʺƚԛŃԝԍǒϺԒȶĎχ¶ЄͺԌԠ',
                                                                            'kȀϙйˢɀî\x85ďɈUЇ=ҁ\x91ƥǘɘѝΜʐȂõԇ\x81ŊŢ˓˥ƙ',
                                                                            'ʹԬϝʰԉ˻ȌȇɵńӷԏˀԜƁӀư·͵˵γŻƥ\xadʏ˓щϳơл',
                                                                            'ùφơ\u0379ʽϺǨżЃȘǏ÷˘Ʊũ˘ǖμʃǌ˽ѵå\x8eэǻʩɏӬь',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƹӜӫȔϰ&\x9eœћŋWưΥȥӫɜΉԏѓМƛϗɍѼǦѦ͵ʆ\x81Ò',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˭ɿǅƑŤƫҴ˺йҰ˭СŪ·ɝђѻȟĲ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 936030.8831359546,
                                                    },
                                    },
                            {
                                        'name': 'Ȇũ βұɻʰˇ˺РʬŖʨDðўӯА Čī¸ӳ\x9cÑȁД',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8916165641840436015,
                                                    },
                                    },
                            {
                                        'name': 'ϢȭĆȇђġӌǱʮέУЕԬαŵӆΗȩȈʰɝѐŻïĂ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԦНƬȨɷРɓŔʹŏmÎƑϾПԐː?Ĵ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165100.282123:+0000',
                                                                            '20210212:165100.282139:+0000',
                                                                            '20210212:165100.282147:+0000',
                                                                            '20210212:165100.282153:+0000',
                                                                            '20210212:165100.282159:+0000',
                                                                            '20210212:165100.282165:+0000',
                                                                            '20210212:165100.282170:+0000',
                                                                            '20210212:165100.282176:+0000',
                                                                            '20210212:165100.282182:+0000',
                                                                            '20210212:165100.282187:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӔУο͵χRƋˈ°ŵѐƨƊ\x86҉ҖңӟѪ҆˯ΚÞʎq\x80ίѣƱԙ',
                    'message': 'Ĉ˗ϣȰζˀËǐ¸¥ѦŘɱҜƸ2ƗΤêǱΝǱÛ\xad¤ÈĤҟ\x81Ө',
                    'arguments': [
                            {
                                        'name': 'Ǎʤ[ԫ˨ӿʕ\x9aȒȗÁɑˑƓ-ńнӶËʜѨύʑ\x9bŖъƞɊˏĈ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7847044660106533614,
                                                    },
                                    },
                            {
                                        'name': 'ʎȲˋœѳɌЈǋͷĴϏʫǒʦѓŝϦjśǙʱ˓ϜçЇШЂЏ˥Б',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165100.282804:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǋ˚',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8569285627704717531,
                                                                            7225417200724531520,
                                                                            -4476706702084065120,
                                                                            -5806813781568062470,
                                                                            2240474586854654323,
                                                                            -8753279600026541587,
                                                                            2029836354919808981,
                                                                            7523012644417472995,
                                                                            4826818167435520955,
                                                                            3554421866818213444,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͳӸL˱ċʶњɶûμҧďiǓĹѵƿō',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165100.283159:+0000',
                                                                            '20210212:165100.283171:+0000',
                                                                            '20210212:165100.283178:+0000',
                                                                            '20210212:165100.283184:+0000',
                                                                            '20210212:165100.283190:+0000',
                                                                            '20210212:165100.283196:+0000',
                                                                            '20210212:165100.283201:+0000',
                                                                            '20210212:165100.283207:+0000',
                                                                            '20210212:165100.283212:+0000',
                                                                            '20210212:165100.283218:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɄҽӫϟЇƛҩ\x96ųƚҜ\x8d˻ǱŶɃʤW%ϪІĲґ\x90 Ÿ҂ъіģ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165100.283439:+0000',
                                                                            '20210212:165100.283450:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȄӈϓΣԁҊ³Γӫ˃ϮҴƍԁ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 227335.3863271461,
                                                    },
                                    },
                            {
                                        'name': 'ǋϦɡºƋѽϛöɦ˽ϢǤöӊԔӍˎ˰ӪΒˈȨйҢœўӷèΌ8',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ÌȉɦSȜŀũȺ\x90ĈԑғӛРEĔʚԐȗČƮσҩľ\x8cӺɟ˨ӑѧ',
                                                    },
                                    },
                            {
                                        'name': 'ŭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165100.283871:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɾƉƱɥ҆ɡɸ.Ș\x9dıǎŵǾΪzūΪѡĔоƧ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '-4ӑ\x88цƋɶ&ɳ:ЄʶьʑѫҽʥŌ\x83ѻвˣŒƁʪǖɗрʭȈ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǂб\x82ƾȇϓΩʜͱtƀєӗɆ\x8eˆ\x8aѥ©ѐҗөȾƣɈƺȃϷǅț',
                                                                            'YêԁҕʬȟϔâҸƱӿʰ\x9dιƉr³δɏζХƄ²Ѥ>ĖϋƣĆι',
                                                                            'ûГɘ˶ʁǍɷ\u0379ӄԪȝĤԏˡ\x88ʣρǗn`ǗĩѪó}Ӭ¯{ΞD',
                                                                            'ʴŨһνȿĂ°˦ӈ[ɽɆǫƣǨ%οş˩ēCĂзПƠɳԦ˃һž',
                                                                            'ҋ˙Ѿ<ŕEÙǫϼҔѢԙÍʁĕĹƚ)˔ҁǀ˧ΗӴ8ŔӸʲśª',
                                                                            '\xa0\u0381иʫȩÃȵɾȨĔïħrĺªԒϕάҋ˗ʘˣ³ˣΫɕʍǶͶŻ',
                                                                            'ҁƊĝŽVɩǼǩς\x90ųғǜñȸћàƊ\x98˻ӮͼӨĜɋLɤŌΑФ',
                                                                            'ʫƋбĪǤśƖϠϙͻ÷ӵѹÀӨ[ӿăǆԀM˩ƃκρїǝ˹Ʈг',
                                                                            'ҘУɣϷa˦ųȔɊƵpӺ҇ÂΚmΞӤӪѕʆȐʬɹњҝ\x8fŵğǨ',
                                                                            'â˟ǝӞfμκАϧȶʒϠ9ԦǓ)ͶӞ˴Ҡƻ\x86Ð҄ĥ\u0383\x82Ȓ¶Җ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΛƬΫԜпюʤѼ˕ΗΙƼѦнɻˌǿϵʂεμ\x93\x86ӶɿΏƶӱĢΆ',
                    'message': 'ȬɘԧƓϥӏķ\u038dŬäǢ*ȡЭś:ɝ\x84ȝӼƸĝŋ\x84\x8eӁȔǗӈô',
                    'arguments': [
                            {
                                        'name': "ΦԘɤɊDeӔļ\xa0ɷȍҦˏˊѮÚέÐȊ'ˑϠʌΑП°ҔϬҕϜ",
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ńвћ\x8bÄļ˜ÉˊWV',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165100.285130:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʞ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'қӚ&\u03a2ϿʸŏеҎǖƪӉҭͽӢ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 960220.1960571501,
                                                    },
                                    },
                            {
                                        'name': "ɱě^'҇ɴÉҋǃƾӲ",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'KΎн˯ĦёϱĩÐpɊɓћRĨϟԣͼO˵|Ç˝˔ŃŸҭ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '°ԚɝŹrĆҗԖƴҿ÷ӦϚȫӋɪ\x9dФǂƢ6˹˭ǸԀ\\ɆүӯЂ',
                                                    },
                                    },
                            {
                                        'name': 'ȤLӎ;ÃǡŤȖβҟ½ʥɱˊӤҎ±\x99Ԝo\x9cѫÀȯЭӯжɎƴV',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɰőÃƻĐ˅ȼ>ϑСƽ˦',
                                                    },
                                    },
                            {
                                        'name': '.˓K(ҢӓѠǸǔϋѾȄǶĮϤZ˲ϬũԨįǀ²ȏѼ¤āЙу~',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϛ¯ʀ±ϋÙӃЄŰҎΫĆǡ@҈ԀɖćЛ$вӭɸԏɪĳˌιŚԫ',
                                                                            'Ʒ˸ԞЬɞĀƶï˔ƃʼѢˤɲŜǄҜūÁŵћԓѠϿúŁн\x8bԝŦ',
                                                                            '΄ǕFêϣѥҶԧĝЪӊϢӪлúж^\x88\x97čϸ5qÿʜϓƾͲ˨\xa0',
                                                                            'űԂÁөĬƺцоbѢÃ;bˉĜҊ҃яӠļтˠɵҼϻƈǯ¼өҢ',
                                                                            '˵w˧fϣѕӉ\x7fˤϊґԈƣϷ¹žҥԞӷȑ҂:ǐ˾ʕƼҤaįÖ',
                                                                            'Ғ[эBϩҕă˥ĲӥyӴÚʌʤ&˱чЫҳ˺Ӷ͵ņŬ˶ϕɹɖj',
                                                                            'ΆʍҲЁԫКӺϜқːɇƌϑ˱ъ×ӓҶ«ьțЁůҘӞĺҗЗΪ˕',
                                                                            'ƛʊǷɷӪǻӭƨņø\x9fâÖϖƒҩңӁƲ\x801˥\x94ĕҡӡ\u038bʾƅο',
                                                                            'ϧԬůǒͶĘЗϬȶĄХΉǺӄƈͶɥƱ&Ų¨ņƮȽԈȁвŎ·ϳ',
                                                                            'ź(ȫͳȯΤĸ@äͽVˏǄʹϺʢҋȅҬƇŉŋԊˮӎìΩ\x82Ø\u0381',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĨʅƷʂƴĆğϦоԪҕ\u0382δȒNƩЯХǂηŖԥȋ\u0383˕ӡ\x98ƫˡϡ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 453192.7744286634,
                                                    },
                                    },
                            {
                                        'name': '.5ɟ¢YÒ҂\x80ӓҫFоťѾӅơΦʯґϫȬŌȳįǊ˧(ȻĒЄ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165100.286866:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'dƆπ{ЊɸҌӗČѹɟЁϥlΪКЊԮɌϢ\u0380Ĭɻ΅\x85ĿԛɆĞа',
                    'message': 'Ƅ\x85ΠǌГΌɳŐƛʷȑѮÝ\u038dԈʘ+ɴʇɰ¨όЌȦȢŤ\x8b®őѪ',
                    'arguments': [
                            {
                                        'name': 'ɐІӡθ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 440459390117072629,
                                                    },
                                    },
                            {
                                        'name': 'ҤȏÛϩзʔ¦ҩЖƊɝ˭ȼʎϖҦЦp',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165100.287428:+0000',
                                                                            '20210212:165100.287441:+0000',
                                                                            '20210212:165100.287450:+0000',
                                                                            '20210212:165100.287457:+0000',
                                                                            '20210212:165100.287464:+0000',
                                                                            '20210212:165100.287470:+0000',
                                                                            '20210212:165100.287477:+0000',
                                                                            '20210212:165100.287483:+0000',
                                                                            '20210212:165100.287489:+0000',
                                                                            '20210212:165100.287495:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʖŗdҨˁѺβ˰ǩBȉZјͶčŌåʡʋɪ\x9cϯÇŭ|˰ʋŘňѓ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2422701951799874727,
                                                                            -4392286635164342381,
                                                                            8368587372954367715,
                                                                            4640217210035894858,
                                                                            1984389992718980495,
                                                                            1960269271240123631,
                                                                            4904540529347868355,
                                                                            -1862935649340302837,
                                                                            385849472493690121,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɳǙӻ\x81\x9eǣǼΞ\x99ȉӟÔȻӛԞnʂĕ×\x84\x84ź',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165100.287988:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƥΐŢщԓĦˇ\xa0ĝ{,Ș_3ŷӈɨÅÚɹɡοҜΩĬ\u0380*ΎԢˍ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 823901.9558847015,
                                                    },
                                    },
                            {
                                        'name': 'Åŝɪǡ\u0379Ǎ\x8bȣÕ"Һїȗȵȗ¬ҊξǊ\x9cљҏϣɢ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6774183459355849396,
                                                                            -4525854432103713831,
                                                                            7646919293690508949,
                                                                            5139500495806769323,
                                                                            8983553138613570299,
                                                                            3248996191675743924,
                                                                            3325348211800053210,
                                                                            6283673640049113609,
                                                                            -3590950336248325992,
                                                                            -1355742341688956437,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ůʦŏ\x81Эȳƍôˁҋ\x9eCϙ£ҟɲѫΦ\u0378\x9aƳƱUӐļǁϬù~һ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7655671899647167536,
                                                                            1760125750864496814,
                                                                            496117839278472197,
                                                                            938229490605894999,
                                                                            -4140364877465953343,
                                                                            2875455349377022478,
                                                                            5810096852478878344,
                                                                            -6028779013240608482,
                                                                            1556552731103273672,
                                                                            -1043926825189691136,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӵʢʚԅşɗí˵ЁˁчÇ\x8eҾʱԊʀ\x9eΕɅɃĴР˻mӿǞǘЍԭ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ґþϾ/BѡҕПӻѡîʐéŋѩf\x82ϒ1ҷ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5507537166095223263,
                                                    },
                                    },
                            {
                                        'name': 'ƁЬN˳ɻʈӋƑd˵éı\x9dϋɢҢ#4Ɗ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7049392179553861701,
                                                                            4537863287186835795,
                                                                            -8446838753666990413,
                                                                            -6888520703369882288,
                                                                            -4129021855518787895,
                                                                            7038562180444710607,
                                                                            3352239701376680072,
                                                                            3260721146678258131,
                                                                            -3971473371581821536,
                                                                            4325911573463492948,
                                                                        ],
                                                    },
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'scope': 'warning',

            'messages': [
                {
                    'catalog': '\x90ǭ',
                    'message': 'Ӝ',
                },
            ],

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
                res = logging.Error.parse_data(test_data)
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
        for test_name, test_data in ERROR_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.Error.parse_data(test_data)
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
                dict(field_name='categories', name='Error'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='messages', name='Error'),
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
            'identifier': "ӛӥć.˾щ&ęȄˢ϶ԓǩ'}łԔŎƎϕИϔËѻɪѝɊёƦҹ",
            'categories': [
                'access-restriction',
                'configuration',
                'internal',
                'access-restriction',
                'internal',
                'access-restriction',
                'network',
                'configuration',
                'file',
                'access-restriction',
            ],
            'source': 'ÇƨƏӝȈҞ5Ɣ³ʢӊ/ɴо\x93ĵΕӒƹ\u03a2ɻIɲĹÐƗԕβ\x8fv',
            'messages': [
                {
                    'catalog': 'ʡ@§\x96бýʐȀɹ#ҝė˭ŅZő+£˺¦ʉҽ˽İÒԭ˨ŕԌɏ',
                    'message': 'Ȁ\x93Ĳ¹ŕʃϋɃϱʤɡлѧǿλЛʑǚǴʰOФFηäʐԬƜ|ƶ',
                    'arguments': [
                            {
                                        'name': 'ƍѦɩ£П˹ö˱ԥǂ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2010169651352649383,
                                                    },
                                    },
                            {
                                        'name': 'K',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˗ĊcҰȺǮƀˏұ˨ȠҎÍɃΈǸƋ҃ǬȢѴ>įΛӦƢſ϶юS',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ǡбȕүǽ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ͼ÷ɶɞźҬÙ΅ɘԟY\x8aӬ\x98ҮƵ¸ϢèĦȱ/ʪĆТƒÖŎrk',
                                                                            'ĀѲԧƞԫɘЄĹҳÀčеʰǳ<ȭѻɂр`ńϫӡИӵӒӔşԭң',
                                                                            'ɱ҆ǿáԁɸɐǦЊУʮŁɏ˹ǅѧ:¥Ӆҡ˛ÿͱǄΙŐρӏőɃ',
                                                                            '˭ȃ\x82ɮϠIѬȡҒǷ\x8cėɚ?Ⱥӄжɤҗӻ˶Ƿ©ʩǕɌϾϐȻӁ',
                                                                            'ɼЫ\x86ŬYºŽĆʵ,ԈŻΣƞӂŞ-ļœȚ˔ϖ͵ˡϐȟαÔƪB',
                                                                            'ғhрʫO˯Ą˃ĨǈЮόĀɅʉҤАɴǓ˹ђƵ\x95ɿXѵϭϘԛƥ',
                                                                            'ʕ˸ʆȖ˨Ƈ\u0381ҎʮčÖƏɌæπǁүΪˢԨ˸ÇʊɞΤԦȧ\u0382ˈ\x7f',
                                                                            'űҡ_\x91Ӏ\x93Œ¿ԛŏ)Z\x8dʫǼϝΚƫǲǱӸ¨ӫó˹ЯƯ\x94Ïā',
                                                                            '\x9bŝɍʳ˝ͳϳśкѪͰdƮİʱʊԇŪŶͺɘì!ҲҠȁ$[ω6',
                                                                            'ΌʌŤʀƽ˻ìńԀœ\x9fӴȮϲ΄ƉӮ\x83˫ȠԝŴàҽȥʋYÌҎΣ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'äíƻ҈LҾ/ԐÕªųɶώӮѹϲĭхθО·˭ԭjӷ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ûƳρϛÑȲɛǓɼɲėѻȏ\x9eɐ2ҳτЋȋĔʫǏɑǓһÅüÚǲ',
                                                                            'ѵ˥ƎЊØӌʭηl·ƧӊȜΠįMўЅϾɋóʎѸʄәŴϠƜ˞Ş',
                                                                            'ωϛØϐɋψԁхĜфЧҏљ϶ϊˠ\x9bϝӺˢÊőȶҔ÷ŤȲưԇɐ',
                                                                            'ě\x86µɤɟçɒșĞʝˡõĸǇǓж-Ûùʩӎë)µЌϗζμϸʆ',
                                                                            'ӔͶŐģ1ŠđFҧˑŹĿӨȢ˞ъuŚǹ˘ІƘʑѨƢ˳źІєJ',
                                                                            'Ȇ˼Ѓã\x94]ЇҘЎUǮɻьǑƩ´ʍƴũҋέªŉπ!Ĝ\xadԏÒʒ',
                                                                            'ԒοɄεʔǎȏѬāĊ\x9cӁԢˋʾz\x92ųǅxȝѳſӦǅǒˣҒˮƎ',
                                                                            'ѻʢɾϤɐѸɜќƸơѵϹƚ҄ԣǝʈȉцȷКǏ\x90ɰӓʃ6ȵʠǡ',
                                                                            'ԔɳʿŅΫĲUϾİɧȰĥҿĪ¤˧ǖј>ԁʋV!\u0378\x97ŠʊćźЇ',
                                                                            '˟҇NŪȧъȌϐΰîʞɇɉ¦Kԛƶǈ£ώřʩͽŐ˪Ýѭяρϑ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ſĊ¬ӂž҅ƌҚ¯\x82',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6686361455211459304,
                                                    },
                                    },
                            {
                                        'name': 'ÞӼΕҙîϤːΟȕғʃӧƻĲąƢ\x9d\x8eƹöϝ`ǐ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            428318.92011525214,
                                                                            513926.44272935623,
                                                                            399192.12094261375,
                                                                            22752.37322449316,
                                                                            598340.3958857098,
                                                                            835736.7279199822,
                                                                            299045.36359377304,
                                                                            830916.1429875713,
                                                                            394843.79133347014,
                                                                            807542.1159400734,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ч·Ӓ˵*çґʷŲ\x8eӢćʆǥϗſ˲6ғсћˑӄºҝ>ßОɿΣ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Τđӈӎ½ШyːҢúӺΣԁ´ȓʬŒϿ\x92ыĹЏӦɟң',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЇɣѧʙԍΈɐˆȔȦɐűĂβӜjȂcɑǖ˚dŇȻϷĭʣÒŚϓ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӵRȼʏɗ\x92ϲğȶͲƁÛgęʕıq\x93ɂɢ\xadĐ\u0380ǙɫĦτ\\ƛҢ',
                    'message': '҃ԥƐԋËόǨȩȬĳ˰ыԝϯŵǀɮɎČ˪ЇдˏğɬӑʓǃƟ,',
                    'arguments': [
                            {
                                        'name': 'ѓȘðʥԚΙɣǺđĜԆȖÚĄȗˠqͿԒɐŤΣ҄\u0382Ǫ±łӍãǍ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            183768.27868203179,
                                                                            587581.0445228572,
                                                                            -60438.94205598982,
                                                                            64213.447995700466,
                                                                            707045.7817763031,
                                                                            182604.27213271707,
                                                                            379489.9378255932,
                                                                            691549.2043674792,
                                                                            499054.9859551309,
                                                                            -99713.04278799258,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʧʏζӫϊŐӈʸɅWäʧӋ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƸϙîҦүÌƍȌўͿʖƿ˧ɒŷɹǨЄȠʻщыΣì҂_ѧ³˔ʨ',
                                                    },
                                    },
                            {
                                        'name': '¼\u038bЉ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Řԫơ\u038bЄâȷÌĐѺʡѮƟΣQѓΩéΏԐȮщúѬ»Ȅ´1МÊ',
                                                    },
                                    },
                            {
                                        'name': '\xa0Ť§ΑƣǨǓμ˹Чɕшû',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1997775176318376996,
                                                    },
                                    },
                            {
                                        'name': 'έеȻŀτβΉѪȕ˃ȷ˂ƈЊϴԖĿҪѼȆɭƤ´ïӲƣʬўëķ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6259805705656207371,
                                                    },
                                    },
                            {
                                        'name': 'ŹǤȀ\x96ĈÔʾŸʇϛ\x80\x8dɋΡ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            161624.71637940404,
                                                                            924083.9237173514,
                                                                            782867.2225892779,
                                                                            858226.0245487123,
                                                                            637934.7836943156,
                                                                            485285.81019535125,
                                                                            663524.2457488661,
                                                                            890181.8812675728,
                                                                            42216.16393108104,
                                                                            105722.15448793722,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'δ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ͿIНŠɈΪԭʼ¤ăшŖЊƵǟˡϊϸҙɢИŀϵˉʹäφƓ¶ͺ',
                                                    },
                                    },
                            {
                                        'name': 'ЦȗϡĦϿҗɘЅϝˑɬԮQţŮοҖЀ MǣóӾәʈ¹ѳЍϭȒ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165100.312304:+0000',
                                                                            '20210212:165100.312319:+0000',
                                                                            '20210212:165100.312327:+0000',
                                                                            '20210212:165100.312333:+0000',
                                                                            '20210212:165100.312339:+0000',
                                                                            '20210212:165100.312344:+0000',
                                                                            '20210212:165100.312349:+0000',
                                                                            '20210212:165100.312355:+0000',
                                                                            '20210212:165100.312360:+0000',
                                                                            '20210212:165100.312365:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ďЗmĸʧʊʩ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            196813.01950633916,
                                                                            832756.5188695681,
                                                                            656728.9471143628,
                                                                            996178.8129600384,
                                                                            172817.51054824283,
                                                                            324441.9401908524,
                                                                            664811.0204717393,
                                                                            129456.26261459236,
                                                                            -95882.84567166997,
                                                                            645617.6237795239,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'UҶƅɅźā',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x9aΣΗɃəżԓұōϘţǧɠʞөϮΘǗɈӕbÛʯНɰϡӐ£Ӝϲ',
                    'message': 'ЫÜųƗʰșЃģWтɾтɧ>ǪѲƃˊʖʕ҉^\x98ĴҹѢεǝΪǘ',
                    'arguments': [
                            {
                                        'name': 'Ӳʢ¡ſϯȰυÔùɀſϮ,ΊǊԊìё˃Ƞ\x8eˌ=fʇп҈ȞНі',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѣÉüөˁĴӳӇЫȷԐԒǭ¶ŕʎƼ_ϏɾϻЄƷӨԇˊʗcѱΠ',
                                                    },
                                    },
                            {
                                        'name': 'fȲƑ҃Ϣϟƪр6ρͺ\x84ˣУӔɈѾ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            483521.5982534804,
                                                                            739052.7848456048,
                                                                            212935.87855057337,
                                                                            804540.3898893652,
                                                                            814330.8413522121,
                                                                            491716.4054024515,
                                                                            707459.25034548,
                                                                            274734.1876429928,
                                                                            92816.44476860788,
                                                                            -84998.57122865791,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȿġCéԊ҂ϺԣθʷȳҖƧɿǀþɐǑПбĬ҆Ȉ¶ʶϴԋĺӮ\x9a',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            889127.4054055056,
                                                                            198511.40902867564,
                                                                            -23242.47962003958,
                                                                            139756.63217583252,
                                                                            652584.3608669576,
                                                                            299327.097754011,
                                                                            925578.4048916007,
                                                                            645468.490694943,
                                                                            571220.9845527342,
                                                                            882227.171924098,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҽȥғ˪҂\x82ƎϊßϢϠÕɧŷʈćΰρ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ԓ}ŅēˌŶȣВʈȊԓĠİɛFÄӡǼɏİǔƭŞґǠӚŅ¾ƩÎ',
                                                                            'ʗĊǻЏʽѥʷŃǎ\u0379ϽӭчǓ9¸ǃ҃ϩȪԘöˡˀһθϼġїʕ',
                                                                            'ƚУȵ\x8dǮ˳âŸΟȩˈӊΣŢΛɗңқ\x9bČè˥ɏ˥ǥMϒȣɵʰ',
                                                                            'ʸʌƖФД)ԁƿďήΥǣʿϛˈҒhѾʼΙ9ēӿĞǼƵΪƻΪЏ',
                                                                            '²ś}ǆƿӥѰ҇ȉ¦9ˤƓʥǭžйúДöŝgǖɃϱ\x9bɪƙыK',
                                                                            '˜ίTÇϵМ҆ÖÇ˛ʩҳԜóԓӇňİЮɲ±WǯӢωԕ˃ÃϔȺ',
                                                                            '\x86ŀŝ˻ŋÌWČgnòAԮПȘҍʥͲƂ»ɺϾʦWϜőҜŤϙҶ',
                                                                            'ǰԩҧ¡Ǐʏ\x84ҪńʁёӴʟ,ĠбчȁŴɵ˅.ʕwгľˮԩӓ҂',
                                                                            'ϣϽ\x84ǻÂƇ\x94ŰŦɁϘӯ϶ȣʌɎŎқҋ˖ӫ.ˑѦ¶ϟӞˢ\xadЄ',
                                                                            'ϭ4ÜɀэˆɝЂɁȆˌӘЖЊӅų\x97Ŋ©ҋΑҭ®ӐӂȩŒҽҹͳ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϟ˾ѸPǙԮщ˥Χӷқ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165100.314130:+0000',
                                                                            '20210212:165100.314142:+0000',
                                                                            '20210212:165100.314150:+0000',
                                                                            '20210212:165100.314155:+0000',
                                                                            '20210212:165100.314161:+0000',
                                                                            '20210212:165100.314166:+0000',
                                                                            '20210212:165100.314172:+0000',
                                                                            '20210212:165100.314177:+0000',
                                                                            '20210212:165100.314183:+0000',
                                                                            '20210212:165100.314188:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƶƺщԛѽ҇ɥҧԖ\x88ѝʈұǞрǑ¤ž°ŌũǴЄ˳ңʀԜƬč',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165100.314398:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѬĮȃШԜǻ8ŴНϸ;Ȣʹɷȿüҝ\x9cЬΓƗѳŹсŃɴǈʓŠǮ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2383204556711044373,
                                                                            -1965964543224410952,
                                                                            1814741967123165550,
                                                                            -4071769634390278952,
                                                                            -295814124055685737,
                                                                            -5051559217855609814,
                                                                            642798134870550766,
                                                                            7848529267648890298,
                                                                            5873501745458344128,
                                                                            6120012490424138141,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϊѳЃ˩ņˑϥȒІɼÛˈ˺ɧȠ\xa0ǣǊEZӌǲʐз˪ͳʢƵȲҞ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԀȐì¤˯ё˴ɅZГ¯ϙŬǛϵ\x95ϴӣĨ±ŻƽѫŜԚȿΞǛ\x8aҧ',
                                                                            'ĝҨҡìԑҤԇʗ ԗȹԫϐ˳ƴ˽ԓψԣ\u0383ӛ%Ҡ϶ˈϖCʾļÎ',
                                                                            '|ċэłέƗǫϿҼÇ\x97ҢʕɈΙ¾¨Ǎ}ǩѻёɢѽ˕ѡԘʙ˴ҟ',
                                                                            'yɲϔ\x9bϐώȄɶ»ɮсӒͱϖνÀŮ@ˋҋ©Lɥ˖ЋˎұČ\x93Ě',
                                                                            'ъԘъԞϡк˰ͽ˝ēϛͽͼҨˍӬʫϦğʴιͷÌΥÔѡȚǼьý',
                                                                            'Ǭˆ˃ҜЫӰɉӖϓɯԨǢӻθðӏĩҲҍȁϡŬģҠȱ´҆ϚĜÿ',
                                                                            'ғӽҏȄ\x8bςŖΫˊЮʘ¶αЗŻӢ(ȬȹCśıÄȸʯδјˤȟӓ',
                                                                            'йČĀőɉʺ\x8dr¯ѐЇnƁƞFЛȭĪŞζооħ¶ȱϖλș\x97ȟ',
                                                                            'ƣĴƿѰµӉɻ҅ɒ-Å͵ɁˈΉχ҂СύϿƪkВŕ˺ңʙǅÕ¤',
                                                                            'C\x8bˈΉ҃Ͽ҈ıȊǲİķԪқҍӢŉʄӅ_Ў\x80Ɨ,δˎˆA˵Ҋ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΕҟÆї',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            241021256146484123,
                                                                            -7038692960581259775,
                                                                            4603488782703801939,
                                                                            -2462759247943247979,
                                                                            -7750457003798716460,
                                                                            7748507010223233783,
                                                                            8169484947836813326,
                                                                            5686752122826577161,
                                                                            4083653358003729935,
                                                                            2687452497087905616,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʡҴĽðąC',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            667912.3549975724,
                                                                            892305.7307960978,
                                                                            798233.3026102759,
                                                                            603088.4339687481,
                                                                            545837.5842630534,
                                                                            844234.1897412767,
                                                                            18306.933690944687,
                                                                            160170.14480846943,
                                                                            631958.6323671859,
                                                                            263637.4251310719,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƉĻ',
                    'message': 'Ř½ŀǆʸƵȦƉäƫɈʁǸàT˻ʽƏϩ1Њ÷ԞΜáҨԗZ,Ó',
                    'arguments': [
                            {
                                        'name': 'пǼɱlӊ$ӎ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¾ԈǪ\xa0GҲĶӘȣɄУђӴjŲ˚f',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 669192.6486018121,
                                                    },
                                    },
                            {
                                        'name': 'ɂÂѥ.ËѨųԣ×ǰƛˌςVʼYҦЎ\x92Ȣ"ϛǳ\u0383ȞʁăҩƜГ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƯŽӤњЂӋŽҁǱ˺ɤҏʈӏřЫпԙѧƝ˯ęϟƃɲŝ˫ǗͼÔ',
                    'message': 'Πǌә\u03a2ÿÜ>ƙΩіΙаĦҧǗ\u0378ѩȈɹ˂ƶԍ|Гɚȕ\x95˾ӯ˄',
                    'arguments': [
                            {
                                        'name': 'ҐÄďůËʒ͵ҝ`ȕʟ\u0381ѫԖψÜʫИǽŖѬӴȐΌǏǁ2ĕϏԧ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4519792199014552075,
                                                                            1556590911261522555,
                                                                            -6561580064458851036,
                                                                            5358948981097661412,
                                                                            6462407794179714515,
                                                                            -1289727420038057081,
                                                                            -7189337153261204719,
                                                                            -8941558210694408041,
                                                                            -7027365167898383854,
                                                                            -2837707338164688151,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȇҍŀцɔƨь˖ѳîåηɇɦɎЕӢǱǎȏȻҚɔ˄ŝNӷΔńΡ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '҃˩ӵY҃ŷʂĺҔĝтɟ=ȠѳŪҜƁѡ˂Αŝ˩?˞ǩ\x9cƭďА',
                                                    },
                                    },
                            {
                                        'name': 'қŞҡǔ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɢӀjɃɧoɈӃЮυȭǔόϷʯċцβҾǮȣɼϐȰÍʇґөȀѼ',
                                                                            'Ŏľ\x96aѐҷԕѵɘʙļɃƎώQȿӐЇ×ѺҎŷʮҜȍԬēЀΗѼ',
                                                                            '\x9fԋȜԒЋη²îș8cҚԎuǘǍԐęʑȎѱ˺ю¤ΑȇԫĒrΨ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƈΨ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˣ5ϹǾЯӧÑˇӶ¬иѣř¡ѮӘеѴŨ҈ØƯǩӽԇɍÒėϭƽ',
                                                    },
                                    },
                            {
                                        'name': 'ŝŊŔӖһƳɝ˂ưÃӲRȍǶƃӶCˠԮ]ұ͵ҴĻǹӂ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            568791.6147479629,
                                                                            291123.05227889057,
                                                                            269407.85499727953,
                                                                            776548.9389810642,
                                                                            25579.816080953955,
                                                                            883906.2489664317,
                                                                            129595.66454378585,
                                                                            310140.99582493264,
                                                                            936961.8941232786,
                                                                            813443.1182733037,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԏþİɦЅXӞȝ\x9eţћʿˤƲԆӤȁӾǐˣɐgɐ\xadӺˡ}yӂɔ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Л\u0380ϣ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҧ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӉЬΞšǲƗǍҢӼ˅ҪΐӘ\u0383ӁĺļҒʆƢLӢҊǸԈʲ\x9aҗϽE',
                                                    },
                                    },
                            {
                                        'name': 'ҪΣKǐȁǥņɻźȕŁѵѹӮɯÆѨ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÈWҥҰԋʣ˱ϜьĠǈĦҔÀątǭηˮњҗОΌǏ®',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1969903188115610207,
                                                                            -8490407195298047673,
                                                                            -3860632067058777086,
                                                                            -2138960661410509119,
                                                                            7764761461791548357,
                                                                            -7874741678593725046,
                                                                            -6544601336416804046,
                                                                            -4598202830471402760,
                                                                            2906183052016409437,
                                                                            2145008545455755442,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӥŉ|ɎʌԄДҬҹī«Ʀǎ˭ЀÈŀƺÀÛǆόѾł®ʏ˵\x9aф\x91',
                    'message': ']ïάĦˀԀѮȖѢˬԜÃbĖ½\x9eʧҳήьҟƔͼіҬţԄơϭœ',
                    'arguments': [
                            {
                                        'name': 'ΙϜΔ?жїéМʗwǡʔҵßʝɲԙԎʮΗ˾Ʉ˸Н9ȏϵǨǩː',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8412939224452983733,
                                                    },
                                    },
                            {
                                        'name': '\x9cњθ϶ԫӉҡʠԗÙƸʀϩŌˑӖɜКԇӼ¿Ϟӄ˔ͷ\u0380ʯơǑú',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ҠЇθğǪҩʛ±O\x94ȔÉĪϸǩœūƩŤε²ІҘэԥʢʊq¦҆',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165100.319409:+0000',
                                                                            '20210212:165100.319429:+0000',
                                                                            '20210212:165100.319436:+0000',
                                                                            '20210212:165100.319442:+0000',
                                                                            '20210212:165100.319448:+0000',
                                                                            '20210212:165100.319453:+0000',
                                                                            '20210212:165100.319459:+0000',
                                                                            '20210212:165100.319465:+0000',
                                                                            '20210212:165100.319470:+0000',
                                                                            '20210212:165100.319475:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԒǑЊ҅ƴȔӻ>˛ԃʩӃːʌǆ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165100.319683:+0000',
                                                    },
                                    },
                            {
                                        'name': 'úŧϮƔŤ°ϩϠȇæЉѤˇı˻mŕʲį˲Ǘ˼WϭÒϤɭӂ×ɫ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɗӎљŕȀAƈĶǻ§ӨzÞǧ2ү¤ϳНΊʫƻͿʓŀ˨Ǆё˃˷',
                                                                            'ТBǭϵǳ˶ǊѼ¿ȤӖêΈáτżшѾ˥3ÎɒŜ˾ЛˀΰÓk·',
                                                                            'α˅ӗҝNԐϾȹȴʂġ˖ͳŁǑšȖΎ˴ÆƝʡ\u0383£Ǜ˝Ѹxɒȁ',
                                                                            '˚\x9fΣӕǨ¶ИҿˀʦѠûѩԝƸˣƝËʊԖ\x7fȥїǍƈ˘ɥǆǂɊ',
                                                                            'ȦςƉ˛ì\x9dɦ¿ξ˓ʻɑҟéƟҾв:Ӊʈȭù²\u038dƊйȍˣίԆ',
                                                                            'пԥĮɅʎаĂǍЬ×ћѿѽҪǍʭχơϩȴšǂȨͱԁĺϮĮөԈ',
                                                                            'ԛɄ\x81ΨΦ<ӠŨÔȁɰЧɈԞʇ˨ʲФƥǬԫϐɢ³Eɗʂǈƞˏ',
                                                                            'ϗ\u038dĤЧĶĢɻÅ\x8fʱϸ\x94йɩƐɔƅȐƑѣҝiϬŧӨɿ\x85МȒϼ',
                                                                            'ҩǥİ¿Ԡi\u0382НӭĭΩʘԪʑъłČ"ʰ¹\x94ǾŵȀΒԋhӗƾƅ',
                                                                            'áėƮκҤ\x82¾ʞ\x98+2ȃ˘ǚЈӜÈɊЎ`Ʀț£ǌҤɳƲȾȈȩ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӾZΚǗǼɭ^½ǐŧƪ\u038dґˀʍԐŜ˺Ȍ˗ÈŪĜʴɿӇȼĘҘ!',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѱŁф\u0380(σŷ҉Ԓќ,ɉˍͰπȗơȯbʦʟȧʱ˛уȊӚˉŔʅ',
                                                    },
                                    },
                            {
                                        'name': 'ż6ѴĀмƌ@ө6ɕ˭Ԙ˴ǐЯÂԛҘɢĽшҁÎƍǁԏс2Ʉť',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7779639888667189759,
                                                    },
                                    },
                            {
                                        'name': 'Ѥ&\x88δАʦńċМαаŏƶЀνбˮ_ŘЌ\x85ЯӿɽӜсE\x9eҿȔ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165100.320503:+0000',
                                                                            '20210212:165100.320519:+0000',
                                                                            '20210212:165100.320527:+0000',
                                                                            '20210212:165100.320535:+0000',
                                                                            '20210212:165100.320542:+0000',
                                                                            '20210212:165100.320548:+0000',
                                                                            '20210212:165100.320554:+0000',
                                                                            '20210212:165100.320560:+0000',
                                                                            '20210212:165100.320567:+0000',
                                                                            '20210212:165100.320573:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԩȥ\x86\xa0ƀHȻŊʞ˥ǺĐ\x8eė(ΌʂʇːÂƛΨȜ˸Ν˱ˌźR҄',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1706306644632878059,
                                                                            7972980228303594865,
                                                                            -6056595467332543903,
                                                                            930014229942999783,
                                                                            2961327949502111579,
                                                                            3387656823196439596,
                                                                            -3252396043432847761,
                                                                            2412726493094576277,
                                                                            435517446905329682,
                                                                            4186532530969759697,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'áʈҧ˜',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ƿҧ',
                    'message': 'ÅтōƋԥŴҝΛөőăĕÝԫɋπ6һƴӐĵªΉѥȯȬΔ\x93žʟ',
                    'arguments': [
                            {
                                        'name': 'Ԅ#ΕŴԏŏϟȍҨɳκŵŉ\x84Á\x93|ӘԅϢѿǋѓÆ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165100.321639:+0000',
                                                                            '20210212:165100.321657:+0000',
                                                                            '20210212:165100.321665:+0000',
                                                                            '20210212:165100.321684:+0000',
                                                                            '20210212:165100.321690:+0000',
                                                                            '20210212:165100.321695:+0000',
                                                                            '20210212:165100.321700:+0000',
                                                                            '20210212:165100.321706:+0000',
                                                                            '20210212:165100.321711:+0000',
                                                                            '20210212:165100.321716:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˵:ӆǮŘШ@ΗҀԙȾӑȌԆҫƸƐƜáYΌªÈÆ˻ҢƸƧўǝ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            465508.7545389773,
                                                                            674832.0118806241,
                                                                            489655.3851482534,
                                                                            347623.8208705584,
                                                                            19471.513189708727,
                                                                            623013.135621231,
                                                                            141198.09142590585,
                                                                            767444.0693445359,
                                                                            -28575.90557070596,
                                                                            873995.5540335551,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ńŦ7҉аɩȉǯ҇ƫǵƉVʥ\x9cΦȲ+Фʞ˖ӵʆЧҵлһȭ˶г',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƥ¡ԚȢΏɹͼҭÛƍʽg\x9dƊ\x89ɼĠНГǇŧ˛ǣýӾļέƃÙҫ',
                                                    },
                                    },
                            {
                                        'name': 'ʓ5Ϊcȋǅʘѩ\x9e',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5410091808374398282,
                                                                            6328253117837630976,
                                                                            654140677171133457,
                                                                            2657286534801916939,
                                                                            -4561408731549958523,
                                                                            -6361335283690683053,
                                                                            3544000074661731990,
                                                                            -3243326222165830600,
                                                                            903523066106201524,
                                                                            -6076714856475544785,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɡϮ\x87ƛΡȠƺ\x88ŚоăӣѭțԠʪͷɩÅǨѰŉƩw',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\u0380юОȷϯŊǤĿѩâɝҏϖwӮƸȋџʗ\x9aş)\\ȓǪҀӁűгΘ',
                                                                            'MѬғϥпІ@ƐɍҎ&ͽÑşѩҐԬҧĤȿʪǜԏƈ[˖ѓҦɟϨ',
                                                                            'Ʒė˝Ŕƃмȱʹӂƞrӽƪ\x9fǐҘѼҦԅ\x7fѝÔ{ӄϳԐ˜ԕІĺ',
                                                                            'ĤąōόҋŇƁяґεhҶɍĿӌ˰ҞʢԘ½α˪ʞӵǔȄӬϬϣD',
                                                                            'ήAūӐΏĽÊыĊ˘ɞˢà.ʯÕҫɎˬҁʨ-ѠҤўƿɍѓş¯',
                                                                            'Ƕθ҅ŌңøȽѕÏŶĤӚӇѓ\x99\x95ɉŽӔҵʤwǟӭĮΩˏ¬ҍt',
                                                                            'O\x80ͿσԟˑЂŠƉpYț\x8aǬӐԔϠˎÎŎ§ȾŰʸgЊ˦ѓȚW',
                                                                            '҉ў&˗юͻȒſǵѻӉ%Ŭ:Ċ\x93ҬƆɰȾWԄԔѿ\xa0ʾԞćƝW',
                                                                            'ˇſϴek?χщό˨Əčǩ˚ӽӓԍΪъ\x9aўŉŻԙŻɛ˓ȉǆē',
                                                                            'ƹӁДӸª9ΓӉȉ\u0381ȝϛϵӚʻæʵӿˠHȔдѥŷӺ\u0379?Ќԕä',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǾǔшO\u038dҤчĨ˞ϔƏΌôƶξ9Τ«ƣçϛκħðqɠˠμϞʰ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "\x9fҹȷÄӱηȯ˂?ν'\x93ӛԘζp˂ѲÑЕѠЇЧ^ÖzԏˢӃʣ",
                                                    },
                                    },
                            {
                                        'name': 'ĠŪϧ3҇ԌРҕԪŪмѼϮ¿',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'σ·ʃŕљőėɵƴзχǸĲ˥ȃȡŌˢƕ˽ňʽĞѼ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '\x89ѕȠ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165100.323409:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÞÜȞӞŇҀpŒ¯ƬҰӨЃίɁϼů˴Ͽ|Ȗ\x8fB\x87ŵӆӇǯАx',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˊ˲ɭʨ˴Ѻӡ˭ԙӍ6ѳҲĔ0·ςԥOԟґõɇѕɚǄбàӧX',
                                                                            'Ƙ\x88κàʦfǇɃԜθƾ\u0380˂β~&åƩЦȰəFęЂϪЯ¾ͽӢ\x9d',
                                                                            'ЎʶͷԖǊYˊĘɽї\x82ʐțӕʟԢa&ɻϩϳÐŎɜΦіѨ˨Ɂ˛',
                                                                            'ďƘϼҋǋʣΘƁɐ_ЄмDɄΔ\\ÆãӏӋa˻˹țЉќýХɂɬ',
                                                                            'ΨԉƾǔËʒіǖĢūȍυũǵȶΰ҆ɤǗԩřŐΛ\x80ˋϑĞҿ-Ğ',
                                                                            'ЁЩүǅҴŤʒͳˆΓÆǇѺА˃ЩGӦȔƐȀˮǨϕpƜЎӇɪʟ',
                                                                            'ʴŀУΟΈįΛƥ¤yRԏʰfˑÖϧԉЅλǑєӋýµдŖĘ˃Ϸ',
                                                                            'ŧч/ŮǰҍSŻʻˏɌʾəҳƄĦӿȽтԌъŊǁ»зѰѽӱ=Ӑ',
                                                                            'ˠʹңϗȪȈˠɄˤѳԎԡù`ϰԦ¸ϦƲѧҩΞêӌʴȸɚ\xa0ȹҲ',
                                                                            '´ªʇϐ=ЎԛŏȤ˷ɀʒϓ\x8eÎ\u0381½â3ԚψǰȒҋЎőңçéǟ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ͻΧǡɱҐŲҧĕцÚԞĺÙ1ň\x809Ȋ˧ϚɞѶĪăǽƥ˸лΩӺ',
                    'message': 'ŔŴҼЧʶ/ɟŴŊӑ҅òԏʢҕ˸Ґ˰ӒӬѕΨΆǑŽͰҋ`҄Ȅ',
                    'arguments': [
                            {
                                        'name': 'ˆ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3020881681773812196,
                                                                            -147427126231292733,
                                                                            2352755752841587584,
                                                                            -4256463012155262795,
                                                                            840749453362837885,
                                                                            3470689290259896877,
                                                                            727019233519791674,
                                                                            -5749228680665712155,
                                                                            2875215396561860753,
                                                                            8966808722438559445,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'гмьдǋԤӅĔʶûʭƊ\x8aԔѼŇėLƜķԗ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŧʽ˲«ǄĔxӄҗɴ3ƚƨÚȴ¾à{\xa0ʣƍƉőжӷΗӅȒϻЦ',
                                                                            'ņƐ´őʢȝªƬ³ȐȡɊϨʲ/Ϧϧӆǖ~Ԅ%ϜɿҒϦĵɔhȀ',
                                                                            '\x95ˈΰŖơЗ·Ɉªǭů\x88ƲΦΰǖͽɺȯҷϢȴƄȧ¼ĝȣȬ\x8fȏ',
                                                                            '`łѴϼʻ¹ѤЖК˔ĳȑʂŵƓƲ҂\u038bɳɈǋĝӡϯŲЭӠēԚΧ',
                                                                            'ǩɪϣѷƒCΉʥ˞ӡ,EƸɲȬǬř\x9aπĔъҳƛԪ\x98ˠô˾ǰĚ',
                                                                            "ΐ˴ǱǆʥʩϫjʾΚͺŉ\x90ԆưεŃѬԛԮƺϿȊɟȫī'Όοφ",
                                                                            'ʒíƸӊĲȸʨɴӅϪλͶō˱þш˒ÃԓήƟѰˡŇØˑRͷ\x97Ģ',
                                                                            'ԭ˩ŸРÃԀăƤȪͲł˥СǒíΉӚĲ¤ӨϔÄѡЁ$\u0380Җ|ò\u038b',
                                                                            'Ч@ɹΨͻѮʀΝʾ˟Ĕψ҃ɚņӎӮϒǛԆŌ\x7f\xadию˅ӻĶӟъ',
                                                                            'ȆϥȨ%ƐȭɜЪ¤ʃšÖʵДԗ®ƺňò˸\xa0ĵςϑԜɄƌȍbá',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƒDοē¢³Ýf',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȝѨÚʈǴŌбČԈΖËǩБψǁϮƄ_cȕ¸ԁ¨Ɋøί§^ɁƯ',
                                                                            '҆ʋ\x9dӭѠɡʺ˅ʶʜ\x98Ċ¿ɎɜŚЊǻĖǻƢUӳȀūɮƈ»νǣ',
                                                                            '\u0379KȳÊƻȂʠ)Łǝć\x9bԩ\x83ďʡɲѡǲӻ¹ԘΝΈ"ɓǼZȅǻ',
                                                                            'ĐϦɔʏӰӧɳȂɏɔБлL¨\u038d;ҊȇCкͺї¿˚ʺ\x8fȦɅ˒.',
                                                                            '˕HҟɣLСϩǔ\x93\x8aòG͵w^Όá˭ʉÕΆƥ˚ÅϨҗѼҊɱӡ',
                                                                            'ȊɚЈʁʳŻɉŃŘƈ0ʽƊΈд˰ƅˬ\x98лїԦҡƳŔƘˣɇfџ',
                                                                            'hΗŰƞ\x93ŧAԚϑŤɡǟʱњє;HéɛѭӁÑȡԜʨΈÜːo\x8b',
                                                                            'ʁxƀ4\xa0ŌĒдͳĒӧȤџϰҤԃ¬ѝ˻ʎНτΒtʦԧ҉ьǒͺ',
                                                                            'ƩÕѕ \x9ax҇ƌό^ʫrŸԏѣҾӍ~\u0382ΩѾȋϫ´қͷԥǓвʥ',
                                                                            'ĢʖĶ˶ΪғһTԃӁÇҩǽȓɢɃѺӿ×eГдшæśúŸӛǩϋ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѱ}ĽҏŻț<ӃϭʨЀΖӘȲˍʶɘɚӘτӑɏɨԠųǡѱԬˎȳ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 663478.549173555,
                                                    },
                                    },
                            {
                                        'name': 'õJˇΦ3ǹЀ\x93əƈŜėʝÝʭ˕',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            258434.20400359097,
                                                                            582020.0699451951,
                                                                            744352.5578987425,
                                                                            461723.85303124634,
                                                                            329608.33361071436,
                                                                            965962.0296095961,
                                                                            857332.1141235379,
                                                                            -34325.87449112399,
                                                                            742215.5760633087,
                                                                            704442.0897100663,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ЭǷɘdɣɱЇŶŎ4ϭʲ?Φ7ϒu×śуҁ$ϸεϝɲΰγҼˈ',
                    'message': '\x97ӗɂӠԍƠîƙȤɅUōÚԀ\x85ˌҽǻdʸ*Ȋàɘ¥ΊǇʬ@Ⱦ',
                    'arguments': [
                            {
                                        'name': 'åНŽҐПӐсɾʰɇ/ʶϽÙʓԠĤϵŏѧҖ«ʜʿØĄњ\x9bāŨ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ѱɬ,ÿäіѝėѦͶ¿ǞυȠͰѣk-ƊʹɖǚǠƎθԘӸԑʵŠ',
                                                                            'ˍćϴ3ԡŕ¸ΎɷŢфӰƏχӗěћǒāȯĘ¸ҥʂŻɌɽQÓ˃',
                                                                            '½ϰԍˑǦŉșĲŶ˽\x9cīǯɗσĄ¤Ҫƫ*êǞЫԬˀǁƯʲ»˕',
                                                                            'ÕΣ\x8eǛ¨Ϸ\u0379ʧŌϷяǃӍŢĻǄѕΣ!ҵ?уӉ˜ÔŵĬ˅ɖѢ',
                                                                            'αťéƨÛǰéуѱƹԗĀϙʶȞԏχЉɂԏϾԖbǬÉѻǚĞҢƖ',
                                                                            'ɒƬ\x9bÈĊ(ΟŇōщԭІǁ˝ΖǡςǸ҃ŔΝɑ¦ǆӘrœƥӅ\x98',
                                                                            'ŪӒɫКƦǃ¯ΉѡϮǈƍǃџƱłѹЂǩʲШ,ЄϡȢ˘ʶɂƩ2',
                                                                            'ˡũ¾ΙҋŁ9ҢĜɓѨԠήÜӿҢцԀǸԧˬЅƥɵԍɷ˙LŒǀ',
                                                                            'ΒӬѽǾϸȖĿԨǊ3ΥŔФ«ɄºɱҿģΐƏxǈЬĶǌɟǢңϋ',
                                                                            'ˆӛȾθӮʉɩ˅ҒјѯĔ°\x83ǖԙоãȺɒΟÆƣŸԤȢ6Ӄ\x9c\x9b',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʡÚβЍεϞВ?ƦũȟÌν¬(϶˺şçηԦΡȍѕԛN',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            9011114171393600911,
                                                                            -5950031202867855431,
                                                                            -4176936038564706213,
                                                                            1341848150238391719,
                                                                            1877099774120223684,
                                                                            -4458395887695738668,
                                                                            7139806032283566204,
                                                                            2910551662112333016,
                                                                            5235273912016976011,
                                                                            -1394685416202808844,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĩˀǨӱїʹɻʒ˞²ԙәх\x9fˆԫЂsԩâԭŧ˼xĪ´п҅ΊӁ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԓȻ˪Ȧ¯ΞЭЁSvЂȒĹÁǾǬТǣҍJϵǀΑνЂĮЊԈˆԏ',
                                                                            'īyǰȜҘǾİȊþԧ«ԏԟ\x96ǱFӨɽңΑǛLʔԀ\x98ʓԐϸѲȎ',
                                                                            'ΐƶŲɪϋɔưҏ΄ȹӻ;Íȵ˻ȏǐxȜԞоѷ¶ԀЙɕżŷƠѬ',
                                                                            'ʛęȥμƤѮϊҭщ˫ӿ҆ѓƨĥǫ\x87Ѽϐȳ¦Ѓԝ˃˫\xadɣàӺԡ',
                                                                            'ˢņ˧ɩȹʸnʚɛҿԄIΈʛѱѭЀьѼҫɓʈΥԬȿȽэʶÄ\x99',
                                                                            'ëÔжԇƶǻŸǆғϧҴÛԕɧ¶В=Ίħ{ͳɓCɂÙЉΤɺȑ`',
                                                                            'ӵѧÒԚl;ƕԥӇǂâ˂\u03a2ѩĒ\x99ƚĭČЋˮғˍΒƦÇɀȑВÞ',
                                                                            'ӡȱτ˽νӋ\x92ƴɄę϶#ĂɡςŭΐɭǖԗΙψöş#ȉäĶǅю',
                                                                            'ȪφŢЃɷ4\u0380üťýƑҵƍǬƺ\x89ȇӆӼыѓZʥӈǓԏ«ȲuϺ',
                                                                            'ɗŕԏœ\u0379˯ĭԟĘЄȉ`ȏJɇƀӅIЅȹѿǾ\x83ΛǌχǷ\u03a2Ɇȗ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǣɾƳӐғ\x9fдāщˈʑȖëúŌ˴ƞƫҜ/И',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ðѻû3ӯӆʨɃíѣ±ȴ·Z˕ˀЛҩǖϓΫqƋҮғĽɪȧËԜ',
                                                    },
                                    },
                            {
                                        'name': 'Ȱ¸ɇҞ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '¹ΡӾĠɊȶɺʦ˕ƫҋъɽ©ʘp¾˴ÀԪħѰÐѿЗāɉαʏ©',
                                                    },
                                    },
                            {
                                        'name': 'ώ\x96<Т˩ĳ˵ʾʢ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'çξҜȆӏϚƞĠʩӅɐѩϏȫӞPʢƛ˟˘%ɇΊŰ\x9eԥÿҝ˦\x85',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 349394.1628301278,
                                                    },
                                    },
                            {
                                        'name': 'Ǖϫɺ˟˴ȈͰΏΪϛɏΑƣʰʐϖѮŸԍǭһƢàǽЍīћê\u0383ӈ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ζɝ˩Īчȓȴ˭Ȩ-ΨˡΛˉɠʞӄ\x80ηʩͶΖƧ˴ӺІԩƦZΩ',
                                                    },
                                    },
                            {
                                        'name': 'ԁңąçқÎXҶјЉ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            509089.04833073274,
                                                                            917282.6225982072,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ňљŇƲӼĪǷǴԌɢÀđβƙŕӣcȥ5ˤӟʩ\u0378ӔӛɯĚϝǳȂ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȃ2ӹƳѱϔɺ3ӪSЯέ˩ǜÙӌ8ˡǾUӡǙ˨èМ°ĝGĒɌ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ˮƟɰҫíƑǻԉĈά\x8cИǍ³˝ǬÓJмʳɒҲeӾ\x80ʄȋΣ^ķ',
                    'message': "Ú#ơ΅ӖūϏǿƘҤԡ°ʵȧʻЩǔԨʡпԍϥу#'Ƈͺ˸ѲǺ",
                    'arguments': [
                            {
                                        'name': 'ОÐИӘʜ×åZЍɪĒĺͷ\x81ȥқӨŁʡѐΐĶQӛӿɅʗsЂy',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϭƟ-Ȝ|ǾȘƗҼ\u0380ѭƙñȚСśȬʿӤΖɫǚυǊΕÙґɘәЌ',
                                                    },
                                    },
                            {
                                        'name': 'ӖÙīəҎԪƂĂĬљѨ˛ѝɁƐƤӄgΒǦȿЂ\x83ǡԡ¾ȹԫŴ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5773967105345492538,
                                                    },
                                    },
                            {
                                        'name': 'ԝʽѫЦӿȁ\x97ʋɀɼɡaЩІʘơ]ƷƲ\x81˲ϸʄʓɖѸ\x9cӼʊʊ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '͵κ.ϚƳΔɅɠǾӉ΅ӂØɔģιǵ˂Ԟ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 604025.8600916669,
                                                    },
                                    },
                            {
                                        'name': 'ѲɐĠʮӋӗ»ƄҕÀьǇǖà',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƘѶȿ\x96ϵƖɿɛɋӿöȖfˢЋжŲͶõŎĮԀǧ˂ʅΪΪʏǹΖ',
                                                    },
                                    },
                            {
                                        'name': 'ÕӃɀŴ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165100.328952:+0000',
                                                                            '20210212:165100.328967:+0000',
                                                                            '20210212:165100.328975:+0000',
                                                                            '20210212:165100.328981:+0000',
                                                                            '20210212:165100.328987:+0000',
                                                                            '20210212:165100.328992:+0000',
                                                                            '20210212:165100.328998:+0000',
                                                                            '20210212:165100.329003:+0000',
                                                                            '20210212:165100.329009:+0000',
                                                                            '20210212:165100.329014:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƠǖИДWʇɺΊ\u0378әҠҧĳŸøҪ¥ʧƅϥ.ΒÎΞдғćÜͿ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8716505693261408058,
                                                                            5346916728187955129,
                                                                            -1882524672104226907,
                                                                            -4119242399840774732,
                                                                            -8542488738586766112,
                                                                            1159063113333785491,
                                                                            -5804134464142595218,
                                                                            -2368310630574143002,
                                                                            5372484764198138126,
                                                                            -2090572102612875816,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'şˬϥȃҌǗÝ3ŃŪ$ÒʤϷӭţΐǗԆϏˑʆΟɯħƚÔʕłв',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7467329655639055717,
                                                    },
                                    },
                            {
                                        'name': 'ѹоʴƀԖɵР¦ΖЫ(',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ъұԐhΗɋÑžʪeϪʱЉȎǳӠǎoϙ\u0378ϛɳϣϝΟԁĠȟŉг',
                                                    },
                                    },
                            {
                                        'name': 'ɿӸƂ˼љêΜˬǜħ&ȃɗɗБIŇqͶǲěȘwԆɠѐÚ˄Ő',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ΡвϫӷŻ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'Ȉˡ',
                    'message': 'ư',
                },
            ],

        },
    ),
]

class SystemErrorEventTest(unittest.TestCase):
    """
    Tests for SystemErrorEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SYSTEM_ERROR_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.SystemErrorEvent.parse_data(test_data)
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
        for test_name, test_data in SYSTEM_ERROR_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.SystemErrorEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SYSTEM_ERROR_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='SystemErrorEvent'),
            ),

        ),
    ),

]


SYSTEM_ERROR_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'error': {
                'identifier': 'ӘźŵʅъǬnǻҢǟǽƿŌÙӠĔɧёԂ?˜ҟЮʋЙǀʾ¬ϛĸ',
                'categories': [
                    'network',
                    'configuration',
                    'internal',
                    'file',
                    'os',
                    'configuration',
                    'configuration',
                    'network',
                ],
                'source': 'ϮƂůαϔт˨ȱľҡƯшӂĶϿҡǁˌȒӯ\x93VɖɷϣԘЅ\x93Ӑ3',
                'messages': [
                    {
                            'catalog': 'ԪћɉBʱŕǃHʁ˟ΒӖʒȠƚń·ѹƄɵЈӽτʍϳ҅ӌˣς΄',
                            'message': 'Ĺ˜ШƄ¯=ÕҙΨяаÇϻˍΪԅƥМԔ¾ЉĬӰƺɤŭɰϗuŋ',
                            'arguments': [
                                    ],
                        },
                    {
                            'catalog': 'ГȽƴӚƫЋѩʼɤѫɑȯ\x93ԅŇɕП\x8a-˟ĆğǹɫǎʁĹ\x88ǳʭ',
                            'message': 'Є\x88ĽH\x8cҺƪϟƝǶ\x9cӥưƉɰϥɫϏӞʿŬǖ\x86ʫӸĤԁǟŷɀ',
                            'arguments': [
                                        {
                                                        'name': 'ˮȑɊѼκɝ½ǡǛĬΜ@g~ǨʎӖ\x82ԒĀ\u03a2zΕªӃʕ˳ƌœ¥',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '҄ΏzçŹ΄DАʿəϾʖĄÄȡǀѳæԝ˱ѝ®ŻƔIñŤΓûÇ',
                                                                        },
                                                    },
                                        {
                                                        'name': '+ţʓȣІ΄ƃѵоń\x9eʦάʎÚțʲǎγüˍrѱΓҒӪѺŹĭɏ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЌȷƴDв°÷:ďӖ§ĉŭȎÒqȸğÇԭЫԋđфϤl*ԥeІ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165100.294923:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'јŚҴˊӴΫҭ8ԥȂξQ˫ã',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƒҗÙ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɞɑ&ϝ˕ґѭ˛ʘȻ#ȳŚҐґӡȿʅӝër\x86ӎϵ˯Ψϰàʻ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165100.295340:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Hʑԭ<ԚƋŹgʀԒˊЮңÉÙ\x8bʾʹʈ˨ҵÁʈϩТвĒɜ²å',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2307273546491843253,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʗˎˏʦâʐκғεн\x9eĸзɻļįΩʉѡŔŹǶȁɄ˜Ш¬ϮΑô',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǏȍВˠʹѫ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ô@φǺʤčңʹҼԃȷʻю\x8e˰ſäÅӍʛјҐ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '·w\u0383˕ǤšTs/ÿÁϘŧюǂƽ\x86ķʦτϲоΚ҄υԂƯѴŜì',
                            'message': 'ԫŘöìŢ˝6ϳɲΛiͲ\x8aϦʙϛΕĊʺФõӰĞǕΥơQß:Ʀ',
                            'arguments': [
                                        {
                                                        'name': 'ԃéϲ%ɤÏ\xadʋԄlѴP-ȨȲĮϖŽ¥ǗϦˮϳɲȓӉԌɽɪŢ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǏЩėYƞҩŦԓӥØǽɂ\x97ÐƢҥ҆Ä˨8ͿɓԊŧıȵåƓ«*',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǤΓԭӝɅψE=үƨÄȝФ˨˶и\\£ųɞ\x97ʱŠҹ"B˟Qʱ\x99',
                            'message': 'ZϰѪ\u0378ȧǁГȀ˭\xa0ƭмЇϒ˕ĻǧҌɜӳӀӎ˱ό˭ȴʨœωЈ',
                            'arguments': [
                                        {
                                                        'name': ']»ʷӃ˥ͰəƮиř·їҨʸ͵˃ȠƋ6',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7678241425764988880,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҝȾŇ·çǅĜô˘ƋіǜёǨǫ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʫ\u0378\x88ŊыȑΆɵ˨ХφͷʴҼͿǸ˯$ɣTӨª',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ìĮњD˚~ʦˎԆʂӈĎї@ɜ҆čãæιÑԠǟ<ѼÙ´ǍҌǶ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 703774.101362234,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȼέǶɐĦƽΘ҇҂ϝʠϻ$˗ɧ\x97ƶԡÏȫĥȔԭԢ\x98ǞԗȆŖқ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӌ\x92ǴҿpΖ\x99˦ԓũȺʪǨΒːӺ\x8eʆԔЋ˩ԤĘӴΚȝÃїλϚ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʩџєÅϯǙ¥ãʆӺԝͿҚϠԊҙ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȻˑƣиūЯΪΥǞѝʖSĒĄӴřŠůȷϥӆʍȀɾΏ͵ϮįśӚ',
                            'message': 'ШӃɎԉǜ\x8fĦͷíƟŦɉȎͽ¾˄˶ƼӅȐaȼјԚΩѐҋЉ˜í',
                            'arguments': [
                                        {
                                                        'name': '˫ɇǶ\x91ʻè4єñΪ˶Ʀ˙ǓʗèËζVÇȶѭГΜѺӞԕ\u038dͰ/',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƿϓҨѷȴϹĞԩŜďŬʯс˷Ą˙',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ё\u038bVǁ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŢŦȏǴӷΣȹˍɔϸȦʄωˀϦ҇ĈԑӉͱ¦тΡǠńЦǼ\xa0ʃN',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ξƥѢԋɶґԢõǫΐê¦ʟѿӏяc:ϨǿɌĢӴơΥĖɮǕԝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҿĤѤĕĪ˫ԊϗРŉ˚Ӎͷ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˨ҐЯů˴ӁҾҙnĥԠ˃ȡҰΑΛԇǍǖʪмıϭпԜ¾ԅмҩʒ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'HǡĺǞ҇ϞĮĕ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 259473.0480350965,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԀʵǞѪġˋĊ\u0380ȀеĊʖǈӥD˱Ћ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˞\x80ĎҒӣԘӯ®ɹǩĄĭ҈ɉÏœȸɗƃ:ϳɣҲǤƚХΪ¤&Ƞ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΨԕэѴSxÅ$Ñ˝ӿƵŅËІgҠ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ˆŻȸǎƋƣЧѫҥЫҚOηѴÁӈÐΆɭ҅ϓĘ˞ƥϱȞЩАǲǍ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʲǸ$ѐ\x8cʙ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Εϛϑ²vưʤϫεώҺê˴Ѓґɵй˜ĸĺ_iȠԅȪԑʞȀʏ4',
                            'message': 'ƝαȮơÆɯҿºŬ\x86ӷӫж\x8dyć˭Ԝǩʭόϓ϶ʐ˴ŭϔ=«Ҝ',
                            'arguments': [
                                        {
                                                        'name': 'ӡǔʬŦӀÜιЌ»ǅŎ3ЁΫȵľЍʂôàѫȏŧƆxϕŻ˯ȸɰ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 696517.1617586561,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϖƘɞӏĽɠʙҬηԢΒʐΈ6àΛ˖ӧ˂ΠǍáѷ\x97àЭǣϘǑƧ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʓǰȲQϷԤoǍȯÃźķʎʟVаƢѽ`\u038dĆєšҴĬ\x90αɫƘÊ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʸȒ¹Ԑ˚ɮσȫ\x87ʳƼƛß˅ԥó¸˛ʭ\x8eф÷˅РĞĜΓƘɊǯ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5473658652407526965,
                                                                        },
                                                    },
                                        {
                                                        'name': 'чƺľˡͰԣʀȾуɫȒTѿϵÝfèԅǮγɑӊрҬ˞~ļũєĶ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165100.299538:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҩΫҢĢĨƠʽȮ_ӅȧʾӰΩˮε˯ˏǜ\x8bηZҍҵϤΜ\x93Ӊй˶',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˴Ħɉ¨Ņ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƯŎŕĥɟΐñłʬƅɊÆʑΩΊүƴБ\x83\x9dȓ6]ί\u0383ӹǧȓϠɹ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ąѯĝʜŞʎфέʐʤʒŋýǺԧα\xa0ѓʫŸ¹ʔʀ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 432235.990506637,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɷ¨ғҟ0΅ёYÚƛɲŤԤ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɬ¯ˊɓТƽДΘϹˈß¿ĬҢȬԏєґ;ďΏ˱ÅЗÂɦƏɬϦǟ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'қΦ+бκƬϷԓǗȗʭ¾\xa0·ϤЊƝӓњȞ\x9aόÁѠÙKЛ\x85ϤƲ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ψҴԞčΑǸӮɐԡǛӻΔɟʉʿѧųɧώȿϭѽΏŧǮ\x85μϯƏľ',
                            'message': 'Űt¹żŤҽҳӡĚЙҭPӸ¢π*ɕģΟʢӒ˙ûѼƄƑͼԏ|ą',
                            'arguments': [
                                        {
                                                        'name': 'ɑéIŹ\x8b˼Ͻɑ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӑǔIïя˳˰}ƈѮˍĉҺțЫΛҟŏЁљˍ϶ѪþKŭӢ9ƛ҅',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 862741.866977059,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɺӀʖ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9dȭʶħŀʈũοțˀƩˋҴӚʼԕԦϮˮIҮǕѵä4\u038bÆ˚ѓʄ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȜӍHΚӇӄȹҺΉėƶΡωǆ˲W\x9eĔĘɬȍҌȓϷӏқ!ªпɣ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӯɫÛϿÒȥ\u0381ȋӊǱԏƷǓˇωЍЭĥїИ\x96ɂşҞȒԄђȭÜε',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'šſϟµόɠӘɐŉòЬýƪ#ǂɢƅϵÈҗζDάεŧҧѮǒAϷ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǂƑ΄ɋ7ϭ"ɮϟɚɤҕɈͳęӇèƃǩ˽ҋ@\x9eȂ¤γǕûѶȑ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʠҦ\x85¿ΫƗ\x95ǃȡʒΘΣɪŸCͱ\x97ӝWeȟƭ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165100.301834:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ъɉһɟĆųơԩǾEьӰǔˬΝŻϜСџȶЉȧíпδįŢ˯ƕʳ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˒2˃ҕǸχƸһ\x98Σŧ˩șʒĄʥĐπԛ5',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ī',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȏ˃°ʚϵϲЇưѵԂȽȦʅ',
                            'message': 's˚ĹѣÂ^.ȗJ*É©šğƳ˚ρѸĕʓǧΫ˶ÃЩӺĔ˄!Ю',
                            'arguments': [
                                        {
                                                        'name': 'ӱ¸ȻϏʛɝÉͰLЭѴJĺЧ\u0378ƳЗϩŜ˫ӤˆʧӢɛƙӾĞӟ¨',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'űǎȄαλƽ¼хξȒØƨҎ¼ɧ\x92ΓŠ¸ƆǱԎƣǰђԫѫÝԄɁ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԝò͵Л˷1ǟϢѧƙԥÙ6ǭĜUʨŔ˜Λ+ţО˄ˁý\x9aŕǚԚ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 722886.7884548849,
                                                                        },
                                                    },
                                        {
                                                        'name': '`Άʧƅɘø',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'фɭχϋwӣôƾώɏȣ҆ͲʪΰɓɀӨƵÄʹӚʒʣ®ƨϽӭ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҿ\u038dȁ˙ƑǉӒơ|ƣӣɓȀųȅЩǏ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 492514.81256521307,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ıɍ\x88ԤҦɝНĀpĞӁĚȫǲԆʅvUԠǜǙVƄɨ;ĤʺǽÐƾ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˪Ɠ\x8fʕюë¿Ɨȉˀ{żч˽ӒeѼԫɬ¸\x96ʋҒ\u0383òƻ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165100.303480:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѭʉжſòЍѢ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȖȈ\x95Ϻƫ¼ӜʛɅˀҷԣԈʗаʘ«îѓҋÂɷƴRϰ÷ҸЁ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѧΕƟŌƣǥҵȷϠФ˖ӟȩʑϫłɨčԉӫ˷ÄǑ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4926711752576452625,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҾƿȠˆŽӺǥĝѼłȦ·Ǥ|τʤ˾ʁΣ&µIҫĮňËɉʏѓƖ',
                            'message': 'ɋɶ\x95ГӅ¯ӹԄЭѢЮ}ʭ8ƿ\x85ɝȽϫκ΄ӺƮȑɼőȩ҄Ӭљ',
                            'arguments': [
                                        {
                                                        'name': 'ȹȚϙБBΕƷ«ЉɆɰˌѱƎѺÒͳ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĻΝ΅ʋơжĎ\x96ŏψɫԉˤȘĖўң»Їƞ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'į~ƮГʴϟðƻ˪ҼԨ\x97ʚ7¦ҬƚԧΐΡȋɠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165100.304556:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Dń\x8bˋˑĵƒ#źсзəϤѝŊȯƏυΤɼɛĚȾҋόɫŒ°˃ņ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '҅ņήǪеҾʃǎ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165100.304800:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԆęҮΉɄ\x7fóǗž^ŅҵϑάƖm8óçŭ˞ЗҚĎϊʔ˪ƨПE',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѥüҢ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƉѺƈʏȟƒҚȁɀRӦѼ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '҇ʓFϐŌƗ4ɳРʳ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6945976756956095030,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǥʥƐ\xa0ʍԑʝƮĹȏԆѹϒ¬ʉDWǄŝ\x99˦Ўǚ+ŔнƾȻϦƑ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ïĢӿĐґτȓȧ\x99\x7fAҊ˾\u03a2Ǵìʴřˆ΅ȻɼɭҰȟʲȇԧӫf',
                            'message': 'ҮҮƶɵҧɨƩȍЂДúԞŭÈÏ˺ɍʃđƖ¯ƟΝʙŢɺқ͵ȑʆ',
                            'arguments': [
                                        {
                                                        'name': 'Ѩїҕ˧ǋԚˑѮ)ІԅПʁύѸ¹ʁȀǞŢƩеˬƆĠҠŔ³If',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȾǲГưҢȅԙҏΗ·ˋǅʛиӖӎȉӹʕɢʜѽ?ʒΚʟԑΦȚӯ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165100.306133:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԋ0ђ˪ԆϰЗԉӝщбͻ˫бťӟ=hˌǌϳŗ˺ʴ¥ɿ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǪҏǃӠдèэɪŃ ң',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 849006.5344034281,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϯʘӏЂѐӀӎŚƺˀȜǝǏsƽΔˌVˎЄғʻǲçɨȅȉŪĚĬ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038dыѵ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԔƼԍӮúκǺ˧ǠĨξǔӷ˪<¡ɣԅĮ҈qͿĀƍȠϺûѾɦū',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'λҀƅпϷyӢɩηƚԈ˲_ѹғţ˶ϱƁƹ2ѣΪɽъЗƼˋ§Ʋ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ώ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': ';ĩ6ɬƆÝZȦĚҞř¹ȇηѬƦҗɘ,ԀǓ҅źʟЂľßӝΚǧ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'error': {
                'identifier': 'ʩсþßς',
                'categories': [
                    'internal',
                ],
                'messages': [
                    {
                            'catalog': '¯Γ',
                            'message': 'ʪ',
                        },
                ],
            },

        },
    ),
]

class UserErrorEventTest(unittest.TestCase):
    """
    Tests for UserErrorEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in USER_ERROR_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.UserErrorEvent.parse_data(test_data)
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
        for test_name, test_data in USER_ERROR_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.UserErrorEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


USER_ERROR_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='user_error', name='UserErrorEvent'),
            ),

        ),
    ),

]


USER_ERROR_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'user_error': {
                'identifier': 'ǹȔĆƱϊӌŪϗƥԝŨ\x94ßņȬǶkƄ\x82vϰžȀӪβӈơʴžǀ',
                'categories': [
                    'configuration',
                    'os',
                    'configuration',
                    'network',
                    'os',
                    'network',
                    'network',
                    'access-restriction',
                    'os',
                    'file',
                ],
                'source': 'Łǲΐ¶ԝΤԁͶ\x94ѢѳƁʵҋˋ¯Гӽҗˏʿдű˝Ƈ˅Íǎ¨\u0383',
                'messages': [
                    {
                            'catalog': "ҪʮʵюƴτедÉЧѲԡ˰Ҁѽ˻'ƢÑԒ,8°ңƺ!ÐWɠ˪",
                            'message': 'áȚńƊŦȼЧðÊʋԛѓΑяpЮɂǅƃ˲ɱМϩǤėŶŧϗHЫ',
                            'arguments': [
                                        {
                                                        'name': 'ɋѪƝϔаɬԦ¿Ħ˳Ýɒs\x8dΗѨҷĨiοȷ\u03a2ѫѼƛʃɶжԁž',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165100.331153:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŰǳѡÃʝ$ģƽŭÔƮәǛʴѻΥÆŖ¼ȄҶÆԫ˵ˇĠIёύÔ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ο˺ӭКɛʹʩğįY҇Ԏ7\x9fϚCρ(ǥȣ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -17270.24342240594,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʷũк?ǧ6ĸƯҫɇŷĮϔιҥϛ5ΧҾΣʒκåɏƔɺЗ҇ā(',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 391220.83733751066,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɔŶԜǴѝсȄӶ˦ŧʓѱ¦ҡƾУԑÿŤGɤ-¾ζˮƹ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8cǣԮ[ʕЕéҞȝɅ˪ɉϛƞӲȍÀ\x9eʗЁХ=Ύ\x97ý.ЦԅӦ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǧ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƀșƋҴàǿӑǆʠӾů',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɤčº\x8c˘Ђˇ§ƛԕǲīήї҉ѻɃоΰőґӰүɘǌêõ˂Ɩ\u038d',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '÷ʏʌҡѤўdŉ¥ȨӬ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȑÓҊƶѫқřӎѬ°ɧͽɰɾʋԭӕőȆèÇұŽӈ|ȽŮѻ:υ',
                            'message': 'ŧ˘ԮʇӪʚɗǷҷdȯǩμöŢ·ˌʏü°ǄʧѲʞƟΧöǋʖġ',
                            'arguments': [
                                        {
                                                        'name': 'ˏ±ʢǱĔʹЌΊҤѤɒȰ´©ήпƑDҸȀ\x9dŖ£ũǵĝІƝИӒ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ìԛвѭ#Ȋʥϧ÷QDϱuƘϲЮYҭǁʕ˳ˎӪʩѥƸϤќVԐ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԊКŀҡīʙϡƺ˱õìǾˑʉƙɏλӭōƌѳИǖˎfǭǙҜî҄',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ήӢƿØwʴ˽ŧӦԃ˽ǜſǄϤ\x8cͳɝЊ˚ʫɠ!ɴħʱȝȏȦē',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĶԘǂ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8135205530635123953,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8c˼ʦ\x8dʶɇ˙Ā\x8aѫòȴѤˌǻyȌԨӃӐɀǨıΓыԟВТĀȨ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '}ÇĀǑɸ\x95ʧÂҊƔӇɮϾчƁƋǐE˱ʠ%ʎȫʜʈAъΝ˒Ή',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƚ°ªӧ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϲ@\x9cɖʭƭɩԑ˹\x9bРıԋbѤŜČ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8356394565928827314,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ͱƕ˽Ʉˈƞ$ǽĜƎϾͺǘ¸5ŶʫɁюԅӒ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7496990372379712954,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӹ˸ƁCϔɇҩϫƕ·ԊĄɥȴȷʹƷWȎШЇǱΘЗkǦ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'όӲрȟɎĶʪÆΚ¹½iϩćcº\x97ǫɾɷºƀ˞ǺӐэԝ͵ƙĲ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΙҜԔǴ½ǎˆǧß\x84ԩÔόǔŎ\x85Ȼә¼ʳԃѐ΄˒ˁ˵ŏγԏȣ',
                            'message': 'ѓѤƒԊ\x8aɎ®áŰÍˎȅĦўй|ƅƣѠȳŴχӭԏ3Ѩ˔Ͻģȱ',
                            'arguments': [
                                        {
                                                        'name': 'ΏǟбѬƚȎǀŷʒԝҀĸҷļȌδǭǩҺϔ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҷӵԗѪŵҾȿƪҎѺӯԠȎρɷϳǖȟ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8dķJĐιҐȭ˒βȴʓşǛňԄтŠ˙ę˖ʜžɇ˧Ԩ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˦ǪȖȣƠϖĮсǭЅԕɔӷюԣǄ!ö\x96ϰϪɠ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɃѥһњҊӱ>˓Ѱæ\x98ċǦͳϯi$҇ΠɀɠЙѝʋӍҀÃμ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˳BϓџɢѫǗԕ¶$ćɭʅɕĀ˴˩ő\x9eƎ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΚϹԠūȑѭ!ǞϽɧэͺŃϯëҤƵ\x81ɢóĪ#ʼʆԔӺßҐԛĺ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '͵˖ʫŠ\x80˴ƭсηĊґԊЉǟhј8Ù',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҈ѫŤɮŦSûĄьǑӉҵģѣɂȂƭ\x95é\x95ДҒΞñ˟τÙƀˍӉ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʴΙ¥ȍʛƥƏѭĘXÈ\x8bӵӘ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĳŌhˎʄ4ǘͱӠЖªғɹѸԉʈяӇɬĪˍȔȮЛȹ\u038dӜɡӽD',
                            'message': 'Ðȅӹɏ\xa0nҌǩͽƗːˁɀ0ąӻʾƽɎ\u038bԢϼτūϩШɚǰӒɄ',
                            'arguments': [
                                        {
                                                        'name': 'ӜϮΩüʭНʈƠϵгѢ¥ʺ©ăωŰӧưӠѷͷЕќɦ2ŜţſĹ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΡӤ\x9böͺĊʷJɉ=Łҍ˂ȋgɄҚѸ˥ŕǮΉÏΌΤ¸',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԨǿǬˆϐљǣԕўӻѬҮ˳',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӺÂǤɑɫ½љҵEĮΉӑɀѵіɴғǹΜơʌԌʶƮʟʘσԋͶƑ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЕĢȴʎŃǴйϕBƜΫлΠцўԀΗĭԡӉęϐȥϾ¼˛ϟ\u0382`ҁ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x80ĝ϶ѺǆýɱȚӞо\x84Фˮķ¡˜и\x95ʫґǬҮïʄϙкԁȋѠ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -10987.45714851415,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϴ0ЈɁɾ?˶ˡɡĢėʣ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÛТΚɂYďҍΈ¦\x8aƂсШƣӾӜõfʪƍ\xadӿŚйǔʷ˺Ȑдӣ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'SƆÍІȊĢȲ˻ĜҚÞƒǦЄД',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԌȀǂIǗɊ[ћ;˘ƢЁ¸ҐʾΘʬŖҾ²ȶ˚ƥʐ҃ȧhб˲Ģ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĖҴˢȥƕw',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ІаԠ@źˢǖІΛȸƊũӝѿʊǍ\x81Ʈ,ϸ΄ɆHыӛβbЦòĠ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '©ʦλɈɥϾԂӬʼˊUɛč²ȿļ\\yɉӦŒȊӗȰ\x8dɚȣƛƠp',
                            'message': '҈ΦŞϺƉѳƔʽͽȻºǡǢɓʚζӈӶ\x81ҟƌӋØƻŒðVҾƥԥ',
                            'arguments': [
                                        {
                                                        'name': 'Νςϣ΅ӃĢȎŕŎΔШBԌ\x9eˠʕǤƩǙҗ·ӛз˕τН˰ĲѼŀ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'иҤҐѺϗΤˈƩƞТ/EˈȾP˅уЄƫΫҮ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԏĒ7ą¥ϏɦơɌkȾαĵќɉɑɵ˺Ǿˑʐҥ`ԝŇʄŒ6łļ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʥʺǛ\x86υћ˘ǟʊҲÙȳƳҒŃԧÞЩȣż҄Ԯ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165100.338960:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɰѷȸӭě',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Y!žʛѲʷϣˢ\xad˩УҒΜ*ŧĄʦΖʯԔДǌþǜβʶ\x86',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɪȬžĪƧ˃ԛ\u0382ԆɐÛԛ\x92\x88\x9cǂҾοԓɇĵŷʻæϧűϟЄƝε',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƁĿџԐЍϸɩΝȩΝʰʥϴŖɗ\x82ҌК\x9aͲͲýΒ6аϥƻΩʇò',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˬǴɯ˭AѡŁƻӏħǃЎŽÔΚӋūϮ˃\x92Ғԋ\x96ĭȡV',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʝɻ˯ʖɭÕӴȊӧĬɐ˳ЉӵӨEГǻ^ȇύȚ_ӔәѥδʍĺŘ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'φХΥΞĬΪ«',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ё#fӅ]û˴ͳϮȖӊͿȈÐƪ˚ŀҏxˠ»ӈΕªʝn\x80',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Äˋ˲Gӣ\u038d²ʰΒϷώìȧā',
                            'message': 'ϜúŘŔΤâϴzϘΉέӓ%Αьnˍȉϑ΅ԑИƱѴêԒιǸǟԬ',
                            'arguments': [
                                        {
                                                        'name': 'ȟχȘѿʳҝǑӻ¯aʹ\x92ӫûİ˽ϙ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˣɪчԠ҈ӻ˵ΌԍǚԊÂʆɚǗƻ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165100.340324:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŐîǷ]˃ȺƎeъÕňҵԗЬĿƈϠϼӟˬέƅԨŌԓ˙Ǣɡяć',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 462867.593278346,
                                                                        },
                                                    },
                                        {
                                                        'name': '¶ʭư˘\x95ͶƸϼϏфŖǴʁȐԕưȝȨĽӬ˙1ɴE˝ƛșÉɿ˗',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165100.340615:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӥ\x9a#ˇϼ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΞљˍĕϾʎŵÓÍÞГԪǪȵȀҸϑúЌÍЀϊӇˏԖώȇψϜ³',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǕɐʟϜѬǿѳʯ˾ʣǃ˃ðϓԡ@Y\x9fҎΦĦϔ¨ȣδvϫЭўÁ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŎѾγˣáȶȢɀǼİӫ\x92ųʍ½ºΚ\x9eʍɵɻBΕѦƿЫȀԈɖə',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƛǃĲ˭ɯњϨʏκжưįȨûйrȠƱԝқȈ\x8dΊȟІǫȎɹлй',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӄс',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '´ϟԟ҇ӛ£ҵȼ҇З\x9f',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɌԔЊΑ8ԘӒԊf5ԓɆǹϝΚŦɴʨǵѠӠņϩ|αɗĔÛłT',
                            'message': 'АԋºǜΣƔ˫ō)ɇƤƿҒ´Ñ¥TƺýӣƴE+Ѳϲ*âЏðԋ',
                            'arguments': [
                                        {
                                                        'name': 'ȑĹӦȬҟƠŪδëсӺʯ\xa0дΚɯϜǈňɜɎƟЭʤΝʋмϵǣ҅',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϦƇǭɉŊѶǯТԃɅāĹΓˏԪғъ˓ơƉʏȡýҡʣϐȘК#˜',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŀƍŕϖUǁģǜȍƉΑĦ˳bЍˢʶĹÁΈԛ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'е˙ЋѷMÙŽдYˎɠƌ5yɱԃʨΠƿΉϵ\x98\x87ˡɣĵƌҽœŖ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 127258131754458260,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԫ˰ƀ\x91ςĀˎŔӸ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʷrï',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҝɱ\x95ǰĶşÚóŀșåΘ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˭ȕӉξƫăԭ\x95Ηʓɟ ψҫЩѿӞӧ[(Ǻėˁơʃɢ\xa0Ӈ҄М',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ļхΌй\x96ɎǢ§ԎТ"\xa0пˤvǉȔҕҫҫǠŝ҈ҥȸвʡӥѥѫ',
                                                                        },
                                                    },
                                        {
                                                        'name': '[ͶDțѷь¸Ďϔ˴ϊМ¯ΪÝ~˙ӏŻźǘȰˡөȊѮåƎͱ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "¶ˎɩҭµϙʢӏӚҾˮ'фӻ˟DҼлԫʲĂ",
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΏόnǚΤӍҙǥѹrôƹưȖөҎӃȼȟӽѧҕƵɧϴюАЄxΧ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'юė8ӌȩ}ͻ˅\u0379ĐΊɿӄɒģ˶ӄмѧΧʖҺĞʧϻ%њ(Ԃʃ',
                            'message': 'ӹрѽĊɦȰęȪΛÇƹˣРʥϞЖʈεԐdԅҡƳDωџEƬǵϓ',
                            'arguments': [
                                        {
                                                        'name': 'ԘʠƵϕϹ\x80ɇȨȤͻͳЕŏ˦\x91ѭоӥ˥ʩϺƕˑ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ņʙӕ˞ѵȼЎŏԟŢԑ\x97ΖÓȚӟēϽǐʛȮ˥ĔʢйѲĖ+',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 518708.33037207054,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x94ǆʀҘәǜʘǳжΠ\u0380\u0380êӳɤɫɇʰʩѸ˺\x84Ũ7ԊӆѠ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʏҸļҘɝЮͽȪȨ˽҄ԥԀєҙ!ëчлȊȕ\x8e\x7fś\u0381ʨƗϑ\x82ü',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "'ʝ\x80ӅÓĦĘ·ʿ\u0378\x8fƐǼπʞ\x87ȺɴœɰA=ȀŀϜƇϳƸƮԨ",
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҫэɵϻ˷Β%ΧIɇɹȟШ³ǃŰ˙QĆώбљҙɗƢаѕǐɥÃ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӕʲϸϝ\x83ĪŦǵѹ\x83Џԁƒ\x81ЇӎԅƚͰɝϘǖʢȅøΉɞǧĤΆ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165100.344404:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʵȭӽѤҐʧҦɥӒȳɶ˹Ύ½\x89çяΩǨˤǭPι˨ûҎÙ/ЌĈ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'äӗƘʵҏǇÚЧƦυ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Њħ˜ğЮδ¤ʙƧ˞рșɂЖÚ˭øӠ҄ƣȬÊЮø.pϗˣ\x86Ϗ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʓ\u0382ũҠ\x92ҒƽƙԖ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǗЦԥĉҚǯɔ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϜѺҏAίɺѦ˲дŊZȏȀΪ@ƝěĩѿɨÕӟËbҡʔ˒Җưǚ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Пʌɿ\u038bǗhѾϊӚ΄ǭн',
                            'message': 'чɨ¦XĚӠǞĉƻԭǡЕñҊÇǿɩŻ»ɺǂʖіǭƄҪǐɶӀɃ',
                            'arguments': [
                                        {
                                                        'name': 'ǖƦиЩͿʄ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'С{īɮá\x9d\u0381ȇȠ҉ϴʱŪÈêºАʊCτһA˝əѮɋŔѳCɸ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѸԆʘӳψхTԄΞбΡȅƫ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 675944.3829743774,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǖŸʡ-һ@ԫӐˊɟLȼƖɹƮŻԉЫΔƒʾɱʺʨȓΩБȑȑ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǹӌ˖Âѧď҃˩ρ\x94ҜȉԊӻͱ\u0383ͻ*ӒąâԧŌЄ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƾеʞÚʒʘȞǿͿƨïţӾΊȤҁ-ˆȀĤǟ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÃŠЄΐʛîÅɟИϼК`)ȘΈκӳÅɞřĸΔ.ɇ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʋťϊ˛ʞɐA¾ҔƯξȲ*FέӱѺχιӤʉ҅ӝčȓ\x93¯ǚǓm',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӘϡԒĤKģιǎɒÍѢ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ćӍƐʤ\x95×ȔіˈϦƌӼ´ЯѺЖ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 743259.3337095906,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĵÞŶӪȫχŸĳLаԃWϐӑΝǆ\x9bχτü˩Ǜè˃ƆԒǅΐȿƿ',
                            'message': '\x9b\x8bϕȳDÐГǖÕԓ\u038bgâʰɊΛåыƼѵˤҨѪŹŝΰˈˎů΄',
                            'arguments': [
                                        {
                                                        'name': 'ɸӺƊʳķĊԬϙȖľɮα]Ǆχ˩',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԕɡ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 276355.9563169365,
                                                                        },
                                                    },
                                        {
                                                        'name': 'äeʳѻТƉϏ˩Щԕʣπ҃ǃҴȈѮƦԥ\x87ʝôƮɢҷģŷНVɝ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165100.347406:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': "ϢΔ|˃ΪϻћͲɯӐũ_ʥƨҔȏΌέ҇Φкˈ'±ћǟÏȱķƹ",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƌИˢ)ȐЧпęcσӰ˃\x8f \x7f',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ȋʶ˲6ÿąт´Ϯв˶ÕʜũΌ\x9aEʕтϚԐδѻˮΤͻϒѩGė',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ïӰˆѥsҵȓǋĹүÒ¥ԒƸȖŰW%èϩʥųșĨˉ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4526585877623425439,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƧƤϢÎљ¡ԝШӀőҩϢɺþʀõҀ¿Ǉƒ°ͺӖ˃ҥǺLÓČϖ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƘŃΑò2ԞҵкɄԧĺ\u0382ѣ˟0íѫ\x95МƼʬαíМ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƇÙʋ.șfˑʵȰ²ЧUÌǑӆϸЂŀҟÖ˟҅γ˞ƸΊӓːH;',
                                                                        },
                                                    },
                                        {
                                                        'name': '\u03a2ȩĚœɲɲѷ҆ŲåаRшѲҁѱ\u0378ѼÎζԞɽŀ¯ǉҸ\u0383øˉ ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȯsʆ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'user_error': {
                'identifier': 'Vñ©¢Ά',
                'categories': [
                    'access-restriction',
                ],
                'messages': [
                    {
                            'catalog': 'ƁE',
                            'message': 'ʘ',
                        },
                ],
            },

        },
    ),
]
