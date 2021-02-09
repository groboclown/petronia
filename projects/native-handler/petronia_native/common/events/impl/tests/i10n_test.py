# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-09T22:29:05.089882+00:00

"""
Tests for the i10n module.
Extension petronia.core.api.native.i10n, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import i10n


class RegisterTranslationEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_TRANSLATION_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisterTranslationEvent.parse_data(test_data)
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
        for test_name, test_data in REGISTER_TRANSLATION_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisterTranslationEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTER_TRANSLATION_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='locale_code', name='RegisterTranslationEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='catalog_name', name='RegisterTranslationEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='message_file', name='RegisterTranslationEvent'),
            ),

        ),
    ),

]


REGISTER_TRANSLATION_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'locale_code': 'ˠ',
            'catalog_name': 'зԖέƕЍǬ\u0381ÎԉΛ˼ň¶ϧȊΘӥϥxϮϸǠσɂţÀёYʫʚ',
            'message_file': 'ѹӅϞěķŭz˴ŜĤСŭǐEԥъå˕ιђКþӠξȳӦˠԮѰþ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'Ȯ',

            'catalog_name': 'Ͳєĕ',

            'message_file': 'ùԙ',

        },
    ),
]


class RegisterTranslationSuccessEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationSuccessEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in REGISTER_TRANSLATION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisterTranslationSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTER_TRANSLATION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
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
                res = i10n.MessageArgumentValue.parse_data(test_data)
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
                res = i10n.MessageArgumentValue.parse_data(test_data)
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
            '$': '¢\u0381ұ4ɐV!ëϚΉҬĈĢɑɰʘħѹʮɽ[ϖɱ˴Їƍ˲ːʡӭ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -4560845457716965948,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 366336.83506636386,
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
            '$': '20210209:222904.999947:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                '˱Ƌ_ѕ?ɶύŧԫąӻǣCǷãƠѱǃ9Ā,¡\x98АҫɞƁʟ˶Å',
                'ЋѩňўFɀʸǛΖʛыʧќ\x86ϭĴӚŐŕɭ҉áӍѿ7ʮƛРβU',
                ' ѭ Ԏı\x9aȌԢǌӟÖèºµНǻďʄάȽɣǆЉҿżԑ"ʙŒˣ',
                'ĭÿǀϢƏȺԌȑЩ©ѫʙԘĠϭЗ\x85Ɇ_ʌҿrŰşőΞɻúГԥ',
                'ȗӴˑǗ¯ЛˑІњͲȔƐǹϊΗ˨Ӟ·=ʬǠҿҨŁȏˆ˖Üȇĵ',
                'øϬɌŵ=ӾˏϙŇϓϕΖāӲɗΚɱåÔƸδϤʬōѵ$Ԡǣ\x96η',
                '·ǡUǍ҇öŸİșyɑѻԦôƦ\x92Τǧʂ\x82ʠEϐԣͰȁƁӡӇȒ',
                'ǧîϤҙЃΨҷϑ\u03a2Ę΄˖ʎǽˏѻюĢǼќƯ¬GʉεÅx\x88ʲҐ',
                'гĤŽ¥ȞΖτʟƅϴӯǦԛѝҚƠ(âҠȩˌŬЍɀĽʜǬł\x86Ϊ',
                'ǈÛˈ~RЈȺȑʕˣÞˠ+VȻӰ\x82ѰɖЙǬώQгδΜχ˳Ͻǐ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -6763020052268049776,
                8764973295998172941,
                4150421869938855618,
                3790817545705484024,
                8370331430518767981,
                -847309620821637783,
                -3658034809466006926,
                5340307945254706639,
                -3456892056136401724,
                745922359949044672,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                771951.6765821886,
                234894.76162764512,
                168428.7234004694,
                405090.964972871,
                804517.7493901047,
                767657.7041897854,
                221080.45055714756,
                215280.64927306207,
                111326.80334076381,
                971561.8850102518,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                True,
                True,
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
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210209:222905.001399:+0000',
                '20210209:222905.001422:+0000',
                '20210209:222905.001431:+0000',
                '20210209:222905.001437:+0000',
                '20210209:222905.001443:+0000',
                '20210209:222905.001450:+0000',
                '20210209:222905.001456:+0000',
                '20210209:222905.001462:+0000',
                '20210209:222905.001468:+0000',
                '20210209:222905.001474:+0000',
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
                res = i10n.MessageArgument.parse_data(test_data)
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
                res = i10n.MessageArgument.parse_data(test_data)
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
            'name': 'ԜûѦЦԅģ\x85ƘѨΉƂ¬òҸЕƃŸî<ӅόϜɋπŎ',
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
                    True,
                    False,
                    True,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ω',

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
                res = i10n.LocalizableMessage.parse_data(test_data)
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
                res = i10n.LocalizableMessage.parse_data(test_data)
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
            'catalog': '҇ò?ǚʍŅ˂ɛǉÇЏ#ԙԧ\x8aϑĆōgʶΝМŚŁɹЉͰ:ĭĳ',
            'message': 'нΩȲđԥϐ˜оөŎӴðΕгο˴Ϙo\x94ІϿ˒υѓǗnҾƍϦƛ',
            'arguments': [
                {
                    'name': 'зϑҎǑÅκÛ|\x82ωӈɞ!{ұB˳ȝÊӚÅҁöʍԛ,ŮQҐ˵',
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
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ΘǅҁǤěšҙ',
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
                                        False,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ņ҇ŧčɓƕѨʍџĨó˓hӵƺžŇбƚ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ψҌ{/ķŌȪԞáѕϨѻʾͽϴĴγϖӯΫԉ҂ǅļŲJéƄʒb',
                                        'ʸŬφ˸ƻðԛÎ˸ţ³˃ҬѸǏǫӽ˵Ѡή+ˁʁ=Ӓ9ĕҘҢǸ',
                                        '˳ƛ{өȩ\u03a2şİğʷйΟʶϨ\u0381ѽвǻэ\u0381ҊȍŐķªʂýyΉʚ',
                                        "ƃώҎоȵҁŚҴʼʧʣáҽԭƌǴÍȳʅˣĎΣ'2pҝʼӜύʗ",
                                        'ƗȸƠûϜ4ǲѽüϬЃě\x9fǀǳ\u0381ɍʀɇς΄ʮćǖǸŚ\u03a2ɛńƗ',
                                        'ĹÉӷÿθ}ѯʺŵ\xa0ɶľǊƅʧΡ˝Ӧ\x99šū«ùӗ+ϙѨӭϢԟ',
                                        'ԇ\x9a\u038dĥīȥÙ2ʙǽőȱϡөНѶ\u0379ǸɄ©ĪŋǑːȶúȗҡ\u038bã',
                                        'ŇԒƌѭʓȨɷϷϲÁѻќҨфҴȗϹǸFѳƍӔɰΊɸőďˎʆѐ',
                                        'Ȥǀ¹ҶоŦBӹcǪȚ҄ǙӢˢʶ\x82ÏɡPԫóȯӻȧǄǼĉ´Ĵ',
                                        'ďŞϦ˘ΏҡƔϔɉǵŕƙsΔƱӰУԑ˝ˠŘͳǻæǘʲυлʓɞ',
                                    ],
                        },
                },
                {
                    'name': 'ũԛŷǏĢȃǏǘ˯ɶЏȑ"Е®ӷ\x91ʺƫѵ\u03782ĝƃ\x85ƗɤƳŵʬ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        -45314.31604011705,
                                        367593.87400916556,
                                        330832.84684130695,
                                        698446.5363815279,
                                        185367.46401141997,
                                        632035.2682661609,
                                        415100.7934877016,
                                        400352.64848025225,
                                        102955.1961432054,
                                        990031.2786702935,
                                    ],
                        },
                },
                {
                    'name': 'ȱtƉǦpϑΙҹȬҶʜXДÚϏȨжĨǌʪɠ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        874220.6877668351,
                                        307762.63542441966,
                                        50467.67120152904,
                                        -37365.05013501526,
                                        718906.33689197,
                                        -12268.583877790603,
                                        916835.9572634756,
                                        577002.485762847,
                                        12296.794290804202,
                                        465837.72230426304,
                                    ],
                        },
                },
                {
                    'name': 'Ԑӹʻǧ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ˏ\x81ȼÎϬ҇ƢǨϓÍžβ˒ϩү˦иτ\x90',
                    'value': {
                            '^': 'int',
                            '$': 8069154128676457838,
                        },
                },
                {
                    'name': 'ԟ¾ǓʍȺћLΡѠ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210209:222904.997953:+0000',
                        },
                },
                {
                    'name': '´ɒɎ϶ɡԫҳƛԢĆ˳ĶʲȲѩŀ˓',
                    'value': {
                            '^': 'datetime',
                            '$': '20210209:222904.998236:+0000',
                        },
                },
                {
                    'name': '\x91ҪǓňʿҨįǓɬϺʃɷɊǷ\x9bɫǂǁ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        '´сԖƿΣǓòҰԮǺɐæ<ʅgϛ˲Ҧ\u0383Ǵ£\x9eяӚ˨6\x86ʬѤȵ',
                                        'ԏΝßҺ˄ʉƷͳӍȼӮ΅Нǒфӏ˹ȦԃѾөʚȪ˂q£ċß\\p',
                                        'ѬDʐ¿ʟŋǸƓӆƊΑĔśЊ˔ѻ´ɭˍ°ьöӐԅ˰ʑΉÎ˖Ζ',
                                        '҅ҢzɰҨрϣAMо˔ɩŧΣYƨϋaӶǠɆȺыȁȽƚǼӾ˭ƶ',
                                        "ȪʀӚÊǏǿɶŉĆ'ƟћϣͷɆʐˊ¼ӒǢīà)ǁˑЖʦϑӥȄ",
                                        'ċҞҰËŕlƍʞԫƿ\u038dΛƲȋǷЃάͲʒɳȐˏӪӫ¢ӭʜƳoǒ',
                                        'Ќ˲HȬÎſӁoοПś˧\x8eŚҸӈ˯ЦѕƃЇ˗oҧˀ\x96ҮÂÙǷ',
                                        'ƟѻØЍʽŨyɘĀ¦ͷ҄\x9c\x8d±жʐфӥ\u0381+ҁԡǎǤѩiPϫǣ',
                                        'ӔϢƎʧZšȀЎWҥȧ\\ȑѠϞűřѐNɎâjиӠ"Ņĥƚԋʬ',
                                        '\x97єšİИHҖȴȬɆǆƓаϫͺûǵɱϮӗƉƒ˶>ӽƙɁϜӬν',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ν¸',

            'message': 'ʢ',

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
                res = i10n.Error.parse_data(test_data)
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
                res = i10n.Error.parse_data(test_data)
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
            'identifier': 'ϩʽ¸ǳƫƣНǞȘǫŬ]Ѱ´\x9eԀɞҌrǯͼ˰A\x99ΎӝЧɕɻʹ',
            'categories': [
                'configuration',
                'access-restriction',
                'network',
                'invalid-user-action',
                'file',
                'network',
                'invalid-user-action',
                'invalid-user-action',
                'access-restriction',
                'network',
            ],
            'source': '\x8f,ˢɞǌȬҝҰ\\Щŵι˸ҺʮŕäǊҩ7ţă²\u038dʉɡŻϮƃԙ',
            'corrective_action': {
                'catalog': 'Ӌȏ\x9b˻ʬŬƎɚªȎʇǱʬqβBɳДYɷȗǈˊ.ѐƱɸӫо,',
                'message': '\x80σаȆoGƸÄчйɥӢý˘Ѯ҈кTÚ]ҪɄϲʌíƺǳÛP˖',
                'arguments': [
                    {
                            'name': '˺ĺ\u038bƀѫ\x83˱ƁǓƎǗ˩ƩȆ{ӶƉŌ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ǳŜȗө˞\x8eҦ\x81ҨɨçхҔĽ2ɂ}ҍӦ3ƈñȧļ=½ˍƋƜě',
                                    },
                        },
                    {
                            'name': 'ѻÞǜҪģF˵Γˈ˗ѴƫêĽоӳÒϳҠ!˷',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210209:222904.987624:+0000',
                                    },
                        },
                    {
                            'name': 'ìŦĻȮ˙Ѕ˶Ǝ-ҡŵʵҙʹ,',
                            'value': {
                                        '^': 'float',
                                        '$': 642308.008345651,
                                    },
                        },
                    {
                            'name': 'ǘĚ˯ƼŜRŬʸҏ˗З\u038bʬǣЭãБϺº',
                            'value': {
                                        '^': 'int',
                                        '$': -4932657244721289040,
                                    },
                        },
                    {
                            'name': 'ĲƗҪɽћĻѴϤЄØы\x8ao',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        61974353230311303,
                                                        -8491657251590011468,
                                                        7951294949548546138,
                                                        -1625634344112855310,
                                                    ],
                                    },
                        },
                    {
                            'name': "Ɓϐā'ӞȑπжѬҎƱÃ˭Ə(ѱ˧",
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -2257018142016833164,
                                                        -8343322533754311627,
                                                        -6842732887516313014,
                                                        1672791827442199946,
                                                        7872218073117854964,
                                                        790969609184088829,
                                                        514777467238116169,
                                                        -732552657011797868,
                                                        3730953826241741972,
                                                        1926010808506152856,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǎŧīҀŞǲÛÕ*ВģʱіΥľLωԭZàƱʬ',
                            'value': {
                                        '^': 'string',
                                        '$': '3ŋòǁÁĒǖӡñŔԢ¶ѕļԛЩ˃ÔŽуκȿȭǜzЎұèʞȀ',
                                    },
                        },
                    {
                            'name': 'ѽǠǗŁԐſóІсØϢːɡʏэ\u0379ԟlΜӌԜͱƑˊU±@ҮЅī',
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
                    {
                            'name': 'ɕҞ\x81ǰƗһóͽ:ІʊϲҲȮ(',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210209:222904.988944:+0000',
                                    },
                        },
                    {
                            'name': 'ˤřƳ˜˖Ĭġǉүҭ-ǡļƽɝ˓ǘͽεˊ˽ə˄þơȀþǮ;l',
                            'value': {
                                        '^': 'string',
                                        '$': 'ZǼ\x93ĝʾҀ\x88ΠѕŞ;ΎɭφǀĄ;ǟȘʬȴԉ½ȯÉ˺ΑEƝ˹',
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'Êœϖÿûá˰ҟΧƗˬҜŐ/Ȯǿѣːʽϫ˯ιȄбʷȽʢ˝Ģɽ',
                'message': 'ƒʖΝӟǪDɓ҈ӷɩΌǡąϾʨʞɶȹ¬Oʆʋ±ĦκƊƆƇцԤ',
                'arguments': [
                    {
                            'name': '˛įː5ÖȅXƟʜɩtǑ\x80ɩķ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210209:222905.001741:+0000',
                                    },
                        },
                    {
                            'name': '§ɋȞ\x86ԑҿ1˜ǅƏɩк.øąθӇϺĲ˧ʦʍԚљĹȤȏů˃ч',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        '}ǳƤȫƞ˄ΞňìʑΰҴΈǁĊěǝɯɍέȡ®ƐìˉǰˎҐəǇ',
                                                        'Ɗвȏ¡ǍˍD˺ӇƙϚëÅɥи¸ȱɨʴαȔÞǰ×ѷϋӻʌºѼ',
                                                        'ѴҎʌϾ\x90\x97ά}ˡ˻Ԭ¿ϖʠцɊҚʗʋΦЋǃӤȓȆ˄ÇǢ+ɬ',
                                                        'ɰĤɶҫӖӳͼӑоˉЫӶςɀΤzԪӗ\u03a2āȧłӫ˵ªϔþlІʡ',
                                                        '˽ϾԭԪ+KɔоɅӚ\x88ƀƶΨʡԓ\x96ԛÐ\\ҲҹʭηłĈ8Ȧőɭ',
                                                        'Ŋēάƪύǜlαӎ˰\x99ȂͼϳħƳȀѲϷÕӷҒʋҼŉʓ¡Ӛɟʘ',
                                                        'ōΞŽˁӼƫҁϣķń*ӯeѺіʿԃţΎԈӯƮΛΓ˺ĄÙ\x94ɺe',
                                                        'ɰɥΊʒ\u0378GЅЛƿЄ¦ӟʗʮÆϹҖ˶ΨѲҴɚ\x98ϤЭµȪΏЈӘ',
                                                        'ˎȋŗѸҏΥȝϸǾǒÝčѦŧѧӂʻ@СͿϘӜˤԐɦōǔѩŔӲ',
                                                        'Ҭ˂ѣИΈŃMѤΎx©\u0379ΪUʹ;ɺȌќϣŔɨˣѠѤǼˢѼƅԨ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'έǈʻĚ¥O\x81ºϿˢАӔǳԏ˔ăԒΞȻŷʡԉɠħʫƕ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': '?ҵƕƬ±VʦѨʹʶԞʵэЧɜĨʠԑǠʐȈ*ȷv]Ҫӆńңк',
                            'value': {
                                        '^': 'string',
                                        '$': 'J@Ȝӹ˱ЊȩΉûğҘϚɳзҏǜӬБ¯ӉĦҋҜж\x99ȒʟüʑǢ',
                                    },
                        },
                    {
                            'name': '%kɩËźƩȔ¶Р#ê˝µВԥƎ¸ÙƐʉćŒʞҧЉҟĠ',
                            'value': {
                                        '^': 'float',
                                        '$': 674487.5377421527,
                                    },
                        },
                    {
                            'name': '˗×ɩďӕхЃȥ*іśφ˫΄|8бúÇͲ\u0378¦¤\x81ƒ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210209:222905.002919:+0000',
                                    },
                        },
                    {
                            'name': 'ύŒŹʁԁǡęҌΜʜ\x9aҸԡǹ',
                            'value': {
                                        '^': 'float',
                                        '$': 21773.461748573507,
                                    },
                        },
                    {
                            'name': 'Ɂϴ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210209:222905.003194:+0000',
                                    },
                        },
                    {
                            'name': 'ѤʂCɥ\u038dӼĈˁθϪНΨѪšĺИTΨǦȰΫŉǕŞ',
                            'value': {
                                        '^': 'float',
                                        '$': 970317.8670733857,
                                    },
                        },
                    {
                            'name': 'ɽĒǛ˘ɗ˺ψˎŀŸЇȈӜȐƸƲ\x86ʏŚ5ӷжϔϼ\x93ȝćƂġљ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ǗǵԥҺ\u038bğʤҽƸЮʷԮЎғİɚȡν©ɭʤwрǗɉŵǢ\x7fϫӤ',
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ƟӦÚʰĻ',

            'categories': [
                'network',
            ],

            'error_message': {
                'catalog': 'ǯ˲',
                'message': 'ж',
            },

        },
    ),
]


class RegisterTranslationFailedEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationFailedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_TRANSLATION_FAILED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisterTranslationFailedEvent.parse_data(test_data)
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
        for test_name, test_data in REGISTER_TRANSLATION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisterTranslationFailedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTER_TRANSLATION_FAILED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='RegisterTranslationFailedEvent'),
            ),

        ),
    ),

]


REGISTER_TRANSLATION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'error': {
                'identifier': 'ӴӞǗƙӰI«U\x9c҉ѻ´0ШTѝˉӮʚ˔ΩΝǯȈη\x9cʾәЪʾ',
                'categories': [
                    'access-restriction',
                    'access-restriction',
                    'os',
                    'internal',
                    'configuration',
                    'internal',
                    'os',
                    'file',
                    'file',
                    'os',
                ],
                'source': 'ԅѴŚ9Ҵ˖żʦͼИÁɞΝĕÁưЍȀ)˻ȍҥˌʾԅ-ʩĝǩǀ',
                'corrective_action': {
                    'catalog': 'ɒ2Ԗӆ{núfҼðɳѠлҳ<ŔŞҎΧȢӳуǍ\x98²єʫԮőˋ',
                    'message': 'ȢȅӃƑɇɭ˜АÎ˒Jˋ\x85ԁӽ\u0383ҾÐ¬ÂʕÂġʊѷҖ\u038dǰϚϮ',
                    'arguments': [
                            {
                                        'name': 'őĖ,uÅəˢǆȑǘϒ҆Ǣ\x87ϧĝńȽţҠӁѦĎӨѼұΕԚЅΰ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'èφςĵɎǂĶΪψӱŊ\x84АȐшäġaŠöӌÈǖV΅\u0379ĀĠŖԞ',
                                                    },
                                    },
                            {
                                        'name': 'νõ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 868104.7666429961,
                                                    },
                                    },
                            {
                                        'name': 'ÊƙɥļɅȄΝѽċɎĭӆҾ$Їʏ+ȳ¹ƱȔq\u038dүΤǜǱӮӶţ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3327569731016722047,
                                                                            7480028207361258927,
                                                                            -2325558611342959488,
                                                                            -8201170200232808257,
                                                                            137588632415435014,
                                                                            4872246398253940056,
                                                                            351332153148977235,
                                                                            558779622143841961,
                                                                            2019400372078607562,
                                                                            -4600549545835329386,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѳ]ǣԃε\u0381ƘҘǽџįĹť҆ԁ½ȱͰé¸ʎȌÇUԞɂДφƧǷ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɟѸӑϓҧѡuèʓɫĺϘqɬŒЌӥŜӓ˭Ś\\îӰσɓǣǒvȪ',
                                                    },
                                    },
                            {
                                        'name': 'ȢəȟҲǳĐïɜɂŌащ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ќϔξ^Ďѽџ˕ćɌГɝӌɢԗ҂ƥƘПѕюȝǊʟ¡εɏԗƞπ',
                                                    },
                                    },
                            {
                                        'name': 'ɝҘȤͲÇƤȴŶԍҊ/Ȗ¬ЊЀЅɾ\x98Ә½ңŐʂϢˆaʣùøƲ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƿ\x9a¤ԢƩʹʻӧÀсԃĞÞIÕϾ\u0378ӒYºſϢƱǇkœԔϱҊç',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ǖʄѿӆJĵҥʁҍɛӒf7Ƶūμ°ȎǓěɪKőВĖƢ˦ǧąɖ',
                    'message': 'ȭſӌ˃ñСɫԐȚÙεŝŶĀĖƵmȥӳɄΪЋӂƘӎƧɦ&ӹѷ',
                    'arguments': [
                            {
                                        'name': 'ͼȴˣȳŦǋҋțǷϮ\x96˶>ΓоƄёȭśɄ\x83мǩӬӈΖėΙεɗ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x9aҬц·оцŷӫĒоМЇũʦӻǟvοЄɀġƓʬҐӑȸi˭\x95Ө',
                                                                            'ȕˇ˭ǇŗЛԏӍάҺțĽϛфԠžˎʳӈήſƹąѦȁȶǽʆηΚ',
                                                                            '|_ǣӆȰáɊϰ҂fʻʿ*ҳӝrʛMƷ7ϩӝ\x86ʒȜʐɁÚһɅ',
                                                                            'ƒǄǟȡΠкŖʛˎ\x8e¾ӾsϹʎ˂ŽÌ,ӔǶȑĳƨðȳ˘ǐzԨ',
                                                                            'ŐɅȡƛ\u038bğҍʈ˴ҫÃˁԘƀ\x80ЫƂԕϷǔӒ\x82Ͳё\u038bѬȻ˺ɣƕ',
                                                                            'ϡοԑԘȪгŭȵŨʥĘŵάϬĸΎLчʃџÚǱκĉ\xa0ö˧Ӊť9',
                                                                            'ϔȅʃʚΖ~ȮɌļϸЃůԬĄ϶ήѾȿј˖`ɷľ˥˯Ԛɬӈ˅ϔ',
                                                                            '˩˽ҍҴͳҔƤȨЬŜţȉ\x8cĤƄϳΞ\x91˧ſ³ӈΉҎðΏΫҷƂÑ',
                                                                            'ØǰѝǎȃĻφ\x82yˉ¶ǕĳǂԀСǧΔKҏɼĺΎĖŞɋƫɓCω',
                                                                            'ΑςďБӡqĎuŉȨɑӉ˷ʪƫԜÏѵʙŶƛϡԢȖ4ƛ*Ȅɇŋ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĐПЩϙӭŽӱǙìO˳ŃӑЬӗǔΤ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȡùņѵ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɒƢУ@<˴ʟѧ&АʩΡȋӋƴːӼƳÿɔf \x86ǳŒüf¾Ϩɦ',
                                                    },
                                    },
                            {
                                        'name': 'ӳĲǌɳɯԏ\x85ȷ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8360817237304737616,
                                                    },
                                    },
                            {
                                        'name': 'ЯӁɋʑʥƝÆt',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǁƱԋʏǡɩǥȤ\x97ʶÀƍȖт¡ʅăɰɄ÷ԃēϚ|ýԇĎkΫď',
                                                    },
                                    },
                            {
                                        'name': 'ʀ˰҉ÙÖȟǠɴԄʴɔʈщŵ˶ċƊ©ҖƯу',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            524594.4189983199,
                                                                            138395.4015118474,
                                                                            -31571.41700847588,
                                                                            20830.744936724834,
                                                                            -36331.99223757231,
                                                                            730012.6913190756,
                                                                            -26900.78439530007,
                                                                            866168.2778064334,
                                                                            884867.4508853673,
                                                                            248242.82986794744,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɰĨƝɛäλԥĂΌ˝Ӏ˾őľȸFϋɡȔ=ʭ҉ɉʻ&υƂ\x88ȆЖ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '˥ƗϐǼȰяˠƑёϣŐʁ˻Đόɞ:íqι˕Ҽùǎ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ŷΩΚϋĬú\u0383',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '|?ŸǈБϊӿŢԬþҐ\x81Δ҄ɂЯҼǻėϷДΟǩɯ\x92˥юϽӏ¦',
                                                    },
                                    },
                            {
                                        'name': 'GȮĥ4ʲěʥŒ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4918649343389417544,
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
                'identifier': '¾ȉϓȉü',
                'categories': [
                    'internal',
                ],
                'error_message': {
                    'catalog': 'Ԗţ',
                    'message': 'ʭ',
                },
            },

        },
    ),
]


class SetLocaleEventTest(unittest.TestCase):
    """
    Tests for SetLocaleEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_LOCALE_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.SetLocaleEvent.parse_data(test_data)
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
        for test_name, test_data in SET_LOCALE_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.SetLocaleEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_LOCALE_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='locale_code', name='SetLocaleEvent'),
            ),

        ),
    ),

]


