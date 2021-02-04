# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-03T21:03:09.662167

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
            '$': 'ě˴¥%ԤР¢ӛΈƸjɾũ¡фïҮҏɖνlԆµЃϔV˒ơӰє',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -3440386911712653757,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 151254.74869922953,
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
            '$': '20210203:210309.585921:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'iÜϒʺШuѵέӀ|њҞːŶ£ӪʺϲȵҡȼƼſį¼ɓоԏǟʜ',
                'ԙ\x8a˽Ţȗ\x86ӿȱәȵ\x94õȷĕͼǙƫӰЦžżν\xadԍǷĜ£҅pҮ',
                'ĳRӑO˹ŘǦҤÕ˚ǹǤƪ҂ʍČΎҞєCǚЛhǯϖОŪӹѭϤ',
                'ϵÿӰ,ÞȒʉϥѠίˏĹɂɷԇ\x92ǩĥŜіś¤˹ϓǲӰĶʽс\x87',
                'ÃĬƮÎȗӰÙνΈϮɿƥǛɹˉˋԋȜɥŨŞųӄɀƙʲчǸӌԖ',
                'ǿλoǫØĵƜӚрРŇáɌƓüϣÒïғÿʜБºɊɏ/©ƾǙȳ',
                'έǴӋΜ\x95Ü8ϔƆƒÁì˄ʇ·ӮУTƴǏѪTý\x9bАȤƲъЩ\x80',
                'tнћʉƑƱƉζƶˮњҡäƶîJΊʂǦˏвӧʲˉɍ\x94үѦ҈Ļ',
                '@ҞЙīŸѐ¢ƽ¯ωӧɎЈɂцƝЖǔØȟů\x85ЉΎʝƛЧƢÞ˪',
                'ĕΜ˰˂žŁǫϚáȚ΄Ѕ\x9aʡûǑ\x84оx҄ĺІ\x9c}Ӌȓ°˅ɆӐ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                7371454988190328868,
                2385144564133470797,
                2111922246227151323,
                5212806185079210652,
                3066754727520259314,
                6254089906431910511,
                1639604892803755089,
                -5826455892820271837,
                -9006890801830929527,
                8802618307783648151,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                260909.2584742501,
                812993.9182285449,
                459929.78384127107,
                250110.13305497984,
                988505.9285320076,
                533948.0360609421,
                730474.0883930217,
                479.6479387390573,
                28866.913608612915,
                180306.56426446157,
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
                False,
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
                '20210203:210309.586870:+0000',
                '20210203:210309.586882:+0000',
                '20210203:210309.586890:+0000',
                '20210203:210309.586896:+0000',
                '20210203:210309.586902:+0000',
                '20210203:210309.586907:+0000',
                '20210203:210309.586913:+0000',
                '20210203:210309.586918:+0000',
                '20210203:210309.586923:+0000',
                '20210203:210309.586929:+0000',
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
            'name': 'ɂ²m',
            'value': {
                '^': 'datetime_list',
                '$': [
                    '20210203:210309.585587:+0000',
                    '20210203:210309.585605:+0000',
                    '20210203:210309.585611:+0000',
                    '20210203:210309.585616:+0000',
                    '20210203:210309.585621:+0000',
                    '20210203:210309.585626:+0000',
                    '20210203:210309.585631:+0000',
                    '20210203:210309.585635:+0000',
                    '20210203:210309.585640:+0000',
                    '20210203:210309.585646:+0000',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӝ',

            'value': {
                '^': 'string',
                '$': '',
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
            'catalog': 'ΊԨÛųśğɔ;ÿ˟\x81ǯԈżEʵƃӧτΤȏ¨ĚӟЩȳӧBUΐ',
            'message': 'ӓԃϭƟѠɏ\x948ѶˋǾȆ\x83ΪȞțǈƶȺʈʖ\u0382ɮ\u038bі˷ľҵȪ\x8f',
            'arguments': [
                {
                    'name': 'Ȣ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        8764580444878058569,
                                        -2761365710720903274,
                                        -3186638868858028936,
                                        -6984251948745277790,
                                        -6251512185488318565,
                                        7564068467343647547,
                                        -6567992854124985765,
                                        2206138799325184440,
                                        578538654344875869,
                                        1483815571582243735,
                                    ],
                        },
                },
                {
                    'name': 'νƄŭǸϾȳʳгԟȱʉNԀċНŤȚȹÖŶ˯CΆӄӑƈƾψńǬ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ƨ҂ϞÿɃ˯ȕơԐ<Ʒhƀ\x8cѹ\x9dŝɳɽDɯ[ȗˬϣËp&Ưΰ',
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
                                        True,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'öӾũȠɋeş0АӣӑǃѪԞɀӅүǗͷȱƕɇʄщøĜūҔȈȳ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        -56661.95258907396,
                                        -939.3536520360649,
                                        928584.8343571058,
                                        702310.6401764131,
                                        -32216.76887603606,
                                        662577.7412230844,
                                        46485.28193372319,
                                        8594.634163322597,
                                        246554.70388829272,
                                        728793.7818385682,
                                    ],
                        },
                },
                {
                    'name': 'ϒÎ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        1592849583862238837,
                                        7574194246118897901,
                                        5150599361734580391,
                                        -7494688491321397067,
                                        7690966720613619141,
                                        4549628820473540011,
                                        -4169773462239519358,
                                        -5179834927952320487,
                                        -5960260913018999617,
                                        4099841512269055134,
                                    ],
                        },
                },
                {
                    'name': 'ӭŘҷǧS\x96ƈɟɠәЋμз%ЙԌL˶ʏЏƋб\u0378НɩŘoд˃Ʃ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'âЫѨĳ˂Ό¢ŊťjΕȌ_Ξ˾,ϠZвÆ\x84ȪԮơԬͿǯȰ?Ҋ',
                                        'ˇŇ\u0381Ƣ&ĺ}ʸńãȇťɪíьǛЬξyљӥŸƶšБʕӵҽðӣ',
                                        'Óʦȹɦ>˃¸ʇǻкʀƫʚȏΔǰ(ʐ·˟ġƜʄ˼PɗǴӃВʴ',
                                        'əͳāҿ¬ɬʹ҉ºʫČŇ8Țԍ×˂ȍЋǇЊ^˧ʝЀǋˏfіu',
                                        'ЕҥҁʂˊÁ~\x88ĨБǨę¬ҹʞѤ²¾˄єʳêƽΘʓԌҋԏɴ\x98',
                                        'XҥŲ6œKӨόŗȭ\x8e\u03a2ҭĐѢТӨϣɋWÁǱϒξǓıǻȬќɦ',
                                        'ϜԛѴͳȣĪƿŰԆɾ$ȏӝyԚӠȘϪʰӥԒ\x98ҏŽǽМС_Cѧ',
                                        'ЋΥȊǦSĖȜ5Ģˈ¼С˂ϕХƵɺԋęŖ,ӼtΨмƼҪɩĖԥ',
                                        'ЎϸӸəԒȱȎԎ¤ɚӵǆÕŎūͼ-BƜΠĴƒ˺ˇІƕÝßЄʶ',
                                        'ňƕˉκǼɗԛ˃ǻ\x9c\x7fdɗˢȂɕʩˆč4˕ȼĵԃ˂ϯΧЀѲɽ',
                                    ],
                        },
                },
                {
                    'name': '\x83йŻѝÌɘÊҪӐÓ¸ĳ',
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
                    'name': 'ˀʁƲȥцr͵ªßӄ˩ϰƒŀȆҫЁͶǮɟÄПЧ~ҡѤȺ¨У',
                    'value': {
                            '^': 'string',
                            '$': 'ӜtˤȢТ«ǕПÑ¾ŧ<ɍҜʯƸϷªЫĪΜȵ\x8f˗ŶԣλVӋ˖',
                        },
                },
                {
                    'name': 'ӚΥΩԢєϧǲԝϷȳʎşŷӴƀŇĭȶρԖԩ¹ԍȳӎєҵ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ǨƞóӳҾόņɘ˽ȍǇѠɿ\x86Δɐ´ϪƪǖNΒ˷ɉӁƿԁȇӧϧ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        True,
                                        True,
                                        True,
                                        False,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'чϘ',

            'message': '\u0382',

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
                    'catalog': 'üç\x87ĒʲʃκӷЉɍá˙lӥўīĭԇǵʖΤƇɇӥЁÊÐп΅ʛ',
                    'message': 'ˤĹǧҽǤӱάŔΗǎȾЖͷӗȑ\x97ɐͽ\x7fЛÇńӚǂԑʍư\u0379ʹЌ',
                    'arguments': [
                            {
                                        'name': 'aϛԉѦ˾Ԗż˭ΗͱԗƿДӶBʨѥ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210309.543795:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĊɳȏǍϩƵȉ\x9fђȞǅ˖҈Ӗǚ;ġːԒĚa>ʸʇĚα\x8fbU:',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 165839.07307518594,
                                                    },
                                    },
                            {
                                        'name': 'А',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            320831.52176734956,
                                                                            947470.4723018837,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϬԎήǉçȫʬӍƪσлҬˀİӐӲЧѾ\x94ũԇSҎӳ·ǪɂСʕԥ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            832471377371510711,
                                                                            3795615756641109059,
                                                                            -4546885293718445273,
                                                                            7895774442835815394,
                                                                            -6701447204203237799,
                                                                            -8371195113590877580,
                                                                            5023352533637165701,
                                                                            -4765777251317011808,
                                                                            7162318626476976148,
                                                                            -4907938646466321678,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѥ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210309.559160:+0000',
                                                    },
                                    },
                            {
                                        'name': '҇ǤƽԟьČϽǄÍǨʪƂǠ˯ĦśD',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\u0379ʌǣӋεДȝϲ\x90Ǜӏ§υСɳ;҇їԝöȝˁԪÛɿҰεǧɦɄ',
                                                                            'ƺӞȼҎǖÎӁŒ_ʢōЕΎӭ˙dƽƨ¡чƕ\x95ā4дƻĔtĖĞ',
                                                                            'ȘΠВҞ\x87đрԓӯ˳ȓȽϕҌӧÀЬΝѳłĂĉȗǸƹњԝҨӯМ',
                                                                            'ѽʁ¤ƄʍήӔЧȊǠԠʧͶӿЄóŽЦѳTыќщϪԧQSˮЏī',
                                                                            'Ԩ˥ЃƏˉÛЩƷǂϳԎђB2Ϛ´ƷYɪʀɭʔɶ$ίӟŒĂǙ\x9e',
                                                                            'Ƭы£ȅӲЯϛӳǱˣԚȿĜӜ˜Ąԃ˺ОmϷŲԨжĒǏɍεʳΗ',
                                                                            'яŧʁњюΪԡƵӤСуΔɺνΈ\x9cĈԞČҌҴȚϾLĸчԇɘлѽ',
                                                                            'ò҄ŀʅϩѲɧ\u0379ɤŔԕ˰ˣтңҽg\u0378Ѯ\u0378ǀԫĮΧŉȶ\u0382áƨˮ',
                                                                            '4ȱѲρӏͷоáԃÃСě˲ſƼÝӎʭJѢȲʪТȷҎĝĆɳuӨ',
                                                                            'ΐēҐΧĦ\x8cТϕ\u0382ņёˈȘӾǡɣґΘɚˁgɗŇ\x80ЅȇԥǾӴ1',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͲŬ:Ηφяη҉ҔвÿƟ1˯ţΐӲΝíÿԎʛӠϤĝϐŢ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 335071.0840246849,
                                                    },
                                    },
                            {
                                        'name': 'Hєʦї¹Ԩʥ\x8fϢǕÌ',
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
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȲʨьҢϪcÖΖҮѦ;\x9eſóEÓѦ˯*ÛӖo',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7086684196973000050,
                                                    },
                                    },
                            {
                                        'name': 'ʔ[èчŻѝŀоδΏɩčöȖ˷έƈ+уƔМϛʨȃȆ@ΜŶϢέ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:210309.560272:+0000',
                                                                            '20210203:210309.560291:+0000',
                                                                            '20210203:210309.560297:+0000',
                                                                            '20210203:210309.560302:+0000',
                                                                            '20210203:210309.560307:+0000',
                                                                            '20210203:210309.560312:+0000',
                                                                            '20210203:210309.560317:+0000',
                                                                            '20210203:210309.560322:+0000',
                                                                            '20210203:210309.560327:+0000',
                                                                            '20210203:210309.560332:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ěрǃԖϰ҃Ɏ¨+.Ӑ¸ǏFƗšӰШþ˱ŁЛ\xa0ĎΧЂǠ.ǩѕ',
                    'message': 'ЫϓΑʀϞҚͲ ŒǙFСŇmеΥĲюǙ҆Ӣəϸțқ?ŰԥԢԧ',
                    'arguments': [
                            {
                                        'name': 'ȇßͲмʪȺҹʃŉǇąʷϞҭȝǰӝ6ϽƂʕȬWӛȻūћ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 557801.0763874848,
                                                    },
                                    },
                            {
                                        'name': 'Ǐŏʀľ;Үť҉¡μЫϤν',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ήҵοЮĊGΊϼɭƔ\u0378ʙơʉӱһĖ+ǲ1ȵ¾3Bʏ\u0383йˏ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:210309.561343:+0000',
                                                                            '20210203:210309.561357:+0000',
                                                                            '20210203:210309.561363:+0000',
                                                                            '20210203:210309.561368:+0000',
                                                                            '20210203:210309.561373:+0000',
                                                                            '20210203:210309.561378:+0000',
                                                                            '20210203:210309.561383:+0000',
                                                                            '20210203:210309.561388:+0000',
                                                                            '20210203:210309.561393:+0000',
                                                                            '20210203:210309.561398:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǷŮģɂϽǋǗɻɌѣ\x91ǘ˧ĸÿʈ˷Ĭԟďϕǲzė!¤ӆnÿΪ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                                        'name': 'йȕϤԔЫљ҄эPŐ˜Ҵ[íɺ;˗CĸŘѕʈȈȴҹω',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʷМӬʃǃ˻iʁҀҟЈӮѱəԆʪГЩ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': "ĞƭĸτρʁҳμʁƮǓǟ«ўҕȰ}Õǵбί'ȤĦ",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '5ŦЏґԒɨМ3ɜŤҘiΜ(ӀʔԎȤƺǋ\x8bÛϼǓYʃÈȟYҁ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˃ƞ¡ҢϰAԄɚʴӱ"Г·ΪǒҁãȲȖM҅ČƎ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 721185.9685394458,
                                                    },
                                    },
                            {
                                        'name': 'Σ·ŊǗ҂ÉĈŻǠϝÖfӚЭʋw',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            964434.6305504811,
                                                                            436718.79298809054,
                                                                            168450.4541069636,
                                                                            312858.34778830386,
                                                                            477769.8197684331,
                                                                            58457.82441919934,
                                                                            661471.3401909032,
                                                                            771335.2095850686,
                                                                            983434.0108224226,
                                                                            883353.6057125559,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'qӥϝɱʱмέԩƌÌ\x99өЦh',
                    'message': 'ʣŔ\x8dτӃщԝЉϳƭş>ұӆѸĲɺϫѫӰĎǢеҖЋǂЄɯôď',
                    'arguments': [
                            {
                                        'name': 'ďʏђ˽˽Ȋã©э',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǥă_ȞΉүӎѹĸǱ·ôíǸİӋ\u0382ŕńЪЇϦϴŪvПԨ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȲԌǢţвӁϾŅРŚΤ%ŚԭʘӢ¿fɊԌΑ\x96ŗŪԩ\x86ϻɨΜѓ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3721816392717706716,
                                                    },
                                    },
                            {
                                        'name': 'Ťņ2ʑ¦ˬÕȸķǾѓˉʻǷҩͱӰȦȬѐðGǂƞ}ÊƪÉ\x97Ɠ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6111422048125297826,
                                                                            7552867918968117243,
                                                                            -3580811563809294870,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'έ¡˜ɡŘԎ.ƵǩȄǄЧʮɪϿȷ#ӂӸǈѠЈԫԔ¯ǯЕӱbǙ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 10432317046567674,
                                                    },
                                    },
                            {
                                        'name': 'Ȧʰϫȫєɚ·ϝǇ"ԙ˖Ъή\x90ǰЂѮήτРϡŬǒԢ¤ϯȐɊԄ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            139413.4379278554,
                                                                            666823.9791327395,
                                                                            135795.36780152566,
                                                                            -81767.83106583753,
                                                                            230609.8920487761,
                                                                            83440.92721630365,
                                                                            290591.4512272125,
                                                                            798350.8586122507,
                                                                            415181.70670402754,
                                                                            418857.2467796367,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŦÏνȴϸчøƒʆѮlʐĻǽòƢơǤҦÝUǍԙȚǯӎɠʕŗα',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
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
                    'catalog': 'ȏ¢ʡȇɰƥϐȊϟøӄΦƣмœҲƝǙΓηӋЊς~Ħġ¶ҖOѾ',
                    'message': '\x85;КоƢŋҭłɬѭǧZǷjӱӫfӡÒӀήӼƻѦMäƩϹŜȆ',
                    'arguments': [
                            {
                                        'name': 'ѰĢř\x91ǕōɶӱĮӈ\x85ӌЂԊŅǄɹѮӣӋ˲Пєȯ҈ҤmǛ˗~',
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĨҺЁŉȰǻѝ\x9aĜÕЩ˕ɪ¥§ӑ\x80ǠôмȠȳĶ˲σȏȌIÍк',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ͰƧνJôʴǦ҇ĿYɳȉϼη\u0380ҕĵǧǌҢ\u038dǔĺͽӃʧϼӔͼͰ',
                                                                            "ЛâƆ'ŀȜĸ:Ī҉ӱȘ\x96\x97ϘɠЈÎԛļȗǈҩџ˖#ɀ>uƔ",
                                                                            '÷\x83Ǡψ˧ѕʿȾɜиɴΛåүӭáѸЍĒĥҬƚƴͱҖӡҨ[ѝȚ',
                                                                            'Ìɥ2ş@Ϝԣĺǆӵћ\x8eʻ\x8bˆÙɁŬ҃ʛÔ˲ɴ»ϫǜѹѠϣȶ',
                                                                            'nƜÞʠ҅ʿϋƀҌŽưαŨɓЦŌώɹԢĜÿ¡ĹˣǶÜǁĂɬ҅',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǝZJвŎɀnУҾǌŒѿҮȹǺ7ʁʯ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ХѠʏǜĨԚNһǝǸˁ҃άŮĝɠǪɷɣҮĈȇɳԙͽŭÓϻºП',
                                                                            'ѓɺŵЦˇЯӛЅ˯ӲƯШӌΆȷĨaʪԭεĂǬͻУÓӿЦϿҔщ',
                                                                            'ʛǺñͶƣнåӔǝʐɔε§\u0379тȀàъȀԛѪҤ,ǭȈӉĘ\x8d\u038dś',
                                                                            'r\u0383ƛƊcԝѶ\x93ӥЂƵҞɟηЃύǀŌ\x83ӐϲʃԣύԅĩŒϓĥǱ',
                                                                            "ɊќԔ˝ʴВĦя´»МȆĎӔ¯ɄɰũȲǻԡМԁΤɤ'˨Ǝ˝\x90",
                                                                            '˪ϗɴҜÕк3Ѱ\x99ɤǧÜʼyɿӰ\x92ҳҜӬʤɷɚѐ{ȗŢǫØ\x96',
                                                                            'ӊԞҫӵƝƢˈόʷwΖŅӀdӐϧԉċԕӑƜАϻŤKюсϺΑ{',
                                                                            'ŗìӜ\x89҃ђҏ¦ώƗЖΓϛѲÿɥƟˎǵƤjġϐӑāϔԂЉ~ѡ',
                                                                            'Ǻ¤ʬƿͿʖGƧ¯βȔɍ:Ɉ\x85ϩόԂÇџɕĺγΡśɤǪǗӃξ',
                                                                            'ѧҁ˔ËıЛɿӭƌϩʩԣ˦˻ÁқѤϬƢɶʬӊƇƃԆľƞҷ`Ѣ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˦ȹˡșΌđǱŪ\x84˘CXԛŠϻːƯ\u0380˧ɠƭ\x94ř',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɷΟłӏõʡψʞǛʀΔ\xadӲāͽßũԣǅ˾ŴʳǹřǥЭ\x9fŜξ|',
                                                    },
                                    },
                            {
                                        'name': 'ĨĘˤϖʿϑɧбéЍҧĶΛ҈ʷɊ˅ŎĪ҆ԬƓƗÓΦǝˋϫȘǭ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǔɶΆϔϒ˹ů2º¨ԄҴɱȝˬӫϼКЖɬɁ\x8bȕęΛö˔ùƓ1',
                                                                            'ͿɆўĸʙóġʲĞΥ=șʐоʿȷćǒɶĤЯҽ\x96ԩƕҨԡБԟɦ',
                                                                            'ѬȢˋϰΔÚёɔƗҏѾ\x90ŘлŖԇƘ~ͽŲƼǸπ˄pӅΜÁӠU',
                                                                            'ҹ[ȹΦ\x96Ӣðљ˳ȦϿЎЙ\x9aˍʖȷ˫ҪΎŒˤ˙ӂēƉΥƵςѱ',
                                                                            'xɅͺ˱űԤǝϷĐOҨӘӢȭƂΔýϠԁаɤЫ\x99ӲΡ˹ʿɮ£·',
                                                                            'ɤĳɀ˛ϳǊȽƨǙɢӭˊ˚ь\x8d²сϐưSƶȲĺÏ\x83ўƯλȓ4',
                                                                            'јҾΔÆҨԣǑΦ©Ňѫ¡?ǖʀǎ-ǚǽËўͿʾˈ˚ёѐԔΠɿ',
                                                                            '~δ\u038bмäӻӕˠʸӎЄŷʍ͵ƦɅǋЋɩŒÚƾȭƢӋƅɫӀΚį',
                                                                            'ώ}ʶäкҹьϨɗ-ǵΔʜ˝ҍ=\x9bSƽɆιfXɇƐǬ¡Ȧɋѓ',
                                                                            'ǣҵ˪ƲMͿɹĢΎԞѠʠҺς;ͺŀčʋԠ˂ĥʩĤ\x8dеѱϯđο',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӮźTҢŠ˭ʩēÄξȇʒů\u0383ҷȸȱ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
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
                            {
                                        'name': 'ǘɼøåɬ«ϩϤʩ˒Ҳ°ĭ±ƿŵЦŶԐŕϲť˰ҫƟ҇Ķ¥\x82ȕ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8191792923124510791,
                                                    },
                                    },
                            {
                                        'name': 'ØΖǼŘż\x84ӮǮȪЬıѓȬðĂΩҹ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5429110622512548856,
                                                    },
                                    },
                            {
                                        'name': 'ѣǀǍǭԒ΅~ƈЎÀѭӰP¨ĜΰƘ\x93ƐͱӁӷƙŖЪkӀʠʏǜ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:210309.566836:+0000',
                                                                            '20210203:210309.566851:+0000',
                                                                            '20210203:210309.566858:+0000',
                                                                            '20210203:210309.566863:+0000',
                                                                            '20210203:210309.566868:+0000',
                                                                            '20210203:210309.566873:+0000',
                                                                            '20210203:210309.566878:+0000',
                                                                            '20210203:210309.566883:+0000',
                                                                            '20210203:210309.566888:+0000',
                                                                            '20210203:210309.566893:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԩǖϢӁȰԍZŜȥÉдɭȆϴЌƧԋ҂',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210309.567175:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΤЃǄC}ԃїΨȥӢУĞѴ7ΎαϘɾιԢûƥԧФӊǘɳȴдҜ',
                    'message': 'ԧøĆǼ˚ћ˲ɗёԨϊƮл˾ŖßǿʛɆ¬˖\x99ѨԇӸñǿÈʷʑ',
                    'arguments': [
                            {
                                        'name': '6ˡһрʅͿǈ\u0379ű˳ϳʝѤxɔɢeƣԈ¬ΪΩφѡӵәȚҲx',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĩˢɪɅӛуŀɄǲӇȼĠʿҁ˃',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʻ£ȹΣӭƗίɍθԩɫǳҰȰ˚£ǹɇĳшЇ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4472464817571751155,
                                                    },
                                    },
                            {
                                        'name': 'ԒҬʨҌm¾ơˋʶѭѷÈҬ£ɠźőĲρЕΐȁθҒǇȁƛ]Ѻέ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǩˀάѽǭѹÄƵĪǗϮ\xa0ǃОþȠώƛ\x8cėѺƶӂҴɯ©ɻ\x9fҬˮ',
                                                    },
                                    },
                            {
                                        'name': '˦Ԡïƥńүξ\x7fǙ~ɂԏͱάƾʜ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǒȡϢ\x8eʆáѹΟαϖ÷җɽñϦAȦУΔϠˑɂщȴΑmкĪŗǏ',
                                                    },
                                    },
                            {
                                        'name': 'эΥλѳҌ˚£ŝȻ҈uŁѝĆҸʶķưÁѝƩҊÁ`KҦ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 466573.0550427409,
                                                    },
                                    },
                            {
                                        'name': 'ĲҮ%ҰЃ',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѵχǂʂƓŌҷÅѕ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -404824192260277749,
                                                                            2373612408172572691,
                                                                            -5044157006896004091,
                                                                            2883318486754010809,
                                                                            3267245836333882694,
                                                                            -3825895655736371657,
                                                                            -468162176723484881,
                                                                            1193671383456647006,
                                                                            -5596880041883302887,
                                                                            7695033132662675325,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʌѶИʝ.ӼȠ\x88ƦȎâԕǒèƑйўǗǋǻçԞӃѝɷ¦ãԧ˙Ö',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŝĿͰʌøɟ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 213785.05392444774,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˕ūǽѣ!іÑʣŰpǑ\x86\u0383ũȄќ·AʳѷŵȼȈП\xadо"ǃЋ\x9b',
                    'message': 'Ѐ҂ʚѐŅüˍДĈȄÆ¤ńӳĚɺӚȯ8ƊύθkΨЮǌ®ѠӋΞ',
                    'arguments': [
                            {
                                        'name': 'ģ\u038dǽŕĂúӗõƉшιӗø',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¦ǘ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7636919218920574734,
                                                                            3559543697628958734,
                                                                            4939488322504458597,
                                                                            7909582330028185370,
                                                                            3244006438785262811,
                                                                            9079365928259434746,
                                                                            -404298415436919622,
                                                                            135521860527496101,
                                                                            -7876291203929047307,
                                                                            -1758336917364631597,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9cєѷǶԀтöƲпӍŇψË',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            835085.891216801,
                                                                            692499.7326145887,
                                                                            982123.1163553807,
                                                                            917767.4551054628,
                                                                            -89049.37126820456,
                                                                            -54876.570061252496,
                                                                            242453.85423755756,
                                                                            15284.84754247991,
                                                                            -62791.29072916739,
                                                                            156023.78573177705,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʮØϣϊӺѪPΖĻϘäʫ²vƼťɿȀ˕ƫдŎȼ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210309.570501:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x88ĩ\x86ŭŨҍƚć',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210309.570651:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȅπ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -28961.49994635285,
                                                                            511387.07060494495,
                                                                            155612.90324765115,
                                                                            925883.8110000183,
                                                                            278683.6096288136,
                                                                            572435.0353934094,
                                                                            809121.1896961295,
                                                                            111863.79043975589,
                                                                            279352.50498615915,
                                                                            131229.23226791306,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԣӦɉŌǩӞΏʓҶƮ˫ҽ˘і>ºâɋɲЯ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˦˕h',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Pħ9оТΰϴ\u03a2ѸáǣȋɱѲŹӯkӷӥ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '\x89ǝԬϯɃԚɧ<ЏƞΏSɑĦһ˴ʉ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˸ɰǮӉΏïҴϽ˙ŽΚƋѮȤ\u0379ӓ\u0378ɮƻςĿʐ!ŊɠèȸɣāЀ',
                    'message': 'ųĈ\x8bʠ˨Ҵӷ,òтѲƋтɹ\x85˻ơùϏKɚԁɗѪɥԨɱ˗ҫό',
                    'arguments': [
                            {
                                        'name': 'ȉªűǑңſӼȴЭ\u0383ԦíњϢӘ\x89\x9cƟѹƠώϟӰπӡЩɲϡƇӴ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:210309.572985:+0000',
                                                                            '20210203:210309.573022:+0000',
                                                                            '20210203:210309.573028:+0000',
                                                                            '20210203:210309.573033:+0000',
                                                                            '20210203:210309.573038:+0000',
                                                                            '20210203:210309.573043:+0000',
                                                                            '20210203:210309.573049:+0000',
                                                                            '20210203:210309.573054:+0000',
                                                                            '20210203:210309.573058:+0000',
                                                                            '20210203:210309.573063:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĄШňŭ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 644244.0158963184,
                                                    },
                                    },
                            {
                                        'name': '-˯ѩѢӺѲғѐʑ5ħɥѼňаËӡȼӹPƋê¼ѺIʵҜǽвɪ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʔ\u0383ӠɎӯќ\u0381ȨΑÕĤɃqǃΊ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:210309.573673:+0000',
                                                                            '20210203:210309.573687:+0000',
                                                                            '20210203:210309.573693:+0000',
                                                                            '20210203:210309.573698:+0000',
                                                                            '20210203:210309.573703:+0000',
                                                                            '20210203:210309.573708:+0000',
                                                                            '20210203:210309.573713:+0000',
                                                                            '20210203:210309.573718:+0000',
                                                                            '20210203:210309.573723:+0000',
                                                                            '20210203:210309.573728:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƺԘʝˉłʨ ʱԨȕžӈϖSʰVYӷɔóYŉђΥɇΦļ\xadϚͱ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -90324.35329313879,
                                                    },
                                    },
                            {
                                        'name': 'ΓnɞͲГƔΨӤӻƑeίǇԑȬɂƠаǫԌ49ʏˉҧʷµƒѹØ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:210309.574102:+0000',
                                                                            '20210203:210309.574113:+0000',
                                                                            '20210203:210309.574118:+0000',
                                                                            '20210203:210309.574123:+0000',
                                                                            '20210203:210309.574128:+0000',
                                                                            '20210203:210309.574133:+0000',
                                                                            '20210203:210309.574138:+0000',
                                                                            '20210203:210309.574143:+0000',
                                                                            '20210203:210309.574148:+0000',
                                                                            '20210203:210309.574153:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ñɘәȼˇԗĢˊĞ\x9cΣ҆џԂ±Έ-ɥŋԎĤţ´Җƽ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϥĿџˮiϢђǦ¼ƝүĚ[ԚҫѵԒЇę«ӝ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210309.574511:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʖȰѻϲʈѱŚʻ9ƾɶÇ˥Ѹ˵ԣNȍȳҧĚЍjEнƝяHǮС',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:210309.574654:+0000',
                                                                            '20210203:210309.574662:+0000',
                                                                            '20210203:210309.574668:+0000',
                                                                            '20210203:210309.574673:+0000',
                                                                            '20210203:210309.574678:+0000',
                                                                            '20210203:210309.574682:+0000',
                                                                            '20210203:210309.574687:+0000',
                                                                            '20210203:210309.574692:+0000',
                                                                            '20210203:210309.574697:+0000',
                                                                            '20210203:210309.574701:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȾϟůͿç',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ХƇо˥ɻĝπлƃś\x80Ƨ\x94ȘҌȌҲ\x8aСȻɼԩĴӬѝžOӸώĶ',
                                                                            '{κǴǚůª\u0380\u03a2ĖӒӾЄÙӨďÐgÏǬ˒ïɎÑŦ˭ŧÔɨɈǩ',
                                                                            'Љ¯ȩ˟ü|ʰȢqčϵμŊɟζӢÒϺȅ^SʽјƌˀƨßЛǷӅ',
                                                                            'ȔбȷŽȒάϘ4Ǵǋîéǥą˧ȂÊӝ¯ͷԡӘґǨʢɐзϝ7Ԩ',
                                                                            'ü\x8eɄѸϤ҇Ȍʃóĩ\x8cѾӈҽҒԡ˻\x94τɝȍǋĠǾyěϝϜǇϞ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ʊԉʋɑ˘σǀӳIĚɶſΒbŤҜѰҋ©ӌÆԟ]ʠʖőúϴѱť',
                    'message': 'ȰЛӜԍˌ)ҤŝlʹЗʈԅͷȪңȘʞęѐвyңҽӝʪѷʺӍБ',
                    'arguments': [
                            {
                                        'name': 'зĆĵ²ίɐ»ɇǺȸΥ\x8eˬ+ҡӴʫˮŚэÂІΘůǫΜŅƻːİ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:210309.575653:+0000',
                                                                            '20210203:210309.575666:+0000',
                                                                            '20210203:210309.575672:+0000',
                                                                            '20210203:210309.575677:+0000',
                                                                            '20210203:210309.575682:+0000',
                                                                            '20210203:210309.575687:+0000',
                                                                            '20210203:210309.575692:+0000',
                                                                            '20210203:210309.575697:+0000',
                                                                            '20210203:210309.575701:+0000',
                                                                            '20210203:210309.575706:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ìŠǭʰ\x92ʓϚϬ§әśːцǵѫԅԦƴƓԏæԫǄţǥ˙\x9dҚωɹ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ͽӴȸƷОӠԅҺ5ЪѢ\x87ΝªĚКϒϿǴǇǱċAпВȞʌɷйP',
                                                                            'УĴMΠԀ΄οŏԑϞķ[\x8c\x97ȗѻʊџ҂ΧϝЇǮà<ϥӕǢǌ\u038b',
                                                                            'ĐӇ<Āųе˦ӚҲǕǰǫϪсζƥʼфɼφɟςœўȋ\u038bУȲʛˑ',
                                                                            'UόņƄƞʎҴ҂Ø\xadʍ\x84ӨԘɋƃąˆ·TŔöӼ˒Ġ\x83\x87ɦĳż',
                                                                            'úšu˞ͳ"Ŕϥα«Иɣ@ķǒʌțҐϱ˧ǙүӵӺγϻŔıԐƅ',
                                                                            'ƍθǶħīɉÜΓҫ¼ů&ðŬɢʧÎʎәԗļχȀкӺΑ\x9fʴǷ"',
                                                                            'ƯÖ\x81ƏʬβĺәήțџΔ˫mλΦӭɽЅԑϛ\x9fΨƐȊĢҽ\u03a2϶1',
                                                                            'Ǒǚϓ\x83ƖȔͱ˸ѵɩȮǓɻΪǅǓĔη\u0382ǦIϾ½\x9aѰԘiӾƼӊ',
                                                                            'ѮһүСĺ¾DӺЇҖȃЃϣΟǙʏǸЈǛȘˠ\u0383ѓÀĜĊÅѝŮϐ',
                                                                            'üÒѭʲ˽ĸΪ!ΎєǭцʠԮŁǁ϶ϛ\x82čяe˼чćΓƦɶԇƫ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǑħҞғ¨ɶɒƻЅԝЗʿɐfKѣű',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210309.576375:+0000',
                                                    },
                                    },
                            {
                                        'name': 'кϹµ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210309.576862:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ɏ˚qҽƸԄŨǟӿϽԮʴʬѸǫγϾӀ²\x88·ˇˀ˅\xa0ƓÒîЩҭ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5474650327852728142,
                                                    },
                                    },
                            {
                                        'name': 'ҫνúɦâȻØƸѧȹ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6500695683904999289,
                                                                            6354670786826549021,
                                                                            6043690485611527353,
                                                                            8896436363086165578,
                                                                            -1026372722527118479,
                                                                            -7655229516614684232,
                                                                            7829657077871256110,
                                                                            -6563767718842326491,
                                                                            -7718861742640666447,
                                                                            -5626037028893976628,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΝҧҘɗ˸*ѵ˂˅ǇȋѪț-ɝ4\x93ѯӯȆғИ9ǖʭ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
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
                                        'name': 'īҿ˹ӇζϨȃͷȓǓδѿȋϞψȫԢ5ŲμҌ˵Ş\u0378ԩҧϐыρ\u0378',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 608036.976744428,
                                                    },
                                    },
                            {
                                        'name': 'МĚӀŹƺ˚ҸдľʪМѴZτϠɯҤȯ\u038dºԐЧнсӀ˻ƿшſô',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ҎʲҗÏъ҉ȾƖӼ˕ЋǠęϬ,Ϥ˩ȦɣƘżͰӽʾʠѳ҅uɃҬ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'λɀʫ·ӢҦ?ǙԢǤƪЌ˩ΦȗӀӨƓ:˵ӭʖȓԇkЪаϗйÑ',
                    'message': 'ȴǚϘɺԐЫīӲӫĝēϰ˒\x9bzԙT˸á¡ŮĄĪӃĻ\x86\x8aˆԌǘ',
                    'arguments': [
                            {
                                        'name': 'ϴ!ʇˬЬĈϕǱҏ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2082339514254338620,
                                                                            1150992520897179434,
                                                                            4485087288120861670,
                                                                            1581608423237309942,
                                                                            4085628667111314845,
                                                                            1038637167770318074,
                                                                            2050066478837643293,
                                                                            -5549679378326756799,
                                                                            4777125828460905253,
                                                                            -669936092838397558,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʞЮǼɹʲłЗΧņґҀƾ҅ΠüʪʚȶӎȦӲ˅ԄΗńÝ,˴ŁƁ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ǫ  ҕΎҥѬíҎӘӑÓĪѧǖԓŐŃ˗ŏŋȮ¾ѪàJѓӮ+ж',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5783518909627830283,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '8Ŭ˻ʊϬԈЩȰʋ\u0383ŧƴɴЂϘ$ӨԆłӻӣӔɰи\x94ʡƚφδƂ',
                    'message': 'Р\x8eΰęӡҲƅѬӯȋϦ\xadȹ˩þҮԍɮ\u0380ȧӰÁҬΏͳʭʑΩһҐ',
                    'arguments': [
                            {
                                        'name': 'ƾĥϥҝѦ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:210309.579205:+0000',
                                                                            '20210203:210309.579218:+0000',
                                                                            '20210203:210309.579225:+0000',
                                                                            '20210203:210309.579231:+0000',
                                                                            '20210203:210309.579237:+0000',
                                                                            '20210203:210309.579242:+0000',
                                                                            '20210203:210309.579247:+0000',
                                                                            '20210203:210309.579253:+0000',
                                                                            '20210203:210309.579258:+0000',
                                                                            '20210203:210309.579263:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȫēċʼҕάӭʁΐǸ#ԫЊΕɀƿҏ*sþмʛϜͲǏȳÄɎ˪Ģ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210309.579521:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԀĳǭΪǟƋÿњ.ʢͰ҂÷^ҳğÜìȮӟ:ҿиʋӨǕŹʧϐ\xa0',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Đϧ8ΎМɃɮЬԒѵϤțÄKƍѽЙӠӂĔȿѸʛĒԋЯԍʼЗ´',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:210309.579836:+0000',
                                                                            '20210203:210309.579846:+0000',
                                                                            '20210203:210309.579853:+0000',
                                                                            '20210203:210309.579859:+0000',
                                                                            '20210203:210309.579865:+0000',
                                                                            '20210203:210309.579870:+0000',
                                                                            '20210203:210309.579876:+0000',
                                                                            '20210203:210309.579881:+0000',
                                                                            '20210203:210309.579887:+0000',
                                                                            '20210203:210309.579892:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӀǘЂ҅½ϙʃɔыӦɌǵгȝ¼ѵɬKӱίaʢǁǉǀ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 227694.65045953478,
                                                    },
                                    },
                            {
                                        'name': 'ÍЇù',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'AʝDͷǇɥњБʁ˨ęӈηАȊһƬǓĘӫӒɇӈ˻ˊǶʙӹεƠ',
                                                                            'H\x84҇ˤəŇǳԥŝǛȨȊʖшҼѬſȹнϵǷ˻ȁϬћăӴЧ-˾',
                                                                            'ʺ˃ǅЧУҗǺÜѿбσƄāЗԪʤϸϒ Ú°~ЄȷɛȖОCçŊ',
                                                                            'Ċ³ԣɬѾȋƽĉ\x92кΡ:ɳ!ԑˍuɢŻ\x95ʄΫǈſƀ¶ˠɓӝŲ',
                                                                            '˸ɥŃΌҼҡЕɫΘçϿʩƖ<ԏцζƴ#ђҦÞԙϣ˳Ťͻȴ\x8dō',
                                                                            "ˀӚə±'ɂɵ\x90/ΟΚǬйˉŠňӳ΄ёͼƽǊÀƷ_ҧΝȔĕҠ",
                                                                            'ʳЉʾаʯ\x98ʴa˕јŲϰǢǬȄXǥ£Ó#ŒǠϜҋŃҜƵ¿Ǣԥ',
                                                                            'îΐяȇϦяʬʮ;\x82҆ԬǉǜνҁхȻАʭ҅ǫΩѴсΟ,χϰɞ',
                                                                            '>ΡȼвǴŢ8ъҭ¶ǖvԢĒjΉ\x84УĀθϭcɃτʺİ_ʪŇŀ',
                                                                            '\x93ÂȰǑΎӬƇɯӘˍ»ϧÈ˥29GѮ\x99ԫņԞɌԣӠʂUˀԦƆ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'sίƑӷ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҟß!ҦȪʄΰԡѹ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 272422.20607479615,
                                                    },
                                    },
                            {
                                        'name': 'Υ˭˶ƐíʡɊȃӒÈҹďɐ҅ѧѷƷҠȪΌêġɀӡΫƳΐЇΖѴ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210309.581081:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ğȶţbʍ',
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
                    'catalog': 'ӥƯ',
                    'message': 'ƙ',
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
            'identifier': 'ҋ˫ʒЩƥȪʡɤӄ¹»ěʒƖǘǜŝǑȭĹ˱ӔAҡǭŧӞqЫԥ',
            'categories': [
                'os',
                'access-restriction',
                'internal',
                'network',
                'file',
                'os',
                'file',
            ],
            'source': 'ʒǕņoԄɩǧÞ˝҂\u0379ƎƁӌÔьČǜԂȀϓӢбĦ¿ˇĮВϧϦ',
            'corrective_action': {
                'catalog': "īˢиɟĮ˘ъƾόҍϥϐʊķéĢζŰȃƼͳԨĔΓƟ\x8b'\x9bĭ;",
                'message': '³·ΣѲЫю\x95ſƶɨ·ßʐŎǏˊȠӮ-ʥͱͱƮӌ΅Ͻ\x80űΑĵ',
                'arguments': [
                    {
                            'name': 'ˌ˴\xa0&ɜ˖ȁэĲϛ\x8cǮΏβӅʩӍϙñІяӏOŋϲҤŁмɉϊ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        "ʗэѾőѩ\u0381ͿѯĒ£ĞƂaһèȗȚ'јϿΒfх¹\x96ͳҗбΘð",
                                                        'ԙįЧƷę{ӄ\u0380ʟí&Ӈ҈йƶkÑ%ʽԌȳ\x9fȞǆӮΪήѲǨϩ',
                                                        'ƫáŊӢ?҄ҚćƓʘŭlƂԂϩԍƘɒ\x88ԘǎΘԉδƺ;ļӪԟŏ',
                                                        'ʹм˼ΠϗϼЎѵã\x8dİʤІīɑðЭЄƉ©ѬƇîΡЦɁʬҍnҥ',
                                                        'ӱ|Y\x91SєưƈйτǗЩʏΧIѣҼlȂƴѣұΑϜǆ\u0383\x84iϓӀ',
                                                        'е˚ќҡМȮTÏƳπ"ӳʹɘÀѫAӴɂɜŴǙɸÄƚÑɡԖуѸ',
                                                        'ʋɆͽѫ·ʽϏɳƸʣ\x99[ͻ˨Ĺ΅ǰЉҠ7Ѽ\x8fХİw9āɷòq',
                                                        'ПƬѷ˙εƛˆdʋџ˜ҕ˪˭ψƂӅӤbť\\ƨ¯Ѯѣϰý˔\x91Ӱ',
                                                        'ƎѼ\x95\x98ҙFЬўԩȌÁˇϲƥҏ\x9b\u03a2ɍӻǦȒҮ-ʸ˺ƕɍҸʜΔ',
                                                        'ǅȠǁȧ\x95ˤΘåƓʕŷǖǔ\x95ˍǾʐ7˶ƿ\x9dƺ\x95ϢȜҨłȹэҨ',
                                                    ],
                                    },
                        },
                    {
                            'name': '¸ƶuðʽĞ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        813125.3491590035,
                                                        166455.51898692868,
                                                        191400.11286295875,
                                                        -82126.72167848812,
                                                        417933.22053729405,
                                                        417075.6141120937,
                                                        405630.67425651866,
                                                        794825.3922977493,
                                                        580118.87573249,
                                                        857730.8492874135,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʴѯϩƉ\x9cңʛĈѴτʬų\x82ɀɲԥĎŁʣāČς˶W;ǖ0ǥЦȓ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210203:210309.593508:+0000',
                                    },
                        },
                    {
                            'name': 'ʣwÏөώӐЪǃǼϮǓ˯˽ӸƗÎƱЌřǰƃΥĩɎɱōБω\u0382ϋ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'СѤãƊšЉλțДϐӷӢаΚÌϾʰӏ˪ƁҖņŹԕ˜Ӭͽҍ(Ц',
                                                        "ў\u0378Ѻ˓@'ɶйԇĕǃŎεʸωœϓϼɸ˒Ѩŏ^ΰʧЀ~ˊԦ¼",
                                                        'ȗHѹϩҲƮʂ˫ʻѷǎгŖԛǂΌѷʣƶƖІ{ђӉӕΑИĵŞѣ',
                                                        'ƈŰŤ˞ˬÅԐ8ȤИоͳŁСӫ©Ƕ˘ȽʇӔ˛˕υĺĬǐщ˒ү',
                                                        "ĿЬ˾0ơʋΒβ҄҅ҪΔˠϱѱͲкñΏԒҏƍǱȊ'ӐЗМΚӊ",
                                                    ],
                                    },
                        },
                    {
                            'name': '҅ȢɿƦϔe²ĥ¡ʪÜԪȑҢ˖ҍňǪӊɒʽϒѵȗPӈºɶϯ£',
                            'value': {
                                        '^': 'string',
                                        '$': 'ǖʔRȡʰģԬïŘȗ΅ĻĀҡŢӶ˃ćԞ·HǒΥɐŻæ\x84ȨRа',
                                    },
                        },
                    {
                            'name': 'ǫ\xa0ϫǠƺҌĳ·ŨӤӊ˥ҚĩӢͱÑÔźuǪяǸжɰăϯӽƏš',
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
                                                        False,
                                                        False,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': '{âɼшʯΕҡƢΫȗƷZǲϸϥȊoΎЪơþѕ҇җԏȄNǔ®\x80',
                            'value': {
                                        '^': 'string',
                                        '$': 'r@7҃`˘©¯·ëɡɂÕҾŚɴДɲÊɁ˩\\ȧ\x9bů˜Рvrө',
                                    },
                        },
                    {
                            'name': 'ǏòƎƨξ\x81ƌȏGʟːҚӊϨŎ\u0383ϊθȻʁπ^ʁɆʭƨĮҞЗį',
                            'value': {
                                        '^': 'int',
                                        '$': -3755660490481682036,
                                    },
                        },
                    {
                            'name': '\\MʱвɰȥǰĮʖӷÑŬοȫΖϽǼɔ\u0383Љ΅ӀпТ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        657404447793483293,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӶґΝ/ϯÑц͵ʕԤÏɑϋˣΝ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210203:210309.594935:+0000',
                                                        '20210203:210309.594948:+0000',
                                                        '20210203:210309.594955:+0000',
                                                        '20210203:210309.594961:+0000',
                                                        '20210203:210309.594967:+0000',
                                                        '20210203:210309.594972:+0000',
                                                        '20210203:210309.594978:+0000',
                                                        '20210203:210309.594983:+0000',
                                                        '20210203:210309.594988:+0000',
                                                        '20210203:210309.594993:+0000',
                                                    ],
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ĮџФ¥҈ǔȣ\x9dɿІŲÞ¶ōҚӦҲƺȥӁŠιЯΛ',
                'message': 'Rԑњϱ\x88ϧȫϸүǬƗ\u038dҿèƑҏɯīԫ\x8f%ƆĮ҆ƗɃХǤϬp',
                'arguments': [
                    {
                            'name': '\x81Ƶӡˤ©\x99βăÎN˼ԚêéW¡ФȤśƽˏÉҢˬә8ȋ\x85пġ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ʽȅǗÄфԖγЉʽӝqÁƶÍůρbΏ˸ҹκϽõˑrŃƗͳơĬ',
                                                        'ɛ·ΊρɻѸƑСӷΤ\x90Ġ\x99ɻϞԢ˪ʋԏʂ[ӄBſǆǨЗHМǰ',
                                                        'ҜʧӆˬɎЫЪɨːÁɡ"ú]ԐδƁɀȾˢȪĜǹЗлӴÌη\\Ɔ',
                                                        'ɨĔʁҭŝп˥³шʏ\u0381˫ǜфUG҈ϗƬ\u038dȉȝӗҮºȰȑťϖɎ',
                                                        'ÓͿ˵°ˎѓԓ×ɪ{Т*ɍȏϝŢƲđĴǿÃѫ#İʺԮƣϡѨķ',
                                                        'OûŢɭŌԚЕϹ\x8dˠ˱Ǡʉςμϻʉϟ(ÎóóÃƌм%ȁčÓӍ',
                                                        'ĵğàҶјŕĽƱɩʛâ˽ȤQ\x89Φԣʒȡ˟Óv˥Ηι;єǉӤǞ',
                                                        'ţǉŃ˖.҈fÜлӽмЩӌϯʄȀ\u0383BǮʦʿŊȦ7ΠŠÂҦͿǬ',
                                                        'ϝмϓǋʜǢȃǻŃμ͵+Ɠ˸Ȩʏѯτх˝Ηһ\x95ОΚĻǳƉr#',
                                                        'ǗȊ!ʋ·е҇ǰучȠѐ\x98ԖҎԚԘ˵҃ˉαʶѴɌ˔ɫİÂ˻ϰ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'нĺΧδѨJȨƛҪҴĵʽԧ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ʡː\\ĊΧǊϹэ\x93Ȳă\x9fЦɣŋЈſԢӐӟͽΝǕЃ˕ʌμɥɱϱ',
                                                        'ʚԇ˦ϗ·ˇԄĬ¯˨ҷʻǼ˦ǩÃ˪ũƳҬҏȱµÇɞîȳʎӎě',
                                                        'ѐӽǪƻƴǶŅЌ&þҨ¾ӟǂşҴԞįȜԃӻ\x7fΊіѺррʦуˢ',
                                                        '¶ʖ*ǦŐԇzȈԀĄѼËӹļӇɄ¿҃ӊϭȾлСēϫǱÀūНʞ',
                                                        'Ԛ˳ӿҘñYҗҮɪӿӽȚѼˠƮ¿ЏӯƿЧ\u0381ԃýƕ-Ɯß½ȕЊ',
                                                        'ȈĂ\u0382ӫ˾¤ϴɗρƎʶʑѰœҳʴɚÞ\x8dɜлƭӧȆĜхɡ\x89·ħ',
                                                        'ÒʛбêԘĊƑΝƖȰѬԙǏĵϊƂƝɈǦѨ˽ѻЛƺμƏɯɦϽʱ',
                                                        '2ÔҭзȞҪҌǼBǰоѲōÒĻҾяʛƌ\x96ΤȸΨĀųȬ\\ŠюԄ',
                                                        'ϤʞӷʅɵȵѐҏˇмΪИϗӝӼ°WÉŴɵӾ˚ϯ\x86ÌʼǄĸ-Ģ',
                                                        'ʬЍʟ\u038dƕ·BƑǯĊюХɒ§äËơɂƓĊȅ϶ξƑʰöҋ©ʂl',
                                                    ],
                                    },
                        },
                    {
                            'name': "ѩʁȰŷӤǉáԖɥ*'ϥń¥ðғѢбUůʇ\x96ɇԔӴúɾőε\u03a2",
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        False,
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
                            'name': 'eˣĊ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210203:210309.596827:+0000',
                                    },
                        },
                    {
                            'name': 'ʍɇҀ',
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
                                                        False,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ȇԏɱlҚɗӅɤŰԍʩ˾ԆІӶȞҾù\x98ӣвΖ¶ķğnŹҭƉ',
                            'value': {
                                        '^': 'string',
                                        '$': '\x84ζãŲˢlgđҴšѠӘʹφνàȊȸɼųҽ³ѷƌХǞȶӾáҝ',
                                    },
                        },
                    {
                            'name': 'йɢt˜ϾͲʤϷϲиĪɵϼ]ˏѻȞǾ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': '±ΌȴͼǨ{ӳ;ŞËŁêχǾ\x91ɀ\x97ƯӸиVnƠÅÇ',
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
                                                        True,
                                                        False,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ԚċˍvŷͳÃɭȑŪĥю¼ç˭ҰǫԡǨўȃӼȯИӬŲʛˏ\u0380Ĕ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210203:210309.597803:+0000',
                                                        '20210203:210309.597813:+0000',
                                                        '20210203:210309.597820:+0000',
                                                        '20210203:210309.597826:+0000',
                                                        '20210203:210309.597831:+0000',
                                                        '20210203:210309.597836:+0000',
                                                        '20210203:210309.597841:+0000',
                                                        '20210203:210309.597846:+0000',
                                                        '20210203:210309.597851:+0000',
                                                        '20210203:210309.597856:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': '1ȬǊɡĒГυ*ɁΦҡϐ{ϽĖȷʒҚ҅ҍYҐèёľϒͳʃͻΙ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210203:210309.598105:+0000',
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ǱǎǙȏΒ',

            'categories': [
                'file',
            ],

            'error_message': {
                'catalog': 'Ӱʄ',
                'message': 'l',
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
                'identifier': 'țЏЏǱӋлÔѮԭÝə˖ЪЈįҺҺфàĸʅǙʨюϙϏԌҵΎñ',
                'categories': [
                    'os',
                    'file',
                    'os',
                    'access-restriction',
                    'access-restriction',
                    'invalid-user-action',
                    'configuration',
                    'file',
                    'invalid-user-action',
                    'access-restriction',
                ],
                'source': 'ѯϸƓȲǇǐӕȭ΅{ԏϖVˬǝǌØƅяЏŏˣкԨˏ\x81˃ʋňO',
                'corrective_action': {
                    'catalog': 'ƴȃӬϐƟѭʃΤЃԑ\x93ϹњˬĠ\x87ǋÝΌȤǧͿƫƮñѧʐƮЗ˲',
                    'message': "ǴȝϼΠпØËXōÙɽȓƄţ'ʽҏʄöϴ@ӨѯӱəˬƐƖϻɺ",
                    'arguments': [
                            {
                                        'name': 'ҧĝȯːƜɬΫаһѺѨʫФϗ˟Ǜ',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȃϯį˸ąāˡʛˑãԀˊ_ӘwΞьӁƋԞŚҚǋфϩͷ϶Ўɗž',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            535788.8912883091,
                                                                            480715.921635914,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʁ',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϱ҂ohǩȅϻS\u0379ʁԎͷӆөGȜÌҏрʾǾњĶюүΝκ\u0381þκ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210309.588186:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҰƗʕŵŶʹͳǼҌ1¨ѧƶĆȶ·ĜǕΫ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5921421521847285706,
                                                                            -861326268114315275,
                                                                            3190068398020567697,
                                                                            -3015284401588327748,
                                                                            -1422243668670605078,
                                                                            -6066351002012078265,
                                                                            6650947201402606478,
                                                                            -8319856908015298721,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'џ²ˈǺνɶ\u0379:ÉзœąϥэРϫɧĚȰ˕ʖ˖\xadԆӳȏӡĚȐЬ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            751143.6997441867,
                                                                            752424.3347806494,
                                                                            37226.59750493913,
                                                                            899665.9720755583,
                                                                            836831.2849716701,
                                                                            186901.01255091728,
                                                                            261457.3700463549,
                                                                            14484.74232476388,
                                                                            46691.9182323096,
                                                                            393216.9553646536,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ſʊǫʤӍșËΐȑˁžӣäŞ¿Ҏǃ˯αͲɪ5˺P\x87ʎͳѦӼɇ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 157274.42199142027,
                                                    },
                                    },
                            {
                                        'name': 'ȹӟԕҖ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɟӷőΎá\x7fƛпǧҽͿǎԏTιЭ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0383ʵƿĨЫʽǣɄ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210309.589389:+0000',
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ƊľτǔĽʁԓʌò\x80\\νɇĔƣ9ϔͷmΛҸȌjéųźȃϲƏƚ',
                    'message': 'ƍφлҥċèы\u03a2ƌћÞǰԢԉʀϗÛɔǔ҄ǡсŝϊ˘Ō¥ƕăƊ',
                    'arguments': [
                            {
                                        'name': '\x91|ƆґԄϮƳtƳ˦Ω˔яԁӫͱώΩȗ҃,ıɢʯŀǅЮàĘƱ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǼѲўΆȌԗǅǌ\u0378ΕSŜƏˎҐɺ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˢӟϩƫˌӴU\u038bʦȌωΧѿ¼Ãα\u0381ƵаǖŤª˝L˒ĻћYώ\x93',
                                                    },
                                    },
                            {
                                        'name': 'ЙRөð˩Đ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:210309.590139:+0000',
                                                                            '20210203:210309.590150:+0000',
                                                                            '20210203:210309.590157:+0000',
                                                                            '20210203:210309.590163:+0000',
                                                                            '20210203:210309.590168:+0000',
                                                                            '20210203:210309.590174:+0000',
                                                                            '20210203:210309.590179:+0000',
                                                                            '20210203:210309.590184:+0000',
                                                                            '20210203:210309.590189:+0000',
                                                                            '20210203:210309.590194:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΜÖөŒ2ӴфǵȿԈÍ&˖ǩʍ;ūАKϗǺώÃτӹ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʗ\u038bŉµȅĶ7˴\x84ΩĞҮΖȆrƔï£ӛƕĮeȋƘǈŚĘ]ȏҫ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            645359.5293445815,
                                                                            684121.6705540462,
                                                                            579572.4523656907,
                                                                            352357.2980666505,
                                                                            621591.6012854644,
                                                                            342262.627794969,
                                                                            598156.7289121145,
                                                                            156356.42687671402,
                                                                            399064.7505724514,
                                                                            39120.95897084809,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '.ϩ˭ɿ3ѡɢǀ;Ƨˇĉś˽ʵŰSϐ¦ƽfŭȯīпˬ\x91ʔ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɠ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            314623.62341552536,
                                                                            540352.1900885811,
                                                                            982174.5137778821,
                                                                            296313.89447887347,
                                                                            215180.89872901986,
                                                                            394487.89892051934,
                                                                            -89391.01598116316,
                                                                            846962.5127566358,
                                                                            667290.1809949878,
                                                                            647551.0512108869,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӿ˥ńαˁȭѡќҾѓėǇĐ\x88ȽʛŗȔ×',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4861209466151246084,
                                                                            4778690597106278431,
                                                                            -7515662533646702916,
                                                                            -754046361613049488,
                                                                            1034194749063162135,
                                                                            5165102435997434482,
                                                                            -2077723925359105551,
                                                                            -8841488036388294673,
                                                                            -1925928697298110663,
                                                                            2919083432468229967,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҞyʊσѷɍѝȱĚĒ;ӌԠϹ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ơȾOҹåҷϓŐҝφəǕāÌ\x9eͱ»ϙˁʀÿϵ˶ðԕȬ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6287942122191709740,
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
                'identifier': 'эțѓɖʌ',
                'categories': [
                    'file',
                ],
                'error_message': {
                    'catalog': 'ǹʱ',
                    'message': 'Ƿ',
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
                'identifier': 'ŪPéӊ˭ӊёÆѵÈµ\\˽ȞÙƜΣ,ҧΌπƹďϼώǋŧZͶҚ',
                'categories': [
                    'access-restriction',
                    'network',
                    'internal',
                    'access-restriction',
                    'file',
                    'network',
                    'access-restriction',
                    'network',
                    'internal',
                    'invalid-user-action',
                ],
                'source': "˪ĕҤÅŭƆǔΔΚҚԂŇ®Ԁнуıűɠʀ˪Ç>ȸК'îq\x85·",
                'corrective_action': {
                    'catalog': 'ƶѪςǜŴ˛\x82YӌōɞÏƚЂԂŬʬ҂ȷѪǳƝǒŒǴƐɈœȪњ',
                    'message': 'ԟȅ˟ƨʁ˝ŹǭÉ҉ҀǒԒȐQΤțΏ҈ҏԂŨřĖƝ¹ӭғźʭ',
                    'arguments': [
                            {
                                        'name': 'øҺΏϺϙʀǷΊƳÄ˗0Ϻьʨ\x8eųĶϾ\x86ǦąІÄ\x90Ʋ*ħύ\x94',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 698383.1007666205,
                                                    },
                                    },
                            {
                                        'name': 'ñʦšтԅƾʟԑȂʪτ˓\u038bкǖӏШ˾ҀЯ˘ԑʭϬϠȕԙɥ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210309.599059:+0000',
                                                    },
                                    },
                            {
                                        'name': '\u03a2ΧÐҪГʏͲԑ҅ƀ:ʂпă`\x9cη',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 748912.24984076,
                                                    },
                                    },
                            {
                                        'name': 'ɥƏ£Ǽâӫйǆц˙ÔdʩˢĀЁāӗəΔӿńюʀUÑ˱ȻĹӨ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            102297.14962816276,
                                                                            -22139.219368433958,
                                                                            176991.91768231592,
                                                                            -66152.92933915198,
                                                                            871518.6867168266,
                                                                            393892.1117716441,
                                                                            232087.7514423352,
                                                                            862534.0068384323,
                                                                            11780.4386412608,
                                                                            608372.6992624458,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ћ;ɘßӊāăˊƾ}Ь',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 959868.1322577349,
                                                    },
                                    },
                            {
                                        'name': '\x97ƷȺǀçęӓӌșѶԠˍ6˲щʃ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 691642.0326199902,
                                                    },
                                    },
                            {
                                        'name': 'ƅɾϼӆѮԌҳȀҮӦɞȐ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210309.599889:+0000',
                                                    },
                                    },
                            {
                                        'name': 'rϼɨĮIɋԄɏӕʌÇуʔċŚΜҙsѤѝƩԮˆѕŐӡӊͶ:Ï',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1440004382447370573,
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'њƣԜӪđȏеϴs;ǗɺȮƹćҴиѢɬ˔ҧʋΞĎĨ҃ΰӅȉΞ',
                    'message': 'лƘʠЇԠ\x9cɏ·ԅц\x8ağúӹŅņ˽ӶϑϸÝEžƗƔπΔѐћƹ',
                    'arguments': [
                            {
                                        'name': '$ҙŌʵϘǻ\u0383ǟˊǝǝЭԎ˾œĬϰQЪșӒμNƍ\x8bίʰʚџȄ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210309.600434:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˣŹӝÌЍ\x81Rʰ\x87ƱуǚѬ>ǺӈƋϯϬs',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:210309.600593:+0000',
                                                                            '20210203:210309.600602:+0000',
                                                                            '20210203:210309.600609:+0000',
                                                                            '20210203:210309.600614:+0000',
                                                                            '20210203:210309.600619:+0000',
                                                                            '20210203:210309.600625:+0000',
                                                                            '20210203:210309.600630:+0000',
                                                                            '20210203:210309.600655:+0000',
                                                                            '20210203:210309.600662:+0000',
                                                                            '20210203:210309.600667:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'UǻЅ\x97șȿͺŷѽź\u0379',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7903449985211397470,
                                                    },
                                    },
                            {
                                        'name': 'ųҀѦ\x94ʮ¯Ųѫ˭δǚěϙԚˍŒ£ĽÍоӢɬѨɄĲˮȅʨ¾\x8d',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            695386.5760569455,
                                                                            320053.7613376554,
                                                                            7982.45685479611,
                                                                            339325.151358951,
                                                                            -38502.250295446305,
                                                                            320043.4756622729,
                                                                            648115.277393496,
                                                                            640960.7070522045,
                                                                            341202.556253468,
                                                                            265349.8816034342,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʾˠĸÖҸέǌэ¹\u03a2è\x86ʒѰйԎʣϔŔƻǄϘԘБϘǮŵǿƿ˧',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɒћJЬ҆ķƄҾ>ˤ˙ĳxʟțӲ\x82Åӗʔ˚',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 897715.8165529206,
                                                    },
                                    },
                            {
                                        'name': 'ԛʓƫ˨ѨÆөΧЋő0ΓˍɃǜԀʫ˂ӀȵÑĕ\xa0\x7f˗7ӤƶĬ\x88',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210309.601622:+0000',
                                                    },
                                    },
                            {
                                        'name': 'õʖƝƚțтƘЪǐɦҎx',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӵŉƗʿӒϯѳːƋżЍƝкǓʺ˵\x9fƐȖѱɐҡΐЕӍˠ\x9bő9Ǩ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϔxΌхˣƕҢîƕϲӈԦ]',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210309.602040:+0000',
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
                'identifier': 'śţJːГ',
                'categories': [
                    'internal',
                ],
                'error_message': {
                    'catalog': 'Őӌ',
                    'message': 'ȵ',
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
            'output_file': 'ǾÑʇΉɛÁЍψʔԤ\x99Ğχ7˳Όѝ҇ȍΠɅҩϓТ҄ԘʟÕēĤ',
            'output_console': True,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'minimum_level': 'info',

            'output_console': True,

        },
    ),
]
