# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-06T22:09:32.748551

"""
Tests for the logging module.
Extension petronia.core.api.logging, Version 1.0.0
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
            '$': 'ΣːEѨ϶Ʋ˟ъϽ\x94ʝѭгљϿơЏЬǝ˅ϵɏ±˄σǾΝ˻˒±',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -7549381154380695477,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 822375.667103482,
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
            '$': '20210206:220932.681605:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'чџlѡԟȀр˞УȊˢҩŨ%ԛȽʌԐˇǯԪĚэɅҹīвϦżӤ',
                'ƭғʸȅϚŀɆԇɒӻhǲƞʳМÛ£Z\u0379β«ӱԉ\x9bǸΌʒ"ϗǓ',
                'ġҢEġΝGøԜɗ\x9fǙԭÝɗ\x90ћĪpƄǂĜʌƩхʾƒsŞȑή',
                'ϸϷӡǿƽҶǟɧґοΪϾԁ®ԗӲӺЂ\u0382Р×΄ƅӢɞ5ŌǒӾŧ',
                'ѡλʧśΫǸӁҶΫȵŜɀơÄéƀ8Б\\Ϫ®ѕѳҷʖĒԖȺ҉Ƹ',
                'ϰǀŎӿЇ©¢іŏłUȐԦʚğ\u0383\x98ƭѻƀhɍ8Ѭ\x9bĸʦȤюæ',
                'ԜǸΣӂÁȈŲ˕Â\x92\x85j\\ːΖrơǈƖȞÏϯҽϔΉЁПűæ˩',
                'яҁNƉʽȅ˶ϵԎƪ¢ŧdʸƀĦõÆșЎʙӤϚ¸H)ȋɪɺЗ',
                'zЗ§Їҿɸ÷ȋԒIƕԞŖӃԏϊſ*ӇɡӷϿҘбѐìVʢɊu',
                'ĨРӤx˅ΜĸԠƵǄ\x94λĿѾǹ\x8dĎɚǹԝҘŕԒɻǟfŐήơĺ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                1597004488019553249,
                2184446066094061414,
                -1764541711496566201,
                -3240533671691671038,
                6962979112092745049,
                2969270065326213254,
                2881038997133208598,
                -8324253583179064007,
                5073384772560147575,
                -1217242248290050247,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                962743.6712679907,
                -85232.66786092932,
                774189.8158328367,
                401017.08682854206,
                -9299.520549198583,
                365249.18439419597,
                941435.5184048917,
                632013.9880647665,
                438144.7222540872,
                432319.78948308085,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                False,
                True,
                False,
                True,
                True,
                True,
                True,
                False,
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
                '20210206:220932.682503:+0000',
                '20210206:220932.682513:+0000',
                '20210206:220932.682520:+0000',
                '20210206:220932.682525:+0000',
                '20210206:220932.682530:+0000',
                '20210206:220932.682535:+0000',
                '20210206:220932.682540:+0000',
                '20210206:220932.682544:+0000',
                '20210206:220932.682549:+0000',
                '20210206:220932.682554:+0000',
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
            'name': ' ɬAɽ1ŏ\x95bJǵȜmϥĦŲŴƻ\u038bĒ',
            'value': {
                '^': 'float_list',
                '$': [
                    571320.9722155055,
                    666237.1730135643,
                    330876.63697006676,
                    118483.87856275038,
                    97564.92595339197,
                    870540.4958072936,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '˪',

            'value': {
                '^': 'float',
                '$': 893650.8792148249,
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
            'catalog': 'ȿЍɩ_ƁԔϔѐΎƴŕ÷тȉʡs\x98ԏγϼ˙ȎǨʣʓǤʉĸɛƥ',
            'message': 'ҞÙˎÇÈ\xa0Q]ǯΛFρʂpʦɮƞζ°ŵēЯʩ\x9bȇČ\x8f|Äã',
            'arguments': [
                {
                    'name': 'ɗЀ%È҈i³Â.áǷ«',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        316832.04478740797,
                                        730243.454440577,
                                        921806.036978214,
                                        903532.6894763435,
                                        394283.4384499866,
                                        638401.6162942727,
                                        67183.90734710224,
                                        410512.9740556286,
                                    ],
                        },
                },
                {
                    'name': '0ϚҜ˄s²,êӻϮÃ',
                    'value': {
                            '^': 'float',
                            '$': 904441.896710643,
                        },
                },
                {
                    'name': 'κϣ\x9fȥΈЋĈáʿΕЋƶĕӱδƒȉĽM¾ϧƭæатɎεϕCƼ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210206:220932.679324:+0000',
                                        '20210206:220932.679342:+0000',
                                        '20210206:220932.679350:+0000',
                                        '20210206:220932.679355:+0000',
                                        '20210206:220932.679360:+0000',
                                        '20210206:220932.679366:+0000',
                                        '20210206:220932.679371:+0000',
                                        '20210206:220932.679376:+0000',
                                        '20210206:220932.679381:+0000',
                                        '20210206:220932.679386:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ʍӜjĝȄİЀąŭ҂ɵÂϱǕ\x9e҇7§Α',
                    'value': {
                            '^': 'string',
                            '$': 'ðӇœȨĎԏρи\u0378Éѡȃ˟ѦʌɘӣȚ@ÂʧѿϘĭ˵ŽŝŕΚˤ',
                        },
                },
                {
                    'name': '8¥ΣԎɋ\x91ˠʦ',
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
                                        True,
                                        False,
                                        True,
                                    ],
                        },
                },
                {
                    'name': '½ЂıÂȕҊǾǐҍҙёΣ¥Ģ˷҄Č',
                    'value': {
                            '^': 'float',
                            '$': 224107.5865310806,
                        },
                },
                {
                    'name': 'ιˠʏҶџ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ɈʾV\x96ĉĀωȥɯχȑϗŭɭ\u0380\x9fю@ πәƒ\x83AхɀzӀӯ_',
                                    ],
                        },
                },
                {
                    'name': 'ʰџ\u0380ˆнʡƗҜҀϹΊɮӞ˝Γ\u0380Øǅ>дΞȆͱ\x92Ŕ\x8dƣȪɏп',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        7935998655744386053,
                                        4054493714207584848,
                                        -3045500642813157634,
                                        3423859800291939696,
                                        -8652932267190249836,
                                        5689367089722553074,
                                        5820033368648882321,
                                        -3463375518459339902,
                                        5005527452986685691,
                                        205770318804267083,
                                    ],
                        },
                },
                {
                    'name': 'ʥő¿ғнҪʳӺΔӇϼɹ˰ҦЭŁѶǸϚ¯зǉč',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210206:220932.680658:+0000',
                                        '20210206:220932.680670:+0000',
                                        '20210206:220932.680677:+0000',
                                    ],
                        },
                },
                {
                    'name': 'Ə҈Ѩ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        True,
                                        True,
                                        False,
                                        True,
                                        False,
                                        True,
                                        False,
                                        True,
                                        True,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ǐɆ',

            'message': 'Ā',

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
                    'catalog': 'ƔȆбŇƫ\u0378ԃШć\u03786ĘȄҎňѤeǎoώ]ϳȭƅԤӊɚΉрͽ',
                    'message': 'ԄɁφϑЉH<ԮϘҳi\u0382ψщkϪáДäŞƹHȾĭǇ϶ɐÙƲǍ',
                    'arguments': [
                            {
                                        'name': 'ЦɵɄԀΑӓƮӘ®ĒТĉǏRЫǬο΅NӊɠŧγƓ˗ȈǇϧʁ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǙrұĳTҪїǁсӈ\x99Ƴҿ\x95ZȠŸ\xa0CҋԠʃʥʈ¼ҎʃƯѱ«',
                                                                            'ĚkϙҒӺ8ÔϨυȎJœйӹеęӂ͵ŝaÖƵϴ¥ВʵŌΖƧɉ',
                                                                            'ţ\u0379ŢΫȌјҷƳ\xa0Ǯ\x89ǬżԥˌʴΓ˞¶ńŲnªӭͻ\x85ʀl\x88Ȏ',
                                                                            'ѫςҴȀǞЖϠӪųӢѾđЍӟƋуӕ˔~ҪЄʙҢ\x98ěѿ¬ĕɤȿ',
                                                                            "ˊ˄ˠԏԙ\x88ϳɺ;АріɘѧҔȀБñҕûǻΙԟĵҸћӻ¢é'",
                                                                            'ќıѐӇǇ˅ú͵ȻƑѷȝȋƫPЬʺμӟ\x83·ȣköǖZũ˘\u038d¬',
                                                                            '˄\x94ҙĐӫaΨȨ˧şƇít}ĎƴƷȕĿʉѼɥȼѾĠÞƀTȬϝ',
                                                                            '˱ˎϾţϖŻɝɼƸԦҠФқΊĦƪғԡ\x84Î|ѽ4ϼf¬ĖAƫЀ',
                                                                            'Ԇ϶˰ίӘ˄ԖȴџͳӲãÚǵɫԥԈæŞʟҖѵ(ɻʁЪļɌf\x90',
                                                                            'âŊϡϷ>\u038bӊeԍlʦ˱ԘəʯǮʛɝʍ\x85\x86ϲȆƧԪ˵ΑƙϴӚ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϚΜχĜqʻĬÊӍįԡǳİ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220932.653992:+0000',
                                                                            '20210206:220932.654033:+0000',
                                                                            '20210206:220932.654040:+0000',
                                                                            '20210206:220932.654046:+0000',
                                                                            '20210206:220932.654050:+0000',
                                                                            '20210206:220932.654055:+0000',
                                                                            '20210206:220932.654060:+0000',
                                                                            '20210206:220932.654065:+0000',
                                                                            '20210206:220932.654069:+0000',
                                                                            '20210206:220932.654074:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˊЏ}ʍ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2154397385474050245,
                                                    },
                                    },
                            {
                                        'name': 'ӦѲʷԅɩΞ\x83˅öȈ\x9dӡƐ/1Оβĉʦ.ɡҔİrӴԘ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4462651483251796475,
                                                    },
                                    },
                            {
                                        'name': '0ǝʡźҜóП¢ȲΫǤǔͲԎ]ƔΜ0ͿāғϴΔ˃Ѝ0³ҡǳĂ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȶӫѽĻ˔ӟƾMĜɳӼĤ)ʔǣәȑȩžԕʸɃӍиМј˄Ƨѥˈ',
                                                                            'ψ¨õǉʨȧϬωSɵ;ϫʢѾ\x93BŋӓЊaϙзцё\x9cǪƽТȲR',
                                                                            'ӬĎØӡϩĳѝʄƜĺiñӔ&ɒhԔ\x90ʿ\x80ңȸɀλѪѭϟʫªœ',
                                                                            'ŪÊƿŲХҮ/ęϹ\x96ȸ\u0382ëʹȉȦӲ\x9cɹt\x89~ȑʵяЁϋƜʔʫ',
                                                                            'ģĪǴĵƐФҳ5SӠʚ˜ŶѦ\x8bīǋÂǐ҅ÕϤʻΊǴĀɼɵʦȓ',
                                                                            'ɳӥɝʹʙĞFђɠƀÅԙȡς\x86ѹǾ˳Ԣȑϳ?EĒĶԪˊŸÚˆ',
                                                                            'ӶɻВʃˆÇřѕӵëЖΆ¨ƁѷԂɵƦҐоɂɢʉŕƑώԈ±Қ£',
                                                                            '3ûƝЅȭεӛЪ4ŤП¶ΥόϖʆҝР½\u038bǟԣђ҈śļƊǰɅŇ',
                                                                            'ȭĊ2ÚʟϨ¦ϱSЪӧԡё˪ɝԋ\u038dҭҵʬ˝ÕҖǣѧԏ˫Ͱ\x91ԁ',
                                                                            'GҰĞʲ9ғӝƟЮɤȡʺɋŮϙѤƉʾÆҌëÆǛ˦ȼҷįǾфӮ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ũМːжȅЉ/пЕυɩп\x88εдƹ¶Ū\u0382',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ŹɐƪЗɂķƐʜȦɂ°ǐʪήӐęѿʿǅɽ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'СUƒйѕΘŀўº!ѻ˖˲ʱӗiТѢʻϗΣйćϞȣԏЗˌлʸ',
                                                                            'ъͶāԍώpқŅƗыːѣǝğԋԖʔΕ\x9bȠǂˏҿΠȃњPҹӤü',
                                                                            'ӭҡǷǵgêԜҿ2ƙΰî[ʮЩǢҭ%ΛǡˎΧԣӜϠɸϹӎѮʕ',
                                                                            '\xa0Ə˔ǐˣɦӢӗЏzЀ$Âǲз\u0381ąɾѬÏ³οϸȷrσ;ŭҵ\x9b',
                                                                            'ǣùqµǶŦѢ5ŷӥ҇1˓Áϒ΅ҕӳǣȰΠɵʋ»1˸ɢΓĦс',
                                                                            'ȿцӋŤӉÊˤрзƤ^ÊőłΕΓΧγſ˓ϥǉΌɒ·ƹ]ÉϸԊ',
                                                                            'Úχ=ҝŧϋØɞȺ,ϘГϻȪɔɮҒmƋʺΕҫ\x91ɂҀӔ˧ǿDʃ',
                                                                            'ĀȡĆɄđҚўɖɽāśƘ;ĲӘŇzϱԬϥЧǟςǸлӛӃΦΙɧ',
                                                                            'ƺFӥƚp˨\x97ƶɎĽЗΨkɬ\x91ɊԜƺŴЎϖŶɥǅ˭ɯϏ;|И',
                                                                            'ǍƎϡ0ĴŸĎѝΑb˒ŽąҶ\x86ԧͿэæǞӺĪҒăϣƸôͳȥҷ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'k\x91ǚǈҚД˘5ɤdВĚǺ¯ˡɹЫмśľûԈöчĉǸФǫɊÒ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɹϠұʆάǡpϪЪϱϯҿɚŴɀĎĝĮӥĿOӢӫί5ʌoȒūĻ',
                                                                            'ӰĨƜԆˇpÈϣ/úŭƩήѶʃī%ȍ˞ԍҊϦҪlȼSӟĉɛK',
                                                                            'ҟЄȽ\x8eȍȀą;»ԨӦǗЍэϗǮΙǚāʁȡŔϢƻȧеΚѠΒƤ',
                                                                            'όʑyϛŃŋɚ\x8bȝʫμǡɰç˫ɸȌɳλӸǼЛϳȴ¾ӠİɈӳ7',
                                                                            'ŖȡͶɬƣʴȌE_ȳʔҍʿѩαÅԩҸɝʩɴЂ(ǎɓ\x84hˌϝP',
                                                                            'ʂʀӋīѯԍ˧ĴſƱƐ˹҂ŮɵϋȥͽŦ\x9cРψЏˬҳ\x91ĉтU˥',
                                                                            '˗ҬӠҗѮŌɗΨяҧĿyjӘʈɂǹ͵ʍ²Ӄѷԩ\u0379ΣпʢŸǪǝ',
                                                                            'ʢџ\u0378\x87ċÄƬǳǵЕЬ%\\ҧɳπΆšҷҩƗӺʎ¡Ϛ5ĵԄǓ˪',
                                                                            '\x8dʞζ^ϰÇZǍȑɈĲȠÀʸĝЀЉԊӑɇȺјƗĀʀŢЊÓ»Ů',
                                                                            '\x97δˋȾ\x84ˠîÜ\x90\x97ɩ ŠѶ×Ѫ\u0380¡ѡā\x92βÄȉǭȏ˾(ë¾',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'EКȸԫʳҨсӝΠŶԒҜҡȕӲďшȶϨјő®ѸKӺŏ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 808826.6954760983,
                                                    },
                                    },
                            {
                                        'name': 'ʜŤɝќÇ\x94ģƦϡʀ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5203996976716630259,
                                                                            1907734344341536060,
                                                                            1431656535881368452,
                                                                            6428802285564385777,
                                                                            -1462185964225509947,
                                                                            -3204546845608453366,
                                                                            2735744657929581882,
                                                                            -4340904501645567443,
                                                                            -4975157357251991647,
                                                                            4312389903373336554,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȅͼϔǱoƩǛԫƶɟȨƲДӅБšϔɅԠԏѶȟЪʑţōſ¦ǲ«',
                    'message': 'ŲɦʤϘѯԟēˮХŨԭ\u038dк¹΄ɤůƤӓ΅η×ŏТѨԂŔßęÃ',
                    'arguments': [
                            {
                                        'name': 'ѐ˼ƟŜ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5701233418354326541,
                                                                            4223146676864745732,
                                                                            -1590877248684167586,
                                                                            -5554609454245777325,
                                                                            5260226325883837330,
                                                                            -5642870237974151449,
                                                                            -1307816635131062380,
                                                                            -3636733881394169672,
                                                                            -7134760002361381,
                                                                            6362159990264024157,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˰ϷӡɅҭ˟\x85ү\u0380İ҈áʹ5ɫӝóWīĹα\x87ʤΌΙɯӤŀɏӮ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220932.657358:+0000',
                                                                            '20210206:220932.657373:+0000',
                                                                            '20210206:220932.657379:+0000',
                                                                            '20210206:220932.657384:+0000',
                                                                            '20210206:220932.657389:+0000',
                                                                            '20210206:220932.657394:+0000',
                                                                            '20210206:220932.657399:+0000',
                                                                            '20210206:220932.657404:+0000',
                                                                            '20210206:220932.657409:+0000',
                                                                            '20210206:220932.657414:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҭҽ±RнDYĸ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220932.657646:+0000',
                                                                            '20210206:220932.657655:+0000',
                                                                            '20210206:220932.657661:+0000',
                                                                            '20210206:220932.657666:+0000',
                                                                            '20210206:220932.657670:+0000',
                                                                            '20210206:220932.657675:+0000',
                                                                            '20210206:220932.657680:+0000',
                                                                            '20210206:220932.657685:+0000',
                                                                            '20210206:220932.657690:+0000',
                                                                            '20210206:220932.657695:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҆\x82ӫ\x85ӱѭҥŨԢʥɃ\x8dѓӨЀéɜз5ȜĭϤ˪єǓһľʄϲŇ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'КȢ\x92ÛğϦĕɊǔ{ϭӭϾǉŧѶєҡϑ~ͶӺáɰ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȲЅ¢pèѢчӄƀēɸŬԝѡf¯ϑ\u03a2\x8fЭӰǶǯѐΚлπŘĺҼ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɧȒŖѽҚȦΕ˘ҔāȞŗ~ʉʩκҩϾÀŮʤҦkʈԥеνγƷх',
                                                    },
                                    },
                            {
                                        'name': 'ǡσȩȺÚŮǋ҂ÚãӆȁҪӋČҜŌȡưϣǖ9ĉÏϞ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ӳɱ\u03a2ʃĎȵӬǄЄǂūñ:үҊǢ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220932.658468:+0000',
                                                                            '20210206:220932.658478:+0000',
                                                                            '20210206:220932.658484:+0000',
                                                                            '20210206:220932.658489:+0000',
                                                                            '20210206:220932.658494:+0000',
                                                                            '20210206:220932.658499:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '@ЭЛʁώ˫ҟŁǯӌàĐ\u03a2ү˘ԭ\x83ƟҧȲчӰ˒ѵ˷ԡӦ˭^Ԏ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220932.658707:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʖƂ»ǔϫӜUˡǔԎӨ^ɔŰңˉ¬ҷюϏ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ăÝ\x9dƚҀЅώǁĆˮÅέԦŴɗáǕƧѱŕМĦϓoɶʧҒrŊΘ',
                    'message': 'ƦɇԮǲ˭Ӝχ³ƏțíӁЧƛѬɂτƔҌҖԐѝĻĈʛȤǶӢ@Ў',
                    'arguments': [
                            {
                                        'name': 'ʄʀȈ<ǑΛѤӾҶ?ϩƵ"ʌм7µĳÉU*ɜiCЂšνƔҳɟ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220932.659251:+0000',
                                                                            '20210206:220932.659261:+0000',
                                                                            '20210206:220932.659267:+0000',
                                                                            '20210206:220932.659272:+0000',
                                                                            '20210206:220932.659277:+0000',
                                                                            '20210206:220932.659282:+0000',
                                                                            '20210206:220932.659287:+0000',
                                                                            '20210206:220932.659292:+0000',
                                                                            '20210206:220932.659296:+0000',
                                                                            '20210206:220932.659301:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƤҿvǘӰȯ1ŏʂœѐ®ȉpȁѰДß˃ҋ˟ΩӺȥ%',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -317452812796702070,
                                                                            565630666395964460,
                                                                            2249078059765076580,
                                                                            -7390825224222308978,
                                                                            -5713794501118975513,
                                                                            8095989878633008526,
                                                                            -6319435730036427134,
                                                                            -1699663642342354014,
                                                                            -7914411458764189587,
                                                                            -6279732746829862709,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʆ\x90҇ˍƌ1ŒĶҫѬњѕĹ\x90ˮÔӼДЇ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'љˢӠӮҶIipϕѿ.šĿ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȼ҇ЃǤ¤ÞıaΌjԁңͿХѝ\x97јѶф\x87қѠțƛįǉӥ\x9f>ʀ',
                                                                            '\x83җɺƟю҄ҳ҂ĳ\\˃ļӺɗѵˊдÒѸƎɌҫ¨ȏǤȌҥӌ$ÿ',
                                                                            'әԉ˽ŝbĻ˂ɥӊ҄ϿӋƔĸΧ˳ЈɓEϵȝĲЌYТ˘\x94ŲϡӢ',
                                                                            'ħх˔^ˇ1ԥ˙ЊɕʮκŕЂǅũʡȦԮÀƢͷЉȄŋÁǪǁѲX',
                                                                            'ͻƭÓϯȫ2ưѦΣӄƩӖòӹΌȒӗƼϠˬĉҳƋҘäƬɭď}Ň',
                                                                            '.ЯԘȍԥԜT˴ʏő˴ļλ,ѦӣϽѡ^6ȚͳËfïШ±˼Νɞ',
                                                                            'ІÊϢȠ9ʕһήǻɌϗª;ѦҦŻˍÞʤѯοȷ\u038dǪűĂϊOĖƹ',
                                                                            '®ƉT\u0378ӚҭЪУéªʕǠʿԜψʞƔҧχƨϧǲтʿӾƒΖʣŃҹ',
                                                                            'ԧԪkыŬɋɚķИЁѸÝŗʩſҺԈϊʂǚʹǭЇҧŤƃ˩ɺΏ¿',
                                                                            'ǖÐɠϟƿˬ˕üƸŜʬãÖÑΟϖƷƑŷҫ8ǿȄѣŢҷԐӊ\u03a2ƙ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҴӉӚÑмʂáΥȥɾģюφɜӎēā\xa0ӥPɝԨû΄Ԡ#ʷʗϏɔ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4581656362697060122,
                                                    },
                                    },
                            {
                                        'name': 'Υý',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220932.660605:+0000',
                                                                            '20210206:220932.660618:+0000',
                                                                            '20210206:220932.660625:+0000',
                                                                            '20210206:220932.660631:+0000',
                                                                            '20210206:220932.660636:+0000',
                                                                            '20210206:220932.660641:+0000',
                                                                            '20210206:220932.660647:+0000',
                                                                            '20210206:220932.660652:+0000',
                                                                            '20210206:220932.660657:+0000',
                                                                            '20210206:220932.660662:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ņɆŷϱԥѧ,ҽșȤθʖɞρƅtóm',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220932.660914:+0000',
                                                                            '20210206:220932.660924:+0000',
                                                                            '20210206:220932.660930:+0000',
                                                                            '20210206:220932.660936:+0000',
                                                                            '20210206:220932.660941:+0000',
                                                                            '20210206:220932.660946:+0000',
                                                                            '20210206:220932.660951:+0000',
                                                                            '20210206:220932.660956:+0000',
                                                                            '20210206:220932.660961:+0000',
                                                                            '20210206:220932.660966:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѲþȝșжXӑӬɽЧ:ʕԐǠҦȥôʬˮȞȯԒԡëũȣϜɜѢЁ',
                    'message': 'ȭΈҏɑŖŁнƘʝаʝrƆȵĉʮљɩϗͲ˦ŏ˃Г é\x81ǒҭӻ',
                    'arguments': [
                            {
                                        'name': 'тˆĒÂҝʦѕƕƊǪ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6770876599599136007,
                                                    },
                                    },
                            {
                                        'name': 'kΝáǤɧÑѲĹĈiϔɘӢΰ?ØƥЉӧŽԞϠѹҕ^ɿňҠӤ\x92',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ҖɲИɗȼŊžШ˭ϡӠЃɠ\u038bτUғКЀȈɥĒӗíŝjʅʃœѿ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220932.661794:+0000',
                                                                            '20210206:220932.661805:+0000',
                                                                            '20210206:220932.661811:+0000',
                                                                            '20210206:220932.661816:+0000',
                                                                            '20210206:220932.661821:+0000',
                                                                            '20210206:220932.661826:+0000',
                                                                            '20210206:220932.661831:+0000',
                                                                            '20210206:220932.661835:+0000',
                                                                            '20210206:220932.661840:+0000',
                                                                            '20210206:220932.661845:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȘȉŒцӌ·ӌҫÉ§ȺŔʟϜ¯ǽ¶ưƒˏҢĕү\u0381ϼԓȿ?ȹѵ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4322315300752085830,
                                                    },
                                    },
                            {
                                        'name': '˦',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ĊůėǪͺъЍ\x9cϷԍBǠÓˍÈʍчʴΩɜͽśѻhʧӞKÿǧǙ',
                                                                            'ѼЊƉĂι˼Ư˜Шȗұǂ5ïеѱԥ<ԟ_mƝ˶˾Ǌ˞ů\x99ÄϤ',
                                                                            'EşύʕǂɆÃΦǠ˻ҫȄɥ(ͰʤВʎïʚ\\ˡϖǋþӝŌĞћŐ',
                                                                            '¬\x9f|´ϤǊӿ\x90ӭŏŵÔŸӻȮzɠ\x97ӛԖ\x96ĩЈ,ûӳ˞Þ¿Ԙ',
                                                                            '˜ϟ\x98ӆķaĴʀį´ΉτʷΡʤѳǘ±ƀηżøԭǇŌˉʚļŬΰ',
                                                                            'ʷrƥѽ΄ӵѳˎʮǬǯϋÄѲǍÜ\u03a2ӲʬZŮѢɖɝƍʨҒφĄҶ',
                                                                            'ѵҰƐŲѡ¦˜˶˴±ҭ˨\u0380Ʉіț˯ÁȊ_ӊʌ҄ΡҁɡŌΊЎɤ',
                                                                            '³ĊŲÉŉӛ/ʧƉƶ˶˥ŀýıқӓģſԀêϛ¾ɱĵ˽ΎǪĊʳ',
                                                                            '®ʛȵbϊ°ҋϸҷűҺÉʒÖΈҗΤ\u03a2ɠӬɴҟĒʉRȻΌșԐЦ',
                                                                            'ģҳ8Äʅҝˆťȧύ΄ѠǏԭƫгИřɳӨм˛¡ҋ˝©ɑ!ϛͽ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '> \x92ƲƦнȔӂԫҨΦɅƖѳ\x83˻KĻԅ͵ґɐ϶҂ȻǪʑ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҧʋɴvˇĹ´˽ˤØOZƆĔńĩɫΜӼIJѼΞ-|¡ǋÓӃǜ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΆьЀѺɷ¸',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '\x8cʅҘÃΡȈчç·?;ˑŌσѮf',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʐȀȬĿΗŽLҒƝЧѠщ¸\x93рʇ4ȷѠэéǮϩӘĆȯΠɞoΓ',
                                                                            '\x9dєε¥ϽƹȒΞЀўƹΰɿϰҸъŻӊ\x99Ҡ}"ϋǀxzҭȝ¬ч',
                                                                            '\xadѹ˂ȃɲuҢλȺқǓƤ˙ҼūĊÏȇфĚǉҰ\x94ŃĠδή\x88Ŋí',
                                                                            'ѻʙȨӡ¸ĜцқΛӨľȒʅǜ˘ϕ®ŐͼɱĉӁŻƊ҆ƋԪ҆ҒӸ',
                                                                            'ΎǌӷΙ©ǏȥŸȧ˙ıҌХǛ%\u038bʵuς7ίИѓώӘǢҷƚӶӺ',
                                                                            'Ďѐн*ҀϑƸсȔϿ»eѣǰɇśɇϯĩΟŪπǒǉљĽ\u0383ϾƷσ',
                                                                            'ťҊ\x83ҌŭԧŮ҅ǈ.ĉɊJңѪӕȸͲѡԫèşÏŋӦŋǢȓĥԇ',
                                                                            'ɞοǇǯ҃üʁжɈȔʫвʵƼȑУʋĵϵʼˣËӎțư\x9eхΐǧϘ',
                                                                            'ΫǎҊœęҼtʄЬĐÆԪǇďψϕMƁӣ®ıřʈȥɆҶҀǮɋФ',
                                                                            'ɩϲ\u0378ƚ\xad\u038bɐсʶŤɇ*_Ğīәʫ\x85мФЉǮѽҀ¢ʽϟǒϣ˽',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҙˈϰȎѼȡԌЮŘÜέΨӶѷƽԫНƧөǣ;˫',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            71545.82178155793,
                                                                            807444.9419666778,
                                                                            156363.54884963692,
                                                                            100637.75444719399,
                                                                            811078.59175854,
                                                                            58228.40807250657,
                                                                            8324.178143685975,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӂϺùĻ8ҮΚĲҽҴ¤ҤҀÊӁԔƫСō¡ΤǄʈwіѱӝʇДM',
                    'message': 'Ӏ/άʠͽƨΞʬДɶ_ðϺчēҚĴ\x81\u038dԀȕɨ˧ȼ˜Ƿ˼Ӽɺʵ',
                    'arguments': [
                            {
                                        'name': 'ǇКHҮѧ4è£ÂҐˡɵ¬ЉȢόȮӈŀɱƌΓɸĔνӵӹ҇Šψ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8546720065647942121,
                                                    },
                                    },
                            {
                                        'name': 'Υ\x8cĂŮƶɲѡҜЂӄˬСǫʍ\x88ЋԞ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 627322.5953117865,
                                                    },
                                    },
                            {
                                        'name': '9ςƤ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "˸\u0381V'ɬÃȲԐдĊҷ҆ǽτя",
                    'message': 'Ȼ˺ȁƙѥŴʣʮǂӞ˯ǬӸѻԫÇԑĕǑКɘӀӫɯāwȩǢ\u0380ү',
                    'arguments': [
                            {
                                        'name': 'ЖĸĩɛpВ\x93ĈЏȌ\xa0ЍϒʓǫЃțϚǲӵΧѾ˼ϹǨϮƀ˱џɃ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            460389344646019831,
                                                                            7153908313100059841,
                                                                            217998572377859630,
                                                                            9171933552576272534,
                                                                            1003288260648353200,
                                                                            -6343945271157728423,
                                                                            -848340265860876552,
                                                                            -6865901326487528845,
                                                                            1965458076509332546,
                                                                            -8863299886914483728,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǭԛƪņʿϮºȡӱÀύҠμƗӮ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ğԄЏ˅ǛѠԦɓƕQÚȘϲmAʻȓƇφǸӌϏҬQÙ¤ѦԘ˱ϙ',
                                                                            'xҩӕʤÖЗƛĐȥͰɟʱSȩˍүǉĮϡżŻңÄǸӸ҂ҙљ\x9bԈ',
                                                                            '©Ԕ&āˬӦ5ίɸǮԍ.ΧʉŃĽËȱĞѩ˼ң˦ʨ˚˨ƸȞȎ˘',
                                                                            'ʟО˰ѹӜԟňˈˆöǶ;ӇêƎʧʵғʌ%ğȹ pľʬöĮ˵)',
                                                                            '˱ǿzҚ˟Ǳ·ńϔƽŞӘˣЬȵ\u038bӹʇʖˇƺьӋńѯ˘:\x83ϒ˩',
                                                                            '˱ȣϱɔɶφκұǟŉyÏ»ϦυˈǪϞΖҋяКƊ҆ҶĚ7ÆϢΧ',
                                                                            '˯Ѥȁʧ8СRеҜЦͶ˪ǥb˫ϧ˳Ӄ=άëФ\u0378Ҡ˭"˹҅îǩ',
                                                                            '{іΘtȡy˧ѨǼʲλ¡ÏΤŭŉÔԫΡʜÓ¡ĞǮЉлөɗŇϽ',
                                                                            'Łɼŵrә\x8eҀļ\x89¬˞ǊΟ:ɵϛƢ¤˽đ˨ѸҧʒδIôȿЖЏ',
                                                                            'ȝ\x7fǲǬĕÆͼ҄?ŗͷїIɳɫȻԮԒƄȿǺǂ\u038dЎņþԤѥ\x80ǜ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǟ×ÆȮ¦\u0379ƯƜԁɋҽғФâβˍӈ˒ϋΛƈЪϝ˱ɸЩє˅Ăѓ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6697542075237185437,
                                                    },
                                    },
                            {
                                        'name': 'ÊѝӞźҚɟȏιʟϏͻІϥїҿ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220932.665625:+0000',
                                                    },
                                    },
                            {
                                        'name': "ԜŁ҃~ӴǓɒŧәºєłȬ'·ȞɽЋďų\xad\x93ϗĊԆˍĉ",
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ИϼįIǇpԏζƻ0MӜѥŰşȈӄļšŚĝǀҐʆȾʡǣǒ¶E',
                                                    },
                                    },
                            {
                                        'name': 'ϼ҆їȨ˂ƾƑұŕ×ȶƑѱęЭϕŘƴƁʟЂǇƣдɄʀxɶŪð',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220932.665917:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʅȊʈ¨\x94ǵΫ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'I\x9dϏˑӸ½ʟΥɠĴУĺЫϰ[ˆͰԝĔĭԍ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƐÀˬ\x80Cѡșʋ҃жĐØūӨPƼkȉ²ɌҠ]ʕƆɆԤþĎƞɬ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˰ϼŕˏ\u0380ӊțͺɎδʴͶӨʅɻѥӜƇҀЅǡͼȽŪ©u%чēƽ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǆеżϽΖиŲқ϶zųȪ˙ĸрϞύÏHĉÃυZÕԧȫŹĬȨņ',
                    'message': 'ЃɈΕЫNµҟЭ\x93ŘƆӭʘ¾λƵˆɕˠΞʙYzÆҲȂÇˮȐ˓',
                    'arguments': [
                            {
                                        'name': '˺ƏʉǥӴɋɛʕ˖ϠĎƁʃͰɟӤʀĻȚњ˕ӚVʹҌұ˲Ґύ˳',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4230465213404293500,
                                                    },
                                    },
                            {
                                        'name': 'ǪқӅ¬ʸН3ҼцʧUŤãºƷʬ¾ŅΎǮӤƘͿҗ=p˭ʞ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƼɼЂ˫ΦŻĒƮɱίƱȋ҇ϮˈƘȤκŊȋԋћ˼ʰϒŀǷŖȝɠ',
                                                    },
                                    },
                            {
                                        'name': 'w¥ʈrɭđDȊĨē',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ԓ¢ɜɅũαĩӄȣƀ˗˅ĖԤĈќϋϡɴӭӫ\u0381ǡ˔ΟϪϛԬԪȲ',
                                                    },
                                    },
                            {
                                        'name': 'ÙǂκȲȏſРŶǆЙťĻԦţ˸ȁДƣ˟ˀͶЌԅ˲ƄҼȺʆɺʆ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '}Орӆ˒μɹƵřʩҦ\x8aƒȫƃȧ"ӯŌѭǓǠīʕ˜ҳĈЩΛ+',
                                                    },
                                    },
                            {
                                        'name': 'ӑϙ*ȴ˳²',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220932.667830:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҷιԖνǒé˭ÑŮӣ¼Żà',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            534435.9227186771,
                                                                            -74144.61476195019,
                                                                            560531.8482869609,
                                                                            535652.6664418139,
                                                                            98796.26847189086,
                                                                            625882.1041575284,
                                                                            561011.9829563145,
                                                                            847884.8771615875,
                                                                            953660.8955146549,
                                                                            175241.03854420042,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѧǾǈy˙ʕʺȨӉЧ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȳяγȇʼƎȬ=ɅҋȡƥčÆҏξǫΫҘɡ˨\x97ƸǞӽãɊz϶õ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            323321580709026988,
                                                                            -4659035393729300092,
                                                                            -1145303606310997259,
                                                                            5302637731434079641,
                                                                            4178782846495149638,
                                                                            -5900987179618970326,
                                                                            -7866185205434679186,
                                                                            2740732692768585169,
                                                                            4479784149311366146,
                                                                            4631097272643996192,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ßШӦʖϦƐȴƝƅμϫƝʋ˹˵˳đҒź',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4717704658096963273,
                                                    },
                                    },
                            {
                                        'name': 'ɾϬjҬƥΉm.ÖӐƂҍʁ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            549663.495367311,
                                                                            188067.12691064307,
                                                                            565081.6882851594,
                                                                            303264.52386845945,
                                                                            -61850.50316699126,
                                                                            516038.14288348495,
                                                                            573724.7659924405,
                                                                            689964.5960567386,
                                                                            -67671.70319568523,
                                                                            855648.2150102535,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ãʾˆǟѵ Ӯ;ȽѨћȮʴƸˡԑϔfRҠƌˡϩʶä?sƉăƭ',
                    'message': 'ƝǿžÊЦ҆ǑϹҭDȖƌЯ\x89ǒĘʧ¦˽ƓԝĜǚҪϵϰɛϋǔ˲',
                    'arguments': [
                            {
                                        'name': 'ÔðϷсµƻҭυЮɩʸȾˣSƣʘҮҧχ±ÂӞȊа\x99ϬƸ҉КЭ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2001621551428084841,
                                                                            -4961324702162070927,
                                                                            143985031803660175,
                                                                            -5227553207439217194,
                                                                            8313546684148300596,
                                                                            6950848401591380109,
                                                                            -1886142797356766861,
                                                                            910795689234444456,
                                                                            1330454905185793561,
                                                                            121421349821136462,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˦ƫÒԥɅàƜ\u0383õ4ʛǒХԩHȡ§ŸѿΈ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220932.669536:+0000',
                                                                            '20210206:220932.669550:+0000',
                                                                            '20210206:220932.669557:+0000',
                                                                            '20210206:220932.669563:+0000',
                                                                            '20210206:220932.669569:+0000',
                                                                            '20210206:220932.669574:+0000',
                                                                            '20210206:220932.669580:+0000',
                                                                            '20210206:220932.669585:+0000',
                                                                            '20210206:220932.669590:+0000',
                                                                            '20210206:220932.669595:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'qãI',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220932.669851:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÆŢӈŅŁ҉çҴĸºɪұǒӝҎğĳó\x9dɗŠēsӅȤˬϖʾҙғ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x8fȀԛӺҖ\x9fдɹɉәӲ΄ƘɍԫϭˠԡȩϏζ˶¨%ƛѬΑė6Ȃ',
                                                                            'ӻŻȳʝΔ]ӽѴъ\x98ɌśњɲɝϵԚϹ˛·ɧ˄&ʜ˔ΙɊɌ˯ñ',
                                                                            'ԂʋfǖǔӣкԆűԩвȜԫФȏ\u0380ЌŞœǨɼǅǱІħƯНәŭȉ',
                                                                            'ĔЯǥϸôũЧҩŸӁӤãɽ˟ԔКҾɔ4˩ϗϥƺ-ƩĠ\x8aѹмµ',
                                                                            '˸ÄȚȻΔ¹ҔѳѿҞxӎӼϑс˸ãϏùŰˆΌ΅өǮųǼΉ\x9aȿ',
                                                                            'ŌˡԒɻϙ˛ҤÁғȓɬӽƎhÑƜҡʷͿқ\x7fŌȴˊǱǊ·ʰӤȇ',
                                                                            'ӓԓǏû[æċќƐїž©л\x8aϸʔɟλʫțò˙ӏʘͲNȌΣΟʣ',
                                                                            'äĸÙ˷ÚӀǘȝfϩҫяʾ˔ɞÙҷ½ΈѹÙƀɴʅįƤƩӢ˹ʄ',
                                                                            'ԏʹƭϤΩǄʖ˵ϲψӎ˥ʓɧԂҟƆӠɐʔ˖ЎjӨңвѺǱҫŒ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'э\u0379ÅόuѤ˻˕bðȣѰӹζƆ6ŴǠˆЗΧʽ;Ȩ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƀ¦RƭџƗɏěѥ\x7fϽ\x9eԗɔȅͳ\x9dbƐ±ӬϛÙõҀǞǤ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 395081.5273368848,
                                                    },
                                    },
                            {
                                        'name': 'ӏӲƘΕΖŖ²ʫԐ!ʒRгӥИѦǣԄ«ęЉҗŗġƨˆɧ1Ş¸',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '·Ǧ\x91ȹȵӫςŵҸˎȳəµӷÞƥƱɫƀͱŅӫҠǮ®ΕďѺ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƒ\x83Ӿ˔;\x90ԧбɈӟǨĩȷ#õƻҐӡǲʝØĸ¥Ƞ¥˱ǔҸ¢ό',
                                                    },
                                    },
                            {
                                        'name': 'όιʫ>ΨӲP˚ǰөȝ¹йĒÁǺʮ\x98ÈңʨÓʗјҪρʋȼə×',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            363274.8575172335,
                                                                            924014.7853066329,
                                                                            57958.78326533074,
                                                                            204070.96628021996,
                                                                            206334.67920689145,
                                                                            269503.73403828294,
                                                                            844441.9332048518,
                                                                            575467.0989463365,
                                                                            131862.0196287655,
                                                                            710382.139189543,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ыů\u0382ѵΦɍ˶ĢфΔҗҢΈã\x97ρѽͰӏНƣΥxƣǙʓɂҬʠπ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 906807.1044405578,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʮƥʀʄĻʟʵӊjїΦː\x80ͷӡҒșɔɄɚɭΫ',
                    'message': 'ԋaʳƥҸÂûщȃԫǆWʺMUˏϭ˵uЈǣƄÅȱөқтѰαŤ',
                    'arguments': [
                            {
                                        'name': 'ųŷԠȠ$tӮmкʰϞĆ҄ѲΖŇˑɆòԍňȼԏ',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӄÜЀҊF¾ЀȡȶԢÿ˶ŶӰ˂аĘiҧƽŽƏϧб=σЦĢӆ˫',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϒʡԥS\x89ŉ˼ԣ[иҽԩŋϷʶƚ˹ϛƬǶџϕѾғƥ҆Ġ˺ԟ9',
                                                    },
                                    },
                            {
                                        'name': '\x9eҬˍŚŠѠœѩоɑǒЈƪůԨ#ǕуӢƩϔɜεѲȓĐ\x97˶ɉs',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1927368637692884238,
                                                                            2970592575612777436,
                                                                            5926111696660328151,
                                                                            9059506103628863536,
                                                                            5062491699192261951,
                                                                            -6550309811722013016,
                                                                            -2823852708426933537,
                                                                            8635555927145463007,
                                                                            -8916733888685366079,
                                                                            4133189388046472282,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÍƐǴӘЭŸƓÆÍɋκЃīëuǰÅǮ|ɹn\x8bÂƑЌĦƐ±Ё',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˆΚfxϘĄҚäĳɋ\x8běʠWӧƺҸǇӢȂԑ˳˸ʯĐЦҬßϼҿ',
                                                                            'ɯƔ gBǙʒȦ!~0ѝўŮЃ˨ɜФǌʯѢ}ǒȨȘTӑ\u0380ӝå',
                                                                            'ЩƚˇÙçѴԧɅƾ´ȏЄʯȢŮĩØöXƨ¡ĀʙˠĆÞƿЌ^ȉ',
                                                                            'ȶ˺ϋˁӦʸʷɏbƻ÷Ƴω˳BѵʰXĖӪ(\x99>˞һɫ±ɍðǌ',
                                                                            'rʚѥȒҮӥƉǕǇњҳρ˃ӑ$ʑс51a\x98ΜϏХȆþ˱Žřƌ',
                                                                            'ʫʢȟ:ȺϢΒæʊ\\ȗǕ\x88ë˜Ҿʨēŉάˋ˒¢κŔ8μǚйŦ',
                                                                            'Ӕɩђʞ\u0380лɞÈķгȜəǽѨ\x8eɓhÀɰ҃éʀϓТїƆȋӃʪζ',
                                                                            'ïɔĹεҜǾГºˁ¨ϊƎɽ\x8beύҕɒԦ˭#ŉӓүґхĎɉǕӥ',
                                                                            'ÆҼit˻ЃżʞΫϪǗʥȞśũҩБɠą¾жɵЂċѶQӣþ\u0382l',
                                                                            '©ɘ\u038dȟEǇ§ҬМʎdΥƫĔſ¤Ѭ˴Ǉ\x91ʣŕ˘ˁI˔ѓӦɡǣ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѩ´hΣ\x8bʷ˻˔ΣȺ?ư˛æĩӡʾνʴɆ\x9b˅ξΐHоΎʊщɲ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220932.673050:+0000',
                                                                            '20210206:220932.673061:+0000',
                                                                            '20210206:220932.673067:+0000',
                                                                            '20210206:220932.673072:+0000',
                                                                            '20210206:220932.673077:+0000',
                                                                            '20210206:220932.673082:+0000',
                                                                            '20210206:220932.673087:+0000',
                                                                            '20210206:220932.673092:+0000',
                                                                            '20210206:220932.673096:+0000',
                                                                            '20210206:220932.673101:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÂʓҢąǹҒĚĉԝfɬԐďȰʴӀĉûΊќȑѮȭĚÞП®ϾȢΉ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʂ°Zĺ˺ŻǶɓɛɳӤh;ƁзӷήÙô¿ȴ\u0381\u0378\u038dƴǂˀʒɆѽ',
                                                                            'ƺǧϧ˨Šʚ˾ЊөŻщʂ\x92äĉϵӗҽŠӖίŕƩѣÆҫŰОǵԚ',
                                                                            '÷ͷǊЎˣȱƤΞ˾ԩǟ\x95ήƂѥtѲ¼Ȏïǹʼ±\u0379˒ϸŘƞġҌ',
                                                                            'ŎŤτĄɊ±ϤjӪҧĪƮ\x95p\x9fыϺɋ¦ұ˩ќȯԭ{Ǝт³ЅǑ',
                                                                            'ǈ-Ƅˢ=ЧǋтťʙȣӐЛӥяАɣѣԢwǘԎϴʚЋˠӭγȧϏ',
                                                                            'ԟƫҁŀȐөǶ\x9eѯĆĹʵ˸ӆР˦ϣſƌÕɮŵԇû|лѩǣ\u038bȵ',
                                                                            '¶Π͵ćËΛϤŤŷM4ÔǮД\x82*\u0383Ҏǈăşɤ¿ҊπɘʠҌԈҪ',
                                                                            '¥ШΨ&¿ԙBã˝ҕЧӆŽʊīʎηӓӭ;Ԍƪ\x90ğӚ˖ɈΓ»ˣ',
                                                                            ';NļәӊǘӟĎԡӛƁʯ˭ΡǹӱŔхБʗЈѹѶшƄȍÈęУӱ',
                                                                            'Ѵ˽ʦÔďԣǿΚĎͷϩˈΟдjɒȢ˒ɺ˼пƁȇ˹ϰƕ˻Èʄć',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʫà҇ɕȺƢͰУÆԔĹӓʋĮͼ˱χæɧͻĈĥ5ȈʲūǣÙҷÕ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 714955.0858375254,
                                                    },
                                    },
                            {
                                        'name': 'ɥ3ӈϻ˹ЪͲˑŇɢѵαċƥкԏљ¬ɣƋĊƎҢԩҧaʮ˕Х˩',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4330036222898611520,
                                                                            1332453786874807044,
                                                                            6202398472893362608,
                                                                            3130769027287223484,
                                                                            8777431227514600291,
                                                                            7903640681564478545,
                                                                            375823414927106154,
                                                                            -5782886258255697317,
                                                                            8506273947959432843,
                                                                            7123714403554692682,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϤȠǑҼ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 832043.9588581499,
                                                    },
                                    },
                            {
                                        'name': 'ӀͿ!MʨʅŤȃӚɄĹоɠß:ùǸέОт\u0380˩ƙʀӇΠ¸ɐħѕ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            638208.7309799608,
                                                                            871824.0095183162,
                                                                            571468.766979161,
                                                                            228679.0999273687,
                                                                            -99065.31234174495,
                                                                            226874.1152749837,
                                                                            466320.649797771,
                                                                            277681.0285301373,
                                                                            412718.06969770987,
                                                                            929233.6761099866,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '+ЖɆƓǘж\x8bž@ϿҽλáԚɇɷӲʟͻԏĩ϶ͱћȵȕ§ɘʤ\x8e',
                    'message': 'ɏ˵λŔ9Ζț3ȬиΖŮɒԮЁѐÓêԁΧʭήĨӯ˳ԓ7ʎĵϵ',
                    'arguments': [
                            {
                                        'name': 'ӳŨʉĢŋĮΆΪѦȥȳɉ˃ɗўӤȴяӧИǚȯѥϠǨđȘİӼɧ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1814316007325654907,
                                                                            5952576369078088049,
                                                                            -932680631679697323,
                                                                            6640392567403659836,
                                                                            6909824055002096692,
                                                                            -5682482222095364073,
                                                                            7492767372888637417,
                                                                            -755654191946489192,
                                                                            -3855992296320526922,
                                                                            -2848272695396300994,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Â*ёĽͿӥˌԢ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƙиΚфԇҦ\x84ϰ{ķ\x98ʺНċɕƤ˒ьgĤvȳǐЀҲνΊú˧ǫ',
                                                    },
                                    },
                            {
                                        'name': '[ξèƹǑΦÖϮĕ˘ϷГƤāªÆҔÐѬΎʽĮıϷјЋҗŢȯƞ',
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ќɉ\u0382π}ɽԨӆưǨҺǾġ'",
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ģӌǆδUҴơфţȡќʻĩZƼͷѐ÷ǓưϼΐϕÌΚO|qŏϑ',
                                                                            'ʹʝʼѣθ\x88ʚ˺Ŏ»XӤƛзũʹ4ΎʸǉŗɧZÄН˷ťüɩш',
                                                                            'Сș¢ðơŜКёСΌʞñąѸ<_\u0383ӥǴǬǣҊŖКʘŲÊӅƘε',
                                                                            'ϥƫȇ\x9c\x8bpϖͱņPοȮˍțϪӑώҽҌǐćϰā\x86ԊʳǷѥʎԢ',
                                                                            'ЃǇʤCʰξɄËΖĂ¼ʩƋŌφγŌƮӢϵȑFњƎžˏâȈȩȫ',
                                                                            'XȌϧːѦȣЦȻГʩźüÞˣӳψƳĀѣғǝŊˣʇƅɬωԈАВ',
                                                                            'ɍѫȃƪ©ÄȷқͿòǧ\x83҈ϛzϥͷV#ǟÄÀ?ɹѽҝ\x8eɹƳǀ',
                                                                            '\x90Ǔ˽ȧ¶ΜħЎƇЦԌκʘӽʊČфΗɾǴǍ¯ʳѠɵˑǡʧЎΠ',
                                                                            'ƮśԀÝŎΉǜθɟR¦ѩű;Ӥ˫ʞşȏö\xadĔâ҇vκԕʜɝƤ',
                                                                            'ԢƉøǝϷϡƵӅȉĬƌMњʧđŇʮ<ԥԏȓԦƪз$лпʕǌǱ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '%ȗĮ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʞ:ðŰŀŇʖGӎʑ\x9cϻų1Ŕ϶ϗƱ¼ěʥʶЉÉαΫљϝҹϒ',
                                                                            '\u0383ƄɹˊЬϋƏƃѵțȷЂ˝ΗӬ\x88ӚƒPȜ҈ҊȃÕ\xa0ťɇʮƃΤ',
                                                                            '\u0383ŘīŻɬϕďхȤʳ\x84ȢĲϱĀҰʰҾӁ#B¢ТΪɘϠũ˽ϡӾ',
                                                                            'Ʌɷ8ȒƳίҵӇѳĖΉӇǚ͵ĨÊʊ˓ˠʺӪìχĐыɍȕɫǞ7',
                                                                            '¢˜¾˧ԭǮԠЌIȅӫʵ\u0383δˠšѱѶʘɈǵȁНЬГƶɂ)щʐ',
                                                                            'ѤľΏʑʺԇlĹȼԦJЄĞöɉÈԀ|ҢsӵƆŋϻԛ¼ΐќΤΌ',
                                                                            'ŋˍ;ӄҎ\x94˧ǿҁÂŪЧϬȍǹŹНΙϛȷáèǖͷ\x83ƥëɟӫЉ',
                                                                            'ˑĺ\x9bǬźő˻ѽϴƣǽѹӻӉάŶȆӁмˆɶԝ!Л˲=ĚKПΡ',
                                                                            'żļѿÚǥƷάЬRОǡԇɒКïŖћŗʥԜӠЧǞІпxʢɯȈʆ',
                                                                            'ěИɔǁȈћƌ˭ңɗ7éØԄԎѹѝΖǯÌЂσ®ѹφȬԆƳɫϞ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ţҗɝ˷нϒƧ˓Ӂ΄ȠX˝',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԑ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            251469.7483044344,
                                                                            -81964.65009987363,
                                                                            826027.441423332,
                                                                            282942.91119909985,
                                                                            313279.43723869906,
                                                                            359788.1207152324,
                                                                            412518.5038478616,
                                                                            760534.27240707,
                                                                            910022.9411229899,
                                                                            949028.8690869256,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˌє0ȗƯǙ4ӄʎԉÊώǄҧέτкӺęɪóв˯%ɆĞλӸßк',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '6ӺǜɵҲȭƚđԛѼǙк\x94ŨǕƷŽ˰ǁӶ˥ċpńʶɃô¦Ġș',
                                                    },
                                    },
                            {
                                        'name': 'ϔƪӅ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5735144990818507855,
                                                    },
                                    },
                            {
                                        'name': 'ǬÐϵvLˢ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'őŔґÖˀ_ͽ³\x7f+ǬˆLӼɜĮӻĴ˒ƃʬъҚÁcʌҌö˔Ơ',
                                                                            'ɕȂι¡ĥ.ҳĀУԂΠѕрпƌnȬӊϟѐЀÀʼșȷϋčñ\u0383˷',
                                                                            "0Ͻ\xa0\xadˏϸǖҥbǝӒȴĞÿŢϓӢő(˖3ԥΟŧЃȓŲ'ɣЖ",
                                                                            'ŀȭƃɳԥ˩ТҘи<ϟЋпϱǢŌÿԀȕĘHȝӛīӻŜǘϖßŸ',
                                                                            '\x97 ¸ƊϹ0%¿ӀȂЩəҎƢʄҪǥӨʼԊДPήɣʁ˴ϷԨ˓т',
                                                                            'Ưȏǳéԫķΰ.+ўHÑʺ˭ϩˣћ;ϒвĦõĀΙɴΓfǇKƇ',
                                                                            '7JēϵϢAӡâˌѮͶͼĀ˸ԁƙʈ˔ɏŶЬʥΐ¹Ŗθ&сųɀ',
                                                                            '˭ª+μʁ3ĸľŎEĆȵˤźӬ\x84ĄéȆFԠK¨köĵʘӄȥʚ',
                                                                            'ѻҧǉϾͽ×ȇüѳɔĹƆ~\u0382ʯǎȜĪаɜ°ӇėǺС\x9dʦҩҁҸ',
                                                                            'ŴϿȵҎТnP˵ђ҅ѡʟŀɝ\x8fȫлo\x8dƁʾUŴϟȵŎØĳӔȜ',
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

            'scope': 'debug',

            'messages': [
                {
                    'catalog': 'ҹϋ',
                    'message': 'ˬ',
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
                dict(field_name='error_message', name='Error'),
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
            'identifier': 'ΰˆÏÐʡ7ǪȗєӔđƤˠͰЋWюǂƦƄҩ˘ǨѾпňȍ\x84ҨѲ',
            'categories': [
                'file',
                'network',
                'network',
                'invalid-user-action',
                'network',
                'invalid-user-action',
                'invalid-user-action',
                'os',
                'network',
                'internal',
            ],
            'source': 'Ҹкϓǎ>ʭ_ȓкХǆŴ˩ÍĿˋӿԊɰԭҤϘһˏϫƐӜϟżʔ',
            'corrective_action': {
                'catalog': 'ЫŹ\x98ӻƆηоЂӎǥӷӰLӡҺʑŽǰȑʷθԜ\x9fÖнѯȵԣ҅=',
                'message': 'ÑЌǛ˛ŇЬҕRŐʍáӭŵŘйɈΫʀԉƈѡмԪΈԝǸǪë˓ȯ',
                'arguments': [
                    {
                            'name': 'ȞκӍӱΚĖӘѕƗ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -8732115105398992136,
                                                        8942625456661061121,
                                                        -3025869338713022670,
                                                        -5433815260450417313,
                                                        4063285383854151667,
                                                        8186444335126009287,
                                                        -5098885972617596918,
                                                        -3642750882227420277,
                                                        7262041603562533545,
                                                        8721001676369832453,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ŒЂʮǭӊҖɔʠӅˌȴ\x9bŚíкɢŧΌУ҂ĝ\x93цҕţƚΞґԎˊ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        True,
                                                        False,
                                                        True,
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
                            'name': '\x88ԪȈӧŖӎҗŒĥǆщ4¢ѷƱtsϒːåÜɄҐļӉİʱőėϤ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -5812095378669814420,
                                                        -7535179018269088973,
                                                        2820400264384234696,
                                                        -383763705492430560,
                                                        -2127385868113267105,
                                                        659035644650296488,
                                                        6482855420213288344,
                                                        -7494685946733223615,
                                                        -438361876144447629,
                                                        -422451003901488673,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ȴďπɧ',
                            'value': {
                                        '^': 'float',
                                        '$': 579400.1287411003,
                                    },
                        },
                    {
                            'name': '\x86ʍϩҼӌӄ\x9bƑҺǸ˵)',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ĦҜɹĔҨʛʀɷκьҧ\x94˫ÏÖ˩ƼԋʕÏϭķ҂ήϨTȧʞɅӐ',
                                                        'ɯpȇƀĤǒ˂ӲÔӘƺѰƊ¬\xa0ŶΓƄșӒєɤɑʬГȎ˃]Ìҳ',
                                                        'ΪʘĈÚʒ)ǣƈǱʟǤЕЈ˳ΎӏУý7żϋǁΖϔʇȵȩΕ\x9cˇ',
                                                        'ɲџƮưӫέӎuɼ\\ҥϡШɃm˄Òîѵb˩ǍˎɠǋȳŞѸœψ',
                                                        'ƄƔÓİƽǭҌ\x8d˾ˢǽδçǦ˖;Ή˦˚·ƴɡϠҟкԉƇʼiS',
                                                        'Ŵev\u0378ʴH˘\x97ƒƻͱɠѝ\x93Ԥɨg҆Ӛ ǀĝЁüϥθĢȟџӕ',
                                                        'ˇ_ǠŨɾҥеԙӡƿѐǺťӑ˕ʛΉЛņϭ¨!ӵɓԙľmÄfϩ',
                                                        'd¯ʀ\x8d҄Ŏ§ǠƂȼƹDǃƽˊԨΡϲЏǋ\x9bŋʡʔϗŕÃƗӵό',
                                                        'ʉϬĂqˁʨƅӠ\x87ӑӋϴŲΩѼʨҢϋӪʫŁʽҷƇ\u0381¤ѻƥθ7',
                                                        'ɍώ҂ȾӐʓƺӾŕ;πȵ\x93ѵ¼ӎϬÊТʽȟȵŧûΧ÷¥ȦôȆ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'źĐϢ҆ıʨԝҭ·Ӧȉ^ƂǼ\x89TʇɺϤąȍǐϫҨԎŜĒϭУΪ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -4178961492857235200,
                                                        -6286937438659034752,
                                                        3779152170844347139,
                                                        -7159701903225768805,
                                                        2599903554909714255,
                                                        -926950398957581542,
                                                        -8693549343905574267,
                                                        -1849363200721934926,
                                                        870185557327079422,
                                                        7141633761209902787,
                                                    ],
                                    },
                        },
                    {
                            'name': '҅˒ǐҲӈëĻ\x8bФЧƺ*¡',
                            'value': {
                                        '^': 'int',
                                        '$': 4692987467018734044,
                                    },
                        },
                    {
                            'name': 'AгY\x8cϽŋȃďɵӬƵЧɏԚϻ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ªԚ³ӓЦԛχѕBɆƦɜʌԛƠƢύЀɵɒϳӥҵ+Ʋ¢ĂǐӽӬ',
                                                        'τЏȅԒΘɅӔȍSȲΪơӺѷȚԡëȹŅӧĖӝεÒËýӕ\x84Ӟϵ',
                                                        'ЙϞЬњрϟӪзҩ˖ʦїɗӽҾιӹ,҉\x83nÞˏȏρ³ʠӀŀЁ',
                                                        'ҳĒĎʭёˠèтϵˣ\x9câʂѝµʷˋνӶu×ƇӷŵȍƖӲŘ¢Ę',
                                                        'З\x86єǳО˽g҂ӻʓnϥԫθ˄ʍºЖąˣҔѠpȥĄӽҥҽƌÔ',
                                                        'ĔƆȬχȞũǻѸϡӱƠʛҟԝɅзҸԬƗΙΕwҥȭόϮāʛɨǾ',
                                                        'ȋJϢϬéˀʌǆĮϽƋԡӽ$ӼӶ˽[˧\x92ÆÞɊ§Яǻԑɫԗӈ',
                                                        'ϩԒ҇ʱǄ\x8cʸǩÊ\x8bӴѴšƉ\x88JϣȎȣ˼Ϙ;ʠИЖμӭźçЊ',
                                                        'ҽ˽òiƗǥЅƔͻϚ[ġΝпԆǊzŒώ˛ӛÍȝƳɈɐơĨŃȭ',
                                                        'KŷЏ϶ˤƣ҆˔Ω\u0378ǑϤʶʼ˶ҤʝƯŏƯiϰˍƄÅÑ¯ʱĢˈ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ΥҰХˎԍIƦъ˽ǯIƥÔ´Ϫ7)ȇȨaʐљΔԇŉѱԭǖȑʐ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ưƇψȽ',
                            'value': {
                                        '^': 'int',
                                        '$': -587670351558651960,
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ʢѩЭΌĜԮȻœіȄѷͺʃæŠǿӐΚŹʬćɘпɅ\x9fːſȤϾî',
                'message': 'ɿ)Ǌòıΰ\u0380ϙ¸ÿВԗʩȿȌɉĸƸ\x84ĉ©бʥáРяԔʙEʉ',
                'arguments': [
                    {
                            'name': 'ʹɄɒǙКʜɜȌèʣςϖȗҗɗмϻ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        150704.48923017288,
                                                        796899.6809136303,
                                                        942761.2873758416,
                                                        467875.4648042808,
                                                        812882.2862038151,
                                                        615536.2212886906,
                                                        192151.29193369264,
                                                        465811.3667200897,
                                                        985481.7052631963,
                                                        391039.7424006804,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ԁýŬǩЪѢɭʛ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ŤŅˀ\x88ҌʈҿɤԏСӼŧѝЏʽЕŰƖ˖ʿΫUɼ%ёΡδɆˁ©',
                                                        'П²ӫȏƷсġńƬԋӳóɻϢŌNαƟƧɌ҅ȇɲϧƥѪ˙ɿӸц',
                                                        'ʥˑҘʼѠīȉǈÒυџҟөΧΏ¾Ϙ\u0380ŸƾʯʁâΉ«ºĦlϋŎ',
                                                        "ԫŬ'ɑŜmʘӥҪЈ\x99źȜеϦííŽYNǯϧÇŠϜǏɄԨȜʂ",
                                                        'А҉ǡЉǯȝˁ˨ėʫζԕ˾ʫĠ҇Ĭ˃˟žΗɋԍʄҲљȄǓԎЖ',
                                                        'δďԄˉǟԟȠνCɣΈ˦ΗŰъϛѿiʞŔl%ҫӸÍҚÍˀҷѶ',
                                                        'ӻҴȄ\x9bȑƝĝ·ӷԠǱ˦ɣцΰȆȆҴԨÏŹԂLÄõ·\x7fg\x87Ă',
                                                        'ɜΗźЮʶĔB\x92ɏgĐҤŀЦǆӈѽіȼƇŖǯŗ¶ʘèʒŁԟk',
                                                        '҅õҥΌΐ˟ł\x94ѮƳē\x8bíƐʄƅҢďԎǽЏlѸŧȗЍҭ\x8aӂӡ',
                                                        'ŝRÅBɘӖќχǖ\x8eЙqöǣĭʹüPšһ/ȇāČҮ҃ЏԂCƑ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'LȾϸвƌ®3ЀbɪηɄЎԢ·ЧФϒƺѰȺӊ\x8b9ƂʃŪӖƾǟ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        328373.752465831,
                                                        784931.3211672233,
                                                        9425.921672555254,
                                                        505836.9070160339,
                                                        253651.67916341475,
                                                        804618.7428974112,
                                                        -20122.647897718023,
                                                        420079.89404488413,
                                                        736709.2078020183,
                                                        540232.2114854031,
                                                    ],
                                    },
                        },
                    {
                            'name': '˹чӘJːζ9ԫаɭ˧)ӢҧŅНɑӬßƟʳ\x81Ě҄àʯ0ħgƮ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': '˰Ϣζ·ѝŸ\x93ƦԜɧΗĲԡ¸˚҃ƦˌЃԐԦ˔γ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        True,
                                                        True,
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
                            'name': 'ǙβǻǜњφљЈԏŐ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210206:220932.693594:+0000',
                                                        '20210206:220932.693607:+0000',
                                                        '20210206:220932.693613:+0000',
                                                        '20210206:220932.693618:+0000',
                                                        '20210206:220932.693623:+0000',
                                                        '20210206:220932.693628:+0000',
                                                        '20210206:220932.693633:+0000',
                                                        '20210206:220932.693638:+0000',
                                                        '20210206:220932.693642:+0000',
                                                        '20210206:220932.693647:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ĞýtɽӔԒ˰ʵƀЂϐΩΌ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        False,
                                                        False,
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
                            'name': 'ȥȌБϿʽž˟ʽʄҕñΧɅîѩ\u0383Ô=ӂҸ\x81ɿѸ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ʵďyÐ¤˂ЫĪд҈ҏӄǩǁТJȀē~ȜͰӌ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210206:220932.694299:+0000',
                                                        '20210206:220932.694309:+0000',
                                                        '20210206:220932.694314:+0000',
                                                        '20210206:220932.694318:+0000',
                                                        '20210206:220932.694323:+0000',
                                                        '20210206:220932.694327:+0000',
                                                        '20210206:220932.694331:+0000',
                                                        '20210206:220932.694336:+0000',
                                                        '20210206:220932.694340:+0000',
                                                        '20210206:220932.694344:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ĂőԘ҉ԇЪǪϨҟǮrѾÇʂʙ҃RҟÒӼҊƋΩ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210206:220932.694562:+0000',
                                                        '20210206:220932.694570:+0000',
                                                        '20210206:220932.694575:+0000',
                                                        '20210206:220932.694579:+0000',
                                                        '20210206:220932.694584:+0000',
                                                        '20210206:220932.694588:+0000',
                                                        '20210206:220932.694592:+0000',
                                                        '20210206:220932.694597:+0000',
                                                        '20210206:220932.694601:+0000',
                                                        '20210206:220932.694605:+0000',
                                                    ],
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ŗʸΡҤǰ',

            'categories': [
                'configuration',
            ],

            'error_message': {
                'catalog': 'Ūό',
                'message': 'ȗ',
            },

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
                'identifier': 'ƔȔϿΚğʡӈǅ˘ѤΘѽфΖøӄûğʔ\x8eŸѕΟ;ҩG˥sÒζ',
                'categories': [
                    'network',
                    'file',
                    'access-restriction',
                    'access-restriction',
                    'os',
                    'file',
                    'network',
                    'invalid-user-action',
                    'configuration',
                    'os',
                ],
                'source': 'ϼϪǽÕИ¦άб\x97ϷӗơҦŒӑɶӔǜȦ\x9c˸ɌЫǥˀ\u0382ӹˤԅч',
                'corrective_action': {
                    'catalog': '·ʂы*ŌҜǏĐ\u0381ưŚ\xadг$Ӄ\x93ʡǠÌφĨɃʗǧĬ\x88ˇĞӛQ',
                    'message': 'ǳ=ωWŻûŚƫǖɈҁӽe\u0379Τ§ŨѠз\x93јŻŲˏϔԃӋ2ӢƂ',
                    'arguments': [
                            {
                                        'name': 'T',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'л\x86ēɶȬʄԟűѝƿɘГрĻӜʙ§Ѝźĺ;ơĿѕǇŁƣŁl\x8a',
                                                    },
                                    },
                            {
                                        'name': 'êʅjä˄čʛ˃UҭǂӉʵǧ΅\u0381\x92ɤΎ˻ζɾʌɀþ2Ȉ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220932.683802:+0000',
                                                                            '20210206:220932.683822:+0000',
                                                                            '20210206:220932.683827:+0000',
                                                                            '20210206:220932.683832:+0000',
                                                                            '20210206:220932.683836:+0000',
                                                                            '20210206:220932.683841:+0000',
                                                                            '20210206:220932.683845:+0000',
                                                                            '20210206:220932.683849:+0000',
                                                                            '20210206:220932.683853:+0000',
                                                                            '20210206:220932.683857:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӫ%*ƾѸęϟ˛ŬҎΡΐ˼Ԛ˰ˑϞɏͿǰk\u0380Д~Ź˺ˆџӊŘ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6046254466537093018,
                                                                            -603589894805369164,
                                                                            224200093444397190,
                                                                            1647231259511215420,
                                                                            3932392235504534905,
                                                                            223731111002816677,
                                                                            -5810533246505651889,
                                                                            8357232108501704979,
                                                                            7465728248118318733,
                                                                            -4325040783184131954,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʷҖľšɧюȨπӈӔƹÕћöͰĳτƃǊɆ¤KÒҁȚ\x7fώӧƤц',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220932.684322:+0000',
                                                                            '20210206:220932.684332:+0000',
                                                                            '20210206:220932.684337:+0000',
                                                                            '20210206:220932.684341:+0000',
                                                                            '20210206:220932.684345:+0000',
                                                                            '20210206:220932.684350:+0000',
                                                                            '20210206:220932.684354:+0000',
                                                                            '20210206:220932.684358:+0000',
                                                                            '20210206:220932.684362:+0000',
                                                                            '20210206:220932.684367:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǌɤɝ˛Ӡʞõ˺sͲњǆàʉɨӆǂĜǙϯЎкǡɑαԄЌÇŉȑ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            229278.42247332068,
                                                                            938882.650186948,
                                                                            474611.10811657587,
                                                                            871126.8382984386,
                                                                            137835.60207169157,
                                                                            392512.4264469833,
                                                                            735798.549128602,
                                                                            338362.74812205334,
                                                                            906019.6664464371,
                                                                            971966.2672724305,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҙ Ǯˤ®',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȢǶǰүˋҩȦπųəʿȽϝҚǹùʘϼÉçԆɚʹ\\шĝϳơΫʧ',
                                                                            '´ϋӄ\x99ɖ\x7fČˠӵʑˉɅŪ*ӉӅӸŵŌǩј\x8eͽɠNʼԬ^ӝŘ',
                                                                            'ΉZӣʺӴЁѯҰӨŸɱвĖΕ1ϹɯȁÊǤǵƼK˜Eǜt>ʑӈ',
                                                                            "HǏEƾ˜Ƿǽ\x98όԬзԔ'ʁä҅ΓȥϹʻш˻Ӽӧϱ6Ʒ\u0382×§",
                                                                            ']ωɋ˄Дќҙɤɀϻ¸Ѩԥ1҈яNϊɴȽҌ˫Óˉ°ùɢgɲӔ',
                                                                            'ɼiɪήΕǥәЎʫǽϸϡ\u0379|ǢʛӉƭщƴiʰΫЈҨԙĬҡ\x93ʍ',
                                                                            'Ç|ўҡʪÍƳʝˈҚÀmɗΈłǶŉĐƞȐˇϵʙԥƸЏőӧҍȴ',
                                                                            'ǎҦ\x88ʦэÜʎǎõϷŞȾŗ\x97ȇŖ6˵ʡƶɶÈʞĸƦгŉÏӹñ',
                                                                            'ӊҡʣ˾ћŽύȑɑЏ˱ɬԭɃ\x92ƺ\u038dĭċĽԪρӯLǲ&Ǵǩãŭ',
                                                                            'ѩԙÁȃϷǜǏJ.ѝʊ\u038bɍɹӳƅіǼвʹɌĦλͷŔѧɁʠʓƍ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'L ǧÃЕġѵʥm',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            499497.2079543205,
                                                                            892741.1235638299,
                                                                            250282.9484071433,
                                                                            175931.24460507778,
                                                                            741691.5000506409,
                                                                            600698.5239668825,
                                                                            340483.14015089546,
                                                                            971857.0084676514,
                                                                            382528.54330122273,
                                                                            307787.56195692276,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¹Ğ=ŅǶЯѻ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            466192.8953695836,
                                                                            987817.3998673239,
                                                                            761776.341512777,
                                                                            492642.83081648394,
                                                                            472932.23322521406,
                                                                            -68371.98226600548,
                                                                            225273.50453507836,
                                                                            595093.7086456764,
                                                                            517442.35783077823,
                                                                            744256.1502235038,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'õӇ˶΅ĚǾöЃ˶;8ӫ˖ϘӠ²ĕӖ¬ϏȔȓɹǾțʾ\x97РŢȐ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 80858065918392139,
                                                    },
                                    },
                            {
                                        'name': 'æԉ\u038dєbĒЄļԬӖѬІÐ\x9aκжϸ;ûԚǀБȦǒǼ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 626313.9266253485,
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ǤŻ',
                    'message': 'έȺӟοô?ďӥϳ\x83äźˊáʦȂnӨԂǉƎҲԀϑɬƧĽʣˍс',
                    'arguments': [
                            {
                                        'name': 'ӡһҀи7ŨĨȧϽkӹ˚±ӆΆԔЙɚԙĜɡJˇҴĤӦsƞОə',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӗˊȐѿΛŚǓȚЃƳÃѬɤ×ʽƸǷвǅAΎȀҕҋØϣºƵʩƐ',
                                                                            'žȶ¯ϓόԡǷȦпŘǬԃʅˇȥg\x84ãƾͲƂҲԉƵϢ\x84Ҝąφɥ',
                                                                            'ȬɟϮ#\x80ʼҖԗĆü˒6ʢ4˔ҏ;ѥү\x82υ÷ƏʍɺӵĶǄЀĠ',
                                                                            'Н\u038d\u03a2ʨʩ\x97ZÉԔŪķѾòƭɂ½7ҶɩьѴџʑœѱöϛƦʎϧ',
                                                                            'ŵɤкœˠκÚҏɼȆЃҺȌΧΰεͽʟˣƀŜǿÂʄƹęӺʗFÞ',
                                                                            'є҅ɽӀƊʐɌĻѲǇȢ\x89ɮőʖƁʜHφɆƺV&àÏ\x9a\x87ЃŶФ',
                                                                            'ȣΘǞ@ˏ0ʙƨγʰңѐɯ\x8a58ć>ȞȠVȡƋѥ)ԥs!ˑλ',
                                                                            'ӼIǔ+ϥ\x99eҌý\x96ӃȮʤԧЯ¸όɣ˺Ʌʗȇ¢ɸћ"\x98˳ŨÒ',
                                                                            'Ŀĥђ9ͲЗǶÃȒĄ˱ɁÊ;ӞРƑЭϰi&\u0383Ǝ³ŏȽΪȑF2',
                                                                            'ƾԄɒί΄%ŀΚbѮеʗʢЯҏыɭӎ¬ѬĹВΝ҈ȗɡhƧÕπ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ý҈%ßǆ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ăРÿ`љџ=İɟίǣ\x8dӅŘƵԧʇǗɌ\x8b\xa0κâǜӍ\xadЗЄșĢ',
                                                    },
                                    },
                            {
                                        'name': 'ƣӘЮČ˃НԢ\u038dˊǂˤ˭ʸΌѣbҥҰҢƖ\x89ӈæҮǣα<_ѹξ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5704195053520784457,
                                                                            420820098073501142,
                                                                            -3811813074616172769,
                                                                            -1576297998977765314,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƺĄĨǘŘʒСȠΌ2\x90ÉѥǞĺҥûϼԊԑɯϯČƲAĜʭȚϨ˷',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ęԚ,ǋʋå\x9bïʹԎԝ@ƴϒơĲĄƎ²нłȟ˔ǻϼɚͲɈҸт',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƠԏÓ\x8bȰ1ʌ˼ŦԞȇŏ˔үɤĮB½ϥĲ҅ϼʝќÑπOŁfƏ',
                                                    },
                                    },
                            {
                                        'name': '˽˝ЇˈƇƦƳ§·ɂǊ˶ԑҏĪ$ɫʃĪјŪƈ˹\x8dƵӐʏƜǻӅ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 277699.60225328547,
                                                    },
                                    },
                            {
                                        'name': 'ӭƸǉʰӅ˺¤Đ9ZЇӤƧM\x7fGƉˤƑǜΈҝƨ˵ãыƧʋѫɣ',
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
                                        'name': 'ȎԔȖԠЏþĜ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8887892460197299652,
                                                                            -1834930843001344686,
                                                                            -6902500596708804608,
                                                                            -4567040005756693421,
                                                                            2287433141891848534,
                                                                            -8269726658128287139,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӸΤϘu˦ƜȂɈ\u038dЯƚ8ŮҙFÚԢҎɍĒΟӄnБѺϮɐŵʴ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8888064589794050404,
                                                                            3969982059086586628,
                                                                            -8749221126715852961,
                                                                            1985891324677569169,
                                                                            -1804733908020689489,
                                                                            1924505600981511557,
                                                                            4597099187641505295,
                                                                            8260079073705308181,
                                                                            -6542193381817818954,
                                                                            6310386951863766593,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˆÚмťѭ¡\u0380ҕY\x99ƙԛҦʚˁ!ѵԝʥɪÅȜ}\u0380Ҫζ҅ҘǗ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'error': {
                'identifier': 'xҧԓɘŤ',
                'categories': [
                    'configuration',
                ],
                'error_message': {
                    'catalog': 'Ƌ\x9c',
                    'message': 'ѹ',
                },
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
                'identifier': 'ƥЍό`ζƆ˰Ш\u0383ƜϭӌLơǣƥXßԔԍϒҫǩΦǰ]оĻԛЃ',
                'categories': [
                    'configuration',
                    'file',
                    'configuration',
                    'invalid-user-action',
                    'access-restriction',
                    'os',
                    'file',
                    'file',
                    'os',
                    'os',
                ],
                'source': '˸ïӴΕɊǰΦƉӀЭʏ\x9bǀхTӄűÂÉ9ͽҠѩjƣԭԊɴĂŤ',
                'corrective_action': {
                    'catalog': 'Ų¬ЌƩѕ˯Á¨љ¾ɐҾ=Ɋ҂ɡТßÌιйр\x8aŕÌÎТϕΫϊ',
                    'message': 'ɉԋ\x99ɾƘΔʑɪҺ/їěӨÛРɋ@ŘáƚɛÃȎӖxǤјΑÁЛ',
                    'arguments': [
                            {
                                        'name': 'ӕđ\u038bΚùВрӼ¯ЖпӡжξȤǟϕƼŽϞÄ\x90˸Î¸ӠƘҭг',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            95801.54253020242,
                                                                            993475.2356607125,
                                                                            389533.97539730754,
                                                                            931198.6376627217,
                                                                            451803.07535964623,
                                                                            261648.01165519614,
                                                                            609987.4895699681,
                                                                            139700.66381404558,
                                                                            978004.207538412,
                                                                            427389.6109512509,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȍɜɥэgĩɯέιЮúÿсĥȕèњʽˡҼƊί|ʑ¸ϢѿΎԢӠ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': "īªɨØBʨҶ\xadєCĵώ˒'ЛҤȢԡ¢ɝʞӕ)",
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6080162088465655464,
                                                    },
                                    },
                            {
                                        'name': 'ѐZƶHƽŌƒʫ˥Ҫǻ·˘ɈΟʷԜϒРřԗü',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5561554722128623521,
                                                                            2783935675487592246,
                                                                            8582747398927001812,
                                                                            6589309067420716504,
                                                                            -7522674791898282207,
                                                                            -9021631681586460077,
                                                                            4236847253385632123,
                                                                            6364307635525032019,
                                                                            -3023830683957005139,
                                                                            7665312677483508994,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǵ(ԍӒг˶\x8aҟӐҭýŪҵÜuɇȝʇϯłʛ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220932.696387:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʻиӁϭǪčёɫηҘНɄϓţԭǦƀgnÜǇʋ҈ƺǈɹήǵȢ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3683106323197437446,
                                                    },
                                    },
                            {
                                        'name': 'Ţѣ\x8fÃķĎĤÉѐěâӵɳԌ7ϋǛɦ¾ΞȨǤԍʅӬųȎɻˇ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220932.696679:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ðø\u0378ǵήӄˢċӻ\x86ŢҒȗĀūȸΌʼĞԍұСǌċ\x8bӯˇ£ơ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˀÜǎ҂Ƚ\x98ȤɗĆǠϗƐȭгʹȦɓ¼Ечњ\x84ňɗ2ѾúȫĢЩ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '«ъΞQҬĥƬ˲ʕĪǋ»ƥūͼƺ˞ϊ˅ț˟ԝNȪõεŴKΤÝ',
                                                                            'ōϛΛˈǇÜӘѳ¨ɞ˄ƄӀ\u03a2ɪӾŤҎʑąʅʂȳCÿǍʞ˙Лҭ',
                                                                            'zͷʛŰɋŉъԘҘĕΥ҇řҋĮыύʊƢļÎӞϒŬԉùȳЁɫϮ',
                                                                            'ңюѿÑUԩό˔ñŹ\x8eʘ\x83ȮԖɄ͵ƊmȋşϨa\u0378ѴĹĲȎЇҋ',
                                                                            '÷Ѽ҆т˧ʳ6äʹ˄²ŗӱѮŏԂʊѵϱӲ϶ǈӨˏСʴϓpɕȋ',
                                                                            'τɤԙåԃ(МŰ"ѾR\x7fѯӑүϨͶËԤϭΓ^Р\x81ɠϷƕиЬԋ',
                                                                            "ȟί\xa0ѤɮĩԄÙìЁϗ˜шɧɮėŖĆ'Ơč\x8eŎУҁҵрόщ6",
                                                                            'ơԘԣЀÊLĎɏĩѴӖdɢлχĺμѹƺþčUȧѾȱ\x8aéRòʟ',
                                                                            'ӆKȲ\u038dӳġɸǶϼņˈİəƯүʉːΆȃ˻LŀіëΆʎȟѧıˤ',
                                                                            'ЯɪϞʗôƥӀҒȧԥϿԏMˋӬɿќŐĖÿǉǞĢHіˬўҞɰ£',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԓQΧ˛ӤɊʌèҰŢmȖʣÉϡǧ˸əǗȹӄ˄īџ˰ƌϻTÝȄ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 206192.46114715637,
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ƽҾʥǉɖ\x96ϵʮɢԓäбΓċĄ˗бѦAđjŊùр˟èӕŀûǚ',
                    'message': 'ŵĩŤӮϭԏŹԎηҽǕǃϏʶƹÃƸΝ`ŉЃ/п͵ȷʪϹΆӕ˱',
                    'arguments': [
                            {
                                        'name': '˪ȡɛN˱˵ԚȨщ\x90ЯŔĔβǸ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'эԏBȱƕˍɛʐєʔѧ8ϮɽЁйǒйƋҞмкƠɞѽɺҗɧҷԕ',
                                                    },
                                    },
                            {
                                        'name': 'ÒǣĬɲ(âǝɌKɁƄҝŒĮϓȝˣĞωǢѵηʲӰф',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3164239887640882892,
                                                                            -8122063513197530145,
                                                                            8786094106773940557,
                                                                            -3459911488428917151,
                                                                            -7213647047989520663,
                                                                            5447034170452231233,
                                                                            8925184432399422611,
                                                                            7432218488667579006,
                                                                            7089224812733622706,
                                                                            6196213842886109820,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˰ȠΙǃɿàʵ_ȺđěˮȠ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3407849788778476082,
                                                    },
                                    },
                            {
                                        'name': '͵мˋƇɼǹŊÊdαCЛ\xa0ƚĊɣϞɒȢãŹѥԥćǛƠƹĕxǏ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5145537233771071841,
                                                    },
                                    },
                            {
                                        'name': 'эӚǤ\x8aӵӎČυҔΟȬϽ\u03a2ʍɠµΘРÙάѹ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĠϮˋҺө˧ʛ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220932.698669:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʗ΅¥ѽԋöӗˆ`ͼßƠө͵lƆɎԀýͳǄˤҐӐ\x93ӎɞƛί[',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 11404.205274221618,
                                                    },
                                    },
                            {
                                        'name': 'ɃӮӜӋϨǭӹʭ\x9e҂Ì\x8a˓ϗˋƠϣϞĎѨӱԟ\u0378ԘйȹǻΗ\x9e',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'чйňϢNϭϲȬĐ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "ԑţұˀѻ·ΥHψҾѬӓȭ'Ъӫ˧ΧůgԅҹɎқĎķȄϮÅȺ",
                                                    },
                                    },
                            {
                                        'name': '˫ǊԁĻǸΕĚԅȇϔɪĀʄεǬқɔıӓƤ-ҫɘƉĵɁǵ¤ϳК',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'RˇґǉϚΑР³ǶЮ҅КĬ÷ŰӜдΏӍӍʉӪȶƘÞԧQɢħå',
                                                                            'ĴƳŕŮʀnʡиёȍїȍȋ¡ӐÆĸʣηӱϬ˗ˇѐƺӲʝǨŠӮ',
                                                                            'ƳƿѼӭǩØϋљːÇúаӉД«έҡӢjΧӠҲ.ŧ\x8fǰоſб\x9e',
                                                                            'ҪÏƬћ˾Ϙɝ^ΣԭЄXƾɦғʘǪϏǳӎǌʯУƩϲʕӝʷͺĹ',
                                                                            'ȂGĕҶɞȓǿЖѪӼ(ɗǝ-ϤҧЪģĔΕΔΖþԑɭЧɲǌơл',
                                                                            'ŃƢΘïˍгЌӰΉəȐŞđˠїУÉԇцәųɇsȡ\x94gĢɱŜǃ',
                                                                            'л˝ŇԄËĉƛƮĢöϻѡҺбчħϞ\x87ΦʡϓӛǽĠуˣԥӤҠQ',
                                                                            'ǔÖϼþǾĂǀ\x85<\x8cʏɓӇŒѸǄ\x94ˉ"ϪpǆŃhįĚϾϤΒ·',
                                                                            '҇ȥɢґ\xadűοϧâŜɂѧ˔ȕmʣȢȌԛʇ\x81¶!һþʄԁԌȜʏ',
                                                                            'ҴdϼXѐƄъƠũˬӦɟѸ˯˥;êϒ\u038bҖԨǫ˯Ąɽԇɐˈɼʁ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'user_error': {
                'identifier': 'f҅ƬԧҜ',
                'categories': [
                    'file',
                ],
                'error_message': {
                    'catalog': 'ʵơ',
                    'message': 'ӽ',
                },
            },

        },
    ),
]
