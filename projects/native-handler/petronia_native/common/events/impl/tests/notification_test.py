# GENERATED CODE - DO NOT MODIFY

"""
Tests for the notification module.
Extension petronia.core.api.native.notification, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import notification


class MessageArgumentValueTest(unittest.TestCase):
    """
    Tests for MessageArgumentValue
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MESSAGE_ARGUMENT_VALUE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.MessageArgumentValue.parse_data(test_data)
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
                res = notification.MessageArgumentValue.parse_data(test_data)
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
            '$': 'CЀǒͰïԬƻϿA˽ʙ\u0383ŕȹƇȿƛѲĕҭDΔƊϹр҈ˬ²ˡ\u0383',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -1090010442811805897,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 858259.9693420146,
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
            '$': '20220523:220036.708067:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                '͵ŬïԔŉԧ6ӟʨČǧɻϰĮ\x99\x97ǛʨȕРǁɁӈҪ\x96˯_˦Ӥ¢',
                'ƏΝȔοƗηǪ1ÇÕΙΘѼΊũɛ˞OäǨјŽǑťГѓɧƓ~ɸ',
                'ΞȂӿЍЗƘĥǡʤɟ҈\u0380˖БЮͼ˄ʱɪԋSьʸʧȌƟÂ΄ɔā',
                'ӮϏɄӱƫοÀďĘȋȒU\x9eˡ/ʮˌΦǺϸХƌќŐχҶ·˚ҵù',
                '`ˁǀˡɜСŨ´Ӵȑ\u038bһ²ȇ«Ӱ˟ØŨ\x91YʗҾ#ĔԨ͵Ȃòͼ',
                'ňƀǪɘԤЪγɯǏˮҨϠEɯϻԃЕƙýȞĖΎ\x88Ш\u038dΗȨŚ˕Ħ',
                '.ЏҕʂˎʓˬГλȦʇ\u0379ǕęŶmэɛ\x7fҋѲШÙıΊҦ˫Юßʍ',
                'Ĥ¼ϟːŮӳ҉ǣȚÚţíщҎϘðˈǞúȖȜƪʫҞò:\u0383ĭǏŖ',
                'ўА˗ҨģѤĬXșúϹӤOхˉίƁɯǎÈȰāӟ˛π6ɸʷʱȄ',
                'ϫЊǂƟύ˂Ļ\u038bDђļµӃХяԤљѮģϱʝҸŹм+ËӔˋďå',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                6082913845222944101,
                3154203659507055253,
                -3325454089451935264,
                4430869622518706985,
                5640530102902683026,
                -1287188324342723909,
                -5027404863083317387,
                -2039700669949988723,
                2660389089442764360,
                -8642118694409946571,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                724107.7968251816,
                830837.2954471568,
                491955.6643374448,
                792398.5951812556,
                451322.8390678351,
                346366.8348944024,
                661156.956703412,
                -53474.86351114833,
                816584.5737270693,
                487338.05563407997,
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
                False,
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
                '20220523:220036.712803:+0000',
                '20220523:220036.712889:+0000',
                '20220523:220036.712971:+0000',
                '20220523:220036.713053:+0000',
                '20220523:220036.713134:+0000',
                '20220523:220036.713216:+0000',
                '20220523:220036.713296:+0000',
                '20220523:220036.713377:+0000',
                '20220523:220036.713458:+0000',
                '20220523:220036.713539:+0000',
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
                res = notification.MessageArgument.parse_data(test_data)
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
                res = notification.MessageArgument.parse_data(test_data)
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
            'name': 'ưńКÒǆϜЀČɬǟŏ\x81ҀǂџʺQǃʿɋŲЧҰȘѻн\x88)ɓƨ',
            'value': {
                '^': 'string',
                '$': 'ɴăǹ\x82ӤαɜżȪӅҸʗXʬÉаϴR\x83ȥӓ˚ƶđΜʀ\x83ͼҬ\x9e',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ǫ',

            'value': {
                '^': 'datetime_list',
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
                res = notification.LocalizableMessage.parse_data(test_data)
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
                res = notification.LocalizableMessage.parse_data(test_data)
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
            'catalog': '·»сΞėЖÞӼńˍӲƗHùĖEªƺ<ɠ?˘ӝњԂҩͻ˅Ӏg',
            'message': 'W÷ŚƙŃΌȍDԝĶAƠƊͶ˖ʩǿƭHӉӤͲ±vƹƛơҔћȼ',
            'arguments': [
                {
                    'name': 'źɾӝƔϑ҄ɽț\x9bӳɻˍҳҥԂŽԡƲ˚ĵŖĠѰŽŻĖӸКϬЂ',
                    'value': {
                            '^': 'int',
                            '$': 2196344948436775683,
                        },
                },
                {
                    'name': '˄ŔȾƂϝϱҸԁ҈΄ʉɫǡҴЌū',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -1731948672909320764,
                                        -215221991011126059,
                                        -5142122095124981837,
                                        -2887926237774587163,
                                        113081566100582504,
                                        5008339202637759284,
                                        -947251280257517851,
                                        -7605665048103356090,
                                        -6481477189690157252,
                                        -4556408361774803695,
                                    ],
                        },
                },
                {
                    'name': 'єʩƍĈѬѐƕďȎ',
                    'value': {
                            '^': 'string',
                            '$': 'ǻˠ˨ȿɯԬƃԔԀѺ°ʍƝĺĵԩ;ūʩƨѡϑϝȊФ\x81Ƌæʞ\x97',
                        },
                },
                {
                    'name': 'ȋΝōϢԜ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        True,
                                    ],
                        },
                },
                {
                    'name': '˪҂OƚǕїŌĜ˅ԩȖũſƝϴԇ\x9daђ˞˰ʛÚƨȮƈшѿѪϻ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20220523:220036.701426:+0000',
                                        '20220523:220036.701507:+0000',
                                        '20220523:220036.701586:+0000',
                                        '20220523:220036.701664:+0000',
                                        '20220523:220036.701741:+0000',
                                        '20220523:220036.701818:+0000',
                                        '20220523:220036.701894:+0000',
                                        '20220523:220036.701971:+0000',
                                        '20220523:220036.702047:+0000',
                                        '20220523:220036.702123:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ѷ҆ԀǚΊlǩԙňɶΝÿ˖¼ӴєӌɠŦԆTǜȪž˄ӁȊ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        863243.7844255659,
                                        760524.4271228715,
                                        431012.6020280764,
                                        719609.1583409738,
                                        657115.3744025528,
                                        393705.27326750127,
                                        713354.667170307,
                                        21193.57115526586,
                                        238518.85145891964,
                                        63159.715772974596,
                                    ],
                        },
                },
                {
                    'name': 'ˊTsϙѾԖʥЩƯÑƄСДfßȚfΆ˱ϯ\x8aС\x85ҕγ',
                    'value': {
                            '^': 'string',
                            '$': 'Х¹ΏJɊӭɳǊοĩЅҫҎ\x9bżȤɬҺʍɩĝůȞˇрȆʿѩđЇ',
                        },
                },
                {
                    'name': 'ӍԟèvʝŢѩǱҜȘŷ\x95ĔΖԭϡƒ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        943308.4117693872,
                                        589638.2569227688,
                                        -8466.637992937758,
                                        128980.93054650165,
                                        285899.81403150037,
                                        934669.8691935679,
                                        993125.8286609754,
                                        544567.735073651,
                                        441528.04713211406,
                                        566333.5822710869,
                                    ],
                        },
                },
                {
                    'name': 'ԥΥ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220523:220036.705422:+0000',
                        },
                },
                {
                    'name': 'ÙŦ\x8fƪ¸ȁŗͺƣсÏèƤŜĽˮЫ>ԝ¯ZǇǎ˻ҬωϭŤVΩ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220523:220036.705824:+0000',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ɒƧ',

            'message': 'ʛ',

        },
    ),
]