SET_LOCALE_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'locale_code': 'чɻ˵gȕ\x8aԉβ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'μ',

        },
    ),
]


class RegisteredTranslationCatalogTest(unittest.TestCase):
    """
    Tests for RegisteredTranslationCatalog
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTERED_TRANSLATION_CATALOG_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisteredTranslationCatalog.parse_data(test_data)
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
        for test_name, test_data in REGISTERED_TRANSLATION_CATALOG_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisteredTranslationCatalog.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTERED_TRANSLATION_CATALOG_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='catalog_name', name='RegisteredTranslationCatalog'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='locale_codes', name='RegisteredTranslationCatalog'),
            ),

        ),
    ),

]


REGISTERED_TRANSLATION_CATALOG_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'catalog_name': 'ųɿ[\x94ēʩɮӽχ0ɦǤɡ˖ȯԪ]rñңԤЕΨŜǌǛБцʠž',
            'locale_codes': [
                'òщʌϢԞǁԢүε',
                'ұ.ЃӁŲҾ',
                '˚˽ʛǂyϾ',
                'лƺȫԧȕүɜǞĄ',
                'єАΤӹϪЖǿɳ',
                'Ӹɀʘ®m',
                'ĮӻȢ',
                'ӓƕĳèʘǍêϨ',
                'Ҽ\x8dȺ',
                'KʛѲwʬǷÁΐ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog_name': 'ҨԢԗ',

            'locale_codes': [
            ],

        },
    ),
]


class TranslationsStateTest(unittest.TestCase):
    """
    Tests for TranslationsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in TRANSLATIONS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.TranslationsState.parse_data(test_data)
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
        for test_name, test_data in TRANSLATIONS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.TranslationsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


