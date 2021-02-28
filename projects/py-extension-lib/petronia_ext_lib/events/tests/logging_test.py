# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-28T02:46:21.958986+00:00

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
            '$': 'ѱJɦµЮт?-\x96ϳɄɺjҏѣĺЫЈ\x9aԟ˺ɭʱƚƯϩΩʃƼә',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -3661549708142172697,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 565508.3508097588,
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
            '$': '20210228:024621.830981:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                "ɟԍƹη\u0378˟ʥǡԠӖʣ.đчԞ'\u03a2ν˲Ɵ¦ŖϺ?ӄӶXcϪԓ",
                'Ѐò˲πҾφˋŹҏ0ΰѕǿċɥԪļӛҝ˸ŧЏАȌұɹĖÍΡƨ',
                '(ĐҗˇӐӑĞǗҽ¬ǌȋľ\u0379ȗǌȿƺǤӉΩдcҮ\u0381ҬɥΌȎĵ',
                'ҒʉԊBЧàĺćƠ҆=ɖԗВqТÞŦ˻ѵ-ƙÚȦʘǔǱƔҗ1',
                'ȸ(²ƃƢҭɨƐ\x92fϷϦРĳ7ĥǬȬʪʧӀ?Ʋ˨6ǭԤϓи\x96',
                'ĠȼҍIН\x81ϣǹȒӑԍȾ/ɩσ\x85СŹŒ\x9exҰɃ͵Áиӕȍϥʦ',
                'ϕŻʬLđǭԝê\x99ϡɯɡƮΊҷˇʗÃǕ˯łҳʳ˨ҜӏѰ˫άѓ',
                'ÃƶιӱlΏǒϜʘԉȆɀǜΒůԟÄ.ҢҪ\x87ϺˉʥȨ˚ΑӃřʾ',
                'ƷӛƐ3ԕPԟΣðїѩɣųѭ¦ӚŶ҂ʂņwƗόʏŖџƽǺþȵ',
                'ÍМӡаĵрjƅÉѠɂÆґԑɌʦſ\x8fJЄԑbΟȗŞƾɲĢҘʰ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -5468456940319421888,
                -7822096833211995546,
                -8761810473017273438,
                -9121667067825626286,
                927583890056422961,
                -6411165599014816849,
                -8735262485955197430,
                -6658647371216494491,
                -9028097723828152129,
                8733159678936924948,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                875562.7697333099,
                -29065.07806528684,
                528734.7139754165,
                525535.2113921941,
                584932.6205235388,
                995568.8218236391,
                950946.5992462335,
                313235.5611868981,
                680056.8182966948,
                732574.6268607267,
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
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210228:024621.831838:+0000',
                '20210228:024621.831852:+0000',
                '20210228:024621.831860:+0000',
                '20210228:024621.831866:+0000',
                '20210228:024621.831872:+0000',
                '20210228:024621.831878:+0000',
                '20210228:024621.831884:+0000',
                '20210228:024621.831890:+0000',
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
            'name': 'ȘˑӛŲɤμȴɽ',
            'value': {
                '^': 'string_list',
                '$': [
                    'Ҟʴѐź«ʑǎǒȅɼˊӡ}\x8fq£ʴǏǀɈзћÀłτ΄šÊͳǲ',
                    'ɹȡ\x7fίŁ\x84ҷɄĊɊɎ\x84ġŐǍҐλǈЭ·ȤŢPĸɿĜȺǦ˚ɺ',
                    'ȬØΠӫŌшˎ\x9cʧж©wɑŶΡ\u0380ś`ȤӥΌ˳\x99ɗ¦ӡÍΎ\x9cų',
                    '{ŴɏӚƸԟȧӒʦɦßʁȱҊǮҠ\u0382ЎĩƫŞǛćǛƆӑӯ\x8dɵԈ',
                    'ŐӫĀʫӧȈĊКӠĪƱ˚{šҩɐѰѫİųĥЌƞҍϢ»ҬyƓҷ',
                    'ɔ·мˬƗԐʀӓԑȢ¯ɣІƤ|ҳ\x8bεжʵƱlҋʕȞȲρƮIŗ',
                    'ͺȧʇïć¤[ŔʛϨȰˎ\x8dԩŁɗĠȾѲ˯ǺƖȗȣϙƭϐ͵чň',
                    'ԃӾӠįǟø˾ѕĤηɏËƩȻƶ҅ʇǊ˳ʦѕбȐńȔʓHƖѧĕ',
                    'ӈ\x7fˈСȥԠΤƁӁƾňĶяș¯4\x92ç6ēЮšϻƨʾӏƣ˦¼˭',
                    'ѦыɻɣÂøѬDˆļͺѴ˚Ϯ\u0383ːō\x93ˋ{ˏѩ˃ΉȻíˎňЄʧ',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ҕ',

            'value': {
                '^': 'bool_list',
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
            'catalog': 'ŉÀʳĻϲ\x9dǃȃƷϯídԜΔς˷ҀԋƐĚѸʀϞȽFʂÌйƃѭ',
            'message': 'ȉǕ˟.ѳʹȟȄ`ł_ϣёӖӁɒǍϋԎвŞѯΑͺРӸǻ_ӜԘ',
            'arguments': [
                {
                    'name': 'ƽˈɅŚёŝǼΘqǶǦӦѹÇɳƬ',
                    'value': {
                            '^': 'int',
                            '$': -8275399296068580338,
                        },
                },
                {
                    'name': 'ҾÓҊˏRóɸCЊЁŨĜȮǩԖ˞ƊйҌĨӿȖ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210228:024621.828191:+0000',
                        },
                },
                {
                    'name': 'Œˁɑ',
                    'value': {
                            '^': 'float',
                            '$': 124101.7108840156,
                        },
                },
                {
                    'name': 'ώƦĔ\x8fʼǑʟ\u0382Ѫɺȿҽ\x86ǭÜҶ´Ǟ;',
                    'value': {
                            '^': 'datetime',
                            '$': '20210228:024621.828461:+0000',
                        },
                },
                {
                    'name': 'ŧ(șɒҏțѶ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210228:024621.828600:+0000',
                                        '20210228:024621.828613:+0000',
                                        '20210228:024621.828620:+0000',
                                        '20210228:024621.828627:+0000',
                                        '20210228:024621.828633:+0000',
                                        '20210228:024621.828640:+0000',
                                        '20210228:024621.828646:+0000',
                                        '20210228:024621.828652:+0000',
                                        '20210228:024621.828658:+0000',
                                        '20210228:024621.828664:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ȞzЂͰΗĦśbӏ·ĭÆîʾėώĖӀ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ӰɟӿȯūԖͱϖŽưϨɈŮ\x8aȎ˒ŧʗӔt%ӳԀρҤbʴҴϺ҅',
                                        'ɾһėёɥԁɟѬЦ˷ǨԦõцȪԕn˓δǴƟ¹ѭ҈ɒ˖ѻýȉÞ',
                                        'γ˫YξβϒСʃ;ɩžƚ³ǥʳЧӦƙǲѡÇνˣЅų*ȯ´\x90ͱ',
                                        'ӽĻ\x8eˬҳˮɋφʴϋҫɖŴČԞ.˄ϟЮЦƶъџΠʦĶӞ˓Ϗҳ',
                                        'Ű҉¦ԩ«ƙԡŁӼOƵx;æʔɜţɲȗƴљǳƒƒʥ\x80˕Úȹї',
                                        'ŕϨ_MКȑ>ԥɐőĬ˅ĦһqѫŶνȁȫ7ЎǇƊ+υԋɣѵƋ',
                                        'ͽ!ΧʼƐdǁGΟƽEģ˧иyѕԂƆĻMԥɍE҃;XǧLͰԟ',
                                        'ʔόɸĐĽǃǹӅВžÂȒqĬϰ¡ӣíȜӹ¸ԧͻԍƧȊʩϹЄı',
                                        'ɹϬƤєRȌѪԣзȰ˛ĮƱсŝƬυŚҼϻ6ԏť\x9aĳΦѺѳҍӓ',
                                        'чȌίҧþʍФȀǪɉϖЩĨ\u03a2ǨԆĝ\x9dџ˛ѫӏζ҃ϔĉŗϯňύ',
                                    ],
                        },
                },
                {
                    'name': '\x84шԚϏ\x89ЏâǜĖјǕѸͰӡɏЕқǗͶˡ\x8eϢͺ˱҈ԩsҚƯ*',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        399730.684676675,
                                        73428.88925779183,
                                        321115.3189119706,
                                        332599.71169709886,
                                        12597.081831551754,
                                        131569.66185301656,
                                        449751.0594580702,
                                        -87631.98398360924,
                                        640152.1626451568,
                                        650109.5026977807,
                                    ],
                        },
                },
                {
                    'name': 'ҠǑʹʭԈÈȉkʡƯƁ¶ҙŵӢơƢͱҿͻĠ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        False,
                                        True,
                                        True,
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
                    'name': 'ȷƮÖЋȣ¸³ѿˣĠ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        456634.6540542053,
                                        922302.4378664119,
                                        -31539.60052634336,
                                        -22526.826908881296,
                                        259865.82920927485,
                                        541249.5148784458,
                                        -53469.24838604139,
                                        762067.6312802641,
                                        453398.3451478989,
                                        746518.4743883575,
                                    ],
                        },
                },
                {
                    'name': 'ԤˎԖhϫы\x9bΆԤӛǢċ\x8eʝǪʱЊÕ«ˡа',
                    'value': {
                            '^': 'datetime',
                            '$': '20210228:024621.830072:+0000',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ŕϩ',

            'message': '\xa0',

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
            'scope': 'info',
            'messages': [
                {
                    'catalog': 'ǃÜһӊ˛ŕħāРhϹԋ\x97qȊϱƊQ҆ԓƼſщÄ\x84´ѼƗˮ҈',
                    'message': 'ӖΓǖɲƴʛȺϲѡôϺɕ\x86@\x82ǋǛúўӖёѿà\xa0˯ˡҲɽȊȇ',
                    'arguments': [
                            {
                                        'name': 'ȥͱºT\x9dӿęȳȖϙѮӛːϗɗ¢%җƌМьҎȀʚѝҷ΄Ɂ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024621.782305:+0000',
                                                    },
                                    },
                            {
                                        'name': ">ϻώȭxl|óЁǕµқӯǩɁĝƎϿʴ0ˀʘқǂʁ'}ƉǯȒ",
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024621.793075:+0000',
                                                                            '20210228:024621.793104:+0000',
                                                                            '20210228:024621.793114:+0000',
                                                                            '20210228:024621.793121:+0000',
                                                                            '20210228:024621.793128:+0000',
                                                                            '20210228:024621.793135:+0000',
                                                                            '20210228:024621.793141:+0000',
                                                                            '20210228:024621.793147:+0000',
                                                                            '20210228:024621.793153:+0000',
                                                                            '20210228:024621.793159:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɦԌӰԫΰϏȺ\xa0ȚҸ@ЅΰĠ˵',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 44471.84292639047,
                                                    },
                                    },
                            {
                                        'name': 'ƺUƧɑџȳϻ\u0378ɃɎζļǓǥ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6987442355651428529,
                                                    },
                                    },
                            {
                                        'name': 'ÕɦŒɳ2ĄϙʛȩċȊ\x8eġƍɐƇľҏʋˏϓ:',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3722442527387438558,
                                                    },
                                    },
                            {
                                        'name': '˾Ǉ3Á·dѭȒʔŁ5ǕƹĞǌӰNȳƓr¢îưęr\x9cģʕәı',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԒӺҿǂàA\x9fˊˌƑˋϪ\u03a2Ȉ>ԘѩǙһáГĕũɡΙʉξɖſȂ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7385553271907452161,
                                                                            8506193039528798570,
                                                                            6289581845296787739,
                                                                            5764162906565862725,
                                                                            -3132909276531712517,
                                                                            -4267832828901855724,
                                                                            -7558442370976170981,
                                                                            2971757602554914973,
                                                                            6298162826388340443,
                                                                            4516971162283772190,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ә&×ΦȏѸ҈ΊˉʽÖӄ\x9c«Ɛăυ¬®ҬŊϬϗʔ¬ϾîMӏƿ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -3868.5061384317814,
                                                                            619502.7159022059,
                                                                            476077.3923416748,
                                                                            698416.2933127312,
                                                                            414932.7722122648,
                                                                            315982.3839783188,
                                                                            297071.0820832319,
                                                                            113924.33213410873,
                                                                            979337.4366911629,
                                                                            556642.8817334424,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0383дͺŌʙƀӢGͰ҅ԑğ\u0379ɸĹɩƶ)ƹǪԐЇɡϒƮƁ˘ЋЭĹ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5389305475071703172,
                                                    },
                                    },
                            {
                                        'name': 'ԉԂϸĮɫȈƨÛ!ƏʂǆČўVΣŴƌѪÇ·ҍҗˡԛ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024621.799310:+0000',
                                                                            '20210228:024621.799342:+0000',
                                                                            '20210228:024621.799351:+0000',
                                                                            '20210228:024621.799358:+0000',
                                                                            '20210228:024621.799364:+0000',
                                                                            '20210228:024621.799370:+0000',
                                                                            '20210228:024621.799376:+0000',
                                                                            '20210228:024621.799382:+0000',
                                                                            '20210228:024621.799388:+0000',
                                                                            '20210228:024621.799394:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '[ϸĆǒ®ԋǭòÅƗɩψ¤ǔΫȪω˹ĽӘӦӯīϽъΐΑƢ/H',
                    'message': '0ӋčҨϕžƂЯʼΖԃʒȉҨɜȵԎ?ºĠŊӴŤǅșҺƕʻĞѯ',
                    'arguments': [
                            {
                                        'name': '\xadʨӇӹʰҖˠӢϙÖɘϖfɈȖ ЄuТƲ\x9eÔξаǎƪGʔζɿ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x82',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 111456.65630447876,
                                                    },
                                    },
                            {
                                        'name': 'ҵόж\x8fĮʭҴǥҴǓїěӠʚΎƟ<ɿԘʦā˃wȺ˅/',
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
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'σǎĚ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǻԓЉĨԈIθóōѕФŚĳΪΰВԔӡ˰ʈɱнȣѴǭʑˑfƩϊ',
                                                    },
                                    },
                            {
                                        'name': 'ʺEɋ˔ÜŹϴϾϗo҇ŠƮϝʔGѤʺЏϐɜȟƾԏƛˏԎʏўр',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4327971529077256906,
                                                                            1919396685323912421,
                                                                            -4317726457367188030,
                                                                            4363909024638491113,
                                                                            5184305671742140270,
                                                                            -4265034945411162217,
                                                                            629163458427151496,
                                                                            -1365982588290819377,
                                                                            -4632530939369126586,
                                                                            5171701364260471410,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɻfÖ˃κ\x8eŊŸȖϿQиϫπĬçɾЬȍ6ЮȲ¨ӄӞӞəǨ˫â',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ΧЫъĔԓ/ȇˮĨВʏӗɊ¼ĭΕϐӄŧƈĔӄ˰ˏɆϔοΜŻŻ',
                                                                            '˳ɎÔȨĴҫš¹ĤſԔŢdŋ˚{ЌȥѓQӺȶÚ¦ːԮˎԡҞ\x9e',
                                                                            'ѳȭǔΨҗ\x93ȋοѴȚŜҗšϳǐȖʺЈǫɊsԦΖӃӞ×ə҉8Ұ',
                                                                            '\x81\xadпȞqЃΉ҃ӚĹѴӍϿƜȜӣЉƐіʅÎåϬîȉɟҴϡӼ˱',
                                                                            'ϧɢƁőʃƘȺɢΕϬǧbɓÚ҃ӳɠœ\x9bΜʡɄΊЫǺШYċĬΑ',
                                                                            'ƬÈЌɳԁȰĚɱɒRʓĭǳ²\x83ʊÉɾωɊɖԦǛjʷǭαϟʊӺ',
                                                                            'ҐЯ˔ɺgȭ8ҧǰĹɒǣӛɁҀƙҝůӕƶėЈγʰΒƋōзѿɷ',
                                                                            '˰ǚȇӇѾΨϲӖċхɚ˨Ѧ˰нв˝ŕіҫΑˬǵeƧԝñɾ`ԟ',
                                                                            'ϚԠ\x8aѫbƇȥʅɡδѓƆѐӽҺѥɥԌёĦŊ˺ѲȞ˛РϔԨȎ΄',
                                                                            'ʽτģȿɛƮƸƽɜȱ΄ǲơȟǆľОǹÉΏèŶɮÕɨïʋ˕ο˒',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ωʯŻƍnʐːʼʹǬ'Z˜ȶğ˺Αɣӫ7ýΌɉ|ĳ",
                                        'value': {
                                                        '^': 'float',
                                                        '$': 745880.3981156196,
                                                    },
                                    },
                            {
                                        'name': "7!˺\x97ǐĮЅÅӓƚ\x92ЪԐцʿъΪ'ȁɐϩԬǉˀПĚҷϕβÕ",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024621.803014:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӖįŸǊŇöҝчȀȰƍ˜ØÙˀƕѮЮЅγʵʜԦäÑidʠ˼ȡ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ǍĹ\x99τΫDĽƑȪκʌ\x98ȴȎǊs`HӀϳԂȴAĚ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -15121.769232484221,
                                                                            704988.7904978328,
                                                                            814269.7379203596,
                                                                            763560.765472854,
                                                                            578157.279343018,
                                                                            511589.2796945494,
                                                                            749815.025805489,
                                                                            197409.14979512978,
                                                                            25995.707539838433,
                                                                            233966.0458085271,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŖĩŔ˱oј˼ŃҿҊϩħư{ʐԣ§ӵԝÀǊċЂȾ˝ľŦǉԄѴ',
                    'message': 'ϪLȉÎѐѓäΐԠԥïΒѴƇöСΨ:ADѾԊԋѰˀǰŪǟӛ҃',
                    'arguments': [
                            {
                                        'name': 'Ѷӎ˼ĶėϹуū҃',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'QǟŵӊҶ\x9bǭĳԙЎĝʬʣҠӧӖɕӭO˻ȵƎŠǚ·\u03a2RԈӓȕ',
                                                    },
                                    },
                            {
                                        'name': 'ȈżȊËεˠã˵ǃˀԊŠɶ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϞʴWӝ\x9fǀôɺɕΓѠʼԘӽˋΑŷΚǭßњѶщҭԌΛÊ,Δ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 507132.55590533954,
                                                    },
                                    },
                            {
                                        'name': 'ϏàµȖōƠʽҌ¶Ǌ˟ӯϝŃԇJ²OӒѼ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'h҇ԕΛ˻·Ǖ\x8aʋ\x8f°ǿ΅ӖǂҰȶψϺȡlΎϢŮņɂğʛɣр',
                                                                            'ΓИɒŴ÷ʊ\x94αǚғMȍІУĐ\x9dөˍӱϋφϷƈɒ]ъĚąųӤ',
                                                                            'Ь1ϰӹYȐ\u038bϛŘ±ĠѠӀƨӇˍҽӵиˇɨϨĜ\x85ŬϗáʇƚI',
                                                                            'ԧųˬòȕˎª˄}fȎѷȕřøʟѺҞĆʄ¨ђϠȌЫ\x85ώВ\x8aƆ',
                                                                            'әДʛӅѽ˩ŹЊĨӴƳOBТɁċʹùΨ+Єӱşǅċʻμγ˖˩',
                                                                            '˅˼ƄʴԝjΔ˜ǰúӲaǾʀŶĵ~\u0379łƜsӦѤȺȱʝÛȥ5Ӹ',
                                                                            'қÙԌӭϧƒϾ\x8aqǲԕтŢÍ¢Αԋλ¤ǞϵȰÀѕѶèͽ/γз',
                                                                            'Īŷǵï\x97Ȳ6ʔŴɟ×`ƳĞ\u0383њʝç¶ȋˬΔĨѷɓƶʴӑɝɚ',
                                                                            'áǴˬ\u0382ЕԈη²ЦȇόюͲŴ`ϧûƊҿπʢðÅύԇÿКϋ²Þ',
                                                                            'ŭ˹Ԇϳ˶Ѓ˺ʧ¶Eϵ˝Έ˄ҩŵĊɝІрɄж\x9eӸȿ˗ԥԗӴо',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'FԧȲÙ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            283393.34338154766,
                                                                            960186.621781504,
                                                                            49736.29338222803,
                                                                            -26814.41337860984,
                                                                            518628.18093820056,
                                                                            129879.41406120462,
                                                                            268927.1237636656,
                                                                            158342.69007799428,
                                                                            -2448.041108804202,
                                                                            466678.1401000022,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȱņÿū,ʉ\u038dƺ\xadʛÜѫѲоȱЉΤ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024621.806304:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȋкɶЕ\x87G%ӛ\x8b˂˔\x8aұ˞',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7013892743292707719,
                                                                            6586043284162769146,
                                                                            6147347735683523814,
                                                                            2856033950142504282,
                                                                            -7571758476981896623,
                                                                            6815111860625165558,
                                                                            -4530529060403807729,
                                                                            -5827916594810006836,
                                                                            -1601346318959820783,
                                                                            -502026195536082636,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9dġ¡юͲσ*Ҭ˩ЕњǍ˴ʡʖȈÈԎД¤ýɤ˙ҙӒȇԅˑ·ĕ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024621.807024:+0000',
                                                                            '20210228:024621.807044:+0000',
                                                                            '20210228:024621.807052:+0000',
                                                                            '20210228:024621.807058:+0000',
                                                                            '20210228:024621.807064:+0000',
                                                                            '20210228:024621.807070:+0000',
                                                                            '20210228:024621.807076:+0000',
                                                                            '20210228:024621.807082:+0000',
                                                                            '20210228:024621.807087:+0000',
                                                                            '20210228:024621.807093:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƲƃΞ~Ʈ;εʿŕʋƣй\x9a4NоƈӈɔþϯϢһ\x81ϹÃ`ϧÜδ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1533192958152028470,
                                                    },
                                    },
                            {
                                        'name': 'ɈʧηŌBCԣѬɡőŚԌ˭ç',
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
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ĩąэʄзҦӪНƫȞʋɫĴǦǠȣѦʓȗѱĨҶˆ˼ΠǀØΙɟ\x90',
                    'message': 'ŢӼ\x9eΈą юŎȽңɾԠѕƅҔȳćƸ˸6ӄҖÝǹѼ˳ǓŚƗ҉',
                    'arguments': [
                            {
                                        'name': 'YĄƏȒǶ˅à5ͻЈѫŕϋŬÏˊ˕Ƙî\x7fИԔЯβÿȚp',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -9003505448689500380,
                                                    },
                                    },
                            {
                                        'name': 'ϡФ>҅ћԤ˕ǾůȿŋӦʑϻȗǜ^ȮӼӑ˾ИΩʾʄkЦʲ\x9fɸ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6129287388130057137,
                                                    },
                                    },
                            {
                                        'name': 'З˗Һ8ůǈӾȁςɐ]ϒˬɺĿˁHñҷxψӽΡʡǨрэξ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ºʩȘξϸԪʯБÑϮȲŔҌɆʿʥ<Ȣ҅ϨÊ"Ʌ"ΓǨİʪʤǶ',
                                                                            'ТӧŒ¸ƙƅɥƈΫȱҎЗԚ)˳ÂЯ˲\u0380ӥɾʉчѳЈʰƥϠʫŰ',
                                                                            'ɍͷӲÛȶ(ǘӎЦʏǏϫ˖ÜJӱƸÑӴĒǉҨԥ»Ƶǒșϭ\x9eź',
                                                                            'ʒВŤĨĶǻǁοĎϪʏŐǄϦɷǑϫϘƴɏê˦ҝĦңOҖ{ΌV',
                                                                            'ѹɾΪǃʐ˥űϤ7κΈ˷\x8cҚǪËŢӥøȎǓ˩˞ʋϳƇƍ\x7fӄ¢',
                                                                            'ԖϩɳҰ\x82ĹѸĭȕұԇɹ˔ˣ΅бƞʨӜǭìγªг҈эёȈ·v',
                                                                            '҈5ÐѽƋһψ\x8dТ҅ҐӴĨ"Ϯ˸Ҏɬǂ»ŇÁŔҙӌ\x97дŨԓѲ',
                                                                            'Ȗǆ\xad\xa0ʣ³œ¿ʼĄө.ѮȔӘӌƆĀм²ӊƼӑǓœ+ʦϜζO',
                                                                            '҂nƀЗĜωɃȫǺѽ˜ńźȩʠţsʝqΠő3?Ĥ˃ơѤҹ±À',
                                                                            'ůƖɾCəϷѿƜӈĄҶ#æOƋю)АȏõявZ×Җ\xadˊΪɠŮ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'à\x9f\u0378ȏ-ƞǚʞĽʇŤũ\u038bɮΒ\x9eЯČeƈʹΆŚģȹȁʴԓ\x9fɏ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8492285711927272144,
                                                                            -1693881974080699489,
                                                                            -49505034051774988,
                                                                            -1110704585364753164,
                                                                            2642118669203721736,
                                                                            1233017404752350217,
                                                                            -469300228928555987,
                                                                            6027422522403405811,
                                                                            -3610928857567587933,
                                                                            -8243577117606065498,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ïјаʦʛǛ»ӼѹĿӺρǃΎīӨҽҾāҢZƂұ¸ίү±ʓƕų',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 640920.7405775642,
                                                    },
                                    },
                            {
                                        'name': 'ɹȱ\x82ƱåėƟɗӡҺϠƳѡˇГ\x82ҼляðУ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024621.809240:+0000',
                                                    },
                                    },
                            {
                                        'name': '4:}ĕ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6898373946460701721,
                                                    },
                                    },
                            {
                                        'name': 'ĐɜʟȜ§š',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024621.809501:+0000',
                                                                            '20210228:024621.809513:+0000',
                                                                            '20210228:024621.809521:+0000',
                                                                            '20210228:024621.809527:+0000',
                                                                            '20210228:024621.809533:+0000',
                                                                            '20210228:024621.809539:+0000',
                                                                            '20210228:024621.809544:+0000',
                                                                            '20210228:024621.809550:+0000',
                                                                            '20210228:024621.809556:+0000',
                                                                            '20210228:024621.809562:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ШĤ\x8aÏƚþӎӞʬϻǭӶúӦRӓГBȒɝȿϺǬȜʦŠɇЁГ\u0379',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            309640.33991748956,
                                                                            673481.5633820957,
                                                                            -88507.1871866415,
                                                                            718587.124670708,
                                                                            56532.42349995041,
                                                                            708007.6057256773,
                                                                            33951.724598225905,
                                                                            225057.96388405212,
                                                                            415756.7900468015,
                                                                            199936.5360198088,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˑʔ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʙΩ΅÷kѸӶVȤΌЀɾɟ"ŦͶӆіû¡Ƹ˔Ϟτˤrö2˳ʘ',
                                                                            'Ϋұϖ\x87ˆԢҠԪ\x96ðņ΄ʻĸͼϯʜԀѶȖц»ѿαƔӡγÐOõ',
                                                                            'ȄʆɗÃў=ũĪƥƓώ˝ΟČҰЉƋѬMȕŢɭϕѪαȭĀÇӰe',
                                                                            'ˢӊĞǲΛÒɯĆɩ˂ԦÑԠƍɠѠȨϥÛϙбЍ_ҍѓ\u0382ȉ¿Οŉ',
                                                                            'ҬɐҾкɨɼȡ½˫ϗєϰΥóțҸǚªͰѼԛθɴîʨŎκЃЕҧ',
                                                                            'ӖҰђ-ОûɍԇʺΔԍʉϽĞΡɅў¿DϤӴЅÄ˱ɓ\x82ɇƍӡŻ',
                                                                            '¡ƅǙѐǬÆԏ҅ѻΫǐĄЅŠӢ+ɩÇƏДp\x86ђҐȑԨǎĊŢś',
                                                                            "\x80ǳӐ'ўԩɤɧϥѧȽԎй?tșĝCƿǁѼʭGØȂʨƝ\x8eҴ\x8e",
                                                                            'ө\x9fͷ¬ѷѰѢӳ£ęƹǻџɬы˖Ϭļ!ãūƂ\x84ɥȕοˮ6оԓ',
                                                                            'ͽƱʦҪӫϾËˬĚŏàȭ6ǋǆəһȔѤ\x99љĄѬĳǜƐʛ˔Ơʹ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ȏ\xad[ıʽ8Ȉ˫ȳǇǁŊӊčʈѸӽιƿQ\x7fϣĀт˄\x81ҵЧŇ˪',
                    'message': 'Æтźɵ\x96ɨӲИJθ0ԁӞƜ\u038däɿҍŻҔҼ˝ćͺʹšŊ҃ͱИ',
                    'arguments': [
                            {
                                        'name': 'ϭ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 548598.3161465524,
                                                    },
                                    },
                            {
                                        'name': 'ϚĦ¤ñїƵƖǊĊΨǚĹ˶xΜȺяńìӮɬ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'õŝϳҷыӟƁíϋɻȗԂƱНǫ҆ФƆʩҦðÒΰÑ˷˥\x85ԢψЈ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ω\x90mʰϦȃҽӂѐő"ǋ¡ʕ8^ǲˣ7ѭȡȱtʞǩ˧ԏwŉʪ',
                                                    },
                                    },
                            {
                                        'name': 'ɚÄǒΪƘĎÍϔӬúŃʭӥ\x96Αҷӏ\x7fȬȜщŭέ\x97F ĺϜɄк',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024621.811186:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɫŞʘԗѕԀҼ\x8cŧ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '§єTјԡМÐǱӠ˅ůэѤƻƨӱȕȄΤϲʊƚȴßźĮχ\x86YĎ',
                                                                            'ìʞЈǻғфӻѩ\x9f§Ԕӵ¿шҨ¯ȋҰßʯϩ(ӝˈϐH˱đƇ҉',
                                                                            'Ďč˛қɾζíиϏǕѧ\x86ЖЍĸ\x89ΣӗɠÜɬʣȥȖҢѬȅơíĀ',
                                                                            'УëЎǉɋ҇ɖ˲òŅА\x8bȓɡʱͲǀÅƠΤϑǥȝһғөΠ@ʯɅ',
                                                                            'ԁϯεAȗ˟¹ȁªÔѮΩЯͺȝǇˀƍӴĨ=ƋȹҨʵȺ˫ΎҏĦ',
                                                                            '҉ҚϦ\x99Ш\x89Ȃʉѕƃ»ȠôГԄqƫɸӗɹıʳƬӚ҇ʷԇēΘΝ',
                                                                            'ӥӆ"gɷƯѤӠUˌǬɨčќӂͼѤзŭ\u038d[ʚˈϨϟ˶ƞΫǙҥ',
                                                                            'ΕЯɗϧɡĎĵŋθ©ȪɸæѤƨŀbτ7ѥΥɛ7ƈ˗˙Ʉȅʊ$',
                                                                            'Ɗӯкǌл\u038bɟўɆӑȘːƄyȪŽƉ&Ò²ҝϐͻȼɚҏzêȊќ',
                                                                            'ĩȝåȆƎʵΨ˳Ǩӳ΄ɠ˄¶ƱҖPnԏΓһȠѷΆΦȖɖѨӻ©',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˇĻɤΘƴҀӬøƏ˵р·ƠȼѶʨ]$Eͼļ\u0378{˶H ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            211305.97302463936,
                                                                            950309.2710739444,
                                                                            481916.36457895604,
                                                                            782593.1862073273,
                                                                            407059.0303578492,
                                                                            260507.54612446722,
                                                                            -8430.890995143956,
                                                                            934594.8690626135,
                                                                            359508.1566420351,
                                                                            4807.903252642849,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƇΧ˵˦҄ϪҾģԦԘпә',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024621.812001:+0000',
                                                                            '20210228:024621.812015:+0000',
                                                                            '20210228:024621.812023:+0000',
                                                                            '20210228:024621.812029:+0000',
                                                                            '20210228:024621.812035:+0000',
                                                                            '20210228:024621.812042:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΔѸԍřҼ˘\x84ƠԣVҔęԃĆϓжЀŶ\u0379ĸ\x96ȦŞƚàȦ8\x81{ö',
                    'message': 'ĴȢШХÔȰǂҘќȇвȬŔǩʴo$ӏ\x98ҦħUС"ɤĪ[D\x88Ƿ',
                    'arguments': [
                            {
                                        'name': 'ФʻÏŊ\x94ӠȽŮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024621.812506:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʤɜ˳ȪȘ?YФ\x8cĵԇ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԑ~ŚƔϓӒ{BÒ<ʓeЇˀ\u0382Sυĉ^ΔȡǟϰǽĳΜȕ±Ѡқ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            8539.48823361333,
                                                                            349069.11787837313,
                                                                            115539.16434658691,
                                                                            809655.0719966477,
                                                                            136832.0156937877,
                                                                            921100.2696069013,
                                                                            360215.04896360985,
                                                                            108125.83036688092,
                                                                            730069.5607143206,
                                                                            498097.00163110683,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĥʒɷÐŉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -81535.20362453768,
                                                    },
                                    },
                            {
                                        'name': 'şóӝȣьˢΊԧȒөњѪǼΗȴюӘʬǻҧνŰСäаƒ\u03a2ǉ҈Ԉ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024621.813274:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɒŃԪʠNΟѹõ˪ˇѭʯƐ\x81Ǜ÷ƦɕҶlŔЈͶӧȰĎ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            939396.7897152917,
                                                                            429001.46314463974,
                                                                            266379.9794251445,
                                                                            592232.5317202404,
                                                                            530638.3673754295,
                                                                            476764.2893202719,
                                                                            741044.353676719,
                                                                            317.2462612803356,
                                                                            -70453.26538343352,
                                                                            38299.74517380289,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʥìʇŝɶ˃àəoˆÖӒtčϬŻũԍĖWϧͱΖʧȵрǮʬӽю',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ҵ˞ΜҋăҧΠA¯ͺ\x98\u0378˨өϖ¯ɼȉϨѸѺͰ˨ʙΉԧƽ˦Ωƃ',
                                                    },
                                    },
                            {
                                        'name': 'ȴӳøĄˉˣ҆ćZȬГ\x98ʵŔ\x9dţіćOũƉi˖´^ŏώƏȭʹ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 787506.9086703447,
                                                    },
                                    },
                            {
                                        'name': 'ϣ·Тɺ˵;ʞЫʡȶˁϝӎΎȞȤǿ˨®΅˘ĹʚДѕώɒ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -9116689862081444538,
                                                                            -7875864840681331793,
                                                                            1480574063634234225,
                                                                            6991718360414035155,
                                                                            5653377841446086601,
                                                                            -609040604973368179,
                                                                            -4645178144430986855,
                                                                            -3002666741224183693,
                                                                            6566851171187603812,
                                                                            1573207650847866442,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĳм\x8dǱӮɺīƤœȉɽąӱӿˢ¯\x89˖ČѽȥԋԗƉNʽήǔҊǋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024621.814331:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\u0382ԭǌ\x92āҎԖҎˣԭɔǟ´ͶýǤƙƬƷҖϹʦтϊωԢʟԝԩҕ',
                    'message': 'Ɖм˯?υĊԝÁЬɕèɅʮřЩÌ˅˷ѾɅƕβǩаŖ\u038dˍΘU[',
                    'arguments': [
                            {
                                        'name': 'ѬɞǓӎͽǠӳ!гÒj\u0379\u038dƒ˯ˑ͵',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 339986.59774597164,
                                                    },
                                    },
                            {
                                        'name': 'ʖƼdЉͲңrƮ\u0378ҡщȷȶЕæ_Ǧ2ҝÔƍ\u0380ͼЛĔьϐҴξƊ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024621.814949:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ԙԗô\x96ʒįñżȅǺ˧АɍԩɹŝʷӭƎț˂ӖΪϸ)ɫ҄Ώè\x8a',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024621.815123:+0000',
                                                                            '20210228:024621.815136:+0000',
                                                                            '20210228:024621.815144:+0000',
                                                                            '20210228:024621.815151:+0000',
                                                                            '20210228:024621.815157:+0000',
                                                                            '20210228:024621.815164:+0000',
                                                                            '20210228:024621.815170:+0000',
                                                                            '20210228:024621.815176:+0000',
                                                                            '20210228:024621.815182:+0000',
                                                                            '20210228:024621.815188:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ō\x8dЁѕӛǧðΈСͽȽ·ǟʂΎǛʋQżiҚruӑь',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǌƢȲȃĤжǾСnϒӷЗ6ӵΗɥϷ]\x99ÑŨȤХǆԌţіͼǝӝ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024621.815681:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԥƗχɓ¼ҧì_EúʰɌŵŭǴɘѕoīӦЦØÕȣ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            685959.1546377289,
                                                                            690587.6813986172,
                                                                            959077.6031107113,
                                                                            935030.2356157119,
                                                                            -75055.12875469119,
                                                                            424390.75437629083,
                                                                            164784.46808807284,
                                                                            912115.725386058,
                                                                            999923.4023121386,
                                                                            769006.0358961184,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƯυɴΫϨŊïҐϻіϥË\x84ÝѩɝѲ@ԤҩŶƃӪũ/ʈ˝Rσȵ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3333869793739304522,
                                                                            3553758008387228172,
                                                                            8164839022446508088,
                                                                            7449638215317427813,
                                                                            2392237260742340789,
                                                                            2233155844214718488,
                                                                            3996864673170781733,
                                                                            1258366204902502603,
                                                                            1350661854922602125,
                                                                            -9092568493629176837,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u038bďҒ!υ²d˵\x9bǴ³Ԇр/ɥыПȱɻoƱǾƓʻ˟qϻţȐ8',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7861798851869607562,
                                                                            -2600650447349338151,
                                                                            -8432881844608684557,
                                                                            -1632524884709546537,
                                                                            7976760150785350501,
                                                                            -7528890042880091963,
                                                                            -1619340658947553165,
                                                                            9018644610522456539,
                                                                            1991578201946611466,
                                                                            6331062945383611314,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ƑȌψϡÂІʴ˺ÀӌϴΧöӲӶÌˇǒόBӅǗ'ɇԤ",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024621.816608:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɫεİΌ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 193213.64208150835,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʍЎӣʀӕҔσ\u0380ġҬΊͲϑŊТ©ҍ˅ύ?ǒӲ\x95ΦȐϝ#ȡεΞ',
                    'message': 'ŕÝɪũыϞ\x9eɸ˪ΛϸΘˤUԧӌ½Уǧ]ąȐŘǡȔˡʠMãҁ',
                    'arguments': [
                            {
                                        'name': '@ЛQLϥ˷\u0383ʉĠ¿"ɆПȏąƿРèÔ\xa0ѯЎˁ˅ÒȢŵȮ\x89ф',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ń\x9aҿԌΐȱġϢ@χ\\²ȱ\x81ӏřƥϚɱΚЖŀƽӰĽ;Ҩɮ>Έ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024621.817834:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԃӃƺͶ\x95ƍɠNżZ˃ӀѦĕÎҝϦ˥҉ŗĕЌңʲɹғϦȞǄƔ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 366146.3032329443,
                                                    },
                                    },
                            {
                                        'name': 'åҢ˓ԨСʾАӟˀzʋɾӓZԝњDĥ˓ə˶řє',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ΖЬŒѵÍŕI˺Ь',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -69827.7139804636,
                                                    },
                                    },
                            {
                                        'name': 'ŧϔʚҟȬǜɔλίΪVŽԮȚŶʮ˟ǲ҄\x93ɚѳϾ\x80ΗͳŪϙˆɼ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x83εȯˊǑÀƲċһ\\ŭĒɌĀҔÏϼҘΝφҷǞʄҕqȠĩǗ\x80ȗ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˚ӋЎғļĝŊ:ΨԑͳϵѐʷˍƯΝңˇǣτʰʕԣͰħƗŏδç',
                                                    },
                                    },
                            {
                                        'name': '΅ǾЛϱȼ\x80Θθ7ԥGƦƂ\u0381iҢϗǱʢѝLʍʤúӤΌԃŠŧƖ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ģ\x90ίнˇҳĊ\x80ŒÌɣʀ\u03a2˫ӄǅę1Ý˪ӣυΟτÍ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϑȬƼƛŢ±śĬϨɀʹӹĭŸƏˢϟĜΰˬŮɴʐ)ΪέӢɨDm',
                                                    },
                                    },
                            {
                                        'name': 'êȳơʓǑѳʭ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            877699.1560925476,
                                                                            -18356.28668171451,
                                                                            160171.24616349526,
                                                                            765024.1043091684,
                                                                            263884.284531224,
                                                                            968775.5478111783,
                                                                            678667.0813467877,
                                                                            558663.2232210266,
                                                                            889149.989081285,
                                                                            -43130.01936042321,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӠƾʐɖźӋʰμΪ8ÀėҤ˦ǥŔӢЎĘPǶʹμӰZ·\x96ӥïт',
                    'message': 'әƛҝӽ˥ɝƄӕѵ7ӌ"ыдĕҡ϶JЮ˹ßǠԈŦϋѢĞѳʡʨ',
                    'arguments': [
                            {
                                        'name': 'ǨǏFɂGԒȗĭȽϪǩ®ўоÑґ˕ЏǛΨɳȚΗŀÎ\x92Gć',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 847527.3325469375,
                                                    },
                                    },
                            {
                                        'name': 'Є¸҄ӥӟ˯ȷЄɃӝiəӸʔȑӈɵȮ˫΅řčәϙșŅ˸0ɍĮ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'ή\x8eũŏÖàͳGнԬҧíΦȶĤŪÌˎɤYίϣ҃\x99\x8eǐр®ȤƠ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƚˮʩ\x9aΘҾͿŞĸğӣЮϞ¼Nʄғ3Z˽ŦѩŵʀčΣԦԋͼ,',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ņǡËĔǟǼ/ƍɪČĘːτÇҏ<G\x83ʸϲҡΑŽї\x82ǕƠџӰˡ',
                                                                            'ФÆʐ«QӤùȤҋӨ҈ȹς\x99ǸʞƐ{ɧЃɵА\x95ϊȿѿрĨ!R',
                                                                            'ҞѐǅģʰīҹƒĬQ\x96ӠȧӐþѕr˫ϼɾś\u0381ɄʨЍŕʋҵǎʾ',
                                                                            'ʩ|öʲίʨřɽЅ\x9eӜˮЋԤʘШŨƲsĺ҉Şʇ\x81ïƓɉõȴΛ',
                                                                            'ʒÒ´xȧǻҞʚƸ[ѯƽӔʹЕċӉȮÂùǂҚ´ԁӑФíoŬ)',
                                                                            'ԎϞѝxϊ:ΤҚУŊӢƯʍÙûπÉԊșж˲ќ7ԊĐ\x83ŔӎτÊ',
                                                                            'ўґ\u03a2ӀFǣԜ˩ʛдʊӮӽQΉƉ˃ӕƱѨǾӱʡŔǔʮΣ±Ϥѥ',
                                                                            'Υɓƞӊ-ƊĎҶ!ċΥĤΆ\x9f˞ӵѲΌ҂ЩԤǢҝŕʿӹƣȭƕȾ',
                                                                            'ʅД$іŲȤԆҭѹĭɫcҙƫʋ¬Ƙ`ċ˨\x82ǃԭτʁˊԢĸ°ʯ',
                                                                            'Ђ҃Ґăà<ͷϫˈфӜ\x92ƻϚǜΗЃӀԚªºѕβҺˠѱ\u0378ȼӕʍ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'эǀɴƪѤɒɠˍ΅ŵʤуϳȸż҂ǁÑ˾ҧϑĢėN\x80Ǡҫǧáʰ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĹʜӯԏѶǜŦα҅˂ɓʄѬ?`Ǘưʡ˫ůżДǑɪώҜѫ',
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
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÖčŝȾҮдӉįν\x8aʋǖϊ¿ɗ¦',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8140919308148952703,
                                                    },
                                    },
                            {
                                        'name': 'ɼЄЭʤϾ\x82ӄś¶\x9fɘ.ǳʛʥșːԗѨŗȉѨȺɋφÅǀ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
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
                                        'name': 'ҡƍȤԨǶҌƜОΨрʐӚқǜΦȺ8\x9cΠˊƊ\x96ȑʅ˴ϳ˹ȥĶҊ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            878042.7898555716,
                                                                            738463.3645637295,
                                                                            -56947.39135949599,
                                                                            404124.61251521966,
                                                                            525914.5759704803,
                                                                            249188.23623325845,
                                                                            955457.5092272572,
                                                                            -96445.47962154693,
                                                                            909322.9460025576,
                                                                            459566.3089972667,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'θǱ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            781973.1581005612,
                                                                            309168.51137965405,
                                                                            569172.7643523776,
                                                                            882627.9445601321,
                                                                            398861.4287049174,
                                                                            489226.6485790458,
                                                                            665959.263454815,
                                                                            -66501.22065454142,
                                                                            842368.1018465084,
                                                                            822673.1732856014,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϿđΟǯʉȣϑ|ɐ҃ȗtИϥɰēȤˤĥǧ(хǸΒƉİΞǥƝŒ',
                    'message': 'ń\x8aԞǏĀnΜćǃ˱ϏɨɶȅĥȀʠʖРɆ˛Ԙų¥ӹʃѼśŮѫ',
                    'arguments': [
                            {
                                        'name': 'ϝ\x9dł˽ɊŸŽԃȜ˓ɁɽϢ"',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -20287.516257943324,
                                                                            -78932.53361774699,
                                                                            268552.75726915785,
                                                                            672613.9882850025,
                                                                            967337.942012988,
                                                                            137958.1974057498,
                                                                            182857.57452479127,
                                                                            521150.01287811715,
                                                                            880260.5954099584,
                                                                            193633.65034254576,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʆϹ\u038dΡɾĥƩǎʝѷȶΌѤĐ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŗƾɿ_ÞҥК×ҨОɡӢĕǈŏγ-æ\x9eӹ˒\x9dȚĆԨ±ЖřԐȐ',
                                                    },
                                    },
                            {
                                        'name': 'НċЭ1ȱϩ!ԈŕПŪϋяʟ°η',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Åϡ/ɢ²҉ʥǷӭƱʑзȁҪ\x99зÒȊРĘɯҌɳ£Ӫѳ˝ˠȒп',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "ɹ'ӊŞƷĭϖʨǞшΑŵӉ΄Ƭ½h˘ìϖǿάҗŲǾȒɤөЕӅ",
                                                    },
                                    },
                            {
                                        'name': 'Ćύ˞½tѡfˋϪђǭȝ\x99ЪɆҞК',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '-К\u038d\xa0ǘҽc\x9bѫӎ8ҰɖԮWΉӁҪǠáЁ_ϮÈοбԚӢÊ´',
                                                                            'Ú˚ϾӢԧ҇ƒ˓ϩůȷЋɐɘhӎɥԈԭҞқУȝΉOəҦ˻ȩ˯',
                                                                            'wǱ±ɒȲǾӼǨUĵԙ\x99τ\u038dƶҥɦϷˏʂӂȺ˰ıƺΒ¥˕ҴД',
                                                                            'PҳɇǑԩôΨˀ;ȳԎƯȠʅʡ%ǶƤЉVˁǍϊэюƦÉɂ΄Ɍ',
                                                                            'ЂϫϯњǻɭΛƚsӒРš|ˉɈ\x8fËrʬɳŻZʝvԌ\x95ĔҎ2ǻ',
                                                                            'ȄҿňҼ\x9dЩώǦȾςɔƕˉ=ʽΕ\u0381ǡϫəʷϩҎöͲ҄˪ƿȓӧ',
                                                                            'ɟԣɒň¸ҪқԛďЅГÂāĝʹӢϵƱɰȢӠþÆːӪ\x8eʖԔąϣ',
                                                                            'į!ƻМѐҬͻӺĒˍӣ\x94ФʇѿȉϺǯԣȹҚƆӏŮҘȗ˫Ěɓԅ',
                                                                            'ӶɩǌƤϝǵȤ\x86?ˇǽǻįӣƕŰӦϑʢ҉ћˢиRӰǟϒԚǹʻ',
                                                                            '˵φЙσǃιͿӑȅԅƈȞļp<ʻ\x9dҳSҠŦάˀƹӂëˎ\x85rӇ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\xadpɜʸΖҺ˶hӺҒuƯΒÏԎʥɴвȶ\u03a2βǿ¡FM˽ГŤа˴',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɌƨɔΣɬǴѱГƳȍӯ˸ЪАЗӗӑϷȮѠƪƶƘϬȘʐĢѠȭϓ',
                                                    },
                                    },
                            {
                                        'name': 'ùóϕˊªϓЖ\u038dԇӂ˚}ƅȶђɴЍ\x99ɺǫЊԮШɲȷ£żδЎ´',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ЀǸˡ\u0382ȚпђҠUĝƣҬ´БÜҍǜԫɎӱÖĉϜǜҏΐêѯTȞ',
                                                                            'ȶʪ˹·\x7fȉΖԂόҶәԩƜЁʕǳžȪǯǣήΕэƳȡѱΛÏȿ²',
                                                                            'Б)ʩӵôƌӝħ\x8cʉiŅĥjԩĿ˙ԤЙ˙Ώȫ±Ļŭ˔ǟʃ?\x8a',
                                                                            'ˌԮΙɶδĸǻԌĤύӍC˶³ɬÇǣP£ÙȾӓ˱ҁųѤƆĉɝѹ',
                                                                            'ƿăЌϲ«Ψ²Ѳ/ǢӉʖƮƺ®Ѵ\x9c^ª\x81ƺɜʙþϩ˻ҕE£ʁ',
                                                                            'Ť@ŞƤԭ%xňЉ˰ťԅvϮýӴϦƖϡf˗ǨȔɭЄѕŚȲķ©',
                                                                            '¥ƅґʺ˃ԧЩЮȑǬŐо\u038bГлǺȆӿĴ\x89Θġҫǹ\u0380șӆaҿȊ',
                                                                            'ŦȌɂ^+\x8bвӅ\u03a2\u038b\x89ќĂĖґӏȼ\x9f˵ӑҺwőԜáÿ\x84ÇÜǤ',
                                                                            'Ŀӝ϶ұʓȓŊΙȰΩӿǈ4інǏ϶Аȉȱёҍ˞ʘІ˃Ӽ1ʝЎ',
                                                                            'űɊǹѬĪĔō}cG´ȯƯΑǅǿȘТύTÓ"ʁąÿÁ\x95ʲЎö',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˵\x7fǕũɗҒ˹ԄϨȵʌ!ԙʝj/ϝ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024621.825853:+0000',
                                                                            '20210228:024621.825881:+0000',
                                                                            '20210228:024621.825889:+0000',
                                                                            '20210228:024621.825896:+0000',
                                                                            '20210228:024621.825902:+0000',
                                                                            '20210228:024621.825908:+0000',
                                                                            '20210228:024621.825914:+0000',
                                                                            '20210228:024621.825920:+0000',
                                                                            '20210228:024621.825926:+0000',
                                                                            '20210228:024621.825932:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͼΑƒˏ\x89ȆƟϞğұ˻йІҟĲƉȉʿĘ®˵¼ԑɊǪċHдRі',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 211859.80393057945,
                                                    },
                                    },
                            {
                                        'name': 'ҨаřûӉԁ\u0382ϏĠŧéýƇ.ΩȠͶ˻бûȑͶǻԮ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ΉŵÄ҆ӫɊѵΟĠϟњϷĨŴȠѼТǞĳԄӌůɸõƼϹưЉiѭ',
                                                                            'ЅĽŲ˵ƴčҧ<\u038b҆ξǖʊí˛×ȔǒǻÅʑǍΏʼƈǃϯǹџĺ',
                                                                            'ɈȀѼ\xa0GԣćҊ;ΰβʝǚϧēľFŅŤǜϓƛÅԄƧԭYʏȴԓ',
                                                                            '˘ιΖȏʆѼþ\xadˉŐʅƟ\x8fĀԄ*8ȘĺƾĔџǒѐϭ°юʂȎʜ',
                                                                            'ѐҕЖԕεsҡ\x81ưБƅťīĊЇҶēɃƸίѓǘѯəžȹËħĝá',
                                                                            'ӭā˻ƾȨ=ɇпԆˢŠIȲ\u0383ƫѝԌҠcʛΦʃҝҌŊ;ɐѪΘƻ',
                                                                            'ԭӍΞϰтΆ˅ͻņšɐȦƶ\x97ԉӻȷΊȹŌЏԠǘǜϴӀ\x9cΪωӬ',
                                                                            'ϙUǰǱ\x89ԣŞҕįЉÓȞDЧăŃÉҙ\x94Ӆ\x9eȞ~бBɊȟωĐ\x9d',
                                                                            'Ν!хԏ\x88ȭ΅θӭĜȩųʷ˃¬χšŧӛq˶ż\x85Ýú³Ϭbaӓ',
                                                                            'ÍʶŞ×ʫͼɞвëò\x85ҽŅҢuȄ7ƊlϏdçκźɌύb¸l\x9b',
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

            'scope': 'verbose',

            'messages': [
                {
                    'catalog': 'ǔѴ',
                    'message': 'Ѝ',
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
            'identifier': 'ԭΈĘԒΤϸќе˹ǺϼϴʍǐǀΗćÚƅŵŭˤȞƐΏĄʙóҒı',
            'categories': [
                'invalid-user-action',
                'invalid-user-action',
                'access-restriction',
                'internal',
                'network',
                'os',
                'network',
                'network',
                'network',
                'internal',
            ],
            'source': 'ŠɎӶĲĕŘʐë.ͼƼĘ\u0378ŔƙʷÑӃ\xadȺæшǳбǷѪʡȈҩŅ',
            'messages': [
                {
                    'catalog': 'ȀĬƴҠһÎFȿʲԭțùӾſǇ\x95@ǸїЇʓʂɖ\u038dǽɴɜĝǙǙ',
                    'message': 'ʀ҇ƀàȪ˂ŉĻŋƲǘƎ˦҃ԁӜӇϤшùxǥĥӕԏměї˄ƒ',
                    'arguments': [
                            {
                                        'name': 'ζϯϮćʊƊįƠȇȇыѿиŽ\x8aѽΡ¦ǫ˒ҋɴŠŉ<ǏʹҐȖЋ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            212074.7098706108,
                                                                            185596.9764306852,
                                                                            335614.8327897902,
                                                                            95628.70143057426,
                                                                            643170.8022432359,
                                                                            482415.825295817,
                                                                            995500.4760426048,
                                                                            340107.6967916529,
                                                                            -62377.77368499422,
                                                                            792401.9180432947,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʰɕȳ˶ΧԏEʠňʶͻÞпҬˁȭӴеӭƅɹѡȭхġ;ʟΚƒƷ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024621.855811:+0000',
                                                                            '20210228:024621.855838:+0000',
                                                                            '20210228:024621.855847:+0000',
                                                                            '20210228:024621.855853:+0000',
                                                                            '20210228:024621.855859:+0000',
                                                                            '20210228:024621.855865:+0000',
                                                                            '20210228:024621.855871:+0000',
                                                                            '20210228:024621.855877:+0000',
                                                                            '20210228:024621.855883:+0000',
                                                                            '20210228:024621.855889:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЖΐѻԊʲ\x89ʏΙɏƴǆɋ!Ąǒ0ŮʪĈɍǑʵѱ˨ˎɈȳв',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'qҝűʒϹѲƀƯѾȼѨșŗɐŮȯҍ\x97Ǔ˓К_ϬÈ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2919042534296768712,
                                                                            -5971007376598695876,
                                                                            1526774054791488074,
                                                                            -8531142891371637422,
                                                                            -1382228505510790413,
                                                                            5041178506563457194,
                                                                            7813776294272180440,
                                                                            -6878756266246235949,
                                                                            6594246327522234703,
                                                                            -5628863670504405450,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɭƟ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӢjûǗҺ¿˷ҝƇɓ\u03a2ɗˌć\x9eŐͿəήŹϺþ\x96ĥ±ɪҝÒ˳ı',
                                                    },
                                    },
                            {
                                        'name': 'Љͷŏϼ½˲þÈґЉζɜӕĄѬ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 21283.173693516146,
                                                    },
                                    },
                            {
                                        'name': 'ԡʠlҔЙΥȣ¤Ĉ\x82ȔӒʅϢ¶oжҪ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4893567680528251295,
                                                    },
                                    },
                            {
                                        'name': 'ЈũşçÃçϝȴЩƢΣѲŏȧϯɄȀ¢ʁ¶ΦȘЙόǌ¢ϢǧȋĴ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϯАȜĠµӎӥǶǻƟςНӢǾˬĉӥšL˯ɛǾǑƯĖ\u0383у҆˸ҏ',
                                                                            'ӥΏєаŌҘӫΖӾƠǢςаБ΄¼ӛԃʑМĻǱǇѿĬɓΛΌϖu',
                                                                            'ΌҵŹ҉ė"υľÇŌʞИʵʣҝɞ}˟ĲҀƑ³ҕѵƒHɃYʩӼ',
                                                                            '\u0378Ǎ(ȼӺɝѣщɗȊ\x96PϰàԁɀǇɥóѲЗǒŗΫЕ˽СӖ\x97Ц',
                                                                            '<ɯԟƔ\x97ǚΉХƎɁƭјŎϐÀ÷\u038bʝԪOº˱ȕΎǎ«\u038dЍ\u0378ˌ',
                                                                            '±°˫ǉӽҼ$ѕ\u038bЉΰыəǈ÷ʴµ˹ӵѾΒ3ÄƭАű\\śǩK',
                                                                            'ǘ\x83ŗƞNѣƂԐӄ΄ϸƭѰǕɌ˲ƗԭoңŌҚʆĂȨūԡЦkϨ',
                                                                            'ʉńeјС;_ɸˤѥкԤ\u0381ȯʊԝʃpΞԛď!ϻԨrёƴΘӞԣ',
                                                                            'υʿʭā˞Å·<ɺӷ$В!ϖǷǖ˖{ƻǩʲ\u0382Μǵ˾ѹōюȍǁ',
                                                                            'αŌЗʹ2®ɬԡǀΐƘŢιhυÙԐǫʢҽʽ\u038dуεu³ə{Шƒ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȓǼτҸû¾ВĝɈ+¨ƽΔ΅ĥӆJ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɫ;˷ǗǯƋǂϿʄ{аΏ˃АǙϖƂ˴¥ҵʺɽUƬЯӳѲӭѼĥ',
                                                                            'Ŧł˪ǆ/ŸѓΆǷlĥɔшgɶ¿Ԑʨ҄ǢJйЩ±ҌžǱĳĻϯ',
                                                                            'ƎċȪ:љ\x8bυȬˢ«ˑǎΞ҆Ҹīѓϒ\x93ԂӚîϮЩɡŒĄʍϟң',
                                                                            'Ѽȵ¸ҏ˾ʧųʀƯӿƦÖŕ\x8dȍґԅȺвɽƓ͵ˊʊɻҮŗЇ\x94ҿ',
                                                                            'ЇȆђυƱʱӆϩѰ˩φÌ˥ĔȦ"Œĭ\xa0ɸӡɭˏɃǿΏÚxӎȿ',
                                                                            'ΎԪȱŖŖöʕƘɡŐӸБФεͼÆʔӅɋř˶Њʯʣ҇ѲӤ˨ǀ˃',
                                                                            'ğĺƉĶǆưΖѣʡҗҒԜʋĹƠɾϬҮͽŉҽ˩ΕŒǠѾϰҔdɛ',
                                                                            'ÉϔĦʓϑ&Ӆ˯ʼǃӈğƮџϏϑфÿ˪ƎǣÒԦӑǭŸɶŤҟϤ',
                                                                            'ӀΒêȻҤĄΤЪІÈǖ˕ǝϻ9φRΦѰΔӕŶȇƵŃҹЃΤҞа',
                                                                            'ҁѭŤԦԠǖƘñɵқȣþțȘÆɮ#ʦƐΉŻƊȄAʇЉӳЖΝĸ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЊĢ\x95ȯρӱҤĿǌɈԠӨԣƓ\x9cǖӈ,ҟ\x9bɧӾϒѷϽѢѥşзȺ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            455908.65295174136,
                                                                            427359.8282117079,
                                                                            228554.18467239774,
                                                                            424187.13670475176,
                                                                            360013.0774257989,
                                                                            839238.0678888138,
                                                                            744830.1888426237,
                                                                            928805.1346635986,
                                                                            963130.6194356896,
                                                                            377791.5268533362,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӴͶҏ\u03a2ώЈũ\x907ЭâɺΠβȗůȞҙqȼ=ԍ3[Ɏ˛d˕Ļ˱',
                    'message': 'èЁɼ\x88ƈʬӰː҆ӂ',
                    'arguments': [
                            {
                                        'name': 'ɒνЍȨĎȫξΏԉԐӸӌ-РΖ,Õ|ǵȭƧʡˎÜԨѸƬd҆϶',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'æ²ʠ´+ΥˡƌǏΈηɻǥвŏԬОԦӐ\x92§pϒ˝ϬѪΟȜ˅Ƞ',
                                                    },
                                    },
                            {
                                        'name': 'Ŷ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӸϟΙåȧŭºʸ\x83ΝүɺǹÔûċ˯wҾǼȻƏ:џԡɾ˰ǁʕЈ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3421765352952028593,
                                                    },
                                    },
                            {
                                        'name': 'ѱɏӍ"Ė',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ҍǵ=ϱʿ΅ДҪϳ\u038bʳǑˢĉӡҧӂӼԡцЦȣh\x9eXӣŽ1Ǻ¾',
                                                    },
                                    },
                            {
                                        'name': 'ȴΨǢʿƧϯpҤǥðҴͿˉ\u03a2ΔŭȴΦùОԠƨп',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            690838.105821924,
                                                                            289586.96696676925,
                                                                            564372.6804131943,
                                                                            489902.68874161947,
                                                                            678349.7939081327,
                                                                            643794.2592465046,
                                                                            924793.6715768633,
                                                                            -25476.233723962403,
                                                                            158569.93726092533,
                                                                            -70447.47805810523,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȣʗДźХӪǲ\x96ϫ\x9fηbĦӊ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            9185166255111869815,
                                                                            -7848217496932128886,
                                                                            -1154751063992828991,
                                                                            2135463054535587277,
                                                                            6839642746421255812,
                                                                            6797582921299804829,
                                                                            2430122801984054480,
                                                                            -7239790944416416662,
                                                                            916352293257653815,
                                                                            5896605395122313027,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԣȥǗ½Ǭө=ʟʴδԦΞԝѸέņξȯԕɰЁѻˬЁɈ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӓϮϖΙь',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4583759630565634552,
                                                    },
                                    },
                            {
                                        'name': '¿ŽҲƃƹ΄ЉЭЅƔЩѺǗϒǈ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2026232696971489166,
                                                                            7190900909992148465,
                                                                            5764166990275256113,
                                                                            -2468671567726699707,
                                                                            1504982674299180222,
                                                                            798385194444527425,
                                                                            -702594831157371085,
                                                                            -2437038781957281587,
                                                                            -7027807062001637245,
                                                                            2349585421561881187,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƣ϶ļςϸ1ԫІ´ÙȯɚɓчʶΎĻЈҺ˔ʲΧǐЮϗϣ\x96ŶOº',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024621.860003:+0000',
                                                                            '20210228:024621.860018:+0000',
                                                                            '20210228:024621.860026:+0000',
                                                                            '20210228:024621.860033:+0000',
                                                                            '20210228:024621.860039:+0000',
                                                                            '20210228:024621.860045:+0000',
                                                                            '20210228:024621.860051:+0000',
                                                                            '20210228:024621.860057:+0000',
                                                                            '20210228:024621.860062:+0000',
                                                                            '20210228:024621.860068:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ī3Ӹѭȯǅ҈ђè&ʍ҂сÊɢņӛʴǙɶт˛ˁ\x89ͳαŪƟ7ї',
                    'message': 'Ђ\x9aҰŻЙăӿŋΕˡ˯QʩàĲ\x8eԍèƳ¯ɺăØÔǦӷ\x9dӄlǬ',
                    'arguments': [
                            {
                                        'name': 'Р4ҾǓǮˋҟȦѡɴR\u0383ȖԓɵӗkȨöäʉӭˈ¹ǫÜΦŏр1',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024621.860577:+0000',
                                                                            '20210228:024621.860590:+0000',
                                                                            '20210228:024621.860598:+0000',
                                                                            '20210228:024621.860604:+0000',
                                                                            '20210228:024621.860610:+0000',
                                                                            '20210228:024621.860616:+0000',
                                                                            '20210228:024621.860622:+0000',
                                                                            '20210228:024621.860628:+0000',
                                                                            '20210228:024621.860634:+0000',
                                                                            '20210228:024621.860640:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x91ʤäɞȴ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʻçƴԛȜϪʤΔϲɻɦ¹ĻZȚħǒƒ¢ȰϷʮҡґĀӸǉƱɕѫ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'вȤy5ЀǿYǈFŹčΎ҈қ҅ƃFЕĔТӬɸŏ˖ǠÝІNľǥ',
                                                                            'ąţҿȬЀĹĉʑȾόȎϓOӒμӝѻǴ7ҵΝǀơǠŲόͱˏƦǵ',
                                                                            'ӿɸ>ȗČďҕӑҞτӿƓ¥±ơϥĢý\x81ǨхĞɨȀŌ9ӭŁџό',
                                                                            'цρǒşɰ]Ǳͱ\x824χƯɃѭȯɉǲЙ˂Ŵ¼ʚůӭ\x9eȎôƝ¥ĉ',
                                                                            'ҦȎЎe\u0383ҽ×Ʋун҂ӫМҪoϮКԋұʹɗ˧ЩϼӮūŁϽͽŎ',
                                                                            '˪ȴºʛӚΛáǸŐѶ҇ҹ˾ҲįԦÜſƛǅ\x87ǱЂѸŀƓƽѡӾӔ',
                                                                            'Ȗ҄Ѵ\u038dԍȼðҶ\x88ҷȓǮӕӣʂêӱɪǆȭήХŴ\u03a2ѶłȪĖƊѱ',
                                                                            'ңż-ȮϡοѸáe4ˀɀӊӎ¿9ǡɹƅ"ϬЊɺƢӘѓӦ˪đӤ',
                                                                            'ɠЦwφ΄2Ƃ\x93Ëėͱ*ȡчέzƣ%Ċ\x7fЀтvδу\x93ӿǎ´ă',
                                                                            'řš-ϸȹAĂҽԬѹƹŤȠЙƛǟԄԫѯљҸÈЃҽʦƉĢνǸɻ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Üϲ\x9aȽˌ¯ӊƹɺί£нǘЧǤҦȭŧқ¬ɸY',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            320618182110934486,
                                                                            7167571637209285712,
                                                                            -6582427293118946736,
                                                                            -4515495547373891904,
                                                                            -413946596111859913,
                                                                            1930870272906940427,
                                                                            2007123243502808564,
                                                                            4660913899474161638,
                                                                            -9101870888036266877,
                                                                            8713704139734273538,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȯ҆ƔΩȉĜӝǏԣǒд',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ҕзųˣ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024621.861786:+0000',
                                                                            '20210228:024621.861799:+0000',
                                                                            '20210228:024621.861807:+0000',
                                                                            '20210228:024621.861814:+0000',
                                                                            '20210228:024621.861820:+0000',
                                                                            '20210228:024621.861826:+0000',
                                                                            '20210228:024621.861832:+0000',
                                                                            '20210228:024621.861837:+0000',
                                                                            '20210228:024621.861843:+0000',
                                                                            '20210228:024621.861849:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӳЛϥŃɦèԒǞpƺǯ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˫\x9eɒȽɋҟɬԭŶԔԑʷÞћ¨ԠȌԉ\x8bɄT\x9bǃǚμҿӝĂͲо',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            843959.9334638902,
                                                                            862769.9923922942,
                                                                            499607.12698544876,
                                                                            277199.044939406,
                                                                            26451.835309276124,
                                                                            141731.39611033502,
                                                                            581940.6531769288,
                                                                            286608.05951458414,
                                                                            -31211.656583883057,
                                                                            970315.6875270477,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɮĳ˝΅ƄϹҍϴȣΘϾԃɝʅ$ŮǯӈϧљɐσЄГďшŻĄҫå',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҟҧɡϳӋСΞĒϽ;ҵɒǂғӉɮǥӆϠ˲ϺԉļSēɎԎĸřʲ',
                                                                            'ˏȵţǶÆ\x99дю½ÎȈӖȯŒκǋʗǥfϦǠŋӆϘƋ;ҿԇʈӭ',
                                                                            'ΉϐԞѴѭǜĕƂϘĆѦ\x81˧ʯNɓɡɣƯʰȰԍӢӸĿĳСԏđӤ',
                                                                            "ɤˁϴєƏÕ˹'ңŌĀ»řˋŒϱџƄĻɟҵĞĵ.ùӤπә˟Ή",
                                                                            'ȔԀ¡ÜȄСɶӸԛ-ǺǔџԥȷѱªʖʦˁҲҋйʯҍ4ǸÏʠƖ',
                                                                            'ăęӾOƌԗͶɎɐш;ɽƩ\x8aƩȹȵȽåžҞΏ1ˌřΥƺ˷ԄW',
                                                                            'Ͷ¶ʿϔγԤΩ4φ˙ˡЖȠȿΕДŇƮщҵЮˎθʓāØG˕Ҫų',
                                                                            'kѰþ˱ϟɩΉǮ9ǃǢƵ˺ǡzĠԄʙ\x92ǩӶχӼgřȬýĒȦˠ',
                                                                            'őƦǹʕӴí˥ñƔƁӱɫӹŅѨʛƿԀ˞əԌΝďӋǷԔǇʸԗǸ',
                                                                            'ȽϒˆˁͰШÜΘ͵ґɆӊä\x87҅ԡǧ;ĺΦϙôǐӥԨżȿŃĵӆ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɖÏăТ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1593832683864843541,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "ПϥǠŨяŷɛ'®˗ӻġұėñĴƕġ\x860Ɛɞƍ(ʰСӐðԌŝ",
                    'message': '\u038bЮѲŉə˙ҋҒƦк\u0379¥ȸρϱƞʼɲǫ6ǁ˩ǄΖΌıЍ»ɓҞ',
                    'arguments': [
                            {
                                        'name': '\x85˳ĉˬʪ¬ʜπåӏǟϪʌϸʗӜʹЀÒjȚЅӻāһӄ¼ƅӦǣ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -11733.28612153852,
                                                    },
                                    },
                            {
                                        'name': 'ǈǬ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024621.863611:+0000',
                                                    },
                                    },
                            {
                                        'name': '(ӬͽǅҊȲÓƂԀӟ\x8cї',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
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
                                        'name': '¿ƩȜVŽ\x94ɜ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2478913874454941221,
                                                    },
                                    },
                            {
                                        'name': 'WhӲɼŞűӲ\u0383yчӂɨĻ\u038b',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԫ˚±ϿǇÔaӀ\x87ŘҒ1ΔϞƤјǭˍпӓţώӌ(ѣǱϛΰ˂\x9f',
                                                                            'ŋ\x93BɵԮЎӶʝУċäЌġή\x82єӀɪǶȽƕäȿШØnОͺϺ˞',
                                                                            '҆ŬҞЋ´ԣКѹ˲Ͳ\u0380ǮӍȶ˗oǳуĢɎɧҝрÁǯӤȀӿÅ§',
                                                                            'SΩїɦŌˆЩȐɵҔƳŞ˄ұŻβηŁɨÍЍGбʪȭԫ]ʩ\x94Δ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '®ʃµƅʁ\x87˱ԜӄiԒƪҺИĲӤɆȃјͲȨʐÿԚЄԞt2Ōʙ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ıΘБȀʯԒŧkɹѪŗəŋ\xadiHåɪMSϝдόƲh¾ʥθƻů',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
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
                            {
                                        'name': 'Ɵyʔ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7908609777872371826,
                                                                            -47463047130552526,
                                                                            -3611599629828846796,
                                                                            1064833711056522707,
                                                                            -7730444268911714552,
                                                                            -6355542913551424733,
                                                                            -8836731520606236964,
                                                                            -2910100777489107177,
                                                                            -4871474744361507399,
                                                                            -4493972331482900257,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '!ĭѣΣϿɗɥΉĸ\u038bЖ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            9035582439497709177,
                                                                            -647231511383398636,
                                                                            534209304843477651,
                                                                            2042111291297754456,
                                                                            4841108132001008972,
                                                                            -428683088565984404,
                                                                            -4000997904403164960,
                                                                            -4346579608216499412,
                                                                            6799474555469451349,
                                                                            -209887990702123002,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʁщΉԛɦϤ˵ñϺ˓ɚɰŒʩҽ\x98ɼгωĸɢҋʦϠǮ\xa0ÑåЀУ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 348728.7656797701,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'n?ԢҮ*ΊʃΟ˧˛BuϿƅů:ʎӆÊ˾ӷʊĿǜpѥЮʸЏw',
                    'message': 'ĥǐ˔ōƐ_ΠşZϔўȎǧDʃ\x97˗ʑŉÓҜ\\ΤӃ¤Ԟɿ҇НǴ',
                    'arguments': [
                            {
                                        'name': 'ӹ˼˸ЋͿɧCË.ǾɠǿĭЫƴȭәҒɣOΊƃ\x88¬ʕОΉӢ;İ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'τȝϏ,҇ȾǴǫηŘЇɇΕψƳĜЗĒъƈ\x91АnʕéѳӡȈΏ\x8e',
                                                                            'ЉϬɁӾº˸ӧώť\x9bŏԙԛƔˇʚɴŊǴЪĠÂ϶ёÑъcǠŬİ',
                                                                            'ő҃͵ӷǬTηԕȀ˥ʓōĳΈΟșЌǄўϬĸ\x83ØԮҧЃΛ˺ȩŗ',
                                                                            'ȀǶҫΚӮÚӮ0ԐͷȦ®Ѱˊ˨ЩAaͺϞ\x9eԪěҠĝ˭#Ɵ÷ŧ',
                                                                            'ʹ$ӷȗԋ\x95ǥԥԫťÓºӔҽϰ\x99ҳϗƐӘ÷ΦҏƓĭҧλǧкѣ',
                                                                            'ÜǾрϢƌàԌƟ\x8fˉȷkƗêοöˠσɗԎ΄҉ŽːȀ˼ʅȍįӝ',
                                                                            'İ|҉ӂɀҙʰˡӃŲ,б\x85Ӎİ˾ɫΨξĔ2ǿʈůĨϓϧďϕt',
                                                                            '\u038bĮȆÅʋøӯʒЇ˰˚ҚƕǨӐ͵ʨĦіóЊzˢӌ4ь\x9cȯЁǶ',
                                                                            'ȥ\u0379іύBԒƋЭƽǩЖȼЯԭǎɔȘˌʩͳѰʥ\x97ʂ˄ʀʭҮŀĆ',
                                                                            'łлǧ\x8eđĺ^¹2ɵȫЕƙ˞ʢƥ\x91ԛδƛüƌfԔ#ЍǼÓҘС',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǽwDȊʜƆˆәϔ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 870337.7815891377,
                                                    },
                                    },
                            {
                                        'name': 'ɍŪʓǇǴʁi\u038d\u0383ƙхƌ\x99ƈʭǁϕȬэӼѡ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƑȢѸɹ®\x81Ӡŏ^ŋg',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2599549037863649933,
                                                    },
                                    },
                            {
                                        'name': 'ɇЎȾҩĈӣԌͶџʨӱǅҝѼǾͰӢßîůŅĲϺɕ)ȐɈ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "ǔҢӖϝɎӽӜ'ȱʝѨŸôСȋºԂģ҂ɕɈǃҹwƽκά2ƶˉ",
                                                                            'ʅο˩˯ďAϓßºŜŐʆɦĶѡʠчϫӇƹҬƚaɛҲÕʑʡΎԧ',
                                                                            "'ϋ|Έ˝ФͶȂȀIɁǗɐщЬįрʘȭȇ͵÷ǁӒѤ˽ŰҬŖƳ",
                                                                            'ҕΌȱƴӮƱ§ĸ|ʑӑΉЌƹĤđҿʏҞȥɧ\x9cɍ\x97ʜҜŠǄħǙ',
                                                                            'ĳăǿҌБɓԎϪȈʇНȾϘFԉɜøʗԋҷźɔӜӶϤʳТѪԞӯ',
                                                                            'Ì\x84Чԩ·&ϾƓƲ˱ҽˈAšǄˍΎˮѮҜЃ#ɂƮԈjԇĻɠР',
                                                                            'ʵ\x84ɽКź©"\u03a2ȱºƻĿӯȢĒǴlԖԫ5ÀȞĐѭϲԆ8xNȅ',
                                                                            'ÛLŭq$҂ƚǟʰӵӕǁʰӠZɡʢЧřÞЂԘɠ˜Ԁ4ԝΧˏ¥',
                                                                            'ĹĐЃaîϋϠЌ×ęȦ§ɸˎϮȧӔƩԖʿӳΊŴĵǼ;xԉǦӻ',
                                                                            '®ǫԙѩԝǕӭΙÐĒ5Ļɋɍü\x86А\u0382ǒɉǽɺѠȠκ˙ǷÜʛι',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '϶¢бѴԫYϾƕǕӗǶŊΠŜҗϟȇ˪бƘÅ˘ԄȠʝʗ\x90ԚȴB',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ÒĳÉȉЉȩήҘӇѽ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024621.868147:+0000',
                                                                            '20210228:024621.868216:+0000',
                                                                            '20210228:024621.868245:+0000',
                                                                            '20210228:024621.868265:+0000',
                                                                            '20210228:024621.868297:+0000',
                                                                            '20210228:024621.868315:+0000',
                                                                            '20210228:024621.868334:+0000',
                                                                            '20210228:024621.868352:+0000',
                                                                            '20210228:024621.868372:+0000',
                                                                            '20210228:024621.868392:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʝsу˄\x91±Г',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -66765.96651764981,
                                                    },
                                    },
                            {
                                        'name': '¢ͽЙÿɵіѨѴÉÙͱȀnξΣʃɋƋúǶˮҳĹ7µʳȖ˚ϑΩ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƓŝґɽҖӜǅ^ϰӚńςǕӅ±ҦјƃǯˇƇǖʚńѥʱ·\\ŀҙ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8360221030215951161,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ĝмҵӐŊàЬϠɺǻӜӏó˵ƉӃҌΑΫƿƤӪ\x9dϠɳϻ҄ʱŬɠ',
                    'message': 'вϛ˦ȆГӢƼҎƠΓ\x7fÙҖāіѐѷԩːʶĎ˵ƛǽƺҨ\x93϶ʦŔ',
                    'arguments': [
                            {
                                        'name': 'ò\u0378ЇϨ¡˵Ϳʜн\x99ɃȉŲƿɴПѧӫȿɁEɨŲɪsμtŰCƴ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024621.869814:+0000',
                                                                            '20210228:024621.869837:+0000',
                                                                            '20210228:024621.869846:+0000',
                                                                            '20210228:024621.869854:+0000',
                                                                            '20210228:024621.869861:+0000',
                                                                            '20210228:024621.869868:+0000',
                                                                            '20210228:024621.869875:+0000',
                                                                            '20210228:024621.869882:+0000',
                                                                            '20210228:024621.869888:+0000',
                                                                            '20210228:024621.869895:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӅơӐʆơ¼әµƯѽ$ȌȌ˰ɉƊЭƴȅĵӂ˚Ӡ\\ũɔϔӌАſ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5512699406233446530,
                                                    },
                                    },
                            {
                                        'name': 'íЛʰЀȜ5ȸЊÉЄӁӈǍǕΥ¯ʩŪђτ¿\x9dӈɎ¤ѯӌԒˈǟ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǵƣ\u038bʾûĬƼζӮɚŽέѿǁ|рǫӂƱӶĘϕӊϳҼ´ϳřʱɹ',
                                                    },
                                    },
                            {
                                        'name': 'ӚΒԎњɉԑϟÙʠüΎԄ®Ïůʲ³ƏÈøˁSɄȲϺԘӡϷªŢ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ГùÂΏѝǞζx®Ȅƀ˕ԪǧƼдԒ¸˅˼аԮŪɕźǚňƟ\x8bч',
                                                                            'ƮŉʁЮɰͲΚӸΖхʂĒ˳ćĕ;ʇƔϘʳ˲#ȤҬɍȯɕǔɦĒ',
                                                                            "Ɂ¶ѓΧŗɑΜҗϹNѩƗhƭʅʷǏ'âҥĄŹ¾ǙȜԪāǩƍԈ",
                                                                            'Ʈҹʎ˦ɿ|ӻʇʓYʔơʥƱ¨ңǊɔ\x9cʫǨйӬЍÐĘʯ\u0378ФѪ',
                                                                            'ɢ¨νӖ҄âԚ͵ÆǥŎÉȣHԗЩƖыǆʚɕѹςˇĴǚНΌĘ¡',
                                                                            'ƇѼʤͱ˞ɉϡˊΪȃ΅ӤιāѯЩ[҆˝ҕŝҩĽáÁȂĩjиu',
                                                                            'άƏԧŉˉ"ũѯΐƊΒ¤ˬΩѶ\u0379ɿҎӀΙфǍљȰêʣϐ҃ĥ¹',
                                                                            'ԍϳ¿ȾȸǥɣHʝӚэΡўÖɺȒϪ;iċҼ[˟ҵԦ÷χƜϮ˂',
                                                                            'ѮɲϬ[CѿɽdÎ±\x9cԉÀ\x97ϱ˷Ȥ\x7fӛʷ½Л\u038b?ʇiɊɥһŬ',
                                                                            'ӫ(àˏЎÎqɰķʓX˒Ϩʅ˅\u03a2ҡóT˧Ňˮ\x9c˓ԗʹƥǺƁ®',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'þíҿВѹ΅˟pŐ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 678454.7029723922,
                                                    },
                                    },
                            {
                                        'name': 'ѧ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʏчώрEβŧđЉ0ʬŐöɭЇԄɸÉϜĸòηIԞMƟɎԓЋ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 482309.13274899253,
                                                    },
                                    },
                            {
                                        'name': 'ųЉǣŧ;ʗɡʫɧϥřΊШÌ˶4ϖ\x96¹ӮVð9ȓ˥ϴяş\x9bț',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            56160.26681575517,
                                                                            -55382.03968795826,
                                                                            906465.794441239,
                                                                            37337.82856054226,
                                                                            79338.42355878436,
                                                                            72270.76962386008,
                                                                            346750.8560010853,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҋđ¨ѻʿъȈψ˦ѡЮҴсѣöкѺɢ˧íġƠʏIC|',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024621.871910:+0000',
                                                                            '20210228:024621.871930:+0000',
                                                                            '20210228:024621.871938:+0000',
                                                                            '20210228:024621.871944:+0000',
                                                                            '20210228:024621.871951:+0000',
                                                                            '20210228:024621.871957:+0000',
                                                                            '20210228:024621.871963:+0000',
                                                                            '20210228:024621.871968:+0000',
                                                                            '20210228:024621.871974:+0000',
                                                                            '20210228:024621.871980:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҲňΤºԏЇː~ȇȕìӧÈϦǞѬ\x89ʆŉƂřŨУrʻԌπÍЂѷ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            532897.7657273063,
                                                                            409997.9034864283,
                                                                            708261.4402486879,
                                                                            951329.3899816663,
                                                                            317308.0817866647,
                                                                            359122.9404731985,
                                                                            877755.6780616174,
                                                                            500781.4037598552,
                                                                            602956.4200320528,
                                                                            496846.930919079,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǜҞ¹ɅӶȗ˨¹ɃʲĨɓϞŷȺɹɏҥʐǪҗʣŠÃÛԨӋ-Ԥ5',
                    'message': 'ɜȡĝɤ˕ϰ˜6«Įг(qюɚϤĽɤԏȢҗɭňģФЕºԑŽɏ',
                    'arguments': [
                            {
                                        'name': 'Ёȸȼ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʩ˾˱ǘϿǩžm®ɯΰ˃ƾˍǼƉƇξșΩϷ@ϟсǼΘ<Á\x8dЏ',
                                                                            'ċΣѫéhΑԫΉǂм˷ǻǁŻ{ŷƏʢпЃ˹ҜҸĀΰҼÁʄǏҊ',
                                                                            '³ӇШͰɱǊԖҵŶђ}ҦDхːƷʆĈjѩңƑƤҊ΄ˑшg<μ',
                                                                            'Ś{ёɏǶԀɵǧǳӢ˵Ǔʠȼ\x86ƮȣƙЀέʻá¥ЌӒϘ˃ƪ˞г',
                                                                            'ФӕūΒĀѴ:ɈɎʔĭ\x96КɵӺæͱȁ˫ďͷàț¶ìИϻӋϔ&',
                                                                            'ʜϤԑƈѱȠ˺ЄĩЉɗƷЀҎˍРυВѬăUϖȰҰӦËʫ\u0381ԉ8',
                                                                            'ɊѧĞʋÓԬιɳ\x96ӹSʎҒԪNӏʓϰщϙΤХσǇƪΚĚĸĈ~',
                                                                            '˓wРŞƍš˪İƔɑѪġŻѻǬƯˎӅ\x9d(\x92ĩʬūҏЈϡнζh',
                                                                            'ĿƄϔϸȊɶԐýƉŭ\u0383ˤкÇҧJ˂ȎèƆ4ЖŦȚƕΒђɱԡ΄',
                                                                            'ńƋʯвоӥΏҬəŮԥʴɘƽϰГЃǥĆŨЉϨCΘ\x88XϞӌéɐ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȸſƩǿªøσǝ{ȶΩͰZѧΰӃ-ҏĳ˘\x89ǉʔ½˗Ӗh҉ĝĵ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ĩщ½ʴɲʑÏ\x93ƪЛĝϺu4˖˨ɣЉϪģî>4ưʓ˹ćȪԆ˜',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x97ɗŒ~ώɌΛӌEǤƕşʘѻ\u0382ʋ\x82˱ӧʐѺԐ\u038bЅȊҨĦϮâѤ',
                                                                            'ĸМɆΥΟöƀòҦƳг_tĮƸĄϸйǹˉ]Юį\x81Ь:ŷŦЙO',
                                                                            "ơИͿuİ<ԏ¤ǠϢƹʿ'=ʫΫвϖéȦȠ\x8e@ӰͰ¿ƃƗkÙ",
                                                                            'ǳʹƭԄʭÎф$оΩНЎЌԌǦӞʆʭϮӼŧ»Ýɪӄ^҉ʮξЧ',
                                                                            'ÈϴѼ;˓\x93ѸʣѭnƸӹȄ$ƇƫϚŲŸĎʏ³tςʄűв\x8cǳс',
                                                                            'ʮIΆǜχAŔΩщϘȘϡɴӘϨѢΪЋһϼȕüғЗҧҎͲʮʟ\x85',
                                                                            'ʍӍͳȆʺΉɡ]Ьľo\u0380Ǥ\x99äКŨ˟ʣ¥Čӯ\x7fȳƺƘЦк[Ъ',
                                                                            'ЩΪӞи8GɎƍ\\ӽɈǰԃĹҸʖřæϋƨȸͽʨ»ŜɆ˶Ȼʕà',
                                                                            'ĂҴɛӉΡŎͰԚɥıɐˮҔάƐșǐAUʚāΨϬȎԘʲų\x8dÁӺ',
                                                                            'ԙƖŮÃȃ¤ӒȠǯʲőРԍђ\x9dɑüӞϛфʹʌǾ²ǔԬΖȊԥŸ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΙҚˏQϗʾř=ˡΖʦαӆϪ^șĲВ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 710920.6536215857,
                                                    },
                                    },
                            {
                                        'name': 'αΒʩːęŤԚƂŭ"ӶŞθ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ЙțǈϹяҶĘѫԊɆҳͶˑϿȫĝÆː\x88ѲӰӴƔȚ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
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
                                        'name': 'ƠÌΟ£Ç',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ǜ˵ɘʏěʉӘéΎCЊǿŜĚɝҚԛ˫ҸŷʲBŅ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ţМÂԌϮ\u0378ɹȷȆƔfƀӅԆƑȢʌΡӛÔθѴЉШғФ\x85γʺÑ',
                                                                            'ԈƬԭо©˃Ȫӟ\x9e}ƂȔĽԒƳƀʜΡǀΞҎƃӮʟҚĐӳßźϟ',
                                                                            'ЀƨŇͼ8Ѕ9ГҋƯӺҬ©єɲũӁԙ˘3ӦɴˤŧϴԘуĭюћ',
                                                                            'ƏӂƶƤɋΊЕĒҘѨĥ͵ҙĘҁʈ˥[ͷѡÐҧƭŅΓʠϥìȕư',
                                                                            '®ԕεϊ\u038dʔȘƬ7ɎӠ˯ӏμϠʭӬĻˤǵΣҮ˜ȯçǖ҇ϺѮʕ',
                                                                            'ĢӿԥєȧΫʅK/¨¦ҰÞҦñСγŲӾÝǷ҃ºˋįƴłѲү1',
                                                                            "ΡˣΜƥСӞǬƖȓģѕӡϷϽȻёԨzΙżҎȴǣȀ'ϻȆϼԎӳ",
                                                                            '6Φ\xadǧѸƿȀǵ"É\'ϛҖҲʙL˂®ƶŜǸΩGԙϩɂѽӳӯŶ',
                                                                            'ϽӇPĢϩӢŮȷϥʚƫŵӬюȾɬъ~˾ʱԫȠðȾіӕěÍϤT',
                                                                            'ĖԔȭýӹóșΫғɎ»ӵţʍў\x8fТԠƓıƜў\x9aƕӊƥєӛSӆ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƊĥʺΟԜlҺ\x97Ԅ\x93қ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'м"ű\x80ӯ#wȡɖ³ʹäҁħҊƪ\x88³',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            95917.03428448882,
                                                                            629993.9943961418,
                                                                            193037.17203218682,
                                                                            856233.98055268,
                                                                            631209.5057632128,
                                                                            795219.3069731167,
                                                                            24122.41202415002,
                                                                            301925.90436192515,
                                                                            54920.787757101934,
                                                                            256073.33691524097,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɏâЂԍӸКΡ\u03a2ʊƁѐ÷ʢ¶\x9fԠϨȘĪǨԐĸĖf͵ɝʵефЪ',
                    'message': 'ʌӒρ£ĭҚǩӡʎJ¾ɺѴњ\x94qԬЙȼѵȠνΞԀĂSҫɒŋE',
                    'arguments': [
                            {
                                        'name': 'ȕŢʧǢíӨfӲҝȨşģԦӫΩϦƄҞƯͰɒԛҸԟĸʝѭόҥҐ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            631250.5430731818,
                                                                            752324.3830848857,
                                                                            160278.44173292723,
                                                                            723420.6441581304,
                                                                            321232.11952433415,
                                                                            217445.1428971066,
                                                                            -12489.603876176581,
                                                                            880501.0607713959,
                                                                            452122.2822026224,
                                                                            118918.4317866477,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ţҫǌΘɞǠϤχϬɤϞɘЙȾҚƿaώԒȺӣѥɕϭȼŷ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2942639824829959319,
                                                    },
                                    },
                            {
                                        'name': 'Ǟϳʼ\u038bʲǏȘBκ˞Ԩ\x87%9ϑj©ĮjπϐʫЧǑιҵŷςrȐ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˢϊϚЗİǌċÒŬ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4699487992239151621,
                                                                            -8335891997833127006,
                                                                            2807294247065601796,
                                                                            6010773138905001902,
                                                                            -2175479577823353681,
                                                                            3014270091424426227,
                                                                            2981814819011489633,
                                                                            -3633380595081720230,
                                                                            5959877495000248892,
                                                                            1144366023967269148,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˚ǎhŚх\x93нƞĎŊʮŀәĝ˥ӓȡʢĬϬЄĐɗĦȗӗgʝÊӵ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -95899.6677870519,
                                                                            -66180.77960043935,
                                                                            773839.8865768003,
                                                                            233487.94915218407,
                                                                            787076.3254080247,
                                                                            684301.3934433511,
                                                                            -50829.00631830177,
                                                                            230462.1004487797,
                                                                            -55070.31717481971,
                                                                            911610.1863463155,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƆȬѕƋìɶʦʨΦΫʸʇɆϰʏӵϼˎ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024621.876909:+0000',
                                                                            '20210228:024621.876925:+0000',
                                                                            '20210228:024621.876933:+0000',
                                                                            '20210228:024621.876940:+0000',
                                                                            '20210228:024621.876946:+0000',
                                                                            '20210228:024621.876951:+0000',
                                                                            '20210228:024621.876957:+0000',
                                                                            '20210228:024621.876963:+0000',
                                                                            '20210228:024621.876969:+0000',
                                                                            '20210228:024621.876974:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʸʑ\x93Ŵ˞\x9eƖΨǡ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Å&ϗѱѽŝϯťϘѥ˴ϼ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            521603.1222300398,
                                                                            600848.5318454223,
                                                                            73144.43586485251,
                                                                            148022.59581836525,
                                                                            192504.9895408986,
                                                                            16533.894225384356,
                                                                            980904.215864476,
                                                                            457170.83974397136,
                                                                            912265.4780134006,
                                                                            513486.4819212684,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '2тȣ҆ӆҬ¨ĳӓҙſЗτ°˙<ӫэºȨǜBȦƂʅąŨȠ@Ŗ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024621.877566:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӊċɿʞтɔp˵˨˜ɯÕɆŚԟϿȄƝʞҫȾƆ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1978460497277572351,
                                                                            -1548549643858516376,
                                                                            9111816200570690252,
                                                                            4484538929172953587,
                                                                            4199623233393727461,
                                                                            8616105551219527543,
                                                                            -8144491651390583539,
                                                                            4664456416355199238,
                                                                            2203921493936780682,
                                                                            -7004919604285820107,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ԗę˕ŏĨԐǨӉʵђКϢĨïҦµûǐϘƼÝқƂȞˆ˥Ƴωºϔ',
                    'message': 'Į\x9bӬDлԝ¿ʸæϨеΑʶͰèʙťÆ\x7fѲҾƕϺqïϤƏƿƷʶ',
                    'arguments': [
                            {
                                        'name': 'ԨπǛƫ¢:ԍĬѹƪɖԇĥ΄ɪӪӗ³ȶџh',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            138613.07842105953,
                                                                            430679.7599123487,
                                                                            970739.5520575617,
                                                                            608317.9602370329,
                                                                            226504.00413321517,
                                                                            901696.9943902158,
                                                                            413170.8618865896,
                                                                            917831.3113672949,
                                                                            -20888.04344337262,
                                                                            461657.3446249025,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'XӾƗ˾ȵȓàǢſҧɸϠαñˍ˳ҿǈȼúӭҶɂÂēƅįѣǎɥ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024621.878518:+0000',
                                                                            '20210228:024621.878531:+0000',
                                                                            '20210228:024621.878539:+0000',
                                                                            '20210228:024621.878545:+0000',
                                                                            '20210228:024621.878551:+0000',
                                                                            '20210228:024621.878557:+0000',
                                                                            '20210228:024621.878563:+0000',
                                                                            '20210228:024621.878569:+0000',
                                                                            '20210228:024621.878575:+0000',
                                                                            '20210228:024621.878581:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ºӝ*ӳŏӀ*uѷʜ҄ɃӓɁ%Ƣƌȇ¸ˡиѽјǫbèĩȁԆϒ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 802869.2615925703,
                                                    },
                                    },
                            {
                                        'name': 'ĥƩʁXŶүƑӨΆчӼɽǣ˛ŃʝĤĂўƲäɊûėϕҸ˂_ϜǞ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024621.878950:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ͷȷИƴгяmЧĦåҤơʚΨʩϬ`ąЇНǥЊт\x8cϐԏЎ\x9dŃ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -76736.78203833982,
                                                                            381418.669823404,
                                                                            894402.699489605,
                                                                            397244.769482939,
                                                                            64661.45172126149,
                                                                            872116.3390531136,
                                                                            808464.3643959897,
                                                                            660039.5228108034,
                                                                            20499.608562091904,
                                                                            694418.9079089358,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϥƼÐʬäȫʤȹƋǘ!ʻϝjÓįʓӸǝěҧǦӦʢρνȁӋʚƇ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˮ¾ýѻjĉŊΝђˋxҢǜϢȱҘf\x7fӝԩЇ˱ɎʜɷҖõýĞƇ',
                                                                            "ɴɯэuϽáüąǄëӪȗǱ'Ӟ¿ўɯ;қEѓѢϰǺǴÙЭʹΚ",
                                                                            'ҞйʆΖ\x8b˒ªʍψ˦ʯѯˇŸƗѻ\x9fə«ǶŉϨßˤĂι\x99ΪĊϿ',
                                                                            'ɇȮΟӀәńļ÷ĔêȀЃƘ˦ȸđ\x94Ъǫ>ǛŨÚǨƮǵӠͱĽ˱',
                                                                            'ЕҼƃ"ӏ\x95ϜҘɚZǇαÿȞ3ɳКȭϾ|ʣжИϋϗǺĽЉĶϕ',
                                                                            'Ĵѻ˄ѓԃʫϽCԞ÷ІɲТӝʹИ҆êǧȭԇļȅ΄ʪƘԙӳʹҊ',
                                                                            'yЫԇƻqҍƍϮρƦǺŰКǓԅɶĕұƾ\x84ǍлΎÞĸɅˋĚː҇',
                                                                            '¡Z´ƨѣɫμϰʐψİǃǡҝ²ʟϠzǜƙǠŢAѤ\x99ƤЙ×ə-',
                                                                            '˹ѴϩΦчѮĿӣƴ҉υϫŒЎЀԘ˘ʻĚƦэǣсџ¼˴û\x92ʮӠ',
                                                                            '˘ćλũŃƺӁӃʎ˜±ϐƫң˪ʍΨ\xadѸѹˢ˙Ƽɷȉ\u0383Ҁɠ\u0382ɖ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˾ʓ',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȃʇǬͼ%',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ФʺԐԮʴŷ²ˢǶҽҲэόʊɛÎƗ\\Ҵ¹Џ\x8eҐԡӀρ*ǰɰƎ',
                                                    },
                                    },
                            {
                                        'name': 'ȷԜǃ\x81NȋƟƔĜňЌѦ|ъʒԥƸӚԃZ϶΅Ėԓ˩Щǽђ3Ų',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ъ(Çņ҈ЭΙЯ)Ǧғǹҽ˝DȶȱɐҁȘӾӯSƱϞƹǹȄɑЁ',
                                                    },
                                    },
                            {
                                        'name': 'ŌӺԑε\\ɳɅОĠǿѼŌ×ɌФϠ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                        ],
                },
                {
                    'catalog': 'ӐҽŒìΰԬѬɥү\x82˅ӭλłɀ}Š҅ǋʉȾԊυѡ3TÐЙǗѹ',
                    'message': 'ŜͳɲƵˮϝĳоǥСÜɷq¾ΌäŬʍҥ©ѽҔЀЂɣɂƧҷəԛ',
                    'arguments': [
                            {
                                        'name': '\x95Ѷҥʶ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ǌŉǁÔ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            675058.7713536703,
                                                                            230876.99822511803,
                                                                            428255.16147247225,
                                                                            771778.3803250111,
                                                                            -52944.15174461491,
                                                                            553481.5484104499,
                                                                            -29217.941184895186,
                                                                            614232.4817891355,
                                                                            761519.8994852289,
                                                                            -77177.7110816614,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Cǯ\u0383ɽÞΉζŉ·Ӝқ\x90',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6908857179019934036,
                                                    },
                                    },
                            {
                                        'name': 'ǺŃϋϏȧÂş~ɣʽãÕɄҞЌҒςҏĲʹ҆ˆЁ´',
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
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԄƣāӅӍԁçĪ\x8bƩψ\x92Ǜ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            267661.87217399845,
                                                                            122215.45524393063,
                                                                            932738.0682962394,
                                                                            626910.108059599,
                                                                            739003.8037291487,
                                                                            513452.9285917457,
                                                                            773828.130343271,
                                                                            56802.820174165216,
                                                                            807774.0289999258,
                                                                            672284.7814650718,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x94ѽȹҡ´ǳ˒-Ï˂˒EΒ>)дЗR\x94ҳԥԒĞʤˢ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -7026.712037412202,
                                                    },
                                    },
                            {
                                        'name': 'ӂ¥Þӝž΄ϒ%ν,ԐũӣϹѰёʣĸӭԎєÒʓĈWMȽӰɡĺ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ê˃ŮǲѕӤϓØί\x84ѽӤǯˎKŇŬȁǜΆяˠǁʁ\u0382ԈƌÔũȿ',
                                                    },
                                    },
                            {
                                        'name': 'ͼƜѤWƇӹjҰJδԅʻӕβοşˏʹũҝΧUGĻɿ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7077692112550734214,
                                                    },
                                    },
                            {
                                        'name': 'ɋ Ү]ϩӗ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 468927.32461536233,
                                                    },
                                    },
                            {
                                        'name': '˚ƭƕʨ\xa0њ\x98Љϯƺԇþɲи',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024621.883620:+0000',
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

            'identifier': '\x7fҰΥҠʬ',

            'categories': [
                'file',
            ],

            'messages': [
                {
                    'catalog': 'ǌɶ',
                    'message': '\xa0',
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
                'identifier': 'ӝĐÜӞď˘ĽġЭͳĞĒГĐ!@ǢҵҜΛsě¼Pˊјΐǚɂŷ',
                'categories': [
                    'file',
                    'network',
                    'os',
                    'file',
                    'invalid-user-action',
                    'file',
                    'file',
                    'network',
                    'network',
                    'file',
                ],
                'source': 'ʻӦʺÖбϼǉȈѺЍÖȭ҃LǡяԂ&ӈɱ±Ӡ÷йҰFҵɽ²Ǚ',
                'messages': [
                    {
                            'catalog': 'ф˟ΖHʳüҩӤʢƲԡï\x87ȢѶʈŷGáĈ˜íˇāҡλĀǃɭĢ',
                            'message': 'ʤξЃɮɢ¨ʶӱ˯ҹȧҡҲƭçėǉЯϳѤMʯʺʃ\x8aɈӊ\x9bʲȚ',
                            'arguments': [
                                        {
                                                        'name': 'ӭÂôΙɜƭɥ˄μ҇ӱŝƥѪųөɋȔҼ\x97ҋ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ō|ͻ˥ȼŔшǒŬԝËęŹƽүѲǮεԗΘɕӡȃƧȿз\x94',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x93ϗ\x93е\x8cÝʎĘҌԢOǒХΌǆ¾ӚŲδ\u03a2їÏɣɕ1ȂƳcʅŚ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѧ\xa0Ϛƶ˯',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -71409.3333505488,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÔĐġСüȘµȧ˶҃ԛ\x9fӦºɐÚȳӮϤ°ȴqŁěĺԗηсӤϕ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ' Μ{ŏӃʰõˣґƯϷѭǇ϶ǡӹʌōѢԜìˇΕɨðϺƪǢ\x94²',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĘΕӽϳͲѾӴBѕԨΜɋǐZ1ɤ;\u038bĄʶҔũӫ˔£ʹ϶ǥƏ\x84',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɁʬκЗ˼Ĺ˩ϊʰҎǹͷȕӯ˅ŰɊċŧ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʂȳƯʚƁӡԗ˼8ҵûɗ\x8bʋϡŞы\u0380ɪºɥōϒӄΖѮӜŞԬÎ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'čάĶ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 799225.0935979113,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ЏѯźȣnĜϒɫӦ˃йƛRǒƀΝěρ ɯÙώøѾɸӓǆ\x85ҳ˨',
                            'message': 'ąʾΈčԣʌƺЄϊy¼ԬΐɧȴˈŸҵśʢԣȱƯEҾԘґŲɣǔ',
                            'arguments': [
                                        {
                                                        'name': 'åɝȍȹĩùѐŗɏ\x8aѥ\u038bȂɕċ+Ƌr',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 541276.4018792765,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѲϪŖӹɷдӿɊƔϒʀΪʙ\x8aȯȑǃ˥ƟĶɥ\x80ȻɓßǻȪԩĈŬ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ôŧ˓Ͼȁ¹ҙȾβ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'КĖ\xadӥÂ.ĎХхȻєŎɍ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƁрɍƅĂҍЮЯõȇĠҞСýȾŁ·ԁ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŻƾȕΥ\u0381ҮѮȏϒÐǖĈˤϨ\x86οŝҴƪӒ©ʖтϑñΰАӮLȸ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɀßκҺ7fªϦЭfåҮǵĶҖȀ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Қԛȯ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŒЄҲӆǐɸȂȟƘӖʮĺγĎǖǒ;гϹɻӗʤɌǉʡȳνʽлͺ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǏΉʎʶÝѸlҾ˕ʢ§ǐǨӰΒʀ4fКʵͲ6кΤЛˇɯǓʌσ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǳ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ͿϳŉĹϴ˥Șіä¿ȗ¦ɝƋʉČϑ¸˺ɤƸλŗîӋ%ËҾʘȩ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҍ˒Áԕҧӄ\u03782εͼ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 105147.98443037894,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˘ñɂŚϯһçϬƜƔɞÛϐþƽϗřÊěÀӭкӎdȺ\x89лϒļä',
                            'message': 'ǁοєĄɱȢ£˼˵ГǥѺӑǿQωҎûԍ\x8a\x9dǿǃҽǰĻΘȷӫԩ',
                            'arguments': [
                                        {
                                                        'name': 'Ƒϸǁ\x92Ŷ,ȕɣƅǏÝȇɺҐѼǼғųϞǛЖś\x83иΐĽȌӹɮͰ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'βį',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɣ\u0378ӱ3˫јÿġϓƾχϢ-ɌǣΚѵéү\x8b˶Ǡ¸ģɔԅ\x88ӪǉѾ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024621.841179:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȪԚʰȕǒƍǅ(ϷɭõӽΒχФϲ8Ȱ:ɧǹΡѶľǃҙƕʈƙÊ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7877753477724478302,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʞ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΰӓȂÑВ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȫ˄МӜ˅Ί}ưFϨ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ќˠ˻Ҁжїȕő\x8fϑЏϥˉ\x99ιԜXŏˋѨƤİ;ѱϱ˽ƟЌϮǬ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024621.842442:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѻˆ˙Ȑ§2ҁǪΩѻлˎ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'аʿӨҴˬϰȜс*ŘӲҗ¤ƫŖˇĥ5ӴŉѕӖĭNԚǉΖ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ľăұȹʤș˷Ǳӭʖ@ª˴Ŷɗȓʔ˗ĉâѕѢūфēǴÿЏ|τ',
                            'message': 'ϢˎЃҲϭғȌ³dÊЦѸдΜɜͺvzӀƐӀԦÔЯΜϢƧɬлŅ',
                            'arguments': [
                                        {
                                                        'name': 'ƞ¡ƱĴƬҀѦ˅šƱ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'уư$\x86»ϊ$"Ųǎȋʵ.ΰϿԣʉгſŇÞċϼƐ½ͽr',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -30929.065550666273,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǽ[½ǪǫŴЎϺҴƔІǕˌŚ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԊӡҠŠΓÝØʴѯȔɣʠӠúʏͻǋϊ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӆȿ§ͻąńɼʩθȔ"¨ʖΜŮRԩʇѾÐAґԍ1ҎƪȊŗɩ˯',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 621192.8297573322,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȍѹ\x87}ƍQдƗȞϨщέŖ<Ъ«ʜҽq\x84˾ÑǂΜѬӛ6ΓҖG',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʹͱØ˱ΟǓǄǯŲƘŉʅ0ԨЌЃȻsA˺ȠƑНθɦõLƂӍэ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 247952.80293837457,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǘӰö"Åњ¶ғlӄĔŏԦҰ¥·ǎЖˋΤìǛө"Ʈ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŷӡӭʲÄǒĘБυǚĭóŇӁīƄҶԏћĲǏϷƜԧБÜ$ȎǗȄ',
                                                                        },
                                                    },
                                        {
                                                        'name': '¹ʦXѪӱʗ˭˞ÚɞǞǓϚЩϩҗΡό˳πԍƻƹȊºЃӸêԃŅ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɿЍġ?ϰΏѲμȑɲʹǤƀѩɽʏzϭǚԨ\x8e',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'дҬ\x92ө©ʳĘWӴпȪɍȑϴǎ҆ʹĊĲϪƎǊÎˠwȚӬСϐɿ',
                            'message': 'іɯŸӻ¹yпηAѨНǢĥҿΎÙǘǉ˷ɢЭϹ\xadʹѦĭżӺ˴ȫ',
                            'arguments': [
                                        {
                                                        'name': 'ˑˑӶˣӀҵƄʔйīϛ˽ϻƆϸIԈȪeɻƠ˵҇ˉǛφӎĊëб',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1892949086030378621,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѥǹϏƸĘ˝í\u038dzŵŢΠØɗ҉ȫîԉ˚Čΐ9ȆiϏŗʹЗÿЀ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ńҿǉƲʘҦ\x8fѨ)TǔǝHȪұŨ+сπˎˣ¦˚ӴÂ\x91Үrɤ«',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΫȍýeʧυÈʯŽɶԇήҨɳԃδƣӂĚ;ӑòνӈʐëǤǟȒЇ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƭĦƆюǿѭԜ\x82ǅĉÍ˝θů˓KǈƐ˜IǫЌſɠűԍϲVԖ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 735913.7811040361,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƚ÷ƱʥŵԃэƈЇЋ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӬƧ:ўӃӋǐ°ӭʬȋ»ΪƮΉĕªҡ÷˖ΏȤϭ$ɾǉŜÉΰҲ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÁòɟĢĔТ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '.ӛԋ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5460596449822123974,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԃÏÀ¢Ћƴʏbű',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 15361.74132446952,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ўɫЉӁmԚԃʎӏė҇ԥҡШÿґ\x8dȓǻΐϰʒӺɺĒĘӆüÈу',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ˑџƠ`ΧӛAһåĲ˝ϩŢƲӥÆƨĎΫӬăÕ%œʑψƻ;ӳȶ',
                            'message': '˗ĳӜÏϼöԟЇʜ\xa0ť×ȲКƭщś{ƪƯƖҫ§ӱ\u0378҃ż˴ƴӶ',
                            'arguments': [
                                        {
                                                        'name': 'őВ¯ȣʯ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҘӂɅơÏҟСƃɤΔªƱÑю˔ΧВ\u0380˫ĶԧÉα\x87iÝ¥ӛ\u0380ɫ',
                            'message': '.ȺʦҎɩȄҶɔ@ƸƎӁμϊ\x86ҷWˁѴǻȩŮΦŢϿåkӀ/\x8b',
                            'arguments': [
                                        {
                                                        'name': 'ŏǿɧŒѾ ĲƞliƇ\x91ђʳ\x99ʿėҠƭĽǉġXҲɨÞЅƛƭǎ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӊҳ÷ÚϏĔ³ǎå˻ыҌșϥҷϰ˦',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЂďӋΝԗƙĥыɍ˽êōƘˈȩʆъӚѓǍΕ˭ɾҶÂ\x80ѵȳȱÛ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¾',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϳыӸьЀǕӪƽͱȊϐʃΨɡ҇Ӥ\x8bșҫʀÖÿїњѽƆȤŖʺҋ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024621.848304:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǿȏǾΜȍ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԎmӋŝӷМϤÿ[DǎŸĬт˳ϺeŠɚ\x8fОЎȬǽǇǤÄǺɷ˹',
                                                                        },
                                                    },
                                        {
                                                        'name': '˫ȉ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʟЀÿӵͽθŒĎɖʚƋϯȻĺŭX·Ęӑԗèʠқ¤Ҽ=ŵûǒД',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϚɭȡƮϰҦԂƉʈζåӞƎ˴ԇ@©ƙƫ]ϏîʾϺϣϲŘēвȰ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 796318.3898974345,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʟФĵЦÄʓĞĉЏЍѦĲРSɲŐˁĩ˼ӘɶɁ@Яʤ^ϐӽǫ˺',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϐКͻ˻7ԀƆĕ\x92ӹϨ\u0380ԇȓƊ϶ϧ˦βʊчǝRǂЈ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\'бĴɅǀd\\hɵĺΙ˔ыOҨХ˟ЩӔƔ¯Ъԥ"ɺˋ\u0378ҪǓǋ',
                            'message': 'ŞK\x88ҴŠΪ@ʕ˶ƏәΰԋŭˍƇѬǣĭëҝǏζѹΉλЉŬ"Ч',
                            'arguments': [
                                        {
                                                        'name': 'žɰ®ɤʠĘѕǡʽ\u0382ʆƾҋǨș\u0379GӎĦ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 647538.340137515,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǄŚʼƔǧΖĿӂˍԣҖ˕ƠċФ\x8cύϧ:Ƴñ˴иԉѺXʫϸÑҒ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˁɋԐζϪ\x92ĳΓʸǓϘȄдɦƌЕҳˇӻμЀѩИˌʏɶřҠāʖ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˽ӭūϊ¸г˧:ʶϓζZɕțǼŤɓϮuƣǃƝԒ˥ѯɑŒ«ѸӺ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǎц\x93ʎѯǨ˩ǏӫÞŨıҀѭ\x85ϾˀӯԉȇƼȑ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǘжġŪšMΡИ\x9cĨǀ,ПЎʮѫҚʜƸ~',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ώ&ЊѲɖ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϺɭƤғӏɄӎ!ȒӮЖсǤΛѓьʂƁÇԜɦɿɹӺcʆϷ˰ͳɻ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɘɅΑ˧ͿȟΆԊοŭƀсÉïΖ\x83ŷqϖ~\x98ƹъҪЕ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȢѶҼҋѢȁʨӌTȜɮɞƆʬŠ\x9eӗǫǪ3ǵg\x9dƦϾ¡§θϨϨ',
                                                                        },
                                                    },
                                        {
                                                        'name': '˼ώÃĿ҃ϾԤȘ΄ĩəÆ¹ЮĦӂƼȯÑϰ˾ΚГpǜÈþЈƼǻ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '2ԧ҈Ŝ?\x90ƀЩҌƀǺƇŎќɨʋŏȭ"ȨϑΥ\x82ҸƤɛҩӫÆ¤',
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

            'error': {
                'identifier': 'ҀΈʪҤȲ',
                'categories': [
                    'internal',
                ],
                'messages': [
                    {
                            'catalog': 'ϼʒ',
                            'message': 'Ψ',
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
                'identifier': 'ԝ®ÍϳϫʍʏǹʣŬЅЌϊɣӨԨȸϻ˳ȀɃÆнӚͼ¶ɺďǳρ',
                'categories': [
                    'os',
                    'network',
                    'file',
                    'internal',
                    'os',
                    'internal',
                    'access-restriction',
                    'invalid-user-action',
                    'network',
                    'file',
                ],
                'source': 'Ĝ˞ćзĵŕԢɱԐƻɰԂϓęʹÀƑҤȠŜ$ʑǷ\x8fѐӇЉϒӀӜ',
                'messages': [
                    {
                            'catalog': 'ԝȶóʅĂȺ\x9bѳӣԩȅОɐĨȄӂŝҫbӇ\x98ȚϢәЍϬӫâdѪ',
                            'message': 'Ó\x83űɘӓÊӃ\x9dȢςǩˀ\x85ÞȃŇќΰӫȇШȊӍͼĨ\u038b}¨ӄҌ',
                            'arguments': [
                                        {
                                                        'name': 'Ԛ\x86ÞԈԍήκϘ©ȑ¥ǹ/ª\u0378ǺГ˳ȾȸȨρЉ@ġKÒϹҷ˾',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƞɨûҙɷ,ɵGǆ4\u0378ˍʙÊ³ΣЗ¿вɿϓ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7552265340162280469,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ά6',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¯ƂȝȓņːǰΏdЌưS3ʫ\x99Υɿˆ¦ўԋȈɿѕͿѥǴԑ4Ѫ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8842455410516459671,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʲѯ$ ˊ£ԭǹ}ДÅŞЕSǱɵģϞȿӉǴʃʶДŷÜǄƭЏΆ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '<\x97ƞӫƢӌӸ˛ȨýӣȰȢ^',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ιкƜΡǒqԝûѢϠΤĶϮŇͿҀʮэKĨmʍƴȲĂřʯ7áÂ',
                                                                        },
                                                    },
                                        {
                                                        'name': '˳',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʁĜв«ԜΉӋɂĂϵҨ˘ϒўӀȯƏд,ԆŝўΜG˹ѴʍГjŠ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŮʦÓξϯ˔ʐҘѿ˝Ҫ®ӛӊѳéśΦĴǾɭǊ\x9cЭƯÀϿд˒',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Й³ĹР',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɒНŮą)ϹԊ ɫ\x8cϑçЮ˘¦ɟʢƩԁǍϫŅ¦ɟҁΙѡ<oԒ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŋҝ˼¾ӇԔȳěˁΥȥɘhˬҟgӔΙ\x9eȶťăϻƇǽÿKgҜύ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ư\x8bΩ¤ŗċɟЯӹĩιӊsʢɩʚǱ˥ƣơǮʯһ§¢е`"ǫҩ',
                            'message': 'Ȍvƿ\x94҉В\u0381ʃ)ʯЪɮӢƐӾŨŊѪϕԃǆĝŠˍѮȔǊ9ȉͼ',
                            'arguments': [
                                        {
                                                        'name': 'ѻЦʨϧæʐľϱˀ¦ѳ˖ŎÐ)Ӗ\x9eɅӏ<ɥѾԙÞΧǭĚғȓÒ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϋǥűӏɮʄΩȷşĈо˂ʉӂѲīƂӲAǸхɋԫȏвťȱĭǻ˜',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɸˌǺĿɝ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024621.888485:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŌʖpˏǌӓèӝʝˤĞәȰєҒªр',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Тиҿω%ԒșèǍĆʂƪԢËѢͽӫԝЕɕĢǕř\u0380àūŘʄʚҁ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 554499.644919584,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ГӵˀήфΙήю˅ҕbʌӾȲӬ}Ҙɺ¡эȸԍͰƊ\x9e¿ǁΌŰѸ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'җΦ˭Ϸŉ˥"ԋҙǰΔËĪƕč˩ʣNðʤΝ\x94\x8eĮɉӡФЌɜ©',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3385838955093476359,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǧÐȏų˶Ϻ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'řҐʧΓһƖ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΒȶƒƼϳ˶ȂӬāŦŌůԑ҃8ԊćεΘƢxǘҺ˘ğϢЕʃŷȗ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5926520447993407413,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȬȢìӳŌ¯҉ĿȱԨʮѳǷé-ˈËŋУʡ"ȦƚпzŮΕɇ(Ŝ',
                            'message': 'ҪͻƫĘóaϨɳ˲źĭѵϻĭƝʊøϦщĨɪWȠǛ«ѓʁuɖҵ',
                            'arguments': [
                                        {
                                                        'name': 'ģľWˋɶԣIҪřǈʹζHƅ˛ʷȹѫΨýѾҶȝ\x87ҕʦʜ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϳŖҲѭɛϹʗϑʢùʾƞÙҵƳċ\x87ɤV ǼΪƝΚЏ&ϛ˓Ϧм',
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0379YҖ˰ԙŚѱƐɨԙԚΉт¸ӽԞԦEѴ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȖőĠȶɨӡԉȚƨόƔőªŇʐġkΞ ţǩƴ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 444060.8581936362,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѽԏϣ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϐҬȸ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'DɷҙԌļȼǵ#ġ1s',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'џŴЪ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǒЮ˭ǒ\x91ǝʑ\x7f£ˋԊҥǋԉʥɉúӄдɫġ¤ȢƝȽɴÎԩήʵ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӊʻɂ¥ƁȭЖĬʉсƀņɫ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȱµ\x85рǅC˝·t˩бƧȍ¼',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԅҟɽωӌЋВѬ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2574237775734768685,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Щ˗ҏТҞȜQƣɸÎÚΟΝΗ\x91ȿǠʀԊþ6ͺ˂ϼϵđñϟ҈ˠ',
                            'message': 'ƿƄԪƧ=ıϘĊŜƞԬƞMήҞҰϟτ³ŀĵƮD˴Ӡͼӎɘżȇ',
                            'arguments': [
                                        {
                                                        'name': 'ȘňsƟ\x8a/čŦyЕҹԟKǺӡ¥ʶƦȼԟ˃Ƚ`ҖƬƙ2ԈŪԝ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĩŕѦŘ´ÀɺңŅϔɗѠϫҫȁâˏ¼ʭҋ|ŨĴőɦзРԆѽʆ',
                            'message': 'Ш=ɚԢɝìʲǼǣýҵʣǁϬĤRǮӻƒĜɊʄªЦŏЃ˺WʈĀ',
                            'arguments': [
                                        {
                                                        'name': '·ÔӇ#ȻҥĂͻ˃дǽнȧČӞ«ʈȽƣŬEȽ½ǵϒԈĪʣϡè',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024621.892988:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '΄ЉtĄ˳ӖȈǩҚБҨƞѽκ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ťκǟϏʣϾŷ;ЄʕŕԌϺ\x9c˚ӎ¸ˈy¥ǞνǋƛƕʔkýѲÀ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǆÿҟΊĝ\x83\u0380ƚȥ˹ĖǐϡǸȽѲʎʵɔŬkнÅ´ύ\x97ʱƕªѥ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ўжǝχ\x84JϗŝzŧǥˋŲԓϬѦȢƛӆԟҬǢӄǑѵЇˋsŝ˰',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˢԒ<ȁӮϩˇӴsҭZȋƷÙҷѮнѡдÏɿԘɤғ\x87ÚĭНʀɏ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8329078800944721259,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǟ\u03a2ǖӈsʅ҂>û»ÊҾэUŇƘEϛɵǿΛŘ\u0381ƖЭǦӡĠưҋ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĳĉІђ¯Êл¡Ǒ_ǲûȏ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѳÃѶԟk\x9aǔ@ȩϒ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ' ԔҖɓЭţΕíϑι\x9fĠǩÅɔKΡ˴ӞΊѭӱԋȰЊșï\u0380δӰ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˽șųΌѱɇӋ5ƂԘȨʐ8\x9eά˞óŵдѝÞrԎӾӇƒȭҪWϝ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˲£Ƃ¹єΕáύӆϻϭαĺƿӶǣʨϫЧ˰˽Ȱ%ΡŁǄƆԝ˅ƅ',
                            'message': 'ĴɊʉɱвϞЃʠĆɠɮǢфȆѢҤ\x84дǳϩ¾жы}ȀШˏУȵΕ',
                            'arguments': [
                                        {
                                                        'name': 'ŬʓʿϘ»ʹjʹŰńĆͱǷęŇӍͺϏҥѷӴ\x96ƀ\x91¬ӶҋħȊ9',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ēάʴǩѼŔǈ-ÏҚԡϠɐ\x92ɽʘϥȸΫԎҤÕΉǁʹψȰʇѱƚ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ìԑǅɖɓì',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϐ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѸĴˁƇϪӲӢ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԕģϊŞǵƴŕ˗ɥ΅ӃĴҏǆơȺΝ҇Ħ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 62739712716305698,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƅ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024621.896280:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϩ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 177219.4620514486,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҢĜӧԜӥРɶӉêѩнʓÇyƷҙÓƇ´ǟ$Ȼ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŵơ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024621.896752:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': "ӏɭoƎȱ˟ěЯ'Ûʲңν\x80҃Łϡ˖TʹԞҗʓϝɘӏӜňɘƫ",
                            'message': 'οȚºυoʝ˸˥ǸªÌҹ6ұΏĴĉҍãŧϺƕǸȕ¦Ȩк˫ʋ·',
                            'arguments': [
                                        {
                                                        'name': 'Ϗ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 144322.46613276532,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԤϾΣħƃ҃\x89ѢЅ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϸΠ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 125502.58833860114,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӘЕʦΨҁѢž˧ϾƟ\x9cЩɌ\u0383:Ƭ\x99ΗϴʹӼǘӮӑτ{ԟĂɗ©',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŦèҾԙʩñ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "Ǵň҄ţȝȊǬsȺƩӀйӦb'ɷðљHÉРҟƬƲʾϻǢ",
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˼Ћńôӱ\x94¦Ȣɋʪ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'KſǜвɊȄ˙Ĺ˧ΈʻʔV·\x89ϏɴʶȡɳƯ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʢ2\x89ȜŪϿǜѰІǮ\x96ÃҊĨ\u038dпȭȴƴŲӾҾԁϊή¬˟ѱÝȼ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'οȊƦƙ\x8c҃э҆өДųǬ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɉ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҍԈƊҀƍ\x9eӛɲҿԫ\x9aӧɜџÚ\x93ӨˈѽɷˡɿΙ҃ņǫΠʼ',
                            'message': 'ÃƂӘˀŸїӔȂǾȦҕȁϰıǯҦ(\x98ԟȎѯВŨҜғǯȬӡȇы',
                            'arguments': [
                                        {
                                                        'name': 'ŶŦ˨ǄПȻчŬ\x88Ȧйɛфˆǈъʲҧɴˏ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6945595138736343146,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȎÁÜЦɝɒƱȞΡgăɄʊhѻĬ;αʍvƃӳǸȯO¹=˳\x9aҀ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ι)¶?ϿҏƯęŀǙӾҜ\x8fΗ\xadοϘʱşҢӐϫͺЫɭѥϼѽaɯ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƹəʋŇӉ0ѹ!ɉ\x87ϏˊҐˤCưѬȍǧӤ¦:ԭˈƔрчůŰҥ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƏÐϓӄĦķɸТʆΕѨОЗʛȷӛΎŀȟðΌΤ\x92ϕԖNΏύšκ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024621.900077:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'јȭә5ǮĨѲƚǀ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѷӖòВ˃ά˩҆ʋʘϧБϬİɱ˱ǮƦǑãȸӫɪŦ\x82ȻϢ(Żƾ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɑѭСuӘøàϚѢѫăȯԮxƛԟϻˊʀȫŰԦcǀŎҦӣʱĬ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'LҌѵ˅AɫԦΒƄςʫҘѲͼˑЪǣ/МԚ҈ȷƦǬıљȌȹĠԗ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024621.901275:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԅƾ˦өΙѨţĊ\\ɞĥĩҾϢɌ˯ĽԦʛʴ£ǚcήƲѳʂԞ\x93!',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 157546.19989934206,
                                                                        },
                                                    },
                                        {
                                                        'name': 'пʍǤԎүΒɾΙђӠƜӆϷѫνʙȊȧʇϦΔȎǦ;δ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'yʽÆχtнȼǋ\u03a2϶ǁʾƽÖ\xa0Ě&ѵԗã',
                            'message': 'КϣСʌԙ\x98ɍǖк¦ɑǸӂҩǣΎԔӛ҉ˤȂʸ&ėӍҡҥ\x8f҉·',
                            'arguments': [
                                        {
                                                        'name': 'lԙģ˺ǏŃƏтiѫıΣŠ\u0378ŻˣƵӘǱǦІğҨҴĭCɺӟѥз',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ςΑ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024621.902415:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '҆Ԣ˛ψpAÑŀßҾɦοǲdȡœ˾ӕ\x91ɣФ³Ù˙ƭЈΉϕˑƃ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'šëÇΞʤſǚΙðƀÿʪƢȏǍ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ǣ˗ŗӼďϗĵ˜Νʂϋ½"n\x98ӆǫԖҎи\x94ːùĐVɇӣж+{',
                                                                        },
                                                    },
                                        {
                                                        'name': 'CĺѐćV˙ͳŅӾ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Қ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÅʉŹĞʷōЦҢɣїƨĖϩϒÒѡÎѻдȤťřǩРϔ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǋϡǦ}Ӥ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024621.903582:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѕ\x8aOȜ˞όɇ˒Ϭ«ӛЛϬȒîӍƛ\x81Ά\u0380øѧ҇ɊƧʌȩĿĹ¥',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '¢Wĸ˰ѻΪϿΎĳӽҝϢǶʆΠо˅ϚūƜҁˍ%ʽɩ~ӊˌӲď',
                                                                        },
                                                    },
                                        {
                                                        'name': '´ƅΉϴĠșʂʃ½čŦ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȱϖȊӊҩЏѥǔύʓΉÂάñĝаɄϯˁʒƈЁÓ˲ӦҸɘˆ˽Ƞ',
                            'message': 'ιɹĎ\x84ҸƎĒǷʸɞӈʂѱCѢͿɝĎƅŽӪ\x81Ɩ@φǗÑлɑԙ',
                            'arguments': [
                                        {
                                                        'name': 'χѭ²ɯɷьӃ˱ʴɨĶψɖáˑɈǒә҇ϩǰʰřρŭʲƍХǧќ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 733228.4087615369,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʤǱɿ\\ǘğΚiԓĦĞρˊçӔͻ8рЯ\u038bЦƄŗ1ԭр½ɐɕΥ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȄłĪŖʜԞхӾ\x91ϋӗĻ˃Ŕ҇ѻŝα',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϟ¼j[ϫў,\x96ʖƠʠ[ԑ\x8aŝʹ\xa0\u0380ωă]Ҹʯ\u0380ӧŴ1ŷȭÔ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'πԒ\x97ɹԀӰϿҘSǆĸʬÂħӌȫϪ˪Ȃ˃nϩʾԋΜɠƹҐӶG',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҳέþĶ\x9eÞȏƩΩЊˀԧʰ҈ȮӉżɧÏǢӸ¶ĝǤҙԝҼ?ҟѹ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ғ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȄԉҧˆˎìЯԜͿóüтǿӶӑʕɓӼӰѵH',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ùʲѸ˾ŞɢҨӴӲҙÐϵҦüӁˌ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ů!ĜθĤuюɵˬҥԥȢВƶ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Pʔβǡ˹ǐɾÙŦԇĕ}ƐƣƛƷƟƉ0ǿ_ʲĽϑ',
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
                'identifier': 'ˢÅőǼҬ',
                'categories': [
                    'access-restriction',
                ],
                'messages': [
                    {
                            'catalog': 'Ӱ\x80',
                            'message': 'Í',
                        },
                ],
            },

        },
    ),
]
