# GENERATED CODE - DO NOT MODIFY
# Created on 2021-03-02T17:03:03.131684+00:00

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
            '$': 'ǰʘɓʸρ.`ЌѡЦΘʏ±ĭ˚ӔǂFǒMҚ«ȷŸfȄ.ϋɱ˖',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 5308950916972158142,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 250011.85196026886,
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
            '$': '20210302:170223.597965:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                '΅ǖȰ\x8cƢϠʨǔîѷNƬԧӢzȒҽÖԎѯĔΛόϪēˏϜԣЮʞ',
                'ǮÞƌƺťϞ˩ƝEҌáʠфȐРǸǗƏ\x90ʶŒŻȵȶǃáΏϑ΅ɂ',
                'ϗƃӴʓƉŬwŻȶˈӴùǗőˇӠɈӝŁͷɘťɭċϼ\x7fɎǚ\x86Ӛ',
                'ӲȾŬϵǐƶǘеЯ]ȋ¥ġʸÌӞԕþ,ҾɖǎȉüƆǌʝӲǎʼ',
                'UЂȏɥēäӠϙYϋÅˮƝŌҨƃԢ˽ϕȡǦπЃǪϒʋĘԒț²',
                '˧ǖр¯˵ǘƑФԄӳǘρŇt\x98Г3ǳɜ2ŠÙ\x80˛ѪЀ΅ǈΜʫ',
                '\u0379ϯқƖŭåͰжċƟʅͺ\u038dѵ˰ʬӿƏΚεΫǭɏ˦ĬƍŉѻхǬ',
                'ɝȄЂԈӃҙҢÝԥ¦љ˧\u0378ʶԬϡĚ˟¬ϞsѾ£ˑѓҋ7ôЇŻ',
                'VŸǐ˒ьοѠƿӬǫʱԣЫƊʧĬΧ˗\u03a2ɘ5҅ԉ|pp³\x9fȶѝ',
                'ԚÞśМȯϖĶƠȾŦѝǡϦéӢҒǙŏΞϋƮƸӍ˹Ìɓ[yȕȠ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -4705841955154160941,
                -4152559917018852562,
                211574656521331790,
                5426108273030907288,
                -3455038110864926854,
                4448238032037892308,
                3597856167868071963,
                2055694118662180943,
                2174911084961956638,
                7517506344537715940,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                117109.13482552656,
                429100.78449309454,
                744266.1398922578,
                135989.30381924877,
                812272.197691121,
                203038.58641902625,
                50348.95821241799,
                27919.08088660534,
                939224.0580429208,
                -34482.771300913126,
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
                False,
                False,
                False,
                False,
                False,
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
                '20210302:170224.824095:+0000',
                '20210302:170224.847055:+0000',
                '20210302:170224.871978:+0000',
                '20210302:170224.895151:+0000',
                '20210302:170224.917999:+0000',
                '20210302:170224.940797:+0000',
                '20210302:170224.962173:+0000',
                '20210302:170224.986342:+0000',
                '20210302:170225.013948:+0000',
                '20210302:170225.041749:+0000',
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
            'name': 'ōòһʚăƞɯ|ͷƛԔҁԥϏĽņ;ѠМѺÍŏοӻĸ.ǳҞǽ~',
            'value': {
                '^': 'datetime_list',
                '$': [
                    '20210302:170223.129527:+0000',
                    '20210302:170223.153209:+0000',
                    '20210302:170223.176671:+0000',
                    '20210302:170223.199150:+0000',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ɨ',

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
            'catalog': 'ˋȔШ˯Ț£ҩâКȾЦΑǀͿɳV`ϣс³ɺӟɤĚҹȧŇφЮʉ',
            'message': 'Ǔǎͽ˂Ϊҹ҆ЃќqƭǪΛЖƍɊiɲķʥȀˏϢѵ*Ђź°ͽя',
            'arguments': [
                {
                    'name': 'ӏǎʛӫӉȡƄ\x8dώԋϰò˗ƃϓſˌΕǳ¸Ɏџˡñǌʵ=ȲĕԎ',
                    'value': {
                            '^': 'int',
                            '$': -5319007401804566330,
                        },
                },
                {
                    'name': '\x80нѝǍѼʟγӯę˪lƂȕÚ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210302:170220.927177:+0000',
                        },
                },
                {
                    'name': '"΅ƸƮŅСΟ\x96ǉ\x85ԁϥϿʵ9Ѝ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210302:170221.025974:+0000',
                        },
                },
                {
                    'name': 'ѝƈ\x96ӔŬǝ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        -82737.9139326177,
                                        876947.9330952811,
                                        867143.4621151657,
                                        469502.6445164138,
                                        112146.53048985713,
                                        653397.2828789776,
                                        629612.2378732287,
                                        58593.52575554562,
                                        -99854.97538110182,
                                        50036.685507585615,
                                    ],
                        },
                },
                {
                    'name': 'ϬģϿǵяԋШɔ8Ҕ\x9aуƴɯǯЎҞӭ\x9a˩µƆǳŝΑȈʊťʹǞ',
                    'value': {
                            '^': 'int',
                            '$': -5082635688632502206,
                        },
                },
                {
                    'name': 'ңԓӄʹǀϯȸʍʭ$ӳΈԟӎϊζӉϛќµԦĶ',
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
                                        False,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ıЕίrΩNĺňqʪǵȐĸϦƦʪŗÄҁľŀԣIȃAĿ2ǺŪƸ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210302:170221.889933:+0000',
                                        '20210302:170221.912642:+0000',
                                        '20210302:170221.933449:+0000',
                                        '20210302:170221.953903:+0000',
                                        '20210302:170221.976447:+0000',
                                        '20210302:170221.998645:+0000',
                                        '20210302:170222.026251:+0000',
                                        '20210302:170222.053832:+0000',
                                        '20210302:170222.082295:+0000',
                                        '20210302:170222.107322:+0000',
                                    ],
                        },
                },
                {
                    'name': 'iϣͻѪTԂ~ɍ`ˌĘ%tɎùяЦńϒĠіĐ\x8dkǇҿѐȀȲ˲',
                    'value': {
                            '^': 'float',
                            '$': -64856.687571453185,
                        },
                },
                {
                    'name': 'J˭ēʏǱѲПǢȨѤĢԓɹ΅ĐœɪȘɮѯɢǩīї:Ҝ}ӊċҟ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -883794003984889251,
                                        2470181804161194015,
                                        -3969666931558686485,
                                        -379903343878134368,
                                        1195221540248475624,
                                        4230132979315454447,
                                        -4700516421503635236,
                                        -3550425042203550750,
                                        -8215793685800414953,
                                        -2944518823813928053,
                                    ],
                        },
                },
                {
                    'name': 'ЎΊÂ6',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -6069699469929619937,
                                        -396104274848133424,
                                        6316196258593885949,
                                        1275873876524071455,
                                        4963904835409347733,
                                        8584926364889945873,
                                        7844919866932784581,
                                        6063060496791732819,
                                        9121006968339996213,
                                        4909000430909655287,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ϡɕ',

            'message': 'Е',

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
                    'catalog': 'ЅҤgĶǧʁåίƸǑɒӬʘȾԋȽćɎ¸ԣϮЁЄԢҁ¾ѱɧÊ˔',
                    'message': '\x8dϼ\x80Ȏч\x85ęҡ#\xa0ȬÿǎѳʘΥYҍKőLEϤƗпɽŹѲϊЊ',
                    'arguments': [
                            {
                                        'name': 'ȲǜԣѪ˩ȼ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:170159.594938:+0000',
                                                                            '20210302:170159.609732:+0000',
                                                                            '20210302:170159.625248:+0000',
                                                                            '20210302:170159.642827:+0000',
                                                                            '20210302:170159.667701:+0000',
                                                                            '20210302:170159.683252:+0000',
                                                                            '20210302:170159.698271:+0000',
                                                                            '20210302:170159.718273:+0000',
                                                                            '20210302:170159.739779:+0000',
                                                                            '20210302:170159.759582:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϷΤĉȜ>ӁƖĈδoSē¶µƗÃŌÌӺʜɣǯ΅ƇѵԣŞąZǵ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:170159.914739:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ю\u038bˏȥʩƻǆяʫęȾԏҎξӼȦήɍοƽāуȐΒTӅÉωEĵ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ЬʭҭȨӉй}śʪhk',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:170200.068631:+0000',
                                                                            '20210302:170200.092761:+0000',
                                                                            '20210302:170200.111785:+0000',
                                                                            '20210302:170200.131442:+0000',
                                                                            '20210302:170200.150611:+0000',
                                                                            '20210302:170200.169543:+0000',
                                                                            '20210302:170200.187273:+0000',
                                                                            '20210302:170200.201513:+0000',
                                                                            '20210302:170200.219161:+0000',
                                                                            '20210302:170200.233338:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǻȓԖӰεǃиеʑɻʋщ®Ȟοƹϥ\u0383ӀĊǽɁ҆ѷxѴŲϳҖë',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'жśрĒ˴J¨ѣһÚÐҡaȈΰΗÚĈͻХǴƌǹƕä\u03a2Pȏћ˧',
                                                                            '\u0380ɖȋȵĢШɥӕĆюĪǭŏϓ\x95ȼȑÔɓвʟXқʩûԝûϿϱί',
                                                                            '\x8dŎ¾ȊǲșʨӭɜӠƙǟ{А\x8cӎδԅԜχɳһǃѺë:ТӭҙӔ',
                                                                            'ʋšАϮеȄƥΎ\xadɵѓ\u0381łԬʍԃƔňɁѝӅïæӡƪ҄϶ԗƆχ',
                                                                            'ӀǬΨϧŒȋȊΗÌɿǝОĜӴWΙǠąМ\x80ƲĳɐňӍȠ˫ԕǞ\x91',
                                                                            'ЙӴ˓ÑTƪŴUơЉ\u038d"\x83ѲǳϵųB\x86ɪқϟşџɒɺҠԈΕϬ',
                                                                            'KѸȉʸɬʮ>ÅȼŧƆˑƢǩѪÏİHг\x99pѝõʰѴϸɋTˈˁ',
                                                                            'ԒɓŗĖŐNΊΪ5ʼLŃǢҝä˅ŇʺˠσԣȬɨţľŵМʆt¬',
                                                                            'øýӕЩ+ĥӪǆȢɱ,\x8dǸˏРɌơІǰßȰɚˉ)ˢѾԩyƖϮ',
                                                                            '˱âƀəÎӤԩ˙ԏ-ĠǵЛęŊŁȰСʎdľ\x80ѮȦ˒ʕĥЋǀĘ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŕɴĺͰҴÌǩÁϥԧʢļƣ¥ʤυψВңN·¸\x80ųβЍ͵ ʴ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'eʢȤԍūļLʮ£ėӸϧ҃țψɲŤÇˎ\u0378ËӽϰπeΛƇʄȑ˭',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6683899625698459924,
                                                                            -8899667330135078296,
                                                                            -9023965761136260596,
                                                                            2976732334763627305,
                                                                            -9134671832094996806,
                                                                            -7512422953195181639,
                                                                            -4457954773439259295,
                                                                            -2731718062268243861,
                                                                            -8369415406613488355,
                                                                            -2701641024046998889,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ίn±ˈВмXνѰήА˚Ԫєgї',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΞÊЕǰǋӉԭӒϭӊҜĢҧ˯ɓğɓ˦ǊӞ&ЮЗŭƊӬӝ҂×D',
                                                    },
                                    },
                            {
                                        'name': 'ɡӧɍЙј!ƊӬϤԒĂn',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            127485.71297793087,
                                                                            783073.6358330555,
                                                                            412932.3217178854,
                                                                            647386.7661714063,
                                                                            318521.6358669287,
                                                                            790471.1786951869,
                                                                            386921.6835351798,
                                                                            449666.7899220425,
                                                                            101315.60996333684,
                                                                            698873.4581341005,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΆŸδҾӾʟ¢ÙʢΈϺ\x86ÕΥљpƁơ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϹȤбͱ\u0382ћʸșʴБѽʚӈНĴ\x9bˏˣƆņġȵıϱ\u0380ӳͶůӑʯ',
                    'message': 'Јϳɬй`š˼üӫSȰγõˣРƄŵҥǱҟɊĥӊ\u03a2ŰÔ˶ŔӰӜ',
                    'arguments': [
                            {
                                        'name': 'Ҡ˵¦ɐӨɭѽѯƦ\u0378\\Ԩ΄ҔǹpƽŦü˯σӷКʷɟϳθѰ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -12123.32136576595,
                                                    },
                                    },
                            {
                                        'name': 'ǴͰˀѱΒMѡȘƬȎӟԐˢфϒɉFДťĆȍȺwƙήÏřŖ˻ԩ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȶѢʌɨƈЮӺŁńЦpӗήÑǟ҈ϵRѧȑnѳҎӊҏΉǆ˨\x95e',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Όυɐ҆Δş¯ȁӹǳωyЅĳ\x9eњϮ0ƗʄϛΞƎǒˑЉвӱ\x8fŀ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4540589112044615093,
                                                                            2804096411276446632,
                                                                            6381992676197387184,
                                                                            8621529474443748158,
                                                                            3923419844176828519,
                                                                            -6579775043706825566,
                                                                            -5733019849703569646,
                                                                            -6804771286561492364,
                                                                            2789512621063543972,
                                                                            9035270459900583261,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӸЄʔΖȎŵſ/Ýǖ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:170202.019281:+0000',
                                                                            '20210302:170202.036657:+0000',
                                                                            '20210302:170202.052713:+0000',
                                                                            '20210302:170202.070628:+0000',
                                                                            '20210302:170202.087228:+0000',
                                                                            '20210302:170202.103334:+0000',
                                                                            '20210302:170202.118353:+0000',
                                                                            '20210302:170202.133058:+0000',
                                                                            '20210302:170202.148497:+0000',
                                                                            '20210302:170202.163154:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǥƶϲԁϩ ÇʻȈэ˔îÉό®ŲŚђϙŃѮҎΊъҙѕ˖ŖϤ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҘȕːȦʮƯÅпƅӹʳӐҲʮƄȼ´ӗƶѱ\x7fӐϛ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            562596.5026139192,
                                                                            -26442.769858914253,
                                                                            -67079.11864596233,
                                                                            889874.2630323478,
                                                                            428296.47665161244,
                                                                            718425.9627438275,
                                                                            555387.9639016738,
                                                                            8777.165118969788,
                                                                            415742.9663549368,
                                                                            163835.4368288432,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'νĂƾϝĬѱǲ\x88ļѼ\x96ƣr',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:170202.543952:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǎώʳƁȹØɜ',
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
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȖʪÒԉȻʬǕɪСԜǇħӕƵάħрҍАЧʰѪϵщóԬ?\x8e\x92ύ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7326547213660019469,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'řѥЫʃŒӻ\x83éΐΈɣǎҸ«\x9eǬʩ×ϢfǖѕόśҷNˎȚӫȿ',
                    'message': 'ǂ˖ŨϿɇ˓ϱɌıʁʙvǐБʲɀӖˉ\u03a2Φ©ʈhԇûƜĬȓʥϱ',
                    'arguments': [
                            {
                                        'name': 'ʹԮÅIϣ=ΝɼĆ˫пѕӔ\x9bǲ\x9eӥ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            538125.2702311334,
                                                                            3898.6625371847767,
                                                                            655416.0446979811,
                                                                            291674.16322603205,
                                                                            -50239.0579657954,
                                                                            -37979.123232550606,
                                                                            388613.181086646,
                                                                            731381.7528426164,
                                                                            -32819.741554514534,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɉɈ϶Ԧ¢φɹƜɥǦ˗˹ԍʓɀǨʨŎú©şυˏӌ+Щ¦Ԝ˷ʹ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:170203.274818:+0000',
                                                    },
                                    },
                            {
                                        'name': '˜SͱȚ\x96һǟɇΜǣǅǯi҂ɬȵТ|',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8553033475075874077,
                                                                            -5273036914200499129,
                                                                            4500118875862650623,
                                                                            -1617128915230056463,
                                                                            -4772147654117384639,
                                                                            -5101262359813702734,
                                                                            -8804818087423909741,
                                                                            -3765411110188107526,
                                                                            7457590143258529967,
                                                                            -8054447376045756238,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԧś˖ҘɃ\x92ѧдӶǺ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˽ĈʟžД/\u0382ʭƯβœ\x83ǂѢҪȄˋиǘӷȏQԓԔѣԉʳϟįƻ',
                                                                            'ΑȮӕ˵žţΥɑӒǃĮʲ\xadˁʬɹȔȻŜʊҵũρԐȩҐvȯJӏ',
                                                                            '#ѐƽÑÓm\x99ԌŤŏɛϔĆ΅фǏ˼]юӀϫÐǠǧхʞāˀє\x98',
                                                                            'ƙìɇΒҝÞϫũÏϜȍԖkȤӭǰƖ\x9cĵԔǟΠƔʂęÒĐѢФӖ',
                                                                            'ƵŵҎКӜȼѾőyѽȄîɚFҞɎțӽξ\u0382\xadκëϽЭѪʅŠƱԭ',
                                                                            'щєӚ\x99ĉ\x86ҾʛƦɨŪǚF˵ŏkӃČ±Ƚ§ѹǭ˂ÆɍѤǤвƯ',
                                                                            'ĪьӽɂоɗюӭȢėʹԄӪћҞƟҫȺŊлċ"Ίěʌʘϥůyɳ',
                                                                            'ěȍѧƎô}ĩ¬çѷγә҉μĦΑʎɽɦВ\x95ȕĊТêȋ˦ԏΊѧ',
                                                                            'ĔЛНԨѷҭӁԬǒ˨бǃӓƜμʃҚĦǙɆǂ·ǬҬЅc˅£\x89ҽ',
                                                                            'ˁƢŴïԃʏȪ҆əȚǺѺ˙ȷǁǚλ¡хЛ˓έǭʹӁøΝà˛ż',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'éɸǰɥˈȒȫƢ˅ƩѽʝωəɥыӔȶωӱǒԑцʒƔŹɯ˸\x8dƸ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'зƿâӲȚɋ˓ˌΌԌȳĢɘ\u0383ԟˋʞϗāϝȬґi-ЋǆȴƬeϝ',
                                                    },
                                    },
                            {
                                        'name': 'ҸөѻŮ\x87ĄuǶŌЍĈӵԃѫӭŮǈʳˑП˘çˀ҆ňå\x9a˜Ѧ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:170203.867016:+0000',
                                                                            '20210302:170203.881699:+0000',
                                                                            '20210302:170203.896446:+0000',
                                                                            '20210302:170203.911629:+0000',
                                                                            '20210302:170203.926433:+0000',
                                                                            '20210302:170203.941412:+0000',
                                                                            '20210302:170203.957642:+0000',
                                                                            '20210302:170203.974936:+0000',
                                                                            '20210302:170203.990130:+0000',
                                                                            '20210302:170204.011051:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȲȞƄˡуΖϸƜś\x8fѲԆűʓϦɟϯ\x91ŚΓ˥Ɔʃ~ơȺɫϊŔȯ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            209564.9711296318,
                                                                            303132.94255843025,
                                                                            471301.02510004677,
                                                                            54768.61986942036,
                                                                            408552.313480341,
                                                                            444427.9481887787,
                                                                            456708.6723126223,
                                                                            438162.3627144053,
                                                                            963209.67469054,
                                                                            -55987.32729111732,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӗɓȟϱ\x8faѰÐȖ˼ƷͽǊȐїԂѪ϶ϼ˟&xĪǬєРϒÒƦΜ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1751995097207434384,
                                                                            1122836894143728764,
                                                                            -1049615241833507278,
                                                                            2568827030433854255,
                                                                            -3708528837053731681,
                                                                            538897492778570290,
                                                                            -8251984368575072194,
                                                                            2486953126434421494,
                                                                            -6846065848648666140,
                                                                            -2678132564229167517,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЭťЦ\x8aσÔέӢʴʓƤʝèϡɮċȵΡɑҼфѸԑ¼ԬâιΛԍ·',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2890730972270564346,
                                                                            7669290945499859678,
                                                                            -3789379304777806360,
                                                                            -4373411860664512436,
                                                                            3036306925959807703,
                                                                            2590711281416480663,
                                                                            -3467855358731288342,
                                                                            2466402896435289765,
                                                                            -3149348250790627351,
                                                                            3421464816271044335,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Hʷ§Ƃɀϯūɪ˄˔ѯӾԉʢъȕѥԖҋƧ¬ɟüƔԇϷưğɌ[',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:170204.882291:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ëʕʍӛʢɉчmƿÛҳɀƟŜӼ΅оҥѶϱʄЕҝ=ϽȏѴʗԦɺ',
                    'message': 'ҭώϢҾʀδтȦÕƥƠŮäʔTłèζɽ;Ɋÿǽ»«АӿSǚȴ',
                    'arguments': [
                            {
                                        'name': 'ˏђӃČ˻ÉɎˬѝĦԠΐêǷѫцЋʒƻİŚÆŉψĸŻŅƋ˕Ό',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7568341488090890999,
                                                                            -3929365373176143486,
                                                                            5187888203230254621,
                                                                            -5835236769405790136,
                                                                            8307178387216933292,
                                                                            8305855851810500168,
                                                                            -5340488473305680250,
                                                                            4021170010046984798,
                                                                            -7458462437372729066,
                                                                            7107790258007616455,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɑѠӳɰӨЀ²\u0380¡ϩ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': 'ҝӶυɑ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҋξ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6988121012112221879,
                                                                            7463565488386333761,
                                                                            -5380422962460677490,
                                                                            -8545286098382429485,
                                                                            7058062822167453312,
                                                                            -4652308704459637280,
                                                                            -3003629296695195061,
                                                                            1500850558323890623,
                                                                            -7329627209465465562,
                                                                            7870754527701997322,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŦͲŌСðȞϬĕ˓ʶ˸ͼʮɭGɛς\x93У',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3794582448644257579,
                                                    },
                                    },
                            {
                                        'name': '¸GȒ҄',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7734142752613184139,
                                                    },
                                    },
                            {
                                        'name': 'ЬĿҞʚ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˽ŷðϤ˱Þˏʹ¸\xa0Ģ҈ьĥɆÚԜëƃӅǞѱȳѿˍħӯ҃òƢ',
                                                                            'űȞƆǲγʊψǯ˛ҒȁʼКàĊƲĴȡRκϔүËìҵЅӔԝΤœ',
                                                                            '÷Ĩ\x90Ʉ>Ɛı\x92ԗ˼ӷʺĮԦÅԛЮҿæҗīƼēϚҗģ˫ҺɯŎ',
                                                                            'ɜщŪԍ\x81\x91ΣңӉΛ\x9bƦӌ®ӈǚάΐöρĔŮԊʀʵĘɴє&г',
                                                                            'ԕԙʾˠȕŷȻѦʍüΠąǄßȢɟıì-[˧ɦŨşʄѭȚŸȊШ',
                                                                            'ƨеԜ˹3κ˯ѸșȧԭбŌĬдҐϗKӳҮ\x86ǧǙͻ3ĿʃƄΘƫ',
                                                                            '\x7fӒԜϳŭŰϏͲԝŃģÅӈņōΓϲ\x89ͼɯÊȦЗʾȼѽεɢļͿ',
                                                                            'ɞŤɎ\u0381҈ʐɛѳ@ӅǗ¨ðȫŧјϘɁϣӜžѧƸ˚ѷªҰRʲF',
                                                                            'ҨȝQǓʜʼȭϸ˻ԢĀίӦɫԏȐĪоƮÈλ',
                                                                            'ΥÔИĎƧΣˮiˀāƥ˰HΆоʱ;&ͱȊԗн\u0379ȱũƜƐčƼɲ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϰɷʂѯŮƏҴǰȳѻdҎſǦҍȤ¤ӴĳȈȹй',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҀŖԋԋƪǋȕ΄ρŽέɄѩȏЗκʟӱ9ÿтǀԝҰʉѽǘm2ѥ',
                                                                            'ӎӧŁȟˮȬãgÖąϿЅŌƎʧnĕȩŭҕҕͼӫыТ\x94ѯǡRѯ',
                                                                            'єʑąʡ&ǘӝŖΦτ±қ\u0381ȍŒκȰԝţûǄƸԤɴîÙ\u0382¬ɬł',
                                                                            'Æ҃ĘвÃ˧ƉĮĲ×њɓӵҀʤʣɌɽдϤȬ˩ҳɟӧǙӍΑ\x90 ',
                                                                            'ЧƷӋРǒҴϟԋȯ¿ɯʔȹđʬǙҸĦ4Č\x93\x8f7Ғ¶ĕ\x87ĤĪf',
                                                                            'Ыȥ`ѿʉĶɼÎóѣЏǳѯ\x9cˇĔémΒӟĂHȧҫďҦâӵȨɈ',
                                                                            'ƗКΪ9$!ϖȏшɿˇɃ8ѦʇҰȋŌˍƒjυєкʗ\u03a2ЊζOг',
                                                                            'ʂȥ\u0378ɀӴԇTė˙ҾɅˀÑҙ˨ňќƄvҙҔšѺѨҽȅӧ¦Λч',
                                                                            'ԙ˦ԗīƘŢδʹʲŵҖϞ˧ӢΚ\u0383ȸÖ˃ȃ˙ϬɣâƹʘŲ\x96ʶς',
                                                                            'Ø҆ȘӇʿ\u03a2ӈ˷řШɭ¼\xa0ĶӳȶѾǇiðȜȕңͼ/ѷпԭΖԋ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͼɎöΐӨЕΓӡНȦxӸYɤσċǳʲɏϬƢùģõ]ѐɇξǎϪ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӪǛļʪŁǡψɯɘ>ψһŚӂйԟɋҳ~ŁƳҘͳÙ\u038dȤү',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            755845.9672186222,
                                                                            282977.51266507525,
                                                                            15183.679837524789,
                                                                            637557.0069066784,
                                                                            489067.87504659104,
                                                                            474124.4621535905,
                                                                            430949.4834533497,
                                                                            299200.5925969028,
                                                                            539124.6343224824,
                                                                            435273.53777396935,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ɍϥå+ǃÄ҃ûcËЭӉΩɒ',
                    'message': 'ϟųɡ¡ԕОҨʽљӭ˳γzȻϳ%ϓњǑͽɆˎɲѐƃÌҚЇ\x82ӊ',
                    'arguments': [
                            {
                                        'name': '˘ı8ĩӄВĒŖȓΰœ{ºЗǪΨƢ0˵ɽ`ӆʐϦȪԄɦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ΣѾ҇ȭʥŤť¸Ԙҩȿʂōʑɥ˼ϯãˮʼʫɄԑȢѫȝȻԢIˏ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:170207.721808:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ԅó:',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8079438307408277806,
                                                                            -6843897816930679251,
                                                                            -5927328628226892076,
                                                                            4707257383676663682,
                                                                            3088373970139006274,
                                                                            -5819159721213802361,
                                                                            -8866667266339398126,
                                                                            -6219408296427413418,
                                                                            1379091489563122218,
                                                                            6730464265014444316,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȜȇǸșƢҚҦŦĹҥ˦ΎӵÞҶǮʛӎЌŚԣϵ´ѐΠԝȋӾǍԔ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1218642138617301250,
                                                                            -6570141194001296708,
                                                                            -4841976207871785717,
                                                                            -3565978452261084185,
                                                                            2211210032277312339,
                                                                            -1164019380377088629,
                                                                            -5082786775787813480,
                                                                            -3288448563017572759,
                                                                            -2827741071078460511,
                                                                            -5513777855619215052,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԓ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ĀÎPϣҺ˒ЩɏȬѨíəҲ;ƹҸӴҾ\u0379ԥˠŜˇϭԄўŤǰ˒\xa0',
                                                                            'Ԟ<ŘјЯϜǼĔӂuÅԊ\x83ʖbɗӬѻӽƍ˻ԕ˃ǆњһΟ\x98ҧʷ',
                                                                            'ѼΉμͿѬюϠƭ\u0379ðȧϩƑlϔɾϮҊşÈUsˎɷŖŴт˸\x96ǟ',
                                                                            'wîχɝЛǥǼÐǗɿӜһɀ³ǥӰЩ\u038bĂʁůƘѻ#±ØȺƴԌǉ',
                                                                            "ʗ'χϮӦν\x8bҳý҇Ԝ\x8aȪΰΡʼŸҎɊɭϺҴƆӏϝфҫȚԚп",
                                                                            'ҔҿЗȶԧҔǜҧһXʋԞZҌҲF]ԓĹ\x82ϗϾѱşĜԛƼƧӬ˲',
                                                                            'ɱҫdʵƲ`úƔUďʮϼÝȤƝęż7ӋˁʐӕȊӯɎ\x80ԗӢɛӥ',
                                                                            'ħƫǫɒśȝƭѕωíˤԖӏβԂyЏƹʃԥИϐȁýȊġÝɨsʠ',
                                                                            'qÉɫŎʁωʁʿϦĖWcƓŀʇΨƭ¥΅ɳįĤʖǴ»\x7fȫɻ\x9fļ',
                                                                            'Ҳǁ˼ѲʷйƧƹ\u0382ӎԆЭςÛɔƧ\x9d»ɳŉΗʺʮi!ō\x9eѵʳӊ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˼ƠԎѪκԣГѓĴǮϹǎ϶_ßϬɗȦԍѴØЕțϳȥӢ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:170208.744337:+0000',
                                                    },
                                    },
                            {
                                        'name': 'oēɷӼéҽζƀЂ7δԜûɚȃѾƯþeɱλńˏȉÜñΦѿчŮ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'gҦľфɇ\x9eЫhȘщ˳ǉ«Ï8җҐӾeмЦ˕ˋǎ²ȿÞϨVο',
                                                                            'ȩѸӹ-ĴӒŨĊǇ˰Šɋ˲ƠɳɉϧaƠÚȞ¿ϠȭҩƏǭԥМП',
                                                                            'ӲΙѻųљПԞѰϥȣǕǾɴǀĨĶ˸ǆĖǚ҃Tȯ\x9aӡʮӊŵ ԓ',
                                                                            'ªʌʰ҇ȳ\x85ɔӌͲȋԤɤÎԣǳЋưӡ\x96ϰč\x89ʸδҩɈ˺ӐǆΨ',
                                                                            'ɟǆlǟͽŁŵƜǞϙŭƦƂĖʍˣɼæөҗԂƊχĖǳӝƞӂʋÃ',
                                                                            'ÂơϖąǼ\x81öΙԒҿѢЧ\\ɣӂΞӷЉԐϋ¾ťΦx@ҕĻԩ˓Ӄ',
                                                                            '\x83ӭʐDʵÌӜç!γʘȣόǄѰˮӁ·ԐҳϬKёʵʐɢkӡ¡Ê',
                                                                            'ÁǐϪɩԋƺĮŗKΜĲɺòң҉ѾŕϨ\x84àӚԈлЊ½ØԣϧĬԀ',
                                                                            'ԞʏΰӺņʂÈѡɃёİѯϔɘғȭӚȶȐÀҿǠΞԢϽĨƙȉӠϙ',
                                                                            '˹ϋʳ\x95ǵżҞɜĬϚțӫąΟ˷ŀƵț#ώŪƞźӺ\x87ſ\u038bϲɼS',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѪŘī¯,ϓҰȕӸȔɷŌ\x87ˍ¹Ȫƀʖ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'μɃʐˁĄ\x85ǪΗϣԑʈƶԍΩǭ0˞ʛƇϊǷȪ˲đ˄ȝ©ŘӁˣ',
                                                    },
                                    },
                            {
                                        'name': 'ǢШ\u03a2ƍЋ˚ӗԚϟӺӨEβ©ʴkӞψȌǜÙƬɠʆ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "ǾΟ\u03a2ʓѧȯǪӢʔӾ\u03a2¸Ũ'ԩ\x85Ƃ\\ƭ˄ȹзÙԢ'ƨĨŐǻ˹",
                                                                            'Ŭϛ[ί˃ΒО.ӽˊΑǦάΛβжĚĠӟÓ/πʎӶŅӡǷсɩ˥',
                                                                            '΅,¢Ӌɡˌ3ԣɬ{ϱńЙϬǵÝңϑХŕҳŚʭҧӹɋβӹșӋ',
                                                                            'ƋCЏҎѿрà˃ßҪʲĩ`Ⱦ\u038dǦãɒԂŉ\x96˨ˀ,ʜҠљӖȘİ',
                                                                            'ϿĄǸyγˡϛВʿM˯ºӗǂǸǧͱǴѵƊЃʕͻĶ\x99żƍǈɫă',
                                                                            'h˛εΣÙ˾Cλɹ\x88ɏ\u0382ȯΙ¶уӋϙ҇ΰɦĎчϕǝҠѣƳƒɤ',
                                                                            'Ù˝ǁΝƝÎœƻѳԑˈĊԛâϔĘϝȓѴɂȍ\x9cыѫʭϤǤǗН¡',
                                                                            'όѹWŅǈŗΐҏƹʃЬчǛ˂ſƩfʕɢöè˚¥ƼϬͽϗѓԖ©',
                                                                            'ȊȈǍϣԈЇ˽ǟ˜JήΌйºθЅï%ƶűҽԤӲЕϬӾȃƏӹТ',
                                                                            '˅ӝ;ѠÁȿ\x97іΓЎƝңõʡ҇шƩħ˰ϥ\x98˪Ӓƍ\x7f˩ԅоҖķ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˑҖÅѧӁ}\u038dƅаҙϩÖЧѧi˅ΫʜêӁϱЂ\x84ШƄѤА',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΡǱȃð5\x8eŸ\u0380ƑύŵΓАԭĸο¨ǥυ΅îp҆\x95ȅǮӯɾҊ\x8a',
                    'message': 'ɈϡȥҀǒBЦ£ɎҬʞɠDԇԟжтȖѾʱŌЛˆŋȮΤԛƐж˕',
                    'arguments': [
                            {
                                        'name': 'ǷԨȍğ;Ԙӹ0ĨɫƈǮɟhƕԐԠʥӊƉʳϮƹXїƟ˳ӱÄˠ',
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
                                        'name': 'ʷȕǆ˲ϡΠсʕʢÖʑĳӠӌ²ýĤʥŮϾΔǐʽҚԑҢтʳԪȷ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            414047.52306539053,
                                                                            616627.0184891227,
                                                                            422060.1982408501,
                                                                            744141.052552015,
                                                                            667872.6173294589,
                                                                            643336.7432345011,
                                                                            650742.8971113641,
                                                                            997546.3398007369,
                                                                            864384.2919332895,
                                                                            191999.55975029274,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҬöƜлϬηԥŽ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɾϘӂģɓͲÉһηҶӝȓǆƟɳmԠʯɴƋȿӪԗ$ǻÄƌ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʨʠҟΦƐïԝWӒѪSÚѐɻ˫Ҡ\x89YUǾåȮĘǨԠXǁ˧oĚ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 3715.5897051411303,
                                                    },
                                    },
                            {
                                        'name': 'ӟњϛÁɝ\x8cFśȚ',
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
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŷRʳіҝxЌϊɓ΄˒κВӘѕĝƠà<´˸Ԍ˓ǻ',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˙ϋϦƷƝϗϹҴʮԀЍëɉвΔżʋ˲ƼҟѴɎŮżÓůŵϤӚƂ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɞːȎ҉İЧӔəŪӂǐхѧЕɂ²ƹρ҂¸εѮŚˣóŒ˝ѴЕɉ',
                                                                            'ϡнӸʸʙΎƝȐĆ˽MҞɘЯˌєŔƸʭčÑі0ÿˋЂ;ҏ«Ԉ',
                                                                            'ŖӧΚӃɻȡZΜӛmβ˪ƷІĄ\x82ҼяƣƅΜˠŃԧԊПʹΰɢɘ',
                                                                            'ԙԥŨ\u0383Ƙ˹ŒѾ҈ƠˆӈĿ¶ԡƹӎƚуɾɕЋʗΎ˼ͲɑɃԪı',
                                                                            'τћΟЈƢҮΞÞƜҴcѦӄԝţ\u038dĊƙНнʮϷÒɣҭԤν³ťǐ',
                                                                            'ќʳҫÚʱŷ\u0382ўóД\x9aǟĆǬԉʑ«ӘƹPһɾѝ΅üӶоЄ¬ș',
                                                                            'ȠÑŠƾУ-İˡɹϐ\u0383éѳƙҘκŽӝʥýŚŲÂʙЁѥȡ˸ѻʿ',
                                                                            'ŶКǑ\u0381ȩÛ:ŁʙΨΘȄ˄Ȕ˱ԥɑ҆ѲӥƻԇχžŹʒι˭ˈԕ',
                                                                            'υļԊΘώɯȂ˽ΑŅĳ\x903ȭıƬΙƒĩɇĉϼȾǁҩϷƲ\x97ϵӿ',
                                                                            'ʅˀĜАːԦӐѐʁʗά˽ʒÈуǥˁѲJ`>ƪ`ǥğԓΉǛ}Ԧ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɽ˝ȸʹȿrԡĕʞ\x80ΉȓγŚ¬CƂȃıѩĔ͵п˚ǮŵńҿҦϻ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 242431.56523573562,
                                                    },
                                    },
                            {
                                        'name': 'Ԓϟӿ\x8fЁǿĉҜ˯ѡҖëύiɿɭшԠ˭ϣȥβkȒˋĵáвĉȨ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3620043240473491244,
                                                                            6109194202123729565,
                                                                            4126170195233812697,
                                                                            -1431366778580761538,
                                                                            2951134918722757258,
                                                                            -659411077913127563,
                                                                            4024487202763957550,
                                                                            2108607482398659616,
                                                                            8791608006318107549,
                                                                            -8393673136599378169,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǏŜʮʣˆƊʡчƨѳǔđ˃ŒҀɏԔЎÖKŒΩѥ¤MǩɉҗĂê',
                    'message': 'ĠÓҺĶӃǵǢē\u0379ҩБ҂ǃƐӌ°˻ЦGʈΰ҃2έƛΥ\u03a2εʘͲ',
                    'arguments': [
                            {
                                        'name': 'ǕPԚʓƁfТpǴό',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'đө\x82\x9fĈ£ˌǴèºƿҘμŠʠϏɫ˨Уɖ5kϴŁϮӥȟʤщ\u0383',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɉЄϼϘпˎnщʇˈ>Ͱήͻ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2254432048896708849,
                                                                            -2531503075914575239,
                                                                            4471342991218761151,
                                                                            -6859319537843531459,
                                                                            9116590981593424284,
                                                                            -5893420206765059099,
                                                                            -93315539221842198,
                                                                            -7733965994655123860,
                                                                            -3424467956187451141,
                                                                            2771776113256237227,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѥ\x9a¤cщÊƔŖyЕƒǫѨїҔ˖jɚˎưĢԜѦƔАǹȞ˯ƴǡ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:170212.825506:+0000',
                                                                            '20210302:170212.848967:+0000',
                                                                            '20210302:170212.869829:+0000',
                                                                            '20210302:170212.888551:+0000',
                                                                            '20210302:170212.906499:+0000',
                                                                            '20210302:170212.924459:+0000',
                                                                            '20210302:170212.943674:+0000',
                                                                            '20210302:170212.961911:+0000',
                                                                            '20210302:170212.983060:+0000',
                                                                            '20210302:170213.005262:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x88ʣǏԧ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '-ɪЯ\u0383ĹȲöԣɡ\xad\x99ԗ˟ȦųϪ¬ΘçƻĈȈʏőxҤҽTϰƩ',
                                                                            'θĂȂƼªOЏєɍаɉіюΨ϶Ϭ²ѦɗϫNi`ăɹǘƶҨƇm',
                                                                            'Ю(ŲϛҒ˄ҀɗǨǒ±ʢȔʗҀ,ЩÚԑKʚ×ȿάſI1ƞӷԩ',
                                                                            'ɫóʎ^ÿʉ1˂Ȏʍm˧ҶЫ˘Ğ˟ѦԬʠфĈБԈʠeɱŵθϘ',
                                                                            'ʋhï$ʼвśԙ%ȥ҂ȎȻŢūǙͽ×Ŝ;ǒÜɲӍлˠǁʼПӤ',
                                                                            'ĽҟȎʒ҉ŮƎѮϐ҃ң<ǌςˮӣģņϵЋ[εyѦȲ\\ǦʤҙͿ',
                                                                            'Ōєġwßγń¯ћЀѱӐUtùΕùчƦʧжњǻӂϙ¡Ⱥˉбi',
                                                                            '`ʩфΒβғ˹ԣSćʹ\x8bɿϣàȜʛԑʇqϱЗΪǎˋʩȝҖөҸ',
                                                                            'ȔǣȜǴˤҚАƹ˘ӂ\x98Ӡͽ¥ɱмӜȯɏæǁˆҁ҉нƊ\u038dѧrѡ',
                                                                            '9σȿkӤȱʹԃǯęƜğǠ¹ќΰԎǙҎϑÃνØԤĴȓǉԦĐĆ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÛѣR\x81Ï\x85τȇȁϮΈЏϠUӅƦ[ѼȟƅǜҢÉȀ(ĜÉӘʫˉ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            294842.31950373604,
                                                                            221426.8142245072,
                                                                            864622.1011924203,
                                                                            273498.69146527303,
                                                                            104983.52194744864,
                                                                            775832.5251936922,
                                                                            41258.139800135395,
                                                                            -15303.816908627705,
                                                                            61639.13922435939,
                                                                            140184.58826724932,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԤuΟПHɦ˼рǋ˪wa',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8131652333317087938,
                                                    },
                                    },
                            {
                                        'name': 'ӷӺÆŔӖ\x94ǲѹʲӫ˲ѵү\x99',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǌӰ҈úŊ˧ƧХ\xadɧiҫƫ˰²ч¤ҶϹ(ɈđʎˌɾςϠƔǭԠ',
                                                                            'ԫўϭʭύΨ\u0378ӐɡѶŒΩɦƁ\x9dτƺ\u03a2Ƴʦ˼ɉEʏ˂щԛˡÑɿ',
                                                                            'ƠΗɑ˴ҠΤПϑ\x9fʕȪЌаɁ˳Ёǉ˻:ǨǺԍϼċԓТįʛϬĿ',
                                                                            'ͷʵGǑӣͰӱÆɵяФ˄˲ѯѼŇдͽȖ6\x90дςŘЫşʓӟ"ǟ',
                                                                            'ˬ\x81ԝȅţҐȰԝраϢμȟ\u03a2ӪӗυýҠåϦҮōθ\\ӴƕǡŕƏ',
                                                                            'ӧȱ0\x9fԙŰzКӀ¦\x81ʒȰÛ\x84ԢȋѴ˸ZȞƙБԕȆѺxάӴɭ',
                                                                            'ňŝȧÿ0ƷƠƮ¹ɱДԍ˟ηȺɮҿ\x91ŝҕȊƈ˃ÍƧ´ʙ˂Ԁӗ',
                                                                            'ҠӚlԀ˓˂ˏϯģӣ˸Ȼ˪×ÑɗĺχȹҷȠƩҼΜȭĘĀϺԌ¢',
                                                                            'γˤˀѕӑŋǥȘӾƁ§ʀɍɯ]ˠϸɋӎƣˇƫӉɧȻƫϨУɢр',
                                                                            '˼ǱѧżóѥɔΆЍċśϨŶBŰʋͺ³Ÿāʲ}˳εMłȩԟȿƐ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ʹǙ¼ƶĮϭ,ӰтԖ=ϜΊ'ɫϨнИʚѲʒǕgɩ?\xa0ѝǞʵʬ",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            344046961132037420,
                                                                            7238995298727556535,
                                                                            -5393829739468404422,
                                                                            2854649291919735231,
                                                                            2681161914771737644,
                                                                            -6016613663775828335,
                                                                            1795230470449360966,
                                                                            -503400430206192300,
                                                                            5584137153671773855,
                                                                            -1955908410766661103,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƌЦηр9\u0382ψ˖ђ˝³',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4665118228267951757,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ìɽÅĂƸԂфΜϫΆƴӢɧʺјЛʐӷɥӝхS\x85͵ѬƚҷΝ/ʮ',
                    'message': 'ӫТӱʨK´ЪѥȕʶɞĨȐĩЧϹRʏΥҮøǢҬʿɹÖНԘ¼·',
                    'arguments': [
                            {
                                        'name': '.ɆźȬŸƌҾӄԗӝǠȂßǍȘʶӰЄдHɻǥԦǦύӌkϫȨӉ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x98ʀıȯԂч¹ѦÑɀԮǌϸƯԮԮʪųǯŏƠɷŦˠƙȊ˰ұΑϝ',
                                                                            '϶ķҹ˻ÁũԢǏVԧӁǭӨϪsҫ˗өɻ˖Ǜѩʗŵ\x90Ιɘŕͼş',
                                                                            'Ѿ0ɏu0ΈҲҒȀbŅ҃α(ΊɯĔΟÞИèϻɽŚȠė˛ǯǦč',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˸ȃsϳˡԖțȪǲŊ',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŘρʡϯҬȱ˩ȵиĵԑƕōjȥŒƝϸԡҫПтӍĻĔʨɖŊ˚ŧ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            316174.75225239183,
                                                                            241315.51588392165,
                                                                            343039.3719409876,
                                                                            647089.4024381968,
                                                                            108348.38486464525,
                                                                            314452.75430423766,
                                                                            711483.9859748255,
                                                                            561907.6459138442,
                                                                            632043.8764394132,
                                                                            179731.84674735373,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҈ͽƲА\x9fɣʖ9ăǟѣ¢ˉɯɜЬAɪɣęԐ\u038dʐ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:170215.461864:+0000',
                                                                            '20210302:170215.489283:+0000',
                                                                            '20210302:170215.517549:+0000',
                                                                            '20210302:170215.541063:+0000',
                                                                            '20210302:170215.565128:+0000',
                                                                            '20210302:170215.588522:+0000',
                                                                            '20210302:170215.612749:+0000',
                                                                            '20210302:170215.637262:+0000',
                                                                            '20210302:170215.661218:+0000',
                                                                            '20210302:170215.680513:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŷҥĵѷӟИǳȅƢΫ¯ɋ¼\x9e;×љɗ9ӨνԖ˖ȈˀҋÏ9ƹҎ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȽӈBĺȬӈŹƴΩԔïӧłʆԖт˄ʞǟ®ɄȗʲҥɐƬŰ>ʩ+',
                                                    },
                                    },
                            {
                                        'name': '\x80\u0382ʙəǉŽɴ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'оӾǳŪΒ}ӣΛûĉ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:170215.949293:+0000',
                                                                            '20210302:170215.969858:+0000',
                                                                            '20210302:170215.990842:+0000',
                                                                            '20210302:170216.011627:+0000',
                                                                            '20210302:170216.033991:+0000',
                                                                            '20210302:170216.055768:+0000',
                                                                            '20210302:170216.078883:+0000',
                                                                            '20210302:170216.099492:+0000',
                                                                            '20210302:170216.119975:+0000',
                                                                            '20210302:170216.141068:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΆĵϑԦѥȊӧËʑȳύƌΜ˦ː?Ɖžˍҿ¾8ȦîҸͽœM˽ԣ',
                    'message': 'ϥțԢэя˭ӪЕ¦ȇңТʂȘƧȅзÿǇˤǚ£ŏĄƯxª͵тÒ',
                    'arguments': [
                            {
                                        'name': 'ԉǫɀј͵Ѻʩɋн҅ʱƊȓˤҊԢƋҕøņǺȊǑŔӼϳ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3790268775634211522,
                                                                            2398684443789187288,
                                                                            -5517018762599846892,
                                                                            -4604476182876628680,
                                                                            3452263683021390573,
                                                                            2293240663714265557,
                                                                            -3172699515333029817,
                                                                            2931228425667170630,
                                                                            -524268526204824023,
                                                                            765100280922596650,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɝ˙ʮXΟҽÐ¹ԅҘǏʖӔųɥϾóƩЇ\xadϗɅΔͼԜȥʲŽтϚ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԘϹk°ʧȠѮ˔ǷҿĆЌԕ˦ʎԇΙʎÆRƎСЪ8Ģ҂Ʃȣ˾Ƽ',
                                                                            'ϜƆȨɲɟɾьЃTζþLЄƱÅτԌԧLЧΤųь³ϣeß-Ūϟ',
                                                                            '\x81пɝÝ ˬƼψ҈ҁƩά?ĮƺÀСѹǂIîҞӈ\u0383Ɗ)Ĉѹёԧ',
                                                                            'ðɤ\x91ÑXowйцʜ&¿зѥӴ\x98Źυ˜ʈ\x80ʶɤˎŨѥ\u038b˪ňʪ',
                                                                            'ѴԌğƀҎȁξҨΒÎԇ®ӞIъnŲĠөāǞŽϵłԮ7ӼԎȍ¯',
                                                                            '¸ƒίԇ\x81ӨÙҐȵˍÁί8\x94ķϒҺ˘ȕxԐÛȷн\u0378ǫΧ¨ǽŦ',
                                                                            'Ȭĥ¢ìγЂǚǱҷʃ\x89˒ԧȔŉѢʈѦɖŔ÷Ǌ\u038bŖɴ½˒дǄņ',
                                                                            'ʭŐƟ÷ˣåӅҮ&һěɰӀӎTƞ˖ΡÙ»ȋДΞɮĥͷŦιǆҽ',
                                                                            '\x9bːԙѐȂMȘXќåьZҺ\\Zŏӧ˒ųˡûɘǍȧҸǓȃӤmr',
                                                                            'ɂŹĈˮťԞ/ˍďΎΆоȮŠơ˂ԢŔ=ҫǽǈαΉҩ;ƪ\x95ҴЬ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƛǘƘ¯',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 887322.6996530066,
                                                    },
                                    },
                            {
                                        'name': 'ίʘ^ΓНЂş˽',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            766501.353400326,
                                                                            911882.1670388316,
                                                                            24236.548163881496,
                                                                            380233.10762321594,
                                                                            851347.8860898912,
                                                                            552657.0241114028,
                                                                            427280.1623807484,
                                                                            683261.927963359,
                                                                            128423.9313408611,
                                                                            275007.95904400473,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԯм·ċ#˫ԅҦ҄ƺƘʢš˩ɳ\x9eйӸЭȨíĂɥeϚϨ±Ҙɳ·',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϏÿƣƦӷǕ|ѵίΞʳԓˋǵç¿ˏ|ȵԣȕȘҫτϺďĚβŁú',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            438399.58502456837,
                                                                            4388.890068873501,
                                                                            114345.08352178201,
                                                                            875012.7109079538,
                                                                            584855.172319782,
                                                                            77354.18319698732,
                                                                            567482.570301937,
                                                                            202660.18470585672,
                                                                            984809.8261298542,
                                                                            919496.1453490781,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΐҡȱ[ʃӇŒ˱ϴōnѱĬѓǂʫζŧѦҸȍɪù;ϸԥƹ Ыϧ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:170217.813128:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÜǼѢѲŸǢӈƈс\x99«\x7fŋҶϖЪϜǺ¨ӒҐϼԋˌΔ½ȹΘӼǳ',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȦԟҭȌȖė˔ҔƘӣĜ\x99ƪгӬ\x9b˕Л҅ëũ˕ˡȍȟΥǛӂ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 259081.28115182323,
                                                    },
                                    },
                            {
                                        'name': 'єÁƲξψӍŗ˩ԤҙÓȲŷȚɯʹx˳ʎӃļǫюɿӀǅͷΫ\u038bҧ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǳĐƹļЋϗАǿϠǵϪ˒ǀЃjϦʲƆӧ\x8a>˔ԀΌ\x8bӯȈɠǇϝ',
                                                                            '\\ɬǍɪΚ\x86ϰгʇÆɃĒ¼ɫɒŨрʷĠπɦ˻Ԃ\x8d\x80Έʆ:ķƻ',
                                                                            'ԨѕӭӶʐҾҁɼθЋ¹ť˶˔ǮӂϹΆȽҏ˺eƚǍŕȋϐƅѓÒ',
                                                                            'ÔıɇMҢ}áÛΆĠȾϨҶѰnƜѸIѽΕňźǛ˝\x97«ͳӡŷӃ',
                                                                            'Ѩ^ҐLĉµɋ¹ԃЌӹƌѩAМԓ\u0383ÅWvɑsɒӽȘˇБìϋB',
                                                                            'ƀ˃Ͳ˲ɫ҈ɣЈçīνMɏΚǫǒѯʘȵΠŝōʠǼǎMҀ*8Ǖ',
                                                                            'ȐҜźҒ;«ðԂѕbь\x92ѻԝƵŝӆȜÑÉśæәǸΪͲ˃˴Țө',
                                                                            '-ʠRқ7ФƑӏĄțхҘȎã®-ӌƪƨǔӢ)ћ0\x84£ʭЍʭˣ',
                                                                            'ΡƬґ©"ǛĦŴҡʯluƫͺЂӂĲ˚ŕѤãӐźΌȖĮЎǵưȗ',
                                                                            'Ğ\x8bǆĠѽǨШЁ\u0379ĴɚԈѩӄǀƌϒȎŹ\u03a2ι˩ȝχÉə҇ԩλÿ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '"ɄʸϴcρʹĒβхϋŧ˾-Ȫ˅ѢŁˍ˵бȫӰȿďŒӕ˦ʼĠ',
                    'message': 'ŞɓӮ&Ù»ƃˢˢѿёŕ2%ÁȨҾ˖ȺίóƶˎШӻòЖӎЧЂ',
                    'arguments': [
                            {
                                        'name': 'ҌČϹɩΕЯ\u0380ЩƶȿǑѪăƝʞԨĹɤŐɴ:Gŀ§Ȃ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǖmϦϩ`ˍЗǀÌ\x85\x92ԣԑŉӿˌ˷\x971åѴūϔ(Əπņԑжʈ',
                                                    },
                                    },
                            {
                                        'name': 'ȪҵӹеGȀ©Ԡ¿îМêέƲˬ˲ƈ³ƏȲʎ}ʮЗЀƣҊЏ˄ζ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 541312.4692950745,
                                                    },
                                    },
                            {
                                        'name': '\x9fКϜΎøKÄͱʛΩ,{ǥҽíʩͰВɃ\x90ĬʷԒ$ϩ·Ήʬ|қ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӕŮ\x83Ǜ˒ǔĲ\x7fӉơƞÑ˕ѕ~ԉƨМҌͶ҇(ȔčĻūĞЇȨł',
                                                    },
                                    },
                            {
                                        'name': 'Кѡˡȓļ\x88ΦɁƅZҸ˂ʝĘϴ҂Ȉɦƻsɨ\x82ʳŁ˯ŅӃŦȸś',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            92173729823138686,
                                                                            -3044875485191852257,
                                                                            9110203992275354317,
                                                                            -1497462957151925830,
                                                                            -4493457469181298968,
                                                                            5213213104141814316,
                                                                            -5551014252448074109,
                                                                            684619647450734616,
                                                                            -5790654712039206742,
                                                                            2199095876320490378,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɮщΊ´ϓƼΈǞΰɺˎĤðϏôńа˦ǐȉԗɳӜ˪ˣ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:170219.146328:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʃǿǟįƋƼcˁԚéў\u0383žǁΰĆЦ²ƇÍǍǅљϟʋҍĔҙǩԉ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:170219.234623:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѬΧˣȑ"νŖϞҠЩ˝ũҳϿίˡ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:170219.321243:+0000',
                                                                            '20210302:170219.343162:+0000',
                                                                            '20210302:170219.367724:+0000',
                                                                            '20210302:170219.390633:+0000',
                                                                            '20210302:170219.414349:+0000',
                                                                            '20210302:170219.445620:+0000',
                                                                            '20210302:170219.476584:+0000',
                                                                            '20210302:170219.507133:+0000',
                                                                            '20210302:170219.538236:+0000',
                                                                            '20210302:170219.567687:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʣƽŐͿĎŏ;ɎƨRɘɡ˖ԡ˗ϋ»ȎтэԮƄѱГϣԧƒ˾ӄϨ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ƚ+ĴөÒƴČɴȚɶ˩ŶÆȄAXэŶɎԂˡǼӮƦ\x85?Ũŗ˽ϊ',
                                                                            'лɲзʈTú˺ƂӜɞЁˋ\x8fɵӬȟƃԛɲǣĎǟƤőʂʥʗҴɋр',
                                                                            'вUԜϥωʤ|їƦӅ%ȺiŖȸɆӔʾӿəӃҢĮƔəƖȱԕǕ\x97',
                                                                            'ϊƦʋ¦фéԭʖиĤ³ģυԇɸϋŊ\x8dΥ(Ⱥ·ЫŊČĉ§ŅǈΒ',
                                                                            '˼\u0378ԓǫƋǪԛ!ʗĀǵϱБͰџɤĘӧфɠ¬ɭϝӰԑʺѐ˅ʀё',
                                                                            'Ϝúˇk˚4Ӑ9Ҿǳĵ\x8a\x8bÁ˘тFǩÈҕҝΑpĞͳԆһbώM',
                                                                            'œҫÄъ&^ʷ~ü˛бĒˎķԠŘǳȶȴ%ˈ£ʋ¦ҳ˹.ɩ΄κ',
                                                                            'фӫҟɭh\x85оκƴЀˮіĮҾȸğʨϤӱë¸ԫΏſӺdΛϬűĐ',
                                                                            'ˠí\x81\x955đѵȐñƷʔʼǦПӕˢѰԉңʪɮɦƌƓƯϹΪ\x9dЮӣ',
                                                                            'ӠϩͿ®ѤÍѬͺΊęʃԙbчӘǑŜԠǖˀь#ϬĮξЪƀƹʒʞ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0383ЀųˏŦǦӤΝʽ¼ɲÓϒ[ӔӞ\x85ņϴѯµȢƒӾĠŒµМùȖ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3889818123290718023,
                                                    },
                                    },
                            {
                                        'name': 'ˮēȆͱʊϔѢȁVĈð\x7fχ΅ь',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x83ǟϮΣӅ\x9bǬä ĄŮƷԨNӧǈУ\u03a2åϔƍɢpɷ˶΅ɕѧԄΙ',
                                                                            'ƺҐ˶ϓĀ\x94eçԠƌϠυЀΡΨȭъɣATĩȥôɳˊŦ?ºƎӣ',
                                                                            'ŴΣӛлΩΪȱɕ\x94ʞѷŹѱϳҌσԏȪϼÌȅǧɆҠάҬǑµαП',
                                                                            'ȎDΥŎļԙ˘ϻśįҁĎʬɏˋƔԂ´ƓɉǶΖѽȽϠ҆Ĭћѝȏ',
                                                                            'ȢʥňѺϜӶ8ӌϟҁþѭɖІνς˂ýûϹ;ҩϼӸɒ҇ϫԉĈō',
                                                                            'ΩX˨ôĎǶ˦ɔ\xa0ӡԗʙǗƥǈķ_πЌδǚȻ¨ˁ\x8fȑѫȁ\xadˎ',
                                                                            'ԁ˦ɟHÄ\x85JʛӴŕҽӮͰљӝųМūȽ\x9bwēŦīӎӅГѼǤǷ',
                                                                            'ЫɽÁѝʘβ#Šӂ2ƈͶiĻҁÒΉ¢ȻȆőćůϥŢɰˣÜɫȳ',
                                                                            'ǁȼ&ö\x92żЊʈɳϕǳŅҭҥϓĭȦŭԧnҨҽϸӅȕȊӇˌԤĵ',
                                                                            "ŌŬȝ˨ɓΊϭ˂ΩɇѺˈrѧʾʪ҇ȵиÈƹЊ'ĻιiҤ˻Ⱥν",
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
                    'catalog': 'ӣ^',
                    'message': 'ɳ',
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
            'identifier': 'ȤϼԀЖʬ\x9a˥ǃȼĨŦҰƌɀǞʜY0ЀҟыŷÖҪÿīёԐE_',
            'categories': [
                'network',
                'access-restriction',
                'access-restriction',
                'os',
                'file',
                'access-restriction',
                'network',
                'configuration',
                'internal',
                'file',
            ],
            'source': 'ČȘ\\ΓŤɁĀɊɰİȮʖьҢ¼ҎΜаԕƳсғˑяЗ˵ǙɗȊÎ',
            'messages': [
                {
                    'catalog': 'ĺŕoIǅϾşƨĮŒWȼКúЙӼöҬņȼΙӧEƞˉŚ¿Ќ0ˣ',
                    'message': 'ɢԋʴԥϹƧɋEʣϾвĠƠз˭в͵ҙkĖϛʭУȼʟȯ-ɚύ˝',
                    'arguments': [
                            {
                                        'name': 'ѣAӹϑBɐ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2695399917487863550,
                                                                            -2324629170448517140,
                                                                            5123610031209909583,
                                                                            -2285970422586797722,
                                                                            371751296426769220,
                                                                            8156341547646933475,
                                                                            -5782358242172537553,
                                                                            -2393206141809296187,
                                                                            8508341290012721088,
                                                                            818719238687671631,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ǦŘЍГЗ˾ιʾ\u0382ǉĎЬԙѽĀλϊʅįӛМǄме'ˬϞȝѨå",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3247262318604540002,
                                                                            6996521584760358376,
                                                                            -2764138979890944557,
                                                                            8339338352053257309,
                                                                            7027598016695771386,
                                                                            2026973245158565073,
                                                                            -3039645799045926721,
                                                                            -1758794608669807763,
                                                                            -6700226821971588111,
                                                                            5146076803498624469,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʡƆԂӏȅШùďƟūѦÈŘΘГȥԞɷ:ļϹϮƝҲʯхȨӐǛʒ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8221101728297043845,
                                                    },
                                    },
                            {
                                        'name': 'ʾɫ',
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
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѽũ˜ŽӐĝɃ˭WɆģɌ`ҚȝĶȅĥӒˤиkԆˊƒʑ҆˓ȷÕ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 195882.0502168935,
                                                    },
                                    },
                            {
                                        'name': 'ȷhčƘȂԊaŨ©ɝ\x84ŧµЏʰʃзƅÀ˝Ԃӫĝ¤ƺςϑӜϳĐ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˴ѶLˋƔчκɾЧˠӻς·ǥʧĘӂԋ˷ǔȵȹԣZϸΦʾːРɖ',
                                                                            'ɇ·ʙŤ5ʪӚʰΦKήӲǳўѹǁЕŝƜơzʥ\x88ŌңͼĈˈƗʽ',
                                                                            '˸҉tˇǯǓãυҞʕԎӾш\x94є\u0380ʫŤȺЀ3ȁǟİϴŎˮԂàȓ',
                                                                            'Ԓ˔ОД_ϱǳѸЬ¾оҚϨÐͻϑ}ǡмôԐȟhσƉ\x9eнşѾ!',
                                                                            'ÐɮĀÔǽĕĞĤ\x95ÕŐʼŪǦʺɂԡѮȼкЛ˩öӖϜzǟσˀ\x96',
                                                                            'õȉqĞ\u038bг,Ò˺Ӻĉ±ýӯƍӥȔY°ĒȒ1Ӕ\x8bҗĝƼϜ\x98Ū',
                                                                            'Ԑʗ%ŽĺӝҴǅ\u03a2ƾŔҞǰΦӦӂļЪКˑ΄ʙƤbҸ˒ƄхƪA',
                                                                            'ǃ~ǖ˰^ɶфЮ§ʹ\x7fӣͱƍȥϬ\x7fƛĤγƌǭ÷ĕѼqѱʜŎҁ',
                                                                            '˒[мĠ;ɝͱRZǢʶΉҙÜ¿үȏЀ(ΨсˏƆΉ¿',
                                                                            '×ӓɻ9ʕїятȍAŪćϐP˹ңжҬǔʩβʽΜȯ~Ӷ˷Ɖ3Ϻ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '΅ʬʢϫZ¹)ņΦȹρ˭ҺºοķлдӘɬҏѓ\\ʁϳӣѲŗ\u0381Ϛ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            805563.2274393731,
                                                                            112762.97793089211,
                                                                            647941.387720081,
                                                                            -9746.090918169022,
                                                                            377318.7108206055,
                                                                            756721.9772363598,
                                                                            137902.70400428367,
                                                                            594448.0077611041,
                                                                            268903.54657096486,
                                                                            183241.95483107353,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǹΚț',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʿƳǿĂɈԈ"˨\x81ŤeЍψ\x85҄¢\u0380ˉĢţҕзϐɐЖԧ\x8aԀˊǌ',
                                                    },
                                    },
                            {
                                        'name': '(ЭŲф^ϕǾӋϞӱÇĨÏϛípӧάεˣѱêʖď\x87*ͶϼŦʚ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6001990039812496333,
                                                                            -8523762240339217741,
                                                                            -3780259416261516993,
                                                                            -6574089568036575732,
                                                                            8144596533866864642,
                                                                            3174066677983575088,
                                                                            -9122843033366479363,
                                                                            -7047208014094351456,
                                                                            8784966174198713661,
                                                                            -797235388863426281,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϏˑĄʺƧʯЇӖǆɈĻӪ˾Ŵ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:170237.263433:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ғȵҒ-ɕǴрǙӳ/БƃΊɹԙҊ҈ŮǗɩ',
                    'message': 'őͺӨLҌŮɒʊжɣÈԉͿ˟уγв\u03a2ϖƏĩɕƄʗѭȦ:±\x84Ƴ',
                    'arguments': [
                            {
                                        'name': 'ϸÈʮҎʬƀΏćȄҾɓҍǣӞ\x9bɓ\x85ʯ«ŽđǇ϶˛ÐψǲԈß\\',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2736589150167232327,
                                                    },
                                    },
                            {
                                        'name': 'ԠɔƐ\u0381їɺʆӒӻĵЦkÐγѐϑ\x8ba\u0383˃Jѵǵɩ\x8fӂŉӧʨɐ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѤʗɥӆқҮłǈĎдΔɻЕĆĲ\u0383ϼåęɎηχƠ˵z]ƌ˄ҡҁ',
                                                                            'ĹƠѪΨŞƜȲɼȞˏȂУ\x98ūӨƵſш\u0378Ǆ5ŉrӚoоԔӢɑґ',
                                                                            'ʈӮӪѢъͳҫ|αŶÔў×ŃхѣеҐѻҁœτʰęҗÝ\x9dҍƯP',
                                                                            'ѴϷΦ\x9dŷЦƶŧȰ˱Nҳǵɵ\x82Ч\x83ɮ˦9˔ʃЄĜǴŴǩ\u0378ȷŞ',
                                                                            'ːÝůФ\x9b\\˖ȌƚƕŊӷΣџ^ŶʤǶԖϞÅӈȖԚһѯ¶͵˅ѱ',
                                                                            '¢ĬϬ҈ЎǦōΜŎƎѼȏͷåȾÑș҂ΊñɥǩσӤӒҿ=ӴҸģ',
                                                                            'ȆSȨăǵʶʦЅēԩƻ҂,Ъmǧŵҽǐʾ/ӊΥϝɴ$ψҎΣʼ',
                                                                            'ʤɮ˭ԬÏôϔӮúBÃӰ\u03a2СXƆęnӞŕŞԗśɢӻ˝ȄЬӳĜ',
                                                                            '˦ωϐ˧\xad˔Ҿѡƌǈ˜αЦУ»ňʘўыҳςͼʹǰҗԏĬƎʎǕ',
                                                                            'ШǆѲ҆ăƓ҅rˤȭφ˟ʙӛМΖʛҮз˺˅Ū»Ǌ\u0381ϋˋвüz',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '8бɏ4XʪΛ9ŕХ\u038bоѴΓɥƓѰ\xadǰѧń+ˏĘˤƦÃĿǥы',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:170237.893963:+0000',
                                                                            '20210302:170237.919215:+0000',
                                                                            '20210302:170237.944093:+0000',
                                                                            '20210302:170237.969043:+0000',
                                                                            '20210302:170237.994117:+0000',
                                                                            '20210302:170238.015572:+0000',
                                                                            '20210302:170238.036465:+0000',
                                                                            '20210302:170238.057417:+0000',
                                                                            '20210302:170238.077288:+0000',
                                                                            '20210302:170238.095861:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǉŐӉIӍÊÂ\u03a20ɞԭίѴʀӹÈÐĲϒӸʾӷÒʸѩгȰоēН',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'șǻ%ʛ\x9aʿdOʭƢ\xadŮčϏяʔ˅ɳўȡȑӳʃμy_яʉ˜',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1719868548086509472,
                                                                            7033007228760478259,
                                                                            -8808702827918620530,
                                                                            -4943800419121430822,
                                                                            7751597738168790272,
                                                                            6026392712428790687,
                                                                            9147422823766815764,
                                                                            -1978119033233297295,
                                                                            4272714357178132717,
                                                                            -870116958355610822,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӤǁEӕKХǲµz˟˹¾ǐŘ\x83ЁƴΖãԈ˯ȏƭϴǈÚϸ',
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˔ϠɮĻ/Ўƀ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5535767773217305295,
                                                                            -2151131492011321872,
                                                                            8736263838004932032,
                                                                            -589697624764884036,
                                                                            -7201074457797015196,
                                                                            6571314582262772254,
                                                                            286854997754441329,
                                                                            5677736585971409608,
                                                                            -1962527075801224890,
                                                                            7983613170574894078,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŜǒƖÏѬº˝ϭŶÄ¢ɺȼŹϽŋȹĀʨԥǿϴͱѳ˞ϸĆĎӹ¦',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:170239.164376:+0000',
                                                                            '20210302:170239.188085:+0000',
                                                                            '20210302:170239.208233:+0000',
                                                                            '20210302:170239.227418:+0000',
                                                                            '20210302:170239.247071:+0000',
                                                                            '20210302:170239.268275:+0000',
                                                                            '20210302:170239.290650:+0000',
                                                                            '20210302:170239.315592:+0000',
                                                                            '20210302:170239.344168:+0000',
                                                                            '20210302:170239.372726:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƚѫYРѩ˰ԢʤÈɤŮʲԥĸ\x9bɧȵDҕIσɬȍԥҧѤӨҍǮҚ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 363450061616314222,
                                                    },
                                    },
                            {
                                        'name': 'ˮҜøĿЩѝΌČҺ#ɤjβϊōΧƨӃ×˷ϩɱĔĲ˰ΌðΊɷƧ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҞңčjϜĐ§ƮϢЧTȟƵ4ćГƍӍ(]ãҶӊ¿Ť«ǷҐ\x82Α',
                                                                            "Ь'ԋҽэ҇ɄѢΜȔԒ˜ȐńNԪěćΊԗԪȝɰê͵ѩƮƏТ\u038d",
                                                                            'ΛˡƯ\x86гϬĢɎԌțҴƈЙÏѠҡόӽʾʲȋΦĄҗ£Ѿзňʇζ',
                                                                            'ƸǅӽǕƩӑrːʕȥБµΥÆŔĿҐŢÆΠ\x99ӖpʆɾӬ3ŚĭȒ',
                                                                            'ӦɈӶȧȒƪâ\x8eΓ\\ΠħсˈȗĈ˨Ϲ\x98˸:ЂӢҕÁÖEΜˎͺ',
                                                                            'ȵϒβѣͿʬ\x83ģʖƴыˠ˹F\x8cĚŐßȶӋɋТˢϼ˨ҭ˰ȬӴν',
                                                                            'ҘӳȁȦnϟɞһ\x83ȕ˭ъ5Ӝ¶ɷԀΗʧ¼ǵñԑѪə˗ȃίÐΥ',
                                                                            'ϒԮ«ǚ!Ԡʧґ҅Ƌřўș«ȉµϝн˨ġwΗ˵èӅǏ˞£ȩǳ',
                                                                            '˲ȜƭmҁTαϓė\x7fӨЛƕɲŤɘ\\n\x86ѽОʈƆò6ǔ?Ŏҵ˘',
                                                                            '˷Ëȗ5АƫřķĆɛȀΠʗϳʊǐÁqΥʪǰ9ѐʠƲԛËϵȹ\x95',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '©w´Ўò\x94ѯɿҒы)θˋŞЌʊ#\x99ʁƍĉίԌӯý\x7fȚȀ\x93ѝ',
                    'message': 'V4ĕÀŁ˽ӔėɢŰɭȒŨȈ\x8cҦϩŜ¼ʎjӞđƤԕȷ\u0378µӐψ',
                    'arguments': [
                            {
                                        'name': 'ӽϽƋжʞѼөϐǥŢĴ˖ʻөЇԇÊ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'έ˽ÎSΫόδsmТȥȾΤʛ\x94σϠ¯ΊШƆϏȤӕӅʧΫɚ^Ǔ',
                                                    },
                                    },
                            {
                                        'name': 'C˔\x85ԮĹ<áɕ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5937829026427717947,
                                                    },
                                    },
                            {
                                        'name': 'ŕ²ϰF˚ьʅǶÎʱѦˣѴɮp',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5246672877619590299,
                                                    },
                                    },
                            {
                                        'name': 'OǎŅʡӲǾſδљ˛Ƌ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:170240.425344:+0000',
                                                                            '20210302:170240.446178:+0000',
                                                                            '20210302:170240.466125:+0000',
                                                                            '20210302:170240.488617:+0000',
                                                                            '20210302:170240.511053:+0000',
                                                                            '20210302:170240.530811:+0000',
                                                                            '20210302:170240.550191:+0000',
                                                                            '20210302:170240.572084:+0000',
                                                                            '20210302:170240.591699:+0000',
                                                                            '20210302:170240.612785:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҰŎǪ\x8fƻǇȭǳŚʾĭΔˏΔʼϠΣӂΥɧńǎҜȊĘȠӬĽŢx',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 134095.2131719722,
                                                    },
                                    },
                            {
                                        'name': 'ŖťʢȁҼɃϘšāΏӌҫӯјŀÁɿ´ɡѫēΨ҈ƶǢ¼\x8fІҾԞ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:170240.824948:+0000',
                                                                            '20210302:170240.849821:+0000',
                                                                            '20210302:170240.873919:+0000',
                                                                            '20210302:170240.898480:+0000',
                                                                            '20210302:170240.921676:+0000',
                                                                            '20210302:170240.945647:+0000',
                                                                            '20210302:170240.968827:+0000',
                                                                            '20210302:170240.991976:+0000',
                                                                            '20210302:170241.014706:+0000',
                                                                            '20210302:170241.039196:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȯϻԚŜҫʏöҖ\u0382ɷƻѓȇ"Ŭѱµ=Ӛrρ)ѩǡ\x9dĞУAяÃ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            598885.7115576016,
                                                                            130133.18959544663,
                                                                            840235.2791102624,
                                                                            172839.69980965432,
                                                                            94578.4609452165,
                                                                            280718.3102099397,
                                                                            121744.97768545189,
                                                                            912694.1182512465,
                                                                            587020.2987547553,
                                                                            490303.8862126875,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¯ӜІҐPȔϓĽȌ½ίӠĄέǫŏɈȽӊúӟȼĦŲŵŴш3ӆϞ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'šÄZĊЅǰĘɔµÄ¡ȩЂшËƱӒ˶аǕȎˆʾӈρˠХƑE\x8e',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2603138449923367458,
                                                    },
                                    },
                            {
                                        'name': 'ϟӨΗω',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8604640572254164146,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԞŤ\x9eċѵɮӃ>ԆўОƗǆȥɓƣIϚźЙѡόαSǴŎǥ÷òҁ',
                    'message': 'ʊ˦û\x83Ã9ļʊxϝʍѩϊý\x8e˰ѧLȬǥƲǻ\u0383N¼ʾ˭ԁӉȲ',
                    'arguments': [
                            {
                                        'name': 'Ȟŉ',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʢɗ˵ǨƘƩÍŮƅӰ˟\x95ЎЀ\x86śę˲',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            520566.8293569132,
                                                                            924251.6709135353,
                                                                            -2543.68071727833,
                                                                            538336.1518590377,
                                                                            475026.0150712797,
                                                                            377822.21805311897,
                                                                            217683.49733067479,
                                                                            610298.9643839097,
                                                                            416068.3792474267,
                                                                            557234.3418081348,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'б\x9cҲƯƿȊÎſʵȘČϘеÓʙȬɡ,˪ʈɱ±ɡ\u0381έIКҷǓɫ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8219303276284252767,
                                                                            -7244660240007482318,
                                                                            2093004007123924297,
                                                                            8895851079356542632,
                                                                            3270162358296340799,
                                                                            -3078687714460563448,
                                                                            -2685334800135711800,
                                                                            -8843341737122251175,
                                                                            -8634398001090790613,
                                                                            -5777207960098381434,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'éĔɼɂfΧ§ƄǩБȴǧ\x84\x83ŲɳǂθƩѯŐ\x8eý9ΖҰϑȺǕҠ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɶʈΈǌφԤɃЅԜʢӒʻΗҥȳűћήΦ˗ƦǆӮ.ѕ\x9fϣǵɣϭ',
                                                    },
                                    },
                            {
                                        'name': 'ѭåǱˆѲŹsůȑčǰʭίѹľǁÅǀķӁʷıǙȧÝCυƄφ˲',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 795978.50876072,
                                                    },
                                    },
                            {
                                        'name': 'ҾŖêӷȆħɱʽʔȮɃʌŗ^ъĉΔǏй˲ʺ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -35582.5504666344,
                                                                            780178.6948177109,
                                                                            178135.42633683112,
                                                                            601945.7667277955,
                                                                            516094.7824640643,
                                                                            14885.712959429045,
                                                                            551117.5941263456,
                                                                            214519.36715103342,
                                                                            749028.8287177503,
                                                                            684678.2414058694,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɍѭʹŵƞŐƩȸɢӹт"ʽÐźƨ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            816089.0116804177,
                                                                            -57451.07567269973,
                                                                            94385.38073708987,
                                                                            964939.8639831159,
                                                                            808020.9796587183,
                                                                            -50094.006824218006,
                                                                            51712.74649805232,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʅΌӱƈǞņԚŇϹӼԎШϰƗ`ăķԈɸƙƠΤ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 96896.25285949442,
                                                    },
                                    },
                            {
                                        'name': 'Ѡǣ´ɟ2ԚŴĘÂʸЬѧǋ\u03a2ȄʫʩӰРї˧џę-ӇʱÉ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʚHðҭ\x8fõγƌΞҍνƞȕĐȜ4ǎƹȷ˴ѪøÌϬȺҮǰǾҤЦ',
                                                                            'ҭúąʧHғԨłϣҌɸǷˡ˅\x8fщЬǷќĘ÷ȓЭϘЫŗȂщϖѳ',
                                                                            'ɴΉΥyϭǦgι˂ʯǗʹŚɺ¶N˨ϱnҕшÁĤ˩,˭ͼǪҫ˝',
                                                                            'ʛ҃ӵƓÄʻӻ¬ˈϣVˋΝȨƊҝЇфǽ÷Ђԭ˹Ԛ˟Ҩȋ¼˜ž',
                                                                            '\x86ϖԒʿƬƑҝ\x8cӇȡƉŭʴʬƴʝÁƮɖàȤȲɹѐůǁĩӵѓҦ',
                                                                            'śxԂΐѸʹмёǩƇÝʇŉȊV\x93Ƌ\xa0ǍԖПȑƩҞĿÁeǔҜU',
                                                                            'ƧˏÉѺĤʨʎϫçǯøȵԅӟàơӰӶł/\x9b\x95ÍӊȇѮӖҏ\x96х',
                                                                            'ȿӉƛЂў½˄ΏǞ&ѥҢşȶ0ʁĐǶþ¥ņSһ\x87ͲƊҟʢÞī',
                                                                            'ЛɫĠМ҃ӲɦԖgʽґĘȎϪuɆʙʠʈˈʜ\x8aγoŶʶŗ9Еϡ',
                                                                            '3\x92њ\x8bh\x99;ҔϾĺÞʁӽƑҘˮ=ÙǫǂĈǆӼÒѹM8Ӿ\x89®',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԘѶ˟ӂʸǯđĲ¹&Г˄ʎ˚ƀԕăы´Њ\x9dϳϰʕǝ¯Ԭˉѱǋ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 116395.77191014763,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǤӫĦǮчΟʻƶԤԍĪǕǞɧ+ӖǠϳӤØǠԞ҉ĭĐʑҐ҂˂ȧ',
                    'message': 'ĩљ\u0380ҧвΈɂΖRǤýŎƘϊ\xa0ĒɝȭȄӜVˇҊҟΙҍіłԎΎ',
                    'arguments': [
                            {
                                        'name': 'Ӓҡǲ\u0381ʣȩȶђNʍɲÃʌĞҳϦӢ\u0380ʖ!ĒȰèØưƘоӕʽң',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:170243.994970:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ļӾɄɁPЌƙ³ŮӎÐЂӥñɘқżɑҁ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2495592815209412420,
                                                    },
                                    },
                            {
                                        'name': 'ư7ɉÔ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6466405858777203801,
                                                    },
                                    },
                            {
                                        'name': '8ʑΥϻü',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:170244.219946:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Пϙγĸґ9ѠĒǩω',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʛǏ˴ӏɰĈӅŐнҜǇͿИBʇԖ˵эɯţήЃɤǟҮԝӦԋРţ',
                                                                            'ǷŸчfĖďŇьďsŷӀēɭȄϙĖʎ˛œ҃òřɊͲēԊæѿß',
                                                                            'ωáƯԓ\\ϥǣ˄óҖƏτиΆѭºˢǍ˵щЯȑͳΧӥʇӾ\xa0ϙʀ',
                                                                            'ʟëʇôɹ`ʥІϦǖԊȅ>ԇyñΑҐĔԠǲĺêǕʔу˝ġÏ}',
                                                                            'Ɓϙ҅\x9eϿҐшvŦǞÃ÷ʌƀjũԟӪĦNǺȲ+ҴÏҥѤ\x98ʇԞ',
                                                                            'Μ҅¢ϑԔЎɡƕь\xa0ƆԚcŦоӻϵӈǜԪˁѪ˴˂ЍĊ%σӼз',
                                                                            '˾ǷɃΆјìȊX¾÷ɥÜИϑëɐ²ϪӘŔϣ ˆΟȾǳЭƸӠƜ',
                                                                            'Ѷ˖ͲӬϤԔˍÁťŬʧǭƲƴńІԌŨʓƩnϩƮƦ˹ɾˏȬ˙·',
                                                                            'ɍˁǡƌӚ˗ЍѭʴӻƿǞơѵ¤ŝʒ˙§ŽÈФƅЂиӊэĊŨѵ',
                                                                            'ϔШɋϛшżή¨ΡͿҴ˳\x84˓ūΎǄ]ˤƊχɭҒѝώҴ˭aƕÖ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '÷Ò҂ƗêʯлљʵϱğѕβŖԏǁȖɔԃÙͳʏȶɟÖѝɤRĥė',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2111624168192680538,
                                                                            2613831960431360074,
                                                                            7265645881526745364,
                                                                            1649239892962415685,
                                                                            5474938616692641050,
                                                                            4811236900843762538,
                                                                            3391075926455820385,
                                                                            -714085653810461864,
                                                                            8929046084876274957,
                                                                            5006579824345096493,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˞ТѩJǠ.ąӂө\u0381ɾťѲӎӝI˶ŏҧǦш',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7279254383434158987,
                                                    },
                                    },
                            {
                                        'name': 'ʱνʌˊǢԓѨӵwǟԗƴ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8110299589184197569,
                                                                            7900101656846984192,
                                                                            -4586571201472559627,
                                                                            7384580018295339179,
                                                                            8443082586969894839,
                                                                            -5672748488715306966,
                                                                            -4642752441008840490,
                                                                            5452017820592016070,
                                                                            -6974859625443270525,
                                                                            7597808078310423773,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÜƐԖ˱әβñ×ȁɈ\x88ǭЛǕ¤вƼ\u038bō:İʢԨʬƽWӢԡƁ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:170245.332479:+0000',
                                                                            '20210302:170245.352877:+0000',
                                                                            '20210302:170245.369747:+0000',
                                                                            '20210302:170245.386625:+0000',
                                                                            '20210302:170245.402839:+0000',
                                                                            '20210302:170245.418774:+0000',
                                                                            '20210302:170245.436292:+0000',
                                                                            '20210302:170245.451509:+0000',
                                                                            '20210302:170245.467258:+0000',
                                                                            '20210302:170245.483952:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԍ\x91Ф˟ôͽÚӬľҪƒҫǞИȒǋΞӹюɪÄĞâǴ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            767524.6998856751,
                                                                            419867.68128379865,
                                                                            413144.0428511604,
                                                                            508634.5777174403,
                                                                            -91123.04659222432,
                                                                            173995.56894918653,
                                                                            346827.62232939806,
                                                                            55080.78712033291,
                                                                            361862.5846254039,
                                                                            575818.537443424,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x92Ȓӑ˂?úęǀȘԅѺ\x97ƑΨĨŪԒѯ҈ƪԪδΒˊζíϕӞэÐ',
                    'message': 'hǥĭϑɴȵ˪Ҏ¥Ά͵ȦўϤǻ˨ƓVȒ7ƅņʪíʐǁKʶϷӒ',
                    'arguments': [
                            {
                                        'name': 'ÏƤȾŶʖяҫԁΜƔÌÍ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4305978816123178913,
                                                                            -5180832873633931898,
                                                                            -3548024627307578826,
                                                                            9142938657050851381,
                                                                            -6209707668194790297,
                                                                            -2112417593281468873,
                                                                            -5014381903649024289,
                                                                            8639781599716407999,
                                                                            8984689248017740205,
                                                                            -6016085927672590,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҮƝą/ŝҼЉԔ˺ҊʁĻ®Ɲƥ¾ɛƜԏЗƨχʰШĤѱчϞɫρ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:170246.318719:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˇѾΣ˽ӵΈs',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            957648.5012676397,
                                                                            84930.81705589785,
                                                                            580324.9765804928,
                                                                            948579.4398604541,
                                                                            -38319.48313154921,
                                                                            793111.6320268462,
                                                                            790910.7645927272,
                                                                            238832.91344292118,
                                                                            72088.18900521833,
                                                                            511401.8695893001,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѡ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:170246.779449:+0000',
                                                                            '20210302:170246.805567:+0000',
                                                                            '20210302:170246.827083:+0000',
                                                                            '20210302:170246.847130:+0000',
                                                                            '20210302:170246.867331:+0000',
                                                                            '20210302:170246.887067:+0000',
                                                                            '20210302:170246.906979:+0000',
                                                                            '20210302:170246.929541:+0000',
                                                                            '20210302:170246.958798:+0000',
                                                                            '20210302:170246.987324:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȵǮʫɺøœѾΐǡąӄΆ͵ÀƚВšΪ\x99č½ɠҍͳҕȚɅĊΌ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ҽˌЇԦѮĀøӨǹƃȾtЯʈә|ψϱƺгHɸȷîŮ҃ĈÝ˼Ы',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            210799.92497142922,
                                                                            390258.8759298861,
                                                                            328150.2142115325,
                                                                            788583.2788124956,
                                                                            567644.6053898092,
                                                                            891626.4996803703,
                                                                            263742.728734894,
                                                                            153189.72330745778,
                                                                            459341.2722878562,
                                                                            252830.94598198507,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӧθѵAēǿӔԙʹȤӆʉEҰϯёhTʛ˙ҞФԇςЄ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϚǚϔşчȲw\x8a',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': 'ѱɶˇϭąɄ3әƤԀʞǺÀTԈŶӇͺͲ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȉɬņ¤ʄԩѻ±ζəǉ=¼ɃȵǗ;ϏΟƘЦ˪\u0382g\x95ҟ˰Ιºυ',
                                                                            '·ЈÂfӪ¢СɫӡξϨ\x88\u0381ŷĠГѲԭɲύǵԎѾɰӟɳÐӎɳк',
                                                                            'ѹˎʉƗ\x92˥ƳȟҖӤҭΛ\x8bβϝĴѬü\u0379ӑȚԄɝғϬѠȨƅВŧ',
                                                                            'ĄȼâȯƗĳǿʤλӪʋ!ŋӌϼɽʪ[Εņϩ¬ʂŦȇǃǤԭҏɓ',
                                                                            'өРʪ˜ŶѥʌʊҨϚͰƪȒӏĠ«ǝēѨĠӓǈϬϺȯ΅\x81ȶ|ҡ',
                                                                            '˟ȭɷªЂĠ{òҎ\x8frЩдωђãŌŦԝВЀɒȧȳӼӄɱǵҡŢ',
                                                                            'ҢҹԔ¸ϑ\x9fżƎŵɨϘrӽƊ˦ʎʵƥŏѕҗ\x95Ы\x8dξĄǫ&hӁ',
                                                                            'żѯШSųιúϋҁ¶\x90ɉϧƎ˵d2ɉжҞʤσ½bĕѕɑӅсʍ',
                                                                            'ΈҽϫѴѣϴΖѹҿ˹әӢȽɄѴVďǬͺԩаŦ˾ːǻËɇŸʕѽ',
                                                                            'ʮɓΘȏ҂²ɊȂ\x8eϮǪԅԘӉԜԡȎϝįЭѱҰlĔЍʘњӊȶԋ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʖĎĲԀӎ˾˪ȢɨȏǃŷȔЄѻCβ°ȪXbb5ʦԝԟԮČӶ£',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            818778.7192146055,
                                                                            322963.9288265328,
                                                                            307403.76610847085,
                                                                            759490.2546594123,
                                                                            459848.1808366276,
                                                                            639749.4931891306,
                                                                            260713.56412049994,
                                                                            149767.4431014426,
                                                                            135874.72675798216,
                                                                            632721.3212956401,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǫΈπόƊʈĬϘǵǨäǒʑѓǙʜǌɋи˳ɃŎƵĨɚӝɘɬȜȿ',
                    'message': 'Јɒ҆¹Ҳˉ2ʦ\x83ǮфpØқξϻҤΩ˟Tŧ˪ƽҼˁ\xadƀɨ˞Ē',
                    'arguments': [
                            {
                                        'name': 'ϙ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3480458977778049847,
                                                    },
                                    },
                            {
                                        'name': 'Ƴϡŵˣϱ˱ŁѣʘʮҲ\x92ԆԀɄҠΜԂřĢϦŭηŃ\u0378ΣbԀˆө',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'qӸˆЯԢ\x9dԌôΉġĺД˃ɜǇΘ˷ĲúϼÙȜȷǋƱΐͼ¯sˈ',
                                                                            'Šїӣ71ĒįзϺ\u0383ûϓÔƥƎʛΠŔëӿƞҁЂʂԄґю˜ľѰ',
                                                                            'ưΑҰ!лӌȼ˛ɘͺςȍ˷iԇ1ҫˋ΅ǇJϠϫҰˈȷɏ˜ÛĖ',
                                                                            'ĩѪ҂ƑşηђĘϛӽ\u0378ˑңȘāбͷͲſHЪɏŧµʅ¿ϚȾŵѲ',
                                                                            'а+Ӿƨϻьɇǟòҳμ×δĽ\x9dӽˣФʻ˴ɵƗΉӆӝĂӚ\u0380ԐǕ',
                                                                            '\x99ù6ŉƳǻ¬ŃӘΦˈ[˜\x94аξ<ҾO\u0382mӾа;ȚįϬǦνɪ',
                                                                            '˧ɩ¼ɿφΙĻƤ(7ƸňZ\x84Å¡Ǡ\x8dӚчsψˈųŲƻԚћĺc',
                                                                            "ǍǳǇ'͵ϏΎӜӝπОǝʭҋкԂѳǜşũ\x9eЈ\x8bӓ¬Ɨʪνƪѫ",
                                                                            'ˮɺϙĆҺřȬΜƐх˓ϝūƴ\u0382ãϝ*ѷʸ˄ēǉɁĔĳηιϡҨ',
                                                                            'уsЭňpЭÄФɳʐʥ&ΔԦнͼȺ˶ƺ×ǂʹа˃ԔӼǙʱβo',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɬÎşӱ¨ӐȷωƇҹ²ԆŴí!ϖʛȣ-ˍ\u038dɕҹįӚɟСʂżɟ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7496938850628127160,
                                                                            -3908522600491871640,
                                                                            -8134805733348564518,
                                                                            -8193872517994041375,
                                                                            3263547736254755542,
                                                                            4662605463476516266,
                                                                            7556222402391512374,
                                                                            -283393590078206384,
                                                                            6696707773045163684,
                                                                            -3811730126366776140,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҸdǬѬ³\xa0Џ°ѠʡӔрЫȥзǓԇ5əҶʍĢʤŉ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "Μ½'ÔɇGеϢɒȔűʧȈˈƓУƴҰǗQѧѠϘʓΖΠǋƑΥɌ",
                                                                            'wƱΙ҉ƪ\xa0÷åAɰ˽ԃӏʏƁÎŦԩÌǢ5ҋԥʨǜ\x9aӠ<|ѥ',
                                                                            'ȗöȑ/ӂìąʑʚǾҊǣasҵρё\x9cÅƟêǱƸҰƆǛ´Ȗӷω',
                                                                            'ĦăǱХĚƯɤӉӦȬZȚ˺ÿѵ¬tŝЁԐqőκēȮұ>ˉҒȹ',
                                                                            'ǂёIĥуbȦʽˑУЈǍҹːбbÉΣ˟Ǡ˜ȴĳÏƖԍοϧĐѽ',
                                                                            'ζȝЫβŮȵϢȷҟѲȩ˫ЅѼBТӢɒιӏԬ˚Ό҅˒ŽƻЅЃѠ',
                                                                            'ŋͷҕ°˧ҶӐԋDʑѲĻĢΒҽĤӳƇǳĔӆǎÍі«ģѠ\x87ԦӴ',
                                                                            'ʶǥʀСȖǫεËΤӟːÊ&(ωƵǂЋĥȧɊȇҍ]ӈʻɿҐңĲ',
                                                                            'җηȼψȌǡ\x9e#Ǚĵ«\x83ҭҌÿԨρȿɴөԞÁĐҧҫʅͰo\x9bʎ',
                                                                            'ϸǦ\x8b_еǂѿĒΞǷ˽ʑ\u03a2Ǧǔɵɐ\x8cpˆæЅҜȋǂƵʽ@ѱŁ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȗ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            524754.0340307314,
                                                                            851476.1446862062,
                                                                            779181.2167773312,
                                                                            683069.1264226212,
                                                                            -32487.9497688213,
                                                                            567372.6081731954,
                                                                            63834.52812780507,
                                                                            568732.5285476199,
                                                                            932519.1344025244,
                                                                            62272.37093211833,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԓʒӆϊ²qěҳɌļǳ¡ņӌʓ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6672925220888840108,
                                                    },
                                    },
                            {
                                        'name': 'ʭӒ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            842028.3936488611,
                                                                            998049.5697723438,
                                                                            770274.5812558727,
                                                                            -47414.75604811238,
                                                                            915394.8543903591,
                                                                            991922.7695961581,
                                                                            63863.40373621424,
                                                                            347836.48311804386,
                                                                            824991.2696498706,
                                                                            104216.00018869535,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŒɁȟϛĴǴāХ҈ҝƮ\x93ӆԬԭƈ°ŭ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:170250.856574:+0000',
                                                                            '20210302:170250.880354:+0000',
                                                                            '20210302:170250.903397:+0000',
                                                                            '20210302:170250.926339:+0000',
                                                                            '20210302:170250.949568:+0000',
                                                                            '20210302:170250.972482:+0000',
                                                                            '20210302:170250.997166:+0000',
                                                                            '20210302:170251.018472:+0000',
                                                                            '20210302:170251.037231:+0000',
                                                                            '20210302:170251.055569:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӰƠǑɎæЬϋˍĀŢ%ԈǬÏ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
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
                                        'name': 'jϥŇPӿǺԗϹюďҌɟŮҊ\x931ųȕҦϤӃ˩ɬϧ\u0383ӤДˬ\x8bN',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'υѹşʴđ˷˧Нīηԓm҉\u0383҆ǾѴʘýɚ¸Ǝ¥ѩУԋÛ˔ȗƌ',
                    'message': 'Ӻ¨ɠмƟɑĥҭǸǽǹįƭȌßŲϰǞ!ˏƘӆĿϦĢмɲωґÂ',
                    'arguments': [
                            {
                                        'name': 'ԃŏȥԭӹʱŬΚ˭ӰͲΈø˭ǇĸȯpΛԈėӺęɾĘŸСшj¾',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5367945133450718038,
                                                                            7427014277342307515,
                                                                            9020043303671535578,
                                                                            -4844120673954051352,
                                                                            -7751848485247467368,
                                                                            -9036662931951484262,
                                                                            2365482318394721299,
                                                                            -806036364728346259,
                                                                            22014004626816315,
                                                                            6962534808934138943,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x91ϕӛΊѵәǦɬšɼʜŪƘĐCʗ\u038dʟʚҜïӾâϳ.ȘЖμ°ʹ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '·΅ª˫®Ĥ\x91ϻςӲӺG˃EΓΣјΞˤԓnÖȶ½νɫÁЧ΄Ȑ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7802192599771123799,
                                                    },
                                    },
                            {
                                        'name': 'ԈɂɾʯȲχѹƩɡƧЫ҇ΨӀѦˢйыˣșϫӰİɱɃϕȈΛ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:170252.345359:+0000',
                                                    },
                                    },
                            {
                                        'name': '˳С˛©ʃĬʵԮϷɝģŕÓʉëɜŅη¥ϡύʹԮœ\x97ĆĄӚɤѺ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:170252.436675:+0000',
                                                                            '20210302:170252.454827:+0000',
                                                                            '20210302:170252.472203:+0000',
                                                                            '20210302:170252.490106:+0000',
                                                                            '20210302:170252.511618:+0000',
                                                                            '20210302:170252.531464:+0000',
                                                                            '20210302:170252.552180:+0000',
                                                                            '20210302:170252.574712:+0000',
                                                                            '20210302:170252.594379:+0000',
                                                                            '20210302:170252.614152:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÄΟďэkĀԚΌԁҗƾŞȈˎɱ\x8eíƐiʩ¢ÕԪɽԚЯƲԙǭ˖',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:170252.723238:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҕϾϒрϋȓȂeԢѬ϶\x83Ūѡȫ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            410966.86678778095,
                                                                            639.6350953794754,
                                                                            403673.6604470179,
                                                                            -53989.450861180376,
                                                                            871537.5916357856,
                                                                            407278.75462113396,
                                                                            231280.12162146263,
                                                                            507831.3551990554,
                                                                            931775.1542837963,
                                                                            -95945.31516684101,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԙτң',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ǈÁƳÔԋ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'є:',
                    'message': 'K',
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
                'identifier': 'җCѸϖȈғѱŴϦҙňĵͳƵӟƀ\x8c¦Ƙ¿²ͽ\x9a¤Ѹɰ=ҵ\x8fӑ',
                'categories': [
                    'access-restriction',
                    'network',
                    'network',
                    'configuration',
                    'configuration',
                    'invalid-user-action',
                    'file',
                    'network',
                    'access-restriction',
                    'access-restriction',
                ],
                'source': 'vϾӜҴɗiѩ²Υ\x82ϏƩ\xa0{ˎÕ\x99Ќċǐɦ\x8fȴϴřƾ*ǡѻǎ',
                'messages': [
                    {
                            'catalog': 'ѠˡǌʗȓиƕѴđʞΙǋaҾƥӴŲŨLː×ˋxɒĸуƙ\x83¡Η',
                            'message': 'ˉѰŮӣQɮӺɝɒǸŔƒпʤ©ͷȫŬπљȽήɮʞȆ0ȿĥӻ˭',
                            'arguments': [
                                        {
                                                        'name': 'ȢÌÀōѪ51ɰ]ɖϬ´Hзʠɗ\u0383ӪΌ\x855дΔѣіō\x89ЇɘΈ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 927046.0913177378,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĉȋͶχ΅ƼƴʓήƒϫϝʡƐ\xa0˓KЍƓΠ˫ŅĻϬ\x89ɉӻǣǻέ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĭǒƇͱ˛ўψӳбϙŏÌJ϶ľ\x80ɾѠұЉϪě\x9bӸΫќԤŶí',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҰÛ˻ĳúğɺœƕȷʬȆǰԌ\x95ȕғƳӃÎÙϳƘț\x9bćǲŬζș',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԋƁʄϛƵҚɀ˖ʷƢ\u038dƃ˵υƵԬȌҞ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '`ƺҦȗ˸ƺ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӢlưŶ<ǡͳåӄƋŮŨåԒɿÃ\x95҂Д˄ҾҡEȮ³ʎΕɵӕЭ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ºęЬ˶Ʋ;Ĩǒ¼ŰưӤǻēƱȰƸ²ƶӓћҧИóɧǒųÉɠҥ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǌĈӒʹ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Íи\x85ΛðʖŵʍͿš˰\x9aĤʱ˕ɨϬʣŅŐӛҩgþɦԈΘƆˤ(',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x98ǁҸˤ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6209907683097722420,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Үʢӆ]ǣ˽ĒΉУɰȟõҭѽʫUȿʆÖЄ˅˃ɊȨsʟŴƊԘȮ',
                            'message': 'ԈǽѼ)ΗѱϘvƥΟаǍ˼϶)ӀƅĤϐőʱʠΆċǟėҶùǵʖ',
                            'arguments': [
                                        {
                                                        'name': 'ȼΞѕҞ˟Ԩ.ϪŗϺę\x96ѾЃ˲ʀëӻЇþʽҞǩ2ŗЃˏӥԠõ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8cƘұΟϧþВľǯҦԥбӄ=K˖ЎɞъÈp|QӅͰ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 527298.9477549177,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӜԧɑңȱȔƄϒűȢąѦɗԘдļ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '/\x90ʰӠ˖˕-ϡ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӟ\x8bг\u0382ȱБũԨɈϜ=',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 159911.92730511873,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˬűʚɱȊȕđҟ;ЅΙΓƒˬ\x9eЌиӰϤƳ=ƀȯɏΉȥҊ5ªƷ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': "Ҋȗѐҥś'ȞҚǁΝʐ˶ȇʛϭԫӆŭȱ1ӼɸͰčϱϵ\x98",
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɨp@ŹһȡŕѳğǚȖÚ˺ƳǡǤÐ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\u03a2\x91ӊҺϫƤЎŹЋϡдoɕĹωлɷƫȽʎԔǅŎƚ\x8bɅɀӞϻɂ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˑē˪HӂϾðЪȀҪҊəіåˣӊӚʆ\x9bG˶ӣŤӄȣӲԍΩʊО',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 549249232738011167,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0382XҵƵù\u0380Ë\x95YΓ˸âǯǯù˶Ӽ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ԅþ)ҴЖ¹ήIäѥßÈ˓ψʷėûɢƢΞȽНϢԊ\\ɱ\u038d',
                            'message': 'ͻιÈԀΖԢºR&ˋҽ\x89ӧαiӑʴʺУЇDшÃВťзŜίƧǅ',
                            'arguments': [
                                        {
                                                        'name': 'ŗü\x85ųºˁӂʠƈȩ˽',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170227.486384:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȼϽɿơNлlχӋηόӡλ)ƞĄ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170227.573344:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϠψѬfӳ\x82λľϯԃm\x82ӖƺіǿȕǰȒоȠ\\ёÜϸʾǃȆşy',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʤ˂¿ύȽ\x8b+Ϋ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĝτƐƨèșȶΗίǭΎβɜCͳΫĈъŦϒɽŝИСԗŨВФқŌ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˼',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '÷γñǛ˅жћԥǱǅ\x7fB˃Ɋ³ϿƗƤ«ӝёŗҶõ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\u0378ЭŗϫǫǄљŉԈʬѕсɪƑҒʩԥȅű˹ûǑĎ\x9fӇϊԅĦәˉ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ÚЮĵÕȗæӴЌ˖ÑƯɤ£Ҟʻζˋ˰țƁȹʑѬԆ˒ҽŝѡцʓ',
                            'message': 'ίͺiȚЛӑˤӏӉƦγˁXȄшǠΪƑǑĮČЊήүǱΟĻ\x82ҤΕ',
                            'arguments': [
                                        {
                                                        'name': '/έѶѰԜǷƳAӾĊϓԠҤŷɿ˳гƘ˵˄ŚŵʉɉɏϣϰʝƯϯ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'dɞŚΦJ҄ɻĵǦǃхͻʇϕǓɇÜĬʍʊϠģ¸фȠˏ\u0381ǉɀ˅',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӱ\x94ďΉϗѐγαΐӏ˺2ʩЙѶƦ\x98пǂɯЏÓúąϙǛ²ĩǹű',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'zӠʶ¼ӊΤ<ʇӓВЪ)ɵΙХэηȮΈ!ҏEǤƞʪ}ɻӘȻʟ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'üӺҺΣэÝǡƓэˇǾԬȏcøϙ¶ʖӄĸº°ӋЄѸȲǡŴ°ε',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 280173.50595711963,
                                                                        },
                                                    },
                                        {
                                                        'name': '4Ÿӌ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϺӋșǈҔʈ{\x96',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȍԮɼȅŤĔРӁʒҘΐ\x96ԓơĂȩì҉ɜѱӶdʇ˚ɠƖӐӁǔ\x9c',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϭ\x9bƣѢǂƓƯȽJϷ\x91ǰ˖ÙļƅDÐЄŔʍǅkҬ7оŸʾ˻˟',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5774286957559773872,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǳЈ\x99˅ҺςáѪλÏƫҠԍȝξHђʥˋѿǂӲΔ\u038dΞѥɂСЖú',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170228.803938:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '*¹Ηпэƽ{6ӚԙϷӔ\u038bǷԠįĨщӞӄʡŌѵˑ\x9eĲОɐҏЇ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x87γԏ˄ʹĜɾ\x8a¥ȎΝͻƠñǸ;ʪ˴ҏӿįά0˱\x90Ѐњ҈¨ǃ',
                            'message': 'ѓҚɣ˚ҸϦҰѴά@ϔѢӉѕĉs:ɗǚĨοĬƝҠЩӟ\x92҈ǘμ',
                            'arguments': [
                                        {
                                                        'name': 'ƞһɝͶˁɈ\x97ȵʱȪƣ\u0381ʫҼƯ\x82˾¬ȴȐξќ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170229.035013:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÆΥҡіǟēØԭ˴Ԡ\x98ƪιЙԕѧªґТƕэӆΓвǵϧȓÇеʃ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '|ðølʹȝśǰġ˲\u0381ԣ¦ѓӕʘƹÂʶͰʳÈńEK',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'гΪХɤəФk0ϭɴɡ҂Ű˨',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͺɸǏgҚĬԇҥӯ e(\x82Ȁ҈ʱԓСФȧ\u0382¿ҺȀ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -49106.68770956923,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ØͰäƚɗ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѷĵˏ#>Ȫþǩ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 916621.6013276658,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɰ\\',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǁŗǔӳ\x86үƬ\u03a2ʈΠҭеѣƔĻògјʌMƕŹÔķxƮŌң§ğ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϐǩҁάɮąȇϰñϔ˱ʎʩĲ\x95˔ѯˣƅ\u0383ҜȺʆяЪǆӞƢ\\Ȕ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҫś',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'уÍA\x9aȵƕʤľ8˚ԉĥƯσTϩ}ҝ¤ƠĘƭȚȶÌ_¶ǼϏƴ',
                            'message': 'ΡϖʋʑƔТŊК˧řȺǕԥìТn˱ÇÕʮѕƅέԈЎɳ¬ӲЙÿ',
                            'arguments': [
                                        {
                                                        'name': '\x91ńұбªҬʇ9Ďѱ΄БԕȊƼԡA&ʧ1>ȣ˦ӢЇŬğDΒƅ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƍSȳtßǦŸΧѿõɸɟλ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ёĉѢ·ҷҴȢƻˊ˫˯¤Ѧъͽҭԍʒεñĝ\x9b0ҷЍɁçѥŴɬ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʹȘåÓäŢʚǤcpʾĘђʰIˏȨϔȊȈчDӸӍώ©ҪφҷƆ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˅ԥȿ҈ҤǗãӞºɈπŊҵʬıһȬњ{˂ʺӑјΥ&ЉƟ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'vϪĻӤ˼ϵ\x94ĨũɇŊкԙˤ¾ʒӼ²˱ϩ#ì{Č\xadȮӢǳȇ¾',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΑG˄ǺȐѦûѵԖŖǇ\x95Ȉԥюϲ/ϧҗ\x9eƹʽɛžąƲS˰tȗ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Įϛϙǫlπȕ˗ϗϐюôɈƭɫѮԟөкħ¨ñʉƮʃȣƾδҸˤ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѺΘ%GͲ˵Ȣƾʿ`ĮԈӸӇŸêЕȿϔMӧӰ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 659685.031523784,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϕƶêɆͰҭèӣďĳΧη~Ý҄É',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǤЋɸЦơŖĜǞÝ)øƬ\x87',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2488283712119536986,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ε)ҏ\u038b\x93БǠŠȕɘȨȋ|ąɷӾĹΈʑΉL,]ӥ΅ϡůȷцЃ',
                            'message': 'ċȄҲţѣʞɤϡˠ\x9bϛłнҼŪȅɫԒÞʶaϧ˟YƖӞԓǄyю',
                            'arguments': [
                                        {
                                                        'name': 'ʺҼǑǶcϫƛҡԦχѕӘȷʡ\x9cˤũǾғЌ/ψ\x9aŏɼû#3ġ\u0380',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĊǪúȩŝȷ*\x9bРήϘ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҤҀѰǓԙ~',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͱϞʔȔӢHΔһѵΊȧˣ#ψǊʺҳѽǳ˺ʏ˼ƌӐˆƥӬŪиƃ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϢÆҚφҹÃʰˡǔ\x85ĊƟƤӳȕШӫϔ-Īɛϱ\x92ϬʎȉĶȬғū',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ňӁɽʠ˺ѣÏԖv҉ҌŭŒÄӹʥŊȠǛɺ΄Ū˰ǟЮ\x84əǥˉ?',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĶЊÔϛʍҤ\x92Ӧӵ°Ǌɟ?\x81ԏĐ%ʘХɣŦȷӒƱӔ®ŵȶԭΙ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -639730128598159362,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Μɮ˕ӉȮƌʅЂȩ\x9cn¿ѤΩbҴ¹TsɩˋСíüzЉŷ\x82să',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ɜ¤\x96ФƓξԋ\x7f'ҘҷѫӳѝӥőŪşϏÓѩɋΓӲҽ\x81ʖ˶ʋÈ",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "®'ƁȫӅƔŴʁȂɋǊͳӫ\u038dΎȄɱōʺѶΓҶԞģЕǠ}˸;Ѡ",
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԢʠԀμɪɏ1ϏдʬԉʗƊŵǳī;ɑɵʏĒõʁɋΜŨΓ\u0383Pԟ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӜҌԓӭѱʴƷӜɭѢɯ҃ɵǄ\x96ңҗˬ˒ӣӁĄ=ΫԮřԎ˜UǏ',
                            'message': 'ɊɷƗĚЎȑƃҼʂĕэϚ©λΧȒҁԌЊǴȆĎƧʩȍͺ҉ѱ!Қ',
                            'arguments': [
                                        {
                                                        'name': 'ӴȶϞñϸȏ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2303946033244306424,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϥ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȲhЕҟAĞӿ¸ЦԎǩ҇¸ЩӤȨʐƘʀ\x86ыҡàZιȭЃҜäƓ',
                                                                        },
                                                    },
                                        {
                                                        'name': '½ѩtǈ˙ǊπĎɚтĠĆТϾķrϣҫʢéɼԃѯȏƮϬñêëĘ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԕǽЫˠǥÓҤȤΈÇϷεPԖσųŲƂӎϨЭИ¥0NƀOҀ3ß',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6966684851708158224,
                                                                        },
                                                    },
                                        {
                                                        'name': '˥ԎЧӾΰζŤČҵ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɉϷņɢƪԞǦ|ҝҬЀ\x7fƵ\x98˻ĐϟŀŖǱѨӰÀk½źʃͺӜI',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170232.428454:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԩПJèδԉιНʑҥԮȁрτˌ˂ћљȷɬɡɹʷś',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȓҏc·м΅Ӹɇπȍ˺ϺΤbA',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170232.592339:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǎȖʨ¬',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѓȴƘƂΤˏúѧȩÖĖӉʰĵĴÝƬIѴƊΰÄ²ċĽЅUÆÇŤ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170232.787001:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'џȬ҃yǛѰëǑȣƴȯ\x85ƅɨaŋ͵ǌҬԇɵĄƅ\x91ΉѹƦηʤA',
                            'message': 'γǄԠʢđɷҲĲж\x93Ҙ˅ǨăǐǇ˪R˺ЄˈӓΧч˯Яǰѥ!ƹ',
                            'arguments': [
                                        {
                                                        'name': '}žtШȧ×ćǴ;fňǦʩμŃΓƍ\\ƼO˻Ȍ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȞˢӋĉɑ҉Ѭ\xadņϹǟмË˛£ʐͰěqÅȏ:ƯȦЫŚyƽǬǇ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Б\xadÀҫЖˈг',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĊłȱǫIăмψуō˅ɬҾʄâѴΡχɒ0ҫă\u0381',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170233.119604:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɱζѪеơÇȚӚZǪʘσΰƞҿˎȱӴÔ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÖЕґύȼгѵʛʶ/˨µmİўʞǮʧĬїԉϫȕѧʯzťʡȵ\x91',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7219871168428509338,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ќα1Ĥ.èԍԓƲ¨нɮЌśǇ˨ΆʨǒȌìƹǐʤȵɻ¤ɷȁљ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 437160.73642716755,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԔĚϓʍó\u038bӬäƓǵğйаɘçï',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˯ҫ˅ЍʛʌĿĲĝÑČʥ\x8aʊ>њʻsϾ˨ÑҾæɟШĥ\u0381Ǽіƃ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'йУŻƙϜiƳˮaϴĢҺRŅҳԬԡͰāǶӕRȩƱǔǴӍ.ɘʶ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170233.619015:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'λȰ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ίˀǢӽԒʙʇϻѨ϶ɿўN҆ϛĉ\u0382ŵԋˊȎʤʉǍʳÕл\x9aқº',
                            'message': 'Ѕƴŷӓ·ĲǵѿçНėƫȿȊʾƌЧҖ7ƚЅȇҽʹԒӍɻϙРң',
                            'arguments': [
                                        {
                                                        'name': '\xadʚѾƒɢ¥Ǳěĝ?c˷{ƒ5ȸ¢ѲƄѢǜϝϫŃГ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҎƊмӨʂnǛʻÃĒ#ǂ˔άнσɓèΜ˷ǉǒԕɔȏƴEзĩҙ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɒļĆҀˊʧ˴åǒɵϮϛхεӉȵψԠӌʴ˓ʪ\xadưźɚɃɈ±˰',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѽʍԋƁƃɸ˺΅Â}ԝ҄ʁΦŶȑĜ]θюҌǽιθɹэӰ˱Vŏ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'φˑұȬж҈ĻͿŦԏ6ʐхá¥ʾ÷Lċ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'CЭç\x87ĞҁЎśëҏӯ˾ħTϋƙΤ\x87ÆȹҸͿȯ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ε˽ƬϤӣSɒˡЂʹĶӆǛΩѳ˗Ї@ȴ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѽ\\Ǔʬή',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170234.397523:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɱ)ȣԈ\x82Γ÷6ϴˏρȣž',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѪpƦџ²чӝԮ˵ҞɬԅƥǐСÖӢҜǯŒÁԨǚƼͲŗȌɓǆҎ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƿәšѥЍҴÉə¿żóΗґ˟ҧј\x9dƣӖӁɁƜŷζÙШћӀȴȔ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2917100959367851548,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˊЂӲȜǗňɛѧƍϚѪϨ\x8aφЎʃΩ˰MөͺХҾ\u0379ӎӅӊhЀa',
                                                        'value': {
                                                                            '^': 'string_list',
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
                'identifier': 'ҖˀäƵК',
                'categories': [
                    'configuration',
                ],
                'messages': [
                    {
                            'catalog': 'ƭp',
                            'message': 'Ї',
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
                'identifier': "1ԜȅƠȀşӵԀλɮ'ƪɉDҗÍԂќϒΝЁδȉİҘ²ˣȤƶÂ",
                'categories': [
                    'access-restriction',
                    'os',
                    'access-restriction',
                    'access-restriction',
                    'os',
                    'network',
                    'internal',
                    'file',
                    'configuration',
                    'configuration',
                ],
                'source': 'ƉěӍҩĺдτʐӿӺѷʹЖ\x91әɹ:ЄǇǘӟһ®šɊßѶHʓǵ',
                'messages': [
                    {
                            'catalog': 'ĳĵɷļӚӋҠȀòɍŪĝɮƂӶьˢ˟˶ǳԉġÖΥʠӪ҇ȪŸȯ',
                            'message': 'и·ȟϣӿӍ©ȺϟǔʗɏȶƔ~ўūҼϽ?φƃƽԘӽĽĎӥPҌ',
                            'arguments': [
                                        {
                                                        'name': 'ȣѱоϟŢӐǹһƓţŋҼƂÐԩɺΑʙ\x9f΅«ŰѿƚǋˑνΊĻ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÓҜÙɷ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĔĤƏԚʵűǉѺſ˙ӈƵʿӟɽƻΟʢ\u0382ÍˇϹҭϞыїӧfôӺ',
                            'message': 'җǮÅσˍ\x92Жΰ˙ɔΗ\u0378ӤNǦɮʉĻʂэӑΨ§Ӌ\x82бˌǂĕϠ',
                            'arguments': [
                                        {
                                                        'name': 'ДȯϥĮӁӠǤŭ¯ːƄѻŸ8уǗƷχҊωйӝӽ˷Ҁ˙\x89ΙƸ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ċpцӑ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Όλǯ®\x88Ӕ7ƑԆӺϵϺӦśéƗÂЁӭԎԑҫϹEŸéƇǅǵʡ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǬǞjȿЃ\u0380ɁȝН',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҫӟůƃkФЈǦѷ·CŤƳΝxѴӶˉ¿иЖćһF¹НΞ_',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2247437899948244384,
                                                                        },
                                                    },
                                        {
                                                        'name': 'сϱʹmҼzɻƢϝϳʷҔɐåƁдÜҲɽѝ˕э˴>ʹĜʤΕВί',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 461066.31195379584,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѷӸϭɗҐƗqͲǂԎÑϱƕӷ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҍͼÿ\u0379ĈәȮϨѻƪЉ˓ωˎɫƄѺҞĝɹǯȃшζҢķÃҎʕϴ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ęǏϨƑȶùӝ҄φ˖άԧɕòǻñɣȯʵҤħʦīȯϛǲÙӿӍȅ',
                            'message': 'ϙаLÙ\u0383яƥ˫ɵПʵοëύҸСťӎуͰҋÝΆǎɏŷʸĬòϚ',
                            'arguments': [
                                        {
                                                        'name': 'ȩcǣҎӮ@ϛѢˣҩØ>ђԮ˃ǪͷɊœˏ\x8bӫʢЊӭ͵љ]ɗɭ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ғżЯǯԮǥԓŚǈǂđȷ\u0383Эȁ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '<ʀǦŗUѶЇüӔʁˈ˹ƫ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Пπ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -135100582807773347,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŗ1Ĝɽ?ȏπȧҷӄO',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɐ\x8fԓģµÌʻÙǫӰʮҤaӡ\x87ӣʴɿѰȈԅȀϟȿ«ҦĔƿ\u038b\x8a',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -75267.1346436608,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĝ¼ʮԛ!pЛэУ҅ðǽʹιʦsԀåɽκ˸ʣȿеʒƘΗӵʗƯ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'œCѼąūĮ\x91ʞԪǏЪӄӠԎҶϧԑΥƼϮǶӲ?Ͷ\x81ȄоȫĄ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Жμх\xa0ɮsåĢɵ\x7fɊƄˆʵɍʙ¾:Ӣ=ɣӎƓȴǹǈ˂MȒˈ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '´ŢЅƑƶƴSӤiȞʉ\x9aԡĉȃgҝΫ[',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӦżeŃ˯ͳŭѕÑЩȾđɻŀ¶ǔʦƃǫU˽ŕԃŠӮԚԒϧӟƹ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϧϼϾϝ;ğˈƶΚʫфшӎҭίϐαлƨ˙äӳſ×ґтʗȮ1˝',
                            'message': 'ŲɼµјϱȲǅϻtÆ˨ǭț\x88ɖԋv¶ʢuεsҵǚТҔѩɾ˃Ā',
                            'arguments': [
                                        {
                                                        'name': 'ѭlϨѫєјˠήŚҡЖт˽ҢҗɴƧƊďϓÀʒԬѮʔġɼ\x7fǤҚ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170256.118134:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '¾ȭųŇӦƙƍɇҠȬҧ¸ţњӃЄХɺʏįѢґÌ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 780977.0890717413,
                                                                        },
                                                    },
                                        {
                                                        'name': ';ǝӶûǄϜЈʅ,§ķáʱÝϜǡŊўͿăɺɥɧʕ˚ŧÙʕʡ\u0381',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĕǎбҽ5șǂƳΎЧӟȬƖű}\u0380ԃŚϿİýɷԤȕɝƔ˂ʕøŲ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 652052.4210649155,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038bʒˏiӲǰɜĹĴ˴',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '΄ԟ˵ɚřȧкОѦѶҼ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '/ԨͲƆϟǚ_ˏȘΊľϤű¶\x832ӑҁń˰ʯȏʰѯ˃҃ғςŞπ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˬ\x96íϕѴӊ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȏƟ͵ƴхTӺе˕˼NŉģɝԏǢ3ʅӱԄțȐοʇҰǂ(ǂΰʣ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7420661975257635643,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǸεʢİsέĽЋɮј\x88϶KѓGɿǮʘɸϬǂѤ˘ˀ/ђǢІ+Е',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2689604380051521698,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ˇϗi҉pԜϦѝǶÕʘԗɪőɔєǥԋļҊβаȾ˥ƚeYʵЄĉ',
                            'message': '\x9aаɢƬҨӌǨůɈɁĩǭеʘΎӴc\xa0īĚˍư˙*ƐӋ:ϫʳб',
                            'arguments': [
                                        {
                                                        'name': 'ӮÿǐМϵÝĨĜǬ˼˟ZϚįđɴƫɃ²ɖʶӣѫϞˌǖƇ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "˧ѩɢΚϳˮɵӘА\x81ÜӾԢĪ'ǇɵļƁˁ\x92ŭϢĻӝǋϟƑǻҘ",
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƲSԦΑˊǑŰЙҜҶŤĎӍЄϙϭȊʞǱ\x9d²ƙ»/аӃҽëӑɈ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ќƒÔĪ_ʊЩȌπ˧ΐӽϱ2ʾȀ˦ÄLÒЊ\u0380ԝ\u038bǅmĤԬưв',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'AңfҚчǙɤӢŖZȃvѻ\x95ѿӦÙʄƤΆʝƞƶлǿӟ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x89ôʳҎŦҌ\x99ĥŀɅōЎЏæЁQĸȱƑæǔ5¸ĐƹЌʈӸ\xadĈ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 584368.8302096191,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Īƞѵ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'РӃЍЅȿ3ԅƳ\x90ӯȼŁʉɾμÏ҂ȨӄБśҾϯҞԁÜɤʛϿɌ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɯԆĽȚĽK',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʺȹҖϵеӾƱńʭԈƦē˦ǥǞƯΧȨŷʚ˶ŠǦQϡʈԞδ\x91õ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϫ΄ĊĤǟ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϒӜɮ3.ɽǷѧ\x93ѥˇȳ]ҋĊуǋϏ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'MѱĸόȻҌ\x92ШҩϷŇʆŋƒѵвƣӚǣӣʈӍӀΊęһŊ˞ѣI',
                            'message': '\x90ӠηǮӅоƀæҹһ˷łĶɚͰҨĘþг;ϰǏңƚ˖Ϧ˖ʃżł',
                            'arguments': [
                                        {
                                                        'name': 'ԍЉfīΝѼ(˯тɟҒǏπα( ŚɂġοˀҏͿÏˤǓȫϚƳИ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170258.091092:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'κ˖ɼùƹҞ+nԜςtEȜτϛҏԞƲϬ\x81гŎɺȉÅԮҩǬа²',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ԛҳ˪ӓɤԗӄǕОѫfʂǁ[ΩӲȺ"ý3\x8fiʍŽXʱ\x84Ґʲú',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ıtҮШǘɢǪХʐßӁ˞ƚćϯвз',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170258.246467:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȉӠӑ#ѦʉџΤîʱŗǩљ\x8eЇҲ\x8afLþɎŲñĲĳƶϷɣҔʴ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170258.338359:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԧώяǯʟΩΓˢʄÇΈ˳zӰ\u0381ȅǯ˜θӵˀĉΊŏưǲӪȻҏҺ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˹ÕǞ$?ӤȞʌ<Ҿ˛ԢƝѯŧǵʏ\x9bȁÆӅȀӟȵɽιNϞȶы',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Йpğũ҆ЖҽŋƟѱ¦ŔxŹÆҭǆˣ\x8bzϣĿγϹҼӵйŃωĎ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'τ°ƃϿ\x93ɶϠɩҳК37ԟµҨĽјÉӍʅӛǌϷӣįϋԙ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ȖΔʋɧǉ\x85ˌ\x88'њǮԇλЋΦϲ\x8c",
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'χčȺ\xa0Ѫ˴ХҚ\x8fxʜӒ˘ѳɑәξ\x9eΫВÙŜ»ŰБў\x89ǽʐģ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ğӌˏӸ˒ϯũµ˕ϩkӺĤɎ˽ΕʂʧИƈȖȏ\x8a˔\x85ɃЩÊ˗Р',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ХϘʃɒԬȫѱǏIʥǞɡҧĦтѲǁȚЬʡS¸όʊѽřѤÃҡɅ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': "ĝĠǺ˦«ͺԣԩԥʥҐЀßŷƩӺ˵ͶɞςUɀԒԢʻђө'ɴҹ",
                            'message': 'ˮ6ӵʡ<ѻė÷ίç˴ƯĭȤPɅtŵԎƉØЁ˲ԈǊ˱ӓҟȒú',
                            'arguments': [
                                        {
                                                        'name': 'Ɣ\x8a˶ʜĸǔɵτ\xa0КɈôʀϊɓԚ˧ԑţДƴē˶\u0378®«Y͵ƞȸ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170259.113407:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '°ȶ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 191288.99537601194,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϔƩǇŅϑȩĹɳʵ˷кŻ·ТūȌҗ\u0382',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8bƩԦʜNǳѳұΡ˶өĔ\x82ʘмԚȠȶЍɴϏǣ˖Ο˳÷ƜʿȝΨ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ζ\u038bÊǤɸK҉ӠϿӴiXĔнԩ˦ȗä@ɮƆҙԟɣPķνǾʫĝ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170259.494997:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x99Ŗƾɶl˷Ɲˣ͵TѐŌκȲΑҐ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĠăЏɢǶͰ\x8a˾ʴ¦ψӭɁĒҏ˹ͷюTǭʹŘϦǤǍӑ˼ӑӹǹ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'KbϯĘүǒĭÖŎƛȀ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԇʝƨҤǕԚŲԆqxȡЭǐɬӯѫƑ*Ãʞ˩ɽʰΥɡȔ҇ӣɓҴ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҰϴӳʊѻҌÆɶʖȥȘоαщ×Ӛ˹ŪΧiʲpňŅΔĜѭǻЅR',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϙсѭˣǎХϩȯ˯Lͳ˨єʾΙϮĵͼҥΡqˠ\x9dȸҟӘ2)γΟ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ƶӑ˰ɷƹǻǅӌǊϗϮ=ΕƴЎҼȜɺѡ˧ɮǃ\x8eӣяηčˋӴȡ',
                            'message': 'ǎļɂƃ˽˛ˮƵиѦ»ϙҋÿԑψōӍǟŴʧЖcɜ§ΌqƯϱǸ',
                            'arguments': [
                                        {
                                                        'name': 'Ӝ¯&ÙζзǨȶΰѩьƤǃʴďɯ\x9d˥ѕΥŧŎҡţıпǓґŞМ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170300.051885:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϣϐ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 510903.3060132285,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҩ÷ΫѡA1ɂ;ƤʩфĮяҳƥ\x95еǴǄƉǆһ ѳāΝѫ˭ϓ\x9d',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 278759.3273197128,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ëφžԁʓkҁ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԡÃό\x87лЂѓҿ7яƽҿ¤\x7fԥ˥*Ł˕\x9dƍȍΣѧŌϹ˸ԃϬƵ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170300.365378:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ωЕѾɴƤ\xa0˖ƝƂɬǈɈÝӺѤƗǾʱ\xadǕȏøƭE·ЍΡKÜ˧',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƕˍŗϷϐʖ˦ȌĤʾѩBԖĿģ˷ˑѳӜӲΣĻѴ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʫƌϼЊԭɌмӈÚρӵ½\\ĎлХώҗ\x97;аʎ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ǯ˝ԌГĶŋ,âԜȑϘȔѩşÖԢƏ£ĖǬǈIǠĶɅƋΏĶяз',
                                                                        },
                                                    },
                                        {
                                                        'name': 'СQlΛǸҽҴыǶǦϿţҴӷǿԦ˕',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˙É',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ß9iѠ˘9ԩĀŽŭίȖʽę`ˆ«XɄƗțĵƃ˂όfÚӿÁ«',
                            'message': '\x88äΗϦˆѕîãҖԋʟ_ПԞş|Nwȳԙż.ӈɲцҟҲűʖƧ',
                            'arguments': [
                                        {
                                                        'name': 'ҠĜԔ˚ȏɻ˜ГλҰк\x8bɁƅ˄җІʗσӯЃĵƏζǐąĄɦʚ˒',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Сͺʔ˔mʿ˘ŌkȩʆѴĥих',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѬύˏȅFŮԎǙΥӎē¾ԫÏҪ·Ұ˴ȇѾƀ/ΞeӖʛΓΊǝȨ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ļɶy\x82ӞњƻȆӀƋЖĭųǭʾɍϪŔӣ¬ĮЍÃ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'č',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҲʓȱΗӘ˳bhπӆɽnχÉΘƬѷ\x7fɥ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˠǂϪȳϐӈǮƯԑөˁ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170301.477476:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0383ɅԌѯqŵԉȈ¿ͳѶӘ¸ϫҖɧсӅӖсʶѣЊ¬\x82\x85џǆ(ќ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʶƽɹҎНǱҟ˅ι҆\x97',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'bѕŪԑĎσɣċʣȧý~ɉŗ^МȆ\x95ņʠ ЌŹӷĴ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ßҎīƱζѰġăm΅ɼb¨ҥ\x8aɯʵŖӠċƁpğҚǥӔʨó҄Ȭ',
                            'message': '>ãˉɆŒҵƊĀҒȞʣĸŉē\x9dҪ^Ƹ=iƙϽτ\x96[˔ʵŹϔģ',
                            'arguments': [
                                        {
                                                        'name': 'йʌzԪcĻ˟ž\u038d˨ƠèјɝíEԬĉҤ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԃҏɚκĽԐǡΕ´ͶЉĪζÀѺƩґƃΩѵɽ·ыťѭӏҡǕǯŸ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѡЌįĈȖόϙ+ΤӬ˂У¸ɈŎŀ~ԉӴε\x9b',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170302.077770:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĦċʫԒϑӲҺċċԬϰǁż/<ƽůјӪҘŖΒԤư¥θȽǟLǗ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŽǗоʬ\x9eԁѫ˾·ɬɏϮÛԟÐǽèʉǩɬЧʙƀǫŹҢѳȤSС',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'tѩɽľɣўɜĆˢŦǫˎ,\u0383Õ©ɷϤ\u038bȿϘčц´εԌмɓȂι',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҘÇѶŦҮЉϞ\u0380ȠʋѼȗKɍôϢĭĆ˞',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'OѓЉ\x91Þð͵ŵˠϭɾɫǪҏѰȾƼPƭǫͿâԌĕӵҋ\x94Ѱȍϋ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -421309352394800920,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȠӄӴбҕƼϭқ6Ҝ\x83\x87Ĕüʸ3ЭϏϝċԢʼЧ\x82Θ.ĝȵԣö',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ІЍ˧ӒÇӕùƆԨȦ]ϨʘßĉҲYĂĺԠɰƞϿåҢêзƞÛ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:170302.666172:+0000',
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
                'identifier': '\u0380ǆʀȯѣ',
                'categories': [
                    'os',
                ],
                'messages': [
                    {
                            'catalog': 'ɞ¨',
                            'message': '˘',
                        },
                ],
            },

        },
    ),
]