TRANSLATIONS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='catalogs', name='TranslationsState'),
            ),

        ),
    ),

]


TRANSLATIONS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'catalogs': [
                {
                    'catalog_name': 'уΙtȷǯ7Ϳғ~ǻʃɬҽΠ¸ͰŤɸIƮƼѪ\u0378ƋUňҚӃС^',
                    'locale_codes': [
                            'ȎҫХ7Ǉ',
                            'ĊǀӚY',
                            'ɅΐɂŏЁѲ',
                            '˹ɒˮѩŉȤј',
                            'ȯ¯',
                            'ǸaǸәɗ˖іԙ',
                            'i˛˺ʺŘΎ',
                            'ǭѨõĻ:я',
                            '˥Ǎ',
                            'ґҗɷʾһΙ',
                        ],
                },
                {
                    'catalog_name': 'ʻϕʠčҊ)ʍΆдЪӊԉΑȭѾɪΎϦƾ_ԆSϧƲȽԙў\x83ȏȥ',
                    'locale_codes': [
                            '҆',
                            'â˥',
                            'ϵƷʞėă',
                            'ѢÈ·Ѹ',
                            '˻˄ζȨ',
                            'ɞ\x8ft',
                            'Ǚē\x9dTĭƝǉҶƞө',
                            'ˈǬƗɸў',
                            'Ѵəπ',
                            'ӥѐǋ˞',
                        ],
                },
                {
                    'catalog_name': 'ƜѪƞȇӓ˼˙ǧӝϝŘϬΪėʄƱ\x8b҃ǣώѐďįƍʆ\x8fƿ«ѕ\x98',
                    'locale_codes': [
                            'Ѕ\\pǁϴóŗ˗ƿ',
                            'ԡÊǶΨƸŊʽυ',
                            'ӂ',
                            'ґЩ',
                            '\x80ϲοǠԪЙ',
                            'Ϯě,ÿƣŐԒƻɺɛ',
                            'ÇҎҋ',
                            'Ëӫћ͵ÀΘŷάЄ',
                            'ʅƣ',
                            'ˋŰą',
                        ],
                },
                {
                    'catalog_name': 'EʱʓǶʘȯ;ȌĝŃͽƒʦĠӰĀҵЏ¸\x93ѷɧзOʹɖΉ¶ȕѐ',
                    'locale_codes': [
                            'лȇʠɗ6\xadԕˏ',
                            'ӔҏзҲǍÔlѺʳ',
                            '˰ˀʓӣƇǭ',
                            'ұɳϠƨ\x84ԛ',
                            '˕á_Р',
                            'Ϩ΅ǄχĿɮЂǖ',
                            'śYʳпŎʓϳӓӛʤ',
                            'ΟļĒķ҈ϔ¶ЦW',
                            'ôIl/ы\x90¸ĸζů',
                            'Ѻ',
                        ],
                },
                {
                    'catalog_name': 'ÎūϿƱЍμĐǊώԈƐҩ\u0382ʴ\x96ŲǹpȪŽÃŻοń˽ĆǰʚӨΕ',
                    'locale_codes': [
                            'ń,ѳȇ˖Ɉ',
                            'ΌÛȯĳŊ1',
                            'ҬγüԠÞƜǛ',
                            'Ͼ',
                            'ΝɌҮ2ħщ{Ʌ',
                            'ɈѪ',
                            '\x99',
                            'ɨȲ',
                            'kˢΗ\x81Ԕϯ',
                            'ȥ0ҥŭѡϽȕƾˬΗ',
                        ],
                },
                {
                    'catalog_name': 'ʂŉеЇƼSϊҔˡɿʽªж~\xa0˓єbɖäūɺǰßԚԎͷɒșĸ',
                    'locale_codes': [
                            'ϸMŚȹ',
                            'ӊ',
                            'ųŸ\xadȜ˂Īϐ˰£',
                            'ЧúĄӴǕЧј\x86Σˣ',
                            'ɱӍQ:ĳ˪Γ',
                            'CӶ¨ӵɲϷƑ',
                            'ȪԮѐĥӆ϶ΩʡƴǸ',
                            'λɩҵȷ˘',
                            'ɛ',
                            'âɲӄÉéҎĀűŋ',
                        ],
                },
                {
                    'catalog_name': 'Ƌ\u038bƽТǘҰϕøɽƫʇҐо~Ⱦ\x8eҬƦӜ8\x97жɲćɈȫȜʧwĩ',
                    'locale_codes': [
                            'Àń6ɾ',
                            'hƬӭϸ',
                            'ƎoϮпшёĐԂОӄ',
                            'Ħϼǯɩї0',
                            'ǅΧ\x81ƴȣ҈ēĐ',
                            'ҦЅŅȦ˙ȜÔó',
                            ')Đǹ',
                            'ƁÝԋѦ«ƏҺǁ',
                            'ӫ',
                            'кĘ',
                        ],
                },
                {
                    'catalog_name': 'ԈҖƫūУƘiƁÔѾũŗɂƅƍʃɽȐöΌӔғγҗ\x84ÖȎЦȓ˒',
                    'locale_codes': [
                            'ƐτñѝЇ',
                            'ҷͽƉɈЙǣ',
                            'ǥƞԩ˪ˌѝʐ{Ā',
                            'ϛ',
                            'ɯʍ˶RήңӋƯӕ\x85',
                            'ŘҥσˆюŽÝ',
                            'ѰԦ',
                            'Ҋ',
                            'ϘήӮůƙȅ',
                            'ó',
                        ],
                },
                {
                    'catalog_name': 'ɢɚwɊ\x91ǺӟǛƵϥʍǛј˸эȟŤȸʏӡϧƦ˽θǿũ.ɾ\x9aф',
                    'locale_codes': [
                            'ÜϽǇҳ',
                            'ǞѹÈѹмψ?Пʚȴ',
                            'ŦYhĖ©ӏó¨',
                            'ӆќǶҸǚɅȸȾ',
                            'ɷƝϘƌˀǲ\x8a\x90Ψ',
                            'ŬÞýӵ',
                            '\u038bʕƩˡ"',
                            'Ǥ=ʪӑŶʚʘƱ',
                            'ҘǡȥΖ',
                            'ȓϔБɍ',
                        ],
                },
                {
                    'catalog_name': 'ˉЪˑĂѫȯɃȑɎĭ˴ŢϙѠƳŗҦʉɛƖѷƆǔńʾѬ\x91sɯѲ',
                    'locale_codes': [
                            'ĈʱϱʗƑXuпΑѠ',
                            'ĖϬľԠˢҍŠқɼˡ',
                            'çѲ ҢѨ',
                            'ԜýҕƝҝ[ʸƅ\x84ѻ',
                            'çӄô"ѐ',
                            'ʒ',
                            'м?Ùс',
                            'ɧЭǗǅJ',
                            'ēΉǐ',
                            'фѪĳͽγ\u0378ӗ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalogs': [
            ],

        },
    ),
]


