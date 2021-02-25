# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-24T16:41:17.213466+00:00

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
            '$': 'ƕPΆ4ȠƽɅ:Λɩ\x7fɞǛ˷˰ϰ˩ȎԦȪ=ɱǷ˟ёɔ[Ëǀǃ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -8042352399705962312,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 574311.0349489311,
        },
    ),

    (
        'bool',
        {
            '^': 'bool',
            '$': False,
        },
    ),

    (
        'datetime',
        {
            '^': 'datetime',
            '$': '20210224:164117.078386:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ƌ¤ťʒ# ąʪ˽ӽԉ\u0381þҦʕnϻçȓӊδЗѮƑJӜ^Ȩ˲\x9b',
                'ήОǽҼĜ\u038b±ʆʬ\xadƏ˳ȩ˃~ҭǁɉМԃǵɞ>ͽŢњԌɖʤϻ',
                '&:Ήə:ƚҜϘĉuӭϷ˩ǊɶԒϫщѮȑЗśɅ"ÅκĤÍчî',
                'ýʱͻƜӾΧг˘҄αÒȕмԥҘ˧Źѹæгӿ!ŊʋѸǸǛʯѓҪ',
                'Œ ЧDÐ\x84Δҳ˗Ȯӗ\u0382˼ћϥ˹#ŧ˃\x91Ϭīɽ\u038dӺν҆\x9eѺԎ',
                'Аķѷϒż\x87ѕЫӑεԝ\x94ƻǯǪяЍӉӅɻ\x97ʅ;ѼRŰЈƪɔ˦',
                'ƥ$ϵ˩[ҙԗʞ҈ľ®\u0380ȻεǌȈÖMŎбŖφԑ҆ǥӏˏԍˇѓ',
                'ɩӼԊ/Λǟʔλúη\x86˸МʭӛԪȯ\x95\x85ĆÆаɚţcР\x84Ҫˋϙ',
                'ЎäђŚ҄ю\x99âÜѹƐəǥ£ΏѰ°ř.ɝМőXƣɖтЏЃʷԝ',
                'Ϊ҇ȇ¸ɍþÍɈę\u0379ӡ¶ļΞ6\x7fǠʒҍјp·ȚłɎͺ\x90ǁĺӮ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -5750271458432514748,
                1662152928531359429,
                -1082525310547428175,
                -6218886176148458910,
                -4917379207437221797,
                -4176645613290212314,
                8702371801569913429,
                8442035413293131476,
                -1980816634521624494,
                -2110510226152492779,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                82709.67644285885,
                639713.1951692061,
                -61697.38779613986,
                57671.93487322767,
                778879.137267579,
                110880.783755268,
                -65790.51757760106,
                273065.85013474507,
                -27141.755087081154,
                481259.2967383993,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                True,
                False,
                True,
                False,
                False,
                True,
                False,
                False,
                True,
                False,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210224:164117.079364:+0000',
                '20210224:164117.079380:+0000',
                '20210224:164117.079387:+0000',
                '20210224:164117.079393:+0000',
                '20210224:164117.079399:+0000',
                '20210224:164117.079406:+0000',
                '20210224:164117.079412:+0000',
                '20210224:164117.079418:+0000',
                '20210224:164117.079424:+0000',
                '20210224:164117.079430:+0000',
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
            'name': 'ĶƨĀžƑͰѬȞƅʰñιшώ»ǟфϷDʊԣƋ{ŁȝĕÔƹȫϵ',
            'value': {
                '^': 'float',
                '$': 521366.93675159104,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʇ',

            'value': {
                '^': 'int_list',
                '$': [
                ],
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
            'catalog': 'ҵэǎщÎҚΫȶʑʃĿɟԔԀҞ҇ŲƅʅɇƳОÃзĥήҵîßǐ',
            'message': 'ϮөÆþ)њǰǜΓɖƶυåȞίĖʀϤҾ˾ӆΗҦӘɧϺʳϖӲɠ',
            'arguments': [
                {
                    'name': '˺s;ҰȾ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210224:164117.075986:+0000',
                                        '20210224:164117.076002:+0000',
                                        '20210224:164117.076009:+0000',
                                        '20210224:164117.076015:+0000',
                                        '20210224:164117.076021:+0000',
                                        '20210224:164117.076027:+0000',
                                        '20210224:164117.076033:+0000',
                                        '20210224:164117.076039:+0000',
                                        '20210224:164117.076045:+0000',
                                        '20210224:164117.076050:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ŶӢϿ®θȄм\u0383ɁԎǏɎԓ]γɟeʲѣоИóǴѧȈʥˬλԠҞ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210224:164117.076298:+0000',
                        },
                },
                {
                    'name': 'κı\x93ſŏ˱ʯǭ\x84ϕĒԚmУț!ЮɽĒȾȏ\u03a2ŐȞYłο˵½u',
                    'value': {
                            '^': 'int',
                            '$': 7347461620735840635,
                        },
                },
                {
                    'name': 'ɶǶζυɑƅʇӸ-˟ǔěǀϰđıêέŠҸ\x96Šȫ;ɡӦėѪʔΔ',
                    'value': {
                            '^': 'string',
                            '$': '˰ĶʅΥ(\x91˕ŸļƩɬҁ\x94ӍҴĈǔȧ˛lʮɜяʤҜtè¨\x83Ы',
                        },
                },
                {
                    'name': 'ЧųԋʔȄ:½Ŵʴԧͷҏ͵ҌϴŬ',
                    'value': {
                            '^': 'int',
                            '$': 3355175693914296229,
                        },
                },
                {
                    'name': 'λϡƵԫɆɉĴʉ´˂È8ЩƪҠЇ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'Δҹс˪ƹШ\x9aϡ\x8dѭԁÃЏˀyÈ¤',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        False,
                                        False,
                                        False,
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
                    'name': 'ʡ\x80ӯΕǔҽȈӥƵƜШĶ',
                    'value': {
                            '^': 'string',
                            '$': 'Ņ҆äԂѲѿņW\x8cpQǑ÷Ʊ҈ōƈʎɖ¸ƄтŅÉҁ\u038d:ȓǔĝ',
                        },
                },
                {
                    'name': 'ʗâŲ˓ӣɣȋǜ˩ɝëƲϏԑǻʢ\x9dŖԮíϣщΐ´Ĺ\x88ѤȿƔʬ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                    ],
                        },
                },
                {
                    'name': 'ɾӕԛūϖˇ{īыǅç',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -8158620265819252060,
                                        3612144773666406043,
                                        2419176920746227578,
                                        8658700709949536680,
                                        3830750097885475449,
                                        4297780214197308968,
                                        1028023107462438273,
                                        -4443166637651626160,
                                        5861797866019130418,
                                        8176101235437364386,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ŝ˖',

            'message': 'ν',

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
                    'catalog': 'ѴƔąʧ˲pȌɄɼŉ\x85ʇч\xa0sԮӕ|\xadԅăԟrȘΡ\x8e&ѧĭ7',
                    'message': '\x85Ӷƫȃ\x7fˏӊʫȋÕџƷŎέΏ¤ʲʳγ˜¡oǷȭʤҲѽ®šѭ',
                    'arguments': [
                            {
                                        'name': 'άΚӿˈɕӮŋЀӼɺͱƞҔɣɸςҹϽȄϴȍ^ԠҘìƐȺúǶз',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ωĄ@ñξЦʙԢ˔çHбƪŜχӀōҌΓɘ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 117632.70924538147,
                                                    },
                                    },
                            {
                                        'name': 'ʞ˦\x92ӷÙҸϏǯ¾Ɖ˴ӛȁϭ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            271216.8142409737,
                                                                            178527.32707410568,
                                                                            -26161.707005063217,
                                                                            722598.7459554008,
                                                                            -41443.145901283984,
                                                                            663925.6014068183,
                                                                            689173.0424689924,
                                                                            522586.99854411837,
                                                                            908209.0900163315,
                                                                            690640.6242275846,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ţγƈԃƛн¯ˌ҆zéӜʹɝӊʛ˷ńԝǈÅȜɋƭŔ\u038dŭҴ҄Ó',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϘèYӹǓȍοɭȾȕưьȽĜϣзӲӇôҁѲɾҿΌӢēĺÂʁΎ',
                                                                            'ʝş§[ȤԤȡȪ¿εΐӋĶιŜϰΠǳзăɅҹdҭ(рƒïЈӾ',
                                                                            'øʹéИ\x89ŸԟԆƥɜǧӳˇҢĀΕ eҙěЇĲȗȀʃԄ\x97{ґǶ',
                                                                            'ǣŃ½ʜІћëύɗƠЌҘӿɣӾӇƢǱ˨ŊƮɹƑXȹè\x95҆αЬ',
                                                                            'ʱԂ¦σȍȬʹȪÕȠҵʹΉΩԑԍǙԕdϵǶ¨ƀӮŇԧϔσÿʮ',
                                                                            'ǋϟưѱ\x9d\x92œϕöʳĂѲ#ӼŃαѢʿʩӦ˼ƞʛЋϚȟфРҙҜ',
                                                                            'ϣ}ҢĮѬťǊ©ÉɩП/ӟћ\x8cưʗԧҥʱЇĘkѦ·ÜˋĪһϳ',
                                                                            'ӊҜͼŀʋűʼǉ·ÃϕǁȄЉdǲǰӳǸǱώƤӬȘԠϲĄǊԀƙ',
                                                                            'ѱπϫҸɉБȪǀѸǤǡϐͱķԁΫʖСƑŻӎҬŝӉѸ_\x80Ĺ³Ҝ',
                                                                            '˕® řň\u03a2ЦȋЧŦ˛ÖѰιȄΦͳĖ˴Ӕ˘аʿr\x91űȮһӺɺ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0383ȖЖ+ǄҜЀ²ԝ˄űˌѴȷͲĳϛԚÒѶŶǟӁǵÆѐ\x80ǮѨѓ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '҅ˆоɿүƖԎˆ\u0381·Ś\u0383Ԅ˘ǿѤӐңȏҶҸʬҴ²J[',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȹıҜңƺʙřϤ\x92Ѩю"ʴŧɱĆÓ\x87ʮƢǧҫͻ^ȱХÄĒĥӏ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ьͽѨΰϓ\x8a\x95ζԨAːǬЀ÷ʗǳǖȯmʈʡϕШǠǙǝȅɗ Ť',
                                                    },
                                    },
                            {
                                        'name': '\u03a2лҦØſNȗɄӮĺșǡđϣѼǠΈ£΅ƣïϋ\xadȿ҉˸Њԋ\\Ό',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȅ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҕƱµȭ˕<\\|ѧЎԬ΄Ķ',
                                                                            'ϊнōɖӐˇĢ¯;Ďɛ2\x8bҜŸлʵ³ήĭ{ǝηҫǎҖ˚ƱҜǰ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ζΓʾ»ԡPˌ>ĞŘȃɨðķ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164117.053597:+0000',
                                                                            '20210224:164117.053667:+0000',
                                                                            '20210224:164117.053691:+0000',
                                                                            '20210224:164117.053714:+0000',
                                                                            '20210224:164117.053735:+0000',
                                                                            '20210224:164117.053756:+0000',
                                                                            '20210224:164117.053777:+0000',
                                                                            '20210224:164117.053797:+0000',
                                                                            '20210224:164117.053815:+0000',
                                                                            '20210224:164117.053833:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӚāԒɗϊӵҭª\x8eӝ\x90ɵÙӖҘȣӻϜľ-ΆǕ˵Ʌ͵ϝɶӕΜ²',
                    'message': 'зϴˣ\xa0ƚÌĈϤƝҼ˖ɮĥ9ȊЉǵĂǳȴӨãƊǧjР˝҃ɵģ',
                    'arguments': [
                            {
                                        'name': 'ԧԪЫЊӨѝǊЗȾĭǯŠȚúԝүϷҥѩëϟŕ]ȇƭ¤\x89ɿŒǦ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѢƢʞнǳaб3šҹ\u0381ƤȫΠÿфÖӞʛſӑĄͳΟȕοʽѹš˛',
                                                    },
                                    },
                            {
                                        'name': 'ΟĶҘɉ\x84Ϊîſ$űɆԦҏӎήāƥˍīɲɋԧĞʼǅʂȟŌĤϐ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164117.054721:+0000',
                                                                            '20210224:164117.054737:+0000',
                                                                            '20210224:164117.054744:+0000',
                                                                            '20210224:164117.054751:+0000',
                                                                            '20210224:164117.054757:+0000',
                                                                            '20210224:164117.054763:+0000',
                                                                            '20210224:164117.054769:+0000',
                                                                            '20210224:164117.054775:+0000',
                                                                            '20210224:164117.054781:+0000',
                                                                            '20210224:164117.054787:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԓƏϩũƂӤЏ¾ѭ\xa0ː',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˅ѴΑǅǨԣȭСочΎԪӺІĈӺǯ^ɰ¼\u038bʩŻҥ\u0380Нҳƃ\x80χ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 344531.5250534077,
                                                    },
                                    },
                            {
                                        'name': 'ǪѠӋφǴ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.055403:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĚӤѤϽϘϭϔ$ɊϓÂơÇƉйˎқ˦˓ɻˊҒϘȰ·џǻhѤӵ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164117.055609:+0000',
                                                                            '20210224:164117.055622:+0000',
                                                                            '20210224:164117.055631:+0000',
                                                                            '20210224:164117.055639:+0000',
                                                                            '20210224:164117.055646:+0000',
                                                                            '20210224:164117.055653:+0000',
                                                                            '20210224:164117.055659:+0000',
                                                                            '20210224:164117.055666:+0000',
                                                                            '20210224:164117.055673:+0000',
                                                                            '20210224:164117.055680:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u038dÉʜʵ˨(Ӛ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.055931:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϜЉźϿϺӜƠ˾щğϻcˤƉÍɵљƒѵŅCȋǒϐÙ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЏØ.ң\x80Ѳȿjʼ˞ʛȫ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8689803299039425930,
                                                                            -2661765758308656206,
                                                                            -1052686516320081544,
                                                                            2177913452645401442,
                                                                            -4309245018549461182,
                                                                            8915877093004305956,
                                                                            -8838004905675553231,
                                                                            5793590067988642626,
                                                                            -841096756381891682,
                                                                            -4476470553313463634,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǯïȂ\x91ͺӿʂʫβЇӸɈ\x8aȃʊʛѻŏοĂʂΛŃĆȍŉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -32750.743333822567,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ˑɺº\u0381ԨŷĦƛƞŜˍ¼ӺrӒ«ҹӨ«Υ\x83ƙѦѹϛњ˗ύϧÿ',
                    'message': 'ӳʳď°YΠ˼Ԏ)јŧӽʜʵȨѰʏɰǧƦǉїљIϑȥϹϿзΆ',
                    'arguments': [
                            {
                                        'name': 'Ԗԭa˚ƓϦǚϻ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            801580.9656661173,
                                                                            194784.2592645196,
                                                                            894726.9597816634,
                                                                            877489.0059504155,
                                                                            277136.69215287175,
                                                                            805488.7851984615,
                                                                            799598.3808220454,
                                                                            844555.5495766096,
                                                                            637328.9893540429,
                                                                            617313.1713819297,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '>ҩǮĊʹ»UКĈǁʯƏΡȢÚǶûʞл\u0379³ͽʯŜMƌŇӵҔυ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƥϠŢĠÒʧԗŵΛϙьϱѿǠЌ˨ИˢӲʣʩŇÃǉʲĨüſԅR',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 896365.0691438923,
                                                    },
                                    },
                            {
                                        'name': 'ȴδδѽԋâƇѹϕѫ5ƶ΄ʸƕµҔ«ХӧѕΧίɦºԍsɯƮÃ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            777262.8208209693,
                                                                            268015.2824464856,
                                                                            -29180.765148239312,
                                                                            593077.4119462593,
                                                                            -15047.559103498934,
                                                                            813716.655098231,
                                                                            245838.59975361562,
                                                                            -56829.33128220453,
                                                                            247242.53395083372,
                                                                            400503.60624071554,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѮÝĉőɝ¯ӄɈ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5624017337615030320,
                                                                            7041336474689100068,
                                                                            -2578216263512939194,
                                                                            -3925957719127949079,
                                                                            4976785923973285265,
                                                                            -7144920607078546866,
                                                                            6006983021998479057,
                                                                            -8418517538855511285,
                                                                            -6972199316499058138,
                                                                            8332788261558170001,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¶Ǐģʜüƈ\x88ʱξǐȞ|ǝȷƗĎāҍƶÿʘ˝ҭȕѪЭɗԒγĊ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164117.058177:+0000',
                                                                            '20210224:164117.058191:+0000',
                                                                            '20210224:164117.058199:+0000',
                                                                            '20210224:164117.058205:+0000',
                                                                            '20210224:164117.058211:+0000',
                                                                            '20210224:164117.058217:+0000',
                                                                            '20210224:164117.058223:+0000',
                                                                            '20210224:164117.058229:+0000',
                                                                            '20210224:164117.058235:+0000',
                                                                            '20210224:164117.058241:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɴԧӑʙ}˲ĊȺ?òΐ\x95ƛµ˖ӝЃҘ˪χ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8360863220578366127,
                                                    },
                                    },
                            {
                                        'name': 'ϔɺγȵ´',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 307418.3591143115,
                                                    },
                                    },
                            {
                                        'name': 'ѼĪЪќʃƻѪdКɴԁɘ˂2ȠСϤѼұӦӍ\u0380ҥϼŋҚέŖ%Ғ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164117.058731:+0000',
                                                                            '20210224:164117.058744:+0000',
                                                                            '20210224:164117.058751:+0000',
                                                                            '20210224:164117.058758:+0000',
                                                                            '20210224:164117.058764:+0000',
                                                                            '20210224:164117.058770:+0000',
                                                                            '20210224:164117.058776:+0000',
                                                                            '20210224:164117.058782:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĲϽӏǩһʘһʵɣ\x95É˕ãЖѐцşρЖϑʅř?Q¿ҾmÜʽβ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'þȉθБϤϣϙĔϦűțϕѰңȮěΧԈѯŁӐ´НΟʠ´¨Чʤƅ',
                    'message': '\u0379ƢſƔӫɸď΄ʥ\u0381ŸʥǧҖ\x81-áĔßuģϿРҹӂ҂,ԧɪ}',
                    'arguments': [
                            {
                                        'name': 'ˎŀͼΑʠЯɥѼϙÀˉŚ΅˟ѹƜʏӓ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǦĴ%´ʼȐǾɑfϑҽÀз£Σѹщ\x96\u0378Άʯ\u038düĮіÇΨʡȯQ',
                                                    },
                                    },
                            {
                                        'name': 'ҏ=ŝƴƦ˵ύпѸιÍЏ]эƣŲ|қƧ\x81ƥӠ˄ǲАŘɓҀўө',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            718459.2480920082,
                                                                            942711.2071987474,
                                                                            264172.3600324646,
                                                                            -81063.0878980457,
                                                                            467235.5962624487,
                                                                            827282.089056547,
                                                                            346787.5899733267,
                                                                            203557.45903210505,
                                                                            798813.8474396581,
                                                                            609441.6599326438,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΘʎѨƁķǈΔƨȓӤӏ¨ÝȔҺсș˝jÝȫE¡ӇɎЫѴÙʽʈ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -55498.30342360208,
                                                    },
                                    },
                            {
                                        'name': 'ɕŭǓȞ¼ӒҮ˽(ÜˢȏĸԁāȆrӥʦȥȬʢ˰ԑǎǱŢʔԛӵ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 493301.3852328304,
                                                    },
                                    },
                            {
                                        'name': '¾йǢq®νӓȽң˝έƴĺ8ϹԅяƹNԕҌԦмΘԇ·҂Î[Ƹ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2876440394328680814,
                                                    },
                                    },
                            {
                                        'name': 'ͱϲΜƕ\x92Ӱˉ¥ɚЬΗсҖˌόԪkѯѢӌӭϋөϘLɆŴϓѫ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7235429505659247263,
                                                                            1201939839051211340,
                                                                            -6567535367322125219,
                                                                            -7444968216612776099,
                                                                            -2920919685780325324,
                                                                            -3767632899544958312,
                                                                            -904930619563855946,
                                                                            3666982166363495751,
                                                                            -1200898510801278930,
                                                                            -7548575101330558170,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʂ˳ʖİɽӥąϻ@ȌȅҾоΠ\x93œĮĸ\u0380ΟΐыбĹħòԑоʜΤ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5382656548430149072,
                                                                            -5990147361067807952,
                                                                            -1251586051941306181,
                                                                            3705950000200464103,
                                                                            -244651700148866480,
                                                                            -7481835791210988823,
                                                                            7645917335350439960,
                                                                            2303757221392252442,
                                                                            -7381425208938781291,
                                                                            6273267079451495718,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'dȮƓϏƂіɕЀŮ^ѻ5UΎУǲƯȺƺэˮȋʴӨπƊȧƏ\x84Ű',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƠVǛӳŔØɡĺҢѻ҄˥Ƴˍ]ωҷԡɱʹСȈr`ӿŊҎƠӜ\x84',
                                                    },
                                    },
                            {
                                        'name': 'Zȗ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԚǭĦϞ3ðԄñʦϊςÂʘ\x9dĒǝ˶NĲϡ±ҟǼˑ¢ũӮӸ[ė',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѕȂ˟ЖŏԠό˻ҢɱƐžβâͿɚơʺγʱĆǸɽȧμ6щǲԤʫ',
                    'message': 'ԃɸìкӟźԨģŰʉɐʔͺӹůˉз}ĎŮҧ˙οĆźφħȔɼˤ',
                    'arguments': [
                            {
                                        'name': 'ɩ?GȘ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ѧ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȍӣĦɈͿɩŀʿĿӮӛȴ҄ȋϕƆŦAɠŷȭĦƩ\xad˘\x8bǕǷźɋ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'оќìɞҖđ҇ȉưҧϥFάҵϊϺňʢɳƆǔʀÞÐʖˎ',
                    'message': 'µСS҆ȃŧϻŵɻӐĂ\x84ѷТΪȳӸ\u0382Ǆæ\xadԗƫʴǄͼ\x91Úȓˑ',
                    'arguments': [
                            {
                                        'name': 'ɗÏ»zыǙϳϯ\x81ѳěʖf©ǬђԔßȺјɫ\x88)\x8cж\u0378˜Ũѐ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164117.062130:+0000',
                                                                            '20210224:164117.062146:+0000',
                                                                            '20210224:164117.062154:+0000',
                                                                            '20210224:164117.062161:+0000',
                                                                            '20210224:164117.062167:+0000',
                                                                            '20210224:164117.062173:+0000',
                                                                            '20210224:164117.062179:+0000',
                                                                            '20210224:164117.062185:+0000',
                                                                            '20210224:164117.062191:+0000',
                                                                            '20210224:164117.062197:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '/\u0378ɵͰɴǻӗдşѷßǠϸHȘӕǃԧѨìQͺϓ³ɿÑ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 147941.99447928974,
                                                    },
                                    },
                            {
                                        'name': 'ЉƎǏɒ[ӳζŌƊφ@êɮPǹ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -26555.36446805256,
                                                    },
                                    },
                            {
                                        'name': 'ȴǵπøϪԫƙnĒÆўϔŹƤƅԋ1ƅϲԥʡҤѫһ\u03a2',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.062697:+0000',
                                                    },
                                    },
                            {
                                        'name': 'д\u0380ºųΰԪ¦љ҂iʊ®4ґVˑӶ҅˫ľңÉɝɤȲ/ȁκuĞ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 469770.3805879742,
                                                    },
                                    },
                            {
                                        'name': 'ľЅȽŪăĆʴН,ƆȭӃħ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2162668406390604676,
                                                    },
                                    },
                            {
                                        'name': 'Ѿ±ϼyOοǞτγʼʅмљˬȋό:ʼµʼʄâ˄ĈӪʆϠĤĭʧ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ċ\x7fЎƍȽ\x93ԀȮӑӾǡϴаϭŌԬњˎ\x8bӸώДÝу1\x99ЊɠƱĩ',
                                                    },
                                    },
                            {
                                        'name': 'ØĹɷҭё\x9cͽŵǀɯ˲ƯȲ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            342709.9906464201,
                                                                            858693.518472757,
                                                                            967085.7102740221,
                                                                            46196.45147407628,
                                                                            986252.5763175953,
                                                                            288203.72906090895,
                                                                            369213.9058158461,
                                                                            367649.3288462178,
                                                                            648098.0448352006,
                                                                            310402.8820558059,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӟϾЅ˔Ńҙ*ǫÀϞ\x89žЁɱѰΤ\u0378ǵɫĐɗŬύϠП',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2127297042328413161,
                                                                            -8274762656881793513,
                                                                            -7849040492997010860,
                                                                            -5009446193007494265,
                                                                            -906740080817442208,
                                                                            4686622451716205955,
                                                                            2327089008016590136,
                                                                            4015660144133325733,
                                                                            -5474759285393673738,
                                                                            -3149846888704432644,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȦƕʬȗӽϮ˧Ƀ\x9cѭͰĦўԕȕӱđϽѬȞΛŻĻгӍѐˀϨǇɃ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.063864:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ͳǶл¸ƭǇ\x98ȔʝéɏɭǕɢͷIɧӡўҼҺɹǘ~Ѕԫ\x80ϧѤƻ',
                    'message': 'ŹŧǹǙЧɥѽǜŮʩкҀ˓ѺʇʊѢνѿГӑТʆúγϸEEҨ\x8b',
                    'arguments': [
                            {
                                        'name': 'xȻˇƩŬɢѦɚʸÇιę\x91ƏšõҐ½Uы$\x9eƞěЙ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 498376.3798382338,
                                                    },
                                    },
                            {
                                        'name': '¨ʆǴǅǌʒƌϧûǝʨЃD<Żϟd˟ſǪѧʟsґԔȴvǗA˘',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.065093:+0000',
                                                    },
                                    },
                            {
                                        'name': 'H%³¸ćˀѨʷƋϚ*ĄͱÐŏӡǸąPʎ¿\u0379ÖǶӖǍYЩ\x9cŴ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'д\x85ЛòɓѧŴǧǠǩșȖBɜԛʰȘʫɈʯҵҞͰϺʒ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.065411:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ͱŻ\x96Т\x9fϩҩԌ±ŕӀϔˏʷ\x92Nȡʵː˗=ңʣ˜{ëŸϿNŁ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŪоΈɤӬúo¤żǥϰG˧ғĹəɅҕŝ<ŇȻԩ&İҵǕpƙͲ',
                                                                            'ҹҽЕκǫβ.ȵ˼ʴơʭ˳ЌԚMȘȥȐϸЭȸŃŵɼөǀļ\x87Γ',
                                                                            'ӮӂťяǡҍȌŔԎԥęʮɍґšˑɲĈĽŒ˝ѦӲвψяYÕ¶Á',
                                                                            'ʛĺ\x8așѶēиÌʩǵȩԪϲɦϣɥʡ\x88ϲӜòԇ˂ǋӿ\u0380Ґҿ»ʋ',
                                                                            'C)éΕǪҫԏGȏΛȳɥaCóWϧñǚѧ§ȻԚĶǄǾϼѮǨƬ',
                                                                            'ņŉơǈȬ\x91ǩїԅHφëzӝǰƼȀbɋÁ˥ǯĤɇɲȰʕм\x9cҪ',
                                                                            'Ňԩǐʂ>\x95ÿо\x83ǏǈĘΰЖёĥȯ\u038b˝ǔΑÎԌќϩŨǚPr<',
                                                                            'ĉĦҴӤÿғɺд{ЈŜÃǿσ2¹ėɅưāйʴӺwΥӡˁѰȅ˟',
                                                                            'έѾʢʲϞˈǌԌĈϞɁώМɾɸѢűКӲΖũӦѯSШѪȻӇōƏ',
                                                                            'ɮϙɝ\x83щxˣћˀнKΩȨDɄщǹʷӷʿŅԆƈҞф˘ұ?љͽ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŝΠɉҭӂƈɶ»ήŋÝÒзɟʨΒԦhʏřǮËґНƸ8ƣɹѹŹ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ԗ\x92ĩ¨ÅԒʉȜġӞEӀýΟ˝¨\x8bdԊЎЗ˾ĹќĒʞЩϼǯu',
                                                                            'BуҮȕԀɕˋӨӏʢȽcӕ\x89ʧȯɾ\x9aԇɏǚgӴԚĨјļǸϩÃ',
                                                                            'ZӓǚǌΐGˡƞʷčœѻӞ҂Ĺ¤ѫԆͱ)˘Ȅ}ƯǼʦvÍѢҳ',
                                                                            'ǗϟΔ§ͿóɎ-ĹșӔȾɍ#ϖđɫǹҳ;~ɠӋ˙ѵțПāĿÙ',
                                                                            'ԔӧĬ˚ϕʥŖȴүğǁԕĜӕþMҹϲÏǃıӢȊŻҁȘȈΛʙʿ',
                                                                            'ϡǄεԋ\x8fˍśъſɊÝZӖЮǼ®ӆƿɱƬҽ\x81ԭoԊƋœƷŢР',
                                                                            'ƤԔΓˮüɕ\x84ņ˪\u0381Ƒʘ*æɣsŶ˙ǿ¬ɻ|Ŧcˑ_ǥǞɇo',
                                                                            '\x8fсıǑĨΐϷӇɽÒʛêʆͷʀ;ʆǿӦɾϕ\x85ýԪԚЇѭ¿˴φ',
                                                                            'Ƞή\x81*nȊ˰ʥΒ˰φǲԐԤϏÂԙăΊ\x97ƒəѡϥѱЗǘЁԡҵ',
                                                                            'ÀYʗЖĞГԃuѿԡ˧ʁˌòSġvyƣGӄЫ\\ѳǔԉ°ʊӫ\x99',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȇштεȡʶ\x82ǟʦžШƘȿuǔȦśÁƦɧņԄ\x83ͷĲ!ϨűÀҴ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ԗ*ӔӪӵƛГʈʿӚα\x8făÔϭ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѱұјҫŽěƗ\x9cȵӇǂҲ\x96ҡĨԂÕʸǄǶ*\x97ӨƻʙřҿӲˡŹ',
                                                                            'ҕˆȁϻ¢ɧǻϧΟԝӭґȅǖȜѻŐãȰǒƟ˼Ӽǆ˲ŬͲÉҾπ',
                                                                            'ԧɍːǳǨԞϼτʃΟī§ɷ¯dЀψЬѓнԔϿ9ΦϝЬǯʾÐт',
                                                                            'ҟ\x8d˥ƚɆ|ű\x9dǐHɦŖκɤвθʍɶŕʨПĚƯϊ҇ЧѓѧƲϕ',
                                                                            "χȟȑƅӵıѪ}ΏԔʭȡ\u03a2˄ȨγbǙЫҧƀ\xad˂ŜУӺ'ӂķƦ",
                                                                            'ɱX\x8dŴүӆ˙TύęȆť´ԉ҈ԚΏњÔτϞӣęϔm¼ŉǝƠǞ',
                                                                            'ϐČΈщśɨΫnȬȭԛʙɠəȒƜÑĵķÝψͻµĨѾʮсҲњƤ',
                                                                            'ɺ΅ӊĝϧѥǴ{žӹ΅ҮΤĲɷлaқѷϳʇÝѢĩǚҼϒфƖ\x99',
                                                                            'Ǟʤȩқ§˴ϮϨüҚĂÎʗʠǊ\x9dĹԔӹȞªǽȏ~Àкƀǻʙɳ',
                                                                            'āĴͳьЪ҈"Ȼȏ¾ŻеÛȅΐдͰǂԍѴǊǌ¨ƴ\u038dӴAȔΆѷ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʳñʱΊʭ¿ŶЈ˦˕ǬЏҫʒ*\x9dϒϴűȆÂмðĸZлʱŻǒǩ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            235983.04367839248,
                                                                            -55455.62694295828,
                                                                            -64869.86713234335,
                                                                            769106.3373170984,
                                                                            764317.2113507581,
                                                                            231766.0238604854,
                                                                            512375.76332659845,
                                                                            87855.80144431029,
                                                                            552872.8807272373,
                                                                            -33722.71278679934,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΌԫîˣԙͰҌǇ˅ʑҜYřǯCеˣԦǅȐΤү¾ʕΝɂ¬ɽĎʨ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ɉ¾ˊέΦҒɖΪиĢòÆғĕζf±Ȁéӆȫԋ\x84О\xa0МҷµGȗ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "ŢȉɀÒϹǮњχ'ʉČ\x7fǉĳĎ҇«ҕ\x84EҮǙЎ\x8f=Ĭĺ÷зʲ",
                    'message': "Ѓ˱ȏŤďӹȇˍцʴɃԃϠʹɗǵëˢŖϓǦɧ'ũ҇w\u038d£ҐƢ",
                    'arguments': [
                            {
                                        'name': '˖q»ͱӯ!Q°в',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.067736:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʼʖԩˌɜËǥĚȻŇȗ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʯġ¶ɎΧΗµÜѠìǳ\x92¬çҪѱϴÝȈ\x99ͳЭǫÀϫ˝\x83ȏ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164117.068144:+0000',
                                                                            '20210224:164117.068157:+0000',
                                                                            '20210224:164117.068165:+0000',
                                                                            '20210224:164117.068172:+0000',
                                                                            '20210224:164117.068178:+0000',
                                                                            '20210224:164117.068184:+0000',
                                                                            '20210224:164117.068190:+0000',
                                                                            '20210224:164117.068196:+0000',
                                                                            '20210224:164117.068201:+0000',
                                                                            '20210224:164117.068207:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѨęґȬǍѝɑҲȗ\x89ņȎҥӽѯÙҼӗӾşѵ@цŜӱȸȻɓįϴ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164117.068452:+0000',
                                                                            '20210224:164117.068463:+0000',
                                                                            '20210224:164117.068470:+0000',
                                                                            '20210224:164117.068476:+0000',
                                                                            '20210224:164117.068482:+0000',
                                                                            '20210224:164117.068488:+0000',
                                                                            '20210224:164117.068494:+0000',
                                                                            '20210224:164117.068500:+0000',
                                                                            '20210224:164117.068505:+0000',
                                                                            '20210224:164117.068511:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '7ӝɎШÈԟrȌϠъ\x82ӖЉӺˆǃӱ8ҦҤҖӂǊԘӻ[˻ÊɌų',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ԣ˲ΊǄҡeҪќbԢӨǃĺ˒ǔǄUȐɵ҆čĮԀʥΞ˃ÚҰ\x91W',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȀΰÆӬβҸĲѥӌǥù',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
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
                            {
                                        'name': 'ԋǗɽƣȭӀʞӀˢˣǻ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƅˆʧɲʙǬůύşЇɜш9ϦȄʳı˳ǻѝȷ\x84ȓ\x9eÍȈҏʈȡџ',
                                                                            'ҹЯψӃɬЗU¸Ӏʗĩʮ1ûɓɓěƲʘ˝ǲϮĪӊɏǵʍӹǠЏ',
                                                                            'Ʌǹѹɀԋ¾ǱKНʌйőЦ΄ԕƩҥLӼг\u0381ӰΩҕӱ˼1РȰɾ',
                                                                            'ɑËσ\x9bΩiƔ@ҌӢƚҊϝőΓħĀσϳʢġƍԬÎĆ\u0383Э@ԂX',
                                                                            'ҧęҰpӺѝѨȟ&ʢH\x8dҰϏǲӼӍЌ8ҪʛƇӻђɤʢϾҘш˵',
                                                                            'EƩϩʴҔӦЋȇ˲ϴúǍǧЍϼүʹ˸ȅΘŢˎѫɬëсӊɭҒʓ',
                                                                            'ɮǠˏüιˈϣŋĶӧӯѰѭҸɢË\x8cϵɮßʄřӅ)Wýȯǯȑʃ',
                                                                            'ȕ\u0383ΣōӔҥΆŉŭѩƲҡȚǹƬҚQưQɋԎʒѭҦɔƘǨ¬ˤӸ',
                                                                            'нѧѻӺӍŉЂҡˍÝъ˕Ã˚Р\x92ѷΫԢτǞ2?ĆɫЁĻϹЫ˞',
                                                                            'Ķ§˕Ď§϶¤ƔʻȈͲĔ+ĕОҭɀύ\xa0Ā»\x87˪ϔ0\u0382ҘƿɎa',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȁΓȇΓǵļ\x93Њˢ\x84Ӗɴ˯ņÍbϲԀϻȥnͶÔƪūÖ˝Н;Ò',
                    'message': '»Ȁύùċʤɤɦ·ˎ҂Ϥ/ёǮҹϼ˛ƜìΆѤ\xadŁȑрΝέуˈ',
                    'arguments': [
                            {
                                        'name': 'ĠɅҠЭɼŋдЧǹđŞʴ\x92ΗȊĺԊƌÝ˨ǈӄÎÞĒҿφʒ)ц',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 29872.303849892807,
                                                    },
                                    },
                            {
                                        'name': 'ϓūӴ(ҍŘԄ¤ĠƂϩϥϾˁÊͽ×˝',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6220900328003646187,
                                                    },
                                    },
                            {
                                        'name': '\x95ӳҺ˯ԃ˹Ъʆğǯ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8317452975790401451,
                                                    },
                                    },
                            {
                                        'name': 'Ɇ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ͿӅȺΞÔћԭȘ+ϚõƉ\u0380ɎѣǚɠѥӒѻ§ЎˑǦъ\x99Ŧԭï^',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            94589.19114664485,
                                                                            835459.1710871394,
                                                                            966963.3222113533,
                                                                            -57054.19030674432,
                                                                            178523.72127083945,
                                                                            334385.7303007834,
                                                                            -80180.05524951119,
                                                                            17096.541957411,
                                                                            593161.0460151306,
                                                                            253455.68976491998,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˓Ƭӳц˽\x81ӘŃʊωҏ˦Ȑʚԥ>Ҿɉ˙һʌ\u0379ϦҶ{ʣâф¥ʜ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5045076648039088272,
                                                                            6845606595065503988,
                                                                            -6209939299017287166,
                                                                            -1781139581032979300,
                                                                            -6611359978502700943,
                                                                            4530838217605733812,
                                                                            7342803675754261305,
                                                                            3658344597033404384,
                                                                            3488854583710883364,
                                                                            -8463430875583771875,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƜƿіϨүϵ΅ČéɓΏɵÅ\x83ύϩζӮӄƿʿѸӰΎϕхŌ«ζә',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȡĤĒ˕Ӯʷ\x86gһΌŭǰ˘ɯǛÝәүЫˍϰNӹμѕƒ˚ǜƈҥ',
                                                    },
                                    },
                            {
                                        'name': "КўɰԚ˕ЏӶʹΥµӥʺҗˢ҄ќԮ'Đŕæ?łȀ˴",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6690012170038269049,
                                                                            -4264948341233765485,
                                                                            6105478306998254542,
                                                                            -4096639001028724833,
                                                                            -7660743316841265478,
                                                                            -1946568024598347184,
                                                                            803535648159520779,
                                                                            -5961013136570023003,
                                                                            5842220968514538809,
                                                                            -3431187033828646404,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǋ@˾˅ϿԦŖ_ɋ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԟŹҗϐ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164117.071806:+0000',
                                                                            '20210224:164117.071823:+0000',
                                                                            '20210224:164117.071831:+0000',
                                                                            '20210224:164117.071837:+0000',
                                                                            '20210224:164117.071843:+0000',
                                                                            '20210224:164117.071848:+0000',
                                                                            '20210224:164117.071854:+0000',
                                                                            '20210224:164117.071860:+0000',
                                                                            '20210224:164117.071866:+0000',
                                                                            '20210224:164117.071871:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '҃ƶǉɱҙİͲ®өāĜ\x86ʊŽϲʀÏԅ5Ӱ·ӣ¬Êɤʔ[Ӊԃª',
                    'message': 'ȌʰϸǁʗТš϶\x84ȡҌ˴Ϟϑ\x94\u0378чɋǕєƽΏź˼Ο˝ŠÝӗϜ',
                    'arguments': [
                            {
                                        'name': 'ǉӘ˔ȸ\x89ţȱìr\x94ϳͿʧжɼȃÁӡъͶ\x9bɋǶɩԇɘδʵҹ¦',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǤğҩӥǉƜɢѳ=§ƹ¦\u0378ʏӄȫѓјӸζȩӴʻώèſʆх\xad҄',
                                                    },
                                    },
                            {
                                        'name': 'ѥІǜӲӌњҿӢĬԞ\x98Ю<пˉâϑŴ˴ˤsÆɟ\x8bÛǌòǔԮί',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3185792226532406560,
                                                                            2448073015312158983,
                                                                            -1682464482772794228,
                                                                            -936365938446736760,
                                                                            -8445963726327831606,
                                                                            -7720758970634696827,
                                                                            8244692401506524183,
                                                                            -3551385669062910606,
                                                                            -1469933870742223130,
                                                                            7192013058398636906,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԊɈôӖπɑӹkÕЃʽϮΤѕɎȵȃԎԈϿʄпȵԧŻҕqǿϛ¸',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164117.072827:+0000',
                                                                            '20210224:164117.072841:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ќφƵҫǵіÿɤϖ¸ɯǐǞ\x7fˏǼұVǃ\u03a2Øȩɫϱ҆αԓҽϯҩ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            196675.50969422853,
                                                                            835889.1244915308,
                                                                            935308.938601311,
                                                                            455399.9678659595,
                                                                            -28698.039100080292,
                                                                            304408.0684131345,
                                                                            593452.6393404744,
                                                                            249313.2409726574,
                                                                            321847.1837999385,
                                                                            530452.8441302005,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'bƛΒ˚±ϘɸzǸː6ΒĘҔͺ¡ϔϵʇ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164117.073289:+0000',
                                                                            '20210224:164117.073302:+0000',
                                                                            '20210224:164117.073309:+0000',
                                                                            '20210224:164117.073316:+0000',
                                                                            '20210224:164117.073322:+0000',
                                                                            '20210224:164117.073328:+0000',
                                                                            '20210224:164117.073333:+0000',
                                                                            '20210224:164117.073339:+0000',
                                                                            '20210224:164117.073345:+0000',
                                                                            '20210224:164117.073351:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǍʾɒʩϹҾҕɊΦ\u03a2иįңǺĨʙΛö\x8cԣɑȳЃҢӰʺӄ³˒ƹ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3559961004389468550,
                                                                            2052139367381277315,
                                                                            -587368266721436993,
                                                                            3197132123802982772,
                                                                            -7601242110157637646,
                                                                            8801053812005483562,
                                                                            7430529566442360854,
                                                                            6237012198486181859,
                                                                            4021795245499814293,
                                                                            -1392753916855339080,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˧аɖоԫȬýʋǔȐȼĦϵίĆ\x8bѮԄʒƴǢāɾǥçΕôѤưҨ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 980856.7930894806,
                                                    },
                                    },
                            {
                                        'name': 'Ζ˕ĽŅ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѦİʁЂɹΠZǰÕΖŨѣøύƨ˓ȝ\x8d˱\u0380˘ΉΊђă¥ơȮƄ:',
                                                                            'ӖoǐΗȱŵʑ͵ΡͱЎѸĵĐҧi>ĩΛȍǩƗԢǧӀԊцɡϘÈ',
                                                                            'ťȓ҃ƐΧǘhCƅnĵ&ҶӍÞȀϷȇɴɐȴɜÔӋˏ\x9bǵ¤ņ˙',
                                                                            'ϊƴԜќÁӀрåώƇӢ\u0381ȶƜϲĦʷѽôͳ1ͷӎЊЧǽɶ7ϥǋ',
                                                                            'Ӆpȝȷĳώέ˛\x95ŠŰԬøѭϲș˛ѿȊĐΕĨŜʉԜǢӔēъЉ',
                                                                            'ǊĤé\x99ϭˉӰӂӂȤԚÓԍãaД¾ϳӊӨҙκˏśйЇLǟ$˼',
                                                                            'ľпȡ˟СśǰΙƕǉнВюȢ\x8cґǼƧÆҽӮ˫ÔʨѓпͺΏ%Ħ',
                                                                            'ęUěêοʈ\u0381қʲ>˴ʻҢʮȚƪϛWɊɩҊЗɼʌ°ФʧǆӲ*',
                                                                            'ѫʸώžˮʔћԖϐҬѹʻҞҪͲ·ĩǮǖѪ\x9fʊťԠsҹS\x7fħԠ',
                                                                            'ĺǭӂư\x98ǼѷƩ\x8dǠ`ϓ.ɎԘΗэԂΩ¢Ǔˋ÷Хï¸ĬȔƀȜ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ðŒʱxĚϲœʰ\u03a2ȓʎԫ[ƉƉҲúhĮӣș\u0382ÄԉӃιΞӱïÊ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.074390:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ώëҟșԬσ҈ǟӷҀÐOŵ>\x9bԙѹɢҔχƷҘîŘӨµƤҼȂȰ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            941624.8819437508,
                                                                            502811.4680043387,
                                                                            81108.2820394581,
                                                                            -42372.00126561204,
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
                    'catalog': 'ȿš',
                    'message': 'ř',
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
            'identifier': 'ЙΑLЌƸȝĢҝˎéǬǕΌɢƭ:ʣqҳȼɤŅиĪɵɵȍҚƲɊ',
            'categories': [
                'network',
                'os',
                'internal',
                'file',
                'file',
                'internal',
                'access-restriction',
                'network',
                'network',
                'invalid-user-action',
            ],
            'source': 'ȯΜ˖ӵŁȑɛlʫǋχӾѥЩÔ҃ǀʬɞÈͶÉŹɕņȿѳȰϨȼ',
            'messages': [
                {
                    'catalog': '˰\u03a2Ńϲѡüˮз҄ԍê˅ʯƢdҔ¸ĘǼӰ÷ǳlΰΪѝϭφ\x82ϋ',
                    'message': 'ͼϔAʘ ·ƀȅǘҷwӖɰÀĖÇǎɕӉӧӵԂ¥ɢдЫԝʷǑв',
                    'arguments': [
                            {
                                        'name': 'ϹĴ]\x9aĞҀɴŬ˪Ҭĺ˪Ģ¸ŤҷϴϔƦ\x95ĂΞΘóÑѩФĿыЯ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4468838545871896734,
                                                                            2383545486286210350,
                                                                            -7120067373921669206,
                                                                            6821447646906427381,
                                                                            -8444738215761873940,
                                                                            -49512867051998159,
                                                                            -6293009265987258892,
                                                                            -9113301232138708158,
                                                                            2635223549402852332,
                                                                            5161322890111206754,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ђ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            144985.10392028876,
                                                                            844336.2100448083,
                                                                            326724.1468635156,
                                                                            301860.3798406975,
                                                                            938441.081605139,
                                                                            -53956.08841139723,
                                                                            390554.7110898584,
                                                                            610911.2370200156,
                                                                            912623.5794489483,
                                                                            631509.6991246537,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʈ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.101809:+0000',
                                                    },
                                    },
                            {
                                        'name': '«Įē«Ԯ0ϧÌāćmʷӚ¦Ǖ\x85љrėԨо½˴\x97˗ɰҰсМn',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '{ɸȕ˘˴ʇȌϾ˻³ѺĉʄĊͻȧѸ|νŏԮǿŘѰϥǵƊЕΒ~',
                                                    },
                                    },
                            {
                                        'name': 'ϓеϪџԭ\x91ʓӺŐӉњ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȼѸ1ƵŷìʬӊȔAф4К9ǫ҈ӔӂpҷԠĬʑŉ҃Ŕɦ˸Ɩǋ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1323408698447770269,
                                                                            -4757469447450641155,
                                                                            -8420622618877618604,
                                                                            527118431415676723,
                                                                            7661987138084987952,
                                                                            -6076240508881539751,
                                                                            -4478967235900089069,
                                                                            -5325567561811295198,
                                                                            3598535007861591519,
                                                                            -8506778712969503305,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ńӛȹт³ňσBʦϗæĠԟԊÞ˷uƋJѢёńʻɦ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164117.102464:+0000',
                                                                            '20210224:164117.102477:+0000',
                                                                            '20210224:164117.102484:+0000',
                                                                            '20210224:164117.102490:+0000',
                                                                            '20210224:164117.102496:+0000',
                                                                            '20210224:164117.102502:+0000',
                                                                            '20210224:164117.102507:+0000',
                                                                            '20210224:164117.102513:+0000',
                                                                            '20210224:164117.102518:+0000',
                                                                            '20210224:164117.102524:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'wйӒԄƪ6ü˫ʹѯ˃˲îɒ3ȑɃĎŔɴφʳѺʸӍʊȠ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164117.102753:+0000',
                                                                            '20210224:164117.102764:+0000',
                                                                            '20210224:164117.102770:+0000',
                                                                            '20210224:164117.102776:+0000',
                                                                            '20210224:164117.102781:+0000',
                                                                            '20210224:164117.102787:+0000',
                                                                            '20210224:164117.102792:+0000',
                                                                            '20210224:164117.102798:+0000',
                                                                            '20210224:164117.102803:+0000',
                                                                            '20210224:164117.102809:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϫɀŤўŤȾĦҎͳƠҙиԜԈ®\u038bȰϕ,MԢПːǮȮԌ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'қԍ˝οĊΜːЏԅυʠzȯŪʟҶԤñҹ\x90лˌǵсɶʏʘĝԗǋ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʢŊͺŤŐϻǠ˾ӱИϡѾԞCȟжR+ͳÄȚԘĢêƞʱԞŵEɅ',
                                                                            'ƀͱʐʹȏҼшϞЈÀˍ˓ŗͽΝȘţԆԓѫ=ҮӽnƁҢίȚїĺ',
                                                                            'кÃЫȏƜƟŃҎ0¾ԬʹÈľΘ˖όę\x82ǌΩɝϥΠҺŇџǛ҄҅',
                                                                            'ЖɰΚԌ˅ȃˆɱßғ˴]ƴѠdξѨӴЬʘϔУәɱѯɡȄfʕɭ',
                                                                            'ªԇ/ĐԖƥθЏůÁzp\x8cʽǏχÅƓǜЛ(ɫϚɾ˩ѣ²ƀΘ˟',
                                                                            '(ʚŃϾΕʤ˹iΰωç\u0382ƟŌɍϴɻҚʔȌʣʹкʑЧҏēœĤќ',
                                                                            '˶ǿҦɀрҤќv˗Ԓɛ\u03a2қӹҫϭş)ϡąƐШҺĖɃӹԐƉӑÏ',
                                                                            'ɺ¿\x8cƌԀʡvćŅʢŋЪѪʅ\x9dɚɉ\x93πʮġcғǌѪΗΨҍÜϫ',
                                                                            'ʾʆ҆Ӛĺȵ]ҭбɊǀϸ6ʳËȽѳǰķžĩĲЁ˩ϥǼûΡȶϧ',
                                                                            'ƶ\x8f\x93˵ȼ˄\x85ˬŀϑԃʈȉóϫƉnȇǄˮƅƬҊмѓѳvїʡƋ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ЎʵƤ¹ßѼѼӊӔȌПмƈӱźǕΚÍϿÏɝϗ\x99[˄ȭЧїһф',
                    'message': 'ÇӟħГÎŮЁƭЗЈýˆλ\u0383¥ƎʓɟӰĆǗδ\u038dԕ˺ЦϮӍĠȜ',
                    'arguments': [
                            {
                                        'name': 'Ϸ\x91tƷҮƖ˂˱ĦҵˣΜ˖ǪćǈǪǲϭ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϛƏҧԐӒ˕!ѶΕ_Ӆ\u0379İˋͶɡƈљǑиȚѤб~Ȓ?ш.ņ\x8b',
                    'message': 'VɜҝԍËҝƪɟɫЇƞѫͽӞgaѳԅɉ\x87ɩʳʂ·ЇӵԂɔƣΪ',
                    'arguments': [
                            {
                                        'name': 'ɿӛԅɫ¹ҲȻΆѪƀʆˢǧ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 971218.947447502,
                                                    },
                                    },
                            {
                                        'name': 'ҢăȹӣȱОOɛϙЈɴƈћeџϷɮɑ˄ƁʇǥƋ\x85ԎƀШҘτ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.104532:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʺ7ҙ΄ѧѷˍɩѲͼРĕΕ*ĠćǕ²K˹ǢΔ:ӌНфƍԩ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʭςŜɮ1˱ӿïɗDɡϬƍKϋşēĄɁȾäўSοӃưȪϥÃȚ',
                                                                            'аϣǁӘΏß·ÑЪβEʦЍѢʱǗϬяȳԊϖюǬͼѺöΌʩƱѢ',
                                                                            'Ӡ¨ʵÑŭϷͰŁ¤˺ǖϐ˺ċͷɘжƾŗɹκƕȐȓЃKҚβʆȯ',
                                                                            "Ǽ'çƞȓγCѧ\x8eŦˌͱƪψԬԙŠǝ<řӯҟȆԈŒşȀ5ѕˡ",
                                                                            'ҁΓ˗ɥʴѕŁUʣнŢĔȰȝ©ϡҷВʟħгυҠǼЦƛǉҟǕƏ',
                                                                            '+ŁʫȦȤԮʫƵśWąǉǓǷì˞ЩГΈ\\ƛϦϣҡˆӕіˁ˃ơ',
                                                                            'Ѓ\x99ǅÕѥɸ\x8eкɍˁƷɰRρГҫ\x96ќƎͺтΤìȋ%;)ʱȀƮ',
                                                                            '˳YϴϺʔϑȃĸφ\u0380½ęʥƵʟțďиԉɣȝǰөЎɢћǨѡŗˏ',
                                                                            'ϗ&їMЬ\x91ŭ\x87ӮVҷѮϾэҡΤѦº¾ӇπΚӋ»ƩȣнʑѠҤ',
                                                                            'ώύѣɮȖϩҒŶQҗÃϳӢȽԓċ˚ҞŃçӭΥʃđΔҐԕ҅\x82:',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': ':țѻƊӡǤ\x84ϗΑTŖӻĔƋϧғʴԌѺɉȗэɔԗ˜ɜίʣӽť',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'PΆϏԀҙěɯҩŠɝΤ\xa0ŘԦҕȽѼ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.105397:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Уȳ)цӽΝŒ¡ëɿԬѧёƻҐʗɽ·ӿĎ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.105531:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ŵɛįŽϛɭʺĜӉҠϗ>ҭȿżʷӸʒźĻȤέҰͼԭ˚ʾ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 332041.79469627806,
                                                    },
                                    },
                            {
                                        'name': 'ƗӖзϔԥҾ˸ɕҜӍδ`\x9bŞ\u0379əëǾдˎʜ˕Ѫ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.105783:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʏȶȊӚȹ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǭǗҳÜɎ\x91ȕ\u0382ƜřѱЯӝ\x85ԣņ˘êӃ/řͼʏɞ\x96ʖӦӿ¢ē',
                                                                            'ΗˣZȩ]ЁӸxƤƪӼ\u0383ŴǢШϊц#)Ę_ȔυΔÍϬϐqʰ#',
                                                                            'ѷ¦[ȼ³ĭˊи§¤\\ЈѬҲǽĀȊƄȆЉƂĕǈáƨсʄFǢý',
                                                                            'ƹϫԈƄÏ\x83ϳŌ¥ѾŚҥΓЁ@άǦáʸ\x89ΖĆзΐÏѥʏʳҐï',
                                                                            'ǠǮ:ëʸƮІǝȻȓѯȲϏÔ\x9eʬüƙȥvʣƨƴҳІʸњɵːѻ',
                                                                            'ǔǝӃбΔÆɴɛŞЭϩϰҜ¸ӀҡÂ_ƨȶѳˮ¢ÂϹƗѤƺčǃ',
                                                                            'þ',
                                                                            '1ѬҔǖåȏϣ\x8eʌǍȬɾϙŅӧʱK\x92ʹ˗ĺ\x8eҒƄΥƉѶHƐΉ',
                                                                            'ƭ»ǟш҃+ѷsҨҁˎӥЎ˝ϾˎҸè˫҇\u038bňĶԁИΣĬf/˩',
                                                                            'ŹԔϫŖHɖ\x91ԐhĞӳŪĞϠҦƊƆʈʷŴҴвİŌňïuǛǒÓ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '*',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʯіːÔѸӯȃǃƺDƒϙȩ˸љ˛˘ÁʚƊӲӚ{âάňӢ\x85İˆ',
                    'message': 'ɨȩ§˟ҬǓ҅ĨЈҘ˖҆baΏϼеҿќϼǬȌťԁϨʒΉЛǳϴ',
                    'arguments': [
                            {
                                        'name': 'ӓ÷жưʭɉ˾İъùʺԤϫӑlΉƲЩŔ\x99ƗɧԐ˘',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164117.106760:+0000',
                                                                            '20210224:164117.106772:+0000',
                                                                            '20210224:164117.106779:+0000',
                                                                            '20210224:164117.106785:+0000',
                                                                            '20210224:164117.106791:+0000',
                                                                            '20210224:164117.106796:+0000',
                                                                            '20210224:164117.106801:+0000',
                                                                            '20210224:164117.106807:+0000',
                                                                            '20210224:164117.106812:+0000',
                                                                            '20210224:164117.106817:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¥HtѣћѶϵ:ǓìԭΡ¨Ǿǿ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4197639255180819551,
                                                    },
                                    },
                            {
                                        'name': '˂˥ҘѸžӎxκƔќҰԏùÆE¬ǋҗĲΥ¸ʁͰїǎ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 519924.66423065774,
                                                    },
                                    },
                            {
                                        'name': 'ҶҙÛɭΠӓǁ˕ˑŽѧԇ/ϹβùԐ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4405734592673932754,
                                                    },
                                    },
                            {
                                        'name': 'ЃΒѩwԄȆȱɑΚ+ȡя˵Ʋðӌ6ƕʿŜƋβЛŚϽНʌӀ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 448878.29860211036,
                                                    },
                                    },
                            {
                                        'name': 'nԠћӖôϙϱʰǶɞӻ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'tƨ˫ϣū»Ӟ|ˏƲԥ˭ĦǼƶˊ\x8bРƲUҫТǲȷȞТĸӼǍƧ',
                                                    },
                                    },
                            {
                                        'name': 'ɮĄʸ°ÑȪ\xad\x8fɧπ҅iˆάЋ\x9eͲȩ˯Ŭ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            203044.5358738174,
                                                                            823246.1879655157,
                                                                            74629.34167687464,
                                                                            380102.14803447004,
                                                                            983047.5121748969,
                                                                            38757.30770118939,
                                                                            952050.3769618261,
                                                                            767179.3919255541,
                                                                            519350.1478789998,
                                                                            385936.99233514187,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ήɆ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.107856:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʹξ×ԝȣўċɉƌǒȈʼƎΊă¨ҫōСɊѤ\u0378ϗь΄ΗŶ˳Єш',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2362939617822500139,
                                                    },
                                    },
                            {
                                        'name': 'ˤĲâʝĳҪŷ\u0382\u0383ŘЅʇ˘åζ±ĸЩЍӫ?ŗʴѕάž\x80œ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 48470.24203125565,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԝӏνø2ʐԅΛȈȂΨґƧʮÝƁɐҋɁ\u0379ѹ÷Аԡ_ǀ}ҨњЉ',
                    'message': 'юňɊĬθƓǴǒʹ{џɘԋɀ@ŜΊ͵ӺȺ=ʗFÛȂѳć¤ġɂ',
                    'arguments': [
                        ],
                },
                {
                    'catalog': 'ĺӌrÈKΒùҸãpʽϼaǼµńϪw΄ŐʊoԍɫíȇѦþБʶ',
                    'message': 'w¶ѓÕòƖ4ǹżľʶɇƢʿѝғɝγӔΞŴʴˁγPȶКɛɱa',
                    'arguments': [
                            {
                                        'name': 'ӝ}BŇǐϫӢԇУą',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164117.108616:+0000',
                                                                            '20210224:164117.108628:+0000',
                                                                            '20210224:164117.108634:+0000',
                                                                            '20210224:164117.108640:+0000',
                                                                            '20210224:164117.108646:+0000',
                                                                            '20210224:164117.108651:+0000',
                                                                            '20210224:164117.108657:+0000',
                                                                            '20210224:164117.108662:+0000',
                                                                            '20210224:164117.108668:+0000',
                                                                            '20210224:164117.108673:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': ']Ɂʶ$Ғѝ\x94ǿêaƿǳԌ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1833251680092001783,
                                                    },
                                    },
                            {
                                        'name': '»ɊöʁѝđʿПҲ϶&1ʎ˦Xњϯ\u0383íʋŨԘдѦϑËŉѻɒʾ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.109025:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x81эЊϞƠԩļì',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.109148:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʐɳӁUҵЦӪе\x96ʕ|˅įĔ\x83ϹȿÑɉŻŇԖτЇҷӷԑΠӍҞ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7157298370513099677,
                                                                            8307165935807531028,
                                                                            7993576091489061873,
                                                                            -6024180561956598527,
                                                                            -2349695505717361821,
                                                                            -3401040085254208417,
                                                                            8314904130865458911,
                                                                            -2348452173841841335,
                                                                            -3533366855954496440,
                                                                            -5671465114784214922,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9a',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164117.109496:+0000',
                                                                            '20210224:164117.109507:+0000',
                                                                            '20210224:164117.109514:+0000',
                                                                            '20210224:164117.109519:+0000',
                                                                            '20210224:164117.109525:+0000',
                                                                            '20210224:164117.109530:+0000',
                                                                            '20210224:164117.109536:+0000',
                                                                            '20210224:164117.109541:+0000',
                                                                            '20210224:164117.109546:+0000',
                                                                            '20210224:164117.109551:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'úȜѮǵңϊ¨ɷǓưρDӆȧ˂Ƽɹ\x98δθʻȥȨĚʅϱ\x9bѻɏл',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3090420684532971436,
                                                    },
                                    },
                            {
                                        'name': 'γΉʣȨƖӣˮÃǛ@țǐ\x9aѵȜȶʕ+ЎɃŋКɥҸµԐÃÌВȱ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȜӀлαZРāĵĢɮʇΕǮʈàǡԞϗζɧʞư©ѼВҢhҶ҆ģ',
                                                                            'ÈķͻϴҢԣȯ,đϔНĈʗΞЀʻοĳџ˷љӠϕѦƶϖÇϥǼî',
                                                                            '¥ϐēшǮӵȜҊȯϚЫŇлƄłгԎëɏdĻɞπЯåӌ¯\x8dЖH',
                                                                            'Ŧ\x90ϫ\x8dȱήǔ$΄ɀԩŎ\u038bΦɦϛƤď8ːūǲ¡ʯȬҮ˭Ͼɭϗ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '[rW&ɉѲʖ҇gòСб¾ӲңԔɿΆҎȖŗӣ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǉɎɐȌp϶Ƣʨ\x9aɾ+ҁƩΨȬҁΘұgɬњƇóϙ҃ǯѐΪɣϮ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4166851200053192503,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѸˣԎ²ϿЕ}ŸĤϣǤϲǒŦôљȺĻǈӓðɉKȜŒŖɦÿΤƫ',
                    'message': '·ѽlєҙoûFҞӅ~¢±\u0381ʃԧηoÅȭĦНʧČǚˈƽȯӾ@',
                    'arguments': [
                            {
                                        'name': "Ĵҹ˧ŋȼӃȬāťϬЪŐˢХ¡ƕĎЭɯȟIgԁƻˮӃ,ϢӴ'",
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            967688.4049613385,
                                                                            196556.9676973822,
                                                                            114617.98027283241,
                                                                            876535.2015179048,
                                                                            353837.07083330175,
                                                                            335350.74203209695,
                                                                            644365.888563404,
                                                                            965272.4824772852,
                                                                            434323.4739953829,
                                                                            356049.03144526685,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӫΕkʻ˲Ѫ²ˠԬТȭΓѪˇ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.111040:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΞņԑЉԪσȤ°˱κĴʵĕoǗϲӵƙƻEΘȈԘȶАŘ˶ĊϨŤ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4896224088153142988,
                                                                            -3800870078352859674,
                                                                            3771843347117107922,
                                                                            6825024118130942364,
                                                                            -4362022740183742003,
                                                                            -1109093087637805959,
                                                                            3539393140541070127,
                                                                            5310850210546482246,
                                                                            5123428684976272597,
                                                                            -7610603573313100486,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '>ŊǍԊϥ˭ι\x82ʯʳ˼ǯƍӲχòˣɓƾ¬ȸ6©ӵŽƽǞӺҼԢ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӧȘǼϏ¬ʆκI˞AƎĪѳtlŏǈȖŵȏºγƱĚ˚GԫԒ˯Ͷ',
                                                    },
                                    },
                            {
                                        'name': 'ãʦ\x99ˊǰӥʎЛ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            74192.75611630786,
                                                                            408814.9640306777,
                                                                            330851.97650716815,
                                                                            546702.0893131361,
                                                                            346665.9219573563,
                                                                            520719.11477815034,
                                                                            405868.9800427027,
                                                                            837626.0927585309,
                                                                            729131.388614322,
                                                                            919916.8311793484,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԣʔɦĞӬΏѡωΖγЍϾӊěԡԥʅ0ƴŐԬį:ХϔɾȚљ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164117.111986:+0000',
                                                                            '20210224:164117.112020:+0000',
                                                                            '20210224:164117.112038:+0000',
                                                                            '20210224:164117.112297:+0000',
                                                                            '20210224:164117.112349:+0000',
                                                                            '20210224:164117.112370:+0000',
                                                                            '20210224:164117.112879:+0000',
                                                                            '20210224:164117.112912:+0000',
                                                                            '20210224:164117.112931:+0000',
                                                                            '20210224:164117.112951:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ůωч\x98ѠϦļǭϧѨƓŘǄTºȏȏºµǜǤ˃ԝѥǭğÆɄȝ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.113590:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ф\x85Ӳ©\x9aŸjƋ¾³ϭЁҥķφȑőϚŗѶҰǝˣ˭ҹҧýǡԉҿ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.113868:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѸʄϬĐЙŜɱ¾±0ҫ˃ɮӽϹʎΔ˻/Ҡ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҞԨҨφ&ē¯ł³Û',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            633470.1250483702,
                                                                            -89043.7412791787,
                                                                            35546.560773790145,
                                                                            -7860.1966218551825,
                                                                            299640.2105165599,
                                                                            70415.2609749813,
                                                                            78630.57309255391,
                                                                            384466.08787138277,
                                                                            704397.7372246836,
                                                                            835187.3614839873,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɐB\x9doƗϯЕ,ÿǰЫɕҍƺɔЋń˼Ӹ\u0379ŗɫμТɤ\x99Ʌ~άԉ',
                    'message': 'ʌΣǻĸĽƇǘþƽ?όűȈĦ¨Ÿτӛ¦όҕɜƁV«Ҽōˤ˵Α',
                    'arguments': [
                            {
                                        'name': 'őÈŖ+ƽӃ\x94ĶҊŷƾ˅ӑԜ˫ß\x82ƾʉăɨϢɚ\x84ƽӅ\x97ѯӸϐ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2139696951782944054,
                                                                            8625042617233301698,
                                                                            4962984993108389459,
                                                                            2148132127816788320,
                                                                            -571983619990378081,
                                                                            -9197222389580149021,
                                                                            -8163027316167689707,
                                                                            6972402172451813582,
                                                                            -1684415528135619871,
                                                                            8955637068731399707,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'вŒΉїҝ˜éÑÿ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            753220.6680202082,
                                                                            188873.30690029485,
                                                                            -87786.31045811296,
                                                                            358158.1765838346,
                                                                            417409.3244111512,
                                                                            941192.6098179433,
                                                                            73108.22812349032,
                                                                            238645.9927111707,
                                                                            33265.92678094815,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'қŉȽȷĦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '͵ΉʥӔȋϔчϗƏԖŞŉ2ɴɲԧõƭҕō˷˶ôԨ˝АԠνǛɑ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Í',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -35221.56977765611,
                                                    },
                                    },
                            {
                                        'name': 'ƌǠԬǀѿҟΫƳ\x95ǄӖɍаɚʶөҊhXӇθΩԥȞǻǥƳ¢˒ӓ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '6ІTǈѨŎΣ϶ǩİύҦͻɔˡ¤˶¬2ĊƛӎН\x88оˢĐΫ§1',
                                                                            'Ǯғ\x97˶6ǜTȄӄЩ˲ȠVĪȠǮΧʼӎğ˳ԜƄɕ¢ΚĹťȖ,',
                                                                            '˝ȩϫß»òŴĪ˧uсϰǳƼԔφæт"ɄχǗЪ\u0378з˱ǋĚҹǳ',
                                                                            'r!Ӭģ0ϭ˨ҵδʌԋɰɄƁʧ\x9eɣʓʌ˷ШʡǻΫȍʜ¤Ɋǐˠ',
                                                                            'ɡϾȊʯͷ\x80ğǘԩѤ*ʇƏҪĔƀь\x99ΩԝЇ҅ø®ŋVɻЁ~Ԧ',
                                                                            'ĨˡӵЉӱʶǏĈʽҗǼλʜFĻƶԞŠέªÛ2ɡYOǅюȻҢˡ',
                                                                            'ƪҳĨͻƹѼѭʵÎęԙОʓџϦΓĿĉӧɡԤМRӶǒѺðˣ^Г',
                                                                            'Įˬȋϐt˚ŞΨôĨøʾЛϵ1ėå˟˯ʞːӀ£ϴϦͽШȥȇб',
                                                                            'Iǎ˛Жĺd+υЊ҆ƏıɅӼ?/ʇ)ϱΑʀɶǿԪɮҹ¸Nʉ"',
                                                                            '˓5ÛɈшЀ,ώɧӖ\x9aԘӇѫӃŔѻГ¼ÐʉǄҿãԉʱΚϏĹҵ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˻\x8b(σʵVҸԙοҩб˞ǟǪҁӅŐĀ\u0383',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.117799:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʺѬ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǑҰėťӯВ\u0383ӥɎҺȭɇɓӷą¿\x91Җˎ&˯ʂϠρ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.118158:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĕŬͳЕѪΟʜĵПʁʲҕ˩',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԐТї®ÝɡѦǟӢĴƋƊӱƩƱԠŢɟЌЄӵéԄȂţǢϦɔ˽Ć',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƪɘʶҠңʑи҉яӋi˞αΐӝͷǣҖѡ7Řª\u038dϴĿЛd½Қϫ',
                    'message': 'Ǻν\\ԖW(ȸСŐţɭʯβɛʬɨ˩ТġÅ͵ӱĎ<ƯӀțЉϛȿ',
                    'arguments': [
                            {
                                        'name': 'ʇȍҬŦǴ˨ƦӞĩ˕Tϥƥ҅đŊʑӊÕәŸҍ҂˄žԄΕʍдŐ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҍѿĦ\x95лƙԛÇǀĜщτŸƱĴcΊѭΡ°ϐeǉ/о^вǔǘĮ',
                                                                            'ˢѰ+҇ƛӬȽϢǦȜŞįялηљʰÅ\x97ɃˠϿҬƖĺӤØӋ˽s',
                                                                            'ҷɰŝ~QĻǡǄԁʲĴǭȥǇѸ˛˶жԜʖүʣȠǇҼΧ\x91Ӟσ!',
                                                                            'ėӰԑȜȄҀəʛ\x95ϯŗǢΐļÖ҄ŌǑґƏ\u038dʭʛǱÅӡɄɲӇĨ',
                                                                            'ѥ4ʃŹ\x98ЯԙũԌψԤƠʀЖʍkʹдƩүԄϐòѲÄĮƪʅ7Ь',
                                                                            'dјЊŒҦ\x87ȱƔèҷЊѴч)Ё;΅ӷҙϲХ˞˻}ӏŰ\x82͵¥\xa0',
                                                                            'Nʫ΄ɕɣǅВςϢȴǆȟфɠʓɞԧԤȌǨƥōΗņC˴ІҠȞĉ',
                                                                            'ĖԛҳΞ\xa0ȬĎČòπǧҠр\x9dӟàӈ҉XʡɺϰʭͷɅ˽ƧAƀҎ',
                                                                            'ìǨҍ˚˗tбχʪɰѤςɗӂ÷βʿˤěɏy',
                                                                            'ɩŏҾӓҽѶУªʑŃģ[ņѝŋȡŷВTǔƠɡӳǙ˩Ŀ϶ϔȿő',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'LAЃѸĊɨhʇͺŋҡԔȧɂЖϸԄΠӦǾȋΉƯɨԙńŒʴ<ў',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ϙ\u038b\x81ʴӑ҈\u0383ˣ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            294431.0908736664,
                                                                            -43847.14034886872,
                                                                            155512.50868028577,
                                                                            32334.785621235846,
                                                                            772978.3315079686,
                                                                            649490.7983886251,
                                                                            976369.9354743769,
                                                                            361584.36550027697,
                                                                            168397.85933690064,
                                                                            300544.8392941483,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'íT©dʣ+Ϟİҡvѽ˸Ⱦ\x7fƪǂΨ·ʴ˲ѽӋҳ\x9cԟθƭɒȜϠ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            160610.09344950764,
                                                                            55099.573181062035,
                                                                            432839.7069365175,
                                                                            -85739.32010882709,
                                                                            752899.639332866,
                                                                            408737.1550268382,
                                                                            4454.604502100716,
                                                                            564865.3104313395,
                                                                            410926.346564893,
                                                                            801161.0928884547,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΜľӁƭнʖԨȄЈĲ΄ʽԏȶǝĻԃʇуˇ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'WҧϾā˩ɜȹÍLȲ',
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
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¼5˯KċʯµÁĘҰȋɲǃr|Ȧԥɧу\x93ƧӸΜȀʏɔ¯$+Ϋ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΚҀƑҚЖʢżʥřТȉГѵȘɑȢ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164117.120585:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϾØſðʋȐ΄fȱ´',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7852536177791707950,
                                                    },
                                    },
                            {
                                        'name': 'νȚ\x99ƚ¬ҚѯӈџêɃǹϹ\x9ad\xadȤϔѴȘӇǣԘȉT\x94ѩˍƑŋ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164117.120884:+0000',
                                                                            '20210224:164117.120897:+0000',
                                                                            '20210224:164117.120905:+0000',
                                                                            '20210224:164117.120912:+0000',
                                                                            '20210224:164117.120919:+0000',
                                                                            '20210224:164117.120925:+0000',
                                                                            '20210224:164117.120932:+0000',
                                                                            '20210224:164117.120938:+0000',
                                                                            '20210224:164117.120945:+0000',
                                                                            '20210224:164117.120951:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'MȜԏÓ˭wҦϲ΅ɿÞΒҌĤʮƒ.ӬɈΡùˣγˣųǚһԊûԊ',
                    'message': 'ԠӒъŨơӿсƲ>ɔʇ@ʜԣȁфȸŧǸɰʤôȃԣΠ.ĳһʫƗ',
                    'arguments': [
                            {
                                        'name': '\x90ɾѬɏÕΣɘϏΚ½ɥԁѲԕ˱Ӣʨ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɂǻȡÏ÷ɛĠ˾Ƣ\x94ė˺±ªjϜ+ʿŋ°ɰʑҵϺ«шѵ^ԖЋ',
                                                    },
                                    },
                            {
                                        'name': 'ΖӮíťƇƳԃΌ\xadҵǹüФ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԗχԝʭƨƎС˺ыƛʄĨҺŻŔҽǄĢӢѫϭΚŜˍćƤӱνӆ҅',
                                                    },
                                    },
                            {
                                        'name': 'ԍɊăӯʰƺгʵӈƢùηɊƧɧ͵өűЩ˩ʱͿ/Ҁ\xa0˙ʢÍȀŐ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ҽϊήВ¢˓˟ӐˀĠϭ}ƂэĄøº҉@ҷȵʰͺʟϤÞ ͻμ!',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3880437894188103243,
                                                                            -3549965394695723631,
                                                                            1986931174865141301,
                                                                            -4857244149155606262,
                                                                            8836753419210930807,
                                                                            -5019674710310941869,
                                                                            4174511440101533897,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɌӥĜȅԘĐ\u0378ή¥ЏͺʄäƨЦŚĮƙǣ҇Βϣӑ\xadƛƋǿɑώǷ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'НʮүȥԀ\x9b\u03a2Ɩ´ӥǡʒҴ˽ҘǫǃɰŁѠȽ\x8cўĩxȞżҗѯͼ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 580542.8378462887,
                                                    },
                                    },
                            {
                                        'name': 'ûÞ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164117.122654:+0000',
                                                                            '20210224:164117.122668:+0000',
                                                                            '20210224:164117.122677:+0000',
                                                                            '20210224:164117.122684:+0000',
                                                                            '20210224:164117.122691:+0000',
                                                                            '20210224:164117.122698:+0000',
                                                                            '20210224:164117.122705:+0000',
                                                                            '20210224:164117.122711:+0000',
                                                                            '20210224:164117.122717:+0000',
                                                                            '20210224:164117.122724:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӎ1нʩЌҺРÛόĒӫɧһȌ\x87Ʀ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'iɚʵøҙ˳öƌƣzеɏͱӆɂšӆӚƳɣΗҾԃчü',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8301201347810515988,
                                                    },
                                    },
                            {
                                        'name': '˖Ә[?Ð˦ԝΜ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "Ҧԕ˼ZɈȻĞ\x81ғ\x97\x8dϛРӭɜƒуÐͺԆŋÔԈʥ'Қ^ȗκ«",
                                                                            'Ӆ®Ә\x98ҋȟŸʳҸƘƪɶʥɱҼ\x8dŊǊХˇΊԌȅЬŻŰpѽҮԕ',
                                                                            '\x91ţļ!BĄ˶ɀ˰ԍӔžvӨɎ҄ƠßȒ˹ΚͽƟӠɣϒZӇΐϷ',
                                                                            'ț;ȨǌĝĳӮ&ßĆŸǃĪćͷΈǪҶŚњɡ%ŦǕȮ҂ˏʵĞʦ',
                                                                            'eϔϣ˸ʹԊȨүвÒҫĤėƈϝОĉ§Ǯǆȿlæġҋ\u0378ƕǍɚ\u0381',
                                                                            'Ɯ?ͶʆάЇԙGԜѠРːϱѮsˆYʫ˖йԥ*ɢӭɖɊɄӐΰХ',
                                                                            'ʸѴzԊ¹Νˊƽ\x86ƍʌċʳˋѱņ\x9dĽԑЌ˩ѥưѳҎªдʴð8',
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

            'identifier': 'ѣĸŘ;ӟ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'Ǭˣ',
                    'message': '˼',
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
                'identifier': 'ə˹ӮϖΥӂϺρɂҽĿˎƀǞɚȡπɶǤ`ӪЭ§ǣɈƺWӯЋʨ',
                'categories': [
                    'invalid-user-action',
                    'invalid-user-action',
                    'configuration',
                    'internal',
                    'invalid-user-action',
                    'file',
                    'internal',
                    'configuration',
                    'os',
                    'internal',
                ],
                'source': 'Ȕȵ`ƌүˉ\x97Ўˢ˚қҝӨȑʩόB\\ӶȟұЌMҗϷʼʐåǐϱ',
                'messages': [
                    {
                            'catalog': '@Ќ\x8bζ®ϭŏʰVƪЮЅǎŝʘŢõӾԩϤeԏŬïӰҧԎԞL\x8b',
                            'message': 'ƄΆˣˎƶÓӲϒѴɱҢĂȥŹǏԑʵҴʜËχφƧӋ҄ϴϚÂҎK',
                            'arguments': [
                                        {
                                                        'name': 'ÖǓɂȘΫŀ\x94чѽɡĹʔԅďÛëӺϨԜǮƶлҺ\x90ɪÑɞȻԝ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2378251721012221151,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҔӏΧύӲȵUӜǽ˸KцçӟƥНw\x8cªϡЦҳЈϐ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǆя\x86ӄǃǮżŤӁϸôǍ҈ѴǖΖȈΒĆƞò˃ɼјҙǙƝ§Ɯѧ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ДΝѳӚѼȂӞΝǃÒ)\u03a2Ɨɡӭʑȓ6Ȝԙ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '+Ʃёѕʞñɋ¾ЙɿłʆŤɌѲ˓ӪёʇŘȋʁЮ\u0378ҶƬЮɢȌɓ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ОɐҞʈǲĺʲƔϚοǂ\u038dĂ\x91ќψ¨ĳD\xa0ù}ĩɤRċΆěʓȿ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ';ͺļ\x7fŠԃûϻɪӘϢʾй!KŤƯјJф\\ãǶěgџɒĽĊэ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȶʛʌ"ǂ\x9aУӍЌĎӫ\x9c˶ćɵtɸȥҋԑАʕƜÊȎѨɕªKӉ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѿɅǶʪӼ£Ĳӭ<ș}ɡӏϣÇǥoӲțſ6ΏʡʾÆĭǜǑɫϤ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'İѸʮˠӗӵƪİȽǰɢ\x99ќǔԇŅÆҧ;ʙRƌѭţ¹ćϷsԨʭ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʐάĊƓмˁɅѳԘ,Ωǝϊƻ¶rԌÌɂːԎȬ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȄïѪīŏǩӀ˩ȖыǡǮԐϒшǝɶ\x92\u03787˵Ϊц§ӼĩɜԔyB',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŽͱĕǢδ+ӬɖǴω¶ԬӋ\x8eːZƴЃ*ԟ˼ͻĎȍԩƅѢϣσʶ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x80ќĳˍӧαðȸƒϾΆëШԮ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ЅXȍ&~Ͷ\x9dΔȗҬʗŷ"҃ӂʌ\xadZǻ˄ĖƤŪć˹ӎΰÆ¶Ԇ',
                            'message': 'ĴŃɍР&˜uȬ˺/ȯSԌʌǽǲȴƭ\x93έä\u0381ӀɶϢĊĢ·ŗ˅',
                            'arguments': [
                                        {
                                                        'name': 'ҁԩΏэƢϮžΈƾ\x94\x9fӍƽŭΊϔŎϷ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȤŀӍËʖƘǆƈ\x93Х¾ɹĎ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ķҦƫ=ʁřė·ћǲϊ|țȉӦ\u0378\x9dЇʓȜΪƻ˄ʰțϘϢŭ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'щӼʓǱ$ÞѩĥȅʌƣŐu¤ЫǮωǝ/šȲʰɴɛҾȜ˄ļƘӃ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŷɽȦ!ɗɂ˖˻ͰɧˣфǞ´Ӱ(ӂȃZɠDˏӝѶšÒď',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'üʣϷ;΅ȧT>ӲŚːUҙȒ¤ʒdфΈͽиçѾĵȮԜѹzӒŎ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˷ƂoΡӒ҈\u03a2ȾåΧӇÄƨǙǏӎϕλԇ\x89Ҥʔ\x8fԝǟ˞\u038bʌÃͳ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8502776099909301517,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƯĠѳkе\xa0ҊʯǹѽɐǞҔӈβӨÉͻʏ҄ĠnΠĒÚĭƸхЬΝ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǻɱőѺĵН^ђĸȰĂћ3μӋ¸ƕǦŲϓԈΏԅĆÊ\\ϫŹЦ\x9e',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164117.085928:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЦǆəʣпΥȞηϴѶ\x86ѵΑԨњʀŌҎ\x8bǅЮeЕҥȀAȄЊå»',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ГKТʻÓÃʞǷɜiҠ7ǒўÚƶ\u0383ȥɖEѲƷÀѾҮӃ;ԞǒĆ',
                            'message': 'ϫӾʰӡҞȿi˜ÜVķҦЗɚ˂Ƨɷu[ɧÍȜCѥϳӀѓ%Þʐ',
                            'arguments': [
                                        {
                                                        'name': 'YȒҧŠPоҝ\\',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'tɠӫÓáÑĳȌʒЏùʃÖҪʬƢ϶=Ϥp˰9ԤƲ˸ǳŉȊӺϛ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϻìΌѦȐ\x97ξƎȳ˒ȰƽЁûМϑʺǚɻΏТ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164117.086651:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƘĻŗԢɖ:ą͵ǃѻЁѡ˳ͷfԝɷӾӂ\u0380ĿĖ˞ӆ΅ȀǬʲ\u038bˈ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8708107574969196464,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϬČɏϐ˜ПÇҧƮѥŹӏÂɯĎ¥ˊӂпŏϫϛ϶ŁҼϿδ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'иƧƪÒыʆ«ӜӫÓϡ˩*ȸʺ˞ǃͿȠȌşѩPϲȧƧϊƐȆʬ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɦԀ\u038dˎУϓ\x97HñǗϒ˯§ѐ½ТƆ\x97ӉԏɭҼǼЂɥOҟқщƽ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȭԢǩɴȚĿC)ҁԊҮϪϲҫΩŨŀǀ\x97ǚҧԂȿ͵ЁԛΆƟʿǗ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 923265.0028899527,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȧÍкÂȽʘǮpťËүϒԑOЯȑԉ&ϴǧȜӳǴɇƢӲˆϺ+À',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˀɂȽśʟĨʆҁԒӐɾϳ\x89ζȳҢԢȒǲ\x99Ǜԡȍԁɘɍ!ƘԥА',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "Õ'ԣѽϜǊ¶ϩXЍAʠАɰЫшӖȇӤһϢ҇\x9aƃ",
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164117.087694:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'üȕƵю\x98Ѿԛ\\',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ȯњʢ¶ƪФЮďĔĊӄҴϛͳЦŏ±ĞҕǫɯȌ\x81ȍ\x87ȓʔѻӇŨ',
                            'message': 'Ë\x92ҟƓʛŵɆӁÚǍʇӕӥØӹӄΑ˲Ɉ\u038dϙѫҗϮ;,ÀƊǊѷ',
                            'arguments': [
                                        {
                                                        'name': 'ВȗʋчǙǮʉҥʈÑӤvΐ\xadϝϟîӥȽEϔ5ӊϬҬÒóϯҤ\\',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʹƬȱÞǇϾґJҟȠЈƿfмļӪɝļσťØĴчиџˀΨԭWČ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'εйÖÃũ¬εɿұԥˡZїŝͺǿĠ(ЂĐ˚`\x8dɲпȻ\u0382ŘӞȇ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '½˱\x89ʗB',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѨťŃʰƎĞˋżђMϗх\x90υęƻʘ˃ʊӌƕ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4183281904723021153,
                                                                        },
                                                    },
                                        {
                                                        'name': 'һϔ҄ԉϺØϸƧҲϝϗϺε˱ʶӞ\x90ĐԤʟӻ\x99ӯ÷ҹͺĆȏǬ˱',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '-ʿ\x85ɪӦӥȳΟͲ\x90ϩžΈҐёʴԅκéӼ*XαҴӊƊĵĳŧə',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ūϡ˓ҥɨОϠЎnöŪǋȫӄȂːҔ?Ɔ§Łʯ\x83ԃ:ϸǉςçɷ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 588337.6355805761,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŀы\u038b',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'rΊΜӚßƧ,ȃʢѩϦʴԉʇǋʆ\\ϏӮΤm×ĐӻÂÝƳӟӫŔ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϖся',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɏͷӵϐʖîƛœɍ+þɝȶóŲƴ˛ĵӂԂƃ5ƑΆҹİǤǌϾĈ',
                            'message': 'ӸͱĴʟβЕɥĩԖžӽάɫҖԥΖȭ§ѿȡΧʺ,ύўù˴сǛÈ',
                            'arguments': [
                                        {
                                                        'name': 'Ӆ\x9cώqǤƥĽҶʹėαɒǂ<б˩˲үƵƺ"ϰѽҠпʁИȗ¿ƺ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȶħѼĠεԛЖ˂ҲϞʐӃƤҳȅǷªʇƈȞ\u03a2ɗņʟŅ?˖ÇƘϟ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'áΚɻ¿ɡɆȼϘԪÙӾҢԕĸ˸ϫҀ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -635300121624365619,
                                                                        },
                                                    },
                                        {
                                                        'name': '8ȩėϏ\x8bȞŰŮӃ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӕӕԝƠŰϘԉǴzĥǦβӥχ҈ƊϟƷ˨ϨƳǆʿӁÇˌȯ\u0381ũθ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǃΎϞjƹӚИιѢƏƔ\x96ӎɕ¹ƨɨ`҄ƁȯşŢЍ\u0381Ӓ҅Ř˂ь',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЌǟŹńżԓʮβϭȢǱÜ\x88ӨԬŮȱκ˃ұʗѽľ˜яѻíлϐʥ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Śӵɢ7ƼǛĵԏ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4422892503562971300,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӓΙ¿ˢҮĳÝŉ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҿ˰υǊ{ƄÙ¯ҍlʘΞǂɂ·ͱ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'һCȽ\x9dԔ҅ȾɠќӨˠ\x91ɩ¾ƴŷƩȕè',
                            'message': "Ȁˀˀϰ'ΒuǞͳğ\u0378v˙ȽϯÁӀw\x80ЛÀѹƬөϯђӄҲ\x99Ŧ",
                            'arguments': [
                                        {
                                                        'name': 'ʤ\x99˅ƱŰҤƶȓά҆ɟ\x82˄ĩ˼ȂαѳӿӭҒχU©ĀńʯǥϘΰ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԪԅǈӣϳƢɑȵŧфԮєţʆËˍдǿʻ˶ҫʴ·ХŜԄ{ȁȶG',
                            'message': 'ǠЉΞʫWΦ¯Ԁƚ҉ԕ|żҍӋѐωуѐăӶĸqϸɠѲˡϪҊϯ',
                            'arguments': [
                                        {
                                                        'name': 'Ɨůc*ΰѝΉҨŅUӭ\x8dǔңeśЩϤʉǡʤƸƙˠӌ]ΊǯҁȐ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1824716193176210886,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǹŝλͽȈǡ3ѦʭèҤԒ˨гșɂdɣӜCŋͺɲƀʌȦ\x83ʌθƹ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΣӕǴɒ\x8fϡƾɛΌʵӹšʞĤ#҈љҜӅóѩ¬ƾōҖʆѪѻҶ\x91',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʸɍ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Нβ¹Ҙiѩ£\u0379FȠxȌǛĂ\x94ҹșԍʧӓƘ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6059134457285503544,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӖлĲγDɻϐζȿШϪϤĘŌǗѥɾҮŎήОɤȸɨЅτɑʨw',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 985639.0807599493,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԑҐȴŚ5Ā˞ѢƂʋӓƾǼąȯϫɂҏԊĺ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'øӧƳǷ˱ŖʜΪțƜʁѠУʏΧȀлϺ˥ԑȁĩĐԫħǲϒӓжư',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŹͿ:Ԏ˹ХŖȡĨӟϗеԉѓȩИʊʖϨЏ\x91\x9eϞϔ1ΪЇπ˻Ñ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ίӦÀXªʪҜxӧƖҞİkƃǎѧӬłӞɝΕ+ԐӥϊΆͻҶ\x97Æ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŨӹĊԬÖɽӱϷĽчūʹϺ;ϾԢʸқȂďęɦ<ӿœv\x86ǿ\x9bƼ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'vђҒѻƌѦԊԭąK0ЈȈ÷ʛ0ÆǮșƥ/vхşƥѶϙ.ѝƘ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǾЌsʟбuφʻ\x9c\x9cΓ\u0378ѣǿȾ˙Ѣpȧ7ʤѣɽԥ©қԧԕǞϪ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 376280.91804606735,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʫˣāȋɓǮƞ(ɨЄɺЮƉƢŶȍÑшșĲгʞʞ6þАӆԋӡΞ',
                            'message': 'T˧wұĈ,ĺС\x7fдȺʘʸǮЗµáҧϫɒȿӓɬ\x8aÜϘЫӚɔ·',
                            'arguments': [
                                        {
                                                        'name': '˘8ǝëB',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԝîˇʯȑ÷į6ҿΫγƼŚķϗ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 719102.1628737611,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϞuØVΡ҅ѧВŎӲɷͰҿѿ˯ǉĦ\x98ØҼȋb1εņǓɈƊï˴',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӧ)ɐɮ˶ψț¯ʾĮζ\x87yAѪeǏͱ\\ƗƻȶӒǓҔǚΪļÙŅ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 570568.0637428885,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƊͲѤƞϸϙĀ|ĉ˒˓ΛԑΎʈЖϡ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 889138.8956461494,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Śы˫;ʅ\x8fƓ\x84Б&ɰŢȮǨΑλ΅ϡ>͵ƯЖˊϮʿƂʂο˃Ѹ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5816747674429969417,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӷ\x95yăԢԅɖΐưΜϳҭ˹ƼS\x7fӱ\x9aӜψʀÏȳӽҥȃԂыƤɦ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'яǗΤƛԇľѓʁөͷҋԑńӼ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Άʅ+ѪĄϧȖ¼ϭԖӆʉpΝ˺Żǯʚ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͺƱћɄ\x8cʼ3шǵŔ҆_ƒȸҋԈѤɹѼpʦώт\x87ǻǷñ\u0380ǚļ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ЩͺȲ˵ȅіɹϧȆ*Ĥȴǖ˨ѶžƚŤĮʊƑҴƐʯÛ§ŧɅ²ϔ',
                            'message': 'fÌͽԣЄʏµȮɃͰΞȡȴʩØѢрѳԭǈŻ\x8fȢ\x99ϋǡпӌƞĈ',
                            'arguments': [
                                        {
                                                        'name': '\u0379ˏΛè˲ˌeӰŐϓǔүĄжʇ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4979959838949073841,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ũЏ˽µҋĦîɞζ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¡ЫӰˍȩ±éƀΈԂƘԎȶǡҰ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 71515911678771580,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʂŀɫ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԩ\x88ϿЦӃȆǂΕ%ˉΦɬȩҧɗԒ¤ҖƅɴӤ˅ѽԘωģɑǿԓƢ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǯОτĠˀʋƄŎ˗ϩʾ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6615771918964576342,
                                                                        },
                                                    },
                                        {
                                                        'name': 'şʤŸÍǛrҧûƑČͿ³·βÄԬԒ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2895709700684054615,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѲԈΖĤkԫµϻӽ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'îˠӧƢʿ#±ɷ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 68933.73211909557,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ƞ\u0380Οɯ¹Ѣ±ƕЈԀʁ˝ÊϾϗЫԢЛЍˡȂӥȅ¶їÍӬϧǱ¨',
                            'message': 'ŊÁĥˋоғĢяì\u03a2ϧԩǪÍ\u0383ӡɠиǐˆĈƻȐ˾ϰυ˨҄Ŵǩ',
                            'arguments': [
                                        {
                                                        'name': 'ɦӉĻҥȏ«ĄĳϏoȍǶӕʇʹːİ¤ӤƇʨØ,EǨԀ"ƣʬг',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ГÝȝ?һĴϹʬƺPҶѼưӀЫˏΨŻҼӝʧΗιŨӨ\x95ѥӮΞ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'φĦҎÙɜжҰćӡǩȗ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˈЧXŵѷƺǐȲͳØ?ѭӦƗƁĄŀˑцʟIõʁԀˠ˱¾ċӃЍ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʢ@ӈҽϟқŴǧÂο˞ɂèşţ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164117.098661:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɗÁеΪȼʘλĳƅлĿÜáԆǆԏȍ˹ўîąã#ʣћнǰ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164117.098866:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҲсȅɃʖǕďƵ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -939369883629721093,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѲˊȕοώtҮˆ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҋǕϒҥҘЦ˃5ΊЧїѯВɭŇˋԝԐ·]ɇqșĉÀłǼѣϼɓ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9fδĻ',
                                                        'value': {
                                                                            '^': 'int_list',
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

            'error': {
                'identifier': 'ȐϬĘȝˢ',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': 'ǶΩ',
                            'message': '2',
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
                'identifier': 'ƄɡҘғтσд\x87ЖűʤaȷȏǚӕќЈŜӰЧ˳чÅϨЧ˛Ⱥӣɩ',
                'categories': [
                    'configuration',
                    'network',
                    'os',
                    'network',
                    'internal',
                    'file',
                    'os',
                    'invalid-user-action',
                    'configuration',
                    'internal',
                ],
                'source': 'ƺοmŨȚʣɤ˰Ȍ\xadǞӍΫZƌԆʍƤԢčŜƤƌɣȎФɣâƦ˷',
                'messages': [
                    {
                            'catalog': 'ʺȴǜԏͲǒʸAӹ˘ΡЏēțĔǈ΄ǚс\x7fðŲ¢Ͳԛ^eɻȻÙ',
                            'message': 'ǓĮƿźȍµȚʝĜů϶ə½тѣ\x87\u038bΣǨŐ\u038d˓Ψ\u0380ԬҡɛɍɁӬ',
                            'arguments': [
                                        {
                                                        'name': 'џΕǞ˨˷ҔҲҒЌхɰШÌ×ӉґӢƣӆ\x91ӺɼŰȥƧǆʌʮǽϿ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'пѝͳ;]Ǹ$ƟŭſόІƯ˙ƦǟϧȤŜϕάǹԣØǤȑɯЫʏϱ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Е\x9bǚӣӮ˛ÝʪЅ¯ΘĎҌɸ҇ŉі˫\x9d\u0382ŢȮʳŃ{ƉŜɛȩҢ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'кѭӹ˹¤ӱǁ`˗\x9fzɚƼ˪ԛȚψơȼҬħɣңŨ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǟɦdɽϏӱǷϣÓΩʕ\x89Љņ˂Ҿĝ\x92ƺxҨ˚ϐ\x95шǦCΣW¤',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 718141.2842670818,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ύʶđ=ӳɿюВĝêйЏÝԏŋʝǚBңхļҁ¬ɋҀ<Бηх\x95',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x93˥z[ȽĮϝŲϔԝŏŁMҢԃЪAЙǡțȀ\x95ȎǑǢŚӶˁϱ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'я˂ҡͳ\x86Ηԏ\x9fȵ˵ˊƠ˸пǐȳʎϐÙҟ· Ɠçʤҙ}ëOӮ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164117.126205:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƴ\x83ȁ¥ԕɸ\u0381ӥЉтȭͷƚϩ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6476087224346572950,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʽǨàϘʴϘjғ˰ɎѻȮϖқƎĻǂΠ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѼԂʄıûëɒԀȗЀσ|ϗc\x9eèʈ<Ƞ˥ԂŚƬïéƫʡЋDʸ',
                            'message': 'ˑ\u0382ԭlΟ\u0380ȏƃӘàžӎʚȕíǕŧΟłЄѩϼѓҕɥˈхƕϔϽ',
                            'arguments': [
                                        {
                                                        'name': 'UˆÖӻ¨ϱʐƃ\x9dԕǎΛӞłȴіȋ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ГхƵ}Ғ\x8cǥӯǊɛ˚º9Ѽʝ§˟ЍƗè°',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȆϸʖǀϼØǼǤ˼ҴǰӀƫ*ԁð',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǳĜëɍŪз\x80DҢԆҔB˴ѦϚȤƭɍŶфӲǩ³ȅũΑèέсò',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԦÎř¬>ƎҕèϔЖӅ¦Ѱјƙ¸Ǘκ·ӵǙҶыЈĎҌɢϽϖɜ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɸӒŪƕ\x90Ӿѕ\x8erĄŇoԨӔ҉˭Εӷƻǡҝӿγ˘ѿ§Ҟæ>ʨ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӻҠŗӋŷƐι»ȜȗŉȗӗӀɌϧѵȻȟӚѠşĐԘϿҍӻ\x8aҙλ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 984909.2530087864,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɩ˨ͼҎϿʦѬƘ÷Ђλƴ#иҊÿЋͲĵԈF\x8aϳ\u038dƒԧϩŸүԏ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȄČԓňϛˁȚǆųɏƣ¬ΈkɇПľѦϴѿŕąүŦɐǳɗҔɒќ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3002896498330450889,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɣĸΖѝȗŶǽӗԢѯĨ\u0379Ԅ˜',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -382842681655470338,
                                                                        },
                                                    },
                                        {
                                                        'name': 'δќəȩԆлǥɺ˔ОɹėϯĭП¾êő',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĤĥKɥϯлtςʫƁΊ˗\x8d҆Ǘʇ\x82тˋ˸ĞĲǔϊ˽NhϒÐј',
                            'message': 'ҝȸǢҷŃÖ\x9aɊρŻҙ«ʡšхԠǖƂ7Ź\u0380·3Ʉ\x90\x9c˖óϽӦ',
                            'arguments': [
                                        {
                                                        'name': 'σϘӃ\x84ǦҝôӻϏȣёнξнɆ»±ʥΆэҧ\x93ĉǌҾϳɉРіȦ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 569169.102481421,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǡǝӅʭӈŹłðӑ\x93{ƮË¦ȇ6µҦÒ\xadԥǧԥ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӁʹƒĩѪϻҽӕĒɡ2νГɇɅгĨиӁȠӀ>YҮɉԪԎɉǳŗ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1407737170633311382,
                                                                        },
                                                    },
                                        {
                                                        'name': '2°ǆƹ\x8aýӜbǉŠʈΥ\x86®×ȆͿǞэӉ`ΒїΟκҶҴǌɊʉ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'şҭԇԥ;ƘГҪƲ@ȆǊūÅ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'лӽɷ2ѼđƞȩԏыľöćǩđźʀώûʂӻêɗƧɲԆįÈͳT',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԋ˦ʰ\x9dӶɺǪԚОϭ\x82Ԝ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 900826.6780745849,
                                                                        },
                                                    },
                                        {
                                                        'name': 'EʎƗ\u0381һǍʹҰɨψҜъǽƬȸїƘҜŉȗφKŨőǓҾʔŵ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʉcɉ<ŦȤ.\x9aϵŗԨʉˈɍ΅ѷ\x94ğʎӤƄ˨ŸӐşˬФˬuÍ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ə',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1201185107281275624,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ńϒ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϘҁѷJƽɐҗǖμдгӷӣĨŎɛӇϮɦΐȨԒĚ͵\xadфҹĵԥȴ',
                            'message': 'ȑӾ(Йůʻ£ƞѾͶņŨǞǙ˺ʮАʥª´ÓҢŴ¤Ϝʀӻʪ˵Ɉ',
                            'arguments': [
                                        {
                                                        'name': '˻²˺ŬøҰɚźэʹʟȹϊҊπɄȢ˛ČӴǔØǾǀ˰ƞǰҜÁ·',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϭǐ˖ʓŀ϶ĈϴǧcwɻЂȃѵšǿ\u0378ԗ\x83˪ʏʍ@ėèԚҔźι',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ύÞѸ˃țŰ˜ȲȧɰЈȺɝҎȼӏĖɃɗӡŮ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԋώȪΊǝԖɎƮa\x98ɂ\x83ƿŋøϛϲyΙѴ(ҙϔΙѯҾʽźɅ¡',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1554328596835357532,
                                                                        },
                                                    },
                                        {
                                                        'name': 'љ4ǭϷ\x83ċƈϣʃVѲ˾Ȫš¿ɴˡѥǶʣӼŃЏнНTɕЅķʨ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5559988198099088239,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǻȼ\x89Ωȯ\u0382Ϊ#',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '/ЇõϋʨҲϮŃƌΌ0ІͺɪéhŞϜϱӵșϔʯԩȌ˒Ͳɗ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7822667458222537513,
                                                                        },
                                                    },
                                        {
                                                        'name': 'άӲҭҊõƲзŊ@ΜӸҚϸǀӪɕνЗɿǞϜǃŜяƷ]ƔŴ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŶʒНӍƳ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -11225.267679910059,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӎӑΖàȡΰƜöʦ\x92ƈϭϫǙĿђҎӐҡʍЋƬ£Ã¢лͰςŏŶ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164117.131843:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɭÖhӘȥʫÒΐőôІģ',
                            'message': 'ͼȓзчρɉǾǄǶѦ˄ǱͷĨˬƨѱ\xa0ǏǅȜ\u038d϶ɫŹŒ\x81ǍԢс',
                            'arguments': [
                                        {
                                                        'name': 'ķğŻʆʄͰvKЍѻЁɷʑѥȜԦļϭƹŰþ˴τëπùϸʦɕʓ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѪɁѯ9ӌʻаѦŅϑĜõƕǟћˌΩǅ\u0381˚;ӫȎѧʣĄқҡϝ¶',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 984311.6795990018,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĭ\x9eHäеȐȿƋɀˠЙÊӍʒΗҞϺŚőӷӼ8ϱ\\ˎ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˹ǭƌā˻ԖҖԃuԥ˹ɭÞŁíԫȓĴ˺ȧÔМ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǂ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 188504.83727665513,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȢŌϑr&ƛýҗʀʍ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÿ±\x9aͲſҚǪԁ\x9eњϗÊʃҀΐƵɂЬěæ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 785232.6778808543,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͳϺǖʔƻʯŘÇǈџȯ˻ɻ\x8aӗFōл˽ʥѐЋЇłс',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'éÿΜԗӪóҪʤ͵KӝƌƾЀÊƱΖƭʝźȝВϏɢŒȀųÒϡу',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϲǝȗ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'тƬ©ǺōöÚцӥŜÉʳѝΕ¯ŮɅȟ˸ϝЭïƞɃŢťѪҥŐԇ',
                            'message': 'ɭҵưǪϝMʼƠʀѩϳeđ\x93ԠȤƫѿŢ)ŗУԌԞšǔέƈǇУ',
                            'arguments': [
                                        {
                                                        'name': 'ĕ¶ďʟѪˢİŽƭ˔ϕ¦ċôʳ=ӤĻГԧŞʈ΅°ʍҝΨӒʼɗ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'æБСĢŘëџ\x9aІϥ½iRȡȨȦ˯Ũ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Жʍ˲ŒҪШ»ѦȌҭīŌʌĸ\u0382ǛϳӦ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Šŵ\x8eʝżЍğüɧϐϱκŀ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ħʍѧʏMȦn҄ɌʕXĳӛͲҋЧěЮϥƯ¯Ũ·ŵȍѽɀҗĲƫ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӯƑѝԑѬƨ>ҠфҗӟοĦóÛ˗ԭƺ/ƩΥƅӪbɅĉǵ˵ѝɣ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 622241.5988334033,
                                                                        },
                                                    },
                                        {
                                                        'name': 'АƟĜ¸Ԩżԓŭ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164117.134548:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʲº>ɫӂϏȽ¿ɗѹĺɴőҴě¢',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'äώ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˬŰ§ƄðξȲχɮ¯ſǥ˨īŕʧ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÆΉήrӅ˼ǭ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4399428511658465257,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'υƞ˔ɄϞӤÀӄƽМЪÄÆ\x8eØŗɹ',
                            'message': 'іƽӫɻѽɤɞȇ@а]°їÆƜϢѡεŖ!Ȁ\x96ǤӏʟzǖˏĖǗ',
                            'arguments': [
                                        {
                                                        'name': 'ϯµþӔԅ½ȠҮ·ȍҨ\x9cуNʣ\x8dѷЩϔǴ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ś=тһďΘŦɭšӇƦɬэɵ¡ӁӑɡΟơîǜ<ĒӇѶяɈ`ƌ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӄƌ҆ȇ4ӾͺЍǝĴϤʌƘЈџϭΟϭƦӜԖ\u03a2ĄΙʥӨϊ~¬Ƅ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 239044.73406657774,
                                                                        },
                                                    },
                                        {
                                                        'name': 'вΎïɷŇ҅Ҍ=\u0383ȁηЩ)ϪԌȴԀ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŐΕʚðöŔPԉ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x98˟ÆδɳЮňΫǧ\x83Łԫ\u0382ԏÁΚȻ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҳ¶ϤǢуɀˇԑƳΈѵи\u0378ƴŘ+мҋõϫԮԄ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҈ˆϑʰþɊŔȨЋʁÒљAyԖӚΆѢɹɢVƴǇƢ+ŜŰʂͷӇ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8500090099081058224,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҭϧƴӁˏ%ɪǐcӁùΚ\x88ДϻŃ˖Ϋšǖ\x9dҽҚвƇï˯ӞT¢',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1609985419460577716,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǕȪʜԦǊþ˘ĆҠѴŤŵ\u0382ΠĢĸɦȁ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʱϼҟÝЀŶΪьĺǫɁ˂öƷƆʚҒӽϽӉǼȂŌӤѮ¤ǬԌʼ&',
                            'message': '΅ϗΕLˠѠĿǆИǣǭĿԀD˓ǈȡӡÒſŷҿɳͷѤɳßƈϕ\x90',
                            'arguments': [
                                        {
                                                        'name': 'ÙЭȒϡʁЩϩӀºӢӲЪ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'мҫͶŏͲÛΌм¡ɢ+ĮћͷƂ\x96ĨǪ˺΅\u0378Ҋҵ˧ŀƟΰǬϵi',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'æώϓūӾΔ\u038dnŏ˫žʐкЌŸǒUԓϚƹʕӞ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǃˉωÚӋĲȨ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ']ǜȱę͵ǮÊʛ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɾƒȸɋſõǁÇĖ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 306396.8451016298,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΖŦʮ2ǋɜЕΰ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ý=ӃļɄ˙AЈŇƄɞnǅӴpƲ˺ĆѡҴƱɳqсʾȯζ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x9dҋVѴӀŧГΙȡ×ʔżӸΘůχɦúʍҙȍϰь^ӞӨǒƸЁƗ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŨǶԗɦüѓƽԙϸЛЄê[ĝǒȁÀɽѼɓӚл˙ǶǰԘЭȘčɌ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˝í',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 242437.07497759518,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҩɼȧƢүçҎǐŽ˚ЉŪԕȣОρÐύЄϮШƪҦȋќƮѳɰȰТ',
                            'message': 'ʬ˺ͱč˝ТƕĤʘʣýƒƕųŏϱʦθӥТʲǛŋɭ ΄ʛҮ*ǻ',
                            'arguments': [
                                        {
                                                        'name': 'ǃƦς',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 201755314927589462,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĭівƦ˩εȾ˓жʖѯ\x9fˠΌȽиӾǃ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʪÍϟ\x99ĩőɉĒŭʂőǽ³˵ɬʇӨƁϘ\x9fˠБ\x82ʱǢΧ¾´Ų',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɫǺӝѲȎàҔÕ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɔɰќ\xa0ȴчыŎӀǥȺ\x94Ҕū˷ɮ?lѐǜӐˁήΉɳʁɚʮГЍ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'GŲǒdŏǾɴɚǏ>ԢФǐ˶ſ\x9dūӠǚҢЌ\x85ыąʿЕƐ˃ʻϓ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǷφҸķŋōgŨ\u0380ԣмʀĔ#ԑ˒ʜĀ\x7fϓŤƓԕʣȒѰИήĔŞ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 91733.0797438831,
                                                                        },
                                                    },
                                        {
                                                        'name': '¬´ʂ\x8dґӘҽЛǓƌҞř˃еǺ:Γǳıϣϖ\x89',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ш4ʒƮέϣҚӁԠşƶ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŒƭɑɊѼĠÜàªϜɥ±ɱ˗ϰҕҪϊЈ˰ҪŉÅ\u038dʅӡσį',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ˮAˋŽŤԠȫϳƙˢƵ\x92Ǥʦq\u038dŵɀʔрżʮнƃʎͻƎɴõӫ',
                            'message': '҉Ѕʐζĸ҈˱ˉРÆ˭ňʢӱʌҺԉǰʀƒȸΝŭѕucɯɧсš',
                            'arguments': [
                                        {
                                                        'name': 'ſĝİŢѸeìБʙȀSҫmҫʍdџҧƱʕҾŐҿĝԋ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԧ\\\x9f>ǩʕťðǎϑΧ˼PԙӘɮҸƄʣΦ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164117.140751:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': "ҶӤэӅƎɦÉϫŔʨ'ɣÓýγƶɆχњǁПӌʱӷϔͰċҘʞđ",
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'UĜϹȑԭʡŵ¢ґ˟ǯǗĔӏ˛\u038bįʣψȈĒрӇŗɹɋщʣćϻ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 130227.36569063732,
                                                                        },
                                                    },
                                        {
                                                        'name': '©ʼĢǰк\u0383,ȝ<ҒčAӥʐѸŁþϳĝʟΡĤӯȇ4мȷƧϬ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƻθòŃYʺl',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'кԦǍśѕěLƅǖ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x97ӇȯŨӤӘƬϠÚȋ"Ѩғμ69krӺσи˗iӋӌфɚύȝX',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȷ\u038bƩʒşЌώȿЧϰέ¹ӆĊǡȸňÚҞӞ¶ģĬƄǏCҊвΔĖ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɥԡѿƋćЛΐ·\x98ɻшҝu\x91͵°Л¿ʀ˘СѯҗǳϻĀrVӘŠ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŜáƘΩĠǣʘÒɁ9ưʑˑʔƏϻȉѼҷШӗɆїҁ:\x88¿\u0380ӌl',
                                                        'value': {
                                                                            '^': 'bool_list',
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
                'identifier': 'ɘ\x8cЅŁʗ',
                'categories': [
                    'access-restriction',
                ],
                'messages': [
                    {
                            'catalog': 'ľғ',
                            'message': 'ϭ',
                        },
                ],
            },

        },
    ),
]
