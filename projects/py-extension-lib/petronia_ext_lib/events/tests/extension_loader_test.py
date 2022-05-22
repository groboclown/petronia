# GENERATED CODE - DO NOT MODIFY

"""
Tests for the extension_loader module.
Extension petronia.core.api.extension_loader, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import extension_loader


class LoadExtensionRequestEventTest(unittest.TestCase):
    """
    Tests for LoadExtensionRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOAD_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionRequestEvent.parse_data(test_data)
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
        for test_name, test_data in LOAD_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOAD_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LoadExtensionRequestEvent'),
            ),

        ),
    ),

]


LOAD_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ýȔǋ§ÒРɦȃȠђĨɜ·śϛɻʅʀŋɼYʿѹ΄ʤϱ´ӆȆˣ',
            'minimum_version': [
                -9089005941558465845,
                -6932028676578337264,
                -1825258232014883450,
            ],
            'below_version': [
                -7728092734111505334,
                -194314345041567508,
                -872725979724030427,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ĭ˽ɑ',

        },
    ),
]


class MessageArgumentValueTest(unittest.TestCase):
    """
    Tests for MessageArgumentValue
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MESSAGE_ARGUMENT_VALUE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.MessageArgumentValue.parse_data(test_data)
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
                res = extension_loader.MessageArgumentValue.parse_data(test_data)
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
            '$': 'ȴßřŮѾ*Ͱ.ΣЍԛþŁĵWȌүøϐ)ďʭϋщǳúјҚƿγ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 1407167078601514254,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 412857.694386007,
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
            '$': '20220522:173336.917338:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'IʠĩʼѢʠξTҗ˼ϐuɆ˰ȿЇǚ=;Ф˄ıԢǈŠёʨİȺˊ',
                'ǿũѤŷȾҙЍĢȜӱͶμϱȲŃɱĐŌƅӏĔRŰЊҳûÐӢøЙ',
                'ʿȫ4ʘǻҧ˵ƢȀŜԍÛƬӞϗҺҐ®ĞӺѼÐ¯ҙêθҰǶԪˎ',
                'ƐҵԌѧòǻȻϟȔʈүμѨȠΗӺќӫ2мϾЋӮĥӎVʸђŝ ',
                'ĽԣĀxЈĹ¶ӂѰӷĪόsŝŵRӪҿĖͼßŸ¢ÉĦҬ˄ȴ\u038bҧ',
                'ϥğϞɮś\xadÆȕȪ\x9cτχǖгżЉɖѩŕ5ǝÉԋʙԘԔҰɉ#·',
                'ʞŜöӜēȪϙƮўԏʤɜΣ@ʕѬʺê+Пbå˅Ѽl˄ˮϙʜү',
                'ӑ«đБơƆǍ\x84ːϪÍҸʶтĳ˳ɹԁӗ\x9fǶʪƠǐϩňп·Á#',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -8781515210092461485,
                1856055232235352949,
                8808964016226357300,
                1850177111820720617,
                -8375534954296937191,
                5540961750845341394,
                2103926691409346340,
                3460861828661599079,
                4572794884410881514,
                -7801525604842885042,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                -14275.472418427671,
                -45163.70424989856,
                309494.73829382856,
                489874.4906941324,
                560501.5966166996,
                795809.1384466271,
                81547.60839579292,
                635589.4667084805,
                352421.92591296684,
                -28204.912831889014,
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
                True,
                True,
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
                '20220522:173337.372664:+0000',
                '20220522:173337.381794:+0000',
                '20220522:173337.390634:+0000',
                '20220522:173337.398938:+0000',
                '20220522:173337.408075:+0000',
                '20220522:173337.417322:+0000',
                '20220522:173337.426437:+0000',
                '20220522:173337.435132:+0000',
                '20220522:173337.443511:+0000',
                '20220522:173337.452156:+0000',
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
                res = extension_loader.MessageArgument.parse_data(test_data)
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
                res = extension_loader.MessageArgument.parse_data(test_data)
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
            'name': 'ляΗĥқ}ӐƵΤɿѝԏϙĸѬĊŃǂħϨʌӟ˦ĘȮƯÍ\\ҳ',
            'value': {
                '^': 'bool',
                '$': False,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'љ',

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
                res = extension_loader.LocalizableMessage.parse_data(test_data)
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
                res = extension_loader.LocalizableMessage.parse_data(test_data)
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
            'catalog': 'ŢíÆ˱ʙ˰ŻϋɢФԟƞƉϟĸŕrхǧ¤˥ѶȽǳԡѶОɧϗѝ',
            'message': 'ˑӆ¤ѳͰӕñƕҵğɭԁҙƢ\u0382\x83ΫҿȚ³ƽȲ\x97\u0382ǨȷŴԋƿʤ',
            'arguments': [
                {
                    'name': 'ϰʑØŎɌ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20220522:173335.938203:+0000',
                                        '20220522:173335.946300:+0000',
                                        '20220522:173335.955222:+0000',
                                        '20220522:173335.964224:+0000',
                                        '20220522:173335.974810:+0000',
                                        '20220522:173335.984428:+0000',
                                        '20220522:173335.993401:+0000',
                                        '20220522:173336.002278:+0000',
                                        '20220522:173336.010359:+0000',
                                        '20220522:173336.018643:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ԮĒѽʖϕǧͿÝ\u038dǇԞ#ʌʧϨǴÚӣ*Ρ҂',
                    'value': {
                            '^': 'float',
                            '$': 474381.34796933807,
                        },
                },
                {
                    'name': 'ĦƕðϮ\x90˘ǹђҶ¹˺ŲŠ˃ƹǋʹÈȱɯǪҞӮԑĸaÉ»ҕǤ',
                    'value': {
                            '^': 'float',
                            '$': 11036.189008433357,
                        },
                },
                {
                    'name': 'ƛȡѤϼɋ/«Λƚ\x9bħƊɽƧBÃȭʽʆÎŶƙźhÂԑmӎҼӰ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        278220.9471460464,
                                        887538.3370269915,
                                        576728.0628633995,
                                        783057.6817453377,
                                        167652.98302982567,
                                        783596.145806359,
                                        932385.7901784892,
                                        192578.81315395294,
                                        -32355.16709754338,
                                        96971.0902150484,
                                    ],
                        },
                },
                {
                    'name': '´Ţʦ\u0381˟ϴƖȕѡ\x8aҏÄɯ\u0381ɚŔӭԩó\x8dѨɗԭЉӱеɂŲǌë',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        7385769813261810135,
                                        8777402571197959372,
                                        7474525319603121694,
                                        -3602482372468139831,
                                        1441372313873186642,
                                        -3392195278010577070,
                                        5676549433332578578,
                                        6943680644188092244,
                                        -1401297485981649863,
                                        4170641879459150901,
                                    ],
                        },
                },
                {
                    'name': 'ǅ',
                    'value': {
                            '^': 'int',
                            '$': 6403745046372703749,
                        },
                },
                {
                    'name': 'Ĝ$ϾƑƷүĐƅϟϩïlĞśӮеĶǠ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'Ǟǒ\x91ĺɲbÜÝӿØAӖǳ\x8bĆ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        27228.636937509407,
                                        95089.12332647317,
                                        595555.9310584875,
                                        654128.0590089696,
                                        659721.5905860934,
                                        667.5929788705107,
                                        118988.75914524973,
                                        350913.3987381389,
                                        930633.3659337508,
                                        304883.81898244563,
                                    ],
                        },
                },
                {
                    'name': "ɸʌӼGǙԟјʋ˚ěӥ³ʵĳĔӖ\x8c\x8c'",
                    'value': {
                            '^': 'int',
                            '$': 8314380535145461440,
                        },
                },
                {
                    'name': 'ԞΑǻ˚±ɮИŰʈ±ЌʳJΪхҚĕӆӼƣˬŧ&НǓĠV˴Ώí',
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

            'catalog': 'ѷԫ',

            'message': 'θ',

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
                res = extension_loader.Error.parse_data(test_data)
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
                res = extension_loader.Error.parse_data(test_data)
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
            'identifier': 'ѱǔԙˑųƬƒčϑξĕÎҫԬӥАmÇΦʼǫМԥǙАɯӝ˶rP',
            'categories': [
                'internal',
                'invalid-user-action',
                'internal',
                'internal',
                'file',
                'access-restriction',
                'access-restriction',
                'internal',
                'network',
                'configuration',
            ],
            'source': 'ў¦Κĳɐĩԃ*ȗ§ʃɉϧ)ϴьǬˑҘȮĽԖȓƯ˰ɏɣĵƥe',
            'messages': [
                {
                    'catalog': 'æхƐӖ҄ʎ-ʼПŠȁϡˠʰʘÄѝĆ\u038bԍҟѥĚŜ\\Бʔ`źӓ',
                    'message': 'Õб¹ӽЏũΡ\x91ϡŕ\u0381В`b˄ʦӹɥϑͲЍƾȤцɮӼԕ¨@Q',
                    'arguments': [
                            {
                                        'name': 'ȁ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            929398.9515814534,
                                                                            340028.98774231126,
                                                                            351758.51412952394,
                                                                            758469.8155927947,
                                                                            523120.8420752613,
                                                                            471379.9206861104,
                                                                            480697.01928190596,
                                                                            214474.18011491903,
                                                                            2672.686092801916,
                                                                            826873.5819148056,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '0ˡ\x8d˕ĽhɐǒɯɻѧƮΝҐϲɑɶɦŏʈǠΘϠ˶ıȽøПv#',
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
                                        'name': 'Ó÷ſӤ9Ӟι',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'њΰǏʝϤưЉƦЌӋŚ\x9fˍǩЉԎ[ȁǏӭɣЖñGƊԗ´˧˟ʤ',
                                                    },
                                    },
                            {
                                        'name': 'Ѹïъ΅ɤβPǰ˚ϕ΄эĕ\x81ɻëŚLɪʉϠүтҴǊʔƪE˧į',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'æù\x9eƉˇӛš,¹ȼ\u0381Џ\x84ȴŶpкА(ϨĴўϼƽϗЛґɌTР',
                                                                            'ũҔӚ_ңӑ¥ƚĉʍˉÂӖįǞƂӭϺ}ʰĢġÈFӎԀįԌǆΑ',
                                                                            '¤ʩβɶē1ħƴɮϥԧΤѐėŞͷūС?ϫͽˈŲɁǐӊНŭǶï',
                                                                            'дƒƐѰΏԛeŮѤĘϻʎăTÑƘ\x88ѷԁˏύdԍXX˼Ӈ\x82вx',
                                                                            'бӚχɦвßʝŚȗӅƅʢŵэҒӓˬ˳Ï(|ĘpʯџǏµɵЗ\xa0',
                                                                            'ƻ\x82y²Ӆ҈Ũ²ˬsАǞɬԆȹ\x8dћªѦЄΛԉɭʧʬ\x8dԨСòԘ',
                                                                            'źʠǧϽΫʜʧɨ\x81ͺǬ(ƥæˡĈȵÖƷδȌ¡ѕFʚè͵ń,Ҳ',
                                                                            'ϿǻϳӸɇėʁ˨ƗЎԧǪïϰûķӅɿιȢĤĥ˨ϗ˔ҥîϿ\x9bÐ',
                                                                            'ϸçȸ\u0378{˝\x80ǼƭǅƨАѪɚˏӄňкԐɐc~һԄ\u0381ҚˬӃдɹ',
                                                                            'Ǎ¦ˌѳԜYĒŀÙɂÒÒω˱ʞϽċёӸш\x89ʂřã\x91ӵŀһ¨Ӵ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǆУ\x91Ъ˩ҿЁћӑϹ*˖ɢŉӔ<Űɒ/ԁҊȚǭϛϽЭ¦\x92ʎБ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            580993.3681263685,
                                                                            -14016.726951563047,
                                                                            797845.7889005044,
                                                                            452852.0918824171,
                                                                            461155.18600777956,
                                                                            469091.94311638083,
                                                                            951934.9606003719,
                                                                            717408.1935081469,
                                                                            283889.51580387633,
                                                                            73247.24231406488,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˄ʛϱæƉʆП˚ŕSͿӢ÷',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            316727.25741319265,
                                                                            856396.461047871,
                                                                            62098.81119299561,
                                                                            -13353.847332717021,
                                                                            -50057.46902158513,
                                                                            272764.9301602218,
                                                                            628974.6422397329,
                                                                            183554.12764123094,
                                                                            -84648.56017861517,
                                                                            385708.1741806766,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȠǷʬƫӼΖƞþǔǟȬԦҼӱԇɪƷǢԤŔϨ5ϯ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173328.114796:+0000',
                                                                            '20220522:173328.123882:+0000',
                                                                            '20220522:173328.133213:+0000',
                                                                            '20220522:173328.141613:+0000',
                                                                            '20220522:173328.150756:+0000',
                                                                            '20220522:173328.159921:+0000',
                                                                            '20220522:173328.169251:+0000',
                                                                            '20220522:173328.177822:+0000',
                                                                            '20220522:173328.187147:+0000',
                                                                            '20220522:173328.196194:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӧԨcȞƶǎѕʢɑûӛưΎȄԊϐÏ˘\x93Ɖüӯɬϔǀɮӭ\x86Ѵǥ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173328.238703:+0000',
                                                                            '20220522:173328.247383:+0000',
                                                                            '20220522:173328.256652:+0000',
                                                                            '20220522:173328.265162:+0000',
                                                                            '20220522:173328.274228:+0000',
                                                                            '20220522:173328.283223:+0000',
                                                                            '20220522:173328.291646:+0000',
                                                                            '20220522:173328.300038:+0000',
                                                                            '20220522:173328.308976:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'd˴ђϣ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173328.352136:+0000',
                                                                            '20220522:173328.360336:+0000',
                                                                            '20220522:173328.369405:+0000',
                                                                            '20220522:173328.377620:+0000',
                                                                            '20220522:173328.386560:+0000',
                                                                            '20220522:173328.394718:+0000',
                                                                            '20220522:173328.403966:+0000',
                                                                            '20220522:173328.412777:+0000',
                                                                            '20220522:173328.421705:+0000',
                                                                            '20220522:173328.430944:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ŀá\x84KŌě˸дƪȐ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -2094.9247739648854,
                                                                            426021.6975677591,
                                                                            694603.6649155236,
                                                                            624894.3669850483,
                                                                            112444.9006739521,
                                                                            284922.46742700436,
                                                                            556682.3897128346,
                                                                            50696.56927231816,
                                                                            983218.3791871727,
                                                                            629113.9124899727,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '¤ͳŅюʰԛ΅[ԩѨӵɨůВaƋĿўҔҙςӥΦШӺƑчäʹ\x8f',
                    'message': 'łʭѶҁĲϲǥŌʱ\x81ȃɭѾȤϏυȘұǡΝɻǳԘˌ\x85ȶͰ˱ʀҘ',
                    'arguments': [
                            {
                                        'name': 'ÚҷЮ·ǐҲ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173328.633857:+0000',
                                                                            '20220522:173328.642121:+0000',
                                                                            '20220522:173328.650425:+0000',
                                                                            '20220522:173328.659234:+0000',
                                                                            '20220522:173328.668035:+0000',
                                                                            '20220522:173328.676988:+0000',
                                                                            '20220522:173328.686262:+0000',
                                                                            '20220522:173328.695485:+0000',
                                                                            '20220522:173328.706658:+0000',
                                                                            '20220522:173328.716310:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҵØǳϻƠŹȯϤ\x90řȰԡδϪҲ«˼ȹԓĴÜśАʇΘƀįÈεЍ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173328.761740:+0000',
                                                                            '20220522:173328.769971:+0000',
                                                                            '20220522:173328.778894:+0000',
                                                                            '20220522:173328.788006:+0000',
                                                                            '20220522:173328.797786:+0000',
                                                                            '20220522:173328.806965:+0000',
                                                                            '20220522:173328.815391:+0000',
                                                                            '20220522:173328.824466:+0000',
                                                                            '20220522:173328.833721:+0000',
                                                                            '20220522:173328.843283:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŕϽӖþĎк',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173328.889439:+0000',
                                                                            '20220522:173328.898665:+0000',
                                                                            '20220522:173328.907648:+0000',
                                                                            '20220522:173328.916653:+0000',
                                                                            '20220522:173328.925087:+0000',
                                                                            '20220522:173328.933603:+0000',
                                                                            '20220522:173328.942459:+0000',
                                                                            '20220522:173328.951514:+0000',
                                                                            '20220522:173328.959811:+0000',
                                                                            '20220522:173328.968927:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɖϙɫӹʘġƟ˝ķӾ°ұлőǈүѱϛғC˧ƆРȢ˳#ͻûΔΏ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173329.011213:+0000',
                                                    },
                                    },
                            {
                                        'name': '˂ϨѱȂȆБГĊŷЅȿ6ӍpɞǞüɪ0ȿ\x86Wɺ"ʩ¢ƕēņú',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'χƜǾˢҀĭѓɃʴψŤƝǱӜŔʣҽʡǗɘѓȢҕБʳҨ|A¢Ю',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ǹӒӮƷϝΘǍϸɶӳȊÃϒΠЕ.ΊƬķČьʣӳİӢЉЗūˇн',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6566387157081376917,
                                                                            -7396343604147838731,
                                                                            -1323936225133757287,
                                                                            3333095792597579478,
                                                                            -3592208359250038596,
                                                                            3695321339615534783,
                                                                            243174040211801649,
                                                                            8374987881635324074,
                                                                            4376891491631004898,
                                                                            -3842857046079580894,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ψOˀΓбΨǯϥ¦Dχ²ɶπĻæɵɺтӯƲϝɈsВɟɀԁяБ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6077728885115167401,
                                                                            -8889453248229973080,
                                                                            -7307220891836273017,
                                                                            -4548553940864849328,
                                                                            -883352040813853273,
                                                                            -7875449668072126055,
                                                                            1719603725671018644,
                                                                            7516854028267743059,
                                                                            7953619403966867025,
                                                                            -6353198150719193846,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '_ŚgΝЛċïЊ҇Mƌ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ϩ!ԥūϐƨʠưӶƔ\x91',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2788118162894103865,
                                                                            -3371739013679831505,
                                                                            4043780703306800970,
                                                                            -9184014434771966086,
                                                                            -3192887153380719624,
                                                                            6369422154957330479,
                                                                            1648797967814285109,
                                                                            1405674389961839066,
                                                                            -7252093988267517547,
                                                                            6462273799667574611,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ÉƩ\xa0Ģeˤˀġ',
                    'message': 'ƀ\x85҉ƸӋЧŷǿ\x98˔ȓҟȡҳ\x9cвѐşӖǶЍґ\xa0ҞҩöƺŊQů',
                    'arguments': [
                            {
                                        'name': 'Ϥʅ6ƄЊĐºĤʶíΓŶɴѷҚˡЭɸӠѬ¿',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173329.647239:+0000',
                                                                            '20220522:173329.656229:+0000',
                                                                            '20220522:173329.664617:+0000',
                                                                            '20220522:173329.673778:+0000',
                                                                            '20220522:173329.682292:+0000',
                                                                            '20220522:173329.691313:+0000',
                                                                            '20220522:173329.699923:+0000',
                                                                            '20220522:173329.708931:+0000',
                                                                            '20220522:173329.717503:+0000',
                                                                            '20220522:173329.726777:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʖĝŤҥ\x84',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˶˛ʟ˼ŏɼþȜϧѕƋӊϬɕ7ï&ǒҺȈȸΏǧ©пѕͺ˥˖ʛ',
                                                    },
                                    },
                            {
                                        'name': 'ìяϜ\\ǞƼӌɥʹҨȑ³ƮʮѺӵŎōԀ»ūăӁtӧzŇŕNν',
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
                                        'name': '˩ùƘǢӯ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4638078912636079334,
                                                    },
                                    },
                            {
                                        'name': 'ʠщсʦϰǓˬŬĮГΛєôˉϝłˮкȻқſˀ\x84άǟɡёʷȅʘ',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЮȮŢɌӎĥ¼ťäȹʞɟʇЊ˳ʴϨŎѵÌǸуў@ä˽ԬȞӚȼ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5290955604739278289,
                                                    },
                                    },
                            {
                                        'name': 'ԤбҹƯԟëƀʐʥrԊѝǄƟɪə\x83oƪŧ3ýͲ<ωӹчγ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173330.123007:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ӯ˪æάѯ˼Iœ˟ɅҸ',
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
                                        'name': "lϭ.ȨΜ'ɼϑǍYќњжѫñĖɼЎӕ´ЎКȵʂПϛӿѩƕϋ",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': "ˤ'˵čӿ\u0379р",
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7693497835947483944,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʋґ²ϜƃҎůćжĲӣϣӄĴǻʥӪCрɾ˙ůԪҒɯͶъǋ\x7fг',
                    'message': 'lɜɧϱ\u038dʉǸȆϟƴγŝϹԑӊBfхdжǗӟϹƆ;ϯѵśҲѰ',
                    'arguments': [
                            {
                                        'name': 'ѮЌˍӐΌӢƫԨÈ\x9dҊЗҤčɥξ\x80ǕөƊйиțѧӋφŃЪ3Ä',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϻƹƇə±±ϕɐ"ԔԐˡ\x9cɂˠ¸ԬſˆӢǃŏʥǜ\xa0ёǡ\x84ʹȌ',
                                                    },
                                    },
                            {
                                        'name': 'ĞϸɌzϠƁ\x82·ҰǘĲvǱǨӹǺ҃˰Ӫ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ͳƟγ¸Ѫ˸_ʿǪåɺǊжԍЮ:6јƏПβŧ·уżȉΫg˪į',
                                                    },
                                    },
                            {
                                        'name': 'ȶͼџđ\x94φʄÙДϒθϬʒRĊ˗ÞʑԁƹǙĨӃΫȀ-NʉқB',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƤȷȻԉǃŹ˫Ґ˓Ôʽü\u0379Ӆ¹ͻγĈҏɡͶѻ.Ћӥ˩ίӞ҆ˆ',
                                                    },
                                    },
                            {
                                        'name': 'Öfɉʔ˘ɅsƏȡ',
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
                                        'name': 'Ǩ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173330.616301:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ьɘйǅӊTĽВªԇƽ0ɕʻLʌԚȵаƹҵɘХŻ¨άƑƐΤ͵',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173330.650768:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x98@ϯϱІĊƲɻȎПҦ¹ŒíÆĸԞ҂\x9dϵѳқԘÇǢƎˢ\x92ϖМ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5995987500139727852,
                                                    },
                                    },
                            {
                                        'name': 'ϟРȲΠĠĚԩǎĘԄȏʓŹ͵ˣ\x86ϪԆҍɵȈğŞƆМӦҔЫŽʭ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˊɨVƶďŰПΓɷȣAԦҿdԪB?ƈӧΟƲŖϺ˲Μд~őӮȹ',
                                                    },
                                    },
                            {
                                        'name': 'õǁѲӞɚHçĝĢ\x8bʉÚέuAò˪ĀƸΩ\x9fϔǥҟїʆƫɍ¼ɸ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ӽԍΑГ\x8f7ȊʧѿñľδѮәđӽЛƶ\x8cŃǃ+ƋѯͶԇϊ¯ӲΎ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӾǻWȆϜ%ԧʬιǘμɞͻзˑľ\x9eΪz¥ȎǍ˨ʟDǻңʷǤ8',
                                                                            'ӨĨʈƚÄǶɒƺæѹϨ¨Ċİ˻цɗҗҫƿȽʼЪЬô˷ē\u0378Ơҏ',
                                                                            '˜ȔȺǯŠΐöϩҴEɐӸǉљɻŨƘԁ\x90їƤʹɪҩěѸɥĶ˸\x9b',
                                                                            'бïȵͽԫοτ΅ҧӃпǞҔӁƩȖȳɈќҝԬąзȇɍ҂DҫJ}',
                                                                            'ƠiVnƁПϢ5г`мɘҜǊӬÂѧͿŶ:ǲŇӂŜѹ\x80șУǊӯ',
                                                                            'ɑȽ˔ǿȯԤԬȹȆ\x80ƨ˯ϝӞǻŕђһɪ\x98źĭŐΐģɞˆ˽ɬξ',
                                                                            'Вɮ¼Ȅ½ʰӱƟüīȞήĬƫүªǖʶӹжĺǄ˪ðȧB˳ûϷȮ',
                                                                            'ͽɘϴĪΕdwàȞʇŝĿѺÚρ¾α9ԋʫӿяpӢ˫ƨĻҏЂû',
                                                                            '¯Ĕ˭ԣΖȠuʄϘǳǒΌϞ\u0380ŔÇă¢fƫˬνįɵĽδɧčʀԏ',
                                                                            'ɃŊÐ˪ЧƚɑˆΡЩ˟Ȧžc½ɋʥǛ˶ŭԫǠƹȺʙǛҝǩŐЯ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԨǙƫɆ˾СзКʯ\x83Ԏ~â˻ɡѬŽқʥžƮ¶ЭԢöƈůƠɬԈ',
                    'message': 'ԖэȡƿıĦ\x93ϦʟϣŐԭӎıοŁĴʆеʰұ˽ĮùŇŋÚȠԚĿ',
                    'arguments': [
                            {
                                        'name': '>ӡǑɛѬϕɥү<дɓ¿Žõ˙ÚωȾ\xa0ˍˇϙʦʵȉ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173331.037015:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǔϤрÝČԆȀ*Њ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ԋ˕ɅʦΧɲÕǷϧƐǾ\x9dѼήΙǍҫƝśԥȈØϰƃˠͱŝŞҙÔ',
                                                    },
                                    },
                            {
                                        'name': 'ʗҭŖǔùï˨',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2509627346604235,
                                                                            9049650003991444569,
                                                                            -4267637044101980790,
                                                                            1537384282240029841,
                                                                            5810817881703699303,
                                                                            4224392742488417540,
                                                                            5283719880004908579,
                                                                            2233632904351637961,
                                                                            -9000607286442216546,
                                                                            5052376741859325645,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȅѼΣKÙĜӡĉūȵȍ\x84ĝψ[ҪǍѕçдɓˏȭ\x9fѿϪįɌԌƊ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            926356.036570154,
                                                                            199468.66394771793,
                                                                            18021.753985754694,
                                                                            44123.7232309579,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƋӀԑˉ˰Ԟƀ\u0379ǴӢŵTŲчýšϙĚʾ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ǨȲϮ˸ƱʡȁςǢԂϩgόɬʝΐčӏСԂЍ4ͽËѩɎϴɺĵɷ',
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
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ʀ\x82ӗϡǻȵƼԮˉĐãʟĩӯοʄΰ³ŘϿψʿӣƮʵĉL7Ԡ΅',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
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
                                        'name': '®ǳѽ¤Ҝχ\x98ÍЗΤŢwʵqŌȜȚҼȪȦԘXЍd\x8d϶UʎāǢ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            8597.517826990981,
                                                                            661051.9545172616,
                                                                            364578.89802551985,
                                                                            419451.91487154254,
                                                                            312710.89904635854,
                                                                            -56081.835653554655,
                                                                            434813.6408913849,
                                                                            825068.8196567246,
                                                                            506176.6892294568,
                                                                            689845.9504704305,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʏƐѵ\u0378ҭϹѬЁ¿ʢǲќɢǃԙÌԅêϠĔ϶ˎԘ˱ǰѕƯǰǴɐ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -9116861181785129113,
                                                    },
                                    },
                            {
                                        'name': 'џӰƱüʻƱļӜĪ\u0380ѐʌŵˬʴËwZĽɪ\x90ȪŞԞ0ԮſʪÕɀ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2114113386393853061,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʩћˍƮɚ¨_ʬӅʭ\x84ԏѮȴтіϞуȁψNϦηƏĕʵ˺ѴΜј',
                    'message': 'ДƆέʎċƝҐͻPΕǕӲFϑδԔȢÆ}Ѿȇ\x92lİǂƚҭYµ˼',
                    'arguments': [
                            {
                                        'name': 'ɢǔĝȞńΌԩ¿Ŀ4ƁƄÇuѯџŉQϖϦҠCȺĘĭ\x84ǢӘģ.',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            162421.5149187814,
                                                                            493516.9594540101,
                                                                            533312.7093726591,
                                                                            132519.11584480648,
                                                                            679354.2826472676,
                                                                            785092.7886332145,
                                                                            316843.91122946737,
                                                                            181947.68431977346,
                                                                            243197.66018067597,
                                                                            32010.09001502354,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ДɡæӔТ}СȾӑі¢ʫNZҐ3ŀĚ\u0378\x96ӮȦ',
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
                                        'name': 'ƾǊƘ\x83ÊƄσͷŗ˩ƙºԝÞþȑOŖǚɹ{ДԨˋŶҮ˱ɺǒϒ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŊǦӻśѰуПΤ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173332.185896:+0000',
                                                                            '20220522:173332.195211:+0000',
                                                                            '20220522:173332.203340:+0000',
                                                                            '20220522:173332.212743:+0000',
                                                                            '20220522:173332.221767:+0000',
                                                                            '20220522:173332.231021:+0000',
                                                                            '20220522:173332.240085:+0000',
                                                                            '20220522:173332.248384:+0000',
                                                                            '20220522:173332.257050:+0000',
                                                                            '20220522:173332.266026:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǎ˚ʡˊʒҎΔɖǑҍŎѬȻȊȍĉѕČөĮ˟ʛԉӎ\x9bўʋѴĦ|',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƶʍԌιѮѴƏлЋȵ\u03a2εέδΤĎơœćlʋɓѳƐēğaɍLǩ',
                                                                            'ÙǬ\u038dӋӔʚÔĽ²˝ʊ\x91цΐǯѧωԡ\x99ĸǭÐ¥ɮăӯҧɆΫȩ',
                                                                            'ȏ΅Ы\x9eoȋüоѺǴ\x8bёʟŬцԗ¬ХӪ¦\x90ɥĉзƈDˠ\x80Áƻ',
                                                                            'ӺΘϓŬƊʣϻ?\x84ӂҎʯɜlûXǈСЙxʓƤӼǳƎǖĥβҞһ',
                                                                            '˓\x92ͻ$ȄĹрƳДґІѮЋȡʥϦ΄ŁǕÙѥϋĸĈ>p\u0383ůʺр',
                                                                            'ƣ\x89ƁǠӗҊӮÕҤ˟ȁHǶԝӕ\x81˱ĸȣ5ŮŴЮˇɰӴȁɹgơ',
                                                                            'Ȕˇǝ_ʖСŕăʬЪ<ŐҷϵжЦЗöχРѓόãőϦ¦ЃɅǦ˱',
                                                                            '˽¿ӯ\x9aϽϠѤȮ2˼ʹǩǻĨʥǄīπԒǞяβEȞӃдǮѪğØ',
                                                                            'ΛӂфтԄӊ+Ԏԥ\x8dŁrľαυʱfέʚ\x97XĞ¸ŻšҳüƼɑʛ',
                                                                            'ʭ\x8cƂɰ\u0382ÚĭɰΝǳʎƊʻ\x87īӅɈĂŵʟɻ˖ԠȋȳȴЇʅÞо',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƅʀԓ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173332.432687:+0000',
                                                                            '20220522:173332.441260:+0000',
                                                                            '20220522:173332.450506:+0000',
                                                                            '20220522:173332.459521:+0000',
                                                                            '20220522:173332.468348:+0000',
                                                                            '20220522:173332.477477:+0000',
                                                                            '20220522:173332.486435:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '%˼ƕƋɆȒФʴ˃ȬƘ˨ƩӴŨ˸ӊōÓɎԅˏɤqҦ]Ωʁàˍ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            185335.49335679773,
                                                                            445361.8410041294,
                                                                            -52158.03847358182,
                                                                            969027.0080270581,
                                                                            445975.7410746382,
                                                                            86939.74395806281,
                                                                            400317.76577195793,
                                                                            874701.9688676966,
                                                                            846938.2555225713,
                                                                            39672.40804858037,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӖŎ҉үŇº9¿Ӈ\u038dÅɰȆƊĴӢɰKȽʯɾ;είŢ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ģ\x85ɨ»˴č˟ɻˑΡŇû,ǰѹʲӝ®цi\x9dӥʫϱѾəƵйŘӷ',
                                                    },
                                    },
                            {
                                        'name': 'ˍ҇ûɿß˸nψӸ°œ#\x83\x83ӦȗƜΦµŊͰłÉȨΣħϩʶ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɇΌɑł\x88˔мҚÎӜƔ\x9cϭԐ·ğˇΌ£Ͱ˘ɢӰ΄ʿҟԪŋд\\',
                                                    },
                                    },
                            {
                                        'name': 'ġ\x9aÑɢȒėцȔӧѵřԭϲ҂ͼԮƃπԝƁөϗýɭƟ¯ҵć\x86ř',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҒЪsԝ˒ΒԊ˚γЙƞϫˬńʻ~ǛɐʥƇŴђԁ2ÊƸŖDVο',
                    'message': 'ēЍČԗˈMű«ͼ˓ų ЈөĤŢԂɶńҗŦƾТӫƟ˼тԡɡ?',
                    'arguments': [
                            {
                                        'name': 'ѪɼƵ\x8aɼӎԨѱХµʵӒæԩǰ\x8dҩȚҲȏεǾԒUħȊ҂ʁü˛',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -81978978035880759,
                                                    },
                                    },
                            {
                                        'name': "ƭҦˇ'ŠѳĮЩĹĄŅʋƣmίɏǽ\xa0ξÖϊ\x8eQƧĎļԕйșʀ",
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
                                        'name': 'ùӷįҾŢ\x9b',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1845596956293988888,
                                                                            6670414354732009543,
                                                                            5766782837715348205,
                                                                            -3968636515322718858,
                                                                            8138074762399520813,
                                                                            -2497952497669557976,
                                                                            -3534198561315504429,
                                                                            -7124693931489282535,
                                                                            8367419165187324780,
                                                                            8312588433549235714,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ъȉ҉˓ѣƝ»|źеðЂP0OЧҗįȗԉѵτȟÌбƈɿɢΗ\x92',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\u0378ƴЭÝΥϕǮɇ2оɘԘ"ȆΎȞӣѣɲīҞцԌȠ7ľЌɸ\x88ʗ',
                                                    },
                                    },
                            {
                                        'name': 'ьƪ¾ЏőϪ"ԑҁųϭрǘΝӊƺSɡНîѧҌʳęХɨɰƧІſ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɪȰ\x8dňÙ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7111725846845050847,
                                                                            -3814618710297740478,
                                                                            -8881301064337696574,
                                                                            -5764895041380683137,
                                                                            -3070714706136674937,
                                                                            7260639107641283342,
                                                                            -4289864877694851399,
                                                                            -952922667607606754,
                                                                            -8359792529543695411,
                                                                            -6349641561451639883,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΝǭţĉƎɨȍĊαǦӟЯҿƽˍ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            520684.6022215729,
                                                                            543371.4638153083,
                                                                            44840.173600512004,
                                                                            547028.9965443682,
                                                                            491166.8356621731,
                                                                            898533.7572797907,
                                                                            987969.8348081566,
                                                                            397224.83355481474,
                                                                            428810.05670697475,
                                                                            658945.3833350921,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¢Ѩ˦ёŌǿçΧȋŁ\x93ИλԨȗįȨéΑlþЭǅ˅ǣѽϽӊĢ¶',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173333.400295:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x8eѥ`ɢơ΅Ɩýυź˰ĲϦʰњϔ˥ǻ\x9fυʘǤӰ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'еȜҋҽӯNØєвǩǅƙϒЧЧǓʋБȽ]ӄΞń˄Ў¶ϲΧʋΝ',
                                                    },
                                    },
                            {
                                        'name': 'Ǔϼ˾˰ˣǞFяъ¦ЄǬӐоǎȍǳΝϻ˫',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4400722172540230319,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x96ſϯ\u0381ƟĚUŬϖķ¼ӻÙԑ|wѽӎĕÇ҄Š˒ǹҧѵ\u03a2Ђԁ\x97',
                    'message': '\x95˅ɞӨΞЮ]ȃв!͵ϳĒɳԤ\x9dѨƎ\u038b˗Ә҅æɩΚмhԕӽҟ',
                    'arguments': [
                            {
                                        'name': '\x9fӍЩÄ/Ƒ¼˪ɮʃàǿӯΒƋјL',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ŷÅĆψiɝ5ΫҭԬрαû˒ŶʰȵвԍƲˮǫϞăϿʦÔ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173333.580213:+0000',
                                                                            '20220522:173333.589038:+0000',
                                                                            '20220522:173333.597905:+0000',
                                                                            '20220522:173333.607069:+0000',
                                                                            '20220522:173333.616307:+0000',
                                                                            '20220522:173333.624864:+0000',
                                                                            '20220522:173333.634185:+0000',
                                                                            '20220522:173333.643193:+0000',
                                                                            '20220522:173333.651895:+0000',
                                                                            '20220522:173333.660913:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ιɱҠš',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1538700179599486831,
                                                                            8599433156855585775,
                                                                            -3228733521534716835,
                                                                            -7123741127173269989,
                                                                            3580919349398610377,
                                                                            -2588836375903464945,
                                                                            7783356530157935127,
                                                                            5176448636148182910,
                                                                            4072394090068241888,
                                                                            -7617268109592305164,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǍįіQÑȌԓϒȵėѡŢȚ\x95˱ãíӟѿӈθΆҳY°ɳ\x8eΜƊŋ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҟκӳŋҫĞǻϔʙњ`]ӅˈͿѶɦŖǍ¿·Ò˚ÑĠТƺǼÉȴ',
                                                                            'ʔưʮ)ŏ΄ŰξыѲжĕʵÓ҄λʬҐӵҦ>ȠԓƗʵɊӌɎǺѨ',
                                                                            'ԤθƘ\x8c΄фπͽͱÃԜƜěӳʨɪȸŒҜ\x84˭ŻϢӪʑѸѕі\u03a2\u0379',
                                                                            'ȐҨ"ʏԨ˩ɜҚǈǢȿҒĻ\x92įӇǿӆ\x84ȓˈ¬ʉѬϺˁήпʌƚ',
                                                                            'ðƮʲȍʰľαӌ\x96CƙʰӌѷчԍõӕŦʙұǳÚԫƗϐĬеH\u038d',
                                                                            '˯Єƪ²ĄϝûψĕӿďҌԮӴӳʔһ˄ȼǽ΅;҆·щĜÅыųҠ',
                                                                            '˸ɯ#ћƜÃy¼ġҎ|ІαҟΪʙπ\u0378ʹҐԞʋĊ±Ј£˄ē²΄',
                                                                            'ƅηɵЧɦԔʲʊӅņѸƠАҜԌƅДǈȃ¡ʋнΑӥ\x90Ґ\x81\x82Ƴˋ',
                                                                            'ʜԡ˚Ɏ$\u0378ȷèҁȀ\x9f.ɰцđʝUƌ҃ʳƲѻʩʉάŜһΑz®',
                                                                            'ѵԜӔŦċʚʏӧ˯ʗμӷҪΞădоʝϺ˭ŝȞ\x8aǙ҈țƉ҃îɘ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʝȌɱ3ӵӦɐ\x96Ĳ}Яр³ԭ ϴ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '\x8dĠƥ.ȫ\x99ȈɆґѩȫƏӣɤШůΜ(ѩӷxƎ\xa0ԏ˵OęɅϪƑ',
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
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΗŅŘƥȠǒcΨ¼öӋҭȞϮФԍАЃǱυ˗ƏưOȟҤ\x9eСťt',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7780222144607519869,
                                                    },
                                    },
                            {
                                        'name': 'ɄʏȬԘѴȍLŋƊԁĄćƒѧƪßǝҮǣӾѮEӿƖϜś˶қĈб',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʥ˱¬ǴѫÜÕĕΗʸ´Ӈų΄\u0379$ƙƛϣ˧ņӼӣɈϽŬƌşϥʖ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ĮӸɊϺ+ԏ\x7fȱ9ʅȃʛͶШ!˵ɳȹȢИҶϊɇĕºƲğ¡҉ǻ',
                    'message': 'șӌͻԕсäŇɋѲȴģ˰ƞϸŬŕϠŭʚЩͱƆԬŨĵһӸьёǧ',
                    'arguments': [
                            {
                                        'name': "ɔӷŤӨ'ϨҮӻ",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ԐӁхҠȯԖɀԚΩɶԢ;ȭĤĔҺưȟėҪȈyɑ1ěеÚӛɖѭ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173334.256394:+0000',
                                                                            '20220522:173334.265387:+0000',
                                                                            '20220522:173334.273607:+0000',
                                                                            '20220522:173334.282851:+0000',
                                                                            '20220522:173334.291704:+0000',
                                                                            '20220522:173334.300466:+0000',
                                                                            '20220522:173334.308567:+0000',
                                                                            '20220522:173334.318049:+0000',
                                                                            '20220522:173334.326668:+0000',
                                                                            '20220522:173334.335064:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÎʩӥҪϴßș',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1504344288146320154,
                                                                            -1552095002414901416,
                                                                            -846903812963061216,
                                                                            -4664440871470165155,
                                                                            -3802520639050590617,
                                                                            1392818740934406064,
                                                                            6463855249567966470,
                                                                            2508715683612437676,
                                                                            -1772510639820072929,
                                                                            5705761008740581015,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Μơ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ĶˆИΤÂԟ\x7fȕνŃú\x97ɍ҄~ǤʄŐΡϖФ˂ɠʻǤśϮӖ˓Ҏ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173334.536748:+0000',
                                                                            '20220522:173334.545590:+0000',
                                                                            '20220522:173334.553998:+0000',
                                                                            '20220522:173334.562888:+0000',
                                                                            '20220522:173334.571219:+0000',
                                                                            '20220522:173334.580331:+0000',
                                                                            '20220522:173334.589508:+0000',
                                                                            '20220522:173334.598908:+0000',
                                                                            '20220522:173334.608166:+0000',
                                                                            '20220522:173334.617433:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9cԋԚ˃ͺӜǴʥΔϮ$ƅHǬѹїɲ˩˽țʂɖӻӼŜКǜ˙Ɏҥ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            218151.83437519794,
                                                                            327349.64166924695,
                                                                            590004.724705695,
                                                                            933343.9366435757,
                                                                            67476.56940635858,
                                                                            186176.99494711438,
                                                                            50961.027634505095,
                                                                            137404.83525156954,
                                                                            730761.8696775016,
                                                                            521688.73667746456,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǰHӒϼɃєɨ\u0382ʬʳяbɤÙĢҫʖˣԜƉÁѕÙ\x8eg%ԚѐџɎ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
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
                            {
                                        'name': 'ŽѶœƊ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 982558.416615251,
                                                    },
                                    },
                            {
                                        'name': 'ԒUüǚǾԐӴɇȓŉýϿÃ?ɪϒǷƤγ"ĜοČӾȖlϸ˟ʅǕ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:173334.943573:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʆɚ\x9bĪΥ\x9fį˹˖ċƛǶ\x91ƈωϔΣԓщǞŉÉʺɥм<ĭ\x95ôy',
                    'message': 'ɱɶãЕǲųėƲšǽˠĿϧÌыĤʂјαƮ˩Дϸǿ˫oǥϕɅÝ',
                    'arguments': [
                            {
                                        'name': 'Ü˰јʛˈ˺cώц/хѡΠ<Ԛ˳\x92Ȏ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӘҾҫ¬ХɚˑKūԢĬ˰ɥÑȤуƽñԏŸùƂƳɀ×ϑϹúư\u0381',
                                                    },
                                    },
                            {
                                        'name': '\u0381ĜԎƏ\x8b¨ѦČъТҕѠӕԜ\x84ƽ˲\x9dԟhóŭʶΈϡǴϴ\u03a2˜÷',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7669244521144020916,
                                                                            -1089115166407568758,
                                                                            -6009795943950127682,
                                                                            -8927040114391733274,
                                                                            -1170682666527769903,
                                                                            -8963849272576579323,
                                                                            2509458020233803887,
                                                                            -5217341315673209016,
                                                                            -7620518317129173685,
                                                                            6183896228062151425,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ІәȣǊšԂǺžˬʰӭĥĭέǻƤчȏeˍѢŭIѸDԇϽɉҰƠ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĄÁĄЯî˨Ӯť\xa0Λ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŖЉӳѻѡҋМ+ñ\x90ñāοϣƈвӅŻѕͶÝȉBçԦɩɍƏŚӮ',
                                                                            'İʖ΄ɗ˽\x95ϥXӡŊņҽŀƮαиѫ3˺ҁΕĚEƵɟξGWѸρ',
                                                                            'ʴωӺψȜшԉϝɂӂĕδӧʽŢҏе˕ƥǮȾǺȇȋXτђěĨń',
                                                                            'ǿ+×ƭÇɆâüɭƺǅΊǙҢWeӑ\x89øɁҶ˵ԠмǗȆwŻ˥ǔ',
                                                                            'ӓĀρΑÂĦԑʦπƒʹɼτԫ˘ӈɱÓÓƳǨ9±mȉ`Г϶ЩҶ',
                                                                            'ΜǧǢӱģ҈ԩп˟,ŏ\x87ҿĊōк£чĬ²#Ӣ˸ƽ"˨ԕńÃʖ',
                                                                            '\u0382ͺΟɽɐɯdƴϰ˂ЇӈɡϬγ½ȓѼɊƏǽǮ-Ѯ¿Е¼ǾΧӐ',
                                                                            'ĺŦѹ\x9eӠϲģųňаʻеӕеʕśшϯʊҋƴЧҏ\x90Ҽӄ\u0380ԮĚɎ',
                                                                            'ςūŪӵƋǦ#Nǿpʺɬ9Ů\x81ͷƙ¿\u0383ɰƶãĄʚԞәʂ˞ʲÐ',
                                                                            'ȁɳąЂэͶԩ˭"ǝͳˑϜȘ\x87ҖȊҾѦәԤБȻſ,ĬÝԆϨɳ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '»ԗ\x9bԊƝ˻ϮҵςƴǭΑͼƾΓӻŏíыєүȉʨų¡ϏŽʡǆz',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4685007663108880479,
                                                                            8120657949584835211,
                                                                            4621397239293908450,
                                                                            8549642163297024381,
                                                                            3681188144937228327,
                                                                            1503409388200346835,
                                                                            6742888380942871014,
                                                                            -1242038980909788625,
                                                                            -5108815049511858900,
                                                                            7002662730728202651,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x7fԜȉѴ·þӿËѳʁŖǣӛĆмϤdѶ0î5ԈѹʄʀΩȇӠǷˆ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -40343.65615141945,
                                                    },
                                    },
                            {
                                        'name': 'ζƏƭ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:173335.497770:+0000',
                                                                            '20220522:173335.506624:+0000',
                                                                            '20220522:173335.515400:+0000',
                                                                            '20220522:173335.524493:+0000',
                                                                            '20220522:173335.533009:+0000',
                                                                            '20220522:173335.541538:+0000',
                                                                            '20220522:173335.550605:+0000',
                                                                            '20220522:173335.559026:+0000',
                                                                            '20220522:173335.566909:+0000',
                                                                            '20220522:173335.577182:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÆɩÉʇëǒЫԔȌ˗ȑƚӹUфǐϼȣ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3445842768375682555,
                                                                            -2534873733961835486,
                                                                            -7130241907437081876,
                                                                            -9030411671450943030,
                                                                            -8477330102207808179,
                                                                            2651120577562672603,
                                                                            4511142542523477076,
                                                                            -7472441563747707795,
                                                                            -8246844584354012906,
                                                                            6310547812713432062,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŻƝɁǼҷ\x89ɗșѻЁŶǒì˛ӥЃƵҀ˳TƽÖ[εňͷ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '<Зӽς\u0383ъɧѫɱǢɊpþЀƐeÒɇғԚȣ;ӱґЈυεȤԢϾ',
                                                    },
                                    },
                            {
                                        'name': 'ʀ·ĵёȾʳӰ',
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

            'identifier': 'Ňϸӥӣģ',

            'categories': [
                'access-restriction',
            ],

            'messages': [
                {
                    'catalog': 'wЖ',
                    'message': 'Ů',
                },
            ],

        },
    ),
]


class LoadExtensionFailedEventTest(unittest.TestCase):
    """
    Tests for LoadExtensionFailedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOAD_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionFailedEvent.parse_data(test_data)
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
        for test_name, test_data in LOAD_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionFailedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOAD_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LoadExtensionFailedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='LoadExtensionFailedEvent'),
            ),

        ),
    ),

]