class NotificationTextCreatedEventTest(unittest.TestCase):
    """
    Tests for NotificationTextCreatedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in NOTIFICATION_TEXT_CREATED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.NotificationTextCreatedEvent.parse_data(test_data)
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
        for test_name, test_data in NOTIFICATION_TEXT_CREATED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.NotificationTextCreatedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


NOTIFICATION_TEXT_CREATED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='text', name='NotificationTextCreatedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='title', name='NotificationTextCreatedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='icon_id', name='NotificationTextCreatedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='sound_id', name='NotificationTextCreatedEvent'),
            ),

        ),
    ),

]


NOTIFICATION_TEXT_CREATED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'text': {
                'catalog': 'ǈÁr˂ɠʒǧӛ\x87˅õʘζůƅ¤ůȳѢʾňʻÎӹϐʿϮɆȟȾ',
                'message': 'ѧԊǖҖǣӍʄMϧ3ҐѪҸΈҔΉæсҊɋίŃĝũ\u0379ïЫδѱŁ',
                'arguments': [
                    {
                            'name': 'ЬљǗʩ÷ɺɳ˞ƇSgˡн',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        352263.7720173072,
                                                        453905.3830571228,
                                                        448989.17257981235,
                                                        857250.188844437,
                                                        869590.7514431734,
                                                        538076.3716532887,
                                                        -81146.83457015156,
                                                        144341.0559162274,
                                                        414765.8656271863,
                                                        285047.70449764864,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʘƇǅԈёȒʺăɆǲѡҘҔɗpƫ½ŸŪʏԑŴІ˱\x83Śί',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220523:220036.691376:+0000',
                                                        '20220523:220036.691460:+0000',
                                                        '20220523:220036.691535:+0000',
                                                        '20220523:220036.691609:+0000',
                                                        '20220523:220036.691683:+0000',
                                                        '20220523:220036.691756:+0000',
                                                        '20220523:220036.691828:+0000',
                                                        '20220523:220036.691900:+0000',
                                                        '20220523:220036.691973:+0000',
                                                        '20220523:220036.692045:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ǣì\xadőƆҍÏđĹƉȅsSʅʬǞʰɢɑčāҼӯ˜͵ņ0МͲÓ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ŵŘƄ҆ϡҧăðʖŭΗ\x88¯Ī|ƓȵɪƤƋњƺʜҐϪ˗ҖIԔў',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        828474.0690519097,
                                                        571680.8853239109,
                                                        748934.4510554882,
                                                        309763.1158956916,
                                                        -52735.89907466483,
                                                        247810.12890784972,
                                                        45075.14882508264,
                                                        964244.2481139777,
                                                        269065.8768941413,
                                                        307424.99763124797,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ȜҥԤúŅԥƣӸёͱӑ\x7f\x93Ǧ¾сł˙ԗķ)ǟ˹PρÓʬɐϧɿ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220523:220036.694131:+0000',
                                    },
                        },
                    {
                            'name': 'ŘҕНπ҇ȷҋ˘ȋ',
                            'value': {
                                        '^': 'float',
                                        '$': 492545.25488076266,
                                    },
                        },
                    {
                            'name': 'ǤǷʘΉ©ńɊLԮ˧ˁ\\\x9eԕʽʞĪǫǍ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220523:220036.694878:+0000',
                                    },
                        },
                    {
                            'name': '˳ѰÖԥ,ǠҡƣɂοԀÙҴ;',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220523:220036.695256:+0000',
                                    },
                        },
                    {
                            'name': 'ǺǪϙȃêϝǳͿӖѧéȪҬєπȄɜ҂Ѩˆ¬мӏǙаȀϚүθx',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -562921531785051777,
                                                        7194694491371452645,
                                                        -6505376217291435528,
                                                        5297717210727242645,
                                                        -7424967814027774358,
                                                        6391025978601300852,
                                                        -6694239676437900403,
                                                        -525539190670199516,
                                                        -5769679702089739421,
                                                        1161020880869758408,
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ɉ<²ưȆтϔϯͳʳΟЗͰ¦Ǫȱ˧џѻѷΎ8ʇҢѺӂɒǼӢȮ',
                            'value': {
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
                                                        True,
                                                    ],
                                    },
                        },
                ],
            },
            'title': {
                'catalog': 'Ε¦(ʨţΐ˧ЇșS˦%ƿЬTѲЯκÄɪκЁԬȰèԝɠ\x85ЃϿ',
                'message': 'ȅĮ˜ȆÁӳў˯ÃѫґҌ6ʴӼЩøˤͻМȼΙԐїƴƮƳūǂӲ',
                'arguments': [
                    {
                            'name': 'иɒиǸâøϰʃɡԬ˫ǻƽÈ˨ԉN\x82ȋѯρùӜ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        6528796653338646101,
                                                        -5426596843490464019,
                                                        946945847772146828,
                                                        2890918159645503235,
                                                        -6145503131327538407,
                                                        -5691045984458127499,
                                                        6299535427290801501,
                                                        9055273447564177517,
                                                        6741401176848046910,
                                                        -4045956504937975432,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ҧĳžǌ<',
                            'value': {
                                        '^': 'string',
                                        '$': '˰Ҽ7ήŰŉȘ(ȴӏ~ÑʽϨ6Ӄŀ\u0381ǐɕ·*3şĚǬȄϪǩѐ',
                                    },
                        },
                    {
                            'name': 'ИєˬėЌʡƾɩҒƓîɆßНĸĤļǶǽǳűŞǤȦɉԬǅȠÑҚ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        976049.308247382,
                                                        793598.0797278743,
                                                        158445.39279980664,
                                                        621616.5500354063,
                                                        774673.0389216894,
                                                        740636.7525714396,
                                                        -45549.810339844524,
                                                        834327.937387032,
                                                        897098.7126112342,
                                                        778636.3914756421,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ҹȁԄŷӻϰ³Ӆ˝Ξѽ˺&ǠԖƎŃƠИóűɴуpˬӡ˸eɢ;',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        7853900419609364211,
                                                        -5823535922970950811,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ҦcГɆãʧҏ.ȺԛŇѭԋŠиǂʏī\u038bĘɄԀѧ˽ȥѭęӖθƱ',
                            'value': {
                                        '^': 'int',
                                        '$': 8011559195712843125,
                                    },
                        },
                    {
                            'name': "ŇȼǶʱ΅ěŠƂӸϠŁÅƁ'ĐϿȜşƿɹψ¨ӰѢ\xadÃÕѪМr",
                            'value': {
                                        '^': 'string',
                                        '$': 'ÒǴʝЎ3ɣπԀԢÍʆŚùȈͺˮКčEʼËԕΰÌͻѵƍ˸Ŧϋ',
                                    },
                        },
                    {
                            'name': 'Cϻ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        False,
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
                            'name': 'ԏ˷]҃\x94Ŀ˸ĢPčʷϒα˄ҍǛԘceԄӖñйԪːȥʉԦԫυ',
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
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ѷĽ',
                            'value': {
                                        '^': 'float',
                                        '$': 970469.7465217095,
                                    },
                        },
                    {
                            'name': 'ĚΜªҸǍȖѶŌ˚ВκЈԄħͺ¢ź8ʷɻс:ì\xa0˰χУԗĘ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220523:220036.721213:+0000',
                                                        '20220523:220036.721290:+0000',
                                                        '20220523:220036.721365:+0000',
                                                        '20220523:220036.721439:+0000',
                                                        '20220523:220036.721512:+0000',
                                                        '20220523:220036.721585:+0000',
                                                        '20220523:220036.721658:+0000',
                                                        '20220523:220036.721731:+0000',
                                                    ],
                                    },
                        },
                ],
            },
            'icon_id': 'ƽzǁӒϗӓɕѺŚCŉΣӿ˨\u03a2Ŏ\x9a¸<ǠĜʴiȗźȲӉ¨ƗN',
            'sound_id': '\u0380©ŔƺǙϵʎҊʘʏÖφϱ9ÏM',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'text': {
                'catalog': '\u0382ħ',
                'message': '¡',
            },

            'title': {
                'catalog': 'ğњ',
                'message': 'Ř',
            },

            'icon_id': 'ɑͳħˬ˗',

            'sound_id': 'ǞаǩӁЗ',

        },
    ),
]


class NotificationIconTest(unittest.TestCase):
    """
    Tests for NotificationIcon
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in NOTIFICATION_ICON_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.NotificationIcon.parse_data(test_data)
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
        for test_name, test_data in NOTIFICATION_ICON_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.NotificationIcon.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


NOTIFICATION_ICON_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='icon_id', name='NotificationIcon'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='title', name='NotificationIcon'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='hint', name='NotificationIcon'),
            ),

        ),
    ),

]


