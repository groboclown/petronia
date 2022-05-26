# GENERATED CODE - DO NOT MODIFY

"""
Tests for the logging module.
Extension petronia.core.protocol.logging, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

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
            '$': 'ΓȠʎԈȍȝЗкĺƯūȣ\xadʸĳɄɋΟӍҷρË?\x8aύȽ\u0379ĝǥ˵',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 3668383451517293401,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 10160.280949528315,
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
            '$': '20220526:212301.445703:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ζрǝ\x90ʿɻONȝϬȏɤͱφƎÓɭĭҝĘǺѿ>ɵҵ˻Ҩͽ˚ԣ',
                'ȊԨ·ÁӣǠ\x94ǺλρԖƺԏԍг.Ňԁ\x99\x8cőˣёΦƚҾȆϿi\x85',
                'ҢʦƼǀʊΌӡжϕ"ǂұӮϱȏàџґʎȯŞǬɣӍҕiĐʖëȨ',
                'ɺƘˁļſŵ:Π\x96ѮŜ\x81Ĩ˽ĝɜԥδѲɹŰϹͷ\x9b҉ĿҸѯΤF',
                'lˢέˊbαǰʇÑʧНѯȰ҂ѐӥȫйʾ΄эΚ\x98ЋѽʀˈαШҏ',
                'ˇӳĻǥЇÐϖϴǗʷŞơɃҩƄ˳˵ƄƖԭ˞ɚûʜіԒүɌԃԈ',
                'ƈǷӧ\x86ʞ\u0383\x8fǷϽϽφǊȜ\x9cąҔƲВĆĪʆЌŵĲͱΒđŮ[ø',
                'ŇŨȼљѵћ¹ȐѵiʭȪμԆзɗĶɱéʴ҂ѷΧŀɽқʳЁȀç',
                "ƎƪʓƷҁʓԤ'љʡʑŉǊӤҀйɃSČȀѢīϪǞƀП˒ёѥђ",
                'хǑ\x7f҄ŴēυʈӚѽԄ"Ϧ˗,˷ԨχԎТƶ\x9cеȐƸƳȐȦϪȱ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                6382542642136962694,
                -3279155468637790870,
                -8573215651583756684,
                -7861338379527881329,
                -1962194852240172737,
                4146126835146353472,
                -1456789011450175903,
                -4676944501152291300,
                -3279622727236082533,
                -6937365055896016552,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                186650.27997053263,
                49019.244735995104,
                89686.65950412943,
                218315.32743568462,
                887565.5936940069,
                -10225.468938814884,
                928975.2509246885,
                370919.4093422835,
                294294.65084330045,
                552392.0872176801,
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
                False,
                False,
                False,
                True,
                True,
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
                '20220526:212302.362999:+0000',
                '20220526:212302.384849:+0000',
                '20220526:212302.408714:+0000',
                '20220526:212302.430804:+0000',
                '20220526:212302.451165:+0000',
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
            'name': 'ˌǬŘǌ\x87˦œɷɣϟſӳΓćŶ˫ŕ©»ÜфӢDžɔџǫґʠÇ',
            'value': {
                '^': 'bool',
                '$': False,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\x86',

            'value': {
                '^': 'bool',
                '$': False,
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
            'catalog': 'ǇR×ăȎˌԈʲщөƅδҶɕΚuðéЈÓЕçǏuУ\x9aYÂȼͱ',
            'message': 'Χƶíϕ6ёȰΛɗȮɛОԘùβɓΒƊǒĩɟõϛҨKϮIėţѨ',
            'arguments': [
                {
                    'name': 'Ӷ˘˄£ƘȵСɬϤ\xa0ʲЂBʜ5Ȱνђ]ØЋƹ\x99ɋÝоÄˁʆԅ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220526:212259.622592:+0000',
                        },
                },
                {
                    'name': 'ħüƻɂйΦƋЏ,҈ѡ0Ĥʍ:',
                    'value': {
                            '^': 'float',
                            '$': 965967.8321875175,
                        },
                },
                {
                    'name': 'ʊȝ¾Ӣħ˰ŗшǤĻGμƿůԙ\u0379ԐƹԃҹȣɆǒ)ԗʱƚgˠ\x8e',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'eɎӧAԡϠοȒǱˡџϝӪJϦʰѵΈç÷ıYѼԖȺ§ǗЖąƶ',
                                        'χЭKFZɒ˔϶ʵԔψO\u0381ҁɵʰѣϦɺǅƶŰӠŞʮМħ\u03a2SΡ',
                                        'ĠǻԬƅƱӊλ˚\x95҄2ӻ¢ɘĉΛxΠƙϠżπΖưi[\x96ԍС\u0382',
                                        'γͿ\u0383=ɒӄЉͼȷ¶\x93ьшЯѧ϶ΐƁӊӮĄ9ҳƩŉнƒˉλʕ',
                                        'ӆѽͷȊɘѓʲΎƧʏТĴΧüÝYЁЉʍєχыοӉΛ\u03a2hԖӌɩ',
                                        'ʂƉΊ\xa0ԗЕȄ2Ұ.ΪĨӍ\x82ǊӛǋčʾȤÐ\x9fØӭÄԧțV3Ԡ',
                                        'ɱ˃ƹĖ˳ŗύàǼГϯɗϤOʱɹӂŲлѮˠљĎԔ-ÄЕéҲξ',
                                        '\x84ÜåɬҴǿӎÃ°aԛ×Ǆĺ7ŬӦԋ˄ċƆФ\x8bҔҴ˕ŶȪýĥ',
                                        'ǖӹъè˩ȞYτЛ)ѵèЁƧӛ\u0381ɮҎĤͽӓŧēɐ\x92ñβͶ4ŧ',
                                        'ӗϫǭǏ\u0383зӋźЛȲƺƑƎқϠɻǛѺҒιӤӱʞʑĪɓũύ˱ӵ',
                                    ],
                        },
                },
                {
                    'name': 'ʫÎǠԮ^˝ʹǰ%ϳλͲΙwJ˭јӴʶ˚¢',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ŹϿң\x8d҄Ԟ2ľϯ;âŚŧŻѺ҈ӲǖʠЮXðӐº',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        1998474706276707290,
                                        -7665263604204064352,
                                        -3663425044622180941,
                                        -8588537557372931677,
                                        5155458625235988831,
                                        6895784667847948803,
                                        5109389957421911096,
                                        -7571887240623184669,
                                        3482217697597170493,
                                        4652995027802343593,
                                    ],
                        },
                },
                {
                    'name': 'ǌƜƁϲƋǾȚΫõŔӈӱ˔\x80ԥӍ҄ĆĖ҈ǯ˝)ғφǝȢЯƏ\u0378',
                    'value': {
                            '^': 'float',
                            '$': 15235.718300403038,
                        },
                },
                {
                    'name': 'ǒĕԢͶԨȺ\x95ɢǼˠɩƂ\x85˳ΊϧÀȄ*Σ',
                    'value': {
                            '^': 'float',
                            '$': -75717.83201947826,
                        },
                },
                {
                    'name': '˄ҒѼĔŻӽˡΪ!ўŁˤɜʆ¾ǇɫӞŒƷɷʹʨάʊʸύԪƁ¼',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20220526:212300.572478:+0000',
                                        '20220526:212300.590786:+0000',
                                        '20220526:212300.615790:+0000',
                                        '20220526:212300.638139:+0000',
                                        '20220526:212300.662531:+0000',
                                        '20220526:212300.679376:+0000',
                                        '20220526:212300.696755:+0000',
                                        '20220526:212300.720139:+0000',
                                        '20220526:212300.742568:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ͷ@љΫɜɵԠʄΞԥɆɼ]ȆϤʵȬĤǷ`ǚõǗ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        False,
                                        True,
                                        True,
                                        False,
                                        True,
                                        False,
                                        False,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'Ģ˘Úăϖ"',
                    'value': {
                            '^': 'string',
                            '$': 'ľʤԪЃϯ¨ͷ´ƹƍэūdЈˆɣŭʈƟ\u03a2\\ΟϯʢʦûγŠ˼ѣ',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ƶԮ',

            'message': 'Ś',

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
            'scope': 'verbose',
            'messages': [
                {
                    'catalog': 'Ԁjʩoģ3ƚԈĹƝ\xa0^ŘӸɀ\x9fǚɊ=ͰңϏŖϽƸϧԡЗʫҰ',
                    'message': 'ųžëϦҾуTŴÓɢОuғĞɃУɳĝύίϴӾҁ\x9dboúŎʤˮ',
                    'arguments': [
                            {
                                        'name': 'ѥǽȰƿҽÈәȒȺeʜ˴',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3068567583536999474,
                                                                            -3568276645539837545,
                                                                            -3584619938659196895,
                                                                            -9213854467000811733,
                                                                            -4983443765931763215,
                                                                            4260111011260362505,
                                                                            9127138056381533895,
                                                                            -2077360752088536988,
                                                                            800342708660331349,
                                                                            -7895566563695349307,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Țԙàƕȡ8ɓǿȠģϽˆĆɁʉŏǨЏ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȼɷƏԊʄ¼hӾȟŘ(ҖӦ҉ƳОΙĪΫɦÛǔ;\x92ùœȐєǸĖ',
                                                    },
                                    },
                            {
                                        'name': 'ӕŗâ\x9bʺɣɆΦȷԗȨĒƧӇӾːДǈêńИǗȸZIQůЄɉ\x90',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ώĭȐӥҭˠαEɋϫ¼ıˀŪ\x89;ʚǹΐëąѴΦÉʚ\\ШȅΤР',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8860602518690944028,
                                                                            -2872460340219785277,
                                                                            8485834377477172947,
                                                                            6831953222322253518,
                                                                            -2905533828609853915,
                                                                            -5132911002976653681,
                                                                            -1587358190746105082,
                                                                            -8231047636806693968,
                                                                            -1319937175428872200,
                                                                            7363821041548602150,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԐĦ\x8eΩѲɼԖԙɇ\x96˂ΆÇӲ8ΊǿљĘĄ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212245.123224:+0000',
                                                                            '20220526:212245.139526:+0000',
                                                                            '20220526:212245.155831:+0000',
                                                                            '20220526:212245.171428:+0000',
                                                                            '20220526:212245.187227:+0000',
                                                                            '20220526:212245.203036:+0000',
                                                                            '20220526:212245.219433:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ŝ°ÕǴгҩŃʸȎύǱȵùÎʜ϶ˣ\x8d-ĺ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -50826.71868011693,
                                                    },
                                    },
                            {
                                        'name': 'ψŉОǓǯˎѱөςË¿бҟ\x9aɈ+¹ȠVγҬΜ\x96ǾĝśċˌĒѭ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 140081.80559538462,
                                                    },
                                    },
                            {
                                        'name': '3ĎͲǣÄþ\u0383Ū˔/ȽǥʳȱԕȍȏѠȯ\x94ǶʅÂΆɬ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212245.431355:+0000',
                                                    },
                                    },
                            {
                                        'name': '˯˫ǢĔQԛ˔ʷҙhЖʄĹŪĵ[Ͳ\x9cѡŪȿǲł@ʱeŮϜ½у',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǀѷЇԐӞѿŚћԅӉrΙƌ£ԤňΩʒɐпȕƹʇϪǵςˮɰƗԓ',
                                                    },
                                    },
                            {
                                        'name': 'ЩɐΛĕΧԬОǏŒ¢ѭȅӲƛ¥ĉчУˉ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʝӿɯƐɀВéŵɟ¡;˄Һ˂ɫǚѪƜÜ˪þʹӹǁ\x91čïÿʦ;',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'āŸ\x9fȽjƒȩH¸y1ɵ\x87',
                    'message': 'оǕÂɖǪǵ#˒ŶΈτŏ¥ЃӍŨ\x8d˚Ɠί?\x9fШ҇ƨǌʫԥӫ˽',
                    'arguments': [
                            {
                                        'name': 'ӂ¿ˤBЛ\x82ΣЂсβǾѲЫԕЎUӥˢȨŀěӓҤǻɔʡҡѣʌϸ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            225887.1564737808,
                                                                            459183.23811439774,
                                                                            71875.56597352074,
                                                                            342248.8841154217,
                                                                            397940.7310995973,
                                                                            851045.177007184,
                                                                            103443.3443751875,
                                                                            75335.01360549961,
                                                                            234986.2352292242,
                                                                            257531.03272594896,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '§ϕĨϭɸǺȗŊԌӝԚԧȀ˘ШȪʥĦƴƅŕӜõȢѥiŸ˄˙3',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ėīҗƍρ˂ƵȌˌԈ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˃ӯ˟ɏі°ҞХȌƦūϿƺơʸď³ȈΏҨŭɾȂцҐœ\x95ì\x8eԤ',
                                                                            'ӡǥƛƥüκӖҞƺиʘƸǮɿӷӣ\x92ǰ҇ҶÕįЛʮßĕɇ\xadĒϏ',
                                                                            '\x92ѣ˹ŲѣʬÛ2Ԭїһɏ΅ӷhӝǹɐʎȤνȐӒӏ˕ҔϮӷӛǇ',
                                                                            'ƶĝēӝǊȃŦǩУǾ˺¦\x9cј˄όƾŝЧǊғЃŎҋѦϚ˧ҰÈϗ',
                                                                            'ӧΫ\xa0ʩÛȩəɄ˱ɋͽϚÇĂ˂ӧӟǺù\u038bΦкÊȜ˕ɒęМȧί',
                                                                            'ŭ"ÅZϹ+҃оȃцtƓԊŰÍ)ǳƗӮèȄӬ\x90˞ҟľˇˤ˚ϒ',
                                                                            'ӦсɘҩҰPȩ¼ģˠ±Џ\u038bȵðȭԔы\x81ȴҽøǰ͵Њč˥ӐǫԮ',
                                                                            'åҶǹǚČЫЙϯ³ʾʐң˄ҠϨʓԞƅgʧэƔŅӓɆԆɽɊĒʼ',
                                                                            'ԣѶӒ¢ҖѲÇǃɽ¢ʞҲɂżвɽ[ҵƬ«ŭҦʝƙŨõǬЂ^˷',
                                                                            'üəǎғʀŶъϳɇӷŭƵвӱȧ˹(ɢÌĢ3\x91қʪїБȲɭ˵˷',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҼñƆ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʙ˪έ_ʗȥΗϩŒȀеŰȦѿ҄ƋǇԢЅҟʰUʇǺѫľǔZȃΰ',
                                                    },
                                    },
                            {
                                        'name': 'ıϘҮȹȈţƏɵӇäŻƅ˪ӒΥsԚ˜ϙӲѩƬХSφӻґúðВ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '$ƦƙгӲ¾\x91ӄиȥҤǏğɢΒDɼӰƚΨǉ҇ҏҶ˰ҒB\x81ʸȣ',
                                                                            'ϷïaϞЈʒЎϜȀëΡÏΆ˰ħǭЖи·ĽǝŗуϠŕӏϗ\x9eєД',
                                                                            'Ŧ\\ŒЛȎɇʑɐͰӂɄͷàǥ\u0382\x9c˶Ҫ%ˎЉ\x84φɯϑǛёҀD˳',
                                                                            'üņˑ\x9cûȜƞ/ѩ]ÅVǛѬЁԜǍçű˷ȌʀҽԃŽʹԎöȸб',
                                                                            'œηѤʊDȡΎƯĐYΊѓԧΥȶщˢŗjЬЙςɏѲҵЎŊЙʗȧ',
                                                                            'ǝѯΪεƁԊԓ2ԚǉӕЏķŰĵƩÑѮˬԄ˺ȗöӍŚϱĐĝŔǪ',
                                                                            '\x86ӕȲƙKǣ"ǰдөԦүŬрHРǿ0ʰӖɅǑѼѮƎɋԬžəģ',
                                                                            'ӳӶɀ²Ɏ˱½%sͿǡώҬ\x99Ї;˫ŭЬcɊΧføɭęд\x9cΗŀ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʮeγŒϊ˛ȼşɔΛѫЀ\u0381ȻӬԢÛϗĳˊĿнΦǞфʕRΙӼǕ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӑ˫ǟϒςsӔϘӶӏĿѪϤźÜƸҍȲɈƘϔŖ"ċ¡çJѷâǘ',
                                                                            'ŁȼȃКţ¡˺ǹtǘю\u0383ψƶʤ\u0383˲ȃʈPʺµū\x99эӹĹņŤϿ',
                                                                            'ҋӧȍƃĽˡɞĊƛӸƳûèýɿȚҼ˞ǖĒŻøÈ',
                                                                            'ďυћŧҐǟυƱѡӓѝ\xadɡѣϱȵӟΏÁǏ\u0380žǕȻӬԦʙÚ\\ŵ',
                                                                            'ƨӯǢϘűʤ]ҁ$ɏӬˁːʲʏϙǫȅǣȸͱȼ/"ɩӞͶœӗӵ',
                                                                            '¶fӊʈNƯҩӴҚŒΟȞӎӨԙÍúњʔ˳ѽ\x97ȡǡʳɹ½ξγǦ',
                                                                            'ȦͿϗľԐԐʆԝȱȺϽʨ|Ŝˏ˷ԥԔԁîүɍĊ¥ҼtėɬPÜ',
                                                                            'юȑӫδɖЈҖȤҜԒɠƴ˯ϢȎŉŃɞғSӰƪeм\u0383˙*İҪȯ',
                                                                            'ɲ°ԛіĳŜúž\u0379ь϶ťіʘǞ˩ĭĶӴȏɊϖʍӵΦĒОѷҧϫ',
                                                                            'JƂ\x9d˱ΖƤЩϥüɡЩ\x84Ї¡ӪƳȍԄϽɝХ½üѰȝΔʴ\x8fî\xad',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '<АоϠѿˤϡҋsˁɞFǛɧԋǺϲԜʭ\x8aAӉŤЋˁ˓ŝЀ¸Ͽ',
                    'message': '˥ɸʵ\x88ΐʪÜϏȔűͽ˸ČЀʳŨɪԁɦďԮſ҃͵ӉŐ\x9fϵҥя',
                    'arguments': [
                            {
                                        'name': 'ˬTɐ˭ѨʮϚϖҭbʍɌ\u038dϴϣɓ\x97ÈʧŵѕͶѶ²И\x9f\x96Ɏŵΰ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8582349165104626017,
                                                                            -4396016917998379310,
                                                                            2742005529043529551,
                                                                            6371718775425288118,
                                                                            209740862748697439,
                                                                            -788863679196288147,
                                                                            -969386125951740223,
                                                                            1103997962149015420,
                                                                            6960932251114705978,
                                                                            -44258075974367505,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'оǵȣ\x92ʓòӔɇһϙаĚǇ3й=ȇ¾ӰǅΪȗчΙMȰыūǚʹ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            67342.615926642,
                                                                            221271.32440708013,
                                                                            594308.3774641247,
                                                                            547929.8642402258,
                                                                            581777.158368755,
                                                                            343438.9490190279,
                                                                            -56900.94439657825,
                                                                            259181.2990636127,
                                                                            211254.65330508706,
                                                                            939831.3038173066,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '}ӯȺϡ§ΫҫȀєʨȺŰë\x80ùэΥϵԪȻåΑъȃ)ûĮԘùɊ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212247.531667:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϼřȔʡҋʡȗΎ"ҦΎōΨśұÆοҐĂŰϮ9ųѬÔϫЉӌ϶ƹ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4249530137749080156,
                                                                            445225785671620821,
                                                                            4869732147456420580,
                                                                            498477636082188674,
                                                                            -8874651697809216662,
                                                                            -2818371235601505832,
                                                                            -4711993582021001509,
                                                                            4747382147898386617,
                                                                            5526539081683596772,
                                                                            -6913836475976491047,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϪΫ¸ǾɴӚÕ˦ȜιǲυL\x96ќΚѝӊѣ«ԞƊɬšԔμѪяɚȬ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            737403.3374896328,
                                                                            675257.4878838144,
                                                                            806810.1877327859,
                                                                            640903.7882947387,
                                                                            -63769.81507286783,
                                                                            864773.7101017669,
                                                                            805783.0287259714,
                                                                            805993.6158724026,
                                                                            -4874.610786444915,
                                                                            450771.5739571679,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɀǊ\x80Ȼcж',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3127993819838895148,
                                                    },
                                    },
                            {
                                        'name': 'Ԋ˾ĜЄԁǗϢұνӘЎ˽',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ÆɪîҽӒαӊ\x88ѳWƼȬîŘƦћ^ȡӘʡѣӽǔ˄ДèßԦǲ˵',
                                                    },
                                    },
                            {
                                        'name': 'ʥҞԫéœ˫ӑВȣʧǼʹčПРpǤuˊāϮ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            67321.53774867317,
                                                                            121889.50235934951,
                                                                            896798.1282623499,
                                                                            748255.8631650299,
                                                                            635258.9431364054,
                                                                            151739.4937385604,
                                                                            168142.54194890673,
                                                                            116207.78896917868,
                                                                            492609.7858979468,
                                                                            242646.93249495886,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѼȔɧƊϯ˥ŏ҉άKˁĉϬƯŹǛ˕rʫæƁˊļПϦхԄʖsȼ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȱ\u0381˻ǇѰόÊǉǷƘŝȶ`.љɘÕʆđ2ʞǾ´ǕˉЂ\xadԙԡˢ',
                                                                            'þ˶ˋʙ\u0381ǎǭɚˬīųЅâϧҨӟǜʾӔ!ρЂӯвǔнӄӊɺş',
                                                                            'ǽɷӘǃМɤ\x8bϒûÕԎŶɛġȾοǲOͿyȇƌǸӄҳςɢЂwǌ',
                                                                            'ʈę¾NΒŦàºǊƂʍѾȷҋҵ˕ǳұ%˘ȝɽȒʰ҃Ѧņ<Ƅʹ',
                                                                            '\u0378tǁεģ\\ԣɸЁŜΑäŅǭϱҡ\x87јæƹ»´ԝʔĐƨғģҚД',
                                                                            'ȊҳΕǠԓˢʺʾʐȓʉSүi˲o҉ʲʎȚѵҫƟʹÔņϥΚéÁ',
                                                                            'ʐԟͶ£ċϥƪǪ8đȔƘYɭ³ƠȜε½ь,κʕӤӾӈ}ċΒˬ',
                                                                            'ƀǬôЄŶʲ>ѽǀӤ҅ԮϡɊǥҵҥƆϤϽԕˋ\x96α|ѽľӠҵӫ',
                                                                            '҈ȪɄъƿɼӡĕƚԣãʲ\x93ǾǾȷŨԡˌБʠq\x8dҸΡɴĀŀȎҙ',
                                                                            'ˀʲκϰЙΟĚʆԬ\x90Ё.ϡȸűȈȈʟѝԄ,ǄѡӐľԞʊҭβ˗',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƧoѦϦöȇԒӇ\x7fǍωÓԎſԏƨ\u0379ʵТӗøЊŀŗϮ\x99ϝ<Μʈ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7191238262706432325,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '҈ŭҶΠ˞Œɬɑϻʛ˂ßĒÚƩȈȭŉҶɐÎXЀΊƏǧӡåˡĹ',
                    'message': '^ͱмn\x9aʚvŗӣ\x9aςƂӗĔģĐ˲ʽѷ\u0383ŤŮǅӂˑԆпȌUy',
                    'arguments': [
                            {
                                        'name': 'ҙАѼźȯϫÈʮVµĬȡζĠyҴˤ\u0383ҾĜɛøˮˑƯǟȗӄȠġ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212248.833031:+0000',
                                                                            '20220526:212248.848971:+0000',
                                                                            '20220526:212248.865401:+0000',
                                                                            '20220526:212248.881869:+0000',
                                                                            '20220526:212248.898763:+0000',
                                                                            '20220526:212248.914685:+0000',
                                                                            '20220526:212248.930580:+0000',
                                                                            '20220526:212248.946266:+0000',
                                                                            '20220526:212248.962898:+0000',
                                                                            '20220526:212248.979751:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԉɧԡǗŋπȩԀДǙę',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1059632433369745917,
                                                    },
                                    },
                            {
                                        'name': 'ҧԓŵɕÈįњɸԂ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7813530152775273339,
                                                    },
                                    },
                            {
                                        'name': 'ā-ѿϐҳǷɠОҜȘĦɆȇ϶Ɠʠʓ`šŤάʐǦçϦò)Ŏΰǒ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʏÆ˴ŲҩŘңħ\x9eɿȲƔĕXƪ;Є˪Ӿ_ɨxȘ˦ԪþΨǀŀ˂',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8128867998351872250,
                                                                            589859379555322052,
                                                                            234726938722462896,
                                                                            1403752073444241987,
                                                                            -7444158673203092697,
                                                                            4611329695664825767,
                                                                            -6146011425360966106,
                                                                            6270479315839238784,
                                                                            1891806964126641663,
                                                                            813336292816538941,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԀÉ˅ϠƒǷВˡάˉΜǭ~όˊĪϷ)ԜěȫҰÝåƀƋǿПƛɭ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʪƯŗѷu;ʵԊ9Ȁȳ˛ʌӢÀóҥҚǧҗ(źõǺ˞үнž/Ǔ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ţŊϛbҐĞΆ˞ǕŪɝƹƝłr\x82ʼǪӢºòʃïά\x8bԧѨ҂й]',
                                                    },
                                    },
                            {
                                        'name': 'Ýѽ΅МϒŨñſȑ˃Ӄʺҙԑěͻ҈ШƧƔΨЇƪóɪƄ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9214243201695860595,
                                                    },
                                    },
                            {
                                        'name': 'ʖ=èόϓ®Ԃт˦Ұ|Ӑ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212249.808704:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ēŐϢ\x9eΌýдҙ˟ƷϘҔϩӰҠχ˟¢њȝɼbӻƨёΈѠʇԍĂ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'τȓԚͶʟԀθԕΪĐ]ϿȞбŠңπ΅\x8bſȰįNǍԔӤ2ġ¤Ϣ',
                    'message': 'ωԈ¸ðÎαЭŐ·°ҨajϤέԓ²҇ʮїŧɀTŵάêӧMƆg',
                    'arguments': [
                            {
                                        'name': '˱ʳʈYΧ\u0380ѭӎлɍŷɛΌÎāǻȱÍÕˀĸԘ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ˮә',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            893926.0576878159,
                                                                            184688.53778420785,
                                                                            749876.6390013443,
                                                                            697224.0318154988,
                                                                            541895.9328539297,
                                                                            691755.3799574563,
                                                                            667852.9744777185,
                                                                            614237.5041472745,
                                                                            237321.47353230044,
                                                                            652185.0202750548,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9dӱӧзϜ½ӪΥϠˢƻ\u0381Ǧџӣѕξʅe.',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1102229589670505163,
                                                    },
                                    },
                            {
                                        'name': 'ǐųӚĕďӽ7\\öБϥҘ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212250.460555:+0000',
                                                    },
                                    },
                            {
                                        'name': 'tǐ˂˅łВɺǦƸɚǑЯӷҽ£]ěρľӕ/ԧҨÄѭӑĹWΞɦ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĝ˗+ԠʼʰȧԛϼуЭӔǬƎ(ύƳȃŶî¶ǟűĤʗԑљʕЯȳ',
                                                    },
                                    },
                            {
                                        'name': '-˴Ūӷðτɹˎşϲ>Ǵ°ӱǊ\u0378ŴˏψǰíȎʰƑΟчɽϕʻS',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212250.604366:+0000',
                                                    },
                                    },
                            {
                                        'name': '©ҎƨδğҥӻϫɨʟƆnȚҊġv',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҔΖȻ\x95эȐȟǐάԇ\\ӴӤŚѬζбЉ҄ӞŖ\x89ɽŘiԪêӍř·',
                                                    },
                                    },
                            {
                                        'name': 'ȅ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            749189.3160711509,
                                                                            481576.713111061,
                                                                            63347.496815193066,
                                                                            501716.8312835833,
                                                                            993564.6068899159,
                                                                            947442.6076921328,
                                                                            739266.1435153004,
                                                                            252318.22277360625,
                                                                            313459.05260909157,
                                                                            70814.43000138493,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϿџʵŨӝʑȫήʠŖАέ\x99˩ωϡ±ʽҌΠ˃\x82ԍͲŹƝ\x9d¾ҥĿ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4877467451075424411,
                                                                            5168513713612615022,
                                                                            -3387013458747273016,
                                                                            1731681128857643716,
                                                                            -4872355392064672259,
                                                                            1653478790555224664,
                                                                            -7140398099984194891,
                                                                            -5122676979579341577,
                                                                            -5602403492890760348,
                                                                            2197323593307655893,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Š§pВųĩǸƠĊ_ӜќŤ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 950091.937696944,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'UΙύȧÐţȱіϿ˽Оζĕ\x8aþԢϭɠТ',
                    'message': 'ˣӆǬ˞ɎҢ\x92ǗƒʮįԫҢЌо0ϢԆ"ҲģǛ1ȭƱӻЁȩǞԨ',
                    'arguments': [
                            {
                                        'name': 'ΜΗљpǃҤĘĹUƞҿdӃϋӭ˩ǍːГʅ\x85łԮЄ˩?ʖįǔѝ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212251.445908:+0000',
                                                                            '20220526:212251.464383:+0000',
                                                                            '20220526:212251.481174:+0000',
                                                                            '20220526:212251.497690:+0000',
                                                                            '20220526:212251.516977:+0000',
                                                                            '20220526:212251.534333:+0000',
                                                                            '20220526:212251.552478:+0000',
                                                                            '20220526:212251.574618:+0000',
                                                                            '20220526:212251.598225:+0000',
                                                                            '20220526:212251.620940:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'õ˰ȥǮӋ¨žǒɨЅůðϹҏƅԮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212251.706859:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ιǉѓÜӆĖñԔ\x9bϜԛĄȤʵĳŃƁ>Ͷ˝ѰόûçȮ\x9cҼΚƆҠ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '¢ǇοԒǽυɭЯΦĆӐЩ\x95WeгŰƻƋûЯҕӂ-ӦϔϼюĊƹ',
                                                                            'ӆŒ¡ÿɼ˟ʁǧξ˟ҽ\x94łVėȞȑ˱\x81ІʴԖԇǿ\u0379ʹčĒˌ\x8e',
                                                                            'ƉʚϏӯƜƴǀeȦŜ.ҩʫѧəɅSʘĨԚɷѭэϤŦȚӪҴʱ҉',
                                                                            'УǣɪҀʟԜрМɽȆӅyǂƕӽǸɒUßƁƉƭȌΩƳͲǊÊҳԥ',
                                                                            '˕|Ԩъƿnˆƀ2ɎϏ˕iŕѬЈ£ĭˆчJҬЎŽʽѣÖЇˀī',
                                                                            'yȉǔԙӼŶʧԝљ\x82ȱίμҝ4ыѼǽn˛\x86ӢЅ\x93ÍKɇӋʍé',
                                                                            'ųιɊkΜҺ\x82Ł͵ŌҮ\x9cȠʈ5ȉĬǃιӳEˠȵ5ϩ5Ǽώʈǰ',
                                                                            'ҜӵƹɗяǮŮҥĹĭϑɍТżΞТҥVĒљ˘НӜӶȓˤ˫ƊѼɈ',
                                                                            '˫ҠɂɴXԞѩȐ˴ʛɔűËǀ\x81ˢ˾EьΩǘ˟\x97І³Ґӭτńҳ',
                                                                            'ϏȂçжÉɭ˞ωäȧάԑѲƢȞρ˜ϭӛ\x8fĦБ˷}\x8dϝɄҶÞӛ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɷʥ3ŭ°ʟϺȘƼѨKĮҩ˄҅˄ɄåǺ<',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212252.038714:+0000',
                                                    },
                                    },
                            {
                                        'name': 'žώ\x88',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': ')ƟW&ӐÓĉʩӓηõӻƥқҐԐͽ=δoнǈԉУӶ+ԑʎϭë',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -16213.141159262988,
                                                    },
                                    },
                            {
                                        'name': 'Ӟ˴\x94\x92μФùӐΘМ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1532686714958294444,
                                                    },
                                    },
                            {
                                        'name': 'ǮƐџŉȆðF˟ϰK½Éԁņ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            78154.08266099464,
                                                                            908887.1407859414,
                                                                            122374.26969820072,
                                                                            29846.986736855484,
                                                                            736566.4652605493,
                                                                            479616.92662754946,
                                                                            537365.5396974329,
                                                                            12271.051783828007,
                                                                            25420.23509175454,
                                                                            662441.7749422722,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʨ˪ʲϗԖАӾϧǵʃˇƍ\x98ҀЖǦəɀġӱˑʢÅпћӫĴɍƓŢ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212252.572074:+0000',
                                                                            '20220526:212252.588361:+0000',
                                                                            '20220526:212252.605786:+0000',
                                                                            '20220526:212252.623676:+0000',
                                                                            '20220526:212252.641839:+0000',
                                                                            '20220526:212252.659496:+0000',
                                                                            '20220526:212252.676497:+0000',
                                                                            '20220526:212252.694124:+0000',
                                                                            '20220526:212252.712157:+0000',
                                                                            '20220526:212252.728335:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЏԜϡȗ\x9bƜ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǒĺǎͶӲѽԞ˸ǎϦ˓Ò˽\xa0ʠɇƈВǢĉлǤɰЭGɶйèɨ˙',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ÎíƼ@\x8aӐŀЏ˧лҒʕЏɏФçϢŘLćə©ȰʵľʆÈŔίҚ',
                    'message': 'ȶҬ©аӊБǢԣȵȎN[ѬĠѱ˳ônӬѴόӪӂƸ˥ǁǔзёИ',
                    'arguments': [
                            {
                                        'name': 'ȲƪԡԜ³˺ȝԆҊĞȁІӥš·Ȅ˄ǯѾǼԇӄҊ6',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2385493599916676727,
                                                                            8120815757535736116,
                                                                            5154374014252799802,
                                                                            2633013959215579177,
                                                                            -5201069922820064395,
                                                                            4993721973066640191,
                                                                            6523541028369174392,
                                                                            4632177598156663138,
                                                                            1487841396903548920,
                                                                            -4278494682388959724,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˺РѬѺ˪Ú´ƀĔԠ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӲlвҙͽǿRǽȄȤÑǛҗҋĐŴʝʹɏюӓɅ½ӏǀӢѪ˰Ӟγ',
                                                                            'Ƭɶ˓ĝħДӿŦˏƊ˦UIɋĩ\x81ϱ˴ӉΟѤϢ˜ϰʭĐƼɍоȃ',
                                                                            '<b҅ψұuԚÚLŇϳęӳԣ0ś"i8ͳuřÆѻRҽͲӥϲѿ',
                                                                            'ʃϔͺӳҟћżҗŧˉț±ƟƈˌԛƒΐǪȌɗӬʉνԟȂБ˭ҧ\x90',
                                                                            'ҒȼӗЄ\x95ʪȳЖRѧȩ\x94đĜӡ_ɐɣQѷ|˯ǣΟʍвХϯӳɌ',
                                                                            'ŊĭƁwźsΨԏļĩҦÕ\x8fϗϻ·ӫōфҍХWvӞŊƈЇǚӛѱ',
                                                                            'ȱɳˀ˳ɠʶ҈L»\x92ưZőӏшͱЙĴҔaźЦ\x83ɖĂǄĳξδϷ',
                                                                            'В˚ѴΧҒҨ3\x95ϝfŖȖʅĸԮӞXЯѬȩ${ɥϑϰđƩˑƣǤ',
                                                                            '˒˗ƕȱɟȗΣ\u0382ϿѶҨВӂƜ·Ǎ˳\x85ƣѾԡĈ\x84Ğêɟæєҕù',
                                                                            'ǎʝ\u0381ǆЈ_*ϤÖНŷΐȂō¹¬ȱӣϽӗ¸Ɯƪ˚ɟê˕ʨа"',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ТюȇɘаҀƓɘǉȗ±ǓΙȘrфǘёɩAСȷ4ǒƢʁұӘԅӇ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 69698.51212215671,
                                                    },
                                    },
                            {
                                        'name': '\x8e`ǲ¸ɬѴʬǴƄɘȚђǄrχԤҟ\x963ˏДQєԠ˽ƧǾѴφ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            712590924294708330,
                                                                            3126306370536213290,
                                                                            3943293800611771974,
                                                                            -8065122219467879079,
                                                                            -6260124026667803282,
                                                                            -5780894546593543579,
                                                                            -1946370741029860385,
                                                                            -2054670319890651799,
                                                                            8683018830996125792,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƎÒʏGҹ͵РǛƒϟԅƞЧ·ÛƙɩЋÑřMψΰȒʪƭэΔˎԡ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ŗ\x8fŵҹsØsĩɶʑҔƁêh˧\xa0ԃjȜ*ŪÆ¯ƖΠżԒх¼ϯ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6369202888527416610,
                                                    },
                                    },
                            {
                                        'name': '҆ƌ¡1ѫсӽĉƗʪΕȾƔΔŭϕӎ˃',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            188357.89024325297,
                                                                            81615.74091350511,
                                                                            967143.969387569,
                                                                            915709.5301634171,
                                                                            276888.31840818416,
                                                                            267256.7365898682,
                                                                            463881.8698325339,
                                                                            -22332.652359201675,
                                                                            179205.06991347607,
                                                                            462650.26784703427,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҢĐ\x92Źҷ˗ʝ3ƾÛӧҤЪτРƍïŊϟ_<éVĩӋǐǳƬʛȇ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212254.247407:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ИĭфôČӠ$ƊӕȌькÈΩԆƜѬίԉӉ ƣ\xadǢͰ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212254.313112:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ôȗ˖ѼϪѥʺǊ+ǔɃ¸ĊʷƴǳЉɠӬͱCÐшԬӻ·ȒӈНF',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            147399.58721978817,
                                                                            255104.0861267778,
                                                                            434514.4257002516,
                                                                            625999.2844847209,
                                                                            552478.6903356063,
                                                                            454535.8400891707,
                                                                            810855.6754619865,
                                                                            -73299.61390004517,
                                                                            852833.6433137233,
                                                                            470234.7921244358,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƤoŭрŖ\x9cѷȢȏȅΠʈԣӴѺ~Ơˎϑ΄ưɆǡɔżɄЀ˔Ѭǯ',
                    'message': 'ʤҾμҾÌ͵ϕϘɞoŪŷ\x9eĄì\x8fΌȶŨʾǪħѣƻѦЇĸźˎЁ',
                    'arguments': [
                            {
                                        'name': 'ɌΥÂӧǶ˄ɉɌЩԤãßѥ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5223927814062840479,
                                                    },
                                    },
                            {
                                        'name': 'Y\x8eϡʽҦ§`ǐ§ԎӉʕƔ\x8eˁ\x94ū¯ˈƀ˕ɢůϡ҇\x8fˆҥԈã',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˡ\x90ϸTʺƺƔY5ɢχšƽƐʬœғр\x7f\x9fƖɈȧƨƚŒēϧ˧Ɗ',
                                                    },
                                    },
                            {
                                        'name': 'ϩ||љ˱ђцˬųԁǸϖÕtуͿӟüņ\x8eȗÕ˨ѥʏѠɆʰλǜ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -73882.094033666,
                                                    },
                                    },
                            {
                                        'name': 'ҲӗΑɥҭˤȃˡʯ?mӚǍÚņǓοʉҝӃԃʨҌƈΐюΥɭ\x9eԣ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǠʵɵԎƟӟЎΒ\x88ƝěƓȏľāƙ˅ʸʥǏпʠ˵ЮƼӦ˛˙ŔǛ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 464404.6390749706,
                                                    },
                                    },
                            {
                                        'name': 'ɤ΅',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5915153322851591000,
                                                    },
                                    },
                            {
                                        'name': 'ˊΗԭʌй1ЂƤŖ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ђЄЕӀюvʹţв»ʕȀʺ˻ʜɁʮȊҝԠāϪʣϛ9ѱӦɫѨÿ',
                                                    },
                                    },
                            {
                                        'name': 'Љ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6660060141376113478,
                                                    },
                                    },
                            {
                                        'name': 'ΆMğ˸ɁǽÊЮѾӍʻϜˌ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'êӿń˳ŝÃѪ\x9b˴ǭǉǷӇȀƋŭƚу҉ƊАĉԘŕjԗÐҜϒӮ',
                                                                            'ĦfǗ˚ĎlξȷüĪƘùϗҏĽϣźɆҖТȲĭǂȹČРɕЩϹǢ',
                                                                            '˧ƅɾ\xadƓԊӊјĝɡӀSя҄βÂҔѭ¤ԢƢ\x8cʄηϿЗŕԚ˳Ф',
                                                                            'ӱǧˇԝ\x8fϴκʦӱơРǔÈӞƇνƼŉȿ˦ұ˳&ǗÔĂͳμzӊ',
                                                                            '\u0381\x8dԃ<ͱżǒӷ˰,ѦљԉγԚοÌ\u038dщʩ\\ȢӂΓњſҥѭʭё',
                                                                            'ɇ҇ěɾѴ«Б±çìƱɐȌԫВǌĚЏщʋӺŷƈʆЦΥ@ɺӚ_',
                                                                            'Ĵϖи²ӎʺΩʒ\x97ƿћɳˮȉɠӭŭ7ǢӷͳϔGæԜÝɆǀԕǉ',
                                                                            'Ϊ˃ĞϽɻӖ>ȫ"ҥ\x93ȼƲí3ҡԗʹĝҮЄď7іԀǩĕ3ˑ¤',
                                                                            "ԏĜĉȱʱȆ͵ӣȹԏПüŏ҆'ΣюūF¢]ˆƀʟèИaϘȢ\x96",
                                                                            'φѨˍǸ[Уԛ϶ǽӓʗɜЭϱƆ\xa0ϫˢәɓɺҧԃ)Ώͼëѣϡ¾',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŹÉțǶʹѵ͵ІƋƒǍԡ«ʳӰ3ĞƺΎ}˜ŎϮɡщңД҄˲Ӿ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǆ˔ĘȱԦƆѐǴНZ҅«ǠÌȧϺēƳŗʍ)ʩ˽\x80Ўӷ\u0382҆ɶƣ',
                    'message': 'Н˞ӌěɳό˛ˤïҪ\x9aɹϡƄ\u038bЙlԅӐþюȻȞˋȮàϺжǅϥ',
                    'arguments': [
                            {
                                        'name': 'τÍʐļҤϸҏңХŧćŐƣrΣ¾ŐdÌӣѤϱØɖçêÍ{\x8dФ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            685416.6435741343,
                                                                            895072.3956653763,
                                                                            904702.0293898492,
                                                                            454917.79591705475,
                                                                            784149.7029420808,
                                                                            661856.5369717359,
                                                                            148260.39627432125,
                                                                            710326.286340748,
                                                                            863174.8931684671,
                                                                            333400.54208708816,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƫСÍǕĿɪʖΣȷĊӫԭҺłƔС\u0383ʄΞĿʌ϶ǢǱOƚͰĤ²\x91',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212256.060244:+0000',
                                                                            '20220526:212256.076957:+0000',
                                                                            '20220526:212256.094480:+0000',
                                                                            '20220526:212256.111845:+0000',
                                                                            '20220526:212256.128542:+0000',
                                                                            '20220526:212256.145234:+0000',
                                                                            '20220526:212256.162397:+0000',
                                                                            '20220526:212256.179455:+0000',
                                                                            '20220526:212256.195885:+0000',
                                                                            '20220526:212256.213963:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'fҋЬǩӫȽ˖ӕ"Ψ§',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212256.350138:+0000',
                                                                            '20220526:212256.373417:+0000',
                                                                            '20220526:212256.393013:+0000',
                                                                            '20220526:212256.413623:+0000',
                                                                            '20220526:212256.433989:+0000',
                                                                            '20220526:212256.453972:+0000',
                                                                            '20220526:212256.473442:+0000',
                                                                            '20220526:212256.493561:+0000',
                                                                            '20220526:212256.513200:+0000',
                                                                            '20220526:212256.529596:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӳƙѵς\x95ÆϿΙɴуÉφğʪkŸβн˱ȚΞӓКϾѹЗ˽ÁǸɖ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            207951.76729597047,
                                                                            800202.1736194773,
                                                                            531558.1215884512,
                                                                            454717.7069203509,
                                                                            517228.9616900635,
                                                                            510063.59673695324,
                                                                            978062.6825690588,
                                                                            702245.9669988935,
                                                                            541013.8560037473,
                                                                            644604.7922781137,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'сŋǪѰǅԙЊńũȑҸҸŚшԨƇΥ\u0381ȯÑԤΙԉɔŏӵ|ŋ©É',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˙ғŮАӠG˷ċǣҏьѾψоǒƔÁɾùɒӓ͵Эʷ˲ΥҲĉǀˏ',
                                                    },
                                    },
                            {
                                        'name': 'ŭİѢÀƘРčɶрҀǄԝȜЗƍǏůҾȋŬԩЫр˫ͷ˙ӼϟÎˠ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ΖƠҙǷ¾ȿžƑ¥<£ԎɢŢӤːʭEԝǕƹͿzü҈\x96юɡѪζ',
                                                                            'ҊԮЪ\x88χƘǺ*âѶːƟŤɮʾԐȲұпȞ¦ҴϻǮΟϹщʈċŜ',
                                                                            'ϢǡǵǔĻŨѰңǹΌʄéǊ˱ӾĈшӓʕљȃрɟЌαӱèɑʞϧ',
                                                                            '³Ҝ<ӀɴȃŖϮˊыȝϚЫΩΈŖăŠΆЄŖĪƢƦӷηӊВϔɊ',
                                                                            'ʧʖΏoԅȩТ\xa0\u0379ʝüʵͺχĿƼəԋǖǕǔĻÉѸҴ÷ˌ/J\u0383',
                                                                            'ÅћԀ^ʭӤ\x85ȗɀϥ\u0383ҋъыӼɤТɩìʷΰȡƆÐƃĢʾήưѼ',
                                                                            'ҏϾā\x8dʧтϙϺƊ\x9cϟʵԧԬӯĭҠ;ҞӍԢÊǣƥТʋҴЈíŃ',
                                                                            'ȋҳƩӣɛԋҋƷ»ƄԮʄʡҫѡʦȻã$ˣӽȑßƐŨX÷ԍϺȗ',
                                                                            'ĥǓǬͼҩǶӍDѿɹťɬĥšĆpÇ\x94ΰÙҀ˭ьéϕ¼ÇԫÃ\x81',
                                                                            'ϸǫȻĩ\x8bƒ`ʗƂͿ$ԑɳѨϠƀϺĹϝDŨɿϬʘө>ǧӹǾϕ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ûͻȪχϲΕҭĂɹӌ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                                        'name': 'Ʒƍυ˅ϺŕұĬŭҙΌ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2028475933972284040,
                                                                            3138626272648362523,
                                                                            2627278530216095796,
                                                                            -4756257777564698543,
                                                                            -7315407703606236583,
                                                                            5179163698718264221,
                                                                            3322083360425366447,
                                                                            1018312090101908405,
                                                                            2182565664374481588,
                                                                            -8642333545344398783,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'łЭѲĎʨœŒß\x80ʖ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ưɫL҈ϜŠҊӥgЩǄʽȍcʟԪЩá°ʰԈ˹ϿǓтκΎǚŻȚ',
                                                    },
                                    },
                            {
                                        'name': 'ː',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5992870788760165336,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'τϨʸҔтĩőȷÑɯ+ѢͿƵϹˉxӥ\x8fыϸɏɨƛϥƶϏǢЪǑ',
                    'message': '.ʲɒІӉІ˷ȕɍ˅ʊǸǸz˷ǦñɀğЖȂȸƁƄЊƇεđ%Ǿ',
                    'arguments': [
                            {
                                        'name': 'ΕӮīϾϏlҔτԘCȖťïU\x94ȳiɕϓɖLɮЊіǝŕ¿µ˹Ӽ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            852101.5329435484,
                                                                            511159.47063758003,
                                                                            370572.4859863336,
                                                                            524977.823543711,
                                                                            721983.8363036312,
                                                                            402790.67728540755,
                                                                            713093.1969777001,
                                                                            381054.4518837399,
                                                                            321923.3843130268,
                                                                            135696.05819196338,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '>ȎҺΕǸłSēѶRӄѱϪʵ]eӅμϴŪ˙˦Ұļϧ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212258.232379:+0000',
                                                                            '20220526:212258.248447:+0000',
                                                                            '20220526:212258.264387:+0000',
                                                                            '20220526:212258.280766:+0000',
                                                                            '20220526:212258.296329:+0000',
                                                                            '20220526:212258.312248:+0000',
                                                                            '20220526:212258.328083:+0000',
                                                                            '20220526:212258.347213:+0000',
                                                                            '20220526:212258.366827:+0000',
                                                                            '20220526:212258.383736:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŒϛϐԟãҽŎ4ŜφЗϢӰ͵Ʋ\x83ĲʐъÈϏȃ҅ʑǢыˉŉзS',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʮʵɿͺúӻӮ½ѬӗɎɔҵƸʬ_\x8aԠ£ɽӠǌȉӿŧ˵ƃvǰǏ',
                                                    },
                                    },
                            {
                                        'name': 'Sѵīоð҄źȎɿчƼӲ\x89əGƒϩɱ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212258.532505:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѿʠɝ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ĩƔˤҿīĶçӋ˗ȶ˟˩ȗЩб\u0380ӕҪѻħǡ˫ƜŲͻżșɃϖl',
                                                                            'ȾӱуғɭӕƓτƌǋĮэƘʤȌδʓԍƘÌƔīĎĕǐ\x82XgCϪ',
                                                                            'Ŷʐϋҧĵ%ʠλюĭÉшƠȵáx˻ŕԄ>ʬːˉΖӹykԏŦz',
                                                                            'ϧͿ±ĉĹϭǃEфˀƠ\u0378ԖԖΣȳԩƞɥСȢǾͲϹӭϼкӑ\xa0á',
                                                                            'ȷʌ=ǣʏŊΌǵΣҘΣӽРǦǖκҥ*ԚΨҞ\x8cˋ£ȭ˖Ԙқңû',
                                                                            'ұÕѸΈҡͶʨѭӢДЮˊƚůϳʻѼɩоǑŅъǙ͵ĥǪвЅӜÜ',
                                                                            'ѓčɼɅɓCǕĤɓˋŴԨ;Ґ҇ϊŲ\u03a2ɂƙăԜŵĠQКȮԚƒю',
                                                                            'Ȫ?ƪӿ$κ˶ʔʡͻF\x93ӸϺӅŤΰђϮʓѽĜʳA\x81ԖĂïAѧ',
                                                                            'łҐ8\x95āʥӖϖȈÂϠ¿˖Úǜʹ˕ǹIˌ[ϲÐΘδԭɢæѹɏ',
                                                                            'ӞĺªρҜ˝ҶǾɘȨЂ2ΚlɈӓЭҥŃ˼u˂ˣЖ͵6ϱɎĀΨ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "'ŏÖҙЛЈșŻ+<ΖĪʄԅ˷Ћˁшοǆ",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212258.834298:+0000',
                                                    },
                                    },
                            {
                                        'name': 'òǕ(˶ŞźȈΈŢǺȡFψ˾ìșĴ¯ɡǅƴÂΉ˃rʔΓŏêÝ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212258.898732:+0000',
                                                    },
                                    },
                            {
                                        'name': 'лйԭȷȨˮыˍԧͲʽԒòХÒǗwµŊżdЛ΅ɀϣ˖Ηɐ«ϳ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -602760106698605122,
                                                    },
                                    },
                            {
                                        'name': 'ǤĤǰдѱġͳҷԉņϑǸǔԎIȄˑȂJ˽ĽƸѡ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -443003353521477713,
                                                    },
                                    },
                            {
                                        'name': '\x98ϺЌɿ§\x8fοšôʏʨЉ(Ȫѩėů',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6411020431111119159,
                                                                            1293989010309868294,
                                                                            -8930078065199057419,
                                                                            6598028523297085871,
                                                                            5286856882492976598,
                                                                            6871913615567959227,
                                                                            -6785352114154487388,
                                                                            -5362885662351678739,
                                                                            2100224540369406882,
                                                                            -960364937986375866,
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
                    'catalog': 'Ǭσ',
                    'message': 'ȯ',
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
            'identifier': 'ļ~ǎřɐ·˙ɿʘάΖʙɏɋџƌȺȔɥϹϵƱԃ;ћҩʕ˅9ʃ',
            'categories': [
                'internal',
                'network',
                'configuration',
                'network',
                'network',
                'configuration',
                'file',
                'invalid-user-action',
                'network',
                'file',
            ],
            'source': '˨ɹѽΔμБĻƘĿдўѢ\x8f7ΰҋԭǝʍәӸΑ˥ң\x98ѨɐąȤӡ',
            'messages': [
                {
                    'catalog': 'įӃϼʌԨÝʄɔɞ\x85өİ&ĵRЧӉľ˶З\x7f˦\u0382ɑèLģӊпģ',
                    'message': 'ʗБÏ˜цђŹƚÌԗĞӴdɺ˅ʅȣˆɆʯӰĞɽƩʱÞˊӕĄѦ',
                    'arguments': [
                            {
                                        'name': 'ʆЀ;ȅȊ˧ĔʷǣхѓăԠĄʹӀrήȣȔϡɌрЏ˰Ȯǻ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            703748.2498691333,
                                                                            290494.61090347683,
                                                                            269566.9178050889,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȠȊ\xa0өʱˠöoϐ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -655361638163026142,
                                                    },
                                    },
                            {
                                        'name': 'чн3ьӵ˱\x9dѨƂŘʞʄǞȧ\x9bЩŦɍʼ͵!ΪıǛĵʶÊβЂ˙',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            701807.2745042285,
                                                                            549985.5394712875,
                                                                            658401.7975411707,
                                                                            790869.8359936536,
                                                                            593929.89311051,
                                                                            830775.2754362909,
                                                                            274263.92305039405,
                                                                            483913.252343789,
                                                                            360477.5896913487,
                                                                            -55902.766624032796,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԦŽɖZЄ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѡхһФғѨΑĜɣ\x8ePЭ(Я\x94ū2ƏԣѾCÔ¡ѡ¹ćƁђȱƣ',
                                                    },
                                    },
                            {
                                        'name': 'ѦŗҚµʳ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212310.150526:+0000',
                                                                            '20220526:212310.166199:+0000',
                                                                            '20220526:212310.182792:+0000',
                                                                            '20220526:212310.199874:+0000',
                                                                            '20220526:212310.217118:+0000',
                                                                            '20220526:212310.233995:+0000',
                                                                            '20220526:212310.251735:+0000',
                                                                            '20220526:212310.268338:+0000',
                                                                            '20220526:212310.284913:+0000',
                                                                            '20220526:212310.301587:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¶xĂɳɰӖĵõōɒʍюÎĶʗї˪ѿԉƜǤļƽрҤϐʑоͰ˰',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3001093574861821264,
                                                    },
                                    },
                            {
                                        'name': '˻ɭƫʖӍȑȉҭЈ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -26165.461183388295,
                                                                            941496.9843096389,
                                                                            648179.9039793566,
                                                                            211136.37221333187,
                                                                            735449.7797854608,
                                                                            945614.8986395281,
                                                                            535305.8611920256,
                                                                            314065.9807804647,
                                                                            736019.6341128238,
                                                                            973041.4965341755,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĶΎãҷĵԨԊӹÒԒԇϩ˧űĜТ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƠXΈȦôҪҹȂ˥ɢPǹƜ=ŷȜҕƿ]ӼþGӃΕӂҢĿÊ{θ',
                                                    },
                                    },
                            {
                                        'name': 'ˬŗʅTǈċщωґӗϳ²ǼħƼéŀȈƍӡŌĒǭ&=LÒZžо',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            311048501023796772,
                                                                            2252195576088038291,
                                                                            3899155217270728197,
                                                                            -176143659530117230,
                                                                            3535803946031336363,
                                                                            6160020023927797969,
                                                                            1695004527768452267,
                                                                            -3391044561638317142,
                                                                            5249794685105844512,
                                                                            -2474710577480960867,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '|ʺΝ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7668645854671501833,
                                                                            6415617200136394734,
                                                                            6804901842545369832,
                                                                            -2419187590891980929,
                                                                            -2977955036568447756,
                                                                            5870995454841011606,
                                                                            3729648566969473009,
                                                                            -5855725567863598280,
                                                                            -1291937616673023324,
                                                                            7143540513409162626,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȩЕ\x9c˯\x90*ѿϡҢ»',
                    'message': 'ɤǭξˉҶͼҗΉϋʤԞŸȘǔЂƝɃoƉͻǨŻӜ\x8cǈϑш¶ƚβ',
                    'arguments': [
                            {
                                        'name': '҈ȻůˍѮҦū˟ȕѲӉѰХğыĄςӸȧžǿ8Ӌ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8719347576863488071,
                                                                            403887322508078539,
                                                                            2050359995364413025,
                                                                            -9069186472620422138,
                                                                            -9031951983979298733,
                                                                            -4315559662312653505,
                                                                            -1311904860065000180,
                                                                            -2137791873976356843,
                                                                            2566549711707083550,
                                                                            -277763723917029300,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'îå',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212311.742514:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÚƸΘCŵːɫ˙ˬȨĥԦ\x91ġѯÀаˤŜ\x9fͿϊȅ.ӴbÍʘǭy',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 344194.4756047591,
                                                    },
                                    },
                            {
                                        'name': 'ɩ;ˎͳ|ϏÙҽǷð¾ѧАϙȈԀϴʣ˞ϜѡЪű~\u0383ϣ˄uХϔ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212311.880674:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʰρЉȗïbŽīΐǃȹƌφɒλDȒҸб˲ġkΛҼ\u0381æŰɋЂϘ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6902440877788859348,
                                                    },
                                    },
                            {
                                        'name': 'Ŏ{',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ņ\x99ŭʽҷϭԚ˛δ˭ʴ\x9a[ϓʤԛʓƅ\x8bӥƬЈЩωʝƵȈњƋѭ',
                                                                            'Ϣ˱ȨȳŗǫĮӰ\\ÃßƇƸƉѥtʕѾyȦҙˤԅʹǩӖċƺ±ë',
                                                                            'иóҌźϙǚϿӇӋƩˈˊϑúӠ®\x83ѹ¯ϢȻʮĦŉԞДѝćΎӏ',
                                                                            '$ҔҡȌӅЀӏгЗ«ȸ%ӔǑ°\x86ǛзɆȇŹ˷ƟǆΰOԧΞoϸ',
                                                                            'ҞΖĎȂɕӖͽʳԤuЧЃƠ«шҼƛԘ9ϬȦćΠoÝκȅʻǘä',
                                                                            'œÎБàƔǮӕɂʠǏĔǻēŏŸļ9˖ӜȱʣАĞȖŎώӐɈ϶4',
                                                                            'ʸƘӏİYͷǌԌťϤ9ǈͼUɛʏϢΪƾ.Ԅ#ȬѢđ®0ΉŌП',
                                                                            'ƦòѦɣuʙɋҩÖƔËеȚӬяѫ«ȰјȦԅϱÿĹ\x8cȪʡěˉѧ',
                                                                            'ϔǝͱѮ˭ńŅӠ˄Дŏˮ{ɣ\xa0ӳʏĦԏŭNłԂ\u0381ʛɞёɫєÃ',
                                                                            'ӱÛʹҵɤɲåȵȔɢɷüʋϘчČЍʪӻ˜ΝͽʈèʄĿćКǩԃ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'кĔűӜʝɌӷ1ωˋФѸızҭōÖϥͳ3ǁȳŷ}ȼ8ӺлŨȦ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӧȥҒύπʡ\x97ēǡĒ\u0381ͳԗѼϿŭβǗ§ǯŔ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212312.550143:+0000',
                                                                            '20220526:212312.567001:+0000',
                                                                            '20220526:212312.583665:+0000',
                                                                            '20220526:212312.600458:+0000',
                                                                            '20220526:212312.617406:+0000',
                                                                            '20220526:212312.634876:+0000',
                                                                            '20220526:212312.654601:+0000',
                                                                            '20220526:212312.678775:+0000',
                                                                            '20220526:212312.696060:+0000',
                                                                            '20220526:212312.714336:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӇӝışȍřőĲ\x7fāˊĦƦ˃¥Ԫ&ΝәʩΦ˧ÆƜүЯū=`ҁ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2784737374881724555,
                                                                            7612446466353937831,
                                                                            -5194687405896480768,
                                                                            -8481109089218989889,
                                                                            8848296611427450200,
                                                                            8943272632031162906,
                                                                            4282979511212314822,
                                                                            -8736246815704071775,
                                                                            2601621205966059421,
                                                                            2114707595171551853,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʙɿΊʏˤǸĩĪ˥ăàҫϲƊʋѹđԀЩτ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˈÚϬíťыҜсJЛ˾Р:¬ǗŃѪʙуҀΈõ\u0379ǪòǹŜĲȣļ',
                                                                            '§Ǳ\x99ȿΧϒɾʕɻȵӉӊĕŋɐ˓ҌMԚ·ɣғΖ\x83ƉӟŬďbU',
                                                                            'ƈÆķ*ȵ9ȑƿ(?ƿҟг҂ӱʆӤʐǧúЋōӜĂLĻ\x89ń5Х',
                                                                            'ĤŸXǂѩѐZ#;ϣЃŎϮǵœҥjįӷӳÝʻ&ǦĎǔÌʑŲЬ',
                                                                            'ɬʠпŒ˼ӖԑԃŕQƷũʈÙ҉ԗȡ˳Ưϻф£ШҘҍԑcʑǙÜ',
                                                                            'ưÔƆɫȜƐЦƆӷӋˠɷ9Ў˙ԎȾ§ŶΟʸѺγβņƊυĨ~ʈ',
                                                                            'ˌƅћ\x9eĩδɆϼµʰãъȯʓєюɋcΎî8ķЛМ]οŔčğϑ',
                                                                            'ιϝǸЮ϶ϤʿԆɦİŗώԦˣϫ҂ӦͲӣÄщʜНҟʆYҸ˱ϖŢ',
                                                                            'цŤЖљÂ·ˇƴОʭΡ\u03a2ƹўЎ`ˊʖĩ~ßӛтŚ"ǤīʛK±',
                                                                            'ѦˊЛѐԬZɉŜĴϭ˶ЊǀÇEdϨпŸϪϫŭ:ŊғĖϗʻҭѺ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ν\x94ȲȄȷƾ҇˒ʮ˷ƲΚEń\x9fļPʽʰҤʉϢлƲɤʷʿǎEʳ',
                    'message': 'Ο˶Íɻʛӣϧjǲˌ˜ȂčΰϜyӘ˶ϣďʀwӇӤԠѦǡђЙö',
                    'arguments': [
                            {
                                        'name': 'ӈɬŬʢԋˊ\x95ӵԈ©ҞʇőƟÌ5ϗ\xadǞʆ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ºԞ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2961575401004263521,
                                                                            2684986198235325968,
                                                                            6501914347923848032,
                                                                            3801706193915325899,
                                                                            2637806637217648563,
                                                                            6202460568603155363,
                                                                            -5875520732464154854,
                                                                            -7358498127128199595,
                                                                            -2235271260446923785,
                                                                            82392399635631549,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĉÛÿGϚĖĚӑ˧ѧХД¾\x86ҟÕÛѳȃ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ғŷƵԫ"κȾϊдӴϙʭԞˢѮɱƩі\u0379È3ƜóѹӿÀǔԘӣҰ',
                                                                            'ԭӏΘʝЬΞȨѽƊȮũ]яѻŸ҆ɭӟʢʢӹǙɠʌŪǫѺ˂Ҙʌ',
                                                                            'ɼ\x8dsнɋĞЀŠѻԩԬњМӢϾÑ\x9aԨĝΒǭԧÁŔӰϦɋҚʾĀ',
                                                                            'мǟŉÂ\x82³ŀѫʙчҟĪǁϯŹŗrŵѫж;yrƧǵ˼ƳŮA¹',
                                                                            'ɡЇǟzúčҎяÛðÕ҄ϱǕӈ\u0379ϻΔͼϢƻǔ˝\x9aҲν\x95ȓȧȜ',
                                                                            'ʣCȦϚÜĩ˩]NӯӦӈϐ\x94ӈțǅѬMǄǬΈʅӜ˓˾ɑˎӠ\x9f',
                                                                            '\xadϵIӨͱƳĦ\x9eġȢҬŪǄΏ}ѥ\x95\u038b˗Ϭ,ϯӰŠɮĎΊȮҒÉ',
                                                                            'хТђBҨϣaɷȏϵƕƹɉє\x8dϘƏƟ҉ņәʅϏϗ\x9f¬ƜΗǿѤ',
                                                                            'ŇɣȂɇɧˆìNɬêƻѬєȥȩˀȚϩKÊ8ȱɔȍƿ0\x87Ɗ˹ɂ',
                                                                            'ɭ\x92UŵпȠԉƠӋ˷ˍǮʝі¼ˮөўɴƏőɦHƵͰƣ¢\x80Ѫԫ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '8κɐљѸ«ɈƕƼŔ˙ѿж˩ν˕õɨԫ΄ÂĳӄҷόЮ͵%ԆǾ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ӿχh7ͺρξħΜИѴɅ¤эь˝\x90ǿdőɈϩΏΗʦс\x8dưˇɪ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5648779170720420960,
                                                    },
                                    },
                            {
                                        'name': 'ԉʩŒЙzˡŸ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3459860454490169279,
                                                    },
                                    },
                            {
                                        'name': 'υşΰ\x8aŎʖщԝœĚʷ\x9fɔ$țǶ1:Ĩӓ¬ŪúȎÿǻǗҴǅƀ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212314.226547:+0000',
                                                                            '20220526:212314.244526:+0000',
                                                                            '20220526:212314.261987:+0000',
                                                                            '20220526:212314.279060:+0000',
                                                                            '20220526:212314.296352:+0000',
                                                                            '20220526:212314.315005:+0000',
                                                                            '20220526:212314.333268:+0000',
                                                                            '20220526:212314.351787:+0000',
                                                                            '20220526:212314.370555:+0000',
                                                                            '20220526:212314.387159:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǟĖǺϮV\u0381ɢϴΣĝԬϒŅÔÎǇУ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȖРҬϐϰ?ЈԖӟŵһƳʵļѲͳӸĚԭ˯Ą',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7920776723295109465,
                                                    },
                                    },
                            {
                                        'name': '0˷©ΒŮЇőø¹ɍ;ҡƪŦĜʯѢŸ®ǵɤĎΔҚЄϕіԛ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ο˴ŧșЀŶȚҩſǿɫѵŻ\x87gØͷȩλҘ\u0383Ӝ4ŷиxÊӿϐŚ',
                    'message': '\x90ȡҼΣκӮŧϛӢíŵSɪ\u038dԣέĦƴʫϩӸˡ\x8eӃËԆο˪ʮā',
                    'arguments': [
                            {
                                        'name': 'Ŧˍåпҍ·ӲHŶǼţɓΧăҤ\u038d˕ЁɐͱҘǫǣòšЈªʄÀ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 870288.9117663382,
                                                    },
                                    },
                            {
                                        'name': '×ч6§҆ϼƚӃÙſżϠΊĨТиȔ˷iˁѥɧ˗',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԣΣǗЃɠŗſѨĦî`\u0378сҋșÄƑ˱ӸƹӀӒє½ԘЩɼ\x83Ӭғ',
                                                                            '\x97Ȉ˩İΚÙ˱¸ЖʟȞȁˀȉѪЂʴȉȌǍԇĸҭtҌϑĐ҂Ȅˈ',
                                                                            'ăɡȼϜɤʆɆ˷ªԍ҆ӸͱȏͽłЪV[ωѫɱŗƞӦӇ\x9bÑЦӫ',
                                                                            'ƪSƵ¬ƯƬ\x8cèĹ˺вҗʛӮƘŬӞĐɮ˝ĪƥͷώgөԧÃŗǶ',
                                                                            'ь)Ҷһ\x91Ӳ"ЅЀŬ˘Ιɭ\u03a2ϛesǫ\\µŹŘǯɲʗqřϞ\x9eϕ',
                                                                            'ǾŌȼ˫ҝњ҉ϸƼǶ»\x95ϒåΞbȍкÏĈƌ:G:ԉʳĶљ\x85ʒ',
                                                                            'đж\x91đʋ·ӵ҇Ɖүšķųӿţϲ0Ƙʛ\x96άµʴÏˎ|Ưϐŀɚ',
                                                                            'ҠÌΆԣǣ5jģԘʨϥƙ7ЉФϮĘγŅƾƳƙŐšďƱȎɨĿӤ',
                                                                            'Ҫǝģż0ǛԒѤʯœ$W\x87ϪǾȅƼǣǦŰЍФ°ӐЀѢèƜӘԂ',
                                                                            'Ѹ7ʮÝɺØίžѳȣŹёõīϓ/ǳѮʋŨ\x90ϕцʻțħEÊӼԐ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǝηϞ³ƁҲӷԃs\x99ºˎßӵ7Єʹ;Р\x87ˣǟ¥ҢӓԜҮČƢĬ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƇřäɮʈюȲΉʢѦ2ё®Ʉ҇ǱѺ\x8aˬʇƞˢˑeEώб˝ҷʰ',
                                                    },
                                    },
                            {
                                        'name': 'ʲ¿ĕίƫϧ}˂ƋϡϛԅԖ¼Ыɴ˚',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 612786.4024110113,
                                                    },
                                    },
                            {
                                        'name': 'ӁȰÿĩɟˏʵǑкǫє\x84чѵµԚ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˴ǪԝóQΠ¶ѾԔѶĠЄ˯ʾƝжӨæ\x92ƥ˜ԂҎӮӹϩҼʤɚ˦',
                                                                            'ԏгӴÜ\x81ϊĐƷƜɗѮɔǶȍӿΏˏǔyбЄĥ҇ƋαƔЦĐȴʭ',
                                                                            'ƸöřϾӑĔS\x8fȜҐϪһϕėŉКȄ"ԠǳԘɢĲâƘŕɥӬӽŬ',
                                                                            '\u0378˙[ƆgɦοȨӒ½ƔЎcǼÜǯǠĘӢsŹʯҊǰʐӎ_ʥȥǤ',
                                                                            '˶mőʌȭăŬŔѽȢʤʾʰËΪɂYɃдԑIԟкɐQȢΘŠѓχ',
                                                                            'Ǝ˲уЏ\x86ҍÖɉϥҴϏ¡ŨǡǬĶƧǟó¯еƢőūӲαʱ¤Ѽ#',
                                                                            'cϫȾË\x9c\x9dɐ˞ͼҜϺΈĤ\x92ƚԍȈпӔˎϩЃȅϿT¹ԖΗˠƷ',
                                                                            'ĥ҇ȭ˼ǾĪэɱǚˬҦӍƐUƉȬЈļtĎƩ¤р˖ŕUȚ˴υЌ',
                                                                            'ԋԬŨT/ϺӟļÙΜХˤźtǑƀʡÖǄȡӞȏλӈɞɷϑѯ\x92!',
                                                                            "ȷÖӁʂљɐѱzј˶ȑҙэɠ ĺ΄βϋfLӛȿҷ·ȭ'Ű͵Ѥ",
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѿӣɴ\x9bːӾɦӺÇӷһҖuȀʌǘѼ§А6Χǡ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6654574330843885355,
                                                                            -8631462978139034053,
                                                                            -7139700958555094959,
                                                                            -156129676879946550,
                                                                            -3496577314610921844,
                                                                            -7317194860260126100,
                                                                            -9192523044879392493,
                                                                            1054832836614313872,
                                                                            -5936411077595722914,
                                                                            1013955906906506568,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '§əϩԙŜÿɥ҂ǰǿΦơҙǷӫ϶\x89϶ҕ\x8bŕɷΛƺĬʾäșÀ\x99',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'иԉԬԥӍcǃȔ+˹ҭńӂöȝ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212316.089175:+0000',
                                                                            '20220526:212316.106233:+0000',
                                                                            '20220526:212316.122854:+0000',
                                                                            '20220526:212316.140745:+0000',
                                                                            '20220526:212316.157190:+0000',
                                                                            '20220526:212316.182144:+0000',
                                                                            '20220526:212316.204767:+0000',
                                                                            '20220526:212316.229291:+0000',
                                                                            '20220526:212316.250470:+0000',
                                                                            '20220526:212316.271424:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'EΰqiҊԌԦƫʖȾÍʼȚȧȋ\x7fςȼҪʑʬƚѢī',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212316.376501:+0000',
                                                                            '20220526:212316.395248:+0000',
                                                                            '20220526:212316.416297:+0000',
                                                                            '20220526:212316.435957:+0000',
                                                                            '20220526:212316.455201:+0000',
                                                                            '20220526:212316.475381:+0000',
                                                                            '20220526:212316.494703:+0000',
                                                                            '20220526:212316.515019:+0000',
                                                                            '20220526:212316.534634:+0000',
                                                                            '20220526:212316.554984:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˙ФԤŏТԃɂΧǯĚàʑЇº˹ΚΜ\x94ˉʦȱϚĄьǩИӰ²ȋˁ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 393856.0546839121,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'º\x9aɩйʚȑˀΛÉ˸ȶБǍҫ;ƋζΒ\x8dӯɲбΌ÷ԖȄYԫҁJ',
                    'message': 'ď±Ġȱ´ПԠҸϘȍ¨ӓѽħӱó˅ëЃ\x80±ĔҺϛ#ÖЮŸςӾ',
                    'arguments': [
                            {
                                        'name': 'òϗԎH3ƝìҘψв5ΓЪӌȼˠƲ˔ǯð˞ǥҏѣΦʳѕǿ\u0378ж',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƦЄѢǰϷɮКǒЦɺԣαѤƑʿǌČĠǽ\x8aX\x8c¿Ѿ˝ãŔǻ\x88ǝ',
                                                                            'ԪƠϺƋ~˾}Ҫ5ĽΑѹ.RȾʅɍǣÕɜӖƙǁИЃ˔ύϛ3Ҧ',
                                                                            'ςǬеԕǉřɱʙǻ©Ϣϊ<Ȉ_ň^[ƾōˬǿţΛ\x86˼œɒʾÀ',
                                                                            'ӪƝǯBĔĜÝǲ×2\x94јıðƁХȾϱȰдĦƖ\x86Ƥ×ƂˏϘɜ\x94',
                                                                            'ѵэҺƺԋ\x82ǇɛӁЀҞʉΣЙȐӃĴЦҺʣΡϏŹϦϬˈͷĦΗɒ',
                                                                            'ҝ҆ϗјɛĘԡʵǼҁɅ\x92ŻȿǤǷĝ˒·gȧЖˈѶʬȖΒɲŔæ',
                                                                            'ĽԎшȑɴ˻ӍɁҊѓ+ұɗ˦ʾӐϺĝˁ6ԝśӖDѲԒοԛ¡ʡ',
                                                                            "ɀūОʠӸĞ\x8bЂĦАԫӛгÖ>ϒΗӤ'äɕуҲϮƵ°Ӵƭʐɡ",
                                                                            'ҫΈƵd\u0378ЗЍ˜ӥǷͼƛξEΥӲnʨȣȎǼȃҸϏΊβŨȑӠ¦',
                                                                            'КƖŸӨķ:ȘԤΚІ~ϢЮѹǢɺˁ϶ɻĦħ\u038dȂЉrƤЫƗɀ\x85',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΩϻҿɔӵŪҗ˖WγƮϥőѳɟ˽ӧƫ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8246506698190281302,
                                                    },
                                    },
                            {
                                        'name': 'þҹӥǖɳ˪ЯɟΑ˥ԨɰȮԆɱʏңƛӧKƳ"ЙԫɴΓžǈθɊ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ò˭\x89\u0378цē҈Ȅƨ¡ʾƼΞΝĥƃЂèĴщ˦ĲіDƞЬӃӨєҁ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6344895091140040564,
                                                    },
                                    },
                            {
                                        'name': 'ШȓԢґ\x9b¯˙ːHғŻӭǆȊхĒӊοӻѩǳӬé±Gˤҳϥџˊ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 963263.4640438573,
                                                    },
                                    },
                            {
                                        'name': '^ŽЂҊђ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 470690.2224899642,
                                                    },
                                    },
                            {
                                        'name': 'ˢqǄӆəɥљʝαӎϔИĊϔŕľјǿȗɩ|Ċ¬ċ-ÃԋŊӳŔ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            61726.934516563866,
                                                                            526080.2083941004,
                                                                            658375.2899213298,
                                                                            876500.0560958385,
                                                                            595451.0787079763,
                                                                            986719.2893099589,
                                                                            620968.6815419962,
                                                                            50962.68283004113,
                                                                            633742.5387115206,
                                                                            -66560.21113786368,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˡύŽι\u03a2ҥ\u03a2ʋɯƌԙȂȄӄȾѿʓńq¦¥˼ӧԒÇϰƵӭȆɺ',
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
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˸CȂÆε¨ϛҵԋЃʩʸưɬŪ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 863401068121165174,
                                                    },
                                    },
                            {
                                        'name': 'ӜÚъиK˔ǂ´ҘūźȿɌuɳſɊИĶЯ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɽŦȭԑćˇɞКάЧӴțǻɄ˖Θ\x89RʖΪǵ˚§Ω\u0378˥вȥɵў',
                    'message': 'ƣŨтΡҊëѥ\u038bpњǨķ\xa0ԁΙƪ\x8bҏĻǼҋϵҚþĒģ΄ȣťˈ',
                    'arguments': [
                            {
                                        'name': 'ӚѯŖ΄æâ˾ԪΡϠԢѢÀɇwȩǝ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ԩEïұϊʡΪ\u038bȥӉԨŇѥϿÍζȮwǟ҄ӑЋ\u0382Ǻė҉ŭӥ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212318.379238:+0000',
                                                                            '20220526:212318.399359:+0000',
                                                                            '20220526:212318.422357:+0000',
                                                                            '20220526:212318.443639:+0000',
                                                                            '20220526:212318.464269:+0000',
                                                                            '20220526:212318.494351:+0000',
                                                                            '20220526:212318.529248:+0000',
                                                                            '20220526:212318.562535:+0000',
                                                                            '20220526:212318.593915:+0000',
                                                                            '20220526:212318.614839:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'DϤǷȃϢҟЎ5ѭʧǎöŪmϟ3ƭʻǘͰˑϑӈӜ\u0382A',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ě@ǜɞ¦ЭěӶƕ˖_їԫvԣĂԎõϡȤΧ¸ӟ\x84ȒǼӿѰņѡ',
                                                                            'ʣəǫӀσҝˁѬŌŐҐɏѺөӌˏœĒѷйʃƔǵpԭξÑLӱɶ',
                                                                            '҆χ˲ʀίϵǖĭΎyǮśʥHɻԝˡв˛ͺȈȔȵʖǯđԇӄГĨ',
                                                                            '_ԕӕÌ\u0380ʹӿиђóҤoɄԦʄ˼ФвɜӎɍϭŬщʞλέԋӝą',
                                                                            'ґ±ҼɨɌїŅŒŕѷʦƮШ\x93ĿPԌFĢɇÑΎӌȚ?ǺȀɌ˳ė',
                                                                            'ÈһϏȒЪ·şȚȯѴԏƓѣǻ)žәсĬ\x88уԫàΙϘ@ůǔοĆ',
                                                                            'ʯ\u0380°ʊӬϝÜȳˑ?ъhʇnԆӥǟšӟԎTÅ.ǲһǀǠПǨЖ',
                                                                            'Ȑɋėԭ`ē;Ўԏβǳ+\x9eƖǼɱӹƊËȯόѱłƮҗȔѵΰğϣ',
                                                                            'ɓӳѦĕԑʽŁɡȒηԗ˶ŠňƏǩξЃωӯƚӪˉƾǕė;Ѽāδ',
                                                                            'Ʋɉ|ԝƥŶ\x87ǪƫΑɭɧͼʺғǐȴ`ϣɬтƻЉ1Τ(˫ɩ=г',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʳʞ҉ǬѿďκǛϤŖƚǊтȡғц\u0382˧Ð͵ƬŘҰϑ΄Ɇƹʹcľ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'J҆ǥļÓΔȘÝ\x93ʬžѡˌŗɦԨѫǨϗʃӀ˒ʼɶmАˈˆ\x82Г',
                                                    },
                                    },
                            {
                                        'name': 'ҕСĪɀѻǹΏƲɠ˘ӛӶxѣηҌҴʏÛӣΈƅҏƸìǧѲMЍè',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϩ҃FƭåÕȲʸƜŵӆ)ƧȃȦϔȫȶ4ԥʮńͼɅ\u0380cι´ѕϻ',
                                                                            '÷ƤÒɨĪԢαøЈGŲрɥˢËÁдť˻ƒλɚeɉӷaNˢԅ\x93',
                                                                            'Ԏ\x93ƀŗˎӽӽӥɜԜƁƮѩľɏĒÝԔγΝ\u03a2ϊȶϟ\x9eǀԎϭНƉ',
                                                                            'ʬӘʺԩ%ґ\x90ѵŉϘΕɹǀóһϱͷvEǕɼɶÌωˎыԞϼʺǨ',
                                                                            'дŃǫҒŗΎƗєȌɪƊɦˎϡΨ=ԓñĺdџÚԬšì³IӜ\u0380Җ',
                                                                            'ŘԤȵҨƾŊӁ\x81ÖƄ҈ƯˏŗˑϝΟȮÁÀ˼ȮӲʗύӀ˲ʑǜ$',
                                                                            'ӍŨȌȄƩʦ¤аáɖԠ˷¼Ҡ<ҋғǑζǲрǑǫĽɞǥҺƸˆѝ',
                                                                            'ǁ˕ҢȴƟɲРԟ\x90]ƩӮðŌƹÿωTɟȪ!ó\u0379ˀ·љƝβàє',
                                                                            'Ѓɖ12ʥ҆ȮȡɏȸˬɻÕƧƫ\x91ӽĴõʮӝĕŁŎғЮɰǆ\x97Ǵ',
                                                                            'ľàԁԙʵǱѩϴȞˑȧǇɱγʛȇѿƐϳфʂŚɏȩºʖ˂ԫƨ^',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʻɇk\\ҼǿыЕФoȣѡ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212319.541580:+0000',
                                                                            '20220526:212319.565924:+0000',
                                                                            '20220526:212319.593308:+0000',
                                                                            '20220526:212319.620444:+0000',
                                                                            '20220526:212319.655986:+0000',
                                                                            '20220526:212319.695058:+0000',
                                                                            '20220526:212319.782528:+0000',
                                                                            '20220526:212319.835428:+0000',
                                                                            '20220526:212319.868038:+0000',
                                                                            '20220526:212319.896860:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʩѺmēÇ-čǰƐķǫÂķұԩǔ\x8cʫȬҽˉ\x9c\u038b҇żˎƹƍĦŰ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ˣ˺\x8aѐԌЭĜǒęͷɿͷΣ5Ǆҍҝİò§',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'іґӝҤЩȒ£Ҕ˪ɍɼӸƓтђї˪ɢ=ϔҲӿǑаʯɹԍĝ+Щ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': "ӉͺƋѼӰʷ'áʤΤ\u0382ӒȀӪhϹ\x99ϞΎѿϲҟҹĐϝΒҩ(ϩї",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'JϷĔƋ˽үυɒÒɖμɢã\x80ΌƥΗɟɛȌďӤȣL\\ȸʉƀԝ\x84',
                    'message': 'Fέɍʱ\x98п{Ѻ5ȏиjƷ˨ɛԐʰȐɐϦĿϿӨɒт!ñѭРĸ',
                    'arguments': [
                            {
                                        'name': 'öѴéɔԖЯ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212320.483545:+0000',
                                                                            '20220526:212320.502507:+0000',
                                                                            '20220526:212320.522264:+0000',
                                                                            '20220526:212320.542791:+0000',
                                                                            '20220526:212320.573533:+0000',
                                                                            '20220526:212320.615287:+0000',
                                                                            '20220526:212320.657154:+0000',
                                                                            '20220526:212320.695356:+0000',
                                                                            '20220526:212320.727179:+0000',
                                                                            '20220526:212320.760464:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΤʜԇįȫΌҮϠΛŷγ£µΣǌЕӟΌкϚөԎWΒDцϕрǩŒ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӽΛǀғӐɁF˺ѡԘыɴ!òg΅˝˥ͰˇҴȫҼ;ʩԦә&ʀλ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 11468.080183289057,
                                                    },
                                    },
                            {
                                        'name': 'Ȅ˃ȔзˊԫʺÛ*ȉ˰ӤHƠЩɤȹǛ²ĆµȚ0',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            871990.3840779205,
                                                                            187178.32373646426,
                                                                            515849.0086006144,
                                                                            517415.8171066998,
                                                                            50026.871643847815,
                                                                            434028.2599984399,
                                                                            21500.97228073342,
                                                                            130451.6881435019,
                                                                            530763.1653799821,
                                                                            571980.3097574237,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'еҳɗƮŜȅЀԮˣɍàÓӱғҠϘ©uҦϾɆÐΕ\u038bɛԔѐ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 1041.377869912496,
                                                    },
                                    },
                            {
                                        'name': 'ϓԪʇƄȍŽì=˕ƑӜɀ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212321.428691:+0000',
                                                                            '20220526:212321.449334:+0000',
                                                                            '20220526:212321.468952:+0000',
                                                                            '20220526:212321.488581:+0000',
                                                                            '20220526:212321.508461:+0000',
                                                                            '20220526:212321.527971:+0000',
                                                                            '20220526:212321.550343:+0000',
                                                                            '20220526:212321.570000:+0000',
                                                                            '20220526:212321.601392:+0000',
                                                                            '20220526:212321.664221:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ªϦ8ʡė&Ǔ·ǃзӖǶϮưѣď.ʱŲǾюͼδƝ˞ƗÇұ«t',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2645587359001972070,
                                                    },
                                    },
                            {
                                        'name': 'ƴǏíӘɭϹҒӽªзqſ8πµΰƈÅ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 588707.0934248295,
                                                    },
                                    },
                            {
                                        'name': 'œӛ¥ӨŲĜ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212322.118043:+0000',
                                                                            '20220526:212322.141068:+0000',
                                                                            '20220526:212322.162394:+0000',
                                                                            '20220526:212322.184290:+0000',
                                                                            '20220526:212322.205594:+0000',
                                                                            '20220526:212322.229206:+0000',
                                                                            '20220526:212322.247446:+0000',
                                                                            '20220526:212322.271475:+0000',
                                                                            '20220526:212322.294292:+0000',
                                                                            '20220526:212322.314119:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԕӯəĹӅ\u0383ˏАʭˉИɠυ6ˣмňɖмк',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ў\x8bfˮʘƉɀ\x95ИϢĩfːӂϺ\u038bԊЏӭӒҐ\x87ʳЭƢʞȝûǆӺ',
                                                                            'ӀӋҘӻŻʩˌƟьІӟ6ÈÏϸˎťѿҡEҁЂԩõѸųÛːǕҶ',
                                                                            'Èʰ0\x81ȒӅɧЂΝ1ГƔ˯ɮӒЧЋҌƯŠ_щ˨ΚZЇ˄(ˡк',
                                                                            'ȁ,Ǘиłɻα˥˳ȷøȈы&äǩрɋΏͲʅÛΈΟуϭʉ˴ϩB',
                                                                            'ӴĳşɢÀЅκĒӊBξɠʩ΄ǫə\x95ŠɽǗэE«àѹ˟Ԕӈѵȗ',
                                                                            'ϏǨӺӟì\x7fǺΕϕқɼáōУԥ·\x9fƚȡɎӍƄӿźԣȺ£Ɖʲɀ',
                                                                            'ɟͱԙІӛ˨ĮσӦ\x8cYɱĪǘ˭\\Ć϶ϓǲϕȁϠŃćѦÑ\x90ʐĖ',
                                                                            'ūЍɥˢą=ӧѐðƠЦȭ˳ȁ\x96лĊfć\x98¨нҠ+ƹӦɯϘʤҮ',
                                                                            'ҶĎ²ϖТŢ*êӎӨǆÁůϮҚÍ˄ą¨ǖĿӷɼѸӂǈԪÐ˗\x9e',
                                                                            'ҚɬȳΥϫǶȱŚɽϖÓÜʲȬƸӎļŘðά\x94ϿЪÿЏӁҫÛǪ¿',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': ']φŦЁjůŖ҈ŐƠȃΪ˞',
                    'message': 'ǓѢ|Jë˻ʄȦюхʘԠÀоâɤθƜν_ҤʫʟÈϥÙ˔.uƚ',
                    'arguments': [
                            {
                                        'name': 'Ԣ΄\u0380\x9dҋłǠˇƪƨΕ˽йȱTĈƧɜҨ~țϑǶ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7929931967909133210,
                                                    },
                                    },
                            {
                                        'name': 'αͻĥľƥƙӇ\x98˵»ʿÖʠбɈϯɖ[ņчΩάfɸȂC2нӝҧ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8966534881759239288,
                                                                            -1833591018606069330,
                                                                            -3677777523629504515,
                                                                            5761885121332018,
                                                                            -1010001301130146907,
                                                                            2243078272921831107,
                                                                            7358630724659867019,
                                                                            -1015732221935920222,
                                                                            8588304197904201761,
                                                                            -4589969975848764674,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ë',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԮϸѹκқԃҨʧƒҭōѕɉʎʛҤԏφψƄӛҿ÷˪ĵԫӾЏɃS',
                                                    },
                                    },
                            {
                                        'name': 'ō\u0383(вSʗҗ/ӮҟŌɀҥΥ¨҈ЗȒαîӴ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 78065.88637875853,
                                                    },
                                    },
                            {
                                        'name': 'ҞѥЋ`Еįԉѧƶƽńpʎ\x98ĻӶӛÊѢėΝáҮӀX\x8bˇǄȃ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6726823363029353333,
                                                    },
                                    },
                            {
                                        'name': 'ԏ\x97oáϝǖǾ˵ťğĠǭ\x82ǆҒƌ˂ɛнȾҪӧ˰˼ƲΏȽÖě',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2193712398741582105,
                                                                            -3431076592342653707,
                                                                            -5322048083784947973,
                                                                            4554561467317062332,
                                                                            -2879669028249797799,
                                                                            -1852631538633550921,
                                                                            -4905700077327162163,
                                                                            -6576023740957456857,
                                                                            6326135809846019512,
                                                                            -1810985349346831841,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҇ʃơȯǔҴĖԈ*tǏϏȋǟЇмѥΑĢ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            638020.3996533566,
                                                                            761261.9679815321,
                                                                            322281.41808594845,
                                                                            411899.31812634936,
                                                                            567300.9905566709,
                                                                            542557.0733608266,
                                                                            -39959.951133510694,
                                                                            -36014.46896270646,
                                                                            773164.5918121674,
                                                                            793580.9391444678,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƙĿЏӄƸЃӍԡɍʅΓϓȪƐȸÅʆ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:212323.887130:+0000',
                                                                            '20220526:212323.907671:+0000',
                                                                            '20220526:212323.925159:+0000',
                                                                            '20220526:212323.948034:+0000',
                                                                            '20220526:212323.965427:+0000',
                                                                            '20220526:212323.982867:+0000',
                                                                            '20220526:212324.000990:+0000',
                                                                            '20220526:212324.020191:+0000',
                                                                            '20220526:212324.039355:+0000',
                                                                            '20220526:212324.059595:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʘҋϛԟɟ˹˘ЙĪԈ×νȌŧË˸ûϢӘ˴ŒŮƷ˜ȑȱԇҡɬӘ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212324.149396:+0000',
                                                    },
                                    },
                            {
                                        'name': 'fԃɼųυĞŮVҘɷ϶ȇάʱӟʑӗʔ˯ԗαӧh¨ͳƮϡÀ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 361095.4634549405,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '¸ǫǣώŲ¹',
                    'message': 'ыȷ´Ü\x80˰ʴӆǣӿӯΡù\x8fэЏԣԢƬϥ\u038bs¼Њ˪Ť\x8bňʷǐ',
                    'arguments': [
                            {
                                        'name': 'Ԓ҂ЇӴiӞ\x91ΊǴΦѲ°Aȫʌˬ˖ԡΜҒ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8041766321877150780,
                                                    },
                                    },
                            {
                                        'name': 'χѾСҶ˥\u038bǬǍ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3256491128547996191,
                                                    },
                                    },
                            {
                                        'name': 'ӳɞҷφǩӉҮԧʬЬ|ĵ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': "ƆψqǜāҢȅñƕхβHįʮ˽ЏӹȭԚҭĉ'±ӎ¸Œƿǃ\x90Ċ",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˅Ӄɞ\x9dǐùҖӺŮľʣҨ9ìӏԔƔœҪƇĴӴΙɔêˣŎϖĪЪ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '{@ɐŌƔӻ~¤˪ğˎϯЭϲѡ9T\u0379ØʍЁόѸґʌÛƟϕɵɿ',
                                                    },
                                    },
                            {
                                        'name': 'уХ\x97˾ãƟ˫kБӑǏɯҐϮō',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8849844975356438849,
                                                    },
                                    },
                            {
                                        'name': 'Ǘɳ#ʟŵɴӖлP\x95ьȾѣпϼʔљ\x97ӅǓҋȾŘϻǘҊɺЙʷʴ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212324.819843:+0000',
                                                    },
                                    },
                            {
                                        'name': "ȵǯγΤʖź\x93ǥýҹ£ŭПϛ\x821ҸӂƂŦЅҐÔƽd з'ǲ˟",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212324.894292:+0000',
                                                    },
                                    },
                            {
                                        'name': '˰ѥϷƒКʢΕԦAˊÎұ±ӎёʇļ%ѽγӱšўԔҶԙǇȩ^Ӄ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212324.961549:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ȕκχ˭Ěύ¸\u0381ŘƥӴŝȮӲƃ϶wέҞǚ˕γțî\u0379ѽÍӖʕ\x87',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӥΧ¥ЂѲĜŒ\u0378Ѯ˃иӝňó\x9dŌȂҡ\x8bîԉ\x9eͼƿι@ɂҰԮ-',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ЎeͰÐǫї˞ěʌǽΔÞ˻ ӒăČŖҜɉǏӀ½Ӣ˪ƃуɦ\x86ê',
                    'message': 'ļҺĀӂ\u0378ǴÚӟԝ˪*ʰw˧ɢŬȯƾҧřЈʧ©ƀѹɩˌÔѶȃ',
                    'arguments': [
                            {
                                        'name': 'ɳǨÏ°ĎԀ˱ʜɦŧΝ£˨ÁǲϹÙğ+\u038dƸ͵ӑšÛg',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6641035234215878997,
                                                                            240385204400910393,
                                                                            2530748176049454870,
                                                                            810364827043163365,
                                                                            -1670968237913215016,
                                                                            8623356638519376858,
                                                                            909094147875293662,
                                                                            -1938804433823999534,
                                                                            6246461707517124823,
                                                                            1646413049166384172,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЊωӪ¬Ϊ{¨ɀCĞёºPƽφĽӐԙӏîԄǌ\xadɸūοʺ˺',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
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
                                        'name': 'ˀԊĻԀĤĞɴɚʟ¥',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3477666441529676393,
                                                                            7862662891441981641,
                                                                            -579969728355574120,
                                                                            7546610679014381777,
                                                                            -5893108133992028864,
                                                                            -83920168079824640,
                                                                            -1698278703292329948,
                                                                            8341557975972214432,
                                                                            5555338806621711087,
                                                                            -8866122064112704524,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӓʤ`\x93ìԦӦɥĸѮԟԉ¿ŤŝĔǰрʆX2ƹ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 258764.41262770892,
                                                    },
                                    },
                            {
                                        'name': 'ҎƂҫżƄʹìŰɜБ\x8bɂ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҏҜƱʡ˓Ѐ,Ň/ҙȄ\x96ϬмϴĒxÍÁѰȧbșǟбŖÞõǦȫ',
                                                                            "įǝÏƈчðł/Хĭɂ\u0380ªɎƠ¿ĨĭȪǕǞ\x9fˊɦ'´ȬȟбԠ",
                                                                            'ѐȠѼɏǋu{˲<ƈĞ\x8cǔȬæ\x95˸\u038bļӔǸϮщȉР\x90ɽŎľÑ',
                                                                            'İҹоŐÌұǙΞЫЯĚ©ҵĳ\x8dʱӱŻžīїͷ˚ˡԃгфʜЅ\x85',
                                                                            'яѺԂŚĂȒAФӳԋŶҫGΉń\x7fєǫeŷͰ\u0380ĹȭȮÍӏљȍϯ',
                                                                            '@ǄÕҞƐͼîӬҔ\u0383ЀǾͺϹаĺɄЎÁЫɷǾρțʈɲȃǮŘý',
                                                                            'ҙƻȺɂʲȍ҃¿ϼɪϺқĺ˖ϔӌҫ·ԣǥœɝԕĿаÚԤПӋԮ',
                                                                            'ԝɯǵĹ\u038b ¨ӄƥ®ȥϲăł˟ʧҙğϠѕԅ\x92аΐӯÔ҂Ɠӛ¦',
                                                                            'ϟ˳ГǷӍʕƆ\u0379ƴӇƕIʯξѵöģʟɥĺҬȕaūпїԍЬļӤ',
                                                                            'ʏϿÞɁн8ω1ύΐ҅œΘԇ7Ǿȹƨјω±ƵȢYǇӚϨƠԃƩ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӕԕ\x91ːˊӹ·ǂɉϝɺϛɈǾ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8094706521666156048,
                                                    },
                                    },
                            {
                                        'name': 'ŕЛƵЂӅС',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4148129263052973571,
                                                    },
                                    },
                            {
                                        'name': 'Ӛфʛ\u0383ıpɓ˦',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 183402036873348485,
                                                    },
                                    },
                            {
                                        'name': '¢ҟҎЕѲΧѷԂȧɩ\xa0ƨ¾ɛȀϼĥ\x85ҞпöǧŝɴƜΙ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            226969.5077056132,
                                                                            570792.2903884185,
                                                                            106344.3847181884,
                                                                            185421.85492845974,
                                                                            336878.4276349249,
                                                                            361570.36859917303,
                                                                            345928.8537471572,
                                                                            -8435.870093333404,
                                                                            683288.4864152807,
                                                                            522258.1389455894,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҅ʧҀņȳroԡƊȵʓӜȶƎƚʷБԌȒŶeƯκѶĶˏ\u0381ʎтƎ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:212326.783380:+0000',
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

            'identifier': 'ӂТǜėŌ',

            'categories': [
                'invalid-user-action',
            ],

            'messages': [
                {
                    'catalog': '\x99\x84',
                    'message': 'Ș',
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
                'identifier': 'ɂλˠŐϜŴўӢÇͶŐƣ©˶ϢəӀМϴҺй\u038dsłȤƔ¯ǯυθ',
                'categories': [
                    'network',
                    'access-restriction',
                    'network',
                    'invalid-user-action',
                    'file',
                    'internal',
                    'invalid-user-action',
                    'configuration',
                    'os',
                    'invalid-user-action',
                ],
                'source': '˔ğęȰƿȜҪԋԆ˘ƞƌѢΟħĮМőʜǛȨȬ˓ҋӾδ҃\x9aµԩ',
                'messages': [
                    {
                            'catalog': 'ɃȬϮΛˠěѷw<ӬҒŢЭȩɼyК³Ɗϛ:ϜˏÊѯuѹŻΡģ',
                            'message': 'ȢˠƽÆʏɌϖ¹ŦǶӳηӸΣ©ЪԀÝ¸ʂʂлǡиOПʹѵƞ\x88',
                            'arguments': [
                                        {
                                                        'name': '˃',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -48336041395519468,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǈѵǲǐү°ӴĒǑԣԙʈιƍ˥ǱȈԌС ЛчǮʵʳɴ\x95xѓɏ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɮƃӗǓĹǎ˅ԘӞĤĂŻϔɾұʌϭƨϿ\x83Ζĺѓ\u038dɃȔ˵˓Íѓ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĥӽԣǰƵƳŽΨԟѫϿҝƳȁEǹ˳űpԚɿȗʾ¡љӟǠȢǩж',
                                                                        },
                                                    },
                                        {
                                                        'name': '˰ʷˊлУ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΐɵȺӡŦΐЉźО\x96;Ŀ\u038dεύǷɵʭɄκ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 503567.9664732147,
                                                                        },
                                                    },
                                        {
                                                        'name': 'фͱ[ӞÂ2:˺©ǌȦȈʚÍƵ˫ҷǬпĥĂɓɒ÷ђ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȥǙ¾ɠΛS˔ĆƄ\x91ҊДΫʭ\x93ԤͽŎsӀʋĜɮСʕ˽ɰиØ\xad',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȯȪ\x82ӰÁəԀ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'җςȜϛ¦єΗȲþнћ˗ШíƋƋԊŝӎϒýTЈÓǁ\x9cҲËǼˡ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϡԅǰN',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1800873137668185036,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ôŠƔiǵЫŜтS½ǤśЪӺƉІɉ¹ȑŻӄɴKԖЄ·ʗԭәK',
                            'message': 'Ѓ˻˽Ïúҿ˸ξҊ[Ʌ¬ϳĝȎ\x98ƘʮҧTŹɨʹ\x87γ˂ʢԠҤѣ',
                            'arguments': [
                                        {
                                                        'name': '˪ŨίӚɉ\x84Ԭχ˥\\Ԑ\u0378ҭЍâyŦśĢ˹ŌАүɯ˔БƆɾӚӆ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '-ä9г\x80ƥʼľʾɁΙѷÎáӓıîǙöǵŘýҢwԞɚТзv1',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǱɠҔȳɼʦ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '6ǼюňѫθüȗԢӲηϹʏMӷӄĺɛҰԏʪƝϮ®ЎЄрŹʮɁ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ý%<ȖŠrǾƍɼ˅ǞĿêǉӬΡͼʽϏɝǼɠJήδʌƘϞ³ϝ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¨´sҁҲԉ˚Ѧ҇ԐυÊVһJӰ˗Ϥ˚Ǭƞ\\ƷҬ¢ɧ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'фĲԣpњŠƊ˜´ΙɃʓƐɛſЗƒȼӅíҸҴѩΕ΄ʅѦǎԎʽ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѳ҄ćĳŜɊϖҤƦҶɦʨʷ)ă˧Ⱥ˒ɼ0ȅΐɿÄԣʲɺʓҌʽ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 947945.5055323181,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƐǷкΟć£ӔŏΌмҮ˜´ӐŢ˟ԋϫҍϟɟWǬ˛Ǫʦүґ˹ų',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 592637.7933070677,
                                                                        },
                                                    },
                                        {
                                                        'name': 'мКѰ\x96ȫѲʐƥķˠδ˭ü*ԛҌɚʣҮǔʁȭӖƉҚƾǤİŤ#',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŏ\u038dȇѴǷѤ÷ʼ\x95И\x91˔Ǧÿ˖9\u0380ƶȉˏǫş!ʹϨКƖŋԃC',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϻҧƘʊÃӢϕȿiƯÒƠԀ˺$ЭгŖZêҼӄŬџÚҵâΦȠр',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѩiˮƑϖѯϧҺ¼ĥωҡ_ѴӤԉTӴƫəєƫϿɕξŖҗĹӋɈ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԈķŭʅʬЫң%\\·ʐ\u03a2ʇ˘ʤ\x9eη˃ȯǫpԥÍżӸҲұЦ\x96ƌ',
                            'message': 'ˮȜК#ǿѐʀˮɟæNˬeӥ¡\u03a2ұɳҩşɵͶ&Žïќӊ˟\u0382Ł',
                            'arguments': [
                                        {
                                                        'name': 'þĤɨԥ¥ʼ˴ΫʅƆ˙ŖÕЂѵΫԡΧԄҞÔΦǩąʻϬϳǅȻ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'cǹΐ\x80ϏҮž\u0381=ҬĲĝӲԟʝӿțqЄІѢʄɳĮɑξϋ¤åγ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212304.516638:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɉԤ˅ҥǑϺЍηŶη·Ђ´\x9aҦ,ўǉÆãǮӠƬԁ˟Ȕӳёʣԝ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '!ŀϗԧñˤЈҔŌ˫ǘ˨ύĸѐĬĕ\x9dʥʬӰґ\u03a2$жΈÄԍžę',
                            'message': 'Śԍȼϧҕ˵Ƞ˼ɪƮƣĒǃʲԜǤϊ˃ŚCãņʣŤȥғХËóϜ',
                            'arguments': [
                                        {
                                                        'name': 'ȴˢ˷ԣԮ³ƚԠñƆҵ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӡ´Ƃ6ČȬĔ҄ԘѽмʠÊʬԧˤиΫ%ҍƗǲ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʐɀʼɬϳŞ¿ҌӮ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҕμ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 625641.4200432685,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŚȋВƬ\x9fӝ΄\u038dТġŢɫȦßʫԡςӆ9lϒΕѽ\x8bŇ[ǳȎʣ¢',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'õҿћʒΐǞȄрҔѶ\x7fЩzĪɶǧòÙǦʺţ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1504460927340824200,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҍϖ˝ƿҨ҂ʴҽ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ңȑ¢ѦĠͷO',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1999675172728698552,
                                                                        },
                                                    },
                                        {
                                                        'name': 'яӻʀǤϽUǻѸˠ1гӧҾǠҮ×ǃə҇ɾͲʵɇ˓Ӻ`ӻ¤ťϐ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '48ɆʒԊZJƮ·ӟ\x94ӁėĤԃζ҇ǾŃʣѴħȕǈ\u0379˲ϡ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6771474559456983415,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҒόǘҲƀ¯ϴҤȵK=łWИ\x81˴˽˃ҩʇ˴ϊÏʤƓŕȾȚˍƑ',
                            'message': 'ЖфԎ΄ńȷǶŖƟΠőƪγшƍ~˻ӫ˪ʟǆҩкĪӾӒԆɅԎʓ',
                            'arguments': [
                                    ],
                        },
                    {
                            'catalog': 'ҭŲћˀáΨΪǙ6xŋЍmɧòїƐƱЩĺŏÁӁҡŽ¢0ӉΖү',
                            'message': 'ËʤõgӯĤøɒûЛ«·\x8bҀԧŒԮĺԄªʛŽͷԟįњϦҊ\x95ȟ',
                            'arguments': [
                                        {
                                                        'name': '˩ą˜ŲԩƋҎӭģΈ҄£˻<<ҌϋƑėцѭӠʱȕĲиȘԁѫħ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӌƺãƞʊǠљȺϦТƟ&žţGӦʵ¦ˢąɷЭӯҬˇҴʂϺҷɄ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˠ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӜЇùϹҐΘҘԈ\u0383ú΅њ"ā\u0382˪ԕˣƽ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\\ĕ҃Ԥ\x88˶ǜ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʣ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x87Ҩ°Ґ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЊӂˣɎ.ʰŚ¡ԛgɪ\x82ԓӼɕҏʁӟӌvǘĴʙˤϧʒѯЮĆB',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -13094076185994865,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɀɚͺӏɁȏŨƺӅХРʁ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212306.115507:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԓӒУʒƥΕʡϞѩͻ\x8aȈӃ-ĕıWѤдā˦ӧ\x85Ӷ ğqѠȒӐ',
                            'message': 'ɻ\u038bˈ{\u038bλƎʯ%ʵӥьFϙƞ\x87ǣʟԉԟĠʺč8ӮÁвϝŹˍ',
                            'arguments': [
                                        {
                                                        'name': 'ӋɥƟπҖŕєˊ¶ƐўȷϩŰԋӓҿţĢΝИǳԄѱҭįɖ\x99ȫӰ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˝řŒ\x8eÝ0Ė\x83μȻӨʠŉуΰҨӎԖЈư8ѿƼÑғʽǻ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 345934.82722873695,
                                                                        },
                                                    },
                                        {
                                                        'name': 'т¼ǴηϽ|\x82ʭӧ£ѫŎ2;ƘȘԚӊǳͱéƐƼˋҙď?ɪʯӋ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҃ʊȂӟәŦΎ¼θϛȢ)ƬʭÔ҅ŢĘzнаʄŀϩÈӚſҰ˺Ȁ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212306.445974:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ökaҘϢ\x8fƥʀʏʲҨӓ2ƆĨ¿ś!ΉҙЂʠǾȤ0ѤĨ҇',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ñĕӕv«ʱk7Ьϡ¶Kȏ˭ˆŊʚӬњȟ\x9eȑ˨Ў˶ĿƷБóƖ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѹнвɫΏǊϵԉ¶Ԭȳňƣ¬\xa0ŃŷŦǷӓƆ½ɡӬфνʺjƷ\\',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʈѕЗΘȯͲӥəʗѣƍϟҤ·Ӛ¬ЙХơӡ\u0383Іо}1ʷԘǆƦW',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŲɄŽĆӎѩϧŮǇ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212306.806673:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΜʬWďʓêȒΉуҶІӒС˙Óȵ`jŹҤśӒűԢŮ¿ĶѿЌũ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212306.874664:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '<ʛéɂļǝƒǁԏːϕȧȭe˖˶)ϝӃӐԄ=ΒЭƮӬВȈӐһ',
                            'message': '˜âӅӂőΥ£\x92ѡfϤҾȁļТ҄ʴԌɒ0ԠӠʓǢ¢ũǱ¼ζƧ',
                            'arguments': [
                                        {
                                                        'name': 'ɒӛɪѧҳϥƘ¸9Ǔ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ІɗɝрΑҍм\x7fÉȦŗϋ¶ҳφïԗѱӟǁӡÑƐжđȏҏɔҚƂ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -10073.246162338051,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȯΰ\x91Ω¦Ϻӳŕ˅ƅ\x95З˰΅єϖҧ\u03a2ȻҖyϹ\x87ѼÚǒȟʙїŊ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ģ˘±¬ɜɏҰ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӨǏʰ\u03a2ɤѧǔ¦ЉǻҼ\x9aʿǬψ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -60764.70259034293,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĝǃ\\ŢčԍӱÃǭŜɘƜwƬͿȾϒʎΫȪЌѬ˶Ŗĵ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƵřǳīȌжˋԩþʑ˻ŌЧãˣɇȴªѫYÞҲŷ;$çǣˎȸʚ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƮȔԣL˚ˢƮЅͰ˱ѡ-ԝ^ǶӘԒ9ғŎɰťԆĹǯЃŃЍΆ«',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϧIԂ˄қȔÿĀ%ŜFҹοҧϢ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΒӔƉ˹Ѝ¼čÉǋqӣѓēaήʳҠϡЖ\x9bҟћЗĀíԚ\x93˫ʄѥ',
                            'message': 'РǽăɽђAɍƖ²{\xadɘŠ!ȫ_ȉѥǒѱԠɲ7Ĥ.ʮǥҳŭԤ',
                            'arguments': [
                                        {
                                                        'name': 'ƥԡĿїϗÝɧșёӰôɛдоЭ\x90ȑƩɆѠĖØĠŒʙнƟǯo',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ţiʚӌӋ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ąј?҂ʕҶӛʌúŎŏʚĢʻ\xa0\u0381ȿωӹĥɒӟŖĥҲεљĂУ\u0378',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɇђ˼½ǱǥȧͶѪҭҗƀАϹҲĔñΆ\x97ɿFҋƣӚͱάǱÔ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212307.862880:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x91ԮʋωѽnȀǵҦƜ΄oЕԆцȇӷиăƱ;ОҾόÑϬԏòXϹ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '«Ω§ѩh˛*ɠ˺ΆϢʨγȩ˫ƞϱƍǕˡΑӟõ\u0380ȇШƯӂýɕ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѳÆҘ·&ζ҃\x96ɘЗƊǜȹ˕ЄҭҌȫ\u0379ʔƀµÆƟԉǫǬpϕ\x98',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƽΔĭûϝĜŎɁӄȻ¼ŇΛҒӵϸŠӿѣˊԅǳΟ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˉËƩåғӬ[Ȕǆ\x8f\x97ѦˁÊЬӰ`',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7963425598493091279,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѓǀ0ȟƏʷӖΜ˱ǏʜNƿ˄ҾӿřԤŃɟнȻ˚ˀȰÄÄǪСҺ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5804234926080530221,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԓ·\x93ĳ˙ˣϘжŮӗŁȚǢŦŵͿӪěƾɞƭ£ū\x81ШƨЀĚŋɈ',
                            'message': 'ήžòĲŝĉ,ʟǎϐȋĴʦщƩҿѥơƄȫǖΡͶƟƵѬƇΰμk',
                            'arguments': [
                                        {
                                                        'name': 'ѡƤХҚȆȱɲҶĮ˟vˮɎǬеϭŔǨΒӛƈǣӰ´ƫː΄Ϥʐȁ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '$ϢéϛAËʟҝҎȯɻȹүʨѫ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЅýïÐ˨ϺӂƗ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Љ¢ѻ\x95ǗǭǭȬāŦkƽʛΠˡҜSŁӪԟԦƹ˜бʺɍ˓@ƽҙ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '_įŦϻƆǘǩȒԗϩϜƊůɲϏˑŗΊŪэНйΙĭǒюǻб·\u038b',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212308.668322:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŝŤâħйѬɩуͿ+ȴӀΏүÑԉѰхžͷΦʅȇʹˈϣҐѠЛƁ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʦӄбҠ˯ӧЬƝĞА˂ǧǮ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6375335744931898696,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʥk|ËсѲцӧάӝĔ¥ıƞȳǫ šϯΈÈȽΜԃЯΊŊȆȏ˓',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϴŨЛҿӆѓ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212308.961368:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȪϒӴïђ;˄Ɯʗċϙ1˝ȔȨϘԘȁÜЊȏȏŶоΔ-ͶȽ*,',
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

            'error': {
                'identifier': 'bïƙԜŇ',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': 'ӤƠ',
                            'message': 'Ó',
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
                'identifier': 'ȑÒʤϘϦԏďċ-ϋăΎƠ˶ǰĶ˒ҌѥϋӾЬʆ%ĴɖļɚžŶ',
                'categories': [
                    'internal',
                    'configuration',
                    'file',
                    'invalid-user-action',
                    'internal',
                    'internal',
                    'file',
                    'os',
                    'invalid-user-action',
                    'internal',
                ],
                'source': 'ʖͰĚєɼӤǮίѢǼҗɳŬҹШГҟχБΡшǙҌȝϒиӖĽɬʎ',
                'messages': [
                    {
                            'catalog': '΄ϞǂΏ\x9eƿӅҳ£ϬϞ!ҲϜΟ\x86Ē˷ɲº\x8aΙ#Ųɏīʏ.ԏ,',
                            'message': 'јĎϾʳ˾ѠԋқīЛ҉²ʠʒ0¯ȍ˲шýçѭƣǏοŸπʧѣ®',
                            'arguments': [
                                        {
                                                        'name': '˴\u038dӽΒ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 346793714666379994,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӅҾұÙԢȓƟÍӮƱҗҜŲЧ¥üϒPuϩɱЛӓ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʼΈ©Ωʭ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˜ЍōʬȘçʢѦŞĳèĶԈˢKѽҎ·',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҏƤҎʍ\u03a2ӓůƗҡЮƋŠʸÌ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4019035041294658553,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ⱦɤ˞Ӆӏϝ]Ʋҕsrӭ\x871ЪҰ(',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 251169.87201519526,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȥɬȌǚӗ\x93ҥϢҋшρҝƺҽЭțȊΰ˴ӫrˆʤßҐОɋSӏѰ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'mȰƶĈνɏŢǽ\x96ҲĤƿъ%XǱԉƣҽÏХ°ˉӄүɶƢ\xadʋʸ',
                                                                        },
                                                    },
                                        {
                                                        'name': '÷ĖÕϥГȞ£ҡД¥ρѤʚӦԤ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȭұňǰӬʈζƬǝԊѠЂs<Ʋ=\x9e*¥ǵUřҭҡŴ\x84Ԓ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɭƾŲƥӍĸѨŶLѷύӆĬ\x98гˣΕͰñʏұ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4439041763176953358,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˪ƤώϞǉņ˯ІԨĹӈ½МЦǤɈӷĄɋƙʈϘ҂ĻɾŌʍƬƇʿ',
                            'message': 'ȖʉԊNƩÃ§ƈµÿ˰ɀ˖ȉÙǣϰԬŹɫǾϻҟɯțƺųЯ˲ƶ',
                            'arguments': [
                                        {
                                                        'name': 'ԥǶˁʹԗ\x8bD͵ˏΐ°ӲGċёEoПǟČƶƕµϕ˨ĆȢžЇ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ðçȇɏϊȮɚ¢ЙѠ\x9eČѵʜʈ˭ι'юХЊŲĹѭД˪т",
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԘԧʀʛͲǩŇ˭ȫĘЉϤп2ӂҐϮ¦\x8aSХΕÖѿȅ бǐҰŃ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ηБɐɶˢΗÑØþ˰ҔǿöѹɐŪ\x90:Β\x89ǯȒǽƇPҤԥƗßǔ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ěʳƣϤɠˈԠá&ɰÚ˽ғӫОњɪrвǍʄˋ,Ѿ\u0378ǕԑȫǄҎ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'WюΡ¾ˇ\x9eϳĨϏɗȤÐȔԮ\x81ɮś\x97ҌҴɔŴŎĢɕ\x87ѶӷűѼ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212328.320280:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӱǻяă˶¨',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 39581.785827252315,
                                                                        },
                                                    },
                                        {
                                                        'name': 'oƭϏÍ΅ї',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 560469.2757367071,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʻ-ԔÈР˦ŗ}Ƿ¯ǒ\\ӮŲπƍÄуǖѿˤ¾ΥǦîɖƵ¶Ȭ\x84',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҨĳʙϯƉľƮ˶ǞeВҦЮϙĖҢ!',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212328.582595:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '©ΟΠȅҼƏ˃ЀʈϚȮȳ2Ź˟ť»ӬΈҖЎ\u0381Ɔ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 79231.82256731513,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȐǷӀɬǭ\u03a2×ԣȀƙ8ÚӅǝpQƦϿҝԮUћǈʏԅǴͳˁX˝',
                            'message': '«lԉʀ{ѱҲұŻĴԣʗ\x87ʤѲá;\x99ԍρпΜυnˬΆͱưȧ҉',
                            'arguments': [
                                        {
                                                        'name': '˖ǞэӾʒшŃYЛәˬʦƑƷɑ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7767324466271839099,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͲğƱ\x9cɶȱЙ˵Ю',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÕΖΆʒʲɡŕȅϫƅΒΚҊģʎҿѝ¼эӼ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038dԖңзԣU\x99ҼͳћΩі',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212328.992420:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'јŗQ\u0378ŜϪчԉСϰʵŅŽҾ\u038bǕ˽ɛ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӛϥɔʚ£WǋѼСǼΈљãƙϊɪ«ƴӌӨo˰œz\x9d£ơßϦÝ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ҝζ«ѰόǠǺЎɾǮԚ˪·ОǟɲǐԄɞTŵѢʜΦǗ+˖˙ȞΊ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÈĳǳѿԀӚʼƭҲ5ӿѣÏˈŬ2ȉȣ˱®ЩϋԉҔƙϬӶğt',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212329.196802:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'βҞģЮǚӘȀɫǝƼɓϟʼњү˪Ϭ˷ƙȝӄƷҾǝƣȒѸҫȴĝ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȶ·íҸ¥A˱ӿĵԀыӺh\x8eǠΗЀ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȒСҸδˢȁ˷ўј\x82˻ː͵ΊΜԐǱӗƟѸǗŅǝҬͱͺƖϨϛŁ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÎľŮϣʋ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x8bҭԧϙѰƨĆй;Ӷϖԃ¥Βƽ\x8dÅї*ПƕɁɆƗ\u038bʍϽНԜї',
                            'message': 'ğR\x9bĮȵɝˎɂͰɗаΎʜήΓz}ÃӽаĮ˖˭ǒҲľƬ9ҊΏ',
                            'arguments': [
                                        {
                                                        'name': 'ü\x9cưѩ»ӥЗͼʺнǢāAʈwңġ\x9cƱΩƿł͵ӐɯʃV˚ҥʫ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 621433.0463296665,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͱŶÎʲ±ϣξ^bÂBˬ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŨƁșǵ҉ӖͺѹͻǱ×ǝы˼ǘŃƔȏŜΫԣуƔ·ɈɶȰɑ˃',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1264727226207338918,
                                                                        },
                                                    },
                                        {
                                                        'name': '͵ә˞ƬԜӪõ\x92ΑQʙĹɰПłɽίϞԦĳēӀʬʀɀĆԬѩįʅ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 230057.74108379713,
                                                                        },
                                                    },
                                        {
                                                        'name': ':ȨԕƞИCɂƹŶѯĲ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 415534.8669529886,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԥςϱɩЩҊ[ưҒӰèŒϪƼͲȇ²7Ʀӫɐэ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 415233.34430921805,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӨßӒԋьkϰсōʓќʁϒфȨљęĀӃɌȩƠХÜӲÿМɐΥ˦',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6692652459176849281,
                                                                        },
                                                    },
                                        {
                                                        'name': '>Βɐƻ\x93üǉ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\u0383ȚϸΨ\x89Ԁ!óȷђќý˘ѿĜҍ{үͰÕƢɅĂҳҵѧĤß;Ӵ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϴЛƻĻƉόο\x81Ű˅ʝɧ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǻč҉э¡\xadԉtȎͼˠʘ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2271843887702393176,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ɨ¥ZdѨɀѽȗƍƸĖɕю\u0382ȣӠѤʄϗ3Ӂ/ƗįҬəÏȎ˘\u0381',
                            'message': '<ҐӛѳўǋʡђʪƾɉǀаȍăŲўжˆӒӃНµ¼>ʧĔʓԘѥ',
                            'arguments': [
                                        {
                                                        'name': 'Ŝ×šЪʳΥͻɁɣǇƛѷϜХĄɪӀ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8428947467853762964,
                                                                        },
                                                    },
                                        {
                                                        'name': '~ԗѵƤʩʣѣ˞ƘʋƭѢԒņ"ɂŻӱŖʞȄĪѲǋ:Ќ«ϻԂɚ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 174491.56900753372,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ПӬ˭ΎжȂƣÜēα\\Dκ¹҅ҹǰɳƅʤYӳƷҴԣԜżóϞЩ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԞнŦСβĔȨΕÖόԓǟ®ԛŻǷȹʕҶͰщҁƭȨëȤӽŔӅȺ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѰǧҷçѺ\x90ǔɀҵ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'λОжǩ\\ɿӥŇŧʝ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x8aǡ+ї×ӈϒǬť˹ԇèϡΒҗ˧wƛŬыϕŉϛ³ԫãϛǛJ\x96',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԄˊЋԇζʍʋ¦ɷȋȔƻ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ВȅͺӴЛњȥzя',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3338414307155315841,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÛɳԤπȻΡάϬΑ?ǎӬ;ſ¾сųʣĵϘҞʯWϻ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '=ƟɧңɂӬȆŰVǣ\x80',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 839369.411014466,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҔӊɶĎˁɸīϪӣěÖҡȦCŁӭ\x8dԑц·qҨǻϴo±cȋρĹ',
                            'message': 'źϡÏŉˊ´ΛʏіӍς҈ҌĘɴКʥԏǖZԏëǵӿʶԐˋ¢ЩǷ',
                            'arguments': [
                                        {
                                                        'name': 'ҌŹfѲƹ\x9dǣӄџ˴ŀӻδƌŮȔӺ҆ɭҲѱʗ¿ƅˌȸ҄êДԆ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 942569.968174622,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԙԓ\x90\x85Ŝ"šεԚğĬӂPŃԔѡ˘ɢşѐß^ŲΆҳTԘӀʩď',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϐ˭ѻƙŃɃ\u03a2FӨҥӹмd²ăЎŪUԑǇ҈ΔƷƉĹĺԃőɗ<',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212331.232039:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĹҀƑ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 990174.2266264264,
                                                                        },
                                                    },
                                        {
                                                        'name': 'РӮЃ\u0382íϴѹϥ×ӎͺŗʜɸ˳; Ȃʉ®λäϰ2ƐǗғρӀԆ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212331.361219:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Qӣϩń',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ſŽʉÓƸԀ҇Ţӈԫɇ\x84ϐϤʯҾП\\\x88ºӂά"ыΫҪҭӯ´ӑ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'λόǈȒσĭU\u0383џΰęȜѣЌưǤİęĭˋɵǯЖ϶ďм˝ͺ\x82Ǣ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŏº\x90ѨȺˆɏʻʵȺӞ{ѷʕО҉ϘмϤĒ¥mʗȂ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˻ǃɲ\u0380ԬШƦҞ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Γ:~',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȅșǎҦũ',
                            'message': 'ƅʪĠǀ\xa0īϛƛΰïƯ˗Ѷ1ЈѽǾԣӎ͵ɐхħЄƁ(ōɃѾУ',
                            'arguments': [
                                        {
                                                        'name': 'ʍɩƟ×',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '͵ϩʐɕǑɺëÎ.ѿϸˀуĔʟǒª`ŕϣџ´8AʄŤƀҧ˳Ԓ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ȉĥ҇Kȋɔӆ\x99ԓАũÅѧù҈ȗ͵ɉĤɧñШҘˀʈćҒȲԤɫ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԣʚΝҝɦȝӧz',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѝʁДvĞĞӿōӸĭĿůћřBƚѿʨȋиɭκʾͷл\x92лŋǩ\u038b',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212332.060486:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'цЏԇ2Ӗ±αǆԠƃŅɇĆɉΰϗȭȀϗɳѥƴϊǖȾԚĻ҅щò',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212332.125118:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˫ǦeƭŖ\x89ʞʐʹңF˩ΙmΙēÊѣ\u0379ýœcѸҚ5ҭћ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϿҨɈ[ɚ®рΏƥ!ǫÍҼįĶ_˻÷ѻĆ8ɠԐӗҘцÁȴ§X',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2514001173944672550,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ью˅ȆȭĪÇХ¿7±ҖқѵʕɭєșҜЄÈ˶ήȹ\u0383җâ«ŌΔ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'њƪǼΘ£ɐŧƕˢΗвʬԮԝȱΔőˤʇã\x81ă˜ȹȪȥњśYɝ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʃđЁҏЎӠҜɴǋǈģȉЫπ\x8eҾ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɗƱѷÅϽ0ΓԭϐҼýԖƛȶǡсĊЯ·ųr',
                            'message': 'ŬƸӬɛĩȘƢӭȺѓ·ӡǿ\u038bĎƹȐСȁ§Р˷ŜȷİǾҏгҾ˳',
                            'arguments': [
                                        {
                                                        'name': 'яҵҾψÓYӕ¹ϔѼʴѨĊǎƽ\x80\x95EǪϠʺɜцώʓ1БŸ³ǆ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӥԝƔǖaӉɐûҞǃ˱ЖӀӚ¢˟ɛѵŘ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212332.660640:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӕȁɄȲϥϰωõȿȘª:',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԝãȘӀҭЏӞϺÔҐԁđ\x88уĘÛϕǅ+ɂ¨ǥ«ґԙȬΐ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'fɋԐŢ®ŅʝŖ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 85325.87555215179,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɺґӿåҐŻǎȳ8Ƅž',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƘʠPʏɏцӪ΅ɚϾЫkɲ`ѲӝҮӆǉŅΖХŞɳƚțʿdªǾ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ψ˧УШͳʸʣòȔȯ˂ϰö¬Ǒæ˃˛´ʷcϨƑØҧɍІËǝ˙',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϧhǺКι',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƉΑШþMиϔљɛ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212333.185679:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԃ\x87Ϻùʒ-ÔɃωɖȘ˾¶еʯӳKԬʃλ\u03a2%Ò×ȥĊӘЎ˻ɟ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Çɓo',
                            'message': 'чиɓZž¬ʝVɺÎКĀʬʩԑԢȋ1ƶНӕƥ*ӘŔӰӭǛϱΙ',
                            'arguments': [
                                        {
                                                        'name': 'Ġǜ¿iӆ΅Ǿdδ1ғԣЫwғ˜ϙû\x96к҆ʌǆ£ϯy',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĈӵΡѽȳԍϡġ\x93ȉ¶ϢĝкȺËȐʠʸƙѩˢ-Ѝ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 128091.92699027856,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x81ϋіNҕƧɰǐĲɦҐɰçмāеʩNҖӊ1СѬϥȨΨɕAɡΪ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7778174815663282784,
                                                                        },
                                                    },
                                        {
                                                        'name': 'νÎǊѼΏBč˧ɽƫЬӷԝԔ\x89DѺ\xa0ϊ(ѝˏϏǏμӛΎʵǬѱ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɦЖÐҰ\x93\x92Ī·ФѐϧϪäÕơɖҩʒƹԒѮӢεѤĽƎXēˈ_',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212333.702027:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѨBØĔ\x90ԂūɆ]Ҧ>ѨʌƣŵЗϮԕɚЫ϶ʾ\x98Ӫ˳ĜѾůϞĪ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǵͿŭʧȖ¬Ǆ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʼϤĄєȁӜČr',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'şɍϒÐĚĦԟӴʩĬ\u0379ȰԩϷӱ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5967154471423864051,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƌύĦ9ɸϰƘȘ¨ȯāùӤlιţԫ϶ĐѧBʔ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -229527604257659617,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Zá>ʆҿȤ3þ,ԗĻИϏӆΧō-ǺǕĮͿÃÂvʪȘ˶fűѸ',
                            'message': 'ԁǡгΞϳБԥͰҶȔxƃǹӅʹɦŁǰӽÎ^Čʎ<ϣuĩ`ȓű',
                            'arguments': [
                                        {
                                                        'name': 'Ƃľπӌˎʣ҄ɥѿѾƇͺüPΞƒʀɇƝƞ\u0379ŌǘŎϪŃ±ƊҐ\x96',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʲǵǐϛҿƁƪǰǭmǆbɻʮƐҖϸɵlǭЂĎҜƿ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x8b\\ϡƺҲМяʙVƶ\x91ЙӤʸɗЋʎƢȗɐʭрќĤ˓Ş˻ìÎϯ',
                                                                        },
                                                    },
                                        {
                                                        'name': '_ѫƢͽЕ˶ΥŕÁӀ¤ŗ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϘʦŋЭǖԙeҮɝŴ´ѳʆЕ˟ȯʒƋөӤëΎʮϪıȫŖĠƩ΄',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ūϓǡʏȮ҂ɝƇЅƴρJǓŨʬÀDҀԑȈЃɜ³ӭȪъӹ¶5ę',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɘ˚1',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1963602944208274907,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ώ»Dʶ6˱Ş',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 380537746819703806,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʣŖ͵щvơԮ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŏФмΤԐϛάӓʩʚҿͱȮɬΖϠBЗáѡϐʣˮԍғȫ˭',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6026398918120696160,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʼȜɴϳ*ΠАʗÑάǍ$βĲԞʹγԋα˞ϮŔ!Мϛ$˙ȩť',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:212335.044046:+0000',
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
                'identifier': '"ԆĪșӈ',
                'categories': [
                    'internal',
                ],
                'messages': [
                    {
                            'catalog': 'ɦА',
                            'message': 'Έ',
                        },
                ],
            },

        },
    ),
]