class LocalesTest(unittest.TestCase):
    """
    Tests for Locales
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOCALES_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.Locales.parse_data(test_data)
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
        for test_name, test_data in LOCALES_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.Locales.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOCALES_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='Locales'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='code', name='Locales'),
            ),

        ),
    ),

]


LOCALES_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'Ȧ\x80ŧǄȧҋǀε\u038b˥΄ώΧȡ\x8dʱĖӭòŀȓƊӉҀŘʮǌΨņͲ',
            'code': 'q\x8b\x98ĺǚ!ʑ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ĥ',

            'code': 'Σ',

        },
    ),
]


class LocalesStateTest(unittest.TestCase):
    """
    Tests for LocalesState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOCALES_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.LocalesState.parse_data(test_data)
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
        for test_name, test_data in LOCALES_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.LocalesState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOCALES_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='locales', name='LocalesState'),
            ),

        ),
    ),

]


LOCALES_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'locales': [
                {
                    'name': 'ѣөçÐǭq1ú\u0383βċ˛҈ӭ|ЏϳsӧʙλȺŶĲɬĵϮщ\x7fЋ',
                    'code': '/"-Єљ',
                },
                {
                    'name': 'ЍԤʆӝŗŒƨƜ\x92пййЮ',
                    'code': 'yԅӮΡ˝Ŀ',
                },
                {
                    'name': 'ͷœ±ÎȘŚЄZɢÑμҪʴŽСāθҬǽҀƞȟŐʲD\x89ğȒĮƓ',
                    'code': 'Ĳ',
                },
                {
                    'name': 'lҘаúӿØɂΡŌäʉɮƃӾ˭˪КɫƞуϦʞÍĐǘϖĒƿȬĽ',
                    'code': 'ȾЄ',
                },
                {
                    'name': 'ƱӕŚҳŔЯϝϗɃӉӝ\u038bʷʹΆӆô·Îϻѣʚˉgʲԍ\x7fȜˇĢ',
                    'code': 'ѽȹrȝˌȓ\x8cȫĭŞ',
                },
                {
                    'name': 'ȒЌ',
                    'code': 'ɺѸϝң',
                },
                {
                    'name': '9ǣʘЗōӂΐтŅȲ÷`ΜЇҜΒʒʊɸHԋɣıδҊȦϯё¶ɹ',
                    'code': '<ĴԗȗЅś',
                },
                {
                    'name': 'гƹȝL\x81еtŒĲѴɣϢzʉȈОˏӶƟ\x8d,҃ĭĿìѰЎǮЍǎ',
                    'code': 'ʣaʩҸɈȹʴȗµd',
                },
                {
                    'name': '\x8cªĘÍΊyӌ1ξʃӿԍΌʨΐ˃3ŞѯǈԫÝƸϹȍɤӸϟԋ\u0379',
                    'code': 'NӦĈƉ.ξԝƳΪ',
                },
                {
                    'name': 'ԥӒӉњӑƐκjΣɓχ˓ʴÒjĖ(ÏΠЕŷÖȗҥЀԤî\x81Óә',
                    'code': 'ʣϟП*úΣ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locales': [
            ],

        },
    ),
]


class ActiveLocaleStateTest(unittest.TestCase):
    """
    Tests for ActiveLocaleState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ACTIVE_LOCALE_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.ActiveLocaleState.parse_data(test_data)
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
        for test_name, test_data in ACTIVE_LOCALE_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.ActiveLocaleState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ACTIVE_LOCALE_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='locale_code', name='ActiveLocaleState'),
            ),

        ),
    ),

]


ACTIVE_LOCALE_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'locale_code': '˩Àщΰ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ˤ',

        },
    ),
]
