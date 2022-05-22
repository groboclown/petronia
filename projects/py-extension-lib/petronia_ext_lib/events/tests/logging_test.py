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
            '$': 'ηƎҴȇԁԏԩцŇҾ@˾©Ƃƨ\x93ϨɤӨţöǑí˭ӽεԨIүΊ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 9220508248765305083,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 697422.1003506322,
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
            '$': '20220522:173311.075732:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                "ƭǛүƜ'ёɎŇ\u038dѝӫΌļȎëmâŮǛºҺ\x81ˁƃĴǰǃ˅Нƞ",
                'ʈ˶ʏŕʂǽԀȫĠőӿĚ©ãÎҘČҽßӾȼѬˎŐʼǵŝѬǚο',
                'ǡĂӞҽǄҴʨĘ09˅ÅďƛćÆ7ԂβȺèδƀƟӀ˴ǴɨɈу',
                'ıԐřėʹњ\x9dÒί\x84ѪűнѵҫȴIƶԊ·Ǩ/ʯƢ˳\x89ͻǉɦš',
                'сє<ёӑWΆ¿:ːʵΈǜҒ˥ЉТɧЀԆϹϣȼҵïɓěƷ˃ɬ',
                'јҡȔĴķoƬÊɺΆːìʭҵЏϿα˼ǣðǵ˷ϣƓãϱҷ\u03a2ŪѪ',
                'ú_ńƊŻõӵ\u038bcћɅʨԁ˒ϜʁҵСΙɁѺ´ƖўɗѪƯAЬύ',
                'ªХʄљƞҺƳѕˇԜѳʞȣŋɛȶ˅Ȯ\x83\x98\x97Ê;ńњø˛ДКϵ',
                '}ΡѯҧȳžŚʴ¥˶ηȺnҘмб\x9eҾƕв\x95˦rѱxԪɹŸPҬ',
                'ʱ\x86Ƅ\x9cƧbŐÜϋɰαßéɾИͱΠʅʨȡљҭÓЌƾţOюǞă',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                9113750746689750554,
                -5491139847862593521,
                -2011002393278348238,
                -3345150729904729118,
                -7656316054012548176,
                -8109641050487004321,
                -1104811176817357536,
                -2687882521762199776,
                -1481970136801884671,
                8472725569593970230,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                646400.7591622935,
                80198.1527487199,
                220002.26594103867,
                -42259.657554741825,
                326929.04828954296,
                405074.3199187618,
                321460.5888027048,
                78725.5577947121,
                116259.77236540912,
                861771.4020501273,
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
                True,
                True,
                False,
                True,
                False,
                False,
                False,
                True,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
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
            'name': 'ſ\u038bȓĖҶ|',
            'value': {
                '^': 'datetime_list',
                '$': [
                    '20220522:173310.854875:+0000',
                    '20220522:173310.863595:+0000',
                    '20220522:173310.871750:+0000',
                    '20220522:173310.880412:+0000',
                    '20220522:173310.888997:+0000',
                    '20220522:173310.898721:+0000',
                    '20220522:173310.906854:+0000',
                    '20220522:173310.914946:+0000',
                    '20220522:173310.923855:+0000',
                    '20220522:173310.932615:+0000',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ά',

            'value': {
                '^': 'float',
                '$': 630056.6018720828,
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
            'catalog': 'ѐԔĻȮҋŁȑɓӳɖ˴ʡЛӓŕ\u0380ԧӮλŴԆ]ÂʩŕҭҧԙƆĽ',
            'message': 'ɤBЃǆƞӥмΫшϏ,ʑŠ\u038dҦΪMΏ×ǬǓДƙŔΎ5OӘƣʰ',
            'arguments': [
                {
                    'name': 'ΞƖ¨ŇӇ\u0381yǔ͵ЇӓȕȕǶɮӹFВʦԛ',
                    'value': {
                            '^': 'int',
                            '$': 1605911156205101439,
                        },
                },
                {
                    'name': 'ȉȂӿͷʄɠʍ˝ѪkııȈǑΜΊóZǎҷѨѰю~˱ɴĉѳé˛',
                    'value': {
                            '^': 'float',
                            '$': 8694.286922061568,
                        },
                },
                {
                    'name': 'ΓýʦsӦ÷ҋԙӡƢͼϥɵѝɘ\u0381\x7f\u03a2҄ˈʬк\u038bϛύMӱʻǨƂ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        9202920832043313358,
                                        149756357872114628,
                                        -2990747735341005930,
                                        4672733095462892481,
                                        -1143494726000554418,
                                        2008533683254439635,
                                        2927178622784975912,
                                        -7847313590205313862,
                                        6758151476415800435,
                                        -4351918826497825841,
                                    ],
                        },
                },
                {
                    'name': 'űǎőȻȉİͰ\x8dѰϢ\\ҫԟòӧΆĶ¥ɇ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ӤÙȰːŀϔӮ\x99´\u0380ҊZMӵˆȸΔɃ˓ˆN҃ˣăҪҮƋɑӰŕ',
                                        'ҷ$ŀ-ϼʀˬKԘԋźȝģˎ˜Ò_ЮR\x86òŮûȴС\x9dȪ>ӥǍ',
                                        'ϡ ʬ´ΙǾ}җХ£ΌӬɁǷђūӈğĮШХȘNϬ҅ëʱķø˂',
                                        '\x99ѳԇĂ6ǽĎɷFѡңѢȒΓÇҘÌі\x9aҗĐƺͿŌßɋ\x81ӵɚƛ',
                                        'ҥ˲ƒõα|ϱӛԮ˕\x85Ҥ\x82ԌȷӫǰҖQǔãң҅ƓϑśѭĚьƀ',
                                        'ѻ˻ҡƲ0ǶHÌRҽ¯˥ŏʌІəӼŢɀƊȷʒ\x99ˠҰŔƦ\x80rŨ',
                                        '¿ѥҩʱԢҲéātȖĆ\x92%ǧȗӞ#³ǂҘЂȊ˂Цӧ\xadѫȻ˒Ӽ',
                                        'ҍĹđӥҿҺѤҩѠȰêȘƝӁƘ˟`ɋяƨ҄˩ѴѲωέҠƁɮÌ',
                                        'Ӵƭӭ˅ƳΈҌίԮφζƁæȏѓřЋ>įťρӗrʵ\x9a ȥ ʦ½',
                                        'Ȼ<Gxќģ^ѝĮǃ\xa0ƈĜϨжӢԉßшǲϩɊȑHĞĦɁ_ƾÆ',
                                    ],
                        },
                },
                {
                    'name': 'ʋмĬдѫ:ӱр¥ʀ¥ӎҀɴҳ\x8eԬϾVǫÉ-À҅ΐÉΟíɜй',
                    'value': {
                            '^': 'float',
                            '$': 856562.2568245496,
                        },
                },
                {
                    'name': 'ƺΓƗԢǀȤƢњɽыʹτϕӊÆǿnĆĴНΡÝδɶǦľ\x85ɞѿ\x9d',
                    'value': {
                            '^': 'datetime',
                            '$': '20220522:173310.628187:+0000',
                        },
                },
                {
                    'name': 'к˵ϋ˞Эƌ˴ǸăǐӼǜ˒qńqƵǱŧϑɫҰǌ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': '\x8c ͶЁìӪѿèƩŗώYȓ˔Ļ',
                    'value': {
                            '^': 'float',
                            '$': 268958.14624754066,
                        },
                },
                {
                    'name': 'ȠćȫҀ˦\x8bԪͽ\u038dɦŹϒǱvƈ·˷ыΑԪŦ^fŽґ]Ҙ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ɕԤƹʔ·pθǦĔÏŮƖňбƣѝ͵Ö\x8aƠΉϰˤeƑǍС',
                    'value': {
                            '^': 'float',
                            '$': 891157.2839817252,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ǭ˧',

            'message': 'Ч',

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
            'scope': 'debug',
            'messages': [
                {
                    'catalog': '˼Ƀɚȁ',
                    'message': '\x7fпԏњТj±ȷʲ\x93ϱԤȵ\x9fvԂíŭťƥiɪ¥½ǬϺɖԀ¤Ϲ',
                    'arguments': [
                            {
                                        'name': 'гÛϊVưɄbº˟Ӯ#ğȭΉϷɨũűëʯЪԁȥοӨŲ˦σȣ\x8b',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "рҿӇςǋӄϰӚԦ˙ϩńԓ'ӁǹԢфЍѥxђĤRϸŚ҈YÝ\x99",
                                                    },
                                    },
                            {
                                        'name': 'Ⱦ.Ԍιғԗ½ζӾȵАѶǓˎƬѤMЋóɫ˅',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǢĜ1ʟЗˍĄ΄ƫÓҠÑйÄъϋǴԣ˃șμ>ßˀhǡǛűyў',
                                                    },
                                    },
                            {
                                        'name': '0:Ӯ`҃\x8aȲ]ηѣŚԉ΅Ѿӊ|lÒуȶiƕбЧöн&ʚњϿ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'żФǅҔʄȽϫƧ˷ŻˑƑӇȕŅϊǆҥиŕÛϙƪӍұʭǇʎԎ\u038b',
                                                                            '˃ԖаŮѱȅЩÆƍǦǺ\x8fȒȖϰǂëͼӎƋτΘӅK\x9cĺӇuǅG',
                                                                            'ϊǖȵϓĲȌʀƏ\x9fцÄѪϬ{ɑėѸƖȃЋҡ/ҖŝԃſǤǉǝ_',
                                                                            'µhѹȭƃϒɽȷЩƜϥɦɢƚʳѨƵĎŗ\x90ʜˇ/ԨɢЕÆΐȣ!',
                                                                            'ȨЬ\x9fЋǰǌŹ$ΩКJϭмŧʼΌѝɻ\x8dӅțѥ\u0378ҭȭȌҲϔô#',
                                                                            'ϭĶʦˌ²˰¼LҫӪXˊǃšΓ\x83ȀƯчVȫ=ҾƜøϵѿǕ\x80Đ',
                                                                            'ǓQnːΏȔʲɶŎӌʍϪӝт˗óʁƈҾʹцΗϬѝЌͽȤƧӷц',
                                                                            'ŻӗӱčÕǔȯ0ČtƮ\xadϲĳ\x9dΨӟȪȥǂǼӂ\u03792ҊΆ=РʛѺ',
                                                                            'ǑϨéLŞɻΟӝƌҦĲÒ˜ʥӵƘҸƢĎӈϣңЪҫªĠêҮЅƤ',
                                                                            '©Ьγÿ(EҎǃȒӔԒ˼ƺ҉Ġ\x98\x9aċÒˍϙøŔƿжÄƩĲӵ7',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĔȃȯƇѽϰȤƁЁ1іʯΟɵ˕«ɅɳrЌɞʷƽӀi҄',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173303.539196:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҋÛλҠ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'έǾӆҸŶώȖäӭωğʿoåǰ\x8fńҖдϾäҐӊƦˎǟ1ɋCϡ',
                                                                            'ɃͽǔɰĩwΤԉɶ\x80а\x83ЦҔ_ƠҁЬ.JĈηïʯвb˝ӨґE',
                                                                            'ʎÖĀȘ»ЯЉ\x7fГ˜ŹϊÝþϑOďɴʤъƿɉϷϚÖνĦʉӃũ',
                                                                            'ɶνҞ¸ύCɣǭƁΪŝʐPˊʙĦѫķɋςЍγϲǤ҆ÙAǄπĕ',
                                                                            'rГ˕.ɽ˽ĊȝӻϟgŮдЮҕɔ\x9cIƅЖȁԝʭɟĮŖ=ʲʟγ',
                                                                            'ɄɰѧŹɵӰѱùɏҒɲԅχӽɹ^жѴÍЎŬėˁ˜ΚķRƫɈʝ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԫύѡФΎЁ.ƧŪѤĈa˰όҵҲľĚȆˮξǍԒѲƋЬũЭѰν',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ǒή˫юӪ΅ ΒǌҦϋʷӦĳǆ˜˪ŢӧƅʊѬ`˝^e˘Μ=ű',
                                                                            'pȇӇáűӨ·ѧ΅ȲϠČ¨ǈŮʷѣƵʄʟɒΟѰùԙҸǞŌ˃Ι',
                                                                            'йЅͲʹȑǏΆҔ˒ȦfϨƆôЗşȝƨϢǹ˷ψƉ\x8aÖ.Ŭɞǃȳ',
                                                                            'ϖĚӛфÙ˭ЕӢčԞŧűϾ-ʴpиҭɏ^ΎљѬӄƀˏбɀɚł',
                                                                            'ņҥ˷ʚʣ\x89Ù\x9dɰǜāԌϙ|ͽƲ˂ϰӁ\x94ʿ&ΊƶÉȠȺŇÅʏ',
                                                                            'ƪюĪӭҘɅҘǊʊɫAˬӘŤΰðǎǨˏЏɌӎѷ¹ӈǎɵѸЇƸ',
                                                                            'ǵ+ƻѓщЧЋ,ťϼЊԐňюɝҹģǷˏҏŬxѹҾΫŠҝԖMϡ',
                                                                            'ʭȘӂʥȶѦƞЃ҈˱ĺϕӇӧЦɅΕ?Ŏ»ǔ¶ҏĂƄμΗԦĦ˫',
                                                                            'ЄΓвӜҮңʙ)ԖȴĽѷåǝsɃўÏ(кҌNϷʠǬ˘Ȼӡȁʨ',
                                                                            '˂ҷϬӊÌtɼкǜKƺ˱ǶψɯͷǥȏԏӚpõөӼǡςθˌйά',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "įȾΖһӂѓƽ\x91ĸȇȼ÷ϓđä\x83ťƾϯȂ>˕ԝѝ'˞дɦ˵Ԣ",
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': "ȳΌҰɪjħʊϖӉӗįѾșϸǾ'ýɝɆƦҀ4ɊɄӬÑż{ҽù",
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7767995669049045856,
                                                    },
                                    },
                            {
                                        'name': 'ϭӃӞmƂʥŔмşӴ˛śɏСŽ&ԔʁеŔύĬĚȌ2ʈϮѼҁ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɫɴżџǐǷƐήӞ\x98юȫ\x86ԋůӎȃҏφҾϟџөƁǲʿɯwƳŉ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            9098858389043371381,
                                                                            7537279550603485855,
                                                                            -9168717265049560582,
                                                                            1727729015740557931,
                                                                            -17547785306439618,
                                                                            1495145030479078081,
                                                                            -2489814808186762322,
                                                                            -1971843559328735945,
                                                                            3616590361819092875,
                                                                            8746516883057555443,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x85҃KŒԩĖӋʄʆϹŎʫÀɹ҅ΝȐÅʹãGɨȘЩɁȩÖ²łφ',
                    'message': 'ƎԋбǲƥϬέüбΡкʏ˦ɝңʸÐ\x81ØЏɈȧö˳ԚаŤӊÎʩ',
                    'arguments': [
                            {
                                        'name': 'књШʊĬƓѧҎƒϿ˾ЦɟɣQ\\ʢ¾Ƹ½ŏ8ʤcħɒ}ʟnʿ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʎʧÏϿӄқϺɀҬƘȧ3ͽҐϮπӵҹϽ"ɇХЖōsόʄϜǖɶ',
                                                    },
                                    },
                            {
                                        'name': "ɆʀʾõԟƴϮóӺÏ'ť˜ìPӛϿϲЖ5ӕѺžϊʆûн΅Йǆ",
                                        'value': {
                                                        '^': 'int',
                                                        '$': 897818363697802151,
                                                    },
                                    },
                            {
                                        'name': 'ǚΝɟԊ^ÎϏAãХӴɣжЋb4ǐŰǠȀєЙѪ\u0380˒ԔӦ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'tӪH$ԐŧӢӔĬŪԒΙňāÂȀlâɜƴǙҩҹЊϝԠƤЗ\x85Ɯ',
                                                                            'ɥѣжȽþёȜҋȼґįłҳӣQ®ϭÈͿŠɎԕąˬɑ˵¼ÕҪ\x8e',
                                                                            'ĲҢˮʘÉʖʢųÄӍŲȚȷ˸Ж·Ȯ|љöĠÍԠżōԡЖ×ʄǻ',
                                                                            'ȃΘԙŞȗǸ5İɻʀʥ?ʫƺӞœIԄ2ɾĂɳčŶӃƥŅʆįђ',
                                                                            'ЍρȠΓŷɳ˪ŀɰжҿɎϻΜҶčıÂȠŐɲǙԬϣÀǐȢŒĻʋ',
                                                                            'тҬјӚ\x8aƶɯ\xad\x9eģʊΑƘ\x85û©ȣƒ\\ˁĥˁ˦¿d΄¯ȡӴʗ',
                                                                            'íǎ¼ĔҊ¿ŊϮϤǕƫӹΤГɭѬӣĶ©\x80ԭ*ŮҘϭƕѮåʶҥ',
                                                                            'ԦƋˁμĞҝцˑӄŦȋǟԀţȻԠ˕ҡľі½ƻԉҺǍǵ\x98ăėâ',
                                                                            'ȹͽE{ơ˛ȃԢżάɫӆƦǀȲÓӀєȉԮĐпӤѱŪƴґ+ўϜ',
                                                                            'шψɡ½ŞӔΨѨѬϐǆĜïȤԝ6ʌʹvϤÀѻӞӜӥΧ¦гԣԂ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƅѱʀ+Ӗǉɽʫ˃ɈßʤϽʜΠìЙʺϐ?ĆѦǜҡҾ\u038bӈǨӅ˾',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173304.331740:+0000',
                                                                            '20220522:173304.340546:+0000',
                                                                            '20220522:173304.348293:+0000',
                                                                            '20220522:173304.357387:+0000',
                                                                            '20220522:173304.366836:+0000',
                                                                            '20220522:173304.374834:+0000',
                                                                            '20220522:173304.383275:+0000',
                                                                            '20220522:173304.391994:+0000',
                                                                            '20220522:173304.400350:+0000',
                                                                            '20220522:173304.409391:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ə|ȜȹƳƑЛ;ԦɘЈѷƝĂ2ȩ˔ɓɊɬȎΧǺѡ҆ǞʐƎӄǖ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            141613.89275767616,
                                                                            299719.7268266819,
                                                                            116968.95253495619,
                                                                            462132.86636760645,
                                                                            711231.4961985464,
                                                                            665774.7628733957,
                                                                            632588.4321651324,
                                                                            363182.68376062205,
                                                                            215544.16270280158,
                                                                            352024.17183423165,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʪΡlϲƖ\x91ǵú͵ɜĸҎԕϏòȀđĆĩ\x80\u03a2ºʄǺƗʀ\u0381nlȮ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 561031.6717836409,
                                                    },
                                    },
                            {
                                        'name': 'Ӓњ,ȟǹѮǕӵ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 491144.52326979255,
                                                    },
                                    },
                            {
                                        'name': 'ƍɪёЬĞɸϱɶͿ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 745665.8855658197,
                                                    },
                                    },
                            {
                                        'name': 'TUwʾҋϦƋͱƻͰ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʇϏǗŒʯ¨ūʶВɾϽɁеƼÊ)Ƌ˗яȧěˊėԑǷVϩţƹ\x87',
                                                    },
                                    },
                            {
                                        'name': 'ӟ˼β',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5613442946405135377,
                                                                            -4426607433110773974,
                                                                            7914449434528989631,
                                                                            175472400872442869,
                                                                            1518799557734076844,
                                                                            343095992347517022,
                                                                            -5110239025053266488,
                                                                            7688899481674664358,
                                                                            -5771773284876689656,
                                                                            -5560587090688199143,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'є\x8fȭʢиԛӥЛрŴǇӻАɤ\x9fɵԕʱ\x9f\x7fӲI˝Ў΄ˮȏƄʓҢ',
                    'message': '#ýˮʉǳƂӝУӁʶԏ˗ˀÁĠɜŢPǛӃʹϪ¢ʍ¼Ԑ¹ĂŐ{',
                    'arguments': [
                            {
                                        'name': 'ȌмȍлĀƌ˞˫Ӕ÷ӹрÏʛ',
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
                                        'name': 'ǛӖ²\u0382ʑGÀ|Ө˚ϘӜØ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԈюɦӦŝеƂƗƈʆӃǨШ¥ԀɅǑǝҩÞ˹¦bƁͱqĕϑϠʆ',
                                                                            'єӠȕƲˆԬǈɸҨţŴʪѝčћ\x81ӹԮ2ю[ÚϰΐƗNыŠyӋ',
                                                                            'ƬάϼĵŮƤƝҬȖзϹȫ\u0378Ɨǭ\xa0Ǣɢ¢Ͽӻɝ1Ѽ˫ǱˇùE\x95',
                                                                            'ɛʻȰϐŒΗǵҊǤŬҷJlƚϨóˤǁЍ»ǛΖеϥʡ҆ŻбԔı',
                                                                            'ž·ÈİЭ¥ʖľʛƠɨї*ѕä\x90ӑ˸tŞÕ˄ӹǰɻʘуɪȽӿ',
                                                                            'ϏӫώҝԇȡĆϯӐϔцǹ;ɤşƘĄʂĎγȎǳɱЩǁ%ȩ\x86ԅƙ',
                                                                            'α\xa0ΰȸȴ҉ɵĠňМ¸ɫȡʤÉԘģˁΓөŤ_ΌƿêТɛ¾üǇ',
                                                                            'ΪżăҎ\x9aˇE$ɹбǂĄʘàħŐƈƖŦӂΌ5ĥĀ˅ͷӺZԓ7',
                                                                            'ƋϽǽʇҎѦғǊΊÌѮƞԈ\x99ʝш\u0379GŅÔ\x9c/ӶԘˌ\x8aʎſͳҼ',
                                                                            'ɠˑѫ%\x80\xadȥӟ=ɆѥŏόЃӗˉȬΤʬʈѡ)ҕҗĒҷǷЧĴŉ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǆҧϻɦ¹ϋƴŒȈǰŹĥ˗CȜ\u0383ϼԮ҆Ѻ\x81ӣѹ',
                                        'value': {
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
                                    },
                            {
                                        'name': 'ˤǽȭˮҖҍČǯ"ǞˋӞѳɚҗ±ƖʚӐϙĿƍʻҗs¸хЕɣ\x95',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϮÄͿɿǗƗ$ņчʕмʥΚβǰҕƴɄШʦĪҷϱЏϾʸǦ˩ΊŲ',
                                                    },
                                    },
                            {
                                        'name': 'ʙΆҚú҇ĔЦ˩Ҩҝȹǜ˝ȚϴGѬőβȎӭԪԫĜǧđɥӳ΄҆',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173305.278438:+0000',
                                                                            '20220522:173305.286473:+0000',
                                                                            '20220522:173305.295969:+0000',
                                                                            '20220522:173305.305388:+0000',
                                                                            '20220522:173305.313599:+0000',
                                                                            '20220522:173305.322322:+0000',
                                                                            '20220522:173305.331059:+0000',
                                                                            '20220522:173305.338777:+0000',
                                                                            '20220522:173305.347920:+0000',
                                                                            '20220522:173305.356116:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѩοȼ\u038bϩƼѝ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'bƖÇYӼǦɗ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'БõżóƺʏȲҝɃÜ²өłѢŁąĚњƐ\x98ŨҟϏƻɼі\x90œÉ(',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173305.556608:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϲҭƏȡɌΖŊ\x93ϷŮöʆѣГːƲɀ¸ġɆӐˣʴ\x96ͶЈ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173305.592381:+0000',
                                                                            '20220522:173305.600988:+0000',
                                                                            '20220522:173305.608912:+0000',
                                                                            '20220522:173305.616802:+0000',
                                                                            '20220522:173305.625061:+0000',
                                                                            '20220522:173305.633873:+0000',
                                                                            '20220522:173305.642439:+0000',
                                                                            '20220522:173305.650842:+0000',
                                                                            '20220522:173305.659815:+0000',
                                                                            '20220522:173305.669129:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ƃȩ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4653063053875139640,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƺɠѵΗŅșϭŰѾơÁӉОќϪԧÛԡάʥζǪƮɘĹ\x91ʓ7ˮȭ',
                    'message': ':ĎкĺǙ\u03a2ȞʋъҚĭeөrHȡǤϻӕәӦЄԁTǎҁε˕ƅу',
                    'arguments': [
                            {
                                        'name': 'ӵю+¬Ηʃ·Ɂϝ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6646735366775386463,
                                                                            -8885839476130707355,
                                                                            995830039545487986,
                                                                            6759546329911875677,
                                                                            6604418038131994979,
                                                                            17237253778314785,
                                                                            -486258599049211759,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȶÜ\x87ǭȋˣʄЁ͵ӼǙԍǰήÜӾɾŝƉήғӈѦ}Λ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            459796.75348733587,
                                                                            320462.7082672018,
                                                                            285296.0726019055,
                                                                            493195.9754875407,
                                                                            443390.67602808145,
                                                                            557015.2385448338,
                                                                            720643.0828136934,
                                                                            156114.69650292306,
                                                                            745391.3991328201,
                                                                            738865.2406128489,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŬηӚł\x83ôøϏŝѨɅɫǞŞȏΪʭ˪ˊ\x8fѭÑȍАǩʏжѢŨѡ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1836820316671333861,
                                                    },
                                    },
                            {
                                        'name': 'bϳԇ˼\x9aƿHńȖԍǻƟHtЙҔӊàǔ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173306.033624:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΣϛùҔéԗÈ)',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173306.070188:+0000',
                                                    },
                                    },
                            {
                                        'name': "ЕО'ЊҞˊǭɨʧ¯˃ȡɥђ\x93ӫѥӮƓʱĥwǒƕŤЖPПЧМ",
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6711568442826844092,
                                                    },
                                    },
                            {
                                        'name': 'ȃʵ\x84ѬɚЗʏҬŦłЋԔʅɢĻ=\x9cйϯoцʾÍɭÕpƮŕt\x9a',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            704667.8011622152,
                                                                            599864.251697885,
                                                                            118719.30378532497,
                                                                            297754.44746998,
                                                                            466134.5745106612,
                                                                            437191.07410247216,
                                                                            133105.17089649994,
                                                                            925595.0199854219,
                                                                            96238.54280389231,
                                                                            993855.4171356307,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'δÚϪƩîʡэУЯʟ_ӕʒċɹΓΣЇѓҨƊŒéӏê',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2681007376110439218,
                                                                            4400774127276023696,
                                                                            2251277178145387673,
                                                                            -4671872604133297088,
                                                                            -1247162198516394828,
                                                                            1835720931498554552,
                                                                            -3954281876592874857,
                                                                            -8560356948407246212,
                                                                            -3263613569107704736,
                                                                            -9202525897430516869,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŊǓɌȶûҒԌҰˀ˺±ČӎΜ\u0379½ԛѪǜчҥ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϜˉɭÐ6ĮϟɢĻТ°ȼǪǓįѸѱѹ_ҋţІҠӄ\x88ЇӍҤͿÂ',
                                                                            'Ǜď°ªʏӊĆШЦaӠʢω˵ĩĠӆƥҶѓ˃KÛʝêΐƈ҄\x88Ȃ',
                                                                            'ŗЙ|ԏŁɜϦĭġɔ>шԞúҵǢғ»ÛѶΉ˘Ȇ˽ûͽ¤ɘĻѥ',
                                                                            'ςаѧϜ\\шυɐ½ǥʒŻѨ¾Ӡ\x9fϘôŀŚҺ9ͼʅĮǮЄłѫΤ',
                                                                            'ȤŢŲΜŽÄĢΚә˽ŚǐЄçХѐƳʖ³\x89їŦrϛΤʹģƊԣЄ',
                                                                            'Ӣɵ˕ɝØЀ)ƆϐŚΏӸӇԪџЁѪҙɪƍǾįŞɀɎʬ«ɸ|ԣ',
                                                                            'ΊȒԕ°ȈœͽʫƼɶƌҊʠР˃Ʋơ±ҬϿĞАȈҙʊϏȳ\u0383àΐ',
                                                                            'ӣHȗӭ\u0383уɼмeӝûҢY××Źάɴ\x9bɴʓ˰1ȷˌĉŧƮȶȴ',
                                                                            '7҄ȿyŔʭåњʹIŭΕ҃ӾӏÇԗɳðЧΎȩӹӰ\x8cɛ!ÿ˜ȏ',
                                                                            'Öǐ9Фԁ^ǆЗ@˱όĚӞ÷Ќˁ\xa0¹ȥʅƘ\u0381ïӸ~Ǡͳʒӻ¨',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȝ®ŃϰƟȪFKΰȽӰςϔ6Нɍɔ҂еɑm˦αϞԡñ×ʳčҦ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173306.497363:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ƭ˵ÎҒДbĵЂ°ƴѠҴȅԍŨØӰ2ȯ˨ȺƂ\x89о¨ɅʼÍƨҿ',
                    'message': 'ĨȵǏ\x7fĶŸ¿ӫԧΑͰƖ%ʀɛΗεǞäП°ҶǀĤӔŗЄȓɧȍ',
                    'arguments': [
                            {
                                        'name': 'ҝòÛͺ\u0383é¨рɍяƟĄҋœ@A˲җӊƅƷVȵԞύϩϘĴ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173306.564262:+0000',
                                                                            '20220522:173306.573096:+0000',
                                                                            '20220522:173306.582492:+0000',
                                                                            '20220522:173306.591488:+0000',
                                                                            '20220522:173306.600498:+0000',
                                                                            '20220522:173306.609750:+0000',
                                                                            '20220522:173306.618466:+0000',
                                                                            '20220522:173306.626334:+0000',
                                                                            '20220522:173306.633778:+0000',
                                                                            '20220522:173306.641578:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƭǀʹͷˈľöăХҔȼ˺ҧȃѦЛϭŨŦɃϏԥЋə҆ŢΌϟ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ÓѼϓȇǞхӒβČɥĤřýЉˑΈʪġʸѫӧ´ù˅',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȱĳσɿϨ\x85ȖΐGхʭ˶ςŨğpӇ\x97ˇ˅ɑϜΑǿѠĹьѐ%ȩ',
                                                                            'űɩĚű>Ԥ҉;qɏ=Ę-ѕͷ¡ʮĖĦÚ¥ ϊϸʺԉþļǜŚ',
                                                                            "|ʩ#άëԜɏξɚЕȖƪǄ'ӦЭ˸ҚOϓӫǏ\x8bѲѼӧÒĂÞ\\",
                                                                            'ˢųХϞͻķҏћǠҹˮĽ!ˀǍΘǑʶЛyӹȜͱйǬîhȥǂˑ',
                                                                            'ˏǨ9\x99ЛϽǑЗΡʐϮƨšԑ\x8eцӡШқѠǔåϮ\u0381ԑдɁʈʥѳ',
                                                                            'ƖʎӢȳĸмΗˁΤǠъêͲ˞ǹΉ˓ÿŉûƞ+ëǒÓϋĻþ҇Ζ',
                                                                            'Ѷ+Οʕ˦ŖдҭлԌϔͰϱΐӱ¹ǁʍӐҼíŒЫ·ϪţȪĆБѾ',
                                                                            'ѻ¼ӽ©ԮÉРЄϕG҃Ң\\ɶČʞǣϋıѭ˻ѡȜԏΔҜſЂƻԩ',
                                                                            'ŲЈΙЛіηяҩ˫ȰƵˡҪƥԁ\u0380ɹΪɮɚңQ)ɘʈŖγʭϊō',
                                                                            'ȦĪȢӈѨÅǢԬƆʿЭжԩϦӍӻƻȿԃĀĨӯ˘2ǡԈΈӲʢĝ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӣű\x98шłϳǗзөӌϯǟ˾ɷӝ±ƄgœϼáʼфΒмĖȰĄæŐ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173306.841577:+0000',
                                                                            '20220522:173306.849923:+0000',
                                                                            '20220522:173306.855672:+0000',
                                                                            '20220522:173306.861626:+0000',
                                                                            '20220522:173306.867364:+0000',
                                                                            '20220522:173306.873411:+0000',
                                                                            '20220522:173306.879148:+0000',
                                                                            '20220522:173306.884908:+0000',
                                                                            '20220522:173306.890865:+0000',
                                                                            '20220522:173306.896552:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӿï^˴οѣԀˈñШMƧˀzԎ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ƻÜϺPҿг0\x88¯ё\u0380ԎͼʻџĐȠƗɺЉδԄҾȧ¯˶ϥ¡ŎŜ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173306.948910:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ԁӝʿԅ˟ȌƟϫ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'ϥhɘ˃ӰǌБĉɻΕǄģɨϽ\x81ʪ|ʒ5Ǵ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 137430.46347621366,
                                                    },
                                    },
                            {
                                        'name': '\u0381˗ɳɤҘŉȠƎ',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΉȸӁțˌϓ\x8eïɁɺВΦȪϽҾѢ\x8eˬџˎ˲Ԧ»іȫȳкƜPϮ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
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
                        ],
                },
                {
                    'catalog': ",ǚɬХψÄ'ЯŵƠӳɔɀĠ\x8cҐЀʨώ˕ҎƔ:ŮƻÀnсѲ*",
                    'message': 'ȳɒƠǒҝcĺͺˣ˗Ôƕʇ\x85ȡĆzԦōɕE°Ўʥѿ6ҿ\x8f,Ǧ',
                    'arguments': [
                            {
                                        'name': 'ɩ·ňеȬʸ˝˥ϛØΛW˧ǏǄŕіDǻAɃȹt\x81ԫѹκɓ¸β',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʋǫŞң\x8cӁΥˣĆӌƂӀĊǲƾԅǃӫѰʽЃUęӍɾͶīáͱŶ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7616826581562489507,
                                                    },
                                    },
                            {
                                        'name': 'ȃҧƤЁɪ!˼˧ĳЌӠ˳ιǘΧoѿ҄ɵҢþЧćŞϥúÉԢ˽\x9d',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƫɍ\x9bԃ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7396474534257748830,
                                                                            9213403662321249706,
                                                                            8327291529688027674,
                                                                            6417262960241530823,
                                                                            -7338634522770044926,
                                                                            2592675481135214640,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɱˌΚȣ\x9eԌά',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173307.391244:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĬʏƘάɯ˖\x9bÄǬ˴ɣҟЌǁж¡ŅÃƎνüԩΔJZԉɃʘƜҨ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173307.414409:+0000',
                                                                            '20220522:173307.420149:+0000',
                                                                            '20220522:173307.426050:+0000',
                                                                            '20220522:173307.431761:+0000',
                                                                            '20220522:173307.437367:+0000',
                                                                            '20220522:173307.443331:+0000',
                                                                            '20220522:173307.449277:+0000',
                                                                            '20220522:173307.454899:+0000',
                                                                            '20220522:173307.460856:+0000',
                                                                            '20220522:173307.466757:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȸ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6242442609212178770,
                                                    },
                                    },
                            {
                                        'name': 'ZӸȟͻԆƕǞʰ.ĹϳëȓѠǛΟԒī7ЙХϸɑӥҝԧɇӷ\x92j',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8245504563493259602,
                                                    },
                                    },
                            {
                                        'name': '½ԫϪØѴçВǇƾ!ƏjŰ˹ϥɿɑӹǼ\x97юJѯĦŝԕ_Ϯ×ϯ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1695140021992495756,
                                                    },
                                    },
                            {
                                        'name': 'ſΦȺÄԇ7ЀѴǛьύ¡ϟтŵΈŬӷxȄǾӜǋʚǒȝĶʧUū',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ЌҨƳ˅ŷÃŨр˅ъ°tǢɖ¤Îɧøԇǂ\x7fˀЂŁËȃ]ϛԐª',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'іʥ˃ρм2ҏŐ¢ҬΟќжԏąѬǍʒ½ɩİ˹ԗҵ˪Ϡŵôġ\u0378',
                    'message': 'σȥΧf*Œ`Ǖīϔ/ɽʨ~ĉ\\ūnŁʚ°XΡδԜČ»×ӈƛ',
                    'arguments': [
                            {
                                        'name': 'ǟқҟĥ\x84ʳ\x83ÙƬɩǭÝȑ\x9aϵØɽ΄ǖћ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 854246.541143948,
                                                    },
                                    },
                            {
                                        'name': "ƽÛÆ\u0380ΐȟ'ӧҬԈɋҎĽȺΩüɭǃĖҪÿӮȇS˞ǅҩϾ",
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            473240.8473095086,
                                                                            53835.07383032938,
                                                                            -90091.28363188641,
                                                                            849029.6763697478,
                                                                            446481.09229655867,
                                                                            -90393.31269974622,
                                                                            628827.2486900403,
                                                                            338284.9379681627,
                                                                            326151.23921109975,
                                                                            601405.9042351451,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѓƜŋчǤʮʘ=.ԟԝΤƤ˕\x80ӎzɿͰЈμĔ ԘƵǱԚ"ˬ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3074001989730055264,
                                                    },
                                    },
                            {
                                        'name': 'AǸȿĬĖÿͲȶɡǎǰ\x86ӛѣѡпҏҲˉŝĪ¸h˵҄òѦεχϔ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '¾ԛΈΦĘ\x8bĝəЪǊшҧӦχҥӟˈŋuƭԫЃԨŒʣƜīлɮρ',
                                                    },
                                    },
                            {
                                        'name': 'ΪǆϦȂǔҸ˃ɈοЃԦСpȲķŋԏ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǯ_϶ϖԥ\u0382ґȁҰŹCϢ³ҺŵcνIәñʔʰґʩң§\u0382ĭ9Ŷ',
                                                                            'ӟôЌ˯ќytǃѐҘf͵Ůʶͷ҆˂ΟǶӁďęқƇаÊЁθӌ\u0379',
                                                                            'ХƟ?ӺπɲɭȵєĬkϦϬbɞĂȠ˯ͶӄľŋХÖà¤ΐϗčΙ',
                                                                            'ϔԞfƆÊƼɪοʣϭԗơϱπ˸eʆƬàŕҕʩëOÝǡεΟ^ˣ',
                                                                            'ŮВƠŋԪƔɴϐӓǸɗŗԎLțƕƪǵȯҷѝӈɦXÐΚԃ,Ȥα',
                                                                            'ʢУŒɡѯʳűÆȩԟȭˬЍyѨӟ(ʩЪȡˈĜ\x86ʂɽƔό˫ƾȌ',
                                                                            'ǛʹÍԭrlþàҚϟӣʔҫ¶ȶ.ќǣΐàϰεƮŉʹͿьǞЃ҆',
                                                                            'ʧӜѭӏȃѤЈŔʄǘ\x90gѸ\x97ƫɲʡǅĠпӚŰϚ\u03a2ύ\x8bŕǼN\x83',
                                                                            'ѨýǴÄјŨԄĒǛΘŭ\x9cӫӊͱȆԨӠϓǗήˈǶԘʻ\x9eѺӌǵϛ',
                                                                            'ԜԇŪԂϙˑ9áƸźΏʅöˇ˧ˍÍĔLŋҒʝʂʽӛΛРÝˆԫ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'łψˎŅɕ΄ɈČ˄Ҋ\x80ѺͿԔǤȫԄӷ˾5fȷ\x80âΡaϙȊҽʰ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2605223405523500462,
                                                    },
                                    },
                            {
                                        'name': 'ȣӴ΄\x8dξŇЏ}Ɏ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173307.868343:+0000',
                                                                            '20220522:173307.874272:+0000',
                                                                            '20220522:173307.880103:+0000',
                                                                            '20220522:173307.885904:+0000',
                                                                            '20220522:173307.891698:+0000',
                                                                            '20220522:173307.897435:+0000',
                                                                            '20220522:173307.903197:+0000',
                                                                            '20220522:173307.909334:+0000',
                                                                            '20220522:173307.915135:+0000',
                                                                            '20220522:173307.920793:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȗȫ¥ȤſŇӴѷǹӇ˱˝Щ\x83ŗњŻȇϼιԉΝſa\x83',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 823605762743402358,
                                                    },
                                    },
                            {
                                        'name': '×ψӮҠ҃ЕDȴ\xa0_ÿɒǱīЙӋoɱ˻җǬǸ\x8eÄ˧ϸǾƬǥǰ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɥӗƀɢrϖjԎ˖\u038bέщȃëðî¼ȀǽʊϘɔɺ¬ҘӵӑЯǀÓ',
                                                    },
                                    },
                            {
                                        'name': 'џęΎЁǺҩӀҫ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1202435947098449103,
                                                                            -950249782805973639,
                                                                            -8852377450420812534,
                                                                            1095592342666662148,
                                                                            103738351284507963,
                                                                            3224450525268501178,
                                                                            3736693658428374787,
                                                                            -206017130862030856,
                                                                            -6601771179850629700,
                                                                            4028768005409635395,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'кԝ˷юӚψš¬ğѪɲ˳PϟϜѰŖҕu¹ӡʋ9ǮʭαǔхDȨ',
                    'message': '҇ǬŠǷīǍ˪ȁɌʅɱҬRŇϥϧʡ²ԄѮɬɰеÁАğʇΤʫҌ',
                    'arguments': [
                            {
                                        'name': 'ТΙɕÍoӼƾͷˏҤϜ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2454049374479490030,
                                                                            -3344750613110629551,
                                                                            8861475022644537469,
                                                                            -1177826660105865949,
                                                                            -3791083208056384661,
                                                                            -5179013696507026631,
                                                                            7095219610283917421,
                                                                            7419158105785572986,
                                                                            5216642581195110398,
                                                                            -8987721265041340186,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȩȏȌē˟ζɵ*ȉŌ¶Е\x91ϕiȜΥˬѸдǺȋʀɕˊԜƫϺǰԆ',
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
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': ':ŨҖЛӏˑʩÿœŔ`ςхżĕȚfГԀɷњЙƾɺzѵʤЉƨ˩',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ι',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173308.290263:+0000',
                                                                            '20220522:173308.296214:+0000',
                                                                            '20220522:173308.301972:+0000',
                                                                            '20220522:173308.307918:+0000',
                                                                            '20220522:173308.313698:+0000',
                                                                            '20220522:173308.319416:+0000',
                                                                            '20220522:173308.325306:+0000',
                                                                            '20220522:173308.331059:+0000',
                                                                            '20220522:173308.336649:+0000',
                                                                            '20220522:173308.342443:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϸȎǿÖȚТаӑʕâǰȓ3',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173308.371690:+0000',
                                                    },
                                    },
                            {
                                        'name': '¿ώʤ¶ιĞӪƼƌϴ\x81ҤΠ·ʇØƀƚуÅoҌȜǉĒ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173308.395334:+0000',
                                                    },
                                    },
                            {
                                        'name': 'тÀ-ɽƌ<ϥˎðбXОμґΘ·ɍ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            372076.31060648407,
                                                                            515751.73651393095,
                                                                            -12290.452313142188,
                                                                            826921.324155745,
                                                                            618646.7751240609,
                                                                            491310.6868021124,
                                                                            784837.3847900137,
                                                                            346787.3192734366,
                                                                            373249.58892497385,
                                                                            196473.94554967835,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϒǎȸҟҤ˚2ГҲҰ\x8eєžұР9\x94μʘс3Ɣ8Hˀīʅõɦ3',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173308.499908:+0000',
                                                                            '20220522:173308.505679:+0000',
                                                                            '20220522:173308.511912:+0000',
                                                                            '20220522:173308.517766:+0000',
                                                                            '20220522:173308.523566:+0000',
                                                                            '20220522:173308.529544:+0000',
                                                                            '20220522:173308.535354:+0000',
                                                                            '20220522:173308.541283:+0000',
                                                                            '20220522:173308.547124:+0000',
                                                                            '20220522:173308.553049:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˍш\u0382σǃԔƽʸԪΧWƤĜƐːƍʦ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173308.586587:+0000',
                                                                            '20220522:173308.592772:+0000',
                                                                            '20220522:173308.598716:+0000',
                                                                            '20220522:173308.604659:+0000',
                                                                            '20220522:173308.610701:+0000',
                                                                            '20220522:173308.616709:+0000',
                                                                            '20220522:173308.622693:+0000',
                                                                            '20220522:173308.628621:+0000',
                                                                            '20220522:173308.634336:+0000',
                                                                            '20220522:173308.640009:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĨǥɁ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173308.669850:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǙçФҬƈȼυń\u038dϴʬπϰƯѤ˾ԕÿӎŖ˚Ñ?>@ϡĖєν˲',
                    'message': 'śʌ\x9a¼ԅɃǻǕɳȯӋЩŇɽ\x97ĲΠԟşúӪԀЖӵȾƈWԨȠϨ',
                    'arguments': [
                            {
                                        'name': 'л\x85Āː@øӀ¾ϑ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            382676.09761294414,
                                                                            345048.9030397931,
                                                                            962847.2634842454,
                                                                            921504.5898290178,
                                                                            450336.0019894731,
                                                                            989701.6769387424,
                                                                            865869.2599867043,
                                                                            676318.7275190578,
                                                                            209297.70602883823,
                                                                            544035.180498059,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϪϩɎȥaϹȕȏЙȘÈƤԟwͶȖÎņŬƘ}ԕĆbŷɆ͵Ĥ[ǥ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            344996.35398122174,
                                                                            274889.03937783133,
                                                                            134099.03497809794,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '.ʸŗ{ӉԢ5ɏʆ¬vΠéǢҖЙĎƃÃ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173308.844989:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȴѓȍ@eŧԦȿ&ųÿĕÂҖΦƄӉϊΌǨϋģWɅщ³ˬÏȉʧ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȧÀ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˰ԃήóƵМчτȽɼɃ¹˵ΕǺЭ-ρʂ\x8bɀʒșВ·¶лâҚ¸',
                                                                            'ĢȦҝŸҭª\x81ƂӂҭҵƳɆԁϮͳƎ\u0378ҡήӽRнƜЗҕЖŃʘĚ',
                                                                            'оȹ˴®\x81ȜҰԪĲʋЁЉ}ϕё§ЋlАĭĵЫmӊμӬÿ˗ˏƞ',
                                                                            'ʟÐƀѽǸѤԀ\x7f\x7fǈѤϲȺͶÑɻʮϿΫ˻ʁҗϣϟɗȋĉіeū',
                                                                            'ɝҒlˣζ.цɰïĪΐƚԚH˦ќɾŮțwόǌɯ˂ҫӆƄ;ʫÚ',
                                                                            '±ĿaģңϦԞЗѧҚƦˢΝ0«ƷҢ˽Ӛƪɚ£ѯƻ˨ʵԨ=ҥƳ',
                                                                            'ȆϦҜ˩¯\x85ʚv¥ϠH+ҫ|ŏɟӹxaʑʳЧĬͲԙЂ˨ЛӺӯ',
                                                                            '\x8aNˍ\u0379ÄÎBNơǯҗȠαÔǱĎӽԖf\x80˯PƉӤŘũŰƍ\u03a2§',
                                                                            "Ͷϕѽ˪ˉÞ\x89ύԖÔѠƘ+'ƤϤȔԭđƗȽȸ҅ʣШ[єŻõ\x9d",
                                                                            'ӳϯɷ3ØÚôΪҙ·Ęŧϡ>ȓH\x8a¯ɤōǖőɒ»¡ҊǛґʤ.',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ªĝƶүԌ\x9cCӁħğ\xa0ΞʎӃȷœѼ¦Јš\x9eÝҎ˱\x95ӫҦ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '@ӓǙʷҞõ\u0382ˍ˕Ҫ\u0380fȩÎ\x82ӓκʒɠn´ӀŁıɦГΊÓ¢ε',
                                                                            'ÂʨӱσчʍΖªǢƼDʫ˳aRĬʕӧʰ-ɢԔ\x98ŘļѥжǠԑǋ',
                                                                            'ԓOΗϽŮͺǷƓЦԌτ\x95V-ϑÆėѸƊoŉ˫ԅПϸƟbϨȲǕ',
                                                                            'uтԫòȓҎ*\x89˼ұԩʻΌŅӷӬԦΛÊ\x9dȱЂØǈɲɷϿȏ¡Ϥ',
                                                                            'ǬӔԂÑԔÕ΅Ѯǈ¼Ұ˫ыƵйӇFΜ˖äӅ\x98JɆĖӀα˴ȿw',
                                                                            'ТǩӞдϣӣ\x80 Ҝ=ΏǐŬͿ\x8eϑΟæɾ҂Ɖɫă°xɎpĨʪԧ',
                                                                            'źΤǟѪѾKĵĿ˲IˠӅǄҷ˛ςʔфŸʈ˵4ɜľƛΕɖԙŹ˖',
                                                                            'ςǉǌӑQӠȢĀžїƱ»ʂ?ąȪ=ΌˊӏҷĈюÌ˃ʪԨϯØǡ',
                                                                            'Ӊϵŗ˶ĒŢȅiɫʵʝÍҲƦұkƛǏϪȥҞњƂҴȋмӌɝФҳ',
                                                                            '%ʸ8Ж?ːʶԑғīʢȻΛ˾ЛɳԢӯȱ5Є\x99ƽʴf˥йхӌɥ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8eʇɺӐ\x899òʜϗͻэɛӗӎιҍɻŹбӀɨ/¨ģ»ȵқġΜп',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѫǢʊQӖ©ˡʒͺĳ2ƪƜҒҀΘ˕ăӟǝОŏϑȔӰ˶ΎӜϯɣ',
                                                                            'ɳ˭,30ȎóĦƛŕǼĥėɺʐȶȈ˙Ƃ\x90àͰ|ǎ©Φ9Ýʠ-',
                                                                            'ȸʈ\u0381Ə\x86ʏǿүԝȥMԙ¼ʌŵË\x85ΡΞȢƀΖѮψϝž˚Вéʨ',
                                                                            'źŽǈҰǍǕ\x9d΄ӭŌťŉλȭ\x87xĴŲΆΕҘ%oȪØ΅őԢǶǤ',
                                                                            '§ȭӵшđѵÒνЄ%ҳĨҁ4²ϨëɈSǓ҆ȸʼɊΌǊƱӞ¹Ѱ',
                                                                            'çѲσɳџɎːѰɬЧмͰԀ˟ßɨ˚5˖θӪдѼƥǯѱτδџœ',
                                                                            '\x98#χ\\ˢƸǪѥͽʒːɡȥрͷΩʣɄӦȶϰˣ\x93ĝԉЂӭВFʖ',
                                                                            '½ʄŞȵ҈β)Ƶŉȋź˘ѓǨ\x7fϓǹÇʻћȖ˃ŏƭiжҗPѹɄ',
                                                                            'ȆџŠȣŐғӤʟӴѱČхɃžѦ´ŐɓϳάʘʞǞʴӬ\x81˰ѶϽɸ',
                                                                            '2ɂԇЀĈ¨˅ĸ҆ėÊƞŅ҄ǓʓХ]Ȩ˔ӡаͶɼνƻčíǷš',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¯æƳɵ˷.Ǽԗξ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 827054.1991125628,
                                                    },
                                    },
                            {
                                        'name': 'ѪŔ±ɁћϒӂƲҴʮφϵгQϺўѫҵĦxƜɁʞȞéƌʥɟҞƽ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6695796385642170618,
                                                                            -7896165546544358489,
                                                                            -5072236028473493396,
                                                                            8235211128147094257,
                                                                            -2439433237479042433,
                                                                            3051061035173130017,
                                                                            -1072339560858187310,
                                                                            -2175746245773417327,
                                                                            -7989094371977451058,
                                                                            -8198775614355255297,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ņҤϪ˚ΥӀɟҳǞǍQƏҪĄЉж',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 125743.16888766884,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƻɯȳǆˆčȢ\x80УɶƷÑʶÊԏυɇɭȁ\x8eЙɲŧͷԌФӝʐƐŠ',
                    'message': '\x9dśįČƊЭ,7˹žӽǗԢāÈhƸʕƨƝ\x8cтȸžҒӴʎяΝÆ',
                    'arguments': [
                            {
                                        'name': '=-ķέ;PΥѯÑÔ˧áҨШƁǭɸ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8070318166223059284,
                                                                            -4677336374301768659,
                                                                            -1123720638006220442,
                                                                            5348713003903079701,
                                                                            -5936825397500829054,
                                                                            -1213583192270843667,
                                                                            -4769585510339594453,
                                                                            -6362714477631922820,
                                                                            1595117626774722965,
                                                                            -1075399691992768195,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҙŁȥUʍ\x9cϝʐ΅ÇПнïę˭ψ¸θɸԕ\x8f¶β\x94ъď',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƨˍԐϷΏҕʩɣ҂ҰʪɀʻП',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1072873691922701872,
                                                    },
                                    },
                            {
                                        'name': "ƽέıʭԉ\u038d\x83wѦ'äƃн҃ћхå\x92ˇòӂóʫɞ",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƟȴˆĜԩлѳҫӸXƧĒľɀĄɢщ˩8ѡШΡ\x92ȕĩħ\x86',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4530738663792035625,
                                                                            1043810319424149851,
                                                                            8716731345907393276,
                                                                            8323452855952628640,
                                                                            4705644941879017161,
                                                                            -1767482783483157357,
                                                                            5079914154439904707,
                                                                            4534788867606176188,
                                                                            897141236122123423,
                                                                            -525496323878997569,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŖʝTɭҽӸѨСԧÀȃǔ¢@Ҋӈàʹĺħ˺ʙ˽ǓѽéӇȯҏ˹',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
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
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'scope': 'info',

            'messages': [
                {
                    'catalog': 'X4',
                    'message': 'ͼ',
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
            'identifier': '\x83\x9aǮ\x95ĆɻńƥȎǒЁŃƇǤ£əΣˎDʛɩл=ԎSŷ˕ȖƉŬ',
            'categories': [
                'file',
                'network',
                'file',
                'configuration',
                'internal',
                'network',
                'network',
                'file',
                'os',
                'file',
            ],
            'source': 'Иԫ˒ԆūƐ;\x87ΠӜ\x9clˬӟԀåȂǙӱÕňЕ·ţòťӒûːɁ',
            'messages': [
                {
                    'catalog': 'ʨшİƒԗƳɃԅƐεө{ɶԂԄӶɡӰ˥\x89ҨU\u0382ɮ˙ҠΖȿԍӂ',
                    'message': '±ʶщhϕщǰΤɌә9ƈѕśűϫ˹·Ĉɞѥȍ¡f¡јӔǄ˨ƣ',
                    'arguments': [
                            {
                                        'name': '£˞ȭѹηшøʁʺʓԄwǌѠŨԈƜĶÝŎgɠɺ\x9aΏɐе\x7f\x82ŝ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173315.812236:+0000',
                                                                            '20220522:173315.821054:+0000',
                                                                            '20220522:173315.830175:+0000',
                                                                            '20220522:173315.838157:+0000',
                                                                            '20220522:173315.846222:+0000',
                                                                            '20220522:173315.855479:+0000',
                                                                            '20220522:173315.863745:+0000',
                                                                            '20220522:173315.872749:+0000',
                                                                            '20220522:173315.880960:+0000',
                                                                            '20220522:173315.889012:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ĸôÊǊΓɒЀСʸҿѢӅУĖΕҽЯӳ®ұǤΨǳƛjKϕ±ϛ˷',
                    'message': 'њԏȞɬũȰϸЏ(«ʯҽ°Ћɖğ\x94әØȪɰ\x8e5ν˾ϋλҞҡΣ',
                    'arguments': [
                            {
                                        'name': 'ŨǌԐͿєϥτƆǐũїϛǅĈ^XdΏӚҢ˥)ҩг\x92Ўμǋĸƾ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʲԈĈëԉҡϪɶNЗſ§\u0379Y(u;^XωҸвЌLʧʯɽāŊʣ',
                                                    },
                                    },
                            {
                                        'name': 'ÈsXҼʟŝУɉ\x81˾ʙ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʸµ3ȟǯͻΒѫǍƸ\x84ϭCĺĀӋɺŌήˇʇԊѤѪɺɬ·жȰԃ',
                                                                            'ӉȏĄȥ\x80ã\x8cƃʌĎӽ\u0381МͶȖlȖđõUжĉĉԔϸѾÁîÒσ',
                                                                            'ϊǑ΅ҢȻřҬϿ~ʯŪũźŵş΅ÛҝԞΑżӿϏҨʵΙʭлͽů',
                                                                            'ʹΖԬǵɦΝӄ,ʳчЃ˅Διљ\\ȫцēԪȠѴ\x81\x8fɍΉļҫȧѭ',
                                                                            'ԤЗʃºǁˣΦԙɔkŘцҭ˭ĈˢԋŘʁҥǣτӌξďѡїЀʌϛ',
                                                                            'ǃҩӃϲҊ\x93L´ԁƱŸƇƭԪĨϼȑŕцҜɇϯǙƌ#ǳpÒ1ˊ',
                                                                            '\x86ӏΔϸю$ɣš\x99ȹџǹĒз˰˖êҾĿʀĞŷθŪÖԆΛԖұǌ',
                                                                            'иɷȠţǫ\x80ȘҒǈŮĉƋ˛AƋ˗ӈϭӍпÐ˥\x97ʀɨ˘şeӔԝ',
                                                                            'Ĕ\x9bɄϮ\u0379ԐʐʌŸΪ˽ÊɁˁĴѬΦɂԈӛеԜðüˀɍ˚ZkƷ',
                                                                            'ʳèҩˬϏЮEѺΎ´ʊҞԑƖs&϶ƊÕɚӬƢaаӬʄ˛ßɋӆ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'θ\x8bǴ$BҏӚʇМǻȚӏ~ɞ-ŀЁƂǧɉʎӆϛĨLƖąɍfŖ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2809525743966546716,
                                                                            6675938893648683231,
                                                                            -2462988732117601864,
                                                                            2224277714819797483,
                                                                            -6326834762739058056,
                                                                            -6598129483627511265,
                                                                            -4035515544426410685,
                                                                            1020229786040850060,
                                                                            -5260422102514008900,
                                                                            -5321667679608110385,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˉ\xadŲČϗкȏäYѓ¬Ӗǅ˩ҜõȌϢʣΊҥГӃεɄӹˀPéϖ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 365315.07454266143,
                                                    },
                                    },
                            {
                                        'name': 'ԝLŜ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173316.286188:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ľȪčϟԪ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɼqШҴЫӿŴFɈҲѻҡѷʞEѶ\u0379ťíɂȉӄˠ¹ϦΨȝȲτě',
                                                                            '¯ˁʸǰµНLɅʧğa=˘ăƾԌ˂ɲѫqґлΦ´\x85Ιҍȵŝģ',
                                                                            'Ӭ)\x8bҦϕя˱ЁȔ\x94ϗƉʰʕƃ˦ħϸѥüӦʒũΠǟğŦÄ1Ҭ',
                                                                            'ʻӃŪэdǦϪӔдѦŉԒ҃öɴЗǹüʿԪÄǺňã҈˚ϒғ˫ů',
                                                                            'ʼԋǶӄǨєȗǦТďǛґ¶ԪӠĦУŏԠŻҦӺҒŰȮҁųёɐƻ',
                                                                            'Ǣғ;ϑʌҬ˱ǶàÕίƥӧbγҾʩҪѶǷƅ˔κãѳ˙´˧ӟɭ',
                                                                            'ǻɘΔӐ˲ƓԇІбӯЯΫѡƴĜԢԗǵˏԠсӼϻѥƪ҉χӻвÞ',
                                                                            'ªӑƥWʙΜǖƚðԥԎʚɋжϽ˞ϱԐɲȋȜȊҷɠưɉɰ\x91St',
                                                                            'Ͻѐ˴Ȍ\x84ʼĖ˫"ѶƯªѾ\x80ȩ˃ҏφϛcѢŜHρӬӢ½ǋìи',
                                                                            'ǉ҇±з\x97ϣĪØҕȁ5ԁɌԘȏʓĳуȣĤȼԂcͿuʭϦϾϧÈ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΠˤǦ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173316.442943:+0000',
                                                    },
                                    },
                            {
                                        'name': '¼\u038bǺѲϱӎӡ˷ӃҠʪz\u03a2ǻ_іĳӗԮҔӕǱ\x96˗\x81ÅƴǓ(Π',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '©ƱΦaҫ\u0382Ģ(ǸБŚȁHƍӥƪωжʍŹԈUиˎѨρЂЉлϪ',
                                                    },
                                    },
                            {
                                        'name': 'Ϩϐ˷ȳйΛʾκĀӞ˾¯˂ĘȔKб3ʤ~4ğƴҟȗǂ\x81˨ΐ˩',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȡԩȳ8Ȥǟ;кĶɮʲɰƷϟӫSˢ˰ɀШϲĳҸЍӽӯǗ\x9bψĎ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -38612.35815203551,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ĭĺөűљĤǢ?ǾȄϑΆмƠъνǒԛйɧɦ=Ӓˠ`ȔĊΫ˰Ԃ',
                    'message': 'ԫgεҨυˊƨɣɘҔ@Эíʲ\x80лºȮ͵κʴИТԋǧºɿҼŗɚ',
                    'arguments': [
                            {
                                        'name': '¾Țó',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ѝ±',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173316.732331:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÆΛPƀÍώҿȆҿи%ʕřϨº˚Δ@ė',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8831149344953012193,
                                                                            5240040973543768104,
                                                                            5847668062713248257,
                                                                            -3715586217693506297,
                                                                            -6230586913910073719,
                                                                            2447910790790354407,
                                                                            6711051666173400376,
                                                                            8850263297955590066,
                                                                            -7824796032011109146,
                                                                            2238898241979850150,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӔАЏǄĸЛpαʝӷԃԉÇ˟HҚѯђɗÀа¤ʳйǮɺʦƼκ|',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1465776000884463528,
                                                    },
                                    },
                            {
                                        'name': 'õńʚӟԚƍɈǳƻDǯǗӰУӘԚĥ˹˸\u0383ĺ\x96ҙ¯ˆОа\x9eͱǴ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Đ͵Xɡѹїȃ\u0380˯6ƵǒːȺÔΗŇѢ<ȐȦ°nŐʹɏĻѾлϋ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˔ĀÝͰѹʔҗҀΐӱŧŵѱȞ\x82Щűƾ\x98ŰŵĬљӕưɲΩkɞя',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 822233.9447925546,
                                                    },
                                    },
                            {
                                        'name': 'СΞţȨѾ\u038bҙÃ\x92ĝаțԘӺλЛľÁVΡýĔʑʢõΞɛеȺҍ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173317.118422:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ѳ΅һіϲĜ\x9bŜAnҥȲ˯γϮȝôƺӐЕºѝćΟӫʻЄ3=Л',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'хǄΌ"ςƇ¡ɆԄG˨ѹЧĲϹҧϺŸŁɔŇ˴ɛԔȥĐԀӼa˥',
                                                    },
                                    },
                            {
                                        'name': '\x83ſÂϓȏӦɰҪсșΑԦRˠRѥ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173317.186209:+0000',
                                                                            '20220522:173317.194365:+0000',
                                                                            '20220522:173317.202315:+0000',
                                                                            '20220522:173317.210245:+0000',
                                                                            '20220522:173317.218674:+0000',
                                                                            '20220522:173317.226593:+0000',
                                                                            '20220522:173317.234897:+0000',
                                                                            '20220522:173317.243983:+0000',
                                                                            '20220522:173317.252595:+0000',
                                                                            '20220522:173317.261551:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǪШԈȐȰ\x9cƠͲЋтȊαƭɶĮЎɏԉˎĆęҥ\x8eԏQҋŃͽɡӍ',
                    'message': 'ƲϗŉìȋD˪ԨҝμʥÖϾϗԆƽ4ʾ\u038dοͷѐфӎȅ\x80+įԚͶ',
                    'arguments': [
                            {
                                        'name': 'Ȯķķʩ\x8fǌҎS.ΞēРǻѺĲѕɇѺƘҳ·ͱȮЈѬƧH˄Àȅ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': 'ʆЅƺɐƒɩ0ҟʦ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5419110110228047152,
                                                                            1264239694451319083,
                                                                            2340264792625143034,
                                                                            2433825981921797140,
                                                                            -1957409335928375764,
                                                                            -8064895227139399937,
                                                                            -5096419277728067557,
                                                                            -3347353068081016106,
                                                                            -202584489078578398,
                                                                            6788441596615845917,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8eƠӍȽξʝfȒԥȀɯϻĥѯΚɪДγ˹Ήʘˌơӽ˔²ԜʦĶΧ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƬȾgҙӲȏϘǻÛҿʕßʋˉÞāºӓѼƉԥǆӟƫ˪λŉ¿τӊ',
                                                    },
                                    },
                            {
                                        'name': 'ȶЌӛ{Ȳʁπ˔',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ȨӻØ²ѱĈʦҬςeuϭγҫ¬Ŋ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173317.734551:+0000',
                                                                            '20220522:173317.742848:+0000',
                                                                            '20220522:173317.751639:+0000',
                                                                            '20220522:173317.760430:+0000',
                                                                            '20220522:173317.768473:+0000',
                                                                            '20220522:173317.777038:+0000',
                                                                            '20220522:173317.786110:+0000',
                                                                            '20220522:173317.794250:+0000',
                                                                            '20220522:173317.802059:+0000',
                                                                            '20220522:173317.810235:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӤƣŀǩԚĲāǢП.˴Һ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 209703.62965218007,
                                                    },
                                    },
                            {
                                        'name': 'Ͱǫɓ˳Ȣêüq²ŽƐӝȰɮҟҞȴ˨ѵ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ņòʹǿ\x82ȒŠñı4\x85¹ɞáшʭҿŏ҅aӪΤӑˑҶ^ϔļ®˨',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǌɹԙǞǅȡŁ±ř=ĈĿЭЋҶ7ɴȉЯŹӗŀЬѷŰĖ.ӿê˃',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173318.038731:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϐӬŨʵˍ͵Ďǝɝțű',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
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
                        ],
                },
                {
                    'catalog': 'ʖҏĜƀɬĥͲ7ӱȼϰ˥ǇщʄhζƌқϋӽԕκɟϯȱtΖрҠ',
                    'message': 'ƯΑʶĤѣǹԃ¾ӃьŰξ;ӷϪŀƠЂӵϢɔʾҩӌҖʮԆ\xa0"Ҁ',
                    'arguments': [
                            {
                                        'name': 'ѧƃ[НμäҞԚȴ²ˈyөҧҿɫԆ7μ˹ɹӟƴʠŝɼҊƄ˻Ҝ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '©ŭƺҐќ˙ƣʒɅʅŅӕ\x80ҤЎђҗπ\x95ҴӫȻ˗ǟԩȍΕəӤɯ',
                                                    },
                                    },
                            {
                                        'name': 'ƛҠώϷʒЭιǴѵѵäиӖПʛԣђ©\x99XɲJώìǂԮWÐ˩њ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 567141.2680868324,
                                                    },
                                    },
                            {
                                        'name': 'ХßǌƱϓωƤә¯Ʋ%UŖV\x8bЌǑ:ʍ˵ēɲȊΆƩ°ӢτЙT',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ŎȶŔǁˀ-é',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173318.331251:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӍƫÙϖˏ\xadDwƮ\x92\u038d7ѾФˣȹϕsȪ;ĳԕɸӜɆ˔ыÃ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2245796090633801818,
                                                    },
                                    },
                            {
                                        'name': 'ŢȻʪȬʸȬФӢѾʫϞƏϸʆóœ˱ͿәæƆƙôѫ2ɂĥŏӗȺ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѹˆȿ\\ʢ.\x9c˩ǢGԡӣбǩʐχEхһΰѮѴ\x88щјάӞ˝вԇ',
                                                                            'ÐȓF˛ѼŰȣѪƌįԜЦĦɅԁҌŰȧԙͱiǸƉϗĆÅ\u038bȎУ$',
                                                                            'ň˖˃јϣ˪\x85ŬƹɭԘҷ˲˾ŉ¿ĵ˓¹҃ÿ҈хӮnȑнΏόf',
                                                                            "Ͱ'ӯсҊԄϊǷȂΕȨâҭёȷtɬҫņʞ]˘ŢȍĜʇҢĐʊς",
                                                                            'τŢˬˊЪʵØȓҐЖΒÉϰƼǇʻɯŏǑ\x9d>ƜԗWҟΊҹͺnӖ',
                                                                            'ӂúƯķŰɿǺɛĶȋѸO\x84ŀηʷƟǣȪ\x90ӿƺѻ˧ЫώχϻΎӘ',
                                                                            'ΓϠ\x83˳ɉk¤,X1˖ȼń\u038dțʡǿDшīɏˀԜґȚʳǉӢ\x92ȵ',
                                                                            'ÁǺ\u0381ɈϺȵʈB˪˷ȝŨ\x98ŰŷǅǷŁħȣΧʮʙӶƶԘƣȸȹ}',
                                                                            'ӢʆԔƵӴȵfEҼɢˌǖчŔˀOЫOˋɪɱļѢmҿɞʚνwӬ',
                                                                            'ЄDΔÝĐºӘҖpŢưǡÜǆΪ˹ϼО\x985ѼνЕҸяф£˾ФЮ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΰϠ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ŞӒų Gěȍh',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ș©ƛԑ°ȓԡӀΩҬļ ˗ʄȯƁĬΈЦŏĎǓȽqǋјɁҹƔΧ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʅŗèԬŎѦӛǅîɖČɣȂєњŕkŴúԇäɦϺЅТē&ͷίƉ',
                                                                            'ӠӲџ÷ΤǵɬƀΧѹђǙǔǧœΝɻ˨ɶƛ\x8fӪȎǗȋҗĺӯүǵ',
                                                                            'ʜâȈɑϔƗѮˀӒҭǎз҇ӏʃŰÄНɃ˲ɮLөNάǩōǞ ҫ',
                                                                            '®ӓœȜԍ˳өȖȡʘΦŇ\xa0ІτҺ+МɡŃԝςNīӒϖƧ\x90ӝΖ',
                                                                            'ͽҚʀçğȠʟǜҌӋ˶ðҺĎԝ\x81ɍϋӹԩʺβÔɧҷàÿuЈҎ',
                                                                            'ʑĽǿŪωΈƴΒñԗ϶ǝŽˉңȄʃIȟАοЀ\u038dƄǣˮʐȕЫʖ',
                                                                            'ʱҜǨǸǝӧʱUĸғġΛ5ʥȉ˘ÚƁȐΉА>ϙŕǰʿоҋͷѡ',
                                                                            'ƤŲКҴĥdҼѳΨĲ˄#ʺѫXјыͼǸыĘʱͳǁ˭ȮǦϧǒɰ',
                                                                            ')Ǒmɐ»ˡθɈ·ŚͰΙЩԥΞûˍƌȖѸǏϔϓǺǥȟɄŐ\x84ł',
                                                                            'ҒеђӼȀˢҫȷɓ\u0379Ͱǹʚȕӻѻ.O͵ҟϗPӷdђԑ˼ɨȫƝ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɺҨ\x85ӓш½ʣ\x89˹\x8cøҘǂϴӢÏШʥ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4002662240189668519,
                                                                            9048115994248019936,
                                                                            -3136276124977429786,
                                                                            -8282488952590679257,
                                                                            -4011348426102232000,
                                                                            -8793229669524808052,
                                                                            -5919890765757315128,
                                                                            7680577830307917800,
                                                                            -1753166129089618444,
                                                                            -3760503742615692638,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȏĲӦǸƸԊƄʅ\x89дÈëśɲʘ\u038dŵ\x85ϠҷƲ˛GēϏƸjǎϯˇ',
                    'message': 'ÄɚӆEʰǼƨӻɌΓǈϏɶjʳsĂɹвȼTΛ˵űÖ_ӄѵʴг',
                    'arguments': [
                            {
                                        'name': 'gӕӐӎȅǬĭĹѫѢÌψʭҿҗϫhɘŨ{ʴʤʥǒ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 447208.9890530056,
                                                    },
                                    },
                            {
                                        'name': 'ҡïǷEîɷӍ҇ԬDќ¾VɲИ˛ƩöȚŮɅΈɐҦǴ¿áź΄Ύ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173318.986999:+0000',
                                                                            '20220522:173318.996306:+0000',
                                                                            '20220522:173319.004216:+0000',
                                                                            '20220522:173319.012954:+0000',
                                                                            '20220522:173319.021497:+0000',
                                                                            '20220522:173319.029538:+0000',
                                                                            '20220522:173319.038857:+0000',
                                                                            '20220522:173319.048124:+0000',
                                                                            '20220522:173319.055714:+0000',
                                                                            '20220522:173319.064793:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʦΦ\x9f˫ҚŘѸѸѩ"ӆǮ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ʖфǓĈҏ{ѤωҊȱК¬˖æɍϕoĐ´Zɂϱɸ˴6ÓɉϼΠʥ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2815367232801142288,
                                                    },
                                    },
                            {
                                        'name': 'Аķ\x94ԧ˞ӧҥςŘԆюɧБǢгƗȧƙĬɟ¯áҔҪɅ[ʠŦ7ҥ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԇҐϣɂȬЖȸΠȈӉЕįĘʹϛđЂʹ\x95ôҿѿ^ǯàƫɚĞǄ(',
                                                    },
                                    },
                            {
                                        'name': 'Ԑ>αŰҴėѺŶàɯҌɴ4ϗqӐԇƓ;РƭͳӊɏѷŽȽgĩ\x7f',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 681200.0858237569,
                                                    },
                                    },
                            {
                                        'name': 'ÔƱĔʧȤӢϓ*ĉ¹ŞĮΖ¡ԢӒ;',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173319.245442:+0000',
                                                                            '20220522:173319.254582:+0000',
                                                                            '20220522:173319.263710:+0000',
                                                                            '20220522:173319.273316:+0000',
                                                                            '20220522:173319.282424:+0000',
                                                                            '20220522:173319.290374:+0000',
                                                                            '20220522:173319.298426:+0000',
                                                                            '20220522:173319.306339:+0000',
                                                                            '20220522:173319.314379:+0000',
                                                                            '20220522:173319.322730:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɸŽǮÄƊŴЩʨĳԞʄԬԆœѵ1˷˵àǁӯԡι',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'lɏԕϴǓΜǖ˓\x81ЦҀϪѦ¶ÌҞƎ˘ҩ΅ԅаҗöˇǢѯӲƞÄ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173319.398526:+0000',
                                                                            '20220522:173319.407496:+0000',
                                                                            '20220522:173319.417057:+0000',
                                                                            '20220522:173319.424818:+0000',
                                                                            '20220522:173319.433641:+0000',
                                                                            '20220522:173319.441857:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЅҤňҸѽƫƺΖĲÍƢӨÞƁ\x9dɾǧαˋЬƚɒɯЮŖĖºǞʠÂ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3249552087721764667,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\u0383Ϊƺƕϑ˨ϑÙDԍʺӼԈȳľǬœĂťѽȜŽўfԘƬҽƎϫơ',
                    'message': 'ǱʋА΄ʯȌe˟ÎĐԉәȍ˷ˆ\x9aɤa5ˤѤϤԗщ\x8bβƤ·«|',
                    'arguments': [
                            {
                                        'name': 'ƜʌʌѸƌΎƺƩӛͺƑ}ǖʅÛȵŴǑɯǃ\x87\x92˓üχҏӊϐũ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173319.557402:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ţ˹ΚӊɗӵŊ\u0379Ȥɸ[ҕьЦɒԜΨ˰ˈųҘяũǵҙŦӏ\x92ȒȔ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1188981434794639392,
                                                    },
                                    },
                            {
                                        'name': 'ʪ˃#¶ÄȈśŦƅӮ\x94¼ҬǥċĻǃ˝ſʓʞњǺ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ϱɃʱό;t¶љɾ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1386024351029071538,
                                                    },
                                    },
                            {
                                        'name': 'ʹЬαÜ¥ӷƻΏͷ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 855854.5879477324,
                                                    },
                                    },
                            {
                                        'name': '\x872ЊúșZІ¯ǳѤ\x8aǀÀӻʐƧȨΜ͵ɟˁǣԅˠƕǁĬ#Зӂ',
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȊϹζąó',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -869673161309444390,
                                                    },
                                    },
                            {
                                        'name': 'ǎɄηőǘΈуʻƙÿǦҕ¹ҕϗ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173319.883214:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʕĂdÜ &ШДź˹ÊҀƎĄϝ\x85yʱ\u0382ˬƤψҊʌUКƌŹĿԣ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'љǃƿԓµҫĸɝԐϼĝʺȅȵĘфϛŖʘçˍɖŗɌĜɽҋήєæ',
                                                    },
                                    },
                            {
                                        'name': '˺VOſŴԫrsѵǶвƜҭ\x82ӡ\x7fΙӛ\x83Ҍ˃ͻöɞÏ"Ē˸',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŊŹӸӑϷʇ¬Д2ʜ˚ԩԜϷɇłԓȊƂ\x9cȂ$ȴɈǨǊЃӕӯA',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ңϣБΖ\\˟ŢȄ¾ζʀǍ˰)ϑұ\x9aőԜҜȞ\x99üMӋԟћĤҞԆ',
                    'message': 'ҹǉЧïωѕɘGҡƻȯȠʴҜȸļū\x9cçǱɬνϯ˩ʮ\x80\x8cĕȯʂ',
                    'arguments': [
                            {
                                        'name': 'ɑÃҠ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ͻКѩ˱οӌ\x91ƜЪûѳëҢԣʤDҁƅI\u0378ɷђʼҤӷǮeáүϖ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ā-ƁίτӨŬɇӒ¿ƹνwԞEƝѬҁɜ҂˒ϰΊǄηŃǉƿӱϜ',
                    'message': 'ǨĐŪҸљȝ*ҵĎ˳ɑѨҙ)чǟѳˈȑƇ¸ϝ¥дȺTȃǷԀғ',
                    'arguments': [
                            {
                                        'name': 'ǿӫ˽ʙӜĵȶǖƖ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ώəсӭЅΪːcÅ\x9f',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 601081.9809340091,
                                                    },
                                    },
                            {
                                        'name': 'ҀǅɎhǃӏƘО/óɨϼАѼ\u0378¢ƇӝϴҦùƼϿӏſÉϾ˙еӯ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӈϭѡƝǗʐӈūɚɉӑūϷƤҬ\x9cĭ\u038dΡмȔʹ´ȗöɯˮ˚«м',
                                                                            'ǳÒʆΘ˴ӻЮœˌͼûŮИҵņҬƨŉɵňЋĜƭђΔΫƊѼZȫ',
                                                                            'ѝ;ѺϺɳ\xadΤ\x9cƧȩΉЇќў\u0383ѧΦƂӘ\x7fÊ|οIԊΰ\x8eҎ[ȟ',
                                                                            'ΆǳșŶʤʍϊѻϳľӤĀƚОƩȜК˜ʋxʋȶДǓяѬԨʻҮϬ',
                                                                            'ĈǶīɬƈήÁƐɶˬÚƠiϋʟҹɨА5ɥȘȜϲДʒӄĚԡϟĸ',
                                                                            'e\u0379Ԗω§ҹƭÇƿγҺϬԂУԑǍŨ\x9dϓ\u038bΏōuОҒӮȳ҈Ҍũ',
                                                                            'ȢÁ5Дҹɜ\x88ӏƻǗ˒ÚǽøɋϵȹbǏƴ_ƤŨ\x9cӓʽʂΜ\x9dļ',
                                                                            'ӂġȓáɓъ_ÎͿÐьʙǌȑÛПkΨͲȭlĞĒȀªσҡǌʸҪ',
                                                                            '\x8eӊэ˅ɘäˣƥѱҼԪƤђķHƭ˕ß˟ȲԮӺƩƺɀΔ\x98ȺŤŜ',
                                                                            '˼ˈϻɏω˻ÂίѴԩҴĀˎ\u0383n.ªxĖʾїȣȖӱψԗċӒгы',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x91ĚϨȂУƒ\u038dʞ&ͽ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 108961.65198011565,
                                                    },
                                    },
                            {
                                        'name': 'ϋяďÃѹË\x84ȝѣѭ˾ʜδÅÌЧǈӞԙ¥лѸӷВɡԞΏȜԮѫ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173320.317997:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҖŌԡɪʇϽϴʴȒĊԓϴåƌŠǳɔʽϒӣќл˷ʘӮӂȇý\u0382ƶ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            215595.83511291508,
                                                                            472141.202425194,
                                                                            756561.0376799298,
                                                                            72031.3181083083,
                                                                            951086.4202292634,
                                                                            859091.9796248348,
                                                                            589756.8555582139,
                                                                            522760.66115772177,
                                                                            766751.5677627829,
                                                                            472198.84833507566,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ђҸщǠҠТȳʟЩɇɲɢɄАϑ\x8dƅǧϩϸҩҏ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6632189735387324614,
                                                                            -2997705664517497198,
                                                                            -7697237360900468049,
                                                                            -3069608672890236774,
                                                                            6096682846895479957,
                                                                            -2696676628236331354,
                                                                            4176159499003587838,
                                                                            -3758131637612815100,
                                                                            -2023302008599888288,
                                                                            -9102525755189089640,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'œςZ˜ԒԠfȳɼ2ΞПӕΎȽ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4188809605255176086,
                                                                            -8601866454856512244,
                                                                            5840374780718650745,
                                                                            2466713977783524865,
                                                                            2499517746712609931,
                                                                            7131513342723356760,
                                                                            8034189678732703271,
                                                                            1326013324378937288,
                                                                            970828408730971513,
                                                                            2735367861434657924,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ъưѠ΄β',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            894712.0815036787,
                                                                            744299.3450937779,
                                                                            432011.8236275066,
                                                                            -22181.883593204082,
                                                                            719443.0920058432,
                                                                            285632.37212334253,
                                                                            372908.1949717946,
                                                                            135178.4666970708,
                                                                            665988.3198743657,
                                                                            801649.1311832577,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '??\x92˨ŬłԤќӣͱΏ^ʘǂ2ñͲçʂƤïſɬЮă',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2596898009615335452,
                                                                            -6830135279571406892,
                                                                            -4668441687253056364,
                                                                            6069545818429361877,
                                                                            -2010204745704677297,
                                                                            -7463298958797658432,
                                                                            6438074377710391528,
                                                                            6007300009025018014,
                                                                            -9168692257490086299,
                                                                            -7374494224048746888,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΨҮρЋηп҂\x9bƹɃƦ',
                    'message': '6ĸŽӔѾқ"ϼUîфϩȌȰϲrѥӝӛϵĄǵҡŲƑǵˑѰɞҺ',
                    'arguments': [
                            {
                                        'name': 'ƨѹЬγǭ\x87¿Ə¹Ƿɩϲ\x90ϔѼŜ҅ȬŏgɷжȖŀҥϴϥњɧˣ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ЯɍǕÚИϦԔˉĨʦҼȬzÆϹӒǁүζʩæҀɽZԒ˚ŦήRȎ',
                                                                            'б\x9d÷҄ǰӉɵȘХlơȉ\x83ҵϗðŨȷǎŽGӟЂɂǡfQ˜ʄϺ',
                                                                            'ПǈӵģĹˊБԥMуĈӾԋԑ{¼ʝȔ˯íŰÁbÝ˫Ѳҙ҉Ŭĺ',
                                                                            'χ\x82ρćɧɇ|Ԉł5ҋBɍȸʺŵĕȦ8϶ѶƳΘϢˠθʓƘʫx',
                                                                            'ǕРԖȹҏβԏ˘Ҵ\xadΖӆѓΉԄǶϧδТϴІԈΑϑԮњȑҸщÌ',
                                                                            'ҏљ^ˬİĠϋͰˇ6ǭM͵ȺäűԈĲ1ǈƜTȫơŰȄӍҿʒά',
                                                                            'қɝʍư\x87гºʹǮΏ\x95ɪʖнРaƇϿŤҭ@Еϓ\\rÝԇ˱ҶY',
                                                                            'ĝү<ԥԏUƫØȊƧυЄЩÏ\x8fӛ<мσȺ˷ÇӽȕƮǮĢαҗь',
                                                                            'Ĩ{ɟӊſĳžZüӧſͳ@ʶh˼λӾ˃\x7fϗÜɒǱK˔cì\u0379ε',
                                                                            'ɕΌЖƢщОǥҷЍйĺʍƎˌŬʑʏÆӦFƁrШпő˂ӋҾΰϪ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϰѩЂХ΅qԜѬ\x94ţʸʿʖǛȩ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 820232.1047024869,
                                                    },
                                    },
                            {
                                        'name': 'ʥӺӊĬΟ2¥ϽϪɏ{ӋȤѺOӐͼԈŉ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5463217915067149774,
                                                                            1887545352867764681,
                                                                            2056504308712666690,
                                                                            3316341462359889073,
                                                                            -8874966894275291331,
                                                                            -1408078304864040337,
                                                                            7065439703343399644,
                                                                            -6060614797200175586,
                                                                            8751909700650878875,
                                                                            -3065689611885332535,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΊÞ¢¶<',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ιǟ\x9dĂķȔ[ʉ\xa0ϨǩŋɋɥȈ\u038dɬǫôԁĲƘυ\x80ʯӯǖӎͻĚ',
                                                                            'ӁʐѽÇʃȧQŻҤԜңhˍőœФƾԜӬπѼơ˃҈\x9aɰҶʷɺѝ',
                                                                            'ӑƲħǌҙНɻϮωδ{˂Ћɱ\x91ӧϡμϞƧԄйʂҍĈƈъȫ÷Ѽ',
                                                                            'ǢВ.ƸҦРęˑѕƞŤòδ\xad¶ˠҔžǃϨɪ1ҩɌӯӌˎ˩ʬ+',
                                                                            'ѝǤ\x8bΚ\x97ЇӪБʺΰ˶ŽdϰгДƺÌиɓҧǺФԡ˒ȇƁ˓ǂĭ',
                                                                            'ҹԛʁҪ˦ąǡˡȽÝíƇǀҼŘ˔ҎĹKˍʝı?əιĢÜ\u0379ԗ˲',
                                                                            'ҦȈ|ý³ςоŴϗǧŇӁΓǸȍэғiJʶƾƜ¯ƞ\x9bВͳ λť',
                                                                            'ŚǡɚͼԈԭϣȈÓӧӄԉƧΐˬŗūȇğĞʲǿ˺Ϥ}ɻΧҖКɦ',
                                                                            'źшĢʲΈaÞԘԐ½ÙʳšаǁЫΧɆΝnѲЗѸŨŉΉ\x8bϨɛĎ',
                                                                            'ѰÕķ˳ɽѼ4ԫɑˉҔTΖʀĻϮчӖЊʙДԥΐ¥Ĉ˛ҁͿÒĞ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϝ]Ǽ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -9183515320725165883,
                                                    },
                                    },
                            {
                                        'name': 'ςɫΨϑÈʵԖºѝьȸѠ˽ȵѱҗ\x92ʖҸ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
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

            'identifier': 'ê˛ύϐ\xa0',

            'categories': [
                'access-restriction',
            ],

            'messages': [
                {
                    'catalog': 'ÞƄ',
                    'message': 'Æ',
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
                'identifier': 'ʀͽ×ɂȵԈΏ˂ѷĥіʴԬťʤ\x97ǳ¡ƿ¨ҼȋοΤұCлҦșE',
                'categories': [
                    'access-restriction',
                    'access-restriction',
                    'invalid-user-action',
                    'network',
                    'access-restriction',
                    'invalid-user-action',
                    'internal',
                    'network',
                    'internal',
                    'invalid-user-action',
                ],
                'source': 'Ʀ¸ƽ\x9aěСϊAƳɁюӶʒӟϩȱ·ȫӍ\x83ȀЩŌьBˊ\x92ʒ7ҁ',
                'messages': [
                    {
                            'catalog': 'ґȚɛӫͶЁ˦24ĚɅǳŴtѾӲΥtϋɖ˰ӜŤ.\x98΄ƀqΊԈ',
                            'message': 'Ύ\x8bЫ˯ʖŽϬˮqʒ˭ɐı~ɌѺʣʓ·ñΛϨΨӝ#ҟ`ΙßǪ',
                            'arguments': [
                                        {
                                                        'name': '_¶ČǊӛɂԉZ ƺԎνӛˑɕȰѯҕɜХʃеØ§ĸÜйѰιĸ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԤПϙRѕØӦſƄř3Ӹ˄ʭģΞŭʠдԌĨш\x8eʮďʹѡӊˋΛ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173311.832259:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'µzψҒĸ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -742798572794807212,
                                                                        },
                                                    },
                                        {
                                                        'name': 'È',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 45501.13724814524,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȘҕѺțɰπǣұŐȤ˔@*ʩĂʧğÚ>йſˣ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'űVѼɊԏѮҀȰÑтѢËǎӅϙНˡΧԉȪӤӘԔЛľфӆӢ˂Ǵ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӪvĂŀŪ\x95·-ǘƶ˕ԛÛëōФϋШį˵ͺϊťǭˊɞ ŞņȢ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɟ˩ԌWİȽĒҜ\x98Ŧɖ\x80ȌһԏŋǃӪǥΕʥτȱƼɦһШӳΙд',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 195406.3073778049,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȇ˩ʆɒĞφĚěǝҧԤ|Żɛ\x81WˡԙƟȭ˨¿ţ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɣ½ŷɅ$ӤʯƺñԌ{ȽΖǼ\u0378ûэȹаŧҠƸҘȒŦʻӨԞџİ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˾Şжºі\x8cП\x93ӼǹųıȚʉƩgųї©҇ń\x94ͰȴҡѫəԈҎſ',
                            'message': 'ƓʩϽNσʰϋӝЛȋѼɽǮʃŰȫĒϽÈų;ªöάˈƬēү3ƚ',
                            'arguments': [
                                        {
                                                        'name': 'ϊΰɊѥɯǈ\x83ѻԟҶΜȳȁҦĚв',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'СϝΖǾ_˲Ȗԁ\x8eϼ=ƾϗśQζЉŖɃȥрÝ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ϲ˛ǭҒ@ӵɬρˮģ0ʄΐГƵЙƍҔπjҿðŚΥƶʘƁŋ@ϲ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʛBӍҳμkǻŋ˹˸ӉҼʛзΚӀùʳԍѦґήǗӓ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƎŠȗΞһƉɧƮԑǏԡ˾ȗЛɶǱχƇǀȴéϠȱʙ˞ѳѥ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɀж',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -9095758688870846683,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĕʐǰ-ӇCGÂV\x9cƍЀʸ˯{øϚɢƁωšōŋҲʋӳÇǭłɕ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6919222596528006636,
                                                                        },
                                                    },
                                        {
                                                        'name': 'cHѫʻΦ£ʰɸƔøоȝí\u03a2ґϐőЗɄя¼ΉǪүӃɳƶǿʧĠ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ͽ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'yǦųȲЫҨϛʆϤͶ²ӵ҄ƒɧōǌ¸ʿƦӥξ˼Ԇ%',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173312.477611:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƌǽӐÔʾЈѷɍ×ƞҠ¸ɇКȂyʈжСҙÃϚɘѩ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'żɒ˽ȸ}ϧǣψҜєʥǡԙЌɃƽρïЦλƙƩɣтѢƃҵµȉƦ',
                            'message': 'ȢȠҳԒΠ?ÜΨԋ®сһҖҲԑǷъBϹ)ʴТÎоɫχɺƿ9ʰ',
                            'arguments': [
                                        {
                                                        'name': 'ËÞ\x9bŌĈ8ǚ*ѐĔȿϭĨ˔ŴȕΨɸԅƣ\x8dлɖƜĩт\x80ĹˣĂ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 799568.0476861865,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѹϥ˛ќ¤ϺȎҽȬόҊĊҸіɓȻԥÃϮȪĨŔļ<ƒϭŪґňň',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɅăȶԘхͽЦ\u0382ӭǲŝi<ʖљˉА',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 237993.87441032496,
                                                                        },
                                                    },
                                        {
                                                        'name': 'МΰҨ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԍ˟ªŷΰˣӺŘɮUȑǂϗàÇЛ¦ȕ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 629454.9254376594,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƅ/϶ï*ǹʘÔüп ˷ͻԮüӁεû$Ͻ\u0378ѠːɁɦˣҊȨѦϣ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'аɡϗ¹L>ɶӯ˻ɏЏԩЕВԑ|ƴηʕѳѴüΕ\x84ѧ˟χŧЭ~',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 887335.2947928703,
                                                                        },
                                                    },
                                        {
                                                        'name': 'μaƳɱcɶȚʘȦȮҴȺ=ǥǡӠǮŽ˕ƶѵĮÃȈĨӳȬ\x9dХǏ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÍFdʳȥÁǽǥѻɖѝұôˢƍμӀчķxũеȎȖНŝ9ҥйʋ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 349567.9827429471,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѴƧҧĄӦґȴҼǮď˗ʭԬѠΜ\x93ВѷӿчӟіɓѩʹВˮРҧɾ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǺжɓӱŽʇq҆δɆҮǄÊĦƚƢĩ\x8eҢԔęɡĦũäӡљƿſÖ',
                            'message': 'ƜȲĤňȊñ˔ȁ\x98ń»ӇɜɴΒȧƆbԅ˾ǌТѦ\x80ɧɞƝЯʫΜ',
                            'arguments': [
                                        {
                                                        'name': 'ǩΜϋ»\x9cшȈÝԩĪ\x90ʄF>MGɴ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΡʣƔȘ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɒО҄Ȁǈ²\x97ǻǚ\xa0',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'oǑȸ˩Ћ#ƍқҡʀ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҨĸĘѱЬŋ>`ȹұњŘÖЛȬӞēӹ´ÕÊǚ˩ěњВӴǧůȣ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɥÙʒҘƓ©ПϲʐɘŇǥ˫үӍ\x87ǆĄǋӹƝ˄Ԝñʜ\x88Ʈƚȍ˱',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x85ÃʀҰҵшĞ˧ˑњԏ&ș¡¡ˣӍӒ\x8fπӠ5\x9dͺԉǶŢҞдɽ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'yÒȑϚĦæͿӪơʐЌ44ƨԛʪΓЄǙΚЭʍȸөԄˈ²ΣԠʔ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΉюµӐʎǸɋиʱҏϥ¯äȭӥӥˬдωΐŖҌӅϘyŦǡϓåf',
                                                                        },
                                                    },
                                        {
                                                        'name': "ʝʥŗ'ƑЌ\xadʗȦҵćŝʵɣ",
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173313.219667:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЬΒΘ_ˋ©аɣ9iʬǴҿɏοĖ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɁӋ\\ʸԭĕμˣƯȺԋ˳ʑȈӦӸɁѡ\x8dσЧʂѐ\x86ɲĴϿԐðȅ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ā8,ϹÕҚƨҼͶșԎ˹ϲдԇԢєԫŏѢǯӶәnӍɋԉѕ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6513674873086785365,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ÞΈȧϭĊӕʡԎϠuЏʒʰϒĖ\x9cɀϰˈ(ϽԠFřƜØ\x8c\x98ӍΚ',
                            'message': 'ԜμϢ;ԩ ҸϗʟϋϱūӅԆʅǻӷԄÐЕɝχÿƣǌɪқɅŉ˄',
                            'arguments': [
                                        {
                                                        'name': 'ϓĪγʮȣ\x90˒˫ɄјӥөӽӳЍήӑʐˢśË\u03a2ɱӾʚ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 805628.6184847255,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɶНҢʨȴ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "\u03a2Уɶǜ\u0381аϤнÆĴʰ˜ɨblӿɔ˝҈λҷ'ҎԠ˓ӷ˕ɠԇɠ",
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'μǷϲӵΙȄǡҭϟEҁҷ˗ԫ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˨ЙĘӃҳ\x9e<ΧˬȭԆÏ\u0381ĳŒԫƥѷ\xadʗî\x99˻\x9cfɅ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƅɒҷϸЏĄƮΒ\x81\x97ˉʶÞƬпΒȩû\u0381ϏµђĨÄLƊ\x9fƢǠː',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 918270.8870498174,
                                                                        },
                                                    },
                                        {
                                                        'name': ',',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˔ŢɬąӣɢŢÇӋѶӳǎʟǨø.ЬˋɌÔˆƆƆ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɐЀμωǖΎԗð',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'c˘ŝl\x93ѐΤҹзŘȎϹʚҎҒҽς҃ЧÙȤ[˸ƱǸԪ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5374118882055235193,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ԯë˓ѸĬ"ҕҢˋϭǶ*ΊƲүy\u038bσтɡ¥\u0381śÚŋԕӻ;ҏÐ',
                            'message': 'СέɔѧɶĠͻԏĲΐӝɱìбǩԗȺаïǒ˓ϴҋõ3Ϫ˥ÄӫҜ',
                            'arguments': [
                                        {
                                                        'name': 'ӑ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 447247.4938432666,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŕΙӰӜǆΊ҃0ǥBÙŖģ*ʁ҉\x8dȺɼ¼ÑБXŕʻɁǲѺźɃ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˶Ҩз˨ÎɄ?ҚŶӲҀ§ӧŉҁȐƱиʂҀĨˈӗpƔʝƍ\x98ĽΏ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ő',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 820918.909753805,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x90ѬΕoɻνʷфϜаQӧŕҘȽȅƝ͵Ā͵ԍ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͶL˟ҤɷÛТԛ˲',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƴĲɤòԪз´Ͱʳªş\x80иƺћ¼˴΄ыЋȺѝϟǮĉȃ˘ȠȦЖ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ė',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӧӁ\u0379ӡͼëИҖ\x9bʛû˩OǏͼʠЀȒʢǴ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʼŠĿǹǧѿϕ˚\u0381˞ԊΤΏɦϡǖӇλτjҭȎǖ;ʪˑӹɪϟ2',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѯčʞĚԀɚ#љ"ŻśϺÐϟ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˂љĚΤàҶ²ΌӨ˖ȵȦʺʕ˼ӃʶƢǞȹǖɃΘa@ԒϞčɀи',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173314.067085:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'үҖ҂ž\x88ѹЁΰ\x86ӉЧюȽԧаŬ\x99ǸОѤʦѰƀUƕϿǵĮҪ&',
                            'message': 'ǃӐʾоȴѸ˓КÇҢҺŽϨɉіӅǒɼʡũǹɴ˽Δ³ԪʱϨϡϾ',
                            'arguments': [
                                        {
                                                        'name': 'ԣԧʠːǲɌǰśϜƗ\x8dɯћу',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2569315092000230274,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȪΠŢqȁʓĐɾ\u0380',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƪȔɺ\x90ɒ·εÛȏƋЯYБĵ\x8cɿή.ŞѶ=Ƒƨ˚ţΆє§Vψ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 937485.9935612434,
                                                                        },
                                                    },
                                        {
                                                        'name': '0с\u0379âŊʉђGxѼȧ3ҀԏΉΩʥɥʮąʱӞƵԑԢжȣnŸ˒',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 731268.762608376,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʙӳї˙ħĥǮßЫ\u038bɋȍĭӱþӜвεʹϐŠˀӈĈъσþņO',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǏƆϽƒØԒo˞˪Њ;[ȽȊŪɘʥыɉѭΝɗŰ˶ұηɪsԇԅ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŵσ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173314.313597:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΚөʥͷŃ\x80ĮʺÅӴԇЈѣĒɱĂåиȌĠΙԣ³пƓ´ǟҭ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8811110447900970873,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǃœϒÛʳȽǲęȒѣ«ЖўƮ·Ŋ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˙^Ж)ɾѹɞƶ˳ё\\õѡԦȏȉĽɲĻəäŀЁµ"ƹȗǑУν',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӥǲ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŅΣӂąŧGźϧԅʕʢ®Ζΰǂӎ˩ǸнӊǨԪ1ϘщӛԡЈ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6758597074331711859,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɵа',
                            'message': 'ÊϝɳɈŤ˗Ɉ×ϡΒҘͲԪhӶϻϣǖJɭȔɺђǳӵӇ\u0378άіǮ',
                            'arguments': [
                                        {
                                                        'name': 'ų{',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '/Îˊˌhɯ*ΏўǲΩ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɜɫäƴԣĿюӆ΄ĪÛΗͶʑßǓƐ^ҶJ\\СҟbƗҖ˒ӗҚũ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΏȇѷÛ+<єǯц˲ɨſЙԅϝţ҄˖ʄ#ӃΌ¥ӻˣɺϬʩҷƠ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7954243408267550897,
                                                                        },
                                                    },
                                        {
                                                        'name': 'FпʈɟǻѓóÅʄļ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 765796.9770616029,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0378˼ťȹʦÁѾĵȼŶɟΚ$ԟФӎǀ\u0381ФѳɚýЀˁϚӝĝ7Ƅϲ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 15196.385856366382,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѹʨ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'PţƞĚ\x8dӵԙɽȦTġлʸûâɘ#ЃύɤCnÚΕɎˎƤÛ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͷЬǤΫύ˘ȸ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5917759856545018053,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҎҋȤʏɐɦ˪\x84¡ӷȄçӸ˧ѴʠÐѵһɦҼιȡɓї',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɋӬĊÄЫ´ѷŏǓ\x9bï˯҉Źÿɯî.ϬѠ2\x89һǙ#ԗȱɓϿ±',
                            'message': 'ӮϰˢȌʥȎюȴ Ɵӵ\u0380ʑ˒PƵ҄ʫ³ΥӺVƦƄîɂ\u0380ҍʻ\xad',
                            'arguments': [
                                        {
                                                        'name': '˾=ϿҀHԆԜǉЛĸ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĥ®vĵ\x8cŷүӂΐӦʺӤαɃˢɁʘҒˋƟƆƳҌзƀӞƽʑșǌ',
                                                                        },
                                                    },
                                        {
                                                        'name': '҅ɹ˦0ȔԖǹЂ˞ƺ1sхRƳӭģЄǚҾďȢȢƞϫ˭ҙʿˎC',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʤѬ\x86ƜƅϴϐПИʋϴϱś\\ԑ4ǽǟĽĹȀʒҭ˗Ҩ˘Êφ҆˼',
                                                                        },
                                                    },
                                        {
                                                        'name': '˙\x98ϝЌŴҵϭѻñҤø˱ʑʓÇÃӢƸϲƕ¸Õ³ԀǗǝΥȄЯĺ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -722927219959078832,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΠԓΌӜΛĸρҎƹƬȐƴѻҞӲS˘ԪӪ\x80ҏɧԞǹӓǐͻȥƌс',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ДИŁϾƏ\u038dӋ3ΟĻɳѧĎҷϘɈҀϣΎƶćѱη\x8aǋаϷƢγӜ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173315.039192:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӪɍȄ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173315.073327:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӢźїѴТȯϋϷlŘƂŋҽ÷ϗЁȊЕԠџQėďʏƆҺΚдˌƶ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŖςɣȎŰƪεЊӉѼŖӃN˝·ЃȽˠȠǏǙʑ9\x81ɣΉƄЇŷς',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʶƄЦŗϼǞǯӆɯϧÃŹҿĺyYˠӝєΞϼǵπОǐĴԬȉuÞ',
                            'message': 'ԕäȂѭєͼΓªɉŨӱƯñӜǢtǊʰŔӚѢûɠӿŷѮȱΠѢ˒',
                            'arguments': [
                                        {
                                                        'name': 'ʕÊ\x96ΨάgԝļӷЭ˃˫ʘĻƷƹҒѵǽ1ɬҌƔҲɵɯŕѶЖϵ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'бǱҎ\xa0ƈΦ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5579770711345996039,
                                                                        },
                                                    },
                                        {
                                                        'name': 'BNʒʕӇ\x8efЏɭɫɗӝßǦˢȾ,ƹǓƨƲңuî`рϸŏġΘ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173315.246117:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ДʄɥǷþ҂χҾΪѲә\x9a',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 258395.285631168,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӫђĬɺӭÓǑϭ_:Ԟ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "ԎԄơӶĸʔ+ˍͼԡF'\u0383ӾˀHƘǢȥɍǏƣӴѷĭ\u0379ǟΪ\x8dȇ",
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȨȚÜӷƷήë¯шÂʲρŢƍӒƈϛҘ]tíŖΒGΖҔ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5430887370385209433,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x92Ί\x88ğȽӥԠˁ´\u0381˝L˯ΛΏǉš',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƛʖ`ǃьʘγȐ˖ÜƘ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'qʰΚǾf0¶ïѯŀʬSӃȜˌόͳ˰ŀЁƃıƭΕѷÚˬÓϖˆ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 341639.687472453,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ãěσ',
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
                'identifier': 'ǬíŨҥɵ',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': 'ˡθ',
                            'message': '˯',
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
                'identifier': 'ȷтоҥυūʜÕư϶κÀЎԈӶ/6üɰʣҌҷԊԋƐԛȐ˴ą¬',
                'categories': [
                    'network',
                    'network',
                    'access-restriction',
                    'invalid-user-action',
                    'access-restriction',
                    'access-restriction',
                    'internal',
                    'configuration',
                    'network',
                    'access-restriction',
                ],
                'source': 'ʌƲѭǴɾ\x85ʋаϫƸ\x9eUΰψɳ˖ԛӃǘӈɱķҘ\x97Ҝ˱ΚT҇ˆ',
                'messages': [
                    {
                            'catalog': 'Ҫ\x9aāśłĵӷ-ɗӾrӤҺɳ_ӮúiӟѱώÕmĕǩǩƞ\x80ʨӨ',
                            'message': ":ÉŢ˒ƴĠ`чèυѧȋƊаϼǧΡ8ҾӅɅʓφщȴBȹњ'ӽ",
                            'arguments': [
                                        {
                                                        'name': '¥әǡM&à7ѻʩϟЀɀʐўǀϕǀΧĿӤˢȁĂΦУǸůΏŞń',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƃԫʵ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173321.739932:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɶ¢ɶǚ!ӆ\u0382˻ϔϷЁȑl7ӌϻƏ˼Éʚ\\ϞłϺСŶʌνϢЩ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173321.775301:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϟXYΏmҁ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȄϮǒώúƵ˒ǈҎԬȔŒ΅ĐƦυȔəǐψ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x91ѭĎyԐƼGθ\x8fƏςɋ\x9fѽÙϲϷ҆Ͳ¡Ãǰǅϭǁ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˍśȚӶӋ΄ǢʣȕȩϗоƶǱ\x9aӶǝͻТŏpvɺʤͲƗҊʹÊđ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 352437.0362725542,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʄ3ӊóɉȌ\x98ǜſϊåДϒϙӽ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɏȞȹǡǩЫӐҲΉèÛȴȌĲӤȵơ!˕Π\x83ʀ,',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173321.984330:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʶöжҺФΚϔ˥ƛΕΰkŖХëîүλǃ0ήЗǽдф\x8fƍΖ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƳŐӊÀүҠs˜ēϰđȿЧÒŠΟxıҙÕƂư˖ŵƥǿʄ˚˒ϭ',
                            'message': 'Ɖ\u0378ʿɿχʯɖǁμƊǢʆˏԢƻǓ˂ԩȺƇűɷÇ,ϰуɴ{ˊČ',
                            'arguments': [
                                        {
                                                        'name': 'Ďӝˑƽ\u0382ƭΥǡВϏԫǌˡʊӋѕɁщΤīϞʫУǾΈғεСĕɮ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǰĕ҅\u0379İҳŹɡ˶˽ŀϾ\x7fЩYǘҁλΙǁſȬϵŲңŬĩϤ\x99ʠ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӮƗλ˔įɈ\u0380\x9bЎЦ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˊ҉ƜӫĔ˸іԒ\x9cʶӴБ\x81ĸӾӧĞť\u0382ƄӋèȁIѯвÌĮđ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĭѤC˼ӟbƨͳԕɯǍҥ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӽǔȣʩèʡԡƷљŭˢδ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӯҦԭřЩƾ˲bβңƿ˗дş¨ˠɵӾƻǓζŢfswϠΜ,ϴò',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӧKЍɘʎͿЄiŒH˩˴ΛWǔɠ%ҘƇ§˯ӎʀe',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'òыͱˣȀÂцȏơмэӖőŴяΖлӢ|Ӯȏҿšɽ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȗԝɚƨʩBĖʛ\x8b_ӠӁãǓĦX҂ΚӇƦУȈ҈ҴҕģĳΌQĻ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ͱ1ϖÁƑɺǍ±ǔЗσɷѝʄȦVԬŷШ\x96ғӺόϤҐԒƁªĵ˃',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3051063093383190802,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɌэƳƶӐԬ\x8cĕ[ƶÁgɅ˰ѕȗɮ%ěΈǫǱԩǗӕ«ʡӋӇΒ',
                            'message': 'aѱϖӊΥӮǢҦЀґӌbƼЍˆņҥʲ˨ӯMȀһÅƉȡˉŠÑǑ',
                            'arguments': [
                                        {
                                                        'name': '~ВŐǚԏXˬƗϭŷԏoίʯf\u038dҸѰҢĖ˛Ù\u0383Ĕφ҆ȨӤƱʀ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'VԌЏȆɪQ\x81qʝ\x9dē5ѳRöƳЩ_нӰďԀǀçÿРȠɖˠϗ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1577995191005907065,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѮԂӹϴдВҶфѾƶϿ½Ł',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˔ҩƪƝ˼Ԝκҝuʠ¨ЀTӄɞƀƴũȯĘӳˮѯȠ£˶ɨғˤӖ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƄЇԍǖînȵɦє÷ӺʞΈҙŻҿРɌїǅɊЭØƫϋǕ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˓ǪąȾͳϘʷҀÈƓώѢȆϜǠƷq',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "UȅɖӲϰҮɓԙɊҶȎŻΆӍƥǕπΓ1ЕqΈɐϡŦ҉ʿȔƬ'",
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϤϝŸʓӆƻљҔÓʝǏӥπʻϾǸŁſΜɎ¬ѱ˔τ(ϫƾʄȊ<',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3749100162285839106,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӧòαżɀ&ҽԕõˊ\x85vάʐǎĊyɗѼ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ę÷uρѦɈӘӓʻǗԮe҂˗Şͺҁ\x82Ѣˢï˨ϹåB',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '«ЃʘĤ¥ʞ\u03a2Ӂõǐсəӑ|Ƨє\x82ѪƄ\x83ųԠƔ˵\xa0ˆ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x8eŲϋРλÔϹƲǆā˵tĠǦТɼϒŶǇóϿʯáɌƴ˃Ć&ɝy',
                            'message': 'ǓiƖҠǤʢè²ťǉÐɖɔ˞ʟԒȁЯʐɦƟ~ђǺΘгϊōȁЏ',
                            'arguments': [
                                        {
                                                        'name': 'ǮÓ+¯dҜĆӯ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϜíϻЎ\x94ȾҐˢ±ΑīȨʒűĆǇ\x91ýǾԄƣȗγО',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1254439554200419103,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŠˮƎŊũʟԟʚЂЏȆǺ˯˂ͶɺѭŴ\x8cԔͰʊ\\˶Ĉȟš',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ţυюϰȈЁҙU˷ϝŷӒ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȽˤʹĖт]϶ĴćĊː\x8fƄȓіΐ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'EМƥΕ\u0380ƿϾ@ӛǆːǄ*˶ӤǰȰĘϪ-ϵЏүƧ}ԣĈˈЄț',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'FƀqǂƤ\x91ǧĸļӪαіΘǅˉ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӗŌϣϵЁԌжťNԦХș>ћȱӟɮȉÎʌĎˊƶѨΆԭ Yʌԅ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173323.105105:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ČȖјƸʏΑӽ\x99оÛʱʰҤ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173323.142059:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɼϜȅ|ϼϐːяԪȷȃrŒϒYũʳȆɨēҷȳʐЩАùГϖҕҗ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173323.178462:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'τҵǦӭƞԠѾͻŐӞƬΆͺѧʷҧЙƬäԡþʘˁeĥѐʛҤЋǷ',
                            'message': 'ɆȓóбԛØʀѴƞȹżҲǵʙȮԔϪŝӞťѳӎȆҒӳǛřŹ^Ҷ',
                            'arguments': [
                                        {
                                                        'name': 'ъзŔӣġ\x92ƧǽӁÖԁ.¿vś',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȉŖ˾žӿͶΝŎů üГnʔ8Ҝnʩ˻ȳș',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ДϘˆϗϯǔċĨ¢хˣǱԕԘʔΡǈτԤíΑCľ\x86ΉҴ_ϫȞѤ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 300767.43102860724,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Юĥŧȡă˰ÕѮФŦɆǈȪȘѝ\u0380ŏс΄ͶͺО3ɳň˘Ωͱ°Ҏ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Þ\x93°ѱχVȇǯƺΰӈİ˄ƻ҇Ů·gʦ²ѡȄɞtϹðˌόҕć',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѕòӿļĴϒɯͲŌӍҸԈðЍȔɾӃĽè\x83Γ\x8cӇhҩƀ\x90ʖĩҔ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x80БȳԊ˖Ґðţ5ԜΥĴЌШ¤ΙİǴȷ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '{ɮRӛКȝа˺ͿєɂUϼԞ˒ɚįѷƏƧŻUÖӂ˔Ҷϼ҆ßԫ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĀʉȼĆť¹\x9eζџ˳ƋɞΫʯϫƁоƆόϥſӅQɤԎ@īн-Ҕ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǡȄŎ\xadÑ[Τ\x83ΧӘԀĺǭθʃ\u038b\xa0źµɵӵӦƥɭʢ\x80ϗӚԬŐ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ǫ(\u0379ӘʞђÈХѿÈΦжěËɡɻͺŭ˴қĉ˵ԋ\x84КʿΆͰπι',
                            'message': 'ΒÑŶЅƯôΰԁԩӬJ¶ȇΑʐɯðʇǌϊβԤҁƴŦҖӍņԂӣ',
                            'arguments': [
                                        {
                                                        'name': 'ԗˍĬЄǊѽ˟Ó\x8aό\x90\x89ЖԢΕŚăȒő¬řЂũԫȷŒΰӉĉǣ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ИƆѨˤɔѲ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 656494.8508194202,
                                                                        },
                                                    },
                                        {
                                                        'name': 'БˢӉZǼыʾɔêɓӉРŚǫӲ˜ȤЪʶŗÀҮ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʇƧʐӈ˳ėþ˭ũЏ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѫʪP',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƮϑkɠΣԞͻŠɗ\x92ȻюD˧ńГΠĿñԉӸΡʦȠѺÖɹv^\x93',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʋ\u0379ÞƜǮ˞Үƥ\u0381Ʉâƌͷ˴ӚϿΑѫЧЋ0\x87ԮʒÕɥiӖ©˲',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϕƸҔґțѳґ6η\x88ʃļǿωσӃĎX¥ɑʢϻԉЅǍДѩɄ5E',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŉųŵϰϗɷӃĄƬˀЅ«ӲѧӾćŀāϨЯҸҾԡ#әʲҸԍ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -339229802581149468,
                                                                        },
                                                    },
                                        {
                                                        'name': '=ĩ\xad>ʏÙĪМʪżԎα>ӔTȒέͼñǕԐО',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 9212627736364926741,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɯøĞȥҐȘȗ*\x91UѧӘƸ˨ΧƿǖģВZ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 301323.7217596422,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\u0382џѼġ˖ӵƻιc²Ȯ)\x9aˇȅ˟ȃ\u0380ҫƑȄʩӅºјȺδԧĀȖ',
                            'message': 'ԙΩɄźŐ҄Ҽ#ѻƌǷʉêxƵǆѷќ;ѣıƙδҔĬΡŮÕ¦ɀ',
                            'arguments': [
                                        {
                                                        'name': '`ʟɚϳÏÆ\x80όȀʆʔź˸ʷϺԮďыΫʝšÄӤѶˎĜ\x9cǐŬȰ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ōġĽƢϡϹӏɵӹҬ\x8cƫǩϣÏŵбѻĎӥȯØˊDΆYĤΖ\x9cơ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҥу\x82ʛ˔ƩθхϨΓăь',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ū˔ӣԎїȅӑɅ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӢɋѻӿŜř[ԅɦźɪҶ\u0380æҤʹžɛȎʕ˪ǗϛƄÅȉɬђe˧',
                            'message': 'ƇĞμǒёȰϳ˲ΌʄЉʭ҇Юāĳģ4˜ʡʴΉƾģњӛˡϵΧг',
                            'arguments': [
                                        {
                                                        'name': 'ĖeƹпƨŦv˧ҎӟÊμ͵ǣǻ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԌƊԘөӁҴώҬɔсЛϷԦШǖǵѩʆӵzáԖƿƄ¢ӣȬĪϖɾ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҹi\xa0ўɃǯϻʓɭǁťɝԒǉѯȆУˊƃӓǪѩϖҐό®ЦΑ ƶ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'čbǼęʾËΆЉ?ŗǢҭΛӜϭƍ˧˻ҼσĜӕİʭȞ˟ˉҊů҄',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÙoɄмѨ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'MŷgŻÅӆҲĎƫѱǼӧ˪Ψ\u0383ȁƉ\xad˟}ӝƄҨƩƭԬǜŜԬѥ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɈŉƒщżȇЭώŞмѩһ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÉԒНȳϼӣ҂Ϧʢ˵Юz-Ƭϟˣƺī[ЕγǆӃˬӲΗŢʋ¾\x9e',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173324.020135:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'iɉȎЋͺƬğȂɹJʩ˼\u038bҍ\x8eԛΔѹ/ўЗÁƐɫӕîуʰԓА',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˨шǱ\u038bA®ɹУϾνɞԘЩǝЄ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŶԃϢͽ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'YФĊуȆԭȻϚȹ¯ԤϾԛϼƏӒ˛ԇҋʏɑµȦǐҒΆ;ΈӉǨ',
                            'message': 'ЃґéŭϚӅɮÁȝΞĔ?\u0381ɨśԙϭ©ɸȒǳˎІҳjХÌɥұѹ',
                            'arguments': [
                                        {
                                                        'name': '=șIȲȱӭϕ˦Ā˓ЩȂԑ΅Ƈ˾',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8488970785953533560,
                                                                        },
                                                    },
                                        {
                                                        'name': '±ʘψҍӖфǯÄŃȝđ\x8bίĠԠ\x89ĺЙRńȧпſtУǀʥ΄є˔',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'иҪҫƙǾβN\x89аôŽҒϻӌЊѷǤϣԭΔ˙úͻÎѫ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'lΕǳӵϳǥȆӨĖœʎ\x99ЉɚɸҮАkƏȠbΤЂԈʸήĉΣҔѾ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҪҡårΝϽԜoԥӸ.ϛŚҍѽӢѓɸʄπύȒʌǅŧҩȮѻgň',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6781388023490695317,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ýÅÄĚ҄ɼŎ5ԓř˕ĳȱΦИǚA˕ύҜυ˚ıš',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173324.254563:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'â\x80ϐ\x92ԦǴê҄',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǝïɖĲ¬ѭͶϢĎнҞƶ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Гɲ˗Ӓ˞ʠƒǿ!Ĳψ˝2ӂɊ¾ÙƍǞǑǡǾԑƋśǊȉʛĵ˚',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӉϒӁԮɦƨӴźɧӷĿɴ\x84',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ªǇ±ϫΏȺȚ\x90ԩíɨА˺ԣїΒԉψЙǷӤɷϒӣͲúʍӸʔԀ',
                            'message': 'ȹƒɹĪ\x89ƽɏȿɜϑȈėңҝҩ\x8fČƭч\x84ң҂ĭԔΜϏӸƬҌω',
                            'arguments': [
                                        {
                                                        'name': 'ЊÓнȈǘңΩˤǻʥ¯5ńƾԦνƍǵХ{ЍɕĢ҅ĥƒÌȧҭд',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҧ·әɗШȪêɿƏȉŐʥÂлśЄӧǆ˴Ȗƕďȭ\x85ϕ\x82ƅ4ду',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЀԂҨѩΘɰǠԊЖϊē',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɠϙʚͺ˽ĆэˮÿʯǝȎÜȀΔӋКȴƪȷʾΑƗIȣś˾\x8aƘ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƞӬ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 64715.42477524243,
                                                                        },
                                                    },
                                        {
                                                        'name': 'αӐŨкӑ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ġ©Ͱϣǐдͺɤ΄ʯʀ˰0ϪӮ\x95\u038dʸʺʡЈżΉѸʭŢϾǳȟ˓',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173324.535441:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŴŎʓԭϱЕёȭ=ѪƀǢ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173324.558834:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '[ӆϞʗљȏʊŪäΚƢϓӼȨΰVӲNØˆя_\x96ČңΎΉɽȬє',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'cн',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173324.605462:+0000',
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
                'identifier': 'ц˃˫Ԅ\x82',
                'categories': [
                    'network',
                ],
                'messages': [
                    {
                            'catalog': 'Ыγ',
                            'message': 'Ӗ',
                        },
                ],
            },

        },
    ),
]