LOAD_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ʯӘͳРЛǻƐɹÊʡŻǧнҜʏӉ\x8bϨɝ4АªĦǏ˼)ƨĲʃǱ',
            'error': {
                'identifier': 'ȡȩыǿԀǚĖӰЫƧцХ\x88Χ¯ϝɍæјͱŽҐ˙ҽθħŗή¯ǥ',
                'categories': [
                    'internal',
                    'access-restriction',
                    'os',
                    'os',
                    'file',
                    'invalid-user-action',
                    'internal',
                    'configuration',
                    'configuration',
                    'configuration',
                ],
                'source': 'ÛɈlԫσԀ҆ЁҐҀРˤιĨͲЈ0ɊÜάϟóʘ˃ĀˈȿХŉ˝',
                'messages': [
                    {
                            'catalog': '˻ŒȜʒӰāϜ]\x94Ʉҋ*цң\x95Ͼ˦΄ʆӳ!ŐȸƗ\u0381ɵʂӝΕƩ',
                            'message': 'ΊѸʄвĒҌ§Ɉɮăǥԭ8fӅ˹ͻūVгҨӠȉӂJˍǈʟ×һ',
                            'arguments': [
                                        {
                                                        'name': 'ʥԂ\x8aßȢϚǉʶƋÊӕϫԏəҗȩhÀɖι¨ǝΥƵғӳǺĩŚʷ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'щζƿѷɉβÞіƉćҚϽѢʬӒСɌȶƍūʺƋʇгʵX˔Ąΐ\u03a2',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'œƑ(ѮͻLΦӓ,´Ҳ҇űRΘҦƹµғȒԋȃԁЧ˸',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Α',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 308400.2322907472,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɦ\x9aŠņԜΎѴØDĨÔDѡūԒӁΔFȚĴэɼʛ]ɺԥȗΝ˙Ķ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȠȨɨ˩ÿėÚдΊʌ\x7f',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȫɓ·ϿːɈ϶ǧϪɱˠȘЊĎӢ˵˸\x98ҵШϫϷԃӌҀʅԨȉƈӮ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'tŢЭҬÜЀ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173325.196549:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĊҼŚ¤AVŉϗѱГ\x9d¹ѩ~ĴҾԈлԣʫȹЬӔқϪʆϊãҔЏ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6326047304048385021,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɵІҨΡȝЭǩ\\ƭрȨщǠжӤ¿ɧԫ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԥɲˡǌĆþϭвүȔćӋОӝĞԅ˚åԙмӨɼ¢Ėªԣ˵ȁлƇ',
                            'message': 'ĢώɸҫúőŌŮЃƣǥ¢9ԤXЩ҆ȁЅӟҒ5hĊШӚ\x95ɛϼк',
                            'arguments': [
                                        {
                                                        'name': 'ѦʋȭsϞұȚѼ҃Ƹ¾Ӌ\x9bԤǯс˽ŚŅŊ\xa0JɺʈɔЖѸeÒˎ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -94.1784423806821,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʦxҎˇø˘ѣ\u03a2рϲԐȇ\u0380Яƈ˸˒ÝТW¡cэ˼ƺͺÄΜӡ˓',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʢɞͰ!lϓÜǟɷƻǙwΠњρӋϏ[ͼԕɯǦ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'í«ƆӅ5ɠх\x87ѷƵΩЂρǶ<ˁØԫá<ǹқƤҽʡN',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǏǍƝČī',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӗǐά\x8b;Ȝè˦ҥǂѦǛɀɮȟȑφǪΨԈǲɁÀΨϒŠӎκŸѭ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 146694.60606332964,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƿčӝ\x98ŪϊͿήǴВǶÍԍ¿ӱӹļΕ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -26324.110209842125,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɆȆмǅτӊUȏ϶ɘΒɷɉ˱gԌΑ΅ûĨӼԫɫҐыщʺŅӃʦ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ğȟ~3ВąШʬÄħŴhӡ\x94ˏ)ȯgЭ\x80$˪ьԓͻ҄İjǛβ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƵƈxƇʤȖvѝёёÍƂǕćŬĒ˃ƗϿҐƕʷŤӼǒӗЏ\x92ǰҋ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 599649.1076040205,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԛґ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȹѕ˰дҩáΎmŁɑϻăƽǭӁǿʈȱƦďҚȲǊ',
                            'message': 'ȴʎʳԗŧ6¢ČЖçҀ˩ԥ÷в®ïŽʜČΈ\x8f%ˉķǚɱÀƂʘ',
                            'arguments': [
                                        {
                                                        'name': 'ʮͳһͰWįĖ8ʛ8ëңӛʅqÃ\x93ɟԬúĺɞͶǯöБbȖKΥ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173325.572295:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': "pŐɓԙѶԈ΄sjҤ[Ҹ'Ӽӥžřɞęŉд¥ǑĢ˸ҴåΩu",
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173325.606943:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŜЫ³Ȍʲ\x9fϾƬéǧ΄ˇ2ύ˸ВӘΎśҲʁͰҚƎCЋΐӖоԭ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѓˡǿÀȏãŷӶ4ÇnҘűλ"ʙӸƋQȥˮaƆ҆ôԩōɏ_',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'øıìϖηϛϾ\x85Ь\x8esάԄҧȱθԘ\x98ϗąuʐ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2416678199145506379,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɋPņʷҨ΄έϵȢļăšӐʩ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8aϓйĽʠΡȞҸѿɻčË',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǢԐǐԗɫӋ%',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӈј˦ƘŃԆн˰ψå\x99Аȝ\x9dñǣƎȄʺҽͻіэʲġKЬV',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÕłÚǙǯΧvʟƥıІȨϗǵƤҪĺ¶',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǡĒϟʝɪέхʥê+ӧǄTƜșŦ˥ɟΌRȭʏȥǇǺ"мϺʂʀ',
                            'message': 'ƾӏ\x9eĝűàǃǪͿ˂śҭϝԠąҬɢǣʄΐĢÈÕҀȯԄԨąā\x8a',
                            'arguments': [
                                        {
                                                        'name': 'ʼσʁӚʺӚҸʷȝʁϠ´ͱÐɉƢ\x9eЃq\u0379èRЪӑїƷϒәϻϙ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɿ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӜМ\x88ӗÀÙD,ћħҘˡțȁɎĸ\x94ȱӀŞ˽ушєĠðԛΙГ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173326.034263:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϧϨӄԩϛǞӑıħƠĲõ\\ρΗӜɀӻǺɤҹѝзŇƾӕ\x9aҁϔʟ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЉҍȩӚʅŘªэ\x9b\u0379ȱŐšʴЩǠůǨЗοӀɪŹ\x85ԢĴгхԗ³',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͺӘ҈Íύʝơŏɋ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĘǵȀ˓ГÂŕԃΤșбË\x84¤ԃѳÑйFƌпĻ˥ɪбƴUÌЊÎ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϽǥҒěчĉԒļΠҌ\x92ʨʗČˏ˻ҷĖƊҤЉ˛NȋȰʣħЧƧʤ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 846707.6971611783,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʭ¶˩ДǙTȯ΄',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4635038874355619766,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȷʗLҊxʳԚѹӳǯӺˬàÌ`βӒтϑȗԭÈ®Ʃ1ǻÂʛ˜Ħ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƴ˳ԑ˼TřΓȷ˃ӘɬʐI\x87˧\x99ǗǌʒѺϙoȬ\u03828чҺƋ˗Ǭ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 34010.12754325106,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '9ŻìыœǷԎԤӝ6ŜƺΣɰч\x8e%Ӗq˲ͷŉŜɽ˞ʣ',
                            'message': 'ÞЌƆǩĶіĽҹăѿΟϩRűφɚɈȤ˅ßÌZɉҞƆѫνһ˧ʭ',
                            'arguments': [
                                        {
                                                        'name': 'ʙhĭѪ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӷă҄ʰ҂ζ˵N\u038bμŋϖɸϺ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˳˒Ų˭ӡǣpÆӜůɑǯԖŦƙӗĢѦˢтdңүg¡Ņηĉәϗ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǽǅʈ\x8dɾȑƮӜžҤΗŚǨӟcӌίήз`\x82ϊЗӴЌÎ\x80ƐɌӀ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3733183043750991927,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϭӷ˲§Ʒ¤ғÞ\x8eβǿǄѕl~ź¬þ˟Ė\x8aˊъϪňƽdЯěǳ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѨПѦʚф˦Ӣęǚљɞğ®ʻłѩƗūFƪȾћӅѥšȬǿμˮʂ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'çÜǚƵΦōӤƀԟȂƏJŲǸ?ĒͳˋбӂȷϞ]ƊƓÖ"ξ)Ǿ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ђǰžҸƚǽΓƝСʘЊ´Ǔ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Š;ʙηӦˑΜʅȴˌgãҍǭӡǝɾƈʻээĹӽˬЄѢˤҊԏ~',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 130754.49939154941,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҽˍȓñǒΥ˂ˠ"\x8bдčԈ!\x8bƚųÁȔ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϷͿΫщʪûāͼѼΜщ˛ѝϾƐ4Ź',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϤļƒɁó\xa0Їw˳Ιɡǩʮ0ҕҳϣӨəmʄѶɔɐũ)ѻћˑӫ',
                            'message': 'ȓ)òϞĮӧУϐĮτС½ҭΣƠƲ&њÕхĶɉǦʗѫԈӦùƉú',
                            'arguments': [
                                        {
                                                        'name': 'ąØπѤ¢ҵ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˺',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '9©ÃŀӺĶƠ\x81ʄˍΜԮʽЦ˒ΩʀēΌЫĩͲϩĢƮŐʂјșԣ',
                                                                        },
                                                    },
                                        {
                                                        'name': '*',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'чҤФΧȄɾĖţʶý¯Ԡ˃йp˶Ϣžĸ˭Δс˷ӝϭϿҐ˯ƀǿ',
                                                                        },
                                                    },
                                        {
                                                        'name': '\\ԣ˃ƬȡιŕПќǺӴVıӼϤўȍχư\x81˱ǣЕѶǻžǨˆԩʗ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'υΧҀѯ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӧˎ"2ćԈѧƮ\x954υɯҲȮ͵®Ǥ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҦȍӅˮǕȒϜǂʯőȰėtΩԛȆӀƝ҈ŘɁʪӕͳɇԕ˗ɖˈƮ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ďЮ˖ŒÐȧήġϓȣL\x88Ъ\x86х©ÐɭκɔüOаϿƻԜjдĵǺ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȆáϿëЙϤˠǦɝċΧʝ˭ЇΞ\x9cɓѭʶœȀʲyȀɁ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'DțƝлȈęǆԭїϢMŦʎҬԐјЪǑǎЀϵǄ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȅũǌ˘ÀрǣàлȆɈŎͿìȭȬƞԉӴԫȣЬϨʛʰɤŸѨϘÃ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'өѽȉҖƕȃːȆԊfўԜԘԆуªԭ·ӇǂΚґȡоҙŞƸ^ùÖ',
                            'message': 'ĻӶÃУxƗʇǍȣšüşԕƉ˄uǴыɤӇʅǢźƐʑ˜ƺķӒώ',
                            'arguments': [
                                        {
                                                        'name': 'ȠǿȂԉ˵ʾҵӁΨΨƁ\x97ʛжϲ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǡȜąɿėmǽкԁį˥Ã²ȩɂČʊν',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:173327.011994:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'öі',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '°ÑąƹҩƏˑǢûϰȝОɃĶĸȺёʳԒǘɐ®\x80ͰϐÄġμŦʨ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Зʠ˯ԞċӍѳм4Ζ˥bϗ\u0381ȷІ˳ʊʾɪħΏѴЁädƤ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϓҎɻжӉƃ\x95ԏkѻҵǑ\x8aɧĶȨŖԄҤїɻӆТͰ˕FԠ˻ʎӠ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǁȇʄҘœӜŰŧ\x90ӶƳөЃ\x8eƼȐмҏøźΩłѭǤӔ8vԄ҆ǂ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'İÒ˰ΠѨ0ɥÎɫʹĺӯϽǟʕѦЄ?ҴѳɜXȷĢөɧԏԂʧԜ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˑѫȵʔ«',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ζK҂7ҫҍźϲԟ^ԧŅωŬϕƵОȰɃǼĹƈèǀ\x96ɫʦǨŇɟ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǯεɃŸӧѼŠ6\x94ѧʬǠӘǦȓƤїЂУʬɀĥŃҪÔΩԤ3ɞϭ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ϹӤUϳ҉\x9bγĨϨԡ$=ч´ɹрʛђRϪȞϘБǧɤӫƙД'Ƕ",
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĭϾɓГǂαԘіƒԗˁ\x8fȱЋȋʺΟåΔŃȄįĳ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ėȃԧѾѤκȿĶхüκƛϝǈЃǄ¼ÄɟϢĘҐ©ӾѺІŮхř˞',
                            'message': 'ũƸȺźǘΊʒɹӦx¤ϓсǲĩŀčѫǓԅ\x82δɊ@ËǶΌϯʣȣ',
                            'arguments': [
                                        {
                                                        'name': 'Ǔ\x87ϩȑĿ7ø§ŗŇɗȃӏ\x9fҘƋңěДӶƷcũĶʹʣӀė',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȜʠĖӹÅҶϼϱЈˢ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1737289584935972069,
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

            'name': 'öвԧ',

            'error': {
                'identifier': 'љ\x95ɀӦŐ',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': '˲ȏ',
                            'message': 'ъ',
                        },
                ],
            },

        },
    ),
]


class LoadExtensionSuccessEventTest(unittest.TestCase):
    """
    Tests for LoadExtensionSuccessEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOAD_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionSuccessEvent.parse_data(test_data)
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
        for test_name, test_data in LOAD_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOAD_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LoadExtensionSuccessEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='LoadExtensionSuccessEvent'),
            ),

        ),
    ),

]


LOAD_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ɁҶmuǨ˳ԩϕ˩¤ұŴ',
            'version': [
                -2906398925608166566,
                -4090835251377504581,
                -1410511946140223639,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ƣɽώ',

            'version': [
                -8029488103356180031,
                -4612159150498995411,
                -2371246672776512812,
            ],

        },
    ),
]


class EventListenerTest(unittest.TestCase):
    """
    Tests for EventListener
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EVENT_LISTENER_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.EventListener.parse_data(test_data)
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
        for test_name, test_data in EVENT_LISTENER_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.EventListener.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EVENT_LISTENER_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

]


EVENT_LISTENER_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'event_id': 'ý\u0379qʭЇķԘķӯʆΜәУϪƼυ\x83ƗȕˀЇЭϸЬBӆ\\ûьԍ',
            'target_id': 'ѦɁӬυǠӿɤҵˏŬȩͷʓʋʣ˰ʁǘюƂƾ.ҠϢɼУ҇U\x9dt',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

        },
    ),
]


class RegisterExtensionListenersEventTest(unittest.TestCase):
    """
    Tests for RegisterExtensionListenersEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_EXTENSION_LISTENERS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.RegisterExtensionListenersEvent.parse_data(test_data)
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
        for test_name, test_data in REGISTER_EXTENSION_LISTENERS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.RegisterExtensionListenersEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTER_EXTENSION_LISTENERS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='events', name='RegisterExtensionListenersEvent'),
            ),

        ),
    ),

]


REGISTER_EXTENSION_LISTENERS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'events': [
                {
                    'event_id': 'ĀГӠυȭχˉԠYԉѫңëıʞ6ȷƕ´ȎŀǩΌǗӭ˹\x90ԨȴѮ',
                    'target_id': 'ӛРŵΞͿѱЪНʇǨƼʐзӖȈЌòѮǘɜɚ5Ңҿìż\u0381ӴǢǯ',
                },
                {
                    'event_id': 'ǐˢˆоèĻ\u0379ρƖҊҸČɬϽΞɃǉȹ\x8aёғĝʶЅԬdһƜ˙Ϙ',
                    'target_id': 'Ð΅ξaǫϹέĨˑĎΤeȩɏӕƥȒıҘƍʺ~ϔ\x94ѻĹŽůѬн',
                },
                {
                    'event_id': '˯ňǎȊӏҿĞŏǰȤѤǴΖ\x9eȐѵìĐ˟Ҙ˗Ӻ\x89ɪ9ѯ¥²\x90ќ',
                    'target_id': 'Ԣƪ÷rʂѾ˲Ϛ;лòÉǾϙǦųËƄЕŋ˩ҍҥΝəǩǕËϕʐ',
                },
                {
                    'event_id': 'Ɖǆӑĕο.ķԑĠKŃĩУBҍГԅҘɃʛ\x9cĆүҩĚƢϱԉ\x9aΡ',
                    'target_id': ';\x96NÐЅz˔ԈŪȖт\x9cҵǋãé˦ÐðrſȾΫҼҍͶʑǻ\x8dŤ',
                },
                {
                    'event_id': 'ЏӠӔϮϭΞ2ԍǤШĮѢƏǙӟӡӞΦǳƾǞӄÅƮƴӶȳ)ɰѪ',
                    'target_id': 'ĪχÝŠŰÛӿ.VƅĪÐJԊҘƽSӏĆìѵʻuğΖьіʾϫð',
                },
                {
                    'event_id': '˒ӡ˃ΟɿΘԊŎҁĂФϷɄÅɞžûΣƬӁűǬѳ\u0382ʸǲʕŉĂž',
                    'target_id': 'ęɑ¢ʵЊȱζз˵ƛ҆dʦǣƕɘşǧ˘ɐ\u038dNKŝjōȞɒҭŧ',
                },
                {
                    'event_id': 'Æ˝Ʒjλđ9˼ĕș͵Ɩƕ;҅˻ʉҷʪtӇͷĶȁŀŀƃь³Ƽ',
                    'target_id': 'ęϑŅʦɋr\'0ο˄ȧűԖ-ÐϦğ"ԭ҉ːѧĄǬ\x98Ɩɺѩфѽ',
                },
                {
                    'event_id': "QƓԭƷĚҵƏêAȡ´ԢɅļӋЎȖӶο'҄΅ʀȋÏВǲǔЫŧ",
                    'target_id': 'ђӪǽǰțƉðλǂҽΠǿȑϡΡҨȫϳȩ\xadȟϴ˸QΏ½ʽĐÂ˫',
                },
                {
                    'event_id': '¸8ӛ:ТƸ΄ҥǪʽҪǞŽΙîӢKȊɵЀЋ£ĩӝά\x8fˠ\x81Ůȴ',
                    'target_id': 'ЬƇ\x8c¶ƯŜǩҰԠѸгɝĔɂɥњñұ_˚ϺÞљȾ\x9aåң\u0380ϷӾ',
                },
                {
                    'event_id': '\x85\x82ķԦҫϮɋȓӭӓrĖZͽȉҢęΟЩNüɑmúНƠdĆʳΩ',
                    'target_id': 'ʹ˓ϩϻҮɤ˽сÜ`ĴϬȱ(ŸǨЬЮǎɓгҢťKɊĺϣǿˌȭ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'events': [
                {
                },
            ],

        },
    ),
]


class RemoveExtensionListenersEventTest(unittest.TestCase):
    """
    Tests for RemoveExtensionListenersEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REMOVE_EXTENSION_LISTENERS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.RemoveExtensionListenersEvent.parse_data(test_data)
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
        for test_name, test_data in REMOVE_EXTENSION_LISTENERS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.RemoveExtensionListenersEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REMOVE_EXTENSION_LISTENERS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='events', name='RemoveExtensionListenersEvent'),
            ),

        ),
    ),

]


REMOVE_EXTENSION_LISTENERS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'events': [
                {
                    'event_id': '¹˹ǧŐɖåǊӣӍŜӡ҇³ɮҎҤ`ԁǗǠҨȗʟŦҙӿғàɊ˝',
                    'target_id': 'ёѢƖ˴ҁƳȼ',
                },
                {
                    'event_id': 'Ưǩ\x81ϜŴȧƊnʰƼ¥ҚʧǆƂԄÎȘŮеӝʨȬʟyΉóʂɄơ',
                    'target_id': 'оԏ]\x95ŎȢӔΎŌ˓ǫѨǌҪɿӹǪбŚůкӘŁρВɋԪЩԜ_',
                },
                {
                    'event_id': 'ӗǄɑçΣΐǈӱū|ϕĭÁȻϹʈѓĖøƕÍʮjɆĥǎƝ·Ʌӿ',
                    'target_id': 'řŇɐ\x8bυ\xa0\x98йҍԆȳ\x7fǠєƹϏΣϔʍĻÊйԆȩўԤðńΧȆ',
                },
                {
                    'event_id': 'ȴдʂȤʓ\x9dĘŲϞºɖ©\x96Κɻ£ɥԥǜɏēɝɯœѼϬηϦͶʦ',
                    'target_id': 'ӍˤŽ\x8cĴǵƸ˰Ȇӓ$ΠӃΏˁԆɀƟŨΑRΥŇ%Ҧ\u0381ɈɎƒĚ',
                },
                {
                    'event_id': 'ЩюˢĲȈѩȿϮā_ϖËɿςɛϞˀ»ѕъӨȄҴɆʆЈïƊɔǎ',
                    'target_id': 'Ƿάˋ҇ŵÑ˵\x83ƞҭѬƩʵΚӣêğƩ&҈ϑөɱϤР\x8fxыѤт',
                },
                {
                    'event_id': '\x86ɈˁīλȫλԓҷхȉӖń9ӬԡЎ-СÀӢǳӳ\x97ƿǷӾϺЩG',
                    'target_id': '\u0380ѐéʝ£ю˛ɉʻàůâԮБԇυΡɕː ȫ˧ʳҩɶƒiXϡ¦',
                },
                {
                    'event_id': 'ˇÂΝʬΏŴёȮΡѢäɴѐҖĖŘʹͿԜʈǐƑџõƈȦ\x93ҌɟĤ',
                    'target_id': 'ԋƁŉȌШѝ\x8fǇjÛº\x91ǤȱȚΙҥЮА´Ӝ\\Ӑˁ\x7fþƗԤ]ƍ',
                },
                {
                    'event_id': 'ɜyӏǼųŕƽˍəȄȽ\u0383Ξ©MǵɢƳȆҖɜшŜǟ_ƲɃÔʿ«',
                    'target_id': 'ȾʮӡĝБԌɦªǪΊϽʲłˬ\x94ʝѫŪeĔƝş\x88a7ªԛϭȍҞ',
                },
                {
                    'event_id': 'ɽÙʵҊɞµŁ[ѱκʷƞźufΠѳϘSƂϘƗϧǎċ\x83ĘǢӿÒ',
                    'target_id': 'Ǽ\x8dѱ\x8cоČӽԍɀ¬δкԠȟϼȩƌͷ˧ˊ˽ά\x98ʻ\u038dХɟłұԧ',
                },
                {
                    'event_id': '¬ӊҭÖƏǑȴȬŔѓUȁǨr\x9fәɩͷўˠЧɀϽ¤ȎƂ\u0381\xa0ǈǺ',
                    'target_id': 'ƎǏhǐŶμĒ˹ȉІϾƯʚ\x99ЩҢћçŵʨı˔jȖ\x91ѯΗЉɅˋ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'events': [
                {
                },
            ],

        },
    ),
]


class SystemStartedEventTest(unittest.TestCase):
    """
    Tests for SystemStartedEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in SYSTEM_STARTED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.SystemStartedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SYSTEM_STARTED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]
