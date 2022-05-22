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
            'name': 'ӰΧӺӡŉĀϕĺȠѺɇ\x8dɠѣHηN?ѰȠӦαϧǦԙˆ}ʗǰˋ',
            'minimum_version': [
                -5030075695383598997,
                -8570026815934636994,
                -6787357684733226938,
            ],
            'below_version': [
                -3533011574033188217,
                -6320838732736551394,
                -5532539839753122748,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ÙѥΠ',

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
            '$': 'ŜыƑÎǭ˨ɟΩS×öóДȢɴƲѢмʈŔԭԣƪɹĝ\x8dè{ФӒ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 5461662093003787999,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 358293.21263177757,
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
            '$': '20220522:172814.582718:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'κΆϳϹ%ѐВŮÈíǷơΗƤҬ¨Ĥ҈ǼӤ2ȠоӓeȘ҄\x9eхΈ',
                'ÝǊRӦғҼǡƵđǩ\u0382ʩOȻȷʽñϩǫѼƟˉɝȓԀˠ7Áƒď',
                'ʝƁĂԀп˛һԉçīŝˍϰΕіʂѽțǲҡΔŹnʉʹ¯ǳ҄ԂŻ',
                'ԩ˧øЫǋӵџ±ƳƊЏ˲λưԣʾЎǏ˖`ǫxņ[ғɖ˧ĳɮϾ',
                'ӁӶĄĥ\xa0˜їˋęɣҷӰǻζģίƝϤÖϳȼǱҏΦЈɪӚïԡД',
                'ҏѵGƆĘűҨӣиήҵѯoҞБƟԡԝĬҢÙӗҘԠÎӗʐѮ;ɉ',
                '=ҐʤԜʘɜɐԊђǉǪȮeɐɽΓϸϣɭWǢҞ¡þʕ˧Ґϝ҇m',
                'ҜʴͲӸς@вŪ$Ǿ\u0378ԕǏĔPĕƙ-¾ңƿyɰѨʾјȿүļų',
                'ȖĮ˳ϿȾǋʆ϶ҾœʩǼ,«ҕäïƨ\x89ƌɚÔфħӤϾʢΔɵԍ',
                'ԇÙ(ĜœΆԪǷɲʽˌʄ_ʬҍ=@ÒǻŃȌҪľ˱ǽȱɔɢɝ¼',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -2884338511273714405,
                -4164257450011856103,
                -3193644491386203839,
                2851281463168116630,
                -7026271159346507333,
                551679720030822166,
                -7883499223189116168,
                -3198001969732505860,
                784192602812075490,
                -1365119215559514843,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                461279.57416699175,
                904362.9407991206,
                710873.8845169891,
                92158.07664204642,
                562197.8357919902,
                321053.31376598205,
                -29770.983480142066,
                283024.39910787035,
                346952.27165963186,
                721492.8931709413,
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
                True,
                False,
                False,
                False,
                True,
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
                '20220522:172815.058075:+0000',
                '20220522:172815.066248:+0000',
                '20220522:172815.074961:+0000',
                '20220522:172815.084128:+0000',
                '20220522:172815.092977:+0000',
                '20220522:172815.101776:+0000',
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
            'name': 'Ϛ_ēŎ',
            'value': {
                '^': 'datetime',
                '$': '20220522:172814.452633:+0000',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '˫',

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
            'catalog': 'Ų°·ŏ\x87ӺêΡˇɢɧDϩǻőɼЈˠ\x94ӻҧǝȕчӛņǑԙȋż',
            'message': 'ŋ\u0378Ư\x94\u03a2ƩПɦʛЋǅśщĹ>ȘȮųѱˑͲʅчɍŵ*ȷЎ¶ˎ',
            'arguments': [
                {
                    'name': 'ϨОǧɶӄҹ˅фƢΡзӷɇΙȴԈ³ʸҋʚϊɽƌÿcҴăı²z',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20220522:172813.620773:+0000',
                                        '20220522:172813.629178:+0000',
                                        '20220522:172813.637245:+0000',
                                        '20220522:172813.646339:+0000',
                                        '20220522:172813.656193:+0000',
                                        '20220522:172813.664507:+0000',
                                        '20220522:172813.672900:+0000',
                                        '20220522:172813.680949:+0000',
                                        '20220522:172813.689979:+0000',
                                        '20220522:172813.699866:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ȀӤѿȻҔǑЄ|ЮIǐƳʋŮɣȠƫñ½ԌʌŸĨǪŗѲaХƀ9',
                    'value': {
                            '^': 'float',
                            '$': 979215.3814879248,
                        },
                },
                {
                    'name': 'ɧώÁĕϡȽǏΛӐƣȆƌѯɹƼŦȞшӶѝ҇,чßҨλѿЊǓï',
                    'value': {
                            '^': 'string',
                            '$': 'ϯýɞŠȢҎǇχǓ§ƍ҅ΉƮЧѭAЊį¸ĆԍϨʺʈʑϝĿӁȟ',
                        },
                },
                {
                    'name': '\x86ҀʋƕΦʸː˚юɦӆǮԊ˸ųOӭϦĈŕʩȀˁƞǣԞΐôõӎ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        4805035753164106324,
                                        -9133606523836043714,
                                        1020364956347435244,
                                        5187511948337260470,
                                        1998844150418491152,
                                        7800942591072913589,
                                        -8955556523253188060,
                                        2423678892276322026,
                                        3124784342258024105,
                                        5345572161641947207,
                                    ],
                        },
                },
                {
                    'name': '¶ҠUƠϱːӁULʝXΒơҝӎŢı_`ӵӹȜɆԢƀņ·ĝғÔ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20220522:172813.940958:+0000',
                                        '20220522:172813.950019:+0000',
                                        '20220522:172813.958910:+0000',
                                        '20220522:172813.967052:+0000',
                                        '20220522:172813.976029:+0000',
                                        '20220522:172813.984652:+0000',
                                        '20220522:172813.993355:+0000',
                                        '20220522:172814.002456:+0000',
                                        '20220522:172814.011839:+0000',
                                        '20220522:172814.020967:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ĿȉǲȥϏƴÁԡɖǸ\u0380ƘŊ˒ϋȫΆǱ',
                    'value': {
                            '^': 'int',
                            '$': 7492098394938487089,
                        },
                },
                {
                    'name': 'tѻCҀѤԎʬƱş҆hWԞưСГ˜ѐ\x93ӧ',
                    'value': {
                            '^': 'float',
                            '$': 524143.5449508404,
                        },
                },
                {
                    'name': 'ӃέÍF',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        -64979.00322476199,
                                        75271.4416170353,
                                        193225.80721761502,
                                        151944.8830923857,
                                        -61317.189387252016,
                                        39389.123171255254,
                                        265166.9807176358,
                                        74656.61520635666,
                                        238260.28535593796,
                                        433814.5808276733,
                                    ],
                        },
                },
                {
                    'name': 'ǥĶФɜͱ¯ЛϷӂԡёȯώȴʔU&QÃăҊÐýùɥȃ}Гʲ˫',
                    'value': {
                            '^': 'string',
                            '$': 'Z°Ь¾\x82ӖϲƦͶȫǮǌЯ¡ľ˲½ѾʶƧѤϊѶ3ÿІqȄɓд',
                        },
                },
                {
                    'name': 'Ĉʫ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -181888893198025683,
                                        -4642925031115164169,
                                        6215969525893297064,
                                        -1650039100547658881,
                                        -8969283912402348118,
                                        4400873985313561888,
                                        -7689554727318431601,
                                        2987587540398117955,
                                        6528195825170779254,
                                        -6071226782749200275,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ԈГ',

            'message': '҉',

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
            'identifier': 'дĒҘʩǣŌǐӎӊ`ɷʈцô[ұʩŹɮΩŉд˜Ƥ\x9cϭǐЖɱÔ',
            'categories': [
                'access-restriction',
                'os',
                'invalid-user-action',
                'configuration',
                'file',
                'network',
                'invalid-user-action',
                'file',
                'configuration',
                'internal',
            ],
            'source': '҂ƼÓǻ҃ӊԦ\x98ѐŀӲsԉĝњǊĴԊOԄьӌţļŁ¾ӊȌǔД',
            'messages': [
                {
                    'catalog': 'όɧïΟˇЅʯȝʴȐƇ˽ɠʘʰɽԒɤΣƍʳĮ¿Ȕ7ɥϡ^лč',
                    'message': '\u03a2ƽÔʰȇϿΗQ\u0380˱ɞƙѧđĊвźēǁķƻ/ҤģƧʭŘǦҁƭ',
                    'arguments': [
                            {
                                        'name': 'ÖʁÉƖƅҌōΞƋôȰІƉίӎʵԙґǱNӌϽǏLPˏЕʢČ®',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɇɏЙʔԔʉΒ˼ÝӊЪňϬɆȹѿӂΪ\u0383ȓǗNϺscĨ"čƠʨ',
                                                                            'ЛЪΚҷ®ƜƱϛϟ$ʫϓÇȀйÿɖʮΖӦ\x94ŭӥ:șԜwȨԨń',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Қ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϕĊ\x84ˠԒӦÿÆÂԊҿѪЋ2ĎҧΌϡśǬαoԤΣ"Ӎİºʈκ',
                                                                            '҆ԨʷêIBmΧșνҸˇӐǚ3зȺѠλʅ҅ɠҥɁǓěυǔȾӤ',
                                                                            'ƶĳԑȆΡәҦӺȗѺĭ\x8cvďФ˫˸ʳĘͻҢŻͷщcȞʄėÚʑ',
                                                                            '˓Ь;ѱМ\xa0%ԩҁҾЀȚϕjƣɶŤʧѯIҡˋvƫԧĴǸҲXҽ',
                                                                            'ƅЯȸþйǁԅ×ԈӚ}ˤӌȃȌәǬâȝ͵˺\x98Ġ˦kƖΉŲjɞ',
                                                                            'QӚөЕɅĥjϣлȒȣΜĎǉåѢжʝĩÞȞ\\ōѩƞӧϩКӸǾ',
                                                                            'ăŖǽ~ЋӉҪϮ)ͺϑҟŝ\u038bǻҒđRѤȻӧÙǿHƔƢԣϏɥҍ',
                                                                            'ŷӱLҋ˧ϖϞzԖӨʦʷÖ|\x90ϊшӅƵǵγη˷јƅϒÀċĚΎ',
                                                                            'ę5ҥ˖ӡϐчδʃŠӭÂŭ¬áʁ5ĈťϔǂęϊʑΎӏѕҤĝќ',
                                                                            'îӰĎȗƯʝӁǶʗļˊԝԕĩϴŽǸÕŁӳȤԉо\x9c?ěʊ(Ɛʤ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'υү\x88Ú΅Ľöʺ˱ĬҤҡñϖңƘʃȩҘ˝ƏѨĜʆʖ)ɁŚҗȳ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ψʦ,¨ҟŀΕǝҶ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8251291551006525857,
                                                                            -4571359166321219071,
                                                                            2821670605957636621,
                                                                            1221953493002939153,
                                                                            4621976079124301115,
                                                                            4414734815621602092,
                                                                            -4351192771086523232,
                                                                            1722346627659275213,
                                                                            -6409531469515542033,
                                                                            -8707806346300904358,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ĺƅ=қʊȖцƭіǭ¼',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8978480391052330135,
                                                                            6271821715770908394,
                                                                            1446244581985706570,
                                                                            -7160524580794372679,
                                                                            -1890296582683657607,
                                                                            -5568984464922309048,
                                                                            -4215782744524539652,
                                                                            -8075727316330198666,
                                                                            -2686476599055638502,
                                                                            1405691748359155607,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "Ƕ·ҝ'ˌȤÈэԔʴfɱѐſүĚșȁ4ʰңǷ",
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            30659.06058916179,
                                                                            356471.14391311706,
                                                                            36214.390259101376,
                                                                            105396.38702187818,
                                                                            897957.5582276096,
                                                                            642713.8242342646,
                                                                            526154.8134479765,
                                                                            307878.0392087314,
                                                                            993742.2155297336,
                                                                            240096.1786066373,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x87ѤϳɥǕąɺӨԌ*6ØƆȾȡĔҳšĴĒӛďο˔ʜѳέǎҊ\x8a',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5745577706970600766,
                                                    },
                                    },
                            {
                                        'name': 'ҚԌϢĚұɲëϨ`ΪѵӞǎ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 784422.6000224234,
                                                    },
                                    },
                            {
                                        'name': 'źʿȯĪƖƫЃȪƗÿË҆\u0379ˎýԑЭԊ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172807.323530:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ӟ\x9dҢĩ΅ԅçȰãΜĖūԑ\x9cͲÈΠɋŶӆҼˇǨÄωƢʔǢȣЇ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1842670530974805340,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '[ǜ˺ˢɈ¡ȯüǬѾљˢЗҐкƥmȢ$˒0үĻʦʽУΛfӲȱ',
                    'message': '˲ӄĝĶ΄ӲĨŝӸúęŹ"Ƅ÷ԈвKБʵΎĞƋƏ£IӽǄ\x8e`',
                    'arguments': [
                            {
                                        'name': 'şүƄǃĲӑțő',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Őϝ¬ȡɄɊ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'nɦȰŽōķªϖκƁƿ\x8aöїνϜ˻ĹŤў϶ӤЭЇȹЩŷИ\xa0\x9d',
                                                                            'ʺёËąÒЄƹҲâǼҎƓŜãԦrҢЬӁ2ʻ)ȸαԜaѡӜǕń',
                                                                            'ŭƏΦΆĄrȞĮĹ;бɶφӸѓɢɫμ<Ԑąɲʭ\x86|ҧjƤŮҩ',
                                                                            'Τ˖+c9ҧɖ²Ă\x93Ԉʱǵό¡ѳӞ˕ɿлεǹϭȮѲWϺȬοѱ',
                                                                            'ǯǴΡ\x93ѿǊҸӟȈé/ ĲÇсƨʸ˹їчϐɱМϗҳŪĔŅ\x86Ǚ',
                                                                            'ФIđϜЉҾÄɍÂʿʶϨǯ˶΄ŬȄҭ$øӭɟѮȷ¢ɦ\x83ĈϽā',
                                                                            'сɬһь˓ѥXΐȚϋʾԤȚùǼӌļ˓ɍ\u038bƹʣȨǺȿāɢɷӁʅ',
                                                                            'Ͼħцԩ\u038dƖɁͽ2ǬȢԑЯʚέ\x8dȽMѹӦ4\x9fƔǧɗäĝŐɔǃ',
                                                                            'đ$ʩҋϋϥӎȬ˯ѿUˈȬϕʏ¸hΑӻӮɡ±ʺʹĴǑѰӛӭҠ',
                                                                            'ŤƎŤȔ\x91§Ԙ҉ȼҐΧϻƉʬɞǚΊ-ȲӷЍӏƒѐȈżμLѭҽ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԅʶӦҍϬïÙ˻.źÈҷʖѕ˳ƧʇɝſƮѝʂƮÇnѤ\x8cȲ\x90_',
                    'message': 'WΈġĆɣͻˇԚԆà\x97ʶӁnʳΗһȶЮЂƐʉĦōµҽ¢ԥǔ\x85',
                    'arguments': [
                            {
                                        'name': '\u038bΣ\x96Ċψ@ǭ¦ΚĨʭɝȣӃʬŤњΚūΆʅΏҕǖһːˬӽãԜ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Čſ9Σԡ>РύΓy҂ÑѠуə˓˓ϲøͻÞʌБã|÷ʕĭʍӔ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4847068410905430153,
                                                                            5604975874091973738,
                                                                            1844741468611194966,
                                                                            6882815883542791809,
                                                                            -2239126985354316790,
                                                                            3596903251649155937,
                                                                            3821127474491439291,
                                                                            -826245116122094595,
                                                                            8850600862953292463,
                                                                            5413064587619224423,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҘÙɥҽЙǰŵɚϠXкӠ>Ƚ˦Ӟĉϑkyhɹϧϋȓ\u0382Ȩ.źҖ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ǜǹ2ɲïąѣƋŇʗĘ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            196556.70117324154,
                                                                            838056.1836856536,
                                                                            104992.0466195567,
                                                                            674133.358668818,
                                                                            949034.7516879081,
                                                                            910188.1026234246,
                                                                            540803.4505373237,
                                                                            818467.9654635001,
                                                                            403036.7780594634,
                                                                            98217.22195658999,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԝşÔĆҽѓ«ɠłʍőÃÄǃЇӐǐİ\x80ҹӼâдӪԩēÀÄԇȚ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172808.009630:+0000',
                                                                            '20220522:172808.018665:+0000',
                                                                            '20220522:172808.027848:+0000',
                                                                            '20220522:172808.036329:+0000',
                                                                            '20220522:172808.045058:+0000',
                                                                            '20220522:172808.054154:+0000',
                                                                            '20220522:172808.062957:+0000',
                                                                            '20220522:172808.071160:+0000',
                                                                            '20220522:172808.080468:+0000',
                                                                            '20220522:172808.089530:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΣǻĬʍǮ҉1\u0380`ʽƲiɩȟɂӪXȇ\x8c˯ċĜ¡Ʌ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2448922214915399349,
                                                    },
                                    },
                            {
                                        'name': 'Ȼԏѧ\x99ȞХ˲ԢӃƹԢʦϭʍ%ɲϔÇǸЙĥӟσȕǯØgӣƐԚ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4620699736473562433,
                                                    },
                                    },
                            {
                                        'name': 'γї¼ҘͺԢ˪',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2804206390527886725,
                                                                            -3613701323977763622,
                                                                            -5524484012122060376,
                                                                            -6987846132095567251,
                                                                            2167342315219045477,
                                                                            6771391962833872455,
                                                                            1299253778983364988,
                                                                            -2592745320806397014,
                                                                            6163311544889490347,
                                                                            8360175419621667270,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϮͶɛȠ\x84ǖǫ!Ϳ)ĢҬӗȱԪ·˷ϊю',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            154946.36711972323,
                                                                            888044.9630135219,
                                                                            340578.2355460941,
                                                                            645050.9522948812,
                                                                            55800.58015324091,
                                                                            955416.3062558679,
                                                                            192864.85939083342,
                                                                            255336.34042874706,
                                                                            621875.3561681289,
                                                                            799616.2814570961,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ûɂӘέ¸кƓĸŦϠԐ\x9fʇĲǔuʫҳ\u0380',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172808.449946:+0000',
                                                                            '20220522:172808.458857:+0000',
                                                                            '20220522:172808.467765:+0000',
                                                                            '20220522:172808.476913:+0000',
                                                                            '20220522:172808.485838:+0000',
                                                                            '20220522:172808.494763:+0000',
                                                                            '20220522:172808.503688:+0000',
                                                                            '20220522:172808.512737:+0000',
                                                                            '20220522:172808.521351:+0000',
                                                                            '20220522:172808.529551:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʘćÅĦƓԚËȡѪƾǍǼ\x8bΐѰƫѠȳqħĶ|ɭƩfĊƕŌǾ\x8c',
                    'message': 'ѣ˟Ҏ˾ǥʋ7ƀвƠԓ\u0383ӼтӏӖ҄\xadȿͲŀ!ɽ~Ʋ%ͶЭŋȯ',
                    'arguments': [
                            {
                                        'name': 'ÒÚϷÐѕʸԇСҘфӴЫȔþɝƩȫyõŜ\x8fɦкĺ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 946680.1314525013,
                                                    },
                                    },
                            {
                                        'name': '΄ûқʞ®Ј¦҄=Ȣȓ\x92őΊѺĬҋʎȀКәǕθԏɁ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3142167193974805855,
                                                                            7450988063404826660,
                                                                            5206729389858182840,
                                                                            7634824970200167617,
                                                                            9120599179984525431,
                                                                            5137917936119577539,
                                                                            729625533491085708,
                                                                            3391604015841989258,
                                                                            5457536752067864296,
                                                                            -57432766490905388,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԦĈΟɋЌʋǆѲ3Ǉʦ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            180696.03795803385,
                                                                            814908.5641342199,
                                                                            81364.58110072569,
                                                                            -85469.37722967388,
                                                                            394942.8469915534,
                                                                            862895.4976017234,
                                                                            319046.99152799067,
                                                                            526327.0412480645,
                                                                            838811.1065553565,
                                                                            -58483.42771622157,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ӭȲ'҂˭ҹѲȚбŁ",
                                        'value': {
                                                        '^': 'float',
                                                        '$': 875281.403540718,
                                                    },
                                    },
                            {
                                        'name': 'Εą(ͽĢ¹Ƃ˶Ϛ;ǈǱĎͺˌћҮľεѨ\x9d¹ǌЉùҷkξѰ=',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172808.925921:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ŜĵûĝƢ\x87Ãԩɠ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172808.961412:+0000',
                                                                            '20220522:172808.970679:+0000',
                                                                            '20220522:172808.979587:+0000',
                                                                            '20220522:172808.988539:+0000',
                                                                            '20220522:172808.997025:+0000',
                                                                            '20220522:172809.005606:+0000',
                                                                            '20220522:172809.015066:+0000',
                                                                            '20220522:172809.024223:+0000',
                                                                            '20220522:172809.033453:+0000',
                                                                            '20220522:172809.042107:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϟňӶˤfȆ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            591029.7238817245,
                                                                            3243.9351922311616,
                                                                            460093.97075527045,
                                                                            989566.5075506442,
                                                                            -29147.217224239197,
                                                                            781035.8674046802,
                                                                            175540.60396147787,
                                                                            327351.16284663585,
                                                                            542837.293538325,
                                                                            847381.3662531723,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Һ˴ИĐŶɇȧȘĜ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 908686.4067465619,
                                                    },
                                    },
                            {
                                        'name': 'ʾ-ʬАÃӒ\x90r^ȷ\x83ƭãӐϋж˲ϊ˴ȁ½\x91Pҕŷфɒ\x92ąϗ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8220748547487826013,
                                                                            5771276841551839862,
                                                                            5615913432969440526,
                                                                            2360184345863679742,
                                                                            -8832922838393096032,
                                                                            -8039061206143271214,
                                                                            -8711169400672074015,
                                                                            8469871655673471385,
                                                                            -4624973663099395860,
                                                                            -3075117630838558979,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ņҲͻőŦ÷ӖLżēʮԠďUǞ2ΖЭЭȏĺïʅëɠĂ˳Ӽсň',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ź\x97ɘҔвЖƫė ʡԗ÷łʛȏÂÀɻȼƧǼĆƤġɀԊÎ\u038dӵʮ',
                    'message': 'ЍșáȅЗĤɺƋȊƽҎĒϮЦ\\όɀLćǬεʺɪǟρИҭlСǏ',
                    'arguments': [
                            {
                                        'name': 'ЇƬԆВɗȧƲƐǸD+ƕ3Š]ДήͺǵΤ϶ȪȷŰ>έɲЇĝ˵',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\x9fǗɋΒӔ´εʊΑʝэӅўŦɸǫEΓӶĉФ´hΡŦӁˆɞɿͲ',
                                                    },
                                    },
                            {
                                        'name': 'ǂäȒ\x98ƆӄɭþĐԏψУȴĺƺQӸșƼȕХӧǜҌőʈ¨\x9fȍϼ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Î²\x9eĠ\x8fӫ˳ɿїЅ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 909743038771393446,
                                                    },
                                    },
                            {
                                        'name': ']хΌ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            246271.33843028924,
                                                                            914841.7530217909,
                                                                            395214.6255970412,
                                                                            957690.0534142596,
                                                                            171534.49370173214,
                                                                            654382.1326319312,
                                                                            332125.0339667102,
                                                                            812020.4381607719,
                                                                            465396.42152558465,
                                                                            283855.5791840651,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'сˌʻѡ\x80ɕ8ʒϢԩƄΞƗΨǵҾЩ\x95Ǥ˙ȨĪƋ.ҕýЦŷ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -485836520514421237,
                                                                            9145994128966871320,
                                                                            2015239501502645576,
                                                                            -6204820851352682259,
                                                                            2338519006301772568,
                                                                            -5375189127533178402,
                                                                            4885564510656434775,
                                                                            -420061785441417382,
                                                                            -6937970022085914869,
                                                                            4771387603996286029,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʱjëϦϙϡʸӠҢ\x88{ƇѣBғȫϥԖɔŘκȶiΐĽӌtѨԙΛ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '3ДȋʆōӹǴːĐ҉Ɍ˱ńʌ˦˪·ÎɎɁÚȠӭ҂ƵƔɛȳͺҡ',
                                                    },
                                    },
                            {
                                        'name': 'ƑĠ҂řđķӱȃΣԗѳќƵΘό˕ƵԤ\x90qΞ˷ΝaƯб@ԫʮ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ļģƗÖԙɾӅřPrЁWĂºӤȅʏȔԍҋɷɣɪǺ7ˠŉЧǖĳ',
                                                    },
                                    },
                            {
                                        'name': 'dˀǟҿәͿ\xad\x86ɯιƫāμʲЋ\x9aŠoӶˠưÀǔĩì1\x9aŖӀț',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            998924.8034502298,
                                                                            362524.1277182393,
                                                                            334196.0289485964,
                                                                            577350.8490653152,
                                                                            635720.5459954841,
                                                                            272238.82478433684,
                                                                            835673.5170375824,
                                                                            408173.62588494166,
                                                                            -35712.84620956042,
                                                                            23351.40664903137,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'z\x82ă˗',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172809.992728:+0000',
                                                                            '20220522:172810.001769:+0000',
                                                                            '20220522:172810.010055:+0000',
                                                                            '20220522:172810.018495:+0000',
                                                                            '20220522:172810.027055:+0000',
                                                                            '20220522:172810.035611:+0000',
                                                                            '20220522:172810.044705:+0000',
                                                                            '20220522:172810.053299:+0000',
                                                                            '20220522:172810.062214:+0000',
                                                                            '20220522:172810.070655:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': ';ӓҭŅRǲĽȁʔΡφČѦžú˯ѫЬȥԏʓ\u0380ɸǠËĨFč·Ê',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҩåiЌїƔȋѮǇƥǁƱѿѨϪG*бɐŠΆŪѬȏҔ҃ǟȫǦΟ',
                                                                            'ɳȰɖÉѿбƏiˈїϲĕƒƽȲΚцʛèҎʄƥ϶еϫфӭĭ˭Ȟ',
                                                                            'ĔX.ʖέBĺνȇӪɄԅΝʻʺ/ҼБΩøòМΏ\x90ʰĄΏòѓI',
                                                                            'ɝȀΗ?Ϸӝѽ΄ĥ=³+єʞɺϭрƦɈЧƃӁȯҴǿͽƒ\x83ЕӸ',
                                                                            'ÀӂɓҀ¦Ҹɕ©ʬѲǵĺËĝɾ\x91\x98þɚ4ӾͱƭΕtӋѐċȔʬ',
                                                                            'Ƭ"Χ˫õ˙7ј˴î¤ӓʦçŚ0ĴΈҐӝ˜ń¡ʆʓзȍƖʩӭ',
                                                                            'ɤƎϬǝКńƍаĲ\x97ӣӧԒФīɓмɶíɗƧͶl\x92²ʓϐ\u0380æź',
                                                                            'ưҌŅBƁ¯ѤĬͼ\u0380ӕ(ǳΖԛƶҶ\x89wˑθƇӪȏϹɪԮФ˥ȥ',
                                                                            'ЈĜίǸʫҦҎůѡәѻɐ¯ѵΆѠ˘˭ƪϳϮPGԫҴǼЊˑ˂д',
                                                                            'nǅpÜʿъЀǢȝjɆĀˈцΜǴͲŰҢцƑť9ĆŋbǚӸɴН',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ÚНԆZǴǆѓƵ¥һğoʬԄԊ#ҀèҮмǫƴŁͻоͱɈә{ї',
                    'message': 'ʬțƅƪ\xa0Ǳɨ˕ҶƬΰʟʩəĨ˙ŎӑǍЙˮβĠʔˏȐ\x9dǑԑɔ',
                    'arguments': [
                            {
                                        'name': '˝ºŝʼóƴWKǻʨΙѰëĘ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŭмí]ӨͱӗҦȪƸÜ˛šǫ\\ӚƤ8˻ӾǤǯʄϝҪɄŌʀѵќ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 419724.3136334168,
                                                    },
                                    },
                            {
                                        'name': 'ӧтЊɋ\x8cʻˉΚľϭɁ˝Ȳ˩ÚZŝӿƘѮň\u0381ǃΚƾǪΰͻȄΫ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '3ƣ\x99Ç\xadҵ˷ƙȔÞįԏϙԈя%ʋϲԙӯΌ\u0379þŔ*˶ͳΦ«Ɏ',
                                                    },
                                    },
                            {
                                        'name': 'lȱϦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'gԧϥĚ˵ϓřɏ%ʈxӑҿƻĻѱǢӓԁƊȪˆȢʑ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8377177468029926697,
                                                    },
                                    },
                            {
                                        'name': 'S҃ȭϿΣƽҔϺӮpϘӱgхϪŎͺƛαϘʇƍ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 623509.7379541441,
                                                    },
                                    },
                            {
                                        'name': 'ԜćϣōӠӒӶʋMˌǽʁǭǐʭȿҼҐҞąPƫςƕӾǞĿ\x90âť',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɫǧдϴ\x91ǰŴҍÔɔԑ³ӲºɆ΄ϺťǆǑŕцгǁOӡћ\x8dȘd',
                                                    },
                                    },
                            {
                                        'name': 'ˁ9˗*=ȺƀˇҗȹһȯΣʘлң\xadÍϐɉgԚȏϑˆ͵ΞΓīȞ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3269745151537091552,
                                                                            -5754173502079947262,
                                                                            5460892664935710040,
                                                                            -7352195225118913542,
                                                                            -6091930091314842162,
                                                                            -831680238030461448,
                                                                            6144251829154609678,
                                                                            8993591275534669449,
                                                                            -7499550859613479164,
                                                                            2833292700107696322,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɘʰ\x89ϲΈҬŞԧǯč{0ģɱқˈmş\x7fͶҋȴę',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172810.727301:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ӝʗ}ΣӞҰӒʱȾɲƛӂ\x8bkǊƀʥ˝Ř',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '¬љǑηδϵ¸YÔϞ҉ɹuԨӯɉ˒Ϧлŷɇ˪νƂÇĢƻʆȗĕ',
                    'message': 'C4һЎɕƇԠМИ\x98ӻŽ¬ʆ4γĖɸŉϧêÒÄͺ˾ęʼѾǬď',
                    'arguments': [
                            {
                                        'name': 'іˑƲȝѿ˒ɞ\x81ťԮӛӞӥÛұϠД»öɫЦëЦђɛϦ\x97ϗӿ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 164428.40514360275,
                                                    },
                                    },
                            {
                                        'name': 'ɪȭϐ·ȣҴĘȕǄϺȟ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 706696.3284879387,
                                                    },
                                    },
                            {
                                        'name': 'âFɖ\x88оȼ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 373694.25648304314,
                                                    },
                                    },
                            {
                                        'name': 'Ù\x8eӏ7ΘĹʁǘʈɋӌN˸VӐʝ˃ΌnәųԎǱgȉåĮǀм£',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -919751717369026860,
                                                    },
                                    },
                            {
                                        'name': 'ș¯Ίđʞϲά͵˟ġ˱˕',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '+Ǐˋ˲ȱӚ҄˄Я',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -96515.28471858818,
                                                                            143484.62613230434,
                                                                            916353.3365269303,
                                                                            869927.8284101028,
                                                                            717806.2603477155,
                                                                            466704.36544049066,
                                                                            714175.093452022,
                                                                            543882.2590148073,
                                                                            139736.58363863075,
                                                                            708250.948521812,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˪Ǐ\x86ǅ˳ѩĵқѣҧʦų',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 113253718265039654,
                                                    },
                                    },
                            {
                                        'name': 'ųЈˬΡǮΧ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 171538.58114747144,
                                                    },
                                    },
                            {
                                        'name': '\x7fӣSԣɁîŕͲ¯<Ƕ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȣзɖԃɛρåťԑ\xadΰ9IІľǥʜ˫ĄԦƂԐԕԡǶъ\x8d©=æ',
                                                    },
                                    },
                            {
                                        'name': 'fɵȭèŬЯѰӪkβǒ]',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172811.326274:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʒưʖёľRoʣύӮɔŵūʡρͳÄıĶРÎσϳѧȋȼйҌӄ\x8e',
                    'message': 'ɉɋЗˀŀ\x97ǓvɱϸʬĥнԌțƱƂȿǃ»FȒӏ϶ȇηûŇw,',
                    'arguments': [
                            {
                                        'name': 'Ȭŉ@Ǟ¤˞ɲѠқȗīˠĀφŦҿʰrÉƝͿӖʨƢ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 259676.68556504813,
                                                    },
                                    },
                            {
                                        'name': '϶l˵ӾƘ˃ν҇οöєlȶ|ͺ˯iчƇťЂnШɸǤϝ\u0380\x81',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172811.432627:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ŚԝҘϤӘ˃ΨɌ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'йή˧ɫљџϢѭÝiϩ˅JtǃˊΛǝĿρΗӷɏÄЅθĘмŒФ',
                                                                            'ϖȚ\x92Ϣǚĭeźʙіƙ²!ȀăңƎҷǊԙӥǳĐ»\x9bМЪÁſҕ',
                                                                            'ǆĶˊ˵ͲˋɜҐûԀΪӋđlƺз϶Φɶ˳х҂ӺЋԥӒuƯξӉ',
                                                                            'љ\x85˝ǲ\x7fPСʕ¡Ԑě¬6ϳ]ǅ(Ӭί˞ɪȕϚˏɫҖřʌûʏ',
                                                                            'ФͰПìˣЮ˧ɕфѯ˧Oєŗɯ(ϱMяйƔ\x93JӡûǽɡίǱȤ',
                                                                            'ΪĜʸӝ_ɒэŕӘɤƼ͵ƌͷЦԓǷbŀȖ˩ӴÜʅɁб\x80ԫϱɊ',
                                                                            'ƃ¥ʵҸϪõѮƒҨİɳ¯¤ҠпŝˏϖʹƷǉƃΧ˓ɷJ¿ǚӐʆ',
                                                                            '˃gζēŠЬӥɰүçǝɵǛ\x80фӏ\xadȌˋ҅ЂɍХKņðō©үѤ',
                                                                            'ǙԊƳӈˤ)V"ʢäŝɢЅΝUɤŝíϤ¼ƾıÖɬĪπĺĂĮʴ',
                                                                            'əǿŵϪƚƖΝ}Ҿdξ\x96ȁʀЖϡFÎƙάΪƬ]ÑͿȵҒ\x84Ϸʚ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƼӔƷɻ±ӌά',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': "ƜҳɀЈÒ҆ʷӉǋкԮԐϕ\x80Ӵ:Ш`ӨǶЩ'\x8fҧơƏӍĘɱХ",
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ηʯ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            112491.01802207326,
                                                                            708626.7329357857,
                                                                            434303.9283258786,
                                                                            582817.3795276774,
                                                                            762897.1758615436,
                                                                            523625.35763164354,
                                                                            431991.45495485456,
                                                                            540116.5525667595,
                                                                            80649.1298203074,
                                                                            254987.22860885196,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'åʱʄPθĤȊϖҴŕȟĔ\x82HǗâ˚Ӝ\x87ӌ²ȼ¿ÁƾƞҠȦì;',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172811.780775:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѫӛ2ͿǀԕúǷɿ\x8a˔ɚ˽Ƕкȟ˫',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'РЙ҇ζơŮɖLéн',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÙѲϫΓĖĒʅó\x9fǫÈϛϫήĉŨһ³ʃšˍǔІȩĂ~ӈƘǸӊ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -765739840684816900,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϦĪѼӁvɮκ\x85ĴýʷųQϾӛǮҶåυʷƒŖĐӠѽĸėƓŬԏ',
                    'message': 'ʘԒѣϒӍӚҮѻɶɣɟγųԆʇʗTºҳ\x82ɆɾÎúϣΔǱ˘ȖF',
                    'arguments': [
                            {
                                        'name': 'ÛѠӇ˷ϵʶˀԨŔԩµŸЃəHПʴћҹŠιǦѕRЖñŴԟĬ`',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            351288.2557497145,
                                                                            515395.6907145566,
                                                                            725068.9046137993,
                                                                            539768.8502898671,
                                                                            584075.6263259886,
                                                                            987620.1944862057,
                                                                            -76256.29472638754,
                                                                            108296.0079743801,
                                                                            -46419.908538328,
                                                                            993832.2006142533,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʄrEİ˄ҭԓˌįͼΛ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3266183603615225147,
                                                    },
                                    },
                            {
                                        'name': 'ΊӮЎϽљǄʳʄșɼsBaԖFǡɛΓòϘȢӓӆƵπˀǐõǉñ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 456679.21601391793,
                                                    },
                                    },
                            {
                                        'name': '\x90ȷ\u0378·łѰšΡöȰƮӵżЪ\x92ÅċǋΈĎԞȸȤȢРȑˋƏ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172812.329206:+0000',
                                                                            '20220522:172812.337670:+0000',
                                                                            '20220522:172812.346681:+0000',
                                                                            '20220522:172812.356036:+0000',
                                                                            '20220522:172812.364290:+0000',
                                                                            '20220522:172812.373269:+0000',
                                                                            '20220522:172812.382353:+0000',
                                                                            '20220522:172812.391483:+0000',
                                                                            '20220522:172812.399698:+0000',
                                                                            '20220522:172812.408367:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΝѹĲăˎ\x9aӫяƑƖŤ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1709101766989971883,
                                                    },
                                    },
                            {
                                        'name': '҃҂ƯҙɮϓžɃҶʐɜ˭ѦÊİɻǑυǞŌрϸǉΉ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172812.488554:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǿ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172812.523115:+0000',
                                                    },
                                    },
                            {
                                        'name': '@ԒƼӂŁԛĩƴÔǁǖĪų˽',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6574690357665176677,
                                                                            7877200301076789819,
                                                                            2740497357517086279,
                                                                            -1885310043182709813,
                                                                            -6892011245014185262,
                                                                            640638192156439550,
                                                                            -6126264526093328045,
                                                                            -526399481818704846,
                                                                            5061197302750949922,
                                                                            -4295450599724661408,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Œζθʶ\xa0ǹJǾԊOßύʙ˨ȩǓԮͼŦϚϡǊӐĈȗǐʨŽȲŭ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԋθõԥ\u0383ƚč;&ҏ¼˶υőƧĭǖўΝɝÞтɓǠ:ɾϡǃ҈ɬ',
                                                                            'ʫÛӶҀȠÉË©ƚċǕȋɦ}ҖǆέͽǨӯģС˫ɋÙǤʿʼ\x80ʕ',
                                                                            'Ɗ/X˹ǗaȫYʿӯ@ǐʹŔҧӽ ҝЛ,Ǣō¸ȭĽҕʁȌђĘ',
                                                                            'ϳ8ϽͿǲӬϼʋЩӡ#Ӧѯω¡ȀʞQѝβ3ǇyтǸ\x9dӵ\x85ʳã',
                                                                            'ЩʫύϷȵƢԣʴǏÀϟԙZѷѬʭΝӏҸǅ\x8fˊЛĶӳ¼ñПǊF',
                                                                            'ʺ˓Ⱥ9ʹɌԃɤѪŮэǯĲԀɆϨȤɘϝǣΉäșBѰήѺʤȢü',
                                                                            'ȺԟŜчϴʉрŷǚȼΰĉʇ˙цϰϢƫӮXȮt;-Ӝȏ\x99ѭɜ-',
                                                                            'ԃˎϕӽź¸ŁGɉǑҺēŔ?˼ғĉΕёÌêĄťϐɑʌϾ£˓Ō',
                                                                            "5ԘqËǿɶҲƛɶƟүR\u0379ćí»ʑοďЧΕТҜϛ˒ԕО'ұş",
                                                                            'ˀԞҟ¢ɈǺʊȦ˃ʡ_Čϭ˩ЉȏʳҖҕӫϣLжɦԄ_ȀƙЗ҂',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϧƲ˘ҡíªɤѝʈÔȟƢлԭåҥсҳѸĶѯoѹįɨʞϜԎӒÔ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4660895029111713613,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѫǴʍԨѻȳĩȶå]GBƯ\u0379ŭƞʱкăˆˤԪԊӤĀȋ\u038bѣǯʠ',
                    'message': 'ɩЏźʠѧ\u038bÆμü±(Ŧʁ˥Жǲӹȴԣª«ʠƒʰƮʳƳʃЅT',
                    'arguments': [
                            {
                                        'name': 'ν\x97DfқɛFɻÀþȻƾԎ^ɆĆͳѕȶԏ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 521046.1493303338,
                                                    },
                                    },
                            {
                                        'name': 'Әӫ0ʪНьŘƤҙȱ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ΈHǥǙÐ\x9cFɶV˟ϢŵǈˎƈÙɺįΥƕͽ\x83ǔĜǨʍЬ]˺Ō',
                                                                            '2ˢ\x82ɉцϮҹȦe{Ѩϛʜҁ\u038b"ώ˒С\x98º;ġɄǵϝӕĈǬϪ',
                                                                            '˗ʦ»\x81λˏÙҵ¸ƓɧʟʉµҡƎ»ʌİΏ˔¹CÂƸ8ęЭʪΛ',
                                                                            'ǿûΉФǭ˝ʌƔȯćɪ?˜ɕ˵ŤΤϣɶ\x8cg{˰ϕӴ}ˑƒHԧ',
                                                                            'ԇ\u0379¥ϯŹȟ˥αʙȴɄŧϮѻȠӡͰыȾįǆӋˑǘɝŬ¼șӥρ',
                                                                            'QԃҹĆљʦҸƎÄĕʔȱLўԫѝşč\x88áЪBΡñª®ѣҵ©â',
                                                                            'əúŤķ\x8dĔ¦ʜǝϭȵȀˮ*ʕɾ˫ύБźϠŰáWƓvϣΎ4ċ',
                                                                            'сŹɛ7ӚǱʲɇȾВӐĢѭϕɯϩĴ˅ηϽϫȮЃɴʨa\x86ԕӈҸ',
                                                                            'ƿѱÖɵѹЬʕťԐ@ϖƹɐȦƲӵčʳЙиȝŚϱΖˇϛђɬԔф',
                                                                            'ſŴ\x80Ȳ#ˋӈŀ˄Hɶ˖×êƈёӳϛĜŎοӧϤʇĶ˦ƗǒА˺',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ιʌҖɯф±ƥʁˆˎԦӊˤÈ˻PQΟӢ¶ѨØѣ&',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˍƮӃԞǤҦžĠҝTјξ\u0378νвƩƫϳťƱѣήŏ¿sӴċɕ$J',
                                                                            '˻ѫνѸ˙ɦƖJĉЊпϱϏˊ(ɀèϕϧ|ː҆Ҿ¯2ė˺ȻǴү',
                                                                            'ϖv\x93ǅϫЅɌʸȑɠʷīΘξǇ˅μFɂ˭ӐԛӋ¤˫õmƭȷҶ',
                                                                            'ǊƝҝɬǽƜĹҰʆȉɰţƵă˗ǰθè\u0382ұ\u0378źŞǙʭǅʉҍгɇ',
                                                                            "ĸǀȒӜԧŗӹԛ[gAӦ¡Ӷ\x88эĮʮ˭\u0381'\x97ǶЗ¯\xad¶ËĞγ",
                                                                            'ȇ\x9dˉуӡÝћԧʎбϢΚӵіàΚɐϺǱԚŗӞϐÐȜԫ%]Ĺ1',
                                                                            'ͶſǳїВÀи˷ĵˎ҅ѓʋɕŀΝ³ŰΫϳШşğɧȑæɂҹɭӧ',
                                                                            'ōæǐƎĭƬģƥʩ\xa0ӽbɊϝˑέѷĺĿˑŻɹѸԅlԬƔƮσг',
                                                                            'ˡ-¯ɓǞȊхԛÄЍҬҒĞǌӏeїό˯ѦĂӷ\u0382ĻϥėȩȌäʬ',
                                                                            'Ħǧ3΅ǴӊϮŻǇБȐʊȒЈƒ¥ŒϗɇëTӈԖħ!Ť˞ˁĒƾ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˕īыѢÓɔӂԉў\x89φŽ.ʨҰ˴ɃƇƞӎԙƯП',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            911514.0897010226,
                                                                            21881.627699116667,
                                                                            581239.9182708915,
                                                                            728370.8758180896,
                                                                            461615.1310822298,
                                                                            125670.82363889975,
                                                                            844296.0397276679,
                                                                            375181.1842738986,
                                                                            524463.8442072403,
                                                                            282063.3869224849,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Пǲłу',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172813.285105:+0000',
                                                                            '20220522:172813.293602:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĈɴǆʥӰŵҝʑӵ5ҺЃ·ӼmGǴϯԓЦζɀ˞жN{Ϯ˲pϗ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӷƗư˲ҿ\x7fÝ˪ɥ5ǲЌˁhеɷɈʺͳhөШŊΣ\x98ЄӧͳOτ',
                                                    },
                                    },
                            {
                                        'name': 'ĩìҚƪҚСϹЯÀǕͼÕӊ\x83ˣɮЈЂϺή0}\x95ϴɯԫТǗəҪ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9005286982351081158,
                                                    },
                                    },
                            {
                                        'name': 'ϋšľ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -107001335215979747,
                                                    },
                                    },
                            {
                                        'name': 'qӹXͱȘӣΉ\x8aъæҿNɀàӄáωˋӦLʧɔ{ҊϺҪɟΟ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172813.438438:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϝɭƙŁǆǎBŶӻԄƦ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 221798.7570034422,
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

            'identifier': 'Ĳʺĸυң',

            'categories': [
                'access-restriction',
            ],

            'messages': [
                {
                    'catalog': 'ſӶ',
                    'message': 'â',
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
            'name': 'σƕċϢԄŬƆɀħ\x88҉ʳWДµbӳʟəOƛЃʬˣMĬşĊµɖ',
            'error': {
                'identifier': 'ƌѩ˗ΑĵӧȈƺЗˑȳІɝˣѼ_ϨΖȟԚ¬ɈʷéΐΝöӝ.ƕ',
                'categories': [
                    'file',
                    'os',
                    'os',
                    'network',
                    'file',
                    'network',
                    'invalid-user-action',
                    'invalid-user-action',
                    'network',
                    'configuration',
                ],
                'source': 'Һ\u0382цǟǨϪѸѐԓǩΠЂƁ¡ǳԏɮ˱њɄЂҵŏӷĵоӳДԌª',
                'messages': [
                    {
                            'catalog': 'ȒAǇĉӸŕĝΛõιԝɜâӊ¡˭Ͳĳ҆ƧоUԇӋʩy˯ϺЪę',
                            'message': '҅ϙƍэβΖǰÌòĳČʈ\u038bɄϐԎ΅0gҗêªӥƌBɻͳr+Ӡ',
                            'arguments': [
                                        {
                                                        'name': 'Ŷю җƽƭі\x82ŰѻšǡǻĮő϶ʹ˻Ԫ4ǫ?4ŝƝǚɆхѨџ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172802.747771:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'óӐʸпԭϟͽϓȔƄӵƿΒͰ°͵qÎʑńӽϙη',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'έӘ@ʲ£ςάĪĺʍʂθvҜȎ¾ɸӭǊϘԢ˞Ѫ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 90206.78234989644,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŹӇØθϺ{Қßą:q\x9eʝˣ˹ȳͻшȼáƟëɩѶӪɣʹʔ˓Ι',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƹȔЉηĜľӞÎȏ\x9fźȠΨ¨Ǒĩƚźł:ɱȭҷҿ\x80Ԁ6ňɡ¡',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƕɧҋ*Шɦ\x96ӬĶЭΩƆšďбǻºʆű\x99Ѳόi',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 648866.7064540199,
                                                                        },
                                                    },
                                        {
                                                        'name': 'чɠ˞ö\x84ΌtґοԨԭŭŀuɶ˦èˤсǛĈӍҖƊϪɆȌǊ\x80Ď',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǥ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÑӯǚΕgɩύąЙ\xa0\x9fӸ\x81ίȚ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϊɊ%ɤӤʪ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 202268.3896292338,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ъɹϱ μ\x87Ɇ´ĜƘѥʖőÿɳΖʃϮøȕ¡ИˬԀ\x86ωʫǕϞʾ',
                            'message': 'ΰ]ѫ`ϽɁŧәˢLȬȞɐΩȝĠǶԠМЮÿ©Ǜ&ɢØʃƽɳӽ',
                            'arguments': [
                                        {
                                                        'name': 'ęҎǢҷƚǬ˩ҁȹęδįƏЁ°İȽñǿʌӨĭˣƋв',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 709360.6755761307,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x87җӵťàēϝǂÎÎɹԄлʻǔǈњǞƵҮ\u038bӴˈӇѽzjʴɅB',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'z8ы˷оȿ˔Ԃ˸ǟϽǐ»ę^Ѻев',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԙˑ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -9115503893580326572,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΖŒʩȇǲ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ЈǫƑ¤ƚ҉ԄԍŨԞ\x8dΈ\x7fĭ×ԊʨȴØKȬCΊȇйМPɵ×Ϭ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ε',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4205118094381976495,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȁυƢĞ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172803.351461:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѡMԂnАʄœƤѪȑҳÛŭÑĖƊ\x80ȚѬЎϵɑ\xadðҞӷϤȽŌȐ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 46379.17942686382,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ē\xa0˴àĴƟϫЁƺԫǺǹ`ʝɬҠăцҎƷ˅ǽ\x96˦wƮϋßÆӀ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ғ*˲ĆŇɞӀ˺ˤ7ұ˚āӛʈԀƴԅҧáΉʙ҉Ԉ@VL\x80LҖ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǈʌβзȿҠÇѰ^ƲԀПѹȮEȊ-ΥҌҥ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ǚ˶Şͼ¸Õҿԁʫ8Ӡ˱ǸǽˀǭÖѰӾɰī˒\u0383ҝǱƩǷŴӕɮ',
                            'message': 'ЮǊӋ¸ɀǅǶğ\x99εȡȡϘªЍҎҲĔЯɌ˄ŖƼ_YӌǌӲжā',
                            'arguments': [
                                        {
                                                        'name': 'ƒɐήԌv',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172803.525512:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x82ѾһӿNӥs\x96ȲӓʒǻˆЕ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЧƦΪсȦȘЕϜӌËɄЌ÷\x85ԛԐIΝǰζOȬcӆӾίÖ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6464906820168031321,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŘTҰy˜Ԇ¼ŻŤʾɕȹϷeԥӱɎ2ĵʡПű',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6462529517793979296,
                                                                        },
                                                    },
                                        {
                                                        'name': 'VŠͲҔӅ¡4ʡɀʃaˑҠîԦ^Ȧ³œϨȺ\u0378',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172803.667852:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǮΗŜuЮξűӤĝҷΓvöʚĩˢĐѐT҉ϷũȜʉδԘĠŠȥȉ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 806906.4803756324,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӂЀȫѯФÖїжȼɓ˼ŁǛҴǗǐȕӘ˲ˈȋЂɐӸưӈӇΨˏă',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7972689800263194616,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǀѻ΄"ȄғEӱϻΪ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¿ƖʂŮˡəҢěOěҪ҄\x98',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԗԪɕїʭĂȗ^ŐӞ°Š.ɊɩçЃȾƱƂ\x86ǌ1',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӺÅӍíȁʊɪŌϧӳҹ8Ѱ|ǨҝwΘʺӻîӏХιːҸѲаҹӿ',
                            'message': 'ʺƞοԩȲӮfŃ¢Żɀ˂ӡ˜WÉӝтАvс\u0383χˍԮΝĶɰҢӞ',
                            'arguments': [
                                        {
                                                        'name': 'WҷŊʮԚәfªњǬƶԄο',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԕеɒʣħƭј;őǮϤϬɍѝѝˀĒӧƆGʆΥиЇ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͺ7ϏȜĎʖϙЙρȭґɄоΕĒΟ˜ɋǎУ&ӺйԨɟĽ˖ͼΣ˾',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -9197092587807618735,
                                                                        },
                                                    },
                                        {
                                                        'name': 'αǼ˸ԁŷĲҐɜ\x86ΌɣΫǼ0ˉҭλʌȲÀȐβįЭӰİʰ˽ǲ҆',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˘FҏўĎmʲǨџ²˝˙ǘǔЀѮɎ΄÷ƠӍɝΚö¹ÍåӠӨĻ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĉӊΰʿøƋƍĎϧʴӶӋҔűЋÁĺϬ/ȺyɹӇˣԩґΈюϻ˴',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʊ¶щҩͲͿAʴΕ\x9cԀę\x89',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2511506202254421434,
                                                                        },
                                                    },
                                        {
                                                        'name': 'r΄ɰτ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 355331.44284108176,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɷҡРėҶϴТԕΦӶǏĔʇȹ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɉʁӻ\x92Ğ$όϙƊвŖρǙɰ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172804.229366:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԡĬ\u0380<΅ǙςʖΙƛŵԛεҫΦνūҦǶ\x95¹',
                            'message': 'ʽӨgǹÛ˱ϳȸʾĳĖʙvſ˽˔ʼ7ȬѣӅňɈ˫ΞУʷĬěĚ',
                            'arguments': [
                                        {
                                                        'name': 'ÁľӗΪːϚƥɚε\x7fNѨ²òϿĦj\x80ϩӉ˳ʱŔĦϫ\x8dԫąҏϯ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĩщяύʰϰЃ҄ȢųͺƝĲɁѥȑŘʧЄϠξӿ\x9fyҴČ˨ʒKԞ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԓочІѩřGҊI˾ϒɝӅˠӻHђϘȔȶŔҪԇƜ˵ό´ȝЂӱ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'þҼʝϬӂ1ʤκ\u0382ȷ¨ңgȊѶ\x95',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'хϒŨÎÆ/ȧŬǛȍ\x80ǭ\x8aŻ®ҏҩˮĀԫĞ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʰѕЫѴϾαΑԁ˘ˈʓīVpv\x96ҫ¦ϲˎ4ԩɑʛ˛Ŋn¥Ӑđ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƍѫͺϧӬ½ĝƲ\x88ŘÔˇҬ°þÜĽɍԌȉњџЇĺШĤʙƑƽ\x9b',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȕ˸cʄ˞ȻΦӻψҙɐЯΚ¶ÇǾκӆǴśԆ¨Ʃ˰Ȩ\u03a2Üʰ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҄ȁӸðͷʆ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ąɱ˜ƴȜɌȂñͺːӁ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÞǏÆčƎȚJÆʩϷɭĪ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172804.613669:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʲɍ\x94ɾƠҲӃЯʁȌǷ\u038dПɔà҅ļӼΪ дԠŰȫϜL˒Ѳſ\x96',
                            'message': 'ѾчѤǾΣɕSɁъЙЊnȡІӇҔ˺ьʊԀȳƿτ¢ԅˋǚάȱ%',
                            'arguments': [
                                        {
                                                        'name': 'ԃþŎ˨úюʌÌĠ]ȳԁϚҖͽϫÈΏЉʿҍ϶Û>áAè>ʵ˙',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĜΌTʔǬȎӞÀϋǜѲ\x82ˎ\x90n\x85ЇȯʚĊЇ\x98',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172804.721296:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЫʡώȚ|ƾ˸ɰhǄԀȇäӑŋœȄ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǤѳƜĢөȂǭpρӢȞ\x93\x93ãğϾƇ˞ѽңʨƼt\x92ҟŏīӚĦ\x82',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӥǥѪ4|ǫưҾϤŖ\x87˸ѱҧǐʼЩ˞Ҭʔӎϼǆȡңʴͽ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172804.790604:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҪқĵϞãӐԫǧхʏрńÄҧɂвχϭɊІŢ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԇlɆԗУԂąоǖԓΰΌ,',
                            'message': 'Ú]ũȞ͵ӉҩΛέʨϼͶԝӥɞÄӎȟ9\x8fό\x88ԎɋɴǺ\u0381κÈŸ',
                            'arguments': [
                                        {
                                                        'name': 'Ӑȅɡ\x83?ӥрʼшӹɂȔǏΒ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӱʮ҇ѫȐцŽөҷĉɭӤŶƚŧӾԌŁΆÔūҠԛĜɕëˬŨȖϓ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϊӔҸtđÛѾƅǸħξǉnůΏ\u03a2Ч˧Ԓ²пϓε˵ƸŖЭѴȸö',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÚģµιЪÂ0ԭЉȘΞr¯ԣΨ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4050345368245025936,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȊŜӫ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172805.000346:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȓӰÜŝŌҮ/ʉӛVґEЄђԧ\u0383ƤÏÌϲȿ4ĝȁƹ\x9dΗƚЍ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 143267.89697090856,
                                                                        },
                                                    },
                                        {
                                                        'name': 'СαȵőúƯȳǆï˯Ԡ˙ȂΪȞ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172805.070125:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǐ{ѥ1˶ſɷɖӷҚƵī\x9a˄ҽӒų\x90Ѹ.ɤǯˆ§\x93ǄȄȮ\u0382θ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˙ƧхоӕōɁуҙȸχŢDƸϸˠӇǁǾ8ԜŬԏƑÚϡ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɇϹԪŢСďэʾĳƠӳȲɈūͷʬůϷŔɾŶԈΫè΄ѽžԗҦҡ',
                            'message': 'įKͲƭǧ¥ӑ\x8eʳʥшϧТz\u0382ǈӹź/Ó@\x8cʥϤԆɶl˥ąʁ',
                            'arguments': [
                                        {
                                                        'name': 'ʖǻϲʮUßȔęh˵ĈĺČԤЊˊįԃҠ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'fǯǢƷɻӘȂԄЬ\x8cƸG˺гΒȍӃǉƗѮÍʋĳӍ\x93ɝϲӲǿΚ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 147052.0948688535,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĮύΘǐ"ҸʹԎĮѓϫЗȖԜŀǌ\x9aϐûʬɻŘǻ®ƍ˛ԬĊҹӨ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -9176819009015196584,
                                                                        },
                                                    },
                                        {
                                                        'name': 'τ΄҃ŀȫɢç҄ҥʧѥЌ>ǾñČ˷',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -78789.94638985483,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΊÜČǷƳғѡśџƪȴҜŭåţƖйƴMчʤϨɖ҃Ҫ®ʖǉόɹ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԎɬŞžȊ˞',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϪɕƨűűϽɭ\x97ÝŻµªԠÜʠʳĻҷӭÎШˎ҃Ūϱ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƵϝůάʜˋΟ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x92\u03a2ɝүɻɾӣ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʜңƇҕÛˑ¸Ņ¨ѤԈӃЎҼ˺ŎȘ}ӲȼϑʆǗ"ϥƿÊ§Ӻа',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 495154.25427942455,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ľԛѨȄtҭıÉӿȿԁʁγгҊCĄQŏąϰ\x81<ЃΗ\x88ԘäĶϯ',
                            'message': 'ýĔɹƺƵɥԋɆ(ıê.ƙǼęАҶʿſȀƘĢԑǂŠӗèΣ΄ʡ',
                            'arguments': [
                                        {
                                                        'name': 'ľΰӁѷƕƨγʙϟǓ:πаɵΡɧ«ʁƊß˦ɅɦҦķɤƸ\u0378Ҫϫ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172805.605468:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĮȹǓҹˉӫϳ\x96Ӣá',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2679295546928290845,
                                                                        },
                                                    },
                                        {
                                                        'name': 'øйÂРʵԔϲĽпӲĎʱɷǗǠ˼ҍǰXΈ҇ƩԊҙZѩξʇҌ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĲͶč\x9cѕɾϤʩʱϔƩʢ\x9dγȉҰƦǮʈĽϘȵˇÜ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172805.712566:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȷ7ϊӶӘкɿѿΆ.ήϒħŧӅ}',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172805.749125:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȩ,ǌӎ{ЅCÄǑʓӈʡ\x9c_ǞEеϟćѶѡϐȩĚΘӰĬ\x90',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӫ҃īӷʸԔǆ˃эaȞӍŊΡӎˀҵќҳө6\x87ѾlżǶΆĨэѧ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȩˠýɯϏ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȂˆПĸʩɛůΎӏü\x8aΌǛÆĕĒƴĿĤ|\x98ƥ»ɧƎŶD\x97ԝҕ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЩШƹҿȐªϓИς¬ϐˣ\x86МʽϘæҢȂʹц˜źhшν×ʪЀԤ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '®ǮʁŨŘԮҌɇ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 911955775850231533,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѩə˲čӕʏȧҙϴĦӪϭ_Ǐ\x87\x85ǌ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ήԟƸуϲ\x98ƉύӀ^ʟ\u0380˽Oɧѓɬ˽ƀ\u0383ԩȽá\u0380І¿-ĘʶӮ',
                            'message': '\x97ʊʻɄЊԄӚʘ˩˧γ;СǶҺԊC˥ѣĎңȚʂßԡƍĊΟǢ҂',
                            'arguments': [
                                        {
                                                        'name': '\x86ӎȆƐȍpԂ\x86[FҏӰȃή˜˧ǆǟЙϩʾõ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '5ˡϮђ¸[ÕȉɹЍčûȎӘӰɇԓȴӈ˦ҐӯĈԇĽ"ɰɿ/ʤ',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x82ɓʹʘ҂/ϔ˫ĒĲɜƥҐȣ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '#ɐìҌԪǷɋ҈Ɉ\x99ˠ\x80\x8fɭʼÃˌ˒ҔΣɯɣΦΡƆżʐǂұŪ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'фȩ.ˎρȆĿҘʃÓȰРĥȜVԍŭƞπ´Χ˦ŰăˢҬ§Ǿ»ť',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҘԋӅɈǀvʆ\x98î¬ĒʧĹӃԩӘ\x85ƉůʵǤǬ¼ЀϬӧ\u0383Ҥϲҥ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ж˶ÜщŝʬӋɩȺA\x90Ğ>Ԛ¬ɚ\u03a2˹ѓȫҥĸϜ˺ĠԂȺˈ˻\x83',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172806.099001:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ўʿȯͳԕəșέƅέěӱ¿ȆśſHƯƲп˱ƆĒЦqʻ\x9asϹҒ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '@ԐoǲîÈŻӉɐnǽҩώ·ǴяӌӸηɋдuˍ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΉƑКѝμƧ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˃ōљƚʣΊɶʑƠʚșơǎѰϵɀˢĪďÈς˵\x86ǰҖӝӁȊӃǔ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4697442098469672159,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԙ҆ɀғǼІǐƏΗŊȀeқԅ±ӕкЧ&ӯ˓ҙ\x85ƎƁʔ!ɨŉѺ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172806.269193:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': "Ƴ˧ҐÊМλ'ɟıɴŏøɲʊπΨʔĭЭ",
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϼÒ\x8eΉрn¼ÔϭЊϮʖҝƄјɢ\x82ѶΎ˜ʛȡ4oɺͰɮӊQǪ',
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

            'name': 'ԓͱП',

            'error': {
                'identifier': 'ЃԢƕǮ£',
                'categories': [
                    'internal',
                ],
                'messages': [
                    {
                            'catalog': 'ƚȁ',
                            'message': 'ʜ',
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
            'name': 'ȤлϗΑЪѠƉơȹ˭Ęԑ\u0382aǕӟħ\x98ўmӭЌcŜҏ˛ИћįԐ',
            'version': [
                -8417871037576619532,
                -701529691452500525,
                -776240959202938343,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ƽsɝ',

            'version': [
                -3247196644595696791,
                -5907581208690165733,
                -3683078643841111673,
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
            'event_id': 'ʨҾȨеԖЁΙŠ\x9fŔŬĕϗ)ŪȰөҿɨƞǟʨ˺ĕțШӀϔīҹ',
            'target_id': 'ƃ˔ƅƐȕƲπuϼΗĵ˸ҶдƠΡƕXâҺͲʋҶƽȏʥʌөǟʑ',
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
                    'event_id': '˴ėϡƽCͲƝǤӬѡǪƲǀϜɳŉͻǉɘ(ʅĢǊǃǓ˽ӛĒȼ\x7f',
                    'target_id': '˅ʮɼ;ϱɌЬĵǙҫƽňɕžλϡԩĥŷKȈ҅ǱɭŰȡġИΎǎ',
                },
                {
                    'event_id': 'Ǭ9\u038dӴҒʸѓɧĦҸ;șɋ\xa0ªVѥșӛԃȔѓІ\u0379ЃϓʭҀЯ϶',
                    'target_id': 'ĆѴ˂ԕ;ˈёʂțвãʖ³©ѻǕȤуðĴĨͷӑӊЗԫԋήĸѳ',
                },
                {
                    'event_id': 'ȷʡѭɠѬƑγ:ʄ:ɏҾӬϷɇĎ҅Ψ\x83ΗјåƄԓ_юIB˱Ѹ',
                    'target_id': 'ΪșЇŶūβČҫұĐǌνхǪāԜԧдòĜѵÂƙĄĖ2ǂm}ρ',
                },
                {
                    'event_id': 'ΡΧϦðԫԃˤѐĲѹőКȤӘΤņџЅɵ\u0379˒E˸ʷϘáɘӘĵΪ',
                    'target_id': 'Όɭ½Ì϶ɔƩϻǞǋˢЍѯʧ¹˰SҐǛbςˉǖǩǮķȢӕ˶ƽ',
                },
                {
                    'event_id': 'ϔƢʥɕåԫѕƙΙӫҀ©ӃһԖϻғǲçƬȩaȼӐ³πϯƙĊ\x9d',
                    'target_id': 'ӨǎΈ˞ʜéΔĉ8ͺĴϖсƶāȥϚŕĘʂƦĦŴǜєЙЀ\u0378ǯԞ',
                },
                {
                    'event_id': 'Ǚњǲɖ\x9bɉſ˨ˑÿ=ьҁŤʠǲéĬ˾ƁϭgԅѠƇθŤ˟ϼɼ',
                    'target_id': 'Зǈpʟ҈ѸǴ·ӮџYǁаŎΐ\u0378Ë1ˇ΄ԛÉҭǯǠ˄űǠЯΞ',
                },
                {
                    'event_id': 'Ȩ°\x88ɚ×·ŹѻӞԐʮȂП˯Ňŏ·ʹ˰ξ˃ҧ¯ƭѩņɱ˸ѵ^',
                    'target_id': '͵Ɏ҂ƜВӜʕāĈˑȍtɌ\x88ĖĒn\x86ƳԏŃʔƑ5ɱё"н/+',
                },
                {
                    'event_id': 'ƤȎǍƈϝ¹ƃҾĢБӍű\x9bʽɗ"ºʒZƱЧƞЪê·ʴϑ\u038dϳ¾',
                    'target_id': '҆ғěƗëӮʹӆʎś˭ϸ\x89ǲƑrʻiVԛЌЭƵωʘʏ˃',
                },
                {
                    'event_id': 'ɼȲI˓æĕ҇ю\x98˔πĸȳàZЩĽ3ǔΪӌŕɕʧ*Qγ¶Ǯʡ',
                    'target_id': 'îă\x8dʷΧԄ\x80ɟɪІąƎ˪űΰǴġӑςпȴŞцlǂǳЉǦ\u03a2ҡ',
                },
                {
                    'event_id': 'ƅʃϏη˰ΒʆԘѻσТҍʺфԦȨȄӡӧΐÚu\x8eƥѠͼҶ~Юѓ',
                    'target_id': '7·ϴԨˇԁ҇ĤƻÌӿʬхƒǛѴы=ϼ˚ӴӞȚϖȡYƲЁˡʓ',
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
                    'event_id': 'ȂϘ˼ҾǈıȑŨϞ*ˬȨԋķˋҲ¯˼\x8cӰ',
                    'target_id': 'ɦӧˌԁƒʽǈ²äȯǩ˔ɻjƋхӳëƴƙӫϔԦȥĹȑԚѪĝ[',
                },
                {
                    'event_id': 'ΒӹêѽʃѯΓöѰƧ\x9eЪΜɈώҊԎӪ³ƧӓɨǌĚāZZžԍʛ',
                    'target_id': 'ʩҠЅʝҰҦǬžʹ',
                },
                {
                    'event_id': 'ҊƽǏ9T˹ůǹ»ăεɢǢņþ˹ȣŸʒȰþԃˡǡ˯ˮɶŏͲȸ',
                    'target_id': 'ɻˑѭΝо^6ɇĴŞʊßɲǥԭʓҍϋMɣǏÓԛfĄѯȜ\x94Ȗǹ',
                },
                {
                    'event_id': 'ЎҧǧқǻʕǀļȮ$Şˡжá±ʽʏͻў×γêwƫѥǣ\u038bʏČ¯',
                    'target_id': 'ҠĴĝӐԄ\xa0ʧӒRɐɈʉϺϏЭŶʓƒłlȉ5ÝӢ\x80ǒŒŋʶП',
                },
                {
                    'event_id': 'ÉµτəţџκІ\x8eͶʛΙԗųžСЎғ)ϗŐ\u0378ѴʂũӯӎЇğГ',
                    'target_id': '\x81ɩӯʏԞȒԍµ˟ËĶˊǯϺƯӋɤΚɕԐŨʓ\u0378ő\x95ӺͳƭÍϜ',
                },
                {
                    'event_id': 'ÎӅʀщ~ԏҢȁҍS˺ΒÔ˄ǽîǸӝƧ˭R¤\xadÕӻġǶƏmʠ',
                    'target_id': 'Ȇ˫TӝȍɺԐ˩͵ĭԎRɧƍɺёιŢǞŏıΘˇѡΚєϊǢƮ+',
                },
                {
                    'event_id': 'ýҾɩκƴŮȂҙЧ|Ѓ\\įѮäVɡфӴȇÕȝ˞Ëȁȗ˃A˼ԉ',
                    'target_id': 'ԣҠА˟¬˅ĪЗ/˼ʪʲїѡıÛϢČ',
                },
                {
                    'event_id': 'ӎðНϊ¦Żɏ\x8cЌћβǦɶƑТͶɊź1ԂҪӵЭŤdжBэ\x9a¹',
                    'target_id': 'ƪцϞąʂʫɆȩ\x94Ĳԃ«ҤiӧŶ\x9dŕШëʃ¬\x85ʰҜώ8ӭʔ',
                },
                {
                    'event_id': 'ǯĕѬfϦʶщĿΞǄɻ͵ǻʱу˽ƚ_īȣҗ\x8dĠӪД˔ɢŨŮŦ',
                    'target_id': 'ıѿơ\x82ҷԨюØ)ԈƺƦїЏ\x9fЅӫŤҥɔ\x84ʏѴ\x8f>YĽЗδм',
                },
                {
                    'event_id': '¡žĿτāыΤ\x8eʑǦïǗϠϥҞ²ëɸӨƁΡĮЧѐӟg˒vĺǆ',
                    'target_id': 'ήƨɪʄѰĮǍƖѦӘЏϻ͵ѣȗѤȠȏ˫ĝßҋΌ·ȺĠÐϮƍ˕',
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


class ExtensionInfoTest(unittest.TestCase):
    """
    Tests for ExtensionInfo
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EXTENSION_INFO_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.ExtensionInfo.parse_data(test_data)
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
        for test_name, test_data in EXTENSION_INFO_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.ExtensionInfo.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EXTENSION_INFO_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='ExtensionInfo'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='ExtensionInfo'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='about', name='ExtensionInfo'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='description', name='ExtensionInfo'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='authors', name='ExtensionInfo'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='licenses', name='ExtensionInfo'),
            ),

        ),
    ),

]


EXTENSION_INFO_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ÁεưГŊĔ$ɉŅǔʀPɹŗҗǈҞˀŮс˺ǻѥԗǖӪ҉ѬǱҗ',
            'version': [
                -1847409551569878615,
                -7206449136747987555,
                -1439228040325907325,
            ],
            'about': '\u0381\x87ҋҢ\u038bϩŨ˼ғпȻжҖʲԝƫԖЧӚфюˁӃӑˎƢъɛĘϲ',
            'description': 'ƀУΧǷЄҜǎGˠƮˆȧӄЍ.ͼĨˈ\x87ƅɬʶԋФλǎQԔςȴ',
            'authors': [
                'SПűĪϲċƫϢƲŧJ\u0381ȲҠǛőˇМѷЮϖLҾGʰėʕнčā',
                '\u038dοɫm\x84ĢѝћӂϕчĄÝϼɴϗқȵҝҀϓҜæûɊĠè¼А\x90',
                '\\ϰɰΤšҨђεÛ˱ɝȣЩøʏ\x8bʃћѽϺЪҙʎԞ\xadɚřȫӲӃ',
                'ΪΈFΘЍp\x95ȢψӕÀН!ԠϺȌѧŌͻǰԎɂσɼԊȔҧЬ˂Ж',
                'ƸӧʎĠрˡѐϪʂ¾Ĩ˭üũ,Lӧȱ˞ɾűθϊʬ}]Ԡƶʧј',
                '\u0383ĚȭҲǠ҃ȕɕǴҵȄ˔ʽҫȋҍőKњ\x9dǶȏʴɏΖ˖Ҍɾȓˏ',
                'ƚʵѸƭҞԉΕϰ\u0378ӴmǡĢǝNРɤÞиɫΞ\x85ΤѦПҥƾɡӥ0',
                'ΚŖǾĚ҂ğŁƙιʶģԇϙΡʧ҈ΙΒӾtEғɔūΫƉΥɤͲȬ',
                'ԐѝɡȫǓëȰUҪѸƣlӺɮΙͲЀѾɸʞȊԧѬПƍeӵϷĪζ',
                'ԅ˛ĕęʖƿǔȥϷӴ8¾4ǾΙŰϞΦ˺žʺǊω&9Љâӻȃр',
            ],
            'licenses': [
                'ԓѝɃΨŖƝ\x85ДʕҲ\x8fфźχʚϱϒÜ\x82ь˷ũћĔƬ$ũɻʛы',
                'ŀϩǢЯҌǩϒϒʷόѨǚÞÂɩʅӃÄϔ£ϠƇˇϤŅѱʊȱ©6',
                '2ȑ)ʏôч]ɣƈТōĮȯŜ˒Rãʱ˻жʷЃɑˮ˗ǉұƞǠͰ',
                'ηºΠɝƅ«OѼŽЫԃɰ˫Ȍ]ʾYҎ*ЇɆβXŀѯҡĆҨ\x95Ű',
                'ǙϯəñƢΡ0ͽȨӘѷ҆Pұ[ЛѠԅƁǬF˕їӕÆϜɟӎ˥Ӑ',
                'ʎԮΥʔŹŏϘ˻ź@ƅˈʻ˷ɣĥөшѦԫȔĳʒ˕\x97ӄ^ͷƗς',
                'ϧЩ[ҾˋšºķѐҺŴŹ!ĽҵˆϗȐvUǁʀȬдѣǵο\x93r5',
                'ºӮѴп®ȍʅϥ³HӡɴƋҮӇϽĂş϶рľƮϲŇ҉ȞӃ',
                'Ц\u0380˻ƽþͰ?ϻʊΣōŢӅˍȯԧΞɥҶ\x88ЛΏƉţЗʈƁѤʟ¨',
                'ӝŶưƇҢʰȔԭʖfȺЪJȟȥɾĝŸȘҵҔµζЧȻːƗĖyƖ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ÃĀȲ',

            'version': [
                -7351368555604273237,
                -1117966135076445569,
                -4581456374212195093,
            ],

            'about': '',

            'description': '',

            'authors': [
            ],

            'licenses': [
            ],

        },
    ),
]


class ActiveExtensionsStateTest(unittest.TestCase):
    """
    Tests for ActiveExtensionsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ACTIVE_EXTENSIONS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.ActiveExtensionsState.parse_data(test_data)
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
        for test_name, test_data in ACTIVE_EXTENSIONS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.ActiveExtensionsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ACTIVE_EXTENSIONS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='extensions', name='ActiveExtensionsState'),
            ),

        ),
    ),

]


ACTIVE_EXTENSIONS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'extensions': [
                {
                    'name': 'bWȯKeǚʔ8҉ъəʸƠĨėÐ¨ȻҽӀǭ˒˔л˹¾˜ũр#',
                    'version': [
                            -6043679960245767983,
                            -4843163577365232864,
                            -4264144191870003947,
                        ],
                    'about': 'ԉф¦ȚQαıăēμȮюαӆΞÛѽϡ1ĠБƂѾʏPǒѣԋɃβ',
                    'description': 'ǡљϭǫȡʤсɻϯ˄˔\x84ШһϤGω¥϶π¹ԅǏϭϱʵԡɽŁ%',
                    'authors': [
                            'ҟ0δƓɯˎǑçЦɕвњhŘĻƊɞFЕҍ¥˦ϖ\x94ȕҲŇʝɝΗ',
                            'pѰƏԬʙˇѨ$ӋԑȹľʼІ\x85ФǊĻҎϯԣǤϻȋ\x8bȂǝºǈň',
                            '¼čƴɮʨɿӹʹ&7Rʊ҇ΦϏ¿{ѱӪƭaišӉҰΕϰʋɕф',
                            '3ӗӤϞБ˜ɖӉƓϑɔ˗ЮʾiͱƺВ˩Ȃʼȟƌ®\x8e˥\x80ŧʰҠ',
                            'GΨɫŘԦĎ_ÅşǺˀӝŚӏԌ\x8aӥǷƅǯԆŬ҉ήʒǍȷPӭŎ',
                            'Fɗɦâ@ƆѼɺʲΐȶϜĪӑɷ',
                            'ÿίɭǦɆvЈέѫŸѳʹԔƧΥԐǄĝŮɄКƴ3˥ԊӁ;5ȉɕ',
                            'ƵʰĻ˶ΏӭϙщǷ\x8dƑΕƒ҅ПŉДԘˣʸÆÉŢǸϸʄϱǊБƹ',
                            'ɴǓx\x85ШбǷԜыıΦɪ©ʽĤȻƫǤǇʣɲƇѲҍƾʢԧʴʭϞ',
                            'ȋӊϘäɃɅ~ӢʭҾȌ\x89ЎɟƥźАˆ˧π\x86ϥЛӺ:ͷ=ÙΗЬ',
                        ],
                    'licenses': [
                            '˩ŷȈǨӤԠНȝɘЎăӍѠʹťŕɌʬŲәԘǬˌҒЕѡ-Юўτ',
                            'ĐȢФɷĖʎѥԁFϽǿπǌԔѻȆ¯ŬʋІƢȸȺÒ\x8fģęУϸϫ',
                            'ҕѼƃ;ԁҲDљҌÂčɉŗΥ˜ƌГĴʵǸӓÅƞàƞӔˈ϶ŬӸ',
                            'ĐĺτǖöŗψѲ]ƓΖѤâ]ǫʧʂӛиĥɅ\x97ʂƗ\x80aƦǔƨ',
                            'ÐԍтԏҢ\xa0ƣQjѪ;ȬĻ=ʡsNδλμТÂжƍQĉǛҍЗƌ',
                            'ϳԭѐʫǷĿϊѣſİǩäƫȱѣŽƪȉđʈŹȯӈˌ\u03829ƕʑǜЩ',
                            '\x9f\u038bΆĂȭқÍɀҌʘŗƱµΔ\xadķύȅäɏrʼÐŔԧΐǿòцÜ',
                            'Ѫόǹ\x87ŊԔǠ²\x90ȪвҟđӍFΛƸјƹÉ\x97ƸȫŖɾ:ԖӔùΗ',
                            'ȧθөŭͰАɴϦŻǜȜſѶΦ˭ſƗ˱µӱѺǹҭ˰ʶČѶηˍƘ',
                            'ԬǚȌХђҀƖқƏƁÀζѝаŒɋΰſΆǛǨцȟҾʜϢԠϩ˙S',
                        ],
                },
                {
                    'name': '¶ώβƕ^ɏеǜȼɁŠ*йѫɯӺЛ¾ԊǠΰΨԃlǕԌɘɺǢǽ',
                    'version': [
                            -6059538268707320467,
                            -4663767942273323435,
                            -5694557186303710771,
                        ],
                    'about': '×˳ԞҚԑϫǖϣпɑƍǼҲɗȜcͻ¡ȶҍǿіÁȤΈҢɽΊʬȖ',
                    'description': 'ӵzӞƔдҘ%шŸԔ\x9cȔˢɮ˻\u0382ËƤāșƅԞEϝüӇ·҂Ӗӛ',
                    'authors': [
                            'ûҠ˖Ĵҳ>˝ԉŜȎ\x86ŷ\x9e˼ĂI\u0380Ĥӎϵԗȶʭџƀ\x95PДК҄',
                            'Г\x8fӺǌqҼ˂Їǥͱcћ¶λōÌǎǋɭ˴¿ҖҍƔҺɍϬʽҳԧ',
                            'ćÅØқΤѮÛϳ×ˈ\x96ǃ\x84ϊҬ1δ\x7fά\x8bӁϴͶμ¸HŭԦи˵',
                            'vѓӚėΨ%\x89Ȫ˲ɲɝΒƧ˰˷Ű5ƶˁɼԒʛҜѨÌŏΔìˀЂ',
                            'όҗΣЂwƁȬǼҰѧʖτċȰǗԩҋÄҧŜµǳʃ9ϺѰŭoОǼ',
                            'нΝÇ˶ȂψΞ¿òÌȯǥΠːźHϩɊ\x82*Ƒϥ£кƃˁɠӹҪŉ',
                            'ʩźKͻæǴο_å҄ȦғɁɃ\x8b@L\x8f˪ԐīOǢőΐϊԞjǎ˘',
                            'ѳƛČǉ˻ΤԠńЖϹӴϖρϕ¶ϣ¨ϏҍŖЇɏ|ӒǢƶŔΤČ˘',
                            "ϏɆĮ'ȚӿE¤ǲѐǵ˫ȨʂƌɷŢʆ>ч˂ήԮǨPУνïŽ˹",
                            'ʻӄȏѶȸNŴɩГţǙėӸҪEͰ¿ƖÄԇҏˆɬVʑƓӠƤԅ¢',
                        ],
                    'licenses': [
                            'ǮҙN˾ˬɪŘ҉_\x9fɉӈѽLʛʞΡѣбɼћǫ¾ѓŠϰû',
                            'ЃƓʭŌŎŋҗȿÉȶѢǳʼ҄ˢ˗ǎυļ4ϯӭ\x81˹ĆυĦ\x83Ēϩ',
                            'ӣԘǐȱҩΈEѽ\x8dҵ\x7f҆Ơϛů',
                            'І҇¶ӄǍˑ\x9b҈ѩɚфƵŋΖӼǂ{ǁ',
                            'Џԗù\xad<ƲɘήӌĭЮ\x90χƚȲ҃Ҥ',
                            'ŒѣϗԀҽɔnƬҍϮӌƅ\x89˹ƇǙΩǱįʫѹв\u0383ʉºͶˀҭ΄k',
                            'ǒáΡÑŀ\x95ξʗ\x85ϭҐȡ˃ҕʸѭ÷ϒӇӟʾ͵ԇŔι®ԔɷLw',
                            'ҟʢҟʜ¥¨ǳ¦ƇhˁƔЋБϣ«ƴϾcǖΣҊđ\x7fϪÁϠϽD{',
                            'ӅÓ3йƔѯŁϲͷʩҶʲжċ',
                        ],
                },
                {
                    'name': 'Θ±ã|ʖ˘ȼҋțӅűǕȜȂΈɠĆÏʐ΄ŵӥX\u0382ԣƠ',
                    'version': [
                            -2180771555414951817,
                            -554400438690438834,
                            -5738230338605049178,
                        ],
                    'about': 'ɜƟθƊǔӴƂӱ¬;ЮÎFțФаʔȂfÅʗјÙӟûÂнŤ}ȸ',
                    'description': 'ʍӶ˴IȔƗҺϸӇ\x8cqƌŠЖ\x9a/ЪÎČȐīѧσБүԄʁŋǪŜ',
                    'authors': [
                            'Ň{)Ċ´ϗ\x91ê˔ɰήάӧ΄уҙÚʶӧľɸѷȌɖдȤ\x85жЄŽ',
                            'ӰԂťβɯͱŷÁ`Ұvϓɇſ]',
                            'ǲ҄ԚʪPʰϽƪ˦ɱҘ¬ϻԊϭҫǥ>\x96ȀĒё\x95юϽϢşdɩƪ',
                            'ʩӇ¯ƿήĐӒȊϪʾѰӬƯηͳȕÎϷϮŏȅŭΡғĲʵҴǨԜ°',
                            'ΛɀȗƹѿϏĶǪÖДϴϐɡȭŷґ˜źԗέцƁ˗λ϶¤ΐżrǑ',
                            'АǶńɷԞϓӡǨϜΑӓºɴ\x93ǧЗɶԋѠҖϮӥÖс˟ɆīǶϬď',
                            'ɷɐʱ¨ѷЊŶѶÎАǛɄȕƾ҅±:΅\x7fҵҌǺu´§ˤаԨÔǕ',
                            'ŎяɶzΒχsȼɳΔιŷҙŠΧГĢҒӚ£ȴҶЗŉɷĂɗϤFǪ',
                            '˳ƫYӎƸͻʖƺĸӢËtӉġ˰ŦĄƄҪȃфˉϗЉúʇжƳŲƃ',
                            'ƆΒėѷĜȥгʙĮȹгƙ\x88ˈɬyđĳȻɛϷǜϵǇȣЉϙÒлM',
                        ],
                    'licenses': [
                            'ɒȶδ\u038bЯɹ\x9dįԄģϜ\x95ŽöaōƼc/ȻѳƝ҈æҮųӀȼМE',
                            'щÜʑԮə\x93˖ͶҩΫ϶Ĭň҈¸ġӗȑϝkhñã\x85еҬʵƀуҁ',
                            "ÄӳϯӉʹӛă\x8eȽάҮȟŀ˒Εͼ0dȸƗ\x82'ЛТȞ\x84ƳƷCr",
                            'ċǐ˻ŔǾԉȐЍǚȋҕťƟІƇǚϺ\x89ǨǗ;ʙƾӀΚԠˉĭÂг',
                            'ӅҌͳſӳѡ҃ͱĂŰɾĪ/DέӥȊƈϗнÍӊʥǖgjïYцA',
                            'Ϳˤқ˟ǈå\u0382єΔрǊ~ŋрƲ˼\x86ƗÊ\x91ȟÀĘάȀǔΏȋƍ0',
                            'xŪȲƀ(ɷѭѕόɦôͱÈϮѵёƄưŵëʏşwƺԝŧǾԦѓä',
                        ],
                },
                {
                    'name': 'λFȿԨάɌɔЇţÄʰÐʃPĻƻȌÔƛҿθƝÑӥϧЈοЖʆ҃',
                    'version': [
                            -3860221549634857896,
                            -2252765598993111970,
                            -8679063503795896654,
                        ],
                    'about': 'ŸBɊɅΏ?Ԇȳ˂ȲkӋњӉůƹĜˬ¶ˣҹӾї\x96ŲюȲ°ʣШ',
                    'description': 'óҼµƷȰοƴʪѯԘȒÐɑѻГɎΥøӏқʡƮĴӀœ˳лӄ˧Ο',
                    'authors': [
                            'іτÊ˫\x89κ´ӱˊûɘùЋʨįѪҼϗҊǹ\x86ˮЭϏJšννҖʯ',
                            'ԤΪұцąԫҵƹªƊ˪ĨĥΠϧÍʑđƵĭӫЋźɚИɁҩ.ȒĦ',
                            'ƇǲЄĞǻŸϼĭϚǿϫƐΩÕ˂ɸçȞ.ȵćʁƊӾВЮФΫ˱ϓ',
                            'ťԜ¹\x87*ϳĭЇŠϓǿƥ\x99ÔɬØӬFȼ\x80òӌφǥőҜBʜɎɕ',
                            'МƦŞбʏԉ',
                            'ʕȮϦӼԎϛ&ӛсȵҙɃqԃʘ2ģԤźͻщQė˳ĖĀʸӧ¼ʕ',
                            'ӋäԁЂˢʈжŔÊɴĲƏ:ɊũČăɵǑΨҀǝӇҨЇͷ"Ү\xadƵ',
                            '¾ĸƶƙÿѐŠљɘ˧˺ӏ\x83ӂȇƊĝúѰŲƶěʬбĭљȪ¶4˚',
                            'Ҡȟƒƴɷŗ˵˞ƃҺɲť§ӣ%ƻʳ<³mĚұśԍϝǗ\x9bùˮ¨',
                            'ƵϡɜĮӄ>ˋɏȿȶԎСūԀǅȜȸ˕ǾЮǁūʁkɀƍaĽТ\x8b',
                        ],
                    'licenses': [
                            '\x9bΞԂөȏ҅ЎɹôĞСӫcLҐѡˏȹѼ΅ǣϏÓѩmȩƶΡДп',
                            'ĕĭԂƑȡĒЖүũƐϟƯóȇǟӻńĘĆɛ\u038dɗψϸʖҨѩ½ԇӮ',
                            '"ĘʦĶȿҞɻʱĠ6ȓvː(ɸҒʢ1ǼӧBƚÓŖ҃ОĢɲǹԠ',
                            '6ԎÁrҚÕYϘѶуʎ6ʭwƌϮȒʨȱΓƕͿԅüʥ{\x9e\x96Ʀϝ',
                            'ʸÂƭȯЊѭϠ\x83э_ѓԉɫƞӛӀģ\x92ѕJҋѢƩΕȀȵ\xa0.ɽЗ',
                            'ӂԒ҄Јҕčʸ»ǳʹƘǪћǙĕвʂȉ\x98"ƖͰʁΙª\x99',
                            'ʩơέ˃Ӈ',
                            'ɑɹŘԀłhɬȹ˴ęΒʓȱȵѓКɵηZԏѷŭŎѾɘǙ˵ʁÑl',
                            'ҡȀáʨȮͲľȓŬАnλҠϾˉƞӨƓҥѠӵʦ\x84ӆ˫ʹȴǷˏӣ',
                            'hԞƈҤӲȨƾʼńв\x86Ώ\u0378ƆҔǩԪĐɷϽúΗƤɟλӽĬzɇʸ',
                        ],
                },
                {
                    'name': '·ԊýǡY|˧Ŗȧʠ˕҉ҷҧȴ·ǓǶҷȧȼ+ØǽϽӓԅЪŷΞ',
                    'version': [
                            -4777485833425761360,
                            -6342303809606796845,
                            -5538075160156005674,
                        ],
                    'about': '\x88εʣȚ\u0383āǆȂϹʱȹˌèƾЪЇǈkӶлӊȘƉӳͷƲϿҜʏr',
                    'description': 'ҀɷɣЂҬΖӄŠҮ˲žҕʇÿ\x95øЎǔϝ\x97ӜƉӗǜȜ;ĖƥЁΠ',
                    'authors': [
                            'ªΡϑˀĬȢyˀȆ˯Ъ\x8fРŖǱ\x83ʦƖǏǟŉǲÿʕԦņҾɏÎ΄',
                            'Ʒƌ',
                            'ҟAʂƼŻþʣyїǱѫʧʚ\xad\xa0ǇφȔˏԍǶҊҌȶϮ¾ğǌԊѲ',
                            'ɴeΖ˲ɢӢӁʀǻΡyɡΘƞƖqѸӗЩϏэ~ȴʷ½ЄʒѶɳҦ',
                            'TǀqЏ_ʼƦԠΫԣҀżZ˟ɚџȧīĎȄЦԪԗΊӠĒǰсƩӋ',
                            'ƋȡѩȌӢǝЉ`λӕҰá¶ҊӀԥԤǹ˦ƝȝȚЌŷǽřźǦŦԦ',
                            'ŭȑƝbȵ°ɈӧȪҶ®ŀɤŷÑΕӾЋȮҫÝѤͽ$ƉŔ+§Ȉľ',
                            'ӢʕɐƢőҖƛӦИmς˪ɰsxҦƷȃϽƠ\u03a2СԚѨ@òćИȽѳ',
                            'þΘǽЄJ#Ψ\u038bȈè\x8fŏŶЇvƎғͷǒнŤɹǀŉǁƹċǄͶ˦',
                            'ΘȮȗŤʗŔʃԑϟ',
                        ],
                    'licenses': [
                            'ʗȐO/Ҹ˃άɰwӍҧԋŸÙΣǖƲɣӈưкҐŚǇҢŬɜѰȨʊ',
                        ],
                },
                {
                    'name': 'ƟАn͵ƺä',
                    'version': [
                            -6332389199787919498,
                            -41937035549046924,
                            -3736876705038945783,
                        ],
                    'about': 'ɥɹ~ƁƈMԤǟ\xa0ƞŁƝŇɘсɥíχϿϣƒƢǁЛϳћĞҲ¾Ϗ',
                    'description': '¯ϮȰϒkɴʦŉҴŲςȖɽ˹ӓӝѝŤТԥԃԆȧѥ϶şȴґÖȺ',
                    'authors': [
                            'ѹЁʦÐϵϠƔ&҆ɬӚΚЧžt>ΏȉȦƏҴŧGȂαҢђbÇǆ',
                            'ɿӵÎ\xadʪX',
                            'ɏΎвȜȬÇüӎЕéƺƳΰӻʈԋʡ҉вҰ£?ÄұKɻԉɷȒƍ',
                            '\x9dÈäϲԁώҾΎŅšƩâϓȮuԦǑΜ˾ЩҤӏļӬʴˤˍ˩Ũŝ',
                            '˹п˟#åǿǘҙɈ҂ÚǮΡЧƃϢŽω\x8cĨyϬʽӓǷʊFӤϏĦ',
                            'ĵҸ½ũӋðēԌŤ3α˗іǋԪҢуŅˢΜϚ\x9f˖Ѯ\u0379Ř¼ʯĊʧ',
                            'æɱӁħǃϻƯԟԟɵ˥ѣǂΚɲȳǙþƌʯѶϴȅş+Ұ˥ɉɟϲ',
                            'ʴʘɝĹЯѮб҉\u0383ͲєѲ~=QЦvʑЂϷŸĄїƲşʴѿϠƐǬ',
                            'ȩӫǘɚöӼΪґǍɵʸʔØͱǥǪиφҡʙ6ϾʮĳӴѡǿėԚ\u0380',
                            'ΣԜȼˮ\x97ϖҚóӥÿƽñҧӊӂǏѰʥĈʌЈΕҭ\u0380Ɯ9ФԨːĴ',
                        ],
                    'licenses': [
                            "˝ҼЖɟїͲҪӄѽ΅\x98ƿʫʹϪ҃ưȘϩ[ƀƙ'ϖHÔUΎ\u03a2ʍ",
                            'ήνÄͻҲŕăʓϬåĊԭːĆʊĤλ4ʓΗҡƐ¹½ŜÌub\x8dĬ',
                            'ϐϽġԫϷӣĞ¨˻ʹ!ʳδ\x83˵ӱϻØǑɶ',
                            'ǑȖҮМњΜӻŧўĭˏĭҿŏˤÞȣ\x9dΈϣαπƔƚ҃ʜϰȽΙƂ',
                            'ǮεȔԥǰ¨ŚĻ˚Аϩʾгʸ',
                            'ѭÎɨЭ)UǪΣԉƸʓlЎÞгN\x93б',
                            'ͺɖԋïюnƤ\x9dȹͿѳŖoңɩұЦe˂ȩƎ§ʊѥΡŸ\x8eʾʽɃ',
                            'ǸΈ±ӇϨǪǀԔσŢïԍѣűϖʸʻǃ\x7fϺ΄ҌňŸѾўųӃѩğ',
                            'ӭʯʊ˯;¾ÄĜŨ˜ȽȽPҠÓǣъēǉѣo¥˲Лõˍ@Ԋҹ\x8c',
                            'űǍƩЋӂρШzОʲϨӵɉϹӇɌέ˵ΔӜK',
                        ],
                },
                {
                    'name': 'ȁϠͼӌ˧ǧԌ\x99БӝљɅҿȖцѴȿԨýεǀȨvǐǕuɰģƐê',
                    'version': [
                            -8010059389182699267,
                            -2582310863906026169,
                            -6414364202366156166,
                        ],
                    'about': ':\xa0˙ϸÍñNɃ°ΫģʙÂűψӧѾѻɍɿ\x8aǳΌӞŤͳ}ѴŲ¸',
                    'description': 'v\x86ǉ\xa0РƺЀþ\u0382ŨɛӠӀɈȦӣŀΊЊǨǐνôќĜНċΣԂƸ',
                    'authors': [
                            '\x9bĝҐћТ«ưПɍЋόĸӘԏϨǭōƕ\xa0ϴΟʮι˹ƣŰ~ѥĀҟ',
                            'ȪǨљ΅ӟӌҽū~Ơ˗ӐнрğҮpɺ˹ƵʆƟΎӘÞʦɱ±ʽү',
                            'Ŭ҅]ԂүλǵƿĿʽȜ{ßϲϙȔΓȮ',
                            'Đ¬ɇɎğΌθÞÃϔ2ȹϔҎʇŰϷӧϯю\x82ϰӊǽɋˤӑѥÃр',
                            'ĪȶλкǀǠ\x83Íǎ¤ʨĲΔȉШЭȢӸʏˉҍ¨Ѩt͵Ïɡʚśʧ',
                            '%źȿCê(',
                            'Ȇœɺνåһф.ʃʗƖͰɭʺӵŏΉÚTӁτƝӐԕοϵªӂoȆ',
                            'Ì҇þÃӜǠ',
                            'ǞǠьԑƆƁϵȩ"ξƊфʑŭУйωǠӧάϭȭĔPŉ˟ӦîϠǔ',
                            'ĵ˶ӇӘѪϖ˩Ã҃vœțђʲϐŷҚĞĹтƌt҂ŕĨϒ\x80ӺĜπ',
                        ],
                    'licenses': [
                            'ŋϴƄЄƚ¼ȰӋ\x89ʧ\u0379ʃΏр=ɜ˃ͷԬǥ\\˧ЮˁӭʡԛɭЪё',
                            '¼ЛԆʆҘǚǡȭѩĐϘƪǪѰ©q\x94ôȳʁʳѸҰȮmʠ¸ӳƞ²',
                            'ŔȀāǾȟwǓђ\u03a2-ɋîˋKɵЗŃÐŲӆҢʏѡT\u038dϒɎ\x93ȹǊ',
                            'ɜDкŏοȝɵЦĩþYŕƳаβŔȁťʷІȬɗyԧˇŸɁѼʽɔ',
                            'ϖԒҽԜ\x7fќч°ƫӃȜɋɚѻ²ˁ',
                            'ǷɾϨŃѨ×8˩ѫªŊƮ$ԄҒΆǐίҭƘ\x96ǫɗΓϢЮ¦ɲпǻ',
                            'ɶԭү·VʫїΗĐӷǱ\x8aɸԧìȻӏӁƈЏ4ΡĈʺ˭ǻӬѠέƃ',
                            'Ѕǽƒ=ΓϚőˌξсÝԍP˻Љ˥ƅϮƶǃûƷ\x8cԄǧԙӉӔӝҴ',
                            'ИÆҤƗВŗЭϼ\u0383č˯óʢљȿƍҁ1ӿ\x8fʔ¿ёӎYψӳˎ×ʊ',
                        ],
                },
                {
                    'name': 'ƄӝùʨŅĊǮäFɔμн@ɉǗˍђƛԤó`ƠƻƼΔ˲^Ŏ®˨',
                    'version': [
                            -4813647247716668590,
                            -7402672942145588238,
                            -2046108757358589592,
                        ],
                    'about': 'ĘЂÐƨėƀǬʍǕҪƴΐɄȻǤҸ҇ΥˤќʒіƴðЅÛʡһɥѰ',
                    'description': 'Ȗÿ4˷š/Òȸ6ωŶӡǎнИƢҙԮί˲˳ƨłVǵíƽʫoӺ',
                    'authors': [
                            '\x8bɶǩǭˎǕλƔȮϓɧǋƎGЧϸȬƩμѝĢǼέMԊΝƆҹ\x90ö',
                            'ȢϾɓΤǛĎǥϪǪЪͳіƘǗοǷҰ\x86ћҌ\u038dǸͿɽĩŀŴмέΓ',
                            '\x92ϡϣӒƫСΪȝҹËŏǙΏͼɦʃҩ\x8f΄Ądǡ˞ƙǞÖǥɺǊǋ',
                            'ƫöʠӭʗŚʴ\x8fĽЖʟΡĶH\u038bëˢΎƪ\x97ϡĉвͺʭ\x80\x8b20\x9b',
                            '˛ǔА˭Ŗ]ʯ˰ҿћɔȗõʈϐȹŉͽǩõӎKϞȤīǚӟ4ɛí',
                            '\u0378ӘȇņҍͿǖáĭϧʆƪƽҋӐîӠǀӜķPк˦êҘфǫ÷',
                            'ɱǇʩĪȼĖԠͱɣ\x9aҿΞm˵әˑѦzÞǻçʡӆƆȃËĲīÈȝ',
                            'ӽĻȷҩͲ\x8b˘ΑȤɪ˖łɐ\x9fƌΊ˜ʺӶӘƙËʁ5ŇԞƔʨʂǮ',
                            'Ҭй',
                            'Ѓ¨ԎȖȷVʶѥƀOɦȺҙΛϲνĊ˷ĕΩΐГάDǽsβƟƥӚ',
                        ],
                    'licenses': [
                            '˶ϼ#Ù\x88Еǐɿ͵ʵӿʹǤԇƼŪШȦɬʌЎ˸zӌźƑȖÿτѳ',
                            'ѸԋȗΆзҰӳϣˌƋʵ˷ҶϹǍɻƩĕѪ®ɰĔÊ\x8aϦɎũΡ҉ƣ',
                        ],
                },
                {
                    'name': 'ĺƮ¡Ӕ˖í˧Ȍʀ?Ã`҃ńʣĺÀ½ɒΘĶēƛĻіȯŝԛ˥ҙ',
                    'version': [
                            -8627992766226169161,
                            -2625163930441891802,
                            -2465210070697194538,
                        ],
                    'about': "ȋԕ'ԄфçΊǻȇk²ίфрǌĩѾƛÉūӫ˄ʿͼHĿђҞʜƔ",
                    'description': 'һĨƈɑсǙȄlȘťήʣŏ˫ә˥çȋŷȟѣσɻˊŖЎқӓ½!',
                    'authors': [
                            'ɟͽȷOÂΖɝĭǵʒϛБВы˨ϒʢτʭ˽λνƇǑǧ',
                            "ñљϚ'Ϣү˒ğ҆ƊΗŲӸԇȀ҄0˽лӇƏǘԣϧΪҝ\xa0ˈpȔ",
                            'ӢȡƏ7љ\x8fӏпӪ\u038bˇӄԘĸғɫӚȶ8ɷДǖʥ±ѿǎNDʝҿ',
                            'șʙC|ǇϷ\x97ǋҽθˈ¤ʆǱͰ©çʟąɠͲëłɵȎуƺģҫƤ',
                            'ɤǻɼ\x8d˸ƜіƗżɁ˄Ǥǋǋ\x9dҩoӗȏƫƂΎɋʝ"]ȗ˾ͳ½',
                            'җ,ԝıӗɱ˟\x8eи˜ʋ˙ѓǶö]ßˁ\u0383Ł҃ȋ±дԑӷп\x81ɔŨ',
                            'ķʕ\x97ʏŇӬ˩K`ɾԦпѬǒϞʓӱǎÉΪǨ>Ѓж¨ɧļƏ\x89˕',
                            'ԞéʘŕƶȼĊ˔ҬѺkȤǋȭқÌơɿƕːϫҠѪƟ\u0378ѰƤһ',
                            'ĤʗҊɿ²ØŬΛɔиɂԫȡǞѽәĈƤÉǃǘɖîȗьȌƚϟ˟ɚ',
                            'ΫĊҖđѺұӯȶɩɔǱ$ĺ˖®',
                        ],
                    'licenses': [
                            'ͷϱƉŸĄȤ6ͻǔћĿԚϫɗˈмʛЫƽƻƫ¿ŃɶȹѹȂsƛǴ',
                            '¾ƃśϼ˯ӄӰЉϯфÄҥ˽҉ҞҥԐúͰȅ¯ЬʾӝϙȶȊԜԧɛ',
                            'ʲʅʪЯӮÚMԚҖˡ˛ǖʋϠ\u0383ĺ˞πӻƻîŉϒtЯΗ6*ѝĻ',
                            'Ƅ0ȽÁϺћԄ\x94ԦƇȗƁʻѪ;ǡӫКϷĦ˂Ѡʴ.ȽԂҪФжё',
                            'ʓÙβЂƦɲȎӧǏЮВȳ ĔǕҋӭvЄЄϊʂљüçҶ\x89ѕΈː',
                            'ʫ˵ÝιÕσ.ďԀìŦяÁŌl«ɥǷiҿÃāѹӺΐуŶƤáȖ',
                            'ӣϢԖʻķѬ¨îӴï\x9böǐԃéɂXˏÒЯ$ҧҚ¸˒ĳίӑÊɩ',
                        ],
                },
                {
                    'name': 'ʎ΄YʿÜȖǉǧіrÿȁɍŻTΖĀҿΪʄѯΏҏ\x92ϰӌŉѲΝƄ',
                    'version': [
                            -511673006879166950,
                            -228476545657499534,
                            -6501191005366402679,
                        ],
                    'about': 'Ŧ\x7fϣʖǾƵZЄ>υK҄ͱƍÞģ-έϪѯύӴѡȆˌǟχБпȳ',
                    'description': 'ƈƎȃүƧԪȒɼѢĳӶƊȑŧм¢ԇʰFɅəoΠӠſΖ\x8fƒҊҹ',
                    'authors': [
                            'ϹǨʷȳɤэˊϝäąԏÞ\x9dȋ°ú_\x9cǮwʛ¦ɯŞʞƚĬЯʷ2',
                            'ôбЪю]Ӛ`ÁϟûŶŔȖЯӋύԛ÷8ȭҳƴČĔй\x9enEϞɩ',
                            'ϧǕεΞīЀȖB˥\x87\x93ɗ ºԕҽŬљȥӎӀԐĻͱɳԕ\x99µDǅ',
                            'ƶӉɊѯŻƱԌżČμƩɄɚȼ\xa0ɽÅ>ǟӒіǊ\x8bϿƄμȒØƽĥ',
                            '\\NϔƴќƸӚɇʢņưчZԔ\x8eǖ˰ЈȬ~ėˆԠЗɫ˶Àęδӫ',
                            'ňɐҙĔρǕϗϓʄĻϝͽβϹǋϯ ʻˌɋʈőĽɋΟɘ\x9dˀҀη',
                            'НӐ\x86ўƇπʊǹƴÊɢȢ',
                            'ӦЊȌZѿu˛ЎɄҪͱǚ9śƇɇ[ǻƝρrQĨћêҿЩԐǤę',
                            'ԧÎ|Aʚˇ|ͿԦǙlʑ\x85ӱü\x99ӜȮƴӤѬӚκʅ2îӎʪщΘ',
                            '˸еĭɖҘҔμȓÝɏʎáӄƦ¹\x9aɍӪ¥@ҴǉљÈ\u03a2Ϙˊ$¹ɰ',
                        ],
                    'licenses': [
                            '+ςŸÒĴѷҐˏĭο˝нǲƈЄҤʾĺȄ\x8dʰҖɇ¯\u0382Ӣшԭȭĉ',
                            '·ǤǮϒʈ\x8aƊòĦȵƑЇėˬİе˂ѵԃĦ«и˽λɋѢўЙҝʂ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'extensions': [
                {
                    'name': '҈ŖͰ',
                    'version': [
                            -356847544719329733,
                            -682892893658976788,
                            -4794723261097187012,
                        ],
                    'about': '',
                    'description': '',
                    'authors': [
                        ],
                    'licenses': [
                        ],
                },
            ],

        },
    ),
]
