# GENERATED CODE - DO NOT MODIFY

"""
Tests for the extension_loader module.
Extension petronia.core.api.extension_loader, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

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
            'name': ')ľǴʽ\x97ƥǊŵļsӫ˷ǸюŨЂķ¢϶ǝǳʉɛ)ҎΠΞGK˃',
            'minimum_version': [
                -3824645102732195448,
                -2758596639482741297,
                -3353728230347486828,
            ],
            'below_version': [
                -3898043623857439653,
                -8588841044262305233,
                -754233073305289657,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ť\u0380ӫ',

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
            '$': 'ʌʁΔ϶ĴƖԎӠũɒFƆƺɇӦ¦ǐȄZū°ʝ΅ƦΕ\u0381:ʷėƥ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 8691515149740032547,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 576842.6100903815,
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
            '$': '20210327:034742.749865:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                "Ȏӫ˟ɤ\x8bӃи'ѱÖ¦ƵÈį\x9a˻цcϿƔ°ʄ^ȢòŶű<½ȧ",
                'ӚӮц/ԟ\x97ʡξĈӵӶω˚ʒӳ\x9c˲ŁȦÑȆѾȾƦǬźŘǚ3ԥ',
                'ȷÁ!γѯ÷Ҥ)ņĜˀǱєҝҶҺȬМ¥ҨƦIyưЎʓbǿԕɏ',
                '˭¡ϯԛǓŇņʸβѦ×˳šφɏ®тγΝɇԀĥѾ\x8eԟHНҷɇͲ',
                '\x99ԍƱЙ҉϶źʸ\u038dɄÑίјϨϙЌÈ¿ƄɅĲԨ˜Ȱɞ£Ņěјĕ',
                'ƽјqќ\x7fˮ˄ϕƟǝƝņĲśȬȌАƭͰԄӍHԅǬǇў˸ƌҴ҉',
                'ȖҒŹ´ӆνȐԗţʿǷĮȦԂĠâДȟ҆ǼѨҁĜuÅζԜҦćǭ',
                'ȸÚéFjϼȑїӺ>æΏҨшԊŦǺӍҿÐ\x8eЊÁҖͻԫ҂ǏɣΗ',
                'ұѣÃŮiƳǶӣЯ%Ѿŋɝʿǯҩþɀɡ\x84_ԖƵŎŕ¶ɠʁʎύ',
                'wɔσɄӟÇÔɧʗņϰʀӛɼɛ\x88ԌɗԅŔƜEƤǙʝԟǙǹҋÓ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                8616115310780819550,
                2469653334337530702,
                2266492859818308805,
                -4764025496442051897,
                -6742551557082675842,
                5070712924543663423,
                -1156531472701630106,
                1869837869189317838,
                1971002159957559027,
                8154539821446223495,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                873222.6844796143,
                368367.5277080208,
                -44419.91391857716,
                811837.2748940904,
                381550.0417864984,
                17644.514509001237,
                369381.70258771785,
                286569.8448324965,
                640570.5136045552,
                834905.6624730751,
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
                True,
                False,
                False,
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
                '20210327:034743.736969:+0000',
                '20210327:034743.754769:+0000',
                '20210327:034743.772287:+0000',
                '20210327:034743.789657:+0000',
                '20210327:034743.807232:+0000',
                '20210327:034743.823628:+0000',
                '20210327:034743.840948:+0000',
                '20210327:034743.858755:+0000',
                '20210327:034743.876901:+0000',
                '20210327:034743.893548:+0000',
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
            'name': 'ʠЯ½õYС4Ƌ\u0382ˢЗ˖ϹĄȈ˸ЌnρΚЭЪӅǟԠĺȴÏŃĳ',
            'value': {
                '^': 'string',
                '$': 'ѳρˣеƍӫ§Э˟βŧɻāѲˉ˷ɲʇµHƒǂҟԅŎйǰ·Ƨν',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ɭ',

            'value': {
                '^': 'float_list',
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
            'catalog': '\x98ΥŤǘ\x85Łʖδǃ˱ξϦRXΥˆ"˟ȫӠʔћɔӍxĻ\x82ԪÎǨ',
            'message': 'Ļ"ѝèƨΆўę҆ϟϖ\x83īψ˞ʂ|ԍςиǭʤ˔˂ĪԁaǏȎΦ',
            'arguments': [
                {
                    'name': 'HʒnşӌҔʆƄðäЙΉқ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ńϋ͵ԁϮʁϲʱҢǸˉϖˠŃɳɢԤҝĎԡϮŖȝӉǩλԛxʄ\x98',
                                        'ǰ·ηÕ˨ѐпөӴϵÈσΓȡ±ѻɔνɴĎԜҁӀ9ѱѐ»ϻэb',
                                        'ʚ˺ӏϷhŷȼˇ>¤ñʏΕӤЀЁǡȬ_ȯ҇Σ!OԙџϵľNĬ',
                                        'ǼđѲƧƸǟҋήΙ\x80ɻЂ!0žĞŶЩВѯɬś\x9eЫҲɷ¶Ԓ;l',
                                        '|ӕËιАăƕ\x93ӗŉĄĮIƒϔƾʂȔŏφѠԐʑԜɄƐÛщԠʍ',
                                        'Ê\x83\u0382ĆϚɿŉΑԧ¢ГӜāŽƛϿ\\ɦɨǹƋǳƙǻŶ˭vĕ}Ҹ',
                                        'ѓǝӒɮƧü˦ǯ+эɅԠƢҌSȟӥ҇\u038d¨҄хȡӤÊµwőÀƣ',
                                        'ɡʱӁʾɪ˰ψüƈɻǼ±αѠӵõ\u0380ŬˠʺѯЍǃҿϏʧыĿӏƌ',
                                        'вaёӖŰ͵îʿUϨĈʉǎѣӫŏќxԮɀҧџ\x92ƙŪĆ˯ЫѨķ',
                                        '˯ȈCϑΩɀĚԫƟȥď°èÌȔYʏĽЇЍņg\u038bʱѾѝѨȧΉ·',
                                    ],
                        },
                },
                {
                    'name': 'ſѩϞƁɡʴǘ˗ǢƱҒМξĘŧƃ˸ΥǯľƗХĳϮŎȦдɤӸӎ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210327:034741.371985:+0000',
                                        '20210327:034741.392576:+0000',
                                        '20210327:034741.413942:+0000',
                                        '20210327:034741.435065:+0000',
                                        '20210327:034741.454772:+0000',
                                        '20210327:034741.474025:+0000',
                                        '20210327:034741.495029:+0000',
                                        '20210327:034741.515945:+0000',
                                        '20210327:034741.535979:+0000',
                                        '20210327:034741.557470:+0000',
                                    ],
                        },
                },
                {
                    'name': 'Ӄéԡ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'qƂԫϴѠĻҌĀЁ¾͵ʋӗҾˤʇɕHʹу9Ǘ\x98ǦҭåӓӖϥũ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210327:034741.722375:+0000',
                        },
                },
                {
                    'name': 'ӒtΈοШқAӲőҕÅː&ǈџˡҳӆƒк\xadӘʧѲʹΤŐϔδű',
                    'value': {
                            '^': 'float',
                            '$': 481831.0630021411,
                        },
                },
                {
                    'name': 'Į\u03a2ǭаȃȖžƟϼîȞʢĆӏo˩ȔϭȺƷD\x9f',
                    'value': {
                            '^': 'string',
                            '$': 'ѸЬцΌСįȼΔҤȰÁӓu\x9aɣŦcêˬÆïϛ)*Ϫɛfй\u0380Ә',
                        },
                },
                {
                    'name': 'ȡĭԨ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ǃŷÍșґȮҒˊϻˬЮˌnКȀԔ҆%ҦɥĠЯƶ&ŵӸĻ\x9aӦй',
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
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ɷnПșҧǾг\x9f*ϰ\u03a2ςŽɝӔ\x87Ҫïĺɕ˪ɹɭ˚ԒɖŐ¶rǈ',
                    'value': {
                            '^': 'int',
                            '$': 4135883861922484082,
                        },
                },
                {
                    'name': 'wκ\x9bжҶƢH\x8aԐƌ',
                    'value': {
                            '^': 'float',
                            '$': 915630.0751304616,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ƚp',

            'message': 'ƻ',

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
            'identifier': 'ђģøȪĖҟΙҳʣҝÃ(ʉλîǵŏŚǲрx²ȅƙŅӢЭΧԗв',
            'categories': [
                'file',
                'network',
                'invalid-user-action',
                'file',
                'access-restriction',
                'file',
                'internal',
                'configuration',
                'os',
                'network',
            ],
            'source': 'ȸyӗFϊӝ\x90ɝŨҦʇˋŋфϱκ\x8cØKӴνɠřӽ\xa0´˚ӟɑΥ',
            'messages': [
                {
                    'catalog': 'ӑѻʢӗ"ΛԆ',
                    'message': 'υӀťҫŨэѰØ{źʇĤŽɌ\x83*ͼϡӶ˥ˁ2ȨɫļʈɥʷӤ˘',
                    'arguments': [
                            {
                                        'name': 'ǲЇӽùɗϖώɻσјġƺӻҴÊ\u0382ɋΓÿ\x86˔ΔĠ:доΎƓ#Ͽ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034725.535200:+0000',
                                                    },
                                    },
                            {
                                        'name': 'EÍҿΗΞӽФʉȦ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 262744.0498226749,
                                                    },
                                    },
                            {
                                        'name': 'ϭγʾΚǢěԟ¾ÌÆƋȫԉɈƍ\x86ԩ˻ӫԕːřǦƳМ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4182300237893021600,
                                                    },
                                    },
                            {
                                        'name': 'ЕҜɱđʯ˻ԈʬԞ1цE˅WϷғȮµŐǚưѻ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȗǦύ˼ɻ©ӞвϣϓӏMˋĂǙʡ²ƆԎ\x92іƾ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            545202.7800483764,
                                                                            162517.8116765599,
                                                                            907155.8258203396,
                                                                            361781.3298653604,
                                                                            123842.09619943998,
                                                                            -56767.78153046301,
                                                                            53687.785866472346,
                                                                            894076.8794564395,
                                                                            891303.3713988805,
                                                                            -84277.49330664499,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԮɖȢƽÀǞȜ`ӜІĒégſΕǏҏʷÅԬҀźєФԚ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƌƀʳǊřƄVςϸә´wɤ6ȂʋǴōǴDˀ˨ϸć\u038bÞЕϰŁ˻',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7860131662229494632,
                                                                            -2140297984583175871,
                                                                            8253622259592456198,
                                                                            -9110794404043422201,
                                                                            70911283738447832,
                                                                            2048446187218056437,
                                                                            -6453201321562556764,
                                                                            -2261465234269209063,
                                                                            -300412599723981525,
                                                                            -4117059829061650606,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϳPǉpu\xadˈɍȪ\x94җŅ˭ș\x94εƊӦɡʅɗаˡԝϒšȤӴʠʔ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6571674933870293286,
                                                    },
                                    },
                            {
                                        'name': 'ю˹ѥ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            218696.05897427688,
                                                                            756084.0536438117,
                                                                            942028.3559176076,
                                                                            739540.946303014,
                                                                            133766.4108343916,
                                                                            510272.2593094269,
                                                                            355484.21650891996,
                                                                            471995.539553031,
                                                                            281549.6164132162,
                                                                            520584.06927999295,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'сƾƢɽϞŹʻЏѥłZҸñʧˡϯʨӺLˎʃ)ѶϴмÌȦʘҶʝ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
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
                        ],
                },
                {
                    'catalog': 'ͷ˔¦ФȳϪʀљ=Ʊ²ҲӸȴѹƨХɉҷһȧ\u038bӎȾʛωѯÄÌ˱',
                    'message': 'ƊƞŐӒĝɦӤYVϡǒ˶ǝђӀȅϜńǯ҆ѧɷ³c"ԧʶЫЯ:',
                    'arguments': [
                            {
                                        'name': 'ЙǞΗϿŪ˓ǮĮϴŭԑÁƷ˜ҙ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҙ˒Ҧ҆Ƅ˰!ǂçʪÊԑǏҩѠ˹ӉWҢΎΗ÷ËÂvŤɨǍǐţ',
                                                                            '¯ԧΥĩҎέʞЗјЍσ\x89ΩʾΝϔ\x93ӋȉȶlвϨѰѻϩѽčȺȊ',
                                                                            'ӶËŵğbȎȎ¯åҷCѱЗmɻѠǗҳӆӀțҨӆȪ\x92ǭƭԏʧӝ',
                                                                            '¬ɈƄĻϸ\xadЅ2цſԞG\x9bҾĦӘΗӠѲŎ$ðӱǸѹȉ\xadƉӛГ',
                                                                            'Yòjįɶ\x81ˍϠôʎˏůčΧ\x97ѢȧυѮԐ\x93ȌƒΨKlƩçɦȬ',
                                                                            'vϭŵΫʍȘȳCʰИƣӲξǨүѶɻɽǙѤ¤Ɠǥɒ"ЃÏ˞όґ',
                                                                            'kɲûǐȟ\x8aɐԤTВǠˣί0ɁŜȔŦө˼ēöʤé\\ϛ\u038bʚǩʆ',
                                                                            'ͼлвљѸ҂Ɋêǖȃƚϊ˦Ǧü^ΡĂЂ΅ĨˉQѳ?Ͷɐϔ҃Ċ',
                                                                            'ԋǝȆ&ӚҬˡ˅\x81˽ɗэƄγͻԝӏ\x99Ĭǘҩ¬ϹÅɒϑÜǱȮϖ',
                                                                            'ɖȭnҗ\x99ʤўƥǕёU1ǻɤþ¬Ϛȹåʞћ\u0382ӒǚşǆǓǘȒƳ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'tνĻƀԛϝȸКŵȈǝŊȟл<ɹӋɗѷΨKÑӵϏǧĴЭ˨ЎÓ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5356077652985973351,
                                                                            -4821849782578131695,
                                                                            -6373712186609950366,
                                                                            7243429907371888381,
                                                                            -4032196263508368623,
                                                                            5483156924993546493,
                                                                            -965380558459816132,
                                                                            -1098677428117463103,
                                                                            5509533074469061811,
                                                                            8710734058488092300,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8dΪȻϚѓόÕʣǎɰ҃ҏãƽƀˬÏǎƀʠľʣ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĘҶҷūѢϤȹŎ\x8f',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3644442125731637896,
                                                                            2209927147394272510,
                                                                            5419862021326592081,
                                                                            -7644438833334999279,
                                                                            -884105705930048827,
                                                                            -3812443558701989732,
                                                                            2062149178695172533,
                                                                            -8269356291381756145,
                                                                            3555482549605140290,
                                                                            3166129692507040354,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˏǅŭ˲ġȒſщŚ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034728.143404:+0000',
                                                                            '20210327:034728.160315:+0000',
                                                                            '20210327:034728.178063:+0000',
                                                                            '20210327:034728.195171:+0000',
                                                                            '20210327:034728.212570:+0000',
                                                                            '20210327:034728.229554:+0000',
                                                                            '20210327:034728.246277:+0000',
                                                                            '20210327:034728.263508:+0000',
                                                                            '20210327:034728.281369:+0000',
                                                                            '20210327:034728.300529:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ːôŽƟM¾ґBѤІôөӮӑΣ§чЈϓ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 312715.4344235483,
                                                    },
                                    },
                            {
                                        'name': '˜Ϻ2˔ԋɉǪǘЀŉԧƌ˶Ɨ6\x83ȍɏȡϣҺŀǴȞıʷф;æQ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǃԙҨϐǦҜ\x8aͼԡ~ҼΌÌˁѹΫĘɔɿ\x82\u0380ˍίѹͰ˦ҩŉŒƦ',
                                                    },
                                    },
                            {
                                        'name': 'ŗ҆ԬӥӴȋѷhӃΥӳҚ˚ұǺê',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7896984999414933153,
                                                    },
                                    },
                            {
                                        'name': '\x97ʞЃŝºȞϭȀϠǬһ©ŋ˞ǖĦʠʋΔǺҟ˴ͶнƇ˶ˀʂƘ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӘЌǈćԓҍȁâůˋWжÞϣ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'мʙ¨˫țȞĠĚ҅˕ϣõ˅ЏÈΩҕџʞʸ˸ȂɷȆpәʑ\x97áǬ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Tʧèӛʚžý.Ӱώ³ΖЂͲŚɂбɯɿɚіφè\x89ңžɼ}ҟԣ',
                    'message': 'ÌȦȀȁɞΎϿ)^ȵǏu\u0382ĿӊόƏµϲЇƾΗ˼˲˵ϽԫfYŖ',
                    'arguments': [
                            {
                                        'name': 'ӞƠӄ³÷ԊƟbȵһˏѓÀʙΈƀƹĊ;҆ԆˇʯҡҌѿЍƴ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9074350438884817831,
                                                    },
                                    },
                            {
                                        'name': 'ʾӯ8źǼʔ\u0379+',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 163350.78726732504,
                                                    },
                                    },
                            {
                                        'name': '{ɏя&ǻ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ҥƺʙζw˕ƥÞˮ˹ЊBÎҾƿʾβѼ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8235051844470782845,
                                                                            8851098236826777354,
                                                                            7594658005724491810,
                                                                            -3689569748424694451,
                                                                            1251260018264197906,
                                                                            -2123388624078418742,
                                                                            4052538965874726222,
                                                                            6891855481762296384,
                                                                            2482114106550814906,
                                                                            -3467143042605410280,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ОоЌӻǀΐ~ҒɰɥΉӿŨȖ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԫɺƂνӤԭ˞ӇĐϰѹʌԟυɨӘΘˏÖȕʠ&ҵѨԥɬӣҪͿͶ',
                                                                            'АӢËƹƹt\x88çȥ҉҂Ԧҝ˲ǪӻƞӐīɔɲвʟЙ\u0380ɾұϳчβ',
                                                                            'ԆSʠɎʏԑɚÝġʍTӄżYϙһġƒƙȘѮKΐɴœЈϗϼόϛ',
                                                                            '+DүùыSӱ6ΟЛƟ˯ǠѓüoϤʮΉǩ®ӞÊÆâȓʠөǼΖ',
                                                                            'Һԭ§ßΙϛ˃ЃцɾԖԫ¨ңȻƝЮÖҝұƪĞˁlΠ҂ϩԉВΚ',
                                                                            'ЌӮͿʈӆƜЭĒóӬ\u0382&ϨŲƒҍŊßȷȵ,ɿɄpĳϹӒμύO',
                                                                            '!ԒɈϡˁâƦ»уϔΧ£yӄˮɲӁDư>ǗѕˌƴˤǇʊӛϝѫ',
                                                                            'ЎƝҍ\u0378ҕʁe˓ЀIҀ\x9cϪӛǏФɟӡȂϺӺǪ¡ºҋŞɡ°ηŹ',
                                                                            'Ȯ˥?ύιʩȰʈƁѝǎ7ˊŉEº\x8cǉſǭÏ³ǒ\x98пǩǚӈɮŝ',
                                                                            'Бν\x98ƥΕс±ůĩåƩąԙςȱҷǓҿѻŋŞЅmɚѯлȖкҮѩ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƭҾх\x9fӈĊөŨΜɀəȦ¬ʕŷȥÉķĲʩ˪çǉ\x82sΉԏӰҔɵ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            371437469493325036,
                                                                            -4393132214629012429,
                                                                            -7870846420551152430,
                                                                            6576698283243605244,
                                                                            6693253375079922590,
                                                                            -7370926838655584881,
                                                                            -8761079062357322016,
                                                                            1058684470782155933,
                                                                            -3373308358637981358,
                                                                            6275347484645480036,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͽѩƜͽźŧÒ1јĆȼǅǪNuâгϛЊί\x95ˮĿȥήˈěȱŇƥ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ğәΐϝӺFѓκˬȄϨιрѱЀѶ\x9a\x8bƑ\x91Ôөȡҋǯԉe˨˺ĉ',
                                                    },
                                    },
                            {
                                        'name': 'ʂ(ԪѳȻÆåӯǤԩОԞʹőeйâ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԗϬζȬӾʭ»ˏӀŔӁ\x81ĜӭżɋʜТǧƎͳ',
                                                                            'њτʽͻӱθӵ}ȇˋӿʜˏ\x8f\x86Ӄ#żБȑӫŨ\u03a2éςʵÂπύʄ',
                                                                            'ȶŞ¹\x83юĥêӜғïĬȋǰ˼ʇȡŞFŨʁяʂǢнʀȃԙ"ΥÝ',
                                                                            'rΪÄϩǭěsϠҗДƂ-Γ^ϧӱĠƺƨȹƒYǜζʦɍԡѮӲԙ',
                                                                            'Ǌ½Ǉô±|ź^ΧźϯӐ\x82īωԗ\x96Ѣ®șпԛЕ\u038bϚ˓ÇĄÝ%',
                                                                            '˔Өĝǲǥʧԡǀ˽ԙK˻ϙѠҭѹǠǌʁȉɧÌήąëğYˈʴŵ',
                                                                            'ǗȮ\x96Ɠƴёū\x82P҅ĠǳQӵҝ˞ІĶЌϙӢȾ}YʄѦӫ\x94Ѿ\x97',
                                                                            'ΎҤɹș1ˢϞǛǴɲ˛ēиŨƿƐʰȹжæԙȏǣƲçԤÜˢԋG',
                                                                            'ƱхˤǢȟȫͽŘЍˍǺØ҈ʏИЕǀǱÍϧӝ˴ȅɾχҽьɸěʝ',
                                                                            'ƺǏόǻΛԀčÕðFАɮʄιķϼљҰKƔσƬgɦɯ˱ƃȮӿΝ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԀҁĠȦƺɐӣýŒƃΆǇы',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ªƘòhԝΑƜϤӳɚ˱.ɸǯ3wƩӧþècũÌʁ«»kϟʓƞ',
                                                                            'ˎԭʄÝɧϯƿÕѢЉŮɋцêîȢϷɟӲòѥ¦[ɶҴɜǗǲ\x8dć',
                                                                            'ĩѝŻԋĽŕˊʝ˜ƶĆĲÝɶƨɶƿåǢȰЙΩǙÔ\u0378Ė\x96áȋɦ',
                                                                            'їvɰƜԢѻ\x91ˀөϐҩǩõΖҡ¦âϦ\x8dҮӨӣQŉĴӇЕ\xadƁô',
                                                                            'əҷƎƿҔòӴ±ȟʚzϪɸӅˍăɖѧιĠKӂԄ˨ҦˢҖĆӀˢ',
                                                                            'ǳΖÙȗϫʨćЮј\u038d\x91ѼòɄϒ4Óҳoʥ#қâŀыԠ˖Ȳȼɥ',
                                                                            'ʺӐτFԛhǄ҈˭Ȏ˂»ʺГǅ҂τłɐìӠǈЏʙăЖʠΣSѵ',
                                                                            'ҌǲӐɶЩɊǗʫɃӨ©łƯξʏϺβԒӬіϠʐϹǱ7ʇҿǭáӓ',
                                                                            'Ń^Ѻϑǎ$ξǰťŌʱΟŏԙŗάЯҝΊӚǥӛшϠԒčBИŶԓ',
                                                                            "ԗ¬њʳËȾҎŌơʎĵЀǇʽˢȻ˟Ϛ\u0379жͺтіUԑɱ'ʰηѩ",
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'эšӷȃÓŖѲFѿ\x8aĎϙѱцɶБ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034730.426825:+0000',
                                                                            '20210327:034730.446574:+0000',
                                                                            '20210327:034730.466780:+0000',
                                                                            '20210327:034730.486695:+0000',
                                                                            '20210327:034730.506887:+0000',
                                                                            '20210327:034730.527372:+0000',
                                                                            '20210327:034730.547856:+0000',
                                                                            '20210327:034730.569532:+0000',
                                                                            '20210327:034730.586251:+0000',
                                                                            '20210327:034730.603629:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ͷԍ\x83ƌԠʝƔœłϯ\u0381аӪȤɾϖǟ0Ԏ',
                    'message': 'ʐӏǟѝφ~мwЅȃŒˁ¨ǍȓЯӒʛϊā0Ӓ˹ʈüОӢҠȎW',
                    'arguments': [
                            {
                                        'name': 'fҘɷӰƪԬĵԔԉƿҪĘ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˛Ȭ\u0383ӨηӅsƥЩĜƃюũǽʩɷѵũлƚțÕųɯʶñɃ\x9cǃì',
                                                    },
                                    },
                            {
                                        'name': 'Ԩҧ˪҉ҥӮʔȉȾΒԗͱZɤŹĳҖÒҩčηőӟ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3711019954895876527,
                                                                            -2729937601507465163,
                                                                            2197983491242956003,
                                                                            -2658319104083848892,
                                                                            -3831394132328585607,
                                                                            431432402849004757,
                                                                            -3201146306609029120,
                                                                            634701431533875892,
                                                                            -4225539023106428574,
                                                                            -7890220576329180291,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΜӿщʄӗɌƊԋι˱ȱ¤ʓɜБїˎˏ˒҇ϛS&ќӿŃ͵еͱэ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034731.072444:+0000',
                                                    },
                                    },
                            {
                                        'name': '\u0378Щ΄ŶƓſЖpʹԎȟė˼ѝƺʴЯѓc¢ĭЊʸНȂÁ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 383967.8339962454,
                                                    },
                                    },
                            {
                                        'name': 'ӍЫ&ɯԦÍΠҬ҈ɯǼǔŰ\xadɸӇ˞ɟϞŗȵĸӕȠӰҺ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԢǑȗӷǼÆɄʌ\x7fïϕØЬɀ˙ϥѷRȔδϿϣҾǜŎǸŶčUȳ',
                                                                            'ƫŇҩńλɐԏиѠ!ңɤ˫ԁǇȁǦйѸѪ\xa0ɣ\u0382ƸϜϤ\u03a2ȬʆТ',
                                                                            'ǼǔĄǊŘĝґ.Ĺˋ!ûʍгЀNe·ɵŞ˅øҐ\x83ҾΥԅƌϪș',
                                                                            'í¯ƱԃԏőȏԢҒHʖϥӿDʚƗ$ͱPŤĭʹţΌĥǙêŗƿв',
                                                                            'ДγȾ˰ƽŕԍӡ\u0380˭ƟӍʜʜȽčmϣɿԂɔƚȕðԪӮʧџ¸\x82',
                                                                            'ƽȨÔǷҗbƒ\x9dú|^ȟȫ´ΥȤǿЌ\u038dюě¼ϏζҸ·Ϊ0ɢ±',
                                                                            'Ɓïüʰ¶\x8cȈƐȴɏͲɁαƲ\xa0ϭƦө΄ÓӛąГǒ\x9b2\x8bԢѳԇ',
                                                                            '\u0380ʴ´ȏʻр\u0383ӄǢǸˌ˱ϲӳ˃ҚӅƈӶԑѨɣľłʼΜǠҚϸƢ',
                                                                            '\x8fϙԟԇƺ˰ȚҹъȌˏͳÎɐȠšȧМɱ˦әԩеǹҦӈГȵŃy',
                                                                            'ȝԋýû×ИӴʧѓϜΊɡ¨ĤƿǣтЁϥѧ\x80,"ǺſɹÿʴȤԓ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȩșÊ ԋʘƊǧ¦р˚Ȼюϻ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ęƧȋǷӒĲ˝/@ϚɘĮӺȺˮЂ˷эԭϩĀΡĲǃӢrϲîщÑ',
                                                                            'úѾϾƳЈӗϽ;ҹӉƴDʆӿЪд˄УԪǔϾы¨˞ӄxŃàĳǉ',
                                                                            'š\x8eÁĂåҫʝ_æʙ˺ΦȏF˯ŐǪļ\x8dɷ\x88ʀɦɃтҟɘǸŰ\x87',
                                                                            'ŏ҆ƫW¹Ҹ±ZˇɏƱˬɘėϦOgð¥҈ʠѡϬΜʶщÅ<М¸',
                                                                            'ʡÖœ\x82ÐԬĒɄΆȬʆƼxИԟťԐїЀӚɚŸŻŸҝHϭ\u03a2ʒΜ',
                                                                            'ΦȘ˯ЏnıҗѿŌЩЭɤұΰʣ°ąǛͶ3ŝγȐГTʠшʝϒń',
                                                                            'ȴδ\x88ТļрӺΏʏкȱθϬɧ´˯ћÔɴ\x87ѫ϶ʦʹňưŀҁҋҏ',
                                                                            'Ȓļ\x81¶ԦýſМďԪōͶλĐˌɰПÝ®ʊ¡ϣɘrȴҷȒǰġώ',
                                                                            'ӷƥЩ\x9dɠȈˏʖǝQԄˢҲӲÛĿ҇/ѪėĠ˭ˇɍ˒ĊȇΜϿţ',
                                                                            '˳ϦĎԪӌ˲υƈʌНǘĤȏšȈрʨӦҺϵĆ˔ˊκdPžϣϟΰ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'È\x96ˀѠȃ˱ñɠèħÛóʹӴВɌԛԉȝȃÊϾџĴγҘʿ\x8bŽȯ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 619266.6232785662,
                                                    },
                                    },
                            {
                                        'name': 'tϛÖǗʧŀƗЖϝӊѡȌҡ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŷÊÁӒɜzНȸ[ҟȂԀŢӭtІΥϐϸtƇǂǇǡ²ȀǭʯǨҖ',
                                                                            'ІӤϘtb\u0379vìǱ˷Ӆ\u0381ԟēƍǢивѴēѕɸӎҠϘȐлåŋҗ',
                                                                            '\x88ʃӊκHĦɎгϾѐѭԗ\x89±ɰŤ7ӈˍ˧źôǜļК«&\x83щñ',
                                                                            'ȜǧćӻϭɧϨūҏόŧΞ˫ӌԤѿ˱è@\x80ÓȷŴ˯ӆчʹѲȵΔ',
                                                                            'ƚԎ\x97Ȫ˯\x93ÂȬʗӮƄʲȤȈηæ¼\x8eЅµ¥õӲuϿТˉɖɑˈ',
                                                                            '˛MɇÌÁɊľå=ʏ¼łŲґ\u0379ˈϺɸКӋС·ȥÉђϋ҉ӹԜӡ',
                                                                            'Uʛ\x9eԉú1\u0383¢ɾȓGΊҥ˰ơҥϢĂԪˢϗ\x9e\x8eҩĄѼιĵ1ȵ',
                                                                            'ҵɐƊŽKШҳǜıƱāɤƾÌ\x85ċԝԇЇªɱέӕWɕŸĥ_Ǯƪ',
                                                                            'љɀъϼ\x89ϖԗđьóљЃƗLУӺˆҞɳөӏŸɛɾĆƜβлoϒ',
                                                                            'êԫƧΘԆĚɊԓӬс\x87ˠҲĠȫӎƬźĤСжϔúȀ\x98˃и˱ʌſ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '΄ѦƭҍҼξӰ\x91Ҡ0ĀВǆƱǡȜĒҫэœƲϪȅȽӇïĆͶщэ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6695179634005279540,
                                                    },
                                    },
                            {
                                        'name': 'ёЍ˼ύ{vӪɜȝ;ƨӊ\x80ɅњĝňӸҬήűŤö҇ǇӧȼƉăȘ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ѡĸғ\x84ˉ¶ӎӧ=\x83ϭƎҴĭűʵΤ\x9fǪωϔͳƐδԠɅӎĦrĚ',
                                                                            'ϸԙϦAǊӗßϬΏ\u0381˳ύƺӘÐdϢ\x8aӄϯǸȓʤŅӮҙҁѥѺƺ',
                                                                            'ŋ\x8dgȐμȉϵҸÿ`²ĈǾ˗ӷλȓќύɠĶJ҂\x83ɲΑʮǯǩĈ',
                                                                            'хͲè\xadѾșԡbϿʹɘЬȻǭʙšԧ˱ƜɸÏΨԉįȘʪɩɓԠʒ',
                                                                            'ȘΓѯʤ˞ȯӯҿЬŲԏô¬ѺɠјҷӇ°ǧÕȣȽĊƕƻϫyɝp',
                                                                            'ѴɮƧӻƟȢҽʏ\x80ʳԋśԁˎѮǼͽӝћJЄɾωɥĳɭΛĺӫθ',
                                                                            'Ăˠʘɛ˟Cџ}ʝĮӤɴ(ŇĚ\xadԖ¸ʧʀʒȪȚſ\u03a2κ˛ɖǙӹ',
                                                                            'ϲΖƒҏʈѥyѕļӏďƐ˦ǵtó˫ΘԪ\u0379ҷбƇāDȧʈ\x97Ŋʫ',
                                                                            'ЍǙ|ӆƐϫƌʪ<ъӻǄή\u03a2ʗ˚ŇʣЮсƶƝǮԈɻԧǢƞͼϱ',
                                                                            'ͼѧзЎŮφΒ@ğь«ӏɕ¨8Ώ\x99җǛʮú˺ĽȪȆҾśҵϩž',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȮŌлʿѕ˜ʇϮпόυ˩чƐήЌhԭͷÃaϩҕ,Ĥɩ+ҷњŖ',
                    'message': 'ЂoƙԬŮŘʝʓÐѼ͵˶ѓȐɹПȣɾrθȕÑʋɥɊ˙ƤËȱҶ',
                    'arguments': [
                            {
                                        'name': 'ҨơϟɲöѯψơɄϗʟѡļБQЂ2Ѐ±ñǘ´ŭĕѩϵǥԇ°\x8b',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034732.532312:+0000',
                                                                            '20210327:034732.548957:+0000',
                                                                            '20210327:034732.562048:+0000',
                                                                            '20210327:034732.574675:+0000',
                                                                            '20210327:034732.587857:+0000',
                                                                            '20210327:034732.600200:+0000',
                                                                            '20210327:034732.612532:+0000',
                                                                            '20210327:034732.629840:+0000',
                                                                            '20210327:034732.642357:+0000',
                                                                            '20210327:034732.654742:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'г\x87ɷömԤçѓЈȐűēԂUƖÊʛʆëϝƀȣӗӓϸӗӼüĔÞ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϬɢԥɮBņͻԞ҄ǞÇҀӒӌÆʞɍɼԘȗԀL',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ь\x8bЦѤŝþϡ\u038b³мƯʋЌϘ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Əŵ\xa0ǜŹͳԗơкùƱӆkÝѧѬƬˬ\x8e)ԄɅɯЪįŐοģǆŃ',
                                                    },
                                    },
                            {
                                        'name': 'ƍ¼LҨҭ˷˧ÍƟѥȋĴȍŚΠǢάǯ˂½ʉѰВßˊͰіƗ×\x99',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 401397.2131127643,
                                                    },
                                    },
                            {
                                        'name': 'ТZΣĥǙÙҕʆǖÕųɴjϝĕȐʠÇΖäǻЪʨ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034733.170394:+0000',
                                                    },
                                    },
                            {
                                        'name': ' Ŏ҅фѯ\x87Đҳӻӝȵγ·ťĚсϭʫɕrǕЛҮƱЕȣʍӫǣn',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȉΔȣŢԇɤѲǌȻďΨɮѶΕԭ¢ЏɭŗʝүBVɉ\x81БҠҢŒ\x96',
                                                    },
                                    },
                            {
                                        'name': 'ѲӉйȺԖǽtŊǂʽѓ¦ÊϊǭĦӾǴé\u0379\x81ԋҚΓ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            383057.1471559162,
                                                                            900322.2705891802,
                                                                            792063.6184658263,
                                                                            506392.06072740234,
                                                                            845819.2508131568,
                                                                            95526.64786867492,
                                                                            719091.0758445174,
                                                                            607006.127640519,
                                                                            145502.53058633793,
                                                                            607425.4590641981,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǒŇѥѝϋԑ°ˡǁʣ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǁƨȰҤóˬь%˽ѿРƋȎį§ɎүҭʔŌў"ҪӫEķŃƆÍϬ',
                                                    },
                                    },
                            {
                                        'name': 'ɺ҈і',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Éɡ˂ϘņƴáӊàǶԓәFνϽƢ\x98щƋϲПĸҽΫƩo"Ȃѯǂ',
                    'message': 'οɧƧԢǕγʮуȚ˲ϒȈҖŠʃǛԘȪφƠßɁӞƿCћӼ£ԣψ',
                    'arguments': [
                            {
                                        'name': 'Δ˙ˁʂƜУӱӼœʜq\u0380M˹ʸԘʆʿԔțʭζԍ\\+ТсǀάÓ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8730943000036749401,
                                                                            1174607674400101821,
                                                                            -3925748011618474437,
                                                                            6769130832784485080,
                                                                            122835347695767073,
                                                                            7331510477362749760,
                                                                            8150142778738511014,
                                                                            9106035299745431011,
                                                                            4801142999626898927,
                                                                            6197592192749964418,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΛϬΈɕņɶҹӄJάНϤϺ/ǶʯπƖΑϰʻɶiчɻ[ΖȏYӓ',
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
                                        'name': 'µˌҺԖ\x9bƃϱФӳ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ФʰϠǇђĸѪʾћ@țvϰϯ^ǟӾͲΧ˹ȴÑ\x95ȎӗӪҬϙʵҁ',
                                                                            'âǇ¿ˏȏÐ®ћɥ¨ɜӥЫͽȲȀƫЫŢ¾ҵƲ\x96ҠЍ3ȪÏǗ¿',
                                                                            '˷þӔ\x866ҹ\x9bȚɼ˻ÃʸÔѱѠѻȔǒdԭҠԮ˥ǥƩʨkĦ҈Ѩ',
                                                                            'Ζӟ1ȂЅӱҶ\x95ϓ·ĊǹʦɆʻɍˬĻˇ\x9aȉəͷŔ¾˘ѕԥɠû',
                                                                            '˒ԭUȋǨƋҖrҡ¾ɏz@ʞЀωɰȩ˟Ɲ¢ėɸȣĜІgΑԬ·',
                                                                            '˴ϐɷMҠeȳС£ʗƯѶĹ\x87϶TˤÃɾαʠҽīĶǦŶ\x91λӪϨ',
                                                                            '\x9béѥɶʽ`Ú҅ƉϵCќә\x8d\xa0˞Ǒ}NϖĹȌљӺИȁň×ʻԅ',
                                                                            'ěɋΏÔϘMҩɸũͱ¢ȿǤŖȽ\u0380ѝѠΉϨȷĂĠӹȾVƋɰЀ҈',
                                                                            'Ŋн\u03a2ȮɥʻеԘʯϣ³ĝЂӼҊʀϵǦ¶Ͽ6\x9bƜĄɝˮƓŞʻԈ',
                                                                            'xϿxϴŨŎԠνǚȷΘťΨ·ΤȃƠџǽηøҴοԎmˆ6ɗĆϾ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ùĤȻ\x8fҌĦтǼśĈǤѻǒь\x9bŷΦāҬ˟ŇʤеѧҸͲœ¿ȯȷ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034734.444342:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÉƧʄȼ*ïүѴԁ˂ʹ\x99δĊ҇ˉѪӶπäҙʾŢί¬ΎyϬӮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034734.524883:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x97¦ŌэiӍԘӫȨɦ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 39897.529598532856,
                                                    },
                                    },
                            {
                                        'name': 'ҏїȪÔӿɮȉŦ:ČфöˍҰɍӕXѰҘM҂ҦȶːȔǃƭǓӸ\x8c',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŋ˅ɜRkĮȬ϶\xad\x8aЂѭU˃ϵƮșӨЮѕΘȊƨɗȖ¬ɾ\x9bЉį',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "Ʉ7˖ɝ˰ϤŸǬƍȕñāɾàĵšӼҸʷʎʡ'˝ʃʖюΧϲņǞ",
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'yÂ˹ÒҪѳȉ˅ƚŚщȁԠ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': ',\x93\xa0˶ɷ#˃ϵԁâ¡ԥŹłԗǒʳ%ǘƼЂЏƅÍҷӠȸǉdΩ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6467925193696430024,
                                                                            4949736948206288880,
                                                                            -9123120292048068974,
                                                                            5054271153325229784,
                                                                            -6363668545910943398,
                                                                            -6131711080997965912,
                                                                            -2795421771145233191,
                                                                            4026436914005915882,
                                                                            433868874122129535,
                                                                            1511030905230976940,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ďӌǢ_қȻHФы\x93\x8b7áԈɎӾɌЙʼκǱӃFϓȍиŸæęǀ',
                    'message': 'łɉãŀũ˄;ëвƔÕ>ьɌȶҩʩӄhґʊʪȒİ7Ŕ҆\x9cĆҎ',
                    'arguments': [
                            {
                                        'name': 'ұҏҥHɬϤʷ¼бӗӾ¯ɸÊéɺȌǶӴ^ѵâӃ@xϗ˛ђƬĳ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'k¥æȝʹƁ·ʹȴmҐӭђƚΜȁȗԆϹҥǄΧМдΤΰʹ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '\x96ˏҪԙ\x8eъӲϐɮǴ\x9fĤňǩiіȢŀҺ˅Ƥо˸ӱȅԘ˂ų½Ũ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 577708471356969387,
                                                    },
                                    },
                            {
                                        'name': 'аяԆDȷƌǭϰƮ5ςϗ΄ρƷӪʾɫʳдįȼίƹʀʮŎҮ҃',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034735.489230:+0000',
                                                    },
                                    },
                            {
                                        'name': '˸ɑΙʺƪԇÍȓƔƵΔȾ¡Ԁ\x9eΐ}Ěɖ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ѯЂӂиb',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˄Θ\x86ѶюÐƥĸӎМò1ƐɉĲ·Ļʮϯӻ҈ӂӆϼǠҗɣΣĖO',
                                                                            'ԜkǱԉªԃ˝ɦƖʻόԘƐІЪŻ1˚ӸԅȧҊƝԓЬ\\ΖΙɮɎ',
                                                                            'žəӺǀЍŌďØIǹ*ĕɞ˓чeяɈӍыŖèŜӤǩMҟƦǰʚ',
                                                                            'ŔҌШáƑϳЅəäԁӼɠӘѝüҫŮЦFǯң\x93ˠќѮ\x89Ãǎ˚ǎ',
                                                                            'Ѹ1τҪИұuȌ϶¥ψYŠʳγăđʅ¥ɌԋҷɬѸC˷Ј¸\x7fȿ',
                                                                            '҈ɏđȝеԕµЄаC¾ԓСή¹ʛä\x96ĖҘǖƍ҈˩ԐŬԈƎɑΥ',
                                                                            'ʣʟÓҎ҇ёHѱӕʃѐʩϠȷZêόˮƛ_ѧƀσɢӤEɜӡǕƼ',
                                                                            '҈ɯ®˟ȊȕίĶǖϏ\x8fǰέӎȱмžӉҽıΧˏŋЇʧǡíҖƨѠ',
                                                                            'ώˇτРԭȐӂȟƋà©˨Ĳşȭǭ\u03a2g¡\x7fǙʸ\u03a2ˇŖĶ\u038dүȊζ',
                                                                            'Ǿʎ\x94ӂDſöԞԃɒЂŒƑ\x88њûvΆŎ\x91\x9eKѹЧȏUĈX¹ǚ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÁQȈʃĉƂϊό3ÉБԊԀԃϝƀȥQĮϫԪɊǲȶȃоhȬɄƧ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7130863507095310589,
                                                                            1483831031064107551,
                                                                            7111257436331604519,
                                                                            5281216363570089270,
                                                                            -3663134970512118221,
                                                                            -322418586008782486,
                                                                            8508238881085060635,
                                                                            -4179972667391626596,
                                                                            8469109749560450513,
                                                                            -6702244919144550754,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '%ҌNЯɡѝԅǯŹҲЦйŢϯҵǘϕʒĭϙ\x83ʹ³ΑӑΤ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 252658.91017089068,
                                                    },
                                    },
                            {
                                        'name': 'ȿˢƧȠ,ɜϞоƠƩԊǭΠωBƁԠХӺϣΊΘġ\u0380ҮϙĄӁѤ(',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034736.176519:+0000',
                                                                            '20210327:034736.190743:+0000',
                                                                            '20210327:034736.203774:+0000',
                                                                            '20210327:034736.217308:+0000',
                                                                            '20210327:034736.230589:+0000',
                                                                            '20210327:034736.243869:+0000',
                                                                            '20210327:034736.256960:+0000',
                                                                            '20210327:034736.272099:+0000',
                                                                            '20210327:034736.285430:+0000',
                                                                            '20210327:034736.298537:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԕ¨ҺĊҋɬǿӋÿȢˊюĢ#ĲƪÌɳǀԔЭΖ¤ţɋϸӃӤͳô',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʮϜҨҾɭ˪ȳæ4ǓԔϷŁЎC\x86ŐΦѽԑùԗˆȉяӲƓƁʭż',
                    'message': 'ʳbŇĽȾñ{χѶ,ɝϤн¹ЋϑltΉ,ϘλȏԤѓˌɮӪ˜M',
                    'arguments': [
                            {
                                        'name': 'ˮԜϩĐɀӃɔáѾтԄĕ˲ӐεÌæDѡƎň~Ӥ҄Әʊ´ѧͺа',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŴεϜ¬ũ\x98ͰƴøѩƎѕʻζԗţǊƠs˙ȩКԏų˽iԛȴʢѩ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 398524.3446051566,
                                                    },
                                    },
                            {
                                        'name': 'ǦϔțÜ´Çʃӌӓά',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034736.810123:+0000',
                                                    },
                                    },
                            {
                                        'name': 'HӡɻɬxIˇŸlʯ˯ӭΑ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1919892801091490786,
                                                    },
                                    },
                            {
                                        'name': 'îͶňϋ΄BƵ\x89tĮɓԄΆƲȉǢɐтʻʴԪàɸɫѴȼ\x84Á',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            494839.8744179546,
                                                                            587346.8238501406,
                                                                            246784.18804359273,
                                                                            946351.8839223306,
                                                                            980967.1908479033,
                                                                            716033.6684489523,
                                                                            49534.84027020287,
                                                                            480870.96920872247,
                                                                            373684.4137609628,
                                                                            913202.2966638095,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЂųªзȜȮǩŦΥȫҙӯŨǻʊȆҒFɎƺЎÌӊϱɏ;Ŏ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1490365610187885938,
                                                                            -4389146058642729785,
                                                                            1021019739566087407,
                                                                            4950060220218762854,
                                                                            6417151522033073006,
                                                                            -4801540431946456893,
                                                                            1598005492978952323,
                                                                            5389765109077468934,
                                                                            -2624384018494508705,
                                                                            7521779345751508217,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʮŷĮȰ~ɶȕƆΥɹѨˌɵH϶ǍǟʇɅ˵єҗó˅ɺӖԨ˪ˏģ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 4147.895022791563,
                                                    },
                                    },
                            {
                                        'name': 'ҸģǉǓƐ;ԃ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɌЦԎ˶НчԠХÐѰǈг\\zԨǦƉüȓƠ^˲\x9cԍɔσñͳNï',
                                                                            'ѽԩХ¢Ԟņ˩ˠӬИƈԆʻʳ҅ıʄћƗϐϛͷәǢΞȑЄќͰ"',
                                                                            'Ȧ\u0378\x96Ǜ»ŻѬмTԌɄʫĕ:ʈӞg˟AȰ;ŧ,ǙǰɿҎлŁͱ',
                                                                            'ԬžӍ҆īǀDƚȕҗʣŪӍԐПAǽƴˎ\x91Ӳɖ{үĥҕÅ\x81˅Ȓ',
                                                                            'ʐɿīŲǹȶ\x9b¬ϛĶϹwД©ʎƸťұƫѵӱÁs\u038dҰȍҗƀɌɫ',
                                                                            'ıȖʙөAͲҨhГӐĦ҃ŝô\x85Ξ\x85ʴ\x8dбӟϸԥǲŽ˅Ҡě҉ÿ',
                                                                            'ϫǢӰχЖũ\x9bѺɾϰ×ўʻ҈Єѯ\x8cΖҾӴľPѶѣȉ˳Mȟ7ί',
                                                                            '¹Óѧ.ØſøčЗ\x88өǊ\x83Ǒʓŉ·ʳĲªҶʴƆďʰŞԚGvĹ',
                                                                            'ήɲöɅǘˇOƋɲʬϘ\\\u038b˲ËҬОĤеҮ´ΠώżЎӔƼѬ˗Ĥ',
                                                                            'ЛЏ`ʴɝϒƩĚĨȂžύªƢΧђȜƷԊͰҊ˼ӣΝҦĿǩųҗӠ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'νɚǉíʺǄΈ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '7ƿӤɟИњМŸȤͻӂÆϯ\x86ÎȚҷɓµҔɃӏƸҿȰ˖ʗ\x80ѻ˗',
                                                    },
                                    },
                            {
                                        'name': 'Ҹŉ\u0381ɦƦÔŞʊŇ0шȞή\x94\u038b\u0379ɗϬʮɘȖȌӵǁҳ',
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӞϨȳĥҰȫ6˄)ϻТȊԭƓĳ0ŭүζҿēɓˀƆņʍψəÎî',
                    'message': 'ƈɐÚƸąŵǥҎчȘȖѨBaĕҲΚԡΨϳɋӽ\x93\u03a2ԛˀ΄ǗÏˠ',
                    'arguments': [
                            {
                                        'name': 'ȔφԈȉҷ\x9aȞϩǔ\\ŷϨÔЦ\x8c˒λβ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɱŢԩ\xadʇʛыĒƧєӞҿԫЪ©ʃαʹʛŏѨɔҥƵѠӌδ¡ğġ',
                                                    },
                                    },
                            {
                                        'name': 'ȳϬћάÚ·ҺͻåұѫνĶ©σѧҿВĊðUǞҪɍ҅ŘӮİӠё',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034738.173486:+0000',
                                                                            '20210327:034738.190822:+0000',
                                                                            '20210327:034738.208311:+0000',
                                                                            '20210327:034738.225597:+0000',
                                                                            '20210327:034738.242263:+0000',
                                                                            '20210327:034738.259782:+0000',
                                                                            '20210327:034738.278955:+0000',
                                                                            '20210327:034738.295583:+0000',
                                                                            '20210327:034738.312319:+0000',
                                                                            '20210327:034738.328979:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ńӋƪȤͰȇ¯KȾЧʶѵӁɃȫʁȧҐϓ˘бҽԘʽșėΘϏу',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5788396364789506642,
                                                    },
                                    },
                            {
                                        'name': 'Ů',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 272713676712496445,
                                                    },
                                    },
                            {
                                        'name': 'ȴĨ\x8eű˞˦˓Ќ§ѥȿɠŇĂϯčƳ\x82ʝēǓӵɖǴǋΪӧȩϮϭ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3612017241568900633,
                                                    },
                                    },
                            {
                                        'name': 'ƖɆƖƍq˾ҫ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ίІҙǆ˘;ΞѱԚcɸуKuԗǁɯʣĚǅÒƸԒƀӬ҉ǭoķ˕',
                                                    },
                                    },
                            {
                                        'name': 'KŪŅԁ\u0382,˺аʮґλҫфʵǄ˳Â·',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            203575.65362434316,
                                                                            585386.8524472162,
                                                                            684099.2058507113,
                                                                            7589.307247710181,
                                                                            835511.1864862081,
                                                                            216040.69497055246,
                                                                            226300.2251323213,
                                                                            469369.5396524167,
                                                                            633503.6828685286,
                                                                            10439.7918246443,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ћòǎĥ˶ϥˣʲѫӦŜȩλǐʞ\x89Ϣ¹чɴȒϧ>Ʊ҃ɆΠˆɃȓ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 993902.4736165085,
                                                    },
                                    },
                            {
                                        'name': '¶īƢ˩ϰĹǾЄӣɏӖ·ӒĐЇϠɠAϕȁʝ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            629349821814061481,
                                                                            -5254399779692429927,
                                                                            -9024135545038526869,
                                                                            -6088025218207377338,
                                                                            7934263480080346492,
                                                                            -2646430005021444022,
                                                                            4730046358061111884,
                                                                            1117774761187438507,
                                                                            6181014091094807204,
                                                                            3697271137765918943,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '<҃јɀʗυІ¢˃ʗұʮ¿',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1827665088594118887,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϑƜːӉθЄα\x9bȵіEɢɷҢˣԤξСӣӆҺ6ћƔőŅџҋǐ҅',
                    'message': 'ŉФԥЕbųӁ§ξĞȮ#ÒҗǒǙʧφћȅȼšǫԬ9ȏɿʓ˨2',
                    'arguments': [
                            {
                                        'name': 'ƘɲԖȣɣэɃôɟȏʀ9Ş',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'śоĹϡɠɳЙÀԬÞƜҺҽɃԬǻҕ!ѹ˛ÀӉϕɴjɨ\x99\x83ȶŋ',
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
                                        'name': 'Ї˄ӭǄ(ůɾƣɻΎ˙в\x83ʀχ˼ŨτΛʲÅ¹\x9fԬЄćτӟŵǋ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˠ\x82ΕӣüԅÌǚѧͲϩρĜНōƟüȩĸȢҡşĺ.ҽÕҔÌŴӽ',
                                                    },
                                    },
                            {
                                        'name': '\u0383˙VЕȌGʻԡȄʿvȸ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1804331110823386250,
                                                                            1880257571129259193,
                                                                            -3938083719505989813,
                                                                            8902231333152539960,
                                                                            9147574677774324584,
                                                                            -449736463886284130,
                                                                            1604704378494812367,
                                                                            -7153783373786942631,
                                                                            6746735715907887636,
                                                                            5795096601907642493,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŞʚҼӞԟ·Ń\x9f£Èȱͳԕћύ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 657108.6680093341,
                                                    },
                                    },
                            {
                                        'name': '£\x94ԈļŬ˧žFʬʓƎǱðӌíҥ·ʦìҘԎǙŜşȎЃˎϕʧˍ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'шϾǽ\x86´ʪѡƱʀʓÁҪɍϋϿӦӿƺiÖː~Ĕҵ\x9eрżҢˢ7',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 386062.34881567315,
                                                    },
                                    },
                            {
                                        'name': 'ԓöϼƎÙĝԙ¯ǃɰφЃƇ',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8a˶ԑęRԙɋΓɪǧχ-ӋǉȳơΧĮƕїєѢ\x86ɳʢДÆ¸¦ӷ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '9LΧЎԀƘɃɨӍĞԏΣӑʉ¯+Ϟ<łSÕӖνƶέȫЦŎѝƨ',
                                                                            'ƘлİȈľ˥ƖԛӴūЌ˷ЂĕŸ³Ѵӎĸŷʘ¥Ѿ˝ÒұϟȉɛϢ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ėp˙ĄӫƁӧȅѠôì˫УъӾԄϦɞмӐzǢǫɇ',
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

            'identifier': 'Śøѣɟʭ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'ȧ¸',
                    'message': 'Ԧ',
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
            'name': 'hžȍԝɟ5ѧδΆ˞Ƙ\x89ѧ҄ţĶÜʂǋʍǖԮåΑƍ˛ŬñŜj',
            'error': {
                'identifier': 'őΩ\x81Ʋ5ʄҕΞӹԖŪғÔėɎχυɗeΕĝɈӑôθщЫÊɃʍ',
                'categories': [
                    'network',
                    'os',
                    'network',
                    'file',
                    'configuration',
                    'configuration',
                    'access-restriction',
                    'internal',
                    'network',
                    'os',
                ],
                'source': 'ǳӠϳзȥǋίĮȡɸʞӱ ԬПяɄɵūѝ°ǲ3$ØԦȝɓƺǾ',
                'messages': [
                    {
                            'catalog': 'йĔόӷΛΨļǆɟƜόұтʁúȭĐΎšęҒĩӂШƟɏwϡуǭ',
                            'message': 'ӬʲВȚё?)ДŎ¾пϯõʔŸfϢKʱ~ŪǿѴҢїyɔųӷӋ',
                            'arguments': [
                                        {
                                                        'name': 'ǅV\x94Ȑͻ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 9184645277509307117,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΚɄ@ˬӷġ¶ƇǷԌ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ηҕƘɉǿ\x93ÛʈѪӷ͵ҼȈ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΞӌǑʫ¡µ҄ԠŔrρƬƃԙͱʂɜʱϕǶ˄ȣ7ȫȿŻʲʠ\x81\u0383',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӺĤЅǈ[ēЩ/ĺΑҦ˯ʛʻ\x8eгÜãҝ\x98ʙ×ȣtȝΌĂZŌȂ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2752108325727189883,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʬéȎ˴Ͽ°ƼŮɒǾ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'aȗ˫ǚɇɎԄŶҬҹπԤ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȍʛȿɩϼ\x81Җǡ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӳԁӋƽ;ӶâӅπʏpƄɩрѳǖΰҬ}ð1ζ˲!ȽθѐνԮͰ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҞŵČԣ?ũRȜǨӅ¢К˝ˏÌЬɳΉ«śхßÎƤwãĝϚƿ\x91',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5343276585132286889,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӀǲéüȪźХΒƓįϦӂµpÌԟƫʑå˺ğôǓQòĠɜʅΏõ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĥ¨Ѕҽ˧ȥȦâҴ\x95ǐśu˵ºʳҷԞiĝź¬ȐȎǥЪͶΪ;Ζ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӈɜňЖӷƵǻ½íǥàѭÁ˹ѲÌʫғͱѣѾÃыϳԞЂΏϥǡʍ',
                            'message': 'ӝąĩ4\x95zʩÂ҂ͱ"ӼǸиїȃʷ!ҖĎӈԈʡƗȞͱļħϨɦ',
                            'arguments': [
                                        {
                                                        'name': 'wʪȍuȁ\x8b\x94',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'үΈәpǨɠǘyд˚ġо',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5515827661335263939,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƍ\x85ÞǧϴхôǢ1Γ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0379ː\x7fêҭǖҮʝŤ¡ʵŇͳǤʆč',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϧ²Цԛe\u0383ҵʎƼЦʊDɫВϕƔɝ˥ΐюϔ˷ԮϺƲаˠԗ΅Ԫ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȏϬ˳ȵĽɲͼƬxǯЉǘГǋʮϓĜŞԏ͵çѤĆȱϬɉƝηҽM',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӥ§ʽхǇȜˌϬǛ¿϶)ϋɴΐƾâ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǟӯ\u0382ƉэЄɡBÃǙѸԑɂŉXǾÊƈӢ˳ϾŽёӯӨƦ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8bίμėʩƱě',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĺǰʴ\x80@óлӋDѤk<ĊҸYǻDȬî\x9e<ʅѴǀ|҅ԣ«ǵÑ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҊʛӐʵì]®ȋѷǷƸӣ˗Ĳ˂ēĄЙӖɧыuӂ¯ƦŜʟѻӀǙ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ЕҕοσƖѢύѽɒД˞ҾƔжÔɐӣäʔú7Ҩð˞ԡöҽMϝ˛',
                            'message': 'ŇӅC҄ǚͼcƤɛƥhʌàzϵ%ˊɾ£ϥҁǐĮϒέ˨ʠˋёƞ',
                            'arguments': [
                                        {
                                                        'name': 'ƿÙÙȎӫȡӰԡϘʝЈөȎΉ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʈȝϳ\u038dęɣǠԝϊzưҶҮŀ>úρĘʹѧϋф',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͳϦųԩ4Ю\x97(Ѡįɏ~ԗӛ˾ȉ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ī±ˈђǲZư5ӛϔԚӐψÅ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΌʛèӪɳγův\x9dǔs˞ƭʓʒ϶ԃҊǆѴҀǅ˯ҵϲѴɌ°\u0379¼',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˀ϶Ŀϰ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034719.841834:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'TôɿКƑӿ±Ʃ҆ĿǬˤϼȬыҌ˴+°Àϟʭjԍ\u0382\x89ȪʚɤĬ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 881396.1761449601,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ğӹˇƸϿ˃\x89ό&ϣ\x9d\x82ȣԊΦƪϡ\x9c',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˯~Őč´υоғȍάθ.ȻʓŊџύǉƺЁǉ~˖ŚΚ˻˭Оĥǝ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɽżԩԙѝ+˲Λ˽ϒĮρȗǋҋyåфʵöϵɋ˵ёȞϏĤųɝǐ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŝɢͽСрҕčÖďήȔ҂ʭ˫ЇϹɴҦԛѤӫǘÑʺӝȅҙϼŘǙ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӽЧđ҆¾έɗΖпɷȡӒ˼ΣɄЗÒ˄ͷΑƧȭϼ/ԗԦԔҰǪȳ',
                            'message': 'ѣɸcŰƑż6ʠŢ˾͵ӑΠǜǢƕҋŠԁΰʐМHҭˣŶλӞЬҙ',
                            'arguments': [
                                        {
                                                        'name': 'hʞʸȿÕӉƉƭЌȁÚȀ˻о\x99Ô¡HÓɎЭ˹yȰāˏγ=ɨƁ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034720.252445:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x85Ċʹˁ˟$ÉЉȼҙΣѿxŰɟұˣˁ·РƗǂȳϦ^ɪҵƧ˔Ƿ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΔЬƣǞϯƐȕÉ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034720.392454:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӖƗ˖AȱƙЬǭǹ¢',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -85165.01620014687,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɟ¡ÉƤɢɣǆӷѶԞƀђҙӯЁϜЖƥƷбΟǭ1µqЂVɵҾő',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'O\x9eѹ˾ӬʤҎQǹƄƫ#ľĉ˔ƍџΐȚǆʭ\x83Èό҇',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЌѻЈ˻',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĩЗùș˜ЭóʆθƗӦѤǿĜ΅ѬӇѭƙӨԢŒӿĿőƵȍþҚэ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʇ\x94éΓНɟѰȁ˶',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6783840991279627105,
                                                                        },
                                                    },
                                        {
                                                        'name': 'OȦѲʝЎÄǁԍƂµηŷƁˢЬ\x90ɗȖŌӌƃŅīқѢʝїЈˣǭ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6465599647032246424,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԩƼ¦ӌîӝˏԑΎčϺцΤʀԆѵίʇˋМӸǯЦİɆ\x9f·®Υ«',
                            'message': 'ɸŷ\x82ҷϝ\u0381ĩіƧāƨθĠäвӧɸòНŴʌ˼ǲ\xa0òҬȂӁɄá',
                            'arguments': [
                                        {
                                                        'name': 'Ώĕɛ˼2ʘʋȄÄǊʐŝ¾ȣşԩСЖƷƬΆӪt\x8eɔȶϫƢ×Ͱ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĻŽΡʤŞ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŭ\x98ŤӓЋ˯ǵˀЄӳǯйʝҿȘȅĄΡͲΖǎɫԁǜīüȮǥÒǘ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6733905251062593212,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΞŗŗӟгǬӋϟ_рӇɲɆYŰ2ªƹкʣ˘ʫơҨÇ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʝΛϬyʴǙɦɃµƑȔЍÜ_Îϯ˂ ѳө\x90¶ѽ;βԉΫ˃пè',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ξΥґ½ȽȼϮɫ\x91`χāƢέϸ\x95ˍɸϩ\xadȒįĳн6)Χɉеԛ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˒Ǆӎǀ@Őψϑ\\ȺȅɭĠηâțҊȮɤЃҹ\x88ƱНЯ\x8dлс\x8fҧ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 154775.61468051228,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѹŏŵЎƱŅʇˤΐʮќĦƎ˺Ȼ\x8bҐO×Ⱦ\x9aϔӺΗ\x80þͼԄĒѳ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '®Ѫ˦јϪϏȋФ(˩ЭԩӤ˩ԃ6ˬӁΜȯϱˮťœÐԜƇŐˁʾ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 637870.3031472941,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ãǾЙԁ·ŐΓƙğԒŸǻө&ƓϬі˕sͰҫє\x98ŊНѪɮ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'έóȊԫϷ\u0379ĨӇôǝýϱˈѸG\x96Ԛ·ŔυԅΊяԛʠ>ӦʙéЋ',
                            'message': 'ƤȬйґD*ҿίȔбҜ\x8aɿ˝ά҃ɡÎϧΖԞѕÜЌ¸ŏ˷ƺˆό',
                            'arguments': [
                                        {
                                                        'name': '΅',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҹs˴\xadБ¹ӉǧϻȌaǲ0ӳшřγƣƕ\x8cёʲΛȥҹҋҫЙĿь',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϻéʜ͵ǯŴчʕ˂ΝϊƸŲАːӂ\x95ʞa¡Ͽý¬ϥРπғΙӈξ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '¿',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȮºŏĈ*ǚΌĕӍӟīҞŃϐȷ\x8eӎӼҭӋ˄ʞĢưɚʒƫΠŬ\x9d',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʑϼVӡ¶ԞӀʦΝƫʌ˨ąϋȔˠŗЋrˏ\x91уƠїʤʿӆҗӋʜ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0379άŷɬӛ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÉȹӇ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034722.327926:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŹŹǚȈɌάĖӤѻԨˈϐǩЄŞӻǈóĄЌԒɅҨҊAǶΦĈͼМ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4710521032620276442,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɦыѴΝϭτϚІ92ƍhǊUFϟѝԨϿȁ\x84ĺԌȹ§ЬхъĀӗ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034722.446826:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϗΛд',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƁăЀȹǊƕ˺ΗșĢѓMRϸǞÖϼrɿĹ\x99Ϊδӹɓdλəϴѧ',
                            'message': 'ϵɧǚ\x92ʦʲĖɟζҠ˛¨ηǺԘRΕӁȧü˸Hčѵ³җQӉɕļ',
                            'arguments': [
                                        {
                                                        'name': 'rĪƖɀӄҝЏêɊ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ĵý\x8aԨǳŤɼ҈ŌӜ*άɒɥФǨcĴč',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȯԕȅGƞÝǅρCÍ˘Ђù\x92¢·ƍǧ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 296298.69316592294,
                                                                        },
                                                    },
                                        {
                                                        'name': 'LgϓȷƋӜÿȢЎůҞEұʺǗʁƈ˯е\x86ȢHϼӠʛԨӦŁѽ˳',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɳφҁ˭кͺ҆RǜʺЭɵԉǧðģǵɌЯʈͺƅϳʅˁϱѮīŤĶ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Îǩ¦ƞńǗ˃',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԇÑȚиˇŞҲӶĔӒȣї\x9fԙϟ$ÞʃYƜ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΞϛɖɁóʬǴ˫ĽIʑ¾¨ҬoȉɱŲӂʧǧҪэźҵhҨ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɆάǶûϓȒұϙНňμӬÓ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 479667.3774866569,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8aŴƬîǾȮЕ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǢӎIǡ¡ӑɁҖΉÉϓԥ˃ӡӳɪ˳ыáӢŨӦ˦ȆƞǢЌɍ°Ԩ',
                            'message': 'ψHǾӶÑΪҡЁʦȘɸɇȕŷɓ\u0380ѝӖɂҒӤʥƃƀӕÙ҆ɂİϲ',
                            'arguments': [
                                        {
                                                        'name': 'Ϝɭʆϛ?ςɀаĢȤÄͽДȿĆҋƈͰвƔ:\x9aȁж˖ƺЈbҬŊ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŏҏšʗȻ°П˭ȀϐϾŗВǦțҹe',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҽx3Ăб˒ˍťęŧζЃÇiɱкȱӉЅɻξϼЊƫ«Ҷ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x80Σъʙm%ʉǳKěŽҠϜƸǸϫ@ȷŀѪ\x9aȏ˾',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034723.710470:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'éňʝ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҩǹ\x86γϖįӌ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͲѷԎâϐ˝OʶчgӀӱ³ĝɲʞ,\x82ƧΨǷӑƚʤԂǤÛʀ0Ζ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 594560.7218245096,
                                                                        },
                                                    },
                                        {
                                                        'name': '-Ē×ŐԖ\x9bǁ˺ŦшΕԐĶƇȸѼӚˈɓåǃƍӽ\x81˺ԙʊʪЇҁ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϧ\u0380\x82ǓϞƱƢŭśȳŞęʛ\x98ŭ˲Ƥ¿ӴѬө=ɛωŚĊϯʣÅј',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɧɩОEӪѬƯԏ˰ľЧÍК\u0381˫ǕèȿlDѵˇ˷˱ū÷ɞЂ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԉƀςƩ\x95ΎÖѪϓúєtȟӇл?ԂўИǋĄÔӘʌ\x8cŒµǤюĐ',
                            'message': 'ʄϺϷƐ\x97ƘΔ\x94ϴԭʩғɓØΣØǾɜɷεлʈ\x9bвľƭɕ[ǰ\u0380',
                            'arguments': [
                                        {
                                                        'name': 'ȫȼӿѭԗϘϹéĻԝɊǴȄЃ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 668557.7522276787,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ȯ.Ŧ²ѕɭÙ¶҅ƽǣȫʁƌˎђîӜ½ŠÚӛÉӛњƗƾѹȣл',
                            'message': 'Śǆ˘¤XϾƏZɟðΘǣЀʴҖ¨\u0382ӕþKʹςɽѣʜĕӶȵЅҲ',
                            'arguments': [
                                        {
                                                        'name': 'ȍ%\x9fϔԬʛɊʀӪЭĔԈЬʻzʑōȇ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 900998.1887582621,
                                                                        },
                                                    },
                                        {
                                                        'name': 'mƖҏѹȿȄƲűŻFÊ0гέ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŵϿ=Ĩһϸ\x98ȓԅχϾͽȍӻѩC˒ ϳʵΠӖPʾѿБéС!ύ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʗҮƳРѼȄ˨Ԥ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΓƿӰ˟όƓϙÜƒE˾',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3087544966436153121,
                                                                        },
                                                    },
                                        {
                                                        'name': 'αϐą\u0383ˈЇœίьΤӟ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6968820579038960041,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ïΕԀµʹuȴ\x95ȕҦŚȽЏϑѼЦНЎŨӜɘǌ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ұØsɌÛɎÛÊ\x99ϔύ˷ǟǼϓɾϬǺΫɦӻђǉÈʩ˳ԞɥЮ\xad',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǩеȐǞԡɎʴoāýÒƊ½Ʉʻ;Ϋћҋτʝ\x90ʴӔԨďσҗγě',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '4ȴÿǙ.ǀҏӞȡ;˝ʬζ»ˠȏΪłӄŖſ]þbѱķΰѢ˪r',
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

            'name': 'ϽΠÞ',

            'error': {
                'identifier': 'қԂӧϷι',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': 'ҋˍ',
                            'message': 'ď',
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
            'name': 'ǾǼÓѕʫʩ¢~˛ȧв\u038bʃÜҫԁ\x8eоϞ\x9dĶʑıŬҀωԭŹϚǋ',
            'version': [
                -7135893210271709790,
                -8465056313871976655,
                -6297213888230717168,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ɰɽɮ',

            'version': [
                -1189909747057076467,
                -7365739732589399563,
                -239627544278283312,
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
            'event_id': 'Ƙɱ\u03812ɾƐʩҤʏźˌБÕԈɐʋqɺ«ϦŝgəKĮӲ=φϔɫ',
            'target_id': 'ШLгϒΐȕũЦ÷ƙƑȤҰˎ˳îӰϛʩġЪҩ\x8eЃđƘкҫEÐ',
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
                    'event_id': 'ǔǓΙ˰bˊѮΤӅԊӸԭýƬƐэŒѭƉô?ǲ^ĹŜӶԞŦŉѦ',
                    'target_id': 'Ӏ4ӯҭў\xadʁ_ǳǥϘӻԏΤʢҰƮŹĨӡνÆҫ˃ñ\x9dԕƝƀģ',
                },
                {
                    'event_id': 'E˗оѝϰǃùÑбţΐõϑѭȢŲί~Ѡ˾˘ǧ7ӻƿӥЮbӗϽ',
                    'target_id': 'яǽпŐǍƞŌѐОbʟĥ¥ȁ\\\x90Ѯͳ҉˨\x91ĦєÝԅʳҸДĚƮ',
                },
                {
                    'event_id': 'ʣɵ-ʚǕѡˌһдѦЃËsƛȬȮѡƁЕξɔǏ))vгҏÛn\u038b',
                    'target_id': 'ɝ҈ÿıҏ͵\x92ƁϦɅʐUȁ¹\x92~ʛūҙҧŕ\x88˱ǵЇ¡ӟƬЈϦ',
                },
                {
                    'event_id': 'ƑӆѴυƧԟѶʭĕϙĖӬrЄӂ¥Ƀҙҡˍ˴ѱϠwüÄϣӤɩƥ',
                    'target_id': 'l\x9cԃѣʫɴĈʄƦҩ\x94GϮҍϰeȦ҃Wʱ˾˭ήʅΐˉŃ\xad\x8b·',
                },
                {
                    'event_id': 'ş§ύĹɊȃüͰZţΝƙ\x81јρѣʳ%\x8dӞƢɰͽЦɩǑÂŃϳѬ',
                    'target_id': 'ӹ=Ȯěӱѷ¬ӑ¹Ϯɱσ³ÚãʕԢјɲŧʳҤƩԗ\x9bŦÕȥԌһ',
                },
                {
                    'event_id': 'ľ¬ůӔӡԄЈĴʪq\x91ɡ§ѤÄVɑлԀÏӘʚţƬˋáԁQƿϹ',
                    'target_id': 'ļ˷˓˔ū¡ŤāŎɁΐôĮϓǨƭ[˅˖ɓβ˳ǰ˛ΫʨɪͶҊʾ',
                },
                {
                    'event_id': 'ȶȥɗȰ˲ǒΧӪ˜˘Ӈ\x95ȫԇˇĺϔйʵϴ˞ȮηκÄƣ¡Ç\x8bǗ',
                    'target_id': 'ӔʆӸ0ǁƔû¶zǗҖǑĠӄѓнǘ˧ΖԇWġºȌû˓ɕϨΖŋ',
                },
                {
                    'event_id': 'ēɲΌљiӸŠǝȢ\x8bĥɉԁƎʅӂӰԨSŋκοΒȊñϾȨ·ȑи',
                    'target_id': '\x89ÁǽŷÛЎƣĠёɽķοɱʯ˰ʋˍțґПƴԞơǘԕѣξЗ\u0380Ɵ',
                },
                {
                    'event_id': 'ˌĔŘЭћɛŤӊ˺҃ϩÛbǋÂκŖƆʦɾɵžý҃ÓǍȸĸǈ\x83',
                    'target_id': 'ŢšӳûƷ/ŨɁˠ÷ÁӮʬҐũ˩\x99Ťҁi˼ȱǖϧȡǼЃʾ˺О',
                },
                {
                    'event_id': 'ŎͻɤȲÞĩЉgǥǕʣɿɗɐ',
                    'target_id': '!҆ĮѨȮșgԡˁóǒʎϋŲɡ\x83ńԔV6ҥΨĴјѺHðÐӭ\u0380',
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
                    'event_id': '<ʦ˞ТҿʹͳԡҼϨˮӮGȄ¥ʯɍĳȴĂNĩĠĖðӟϻӫĝΡ',
                    'target_id': 'ɕϖĭìŋӞӄʢғƶΆɃ(ѤεφɐѫӂϪ\x9dņUԔƜˎѥӹԎ¶',
                },
                {
                    'event_id': 'ɤưɋԪȤɀΗÝɓɡDǗҬ¹ѳҚƟƎɛқԁʂ<ý9ȶøĈԐҊ',
                    'target_id': 'șѣhɈzгuƊŜʍøȘѺҶ˥·7ʐŎĞÒӂɬǆǺ?ҫȏ\\Ћ',
                },
                {
                    'event_id': 'ʆǘǍʚҗ$ҍǜʢț\\ϨǢҚ\x8cӺԅƌɃPĢһӂї˚ǡmӬŉѬ',
                    'target_id': 'ΞƵΚĄ!ĜĖкƼƃĘӞǄƒҲԮԗţʎnû,ӠġϣɁřʙʡʤ',
                },
                {
                    'event_id': 'Āƃ\u0381Ѯ\x93ЇΛӉӧȸəԪͶŉЉЉʿsŁĝ˵ʎłńˑķӂЉ˂˵',
                    'target_id': '\x85`ԁԙõкŪԧØíêȱɛÝɘЪ7ч¹\x89ԁДX\x94ɐКɶ\u038bəƧ',
                },
                {
                    'event_id': ')ŊƀӓͺӘƮ:¿Ǻʂ¼ĺ˷јӻӆΟͰǝǷѳфˢ˳ӖłƉȌÚ',
                    'target_id': 'ёɐâ˗θʁƑΤƾԥˎǈɅƲWҫЂӨł)åԛ\x84)˭.иɶ¢ε',
                },
                {
                    'event_id': 'ѱÎ ӠΝ\x8eț\x93țӢΛñϊ',
                    'target_id': 'Áȃɹɨɉџҹξ˚ӢT˺ѠʺԬҴêƃǭĶƚaƎ¯ʻŸе&]Z',
                },
                {
                    'event_id': 'ЌџȼƱČĿ@\x9bǼZǇӵԨǊÝΐϤҒѥĦԞѨѰʖʺжƚȆÆd',
                    'target_id': '8ɕΦҁ\u0379Uɶ£όʟȧʿϒɻ͵ЈάӀǾоЬҚfСςƢяŞόǳ',
                },
                {
                    'event_id': 'ζГϗϵƕϨͷцɰ\x8bĺ¬νԞǞԅ×~ѶǭƦ-\u0380Ɲ\x92М',
                    'target_id': 'ӔɧӂˈCԇ˯ǹȿЧӀɲӋѫőΝјĉӪ˳ɼōқ´ƞөͳӋ˦ǟ',
                },
                {
                    'event_id': 'ÃˮжҷLƾȗоӽΥɳzϗϸѲʧͻeҥϮƺ\x84ѰϴƝϼӦßƠі',
                    'target_id': 'Ʋǌē\x8fщҊǐϵ\x9cӐÌ\x9cԄ҉ͶНșòɛ͵ωζϤ¹ˣΞЎŲѦЎ',
                },
                {
                    'event_id': '˴ɻƗˈˤʤҖ˞Ƽ°č҄ŉΑäɨˏƊжǑԙēδɨЍȰ\u0382κëЀ',
                    'target_id': 'ȅԙǭԜԫΉѲßˋПüɿ\x84ωќһǅáӸʢŞ,\x96ѱgǝȕʤư˂',
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
