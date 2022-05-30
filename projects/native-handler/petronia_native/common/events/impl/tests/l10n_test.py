# GENERATED CODE - DO NOT MODIFY

"""
Tests for the l10n module.
Extension petronia.core.api.native.l10n, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import l10n


class RegisterTranslationEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_TRANSLATION_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = l10n.RegisterTranslationEvent.parse_data(test_data)
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
                res = l10n.RegisterTranslationEvent.parse_data(test_data)
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
            'locale_code': 'ɀȖɔȡӾ͵Ť',
            'catalog_name': '%ҟϛǦԞЦάˆ˓,þӁӚŒdЁѕŷу҆Ȉø¤pƦ˪ǧ;ʾχ',
            'message_file': 'ϋţӒcɌƟŴ΅đ\x86ɶ×ǎӓķЬ\x8cƆϦ˥MϵǌЧϼϻ͵ǁˊ\xad',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ΰ',

            'catalog_name': 'ϸʾƳ',

            'message_file': 'ĚĐ',

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
                res = l10n.RegisterTranslationSuccessEvent.parse_data(test_data)
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
                res = l10n.MessageArgumentValue.parse_data(test_data)
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
                res = l10n.MessageArgumentValue.parse_data(test_data)
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
            '$': 'ǖrȒʦѷЕʲʽϖǘА˽ϿğÊΎҫόʕʄʛfʜ}źŬОΣªƒ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 7786821836456440418,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 249101.6119630956,
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
            '$': '20220530:170406.689611:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'îԋzƙщ\x93sƌńźΙƛdҤӭͽ˗ϸ¢\x8aұ©)\x99\u0383Ҝϻȣϴʀ',
                'ˌҔ(мҜƥӧƽ҆ΞǼԌȶɄ¼ҋʁʝʬџƶӧXÀσԎÙӃǫǿ',
                'Ȍîƍƅ(ÏǕԊҕҿǻĀтǫξӺԉΘνŘƧɝјҪǛɱéɺнѻ',
                'п¢ƷĎ°¸Ʈǜ¬}Ϫɋȣˇҽ>ơSьʕҳԣѓʗ;ϲÕάĠ\x8a',
                '\x95ϋʔϊKĘĕҞΰȁҶǨͽӏʬҧȝɟʐ%хVԟKˉ4jˡǣ¶',
                '³Ș˪ōв*ҽԠђɏѰІʔC\x88ǉwƀшʢȘϤȤЄǕў\x94ЅҘ˧',
                'Ǧϴ®ȚXŮҚҵùӕwżȅѸѮ\x7fȭ\x89јԋĆŎΒ˹ОɟԀҞëʒ',
                'Д˅оÉƒнƊӠÕÿϣΫї˦ıƑϚƮɶ<ҰĢ˰Ɛѣǧ˺Ȋ:ӣ',
                'ǯʲĐӎȝдɼ\x94ĨтʟҍΛɈƤԔѣЌПǩˣɂʚˉƣЇʸǮǩʵ',
                '¬қʙɠџҪŠˏβњЀϙӺӸζԭŋxЧˆ˗òŊäŶȩĐӪѢġ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -8320696870068395975,
                7134586336617256413,
                -4117257054077529143,
                2327657781151649791,
                -3583869027264327501,
                -2012232915306471657,
                -7713240407677828781,
                1117143694863131186,
                4846242168945499189,
                8627810795858159194,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                12698.153700680108,
                75620.74942203652,
                593526.0232405373,
                323154.9848911461,
                702031.2708458796,
                183272.20009839057,
                237423.54627740942,
                544503.4074509953,
                522729.0774348738,
                -58433.06618493527,
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
                True,
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
                '20220530:170406.694708:+0000',
                '20220530:170406.694800:+0000',
                '20220530:170406.694890:+0000',
                '20220530:170406.694979:+0000',
                '20220530:170406.695068:+0000',
                '20220530:170406.695156:+0000',
                '20220530:170406.695245:+0000',
                '20220530:170406.695339:+0000',
                '20220530:170406.695427:+0000',
                '20220530:170406.695516:+0000',
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
                res = l10n.MessageArgument.parse_data(test_data)
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
                res = l10n.MessageArgument.parse_data(test_data)
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
            'name': 'зmɓÒƧë½áùӾòˊ·ɣÑɒßĶʚÌīʽɗӤϠԏũʿÙγ',
            'value': {
                '^': 'int_list',
                '$': [
                    4833423143490192846,
                    1487485867973203112,
                    5487660967677581836,
                    8973796065505597431,
                    7304203134700011213,
                    -7362759859004841978,
                    -8806667210487539710,
                    4814755182603517497,
                    3138356697627963433,
                    -444339915582112468,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ɣ',

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
                res = l10n.LocalizableMessage.parse_data(test_data)
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
                res = l10n.LocalizableMessage.parse_data(test_data)
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
            'catalog': 'ãѡƭϨИǫѴ[ӥ҆Þ\x96Σ\u0379»όɶҙŏԇıǂ¸ΑǤңƠȉѹϗ',
            'message': 'ϱȥϓĶӓЪй϶ɉ\x8eӧөÕϲΔ%ХЂӓόӡˀԂŭƢǆńϘƤһ',
            'arguments': [
                {
                    'name': 'ɂģϧӤkȬʴ4ƾуʕҧϿӑƩʣ\u0379ӆƒԤ}ƳʜиǓɾ\x8d˛\x96˴',
                    'value': {
                            '^': 'datetime',
                            '$': '20220530:170406.681421:+0000',
                        },
                },
                {
                    'name': 'ʵǎʲԋӞɕˊ\u03a2κɍӴ´ªwıϙʗÑ˝\x9aǚΝҢ,àɃ\u038bƊҟ/',
                    'value': {
                            '^': 'float',
                            '$': 763638.2251947492,
                        },
                },
                {
                    'name': 'ҰΈöɦʅϷɨĥɠʕβƛŽǙ\x83\x82ų',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        6440366092035474234,
                                        8382440163798121891,
                                        -3367343705318555418,
                                        1028939594040328515,
                                        596461532972992813,
                                        7911687789417526388,
                                        -9045841559445898432,
                                        4631745290549516226,
                                        5577934040983714852,
                                        -5262649637912193905,
                                    ],
                        },
                },
                {
                    'name': 'ʁɖµ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20220530:170406.683517:+0000',
                                        '20220530:170406.683604:+0000',
                                        '20220530:170406.683688:+0000',
                                        '20220530:170406.683772:+0000',
                                        '20220530:170406.683854:+0000',
                                        '20220530:170406.683937:+0000',
                                        '20220530:170406.684020:+0000',
                                        '20220530:170406.684103:+0000',
                                        '20220530:170406.684185:+0000',
                                        '20220530:170406.684267:+0000',
                                    ],
                        },
                },
                {
                    'name': '~˚ЏǴǱǖƜԅ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        True,
                                        True,
                                        True,
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
                    'name': 'τӥȩÖԊɒɓѬKÙˤ΄ȝ)þ;ȁǸғ˴HƴҹȍōƦϏҺЛo',
                    'value': {
                            '^': 'datetime',
                            '$': '20220530:170406.686113:+0000',
                        },
                },
                {
                    'name': 'ʜƘɬˌҼʿ˂ûʟұхӟΘͶ',
                    'value': {
                            '^': 'float',
                            '$': 894142.1707215869,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ѫѕ',

            'message': 'ȳ',

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
                res = l10n.Error.parse_data(test_data)
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
                res = l10n.Error.parse_data(test_data)
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
            'identifier': 'ӾŬΜƨ\x9cī˗ůԢӔůβ\x8cѐʲ¿ǧyсŔɚӾʚʖūçŕǗҾL',
            'categories': [
                'configuration',
                'access-restriction',
                'invalid-user-action',
                'configuration',
                'network',
                'configuration',
                'network',
                'configuration',
                'network',
                'internal',
            ],
            'source': 'ǑɐźɎ,ɴȽΈͻͰɈǡȢԉʨѪJԞʐśΊļũёŶϴƔѻWƌ',
            'corrective_action': {
                'catalog': '\u0379ћԌԜ\x89ö#λ\x87ҰΉȠҪќпͷȯƛԜŤ˞ʦϿÝáҥ˙ԥкǌ',
                'message': 'ƑûɁΆΰИĬŻ\x93ưΕ=˟ӝ˯ȔªӅͿΨ¶ЩːϗȭȒӛ˲˥Ԙ',
                'arguments': [
                    {
                            'name': 'Ӡʀ\x94Ȗʼ҅ȗʘÈχ^ɷҲҕəŲƟɛѹŦƺԋѵѕǤƂфӞ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        445821.22100341844,
                                                        659794.5529587528,
                                                        92208.42852417714,
                                                        34766.44730760998,
                                                        290955.97118659096,
                                                        526020.7294526086,
                                                        -87761.37727679223,
                                                        954934.3148497844,
                                                        707508.5250880264,
                                                        503432.1859449287,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ŠБӳȼſ¤\u0381Οî˨ǓѭʑЯə¢êЬ҇ɴĭǾԊ\x81Ʋдâѡɥǚ',
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
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ҙ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        False,
                                                        False,
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
                            'name': 'ʑ)űҎΞ,Ǒˤиǔ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        '\u0382ђĒ\x84υŰ˕Υʼ\x8cãnƖЋӮќɏþ˼wԮҶ\x8eɐΜčγЪņе',
                                                        'ÆҎӛłuĎŃϧµѬfɕßƌgχɁ"§ç\x94Ɓɾχ±ǫĲƉȜι',
                                                        'ǹԞԙшɁġÕ҃)ƿŕӎƔҨ҄ϥƎGHы¤ȜЯ҈ĖʥԬҁԍ§',
                                                        'ҀȤDМЮΟІɄӽǽԖӞʯӡĆÎϼɈś;ǦȕŧɴԔʈрǑˋǥ',
                                                        'žÇǻњʒнνΌȳԇ˾ӳăȯӏ[˵ѾϲɔņœȄҝGȶԊԉɓǈ',
                                                        'zҲŃҡɥǾ=\x91Ɨ˾Ӊ\x85ëПɽлѿԏʳhȑÐȇҌИϐЪěǹϝ',
                                                        'CƪǩJдЃΪLō$ΉȇEƸǤȗʉҠȟŉƧɝ˦ě¾ʰѣ˘чț',
                                                        '\x80Ө˸ǻ˦қТƫѸ\u0380΅ÒúѼѡvӝҰӫѬϸŀÖDѳųѽϷ(˜',
                                                        'Ͽŷʠєæз˸ɖÍřʮѺ˂ΝĈҟʮȉȧԝóīѲӧˤԜŜҌȗǒ',
                                                        'æŬɶJΆΠǟκλŮӅ˧ӶЋ¨ȎĔ\x93Ѯ¨čQйĲӪŤԐƷɳș',
                                                    ],
                                    },
                        },
                    {
                            'name': 'тsʱĤԋ\x84ÉɕɀgғˍȯӺнЂԫϷςυ±ΦȊȿĂɻӣßuĮ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ʀƧR˽ҬԭΡʨǋѪǬɹŀýÖɘıүƩǮ<|ǂԏ§WE/Ǝү',
                                    },
                        },
                    {
                            'name': 'SŪʖԜξKҞčȎΐƚʘȺ˵ЕсȻԔӖϊÞˎɉ϶6ЁϾĘԬ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        True,
                                                        False,
                                                        True,
                                                        False,
                                                        False,
                                                        True,
                                                        False,
                                                        False,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ùʵŔд˹ѓ«ǖɊӚǈεӿӿƊԓĒśȫőʝ\x8a˲Ͼ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220530:170406.676029:+0000',
                                                        '20220530:170406.676114:+0000',
                                                        '20220530:170406.676195:+0000',
                                                        '20220530:170406.676274:+0000',
                                                        '20220530:170406.676353:+0000',
                                                        '20220530:170406.676432:+0000',
                                                        '20220530:170406.676510:+0000',
                                                        '20220530:170406.676588:+0000',
                                                        '20220530:170406.676666:+0000',
                                                        '20220530:170406.676745:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ԭ',
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
                                                        False,
                                                        True,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʩǺԭӿɍʻʩτĭȌˊFдƬȅʽ҃T',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220530:170406.678549:+0000',
                                                        '20220530:170406.678642:+0000',
                                                        '20220530:170406.678725:+0000',
                                                        '20220530:170406.678805:+0000',
                                                        '20220530:170406.678885:+0000',
                                                        '20220530:170406.678964:+0000',
                                                        '20220530:170406.679043:+0000',
                                                        '20220530:170406.679122:+0000',
                                                        '20220530:170406.679201:+0000',
                                                        '20220530:170406.679279:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ξŠМ¾ѐ˛¤ʗіǄԛėѻЙǢĆȣͺьżɦ҃ɽӹĳʺķ˲Źʃ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220530:170406.679863:+0000',
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ʩ\x98ʠƺ\x9eĈƍԦ\u0381ɤʷɝɪ[gYk·ԕ΄ϷŀĥʜǪŔˋγëǧ',
                'message': 'ԋªʮȶҶʾʨíеƺѽӕW\x95ӑțһˤЬ×ɋĝĊҝ\x88Ϡ;Ϭ\x9dȗ',
                'arguments': [
                    {
                            'name': 'ЁæэđƢРԨɣЯĐĨʠόƷ¶?ѓˎ҉˶ʵƦѪ¿ʵˊҗѧ]ӣ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        '{ŽɑһӿěҍŎĊĒϕɯӜãͿȞȫ\x88êĉХφϔҁäΡѵ\x7fμú',
                                                        'ϩƚĖѴŧҭЎǆоĮņҾū˥ƣӾіłˑˮ˫g)ƷőԬџƅӲȩ',
                                                        'ӭRЧfҼѼɿĹЬÝҀҴ*ǥǖţĦƞʘʊΘɫƺůүɗňĆLѨ',
                                                        'ƨá϶ĭƙÔ˷Ї7\x88ӒЙϱwѳ\x8dɐȚ·ĜξèǢϸȊЇΪȳБю',
                                                        'ǂЏơł\u0382Ǘ^Ҹ˱ԝυӑΦɅԐɀàϼŇҧйȀκű\u0382ʰ\x81ѣӀY',
                                                        'ЬзϬ˫Ŷ«ːUɛѷђСʒӘȗ϶ƾʯϯǫȲҮƾɀӊʄÇҴÍƙ',
                                                        'ęхőӘЍζǝϷŞ˓ӯęЇÔҗĬϋʝȥÑȵΑѾ7ƗѓǆǑʆǮ',
                                                        'ˡĔɣŔƵ\x7fǀØѼҌÿԗԗΨdҟÌѥҊ˛ʜŢԔəʛŦԥбƯ2',
                                                        'UЊƿȏȶōҊўϧԅʔƹӆĢԭΩʑčрѿUƺԑAńƇЁʦɾЫ',
                                                        '\u0381ŷӉɕҤϱù\x80ЄͻѨUлaѸ˷їҫÅDқɾ9ҭʉǯŚΕ6\x81',
                                                    ],
                                    },
                        },
                    {
                            'name': 'fǎãǭȅʑΫЖÃǅҝҳҼďýǓϻļ²*ҀҊχʔϵë',
                            'value': {
                                        '^': 'string',
                                        '$': 'ÌĵʟÝϓɻːǞжɦѹΑ\x83ѤеƾԃșǶχНІφӔнѷŁӵĻЛ',
                                    },
                        },
                    {
                            'name': 'ДƝΡ˟Έ˓ŰˋϱÀҩϳɡäΪȦ˂Ҧmɹѩſϡɾ΄\x9aӥέ\x99ğ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        4879271564692903490,
                                                        6408674465811200724,
                                                        -3060317683128133270,
                                                        1349471394873784238,
                                                        -3997772519831244833,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ƿƯ÷ӊѓϛ\u0378¤ɲǴˈ\x96ĒЎй\x92<ԦӁ˅Ѡ˯ɪϢ˟˯ʷȾ\x88ÿ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220530:170406.699422:+0000',
                                                        '20220530:170406.699505:+0000',
                                                        '20220530:170406.699585:+0000',
                                                        '20220530:170406.699665:+0000',
                                                        '20220530:170406.699745:+0000',
                                                        '20220530:170406.699824:+0000',
                                                        '20220530:170406.699903:+0000',
                                                        '20220530:170406.699982:+0000',
                                                        '20220530:170406.700060:+0000',
                                                        '20220530:170406.700139:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'bӐ@xӉӓȹ\x83Ȱ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220530:170406.700710:+0000',
                                    },
                        },
                    {
                            'name': 'Јъ«ˁƏ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -2497374672581781309,
                                                        1102914586053907973,
                                                        6919052810006472981,
                                                        -3746370284395968700,
                                                        2332915411099039954,
                                                        3045631067931779320,
                                                        2541953748668537677,
                                                        8854463454020872070,
                                                        4871455951514697682,
                                                        -8031640600419564408,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ż2ňΏɅөȳšǷӧϾŴ@Ӭ\x99τ\x93ǒǉƠĴϴã=ѹȝҮêτҸ',
                            'value': {
                                        '^': 'int',
                                        '$': 8197054244702858570,
                                    },
                        },
                    {
                            'name': 'ͺȺњκèʁ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220530:170406.702693:+0000',
                                    },
                        },
                    {
                            'name': 'íŗʀ ЅҒȌȄѹЌθ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220530:170406.703096:+0000',
                                    },
                        },
                    {
                            'name': 'óʹƭǋKЊŏ²',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ҏԁӦȂǛ',

            'categories': [
                'file',
            ],

            'error_message': {
                'catalog': 'Ŗȩ',
                'message': 'Í',
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
                res = l10n.RegisterTranslationFailedEvent.parse_data(test_data)
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
                res = l10n.RegisterTranslationFailedEvent.parse_data(test_data)
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
                'identifier': 'σӴħΰςbʍʣɻÉLˀȫƓΥϡĤάʆ҄ǍӓчҖӣѓɝƧȕδ',
                'categories': [
                    'access-restriction',
                    'file',
                    'os',
                    'os',
                    'internal',
                    'os',
                    'configuration',
                    'os',
                    'access-restriction',
                    'configuration',
                ],
                'source': 'Ϗɼ±~ˠӴʘȶǕƉ«0φýɗΠǽȀ҉Жұ΅ŭ{ϚϕƇҙҡò',
                'corrective_action': {
                    'catalog': 'ćŪєиÐĵˠЈщ°íԩоʒɋҲѐǝҬĽÈӓ¤ņԙ+ŞȟѐƄ',
                    'message': 'țɴS×Ȧ·Αn˻ʻ\x9dɆƒҍͳɄǫȝȨǆÝ˙ĀѸЭɎÕҴ$Ő',
                    'arguments': [
                            {
                                        'name': 'ǰ˙ƶǜaǉǬΚƿÔѱÃң˩ԠġĶȭ\x99ƋƅƌĸȆġɛШԔƯġ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3221833966090933114,
                                                                            3969777580656326919,
                                                                            -7992028734720530792,
                                                                            996131951174705738,
                                                                            -2677680296095254129,
                                                                            6934454909932560617,
                                                                            -1457918119903235141,
                                                                            -9207493155162782603,
                                                                            7342598513917186058,
                                                                            845752657310494817,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ɩ½őϪ˅ʖ˧μͰƏȆҸp»ƘĬϿüĪůΧŕӻ§ӐÌʄΥ\x83ć',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4149343376409382835,
                                                                            -4454082272025162459,
                                                                            -24109774740430388,
                                                                            -3036645617359714893,
                                                                            1666229360891064854,
                                                                            8798213237595147036,
                                                                            3189546308629922949,
                                                                            -913550745251697450,
                                                                            5669880828862041165,
                                                                            -8357982535099480120,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǤƬɨʶϴbҰΑư˚ƵʲԞĽ\x99Ƹ϶ȽŭΠҰέ3ԥŰŲ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 930501.4094289624,
                                                    },
                                    },
                            {
                                        'name': 'ʯʢ˔α˲ɫȖʅśŒȺ˛ʠҐǩ\x7fžӹǋҾÕϡȱ\x81Ґς\u038d¸ŔĹ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 340238.95392143616,
                                                    },
                                    },
                            {
                                        'name': 'ȱȥȈǂçеĝˈǖʠӓˉƦΦɄ½ͲwǇɭԦǇǥƮҳcϚźϬϔ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4582800332853382350,
                                                                            -2062291771526793712,
                                                                            6858792292644524619,
                                                                            1071729106156744520,
                                                                            -3995727768174968058,
                                                                            2899140150984680067,
                                                                            -3028608207461023009,
                                                                            -6815102261642525730,
                                                                            -6215258208137478896,
                                                                            4697095327409296572,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˖ԭБˆʲ¼ȹ\x81ʃǞӕ(ΠϲіȾ¬ҡęeӺ˨ΫǕЕņľ\x84ό2',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ѱ\x86ЎӐčϘΦӼΌϡѳĿңϪǮ\x82МуśθҴ>қѰԋ½Ԗ\u03a2ΦŦ',
                                                    },
                                    },
                            {
                                        'name': 'ǫӳʚҀ¢ĦEßĥĲʦϕӓʬƉ¦ΈɖԝãҔэМwɂå˹ǲ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7292484277337453631,
                                                    },
                                    },
                            {
                                        'name': 'Ô\x7fȅӖͶ²ΆȎ˲ȅѤȊ',
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
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ή˶ʓþǓӍí\x8fˍɨȯŋ$ǌ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220530:170406.658201:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ϊ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 455937.9885748307,
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ȐСǉϙŹǼɄÁ˟Ѯ\x82ξÝEҜώȤԋʮŷǏɥϬʕȕϣ&ʏөŐ',
                    'message': 'Ӷԉ\u038dЬӠśрЍˏƞ΄˵ԒĎɉǣèƊ\x99њԉ©7ҍԭԓˑώÃǬ',
                    'arguments': [
                            {
                                        'name': 'ӗǬʻϐǗѩź)ϴóΫӎŨƑŁǎҏɢƻǭº',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            791012.6039451051,
                                                                            982880.6681775809,
                                                                            122902.88696517076,
                                                                            480223.4406389678,
                                                                            486599.82971306704,
                                                                            794746.4711970931,
                                                                            763332.7308844699,
                                                                            992587.8899347205,
                                                                            953707.862362681,
                                                                            825208.3666142063,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΰɇ˾ЅźýϬǋϲӉǺS\x97ѽ\x88hʙҥԇΚόЧӿ˜Η˟ʺϩş\u038b',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            398404642784178652,
                                                                            4228751002729408172,
                                                                            8678603327343206387,
                                                                            -643006530281697937,
                                                                            6707067826596954919,
                                                                            -2564949132507634596,
                                                                            2126481162451579130,
                                                                            -4595756721717737664,
                                                                            -7681400807876874641,
                                                                            1314000067776412735,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʷԃ¬уѿ¦˼Ӌʡ{éԐѯȂJɢφˑtɀǄϒ˪ҠИӱͰƩϐţ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Йʼ¤\u0383ǤďâəóƱ\x94ҭɸŗҿǍǐŪb?ƹѾӮ\xa0¼ӝļįЂɓ',
                                                    },
                                    },
                            {
                                        'name': 'ǋĨнɹԉ˅ΌƼΌɪԄѲˠϓ,ъĴÿſЀϏɟƒΜ«Ӱăщ˨\u03a2',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 250827.12979472982,
                                                    },
                                    },
                            {
                                        'name': 'ӱ϶иϖėϰþȣЏь5Ęʾ¦Ё',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȝŦЉӗЪʪШϯ\x8cбûʔГßӣӧјӬԪơ\x80ŠӉ$ĨІɨʵͰɠ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220530:170406.663041:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƋΪơOɼԗ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            877613.6013730085,
                                                                            239322.85370698088,
                                                                            516107.65369247575,
                                                                            339687.62503023125,
                                                                            977198.5158704461,
                                                                            957991.3388750469,
                                                                            936641.4927698388,
                                                                            999260.1266382867,
                                                                            368991.4962736216,
                                                                            791909.0021226668,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'έ\u038dӖǍ\u038dЎҌ¶έОoƴˮƽʵԝέӗ\x9cñƭàơӖЛ\x9fѸ˱ΡƔ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'lǖUuħҨ\x98ŐƟɊȁѼˍʈКάɵȩȾ˛Ѻ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 870404.8687236808,
                                                    },
                                    },
                            {
                                        'name': 'F',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            860756.1977509422,
                                                                            515394.41784204287,
                                                                            627824.97537009,
                                                                            815018.1566439655,
                                                                            520304.32074414333,
                                                                            239214.02081868454,
                                                                            295481.97521215293,
                                                                            645508.763716613,
                                                                            894497.7082233452,
                                                                            210292.77421592502,
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

            'error': {
                'identifier': 'ȭɪɫӆʼ',
                'categories': [
                    'access-restriction',
                ],
                'error_message': {
                    'catalog': 'µΣ',
                    'message': 'Ϟ',
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
                res = l10n.SetLocaleEvent.parse_data(test_data)
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
                res = l10n.SetLocaleEvent.parse_data(test_data)
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
            'locale_code': 'Pɯφ\xadίľϛ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'œ',

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
                res = l10n.RegisteredTranslationCatalog.parse_data(test_data)
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
                res = l10n.RegisteredTranslationCatalog.parse_data(test_data)
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
            'catalog_name': 'иЭоǅ\x88ǠŲ8ӐʓœŤψȚNͽȋҔĦ\u0378ŹȖµʳŸΎŵƿӝč',
            'locale_codes': [
                '¡A',
                'ÉɪŃ',
                'ȰŖʩçқΟѽ',
                'Ȣӷɸ',
                'ʇͽɤђϬҵ¨',
                'ƤѫVǨʵҷζØȼ\u0383',
                'Ұ',
                'ȇιʦǰΚ˦',
                'ǝѽ',
                'HŐƁıeˎΐʢ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog_name': 'ʐ˒Ѹ',

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
                res = l10n.TranslationsState.parse_data(test_data)
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
                res = l10n.TranslationsState.parse_data(test_data)
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
                    'catalog_name': 'ψ·\u0378ɹưǊ®ғȟϖµԫҕĨÄǏā×eԈˉ˪șГkƬϞƪӿ?',
                    'locale_codes': [
                            'ҫ:ƬŲǥʇ˾ƟΖ',
                            'Ŕϐλ',
                            'ΔɴʴкŪӟƌӡ',
                            'ʨЧʴԈǫS',
                            'aζɟϨЌ˷ʕȍ',
                            'ξĹΝЍJƘ˄ž',
                            'ǀ',
                            'ÚҴǔē',
                            'ȱ\x98ǽǞ°ԛʤ#»ϛ',
                            'ȶ',
                        ],
                },
                {
                    'catalog_name': 'ŶĒīǷÆ\xa0ʃǲҨƦɒʳǺϜҏɣ(љƌď',
                    'locale_codes': [
                            'ţöȳƅѣǪğň',
                            'ύȟϬɱ',
                            '8~ƮǶͿƋ',
                            'ƉÖȏ˧',
                            'OΦҙİԤĢm#ɠǉ',
                            'ΐɸ͵Ɔ',
                            'ęӔʰϥ',
                            'ϵθ\x85яʾϧjҥϓˀ',
                            'ŬˑȏʗζĐͺņkϷ',
                            'ΒƢƵǉ˧\x92',
                        ],
                },
                {
                    'catalog_name': '¹Ӿƭƫ_ƿϜŎԕ˻ȖԫŹҀȸčɩϖ"˹ƹȈӓA¯\x9d\x9aƐ˧ǈ',
                    'locale_codes': [
                            'ʪñŎƩɾw',
                            'όԬɩɩŖǤƼqР',
                            'ƔåĎϕğҍȰԑȔ',
                            'ǰ\x81Ԧϖ',
                            'ǌʱǗҌ',
                            'ШЉ',
                            'Ӡӄɸ|ѐ˶ΧԈ',
                            'î\x97ô',
                            'ÝΑǣĞuχ',
                            'ѕӾ',
                        ],
                },
                {
                    'catalog_name': '˅ɿȡɽʔΧӑƸ\u038dđiíǥȢ͵ϦąϝƆƋʻŧ~Ìǩʹº`Ģā',
                    'locale_codes': [
                            'ƜhÃӽ',
                            'ƽŁÌǼ',
                            'Ń',
                            'A-ĝɝԐӰϔ˶',
                            'ɋ',
                            'ȱŦʋɗϮЬȂƺ',
                            'ɝÍϾ',
                            'ʭҜƭñĈů',
                            'ŵԦϊԐ±',
                            'ϸýѺãǰŵƯɴ˹Ԗ',
                        ],
                },
                {
                    'catalog_name': 'ЅȁȄȈѫЗŦβМƔȥȹґЗºΠɄτŗҙԤĻǭ\x83ΐƂ¥Ⱦɔs',
                    'locale_codes': [
                            'pqžѮɼǜ%',
                            'ĳêʈ\\ʓ¹ҝ\x90βȑ',
                            'ƹ\u038dƨ2ϞԔiȔ',
                            'ɕӏ®ԄȺȁЌПǐͱ',
                            'πǡ´/Ŷʪ\u038b·ͺ',
                            'жŊƚ1ВîǶμʄ',
                            'ҹɰҌ˔ƐϘȷxƔӄ',
                            '˲',
                            'ɼΦΐͲ\x8bŖī',
                            'ĺ˹ӯķŉ˵˪Å',
                        ],
                },
                {
                    'catalog_name': 'ЩƪөȂɾǉ£ЃɫħϷχȫӿďˀξҍͻîżˏØŎÔӾԝ÷ўŏ',
                    'locale_codes': [
                            '"',
                            'E$ʕ',
                            'ī˰˨ӍŝüÁ',
                            'яȄкԀVʎųϹ',
                            'ɯԚǇгŊə˝,ţ',
                            'ρ',
                            'ѭ',
                            'Ř',
                            '\x82ǇŘɱƭўͶІ·Ø',
                            'ΩҜƐɒԍƐˀ',
                        ],
                },
                {
                    'catalog_name': 'ЏхǕǡêπԁίQƄɾŕϞѵ˕ţˀ\xa0ƭȔȧ\x8fÛÎǧĊǱˬБǟ',
                    'locale_codes': [
                            '±Һ^ƮχƸC',
                            'ť5ԦĂʛĆ;',
                            'ѩІƩˊĮ˹Î',
                            'ɓƈβλȁϐɉ',
                            'ƃ˫ӊ',
                            'ɄјgpʠɪҌɱҚԝ',
                            'ȃʲχΤé',
                            'ƒȋȪԛ\x8fэĜη',
                            'ѹϸўİʂӛĆ',
                            'ЭʌĂŃʇʔԈϴɠ',
                        ],
                },
                {
                    'catalog_name': 'ˍȰ˘ÎJҙҞŒԆɤ\u0380йʏāóԕ\u0380ƨʢέĺΈћ˽ȃłƓȎƎÌ',
                    'locale_codes': [
                            'Ѡ\x9bÎѴňʔ',
                            'ӧԋʯӽËÁЋ\u03a2d',
                            'ь˷Ю',
                            'ǅœҳǙť',
                            'ÑѭԌλΦ&',
                            '\x89ĨӔĶAʓ\x9fƅÝ',
                            '!ȯѻ·Jįɜθ˰',
                            'ʠŊ-Ђҋ',
                            'ӳӪºƈб\x81Òӈ',
                            'ȸʿǢͰҊϪǸϧǈЛ',
                        ],
                },
                {
                    'catalog_name': 'ž3Ĉ¨ќȢƶЇǳļʏȜƨ§˩ѷŸaˣÑō>Y˾ϫŨǛΑҪķ',
                    'locale_codes': [
                            '\x9bɘʂÀԢy0ǛŤʏ',
                            '˰ɎːǆэȊϋɎI',
                            'ӤʳʪƼʶǇ"¦\\',
                            'ϯ',
                            'M',
                            'ȹ',
                            'ʰȣк8Ȁ',
                            '˓ƭ',
                            'ĐӍɋÂ',
                            'ˮĀSþϵ',
                        ],
                },
                {
                    'catalog_name': 'Ȳс_ƹžм˵ȺɷϾŒтȌŤӛȄʽʼȨȾΫvĿƹȃĦϔԌѢƊ',
                    'locale_codes': [
                            'ťԊƘ',
                            'ϐϔʂФѦmǐ',
                            '\u0383ƶ˞ϻɔѹȱʄĝΐ',
                            'Εƶ',
                            'Ҹл¢6ΰùΧ',
                            'ЕϮƍϪӯ8ÞϖϪ',
                            'ЄÃԉґɣŸεɧʕ',
                            'ȹɒɺ',
                            '»ưоқ\x8cɝŢ',
                            'Њ',
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
                res = l10n.Locales.parse_data(test_data)
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
                res = l10n.Locales.parse_data(test_data)
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
            'name': 'ȯlþÆ±ЅґȦ˯ƔŃ\u0378ƦêȑA҃нŕ˺ÇсКſӇеǄфĳ³',
            'code': 'Ů½',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ȗ',

            'code': 'Ƹ',

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
                res = l10n.LocalesState.parse_data(test_data)
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
                res = l10n.LocalesState.parse_data(test_data)
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
                    'name': 'єдƵӷƢђ°ΙаŹˤҭэ¨Ýаϗ×ϩ_ˈûγÖoƀӗТѝ˩',
                    'code': 'ή˷Ś',
                },
                {
                    'name': "ԌĔЛɈЋȊжÂpĠ'ȵΜԨ\x9dӅȎŒȨÁ˒ʳӝʡɹҒÓB;ʼ",
                    'code': 'ŸeӳƳʦĀŨʍ',
                },
                {
                    'name': 'ĔӂʲͶȑǰ¹Ӫļ\x8cƵϕӗɫȉО˂їЋ>ɿÌӰԕɛŌаA®κ',
                    'code': '˟ȑ;țɍΦá',
                },
                {
                    'name': 'ѭӷѡАƭȔǉȦ¥ţιԡ\x99ӻË³Ą\x80Ӏ2Ϸǽєˌӿcҵӷˠо',
                    'code': 'ϤΙQϒǍƺŜϱȊ\x8e',
                },
                {
                    'name': 'JϘÉ\x9cǲ\x8fϗȆÙŸԨÊʧҋϙƺԩʇҟϫìΎ.ҦφðťӂΚʠ',
                    'code': 'ѵȿ˴ҥԫʏԨŷ÷',
                },
                {
                    'name': 'Ǚԝæ\'EʳʟҸΝ\u03a2н"æ}ӗΩ˰ƖҝӟɿˊʶƷŽǬĩԜéō',
                    'code': 'ё',
                },
                {
                    'name': 'ČјʘȸšɒŌлʢΟǤhʺϟ³ȕnǄɮŲêŒңʘОɑѭŽϫƭ',
                    'code': 'zŬǜÒԇ˞',
                },
                {
                    'name': 'ӄũɡȚEÛʂɟśȸ˄ʧ ȡοƭӳ¾όȝИʀҝϷƱ¸ŘΐϜǠ',
                    'code': 'ѩƉ',
                },
                {
                    'name': 'ԉĞϡς˼τӥ',
                    'code': 'ƃĹÚ˗Цǳ',
                },
                {
                    'name': 'ÈԥƹƃˬǰȐMԟèϻDɻ˞ìŃϝơƱ\x85эˀɶǩӧԧԢʥʰ4',
                    'code': 'êŐҼЄԝÂ',
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
                res = l10n.ActiveLocaleState.parse_data(test_data)
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
                res = l10n.ActiveLocaleState.parse_data(test_data)
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
            'locale_code': 'ө',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'A',

        },
    ),
]
