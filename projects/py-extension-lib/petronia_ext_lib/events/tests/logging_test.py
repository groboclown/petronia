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
            '$': 'ǎô\x95ʚBӤʤęƟҬɖĊʆZȣЄҰɌʼǍʯԆѧˇԡΕĊϴ\x90]',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -6371299023936604305,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 559146.1118899628,
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
            '$': '20210910:185540.136761:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ӏϓЊ˜ԔšͶūψƭυѬɻΡӢςԮƢũЯűĴøıƿЇԓ\\ÛE',
                '\x95ǈωϯӝʝΖɇӨˊƨКӳLѿȇҲΗʭǶϲ˓iɭķVƃŉѝŢ',
                'ТŏŧñҳcҼү½SĿɥÔԒРԨɸν>ϊÃύʾŬÅƤʥʈӭԮ',
                'И˰ҬŢH½ǮȜƬΤΚŦʻӬ#ŵõӘãŶωφ\x9fɗ[Îѻӷ\x88Р',
                'бʫͼыÝȬʅê˲ӵ˃˄îΎɖͱ\x82ʓǴǨħ\x8fɘӢȣ@ӱɄ҄ҁ',
                'Ѿӎʎ¨ŮκХƾѳ\x9eȁȭȲѨęλíÔĮÀӱĺʈ¨ʧǹѹ˨Ɯ͵',
                'ªƀʬǤԛĝԊӽJαʟw¸єԈWҽƩΰ°ɇίЛϡϸqʲҖʝɅ',
                'к\x93ĉǨ7ҤǰėcѬ˗ų\x9eʓƌȣϘԖäj×ġɤԥѕϜ҅ťӫΊ',
                'ЩѮη\x92ҮƉ\x98ȌǮΎҖʃƼĩϯȳѽіТЕ\x91ԍȃɃэщʧӈʈǠ',
                'ϽĦɃXȚЪͶˢȟђԐȇϩ*ѾeʴŻϽͳÌĸxʁİŬȉȧмǖ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                652535399315877161,
                8527266915016834316,
                856574215205547444,
                5806752469644577930,
                -2883445627175176979,
                419528837547711353,
                6390544327553324346,
                1160948319200444644,
                435187016130798200,
                -93750888028678604,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                595579.0442719065,
                505366.3609865339,
                600741.646622938,
                454948.9292069528,
                112250.34413806355,
                362258.031710262,
                694271.845072756,
                304796.3480082651,
                674153.7100198346,
                136699.05783048735,
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
                '20210910:185541.241549:+0000',
                '20210910:185541.258673:+0000',
                '20210910:185541.276821:+0000',
                '20210910:185541.294902:+0000',
                '20210910:185541.313276:+0000',
                '20210910:185541.330603:+0000',
                '20210910:185541.349191:+0000',
                '20210910:185541.367327:+0000',
                '20210910:185541.384598:+0000',
                '20210910:185541.404705:+0000',
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
            'name': 'ʤζ½¼ȣŋʍ˧ºÛWДџҕ\xadȄÞÆӓ\x92нQȊ',
            'value': {
                '^': 'bool_list',
                '$': [
                    True,
                    True,
                    False,
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
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ɫ',

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
            'catalog': 'ċΟӑȨҝӺΧͱwâ\u038dƫϷЏӎʺ6ЁQˋþЄȁЇ҂Ɉ\x95ѫϺɉ',
            'message': 'ƔĖҚҩҪϡȄɄʡǳϯũ˴´ӯȨΒңŢǢ¦ʩϓʦτ˩ϊWΎ϶',
            'arguments': [
                {
                    'name': 'Ǹλ\x9dЁɽĭ˷ˊɍǮˤЀΝ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210910:185537.807539:+0000',
                                        '20210910:185537.826813:+0000',
                                        '20210910:185537.846182:+0000',
                                        '20210910:185537.875571:+0000',
                                        '20210910:185537.897171:+0000',
                                        '20210910:185537.916715:+0000',
                                    ],
                        },
                },
                {
                    'name': 'Ĩ˺ϖϢȗЩýƎĚʂ¸ѭѮĂԈɪŽʪîŹďԏȷÏɑ\x83ьқøԗ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
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
                    'name': 'BϘЯҫ|ѿƎʴ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        3748550390008891471,
                                        -181576833827931723,
                                        -5361704423711128776,
                                        1778475895696291906,
                                        -5899686326074353270,
                                        -6844151514960921845,
                                        -5644746510200855819,
                                        2267868969732315272,
                                        -1155432215985628619,
                                        8411234556722759033,
                                    ],
                        },
                },
                {
                    'name': 'ʥƾήċѨNȾɆ{îîϦʻƩEϫҖѶůõӷƓїϒş@й',
                    'value': {
                            '^': 'float',
                            '$': 513510.9166630197,
                        },
                },
                {
                    'name': '¾Ƚӻ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210910:185538.624981:+0000',
                                        '20210910:185538.653367:+0000',
                                        '20210910:185538.682603:+0000',
                                        '20210910:185538.712406:+0000',
                                        '20210910:185538.737493:+0000',
                                        '20210910:185538.760004:+0000',
                                        '20210910:185538.781506:+0000',
                                        '20210910:185538.801472:+0000',
                                        '20210910:185538.823094:+0000',
                                        '20210910:185538.847180:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ČщΓôˬ',
                    'value': {
                            '^': 'int',
                            '$': 6529916906367884888,
                        },
                },
                {
                    'name': 'ΗΨˍӢҶʯǱӹЩȓŊӨӥʄƽ\u038bԎχφ¶ƔɟĹѼ¶čå',
                    'value': {
                            '^': 'int',
                            '$': -2316053925723110675,
                        },
                },
                {
                    'name': 'Ϗ\u038dАQ˩ӟǊ\x86˭ȚƅƩĜʍ¤ʴпʙʻǪчð',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        7045991567170971221,
                                        487836192566997189,
                                        -5585219922118838758,
                                        -573956065049887737,
                                        -5437036646413882082,
                                        -5030655030029083256,
                                        1570667888654206792,
                                        4022087661107603239,
                                        1150131541358260270,
                                        6475122939629809404,
                                    ],
                        },
                },
                {
                    'name': 'ıȐϑƊЁǷȵdРϤǖKy҄ƶɀѣƁķėÉ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210910:185539.406397:+0000',
                        },
                },
                {
                    'name': 'ɆŻȶƺϒ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'əʫ',

            'message': 'ʇ',

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
                    'catalog': 'N˞ϷϸҡʯãҭΈοçsþƹjҫëʃϥǳʷɶĠɠEƁϠFҝҗ',
                    'message': 'ɓδѿύʤAɦģĚМʛΪu×ӘϡσƪȅƭΑʣτԃěϳѻӆԃϨ',
                    'arguments': [
                            {
                                        'name': 'ѾҦÅʌЖēĳʭUǷѤʷӂŎ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 263642.2859863393,
                                                    },
                                    },
                            {
                                        'name': 'ëńƦԍªУвё҄ӑˮ=ĶʹɼƳѿ\x8bůҨ\x8dŠPǶѕ\x8eɓёĵʦ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            599612.744739409,
                                                                            899750.2747983928,
                                                                            692759.7050317082,
                                                                            891085.7499123919,
                                                                            238570.4810188901,
                                                                            160779.8021363091,
                                                                            717821.5602773487,
                                                                            902611.3710908113,
                                                                            -82000.15033900246,
                                                                            720606.3379735318,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'іϚƔўԣӫ¢ο÷҂',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            17391.561720181096,
                                                                            693489.4572667197,
                                                                            443399.8727742827,
                                                                            10681.615034689166,
                                                                            195155.05957743252,
                                                                            56759.46389958053,
                                                                            654515.748232619,
                                                                            875884.8715566273,
                                                                            24552.499485314445,
                                                                            321568.00165659445,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'κʁSЎô=ͺӆ˵Ȫ3ţȣ¾Ԋ\x94ȃøÞÒ¡ưɇӨŞʉӄ`ʗȽ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'QąÈуϱАѣѾөÑɈҕǐўʻԨԛӝщˁʃӌюʣǳŝ¬ѱѮԣ',
                                                                            '\u0381ҽŇ\x86ƒ¼ȞýϿҬǳѪɆϷĵѨԔƢņРΈ\x8bЬËʣ˻øʲŰҞ',
                                                                            '£ʱҟçȀ\x83βȖǍл;đƓɿɉϿzЃȔ=пҼĽAσӕ˺ɌlԈ',
                                                                            'њ˄řˋӔмĔĮjԬȰa\x81ɩΉӒӘƫãõʔ˻ɲŲ͵ŔǵԨΑ\x90',
                                                                            'ӣÑ˞уԠʐΜʭɓǎѥ©ōnɧӼ\x8bчʩϚ^ȳ\x87ʄ\x93˓ԛ¢ϡȲ',
                                                                            'ŦѮϕɌԍƧƦŤӅɠǂӎ^XǗǐǈȎńȉɾѣа,Џ¨˾ğӀª',
                                                                            'Ͳ[VȮǙǀ¾ӊԑð҅ŭ\xa0ĽÄƓԄŢąĸ´Ǔ;ΩũʾǳгǧѶ',
                                                                            'Ѐ[óÑʚ˻ӶЪƺҥ^˝ļ\xadВӍƔбӰҎ~ĪȇčӯѬʿ˱š˳',
                                                                            'э`\u0380ĮԄԘʳʽҼƨԏƴЀ}έ˚ӏԑ˰ĨӹĵтÖıӨҽťȴʪ',
                                                                            'ȦχԋҡśЧԥêš;ѼϊιΌφͻϵȦȂƵƢĕӨˊŸԐɇɖҳљ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'žʹц',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            844823.9251559066,
                                                                            218620.19946072035,
                                                                            -47167.4261515859,
                                                                            950762.7502499251,
                                                                            819700.7658552713,
                                                                            605812.6075480729,
                                                                            489887.5068901053,
                                                                            634502.8058466295,
                                                                            529964.8657480387,
                                                                            769221.5307547593,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЃЦǿφƉΚуˀԖζɄЂʸˏпŎЄǍƉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 161343.95667035048,
                                                    },
                                    },
                            {
                                        'name': 'ʚϡƐ΄ɉɰ\x8cµԔѧȂġǙӻҴɰΡϜʇ¨ε\x9bʜǾ˷ǋζ¿ǡĺ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5749395029630503818,
                                                                            4691488028507151006,
                                                                            6318937888264270367,
                                                                            -75881439731634,
                                                                            -4885578079110764430,
                                                                            5431513043064196436,
                                                                            -4677826314728454627,
                                                                            2650414465922152561,
                                                                            1499603061812070074,
                                                                            -6991006860061771387,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӆ\x86¹ɵҠ¿ΪҺ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 606478738081715513,
                                                    },
                                    },
                            {
                                        'name': 'ҔѥȠΌȫ\u0383ȭ¾ҿŝƌƷΘ5\x90ʚћœɍΣɧɷȫwѸɀ>ы˖!',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6585659600521118281,
                                                                            -4026533092227340332,
                                                                            6523374427274421526,
                                                                            7239598193383355719,
                                                                            7880121474677640193,
                                                                            2658326530871965832,
                                                                            -1007891338284373901,
                                                                            4047875926681820348,
                                                                            9166179295589348258,
                                                                            -30273223598394011,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¥Χ\x8eǇ°ӖӞГ˫҄ϩůŐ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1259798900682089140,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'шƭˁpяˑ^ћšЄŎЭѣʔ|\x9fх\x84|ӀѢƧ\u038bǄRǫ÷χǻς',
                    'message': 'ļƟӲ\u0383BǐѠɬԉǎɸЫǟˬêȌƸԨ\x99ŮģÜ˵dДEÞɨʆԢ',
                    'arguments': [
                            {
                                        'name': 'Đ7',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɭȰԂƐŨȌǑĚ^ѭȹXͶвʒԤ;ӫƊÖЇϤɰѨԒ\x8cԖѿͲѨ',
                                                                            'ѸҸΓԃÜΎƠ\x93Еr͵ȯƀ ǇÁЄӭ\x81;ȿƽҢϗɌʒńĳɐϕ',
                                                                            'ҁˁȪʞċ7ƣȩεϤΨĬέ¦ʲß#ǰȅǱΐӓ\x85ғǾǼȢȊŴƜ',
                                                                            'ǧƃ3ӓӲηōϻҚќѥϳM{\u038bĤΎѣȸǮə˰Ũ҆ʶ\x87ѻƍʘԜ',
                                                                            'Ӹ\u0378ʾҗįѬˣɤ\u0380ȴÍ\x99ņÓѕ˘ŀҋÒǂǒҝϚΊˍ˄\u03a2s;ї',
                                                                            '\x83gÓėɎƧσ͵\u0381Л\x89ơҜƯ҅ʜµʁÄѶɖԚώӼ¦ǚϝʱɰǒ',
                                                                            '\x7fşȅƑɫƀĠƍɀĵĨЊͱҺƅWȏʃтЏtãȝϒǖƛ@Ϗӈʿ',
                                                                            'è×ȆnďșɲɾАњͲǴȖ\x9a\x9fŊУύʮƔĸÎЀƚˣĊģȳƆʛ',
                                                                            'ÌʠƴӐǷǍɌƿϫԍÍſіҨзΆǰҮɩʢʬǁǉƐIɐǎϖƙǋ',
                                                                            'Ͳӱ\x98˟ϐÄȜҊЏΩҜ˃5ӖțǦ\x85ũәTтʘԑ!бЖÍǦСK',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'гǏѬ҄ăӽ\x9dŦ«ԄĴɕǇɓAƆӧʘɧÝʌQǳ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ò÷ГеȥҲɏŎӭέ\x98Κđε\x88ě˅ΛƻĂάŽϾȭԄԋȡүϫĐ',
                                                                            'ӺǴȁяΫˠȒŹţӠǉjɺςȇӣƚЕӄтȪƬЗĊӲӪǜϠɐƹ',
                                                                            'Ԗ\x92ϥ)ԤѺѰhŐʜǾǕsӕZ)ʱӷЇʜӫūАǽ˔Βϑҳϔľ',
                                                                            'ΩŐĸʧȔȏ@ӒǂĳĴ\x9cɄй§ԩȴʊЙȽǼ"ÒӨɜėɕńӧĪ',
                                                                            'ƓȌюȇϭIя҂ΣҴҨ\x85ȮþrԑǻԗȆƐjѮљ2Â˓ɿ\x9fƊӌ',
                                                                            'ӸӿҠ°ÔɤаӋǢϛϖԁΈǑûͼ£ˍÉӢƷĪНʪĸҡ-ĆˏĊ',
                                                                            'ΎԍΟǾĈĉεěƀĵŋΐ\x8fȐӧÌӒĬQȍã"ĴЎԮǻêӠǷÉ',
                                                                            'ҾλώƼйɣŤçǆҔzψӷɸЧãƅτʓњÃ˰Ưөɥ҄ԐӉӎԝ',
                                                                            'ͺЊΆcӦȱԦ·ĶЭӮŸԂƴΝͿƍҐϒƓҥĞʯмǫ´ġЍˑϿ',
                                                                            'ƗȄEȮé\x85âӸîШєɒEŖɏӎƷàЗ\u0383;éϋƇӓϫƛͽƹƄ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'τѩ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѢћӤ˾үԬǇ\x82I˄ƽԘɔ\x8bΰ\x90ÌђǝˊжіʩȘȿ]ĩʏϴž',
                                                                            'ƘЩӊƔʽѷÔˌҊɹɹ҇ȆʳͲßА×ӄћƧȳԩȗ˞ͱϱ¨Þˬ',
                                                                            'ϿÊ\xa0İʗԙТǲέѤͱƯǟѺž¾Όԋ¦®ўŰӀʝþƍԭϠӾӚ',
                                                                            'ƍ˴ҳŅϡиƈƗ΅ъʴ¨τɮѬ˼ÓƝњЗ¸ϔКӬ;·˂ԑƞѺ',
                                                                            '\u0381ԐлĤ¿ӲˏπȗŤŠƗФƽWɧȫʨˑǶБɼԪŽӈǚÅɻĹY',
                                                                            'Ã\x85ԛϧГ&ΊӇάͰǍɁӿŃƍ|ʼЬқǈΓăϾÄѧ*ǁҲǀű',
                                                                            'ɸ˫\x85ѽӊΒğѶΰɶĆƷÚìŬӺĎΕХӻȶ\x91\x80ѩŀӝȲ˜ɕɃ',
                                                                            '\x8dé˄ԮϧȸωͻŠʬ=ɥ˘ĳʇӎŝҶǖȳIɼƆ}Gύ\x89ҨɭԂ',
                                                                            'xӽǫψĉȒIêȁɳӓ-ˏΠÞäЗŌ˻ξȉèΓο¹˶wДŬ΅',
                                                                            'ƸɗΔ4ѓBϙϨǾţ\x83ȣǾƔπҬχ͵qϭưȆИØәўƏʈ3ԥ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȚӯҜԞЗSUɦƼӷȲűʿʒĥ_Ӫҿͻ±ƦðǒȨàRiȨŜm',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӳŴȳӱԘ¢ӦӠщÀȨ²\x8eҬȢÌѿǚʄDϼӫѺѠԎƣ\x81ԄÔΧ',
                                                    },
                                    },
                            {
                                        'name': 'çӞÛʧĽƞŉȉk˅ћƑǵ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185521.337764:+0000',
                                                    },
                                    },
                            {
                                        'name': 'XӌǾƀΤѫ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɒ4ǏǝǼϘ·҅ɎŘ˚Ϊ-ȆUŪ4©ćŨψŦWԧ²\u0382ϙkΨЅ',
                                                                            '^Ƞʆ\u0378˦ΞÖ!ƧÞƚôbĿыԉɹɟ\xa0ҶԃҦб\u038bʴчƴɟ^ǵ',
                                                                            'ѧŵӽɳΙΙĞȄҎɔĦя\x8dƲŻШƇʨьʎ\u0379ӬɸÍȠSǞʍŸӦ',
                                                                            'ϳҋè˾ưЖ~ʂӮλѭ\u03a2ʐɀѿʕʈϱʺĨƅҔύČúӸεǹ\xa0q',
                                                                            'çÚӨ\x9fȴÒčҥΏæҕҼ\x9fԤˎšϞ˧ϿӚҐё\x9a8Ӻӡ˯ƴ˒҃',
                                                                            "ë\x89ǞuÏϹ{ɨӴЏʶīƢíӎʍƘʰƄÊěΑίµα΅ъ'ǡЪ",
                                                                            'ç˻ǢΗĖԎɇƺӀý˚ʘɲsϐǈMѬĒӌşϗƤǻħþϫаӚχ',
                                                                            'ǑӨy˺ƜɈпÀʟԘîƱӑšʝǹňʑφӌã6ҏƝѻϔ´FĹ˸',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'jŦɘş_үȡȝ\u038bǝȤьԦӃIЛʍ\x95˞bʵŏx',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 838488.1230762319,
                                                    },
                                    },
                            {
                                        'name': 'λβǫƊĖ#ɞM',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185521.720941:+0000',
                                                                            '20210910:185521.739245:+0000',
                                                                            '20210910:185521.756658:+0000',
                                                                            '20210910:185521.774159:+0000',
                                                                            '20210910:185521.792440:+0000',
                                                                            '20210910:185521.810700:+0000',
                                                                            '20210910:185521.828586:+0000',
                                                                            '20210910:185521.845014:+0000',
                                                                            '20210910:185521.861810:+0000',
                                                                            '20210910:185521.880277:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Š\xadȶͶĊӞҦŋǏʑҞк¸ϱёViӄҿêɶȷїЯˈЙѥĊɽʤ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2192755862500240748,
                                                    },
                                    },
                            {
                                        'name': '˾ɑĜ˒Őϫϧ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'kMǗԏӊĭŻƔŰóƨȝӊƕÉЀǨŧʎĐұuϏǅłʉӨҜЛ҂',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'pƄθѢȅѤөʞίłĮ9үĚЌƃ ғӼǵԙѡ҇',
                    'message': 'βʥʢЁĜ˪JȢӼΙũŁʩôъҴďƕˋҲ\x8aȁГж^äBΚŧÆ',
                    'arguments': [
                            {
                                        'name': 'šũˎή˚äŚΏώà϶ȏӾ\x8bІĂŧӖ\x88ʡ¸QѼŚΚˏ¹!Öʘ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5747763176501646295,
                                                    },
                                    },
                            {
                                        'name': '˟ŢƤѮĳRҤҶ˸ʋʘ\x97ϬȱѺƼǓÁ҄ãӖŗȌҚƪ§ωҪő',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185522.289317:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȔӭȻӊσǃIѳʒǻɇƣʃ˃ϴȔ?ˌ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '°üˉŘĐ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3034125015893767420,
                                                                            3191954525197843977,
                                                                            2877724928691034358,
                                                                            1397348088697325607,
                                                                            2934270024676130181,
                                                                            1078342425624993736,
                                                                            -2286373535546817238,
                                                                            -720233445883131703,
                                                                            -2680303538114185534,
                                                                            4589754491198089251,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȚŨ+ҌɥӃż8ƕȠʊƲƷė',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185522.691038:+0000',
                                                                            '20210910:185522.708444:+0000',
                                                                            '20210910:185522.725365:+0000',
                                                                            '20210910:185522.742119:+0000',
                                                                            '20210910:185522.759406:+0000',
                                                                            '20210910:185522.780635:+0000',
                                                                            '20210910:185522.803144:+0000',
                                                                            '20210910:185522.819378:+0000',
                                                                            '20210910:185522.835872:+0000',
                                                                            '20210910:185522.852359:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҍΈ˟ӿŖ˫νΙ~øɺkÓƴ\xa0r\x9bɎ˟ʨӷ±ʊϻФȖϘÉԭˎ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Μƨ˴Рϐ9σϋǜ²Ѹ\x92ϚŸǗ6ϓЎ˥ɇϧѴѭÝŝȚþвʱɦ',
                                                    },
                                    },
                            {
                                        'name': '¤˷ѲvͲѷǇϭʂӄѤʦǅӓ®Х˰ԖΓӬψiʼQƩˈˋѲŠѿ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˣҗҹʹɺӃfБ҄ӌŘ\x89ȳǾ҄Ëɂöɨқ҃Ð|ԚЂɀ¥Еíd',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -577602339568704633,
                                                                            126184255666723674,
                                                                            5872366810979963653,
                                                                            -5039654324347969747,
                                                                            7677247396541656323,
                                                                            -9149176710637321839,
                                                                            -2890738253158176018,
                                                                            -1919672081834980881,
                                                                            5532434148439858839,
                                                                            -7832979441302603315,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȇæɕǁqϙ\x85ɫZҗƦԋĪNʈǽΙžfǥǛȫθáƒϕѣӪ*ʳ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 446900180729732776,
                                                    },
                                    },
                            {
                                        'name': 'ƽ\x8dϭɒ˨ŹҸӸԉÇπϗýŽΛǜƀʟŞȯмηеѥ˜ȉӸʏӤЬ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΦĶÜſ˷ˋ҈ɋΟɚԇԖʍˁс~ӠӄİΆµϕ˦ʍԦūԋѨРԤ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҬМǱώό˝\x91ѹӅɯӲЈ\u038dҊǋȥЉњРɭɄʶўϛ\x88ґſ0ʞа',
                    'message': 'ӽĂ\x94Č˝ηοɥÿzɛǷΈѵӪͱėȔˁԅΧţƗďҍԭӍΧ\u03a2ƴ',
                    'arguments': [
                            {
                                        'name': 'ȄÁԈҾĸǦ-ҀȉОΚˊȝ$ȹďӍб<άэΨȑѼȯʴЈ3ҋĚ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'źѶƫϸìȮ˞ɨ͵ýƤϑҵҭɌɷЊԮҟ¨ЦϐҖJтύє\x92Ϫï',
                                                                            'ɺиѱŷgʓԮµâБщqϫÍ¦ƔƓǣŰ#ƍѡȠȯӣԤśåӞ;',
                                                                            'ӺŜ\x91ĸȀҿĆǣɇӭŁҚȇ\x94ЋƳðήνНŵΩϰмɠԬҵÂűù',
                                                                            'ʳƆ˹ʹǯҙȁҼȘrӾˍªPҟZҕǖЍϷȶʵŝŎұѩҷjλι',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x88ӨοÀ÷ĚԝѴѓѕʓѤ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'uзƵӯΏ˸ёΗɒȼιǶϜǵҡюìȞɟӒ£ŘϔĹΕƁЊъЕҁ',
                                                    },
                                    },
                            {
                                        'name': 'Ƅӆͻ҅\x80EʓʖӎmϯԛɛēÌͿĀЙ?',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185524.006164:+0000',
                                                    },
                                    },
                            {
                                        'name': 'nϒɱĆŁĵƝFƻˬ¢ŜĮԥԅϹУ>OҖp0҄ʂȋȧƇӲß»',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3002665819188714633,
                                                                            -6438000461173774250,
                                                                            -5427015593791227773,
                                                                            -3117968741014443091,
                                                                            6605561365981171021,
                                                                            -1083381755571675594,
                                                                            -4727202676346372787,
                                                                            5951588108959259484,
                                                                            5550721034071200877,
                                                                            -8825766017819824886,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƲǜƓ*ώ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɢ˔ПӪóȨÔ0ϢѕɚΙſßӎĸ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɧɇǰ˓\x80Ӗǖȶʽȭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185524.546748:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĠŷǂҽЍҘɍӠŢɮŀʌҘbȭîʫҍӈыǇ˞ϭƹPгЇƼɢѨ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            12234.183255340206,
                                                                            177665.0668773608,
                                                                            544318.6807075201,
                                                                            146185.6965672503,
                                                                            454395.4391752031,
                                                                            684103.732118758,
                                                                            237257.23851970967,
                                                                            700221.5386508813,
                                                                            465154.3117072297,
                                                                            523623.58316177456,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'īz$ϓǸƴɌӞ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӬÕӉΧӘЗŔȵЄʳҿʸ[яĕɈūöԬЭþӷƥɃѧ÷ʨ҂ӝҕ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ţңǌÒӚԥҦîԏя¿ϞFƓǓ\xa0ː×ȆˉwЙ¹*ԑц˸υȩƦ',
                    'message': 'ǴсУӯǤƘ˧Gӏø~ȞξˌӢђώŤŗԩԠnǴϊŬԄѽFȫÛ',
                    'arguments': [
                            {
                                        'name': 'ԂŚӚԖÇ\x8eʬӋ!ÈшʯÐĎкхŖɈʭѵʏ\x87yǋ¬ƈôύ҅T',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': "'ǘŬώ˟ƃǺ\x8fϗв¹ƻГbϸ=ƘҞҡǚü»Š©Ġʩԩӛԃđ",
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7308642914204441963,
                                                    },
                                    },
                            {
                                        'name': 'ºӊqԗȩЩğǀ˱ЎӤɠƩɅЂʃ҇әʈ!Ǿ¡ɷˆȾúǊÓʍ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "ӍТǏ~ԓíԩ'ЉѣƾӦǌoqӜ÷ҵ5śΐǶǘǱȗӟӪԥGԓ",
                                                    },
                                    },
                            {
                                        'name': '˪й',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185525.673309:+0000',
                                                    },
                                    },
                            {
                                        'name': 'юƅР˛Ҡ0ԑąӤµͰΞϣЏϩɉǈѫΙџ^ɪӧʍóΤŞǨYҴ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185525.750762:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ԕ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1719599597660085317,
                                                                            5697993153813770834,
                                                                            3298309294178340866,
                                                                            6281333072749721368,
                                                                            -7899830917911395643,
                                                                            -1859671760103371268,
                                                                            -2820611495549866013,
                                                                            -7572779757211603430,
                                                                            7641837679344383922,
                                                                            -3008047579243428866,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¢Ͱ\x99',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
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
                                        'name': 'RʟϜƽԏ\u038dñ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ȟ΄ѪOσŽ\x97·țКͳИӡЗȿɋʗӣӻіǖ˨ҢǑĖӖOѕĈѶ',
                                                                            'xˆǳƢˣǏϜё\u038b˙ұʣҴ¹cԑ0ʉÿ`ѡ˫͵\x92ŵH\x99ɄұҰ',
                                                                            'ͿnʴƼƍS¡\x88xѩÜΒӶƵƚìíҥUӐҎ6ɚВǷǺʂƢˬʨ',
                                                                            'ЍȹľҔËɀɻϠǁʸìʞːÈ¢˺·ЂҶтl˨\u0379ȍļɽԋȍəԉ',
                                                                            'ǷҷȨɃ˓RˤǁΙҙȴϴ˱ЏЙµԧɷӝӀȽĢͶǼЎ\x80Ҝȉ£\x90',
                                                                            'Ȥ9ɤȁ\x8cӵҖӱΰā\x9aÄєұǅ¥ÁҰΟΉěǻ®pûӇѨɋɌƮ',
                                                                            '\x82ȀЇĪrȰÄŇϓÒƏЅѸЋƳеXɔϮл8ҙȱôɺŮˢԐˆȠ',
                                                                            'Ӈõіʤŀωǟψi˅ʌӔĢˮʌ\u0381˦҇ɁEȘѦπ˷ϪFά×ê˥',
                                                                            '4˵ӉНɒʢѤǻͿӺʚ¸ƶʽƏɴɄѲʒԠʀ˹íŏk\xadąźŧű',
                                                                            'ŧԒħɀӻԁɥԎʐżӲíʕɔԃԝԦαѣϡʩȻћÓƄĲʨάУŮ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɑŹԐʮǣŠǡԍ"˘ЅĘԠЛ\x8eȒǁҢǩȚЇʞʏ\x8fчӡ˽´\u03a2ȸ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5155675884271855271,
                                                                            -1662912846823269876,
                                                                            5122859842717308429,
                                                                            4953639778046042947,
                                                                            -8979045062483542717,
                                                                            2750099151684040173,
                                                                            8734975567493197227,
                                                                            1711072742614299989,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƮЃ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185528.620928:+0000',
                                                                            '20210910:185528.640515:+0000',
                                                                            '20210910:185528.659898:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ğ7ǆϢ\x9ciƶкRӚшǜқţμƶχ3Ûƌϭďӫȩ˽ȬʓϨɣϻ',
                    'message': 'ҡ©ƫɵΕөſ)òNҌԂƄǍ´ϜƬğŅ§ԟʄӣЛҥЀҚȊ+ş',
                    'arguments': [
                            {
                                        'name': '˂ҥΕƷǐқУЪӃŻĊĬ\u0380Ҵ.åϓÑԫɾɁɀѭ9ˎ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŇҫêӹъҔαцϖ?ȂбŸ҄cşϴɖж˳ǶѝȠ˼åʮ"lςȫ',
                                                                            'ӵéǜћЊѐȳҪȥģϳӏƳ·ėΓƌŝɐԂ\x9aԋėWɞDǇ¨ϷŬ',
                                                                            '¶ΥĝѿŶǳ8˔ĤĭæǾѳӨÞшςŎʑʆęƲıìӬɏЛǧҔЫ',
                                                                            'àԭЖéϰӇƴԚŵуȹʣǯȘĈĞʝȺˋ΅ĳΣɁō\xa0RƺČʉż',
                                                                            "ūĪΔӘЄ[˱Ѕș-Үьǝ\xa0ʵ'ԋFі҇ʛȒȆĺƒћșɲӌ?",
                                                                            'p\u038bĠϙӀͺҷҘϻˤΣΣһŐ%ȄʐϒҋŵʌΤЉǷϟ˖˥ҋŐƖ',
                                                                            '˔\x96ŌǫҚzQΧѕЄȫeaĔʣάӡU¦ҮҡʕƭϽĶɸЂӉɯҥ',
                                                                            '˹ÄǢƦϸǡŚк\x93ϲˇÒӊäӆÊеǆ˼ʼˤ\x94ŵԦɱsӺőҠӚ',
                                                                            'ǣǧʝԍǟ҈ŖǖҒЖΌћǢɍǣȧӐ˓Æ\x8bϺƸκuƭӫѫΉϝΉ',
                                                                            'ĻȦɋFȂʢͶИǠňĦÃ\x99ԩƸΣȐƧ˰\xadʥəçœψS¬˭Ґˢ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϣ҇лɿ˭ӜɫүΎƟϝďƃӒşϏ+ŌԋŒȸȿȑČŶҁ˃\x98Ϋŧ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185529.092111:+0000',
                                                                            '20210910:185529.108207:+0000',
                                                                            '20210910:185529.124823:+0000',
                                                                            '20210910:185529.150120:+0000',
                                                                            '20210910:185529.168296:+0000',
                                                                            '20210910:185529.188947:+0000',
                                                                            '20210910:185529.208689:+0000',
                                                                            '20210910:185529.229556:+0000',
                                                                            '20210910:185529.250491:+0000',
                                                                            '20210910:185529.269743:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȗțƂÍśԜʡƦӃƭєСκJ˙ʎ!ԏҞΕʱгӎĭσή_ΈΛ҃',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            609769.8294719581,
                                                                            549677.5301117669,
                                                                            625158.0659837786,
                                                                            611212.153763343,
                                                                            240752.11981051153,
                                                                            288431.81415627326,
                                                                            687298.4094260726,
                                                                            218333.02781356237,
                                                                            773331.5006133507,
                                                                            -49284.95540058632,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǂZпʗŵȐƧ2ǹ˖ƵӳԠ϶͵ɠɮ\u0382',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 59739.57275712889,
                                                    },
                                    },
                            {
                                        'name': 'ҺιƏϜνşʌӜѫŭ\x9bÙ6˛ʈƃŁȶĔə',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8083410851084824614,
                                                    },
                                    },
                            {
                                        'name': 'юήǂÚϥƕɧȶΔȇɍ¯ĶτςѿˇªԇҀŐЬŚʝǾùĆӯĠҔ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɾљȨӷÊңοŰCϏƒɃʋnśȓ˅ˁćͼƓċϓӵ!ЅӖĒʽӗ',
                                                                            'ˈҫ\u0382ĭĠπƔ˵ЂћϲřѰΡĮЄȤјϸҀŘǳ\u0381ѝĢɵΎŧɇҾ',
                                                                            'ˣԍϠûҒЍ˽1ňʘëcѕǽƢ?əӊȦҽПƜԋӑҨӃηԔλć',
                                                                            'ˌϻϏƥÑΏÀЁŜ{ɡФԔƖҪȭ:ϳɰNBЪ§ɯȐɷԈƼϘӵ',
                                                                            'ҔǰɹȌʪЊ\x99ΐůǚ\x9aόҶƞųȄ˹ƨȤžΏèӌɡЀhәԚđC',
                                                                            'ьȮϜŏҶĩϸЩʑ˟ȍŌԮϟȠӟ˻ӮӏʋɧˮjσΡh϶ʦϮɐ',
                                                                            'ЎŸ7ȅα@ѸϘѱƲўŴϴeƶ\x9eðǌƷЇ¨uцèɠƣҸÉǳΎ',
                                                                            'ƍ_ʇɭʱƕɼѺ˪ǐʱ4ŜԚΟȶψ˦ˏϸúѸȨǷЧәѲɦЧԟ',
                                                                            'ŞғӼʃǫØͶԀǗӐƥɞ˘ԭԬʨʞ˃ԒƬӹҰȌΜɐҴĩɀĎɤ',
                                                                            '\x87ȲѸԬʄ˒jˇįýœЦɯʧψǒ¶ҞĞtĚüƐʟ˼\x85ŷϚ\x80і',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΗӕɞĚәʟȵʞ¹үіͱƔřѪ©ҹƑǴğĂ˄ʽɠɝB8ѕӾԇ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 575313.9702660468,
                                                    },
                                    },
                            {
                                        'name': '\x9bғ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185530.162413:+0000',
                                                                            '20210910:185530.180054:+0000',
                                                                            '20210910:185530.197630:+0000',
                                                                            '20210910:185530.220810:+0000',
                                                                            '20210910:185530.242408:+0000',
                                                                            '20210910:185530.262807:+0000',
                                                                            '20210910:185530.283143:+0000',
                                                                            '20210910:185530.305072:+0000',
                                                                            '20210910:185530.323785:+0000',
                                                                            '20210910:185530.341020:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĄÈ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': 'ҒіҾô=qʶȐƅӘȘΛυӸұʪųϡӴҔԬͺĸͲϙϰӅėѾȹ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ГbѓƩʭќķͿāҐ;ȚY=íƏ˓åкȪƊɝӴȒΥнː˫ѡγ',
                    'message': 'ӿѓÜӭʟǞǝGθˑþ˟қ^ÞǊѨСȈϕǨɪȹĐķщɗtLԀ',
                    'arguments': [
                            {
                                        'name': '˒ҙȏ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185530.871187:+0000',
                                                                            '20210910:185530.898090:+0000',
                                                                            '20210910:185530.925935:+0000',
                                                                            '20210910:185530.954170:+0000',
                                                                            '20210910:185530.983110:+0000',
                                                                            '20210910:185531.007425:+0000',
                                                                            '20210910:185531.027816:+0000',
                                                                            '20210910:185531.056703:+0000',
                                                                            '20210910:185531.077742:+0000',
                                                                            '20210910:185531.101205:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¯ԣŃȲŎԤPõͺЇΥʂЊ\x88ΘԢçáʭїӇȥŵƟИˎʤԄҳÔ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 't˖ԙ«',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7447907251614330938,
                                                    },
                                    },
                            {
                                        'name': 'мСˡЗӗЂơƬď\x92҉\u038bԄӰù;ͺɡґjɪʡȏȐ\xadӝŜŸ',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҐƸûϥ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            166727.4263889275,
                                                                            528598.5431295699,
                                                                            575839.1086147113,
                                                                            166589.27001878875,
                                                                            391859.6235428084,
                                                                            774537.3300635413,
                                                                            205944.0224802738,
                                                                            611198.4790769191,
                                                                            286195.6354314337,
                                                                            359060.7431688777,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԁ˓ёϺƥ\u0381Ț2\u0382яǷ˶т\x8fȔLΆӕȃͽЖƢҰʘǝϰϮ˝Ԑɣ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ĉ˙ѲуӗæπŨɐʉїοʨǠ҈ЦĹϖźľɯɼӱŤΖɶКѠˬɅ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ϸʂ¹ҏ҂iӉԧŨƦΈoӷΫƙƧ¡ԓɍҡϻкŘƆҿɋˎХ˩Ӝ',
                    'message': 'ӵƷӨs³ƲÒӍУʘßȡСįвſ>҃ςƤǴѭȜ\x81ǜÞɟĘǥȅ',
                    'arguments': [
                            {
                                        'name': 'çҚӒƚуΖBŎȝÞпʕÉΎжӶғȌі®¹ĝӴºȌɴɻũҮǊ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -27572.08688813477,
                                                                            697618.8235884218,
                                                                            210114.22299178614,
                                                                            614530.3360382926,
                                                                            213961.3800818362,
                                                                            413314.62455288274,
                                                                            458111.56862371136,
                                                                            713917.1053154388,
                                                                            -48239.00529932552,
                                                                            547447.6389261655,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'гǍŕ%˶эȸ\x95ӁƉƌˉԮогп&ȯ˪',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1624932285296014129,
                                                                            7925909290710745567,
                                                                            622503775698274771,
                                                                            -6361599261170146996,
                                                                            -1990758646858889893,
                                                                            1438838340869451139,
                                                                            -6582119563900283192,
                                                                            1966573528686370407,
                                                                            2476834899120207098,
                                                                            -8098462575451699031,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˬxě\xadԓҠǭʶȑӉтǣ\x9bŖǃƚ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŇΗ\x96ӷΫɱƩʉΏ\x82ïРеǒ˩ʷѢϞĊͳΤϼϏɈĞƫсԛ\x94%',
                                                                            'ȉÔʪ˸ʗơӌƮçӪĠҍǢҭǄǪČŷЊ҂ίϷϨУӌĴҾƗˣȴ',
                                                                            'ǪʂҨůɬʍȡэԠԓїҘǽʿˍ¤ЀĨȆύǫӹˍϴǮӌѧԊġԫ',
                                                                            'ɗΠҊęӦʳ˙κђǧ˧ːѳƄԚϠ\x8f˪΅\x9e.ǛőόӁsƋӟ˰М',
                                                                            'ö\u03a2\x85Њљƫ˯˱|Ǹˍːԕɣƾ?ɿҷԟӕƐǭLҠ\x9aЉƱƻԖŪ',
                                                                            'ĕϱ>цőƝҵǰ£ńĦȈŇʃţΨĄтǃʏӇ2ìџɗý΅өŭK',
                                                                            'B3Ťƪ\x8b҇\x8e³ǻ\x7fåˤƝөеȚźº/АԆ\u038b˴ϞÖџ\x8fʝИ˱',
                                                                            'ζԑxÜBˏɴŇάqϘɲƲԨƎѻǍϮɀʕĖÍN:ĭӍɁĎ2ҧ',
                                                                            'ρёχҶӢ¥Ҽ˜ÐñĸÇɇҲʟ\u0382Ŗ+ËΦʛҿҭƒњȒɑȾĦǃ',
                                                                            '\x88пϸFŅѐƲFɬҼˤıʜǣǷƭԄ҄\x86сŲCҼέĽκҶ\x9eђÐ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'цґȍӭʂÆ\u0380=ԄǄ϶Ȃʸϡ\x91ʵġҐ˙ÇҋӑΗȆȎϝ˒',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ИΞѼ˷ȟɷ:ҊŁӆ\x8fϚʅÒ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            335812.60204901965,
                                                                            517716.29416214896,
                                                                            171741.14588998776,
                                                                            787068.5581013617,
                                                                            127516.68009914266,
                                                                            -24988.82978227394,
                                                                            499183.37044503645,
                                                                            623854.371408842,
                                                                            416517.32300874573,
                                                                            -15845.972563726245,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƾ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1416610900398671080,
                                                    },
                                    },
                            {
                                        'name': 'ʡƨèȍʃͶGǥҺÈ\\ӷģǌŉãΓɊӮӹɓȟfϕBҎҔ\x81ќž',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'IϠɈĒİӸΏƱЋҖʠĖíαҶƇЫӅ©ˑÀφӋўϩӸȡϲʶʠ',
                                                                            'ʧ¶Êӗƭʇă\x98ȍҵǚǭö҂+ŜѱƀˁӲȹБćЛ¯ԒŸQҟʝ',
                                                                            'ʖùҰΠҞϽў}˄˘©]ƈЭΫʟƪȃ˞Ц\x96ъЅˠýЧgƨңq',
                                                                            'ӡұԩʾ|σϽƈǌϢËԁêϏuȕ˓ƃĸʙϖ˼ɵƕƥǓāʘӟ˾',
                                                                            'ˇԈͳɠҀѨɤώˀhӉȐ¬ʌԜҦɒ%ѮȬәɭχӚǀɔzʠ¼˹',
                                                                            'ФʆĠŃҏӱ\x9dʅΖŲҙ¾Pηʐ¿ȧӓȔÉƯȝwкJϮΈп:°',
                                                                            'ǽϜŃҋǝɂɪЩϧö\x8abǃű»ϟ˟ҶǤԕŮҡǹȹӍĸǩ£Ĉѧ',
                                                                            'ƃȷŢЗӯΚKшÁԎøЏì\x82ƼФʾɝŬ0ҀÛˡϋãȕɼҷŀƙ',
                                                                            'жü»˹ċēгҐtƴƦӬƼЫ\x92\x81ϨӃԌȇλʹĉ6ɥΧʬțôΰ',
                                                                            'ĨϳMҠѻƞԑłĴҍǁԦӹϥδ7ÞϩǎЊpюƆǥȓͿɴƱBԘ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҩNřȠĘɝŶˋЯβɛӺƬ´ƼʙYȭȬʉӍZ\x9fĞēȀσӶƑa',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185533.798165:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȁӚӜԅ\x9bΖԬĠϮę҄ȂÆӅQϽäÔĬŨº+ʞĶ\x7fτф·ҪƝ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            28470.223461096786,
                                                                            899467.4861994527,
                                                                            720331.938040219,
                                                                            721072.0005019072,
                                                                            550048.0295463596,
                                                                            138476.62389738974,
                                                                            205774.89570822008,
                                                                            379776.83099598554,
                                                                            109871.88500192453,
                                                                            929498.6465594854,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'šɴжEϷѷԉɎƳƻεϩ҄ɴȖĠђğɳѶ¹ǄɆĄ\x8cȜsτĆˈ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            342222.2689637734,
                                                                            945114.4062394792,
                                                                            178112.08443455893,
                                                                            268745.0437745709,
                                                                            669030.344199743,
                                                                            43219.58641872922,
                                                                            510273.61735503154,
                                                                            655568.1988359991,
                                                                            -90496.24293554355,
                                                                            618444.2508482661,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x80Ɖ!όgλσŚ&ԅгʋɾ',
                    'message': 'ӌηáňώѼf÷ɮπƻćћҔѕǼԈ˭´Cкõ\xa0ӀЦЖѴǬ˙ˌ',
                    'arguments': [
                            {
                                        'name': 'ňNϲòφ˥YħҳrЧИtїťϫöƔ΄ԓ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҹԜèǪЅˮħʊǛ˓φѱǪ\x9fԃџíԁǇÍıΩÕтɥӂǮԏȺ˷',
                                                                            'ʎʓ˒ǌцŻЖҪ˵ӅРɠŹѝƗӓŞƮÝɔ˩c҆ĿӸ¨Āҹʝβ',
                                                                            '˳ǟŁbΛ҂ʩӄӖƐđњɛўϞğʾӏϻȋ7С:ώǼϹɱȌǂǀ',
                                                                            '%ȴǘΡƎΉѕλʲʖʱ\xa0ѠіԛӞƔ\xadѽĄó\x99¡ӉȅкˈӜŷʤ',
                                                                            'nǘɬìҹɭҵɭɣʙàϛаǞƕǣĂʲсyœѥŖӖĸȤϒU\u0380Ќ',
                                                                            "ӆƜѱΨȩÖʔȭȣǼԤӃ¦ˠGҤϣϧƫȋԏθѧĖýӪʛ\u0382ŵ'",
                                                                            'ɫƥ=ʕøѣшӕӤњҖҠŗғ\u0379Ʊʼ<ūƎƧȡ¹ӋĠ\x85ÒȐİq',
                                                                            'Ԑ=ѵŋ˻3óŚӺӜԙˌƃȻƗȒű¾ɁͽžăǞƏċԓʚҸφЂ',
                                                                            'фɘKʫȍʂŶχǳӉψӣͿЦҾôwЅгДđѴύɳ˼ήӿJĲʔ',
                                                                            'ҋƀɓЉԎҔ-ʜɛ\xa0Ƙѿ΅ʽԆΪ˰n$ʮϚwʭȂѻ˙ԌкȽΦ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ң\u03837ťɝԬ˽\x9eʭ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĭѰӨøϏѡBȎѴƺԙψǯϩÊ˪ƮрŞЁɂЏ\x89ȗƳԄΆʡ\x99β',
                                                    },
                                    },
                            {
                                        'name': 'ρéωƖžtʌ˭˭q±ġǜΥȠïσŜ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ϊӡπ@ԪгʛӕɮсΙ˼ƧΞƩɑǆ?ұѸ\x90ʃǘͿӷ\x8f˓²Ȱλ',
                                                                            'шƛªҡƦ¼Sàа>ˤЊΔŪ\u038bҝòȵʈÎѤ%ϘʍϙфɈţҍη',
                                                                            'ȫȆˉԡΩӌćßØøɑζʤ\x81ͼНȱɱʒθӴʵʺθ¨\x8eːčħҶ',
                                                                            'Ӗ6ͶǒăԨŵƾoͽǾļǇлЦčӻďԌіˣӼӧ˻ıƢŶƔþԕ',
                                                                            'ȜϼǈД ѾЅ˺ЮԐÎƫøМƝɟӏȫҖƑʕΫƶґvƭϯƿɀԙ',
                                                                            'ÈыƥɰԓͺĩœɋϔцƲҶԫӑӟɄeȯĉʉӰōȌ҈Θκ\x81ѭǊ',
                                                                            'ʧҒʲҁµӴĒáŠʣ9ŰnέӀҏĊΚUƬԈϪϨҶ_ӿҚŽ˻ч',
                                                                            'шѫˮaҷʹ¡ϳϏaβƨď\x87Ͻ¨ǞԧҙȈʔ\x90Řāīсu(ŮΧ',
                                                                            '.ЬʨҼŧӭɷЎ\u0380хӝʟϫŸҊïţ\x95[ϓǞtӚͻɄԘќȺӹϭ',
                                                                            'RзжȃĦƾƴǽΣȮ¯ĒÃ\x83жСȕ\x9d\x9eΙ˫ŁҿǕѩѯVЛԛ˕',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '½ǃʗƫƇ',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'QǡЬͱԜɃʫԦ\x94',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʔƗҸŴ\x80˳Ɲҷːǿʮ\x86јˏVĕÑѴȎÁńü҆ВϗƏӚʝɉǡ',
                                                    },
                                    },
                            {
                                        'name': 'ȲϛǇƮľŔƇЖкӿ˒ο',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĦöәǵʮηѷĨuƢԋÈѮЪƭĥ:ѺõϐŤăÍҧƨϕʆɃơҫ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185535.598433:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x85ϪҰԕпʽ˝б´Ѯɮʘӽ\x8eǟϙ\xa0±Őõģʩȩ˘',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ͶĜˆāĿͺȖϠ\xa0щΘ¹ҿȨɦύӠХūˤȢԜįǝviЫĲɱϹ',
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
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'fAŋҤÚȫũГλˎŐ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
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
                        ],
                },
                {
                    'catalog': 'ΖțԋƼªʲTɍԉҁԬȋȡΜʱѤʂ©нʀӢИǅŗõϮҕҒӎù',
                    'message': 'ȿȇȑŞιӋ÷Ȕǌ˯ɡȚ[Ú`ϡǘâȍʲƴЄȁkЅ˯ӽЍʷӋ',
                    'arguments': [
                            {
                                        'name': '§Ρǂęʹ҃ϖŐ¢ԗɵӌ%һѪƖʒɻ·©ÂƱѱ·Ͱʰύ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185536.406062:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĆʌΝżͼЫЪ˴υҖԬ˴˦ƿ˘ϒǖʆ8Mʛ*ҍ\x82ԔVʼoϮ\x8c',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǭȁʾΦͶб6ŊɽǂȔɳ˰ĥ͵Љ\x92мѻЭϷ\x9aϰӾ\x93҄ϷµǺѓ',
                                                    },
                                    },
                            {
                                        'name': 'ȓҧʞώ˪ǫ҄˯¹Áŗ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɊЊңʄ9ǆο˔ϊͳ;ІϙŤάˬ\x98ԠđļʋȯԐYʖǋÒÞ.ǹ',
                                                                            'ўԜѕϳ%ЅΑɂňˣŌˈеƏˀļȈˡΠҾëʪȜR\x82ҀɭϹȬ˔',
                                                                            'ԖQLĚǎʇѠ^X\xadѩ|\x85ʅʨ~ɐѢͿЮάџηəԓԁӫЏ\x86ʜ',
                                                                            'ñZȮ¤ĜӖŵʽИóĬCґ-ҌǶƝˤĆ˵˙ԘbΜȂ\u0383҅\x98Ŷ\x8a',
                                                                            'ʀ\u0380ȍɒ˦ЀҕǬʯҚ\x9fΚ"ӠʜƏƃѹŸʏƍʻҕҋǾ˄\x8dљӯѢ',
                                                                            'ƴӲƝѠʕʸɸήЍƓ\x91ē¼Ĕ΄҆ʓɁӄ-ΐВŦʑČΜɹȦ\x8d˔',
                                                                            'ţéɔҼUʝΡҶЁԊʧUӲě[dԞ\u0383ӈȢRƁ!ƟĖΩǢѻӻρ',
                                                                            '$ëҚ˗ӣmˬˉSүȸÏ˚˳ͽ˼Ƒǚȥ\x9bĄбǮĸƄԦҁgæý',
                                                                            'ɔŝƲөŬхѪħˍђ«ÖĉӞňĽȰäҶӪŨʽŽϙȒˮѧŅĸҠ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƳǬɾ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 295238593886470510,
                                                    },
                                    },
                            {
                                        'name': 'ʸĳĴ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2302164847204847892,
                                                    },
                                    },
                            {
                                        'name': 'Ƣĺp Ӧяˊ^ӒʯŐȆő@ΖӫưÐҶʵ˘ӦñcħXʠŇNŐ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'гӜҘŭIʎ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4848719037573216566,
                                                    },
                                    },
                            {
                                        'name': 'ǷȾҁŧǡƕõƯʥсˬɮʰɄҐұǍń˝ҋ\u038d\x81ӯШɽřԥӧˁ\u038b',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185537.153884:+0000',
                                                    },
                                    },
                            {
                                        'name': '²ǀоȽӿҡƺВkJџΊĥɣƠǆƅşҊǧ\x9fǖЛɊţƗЅϙӎȔ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            113211.06172001603,
                                                                            912149.0998727683,
                                                                            511797.71014754835,
                                                                            152654.04143581685,
                                                                            269757.8114062995,
                                                                            439752.4170856611,
                                                                            291300.4862934455,
                                                                            864464.3925145062,
                                                                            607014.624227117,
                                                                            -66107.29866535813,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ρɓɫ҉ːʂϏɰϪǋѓƨӔŵϮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185537.495056:+0000',
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
                    'catalog': '\x84%',
                    'message': 'Ǵ',
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
            'identifier': "ƔÅИɎ\x87ФȗѻϔҢȢҙĿĀԋҾԕґǯԂɚӏĹ\x91!'à¿Ūҭ",
            'categories': [
                'network',
                'configuration',
                'invalid-user-action',
                'file',
                'os',
                'file',
                'os',
                'internal',
                'network',
                'internal',
            ],
            'source': 'ĞʙӦǬȯɕŲŖɉ7ѷԛϘSĂ˗Δȃи$ŶԢΆƦΗӇѺȫьд',
            'messages': [
                {
                    'catalog': 'FˁιǙЪ\x96\x84ŊԐ˱\x9aԇiƚʴйƳϽÓ΄˾ˬϤӞɶЏȏфɔA',
                    'message': 'ƎˋϳϼɸһΪKȞ§Ŧ;ĦǠʊҲƽĹċȅаƎŨɐƓĆԛˉƾѻ',
                    'arguments': [
                            {
                                        'name': 'ӼŵAԓ¬ӴϜűéЏʾ\x91˼ʔÎԑϭͿϫЫ˵ҜȁȤųΣŕȲÓÈ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8180302434329135235,
                                                    },
                                    },
                            {
                                        'name': '¨ҧϛˏҐ`ӜѵƀԛΑСԡGӉ\x90ņ\u03a2ȣEҕ@£ζҦ˽ҬåМȀ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            611528.3451492884,
                                                                            864692.8997115324,
                                                                            790872.9928961319,
                                                                            617500.7152383644,
                                                                            189993.54784091766,
                                                                            526222.3333196526,
                                                                            768161.5115911867,
                                                                            571343.8097094264,
                                                                            480896.8163728076,
                                                                            596929.4406845057,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӆ¥ǘеϫʥ˝ɮȝɪƺѾӥȗӤγĬ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185553.561393:+0000',
                                                                            '20210910:185553.577833:+0000',
                                                                            '20210910:185553.594941:+0000',
                                                                            '20210910:185553.613815:+0000',
                                                                            '20210910:185553.630838:+0000',
                                                                            '20210910:185553.647023:+0000',
                                                                            '20210910:185553.665051:+0000',
                                                                            '20210910:185553.681942:+0000',
                                                                            '20210910:185553.702502:+0000',
                                                                            '20210910:185553.723615:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȞӞΉ\u03a2ѳƶʦķԨȸБӒżŒ¦ɀŭҋîʧȴʮȧԑƻÛӡʖßŧ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            37521883462700157,
                                                                            -3264625902380212044,
                                                                            -6914515502186221999,
                                                                            736531185710852673,
                                                                            3593323795115488500,
                                                                            -1674077824224739929,
                                                                            7571188563975830415,
                                                                            3231920669739274115,
                                                                            -1318737688007797360,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȨƀûĀѪӦ°Ø/ҚæӵŎ\x8c',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'oͺр\u0382Ԑӏ^:рʶɂшƆeʾ\x86ԫɊΨÈҍ\u0381ςǛ%ȋɐXҍɡ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x84ȬϗÔЭӘǨΦŞÃƃͻȨÊя¹ʣɧǠȻʹĐĪΞUͼХҧѬʝ',
                                                                            'өͻѪӍɉŦԋіɃňШћ\x9d\x85ɼĤύ\x96ʲϏQθ\x8cƲǣɛԮ\u0379ǝ¡',
                                                                            '˟·ȵʋӹ^ŭĲҤĬψԙϗȤѬһ˝Χ\x9eҜζƫƕƊůɊ˳η¾ƣ',
                                                                            'ɯÙ¦ȿΩȉʺʮүԖǡǽǶ¶Ŕ\u038b¿WǍѣуIĥŨɻėìҜO\u0380',
                                                                            'ҳɃҦ©ǔȡЖҳËҁԠĆз\x9bОǅò®ԈʆƫŏԠʿȚҙ\x88ěκπ',
                                                                            'ʁĭǼĐɴÄέőϞ˺Ƶrͱ¸Ø˖ьӛƳɀPX΅Ǯʀɧ΄skǫ',
                                                                            'ЎɻkҽŻӗŬ˝ΊɝũŰ®ŤԢӠӟҵßϲΆǉкқӈǌǑĹҶɽ',
                                                                            'ΡŖЂɸʮńԀ,ǘʖÅʖлǞǮΌр}хĵ§ɄΔƵǇ\x99τҁӈ)',
                                                                            'îʻƬȠΠ¾ϧϜŗ¦ВɠЉʦҵΉ\x98˵Ԝʴ;ϋƞόɩй°ñǪϓ',
                                                                            'Ҵ\x87ƃħň>˕ǲÌƘї\u0381ӭδŷÈ˼ϼУåƠʩ˸\x94˾ҐĥǳҾ,',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʚǑ×бЫȟŉԄĵɓШċΦ©åЃΞʅ\x95ΆҢhǌšÌԌ¹ё',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҬƮĈΫ\x8fɦÄȇԟ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4058182865212962749,
                                                                            -4652641489374948379,
                                                                            3649349578105140571,
                                                                            3630743932741359851,
                                                                            -1260074705194143704,
                                                                            -5608949505036393122,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʹơǯɰ˸ƂÝcǣϒ<ŢϩƷΪɕ¾9·ЕàϳԬƯȵϛƽʢѧȔ',
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
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'KɫȔêѢ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 797203727009057707,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ÖҌ;ѕϴƔh³ɌˀϹˢ\x94ĜҶôͷưЫ¥FщȎȦɛʝʙ˷ɜӗ',
                    'message': "нӖʶԣɗ˅Ɨ'ӯÌÅԩВśǧάҾЕɕӕϭŞĂ˦Э+Õ˼ĩǜ",
                    'arguments': [
                            {
                                        'name': 'Ҿſşǫʊ\x7fʼúӏǐɈǼʥȱφӰǱʩɐþѹöŝӈԎKԗαӎË',
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
                                        'name': 'ĺȍϙĎѵ3Ԯϯʹɞ˰ʑдƮɈ@ίͲɸҘʌʖßʎ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 954429.6779061712,
                                                    },
                                    },
                            {
                                        'name': 'ӑ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 12326.81934478182,
                                                    },
                                    },
                            {
                                        'name': 'ɑǄǮҊɍȌԋǩ2Ώɿӏ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185556.031551:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɐ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɍ΄ĕ&ЮɞѯǭťŉɋȀ\x89¦À¦\x9dѰ¬ŤńȹȚӾґ ԉ\xadʢҳ',
                                                    },
                                    },
                            {
                                        'name': 'ĚôˆƞƩȓČŹĠǢӴͻη˱ϒñÖˑŢʧЇӖʍϾӈĪʽΘҵƃ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 929432.8593543365,
                                                    },
                                    },
                            {
                                        'name': 'ԦҫǸΜƬǤ$ȃІɰL\x83ӬĆϝ˺Ŷ-ɰǋΨNҚʩǅʊΠҩ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8420132087230235134,
                                                    },
                                    },
                            {
                                        'name': 'ƯʆƎȂѻϪ˪ˌǘИƧJϢʛǰǢȲɡAғӴƎIɔЈèNgҖҎ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            271565.94282094244,
                                                                            391443.1491932344,
                                                                            -11621.777369205854,
                                                                            -94733.29922430002,
                                                                            278590.7109099889,
                                                                            896842.6047681955,
                                                                            344875.36059428786,
                                                                            968631.406817653,
                                                                            142463.70046147238,
                                                                            552255.9194055733,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0379ԢƮЭюʑÌЕǜɫϵπʛŐǌӡʖȇiγ\x8c',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɳƭһ҉ͲѹҌ˴˓ϺϨӡˉӕƠƲѡˢЯͽvÙɦ\x9cΕ¿Ϸҽʾs',
                                                    },
                                    },
                            {
                                        'name': 'ʂʝμяпǬȍʚ\x94НʸǃҕϞ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǥƧωţμїΞhȵЋNƃƲ:ӻƿďĬŷʼ¢ĭѽʜǯ˧ÝтdĽ',
                    'message': '\x8fɩCɺԛʴʁĜΜӢ;Ӵȳ҈×ϠȮӥ5ѝ˅\x93ҏðV҂ɔǉ5\u0379',
                    'arguments': [
                            {
                                        'name': '˕ΌÅȂʽŧ\x84 ˉыÍʩ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185557.191047:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʠҶҁ¿ĢǥˬÆƵÍ˟ϫƋÊ\x88Íφ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ь¸ԛƸƫŉǩˑϱ˻ʲΛZΙŲӞĲ˕ͻҳɒ^ӣъŊëŏÊϛ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĉƎ!ɍʘƴɥˎ҉FˌˀƶƟТČӿæǅ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ґŮʏɒsɞƄ\x8eҺЯчИϯԄҾ\u0378ǩÎҁ¦ďǮνɩ»3P˰ˍʏ',
                                                    },
                                    },
                            {
                                        'name': 'ɧœʁϒӖσ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185557.697860:+0000',
                                                                            '20210910:185557.715824:+0000',
                                                                            '20210910:185557.733495:+0000',
                                                                            '20210910:185557.751461:+0000',
                                                                            '20210910:185557.768797:+0000',
                                                                            '20210910:185557.786966:+0000',
                                                                            '20210910:185557.809490:+0000',
                                                                            '20210910:185557.836735:+0000',
                                                                            '20210910:185557.876893:+0000',
                                                                            '20210910:185557.905751:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʣǲŸȬˣӲƹ\x8búˀǱŎƄˋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185558.023396:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɞКѭɳĊôϋſϗ\u0380ʉǄħ\x80ǈϊ˼ӃМýəˑÏ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1299711664878005936,
                                                    },
                                    },
                            {
                                        'name': 'ѭˤ˜ɟȣӅ2ˊϡ˶ĄьҀoҖŸѦЎƬȚƐɏϙɭΰù',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185558.278713:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɘʈѠҶ¯ǨŮħ˺ȂӗʢГɪ͵ȐӇҮĿҸČԆŨš˼ɯY',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4996331288942893182,
                                                                            7683764474143766613,
                                                                            4403304091931385893,
                                                                            7692104322106908227,
                                                                            8050125466933410421,
                                                                            8955665995711018079,
                                                                            8970053996180365553,
                                                                            1252077805280861062,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ëɒɔȵ¹ϲŨΛIчšç\x85õҪӉ"НĪȹϪċə\x91ϑŨƳʁēϏ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʏɶ\x89˼˥đʄЇ\x97Œĭđʼǒӽǜƒ\x9cФϥđїӤҊԂ\x91ϺќƥӖ',
                    'message': '˛˾ŞƎɨΠåѿ\u0378Ăԁ:ЉȧӳȪ»īŧΩô\x8cǚƢϨǲ;ĺӫӖ',
                    'arguments': [
                            {
                                        'name': 'ƂʵˀϰһĞƶʫ\x83ƪʛǞǫҿɥƺǛļҭʮáŠƝѺΞɹЎ0ӓԣ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƗŝʖzС5ʩΰΘљηĢҞʶЄ_˂ϳżĥǱΖƧдȽҴү4ąʈ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ϕ҅ÈҘλņΨɕïȆȁСЪВʘӻςƅпҜǿʳȑӀȮ\x81Ǜϥ\x82\x91',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -70339.83476949247,
                                                    },
                                    },
                            {
                                        'name': 'ǝǦЮѺʮǑƞӌːȇνǐȂ\x90șї:ƦɦԄ4ѽфʑΤζ÷<θ͵',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3851474968206155728,
                                                                            7298743565971359618,
                                                                            -4430862286687331217,
                                                                            -201622222557682150,
                                                                            316459393227418365,
                                                                            -8903524849129446756,
                                                                            4627044500395008649,
                                                                            -4957157493160078584,
                                                                            8970816668471145553,
                                                                            -2680663734889445494,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ƿvÐŠȈ\x8eүϔńйɩϾμҔғʩ(ƅƌqӔϸÙȵӸϻˊɹ'Π",
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'PˆϥĴ\u0379ңȿѐѮΎЦȇʚ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7697485711024533285,
                                                    },
                                    },
                            {
                                        'name': 'Ӫˀ˳ˊϕŜШ\x83bԧ;ЀӯԖπ˾\x98ıѭѝϐãƚÁΐˍԣ*ƕ\x9e',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185600.014967:+0000',
                                                                            '20210910:185600.033048:+0000',
                                                                            '20210910:185600.050639:+0000',
                                                                            '20210910:185600.070785:+0000',
                                                                            '20210910:185600.103518:+0000',
                                                                            '20210910:185600.121797:+0000',
                                                                            '20210910:185600.151784:+0000',
                                                                            '20210910:185600.182486:+0000',
                                                                            '20210910:185600.215168:+0000',
                                                                            '20210910:185600.240691:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'υѐ¡ʎʞʞ˶',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 200627.67921546032,
                                                    },
                                    },
                            {
                                        'name': 'ˬŗɠКĻęˢԖȉǹĸϳо҆ϷЀ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8042390457539619402,
                                                                            5571588263239163485,
                                                                            3540456774539643929,
                                                                            -2237756199641000997,
                                                                            6393622183732475715,
                                                                            7489133450429819817,
                                                                            -458344140968206644,
                                                                            -8060478046377210805,
                                                                            2678667984167129752,
                                                                            4527801972822332306,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˫ɘơЇρԙҫӝψԧ)Еǹӟ^Ǧ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5839806940485284682,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ĂӺԥëŉЬЬуЈпˠǟҐϽǅӹƵԅЉȃУϔѩƎΞ˗6ƈ˧;',
                    'message': 'ȻjОŉŬҴӽӎ˒Þ8ǜϜΛ˷ŏϭлȜӇȨӑŢūӈȚΰӹdǡ',
                    'arguments': [
                            {
                                        'name': 'ÙͳôŮ˽ĠǼϷ\x9aµʹ§ѕӨѽˊԆȚƢ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            919662.635036497,
                                                                            357289.7531370102,
                                                                            749551.1668575379,
                                                                            761591.879664306,
                                                                            854617.3274960695,
                                                                            670343.9712828653,
                                                                            741821.4563276,
                                                                            276715.27795873187,
                                                                            323178.542327135,
                                                                            39245.46893588969,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ĕå',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˺\x96ɺǐȣɲɋЎ҂î˱\u038d\xa0ɏǪʝſгʸĹǪ˽c}ɄɎɞΖMφ',
                                                                            'ЫϋÁџϣΘҤԥSǵjγɕ\\3ˤϸˍãĸƗӎˉԒҐӞҥЦэΎ',
                                                                            'ЂĘɭǮ˼,ĶьƒɽԋɐӭЕǿŌÜƄÆӮȡЇƄҤΰ¹ÛώʕĎ',
                                                                            'ӺŁфţªЍѽϳӦʞʪˌ~ȣĢʚɲΕĵɫŝһјѬɋXҋʥ˗Ў',
                                                                            'ӯɰ\x9a҄РʷƅɳˎüĬθӍʗʽӏ˯Ģаԫϐ˷ɵĵƲʹρ\x84ʎт',
                                                                            '¾ИӫӷơȫЉǂ%ѡҥЈƘxЁʔ҆\x98ѐ|ӦϫϩСΥɥ˕˟ś\u038b',
                                                                            'ӜǾͳӹȟ\\˚ĽÏгIϹhΝ\x87ȅώ\x96čѵȴϾήӁҊпϞ·ɳͲ',
                                                                            'Ĳфǌɼǫч!ʹØʕʣΖԕʡЅς\x9dɜ҅ƦҾG\x9bоҰʴŵӺѠ˯',
                                                                            'ƳƌИԕˬԔįÊĴӓƻ\x9e\x8fԝ<ӬD¦ȊГΜĭʺȡѸjÛ\x99Ƅϫ',
                                                                            'џeǼƾʨúЙŏψԁ˺ɺFԟΟȏԞʤθ`ȥϓˢ\x85GÀϑÀҀӠ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'у\x85ĞӨ˷ȩǱΒˤǁƔƻʫ˩Ӛљʉ',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҙɹȢҚbƨqȒĳLȅ\x9bʺʺӆýĕӛGʘ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˁҐŽ»¸ĭʐǇCÆ˔ɷƠȨ³ãɯòѕɿƇˌȟлӞѴƆѳřȾ',
                                                                            'ǒ~ӢÉχί˺ĈфMάϺɤǎϙlȂѕJȡʁϪȏпŏɃɂцОӍ',
                                                                            'ӒϪӎƫĳłȝřȇшΓһĀȆ@Ѕɮŏ4ѿ\x81Đƙ©ʎçȍҖɻ\x9f',
                                                                            '˯łӛҘȷŁΟьɦȕ%\x9eӉӯҐқǸɤ˄ϼƽӵȇүvʇӟ`òψ',
                                                                            'ΎБΝˀѝфȚ²ʵϩôƑǌƞδПѯς\x88Ԭ³(!ԁůʈîϙȣҋ',
                                                                            'ЁżƣêЦӜĴҵͳүǍƻ\x97ӈãǖ·έӅ\x9aӼˢıbąԖɠǻЯǪ',
                                                                            ' ǞœЈŭԩҨ˝˝ɹԎȮҧӒΔХͿПӀć˙ѩĹpIө\u0378!\x9eə',
                                                                            'їӇyɑЂ˖êˏƬªǠèдŏɁȓÅ˜ęΠϋŴƦ\x81Ɠˎc\x8cϷş',
                                                                            'ЖŁ¨ѭϔĸâɑ$ӿӵ˦ԌѪ)јˇŖƥΡԡϰĊԑǬǅ°ſƎґ',
                                                                            '˭ȂәӕȌƑΜƼ´ƯƴƍƑӜ%˕ӛѻgϜЩʗӑΚʂUѓѺԎ,',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '϶έϞȝñԬʚƈǆӋЉ\x90ɸƙɊ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5227579378970312001,
                                                                            4354365881720670193,
                                                                            9218816106259533164,
                                                                            -5383988921893079224,
                                                                            -4709982359225710217,
                                                                            9096442269012395297,
                                                                            534874951658468855,
                                                                            -2565311938392019431,
                                                                            1716169950769191734,
                                                                            7186279403757555417,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ύƔűɱϐѶǏñ7ʇрϽӵɤԣԞлԌРÚ+úñΟǾӁӨͺȎI',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѻӂЬ˙ЪťҋβΗƝ҆ϔҿGЖπΒgʳ=ǘˍƖ\x93βϏѹʥǜϹ',
                                                    },
                                    },
                            {
                                        'name': 'ԎԢÀѻӖǒƉӞўI\x8aǻɷĩ¦χԉғɧҕ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -89707.31613800574,
                                                                            82500.82597007093,
                                                                            509066.8166164827,
                                                                            114580.98414690563,
                                                                            254519.5671031294,
                                                                            524746.406244067,
                                                                            622073.2886172507,
                                                                            732310.3998935384,
                                                                            282453.5317786633,
                                                                            261886.61103729572,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΌӯǊÑђҳʱ˒ǌɰϓ´ϲǗɂüèęǯπŢΆÂʎƘǏϩńȊо',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            982352.688397256,
                                                                            547095.5421161487,
                                                                            3567.315963674657,
                                                                            239385.51736252732,
                                                                            565777.5659527694,
                                                                            173209.97614873026,
                                                                            197918.68859414954,
                                                                            63209.94866554308,
                                                                            380685.9379995501,
                                                                            490272.8525155353,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ətÕzĀѧʦɼdɎϵЭȕоӉŏ˽҈PB¢уƇƜΙϳҞ\x90ư˪',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŋЙԣȻʏǯȜӥŻ!ň˭ăˣůʌʡї\x94˚ĭϘȹӷ˺ƞɍǯ΄Ʌ',
                                                                            "OўǊϳԦaVҐȏ'yԄæeeŭˇϚ;ɯ˕ǉψѨџˠԧƆƜw",
                                                                            'aƅτƛİł\x9aŞˮŢȽĨŨƷӀҰ\u0378Ĝ$ϊıԆμўѣǌ˦ǣpʻ',
                                                                            'ǉЈ˥ОòәүϰɟæɈӚӓӀЄԑ`[©˻(ȁҙӑqѝƽъϢ˟',
                                                                            'űΤƆϠΤԍӲƭϕϴӿżЯƁӥІ\x8aҊhŷɶǣ;ɛӕę˹ЬȖČ',
                                                                            'ġãЯīȌĶέ°ǥұń\x86ЬŞԀɞıɈȣҼѓϯҝΣɮΛўƪжӶ',
                                                                            'ȠȩЏŖ7Ïʕ×ĂƲǕЮ_ɸµ?ȢѽǹΗ˱ϨҴϕˀԃĸŽҫÇ',
                                                                            'Ů«õԒΖĹ\x8fʱћ^ǄВɣˈf\u0383ƭȱъΆ˚\x8aɋҪǆĒц/ʐЩ',
                                                                            'J˼ћţ6ӻ©Ɵȭϗӂ\x9bœǉӲŎϔ˛ʺӴıǩʠҭ\x9bЅĂѫâ\x90',
                                                                            'ɿϥΠȪ\u0379ʍҎȁϓ˅ϐǾ˨Ŀ[ғÞȟΘˎɎʦнѧҎϸɣźøɶ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӻҥɟӈι˦˅ȖЯΣƓƫǳĤáѻʲ˔Ɠψɽđ\x98ƤƜĨӥ)ΦО',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            83631.62731393968,
                                                                            934905.0253191894,
                                                                            643247.9706931955,
                                                                            366272.88920068403,
                                                                            266771.53057459416,
                                                                            866172.9127719654,
                                                                            249993.48423868365,
                                                                            876306.4253302292,
                                                                            929335.1890692847,
                                                                            -52853.94692085667,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʚԂŏӾȷ˻3GűўŇęуӡ\x86ʢВ\x80ɦıС®ȂҲƧŜΤ:ѿ¦',
                    'message': 'ćyϜѱūæћŧǜпдљƧʒȕįǫϮʤòғÕʾˆϓ¼ҩΉƦŚ',
                    'arguments': [
                            {
                                        'name': 'ƴ˪ӼÞŰԞǃљƩҶΙϩяокϕʊǱÀǻѷǉ5ǆįңӾЩњ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'g˚ȅтЦâԆ ԃΤүТhӱҞϲĢӨҵγŔ¬åÐŠΚΪѡЛԔ',
                                                    },
                                    },
                            {
                                        'name': 'ŨɂВλԒғlҍЫуҔɒĖгӘӂо¾˾˛Ȱ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8098536696553685431,
                                                                            342754985390210599,
                                                                            -3529965741619843368,
                                                                            -3358588559949037426,
                                                                            5279155890378604631,
                                                                            -4262740618174985892,
                                                                            734737071266465008,
                                                                            6588562027743730737,
                                                                            -6494609252679035699,
                                                                            -2854376526081515344,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0381Љ(ŐιȈr\u038dķɗʣҽǨΦύɛȘϭҮБԗԪHϏ/ѮԆɧěѶ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '\x86ƂѲљ\xadűɸŶʿӱɭРÜŒΖɀ18˛×`',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6486517270786975327,
                                                                            980669286672895412,
                                                                            7079762798516881845,
                                                                            -4324466235182272379,
                                                                            6486137039530763892,
                                                                            -7186020063794003652,
                                                                            -2896455400489773480,
                                                                            -5021803695831534156,
                                                                            -3415777232092682518,
                                                                            -8882140928451334079,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ôȦԚĀΓɰ\x91ψҨфξңζǘŴϔȊϊ-ʃɎȇħ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            388290.75212487485,
                                                                            569944.5339189756,
                                                                            454859.49441814853,
                                                                            440589.98249568185,
                                                                            839807.8436309494,
                                                                            338622.91724566714,
                                                                            325450.11616026936,
                                                                            515943.1102557448,
                                                                            896041.2391662981,
                                                                            671243.6578070143,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѡǄŊ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185605.834344:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʚʕʂ\\ΪɤǚƬǧƝƱҩЌнЄŒʑƞƴ=uĘИĢҸ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ȁĺa)ͱΚȕǳӕ9ҪĐģӵΗĆ˝ɶ˟ɎŌϪɞ\x9d˓ǸăԪϔԐ',
                                                    },
                                    },
                            {
                                        'name': 'ȶԙǠǇɣлӇθͼȌɌ\x9bҘ¡ȵǐǋϩϞО·\u0380%˵',
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
                            {
                                        'name': 'УŨȁ˝ːΔȀźЉԜǏqԆӥƹǆʴϝ\x95ɀɩɋτҝ҃ʲӬĴ\x99ŀ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185607.600548:+0000',
                                                                            '20210910:185607.624727:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͱƖƃǘĢƦǹ\u0381ć',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'έ3ŭΤԘ\x93ʒєóϨ\u038dœψӪμЈқɒѤ҆ҸҭǈҕѠӊӕʹԬҖ',
                                                                            'ѡѲǥŖϰηЎ˸ɨЅҔ˙ɯ:ӣǗϒ¤5ԢͺĭҢЀȷƿˑСɐΉ',
                                                                            'ӅҐfϟȜưŅʹʜç˽љÍʘϩ˸˲ßͼȁɲϷ\x80ʔИŞW˫ȐҠ',
                                                                            'ĝÈĔϳӰ\x9eƇɬũȲëθΜ\x90˥ăȌüǕ(ϾëŲċôźǨϹ\u0382ϕ',
                                                                            'ɭɥЌüĆˊӻȮèȞ˕ȁƓ·ԡέϰӌРԕԑɕΥԓχÞˠΥƁǎ',
                                                                            'ÕǋӪ΅ԓϫǓϭoΒř\x84љȖƖȈшɾÉĭüĐɪʅ\x8aįǪȐΚɗ',
                                                                            'ЁɑЕPΡз ԪǼˌ˙űұƤ.ɧŘҌ§3ӝȈñǀX6PҰțȢ',
                                                                            'Ӯǯ\x93ҝΚʜ˳ɓҡŞүӋψĴӛҠƆԥǃvʤũĕưĄΕĚ\\ϛȶ',
                                                                            'ͷҙˇźпʱQÖαʬʃ˜ȦąɆҎҕ˫χ\x80śҬʘϲЗŴă-Țɏ',
                                                                            'љżϛԟȊώȪρ9É҈ΑσӢŐɺĴʃρԠ\xadĸȅϏͶ˥в˂įȒ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΙϴѯΠĚΒġºT;Ƥ\x88ǀŐķ\x96ЁǙǪġǃɱҪȵΙņgҸħȖ',
                    'message': 'ҒƠɴŨқɅJ˘ŵƢҒˍ+ΘˀƛɊŹȽҊșʖfĹǋǐˌԭˡȀ',
                    'arguments': [
                            {
                                        'name': 'ңԔņѕȏÁҴĄԖϩƔˣÙ?ƨRθωàԔ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6974583979558974713,
                                                    },
                                    },
                            {
                                        'name': 'Ē˕Ϝ¹ЏτЏӠǓǵ˷îќΟĢƝǶŅɵΠʇćΕȚҷԄŔǻԞ¥',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'Ңƽ\x83ʛùǜϙϙ\x8dԉƝ\xa0Ԍïҋ˴ɻϏŇŚȰ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            405902.5985397078,
                                                                            139540.14643480146,
                                                                            776515.3978413955,
                                                                            -3769.327380512812,
                                                                            871505.7803507557,
                                                                            -13116.694069882127,
                                                                            -88742.12950074917,
                                                                            329337.97606166446,
                                                                            130884.37263002523,
                                                                            904275.3270121033,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƶЊʍěɿqąƍѦƸǄǞƏ«j΄Ⱥȱŵ\x83ȩĠ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            812690.6469247596,
                                                                            938823.8425621341,
                                                                            107840.13047071462,
                                                                            917441.3010625264,
                                                                            -21487.93831729509,
                                                                            821145.8122494512,
                                                                            636196.1283282465,
                                                                            902960.4894257071,
                                                                            411305.7363445836,
                                                                            333855.8596723437,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '´ıa\x8aˆiʰќ\u0378ʒhϏқʙƨǃƶ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2241875770802689533,
                                                                            7574203115105324049,
                                                                            -6779680425479164729,
                                                                            1195565635577436325,
                                                                            -9112083943249810289,
                                                                            5824499001969084939,
                                                                            8688733682474944565,
                                                                            5501439364785904150,
                                                                            9084454027557435657,
                                                                            -8371028371911021366,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɶ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3130117097473565630,
                                                    },
                                    },
                            {
                                        'name': 'ŁǅԭÎɶ£eʝп',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            838928.9453681223,
                                                                            -55288.79080714696,
                                                                            695814.8999316797,
                                                                            312261.26091869466,
                                                                            19331.122901973533,
                                                                            746462.5961943084,
                                                                            53976.745283672964,
                                                                            205728.46528902795,
                                                                            438005.8070350803,
                                                                            984138.3394208727,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '$Ӫ˙Ӓ\x91ųӝҫ΅Žѭ³Ϻʮ˃ӱѢyşņϊɀǥөгºĪɬЉÄ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2051671467517935826,
                                                    },
                                    },
                            {
                                        'name': 'ӣБÎǝʫ\x8aϮ\u038dųõҶƇĪɠ6ьȉƯýºʴȧфVưͱÕÐȆţ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -28524.151632008157,
                                                                            736540.2628854058,
                                                                            515008.74312824244,
                                                                            582755.4254080412,
                                                                            977828.7184763786,
                                                                            348578.0243441098,
                                                                            53306.52077768635,
                                                                            697170.1517359557,
                                                                            935678.4447395504,
                                                                            520552.0269855922,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'íϔʲ\u0383',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1291567754072170138,
                                                                            2260065125137636641,
                                                                            2694471748664059364,
                                                                            -2186874128423012745,
                                                                            1382298014952392377,
                                                                            5049177043512658004,
                                                                            4248843577774013222,
                                                                            -1143533138639806193,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'нƇlǝŊƢѳɅɖѾӂƞǒmɻҌΓ;\\ʾӢ8σƷӨӿύɆ}Ǧ',
                    'message': 'ɴȌϾʳхŴʬԕӝǨӭқ@ɾƙQԞɿҴǩɾϜуØŗҭӏӑӕe',
                    'arguments': [
                            {
                                        'name': 'ƤɝɊgÐȗɐɘҏʄмη\x92[ǭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185610.651587:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȃНȎΖˏϺșɨʷÚёʥчфМˌǭϸŗɞȀɞs',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8079898093208041451,
                                                                            -2693459599350990344,
                                                                            3164366385368940029,
                                                                            2334187667554548930,
                                                                            2893550192945246173,
                                                                            2630847728992614262,
                                                                            -3627115533553160663,
                                                                            5124647539672041088,
                                                                            -6442896264297626203,
                                                                            359477787824451132,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѱʊˮǉӅ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҴˡǑİĀ\x8fԩԧōǠЂ\xadƩϛԜ\x91ϗʚҩӊƊϮ\u0382ȧ\x85ӾȢĖѧǷ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ɵ\x86w4˟ЪΉ΄ϔùßӡ¾ьΰɟӨԗнѺƽ\x92ҞĂȏŠǿыȸʥ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'ùҡȍĂĵѫʫϔ\x9fɉĞ˜ȱțΡƏTƯƏŇ¤\\ȡɫɵ^\x93',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4977026210500997297,
                                                                            4588863942520839027,
                                                                            -7783160872561117633,
                                                                            -6565808719690407006,
                                                                            -9067975159396311925,
                                                                            2612868481631489052,
                                                                            -5053527056028578541,
                                                                            -1972174722255248567,
                                                                            3970315546203755101,
                                                                            6182388516045290880,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӏԅЦҡˬεʞ\x8c\u0381>ˣˀǌυéɵ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'DǶҩѭəɦ>ҀȜѮԖґͼǗЎëÜǣ¸δʞìт=',
                                                                            'ÐВŶÂΞǆ˯ϬѨƍʓҁІǑƎ\x8dÙÐŰѝƇѷȆ!ҽǱɯʝƈΚ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϫðčǮӪȑʤŵ)жұšŎЧ\x8b\x94ŎӛӑɯżŮͰǸѾΕk˽Ɲň',
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
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƆiΗдłɘsϫ˅ԖaʍҭκәԔõφǡҰҒӕР',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 909801.246506446,
                                                    },
                                    },
                            {
                                        'name': 'τƽβʴϠ}ÙʅĒɻӼӍ˯δyţʌԡтӂƺҟE\x82ˡ¨˹ϹʡȺ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 902828.42833055,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˭ÇέҒΐ|ȾүƖΞҖԟТҹȘǖɃÝʠњſčШǵө\xa0ŤĎǶƕ',
                    'message': 'ʝ҉\x9bº\x86˻ȚɌšįƑjĐԏϴΩǂƩăŊˌǎŖʇӝɻɀ_ȢË',
                    'arguments': [
                            {
                                        'name': "Ѱп´ɡĮѴҽöѵόԧɍſҨšǋΟÉ\x89ŹǋΈÎјКß˙'ПΩ",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185614.336998:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǦƉȺ\x99ԤǾ˥ӱ˻ƁӳғӀПL',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 673745.7513085544,
                                                    },
                                    },
                            {
                                        'name': 'ΧҩɜǡӳђȗǢ\u0378Θ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            766897.8732799336,
                                                                            529417.1497462128,
                                                                            435767.4382456412,
                                                                            946694.979734818,
                                                                            320773.91920984496,
                                                                            642335.3357098575,
                                                                            943206.4314484858,
                                                                            33722.58658225546,
                                                                            221395.57679804135,
                                                                            130479.68402961586,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϝŚ}ϥăĥǍˍ\x8bɫɩȚ҂ĊөTїǲη',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185615.354758:+0000',
                                                                            '20210910:185615.372362:+0000',
                                                                            '20210910:185615.393983:+0000',
                                                                            '20210910:185615.412746:+0000',
                                                                            '20210910:185615.429716:+0000',
                                                                            '20210910:185615.448662:+0000',
                                                                            '20210910:185615.469440:+0000',
                                                                            '20210910:185615.499529:+0000',
                                                                            '20210910:185615.530141:+0000',
                                                                            '20210910:185615.552928:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŝŐΤҥĕkɂ˽ʂɀ\x99Ӷҡӯӝ˂ϜЌnǪʑюȗ¶ƛİɶȪǡǢ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2062713184816633892,
                                                    },
                                    },
                            {
                                        'name': 'ˆʨұϛͰһƂÉѡͱɷѥď\u0378Ƹð',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɒN¾ʃɊʪʵMӻʢ¶ĵƤǂϤόƲbǌȅÜŃρʟĐɸ\u0378ҷ@œ',
                                                                            'Ņəϴrȓ\x96òΓȿͳҌɎ˟ȟӁǴʞТđͻ˜ϒƂпȍύ˃ȜӛȨ',
                                                                            'ҨӳӢɈΗá~˷ŚҿÚˍǳ\x9cǌђ˕ѺâĽżсźÍɥ˄Ӹцɸ«',
                                                                            'ͻώ"дĆӌԒď\u03a2ґɬĠÀюάƪʪ&ȑɊі÷áũvњϬϟˍ˾',
                                                                            'ƋФԋƕˡʾηÁΩǏǩ˞ʜФ#ȹЪ9ԓѲȼĩϋѐԭƛϼΥNư',
                                                                            'ϤҌƐͻȇǈȠєìZοƫǾÎŇ´ӕǙ\x96ыϞ\x94İɿʹϟʶǔĿđ',
                                                                            'ЖΰΠOžŮ˓ŭǙΨӿԕѸǰßδɑǘıνƣǄϼ0ƈƧȻ%ΊͶ',
                                                                            'ҜЖ\x9c¥\xad˨ğЕt9Ƣʆ\x8cѢԗɞÈјɠɿÀǺǞƯŴƝҐɋɆҵ',
                                                                            'ÖԈ\xad¾vʑω¬Ǧх\x96҃ѰȭčïϛƆŋȷđƈĞɤAɽNҚӫϠ',
                                                                            '(ȱʄNȊԨºċŨɨȀΟĻӾŤƇÎ˩Ԃȫʲ\x89âȹԫŉϵԁʚ@',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĥӃGBύѸΗ\x8e',
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
                                        'name': 'ԊΒĄәȽƶҺʔ\x8aƿɗΪŶ>ʀ˯\\ŔìƏ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ĻÛƞɀ˺\x85џȬǂȞˮʝӚõҊϣˑʫ˪ɬ;ĉҗΖǴfTϋʸΫ',
                                                                            '˜ӔӮϚϊŚkӓŖіėπԣ΅Ćɝ˴ʮϱЪєήāĪɣКƂӄΦ:',
                                                                            'ťˍsȰӲԋūязɱӪ\x89ҵͷʝĨЪŞҡØˢдŲĜčyґǼ˶Ǫ',
                                                                            '҉ōÅœņŸÊ˧пҫҏҏҵƳĽϓЭœуϐKZ\x9fƣ˱ГǊΏǩȪ',
                                                                            'њƤʁʵÐȱÄmĔҶć҇ĺωȆϠϣƎɼŔɺŷĸèԚΗ;ŨлȄ',
                                                                            'ƹ΄ţѩΐǸǡąԌȺĩԆϩӅϧʮ´ŜÚ×οʍГΉʯx҂ĢžϦ',
                                                                            'ĕȜЧµuҨʪēžĆλϓAМӺǎŊƏM\u03a2ɌĄw˵\u038bːͿɜѐã',
                                                                            'ɝҖȿҔòў0ġΘ҄#ͽɇʌʶSȐϓӸԡ¿ԮƱθǺǢщŒʦĀ',
                                                                            'jCҺȱ\x92ġɂѫӅԎŎˏ҉ǽC˪λȣМ?ÆĵųΗϱɀÛϡdŨ',
                                                                            'ŽŀNӼӵϩȝӿǟǁŦPĝȼNѣӃҌµɅɑι\x93ϼǜ¶\x82ɕʓά',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǌ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'øΘԮӍíÄɄƔPϤϼħƽʆƃԝƦӢЈД˙jϥϦ¾¦κX(Ł',
                                                    },
                                    },
                            {
                                        'name': 'ЙĎɢbѣŅ\u0382çɹĨł',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҭÑŻϤƌˊƟĪѼŔʰөJǍđйǈʤǌȤƻįáǀ\x91Љ\x92уîϸ',
                                                                            'ĭрĨ˜ϰʅӯξđƎϴӢʕ#ӷȉЍΟʋҚѰ§Η5ƖΥsɈǵϠ',
                                                                            'ϫҀÑƟό šЌʇɂƕ\x8d\x8eͶɿʯŎǮŲǆƖʁЃӇӠʰ˺Ⱥǔԇ',
                                                                            'ϬģüŒ3ʂȹǗИzơ˸˯ɏƠĬ\u038dΎƢƍԎćȮƓЭҊWЯιƛ',
                                                                            'ƄѨхƾ˰UӜɭΐϡɓƔüЪŪԊǚσ¡}эþԣɌ˨ťǵĉÀĀ',
                                                                            "Ŀȫ\u0382ĳҬ\x84Ѹ˶˽'ϽѓǇΧˆˠƻŇҞBɕǖ҂ѧДȠϟпȋа",
                                                                            'ü\x84ƓǂϰɑȤƻȇԠřǏ˛Ґ\x91Ԅϊ\x89Ҳ͵Ԉԛ=һϕÖЯѠѾ©',
                                                                            'üʅԐǄǴºҳǹԐʝ˖9фκϒʥʁʼүĵȲΌĈ͵\x98҃ƫХɲ˕',
                                                                            'ǸήʇŷϯťτzɗͶȸȅϋŷϤ¯úҕƯОǕƍŴōǿ8\x88Ǣο8',
                                                                            'ӘГ\x98ҝƁȄ·ŗ˼ѝť˚¸ˏʿʻƢВŀǖm$ƫfӁǞӍnԘІ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'аŴϓƠӘ˜ʓϕŘѡŃӁƾȩxӹоˍӥɥΗ˒ǲ҃þҡЭπџ(',
                    'message': '\x89Ѳú϶Õ҄ҼƖϮλјҞǉUɆÚſ%ψ?œãҢǬuńˑĒҠɝ',
                    'arguments': [
                            {
                                        'name': 'ġȂөdʶŽ\x98Ɓ҇͵ŭЊñΈ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԩΨƅiʙѫԔΕьLԚУƃÕǒŁ3\x84ҲǻɆȥϟ0ğѺǑˁ˩ʋ',
                                                    },
                                    },
                            {
                                        'name': 'ʬĚλѾʞϿɨ˹ǋˌāŐѻώʂӺrȌӣ\u0383ɑƐǝNр·ПҖƀΥ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185617.165240:+0000',
                                                    },
                                    },
                            {
                                        'name': 'čɟɂȯʨÓQЀƧԂÂЉϡҹŊɼȩŔ˶ЬŃiÎάÔЩ˰гùʹ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ˑʅæ^ӜζȮϥԧτéƍԄǽ\x93г\x96үƼ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185617.994367:+0000',
                                                                            '20210910:185618.020540:+0000',
                                                                            '20210910:185618.038857:+0000',
                                                                            '20210910:185618.057020:+0000',
                                                                            '20210910:185618.074555:+0000',
                                                                            '20210910:185618.091472:+0000',
                                                                            '20210910:185618.109732:+0000',
                                                                            '20210910:185618.131450:+0000',
                                                                            '20210910:185618.149122:+0000',
                                                                            '20210910:185618.183976:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҽǁΚŽэĿЎϮΉдРҜԨΥŝΉæ¿ԟpʋ҄ÐӈϚгğœƬƛ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1743388694008290440,
                                                                            -283178328207024830,
                                                                            3308828154235213929,
                                                                            6304859023476711777,
                                                                            6975036648255497345,
                                                                            5532322615279332972,
                                                                            -6001324684329996119,
                                                                            3161687405975240381,
                                                                            -8513901670360758585,
                                                                            -8284238971941358225,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƈǩɁѕϵõѥŖҙĉ"РҵȓĕĈÇһͼϬfΠíӣ×ɃƩкƹЈ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŨΛбэĆ³ͱɚӈǋƉӡƧȝрǂțåӣ˦ӜӯϻЈ\x8bąƘ\x9cԖӮ',
                                                    },
                                    },
                            {
                                        'name': "уʊý\u0383νϭĚԒ·ÞċԒǮҪȗĘҀÀɉҬ'Ğò\x8dʑ¦ºħəÿ",
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɖʈĊϘɺˀúѻİҨÏ\x98qϗ˷ʛϑƀϰǔĮŦÜάɜɣɛˆƯó',
                                                                            '\x8fҹɩғώΗиŷ0Ħ ӧΖɰѮǻʳʗԦ˳Ԭϰр?ŕĴù˻±Ԫ',
                                                                            'ԖȜƞъҲPxIŇɂɵnƼЊ˗\x8dɌǢ&ǛŃϘʻɫϧğГϋȰӭ',
                                                                            'ЁӉ]ӕӤʅҳѲȏȤʊμ\x8cӄҁʄ;ŏҝˠηóþƚЇыŢϡfˬ',
                                                                            'įΪтĺԁšˌɚƁϵҍŵĳҶÙƌϣԉÎɚˤˠΣƻԠωЏoMɯ',
                                                                            '8ÝǀΑ˶ʬÊϗ!EŉψɇʕɜǘӮПɦӴǊύPgÂ˨Ǌˮâӄ',
                                                                            'ʃ\x8cʹӅʔԕŖ\x92ɐ\x9dԝϜǃȳ³ԨɻТͷϘáԑєɩgҭd³ôˠ',
                                                                            'ϟǃ\x8e\u0379юæɾ\x97ŧ®ʛԘîƌƻӓĿīҝӞԦȶʘɒӄ·ΤɕƝ\x88',
                                                                            'ǫ\x86ȬƶЯɨѳǻвÁёң˟ǗǉЧMÖɩłØ\x8bԚƱҶƷҍ҄ɗΚ',
                                                                            'ȀѩΆԔйяȿʡΕȔǊǊʨƤ˜ƇσŽʆӇ·ͼĹɓǮĐǱțԐ$',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʱεÝêŵЅкƤũӓ\x9cȡͿʏь˗ϝÞ\x93\x8eԅυȕ˨¶ǸQȕϫd',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5338636181907551406,
                                                    },
                                    },
                            {
                                        'name': "ШɃģ˅ЕÆvǓǝͽÀ'ǱȒχҴ\x8a",
                                        'value': {
                                                        '^': 'float',
                                                        '$': 225408.95599437138,
                                                    },
                                    },
                            {
                                        'name': '\x84ǇǽћԜѵǨũʯјǲҍѨȤЋĸԄԬÍ¢ԃѦέΰͳ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
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

            'identifier': 'ϨҞƠ˵à',

            'categories': [
                'network',
            ],

            'messages': [
                {
                    'catalog': ';O',
                    'message': 'ϒ',
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
                'identifier': 'ȈнӕҹцqБԞaêȌϿӇӘ҉ˠѷΐy\x99ϞʡԚɉѲ÷ΕŽфȳ',
                'categories': [
                    'access-restriction',
                    'configuration',
                    'os',
                    'internal',
                    'os',
                    'file',
                    'os',
                    'internal',
                    'invalid-user-action',
                    'file',
                ],
                'source': 'ǄΗɓϼδɃӄ6jȚњѿ&ĆϋжȬǰҨǴį˾ϽΗƦІиӱԂɕ',
                'messages': [
                    {
                            'catalog': 'ȀкƱģ\xa0ºʠϗȅ\x92ʻѴиlԉαrԣƱҽŗʑIąНÌƅұŀƦ',
                            'message': '͵tàʾȁԒƷƽý0;ĆèώΞή\x86Ɂơ]ѪǑªʹΣɬÑԪəѦ',
                            'arguments': [
                                        {
                                                        'name': '΅',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'е§ɐ˽ӈȴɜźԢƐſӶѓ]ʤ5Э˥˞)',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 874734.1004504894,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҳ¶¹ӵǯДōɉÔʻӆыһÂǰԊMɏϷҸʠПʐøʹĪҿġŬk',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2087994808988427019,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĚϘĨ\xad=\u0378Y^éη/ҿϛǗԉΊº',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҰζԨϗΤĹȪ˛ʩАș϶ŎʪȽЗɉϺνөЂYËʴo-τƋȕA',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'KŚӽóҀͶʒƺ¾ơǯЫԃӡ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƙѫѹυɰԖͼкȗ҄\x82˧ƺΨÃñʝȣѝĢĒ ΜǝɫĉʲĚöù',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȚȭʥΰͿġ˚ѶǐӬъˬӬйÂ˰ϿȋŨԑȃϳƉİǄӷˮâƟǥ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʮū˜ϕŁҕtŒҫłǉϕѮʽkɤҊ¾ǸȵWҜ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ļ\x89ԛʻšőǁ¶ƉƻvȽQѣУΈ\u03a2˗ћ˲\x8fүȝ˧˾пӥңˣі',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 350418.4889273804,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȺӊȓƔʾŌ҃:ăǧЕƁ˜ǝԧT\u0383ϿìɍʖЮҫǄˏљÐÅκq',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 525735.2279891643,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ωŽȟǬʥΖħθøԫĞŐҜŸHȿĸΛφțùǱπªƯхɣʫʔě',
                            'message': 'Є×ǗșʕĽŜї\x97ƚăɠό\x89ԬŭPƎȘɍËȰĥȤtɨʧӟˮà',
                            'arguments': [
                                        {
                                                        'name': 'м/ʣҍɳӖɒ΄˾ЌĚӒδø˃ΥȑҾĢӾЛʚȱɇӊѱιΣϬ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʺҼŃ%¯γǖҀĒϞƃ\u0382ԙÒ˗ɂьʑʙυb°ϺΉȢӊψ˵Ѓƴ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'jҿҩZȆȝƋÓӖ Ɉ~ɲdŤѠɨŮĴ4˘Ö҈уɔ2ǪԫΓԫ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '_ɛʢȣɄȄҿӬˈšȜ\u0380ėϤњʣҥǄҲԣ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҢѓԦĚʋʄƒ\x89ӆσȘІȎĆȻҁĬӓԘɇφƖĩҳȆѾΈƾҚ¢',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'óȢ]ЉΑʚƜԧЭƞ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˽ӡʎ²ԀȕԨĸӂ҂ÿIƂƎϟŁȄĭƕϸӺčn\u03a2МϮŔɖǇÞ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 578390.6858794885,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӏƫũ²Qʰϱǩ\x80фǷɋʼFҪƆгüѶΓ˖ѡҧа$ҡӔ·Ʈǆ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɵ˸ƌƣρèѱЙ˰Ѹì=ǢϵȪƭɀФӕȮȀʡŉ\x97˺ыМҍâГ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185543.405383:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'щџiЧ]ȤИȒŢɵϊҗêӬΞ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185543.487928:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѽВƶӌHŃҗȏȥΕϢ\u038dϏė\u0383˨ςȋήʵǙςþɑɡʅÍѐѐĦ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĜƉΙ²Ʃϑʀµ˲ӓȚΕª˦ӮѯαÁΠϽ҄ķЗԞuƚҸʾȽȬ',
                            'message': 'ѼŊȊԅ§ŸʲȒȉηƋɱϴӱħ\x85ʺ\x9dƅ"ʐˎʢ8ʪÕŴҦίǛ',
                            'arguments': [
                                        {
                                                        'name': '\x91ǚψɴ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ưɈÚĞ˶ћӂϻԣĶϾҙ˴ʬ\u038bʑƁķАƼ$ȌģȔċˈTҸĂ`',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϓŹΚ"ŕʉʋǵЩԚǣːѸҽΫ\u038d\u0381Ȑqɡ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ťЕȆȿԨϖǚ9ŨΜnʃѬʼɭźƚν\x85ɰǛ˙с)ʎƱɠɆĻɥ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʺ6ʫԫěƯхԦӇэ+҅ʓҊ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'EƒņӽӛKЦɴ˶ɤʢϚʷ΄;ǶзɪцЍǮɜЭΘɼ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2092958543754289514,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЂåǖÍԚ~Ŗ\x89Ρ\x98˗Ӿκήǒ˪ǷťiÌ˙ĉǧǆǵĞӄǤѽ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԌĢǓͼѐӅЯɞѦӞęŕPÂӜÎяԣ9Ȟô¾ŶӚ8è¯ǾåĖ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÝΕӆμ¨ŔŲ#=ūӯ˄Өʖԛ҂ԦԌ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɐǊ`ЮʐȻ΅¢ͰϕǰϝɐĐϥ˽ȭƊəˎϞОԧǗìZ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϳęҽ.\u0383ɽÏŇǫ«ϋúӼЫuʳŖ+ē_Ɇѹ*t7ѡǸŉͱт',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ËïGЎơǋΚжƄįӹļÑˣ\x82±ƳΔГȵKѵ˭Ȑ\x88ɄϏњԒ.',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x90®=¨mӺɫʰȴ3ɬʖјЍ\x92Ŵ]AɚѦͼƫċҪƿӗӚԒȝ˥',
                            'message': 'ɱŉCĻѮʂˡģEˀ\x81įЏʌøɅŇñͳǆӝҚIѹːǪÁôκ±',
                            'arguments': [
                                        {
                                                        'name': 'ϲ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Бè¿ǉ˞ǝƂǺıƮҨϭǘȯԭђϼ©Ǌ?\x94{',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɛȐuˋѤ¶Ʉ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǷҥӈɔӦÛĠώÜΈɷʀЋĭɶͺԞχϨѼ\x7fƹҫϥƛ&љɍϩ&',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӷĕXȄ8ԏūҒҶӃϣсǰĥҕЋòAϧǌýЁÌɄÍӽѢÇ҇Å',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185544.956357:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЙϋÐʹТ\x96ÙĲȕЮŰ×ʍʌRϑѰǽβсΜӛȹ\x81Ƌԁȑ^˜ǌ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185545.034050:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˌóïӲɴкӢҾˠԎϗ\x92đ˘Äʡϐȱ\x9bѓʧǑԨ-ɥ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԉԁʹçǧАѮȬЦѬӊƏõʐʱԑͰƪ¯ȱʞʕƣ,Ϫ1ӏ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 829259.9441098523,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԎЉƱcƴȷ0ɰƚѢҖƆɾ,',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'әΆ¹ԝƷӆЃˮʉәԈӃχԎĖ/ˀȾԣӂʯļӾʬϻϐMɳӸg',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -74657.61999585254,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÏсĕҼʹʳǺ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǐąʾԐӈϒ\x83ɿԬɖѝǸǩ´ҫƈĝуűѐxŋǵǎāǧӄψXw',
                            'message': 'Ѱϩƨӷπʮ\x8fŁĖēѩȳ\x8cΎэʋîǛŉјȡhbƎňΰ˖ҟÂѺ',
                            'arguments': [
                                        {
                                                        'name': 'ʅÔʰͷİрĲʣ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8dˮþДӓʚŤ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'πЏҳďǆӖÊKЂԑŒʉтaЮϒ}ϙ҈ϥʎԌȆěŧŕˇѡҩӑ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '=Ω:ÊĸɆӀĤƈĨԢϾ\x87ӳѬƫӴ˲æȹ¬rŝŕƹύ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѤʕˤѺǋǶ¾ÎйэѲűҞέwʃЯӣ#Ӡԓ\x81ѹРÊ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӰƋļЌЯ§\x9dŀåѡΛГԨȫŌЬƂӗȷäКұäTд£Ӥ[ȪĨ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʽĳϤàΩâͼ[Ͼӓ*ôԭŽʝԠфΌ˞ſʩφлdϿ҆ȃȌĈĲ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɲґ˻ԀϦӁȏȬÝÇώȵƥӥх`Ȇ˛О\x89ӢɀѿàǫGΉŚ*Ѓ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 566422.6751103058,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӓ7νÙƼ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȇ³ɈЖ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȑɯłɒ÷ӈ\u038dˇƥϗİҖΑˍjĽM˃Íϣɋ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ί΄ȓɝЄ˅!ԘϵͱɇoψЦѫƩʍλȏ§њΦɇ¾Ȃ ӜÎoԡ',
                            'message': 'ҹΰPȵʥÖЬΜϷŔ#ԓ2ҶΦƁºЎыƾ÷ȩǅҀƛТã÷ɐ ',
                            'arguments': [
                                        {
                                                        'name': 'ïк҂ǃÄŽ¼ӸýʒgĉʅļǯԒƛȓλɸʳŒ\u0382ĝ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8533583338664346896,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʙƙ«ɎȭéδƔǺŖΎҵҌüԃϲ{ϦѕɮˤμЏ\x97\x9c&҇ˇ˴˯',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185546.727389:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԒƾŹҘԚǣɹǔԟ˴ˌϭEÐɛԓІӃԔ®Ӭ2Ш²î˽ʏPʈє',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ГϋƌԓƕӶԏ©Χ{ǘәǷĝdŶĩшңή',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѓXѰƬ\x8dѓƫĤˌ˷ȃʇӹιȿĀϭͼβʗɗʸϥʨƴǟѥfΟw',
                                                                        },
                                                    },
                                        {
                                                        'name': 'бƒİ҅˭ѾϓˍηӍԗºǌԔӪȻͿņ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԐYwģЭƗȘŒƕ0ɚ˨҂ƀ\x8cԞŮρɓʾȢŵøùѓМæωǍͳ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŵö³Ơˁƭ;ɵĞȺˉŭ·ϳȽμѲƂԪԐ`ғӻ·ĝˤш˜ËТ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185547.245095:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˆљƯÁԋѾȏʞ˷τ\x98γΡEӌƜʔɜ,ɤӉǡґɢͽΓƈőѥ½',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҙ£\x9eũ˫ĂҘˬƀєȓ˵ѥκοӍȬӝ·ɇŊǩΑfǖԅ\u0380Ż˩ŗ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185547.432438:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӌӘșȆҞħǏ£ϼΤАѯĚ´ѿˑȔ?ϗĵ¿æÑʴћчįiʶ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185547.521688:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʘϳŉхđΤ҈ǥħñ\x8fԑȻůӇӨӞͽѦΎѤGԛ˅OБЩYФα',
                            'message': ' Ԏƾ˞˞\x94ҁиӓŞʶÇҁŹɭȖѰϞAυŘЮԤѼ˯ҌӊбҨǴ',
                            'arguments': [
                                        {
                                                        'name': 'w\u038dδōԩʒ*łѽ˛кDŹ¥ʶҭ³¼ğѷϻͿĲÅƆėm',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'оĊˌŎőХȶŢӎ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƁŝɫǝÂ҇ѪұĽηдÜȈU\u0382ːΆҐ\x90҃ÊϋЎĲ·цbç³Ş',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǲϬǕfʝƊԋ˴ȅƇƝˠҷȎԪēɭύÐӀƚɆήȥɉЉƬ÷ʡδ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0382˘ÅˡЌЕҼşϬɼˡƏѲÑǃŕź%ԐЌӴƦȲЁԥĵǂ·ùɈ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ōГʪɏȮєȵüί\\ʢǁԅӧ˨ǰ˟ϠǉЛԂćǮǡп\x9eԞyӯŷ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѝЩ6Έ˼\x80ƳВќXǵʨ҄9lўѳɊƿ\xa0ϳȟ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʼЦҺӋΑżƢϚІŸ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185548.204911:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҺΔϚλʏфè¤\x88ʹ˭Πϒ˔ǃҜŤǧyөŇӫ®Ɵ3',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƖĤқÕˉĶ¼҂Ґɕ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϭҟԒɼʉ˚ÁӼҖÄ\u0380ëʔ7˦ϷД˗śΊæʍĞ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˧ӥѿɱǢɒӎҥÿќ/ԐˠɁǸđ\x7fììʺĘ˙ӱӂ\x9b˜ҫӓȁӳ',
                            'message': 'ÄÍ˻ēDϦ˜ϫCΌƉѠ¬ƳĪÐʞЯʝëɠӘΤȘԚÁȇȌ·є',
                            'arguments': [
                                        {
                                                        'name': 'ΎԬóϩ˔ыΡɈ÷їȯɝʺɮŲӪ¢Ɋƫ"ԩʁɎɵø',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'š1ĈгƏőŖΫʭЛ\x84ЈΠɁґĚҵӺéɼ\x8cãōɏѧɵƅȰӈч',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185548.698609:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӧʤƙFĠář-ÆȬ4ӗȕ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǛSǷÇľÌ˻ųå\\.i\u03a2Ʌéâʘɥ2^ȝ\x91Ϣ!ñѠӺʫǴƩ',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x93?ԎĘ/\u0380ŷ˙γˍĄІЃФӍƺ˟˭һˤƖҍH˧õԆЈӯЯӔ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʮÇȷԅʬďʬԣΫ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 450592.91835569835,
                                                                        },
                                                    },
                                        {
                                                        'name': '҃äʬÛʶǳŎ¸;,Ðϸ©ΟŇĤЏÿӧԂɆóɐѩѠˏʊҊТӸ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǦǵÉϐѳѡϏԃũsǋӡƹ«ӰǃԑͻĴȢӒχϽӮӔӟËҳϱК',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185549.072925:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Д]ΓͶǂʦ˱ϙԬѵ¿ɛɉӂgԔάµѦϮĺьƥɈΰӶDљ\x9aɀ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5492011990638953599,
                                                                        },
                                                    },
                                        {
                                                        'name': 'éУț',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΚɹɤςɾΞƗҶϐɉϰŢˋɒ\x8cȯԍҼѣøҸӕЄ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 793522.1848134624,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '΅ӫ˽ӢԜˋ\x7fɠƠņěԓӢȏE҆łԙʤԄӱʿғǋƁhΊȀŁÌ',
                            'message': 'pǶ\x85\x8b˾\x91´ӔßÚʞɇwĄΚǰϑɧԄ³ʵǍʝƎћǆӃUӏĂ',
                            'arguments': [
                                        {
                                                        'name': 'ȺЎњ^ƵɓˆМǚʶʴʿԆƪ/˔ӺӤɩ˳˂ˎĥƚĺӾԀâȒ\x84',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 443200.5386546054,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҤԊàʢŽǣm',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3946889165785881931,
                                                                        },
                                                    },
                                        {
                                                        'name': 'шø˫Ԫ9ƀӑЄƕιιИÅϠȾͷǙ\u0378˥һԕԋ7ʰëйÊͱтí',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȯηŭțˤƜĵ¹ǙӠӚή\x99ǰCǃϖӵԈ˕б(Ѫ\x80д˞˚řҊǿ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '.ƍǒġҿ &ĳƸ0ʂ"©ʷ9Τρ»ƎӼ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˣȋѠѮԘî˅Ʋŧ`ҠȡɺҺɳ\x87Νʹɛĵҟɤӡčѐǹ˾ɅǻО',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǰ\u038dͱљĻʽÊԫȂſƼɌƥъƝԍ˄҆ŐԈǳŪӨ\x8dӹԁς˹¬Ğ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8569560591646643263,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԋ\x80ϽƏŪǷȂАϠӽҿ\u0382˽мЃä',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȴ˃`Ùҍǽ˃ЙɦʜήǘɖҲșѶϫʾ\u0380ùӥӍ\x91эÃΌ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4991713947669434862,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĻŦѕԞĢԮƚȫϺŔÄϽԫƚȺv˙ŢАҬƌј%ªü9ʎʷǝ˰',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ǚ®ǶåUsԦҔŘώЏɳkӎƇãԮɽҢϗ¹кɌжΑӦŅ˴ϋǱ',
                            'message': 'иЩǝЄǮPϐFӃ%±ʆбфŦȒԓķCRlùăЌŎaĲ҆vä',
                            'arguments': [
                                        {
                                                        'name': 'ρѫˈѹǺ:ԥћҎɧӮ˨*˭\u0380фӶ_rҫʺȉŖĨж',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǑǮѢҙɀ&"ɴԠѪŸІǴЦŒЎ\'ѩѕȐě',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѴωƜŢԥИćѮϡ\x8b',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'þʅʌёƳàΤѼδӅƤȜƚԛ*˺ȈGЪƖʨŘǦ΄ʌϑɑ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɀӔ¯Σ·ĞŊŀ1ȏůŐƟř)ƜҭѕϩĭˏÁɳġӈɮԀϗӸƯ',
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
                'identifier': '|ʵʜʴƀ',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': ';є',
                            'message': 'ΰ',
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
                'identifier': 'ЫêЃůǞňʅΏʯњԗØάĒʦԅϥɫȤӈЋɠȱγɕʽƤŬҪ˝',
                'categories': [
                    'os',
                    'internal',
                    'internal',
                    'internal',
                    'file',
                    'file',
                    'access-restriction',
                    'file',
                    'internal',
                    'configuration',
                ],
                'source': 'чǺӠѧ&ȇԖśǩYvϚԕ˴˚ʖԭОҎʗǳJõΨ>ЌĺɝʒŃ',
                'messages': [
                    {
                            'catalog': 'Ȟɔ§І\x8c\u038bЇҌѿŨ\x87ǮѠ>\u038bԘɬϳêĈǆкӫɲΉӴ[вƺ҈',
                            'message': 'ѪҪȏԗˠѦǮɛҚϰƼҐŝ\x96ȝʝԗ\u0383ģÉӃŒ,`ӡҨ±Í˝À',
                            'arguments': [
                                        {
                                                        'name': 'иÿȫǒϊԦǸȹ·MтӐԓӜяϐȷԠӢǁʥԅ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƍѹӛʽɰEѵūǧѱ÷ƉԪ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185621.269909:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ыŵȖϖЏԬĉԉƝĸɎĤϛ˪ɔÏɊ!ȼʉʈǄ˸ǈ:ҺʄɄȴɵ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3281682290918877760,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȧ\x92Ѕ˅˯ƪʖȰӃŞӼϦͷԀɴ®ƭʞ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185621.453503:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ũЕĺñ¶ΈЉҩяbʵҕƫ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӧƊԣĀ˦\u0378ҋųɂӫԐRбұ8ˈðșŇƎȼԕʨÎ´Q9ŷʬԂ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƓŬȃԪŨӱԖČјħąʊÜӈřͼàѸ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 420189.46008372307,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ґĩǧÐĸPҁʙЎȓHɪ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΆǑǒӇȷ\xa0ҭяѾΒéɯâʯӮҺѱкġʠŸ4ĩĤȱǂ\x8c\u0383Śȵ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƇîǊ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ħӢϙЄƾΡȇ.ʁɃЋѣɢ/ЏBͼɮцʦŠϽҵԭιƧӘӉ\x87ɮ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɨǪν˰ɢӟѕѴőҿЕѓǝƫɥqЙĕӪȆұЎȱ§ʘ²ˑʝʝʯ',
                            'message': 'ЫыЎɤɖЄǅɳýϛÔήÂԘúĎϢͺіɌĩU\x9cȬЇȲȿɮҨǠ',
                            'arguments': [
                                        {
                                                        'name': 'ϾѐԭξɦԊąƃ\u0379ɕʄѪϻӫРˇˣǖ~ƵеίϾǳҫʷԫŤԡô',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƾ^˚Ǧˇɩŕфƚâԛͽ"ǻǲ\x8bЗŬҥÚĸÊ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 890971.4799777988,
                                                                        },
                                                    },
                                        {
                                                        'name': 'КÀhôȞϗʱǵşԃĬԑұPȀǈ\x81κӪʹÝӺʾɆ\x98ʳɔǘӬӚ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ύĄǉҬ{ѩʙΟɃrğ\x9aʨɡĐƸφ˼ǦϚЂŽѳÜӆʙȃυҀZ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 327038.61510230333,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x90њȾҔϿOȈɇʯěӺѴđęӶǜ0ÃŶİÇʠ7ʟħщԟìђė',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6348667321665050074,
                                                                        },
                                                    },
                                        {
                                                        'name': '·ĉɅэb ɭ˷ʖϷΚЪ\u0383ŒҦϳBΓɺǮźˮŦԨьΉƶӹπʈ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2432683014101267987,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x86ėΉťМ\x8fƚ\x82ȫΊцӁĨ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '˰Sǫ2\x98ЏŅӇыϻþʫʇ΄ƿϙӤK%ӻgƍϞǌƑƴϐНэ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӣÛҙƄоƝ6',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɨ˫ӞˤІҩŴɝ˷\x93ȠǔȬ͵rWȃϻД˶ƚβƚɆˇƣ˖оAɣ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185623.427873:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'jȥƘȶφɷΌʩzƛȥȾțŁƆģļώЮΞԝЋėÏη˓ÔƆϱΨ',
                            'message': '˛тű\x9fӷĳƍʹ˱įÎΖԤɸΎҥÿǕ2ÁʮRNǁ΅ΗԎ\x92Ԧˏ',
                            'arguments': [
                                        {
                                                        'name': '"ΙԒZƮþ˯˨ȪщъȒԆфoҷRԂȫƛ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 274866.82282512763,
                                                                        },
                                                    },
                                        {
                                                        'name': ',ψɸнĂƗòӶ´өӇҜĥѻ\x96ӇȬѐİȊŏΰȚ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӊȾԝ;М˂¡\x8fӆӉсȲ˝ŒÑð³˛ӲȁψʺФ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԉ˫ΦɦН˫ғɭƵзɡїϑĻ҉ʾʞԠĞͳāɞТµ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 227641.14963837515,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ò1ªʃŔ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʽϜʭ¤',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 698753388894784303,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӼРθȃҸњʒѷӺГǫvҙаңƑӍ¸Xȝьҝ҅ςҳżɘƵĭN',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɫQwâõÎ»ˡжÆϵҢɌ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'İțίbɐȔЩPĖαόǯϘɱƯζǕOƈŢғԭȘԘñ΄ȏҷ\x94î',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΰˢĉŸοчLō˸қǻÔЕ´ǚŏҚ±ӡʣģ\x8cΖɠл',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Έҡҭƾ»ӯȾЏǖȆ»őɱÕӑ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȅӺtЏʅκʆΚԝƢǘ˗ĬȶİԠЏ˥њ˭ʅΰǡԂӞκ.ȴ\x85ŵ',
                            'message': 'ɲ˄ŷИñĥɦȦHϳɾѡɳѪĦϺԬʍҋÐ"ИпǖŖō\x80Ȍt\x90',
                            'arguments': [
                                        {
                                                        'name': '\x90ІЎʴȉԇǍˡѢќƧ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3511720137762593818,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȒçȂǾ=ӢŮ»ˍԇeӵÞӱԚԙ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΕÑʒӪѧƥÀΒ>ΟȴȞȩʤЅɳԜЍȈªТʃϭҒϚЊËƆĊЈ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɨ˓ȧūeԊЗђnzȡλȜƩϗʧԚѸJԄԔǞЬŔϤзnèу\x88',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ïɂĻɕ\x8aӞԌϨͿoöӛìѷƈȼ$ҍåͺ_Ҧ|ѽȫ2ӁɈ4ҷ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѰϡδɌђϠ§ǃҧɪłʢԀҔǺȏӄȧţÞ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ы'Ǳ˰ҝЕ˅LҀʴȫϜʑȰԮƸŦΞɳАEϖιԧġĿȴѼю\x98",
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÏŰƽÍпˈɹӰ˳§\x8aËˆÍӣ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 701210.4252301442,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΈӂŖβĆӋщŦYӼXӇϘ҉«ЯȡǤáǇƅǶŸξҴȏМƬ˲ԑ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185626.593908:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѵ\x89ɾҳÿ˚˫ƸˢɃȊƈӖʨұíөeɅ/ǋШѹԓƫȄǷԇΠǊ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ͻώҒʘƨӺџѳkYMǩ¶ɓšƓƞӐƱΌͿŞŰƩѳÓӟkπǀ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɌȿЅˈĞɼΫØɞƵʾҮͳλωǈͱΥŵ¤đĶǟļxǓΒνƘԥ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185627.462346:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ϸ*ƝԫВП˽ʡǺʅʯԏƟ',
                            'message': 'ǱɿНȉϑѲͲͼǒӑҚҁМȜßϜņęЗ±ԀԁƵʋ҉ԈÅΊδĊ',
                            'arguments': [
                                        {
                                                        'name': "ǕƷ5ϭ'ҭϷԂШ\u038d",
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -48034.17288090761,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȂƹɿԬҘÒ˗\x9eŕΛШÇ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ä\x85ʵƫɹɺǽˡǂфʭʺƷƯНȵíĕѸĿ°ÛөҞΧУΠ˘ӈì',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԕǜɫǎƠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185628.096551:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԜτDǤхԟ^ӶɹʴàҿĀ¿ƲǛÌ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȉǏӅҲθРčĩӁʫїΫƿνˀʐȬϞСΫѪҸBǀģȀƠǅƅ\u0381',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'șӔѹ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԋǱ\u0378Û%',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4624167799536373145,
                                                                        },
                                                    },
                                        {
                                                        'name': 'уЋұ1ȶԨҚĩǼˎҍƠƋȇөΰɫ˫Ҕ\x89ЏĬȎ\x94ǯԡÇ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĩͳːǐғiЩЭå\x80Љ9ϓˣƃά\x91ЕАũƟӲΕ ǢGЅџщη',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185628.730968:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԦϱɂȮɡ\x8fҨЍĢoɔʳԊԎǇĖĄɒД˱ӭ|Ϝ˗Ƀʦqϛ\x9eȶ',
                            'message': 'ԄΕɮǮъ˻ɪϩҶ\x87ҏʺЅ˃ђҹgҲќŶΛ˽>ˌϡȸɔҷšſ',
                            'arguments': [
                                        {
                                                        'name': 'э\xadɌ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8dίĆʔǀ˱ȟЁ\x94ӘʖҟśȎ˙ȔÉȽşθѮˉѡƯэ-ŔîԃӠ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8890779948740559730,
                                                                        },
                                                    },
                                        {
                                                        'name': '4¡ǂȬϓѸЋіǵʣϪѲȷ˲\x9b\x81\x81įȦ\x81\x83¾ŨԖ¯ӻĬϫӯ´',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԛҌáԭǡƆȨˁ1ɟθNű',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2036685119869129389,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˉƟʸѩĩҲɫʧĥɧ\x95ӑӰǕ˕²ӐǊцŅӉ¾\x9fʙ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȎƎҰγɡ\u038dúâȓǗǈƓЧˬKǗ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8124167190909782173,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϓВψŌ3ǱȓșčĘЎә',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ń¢ƗʘԎ˓űάɔȋ˨èÑΡÖɶɌųУˡʗ˽ӳԕ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5043297825217555034,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƞȀӈÊȈӃ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԨАùŒ%ȟҚŸΊδȡӪǳÕƻΕ£ˁоZȊҽÉйőɑˇɊӹɩ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'λ1\x93ɘԡјͺνϮшſәžʤ*\x9d΅җ˞ǠɥѸџ[ІǀҗЭʲ$',
                            'message': 'ƈͷϮ҇ɝaŊǺžöȿ7ӎǼҏj˝ʹČçáʃаƺʅƫǩ\x98Řç',
                            'arguments': [
                                        {
                                                        'name': 'ϧƏƖŪө\u0383µЙЎǅƞ˥ξҦΓ³ŬƛӮŀ{дɤǶũ?ҧ͵ƭѾ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185629.975784:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǸЧLƷЂҙ˖ÏęωeŊɻʱѐēȉɰ¶TI\\ƁȢˍʦЯɂϋɝ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŸrΧҋǑщǚҏ¤еĞʸ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185630.129246:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϳǣоȘEμ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʺʏĺǻɾǺÊӗwуΠԕĒπ\x8aӹĀΈȕҿɿˣԣ҅ПЯƪʬ\x8a3',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɘżŶǿϔïǼѝɝ+ʽɌǟíƋϲԭ\x9e\u0378έ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĶЖVãȆȆkӢ+ǍǪƍˎд×}ɚʈ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȌҷrюǋȼϮқ\x8c',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Κĸϻ˸',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʛƙϑRÀɼʱʖҮҸ\x9b&ÑЍƽτөƌńХ2Ėҽ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'U˼Ăoʹ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɆǢԌÏӴѻαKƊąȬʆτι\x8c\x90ΉǑˉǂˍɪрɟʄæ\x94·XȆ',
                            'message': '"ƥу÷юŦ\x96ҌȖʙNВȴѐ6ӣȑ£ȾҁͰξɅƶϹǩDFѱԣ',
                            'arguments': [
                                        {
                                                        'name': '?ӮɇʇåJ½ɇŎ˶ŵвÄӸɋЙːдγƒ*ȥŭäǹƊƟǦ˱ǡ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4586283732316112172,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԤŤԃđԑlЪѲϩʵʲСЪԜϞŢˇĳ˶ť\x90мŶˊȑjǢ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƌÃшê4ӬǆªԜʑŎђȑҕҫǲЂҴʶӎЂ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѵ˒ҡѓͼÊĄβɸ˻Ѳū\x92\u0383ŕĮ\\',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 422652.9397014609,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ď#ņ\x96у[?~ԧŀϳÃȭô¢ȳЭȓͺȹÆǁƍ£ъˣʿsǩř',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0380Ɣ\x81ҹŦоƙ\x8eǀťûңıӏ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 960149.8278229157,
                                                                        },
                                                    },
                                        {
                                                        'name': '˥γ\x92ßN\x9eΐƩɧːĸЭƞƍГ˼Ŗ|ǙԞş(\u0379˨ѩɜđƚ˵ѐ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'χмиΌɞӘƓԓǺϽʺϪƴӧ\x8bĶȞɐ˲ԣυ_ǐȿʠΆΓ¿Ƣȣ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЪÛŶę\x9cԭǁĲΑȂξϸƐǯȚ¡ŎˌϸPȣ˪\x91ϩé0ÕӜ{ɧ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185631.704720:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ςͰѵϜЁƶζҟL',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4311130193225279521,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ͻǺÅǢġűǏŉƲңуMXʡѵ˫ʅɼɾθȦy4ŶԋĝɏҶшʝ',
                            'message': 'ȲɅɇ°ŮήқνŰ×ǂȅƃәʀѢϏưʪȃƣƗƬ¦Θа\u0382ÅƼɧ',
                            'arguments': [
                                        {
                                                        'name': 'ΜϱǨҿʇΦˋνʤĥхʭĳˉŐĸ\u0381ǣЫӃȱ\x94ϒǪȓʚϊwǩç',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185631.930213:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǃĮǬʶ\x89ʐZ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '®Ŏю¾ӥϼџȋÌɀƋЗɘԗƁƯļобĚò\x86ǽʌӫӀǘéĈͺ',
                                                                        },
                                                    },
                                        {
                                                        'name': '\xa0ëńȭµęʋϴŇ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185632.072067:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĩ҅;˛˰ԍЗ˭ĈͼƮ^˗ȈϮĺÞҠοɉќϰŶӰӬ˸ÉɽɬӖ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x92ǊςѺɔѯUDǘğʟҚĶΓ\x88ǵčÀxō\u0382ődǞʲŌͱ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԖҼƙGʓ}ɄħĹĐ˭ˏŮΧУ7Ŝё¥Ԉϙ·t҃ƄǃԜƭĞ\x85',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185632.319379:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȒɨşɬƸáѪ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185632.393026:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĊûѱzѫʤϺȄΓΞӌ\x8d\x98ŮïУжγ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˹įʓҘϭ²҈ĐʳŐǮ\x9aŽƌԍóBӳȩƸӓӔğѣǧʒ\u0378ëϠΓ',
                                                                        },
                                                    },
                                        {
                                                        'name': '˔ȶƥʋѲľҲˌďόϤŦгˋчιȃӳɐÞƋ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӕö˕ɪ®ɝр\x7fʔÉMβȖŒȄϩρηԦŀ<ŜҝŷԃўƊÉĭ˭',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Δ҉ǹÁȗ{ԣʣĵɧąпЅӼӌӗ˼ýќВʎƺϋηӎΝǱĢ҇҇',
                            'message': 'ʲԮʁīǥĩҽҍϔƝɵĄşȌŜũХѻϧМ˸\x9bІˬͺԫĳȩҿˌ',
                            'arguments': [
                                        {
                                                        'name': 'Þǃ8ϮéʌʐηԡԨ\x91²µȹ˄Ś˸ВƾʡˇƒvɞÞӉɡW8Ԁ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʉǙ\x8fǹ?Ǣ˃ʥгȴλ˾љ\x9cĭѵ}ˮͱ\u0380ľˎԛΐЬãӁяʩƪ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 468609.8234153426,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϭѮƈāƳN˯0Ӕ\x93ӲF\x9cɌ\x86Ӆǁǜ\x82čԬρǕӁϏųƁͻ~ƞ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 173265.22186442727,
                                                                        },
                                                    },
                                        {
                                                        'name': '\\ԨưƬҀġϸǥėΖɄ½ӇȇԄЪÚǢȡŸ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԉҜҀԒĜɹìѫÅiŊӠÉɍȁǦzȚɯɣëƅ\x91ΛЅ\x86ԐVЧǴ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϹЄԕɱÈRҚĦӮЇѩì˻éʓљɴɥЉ\x95ƩѯɍƝɋӭҟКʫ\x8a',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185633.236772:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '×ϖҘǒŵ˦А˾Ō˲',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˾ʨҭϿ:ţʑӮ˴Ѽѩ\x85ŏ¦Ǘ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŏǀȖцƺƒϬɶјɰ;ʝɌqŻƑҤѳпDĶģҺЁɽĽa˝ԩ¹',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʝÒѿΌÑщѶȆˀНѬǝԍřѥȇӉдңǑҏĕŻʘҖ|вɉӁУ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϘıθҟYё˓ÀƮǀƹǄԙ|ǥ\x8c£ɪє',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -1254.6678752812295,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŻˈЊǾ,ͽϿˁĽǟҭʵĶΠÇʏΛĬȌƄˀŦ',
                                                        'value': {
                                                                            '^': 'datetime_list',
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
                'identifier': 'ɍϾӖǐǴ',
                'categories': [
                    'network',
                ],
                'messages': [
                    {
                            'catalog': 'ϔƮ',
                            'message': '-',
                        },
                ],
            },

        },
    ),
]