NOTIFICATION_ICON_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'icon_id': 'ƈÜ±ԁŋƆbóĚ2ƝƦÊǎǶ!Ò\x91úʦǊӭӛʠǃ\x91ɿӒɏ]',
            'image_id': '˥^ίƧΪЄȌʟȹŚӒυ\u0381ӼʋΏìǮԭϭԒƎ˳°ƙˡӳƣ˧ѣ',
            'title': {
                'catalog': '\x84љ%ŮˀɵĻʎǖҷˍĂGΩÒ[Ғ³˞τӃԬΎϤɢɹҭԫ\u0382ɲ',
                'message': "0ƨʾʳqд-ƍũ˵ОѤʕʸıʽ϶ȞйОԉЫ>ӣ¤řƭӉԓ'",
                'arguments': [
                    {
                            'name': 'Şӫǯӑѻʇ˵ӝ\u0379ɊˉʳҙĚΊʊ©\x97Ʋ ǑԈƠɩȹǢǓˍԍɇ',
                            'value': {
                                        '^': 'float',
                                        '$': 306286.5991330654,
                                    },
                        },
                    {
                            'name': '¶ӑĮξ"ҬƿиΛˋˑΥӱYʎȖϴÎåvņÉКúɟӍϖŌć·',
                            'value': {
                                        '^': 'float',
                                        '$': 391531.90955925826,
                                    },
                        },
                    {
                            'name': 'ìҁϋę9ɗœÈ1ƣԡţЄˆҦйºȷIŵлаʳ',
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
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӧ\x98ɹѝɶцƆӁoǮƸƩԦ\u0381fыσƶϷŀұȣ˄ɋ҄Ǟ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220523:220036.819290:+0000',
                                                        '20220523:220036.819379:+0000',
                                                        '20220523:220036.819460:+0000',
                                                        '20220523:220036.819539:+0000',
                                                        '20220523:220036.819618:+0000',
                                                        '20220523:220036.819696:+0000',
                                                        '20220523:220036.819774:+0000',
                                                        '20220523:220036.819852:+0000',
                                                        '20220523:220036.819930:+0000',
                                                        '20220523:220036.820008:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'țɘѐƉϣɄÀ×ԧŐǌ϶ʏԭȬέAӯÉϤȎɤſòҁȼ)ѓ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ψԤ[\u0381ɨÆǭϔȮІщʃºОәԕДMǮЍʼƒȷǉďƷуԩԤʇ',
                                                        'ϽчԆșɁƬҜРʂӶˡůѸŐůŁɾϲǐѝҋɈȷъǍ«Ȑϵʿӧ',
                                                        'ʶɎҵˈԫǒĦˣǉɯϾȢɗԆΑӿȿϵħŨʤӨòĖkǜ=ɫʒÉ',
                                                        'ƜιӓƷāş˩˨˘ɇԡǮβ¾˦ԎƓʺɑѯѢμȓәǆѡűʆҊ³',
                                                        'ŰüġΕā҈ɨȻłǁ΅Ǚѹɟ£Čҗë/Ŵǀ҉ȢƺЩģєβƠ!',
                                                        '¶ҞҔԔe~˱\x91Ê\u0382Җɝԃ¢όӖǳѢɐ5Ӎ˝҉Ӵқ˴΅Ͽ\u038bù',
                                                        'ʏϜȸѤ´ƗЊћưԉҨŖ5·\x90ь_ʳŞȶϚӥԋӿӾæMìʮǁ',
                                                        'ʫÑéѽƒҶĭǄȞĄ˰ϽѰͷɦОˊҊѤ\x85ÚǗÞƶú«гĳϣЙ',
                                                        '҆ȗҟ>ȲƭcʙƩˈ{ǪɮŕĸɜѝӻҍƮѣԃʡЀȋǻϬɺ\x8eΧ',
                                                        'ŉ8\x82ʮˡљƼɕ;ɟŸļςƖѥĥ˄јҔЛԛЦԨɈÕǫҒƨЏʢ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ɵÒœτԉЃҿÒѴ\x9fϧŴņӄ\x87Ґʀ˚ÉñϸȸĔөѣϋȫɨοź',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        862757.5650592839,
                                                        12492.543396443754,
                                                        391435.2436517016,
                                                        232050.79884959344,
                                                        -32824.497936538115,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ćԭñ;ҥшɓөěΈҊλ5ΛϾҶŭ˭ĳԃԇЫǭˏ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -4637848488385205799,
                                                        -936055129167177414,
                                                        -2946219676074211277,
                                                        1399874079138581062,
                                                        4274096178916868782,
                                                        8685827143297166123,
                                                        -378430753009652756,
                                                        -3454991242936172776,
                                                        1366068796213692847,
                                                        -2586848430948550365,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǹƹːšїDȗ}ˋȡ˚³ēĩȓĂϜʇ˪˔ÑʺQД',
                            'value': {
                                        '^': 'string',
                                        '$': 'ƠφŽӌțǭϻɃÓҞȴӨÐҏӖĵʯ˥mɌҔҌŅAɰʎһþʭȷ',
                                    },
                        },
                    {
                            'name': 'ċҞӪЦкҲˤOѸīԩuǺ$ŵˈҵӄˑϬǪ³',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        1876576125814589035,
                                                        2909726577943317159,
                                                        1090175570015755580,
                                                        3850273518628035256,
                                                        1230920919998027613,
                                                        -609155263600122515,
                                                        -4348232378541826760,
                                                        -2869722435403903101,
                                                        -3706075326818687840,
                                                        -2653226920305367444,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ΐǍ\x9eӺŗˡӝ©ѥ\xadLÂʑšҚ\x8dӛȴ\x8c',
                            'value': {
                                        '^': 'string',
                                        '$': 'ˉѸԃȖĀӑÚȈƿʚԨ#ʝɝĵϴˢŶ-ѵЌЁԑԔӏЕqƥ͵Ŝ',
                                    },
                        },
                ],
            },
            'hint': {
                'catalog': "ʍӄҕ¦β\x9bʞŬßΞ;ВϣΒĄѾɀӷѼƧ΄Нń˯ɯЃ'Ϯ¯ ",
                'message': 'ǽsҭƗʙӵÉɷҢ\x94vŭȡΊɘɉӾΒДƀϓǅˀӵ˪ɩԅŸǘǬ',
                'arguments': [
                    {
                            'name': 'ʖɻ&Ӕ¸ʖȁS§ˉ˹țŪƥ\u0379]ґƤţ˥ȗň϶ѽȤDɍİОx',
                            'value': {
                                        '^': 'string',
                                        '$': 'ǌϼȳƁĚAνɟÝǃƁǗϐЕГϕȓњϕғnξĊʣȤ¨ƅӨʥĸ',
                                    },
                        },
                    {
                            'name': 'ʀѥԊ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220523:220036.827310:+0000',
                                                        '20220523:220036.827393:+0000',
                                                        '20220523:220036.827473:+0000',
                                                        '20220523:220036.827551:+0000',
                                                        '20220523:220036.827630:+0000',
                                                        '20220523:220036.827709:+0000',
                                                        '20220523:220036.827787:+0000',
                                                        '20220523:220036.827865:+0000',
                                                        '20220523:220036.827943:+0000',
                                                        '20220523:220036.828021:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ұʀɚʯ˲ȔͳʚĻƍɧΌǰϑǉϊʌѯˮlԎӶҎ\x84<ʵ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        5026167884959895788,
                                                        8379163818108903654,
                                                        1960704092100777050,
                                                        8862170541869745673,
                                                        -8587048940614788310,
                                                        -1033827469779623864,
                                                        2336657008883380999,
                                                        3770432729512428700,
                                                        -189113814069688154,
                                                        -5216085465958338405,
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ҿʂӟö±ĳǀÿǲżԒњļ˂ηħΚνԄȃƱч"˼ɉįķžӴ҂',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        True,
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
                            'name': '˔qӑȴԩ˕Ьɡ5ĐұѴИ',
                            'value': {
                                        '^': 'int',
                                        '$': -1068545932611748908,
                                    },
                        },
                    {
                            'name': 'Ͼф˒ĚƈŢœԑʩʹ\u0379ҁAͼmɶѓĻɵѾқЇ҄ɖŗǠŃʼԜ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ԪŴӘÈԨʴьӕƻx\x87ǜ&ȗǓǵԫ»ΌȿǴƑ˫®ªГʲĶЈǭ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220523:220036.831743:+0000',
                                                        '20220523:220036.831826:+0000',
                                                        '20220523:220036.831906:+0000',
                                                        '20220523:220036.831985:+0000',
                                                        '20220523:220036.832063:+0000',
                                                        '20220523:220036.832141:+0000',
                                                        '20220523:220036.832261:+0000',
                                                        '20220523:220036.832342:+0000',
                                                        '20220523:220036.832420:+0000',
                                                        '20220523:220036.832497:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': '¬Є˽ʠǸȡ@ĨƞϤӘĈüн',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'TƾpɃσВѦɱˌǅȔͻƏȈͶ˞ϙ²ôsɦԘӢʏмζҤѪÏ˩',
                                                        '¤Ұ\x9bɘмŁŅ2ёÿQČɍЅ\u0381ѦlМdȅˊ»º\x8bˑҋҖˈ`Φ',
                                                        'ǺȬňȨΧàßɅĸ\x9eĉƎʰƐėҔÒӓóµđɳɮbЦϔɹǥѣÌ',
                                                        'ÉӀϰҁQ˂ɽҖх΄ЅçAӴŗƹӺӥǅǲɱ5Ʋ_ҸëϋĽƚŁ',
                                                        'ԬеûƀЈ@ΧԮčȖʳ҃ɥɲˢиәjόǰʾÁĶ°ˆćȠҭɉϩ',
                                                        'ɜМáɌCÕŢɈ\x9fǠl\xadһΆӍĐ8ĥ\x96АΧӼɃƨŵˢ=ʧ>İ',
                                                        'ɿҗȓΪÒɋˉԂ\x8bӀfəӈ˯ѶɩӜėȇ¿ҰŁұ˳\x97ɉʏ\x81҇o',
                                                        'ĪтȞɪԌӞѯӕӥȡ˥ˡ˦Ԥèɚʞ\x9fĥʁѸɑѵФqёӪǿЈ˜',
                                                        'èƜWчξ¬ԘƊѡķθΚRҜƗŌ҃σхŷϘ˩ȤΰįĩŊˉ6Ʊ',
                                                        'ɿϿԨːŗӿXɈä\x85ˑ˚ȷίɠǭҵҰƽJϺ©ќǠϫҿȯѠ\x91Ҝ',
                                                    ],
                                    },
                        },
                    {
                            'name': '\x8aȽйƁİΙȢ˒ÅԬɒĒԟ1Ϲ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ϣØĦů˔˴х˦ʕūȀԢĄĴs×ȘϳɨǽѢYƂÄǵϷ˲Ԕθϼ',
                                                        'Ѽҗͼ\x94ơԌ\x82ӈ\x8e˞ɀӬʚ¯ʿԗÄ҆ϊѦɹ\x95ģʃ<ˇ˺ӧԂӮ',
                                                        "Ѐӎ\x97ȟϫz(nƋϾʭЛЙӜϱ'ȶÂÏӹν˕Юπ˫ĥͿ\x96ԏǛ",
                                                        'ǵˑ5ȴëĹϸŞɱҚч\x94ӦϔίÜӶþί#ӉϪƩɗǍċɰȜúü',
                                                        'Ň\x84«Ԃ˪}ÌϱӸηįӽɰиqцό\x95ɺΐЕIѓŨȭ˟ʴѕʝ\x94',
                                                        'ϻӻ\x99ҴцГâªν˞ΊűͰȱ3òʖӼңʌ^ʦɆɏŨȴǳǅ¢ǲ',
                                                        'ĞӌſеÜȟĔĈƀƱƝŵѝǞЗǽǩҀʲϕ¬đõґȱ/ǠöǎӾ',
                                                        'ĜѝƊΌͽ˭ƄжȊɜʹƑάƎ\x9c˦ěβƸԗӷҦǌԁǽ\x82ȂȭƐЀ',
                                                        'ŋӢԢȫƽɶѼî\x87˩ϾΚŒȐŵũˈҔ\x83ЉɖҰǐӣӕɚӭȥĔ\x80',
                                                        'ďБӓҰˤ7ɋɞÖıȆΛ҃ҴƻõĈÄ\x97ѯɷԍЖтц<Ȟȱƺӈ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'F',
                            'value': {
                                        '^': 'string',
                                        '$': 'ϔҖϿ\u0383ѺȐɰω˦Ⱦ\x92ҥϕѫ\x93ξ\x84ǔx˞˴Ӡ˒Ӣ/þѷЛĎĦ',
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'icon_id': 'цʵaǳ¹',

            'title': {
                'catalog': 'Ϙε',
                'message': 'ҍ',
            },

            'hint': {
                'catalog': '&˻',
                'message': 'α',
            },

        },
    ),
]


