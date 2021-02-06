# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-06T22:09:24.435119

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
            '$': 'ԋƲĜʻʭҦФƼɴʅƫɟēІϩ0ԠǣЃЂί²ӋÇąҥҭęŻȆ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 7836004106958121579,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 419731.17311777774,
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
            '$': '20210206:220924.326958:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ʤдιĮӮȧť\x8fцŋԕģɩϹȽϿƯǡǖȭXϿƸҵɽҦҭԍiǕ',
                'ЉʚБʤΕēȅf½ԦƹQ¡эǵΨȬȪ^˭ѼȷĦœ˝ʁǁӥƚ\x86',
                '^ʍЃщ\x86дÚʼǐˏ]\x80gɫЈУλ˔Ɓ6Ӳɇ˾ƔŉяΊƣ˒Є',
                'ǱӅʩԎѓ\x9d˞ѸϋʼƊƫ\u038bґŃǥȭ҅˅Ư&Ü˰ɗ\x9bē˾]ġɋ',
                '\x8bьӠƍθТʄ2ȈЁˏҁʕƏѫγŐϙYɁãŎ˶уΌ˸ѪķŴţ',
                'З҈ɮ˲ӍȮɔ˭ăʸʜKȄũУю˨ϧЋɍ§љˡǦ¸ѯϢƵnƺ',
                'DǲЗϋҰʰƲǼʦǐƩɝЯԀқȎјǤǾДжҙʺЭ˳ӢƍY¶ʸ',
                '(б\x96ȪўҒΛƗȲ|ǈT4ǧɑ\x84ΙŴʭδƞ²ԝɼИҸЁˏŀɳ',
                'Ƒ\x8cˣѝ;ЯѱnʋӇѳѨƻƦС͵ǼǐӒŞǏʒ\u0383şɔ\x87ŴԨʿǌ',
                'áȀҤɪɅìɓцĔËȗŋӎћӉҋÔңďůĥĢʸ˺Ѩ\u0379ÐӦиЪ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                876759171891951511,
                -8612840684495480897,
                -5533346780247095809,
                -12634817235815644,
                -5775336018183900983,
                -6549724076354403856,
                5940388380400675314,
                3372244604503286123,
                -522209082651067306,
                1118876304434573531,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                412875.1022275882,
                5309.439378448515,
                717783.9778882887,
                -18795.78358667463,
                636329.6834707966,
                84549.2706810243,
                664438.7912144247,
                499173.6619597293,
                283598.6124042217,
                733648.7716673512,
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
                True,
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
                '20210206:220924.327939:+0000',
                '20210206:220924.327951:+0000',
                '20210206:220924.327957:+0000',
                '20210206:220924.327961:+0000',
                '20210206:220924.327966:+0000',
                '20210206:220924.327971:+0000',
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
            'name': '\u0380ʋīӲʍӚȷөȨõƮюſçȯǮӱŏщщҍƠӁЄʞ©°˂ӤȆ',
            'value': {
                '^': 'datetime',
                '$': '20210206:220924.326756:+0000',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ȉ',

            'value': {
                '^': 'datetime',
                '$': '20210206:220924.326822:+0000',
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
            'catalog': 'ϮҔʥћϼ\x8bɕƾʋȅλ˝[šiԊ]xɵ ХĶ\x8e@Ë\x82ξɪЧʝ',
            'message': 'pѸ!ɂò\x84Ϲ˯ǖȻȟө˾ͷÓ²ďѨlѓҶeσǮ\x8fjzmǧ\\',
            'arguments': [
                {
                    'name': 'Ɍ\x91ʯaɒĠɠ¤;˺Ëȹ\u03a2ψƄØϋԋʯëҺ\x87ѧÒɯƄҚϺˬɝ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ΙôΣεIĝϯɚ!ǀȶŊǨŊ©ɏƶèƮ\x8dҗſуƐӰȓɧҺ=Њ',
                                        '˚ЁɧЉԛ\\йƠȳϝʑŲѷƱʸҢ®2ʚûÍbѥğŻȔΧкƜԄ',
                                        'Қ\x92]!ǹЫʴԧ҃ҶǒÑ˝ЎѯƤŭоɸОa_Àè-Αɭŝӫ҈',
                                        'ˌϝԚǣ;Ā÷\x8d˛ȉӨэəсɒǴΛәɐЋ˔ҸӞŸKŏƸΗE˶',
                                        '~ѽɓƾȻ9őҟϋąѝҔ΄\x9fԡϵ+ƩφCʆŬǔыɗӁÀ\x98ȋҖ',
                                        'ΐҸεǘ\x82ǨuʹσҴā˔ԤЎǳ\x91Ǩ|Ţc˖ŠĄбǦƷӀϚсˀ',
                                        'ƌьȥ`ʇƁėTԂ!уВ΄ĈȮ±ζ´яıʚӰ˚ǘк\x9fԜΆ˧ć',
                                        'Ȅεҭ\xadӁ?Ɔΐ˰ǻ\x80lČ;ϤӯӼϊɎԃ˳ʃˁΔƚâɽÖfЎ',
                                        'ԋәҹǩCΚ\x8eѿŖşΪĀÛǖҜϚÜЈǇĦӜѐƎ˙óбȆƄƀ\x9a',
                                        "ӲӨʓŔʲЛ´`ѐEǖԙēǏŞɔɧʄɈʒӷϟ.Ãˣ'ŧϨˏl",
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ә\x99',

            'message': 'ǝ',

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
                    'catalog': 'ZqɓÞǋӹȒєԟөԘțƤѧɰūб´ʬʦʖkƟɎʮǓÑʈʫԏ',
                    'message': 'ȍʚǶŎԢ\u0379ȩǤɭҹӤāҎӮȵӌϙΨƑǿǀʟȻͼӤбӮсƾɛ',
                    'arguments': [
                            {
                                        'name': 'çʄƫҗśRӬÏ\x97ϨĲ\x86ǽɂϵνӕ·ńХҝǲƁʐƇџϫɈɞŻ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 626598.2543475963,
                                                    },
                                    },
                            {
                                        'name': 'ʉ˴ģˋ·\u03794ӷƩқǷ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɤǈºцҟɛҏŤď\x8bɑˉοøѵǽϑϕ±ԐɒüӍǼɢˁ˙иɊζ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʊ˄ā˜4ƅ˄εԘд\u03a2˥Ф˭ѓҍσӴʊǛȎӶ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5619767067949283100,
                                                                            1713724554845639353,
                                                                            4196350703004207425,
                                                                            6352329689778880708,
                                                                            5116661383517350537,
                                                                            2767453021167977993,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɆΔҁǋәˤ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4693575916533868660,
                                                                            3655987975777263695,
                                                                            3339068628836462151,
                                                                            -5792110841468718712,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʄɿȨx¥ÈüŒώʢҬvёҠʌͿˣƶϰéς',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220924.294582:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҷŮԥїҾ¶ӗư',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220924.294821:+0000',
                                                                            '20210206:220924.294834:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʄÒǨʝѨ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ρͼ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '¯Ήҁ\u03a2°ϱ¡˼ϩѨԮ,BZĳӊӐ˜ǜ÷ȵŘЈŌΦǆNЅˋɃ',
                                                                            'ӧұӾоΘǮз&ӖƆӤўϳƷ¥ϩƃш˭\x81ӄдɴҺǂ˘!Ðã[',
                                                                            'ɿʃȍ\x9fƠ0Ҟқүѕͽ\u03a2΅ȡƧҫǒÐϨˁMuԈ˥ҋGқØƢŅ',
                                                                            'Ɋıjźī˙δňћêĴҸиʖdʷūŜ\u0381\x85˛φѲƗÍ˨ԋϾȥΉ',
                                                                            '\x8aƁѾ6˅\x97ŢɤøԡûϣâŽнαǶΪ˟ʧǛэҠÕɍ¿мĹЙЇ',
                                                                            '\x8eϠ\u0383±ү\x9fӄ˒ɹΜΖʖӌÆıҏɜЫҬСáŊΗΔ˫ϜʏǯʟȔ',
                                                                            'ĔШĭȨ˥ƖœћҭʠˢƶʫŧХÀÜıѼŊǒǍ˭η˵НˁѮȾʿ',
                                                                            'ѮԖȡӁʗԀãũ҄ЗԆɶΨ˫ɭήΞҥɑƿǒΤś$Pǟȱ\u038bΏǗ',
                                                                            'ʨӍʭ҃biƩԥНХƛNÄĎеӷêҿTĻȦЩþ_ŬVѠȹƛθ',
                                                                            'vǸǵ\x8dґ1ѵѨ˝łPéһƻұЎĈ¢ǦӍĻȾʋĔ \x96ЪêϖǪ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŘaƗ҈QӯΓƙYѫԩӿ˖ʷѢʃΦǄǌʱъÂċԜ˳ϷŦ˾Ё\x95',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220924.295737:+0000',
                                                                            '20210206:220924.295750:+0000',
                                                                            '20210206:220924.295756:+0000',
                                                                            '20210206:220924.295761:+0000',
                                                                            '20210206:220924.295765:+0000',
                                                                            '20210206:220924.295770:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Wʅ˾ĈƽʮʓǯІğ¢ξ˚NϯԖ˞řƎʐϘȩɍΩύԜʥìĮ*',
                    'message': 'ԠƂϖҷϊŽÝҨǽ>ӿΒΙĢɟŎӚˌɥ\x81П˫ʒ\x9bӳ҈ϛȌҵț',
                    'arguments': [
                            {
                                        'name': 'RѯӭҀŴ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': "ʾ\x9d˨ЩҁчeǮʒӡơΕӫĮ~μ'ϐɵϾ¯Ҕұ\x99ӝȩ\x95ϻºÓ",
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6036669317292472396,
                                                    },
                                    },
                            {
                                        'name': 'ˁѝȜԍщľђìuýőǈƥ¡ʹǑǹ˘˝Ť˄ǩ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŵԁɐcŎɱƑʂЃZåǯʊϬ¾ӇҲǜɴ˅ĵªȧƔґΏĆԤ˓Ϻ',
                                                    },
                                    },
                            {
                                        'name': 'ҳшӕ}Ќ ΰҏ˙ĕ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ґćǲPǋӟÀ\x7fŐнÁ\\ȴ˥½,*ʘ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            32187.635634688282,
                                                                            196364.98115707847,
                                                                            715336.2884934818,
                                                                            660126.83796156,
                                                                            372115.37711272767,
                                                                            299107.8364820378,
                                                                            770816.304130026,
                                                                            771055.6843041328,
                                                                            80449.78365679632,
                                                                            940486.2262396903,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҁŏқ+έӒɅˑ\xa0',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 705956.5032715349,
                                                    },
                                    },
                            {
                                        'name': 'ǍŠҵӽԮˠ\u0380½ѐɴԄ¡˾ǀӚųȋ˗˦҂\x86ѮҼȓ²ʬҨȎԡ¡',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220924.297387:+0000',
                                                                            '20210206:220924.297401:+0000',
                                                                            '20210206:220924.297408:+0000',
                                                                            '20210206:220924.297413:+0000',
                                                                            '20210206:220924.297418:+0000',
                                                                            '20210206:220924.297423:+0000',
                                                                            '20210206:220924.297428:+0000',
                                                                            '20210206:220924.297433:+0000',
                                                                            '20210206:220924.297438:+0000',
                                                                            '20210206:220924.297442:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'һüѮǿӮ˘НЀιųˤʁʜϫÆţÄůɯĐͱƂ\x8fʞ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Эʢ5ɁœėȵƟõӯġ:вΞϟ\x9dγӦΓѪßĪUŐЄЫΎ˨Лӝ',
                                                    },
                                    },
                            {
                                        'name': 'Ǚ´\u0380ӹԃ\u0378ƂëҪ¡ȧԤЪ\x8cˢXͱ;Ю\x92Аԣ#Ƥʦ§ҷĬŎҒ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'PƠԁɾљʒʈĠˌȏȰϗķǷƮȋūÈƆː\x9d҂P˃Ǿ˂Qϣϓ.',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -46093.5362439133,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ɠø7ҢĂĐЦɐ<ӋӋǢҷɼώїȧyŢδхý҉їŵÔPqíɫ',
                    'message': 'җНҋŜŬŬΘ\x9fūӪȱźпŖȏ\x82ɸҴĴĚԣS\u0379ˈƚĻɅÚ˄Ӓ',
                    'arguments': [
                            {
                                        'name': 'ˬɴ\x92ҟAʩDƬё¼Ӑ?ķ®ԋɈϵ´GéȬѠ1ȝԦˎɭˋΫý',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʈѯіɄԁδȬШȊʿчғÆ\u0378ӟ³ӢтƕòѢҤɻĝΞѼȩǰψ˱',
                                                                            'ŗȌũҀѥǇĊǫϓќɁήŦӦˮǋĵǛҐðÚɜǉɎуɎìɧʩѱ',
                                                                            'ӦȭԠƬұԂQ¬ǖϽƝͽEɏΎ`ĖӖȴɡŹӈWȀōϾζʌ˴ă',
                                                                            'Ĕ\x85ԝʿɶʌÖӧÊlʾŒпЃrÅ˓ԅ\x8dҫȈSͱΝ»ʜƎӟśǎ',
                                                                            'ЊĲΞͶN\u0382¢IѾйƍŴÛȒҠѩŸˬçӀӇ˺σӶB˼ƆǾшĴ',
                                                                            'ɰɆҾʕ˸ҚгÃĖĆǟ˴ſˏϚб˺ȀҼĜѕȊʵ{Ӝʴϋ±Ϧд',
                                                                            'δԋǤЍ"ϱ¯èΤʜɷѴ˥\x9dɭԔƍ\u038dǬƀJГϦŦΨ˥ű\x88Ю\x94',
                                                                            'ɠ˄Ôɦʜż~Ƌѯ£ʟЮӮдМYǬҩԥƪё\x89Ćʶԣ[Ɉ»ǩ\u0381',
                                                                            'ȎƵîԡˁηҥтãȄˠ7úŝƢƕЩӘЉ\x9eȼԀtʔŜɟŗԀңƆ',
                                                                            'ůџ\x8b°ŲîƱхǇЫҕēʆӏмѹPͻwġÎîˉȠͷ÷ӯžҞĲ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԡ?\u038d~ϕǉʓǙƢʲˈɋ˟Ԋ\x7fѡσҫǃƹƐϗ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            355728.12685774727,
                                                                            17542.027419834238,
                                                                            142963.32715440393,
                                                                            337826.0241729205,
                                                                            747014.5501109904,
                                                                            708815.5911199729,
                                                                            611264.5991761676,
                                                                            439255.91538269096,
                                                                            976132.738342922,
                                                                            495697.68638472655,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʊɷ¬aӌӻʊӕҫĘμӋӘʌσˋǭČ\x8cϔʤЂ\xa0\x94ӴƚʒkƺӞ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220924.299255:+0000',
                                                                            '20210206:220924.299268:+0000',
                                                                            '20210206:220924.299274:+0000',
                                                                            '20210206:220924.299280:+0000',
                                                                            '20210206:220924.299285:+0000',
                                                                            '20210206:220924.299290:+0000',
                                                                            '20210206:220924.299295:+0000',
                                                                            '20210206:220924.299300:+0000',
                                                                            '20210206:220924.299305:+0000',
                                                                            '20210206:220924.299310:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɍ\x88țǄбUЅʹyϠʔəԞĩŃҚϤÈіȧҞȬϳŬǛ΄ģȠŜű',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            709374.0379198423,
                                                                            624271.87084243,
                                                                            551017.0932688619,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΜśӗʣŧëҨĨʯѻj\x84ӒȢ˓žŭҙшХςĕƙǔӆƯ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220924.299929:+0000',
                                                                            '20210206:220924.299941:+0000',
                                                                            '20210206:220924.299946:+0000',
                                                                            '20210206:220924.299951:+0000',
                                                                            '20210206:220924.299956:+0000',
                                                                            '20210206:220924.299960:+0000',
                                                                            '20210206:220924.299965:+0000',
                                                                            '20210206:220924.299969:+0000',
                                                                            '20210206:220924.299974:+0000',
                                                                            '20210206:220924.299978:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ęǄϧʵԤҋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220924.300182:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Jʯǣ7ÐѦƹ˽ѬͿҪŖʯϢӤƋʙ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            9204742026753578257,
                                                                            -1444047027955575602,
                                                                            7058510418920764174,
                                                                            -2484640223813375674,
                                                                            -3740340704493342565,
                                                                            6672440034319454493,
                                                                            803119416506877046,
                                                                            -5788573864593155595,
                                                                            6805963463664217985,
                                                                            -4359998168301417594,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ιӀTӈƤ¨ƅэβū˻ʸϿʈÑηΰĈʲϩăӾĸЦƫƣδȲƂǒ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220924.300548:+0000',
                                                                            '20210206:220924.300560:+0000',
                                                                            '20210206:220924.300565:+0000',
                                                                            '20210206:220924.300570:+0000',
                                                                            '20210206:220924.300574:+0000',
                                                                            '20210206:220924.300579:+0000',
                                                                            '20210206:220924.300584:+0000',
                                                                            '20210206:220924.300588:+0000',
                                                                            '20210206:220924.300593:+0000',
                                                                            '20210206:220924.300597:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ſ\x98ӝтɆҫHk_SȄӻюȺǷĺѼŷӄΉӉĢħ£8Ś\x81;ӀÙ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƻ˪ёүǊ(ϱ¢aƥ˻LԭȾȑϏǦ~ԪӲŶ¤Ā҃;ӑԎɐưĤ',
                                                                            'ŗǞ\x9cɻɴϢӃǊÑŒ҅ˍìɡ½ŨԈӢѤēVɆ˃ǯқѯȬВÃŌ',
                                                                            '˛ө˪ǴɥѤƏȫȭǹɏɃƼҜˋӹӋŚˠÒŸɥӋøĉцӎƮΨј',
                                                                            'ɧϿƊӀ2ɫėӊȓpɲҩӔ·ʉDЪÌЮφǁ¤ʘӲį0ĕƃĭҮ',
                                                                            'ƍҮjЎʟŮĿųŢʙзпíÿЉЯӘСŭˍ˛ϘȠӷ҃ń˟·ǍϾ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Bү\x96ԥĂҫˊΚęƝAԪȜʒβˡēƩϾüԔδwЄ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'θԬďφ\u0380ϒ}Ҳӛʘʸøʱӡƿ}ĀÈàƄŤɌ˩ǚʌҩϚȜ\x9eѫ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϽÜƟɄǳɠзҥƌɃͼͶЪÞҚĥδГΪҮѶ\u0378φɧѱ¾Ɏу·ˡ',
                    'message': '£ŊƥĐ҆Ӥˮ{˹ҧШŢқˊȄƷ³ζʔ¤¯ȜвϺШҩǁΝ˙л',
                    'arguments': [
                            {
                                        'name': 'ʉĿŻʹʌëλéȄ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĢăϏȴ"ԎԪɇˆʿųеĮƔԞһәɱʧԆϫ}ӱʋŅϣϔҧºя',
                                                    },
                                    },
                            {
                                        'name': 'ǄĜĠУdÚ˫Ќ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1946104286009071688,
                                                    },
                                    },
                            {
                                        'name': 'ƯŶӫтьϰʑӒďǰǄ\x8fҴӉΔӧГɋƣ;ɺșȚVæӂʔ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1443157147611542955,
                                                    },
                                    },
                            {
                                        'name': 'Ѽ°ƳŉʺƼȪʘɇѲeӵȎϕɅėϻtMɎюԞǪ˸ʉčÇÝˤá',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 626763.6106215772,
                                                    },
                                    },
                            {
                                        'name': 'ϜъƜʀ\x94ѯȚ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220924.302231:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x84ȸϸƢԡ\xa0ʣͶYф"íԚӊѢ\x90ÿƊӓĀŻϕjΉĜБƹȒҕ¤',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǎӾÒƱˠĐmԘѢȭҚȉňͺӎҞԟƨǷkȡѳǍϖ˥ŌƹȷԤӉ',
                                                                            'ԧȧөʈșjūΨ-УvϩФѤԗ¤ԩäӈԧŨÆ˪ѐǬҒΑɕɃӋ',
                                                                            'O)ģƚӡ\x8c*-ЀӬʁӣӃȘĎʈǓǝǂһǈöϺÎ҆ǒӹԦĎͽ',
                                                                            'Ǥƚ\x86rXUϹ͵.ɥԧϰȖˣϑ˹çcԦ¼ǶLΙǧҵˌǉ˙π%',
                                                                            "ê\x9bnśÄĹ'«ȰԧѧʛҌÍƝÏζл҄ΖąγŚ˂«Ͱ\x91νДԓ",
                                                                            'ɒѧɸ˟ʁǧŇϧ\u0382ӈʱ5εΤԪҢÓџƻ\x8bǵʕïΈσ¯Íȭɇǌ',
                                                                            'ԌȤDŜЗ˛±ӎыǦбҏλӱοɽíҮɼšǋðǏʕ¶ůʹǓѪΑ',
                                                                            'öi\xadóĢˊӻԌȱǏŌіӸȊŰԞɝ\x96ĥɀȘҥǈĹƻòǫɜȘʏ',
                                                                            'єħӖˡͶЉόϟʦТƉĪƴȾ#ΩŰʸúž0ӨĖӞ˶[\u038dϖĳϩ',
                                                                            'ȫӸsǃƃāĽԁӼƋΊ\x98υƻ,ҦĆɘźΜѡϧɕk˅ӚǀԨԄˆ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҞȢʘΓӢ\u0380ǃѣť$5Ԗǈϒҗȥҥɹ¾оӊт\x89ʤŻϭŘ®Ų˛',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 834758.4511899477,
                                                    },
                                    },
                            {
                                        'name': 'ӫěĢʠп҃ˑЗŃʓŨʵ¦ũЄϓԏʸӲéƻqыр³ʱɈԭɼơ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -38780.569136878265,
                                                    },
                                    },
                            {
                                        'name': 'ûæЕӧв}өʕØ<',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 62781.10069722711,
                                                    },
                                    },
                            {
                                        'name': 'hęħϧҡФСϻϾŏԝ½ͶqмʍčíϊϚúƸѥҗ\x85ˆ˟ρРϴ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220924.303247:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʥUƭař\x95ԡ¦ƴɕθŘǥ¯ӰͳѥъЮ\x82ǠʎϹϭȱҿŦÇκο',
                    'message': 'rÉʑŊάρ\x91țҝƩɎɦɶ`ѬҫԔǀəǏɔĤƞ</ƺνқ)Ɩ',
                    'arguments': [
                            {
                                        'name': 'ЁÈԠιӘʮƑҬ°ɠzӘӍphS\x93ƂӿͺȊʝǦGR˂xȺĿО',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'όѓɿО',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'æӍϯʫԦĳǐϮԄĨŢħ\u0378WӃΚͳ˴ԆíЕʵʽ^ъԝƅūΥʇ',
                                                    },
                                    },
                            {
                                        'name': 'Ġʮ\x8d±ǼƋԐǇȤÒʅȾʍΞÂȚҧŽƤ˚ƍӕɒ˞ƄԜҀωȷ¤',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6226643021754962169,
                                                                            2253905285384510415,
                                                                            7635859706422740545,
                                                                            -1286286007195258564,
                                                                            4592951047680773079,
                                                                            2504836695072919308,
                                                                            -5361212035798633322,
                                                                            1771941704568254234,
                                                                            1595683080381934464,
                                                                            830137588405999806,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƈΊĆ\x82ǫø\x9aŕǙλҔ³Ũʒɍ»śΌяÀƸĤ\x93',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3420488501440352030,
                                                    },
                                    },
                            {
                                        'name': 'XҭŽ§ȼИȑǒĲϺ/°ϪĸʥʳɑϋРɬÎĭ}ë˭ϑÑĕ˧ǋ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 685484.0298158448,
                                                    },
                                    },
                            {
                                        'name': 'ηУѲɕÂʛOˌʐνɹ¿ԪZĬœCˬjҹ\x8d',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            758116.761981124,
                                                                            400381.9779432409,
                                                                            25828.697264264236,
                                                                            752548.0065032437,
                                                                            88043.04886808648,
                                                                            874538.7648225883,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƢʳĞÒǋωBϟpλƦʓǯŦ}ɣɕŠʗХȿëΛѐӟǷѾĮƊƸ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˛Ж§˜μΘǱʩÈnЖÜʃXҥҧ)^ÇĢųɴȒ˅ѮíӆĪƚ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ĝ¹ԁØхǟʃӶʃʩȁȭĲԗǦʉźӧCӦ˝ӂ»҂ǺЍƼƠ9ô',
                                                                            'àʦȫ²ƬŌκɅο˾ǀÚ˺ɹſ˾Ƃ\x90ȓѷŵɀ³˲NɔͱëƥԖ',
                                                                            'ȹӞӿѣѠɆɳlȗƼ˭ɯ˗BΖ¬ЀBē˰ȓ˷ԟя%pʵŚќÚ',
                                                                            'ƯȢˢĳǑРƧŴφſɉˇŷΞ2/ǥʻΛç\xa0χȦÕ\x97Ɛ<Сˌζ',
                                                                            'ɂӠĴǄӊ~ӅƤġƐђщџǡӵѴ\x8cƝʳŀŴǂӓѪӾєӸKԂȜ',
                                                                            'ԢȪǕúǊΣ҆ǼɷѼγӤɮ/Ӎϖ˚ɫzͻOИСђĢÆϬnÔ$',
                                                                            'âˏǿĀʴӀйfІщvϲ9πʊŷʺłǱӗōӋđӻδƴčƀӥ\x9b',
                                                                            'ҦȢØźʡʏЉўw\u03a2ХPƕɀƨŔ\x9cϮѹҹӿψśҙђԡʉΖɷΔ',
                                                                            'ӊͳǡȡƷȭοϿÒ×sѶ\x8aǶŗɎȹcԠɣzĴѿϔξζΊƞJŭ',
                                                                            'Ϳʺ\u038dӕʠȍюĿhˣ¿ȸȝЎǤʒƟ-ЈÔΥѮԚ҂ϽԑжÑ\x9cƩ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '"',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3915646519456265337,
                                                    },
                                    },
                            {
                                        'name': 'İϊΩ\x85ʩʮʿϽ£ФĎзƆӼϱʙϕ\x9aуđҷćȍĜǗӑ[ˍ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2481875883474644989,
                                                                            2429778159426914663,
                                                                            -2396686105545202777,
                                                                            718096241864966229,
                                                                            -5474187068286724847,
                                                                            -7533708427645786576,
                                                                            4962572840750515774,
                                                                            -1310210887855670547,
                                                                            -7561097952419521324,
                                                                            6597433660611617718,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΰǀыͼАѪЙЛˍĨŴËȩԁЅԧ˙ˬşмηƤΝϒ\x88ʍɴ_\u038bP',
                    'message': 'ŜˢήÉ/ҖşҊЊǹ\x8cҏҘбȵđӀԃѯ͵Ҫ\x7fҿл˞ǽʦҞ˵ˈ',
                    'arguments': [
                            {
                                        'name': '\x99ԟӳԒľЬǉІʽȂĮќĹѸ҉\x88ҍӷ\x9fӉɁȊÇ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220924.306421:+0000',
                                                                            '20210206:220924.306434:+0000',
                                                                            '20210206:220924.306440:+0000',
                                                                            '20210206:220924.306445:+0000',
                                                                            '20210206:220924.306449:+0000',
                                                                            '20210206:220924.306454:+0000',
                                                                            '20210206:220924.306459:+0000',
                                                                            '20210206:220924.306463:+0000',
                                                                            '20210206:220924.306468:+0000',
                                                                            '20210206:220924.306473:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĀʖωҬӚɪŏҟĠԕјΗ˛Άə҆ŚоˇʪƯƧ\x89ęӗƲʝȳɩĩ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҾīϷϗƶјζХˊѫ=ΌJнїЮԈʘѓVМȖϗŉǕȳȴBɢȤ',
                                                                            'ѫπЎûēČԁȵǙƨɽ͵ɂɦɫȓϟΪтƬģ\x7fʠԡQфϝɸϙϜ',
                                                                            'ɾ«ĄΗϡġ˼ɧʟԓхɖſÇηĺѺƯЇôР°\x81ʽΆҒƘńıҸ',
                                                                            "ʬȌ'˅ξĉώѕƧʬǾı½ҼͲӖψĞЇƎˊˇˈ0ɩXӉ\x8eԑ˳",
                                                                            'ҡÒğȼΖјƾĘȀπ`ϵҙӏʂȎĶȈȅlʠƒÆƵćʉ«ɬľ±',
                                                                            'ĳӛ˩ТџĜĒʣXϦξǕ6ĽũȢсРƵӝѾϑӰɺѐȿ\x8biȽС',
                                                                            'mƘƫҰ·ʳȚĝҠƁȭĻįΓưmЗ˚×ÑǇǧωǀǂ\x8fÙucɳ',
                                                                            'ƈ˹ͻсɐЌΓǁȼѺXѴƄϋȥӰHɚӰеɯ˄ı˝ŨϾԃƋǺʚ',
                                                                            'ѢĮΑƳ҆ƙϽʛφΪΔʮĠJǥҾӤŉђҥ£\u0381ӼâΒSăɳϟԂ',
                                                                            'šϤ!щɻȶͰÂɗȢҔƗʤԨѬǣ¨ˁͳĥɏЀЅwɤþˋ¼ÓН',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǹ¦ȖкǽѣΞԦ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3236406724742108752,
                                                    },
                                    },
                            {
                                        'name': 'ǈΔȽΩѼїόđԆɻυӑķËόčѦɽɣųYÆŬőãѹʟӴģ»',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            199209.94552975963,
                                                                            55009.48957697651,
                                                                            51299.72045108874,
                                                                            443614.26039216795,
                                                                            783143.8874529207,
                                                                            599587.4910759329,
                                                                            564272.0471897738,
                                                                            195263.454611886,
                                                                            179921.67873589037,
                                                                            490134.12727549695,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŞȞ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            48021.46282205012,
                                                                            872068.8829145399,
                                                                            662751.6247681524,
                                                                            12976.501909669329,
                                                                            586202.395971349,
                                                                            937866.8114827063,
                                                                            746507.524572023,
                                                                            229785.5397467938,
                                                                            -36393.55741238443,
                                                                            862606.9457731748,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˝ƁǹӽˋĴѷ˼ϲ!ōʆ˗,',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӇЙЧ҈οŨϟқƂƗȅжĘbǚϟϘцЇðӆÜφёǺǏΤƈBp',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѨʳɞƟӤʉŀʤtɹԫ˭ϳоƪ˨ҥǉїϴǋμ˟чШϯʇґҼɏ',
                                                                            'ū˞\u0382ȚňϗӅŜǥӕӘЎaΆǵʼԌ˚ɚѺГЗӧėѕЄmˌąɃ',
                                                                            'ЎˈϛӐȪƦ\x97ѭ\x9eΡʸ¹ǰԥjÜ˄ҍ*KǁŖɊǠΣϮѳӲɂϰ',
                                                                            'ơȧƍǯúʠϹʭĀΓԆÄĲѧļʙˎȮ9Ѱ©Ρ͵ǸϚϗΒĬԅ÷',
                                                                            'ʦƳϠ\u0378ςʅѕͻ®ˢŵTξǧԓ˴ç0oѮЁȮϋҞητп҂ʬϖ',
                                                                            'бͻúƒԪϽʹɷ϶țǌŦĲ\x92˜ͿыͿ÷HΞʀǧʥ\x93ƙÜ\x7fΪc',
                                                                            '¼üҰή\x82¾ɧ\x99Ԝȟǐ˲έǼԥɶѪҍzȿIūǙxÖΝLΟ\x8f˄',
                                                                            'ÊÙƺ¬ӡ*ʛӸʈЯϥɥƱπǹÃëϨśšǀǆҟʀ˻ӑθρıΈ',
                                                                            'ΤÈưĆ\u0378I\u0380͵ʲϩ˻½ӂ:ʜ˖ȇ\xa0ȃǊƆƩȎҁlӮ¢5őǦ',
                                                                            '\x80ž\\лɑϊБĩ\x92МԕƺҨӓԭĵǆҬΧ;ѡбѧ΅шΈĶȒЩģ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϔCǑĝƐҴƾӖNҏɸƧʧ\x9d3®ҨίίŌѫ\u0383ʶơʼӕαȳʄʲ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ĀʑʷжEЧȼ˃ΒX\u038dΚώŀɋȂЌΪϗҪǝ\x9bԪőƀӆƭг˧Ӷ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            396455.2693401503,
                                                                            957137.7808796854,
                                                                            25633.84097653978,
                                                                            -35934.714181869254,
                                                                            425495.882155715,
                                                                            906038.5129988377,
                                                                            63082.885521461285,
                                                                            858214.0685803309,
                                                                            255044.92370852042,
                                                                            103851.37053543175,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'gÜ҄ÿ¶ҬҳίІɲwϥЫʻȖƃͶϐПҧϖбȵĈЌʁϨńʣń',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'šʣɡΧJѹǾŜŧ7Ƭu\x83ԄêΔϴɏФЙ˃ФӀȥʚ¹·ǩȰЧ',
                                                                            'ξĠȱ\x83ĥEŋɧшχrƦ\x9aзҙХҵƏ϶\x90ԡWɈя¸ɓȼҋ˟μ',
                                                                            'ΦҺ>Ңƈy˻хқҾўͲΧЋά҆ȬӅƘé³nŷԡƣ˟%aЈң',
                                                                            'ʛƁùİ\u0380ʱʔȳĳęӀǩèҨcUѾӤʝɌȗϺˑſϯԫĿԛӁƛ',
                                                                            'ϝ´ўÎ%҂Ҭ\u038dUʟʡƈ¤ıvĞWΒӲƆɊӷaʘmʛʂй΄ɟ',
                                                                            'Ν»{ʣӮʹǐӋ¢\x99ЮͼûŪωΔPDҞƟâ˛ЯНŔƃäçɣ-',
                                                                            'µǆɨ\xa0ĬÊǛʼđγѫɆБf˯ʾɢŨԘɔÐŒҀϙƌˢϾÐ¨ƅ',
                                                                            'ҨʾΉԍĨEЄԌ\x8b\x9eϻɍŭ®ԟλԆʊǬò˸\x88˔ʚӺŗ˹ԓǤƑ',
                                                                            'Ӫ\xa0ɔʟ÷łш˪Ȣǘҷ\x95ѪŰýԚˆ°ÞʝûĲɢȠԣтfŸħȗ',
                                                                            'NƉ¶БɺͿеӻӋǖʐȩҶȔҷГūдǓ˷ÑēѬΨdəӥԛӚП',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʌ\u0380ǾjƼ',
                    'message': 'ѣɜΜͲƵʐǇƿ5ėԕ҄ɑΪΞԃɒǊˈԑЭŻÄԎƩȢÍ¾Ȉƻ',
                    'arguments': [
                            {
                                        'name': 'ԒэҪҞȾǸǽ\x8dśђΡĔǟǃęЦͱѿʯŁЛǤğЧΌǺμą˾ÿ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220924.313335:+0000',
                                                    },
                                    },
                            {
                                        'name': ')ƹрĂ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220924.313703:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʵЉÂɇ¥ϣħΉģҧΓάѾώԪӪwγȜЅ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 107893.64644812877,
                                                    },
                                    },
                            {
                                        'name': 'ψϘǉÊȊ·ʫǗǇǺ5ϯԒˈζøȲWϰ˟ѽŠ\x89ΑĹňЗŴǙ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĨƏƈԃvƘϊӟОqӤÕΧɝŻÉӓɘ˗ϸș˶\x83ʬƒğÆԖΎԊ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
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
                                        'name': 'ʭ˯ơʢνԀŝΚ˛×ԇöƩφɋëӰǌІ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            800739.3165400237,
                                                                            123923.57218638185,
                                                                            261585.86344911857,
                                                                            979883.0375467117,
                                                                            197798.5211907231,
                                                                            -93464.46927018325,
                                                                            98940.67510880993,
                                                                            518102.23295487976,
                                                                            410601.4401199899,
                                                                            979011.547599755,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɤÐXʥʳЛÆΗǛǭÍńǋĦɂÈÏʏĶȴƏŀeдƄѓ"9˽Ň',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2892965884306343629,
                                                                            -873356473056918348,
                                                                            -8850958359459021694,
                                                                            -3502508571697932428,
                                                                            -5073428748747411087,
                                                                            -4685950924367261158,
                                                                            1272771477280065126,
                                                                            -6621534633872993954,
                                                                            1405324751237588962,
                                                                            -1026292795920445072,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѭшȻÜϊíĝɨҳҼцǔƨͶΜƦɛŗ҉ǓƎҼøƘğ_Ӗ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
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
                                        'name': 'ҥҌ҄˜ӤТȨǘŬƱýЗƃΒƥq˴ʠ͵ǴˢД=ɤɋ¼ҿʏÃ΅',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 787811.527406765,
                                                    },
                                    },
                            {
                                        'name': '˦ӗЭԟŉ\u0383ԜǝȤǎɯǏӥѹ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7593387521495051432,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȫʏвƄԎȩ\x8aͰjhuÿŢ',
                    'message': 'äǂёȆʇλϮћɫÍњȥˡŬǞûԎ˜Шïфϑ\u0380ƑϜЮê,uΎ',
                    'arguments': [
                            {
                                        'name': 'ҿѝƭфëУƢӣϟˎ8\x9fÓМІʇ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220924.317577:+0000',
                                                    },
                                    },
                            {
                                        'name': '»ΓèŢӃĮЛȓ\x9c·Ʉˊҥ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "Βӷ,ЭȠƅēϣ'ĪbA®ī³%ƥѤϮԄӚЄÀgҢÆѐ¥\x82ù",
                                                                            'ҡˌȇӠ³ĿȟÌӄҢŃƆ¥ҍ\x94ʷҙĈΝčόӺƛȐǐƷũ˘ϷЫ',
                                                                            'ĬŮԋϦΪϵ\u038bƹőɝζȮЖ¿ʟЍмȯѰĬ\x84ОƻȞİåǼȞΌ\x9c',
                                                                            'ȟȮэκėĹ®й:Ŕy(ɔ½ˍȭΊĲӀԇÞɩȻęѽӉƚЀӯʨ',
                                                                            '΄Ъϒ$ΜnxòĬҜIȉÂĪˠápВ(ı\x8fѭƛrљӓƎ\x97ʺǾ',
                                                                            'ñΜ$Пв˗ҞЪʂʀȅĤBƝȱȒƲͼýśшȭ-ŜɚƩńǅʌ\x9f',
                                                                            '_ɌφÓӑˠɳӧ\xadĆѮgǶΌɲӭϬȿ\x84\u0383ѱҜӗхǶʿɴçȺ(',
                                                                            '*Ğқ,\x80$šҝʕȲҒєȣƒҥʹɤȞԤ˷єўӞˀԎɟӪċԝӡ',
                                                                            'Ę.Ϫ˥èΞϸԋȸłЁӣĮ˹ʉԍ/ȵӣȳǫҳǀĬʒƻ\u0378ˆИɣ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǒǶϜЁÇǸŉ\x8eˏͶȳƦÊ>ӊǃ\x95ϮφҚʌӑƦŽ\x94ÂĐ҃Ȓò',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220924.318907:+0000',
                                                    },
                                    },
                            {
                                        'name': '˳ӡлƵǺƪό\x83ƬΨѐïƎӼεφėèȣϗ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Zǉȇԉċӌȧ·ʬǆȠϗӧąĀɣΣԚŇȕŒ˫ĪȚƜ¥PŅ˦Ǎ',
                                                                            'Ņϵ·Ɉ҇˕ԢĮЖǍҚ¿Õȋ˕ËҔɸřϔёе{ĒѼȺ?į\x91Ȇ',
                                                                            'űѤHǖэ+˦ǈŃɝƸύțӛ҉ЏͶ\x87ΒɉłΑфʒԏѕҗǌȣȳ',
                                                                            'ԫʰƥŇϨʣÙқЕЩφғӿʊ\x97ԟ0ɺҩǞȇҚѵjǺѰпŞȭī',
                                                                            'ɔɨҴş\x8dˌΐӋЁЌń\x97uӺɹΗ5ɮǶαȧϗɺʓŇˋ"Fцʠ',
                                                                            'ý3͵ǺƔ¢ưщƦӻĦϽΔ*ÅǌԕўϧѦȬģʝƘϞļʗŒЩ\x9b',
                                                                            ')ĭưrѓӍˑхӟʣΔďԬкȻǂƊ£ƲďÉԊΙǕԈʋ%ȆĸԜ',
                                                                            '"ҤȾϓǦсțƳѱ¼лÏĲΊʕӏԒȷěĺӁϘƔ#ԡԂżʖȲʠ',
                                                                            'ʶѾ3τӧƾ\x99ԀǧğȊ˥˶ſŧȁϥ ÈȃŔуbƓϔÙҾȿ\u038b\x92',
                                                                            'ŔҚǥÑƆ˛ðѲiёњ;¿ԒļȺɎȏȀĪУҔȵwҎх¯ɔɂԢ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǭĶɪ\u0383ÐǻăëǾҟƟīʻɐ4Åϟɟϐԍȭ¤ԐʒŸ˥\x93΄Šł',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8125461061963142226,
                                                                            1067161068281459474,
                                                                            -2304264991147491819,
                                                                            -5998162043976047600,
                                                                            8165035559048236056,
                                                                            6709510503488593897,
                                                                            7284343153422388372,
                                                                            -5619011355984275610,
                                                                            -9076852377689812864,
                                                                            1377416309939424639,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʇθýԜӟ\xa0ĵǶҼ˴ΒiÍӒ\u0378ęλěβʹϔϨõѬÁЮƚЉƧх',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220924.319917:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ZҤuˇ\u0381\x84φӏӟŝ΅6ůĪȸơӡҢ˘',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ͼï#ǜϔʐώëбѰŖʐȫʹÍѦёʶ˔ÁǞŘå˝Ɛ\x99ΆȿӾv',
                                                    },
                                    },
                            {
                                        'name': 'ԣŴҨΥӰАɷӢѡЭçўѾіϊƆȟþέ˾˱ЬȘѪǢìΌчƯÂ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ˑȬл',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 642436.6939500988,
                                                    },
                                    },
                            {
                                        'name': 'ЫҎƔԅŭ\x8aҠđǰʠŽӅţõƢѻ˺ήʮˣЎЍ\x8d˰č',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7574953636083049699,
                                                                            1994795985819575180,
                                                                            -1219695016787939448,
                                                                            -3221078230039690780,
                                                                            -809041742387088848,
                                                                            -1668892959903834969,
                                                                            7973348270334040529,
                                                                            -6254516520608775234,
                                                                            -5332919287670785642,
                                                                            2130475464030430056,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '϶Қcǆϐɇȫ΄ʂȋ&ˉөЗͶ\x90¯',
                    'message': '¶\x82dǛԕƼЎǢȵưωRļ}ȆеƎȗѤγЙħΉt¡ŃͰxСϤ',
                    'arguments': [
                            {
                                        'name': 'үŀ˺ʄғʊңʳΚĊOҎJђΕeҝ\u038dĚãӱ\x7f˅ô\x8dԠŭԣǳӭ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˍ¶ʈϾŐěΔfȕńлɅӷˁǞԅʫԒǋɑԊʙǴ\x8cԍ\x83źӶʾŘ',
                                                                            'Ѩǐύ\x98ɰыϋĵðƲMŇѸʸӎҝǯǥɺÚӝԒʠʐ9ŵ\x81ĄҺ˃',
                                                                            'Ѣ˒ß\u0379±ϲõ҅Мˡԥϟɿ͵ƧЏ˸зЙĸŖśӔɈɄçAϯӆǦ',
                                                                            'ÿȖγƌĈȣѯЇĂ©ĄǙϱб˖ҧЅӆβɵϳϳķːŮӗĞƄ˚Ý',
                                                                            'ҠͶΡǾРĘČϜӖӓÙȁуЖΡӆЇȭ¿ǵˤƮƏǶĳ²ʬӡѠŚ',
                                                                            'ùӗǝʑɮΓԮɫΟ҆ĸҠĤɻΞˀҗӋɬ\x81ѢҜ҉ӾĪϥѐӪȖǔ',
                                                                            'зѤԒƽ΅ǙŌȾŞȧ8ω2ˠʜČ\u03a2ŒŬāһƴˠϱɷ$ǰ˞þ\u0378',
                                                                            'EċѭǔǰθЏѡÛŷѽ¦ѐҦʇ˔ƈˇԂĴà˒ìԖ˅õzЊʛȔ',
                                                                            'ҫӠ˷āέ¦ľώȔѰīFщ\xa0ӕ\x92Ħѕ˙Ϝ\x7f҄ʨuȯɝͿɂȕ\xad',
                                                                            '_ʈϜИ˹Ƈӡίδí\x9bˬŔϏ{pѳӒЂơǪҐľԉ=ѭӜҩрȆ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʬӛφРϳщƉţÏāƲπƾǡɟ¦˧с6ʶԓ\x99Кʀ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
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
                                        'name': 'ˊįǌċԫɖƅʔʓʡ¿ýУpîҡąԂǸЉ®íʒαӦɿϾϼЩɍ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȑlсhɉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -55359.42692952176,
                                                    },
                                    },
                            {
                                        'name': 'ѕƯāҵѕǍcǈƫƁʻоċέМɑˀǮčÇƻŸѿќЪʻʆ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3853919283143553502,
                                                                            8398069795898774200,
                                                                            -5963206000968311579,
                                                                            2552110776245700054,
                                                                            -2640540871823807050,
                                                                            -1425637094048579340,
                                                                            6408146284095371258,
                                                                            1054471689140245938,
                                                                            -6237880146193083342,
                                                                            -860771482569338776,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҸɩҢщɻ\x8aƶΡ˾ȡɲŀʔкǗ˽ͷТҔȿÊƭɰ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '4ǩŨƆĎͷĵ¥о˝ȑЬϲ&ЮϕũʊͰӪӯrįӧʔӰӼdɟȳ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'èʉDæȻƦĲӶȘӝįKϦѢï´Ɋ˭Ӡǒыѯ˄ŔȸԪӔɽDǤ',
                                                                            '^²ǘȾƀàӵԡμƠ\x9fͷØ&ŀǡԟôћΟкďŀǂѹʼɢȌ˦ƃ',
                                                                            '҈ȋŔύ»ś\xa0\x92ǱóQŭ&ΆnǗӊήĵɉǅёˏ¨ǾЉɛөȺǾ',
                                                                            ')ɁġΘӺ"ƑťǋɺYÆʪɶʼҝAήѪӫ\x8bɻ¤ǂƶӯĺ,Ōȥ',
                                                                            '`ɅĸǯαǽĹ\x9bӴƃ\x8fŬ·zӜȮѦʫŹҏΑӏԎʯξȷȣyϸs',
                                                                            'ҚǓЛUЏвȅËԁɑƿʛҭ\x82˰°ǏЙǁǭ/ąƹ3ѺɯѯЁjУ',
                                                                            '|ΡȁíƶȉҏЂӷɜǅcчɋӥԁɰ˚ɋʪȂԅ²ΘμӃ˓Ϊ˷ҝ',
                                                                            'ӑÍЍЅԣΡĉȴҖӚ-˰ǲԫƜíΙяεɼǓƊσѷʵǉźƇǧÎ',
                                                                            'ӟŹńÌʚыϐÉѶbѣҦӌУȫŮӯiϝʣǤˤȎҁſӑÛūоƏ',
                                                                            'ԁñěÇȢǴĹȔЃηгęƌR½ѫ˰әˋȪԄCɒϱθǨͶęŘЪ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȹŃϭΐĩӪѸřĔŌЀɜȱƪ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220924.322971:+0000',
                                                                            '20210206:220924.322984:+0000',
                                                                            '20210206:220924.322990:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѫžΐǷĻšʧćƪԞǄAŌüЯЦʱǊѽƷ҄@ӵ/ԚҢ˟ƨɨˇ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220924.323177:+0000',
                                                                            '20210206:220924.323186:+0000',
                                                                            '20210206:220924.323191:+0000',
                                                                            '20210206:220924.323196:+0000',
                                                                            '20210206:220924.323200:+0000',
                                                                            '20210206:220924.323205:+0000',
                                                                            '20210206:220924.323209:+0000',
                                                                            '20210206:220924.323214:+0000',
                                                                            '20210206:220924.323218:+0000',
                                                                            '20210206:220924.323223:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǧψēÃʶȗɆͰȀѪȓƅ.\u0379ˍ˖\u0383ϵƋȗʕɑge҂ĉϒƆˑŷ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220924.323435:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'àw2¾Þ{Ƅϊz҈ƟĒΩǓȮ˷Ԍ˲ЀǣСԝЧɷǱϕʼƻȜѥ',
                    'message': 'ʀԀʶȮȌ²Bɮ5ʙȟÐһƍ˹ЯвüҘǇˮ°)ѱÖ^Ő˜ԑҕ',
                    'arguments': [
                            {
                                        'name': 'Ёŧ҄ȔǷȟҔԖɥΠ\x90Òν˼ø}ҐƫŽͳ»ćяƟÃǩϧŖɦθ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            15118.64272239471,
                                                                            287563.9298667098,
                                                                            101665.95397816677,
                                                                            710844.1866365771,
                                                                            -14118.595323528774,
                                                                            961465.5532686531,
                                                                            -97287.47406221919,
                                                                            103392.33147677753,
                                                                            99534.99557078016,
                                                                            100944.80300263522,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӻ¾âȒʾΠôҮ¬ĖγÛєʹɰʡʴĈˉɎ\x8e¡ŘÛ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220924.324259:+0000',
                                                    },
                                    },
                            {
                                        'name': '˒ȩΥϓʺ\x89ӶӎЃʹԇ¦ҧʨĞь',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˦ϔʱԏ˥ӢĥɔȐϲѓԛλ4ſўсǇăÂÖҞЋϡúơɞǲÂΎ',
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
                    'catalog': 'Ȍҟ',
                    'message': 'ƾ',
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
            'identifier': 'ұàȺӦÔ¡ʶ(ɒҨ\x86ȳԄ˲ʥԉИǈЈŐĘƖӸĩηȑȘʔĲˈ',
            'categories': [
                'file',
                'access-restriction',
                'invalid-user-action',
                'os',
                'network',
                'invalid-user-action',
                'os',
                'invalid-user-action',
                'access-restriction',
                'invalid-user-action',
            ],
            'source': 'ǲçˊɄʹƼƊ\x9eȟѓÄȊÃƳΣџȾҷȋуѻĒyƆ1ЦǪѱάЮ',
            'corrective_action': {
                'catalog': 'îĆѽϐ҉T˭½Ĝҵ\x82ĂƟƚtϦǚȆƢƮϗɬσǡѸ҄ʤͱͺ\u03a2',
                'message': 'ϺЦЎхƀɚɓīӍʔӏӝĘșΥʹѮѢåȵңȬˇ˒õɨȄӁŜ\x8a',
                'arguments': [
                    {
                            'name': 'ѝөѳєǨǥĿ]ĞƖΛºӱuǟԣԇ',
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
                                                        False,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': "Ęѻßě'ĵӪ3ȯ\x9f,ʥĉ½ѮɐƌϺGƂ",
                            'value': {
                                        '^': 'string',
                                        '$': 'ЍɞʥÓ˺ɸˊʒ\x82\x83ʯчŅԁmġǚ\x9bʡħąɀɰŪԈŔԚ\x9dǹӺ',
                                    },
                        },
                    {
                            'name': 'ËӤӤ[К\x9bþƲƄԛеȹėzљ˜бŢWƨʋĳɁΡϫѺыԓФŪ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -7762120060560298417,
                                                        2837591026819800486,
                                                        2007217458558963421,
                                                        2477491453102473051,
                                                        2898002439514522687,
                                                        2366614546094240362,
                                                        8558711927359779155,
                                                        8757996260884686133,
                                                        -2281104074255095850,
                                                        3946517490493885634,
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ӈ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        715060.6421001048,
                                                        401554.1798456692,
                                                        922130.8920853065,
                                                        410580.4184753971,
                                                        742441.2909834469,
                                                        -4714.583842774096,
                                                        112237.238285859,
                                                        -92034.85599121482,
                                                        294931.32797611644,
                                                        36730.3284261692,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ρɨͱһА\x86ąӹƦϧĨĜ×ΰ\x9e±~ҖÍĊϮǅʐɝ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        4931112269947282909,
                                                        -5106072602722596507,
                                                        -5378576910013948999,
                                                        5902764720171002656,
                                                        -2890746410596911991,
                                                        -2657488103888557558,
                                                        4443289046710197122,
                                                        -4317015686502143325,
                                                        -8108675266378956361,
                                                        -2850190820552017033,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ơʏʬƋӒӳҚсȎ%ĪéѮF\u0379О¬˖ĶΏ\x7fг,',
                            'value': {
                                        '^': 'float',
                                        '$': 791141.2103147048,
                                    },
                        },
                    {
                            'name': 'øĝҥϬƕԪ\x9a҈',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        93644.1531622223,
                                                        663337.8558785816,
                                                        81034.3416650295,
                                                        362747.7780603032,
                                                        796575.8332763604,
                                                        992448.3999229963,
                                                        458009.45882958977,
                                                        742877.9188465794,
                                                        223847.55296466628,
                                                        460527.70023083803,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ҕѪ.ƃǄұũúȍˁ²4NѰʋσ\x9cn\x82ʝǚЋДЃ҆ǦēŌɊĬ',
                            'value': {
                                        '^': 'int',
                                        '$': -300710143681947688,
                                    },
                        },
                    {
                            'name': 'әɚԣě¤Ҏų˾èͽϚǇѶѮħ˒®ʈ˫ˋǖ\x83¦OƞA\x94ω©ȶ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210206:220924.337323:+0000',
                                                        '20210206:220924.337346:+0000',
                                                        '20210206:220924.337363:+0000',
                                                        '20210206:220924.337373:+0000',
                                                        '20210206:220924.337378:+0000',
                                                        '20210206:220924.337383:+0000',
                                                        '20210206:220924.337388:+0000',
                                                        '20210206:220924.337392:+0000',
                                                        '20210206:220924.337397:+0000',
                                                        '20210206:220924.337402:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': '½ΤʶѴÿǸ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        '¢ƜϪęŕÚΓҴȋð"ԌҸƹȓřѡ´ѽȼŶ¯ƅϽƯǶȨё:ɧ',
                                                        '¥L©вċԔ¤±ԇȬ³Џ\u0379ȚȌ˽˟ӨķQҖĻɞЕ0gɳ\x97Ʋ˚',
                                                        'ȩǻƯýőhюӍϳɪÚfǗ˃þ½˰ȶҹÁ˗ŗȌһǒVӇÇʷј',
                                                        'Ì˺ѼħűÐÆĸϒͰϽŦҡӻ\x8aÉ<Ȏþʓǧ\x90ѕːǭˈćm÷Ѱ',
                                                        'α˚ȬkɘωȐ÷ǧ1ҕǢĵΐWϝԙѓư·ҊϙʕľбѣĠŽԬЁ',
                                                        'ɒϭÀҕш\x84Ͱɘˉʈ2ʝGĿĂ ԡĿϿ\u0382ơлŖ· ;ҰǇ¬Ʈ',
                                                        'λaβpŗӥü÷˴ƌƏϾĢzόĆӨĺϐВ҉ÌҶ˲ӏρƨЭȞŸ',
                                                        'ʗŴԐи\x87ҰДȘGˇƠҚ§¦ϏāʿǼʪҴĉϸt×ҠʘԎưѧҡ',
                                                        '',
                                                        'BĔ˴ҙȂǋđ ˳ЁĘ\x9aΆˊQТўӄţҪНяҪƖѮɅǼϲˌË',
                                                    ],
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'pӝǑˊïǝЎ°ƘɒκĔȓѲǨԨӟҭħɡśȷѥǇė˹/ϭѣǶ',
                'message': '˺ĐχFŃϞτɟwɉӐĒȧщ?\x83ǩϕɗyΜčʖĕǡǽҡOÀĚ',
                'arguments': [
                    {
                            'name': 'ȹԋŤԄӀαЧѪɹŌ³ΖϺÀ\u0379űɪ˼ҹɺ\x81ϩ¤yҌԧƀѻϙ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'Ưțʄoɩzǧǳ\u0382ҬЁϖķħχҖҦʧʌkЁ˫ҴʾΑËƄ˟ĝY',
                                                        'ȦǏqҊӈАϷМƳҌúX¤˩WȫǞҹŗԙżϾҰҾȰūƵӷƌʹ',
                                                        'яæbȱʞƍƴϻİѫ\u0381шаˊǘƵǏƚюΆĮ@ф¤ҦlΉˍƩϔ',
                                                        'rǔΘſԑŀԐ˱ìϊоRȇĳǧ\x91ȩŧǭȋöʝϏWɤƪʃ¦Ȓт',
                                                        'CУ\x82ĈǾζЖÅĤȑΛ]mĮų˹ÃԜ˪PІýӬԜǉԦ\x8dïĔϤ',
                                                        'ȍjͺԦԔ\u0380ѾĝÕϑӣȷŊΓȚ>ɬlć-ХəГԐӡȻԩчӽθ',
                                                        'щʎϑƿȈҧÈ˞ННξæΧͺԢļʨ»ãΖєϢYӡƶϳL˔\x8fΖ',
                                                        'Ȑ\x9fōǁǯ·ʹ˔f7UϞʙԞ\x99ƿȂӯÙη˺ʗȬ"/Ɲҹǘ˚ч',
                                                        'ҫƭǜȶҿ÷ċ\x95ŪþǡϒϚǶlлӝɅυ˥xŖϣňƴɞЬ˽҂ƃ',
                                                        'ȒɡőԈԩäЮѝǘυΕßƩʙəƅþάΫǘa˰ʬҮǥԉʤСÛБ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Сřʳƣ˕Ŝѐƨ9ӈ\u03a2ÍɴЯáɀӼgϙӬ\x7fƼӄԭΧʕʌƎΕŶ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        495581.7907812955,
                                                        -99370.88053052523,
                                                        780858.2547108772,
                                                        323538.75838066224,
                                                        701158.3914746483,
                                                        565032.001139236,
                                                        319036.2112283456,
                                                        410492.5030616486,
                                                        375456.2169337659,
                                                        529674.6221962507,
                                                    ],
                                    },
                        },
                    {
                            'name': '΄ȡӌʒρң\x9eÝ*ʨʯǓ;ҚƌМĒƎʀǅɺԅ¼ŉêäƊӱƗӒ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ũÅˡžʅҐ˅ΡηɓdȋȺ\x9cĸʾɫԓΆǁѓӀǀȑҸǽтë5ç',
                                                        'ӕЫèƴųʫƠїĎЌâˢ½ʃʞѭʿǗӵȵȿδʸĨφͲņƪЙϚ',
                                                        'Č˛ϽҿшѶƯˬ˥ӫʥyдѡѰʹћфӄòЫ\x9aҥƁӦϦÙˇŗȂ',
                                                        'ƮҩШѦԏÂБϛΩϏSˇόԥŋσӳԕ΅ѬlƾԃĜЍ¾ΐĴŴΰ',
                                                        'ҹDЦŵÿȷ£ĶȔҤăȉƶsÈЙǛɣДҶыÈ҇ňǣ\x98ҵʔЏ˰',
                                                        'śғŸǿɍ0£ѪʄφǷԑȘ\x9bьɘÀӖ˨Ȥ>Ţɧ¼ƩϰȟȓΉƎ',
                                                        '\u038bəɲŦѩΘδʬû\u0383ÎтԚыɴåԖ˞\x89u$ӾȐñҵċϦѡԫ˩',
                                                        'ϯËŞƯŞRƇÑЙƌʻŌ[@˷˦ӔǱÒĶ˂ӴѓĶŋўʫԈԠʭ',
                                                        'Éȫyŉ\x83gƽɓвõÐʉŸ!WƶХȷŘǳЁµÜĤʧʙîǥΠΝ',
                                                        'ҽӺÍѠʥ˨ЄĠ˰υ҄ĭђ<Ǽ˪ɁǸƤμǣɿ¹_ϛǺȽϵЈÝ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǡŸǻˍÙǨ\x8døόРˣµ\x86ˌΔƫҧѢçГɱǡ',
                            'value': {
                                        '^': 'int',
                                        '$': 7872626984766082666,
                                    },
                        },
                    {
                            'name': 'ȌœʔԊɖҏŞԒХƸǪɵĿʚЇʡϏÉŚ˂ȖˬLЇН\x88ϭǮ',
                            'value': {
                                        '^': 'string',
                                        '$': 'әθHɃɱӂѸáѡΕԃf\u038d\u0382\x7f\u038bϛÂvƀǞ¦ÀȄƠ®ЈӄƇ˹',
                                    },
                        },
                    {
                            'name': 'Ы\x99ǜЫЍӆʈ',
                            'value': {
                                        '^': 'int',
                                        '$': 1012721174716856412,
                                    },
                        },
                    {
                            'name': 'ӠĚ˒ǜ¹C\x83ȀҾͼ\x9b³ɝɬ\x8b\x98ƅԪƳË\x8fӿӒ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        7167489731754834824,
                                                        -5461955831780214632,
                                                        1032176354207240442,
                                                        5918263739546557502,
                                                        3667496390620589086,
                                                        7593364664141025849,
                                                        5830508493965511172,
                                                        -7620668965711102921,
                                                        8901775161873222322,
                                                        5681621654474517908,
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ͳ*œ2Äĸ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ΏǞnӢƯԪӢΠϹӉɖɼÏ˄ˀΝҩʝȄȭʩŒʶБδΛшЛȹƼ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        271854.7726766065,
                                                        866703.8787552235,
                                                        803689.5607979322,
                                                        812830.269231346,
                                                        48364.57359466734,
                                                        855598.2832548083,
                                                        86424.19603920236,
                                                        560774.5409099214,
                                                        333105.5839081695,
                                                        89583.9776161963,
                                                    ],
                                    },
                        },
                    {
                            'name': 'cȭɄαƄ˟\u038bÔԐĥơ[ţ²×¡úƷƽ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210206:220924.340798:+0000',
                                                        '20210206:220924.340811:+0000',
                                                        '20210206:220924.340816:+0000',
                                                        '20210206:220924.340821:+0000',
                                                        '20210206:220924.340826:+0000',
                                                        '20210206:220924.341864:+0000',
                                                        '20210206:220924.341894:+0000',
                                                        '20210206:220924.341900:+0000',
                                                        '20210206:220924.341905:+0000',
                                                        '20210206:220924.341910:+0000',
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

            'identifier': 'Ρ\x8făɯ\x96',

            'categories': [
                'invalid-user-action',
            ],

            'error_message': {
                'catalog': '¼¯',
                'message': 'Ю',
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
                'identifier': '«υѳъIĢŉˌĬĿ¥ѦǱǤԠΩԐɭˉτКΊԛLΝѡΧΡ˱Ї',
                'categories': [
                    'invalid-user-action',
                    'network',
                    'invalid-user-action',
                    'configuration',
                    'network',
                    'configuration',
                    'invalid-user-action',
                    'invalid-user-action',
                    'internal',
                    'access-restriction',
                ],
                'source': 'ůʬǨ\x9bƠв·\x9dçƢƮǷÏӊ^ҟĀɩԫҚ˦ӣļ©ǻɀưӶñӼ',
                'corrective_action': {
                    'catalog': '΄^˰\u03a2ɦƗƍѕ˃ϝΉӎǐҹȓΡɺ΅\x99Вɠ\xa0ҕȎźȥѢħ˯\x83',
                    'message': 'Ńɻý˩ǏШȀΔӓŕцõӹˉΫЫϫϾ¾ɈѼϧӍƪЌʇɖĒԪϚ',
                    'arguments': [
                            {
                                        'name': 'ыЏ\x8btΑԇ˔\u0382АϧԬʅԜң˨c',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˾ԀӚôдп\x90н7ñkŔАмЄj\u0382ΥѴƳäRˬļҖ2ɳ\x87ʯ˰',
                                                                            'āʹ\xa0ƨǘæόϩʑ¨ҶҌдҤӋȶȟǤѿȒҰ\u0383\u0380ʏ҇9ɜĊцү',
                                                                            'ŉӎͱŒĦŃύǲεгΓӬŖϹʍȫǑɆɣɯЊHĽΗʃűχȺУʆ',
                                                                            'ΑСΈйȦɹоǺоǿԄӚɯFȑЊкƗσȹώØээȧˢъСśϲ',
                                                                            'ǏŎßԉǷԣűAӦɆ^{Ԃсȋȼ˵Ё\x93ӥʿȱȨ\x9d˳˘ÆϐЭв',
                                                                            'Εӳ˨ѻǢӗΧɱä΅ƁcĭԖkűʹҒϔ\u03a2JлŷȮĬÐ˕Яҹʷ',
                                                                            '¦δΆϣʦǔǼɸƓϸǊÀǎ\x93ӪsӌҩɆѺӥҚΎӯXӫȋVƑҴ',
                                                                            'ԛ˟ΚƥɰТТŋкòˡѯΎΈΪȇʗ`ФʤSȓ\u0378˫ѸĀŜüϼģ',
                                                                            'ӳӝÁŮϲȻ\x87$ĲϑǠoȓ$?ĈƉȽɆӿϚӽʇȂдčϒъňƳ',
                                                                            'éèϲʮмҬӝœő\x82ˑϴӼ˟ЬԍΈʹΝԑˈɺЗ¦ΔɾχȆɨ˛',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȱԏϊʚӌġ¡ԜʐԒ.ѵȱȱŕӑǤǄǮǋϡ\u0380\x88ňΓ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŶŜ7ȈΑðњøȿǱůĤ7ԄǨɭıϓƃȒņ\x97ʬɆүԒѧģȾЩ',
                                                                            'ņʮίȫѤԥǭŊƳư@ńǊʭ9c9ŃĪΣǅǜхБеëӒӓ҄Ў',
                                                                            'Ϥʛ:ԧȖÞ]GÎķЧҷʏĬǬʔ\x83ӝvȖәПҶ˧ģԬȲʵșʄ',
                                                                            '\x93ЀҷƢЯɘөĩӉħðЛԖw¶ĠȑӰ\u0378ĥȤÁĜҠ\x80ҼӎΫʙʨ',
                                                                            '˯Ȼǆ>ʎċӦ\u0381ѩ9ӖТ\x9c˛ӌπ˔ν.\u038bȪÇˌɻǃmųİɠÄ',
                                                                            'ϿyʁҗÂЃ\x80Ěљ\u0379ƁȃµǤ\x88Ȧǿџгτ\u0378ǩѩϧȾΈͳȳǣ\u0381',
                                                                            '¢ԥȟoʏ҃ǰӽϜȏĠѤ¦ƟΑͶЕӑŀƮåÉÓшŜ˦žĂԢ\x8f',
                                                                            'эɡÉаѴΐΘΠ#\x9f]\x87ˈӛDʙ°ɅŐԥȐϡȢОǳϦʁ·˵ь',
                                                                            'Ҹ`Гĳǻϋã·Ǖͺ\x86ƥŶɟԄɸ˙Ӷ$Kϔ˛ȨÈϜ\u0381\x82ӅČî',
                                                                            'ӠƹŐӬφŭʍǌΎǇȽǔͶ˦ǀϐȴȊŚ\x8bƝYɩ·ʻÊ\x93ňӡɮ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҐƤ,4ƀbȩąԠÛĄɡÿǷ$ħʼЃ˂ɯ2ʋŖʐЮ\u0380ȅЕʘ\x9c',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8015104533465937633,
                                                    },
                                    },
                            {
                                        'name': 'ɍǃδаÖϠωΒøÁłˢš',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 351825.8224193764,
                                                    },
                                    },
                            {
                                        'name': 'ĄǯӅϳӐˊɒǘјӳjϟbſÄH>÷ŶΎ˳Ǌϲԥώѽѥ±Џҳ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϘзŊӧҐ^Ҿȿȳ-úy\xa0ύ\x9dɶŲɁϼҌìǑӚƥ§ΉȇZ\u0382Ϩ',
                                                                            'ƄâόðгÏǛΎԗ˱҅7?',
                                                                            "Ӗӗ\x84Űǌз\x9fĪѝѣ~>˨ӤŪζʁ˳ϺϪД>\u0381βӒƂϛ'ȽӔ",
                                                                            '\x88ˏӏƀŦƖǤɻɐưƇǀӌȻūȰъʡϙϠӮ\x95ǰʻйӏļԇȊÏ',
                                                                            'ҬмȵɄɭü\u0382ɫЧŷΡӠŘҴ8ŦǯǷҚπηӛ4ǂʵʡǧæŀ{',
                                                                            'ʅïӀѩφɚʅVԂʗĜƱ;ɍ҈ˉɍζӸкԒȝςǸҁсϡiŝќ',
                                                                            'ҰȉҰԛăœĖέƧǡƦ7νɊǤԧōӅǪɖUâǒ˺ӑ4ÅѮėƥ',
                                                                            'ǙʋÛӻ΅1ď\u0379ҀԫǮȆ\x9bǕŁĽŵϘфɛǢœәNӧԅ`\x89ҩӄ',
                                                                            'ŶҠԍπϐĠ\x90эɓȭпÌ\x88˥İǟѾԖĈſÛŒѴϏηԟҫЧōҀ',
                                                                            'ƸҥãϜɆƤñåǛŀƓϿɗƮǢҜҿVԁ˄4Σɜ҇ĠьϜʝīԟ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϸˬσʑɋɺĎБДņҦˍ ʫTӟьʼªʌŎǰӻ΅¯>dЄǋа',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220924.330171:+0000',
                                                                            '20210206:220924.330185:+0000',
                                                                            '20210206:220924.330191:+0000',
                                                                            '20210206:220924.330196:+0000',
                                                                            '20210206:220924.330201:+0000',
                                                                            '20210206:220924.330206:+0000',
                                                                            '20210206:220924.330231:+0000',
                                                                            '20210206:220924.330240:+0000',
                                                                            '20210206:220924.330245:+0000',
                                                                            '20210206:220924.330251:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ƴ˭ÿŭɘǯʁÞӴȏэbÔĳ¤ԘбҙƐƝ\xadʃ¯ҷɓÓҭİǵӨ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -5599.974784318445,
                                                    },
                                    },
                            {
                                        'name': 'ŋ˖ɠʡԁӢĢӠЎ΅җĴ\x95ʶ\u03a2\x94ŇCʘ¹Ϊўђƀ҃ҪʬɐŪ҉',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'rƝЊѺɸӖǞʛÍь˶ǋͲöӇОŏɈӋҨϣҕǚʔ҂ѷӰΣëǪ',
                                                    },
                                    },
                            {
                                        'name': 'ΎЬƧȋӁĘϓĥͶƘӸ˾ɅʂxћƄ˥ƷėńѷŻUǱƱʗ˙Ԟґ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            987952.3554426476,
                                                                            32897.48858484544,
                                                                            865989.9323107799,
                                                                            749352.6493625997,
                                                                            552622.6756884886,
                                                                            828231.1876063874,
                                                                            527841.984603639,
                                                                            71494.69592748483,
                                                                            185364.12451531377,
                                                                            293211.41501605714,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˠʠ¼"ʐɐӎɦŁ°ʞɻǔǁʃĊΪȃċȺ)ĩԮ\u0382ͻτİǐЪŢ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            616406.2646790935,
                                                                            814342.1082187573,
                                                                            641295.8706699306,
                                                                            525998.5299864112,
                                                                            268845.10460810945,
                                                                            341263.36990826065,
                                                                            487985.09931254596,
                                                                            -26018.737046012742,
                                                                            927632.9062504708,
                                                                            -99390.38510692085,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'Űƙ˟ňЅԁȾțԗȃǹ\u0379Ș\x9a±Ϟ©ҭΤћҘЈƓǶ\x9aĠϲ;Ӧδ',
                    'message': 'ҝȈƚđ¨ЉϿμӂŝӓĘƬ˱ͶSļmŎӿѦĀЎnԢȨԧUƀĘ',
                    'arguments': [
                            {
                                        'name': 'ƫŎȶʴʳжΔͿȃγõ\u03a2ΰήˮŘȤҫҝɻЍҸϾιя-ʼΪɰŲ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ЂªŁŀϱɞöɦǒ\x9aœ¤Ԝ;źȟȻьЕʆȝĻƚˬӞаŲԘ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʏƄǺ"ɎŹ\x9eӔɸҋшΜ˳дӺʈ\u0378ʥȡƪĶʊȇ˄ȮƇϾȒƏӼ',
                                                                            'ʀ˶òɾȧΣʹȷԅ(>ǣğɞȾ\x81ȵӝˆPŷāӕχˡӸþ\xad˓ԣ',
                                                                            'ŋΊϰ¶πͳ\xadê3Ĳʞ\x9fƈŻƝʇϘƱªҠ2ĂΈ¨ȍ¸ʟΌƳʐ',
                                                                            'kԙĶΙķǆҲǴԂǹҙÏɰƦƛ4ȫΎȭòƶʇ)ӁˢѶΟӞŧ¸',
                                                                            'ԥ\x95ѭјƛǵӶȉǣрΟyс,vī}ηɗȦήˉҜԉ\x8dĻѭ҄ҽӵ',
                                                                            'ˤıԬƭź˄ǹѪѫtЃӪҾ\\ƅ¿φǠˬïÔʍɠÅȘĭέ6ǌĀ',
                                                                            'ɂėʄѷʞӆҪũóϷːVδҴȰqǊ˼фӀДȌʈӨʑǹŬƫɯ˖',
                                                                            'ıȊ˷сč˽ˉŖΓķDĚҢΑēɈͱʸϥşφΌԟҳĚİɯɠǲȱ',
                                                                            '˜ñ5ªιԬμдԇ˴ϋ\x98ͿӼǼƴоŅŀʔ%Ȥu\\ƱʕШǖҿɻ',
                                                                            'ÿ¬ǩлǌұĂĆɏɰвҽ;FäђѲSˮԧ˅ПωԈŖεĲǮ0҄',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˋ¥ԍȹϦˬ=ɁҿʘɡʷĭӧЪŬΎŶϬ\x91ԆџƐ\x96ͰѬш\x81ŐϷ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'þOч<ΫЪɄԩ©ԙTāҗ1ŕбʟ˼ĬOӪқ˛ɚ˥ǩŻϮ¹е',
                                                    },
                                    },
                            {
                                        'name': 'έКӽэϯǀцżïʹˇ\x86ƴȂɌȌa&ˇ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220924.332458:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǀȨńʅLϕ\xadǥϻԥʕԭųƖĿ˔ӎЍҏņÜϴĞǥƣʨȚΥ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            994663.1890100816,
                                                                            177035.19709998218,
                                                                            825135.3917407041,
                                                                            507549.38938467065,
                                                                            852446.9848756203,
                                                                            771357.4530511086,
                                                                            862009.5586219684,
                                                                            129157.78735414217,
                                                                            -39589.8487393797,
                                                                            -64308.68920377809,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȉňĆϣ\x90ʶʭԔʹЬ҉ыɶϏǶf¨ɓĬțw˫ӏ҅ÖҴXçВЄ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220924.333203:+0000',
                                                                            '20210206:220924.333217:+0000',
                                                                            '20210206:220924.333222:+0000',
                                                                            '20210206:220924.333227:+0000',
                                                                            '20210206:220924.333231:+0000',
                                                                            '20210206:220924.333236:+0000',
                                                                            '20210206:220924.333240:+0000',
                                                                            '20210206:220924.333244:+0000',
                                                                            '20210206:220924.333249:+0000',
                                                                            '20210206:220924.333253:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '%ó\x81ӆƦмјʀԮͷ҂Ϧ\x93ЫӸǋȐƯǔʟÐƁț\x8dŞȞƑ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "ňΣɥ)њԈƞjġԜˢ:ýú'Ϩ˔μǠˋ\x8fʮǈгÙţԊϲҮԎ",
                                                    },
                                    },
                            {
                                        'name': 'лӶ³ŒЃǥǜǴˢҟdƔw¬ʥμĨɚƢŠĴА',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220924.333692:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x8eήԨɷǉĻӃҼϴΦaИӆƀÃǜͼέԔƦɷӖǝʦҊȵÝǥјȿ',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŅѩĶγöӴԕΡͿΎčÀʲ϶ʓȐѪś\x8cˊь<ŭԖҌª',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220924.334074:+0000',
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
                'identifier': '͵єξӌΦ',
                'categories': [
                    'configuration',
                ],
                'error_message': {
                    'catalog': 'ʢū',
                    'message': 'ȣ',
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
                'identifier': 'ԜƣĭËǧӐÝʁUӅƈŬӁŇǕώʄҥ<ĎǓƬ¡įĈҝҖҐǧΧ',
                'categories': [
                    'configuration',
                    'invalid-user-action',
                    'os',
                    'file',
                    'os',
                    'os',
                    'invalid-user-action',
                    'configuration',
                    'network',
                    'invalid-user-action',
                ],
                'source': 'ɖǸʕԆǏӳƟ˷Ó{ȩďфʔ',
                'corrective_action': {
                    'catalog': 'ҭϣǥùɁˊȭ˂ǣɝèuiмɹ\u0383Ò˸\x89æҼͱǖϮɪ҆źԕрѮ',
                    'message': 'ÎҀ×ԆğԔґƟʚ\x8cӽбнɐйƿŷѣΖԃŕǷ2ĳȺȌԋԕΗɮ',
                    'arguments': [
                            {
                                        'name': 'ƞ3ϒ8ʤԧˊǈŷȹ¦рɬϮŚӊSqɠɚЮѝҴҔĞŞâʢËƙ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6400455808208474422,
                                                    },
                                    },
                            {
                                        'name': 'Α\x97ƈё˹ȄΘӃʆʾʛӅ]ёқ\x92ϝǽ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 869544.9966613075,
                                                    },
                                    },
                            {
                                        'name': 'Ԩќ(έӑԠЕʹʔɈņя',
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƭ¤ό˱ԫǋǉŖʢӝ\x9e',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2547922996019131465,
                                                                            -3757648697997467750,
                                                                            -3455922226078894546,
                                                                            7307994714872144554,
                                                                            -8617133995458437194,
                                                                            -8165858463372473430,
                                                                            -8910711981498999365,
                                                                            3927766640512293779,
                                                                            -4190588427091878590,
                                                                            3724112718693156487,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ўæʡâҩ˄юĐԡԧʤǦˤĮʽĤł˕=ΕÞԆЗьӵþϬĲ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2934275133268989760,
                                                                            301777089741602444,
                                                                            -3568101985567224684,
                                                                            8798323847306213806,
                                                                            4510355012094488805,
                                                                            3871259047632616912,
                                                                            -4325358545246828805,
                                                                            6149774160915609106,
                                                                            2227949778386355454,
                                                                            -7910008606469279380,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҸϗԄȓΰʯӛαɚԕҝ҄/ɐ˲˖ѴϙμΓƖʪҞƄǧεȌyŵʹ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɣǭѫ\x94ΉҚϓ89_ȽҒĖjʒƖƳԘm:ХǱƟ˚ʵŶƩʃxΩ',
                                                                            'ʢɒ,νŬ˼ÕǂDͽʮ˵ǄĞήɉıɁϿԌƩɫΐĀǄǛӰČ\\Ѩ',
                                                                            'ʖԫě4žǍƧеԑʗƹǵɫ7]ƳӰуƦϋƍʪťΜƧȤ\x9aƟƨԛ',
                                                                            'ęǬˠȓźŹӸˁϩĈºɊӶȌŸ\x9a\u0383łΜʁɱPǢ˅ĽԜ˄ЦɱԚ',
                                                                            'ІԃӮͽӓԐЃ\x85ѯ\u03a2ǻĿΩʁѐ\x96˵Ʊʅ˶<xƀԐԤ\u0378Ө`Ίˑ',
                                                                            'ȲӣӱʜoăЖñȇʀ\x9eǩƝοźǛν\x93ǒШчƒɳȐ;ʧĦѕуԟ',
                                                                            '5ӳɞɚǌɃȢʏő\x9fʅ϶;ЅЩ\x97Ђҏ%Ҫ˶5ƭƥԁʾЩVԩϪ',
                                                                            '˗ĳƵ)ӋÍʼʶÞˬºPħʍЛЧϩԌΓǚȲț\x86ǒʳΔƷιɀ±',
                                                                            'ԑԞȇŇƯǹȃϬͰðǽҘєΣǇCϰԀЁȄǀǧÐ\x7fӝ˗ƅǰƅě',
                                                                            'ĪԅȿЈæřßϒϘsȲ¶ƘћĺɆ˻ΨåǩÕҴБɘ@ǉzģТú',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'σ҂\xa0҃Ʀ»ȥǾӢ˅ăΪ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            386281.29821397655,
                                                                            251185.95236534713,
                                                                            912060.7687451841,
                                                                            -72802.01060964541,
                                                                            419218.25774892734,
                                                                            506291.37703417207,
                                                                            -26741.12389784836,
                                                                            744463.3489257882,
                                                                            848097.3462308561,
                                                                            599379.1360257472,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɹΉ¨ȝҊԚžӰFӲβ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȳŘ?îfσлСĚĦƙȳʏȜɸδƋ`Ҷ͵ЗǺmʽǘӨÍΰGԏ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԉçƁǋηɉёǼǘɷōʆ\x8b˙ŮßćЊ·ЋΤЗһƚâʡѵÜŀҗ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            492231.5166611542,
                                                                            715877.6401627349,
                                                                            470118.1966360824,
                                                                            643948.7508084221,
                                                                            609950.7797871141,
                                                                            980875.1351769136,
                                                                            385880.8159684011,
                                                                            190894.19592889148,
                                                                            77969.93301224461,
                                                                            497209.77007141546,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'қѮј˃ΜWáȅRђ˽ÓʁЧЯȻЙʲǳпŨ\u0380ƐԕƗʡ˽\x95ǉĂ',
                    'message': 'ɩXϤāҋÓϣɬπа¤ΡБҸԂԥѓˌĹĴǍİѲ\x8cǇǒɑ¾ūҊ',
                    'arguments': [
                            {
                                        'name': 'WƞǩϬȐǀţϛȁà϶ȶϐԛӽ˽ƃ6¥Ӭί\x97ŸˮƩĤʀʼэΌ',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʯȫϝÑĭÍӿnň@Ňұ͵˦Ŕϴ(Ή',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220924.346135:+0000',
                                                                            '20210206:220924.346152:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ђmѓƴΕǷθҝ~˰',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220924.346367:+0000',
                                                                            '20210206:220924.346380:+0000',
                                                                            '20210206:220924.346386:+0000',
                                                                            '20210206:220924.346392:+0000',
                                                                            '20210206:220924.346397:+0000',
                                                                            '20210206:220924.346402:+0000',
                                                                            '20210206:220924.346406:+0000',
                                                                            '20210206:220924.346411:+0000',
                                                                            '20210206:220924.346416:+0000',
                                                                            '20210206:220924.346420:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'τȧ˔ȊũĆćƍҠȥɧĎϡs³Ǒ^Ϗˊǁ¬äҊǈοoҌҭǂˈ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220924.346665:+0000',
                                                    },
                                    },
                            {
                                        'name': 'φӓƽpΘҒŰөƠ_ʊҨXŠѝ\x84īѺžǳҠĹάԔӶӠҟɡŚ»',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ӭʱʼ˄tİɎːr΅\x99',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'еȏЖԘȫěӔðˍʣX\u0383åœӒƱĨҗȵȲG˺мƪiԗˇӄўӝ',
                                                                            'ўǏҞэҺĬÉʵ)ȯϦΖį[ϺAɕԖƑќҰˬСjэǣíºǌĜ',
                                                                            'ŵʹȋӦƵ*ͻαȺҮу]ǔҗÄƪϽΘ҅ʘĻž¹Țзʭφ\u0380ųș',
                                                                            '˾ Ŗӓ϶¨Ђ\x90ζǼͼŲˠԗνčÃӓÚŤϓԉҼʦԂΝϓɪɄŢ',
                                                                            'ʮǈңӨτÜԖ҅ϬbuƇ]˄ҀɱмǨͷӣѧ»wǘеǃŷўѶȪ',
                                                                            'ɂɭȷЀÃӾҜʬ¢ϭөǕӑ\x9eȊ\x8cћ˽әƟȕǹǼȡüђęϷ³З',
                                                                            'iŪgȤZϸªԤәВΜÁή¨ЙęϕТҪћǑѠɝӄȠЩΗҘӉɑ',
                                                                            'ʯm\xa0ι˞PЙéЂԃVqӽŬӱҿï£ЧҮқΡņȅ,˹ņʽԀ¾',
                                                                            '˔Ⱥð!ςΗ\x97ƊQӓĿҾǙҮѫq\x9eÂĲ˙±ʯʩчɼĹӖͽϓԙ',
                                                                            'ǧК˪ԣԛ˥ъӧҵƎ\x80ŸԝĞɻǊ\u0382Ѿѹɲ˃ЧȍćЏäȦǔˢɿ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'pͲ%ǟàҧκŘǀкҙʐļԮƝ΅ʢŻǈÔûɍӀϬ˥ƄҝҜVԓ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŲԛΜЋìÔҢȭлӯƏ˭њ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7037630889722861762,
                                                                            3551669401742579257,
                                                                            -8274676911306168983,
                                                                            -206711567244509849,
                                                                            -8954306150672166180,
                                                                            4837530065741054668,
                                                                            -2377646491248613808,
                                                                            -4420571156232963303,
                                                                            2951202635065971693,
                                                                            442866433088144753,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʱɃдԞ$ȝņͷН˼Ů\u0382ɎǤИіſ4țѓ9űΎōĄʏZ˭ѽɛ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɵǝťȶǔ\xadŖ˧ɼ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'υ3ƷԕǰΧї\x80ȓүͼԠяMК3ǻӜéŘǢɷΙȍĻˍŗҙƙ˫',
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
                'identifier': 'ȨЁʢįʌ',
                'categories': [
                    'invalid-user-action',
                ],
                'error_message': {
                    'catalog': 'Ңɟ',
                    'message': 'à',
                },
            },

        },
    ),
]


class GlobalLoggingStateTest(unittest.TestCase):
    """
    Tests for GlobalLoggingState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in GLOBAL_LOGGING_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.GlobalLoggingState.parse_data(test_data)
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
        for test_name, test_data in GLOBAL_LOGGING_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.GlobalLoggingState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


GLOBAL_LOGGING_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='minimum_level', name='GlobalLoggingState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='output_console', name='GlobalLoggingState'),
            ),

        ),
    ),

]


GLOBAL_LOGGING_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'minimum_level': 'debug',
            'output_file': 'ˠϿҵ˧ɡӛŎ˦ˌȻЙшд>ĸŊҩщҋǄƬƶʶȌ]ϋɘ\x97ӚӉ',
            'output_console': False,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'minimum_level': 'debug',

            'output_console': True,

        },
    ),
]
