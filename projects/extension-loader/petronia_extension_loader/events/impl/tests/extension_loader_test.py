# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-08T21:23:11.276348

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
            'name': 'àôаʎ#%ʪɿԦʈĆÂɯ~ːƭɿÎ³ΙΐҏҔӷӦ˽ǷrPͼ',
            'minimum_version': [
                -6370832687880430834,
                -5566619956817424528,
                -3248411709554040464,
            ],
            'below_version': [
                -4695670845345857169,
                -8210112511954881450,
                -9111172891349351967,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ΜėT',

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
            '$': 'ωơ˴;ĚӷǣɴɭΫɪӓɬ\x97вʭǚVǒNăɏ:ѸжÅΝӓɴA',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 7191623691649065821,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 302193.00585561234,
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
            '$': '20210208:212311.210595:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ðΕ\\Ȯ˩ΕƳӑжƔˆƵŊʁǊßμ΄fȻüÒƣǥ\x86öʯǲӳɂ',
                'ɂӪŢˡϗϳъÇ\x93ӻϵǹдϪʿƜЂ˘ύûƔˍ˲ŠɗԅʷΌћƮ',
                'ʢſƥ_Ԫ²ȪԆßů=ѧдϔ˯ї(ϤIĢ\u0379ʵȗӝЊȶſĴˢˮ',
                'ƸҭʅɟŎӟҽæϋӿ~ŗθҬěԍӾЎʠGоΊѬPф§\x8aҝ¬Ģ',
                "ΓhӏPɽæǱʨұeyǁˊ\x9fîΠҭԩ'{ƛƕɴğɹūЇȒοй",
                '`ʛԇК˶ҏΆăʧ˃#ϦԫӀɠұˤvʋƝʻϻʃԆŧ$ѫҫʞԟ',
                'ʰĚqˤtɿɡɨЄΒĬĜώǶώ±ТыœΧУіòɽƝÞtʢЭ_',
                ':ϢưʦƤøſӉЌҋΠľʗӢɅ,ӌ¹НлЙԦΚǣğȰ²Č=ˏ',
                'ɏήӘз\x80"ԂBŸȹѼӚˀϩϳǉĴΉӯɲΥǱȳƽ~μȵȣűʔ',
                'àΞѰ˃˞ɽТãƨўęřùǲʱȣĚǜ¿ǂЁĕXîˎӑ|űΉͼ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -3496568171034702522,
                -2742155724033644364,
                2749945236456506674,
                4632659890047872801,
                -3194313306117432108,
                -5986240413969615745,
                990392010468313786,
                6608596563662294289,
                6075291655743282467,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                348718.54482968926,
                815283.9211885553,
                138307.01070613886,
                497571.90508629556,
                -2337.9629158774624,
                657217.9621499501,
                792893.968803039,
                -83193.90348063034,
                424980.89243495127,
                972913.9960345742,
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
                '20210208:212311.211384:+0000',
                '20210208:212311.211393:+0000',
                '20210208:212311.211399:+0000',
                '20210208:212311.211403:+0000',
                '20210208:212311.211408:+0000',
                '20210208:212311.211412:+0000',
                '20210208:212311.211417:+0000',
                '20210208:212311.211421:+0000',
                '20210208:212311.211425:+0000',
                '20210208:212311.211430:+0000',
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
            'name': 'ӲlҷƆƁΚÙʑԉöǋϱʣҢ@ÉБ',
            'value': {
                '^': 'int_list',
                '$': [
                    6667008981200157995,
                    -303736595938332306,
                    -238203216225834036,
                    7698980609971184611,
                    4513887137082648961,
                    5603759224628340469,
                    -6299189693717807519,
                    -5427323499178797548,
                    -7532908140795434463,
                    -2145524804600947269,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ă',

            'value': {
                '^': 'bool',
                '$': True,
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
            'catalog': 'Ϗɟ×ñóĲΤƭʶɠԆӨЪρ˄fǬ@҃оƋBεɚŋϙ.ɍɑΕ',
            'message': 'Ώ,|˞àĞȲΎůϛɴХɜϲɑѤƂӌңΕǵЪǒ˄ȮӁǓ\x93Ʉԟ',
            'arguments': [
                {
                    'name': 'ɐϮйį˷÷CδʢǞьΜƔǾɀȢЈűԭеϺѤҁ³ʳԥȣͳϱh',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        286596.6259800764,
                                        25317.41200399748,
                                        115352.67201801378,
                                        345504.65257800085,
                                        -25696.235625057394,
                                        136945.91823031218,
                                        831791.9276978122,
                                        844054.33721274,
                                        456702.64751617657,
                                        932301.443765991,
                                    ],
                        },
                },
                {
                    'name': 'ϯ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210208:212311.208401:+0000',
                        },
                },
                {
                    'name': '\u0379ƫϲȃӕʑƻʀȥƴҿή´ʯ@ƉˏɌӲԐӝм˻ϽǃѳɃ<Ȍԫ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ѲƱİ΅Ҵǲǌ\x98H°ЋІԡΙÛũ\\Ѻӆ˻ЊȵƇʹ|˾рԧĿ>',
                                        'ɜϗPŹƇӀǬɨԚ˚ˎwЖƟѧ˙ΣŰxԒɩˁŗô¥ɀòӜԜџ',
                                        'Җ˖νѶԔǪɎ˙ȌЄŮǛӌӷ7\xa0ІǊΕӞѦʂкƑɩːȩþƳċ',
                                        'ƎŽĊоϿDʬѼǟ\x8fӈψ˟˲ϻɞ˄Čɴԫ£˓ϐȜҧѧÓѓ@ˬ',
                                        'Зүǳ˘ӝΥɐүçӼƙ¡ǴÊʨԒѺŸƫÆҁФŸŠ[шѫɿԦ\u0379',
                                        'τǉҒƌҢ҆R%ƌø\x9bдUѾˎў#ӷȋѳǜ«ϼ|ċʁϏ\x9dĦŰ',
                                        'ɼʟӀίōγǒŌɇП˷T7^>ƼҰШŋԦżõϑԕƓʊǎ%¤Њ',
                                        "'лċ+ÓȅÌç҂˟ŔѰ/ɩQÔʑʞǊ˺Ϝđ2Λ\u0379áágΥө",
                                        'ϻϨΊϺœȂГɎČԑyƚɤǜƷʥάɑΪůˏƬˠіĞϞɟĎӢƚ',
                                        'ȗőĹ\u0379Ӯ4Ŝʝ˘σҏɂπɧ˙ĎԉǊОŵ¼ήӕ\x7fî˱ήш¨є',
                                    ],
                        },
                },
                {
                    'name': '\u0379Ĝ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ȹӺʇƸѦ',
                    'value': {
                            '^': 'int',
                            '$': -3296044294152764444,
                        },
                },
                {
                    'name': 'ҌȬż\x98ƼǍƚǔĪӿ\u038dҿˉ{ȊǺ\x8bʼërƵϪƇӭȼüƪ˧iď',
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
                {
                    'name': 'ȜXȫʶēŹ¦ƄȁʳŴMɃbƸ\u038bƝɭ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ΈΫċ©9ʩсˣѸδđţ,ʞҬҶˤʛѶɋƇƲӮɔ{°рƪӓ9',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -3907035596156459937,
                                        -6238115075215072724,
                                        8747696349522662139,
                                        7487597368464095832,
                                        4762668483693739079,
                                        -2691256180940718329,
                                        -8198579411764417373,
                                        6054770229705632275,
                                        6560381741930704494,
                                        -3641090617812327811,
                                    ],
                        },
                },
                {
                    'name': 'ΉļȒ\u0380ŏϨ҂ƆљȐӚѤʁ(ƔƙҤ¬Ԥ÷ЄŌͲƘųʅˤɟǖ˵',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        450595.15355745214,
                                        13960.311801602234,
                                        567837.5879239385,
                                        269561.6786843836,
                                        768194.0239095974,
                                        707728.4767929952,
                                        -63486.02679454598,
                                        107891.09561971462,
                                        88840.70655785294,
                                        228809.25116034655,
                                    ],
                        },
                },
                {
                    'name': '¬Ԓ',
                    'value': {
                            '^': 'float',
                            '$': 486676.7411038433,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ýϋ',

            'message': 'Ε',

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
            'identifier': 'ɍnӒɜЊğϹӿҳ\x98Ϋʹ϶zϿƂЯǩ{\x8bҊȿтѮ£÷ӉˉɅȣ',
            'categories': [
                'os',
                'access-restriction',
                'network',
                'invalid-user-action',
                'file',
                'configuration',
                'invalid-user-action',
                'internal',
                'configuration',
                'os',
            ],
            'source': "ˈ'`˨ѶԦ҂ѱʯãǂǾȱ\x8fκaťԈƒqȣˈȤԎӲϣѦʣ\u0382ˆ",
            'messages': [
                {
                    'catalog': 'ůɟ0\u0381Č¿Άb˼ʱϝѠVϪgǵǪқϴÎӥσΠøԫ\x90ӱӣѭ\x8f',
                    'message': 'ɡʻÀӍ\u0379әљŒq˄ƪҲď0ťзЉԘɸɎÎāʈќʛѰĠщǝŦ',
                    'arguments': [
                            {
                                        'name': 'ǅćɎԊȂŗҝ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8616149027899720153,
                                                    },
                                    },
                            {
                                        'name': '¶҄²ҾϛȭΓ\x9f',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԕӦӽ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            644065.8335611477,
                                                                            888792.2241620423,
                                                                            23836.769612639604,
                                                                            470568.9818626649,
                                                                            -62973.02289321377,
                                                                            36634.077826379595,
                                                                            185312.5573783061,
                                                                            691106.5330990324,
                                                                            732018.344976885,
                                                                            143220.06669382646,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѨϯΞ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 282668.5275068148,
                                                    },
                                    },
                            {
                                        'name': '{Ⱦ/',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212311.183101:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ö?ЬǹѸÂ˟γϖЊśǗěȀƃƵ\\_\x9bπȰԣɄȶыӫɉ%\u0381Ӧ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212311.183253:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĚͳàҨϧҦ\x99ϰũл_˟UӝPϰ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7949457703078985080,
                                                    },
                                    },
                            {
                                        'name': 'ĵȹʤƒΩʞ\xadȓҬiƘэiʒŏәӽЉј',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3643596524932886808,
                                                                            -6814163190302715783,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x7f\x98HЕоɀ(ĉ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            150844.25584989853,
                                                                            782104.8714524852,
                                                                            677925.4429547178,
                                                                            673281.2272791921,
                                                                            280.47650944533234,
                                                                            275873.8628695727,
                                                                            384247.1485359155,
                                                                            293386.63563344226,
                                                                            43189.8431596561,
                                                                            332357.26750196837,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'άİӰӗUƭ½ģÀćȃȮ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            253204.3435173516,
                                                                            596119.9824258952,
                                                                            109778.5643382156,
                                                                            268240.79775731376,
                                                                            224456.1783876156,
                                                                            628565.7380844546,
                                                                            235979.6883517768,
                                                                            -57235.794329421384,
                                                                            564236.0230717569,
                                                                            827886.5032767536,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '¡ӽĭșĭǊʙ˫ѹϲƷTƍĴћìǣЍіӊλϩѥʩÁǿʑœ½ɿ',
                    'message': 'ԍ`Ӣ˳ѨƧž˸ľÊφȋXŖü!ɾΡɐɒΐ\x82Ҩ)Ǚ˘ҲѸϑх',
                    'arguments': [
                            {
                                        'name': 'ҾҒѓʃҎҬƦǐ˝ÍĞőþӴɉԪ/ıƞǀԚ҇ŞĀŃӾϪέ˗˰',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            726552.6357361386,
                                                                            582591.5242441037,
                                                                            622086.346551342,
                                                                            78916.08697319543,
                                                                            894919.5380824885,
                                                                            240609.35214901506,
                                                                            220744.21669082274,
                                                                            370789.04904904374,
                                                                            115321.10772983203,
                                                                            780081.521084075,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƈƹcʳtƐȴ³Ԛ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѥˈYƠҋϦİːӣϳõɺjЗ҃Ńї[½ŁqŒˢǰţХЎӹΈӎ',
                                                    },
                                    },
                            {
                                        'name': 'ƐÜь\x8až¸íąƬы',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212311.184808:+0000',
                                                                            '20210208:212311.184818:+0000',
                                                                            '20210208:212311.184824:+0000',
                                                                            '20210208:212311.184829:+0000',
                                                                            '20210208:212311.184833:+0000',
                                                                            '20210208:212311.184838:+0000',
                                                                            '20210208:212311.184843:+0000',
                                                                            '20210208:212311.184847:+0000',
                                                                            '20210208:212311.184852:+0000',
                                                                            '20210208:212311.184856:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҩŸКʜ˂ZҺ\x90Ċέ\x85˶ʌϽÎƳǙǴɣɌ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '´ҼˁˊǎĪσѷӱԎυЦǰ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212311.185431:+0000',
                                                                            '20210208:212311.185444:+0000',
                                                                            '20210208:212311.185450:+0000',
                                                                            '20210208:212311.185454:+0000',
                                                                            '20210208:212311.185459:+0000',
                                                                            '20210208:212311.185464:+0000',
                                                                            '20210208:212311.185469:+0000',
                                                                            '20210208:212311.185473:+0000',
                                                                            '20210208:212311.185478:+0000',
                                                                            '20210208:212311.185483:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ñ˼ҌɾǜɰȇybΊй'+Άσ\x96Ȉ¥\x9aǫмˋфӥȕ",
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '¬ĜΒӄųÙһɡԘuŠ\x8eʐԛˢşњɬǯҧЄͶϼØЅґϳȣ4ʳ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ю`ʊVљɈΒǁĪћŦФȢşцǡҹЀîο˻9ɿ²ӟҨѪȏȃт',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1906475634110548159,
                                                    },
                                    },
                            {
                                        'name': 'ΰҡʍРŸӃӘѐΌҬ˥ϢͻŠӢŜԒñɽѽõѽʔ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ЭĩѬɛý',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Όˌɢƴ҇ңъƛƇ',
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'єЄӋ}ɋ\x9cɞvМƟɘĴѳǙĒbƅӄ\x8bȵƪ\x93ϾĈ˰ƳΌɪńØ',
                    'message': 'ȯǬѕˠ˘ψΎˎǕƌʇǮǒħĠȞƠɪǂȍɺЌξʇӃԗȹ\x91Ώĉ',
                    'arguments': [
                            {
                                        'name': '«ςƝѫϵѨҬӍψƂЌǏǭҽԐϲΜȗЛАͰΛˬѤĘЩżʖϵΨ',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԅ°ΔŦÌͲіλӞɗ·ɛΪ9ãʁ¦ɖ϶ϸӌω',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'JŏƏҳ0ǘǡʸŃÐǊχ<НsȑԓĈȾÝƩ\x9eЍȽȂΈvˊҽə',
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҟ\x88ԞѦƽ˩ȼŇӍ¥˹ɛӞÞΜξoȥĕeȗˎĪҏБǇǟ˜Ýϛ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212311.187960:+0000',
                                                                            '20210208:212311.187992:+0000',
                                                                            '20210208:212311.188000:+0000',
                                                                            '20210208:212311.188005:+0000',
                                                                            '20210208:212311.188010:+0000',
                                                                            '20210208:212311.188015:+0000',
                                                                            '20210208:212311.188019:+0000',
                                                                            '20210208:212311.188024:+0000',
                                                                            '20210208:212311.188029:+0000',
                                                                            '20210208:212311.188033:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʬ\xadѶŝǻˬӯʚёÈͲҮǱӇĥҜ#ϙ;ɉĲ\x90˻ɑЄǢ\x8b¥д\x97',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ζÐрʻȞĔɁɜ\u0378ϛËӉͶЧ˺фa˞Ȫ˘Îȷ@ˁҕ:x',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8354980217061740256,
                                                    },
                                    },
                            {
                                        'name': '\u0382ŁɩĖģԧWʕŲǭʏҹǈ)ãԣ҂ʧҧĀÊɽӢҨɳǓSʆď',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5860642423502626357,
                                                                            -4902466576184655266,
                                                                            -3355478955381169535,
                                                                            -7058569129771842769,
                                                                            6148692101542189687,
                                                                            -931895833725873537,
                                                                            -9116859472277294273,
                                                                            8370151849079585626,
                                                                            4659250267868528081,
                                                                            -6622444192835187378,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʬϏʶӀ˓ȽӼļԁʽο҂ːĉˬҷɔɈãү\x9eǽñ˛ѥΉťĒσÖ',
                    'message': 'ԎЅҊȴаǖȽѥɂǍͷԑ˷Ʒ˞ίɐgƉɝѠʲӑȃžɫŀҞȒ΄',
                    'arguments': [
                            {
                                        'name': 'ŔҷѰѕȦʨ˦ҙӦˌɧ\x91ϗƦw˚ˍʦŐ>ΑϽˬӆ\x83҅\x95ИɼЀ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'níӝǘɬӌоӆѴˉγÚ',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǧɦƛԘҾǶȥpMӹűÏơĕ\x95Ȑ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 924976.756139346,
                                                    },
                                    },
                            {
                                        'name': 'Ҏ¶ǘ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'һôҢҙӀïҲʼ\\ɱʑ\x86ųɘҤ¼ȽΏφƂТˈĎɎǨȇηËʸӱ',
                                                    },
                                    },
                            {
                                        'name': 'ƋҦ˻ѵԡēPюԄԇήЃǋҸǹǢŕρƏ҅ЯˎѡɕĂƐΈωɕƫ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'N˦©ȝ¿ɽӿ!\u0379пˇPӬΐĢȒƕǞѓʉÆ\x99ȍԬƟȦ\x94ӍřԚ',
                                                                            'ʷƦΆñГZčԪ×Ȳɑћѽ(ǑϤʿĐ˅ҍɶºӌ\x89_ԕ΄µˠ¢',
                                                                            'Ѯ¡ʆĄϟԈĎ`ŝҙőҘӝƐϋ˦Ǔ\x84˘Ƽ҉ǖιωѝÆŬ~Ûʻ',
                                                                            'ЙµǝĮԧЧ҂ʗ\x9b˟ˣѾǮӞϯqѹ΄}ԥɪǹÞƒϳԌʎЇӥȣ',
                                                                            'έɋѢΏҪхÞЯȳҞŞƀǍЇȠҒƜ5ҺźƮ%ʜȥŊǀňwÎҺ',
                                                                            'нҚҪԠʢĒǮǂØΣ.ȅɍϡ\x97ҎΑʈʄ¿ŢİɹˏŬ\x99ȿÐŲΑ',
                                                                            'ьĔIŀmҔƻMϑȂ\x8aӒ\x7fqҷ\xadņċ˃ύąԦϧ£«Þį˘\x80Ӈ',
                                                                            'ҫǄòʡѽtЪǕŕӐӼэń˽ȓ_ʖұȍǝ˓wȡtGЄ{ҔѬӜ',
                                                                            'јĹtԢ:ѬʪҁĨ˭юѵȒΌă|ŒҸԠӊǤў˹ԈƍŽóɊϖъ',
                                                                            'ѽpϋǟőϯʽϙωЍЉ\x96ȫӶϴƅӁҭ˄ѱģǂȣϞ˅˾ʭŤ\u0380ö',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϝɨǢѰϡғΜÙŞҮÄƐȕгȼ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ϓґ<σŻҎŜҫƕǟάȝӜóģʳȧʖÒAXŊҧǭӉ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǊɣʶȀȔĖ\x94{űTQųҠʴ˝ԇщʊбʧҙƑ\x88ϸӝœŜхҩƇ',
                                                                            'žȵ¥ЩȈȬīүџǬʎǾEϫʴԠнРg˪ñГҞhÃԤʇūȬі',
                                                                            'ҧԮƈΓğ\x93ŬĔԄƍʈ˓ŠɝăƞшΑüѠӜéː϶ԖʵȂƘĵÝ',
                                                                            'ԉ\x8eϗϪѮіѥёІ\x8c\xadьſͼͲˤиōнǓǸ\x9dɆƫ\u0379ѺΓΟΔҺ',
                                                                            'ıĂΓȕÈÓАlԍԞπǽýĸӁчo˫ǺƁªԝ\x94ӟ˽əȧƨӄˢ',
                                                                            'tƩīνˋѡWŚόǼωϳmŪìʶοԑĮŊԛā˰²ФΑѵЕȧё',
                                                                            'ǣӚ\u0381ЌúˁʟŹȽu_ӊ˙ʗʽ\u038dɄ\x97ѸǫöˏΉԡ°\x8bƳϷ\u03a2Ѓ',
                                                                            'ɪÌ¹¿5ɃϚƂȣ҈АӚÇʣ\x84˼еȆϚͰʙ˸ͶԨ`Τʜȱñ˔',
                                                                            "Ūӛҫ\x8eͻ5ϙϿǯ6ɭғСǤδФUĞɪϦȃŐ˅èη˥Ҟ'lW",
                                                                            'ӧГ«Ĝ°ǜŃU|фԇöĄwįƽԓ~ź0ËӮĲҡѢȩŢÇĞƶ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˔ѷźĥґέґǩǕ®ΝÙǩжЦӮԦӇ\x80˪ŢËǐҖз',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3301308436206263625,
                                                    },
                                    },
                            {
                                        'name': 'Ūɉa\x9bʸɷĠπЈ˷\x88ƫ҉ιƬΡÝϑДΖ΄ď%ԪҞ6ȯɰÝв',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212311.191150:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǃіΞˇǮ\x9aɘJπèąŁҸɅ˓аҼӝǃFʿϺҰƅˌɢδѨ˽Ɋ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2185587445551724116,
                                                                            -3654376213461403315,
                                                                            9115140566691922210,
                                                                            5735405874189447270,
                                                                            8997334521337699374,
                                                                            -8346758936033443030,
                                                                            5399164112028299441,
                                                                            -4028510550308933283,
                                                                            -7962063732107679571,
                                                                            3794197830871436861,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ťËԕѾғѐϼ',
                    'message': '¾ȟǠӊѥʄԓHͽ/іȯɥçÕȠ҅ēӦźtɓȗˡѤ˖éӌțΞ',
                    'arguments': [
                            {
                                        'name': 'Ωʅő΄ѹk(',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212311.191846:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҧȣ\x90ʃ͵\u038dˎΤʹlѽBɆЇÌУˏΟŠ˳ȝãΡѕÍЫͷĚҤѩ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -72801.69042118048,
                                                    },
                                    },
                            {
                                        'name': 'ȮʑΧйѬĎӚƺ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212311.192143:+0000',
                                                                            '20210208:212311.192154:+0000',
                                                                            '20210208:212311.192160:+0000',
                                                                            '20210208:212311.192166:+0000',
                                                                            '20210208:212311.192172:+0000',
                                                                            '20210208:212311.192178:+0000',
                                                                            '20210208:212311.192183:+0000',
                                                                            '20210208:212311.192188:+0000',
                                                                            '20210208:212311.192193:+0000',
                                                                            '20210208:212311.192198:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'љηˠҁщ·ʲʀƦԗˮά\x85ʰӄĸ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'χǞц\u0380Ǔ«ö³ĴώńΟgƁk¯˲ˣЌBәφ΄ɉϴƃЈʚŢ҄',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 684934.4453713626,
                                                    },
                                    },
                            {
                                        'name': 'Ȧſ^\x95ǨъʮɒЛҤîΜҟǞ0ήƪЇӸӓͰҊɬßБρkÊӿũ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĨˊƑĜ@ĪϞϢōƷ˒эԍіԈȽBЏļțɉÛэ\u0380ɇʓƣɉаК',
                                                    },
                                    },
                            {
                                        'name': "ͱʵôǝϤЀ˞ϦϤӼ\x96ԐZДÁҤʉȴɽ'",
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҿɳɌƝ!Һ.1ѳđӵиâψȬԁԙԭʑҴƍύʐΤņҋʦɦĩ\x9b',
                                                    },
                                    },
                            {
                                        'name': 'ũȘҫʉǓ\x99ǚʻʩǾԐ_ωξϯóΣӁɛзÇʛŇϜ\x92˨ЧɬǌͰ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212311.193160:+0000',
                                                    },
                                    },
                            {
                                        'name': 'șɎӐ@шԎĮ\x86ѼŽˆӍ˴ɔÔӷͷţσƕҁȻĤŀʉş@\x89Lƀ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2143161766022247797,
                                                    },
                                    },
                            {
                                        'name': 'ӕ϶ԉŏϱȮȬ҆ʑŭӿʫ˒Ӵ³lȑΔçӺѩԞΙǞЗđ˸ƝͻɎ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ơˬ}ǑӯцϹPġĂƀιũɼīʌ\x9dƒ\x7fǻŨԟѺӁ%Ӷ>ϋǳ\x80',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȋћѵǩŠǻѵѝϭʨԋʅəжǅēӔɯʶʃ˘ҩȨӹ{Ȏȍ˃ћȚ',
                    'message': 'ȫϒԋԔƿnƪҟΏ˻ԠɢŹлoĽΙɠеĥÄϏ\x81˙ɁɮƆɩôА',
                    'arguments': [
                            {
                                        'name': 'ԈǰŤʹĞȜӱĜɏųġ;σ{ȸȆˋžӇ\x7fԓ\xadʵčȴțȇʓȍŋ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 18824.3635886961,
                                                    },
                                    },
                            {
                                        'name': "ȁѭ\x9c\x8eƽΙɓ\x8aα¿Ҹáɽ'ˮҦǭ",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɏȦƭr҇дӘέȊϡUɍщƄèZAʤƺƴҁЁʹƮ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212311.194194:+0000',
                                                                            '20210208:212311.194206:+0000',
                                                                            '20210208:212311.194213:+0000',
                                                                            '20210208:212311.194219:+0000',
                                                                            '20210208:212311.194224:+0000',
                                                                            '20210208:212311.194230:+0000',
                                                                            '20210208:212311.194235:+0000',
                                                                            '20210208:212311.194240:+0000',
                                                                            '20210208:212311.194245:+0000',
                                                                            '20210208:212311.194250:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '´ʹͿȓpҫˠЙưҨϕԕӳʩǨ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212311.194488:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ϝɧȳ³ϿūЕ˧ΝˆĢАӈɃ˒',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7687787932797443794,
                                                    },
                                    },
                            {
                                        'name': 'Rűјϟ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212311.194761:+0000',
                                                                            '20210208:212311.194770:+0000',
                                                                            '20210208:212311.194777:+0000',
                                                                            '20210208:212311.194782:+0000',
                                                                            '20210208:212311.194788:+0000',
                                                                            '20210208:212311.194793:+0000',
                                                                            '20210208:212311.194798:+0000',
                                                                            '20210208:212311.194804:+0000',
                                                                            '20210208:212311.194809:+0000',
                                                                            '20210208:212311.194814:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӂ˒ˢ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'мȢĹΩҵ\u0382ÙƃɕZfѥѐʮбҋѡǤͼȄϚ?Ҝǧ˜ŅŘĽЈӷ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "'}ѪŸǲǺjŏƭƚВ\x99Ē\u038dΉƋ\x90ˣГзәѨƹχϳ˗гưɠԨ",
                                                    },
                                    },
                            {
                                        'name': 'φñɂsάҒԂȽЧԋԝѨЫюϜɎЁҸРôԙцĲѽƥҜĈ\x8cПґ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Δ˽ǤџӒƌϞĖa¸ʽFԦ˫ȪɧƣɃЕêΔИ\x8dЙɭΐνBƒѰ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ūƕȏŶѶiǻɿѫȉθΗƯ(ɍ˾юԡɓϑϒŕʯϻ\x92ʖUdͳѪ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'εą˪ˁĲŐ·\u038dтÄ˸ŌӱĚʡJƺΰȿűÌҾ',
                    'message': 'Əˤω˔ēԏӰ\x9aɭӐԅρǂϘґ\x90ƛÕΎEҽ±Ьήλө«ҝ˅ƙ',
                    'arguments': [
                            {
                                        'name': 'ϽΫ²»ѡÒΛťʦƛű\u0378ӤŝӻҤБīѠҔ½Ź"ʶ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6698274071219394759,
                                                                            2624754052557863412,
                                                                            5501478814605360462,
                                                                            -9079514931569342671,
                                                                            6276644853910534206,
                                                                            -210438106523890996,
                                                                            2599356682001674156,
                                                                            -3452751209862551453,
                                                                            3632449426946839781,
                                                                            -8854726894155190837,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɲɜɁшΫŭҨФыϻēζ҅Ј\x8d',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4184999031005894152,
                                                                            -2191066023848242669,
                                                                            -1596794128287054633,
                                                                            813460495745582548,
                                                                            -8111807237876622311,
                                                                            -7956246392160894261,
                                                                            -3821390788832927465,
                                                                            8802668102273111283,
                                                                            -8070162719142247515,
                                                                            -3735727698581353282,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˾ԧкǃCĿ˜Ķˈ@˭ҥʷӯ϶ŌǗ½ӉŸHŜƯ@ʺ¯ũgɓ˥',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x9fϪê:ķëĚ\x89DňѰ˾҄ȃƸͻû?&ѐϫƣОӺǾυώΥӉɤ',
                                                                            'ȃȽ<Ƚʕ\x88ÏϺ˸§ąG]҃ʝȸԝŃȤԐιO¹АϤJɒ\u0381MƓ',
                                                                            'Ȼ^ȅƲӋ«ƛɜ\x88řж8ѫˍѐĂ>ɀ\x9dԤʽЀʛϮșɢ˨ŊϑѸ',
                                                                            'ιʎҶŞҌԝȤŇүfùҵʢ\x97;\u0378ķ®ȉŨɫũƅĒőˡѓœдѰ',
                                                                            'Ԕԓŧɛ`ʌʽʧȟŨɧҷëξȨΎɛԨγśɬŰµ\x86ӿȏъˊ2ɞ',
                                                                            'Èɠ\x88¥ȌşζʮБƝčɈĢ®ԙͰɅÎʾ\xadϮөûŪжòЯѓïӑ',
                                                                            'ӂэ΄ǹǞʦsưS\\хɰԌĵԅνλрʲοѨmàzŢ}ҡЬÛƕ',
                                                                            'Ύ]1ƲʁÑČƆԈІ˥ǏѠŖͲȒаъŹҴԌDѺ˪ąĮ«ȂǱ\x83',
                                                                            'ɑ£ÀѤÌҽΧŃɮ\x9dÞųʭĬǏ˦ʼЊƱ˼ҳƹыĭʮť\u0383êĲg',
                                                                            'ԓӟӛҳȅUǫzϰĽԌdƶʕÒĶх\x82ȗЍҳɚɥƉҼԢƳΊʞ˽',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѝӄ²q˪,ϴвԋÆƭ\u0381ПȞӐ\u038bҊɿҸ\x9fȵǒźáǂǞȈґ%˹',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'δΖωҫșŒäQ˝άçӘŹWáөϖͿSѣλʹπҀǐĽӁȻ»ȓ',
                                                    },
                                    },
                            {
                                        'name': 'жĚư҅ñʜʊŗÑёjœŅɀyī˛ʹƜʴŒЪҾˆөɆΧēԩӭ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'âɚƖʤŢʯʺέέ˗ѳԃΚŇǸǅʶΨïйıˣȵĤ˛ËŇτ"˃',
                                                    },
                                    },
                            {
                                        'name': 'ҎғÎŰъ˕ʘѠ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'јΙǔʙŕ˩шʺƾϮʐɿʅũтƀ\xad\\ʛνшåŠşªүтƥVµ',
                                                                            'ЛԔϒΜɡeΗçĄϐƵ˓\x90Ɍƞ#ЛÛ#ǉΉɬˡчиz˴ιӦй',
                                                                            'FȆΑ\x91΅ʔыЧɹEɌ¢ĬǗ҅ǐŮǟɣǉҪП˼ΈρŚҥϘл\x86',
                                                                            'ɮӏоӺҗʓёɟЎϖρĿǒ¬ÜԔǽĶԆѝǯ$ѠДѝœκȑê·',
                                                                            'ԊŔ²ȢńѷʔɏÇÈѼΝ{ˑӇϪǻҎҦƌnĻϞ^șӒΰϨ9ˢ',
                                                                            'ƨ|ϞζˇѕӀș.ӦйȫѠʉ7/ԊǍϟˎǖБАόб·һˢʐš',
                                                                            'źЀɷΣӏƦǳҒЯ-ИφWˣ\x83\x85ĻˇРſͰDʓ¾ʎȢǺϿӣİ',
                                                                            'ѥζϣĊȻBŗόȧȲŴδǙӷϴĜѰÙɱϰ҅ϝʟ˖¸ȔϠԤѵζ',
                                                                            'ŀǂaȆιÍΜς¶ĘωƟѳŅɃ\x9aʁ¦,Ԅ¶ϥæ˰ХĦ˴ʉ\x88Ө',
                                                                            'O=қʓ˒ʯ\u0382ɵғӶʹɲċǘƠʓздϏ;ӜԒÐ÷ϨԑɅґёҁ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǸϳҗΖvöɠЯƝȀϼƉǷǳƠ2ӹˉϢ;',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x95ʱȯʉĴɊԩ@ʜԄү϶ɼΙFғ/ĭƳɓ«ǦҜϬѡа7НÌƒ',
                                                                            'ȺžȜ\x9dˈʱӟӪŷԇˬӞƼˇϿą\x9dƌȢ\x93ыΛ˴ĊŒӨÆF¨˗',
                                                                            'ԄĄВǑǧδҘϘǹɞƅӿӖɅ4ģđΕɫBѣʕ҄ˣʟŉҊʌĆ\u0381',
                                                                            'ʓҢԖϦ·ΎÏӐĖńǗȅūƢŌпҾÒҽÿŸOȑ˻ƫȍƑ΄ѣľ',
                                                                            'Ӭϰ¯ϦϫȣήƒȨԛơɌӚƓǱúȉҹʰ(ĘӜ·иɒЦʕčәƟ',
                                                                            ' ҁөyЅĢ6ʙɲΘĕҔΞԆƴθƊFЙºҌҨҲϼFϋЂ;Ѝӧ',
                                                                            'ƾʊӵÛԍвĤҵëÞưӽǽéŢZɎƨѡǊҊĖɝҖĐġ\x7fӛǴʼ',
                                                                            'ʴыƆϕĪqȊΡ\x9bΰɈѾѬĹ¦\x9aτѭʐǹšŬLˇрʦŪϞ\x86¤',
                                                                            'ƞ©ѥǖůͻӾđԌƼɵЖkҿʌĪ˅ӨɪГԘˈϛŊǟǼлƪԏҾ',
                                                                            'ͽӡό\x93Æţ.ҘđõUӄöÊЌċĴϠҺƪɫғІϾWɼӚʐ҆˺',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ĥ\x99ØƟƛːΑfϸώ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3718378469412775406,
                                                                            -2954681190093985246,
                                                                            145770372656376036,
                                                                            7734167390210163017,
                                                                            445362585386758861,
                                                                            5804908308250255476,
                                                                            -7443959581900025145,
                                                                            -7502707910136113138,
                                                                            -1372374603798138033,
                                                                            -1048873530167463,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'âџ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212311.198291:+0000',
                                                                            '20210208:212311.198304:+0000',
                                                                            '20210208:212311.198310:+0000',
                                                                            '20210208:212311.198315:+0000',
                                                                            '20210208:212311.198320:+0000',
                                                                            '20210208:212311.198325:+0000',
                                                                            '20210208:212311.198329:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '|ˬӥɁεѱƅƅυт>͵ŜʺňѸЙiѺŒЭ1ʡŝʵƋ¾ӳϨŃ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            339908.71727347263,
                                                                            100278.29761214176,
                                                                            203719.92191656458,
                                                                            -54481.475394578214,
                                                                            311470.9588092632,
                                                                            110043.25249527075,
                                                                            -52703.12337722389,
                                                                            314825.7213799024,
                                                                            -74306.30799850111,
                                                                            509042.6262726267,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ІǊʊǴƿ\x8dǝǉ\x9eӔƭ¥čќѰɵѣԋŨNωӠмӮƯ\u0383ǊМғɋ',
                    'message': 'ʲʬτѵ*˽ΠǘЮȬʌÐōҟГƆɍӹήʥɻV˝ЎĿțϨ\u0380ƍ˷',
                    'arguments': [
                            {
                                        'name': 'ńюĥǻ\x85ɸͺԊǴͻ3ӏŸűĕĳâôɞ·ÖʬҳǶȠӢÚˋˀӢ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 772512.6787633603,
                                                    },
                                    },
                            {
                                        'name': 'þĝѻ4|҈ϱ\u038bÕàƝϤЩÛō/ҺѰҖŎƏӶ\x9bԪ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212311.199236:+0000',
                                                                            '20210208:212311.199246:+0000',
                                                                            '20210208:212311.199252:+0000',
                                                                            '20210208:212311.199257:+0000',
                                                                            '20210208:212311.199262:+0000',
                                                                            '20210208:212311.199267:+0000',
                                                                            '20210208:212311.199271:+0000',
                                                                            '20210208:212311.199276:+0000',
                                                                            '20210208:212311.199280:+0000',
                                                                            '20210208:212311.199285:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΩǲĮǾӑǡɫϧˆĦȓŉҢ\x7fԁĉϊʮǱѵɖѸΔȏȀ\x8aƉ\x98ȸĜ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            798370.6727795926,
                                                                            915163.8288793046,
                                                                            450532.07558365795,
                                                                            698863.1122742929,
                                                                            689442.9750413942,
                                                                            933379.0700667484,
                                                                            685722.4443195687,
                                                                            872653.4336357367,
                                                                            129664.99485926423,
                                                                            -52288.96744770657,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ПˍǽĄА',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212311.199741:+0000',
                                                    },
                                    },
                            {
                                        'name': 'цҴҿŖӽ˜ǯȱͷȅӆƸҦԀш',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212311.199862:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĉǾz~ńӺΩʸȧțɡϰˡͿdʝЗԦʏɵ\x98ѝӍʦá˽ѱΗˠϟ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7878410392750399025,
                                                    },
                                    },
                            {
                                        'name': 'Ǟɞ®Ȯɂӡʍѹ\x94ǊýҚĞǁѰʙRƕ\x87Ô½ɿѝëӶƖ˼θ¶ԩ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212311.200112:+0000',
                                                                            '20210208:212311.200120:+0000',
                                                                            '20210208:212311.200125:+0000',
                                                                            '20210208:212311.200130:+0000',
                                                                            '20210208:212311.200134:+0000',
                                                                            '20210208:212311.200139:+0000',
                                                                            '20210208:212311.200143:+0000',
                                                                            '20210208:212311.200148:+0000',
                                                                            '20210208:212311.200152:+0000',
                                                                            '20210208:212311.200156:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'әφ\x8e˙ҲÿǊɨϤҟθʨȧφàѩЂʼʬϬ\\ʃҀ˰ӿĴԐ\u0380Ϯǁ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ы\x93ӤзΧƕњԈԕþʖɹЌλ\x91ѿ\x84ʾɅ«ϷÇӀʣҧĦϴƦԈ˲',
                                                    },
                                    },
                            {
                                        'name': '7ŇȜ\x98ӊȅƝǷȬόɺȃӢʷ:Ćž˂ʟɬƺҺ΅ȜӌϕįŬÜ~',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212311.200539:+0000',
                                                                            '20210208:212311.200551:+0000',
                                                                            '20210208:212311.200557:+0000',
                                                                            '20210208:212311.200563:+0000',
                                                                            '20210208:212311.200568:+0000',
                                                                            '20210208:212311.200573:+0000',
                                                                            '20210208:212311.200578:+0000',
                                                                            '20210208:212311.200583:+0000',
                                                                            '20210208:212311.200588:+0000',
                                                                            '20210208:212311.200593:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѓ»\x91ϛŮǛǝʂ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -66705.12444551704,
                                                                            -89938.52328013793,
                                                                            252351.29134591704,
                                                                            595795.4312700232,
                                                                            361877.7924442904,
                                                                            939548.0548878029,
                                                                            356083.1665026736,
                                                                            81397.34044988509,
                                                                            778597.0439786203,
                                                                            -17134.31072546933,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǠŋΠȢёʋń`ƍʿǄ\x85\x81ќȅ¼Ø˩ҀˍѸзŖљīį5ðρΊ',
                    'message': 'ӁËĸЎƮȢè\x9eІҠӠ[ϑȈÐԐü¬ѤŷϧͰːЖҽõeѓ\x84\x83',
                    'arguments': [
                            {
                                        'name': 'ğҮЪ˝ДǧҿĆ ϥȧǆʈӶNȐĨ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3589856690546469854,
                                                                            -8640841334274466757,
                                                                            8325557672420191633,
                                                                            1464360881178341857,
                                                                            3427224344161624985,
                                                                            2796922777992343898,
                                                                            6192195739860072439,
                                                                            1303606160817250751,
                                                                            -955317905111119437,
                                                                            -6835451067074056521,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'џѷɲƖďѰИȀѥbѽƲź\x8bEkȷĹ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212311.201609:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʎȫ\x9cϾǧÐΫŢƴъ¢ȗҐԐƍцӕϙԏ>ХӥʧŹ҉',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1165066879072274639,
                                                    },
                                    },
                            {
                                        'name': 'ӝȘӖьǕɞҼǷъǍÜȆИӹ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212311.201879:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӞŞԮʾҀѻΒφɺӽĄ1ű',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 544251.4408247878,
                                                    },
                                    },
                            {
                                        'name': 'ΣΰͳĭϣǞϯƹӃǠī©ę¦νy\x87āƋ1ĮȳОě˛Ŝ˥ȝǸу',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȥ÷ƙӟѵ\x8aĂԌƂαŰYʎйυǬ\u0380ШêʅѤƀӭĎŤЅϻϐkȟ',
                                                                            'ϲӋʎ¤¡ɧɘҜɢґ˂θҺЋЃμǔγȃɦϘϮϬńˋǌ˥o2ļ',
                                                                            '~ԝΨϳ´ѳɈǦǷȤ^ȞǠџ¢ĈӜӈЁϯϯǫūʺͲuƼʚĒȘ',
                                                                            'άəμεŧΝ͵гěȅЏɋŹѻѿł¸/ǌɖЁõ˹˫Õ҈мQ˖µ',
                                                                            '5Ț\u0383Ɛ҉ӺˋьЈЪǃ·ʾϞїǊөýԠЁӇρаsϛ¸ыaŉɜ',
                                                                            'мˢăģѹǻӜ˻ΠώȌјYŘƽ˵ўСǃȈӪƌʐԑƄ˨ӑσȀȧ',
                                                                            'їԅȋаp\x9aðČưÎ˅ȔǹΕRÂӖҁǶ˚ӾұћҟцÞҍȒĚɵ',
                                                                            'ѱ˞Ŏ]ҡyίаÎίÞŔԎАĢƒƛϜĠыưŦ\\Ѹйȳϭбɱѱ',
                                                                            'ɾџǈđҥѤԊDƸɣāϪ=ÏƳª$Ώīɡˁͻn¨Ϧǃbǯӣә',
                                                                            'ίƽӮĴДɺˏϗɘǡYȡԖ˹ƸшϏѽαϠҋϡͳēɘɇҥ>ĉЖ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Δϲ7Ҕèȕ\u0379XʴǷ{z˩ɋǍƆʦξȄƪΫɋĔ}YеΑӳêʨ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            666506.9847728735,
                                                                            85167.21211576698,
                                                                            305545.2410328241,
                                                                            -91823.4788510929,
                                                                            535933.2534327374,
                                                                            506483.5655341373,
                                                                            396409.0170931191,
                                                                            720839.6898167831,
                                                                            342301.04819953203,
                                                                            154093.0936503976,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ůӨĈŜȽϝԢʓȔʤȇĉīĘåʲƹˮǲӴoÆ\u0378ǶΦƲӨĭÑĸ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212311.202819:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԥƎìŹɺþʱʱŏʍƭ҆ʝɀŐĭΔϥ¯λҚє\x99Aɯ\x86ɺʑ\x92Ѓ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 430414527849806381,
                                                    },
                                    },
                            {
                                        'name': 'ȲϽôЧЧƋƤȐӷъӬƐʩȯæÌ£ӲҀĬręɌXź5ҏԌϯȋ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˤ\u0380ǔʖÿĀӒήȖϦȟϪȤɵɼ¬ʸûŷ˓ͽʤÑǅĕԛҒōͱĵ',
                                                                            'ѡ¾`;ϓʆoϠƺ҅ΝϊĉСˆ\x96˦гЙȁ˙ԢѬԎȇϿԟĤԬċ',
                                                                            'БƐѷÆлҚǵȩǡɇӫ6¸¡Ȱ˨ɴũĴȍͻʽѹʹ]ɷƤƣôϰ',
                                                                            'ϵʍ\\ɀ»\x8aҋDsӲ1΅ѮԄ9ʿ%ΞɊϽ˾лͺɅʏËѺ\u0380\x96\x90',
                                                                            '\x91ɓӾϵåȂɛΎÀǯ7ѸɁǀLԀˉЩ΅˝\x82ш͵βωΫџV6ђ',
                                                                            'ȼΡƛƂʌɈƫɭԒȰÜрŜ«ÚӳŘÛόŐΆǯeɝ¿ɷϊ˞οʕ',
                                                                            'ŐƥŁȧʲŔ.\u038bƖϦμƢǻŐТȂіΏàOĆԀӵήԪĺ\x9cġШž',
                                                                            'ηʦҰɑΙ»ЇSȝ\x9dÑší҆ЈҝʃʂʸќӺ ͵òóįǵĚϼȚ',
                                                                            'ҮøЩDиȓѣΒƢiϺʃѤԓԭȿÎź΄ϡ\x83ӲͿŽƈȪƔSԚЯ',
                                                                            'ù\x9bӵ ӅÇŤŀ¦ŗûý·ԡȗΨĴλφɶÖçÞһɎРԝƄV҈',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɸʧƉƫŏрɞÞΆ§ф×ͻϰĤ\x8eʍ:νÁć#˽ĊɩΫОѼƴ}',
                    'message': 'Ǡƺεҷǻʍʆ\x84\x90ӭʊβлКž<ЬϳγɘmρԥԋԎųɑ\u038bԕĤ',
                    'arguments': [
                            {
                                        'name': 'Ъ±ήɉɧ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            933074.0313414683,
                                                                            120035.6865685079,
                                                                            567598.5187772332,
                                                                            419479.5912285114,
                                                                            583780.7202131771,
                                                                            709692.7392829044,
                                                                            41125.227009725786,
                                                                            895154.2437318324,
                                                                            795957.0850862272,
                                                                            64939.13446335157,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ãςʁҕɨɑƑƞХӴφ5ŁɄӳƸʲǤʊɳȬĚˏЙƣʙʗPĨЇ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212311.205121:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҼǫʢɜĻ˪ΓȾ\x8cŲğΊʮźбėɀМƹĦǮÌ^^ҶČÿ[ԐĤ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϫıΐӢλӝɦ\x93ϷČԌϩęńi~\x89ԛҤӟДϺӑҵɕԗΤʂәџ',
                                                    },
                                    },
                            {
                                        'name': 'ϮÚôʢҢƲÝʂԊÒɚʨӇԦ¹',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '˓˪ǌѢˡJǭˁώlƚŠ˾',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'đӫéΪϋԙÞʒ҉ç҉ʸ\x9aӗʯ6\u0382ʢҾȇĮћҧœƒĈћˍɱ˪',
                                                                            'Зэɱ\u0379ːԕƁÎƁ˛ӜƂʾȗɞΘżϗ4ìâÊiˀǓҴĶЛæ<',
                                                                            'ǩЪҝģϢƅ\u0380ƧЏԢȺΜȐťǷǹ\x9eģʱȜсȂӉйΈǾЅΩΘÄ',
                                                                            'Ƶ}˱ʈ«҈ӬѦԔɚӯ˺ηŰǬŉηϻ˰įϔ+ӍǰЈˑӭŧ¥Ǉ',
                                                                            "ɅǪϖČ͵χХӮъöԣƙżÈʍƹŒɢҴѨш*Ӂůѹ'þĞ˯\x9d",
                                                                            '!ϯǃҼгҞXϼ˹ǕʽʢͽЈӔӬҀҳɽϟТӈɒӓΎ1Ԭʎ\x88ӳ',
                                                                            'ӚɉÜúѿͽƥ~ǽǁϢŴɼЧЧӯǼȰǒå\x9eϻƅ˦\x98Ý\x97Ӝˠʥ',
                                                                            'ъԘӓɉӸˆҧͻľðÍĬ>ԪȁəԞӚʾͿҟɌҨъԫŵѐΆƻҴ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʰԦǷʚ\x8eԊƐʾϾ˫ӭ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĖrƟɆƻîIFȾŕ˸ɏΟǈÇѵӓÚŰȨȌß˾·ňʖїќӂϾ',
                                                    },
                                    },
                            {
                                        'name': '˻Ͼ<\u0382ɪџ˸˺ͼˊ¶ϛҪԋќӿǵϾɱƢ/ҟϟτˬԆӍϡǴі',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4200879937494559990,
                                                                            -1482424551539229879,
                                                                            3563613274138128600,
                                                                            -8274684977031702672,
                                                                            3720592520488679195,
                                                                            -2028511737092276539,
                                                                            767124071081004494,
                                                                            3997278996520978017,
                                                                            -928762920684776037,
                                                                            -2911234658285505470,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ãɿȴȭϴ˽ŭϣ³ǵύӪӁʽχеƣ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212311.206292:+0000',
                                                    },
                                    },
                            {
                                        'name': 'IǾзԝІŒΠ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212311.206417:+0000',
                                                                            '20210208:212311.206426:+0000',
                                                                            '20210208:212311.206431:+0000',
                                                                            '20210208:212311.206435:+0000',
                                                                            '20210208:212311.206440:+0000',
                                                                            '20210208:212311.206445:+0000',
                                                                            '20210208:212311.206449:+0000',
                                                                            '20210208:212311.206453:+0000',
                                                                            '20210208:212311.206457:+0000',
                                                                            '20210208:212311.206462:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȝƺȼ»ūÂ˕ˍ\xad3ƖǓϗɔ˺ơ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5149180971011486763,
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

            'identifier': 'ñȩЃӫǴ',

            'categories': [
                'invalid-user-action',
            ],

            'messages': [
                {
                    'catalog': 'Ҋ҇',
                    'message': 'T',
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
            'name': 'ŝӡήԆ)èӢʖфϫȔȩÕήƠ\u038b˃ϱʪÑğ1Пǳ&ҼИʄ]Ņ',
            'error': {
                'identifier': 'ҁдҶѽ҉ŵú˞ЂђВĮç.ʤǁʦѸӤˊˏ\x82Ӯϱɱ˺ʒˀķˈ',
                'categories': [
                    'access-restriction',
                    'configuration',
                    'invalid-user-action',
                    'access-restriction',
                    'network',
                    'access-restriction',
                    'internal',
                    'file',
                    'os',
                    'access-restriction',
                ],
                'source': 'ǭΙěùɉŹŷѲÝѲέĨӶƢҩŤþŵ\u0379ɲơʏѥǓιǑώςǭĆ',
                'messages': [
                    {
                            'catalog': 'ԡώǮɂŁī˛ɘǞǽðZƳ˾ҏиŠɲΩӳ°˪ʾɦȁҸӹ8ʼͷ',
                            'message': 'Ľҟ˜ͲАTͽҿӆԤÿŏȟϹпǗӔ\x88ȄƑί<ԍÃҙƝβĄА˥',
                            'arguments': [
                                        {
                                                        'name': 'ɣҴҔēWĲʰ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӁĿ˩ȌεȥҏϺŗ½Wԏ3ǜ½_ĂˍŜʎʢŰƔ}\x87ǣÙƥϪĀ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212311.162234:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'SӻΜʥҥaĻ?ȐӀ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '3þӚɚ³Ȅ4ţΘ˫ǺȔÈϾ˄ģέƲβèԄǱԖҵ΅ǟȒϊԨʯ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1424699093608060790,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȻĐɴбɿǩӟԪĪ¾ӍƂȘοԩм4ϕМ¥hŚ˰ѢʚsҲƏͽʹ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x94ΟˑōЯʹļ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӌϫҒԘѕӂƗøɬ£\x81ŴǔѢǒĚĝ˹ÙЄ˻nΥҋ҇!ѮЊɿĴ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212311.163853:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʲƀɼόĽĝЪԇÍƝƛhήżˣѽƟΣɫɁҔĹɑǃȶґ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'êϔÏfНΑҼȳǸơŹʼsƆ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɑζǛ9ç³Ά',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 526975.6846027796,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x99GѰŘǶÏ\x93ʯƐ˻ε\u0381ԊГ§Ό8ŘǔvфƙʐŽÀ\x97ϯʉʢŜ',
                            'message': 'έɸΏĩԊϖ͵ ½.ҿԆǼɩén˴ї÷˜β¨ʂĺз8Е˂Ūŀ',
                            'arguments': [
                                        {
                                                        'name': 'ÛëɑӦH҂Ԥſο˓ì˶˙ԧԖзӴiȬςѹѾϫ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -73856.72203198411,
                                                                        },
                                                    },
                                        {
                                                        'name': 'OƳ\x90ßĪҊƇΣ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϻk˷ΑB˗άƠӠ˜МıʙҞˎĩρԎӘpŇώТʈ¡Ćψɜ\x82+',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɊώˑԤѝˀѵђΜҮЎˌӬˑΏsŘÑϞ¿<ƑÌ&ȫɤɪɬɋӋ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'JΛӐԫӑʑʟҪıʨĕͺͺϘϩǨРȣʁΑӃ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˓бòГöʐȕͱ¼ʓѶӼӾēŠåѹȲѤ˻ɗѰÏҟ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǚ˗Ǉ˒ζ\x8eŚΩƅ\x80Ӱԣɯȳ¢ƞҥЈĢeѧӄЃɒɁjƈɊƿ_',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x92!ʏȋϺǥWϟ˧Åѝɩjϧα³ȹϘ\xa0Ǿüģ¹ŭЫjӋȤєҺ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȇïɌπ͵ψёçͷύҙ.ԀҊǕɼάЮ˨ɪäǛþ>͵ƃȒÃкǏ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6440969924846361689,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɟԤXϷMӗжɗЦтĘĊŅȿ\x80ҭŏΐ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǋĭϯ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƭΖϯΣĬâȻÉ\x95ƻҷϲ˝ɱŐʐĎåԨĊ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƌëÀɋȪΗŰ\x83Ȇѻĉū˥Į˥ƲɰǰĐ"Ƶӱ¢ ìɼϛԢѭИ',
                            'message': 'ʐÇҴʾÊѫϣφѭζҐŶɻǽǸŇŗÑӌԁ¦Ő®ĤĈӟϛϹаԏ',
                            'arguments': [
                                        {
                                                        'name': 'ѽΠΠ\x88ĎҿǇȕǪΙʛŎӱȡ\x8eĲΘŒ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 92961.15686003398,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǙʈúħɄȨњԭ«Ǝ\x9fŜ\u038bɮ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϯ\x9cHƸ(Ƽ>ŭˆ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0383ҾΩ>ґ<ÊÐŕĎΧăơȼϕˉOPɱϙϱЍϞʚÚƮȞД©ϱ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʲÅѫOΫΪĆΓѥлƍʛÞë˥ʪҖЈĻƽρʆŋŰ϶ѳϼ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212311.167190:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѶӳþǣҺҰ˷ЦԧϪЗƵ¹®BϑɏɐΝӀƪπШ˔иʇS˭ǔ·',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҙƁǂѪΉþìƁҭȚ˻шƛǫΦ\xadӒƝƔЯęçЭӂ˗ΤɻӥΓĨ',
                                                                        },
                                                    },
                                        {
                                                        'name': '«ˋп5Ƀ§ķȚÚŧʢƥȭ\x9bƤȢѐƠΨGШʺɤɵ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϔ˃Ί˛ƊϾ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212311.167623:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ĉ%ȩîȊÅʓ;ʱɜЙӍ˜ȳīɳʧpĦĆ҄ȍɆıŵ˶đφɭē',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 703359.6377705381,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʈ˻ȃ\x9cǐ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҒҶǥѓ˙ʲϷ҄ҟɟʌŊO\x97ӼїǂŮvˍάVÌȮ\x99ҬƩɮǿƂ',
                            'message': '\x90ɳʋȧЊÔɃҎǳ\x9aǰԩѡҳŐԕ\u0382Ү@Ϧw˷ԖCӞΉѧöɻ˴',
                            'arguments': [
                                        {
                                                        'name': 'ǲνѶʰҬƣƈӽÎʧҧkČ%ʌŐļω',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǪԅЊÿԇ˲ĐɁΒВѩƝ\xadɨ˖ŶǬ¢ɸӖǣȐ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҏәӏ\\đЉƀѸ˄Ș½\x9bҝϋͻãƷÅɻԥîʃĸ\u0379ȷ˾ɐɾҬӅ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǒ\x98ӬϜǍΕö)¤Ǵ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'оˈΚϯԊȊļͱπϟЁϠƳϽȿϦ1ϟƽ˜ʧ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 200237.15564111172,
                                                                        },
                                                    },
                                        {
                                                        'name': '˅ȶϷɊ\x99Ҍ͵ɘ˫Ȉž',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -305245881088891780,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǃǮ«Ђ˨Ǯԡƥ%ǐˎɔ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ˈұǨǎςΩԖΣ\x8eѐɁdĹƅȃȭӇҲ\x94ŬɻҍȘŷȱŨōѡȃȗ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӃΨ[ðEƦΪŦӕķ×ɦξɓƳșaƌԋɭчƁÎǞУѱКΝaӣ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '-üưγуӈưÛdȜӒҁƻ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212311.169447:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˧ɺªʟҾӻԅ\x92ϗ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '$ċҌʍˣÇƭɥãŪϘѯӀpȞʩK˛ƪōӋ>ɛ±»ЗÚƛ=λ',
                            'message': 'ӋƢˡӔӭFuʓŕǘΓҎhϧNӘƣˬƚұӱԔѡȨøʙǺ\x8fˁ˗',
                            'arguments': [
                                        {
                                                        'name': 'ɏ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѹЫʠϙƸ҉ƐɯʔDϠ˦Ӵ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϵĐª˺ʛǦϔј˴ϼƕѐԩѼˠªӰʂ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȩϵвɿϺrϲɑêǨÕ(ϬɲӄŅ˟ԟͺϗĠΎǌBȨaҐ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'қΐʝʙŘͼӌɃ{ě¸ɐęϫˍ}ǿΊ\u03a2Ӻĭѓě&ķȤΫ¢Ѕ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӍʦȓǮ˧\xadˉѫ0ҕŪXчȟ˛QЯƪ ƯŖԤǃê¬ǛӰûǘ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 177890.55809416337,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Þ"ԨЋɨЙδǦԉDɪӵą\x97љГϐёĤǞӞҁϒʅΥԪȦШƸӻ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӰǂϤƬЪɕǉΙ;ηϤȳEŠƌŴΉ˂Ő¾ɯˑ\u03a2ˮԀƹ6Ɖ\x9dķ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 263266158832880443,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĊÿѻʅҁĂϧȐтǧȍҷͼt<Ě\x9fӗĀӃ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x91ѓŰÜҊɅʱ˔śЌџҸӠαͺĈȳyѴźЗčÒϳȯͽJʎȨÍ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǖ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'dŴǝŬʧŪǫҶŭкѣεūӃ\u038b·əĞǁȀӑ\x86ȗϩѪɧҳ\x82˘ș',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȢƪɻƤĥĻͽȝǖӟȖǧɌǤѕԜʐхĬϱŹĆ1Њ\x83Bɨʃѣѥ',
                            'message': 'ӂŗЕͰˉÂÒʝǪχ$\x94@Ņ¸Ǚšҕ3ԭɊżЙˇВţϓȮʊą',
                            'arguments': [
                                        {
                                                        'name': 'Ӑѧ¡ϊƶƘŞʩhԧiάç˜ΫϙɅ5ȞËϼīɅш˸ԟѪǉƥĢ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŭԆɀԘũҠσțȜĆxǁ\x94ƷʘԍȏҞv\x94\x81ѸӑгφĎ4ͰǇӠ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4360731045334238427,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȪĉΙǂ˷Ѐǫжůxʮ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԡ\x80ƵȤǴӧĻзȔ¸',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ЦŚŰӯíÞʏǜƥЯƺúȘҍʫҵɣ^ÊSΜǧȒļ~ϏтƦзɊ',
                            'message': 'ͰɨOɻҟɨԏѱϣԟȯ_˗˚ǭӫ\x8cѐ=ˍӢǼ\xa0ļʐȈӈĸŔñ',
                            'arguments': [
                                        {
                                                        'name': 'ԝβɧÏɬǊóŻɐćʎ\x80ϬhРԉ\x97ǦȌ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ґ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǌҺү҃ОňͰХͰÔӞɮѽӢƣԘĬǿ˭Zɂцˡ\u0379ӖɫƗʨˏő',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÏĺԝѫĈƅ\x92ӵrȤěнӖƷҋȾ4ҟϖǉŹ½ͷÁ˃ħôӁɠǩ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӽˬŏɵԅəӄȿĽфȪŐƙöǨΰoǪʄιȼéɰāǾʆǫϺƸʨ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƃƾ˅ÞӋѤȳĠƮ\x88ȜƜɄĪͿ÷ɀΣĳԫ|ʰʾďͻʤƨȞ\x82Ҝ',
                                                                        },
                                                    },
                                        {
                                                        'name': "țҟ'΅ƨ-ʤϽȡτÌѮжϛϟɨ=ϦƶɍīŌƞȓô2ɰƢЙŋ",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '±ҦнƇʪѾǃÚ҇ŲϐЯřϾl˵Ŋ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˺ӪĩŞʅ\u038bӈĉɵӌӸɖѐԃɵѵÍѳчʥżԟπˉǜȡÞкƜȕ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212311.174538:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʏeʵƧȧȍįψοȕǋǝǣȅԙҝϴǮNҠ˅ӉĴϣǱɂȵĨǽʻ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȚæǒŐȐԃǾɳĪBϤБǌ˅ƕҏ±æчǡϳĎЍН3ȯyѤũç',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5024110321785484267,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӤģӭБėÏҴǶǙЗϞгЧζƕ˪ƠЏTʭť¢ɁZɚąˮϠÜП',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212311.174977:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ПÓȓșϷʧĪŚßźʴƋђÍϢJ(ϫЀŃ_\x99˴×ґӽӃ\x80ȉȁ',
                            'message': 'ӥőϼǄ¾ɻԮώ2\x9d½δȵ¨ʨҪîԊͶĥһɉȗƠʹƶ±ʟʍƎ',
                            'arguments': [
                                        {
                                                        'name': 'ęщҍǝВьthǤɡӒˡӖʞśӗаGΛ҉tƞ¾ѠâŔҰƇƳ\u03a2',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8fɏðӥƐӱ\x8cʓĉϖpϒˤ£ħǾǉ˧ďʦ˵ǚɃ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӝˮѥіςёʌңԥϣɖѧʊʉΠĕǽɏмӸ\x9eȑÇȫѦѿΤΙ˦',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 383356.3628157703,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ôʞƓåЀD',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5159212972017145669,
                                                                        },
                                                    },
                                        {
                                                        'name': 'mԑŝʷ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 594357.0047485586,
                                                                        },
                                                    },
                                        {
                                                        'name': 'nʚɪϋ·ӟŝѬҒε',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3522404847782008376,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɸϡŢѨˉQӢɝ˜ƧԧљƒԞһϭ¸ӷͺBʯÕ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʁȮÇĳˮЬìιÖΰưǴ\u0379"ÕĉЌϣәѮȤƂɌЁӊ҇ИŽʎ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӿȇò¬ҤȎŨΧΈƞΫȚʲĖώρȒ˧ФƎ˖öѧÒȮÿɉЃ\x95',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĆɟɣӟѲѵ©ªˢhĕ҄ƷσϝвɪÅȬɑnŬàЊͰϱǼԤ¼Ɩ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԩŚЉӜȻԚșæϱϥƩτԟѲ˽ƛÌѢѲƃļЌωɬά',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʹʹʳϏ-҂Νřƀӈ\u0378ÆǢѮү\\ƢƜŎԆƮчÎËȡB&\x9cǂϨ',
                            'message': 'gчŗѧπȧ0яŅˎԓЂ҉õһå\\ʊ\x91ƧƼJҰȲŬԂ\x8cEƖŠ',
                            'arguments': [
                                        {
                                                        'name': '«Ħǡ͵ȼƛ҈ғҨӧԅʱǢÙӇķӵÖһΚòő\x9džĚϯȫӋƦƊ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˓ʳ˦\x87ǢҡȽѡԊÊъѻǗγӂΪ¼ΥԎϐǜΫɽѿ˶ЗƂώɯu',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '×ΦƈґʵΜ\x88ӸϽı¹\x9dŤʱʹͽ·ҚĘȂӯΌӇϹϖӈϴΥĎˡ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1942539258585966244,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΚЅˤÇ@²ӛΨԠiɉуѿ÷ɕӱȌ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5966820977937564185,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĦѾϭÝƳɢÆґϽиǎЫΤŰŵɸѵÂ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƄϨҝƉzƈ˱ϹϝȳΑʞƣЀɷτEӆtʱċКʎ\xadˤҕɽԊ˜ˡ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7897764191707561444,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȗƴǊ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6385925791543939631,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͱԗÏÆ¡һϓÀēǋЃƹҠ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѷǨʵÔ˛ČπŅȤϔşƗϻ\u03a20ДɣӴωԜ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǀИ³ŌǱť˓ˎ}ĝΐʒ\'ˊ²ЇӟŶ"˹ĽƋ˲#Ǯυ˪\x8dϞ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ūӹҢºʓͳ½ŨǎФčĊŔȺQ2ΖеԏΆӼԂЏӉƁ$ȜǨԀȔ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ŔҨHÇçԊȔcѥʃͶ\x8e˔Śˢҕ\x81ҊśșЈȿĠƢʾƦcÛɖѣ',
                            'message': 'ɾ˽ҝɪ;ŪǤΛ5ԚũȍĄѳˮϸʮϤͱ(Φ\x93ѣӮ\x81Ķƺ˩yϖ',
                            'arguments': [
                                        {
                                                        'name': '~eΘǟӥLμōʀӕȻνҚΙʼkЙɟѝԇŮϥĹԊνƗɸ,ĭѠ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3733366435014992799,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ι˅ţԧҲɅЌ.\x94ĉǾθӕǙ-ϵ\x9f¶ǎíŹϵņŝƢɮǺ¸ʄŕ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˾',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'VѧϏԡΟΩɧГŞɀÀƶ˄ӪˇǧÕ2ȒśӿүĤȲʧд',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 632421.3705516183,
                                                                        },
                                                    },
                                        {
                                                        'name': '§ǈӚźƔȫïϥ\x86ұħƥÿȓΫόσӱȢîÈҡĂʹѿϧȠ͵ƹǈ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 974032.7493063859,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ưҝåАѕ˓ȉpˡMӛώȠĴȱ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӺвʩіʝæňϽΚʋϏɟ˽ë˙ҭȕҸȬ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȪžˀŹǯСvЅɁʗľВĴS-ԦϩԓÝƶͰʀǞǄƷ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԭˬƹŻęЍжKŤê£ƕǣÐΉӍӏӳ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӘѡƼюǁ«ɯÃΊ,Ҙˎɲ°ʫʵŵҢ˚҄ƇďїάƏĽԅGwɊ',
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

            'name': 'ɰ"\x9e',

            'error': {
                'identifier': 'ӎ҆Ĕ˕Ŭ',
                'categories': [
                    'access-restriction',
                ],
                'messages': [
                    {
                            'catalog': 'Ӫґ',
                            'message': 'Ѩ',
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
            'name': 'ƺԫɅ9ŹÌҥџzΓχ²ȉƭȿʄƹ\x9cΈɸҷkĥɧľЮԙԔǐΘ',
            'version': [
                -838592050563774381,
                -2497194018473014377,
                -7407448187008178416,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '%Ŕȴ',

            'version': [
                -5011479795730245675,
                -353290544836295568,
                -7405662331204696836,
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
            'event_id': 'ȔǒɾȺт˚˘ԭзˏʟʣвχϧϪXϊ-ҕɣͿƌұʄȟŴǑҁҶ',
            'target_id': 'ҭпѷҢƬķ˜\\ОůˆϏʉѭˠРё҆Άϸƿ˓ϸŤҥ^ѯѹцǫ',
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
                    'event_id': 'ԡѭҺĖ1ӑаŽЖ\x96ʰ˶ʠĮłҰҢ}ȶÌбъġÜȃʐԤƮ\x86˼',
                    'target_id': 'ǉǞΠʽÁμǚѮͰÜЍǴʾĂԟŉϟҒmϓê¶ˁȱ¡έȽˊ҈ʵ',
                },
                {
                    'event_id': 'ѝϣķŅӼϷì.ёƒĸʎӘёнЇȌӷѠӷaȔÂѨ˵Ʋң¨ћɂ',
                    'target_id': '¡Ŵșѡ˒ɁȳŌҋɩőˮ˳2ƕȬӥďęʑЪċѪĻʍпɓʃѺˁ',
                },
                {
                    'event_id': 'ӕɣȜ`ϖʊŲȓƥӐЏżӂмȖОȹʱ4˕ҐɪҠ³ʼ˲ƳƔI¨',
                    'target_id': 'ʹä=·ɈÌҷжӾҔϨňԚϪǋĐ˙×ĳ#ɸȋяҎȈ˾ɑʕҔΦ',
                },
                {
                    'event_id': 'ˍȘӰğǈʝƚ\x7f\x93ȗȮȥЫêʚþ;ƉРϫϨҿHҥȀЋ\x95;Ҷʲ',
                    'target_id': 'ǭГΕˋĀǥ¸ѕȺƜ˽ɉaŬB}Ӝǒϫˈ\u0379zǭɟåʗѿWȏЅ',
                },
                {
                    'event_id': ']ԫ:ŦӞ˸\x8cĺҋɨäϣʎƄѸЌ\x90ҍӐ·ҡцӐτӂć˪˦ƪ·',
                    'target_id': 'ɒy˺ǪЪˢwʮĽԈcʁΈ˧ϲɿΊ˨Ĺ˃&ѥΊ˨7öѝЁ\u0381˱',
                },
                {
                    'event_id': 'ɦј˙ʻ×ŦòĢϜ¯8ŒįȲʠЪӴ\x8fªĭŠ˥ŴшҚ˰óҴȏΝ',
                    'target_id': 'ȔɉŶ{ÌĸΏνÊƝ&ƛέ£ΖԨȡϲČͺɥϥƺƞРư\u0379ČˋǢ',
                },
                {
                    'event_id': 'ĪӼ±ǦϪҺѮĲǠұћҋƱH˚Žű×ѤȽŵӣßΪΜͽѣȰ¥є',
                    'target_id': 'ϚŌīѕˮǛʹΦĐКΫ\x85μhӧӪиƀǲǸΰέѾɕκmϮѨǼϨ',
                },
                {
                    'event_id': 'ϴųlƉʃp҄\x9dӵmԛϻ/ϫΪЂˎхǯŃ\\ɶǸφī@Τ"Ѷч',
                    'target_id': 'țҵϢϼĲԡҠя˖ɰȘÁǲƮΤΣԒ˟8ɞǴ҇äҖѹɝзΉ\x88ŏ',
                },
                {
                    'event_id': '\x87²2ӣµԘΘӂʽӫĦ]јĬGлԮbϦ=ȥϬ˵_ʦ\u038d\u0380ȋ',
                    'target_id': 'ưȼʁɶɭҀљԒŚʊɐĻÛ˹˞ҡԅϖξɘӎҥВŪΨːØº\u0382ԓ',
                },
                {
                    'event_id': 'ɥӱϟƖ_ɆʎŴΕӫˈԖɎČĂΘ\x92˹ˀǞƄŞхxȗеǊЛҀ¡',
                    'target_id': 'ãȰД˹Ɍ\x96ǝǬͽȨģѶϧч²ͽώǶ\x97ПvǡĦӚˢȰΣп˩Щ',
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
                    'event_id': 'æ҅ȼѕκģϨ˻ΨѤүϽԈнˏԣсƽđҏğԒԖȠӏæǧҫҺŻ',
                    'target_id': '¨ˬҊǤϑϑʚ8ϴ˲\x99eɧTìΗ˯©ϡǮǥ\\øΝĒɝ҅хԎē',
                },
                {
                    'event_id': '[Z`ʛ˪ƾ͵ø1Ɩʲς}Ʃ҄ӉɑŦĩʋãĪàʺӶōʕēӜƨ',
                    'target_id': 'ǅľȋɁŢűӦӉ2˥ƃΕǊҜŌƯą\xadкʉуоĦ*¿ÀʮèþΎ',
                },
                {
                    'event_id': 'FɜȺϊʋϲǿƧ˺ѷԈάҧÄпʮԍǄύo Ƥǁ+«Кӛ΅ƿŶ',
                    'target_id': 'ǕSɷɻǺ¹ТĂѻΪϷ\x98˯ɗɌÔćřˡĭƿ˖ɹȡȇːѨӪƜҼ',
                },
                {
                    'event_id': 'ǰɿ-Ѯљōǹӟ@ȝ˝ѥϑ˪ц*Ė;ĲʹɣșԄ¤ҜƩǂĬòT',
                    'target_id': 'ΗέИƀ\\ơư{ɌˊÃąǨ¿ϹӭöDϥЛĮƴϵԂҜʯ.ʹνǥ',
                },
                {
                    'event_id': '[Û\u0378Ǿ¼TӕЧƦʟĮʹʁΝӝӮЏɓˡԆȻ\x9cӉ]ǿԥ\x99,Ȫӧ',
                    'target_id': 'ΆӄåΟˡʝϪʯɾδĨ˨Ñ\x99ěλ×ÉŚȪσ˻Ͼ@RƁ҇Ρ^ɬ',
                },
                {
                    'event_id': 'ʚȽЉǴȰƭ΅ʕȎʋğҟ\x9dÅˤřʆρτҡҳ\xadΰӷnʹÖȊȟƊ',
                    'target_id': 'ʛŎ˻ǢȹǨӼψňȒОǂê¼ǀ҉˧ҊΒ`ʩӽ©ҽЯǧüμuҐ',
                },
                {
                    'event_id': 'ĲѱēЌʵǺύŖ˒ƱzυÞɭƃȨǃϖɧŅɥЛɯɳ@ˤԀʅİM',
                    'target_id': 'ðȧԧʕĤ¯ƣ\u0380ϰ\x9cÿӴӗγ϶ԠӀśмrıЕʟƑ©ʸĬŅȷӢ',
                },
                {
                    'event_id': 'qöȣĊӈåԮÈьһȈmψќ~\x82fƊѡϊқЬЁƏ2ЍлԥqϽ',
                    'target_id': 'ˁԒϡYҡfϻ·ĉсƪɏΕ¬ś˜ĹѴ#ʷȢô\x93ċǋΠӔΚӺϼ',
                },
                {
                    'event_id': '¼ԢҌÅŁǃɾĜʎ\x8eĺͳʛĞ!λ˺ǎŲӓЂEȢšőÖȯКҎ·',
                    'target_id': 'ǟөĳʜƲӢҵα҆çѣѰɈɃʌԖϮԚǓϯÆϱȾǊʠ˽ɮӘϻó',
                },
                {
                    'event_id': 'ƈIʮˑ½Îą҄ԋҤÅѶʥќԘǰóƭ½ãЂŖ1ǏшїļӱŘΪ',
                    'target_id': 'эьҢĳƪzɠљԝȁĜәͺʧŹȊÔ\x9cȾϞʻČƖǠ͵Ƭɳǲ΅ʹ',
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
            'name': 'ȶɮĖʂǵӰϛуԍʹӬ@ɟϰƁǠБͲƝ\x8bÔӴȱγȌәɊϴāǱ',
            'version': [
                -6259346287870309595,
                -7880519126841912177,
                -1048595058216378871,
            ],
            'about': '»Ĕ˚NʱȎԣäµҀLŵʹПƧÀɹǷ\x81ʕҶ\u0380ɏŷÇӺŗϰ˪å',
            'description': 'ӱԊ\x8e6ϘɬїƽƱЄ\x82\x8cҞ\x9fƎȖԭʡǪgǜǞȧɛȮїҏƙĞШ',
            'authors': [
                'ˢПÑƸϲϭiɞβϜóсӖӍȮ-AΟƟˍǌѶӅԓɜå˕ȳeԙ',
                'ӻUАɡťȤ˲˻\u0382ΨħɴŻéӨΔś\u0378%ԣʾθɒȍӭӏχѕɡĘ',
                'Ԗs\u0378Ѱљщƽ¤ԂǇ_ΜӈɰӒƂϪѱǯϖƖǍćϳνΰʪάâ÷',
                'ƜӢǙҔΩԖʆԍˈPaǈФȹK˖TԍУĞˤʔǽǍӢřˉʌȌν',
                '¯ǂ',
                'ǿpԄƍѽſĽЍͲӟŏɧ\x96ѪϭçɋϨêǉƗҵėȕƴжԊɔbΑ',
                'čǫæǁүƐĦӀǷɦȱӘ˱$ȿʡ\x83ϞӯҤͷǬɯuZǞƩʩѲΦ',
                'ӠƕǨ˚øūˣÝǻӦϲЧ҄Ӆɑɍ˘ʯZгǛ˸ƍǢșɮɈЖŔž',
                'šĸԊʼ˙ţϯѲ±ƊІǤǋгeˉώĲҏУǶƽɑɯ\x96?Ɵȡ҉Ò',
                'áɳʸЁq&}\x85ӐǚѝʜǶōʔǵќӻϭűϽ˼ċÍ9ύσͳȆ¬',
            ],
            'licenses': [
                'әȨʗƇƗǾЋÌx%ȜʒԕǥÚɌɡ²)áͲŴяſʸɾ͵½Ƒ\x9c',
                'ȖǠͼώыɐґʼɳҾqʟļĭΝνHɏ҅ΎÅ×ηΏωӷ¹ņĥΊ',
                'СŊlʟжÁЕʎқƜςĘϰЭoǆ+ΪПӃѴʪԟǻʡȆ\x7fÒȲԩ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '¦§Д',

            'version': [
                -614591040803650766,
                -5615419127318656235,
                -7046327527450915463,
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
                    'name': 'ǻӄ˷ϬӇąǥµʍŮϽĬɺӷ}ɬƍĠʹғ˃ϣӊlɺȜѿм\u0379ӹ',
                    'version': [
                            -1114995853671492930,
                            -2517706711014944903,
                            -328743601927669889,
                        ],
                    'about': 'ΰȭҜѳĲаϧӟҧѷɐҼ\u0382lʖѢ\u0378ӧ˦ʥѠҩȬϊԘkΆЧҷƀ',
                    'description': 'ϤǰƝőŘЏŝ®Ϟû\xadҫɜϽƬǡȧðӆĒǿǱ\x7fͳ5Ӣԇϡħϣ',
                    'authors': [
                            'Œǐπϙǎ¶ҩӊ\x8bԖǌЙÇμϒÑӁϢ\x85зËǪȫЖшт\x8b˰Љ£',
                            'źɧζ,ˡωŴȫїˣʌ£ƢԄɆіА:)ȘſɱŕëзҧŞŶ\x95ɘ',
                            'ÒʲϤȥʎӵԁГƆΨҽʡȩþʖϙΎŀʤ\u0383żЈżř{ϒ҅ԝňɓ',
                            'σϕ\x92ЭĩѸИŬĎΣà\u0379mʘЗfʑԟɭӋЄЄϰϞǰĥԊүυƊ',
                            'ȾѴѹÛŭǳ÷Ƅҟ²ʜТǵ˹˯ƤщȆȤёťĸ>ƢӰoϖƭʃҺ',
                            '\x8f\x94ϳӣѣˎÇ҇ѠΏHÞ)ЬŃԉΦɯĶƧΊŖŁɷӄҠʽ`ĲƲ',
                            'ȚȅӤόуԋ\x83¿ʮƵǟ#ʈŇӯƦƒ·ŐŞͿϥԊͲĊƊΫĬõӺ',
                            '˅ʪɄёȢΠ+вЃ\u0381ŝ/ŪԚĹΌҔ`ϊλƨҔªǴ˨\x85ăҺ˾\x9c',
                            'ǱõȊ\u038bıåºĝЕǏȂѼПà˚ҹ˥ȈɟȦ΄UƼÞűӀ˼\u0381Ъԓ',
                            'ˎɡјτĥǨȮщρœǶ˴ȇАҟɲҦҥwǄΞĔÒÉĪѡŜʁʎÃ',
                        ],
                    'licenses': [
                            '҂ӝƾ2ԕθԗФӚǫʆÎÁΨəƍŷӋа˫Œƛȣ\u03a2ѺϥӨҐ^ԋ',
                            'ígǁΞһŀқ˥ϡ5ǜÚǐɸͻÚÅƶґʽîˈǊҕȼŒҗöǩϭ',
                            'ȸϦ;Ö\x8fЅɃϜϴ\x8e˗ǋȆϵOɈмjɾ˾ǌζƷǶԒĖŚǷɅɠ',
                            'ŉψĉўϮŶӴĞȁąɅūȯӲΎƵǁңŝЮѰɦҶòԁ´ĨΰԒģ',
                            'Ѯ@έбğѣϿƤwF',
                        ],
                },
                {
                    'name': 'ˋ˾\x8bβʪӣ˭ňÎÜāğșΟҥ˺ΒϩƵЮԊɊЁШ\xa0=ˠėԣӖ',
                    'version': [
                            -3874098952642078694,
                            -4710789335745860473,
                            -3892125455622373712,
                        ],
                    'about': 'ΨſұɃÛͺΜ²ǡǣзҴҫ¹ɮҖ}˱ΧȣӑϴĬơɘƩŔБǱǽ',
                    'description': 'ƗăϳƼŮZǌîȿÌȗŇĳħϰaуªϪԆ!ѳÇɏĐԜʱϲԞҊ',
                    'authors': [
                            'ùŃŌƫ\x8c˟{GǂҀϧęѱҬÁʏJŌɫįɞĉȽ˵ȏѿɚ҆ƌö',
                            'ĮѰr/ͻҰà-˲\x86ɏˢɵˤƩҝ˗ɤȥǌƊ˸ɷɚE´Йȃƽӵ',
                            'ŎþѷȄф³\x92ĉȁόÉ\x9eӲ>\\ѫΙ΄ϷɼƎǏΛ˪оʅȻŸĨͶ',
                            '±\x8cÛȶе˶ϻрƃ˥Ȋ`ĥ·ҺɉǶȳÄɤҎćӌ˺КӡϨЊŔƿ',
                            'ѭǡΉԥÛSƄŠƣ\x7fɘƿύƲŎϞϿˬƸΐСŐȾ}ϞЕǲϢӔə',
                            'žσ\u0381ӘBɞǼΈļУʯЦɚϧÈфʰˌһ[Ā\x87UцĩΘСҧêИ',
                            'ҁӓʄϹӽǦǋȰ˹Ѐϊ\x94ȷʭƓs˩зҏӈԐԋԫʵ˅Ţ ý˼ˁ',
                            'bҖĒ҄үĹŪϽFÔԆ˹ɛěɺŪĿͻ¼Ňңr[ɽxÝэƾхĔ',
                            'íÖӡƁɧw\x9fńǶɴȍӤůԡʛɞiú:ļÓҝĆӑ˭ъeҮѮ\x89',
                            'ʶҌОќ1ɞÝɏӁʈя\x95Ӓі\x84üʝрģháɍ\x9cǞǥ%Ѩ˗ңȣ',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': 'qПȤȭΐșϒӬťƔ˂Ơ˄ȟľŷōȵɻìϫ¦¿\x8bɊҲǹƓҝõ',
                    'version': [
                            -7074804915146553715,
                            -8447738854335227229,
                            -7918251690657571832,
                        ],
                    'about': '~јJѿǂ=ȈȰƒρǣǻРƔǻöӽԨƊ\x9aɱʓ˱˨ԛņ¥ɦȏǃ',
                    'description': 'Ϋ¹Πɑ˛ϟɂБҸ÷К9ӱ˸\x8cҢ˰Š\x9cϟϘΈƀѹѮĪтϳçϨ',
                    'authors': [
                            "'ɴĆʻɞї¹ҷŢƾҟψŴǁƙё҃bҟğ¡GȱхZʫɢYǉȀ",
                            'ʇǉҥǂȚǙ΄ā®ЈңψʖƢàѽʰ[Ӗ½Ė҈ȕˇȆϷǪΦ˃а',
                            'ӘːѶÑŘËѯσʉԌŒΨ϶Ӻ\x8aɋž\u038bѯƟҸʌϨ-ƢŦȺӲǏѺ',
                            'Ӈ¿Șòηǉͻу^ҮǉҋаđȭэǻԛĤēʑʶԕľ?ΚʗҰД}',
                            'βČΟԭâЭӖWϺ·Ϛǂԫ«ŧӗЕÉ\x9bЛ\u0381ņȉϟů´ČΥ.Ӹ',
                            'ȩ¢ʯҵϑԨƕɟͺԗ$єȋϗˁǪΤʜɰ7ǻњˌΝęѭҼϗΫȇ',
                            'Ĺƻԉ˟ҍȣДɘѽȨ.ŴƹȱđԙШDǨ0wÝȘʠ&ƓzԨėΦ',
                            'ΚНǈξȍɷνʫ»łҸɛϙˡˉοɵқя0\x90²ҡҸͽ-ӛɯ\x9b\xad',
                            "ĦʬŨIƄϧѧюȉ'ϗ˅ΒԇЊηĒεϺƞŅˮͱȖУȹҦϊ\u0380ɗ",
                            'ÎЁӦʕҴɛSˢȱɫȪƱƨ\x97жlҸɯҤãȗϵҩұѷǪțȣÚΙ',
                        ],
                    'licenses': [
                            'ѵ',
                        ],
                },
                {
                    'name': 'ϩаˮүˆԁ}ˌ˴ԪįZ˛ѼӇ»Ώå,ǧ˛ɒ\x9cµ\u0383ʊΠɲǦ1',
                    'version': [
                            -4034354776042911594,
                            -3596640417397365103,
                            -5114489486603514223,
                        ],
                    'about': 'ʫǃӷʖΤđĐʣÁԭѕªƊçћнƍЖȞʄǏϲǆ!ȸӋҟ',
                    'description': 'ǱӋҟļː`ȰǅƮсɦΔ\x83ЧϞ˫Ÿ$ɝˍȝÙӦƪʒԘƷΕѩд',
                    'authors': [
                            '˘јӈНɤƶLҽόʾǸ˽ѷa¥XǒɊʡ1Ϋ˟ǿÉðϯͲh^ń',
                            '´˸ŭѐŽʵѲȺч¼ȆпˆӺǫϦҁЏ˕\x9bŚ×ӇƐQ΅Ä˖ʚϴ',
                            'ŇŃ·ёTĐǅęŔЂԖќDʝ˸ўȟΝγϩƔΔӔĲĤǒѴкǇ˕',
                            'ϋ˸ЊƨҩĒӡƛȨϬ:ǂɵǋÎŝ¥Ř\x86ƔǾƜɑ˱Н¢ĜԝǑп',
                            '˳ҿаϻʳΦˁӄϕКԫЩˇĘŉԝѕ\x8bīˡɠˋЎǢIĿ˸ɚҡĩ',
                            'ȡǻ%JƧϑĀԅ¶¬ҭʡOϬāŞ˒ēȖļƎƬĠǢÂСvҔҦȔ',
                            'ӬŠ#ΠȧȪÍѼɦρʇϣϪɸҢίȨԁǴȷ˅ѦĻɝӕ¨ãćʺʂ',
                            'ǔҧɽĐȮƣƂΐƈԮʻыH˟őͶŇШϩ\x8eЄҞϠͲȔȰΥǇʑǚ',
                            'ϐϓϑԅӶηǖɔȈǡsΩӨǳѽԦ\x84ѤήȆPΧĹфĬģɋаӔĕ',
                            'Ġçϓȯϰ҈ϳǑ\x88˾Ώ҈нΤӬʩȜʍɊ\x7fɌƿʒԄȷÚ˫\x83Ⱦś',
                        ],
                    'licenses': [
                            'œÝŲΕēѾω˱þƏǊϞщиԇїǚ6ХҽФ\u0378[ҬԂЛ-IζΑ',
                        ],
                },
                {
                    'name': 'ӦŊɊƭȉǣſĀϲÙɈԣåɶԂȝʧ6ʥȄИӊɚԂҡхɤï˦Ԥ',
                    'version': [
                            -6308134331682237525,
                            -314390019705788427,
                            -3946079395888048460,
                        ],
                    'about': "˪Й˟Ԧӕƹï7Ӗǣΐʴ˺щŠӹïЋϏƁú'ǻэgˇЧˌvѡ",
                    'description': 'Љʟę\x9dʕnԒпÎɬǓҴȪC0ϟÂlʊɌаŏ\x9aě¡ɀˋ.Ħ˅',
                    'authors': [
                            'ʸ҆ԐÿʋϬƤØѼϩȝвӘϭţƎƀ4Ȩȥĸćѷ5ԕ´Ѳ\xa0Sȯ',
                            'ÖƞʢŦˆҷҳʔ˻Ӂĕ˾QӺŚыӊѧҰɰԇîjǯơÅȥь)Ћ',
                            "ƙɿϱѝĒ=4ǍÆŉȞǧ\u0379Ǻąˠӏѹ\x98ɴ'ĽÎӟ8ºÇƩɯ΅",
                            'ŵʿϰȞɢɃι"±ӹƇ§ƏǙǈĶΈјΊқ\u0380ǢȨɌҸɇйɏˬϝ',
                            'ʁԎ°\x8eɦʚÖƩù@FɓƏρƐń\x96ƣИęξʦԬФӌ§ӨăӚ˙',
                            'ɛаϩǌZƿƏ˵Ӿєϝȥˁ±ʃɖЀȔżӥȵӐhѰԆt7ȓƕ',
                            'ŬŕñŻɚҦŽ˪ϜǫΩ\x99Ɛåω2Ʒǌʀ˸ӖЦĶƐzƾəĸƗі',
                            'хFҲǢΖҡӓǥȝȀŤϔŵԘƶǪϢӷðкËŒϕӧǣ\x8fȠ¥İŴ',
                            '\x9cȋˡăʑūӇΩ',
                            'Ž˺ҫ\x9eБØχ_ɿѴ\x97˩żЛѹϑҠĳƘɔ1ÚϒöѦʷĲ¨Тʌ',
                        ],
                    'licenses': [
                            'ǶÛȗϳӗɀӏӋŧȼĻЅƱԆЎvýȺǿGжůΨѤԭ]АÎ\x96Ԏ',
                        ],
                },
                {
                    'name': 'ýԈšRɩɖŹӦ˖Ȗԩ\u03a2ƊŒ\x89ʛċŨнʺƭŨӝӻŲhťϨΆȎ',
                    'version': [
                            -3471647102753370635,
                            -6561390051630061662,
                            -3573761569227687679,
                        ],
                    'about': 'äеǅ²ˏӡŉɨĠα\x7fİƸԩªжӢ',
                    'description': 'ɻӻяюȾ²\x88ȋ\x7fӵ¤īу˵Ў\x84\u0378Т҃ҙκѦȌ˧¯ъʷӊ˙Ώ',
                    'authors': [
                            '\x99ƠġǻsƲ^ӻȪѯȰԆ%ȌϦб΄ʛѡ¥ԬˢΠǜɷҤʏӦϛϛ',
                            'ˌĿFǇӝˉӡϿMϮѲŻȨӑĠЕɭҬԜ¸[ǴŒ\u0382ĻħЪŝΉγ',
                            'ƬәǏӯυԉƬӯĤӝ½ӆũĈБͳϪ\x98υż\x9eҼѭʟΧĘDԧ¯ƍ',
                            'ʡŝĐ\x8dēӰ~nʊķ×ѤҬГǰʖǹїΠҏдȏѭǃϦĿӟɇǼҒ',
                            'ԥΚσȣώԇΜχˇԏ\x84ŗʫÀřħδ<ұ\x8eѢ÷ӟ˻ϷʒʚɏĪĲ',
                            'ЪЏΩҚ&ӞӊŰѤȞ˰ȼưRхΝ5҄đÇҢӄґϑǪӠϿʭˏ ',
                            'ШҺűюґőīĥçΫϷɖĢǭƌɯˊӴßΏϧΑāèŘϯқӋÙ.',
                            'œΟ˹ƫƏâÝÙѕ\x9bŢďɌȌȟÂʼνӜѓ\x9fѝ˴ēʈȾӼ\x90³ӵ',
                            'ɠǆɥƖΊΔϭțУҨęԏĜǄҔǀ\u0378ȶƛǴȩŹȇүѶɣԀϑɐ,',
                            'ҭMţőŶͺԨ\x97ȇɄĈƛĢ˻ώ«˓ͷŒɻş1ӴͱΆǩ\u0379ɲ˰҆',
                        ],
                    'licenses': [
                            'ƻӧǣŎӑΜ˥ϽђȳĮ\x85ԇ3ѩϗĜҧĹȂҒϖ\x93уʊɭ0ѣ˂Ϊ',
                            'ƑԫØԌóѸȮԙӸɽЇтä¨ƨ\\ðЗΒǷ͵˽āѲɱɑȷ\x94ҽ!',
                            'ʳęȶJ.ķ϶\x90ԍ\x97Ҭɡǒ«ˁɂhϯѕÜɠĶϧΐԈϬѶ«Ωʍ',
                            '˷įĤƢѺ0\x80ʣĹϖϽЫǟəϜ©˧υϹ×ɗΕнЧȣųmɋc.',
                            'ʔ˅®ҴĐƸƜԛÐȪ˵ɖу®f҉\x8cͷϡAѮʰńʣ>εѻ;¢ș',
                            '¤˫ԈįΣӠˈɜ˷ƛ]ϸР·Д¿êˇΜЮԜĈ˫Ȝϵƛɮɣň˂',
                            'ʒʑƥпÝĸԀφċY\x90ϼ˜ζȺѨδËɊԚϏ2IӗјӘӻȃ˹ʖ',
                            'a\x98 мɞώӝ±УɚѲ;Ýџοdǒԃ˜±ȽƮќĆȏœǗЂʙǈ',
                            'Ġ\x82ʷOκʥ)ѲԒɑзƏʋΑΓªŘĳΚƻӸȅªԩϒcŭΌͽ',
                            'LɖƃĶήϾԥƓǖ\x9cЍαԁ˧ϠĒȋóXlVŹѾ95ƬŧԣƟŁ',
                        ],
                },
                {
                    'name': '\u0378;ɛ˼ćǹȺЦәɮѳѲɝρʽɑůǘќÒɽˣŅζǽȼӰÝԦÃ',
                    'version': [
                            -7373862023911342260,
                            -4278946314013872601,
                            -5243786515913236759,
                        ],
                    'about': '*ĔÀʊǻɹԉ8ʇӴӋȊǤ\x83\u03a2ћыŝӃҭ˅ǜk»Ӻюˡ$Ƀî',
                    'description': 'MȄVȘòćœŒŴЃ#дǦȌȲìӤĦΕѡǁˇϢϒŨˆ°:ɧȔ',
                    'authors': [
                            "ǆβӞȶαɻЄȓͽΜƘʚԍӋήØФѮӛ'ȁϣ2rȌϥīı˓˹",
                            'ʣ϶¥Ԍˌʥ˕ʄɤеđʮԅѷ',
                            'ґȨɨԭѬΥĘҒӂʨ ïҺĤЉĔқNʋſǾӨЖԋ\x88?ÍǬÁɗ',
                            'ÑçʂɖԂŢњRɻĢC¶ǂƣξϰŹÓрøʞѿ/ƐӝϙˤŶϱȫ',
                            'ΜµȇŰӽĞDǌk\u0382љАƢҎǃ˲ʴșԪ<Ȟƪǐƨ\x9dĳǡȐʔz',
                            'ԞϔőPjHжǶƯ«HȌ¡ƨÁɎͺÀи˟˶IˌЅѹXˍӳÜҕ',
                            'ЌɛѤɦς·\u0379Ç·ԌʼѥԤ҄κǱԟ«Ē£Ŭ˹±\x97ȮYɑԑВĀ',
                            'ƜԭĲʼȯýԜīғ',
                            'ѿӡİúʙЙƇēɒғɝǼƒΐќСþɀ϶ȉīƙƢ˂ƹ1ˡѹƨť',
                            'Ӥʯ3ҬĶӘȺŮҢ˓-ȳˉǚŎƄȒą͵Ūʠ˽ыͲ˪ϿїɍПκ',
                        ],
                    'licenses': [
                            'pįҪɢҺϊҟеұάȎȱџĨɨˏϔǄ]ɚΚԠiϭѢƛťӕПӘ',
                            'ЌšҰɲʶϡӯɪЏ˫ĠHÎŚȀјăĖΪҴFк«ÑΟι¦Ӂ?ӷ',
                            'ԎͲ\x9bчɏЀˁDɽϚ˟\x80ɄʦΞÁĭн\u0382ˬр˳Ǥ˚ŴҞҶЍχɥ',
                            'Ӣˉ*җѝƙψ"ӿ\x8cԪίҌʪνˆΫΧѻ˄ԓԮϓɼΑÄЌа¦(',
                            'ŔZŷ˘ŢȳҭɐȸӌɻƚÏ\x90ɨґȔƍдЖќɑжӂʻΟѺΠǺʆ',
                            '\x9eӺÏǥɫ4ɃД;ӇДƼǤЗй-ǮȯÍɿɪkǣřʡLҨұŚø',
                            'Εé8Ƣ7ϛȵ҃͵îӦŬӽΌwʽ¥ҷ¬ʏʡĴʘԨѲ§ŎɬǑƌ',
                            'ɥĸΧƒǢЍʊˑ\x9d\x8cǅ|HӕЙԙēҷƱƢğɶϻѲƾяԎƨ®ǡ',
                        ],
                },
                {
                    'name': 'ʹħɨ҉ǸϞЇUӤǍ\x8fǗĐΉϟ^ɜ\x7fԏĒѼțǳɒɾЖ×ԅǀϣ',
                    'version': [
                            -6812807492289050694,
                            -7760195044698970644,
                            -4003518769386816418,
                        ],
                    'about': 'φ{!,ȕ҇ĚӷĦ·\x9fҨâ',
                    'description': 'ňԫԦeǯ˷ЂȯԢǥ9˯ȬҊŢȢ²Ōǩ˱jԏϸˑѶ#ũɆҳE',
                    'authors': [
                            'ĮӋăěԉΉĩǷΦϏʊƹϺΪΫĜ9ɟŻǪм\x9aӭñ¶ϣːɴтѮ',
                            'ӕBħΧƶʲ',
                            'ÀȂȥĩӊ҇¯eѠΎśŇľʞŞɈʮǁ+ϰĹ҄ϟɿϬǷӾƘӅЯ',
                            'ǩƃ˕xƶҞŝĹsǴҴҬɝǸʄѐʞ·6ѐɟı¼ΪȥϼҾ˻.М',
                            'ȦˊōԭŠǉ\x91ȴѧӇ]ԨŜ+ʵħ˭ʝ˰Ɋ\x86\u0380҆čМ\x93÷ʇѱˢ',
                            'δ˚ҕ\x8aӁиƋӎҳƃɦʙȕ҃ҵʎ˔ƚÞþ\x9eƞέ<ɮѿƬϙИz',
                            'Zәӄ˶һпҕˆʏˌɁͶ\x86ůȩ\u0382ó\x9bϔWXȖФЧФŵϳɞ҉İ',
                            'ÅҝnЛȷӒÛ>ŝȼȌɝˏήhȋӤˌкΣӚõƩЫļɟҎƬԮb',
                            'ӕӈƭ˄&dĈԍbãȮȊŲ\x8fӁwҖ\\ӚʑWӀʍǣȱ˭ҾɼťΫ',
                            'ȻĂǁ˫ΖɊĽІоŴĜ\x80έƩ¸ʥȣĤԨëȶĿ҅˪Ⱥ',
                        ],
                    'licenses': [
                            'êƫҔžԓѬʴɷʇȳԛ˹ɐǍӴȋΑϾŧћɽǉʈĝƈʢƊƎϮȽ',
                            'YƏшʚɗΖǡĴͶ¤ԂӡƊƟѫ¼ԎùâǨΝkâŌ;ʎNǛӝt',
                        ],
                },
                {
                    'name': 'sФюʹʼҐȰήϛҦӱŧЅź¹ȐˋȷЛƷҥǷӳҫοӠƵlŞ˒',
                    'version': [
                            -5361023548279675058,
                            -5444156087244849325,
                            -356950409429765453,
                        ],
                    'about': 'ǥԆØøи',
                    'description': 'ȫ˓ďϓфΰТ[Ѿ όёщĸYҼȿėɺǬͺʛԕħÓƚҵӨ\x9a¬',
                    'authors': [
                            '·ϯͱµѢȠԄDςrńƹɋƦӯĮлɴόӃ҉˵ŤҶΫϖˋƜďҗ',
                            'Ύ\u038dͻŖʍıӘΰƧ:Ɍ¬ƯƲĚ҆Ƌ϶ĶĪˍИӰҝԏȁӧɚůƇ',
                            'ʖŚΑνʚϹԊŬÅӋϔЖƳΔҿΕϿȟϳыӛęƬǲƻҮҼzоӅ',
                            'ǃҽˡˠ«ѷǳđȇͼҒѣǣтÍˑ¡ˮҿwʆƀΌŗʙθŏɻåЦ',
                            '˩ңϏɏw϶ÎƑԧɥǧтźʒŒ-ʰґÐȖˊаσƒԘɮϏ˾Æ1',
                            'ϤƽűϏǮĆĕ\x82˥ГҵlǺӟӒ˜ѕѸ˥ϫƣ˩Ί.ԍԐŤԅӯ`',
                            'ҷȪωӟѷψť¦ŲǕY˅ǟʤl)˳КιӓǉѶҩϙόʹʸ¼>ȫ',
                            '-ԧӂűљңӬƓΘѾŪУƟǯλȃț§ÐАϾϽ8˹Ӗҳ΄\x81МС',
                            'ȓƜƼǀAWйʒɋʻƈȷϏԫʢũˣÊӊŉ˱ΤɝӺϱȲȖȻȼ',
                            'ŅԢɾǕΛ(ÿƴЉˏ˟ŷɪ\u0380ѢΠŉeό фƮȊʹîɏϐӳͿɿ',
                        ],
                    'licenses': [
                            'Ƌ\u0383ōˈӺ`ġҹЕӸѶǐα;zɓϻŞĴϣţԇǗŵɶǑʒ҆Ԋ#',
                            'İү£ϫƋ˼ǵѾԧʓωԨЛǗԖ\x9dɖ\x90ўĦЇÀӭ˃ʥέyӻʾА',
                            'ʨιʦ\x8bˑŝȭ&ΘӴɑ',
                            'әǴξǒjѣ˷ЉǈєәσɹϧȆŴЙӀԆ»Ӵ˙Ҳѹέżқ·Нs',
                            'ѣƱŖʻˈî«ʲҦǥ\x84ˬϤϋӊϰßεƶԟӌ˧Һͻ',
                        ],
                },
                {
                    'name': 'ͼ˯҆ΧȇѹӑƆ\u0378ȒңʍϼҶЯϕňʃѤӳɭȡ˻˞ƿŨ\x86ϱЌŊ',
                    'version': [
                            -4598994126124350725,
                            -5425846301686081145,
                            -2648985981675648327,
                        ],
                    'about': '|ΧYȭͼ\x95ԈÑӛŬȣӬȡHÅеėĄέȠϱ+ҿзíπŧMɓѬ',
                    'description': 'ǌьсʒУƛżҸÒ\x90ӢŲҢǹîÐþ®˖\x8dƻҁːāě˒ԮϹX©',
                    'authors': [
                            'ÚWӎʧӚĺăη˙άĜ\x82ɣӞҊ5ơӵӟʃjŕŮœΨ˺ɀхͿǯ',
                            'ÍӄӅĺʹиĒԘƼЋЉОЅϿʌϲцɠɐ{Ký\x89Ѳ`\x8fΘˏÉЈ',
                            'ʙĀӆЪηŃʲĿΔԡʾ\x91ħ¹ʋγΡţЄϺÛШѐљʙŁ°ʚÉЅ',
                            'ǮŶŢŒɅǒ3ҞɚƉлŪǁ#Ѓ˵ȁĎȌʗ˗\x80ΫЕÆԁͷβd.',
                            'рƐȉЋ#ėӹȌԡŎԛћɃ3T ÅøŌÆĵμӨҼԅ\x80Ӣ˲êѝ',
                            'Ůěѡ',
                            'ѣǲғаǣ\x92дʭƝƑй%ЗΚĹѾ˟ȁӞяӺГŠ˻Ԗȓ@~Ӏҹ',
                            'ͼ¹ɠʘϣ1ĵȚqɤҝɜϫşβèұʺhѭФ«ʚǡ˔¿ƬǞɁɿ',
                            'КԭEčΚ҃ѡʬԉĨĊВɠȮȦÐɗˊʷΎы\x9f˩ΞѸƮӶϝƫǞ',
                            'Ґ3QӴłÅќ7яŪГ>ʣ¯ģɓǎҩҹЀмˍСҳКǋξͱ55',
                        ],
                    'licenses': [
                            'ǟfͼā4ɊƯé\x83ЛƎʟ˒qxÞËʈʒӜǊØċƐмȆÅ˻ĝƝ',
                            'ˏǚðΑЮƁØ-Ϥƙф÷ǣӬҀʲ˾ԋƇϣƮ&ԅћĦчNŒԍѪ',
                            'ωҎŨʥȓƎ',
                            'ΠȵèŹѦЊͲ9Ӯʏҿ¤ġθȫŝҀІ˩èǪhΡДҘRѝŁҭɒ',
                            'Ъҙ$ǈǋʆǮǄнBȣƄ¿ҕıÓ°¥ͽŒ2ҩsѩlľɋʂ¯˦',
                            'мѼ\x88ƛѱǚƝϭϺԋ0\x85ǂƂĉÝԭʹΰΞ҂ϸɯƔʹ˘ӱÆ¹ă',
                            'ųʢϸԛеԎȵȸW\u0381ґļ',
                            'Ɨʚ¸ƊŅúǽˉԧӫͰӨԎҢԣѺ\x81ϮȤƿќϚɬ"sȕƽˬϏƽ',
                            'νɍΑƭԈɇԋӰɕӴ1цҋXѰƨƼŕӒԠˡʿ˝ҎɼǬƿ*ζӉ',
                            'κϘКĥƇοO˺ҭʆƀʩ\x98ҷζęӷԊɟƙӨѨO6Юˤę˛ƞȝ',
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
                    'name': '˜Ϩɢ',
                    'version': [
                            -4220388752500698020,
                            -3060865951047756214,
                            -4551258112411564391,
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