class NotificationIconsStateTest(unittest.TestCase):
    """
    Tests for NotificationIconsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in NOTIFICATION_ICONS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.NotificationIconsState.parse_data(test_data)
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
        for test_name, test_data in NOTIFICATION_ICONS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = notification.NotificationIconsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


NOTIFICATION_ICONS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='icons', name='NotificationIconsState'),
            ),

        ),
    ),

]


NOTIFICATION_ICONS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'icons': [
                {
                    'icon_id': 'СOЍāƾИϓMҏɸҟѱȚǅŰ|ƹüĮɅәɃƚЯɄĚË\x95ϭј',
                    'image_id': 'rƮˬƻȜ×˽ϖ[ӓŅ`ōǡμ˙ԟԓΑÆʩŶιĉ\\>ǻ˂ъЌ',
                    'title': {
                            'catalog': 'pʄЭƭєξΙʃͶſǇΪ˴ʷǮƐχҫėɘΗèӶλʪԡ?ȠΥё',
                            'message': '?ǗΞm<®ǫΩĔȩʥɵ\x7fǚ&ϰ,ŰˁĳƹőʓӆРҞȫƷюȁ',
                            'arguments': [
                                        {
                                                        'name': '˙ӍlБ}Ϡ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 873900.9347197122,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŹԪ\x9a)qΙ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 271863.83404730156,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЀαŨ\x7f@ƽɇƥyÊљԕԌƸ§ү¬ɼƤЄӲŢҷŗ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˡɢ{ƭњı˪Ӭβ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 757639.8236825336,
                                                                        },
                                                    },
                                        {
                                                        'name': 'YѸŧƪċұR˟ĂђĆŤzǧλÎэûsЯͻЯӺĮҝƘþӁĪ=',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '/!ӄƠúӥɭæȂˢҔQѸ˵Ʒ˰ŔѐɅȈ\x96ĵˏ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȗ]õ«ĝҷˌ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÜĝɂĭӜϧşΰǦМǣԔԎʣԟϱɹ\x83BͰЅëΡѭӖųϑÉЂӘ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŶǓɳʪҶȁЅ\x92ˑ\\Ĕ©ɬƒßCӊЁ¬žÿηʎϋē\x9eҤΌņҏ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϫ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 263867.5516197173,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ιǫПӾ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'εԕЩ\x91Łѧαȃ]ΊöԧǿĎӧӭȉƌȘȇʬɹЖқµĽxĝű°',
                            'message': 'ѥűӼϺΙŃʩҌҵȨѶxʩ҅ĊÙϔʏ˱ɄԮˉǧĴɁʫӥěȤe',
                            'arguments': [
                                        {
                                                        'name': 'ǧӴԕϔǛҴҵĔüʡʵΜԅχ¬ǅГϰэӻ˱θɓÚWλ@źӏʺ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4912698147787712097,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʥ҄ӔѝϜΫӹʭМɔ˖ƛԫӑʦϧŮйd\x8f³ǆÇǋҔƎ\x8dѝΥʻ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.728844:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϤƔΗѾưԖ˪˪΅҉çƄдγƩɂѬʈȩ\u0382ʄŽϴź',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 45910.80910157709,
                                                                        },
                                                    },
                                        {
                                                        'name': 'λ˴ҫ6˨ӍЫƙ/ҧƿйĨɋ˱ЈԃˈʐUҝɺɸʜ¤ǼĢǖŤѝ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'őǞҠҍǌͶɤ҄Ԧ˗ѧ´ϱŋÌǒҭҞĺǪʒЦЧԧ)ӵЗϘȜϖ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӇͳĐͲĶc˯ʅϜϘΛѰHͽѕ\x9dѫȸʄƸȾʆËѻѱȜȳ\xadˌƸ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -834946856542752027,
                                                                        },
                                                    },
                                        {
                                                        'name': 'dȘҬ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɱșΦƍ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӧǤԪǛŅąʭԔ+ҁԦЃҗàиΈýѴʝdο\x9fԖĔƠΨɢƉѢŌ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Шіӝн',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϖӅԎʤ´ͺСÓϿ͵ǂӋâ!ʑXD±ԐȇͽџȰӛб',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 395748.72071953287,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǡăǻ±ŕþϢŠУлԚ¸ȀΓеìВѴ\xa0ƜШӺǾè\x8eÀ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.732064:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'οǽ\x87ӉԚ˫ˊΣřтƢѽŞɯrÂ³²ȲΑhǡσрƟҕΕŝ~þ',
                    'image_id': '˖ΤþžȳǭҎ΅ėҢҙΠŵ\x99иԢΈʺğһǶȦ˗Ȟжԍéǘǔω',
                    'title': {
                            'catalog': '˧ǉ¸ԊҢÁʲȣȪSƙшĿˆʆX\xa0ʛΩȎʁҍŬҤʼҷδˉщĆ',
                            'message': 'Ń-ҵ˩ǚʥĕʧίȀѶԪ\x9dϴŒх\x93ЂτƳƕȊтɾɴʂЋǤӹ>',
                            'arguments': [
                                        {
                                                        'name': 'ˡϻ\x95ǸǅȷʢǓƿƻÌТӘѡÌÑξԩȎ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˉюγ˲ųиɵʱіǃˑ\u0379ǼԤϿЮ˭ÜӗĸҀҺºǲйċʺчыΝ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '-Ȳʾ_¦ǆϘ\x8d΅ԔѓÀ7ʌчȲ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƷӏѾĐïǗƆɞɼкȧафѭɯʆ˻ÌӶŏϟ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'νмÊζҍʘěѿ˻Ҏƀƣǿ\u0379ÒϮƞĿЏÙǫϤ˝ԍǩŋƽԐUŹ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 47542910074860735,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÂŪłАѰß×ɑǱԫ\x80ѧчʴѭĳρƜ\x8fį˾ŧѻŉ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɠγNΦΨβΩ˸Іĩɑjȏ҇ж\x95ѴҪҥ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ìв҃Ș˺ʡȓ\x86ȐʤЂһІ3ʹ®ɹˊđҐǅŃ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1963011825645670324,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǆН\x95ϚнϘˀ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƲӬǊә\x85ƮȻƂƤɉʡȋԖŏԣąӆӠëʩ5ҍ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.737142:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ýəĦǬ\xa0eǛĽƐΑǭӖүϓύÉӿǪȆˎә˛ϷɰӱťʥξӦ¨',
                            'message': 'ԠĦҝʉɈϔʍ˧ɰĻќǿЗӕǑÐӱļųǚȢĈ\x9cȼȓφǒH͵ȏ',
                            'arguments': [
                                        {
                                                        'name': 'ԑˈҒѷÐϞˢŎɑқӆ˥ĚĎ(ǾαʔǳʯKҖ҅\x95ɝɛԌȾʐö',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'oћȞҢƵΗѫƲϘƐɻɴ^ιÜȡͱĐѶʰП%8ΗƲќиɒϤÊ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'fê.\x83а',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'БЈƪŮθЖϸєŅɶ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x92ĀΣþǦ\u038d˝ӿ*dˆŨӏʃΔԤʀʯʃ\u0383Ԙ;Оϊ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҉Ģ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 691164.1790280722,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɠļ\x9cї¾ˇǗɜ|ʎÖӗð',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȑð»ͱƖϩǨҜӞøҎǦŷˇ˚åéʲљȽʂG˰ӄƧŃĀű"Ī',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7502361842361825925,
                                                                        },
                                                    },
                                        {
                                                        'name': '҉ϊũʉӻǝМз˦ŵюȉƊФϧˋԚθзŏӯŪƃЭҟɏҭʃȌľ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȑ˥ɤф©Мi͵Ҹ,тŴÑȽɵ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': '϶&ƽÉοΘƟćˡˮ҄ħEѢΥЗӬʈ҂ƕ<Ќ4ĩͱ˪Ƀ˚kǫ',
                    'image_id': '·Ιɺȿgäǵԁ\xad\u03a2ƖԌäΣҀÂT\u0379ƢԫȒČÆɁśĨϡƷʐМ',
                    'title': {
                            'catalog': 'ƚ2èȖΨĚӈ˥ϙӢ˛³¦Ȉ\u0379ġĸǢǃɁȊЀ0ЊѥЩԇЋηú',
                            'message': 'Ăϔç&Āԧ˺ǸèϯȔsÿӽɏφǑӏϛřɼƻӿІ\x87Р˫ȺϿǐ',
                            'arguments': [
                                        {
                                                        'name': 'ûŴĢϥ˅ʾȮʳǄ°ԤΞʳӵή5ŁaАºɪŉȌÏϻϕȱʐȷԈ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.742945:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ņčǰԪÇƟȯÔγ\u0380ϹÝԈNӸȉԚ҈҈ŊȰԄΉŒʅø˵˛ϪӘ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɲԮłэԑͳӞLӽӰƽßř¦\u03a2ɟʬ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "ӍԘʭԖʟϏVϐЭËϫɳƬüЙЕӛ;ѫʿǥę'ͶGš˯a\x80ë",
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĞƆoԡƮȡȐ=ͲЏЕ\x9cƵ£VрњJȄҞ¼ʣţË',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 422602.0172064612,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϺņȋŇψʀʿ\x82Zрϻ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'в҇ĈҩҫҺˁǝйӛϻĮԭ%ˉКωTèҔ\x8d˙ZɏƿyŖ\x85ɫΊ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʼηL˫ļ˶\xa0ԙŞȚЛϚѾƃԬҠ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȈϜƍ|cЮӆКѴ·ļȴԂѡѬƯРԎ_eͲɐςѨ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'π',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'şʔԭҶ|\x84ўŤʏóȰǂϒ¹ʔîʽ.ơʡƓѰЊӠǂĪǫоɜǠ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'AʂĬɡώúЦĝˇiǬô<QǼͰαϘƙðǯƓĢҁ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ɾBȨȘҲӦØ˂ɫԟȖ˄ҩǈƔɤłƈɋԠҩрȿ˫ЌѨȆƙ÷\u0380',
                            'message': 'ZȜĞɐͼԠśɻƫѮҰțӭfůɖĕԙԦɨĬӷԂΣˬɺ҇ÁǊѭ',
                            'arguments': [
                                        {
                                                        'name': 'mȅϓyһóʇȁCѻԍˌНÊŨǖǤ҃ȩ˱ˇȴŧΤǛȇɚԨ²s',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƽ)ʒǑі΅Ǆʮ[\x8dĻʒ˄гЂѷС ʹΠӃ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8123462178149039416,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѧ\x8cđӏd˔ɴάӵȘσԕǌϞǋʰĨ϶ʬήŵʱʎѼʃІͳ˦Mİ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '/ˤ˸ǊџǍŭӹӓǶ˷ɅуҠϩƦӞǿɼĀ˪Ԇ,HϽύ~ӫ:ɭ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'R',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϻήϫƋςǻǎƊƦƞԙҌȆǦŽуȥÔƸ\x95ҼϮƼɊѺƚљƶǨȚ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.749588:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '϶ғƵΧӤΥԬȷǢ˶ý÷ļ΄Ǚ҂Ä\x87ӣȰ˂O"˄Èɵȗ˦Fp',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x84ǟƹŰӒŝɷӟƹņƤɫ&ĤǴӕ˷ʏ\xa0ԭ˼ʱɬƋ§˾ȉҧȂ˲',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӱ˘V¡ɨǰǞͻѬƧ˻?ҳԍҸ?ƞȮ˖һŽ϶ʳcԓç˥ʷŗđ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.750390:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӁŪɝʉ]/мʈȀ¤ģȝϫ"ȖȎǺɕĆ-ǃȗĄȹȳ©Ŝэԫ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ť˾ÕϢφϠǲѝżŨâǝуìҴëʦɊɕ˨ЈńĵÖҹ´ǶԖҦł',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.751170:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ȉɾ\x86ӫɰΜaЄӧL[έѲԗżчńȇE[IӗæԢƤʀǈұçɴ',
                    'image_id': 'эԋǮÐŃ\x85XϞЙӌȵƥ{ɨ#ΨӪÜ\xadő҇Ɗ\u03a2ǞìɳËȨȮс',
                    'title': {
                            'catalog': 'φǈƙΈʤƋȦǟ\x80ŗŖŚҧǓɿƊǋφФȗǢʇ˃=ǀþÜ±ķΏ',
                            'message': 'ʡͽȳэҗɘк\x9eǵ˛ΜˊЫӳˁЁÈєϕŊǤπͺԊЃġ5ԩҊө',
                            'arguments': [
                                        {
                                                        'name': 'ԢʅƥɉǐӑΝǡÀԚʦƽӏќțӷϚӏҌʐżϖЙƟǗtʽˇƍƞ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ІʀöҏʩӯԟǿҦѠӼéȿĕ˪ӶɘÐóʑϑˠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.752855:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'òϓÍњнñŚ˂ХͱэІ1Ӱè',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˘ʿωˢʁ/ɠĖ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1541369814975612661,
                                                                        },
                                                    },
                                        {
                                                        'name': 'аѿҿӯ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3974420542821774032,
                                                                        },
                                                    },
                                        {
                                                        'name': 'əȂþ\x8dɽʄȨÚӽίёʯþțǏ\x93SύȴɰȻɵѺЫɃ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x87ҜСēҜȂ˜ҙЪҪɋèǙԩΆɭзǫĶǥšàĸԬˆʕҞΡɯλ',
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038bȶƤʠϑCƷȨKƚфĘа϶ÝʗʈʎǧƾƲȱԤћӹʶ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 952460.5535296183,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӇʣΫȗȏǡǛϼɶ\'ŀǄÀΖϘǐʇĥ"ѷΛ2˘ХЮҶ˽ȻǕÊ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҫʌ.ʱÜΝŤŧЀ˷Ȟųãѥ˟ϽΠȡӅс;IΗӕǞĵ\x87ҬkÉ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.755742:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ўʘʺńҖˋ˨GɅЃwɐãñʈȳ{ШιцĆԎǯ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2450434339798033015,
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ĲњŨѦѡ8?ĭŚƯƠȉԒo#Һ\x8bɈYӐóýΑU\x95ʼХĢ҅0',
                            'message': "6ǡЯʙͽéӽОƚԣǩ˴Ԭɼ҈ɩӖόĵ'ӰɈɹʞѱ^ʛƦş÷",
                            'arguments': [
                                        {
                                                        'name': 'Ů˃ſTϧĔ˻Ĭę\x9fцǗЗԬӻ»AЙӾӄ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 574097.4198993293,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӰьGνяAɬƈЩʎ˅ȴcѳPɾÞРϝƖ\u0380',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ъϻɺͱůfˬr ӫʃ˜ʏʪӛĩҠӎԫräζŃʱəӫӞ)ȵū',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҏȚΉǼϒxʡѴɔȢӼƠAϕШ\x89Șȟˇь¥ςЀɑΎN˗ɵɂ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȸȼǆ§ϼҶ#ũ8Ðѵ\x87iҾC\u038bҍқęΈҭ¤Ԓ\x89ҟ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҼғӀΣηв҄ɹΠѥӢјǰ˷dˋɍʕЉӻ~ҜȞŦЍѫЋȋҏǘ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΙȂɓ,˯˧ˎ¨ŢëЋŪȡɡӣɩѐԫм\x9bξͶ±ǥѫϑϰөӈ˗',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӼǈȼϞϰ\x9b҈ёђ´ǫĶ3ƭĄäέűеˈѿϵӜÇф˧ʾ¦ǉý',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЖΓϦӚăxϧƈŖ˅тҫ*ˡæԃ6ZßѣϤԧͶЀâ·ǩïɮέ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 914688.8690149512,
                                                                        },
                                                    },
                                        {
                                                        'name': 'vɠǰʳNβ0ř',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԔԛƢ\x93˛ΐřȱз\xa0',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1733750739708092688,
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ƯɳǋyȃŐƗτɬĶЃ÷ƭΩ¬ĈԇѿÀƠ5Ș»ɁĞʪϨƫ͵ȇ',
                    'image_id': '˴ҵѸĉˇ\x92ǡ÷WǉɓќϷ¹μҜϟ\x92҃śŀϋϞʠ˻ЈȀĭΝϯ',
                    'title': {
                            'catalog': 'Ɋ˖ĉßӣ\x98oˡкЄѨ\x90ǫҗ±Ȣц¢äϾπsлԌǚ˹ɔӧÔ|',
                            'message': 'ƅωˍź=ˌƈЗԪґĕϬ\x89\u038bĔùϒǋˌɵԘóȭвÓŤ\x8eņ˯Q',
                            'arguments': [
                                        {
                                                        'name': 'ЧцӦҧ˧ѷҫôˠϮͰǩΜ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.762015:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҌQжƓϽӄÞĿѷиӶ϶ǵȖΫĊ˕ΧŭԙҎƙǣҩϚÙǆНÙʈ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 557708.1386618327,
                                                                        },
                                                    },
                                        {
                                                        'name': '½ƂŐSИӵΌÅҦǯӬүƏˀтӁŢʫϛϾɮ҅\x8fʭϝԀʐх˰ɚ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'PһɶӔ\x89Ӝζ˒ҚÖЅ0\x94ϩѾОԞȮӌʩȤЩʍѧò˗ĐɉŬδ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѫđíʅÖϝĶԙĉόȿƚǎяĎяҘ4έҘΉβђҶж˼šЃ˓ǜ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ʛǅԋϮ\\ʐǨҼтȶͻɲʷ˘Ø˖#Аšŕ'Ӣˢ\u03a2ԮԐĒӺ\x95ί",
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѯқѥ[ћʻ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҙʔƗ#˺ýҏȮ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԃǻǑ<\u0378ŋФƀ.šȃҰǥ\x8bҺ˟ƙĭ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'łќǍϱԖԂ\u0378BѦӀRƼѕĒӪ˥ȢϬɒƋřʧȑ,ARԌŸ|Ǟ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.765756:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'Ʀȝ,ȤοЅKȾʕʮȼ\x9b\\ƮЌĴ\u0378а҉Ѣ¢ǬӵǝѾķѽǑӋǀ',
                            'message': 'ҢЩʆȰфťʘѐώɮ5^ȯҸÿxƑǅQɪÅͱ{ŴʧƚKͱΕϚ',
                            'arguments': [
                                        {
                                                        'name': 'Óȃσ\x90ć¬\xa0ŋʮ˹Άʆ\x8c&i²+ˍӗeѕРəƆéԄƗӮȫԄ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʷшÅƹӦȬ\u038bˌκ˸ԆKӾϽʙңцʜƸҽ×ѝъ¨҅ɒèʥђñ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '+ɠƖɣӃʁйΗѦʠ˷ǜŶƋŗӁ,ӏϨɵȘͽƆÃƌЌǏѻƱѾ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8208152995009853260,
                                                                        },
                                                    },
                                        {
                                                        'name': 'êKȃʹйŏгȉӿǝЊԢąχ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x88ðʘƶťǰʵˉʖķӒΫτȮǹˮȡҌϋǹƹΠЦˎňoˏɶƵ=',
                                                                        },
                                                    },
                                        {
                                                        'name': '4S\x89ķҽ\'ƍҁԗӳ\x81ǌӆԌōȏŔæX\u0381ѿӮϱt"ɢ\x90Ǯҥк',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8dîđͷǳԨҹЈːνңOҤЩǬȩϊϊȁzġ˔Ԑʛ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¼тѠƙȅӆc©дɑω\x91ӚӇǋɤϢǈ)˒ӳѢˍ~ƦƹнШɏμ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 186898.62982574926,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѹʋÚʢпΓӗʡɛˁȕӼʅ®ˡПіŪǭ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6990593639241805884,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʌǎ˝Љ-]ǞȄ9ʌ\x92ơѡлБ˶ΠFç͵˾В°Ŧѽд˛Ԑlv',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6424789383128990001,
                                                                        },
                                                    },
                                        {
                                                        'name': '+ȱvƐ˞ɞ\x88Ȓ\x9dӡʦĝȕ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'üŻӚǫѣçßϧϲƅұԉ\x9fȘǚϪԖȭԞΙϴɡ²Ǟ?ˇÊϵȒű',
                    'image_id': 'ϝӛȠȁӲŤ}\xadŁ¬ĊǳǋӮЫǦяћ҇ʰ°ʛĭħѴʥ\u0380:ϛɎ',
                    'title': {
                            'catalog': 'кźȢί\x8fbtȼӽd˪ӂʏѽë\x82',
                            'message': 'ˁҙǑɓ˳҈ôĤӉȰӸȠФïŊԚʔдɹȴÀnӼΆŠУǶзϽѧ',
                            'arguments': [
                                        {
                                                        'name': 'ǟ\x8bɻąĲƭ҉ϑӿѻ¤',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҇ЦϿχęʩ\x86ҏϺʞ\x8b¦ɗɧũ\x96+ҟȎʩӻȊ5ǷӐӯӈȃʨE',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԟ˒қĽά®ŰσƖѡȳ\x7fϜǄѓ©ˈӠŭԂěȱ\x90ȭ˼kʋϮë',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 414662.1251988097,
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ȵѻзԉġѧɰӻҎԜʔǇʔȋÕɈMƤϴʅͻƠ\\ӊĻȆώʻïʙ',
                            'message': '͵ȍɮĨŵǪќԌ,ÈοӋƴɎΓŰy³ƅҐ·΄ΝʓɒКƳњɝӿ',
                            'arguments': [
                                        {
                                                        'name': 'ҏҾԟĨ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԉ\u0379Ќ\x83ӛҕwʅƦřȑŨĤżμӻ\x8ańҚԋfɘȡĜ¸ʉѾăżȀ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҶҔȫҰγ¯ɰƏѹҧǹ½',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 587092.8565784722,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ķ]ƃӘӆŠ\x8d®Ύϒʪ\x7fÊzŠǁϭѲѲΘ»',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȭӔĪÔҨ½Ķ˞ҽκǦΘȻ\x92ɤ\x80ӁЇ=ė˄έ҄яµȰбʫĉʿ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4118167402371259124,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǳť˓Ƌēӭ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΕʙʘϝӰÖԗįϧӏɫԎѮřũ΅ΰҲT\x83ϏɁȌώϾǍɒǰŐҩ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĹăĶӡȔӨćï\u03795҇ɒʛǖΏƚѪŌжтѫҚŝ\x90ɟƸʹԁѩŅ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǋ\x94cîɄΤ\\£ɮµҞ\x9eʑʰźҐϿËƱԆӣʟіGɪžɾӲHʵ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "˹˦ԎΔƢƲ~ƣӹ/τ'Щϒԇӳһȱ˯ďƼ˽\x9dĹϥǍɞҵıǽ",
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŵԘǍӢӒӄϷǴȭƱʐķЈÛħđϣтưѸɵɃоԕƍłЍӯĦ˲',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϏӘĤˇŇàԘ҉ƁρӶԎѤXÜɋ3ƾɊǕʒ\x95Ƣƒϴг˝˻',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.776905:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ӴҵӓǰТɑϺԘɓϡìΛӠēБ(ɨκɝŪͽѸEɽЄƯʠԡΙʖ',
                    'image_id': 'ˁѧԅΝǌӵĴδɠҐƃÙѧʽĵǅǩϥķʡѮТáįņϕ˔ĶȨÝ',
                    'title': {
                            'catalog': 'Ҁͺ˘ұʧ\x80Ϛң@,ϟ˥>ЗĀЎѵ×ť\x98ɋ',
                            'message': 'ƃ\u0382БфνƤ¸ƻӊøǻːХǎʹɕŃɘԎ˴ϴ`гQϓϊȁʶ]Ȑ',
                            'arguments': [
                                        {
                                                        'name': 'ͿÆǈȀϸԔϳɢ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʑ\x97ϸӵơƛΝĪǹΝàŏȀgĽ´Οƚǰ\x84ȪČƟҎȼ¹ЍТŴʝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŇԜkвғТмӗÆȋŁƨөԌæǠ¬ϨȅŦџϔΈΆӵ¯ˁ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7478965792249154013,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʋɴŦƧ\u0378Ȃʙ¸ӖϹӚʙʶʖ҄ɠüҝħSΐ\x8dɱϗɃЫԍ¥ȔΖ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 106990.34198211634,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʴҿѰƽ^ȄԇȸѢЙԓ=pѠϖǏɔԂłǞ\x9eЋҖˮςοȗ҂Ыӣ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7736625954026618416,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʦѢ˹ËƻʁќʠĺҰp:Ҕɰ@ȃϫăӛԆĕ҉Ѭκșυϩϋ˥\u0381',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӋүUCƅЖҲӓɄɑı\x9eɝʶӑдȾњɬʛќϬGÜŧķϘȠΡʥ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƢěȫƺҎӣ/ģυɅʷ%ŖԎ\x98ɵȒƫÁΛvĻњϨΫˎɼĘϏѥ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¸u',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƋӣЈʖЋƤɓĸEǆɪԜǉ\u0378ēƫуҔԧҴɇ±АъľƋñʿàɴ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǀЫωVǈ-ԏ˦-Ǵӏ¿τÃțʚˣӦ,ёĄЄѼϫΥƕʩѥԎ·',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ůkы¿\x99Њȉ˨˸ԓ1àʇǟɠЉ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϧ\x93Λ\x95Ϩŗд˛ʆȝ\x92ϣZȥѾ\x94ǗȁûñυƧɯY\u038bζҞЅɋ΄',
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ƯϳϤғԝǲ˲ȏмcºƮΝϒҺѕǈƣҔ˷áÖʌҁґŋĻɑǟΔ',
                            'message': 'ЃȅÍƾiǰȧνԌжͿƳîǊÊЮǀƇοʸЁ\u0380®ũĂɤя«Uű',
                            'arguments': [
                                        {
                                                        'name': 'ĘƐ³ԣ\x94ƮӀ7ƾǥ¼ǯǊƩxϟěŬ;іȴςқʬԙτЎȄЇƲ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5848456131317965216,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʈґ˷ѦɩΕʾҳτиMNŸȱШϊƫё\x81IȧĿɍ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ưȉѸƄь',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3396011063314891138,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŠɲԚҁ\xa0əҾ¸й\x8eƉơΦˊѢҰӓ\x9eɆΗɫθҾǓԕӌϨϽǩϦ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ';эБΠ˴ьпȣԑè(ʳɡлŮʢȋǿÛю)Óј',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Їȋ\u038bэǛѵͳ¦ї¹ҙżǕȵŏ]ʆÌϊУѩ\x98ЊϔʰĹΤʣʾˈ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƞҔŹѻӷЏТƇҔԤˍЭȬˁˡγĠҗ˙ʞǚԚȱϕѢӦӡШśԟ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 130663.72652536433,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɏÅэʧ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6745207252105466202,
                                                                        },
                                                    },
                                        {
                                                        'name': 'đŧѠǍ\x93éilцԈάχҌʪˊMԚɮ¥=ІƁŏԫU\u038dPaǁԥ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˃¯Ⱥ˼ȃʁĽćҀрùǡҨɭԫŖǡЧ¯Ѓ˼¡{ӫԐǽ\x81ǋӷʠ',
                                                                        },
                                                    },
                                        {
                                                        'name': '}ɨ\x87ˑӹɯǔѝǻȁīƮǬԪáŕ˸ЎŚѳʣѣӑӉғƾТţҁҗ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŃaʁTϽŕǗÿ˯Ǧͳʠ¥ӌӢÓѽԌĮ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ZʋΊȾ%ΨŶĢΰʼ£΅ΚĎϱŚĺԭҥ¯ӎǩɅѾɣϹɛÌ˄a',
                    'image_id': "\x95Čýʩԏѿĕġ¿ǭҧ=ϝӞĶțхĉϾ'ǳ¢ͰσҒǒ?˯ǯї",
                    'title': {
                            'catalog': 'į\x86ºŪlϚѸ©®ҀśʪΤY˾ųɱ¬&Ҷ!ˣĴOì¬ԛʣͰȃ',
                            'message': 'ԙͷԞǲǶʢΤϯԡƤ˸\u0383ÓѽæľǘǫЖo\x90ǀɲćΕɼÿѴŲ^',
                            'arguments': [
                                        {
                                                        'name': 'ơĪҾĺÏMƕ\xa0ʸăҌұªԚԨųѢǃô\x8eˈū',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŎƜƌM˓SҸƛҊğŁʓεԨǹˬƧӹƭώЌùəɾƋȳ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8632392107599382710,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΉӣǼǔӻҩҶŻˮĬлˡқǧҘгƭ6Ӑćʉ\xa0г',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ёʄѪԃҴ³',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϢȌ¦ɽзıϞИӷԢȁŜӕ+ӌ0ʧUƪӌљ´ʭ$',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8cƬƜФ˫ʕǪԆԬѵ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˬӲɔ\x9cʳHqӚϸɦÍĘĢŬëʲĻŗѸηƎЗǈ×ĶǞēǏĢϯ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4249572899456828270,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԉk',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӫŋϔ\xa0ʟӏGӟҝʌƽҜǤЍǉõîŃϱlҥНȤžʅϫҰ\x91ωӊ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -23955.668047570187,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ыiʡϲ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.791316:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ˮɖő\x9aʆ˵[uƓÅĽ˛є#ӦӒʣдðȎȬǊƚЋrӣÜѥʡƝ',
                            'message': 'ŕȯƒɇèЇљ\u0380ÃͰЌȕҼԍӲČ˩ĹҧŗɑΗʈŲЀԔeԙПA',
                            'arguments': [
                                        {
                                                        'name': '·˯ԂЯ5ȶ+ÉѤǬԟΓ´$ǨƂ|ʹǘƔʍǘћӜ˝ӹɶżǪŵ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ªιFʼәбÒ\x83;əӆʹΠǇtˏCЪћъɨƉþǨѢ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѽӠǻƭ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x90¸ǱӶĥ\\ʇưŕˎsɞƑӆɛ˰Ǝǡ2ΖӃɊƥΠɍƦǋΈҋƫ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʃӛԤ$ȗ¾Śd+ƶ\x85ХŤҩƐɦLϻƾȽŬ=˼Ήɻ˕Ҏтə3',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĊҘʌʄǁġɓɓγǶ҃\x8cӜwŗùɎʔJҰӴЙÑԑ¸ΒԂѤΒʙ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '-Șǂ³NƫɈȆӠςψțԥ˛ʝыɓԫıпШ˒Ҩ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԄΌ\x93Ą~',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 2750.487981190614,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0382ŖΡGӏːƆØãʁ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'þǍԓƎʃ˸ѝƔў˩ʉҏƭΞŢȷɍӘ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': '˶ǒǣŞпɏέ\x93!Ϣӿ¼ԠÌ*ɋњ\u03a2ѮĦȳƏʳԏӲɧȖŰƠρ',
                    'image_id': 'Ʈ;ϛ\x9bϯlӪνԡ¸ӧҸőƆ#Ԟԓ\x97Ƚƛ\u03a2þϸɷӅ˰ʤƧГÀ',
                    'title': {
                            'catalog': 'ԟåҔϡsȜøό',
                            'message': 'ʖɻƊЕσjЫ϶ɔѺӥӼԥшɯ\x86˪ůŐșIϨςѱɞkӷǾʨͻ',
                            'arguments': [
                                        {
                                                        'name': 'ӢѻʤЧӌɪ"цŘ ϏӘęĈʵФѓӤΒÂȵЮǫ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɆĿ~ŕ˔ŕ\u0383Ƽ΅ŨȺǶźӮВѧϢÖĠʉΥʈwŞӦΑјºєʲ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Þ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5168659634827290832,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҁÌѶдԊʬѩɉϙĸ˔ЁƐ\x80ĨкŢħӲʉɵҽƃčʕȩ\x9eÐҗο',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 632681.1470948971,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɞͲүsƖŠԣȇĹȎĊq\u0380Ӽ@ƦãȂԎʔɌцжЍõϽʯɥ/ſ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 600350.191013578,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӹïğ˃Ñίӽ˲ӁǯÓʒÞǏƐɼк҂ΔŗȻϙʌ\x99ǒ`ΜЋĊχ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѕӈħЫчġ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɖùŠ×éɇȣņʢÞČǤƝ˰*-ɑMΙʿ\x8fÃӐұƚǿǽΠѮġ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѭӈI\x9eƬԀνʛѡ˥ǱŷƚǂҵȯɧҘŝ¡:±ʫЖPǓԩѢǃȽ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.799523:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ġŴ\x9fғĚӢЖԪʬΔέϞӓϯԦѳǛύһԀĪЯ_ͳ|hйÊ}ʳ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ǣ˘\x9a˘ԉŌčЦǧӀƍԪο˥ʦ˱ѣίÐ҂ǫ\x7fʡ`ѥӆRČϔӒ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʃ¯ЎҷƜľщǓδǕłπлuıѺ;ϲ҇ԇɯèĂϞ`ˆΠРĭϬ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7574675717614739051,
                                                                        },
                                                    },
                                        {
                                                        'name': 'YӮɳЛϯÉΦҾІʝČͼƘȭДҡêө½ή¿ʷʛñEǺș¬Ҫƃ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'ҀɲʹӉȖĸсÍћЏɟәϣʫ\x9dϑ˺Ɇ¿ǹƲÐҔșƫgǷǖũԆ',
                            'message': 'ЀDӏɡЗʄǸƈˢҕΨȫƒҐъ^ʠ¦Ӈµ˶ЭбÚҸÃǶȂȣϖ',
                            'arguments': [
                                        {
                                                        'name': 'ŦЀżϘǺІɒĽԖƳʯÁνìȹġʆȍДХҤäΐλ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʆëӜʰʹ\x95ҩ,ĥ϶ȼɑ9Ŧҍԙ\x98',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'TɓΊκʬʪʑϋĬ˵Әƣƽʙ7ͼӕƼÊxϐŀŞƂӡǙʹȀφE',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.802479:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': "ϹϦȦƄƛ\x84'ǝΉĕуˤ΄ƹ£˲ҶǉΨо˚âĤ\x9aɇ¹",
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 966188.2147208916,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɲ¨Ɔ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˲ʭˤжǢѳƂѮɔ/ȳΡˆ:',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'жӥȜ\x9fǮ²џźȏϙ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '@Ρĸʲw¾Ǉ\x91ыЁԉΧʍƑǹO',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Л@бυōʔЋͷ9ʫɤëѾǞМӪϬŨ"ƹϠɣнϪŅʮǩϝԧӃ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.804938:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȎлǌԅБɻʋ6Ϋ\x8eҖϡǋǈVŰф',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.805331:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                },
                {
                    'icon_id': 'ɍʕˮɠԛͼƱЂӧІҼưɐ(ȀԘĪʟĘɵɕΦ\x83ҍΜǬȖѵɝě',
                    'image_id': 'ǸƍɯÎËύӆзȻѨȰȜ˙ÏO\x99ʪˤȬƛʑƜӔҖшѷĀŮƟą',
                    'title': {
                            'catalog': 'ϧЉЂ\x8cƙ˓ɾǙҫΉѴѕŉнȈǨƺÂņǾaƯƽуǏʕ\x8cˢǎƠ',
                            'message': '˂ƹȊ½ƟҼɊω˦Ĩ&Ԛ˥ÄӝНˮƿʮȦϷѪ˥ſʟєҐӗƝϐ',
                            'arguments': [
                                        {
                                                        'name': '[əʧôpԏЄӱɫʬԪԉ˅ϟ1jĸϋԘ\x85ό\x84Ͳ˽ʄӗıˣϞΠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.806577:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȏԣʵ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0380БԌɇҼҁ:ttÙєƙȭϿҀѢԭӵʂúmɸĊӛӞĸȨ"1ӑ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӗʲϲʓĄҙĤ˫а˃ɈI\x8e\x89сʎΛǑǹ\x96ϱҏ¹ōϫͶƻŰѻ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЎŪѰçҝǐĈϞη',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЭϞԎͶЅԍъĀчɖҰĦҩӚЀΖɣʺҾҁ˧тѵ(Ƨ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʔ5ϛÿ\x82³цţJn3µȵ¿ȳɱʶįM',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʡӌÊȚɷ6ͻȯςČХɁ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԆȀќȟȽQǮ±ĔŜE҈ɳćӼҁǂÂҮӕɎŻOˆ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'τRĪˉĝ{=ɓЩȋѲφЍŵî',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    'hint': {
                            'catalog': 'įξұΣΎϰǍɋԩ҆\x98ƺˀÿЌϳsӚc_ŶˎXöїίǙƲҠȚ',
                            'message': 'ɼϦӗԔͶ@ǂƢчƟҿʨҒбŶɀŸп;ЬǆɦƍʥЇȸƈƢƝȆ',
                            'arguments': [
                                        {
                                                        'name': 'Ğχіӳ/Əԫȇˮӽw8ӼΠʍƤǮƾƸԍО\x9aȑʆǃsǎйBȺ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĳȅʺӭԧĲįӭŅɄÚĨϝċˇɅɑωůƶϗt\x8aƖwɳӦˆ"ԧ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȅ]жǌ°ԡϢ\x96ǴáZɷџ¨ԚβɇC\u0378ƛϯΚǾę˖ð¹ǭʄͻ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӀҥυÓБʺʗϔɅǈĈíκʽӌ\x96˂҆?ӄΦɥҾθ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǮŕεŐ\x84ȤшԋɞȽ\x98ȋȀΒġЧЈɳɜƠŴϰÞĶӂ{͵ůƫŷ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŗ˙ʩȂѠǲϖΌa\x8bõΑ Ʋ}ÿɓήфˏàǜʓȃŷ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˧ð˾?ȬЇńwǸƻӊДē¶ǏŎ˵ϼўõϥ ɽΖƬΉɚˈӼí',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѹʽϞаƛѩȤ*Ι\x901ɃҶţҐƺ·|ļ+ʈ0ϻχӾΪ\x8eŤkz',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƶʄǂсƳψʼίԚҋŵ˰ȧǅɴˬГӚсŬ4ɂϿ¼ǘЊЙҔ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8361838149292055167,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǐҕϪȣӴΠɏǄ¬ńȓγ9\x93č\x9cȧmӕͼə',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x95ǢȩбϰкċΣèГ͵ŌқΤϑѢĆȺΚ¹ЂЯʧӀȘȄɝ}ť˳',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĶɡќɬɅΛ˹ӁƑӡϚŌχʧ+\x80ԄѦЬґǙŨѕНҭҭƹўƺӃ',
                                                                        },
                                                    },
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'icons': [
            ],

        },
    ),
]
