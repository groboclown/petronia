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
            'locale_code': 'ËȽӶȦǏ',
            'catalog_name': 'ƟG˔ҼέŸλϵUΗԅHÇ$ңƹңϕņͿǗѓѻΞǛ7˪ăăɘ',
            'message_file': 'ɜɷJМ˟ˌƁ\x85ęǛ4WÏɓȚk\x85\x92ԞȖέˌʰŒԮЭЮʕÜѐ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ұ',

            'catalog_name': '~ɲ\x82',

            'message_file': '-А',

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
            '$': 'ǴѷȥԐɸҰɎӾŎӍȇһɥӧ¿ŻǭӥІΈϬʊÉүԠӔӰǘ˵ʿ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -7663010854199061236,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 354674.7488293801,
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
            '$': '20210910:162108.722783:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ӢǞßģɬāΑï˼ИäľăВԥƵԘʂǰ҆ʳʹāȕЌɴюƘεͶ',
                'ˁΊǹԤέ\x7fʁЦͳθvұƧԀŮȂÞ\u0381\x99ЙӮЦʡόгϾӣҏЊņ',
                'Èģҝßȴ8òŪͺЖŜ]ЖƲ%ďԁºβ·ŝФєlwΣˬƦȖʃ',
                'ǨˌʂŝȁҤӕŐȤӟяӢђƛȄɬδȆƖǐňͰўӼˏÈӠȅύƵ',
                'юǓԋϋɡǜԐĉśҏʋúƟ\x8eÂEϢҽґЀıǨ9ҏãҵǀΚˉѦ',
                'ҍ\x8bхϺŜɈǸΰӗÑ4ś',
                '|ŰԢб\x9cŭϷР˙ÿMŭOȅԟȏÖԟˑο@ЊħɓñԥœǶ\x96ԗ',
                'êĿδ\x9fĐµƒ˚5Ȁϙ˩BħҒΨ˹ȖцРЙ˅ƺ@ăеύ˝ѲѤ',
                'Ϩ\xadÂ\x8aѷǲČЙ8ҐӷΪЙʛȩˤҒeǛԃтȖÈәҎΏrǙ\x84ņ',
                'ɄƏ\x9cŉ\x98ҙ¦ԛ)UӄύҮɻĊЭʱҦáˁşɏvή-\x86Ǐ¬ʽԇ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                2873503905693704890,
                7766936539211877585,
                -644006678765456732,
                269776922758988895,
                1756004957475286629,
                226320020142187840,
                -8627218174116429254,
                4002847926724721168,
                2551504846879627796,
                394646528565236447,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                511276.26005800755,
                124806.49233681502,
                -74058.11548557517,
                968018.5912345522,
                663182.7948435947,
                395765.7376794759,
                108511.11268762295,
                247405.84930767363,
                -69182.03731801274,
                34995.218333179655,
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
                '20210910:162109.817699:+0000',
                '20210910:162109.838265:+0000',
                '20210910:162109.857527:+0000',
                '20210910:162109.879305:+0000',
                '20210910:162109.901720:+0000',
                '20210910:162109.927609:+0000',
                '20210910:162109.953969:+0000',
                '20210910:162109.979895:+0000',
                '20210910:162110.000243:+0000',
                '20210910:162110.020441:+0000',
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
            'name': 'ʜ˹ɬVBÃϸοĥǚ',
            'value': {
                '^': 'float',
                '$': 346669.8193908763,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ʌ',

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
            'catalog': 'ƱԢ_ȮƷʯùҵąąѓʯőɍδȁǝŧſɨЦǞѦãUƈɔϱУϤ',
            'message': 'ɟĮӇɏӪǑϻȆĳԜЇʰ¥ŔӕҭǓ϶ɨѐMÔӤЪǨɐʺɦCƅ',
            'arguments': [
                {
                    'name': 'ɓԬGÀϕԌĚŸ\u0378TN*ΦĢv\x84ʽȖʞɸ³ɯТƍǮĚϯłԄѧ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210910:162106.719272:+0000',
                        },
                },
                {
                    'name': 'ŬЪ\u0380ȷĖ~ƼʞȿǏȔԮҽӬιҁΦħź˱ӅϕϖhÿһЁÖʄ˒',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'Ɏʆ҅\u0379ĜǢѮǠĕϡѿϓ«ʖv]ƭǭƥϡǫ\x91ɄUЗFɦíүó',
                                        'ˉXԬ\xadeδYɐѧÍˍϒʮέі\x89ĔśӀhÉЍȈȜ}ӷ|ԩŨҤ',
                                        'CԦ˸ÅȩŤѬӮ˾ЊжҎ\x92\u038d9ǔsƤƳϤǺоɶҾӤŻлϋŴң',
                                        'ЏŪӞ˝ǹɇϲ˕ЮҧʩңʓɢŝȏτѡɄkƪӨѡħŔǝϝȻҜȧ',
                                        'şνîȥ˱ϦͶŤӠѾǒʘȐӊƞѶ\x99ˆϾųӻЪɓȧƛκǌÝǫԜ',
                                        'ȣƳĮ\x9d±ƹҫȝɟĢІɞ҆ĳ\x97ѸƟQ\x80\x98ѼƆӾЎɣ|ѤhԊȯ',
                                        '2a¡\x91ϠįΥɚΗȲǧ? ×ɟӚɈӝƖιǐԌ¿аЉžȈŎƯž',
                                        'УϵˀӯҊ˔ƤɞУo´ΐЀԭb4Ӿ8ˑѬÑӹϣɎҤЙÖʹʓĦ',
                                        'ʀă˕ѺͽfϑäĤþʃÎʳʣЖ˧ѶſKpΥҵӥɨѻʘԏԚкҒ',
                                        'ζǆӵʛ`ĴĖϙӽԩƐƘģҟŸҏʜҹi˧Ǵÿд\u0378˯ˋӠҡѰƯ',
                                    ],
                        },
                },
                {
                    'name': 'ÍȮ/Vʰв',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ǲ\u0382λÙľӭƈĝĖñʝâʁ\x93ɅɍӟιĮȂϰʌǘϩ#Ȯ5½аȂ',
                                        'ɬƜʥźЖΐ\u038dΤȽˡӟɂÀȽϪԋѢƉζhǴΧΊ\x85ͿѬκAǩɥ',
                                        'ɬΠEΈӪЏҫϔƭʮïЂϕʋϾŞϿÚӜҠ˦ɸĀʁȄҩҲĮʩȤ',
                                        '4ӅŵρӎҺԔǜʚӏұxВ\x85!ņ²ĬλΛӦтȬƭҶɂҩӐȰӍ',
                                        'ΰƽɰbŒң;\x92Ĵϫ--˂ɓӒι"Ѧôƈ˙ԥƢnΔӼ\x92ѬǕʕ',
                                        'vӞӔԂϳԮЅʮ҃ѽˡǭÞÙǪҲ\x96áɿКǽ˛@Ēʸùӆ0ƽƺ',
                                    ],
                        },
                },
                {
                    'name': 'Ŕѩ6ɌĎ\u0380ӉŕĎȦѧʇĎϤ´ʜȄ˥χӒӭΕʺӉŅ˥ΆЉӉЭ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ŗĠ\u038dǂɸZǃȮű',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -1384448825017516811,
                                        -4468666859597704442,
                                        -7963655580905852510,
                                        3784927903576893537,
                                        -3041049521770485150,
                                        1673968378076417696,
                                        5109634764254294182,
                                        5498858110240920494,
                                        -5794090089729008020,
                                        2313020055137546622,
                                    ],
                        },
                },
                {
                    'name': 'ϲӇ}ūɍƞˊάɾϋFǳĢҷ®',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -2065963971804286757,
                                        -6060536089013332998,
                                        -2357196859699110097,
                                        8768741508918012154,
                                        5733001440978248801,
                                        -4379649858740235917,
                                        -789630072921775464,
                                        -8223523003712772215,
                                        8950467557607345496,
                                        1309311014724750273,
                                    ],
                        },
                },
                {
                    'name': '\x94БŽΕƎΚϢƛŞŪЕƾӛd|ԆŝƴȎʡȣ0ǒҸĝ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        True,
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
                    'name': 'ƭÃћȜɊ.ȘͼɕƩӍʲѕɐʦKòӷ\x99ɾϹĀȴĚʁ',
                    'value': {
                            '^': 'int',
                            '$': 7057696806141997457,
                        },
                },
                {
                    'name': 'óŎғȊ"ɾ҉νʊӃϲ˛ЎƍτȝцȪśʠǞěȹ',
                    'value': {
                            '^': 'float',
                            '$': 785697.8289985385,
                        },
                },
                {
                    'name': "ŜύñѿǵӅĒǼшҪŐҀʣȊř'ДиƠзˍίȤіǗ˶ȭëʼӠ",
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        729056.1335707493,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ѳt',

            'message': 'є',

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
            'identifier': '˩Ӫҫȇ˙´ŢŬ\\ôͳMęʬѕĐȝȓɄǝ˜θǜԋͱrÑӒϞ~',
            'categories': [
                'access-restriction',
                'network',
                'file',
                'invalid-user-action',
                'file',
                'internal',
                'network',
                'configuration',
                'access-restriction',
                'access-restriction',
            ],
            'source': 'ƭȨɾӒŒʞșˎģҫЭμʯȾӷ.рɾЁNʀХɼʛÏ¶ȵҢ°ԉ',
            'corrective_action': {
                'catalog': 'κˆŒҧŋɬʤʨĹGʑűЁŦÕѿЅіȜ7ԤФ+ĬʁʤǓ˔ɠǊ',
                'message': 'ӂ΅Ёǆϭ{ʅԉИӏŁѽlÐˬċπήƺǦʔ˙ɵ\x8fʺ΅ʌƣύ\x82',
                'arguments': [
                ],
            },
            'error_message': {
                'catalog': 'ѡ˭ʍѿǗ\x80Ә\u03a2ǍάԁQΡǘǭӚΙҌЧϻņЩüӌГpϞōŴƘ',
                'message': 'ҕЌ$¡җÅXԔӔνάɥϰӎӼƝӳ˸ÑĚȵżƠˆɀҽȭ\x9aѡΰ',
                'arguments': [
                    {
                            'name': 'ʸҹƅ˃˅sǹǶǄ\x84ΤtԫȀԌгԔɚ.BʕǺҞϧ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210910:162110.294579:+0000',
                                    },
                        },
                    {
                            'name': 'ƁδїԆЫђȢɨѶ\x8c˲ņȌԚŐȽɢɍˁʘàͽΰ·Źю˞ӄŦҌ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'eú',
                            'value': {
                                        '^': 'float',
                                        '$': 94230.17877784214,
                                    },
                        },
                    {
                            'name': 'ƪΎȮ«ZўǮ',
                            'value': {
                                        '^': 'int',
                                        '$': 2242677021580713785,
                                    },
                        },
                    {
                            'name': 'ĐЩƋϺƯӿüԗΆτѿϥɑ,ġԂĹ\x8fŅжȡƺŖОeǱɅ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210910:162110.593694:+0000',
                                    },
                        },
                    {
                            'name': 'ʤǰ˪ȾԕÅȠѢԋ\x9dѲcįϸʻĢȒδɜɜǞФӝįBўћ˗Βǋ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ВƆΕƤïȥГ7ԓѸˌιʺΗǉίȺЊơΕѼĬ˱ˢŸЗǃ<',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        True,
                                                        True,
                                                        False,
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
                            'name': 'Ũǀʩŕ҂Ԇ\u0382ˀȔʓҍÿхH1ƝʈʢȺͿс2ЗȉɺƪΜԠŘȢ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ӘȮѳɑŽβҨȻκÝIԁǌɅҨ³зʨϼǱĺ˟ӊʒʔˬēĎҐȚ',
                                    },
                        },
                    {
                            'name': 'ЉԥЏ˘ϣɿɗǼƅʢѽơÆӊϨȊr\x96fĳψŲɮƛѹѷʴѿŴҮ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        389.2125269640819,
                                                        934699.9378819867,
                                                        470457.3530083974,
                                                        914725.1040828335,
                                                        430024.96438663895,
                                                        991810.2853591118,
                                                        370605.6807364752,
                                                        504484.10947012715,
                                                        195906.56208046223,
                                                        -16160.621541220782,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ƙűE¶ϕӭɿӭ`ŤΧ',
                            'value': {
                                        '^': 'float',
                                        '$': 368973.6635701884,
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ƬȨĭŏh',

            'categories': [
                'file',
            ],

            'error_message': {
                'catalog': 'ĝѣ',
                'message': 'Ķ',
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
                'identifier': 'ȑʓіΓNǉӧшΈφӚɅнτƏ¤ǍĕϏʯŹәʑȞӭǆƨPņԛ',
                'categories': [
                    'access-restriction',
                    'network',
                    'file',
                    'file',
                    'invalid-user-action',
                    'internal',
                    'file',
                    'access-restriction',
                    'configuration',
                    'access-restriction',
                ],
                'source': '˖ЬԩϻДрęƽαƪЬiʡ@ҜͰɡ\u03a2˥ÞǮʯ\x9d\x80ҁʁɮ: Ũ',
                'corrective_action': {
                    'catalog': 'Ͻ˶řŮԏΕǸ˯ћʷҎѴŰĎʳɞƈȓǍΉƵФӇțˍҽѥŉɁȈ',
                    'message': 'ʙӸę£ί˱ûʵΐʙӎř\x81ӿԋЌΜϸл˖ԙËȅЎħɞɍђȗß',
                    'arguments': [
                            {
                                        'name': 'ϯłřԣǗ҄',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4100804131701927789,
                                                    },
                                    },
                            {
                                        'name': 'ЇǮͼ\x80Âö˻ˤ&ԋȒƄΚǇθƾĖΛƌɺɏȯҦϻӦ~ҎʏʖЕ',
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
                                        'name': 'ү\u0379ΒɣƶďҋƎŢåѷÛéűɻҚѢ2ƦҟβЀȈʃяȂʳǕ\x81р',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1558553878775119297,
                                                    },
                                    },
                            {
                                        'name': 'ȋ˨ƈïÊǫӽũ˟ǏĞʞ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 755472.1698527035,
                                                    },
                                    },
                            {
                                        'name': 'ȥȀʃsƚ;ҵÃȠҊ½Ӗħ¬ÑƳ\x7fΖĚ)ȿΦŬ=ĽɆoͲÏʵ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:162102.728725:+0000',
                                                                            '20210910:162102.746618:+0000',
                                                                            '20210910:162102.763530:+0000',
                                                                            '20210910:162102.780473:+0000',
                                                                            '20210910:162102.797959:+0000',
                                                                            '20210910:162102.815715:+0000',
                                                                            '20210910:162102.833405:+0000',
                                                                            '20210910:162102.850733:+0000',
                                                                            '20210910:162102.871515:+0000',
                                                                            '20210910:162102.895902:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΊΌϏëƍtÇж˗˖êϬ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƅȲÆЦԎȻʹϙxІѻĭςrɼƫôʨɦ˒țӀÄNƧˋΓˣԑЏ',
                                                    },
                                    },
                            {
                                        'name': 'ǉƈʭϪԊǓɳȅАğKΐ҂ƺшɽӁЌϬʂ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            748089290272487468,
                                                                            -4173753873279224997,
                                                                            -7518983076661754159,
                                                                            -1422374103528952657,
                                                                            -628677514556875428,
                                                                            5763056876647097596,
                                                                            2181129855540044312,
                                                                            219041626929378867,
                                                                            -1642485486221100707,
                                                                            5998056920949151033,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'áҴBƈ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            378571.89095254283,
                                                                            49447.81543492753,
                                                                            142923.8598842055,
                                                                            843526.3772918134,
                                                                            397093.45076081564,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'тŦȮŔ˚UӮ\x8aFŖƋӌңбяGŅʨΈѹʞˎɫϋ\x8dùӨlҏ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɵˉӆΥȿӧ\u03a2ԄǎɨәǩħÇþќţʧƓЊƣ˳&ôԘ˯γϯЌǛ',
                                                                            'ɖԣΧƓȋБҽʝΙуϛΗӒ3ωÓÁ\x93ұųņ˞ϪȎƚƗъåʈӊ',
                                                                            'ϬǶЛĒГ\x91ƽΠɐжeāԘ΄ԢӮ˹ĽƅȰҗԀеʽʄԑҒМӉƎ',
                                                                            'ӘjƄ/ӤĖͺlƓeʑĳĥȀъϮύ\x83ŒǙσ҉«zјĈϑӢ¥Æ',
                                                                            'ʦ҄DǍɼɥǡƨmƂĔПˎŪʡЬpϯŜΞɅªMҋƂ΅ʚȺ˳\x95',
                                                                            '˱ҕ¥-єЎ\x8cÿ˴҅¾Ԏɟ҆ǶƣˎI\xa0ʁĽÉãԠѥаþνͱЁ',
                                                                            'ʽ\x89ҥOȳΎȰӺ˫ʉ\x8dɊӮ9ĻӲϟ\x95\x89ӴɬɀԁӖQђKaćȫ',
                                                                            'ΈɁ]ɡԩ¯ϣʦʳ2¦ӄȦkǘȤɸɳВ˞ǈhǗ\x86ʖǶ<²ȓϯ',
                                                                            'ΛьԖ˕ұx\x8dȯӂėøɘ}ơŌ\u038dȗ¨уűȗAӽҔćȤʀȥƥɉ',
                                                                            'ϤПвǱėǲȼÓʢȄњҩǯ¦`ǵјδѫˍóԓǻҕͷɹgˑůҫ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǟƫ[ЍɉƌҵԬδˏҙϨŕфӜjӼĊѨğЋєԀåsùԨaҐ±',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
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
                'error_message': {
                    'catalog': 'ǅ+ѡөɝǕƲļԮ˙Ȯ1Ŀ¦ƔüЏʮҮӀˇ)ʬϳ\x8bƑɉŁҧΠ',
                    'message': 'үêνƭȥǁϕ\x88æѶďƂƳʂÜţϣŅȦ(˦\x9fɛԮƩŵſĢ.ц',
                    'arguments': [
                            {
                                        'name': 'ɛҘʗȕŋĤЯ˗κӴϮҞ˷ÓϳʃʗKρĚȉπ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -970927588339843976,
                                                    },
                                    },
                            {
                                        'name': 'Ѡӽ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԝϰǵȂtɼД6ǣƣĕŬІπ\x9aɚҹƾƮ˳Tϓǩ҅Γͳ*ɏƳɠ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2456543995898681555,
                                                    },
                                    },
                            {
                                        'name': "Ƚ'\x9dԑŘŞӖˀϨҭɐ˄³áò¥ɨąʗɹ7\x95ѯƎǗtǅ҂Ģк",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8013014999385494950,
                                                                            611040482329900177,
                                                                            -8791892975731744867,
                                                                            -8213271848618325965,
                                                                            -4097480785717375077,
                                                                            -6308478524117538492,
                                                                            3248561866318168715,
                                                                            4752868810478608554,
                                                                            -2905469016761768086,
                                                                            -6310648978450349710,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͳĉɁɋĀҷśŵ!',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            570546.4913140184,
                                                                            463388.61180856463,
                                                                            746517.8157217244,
                                                                            517216.09131502546,
                                                                            -47077.700502556574,
                                                                            782475.1786101479,
                                                                            337494.14754091494,
                                                                            996610.9937320559,
                                                                            510994.0754446605,
                                                                            337708.37819354,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Пȍ\u03a2ĮǻӂүʰˎŢǮϣÌƂЭϓПɢΨĻɫԫƆƮʉЫ \x84Āǳ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
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
                                        'name': 'Α΅Ӝѕ˺Đěґ·čȿԜĩӛѤ¥p˄ǇtϹĥ\xa0ˎ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԀƝҵ;Ϋ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҶСž҆ҊʱùĚˡʞɃUʓϗɐє˥ɗԑΣČѳęҽЄ}ͷġϞǤ',
                                                    },
                                    },
                            {
                                        'name': 'ԙҸƚҩ\u0378Ǩ\x9a\u0382ϗoJӯˎĠļԬϿюı/ԛǪԘƢрƝǵˣŗř',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:162105.513725:+0000',
                                                                            '20210910:162105.530117:+0000',
                                                                            '20210910:162105.547521:+0000',
                                                                            '20210910:162105.565247:+0000',
                                                                            '20210910:162105.582729:+0000',
                                                                            '20210910:162105.601775:+0000',
                                                                            '20210910:162105.619224:+0000',
                                                                            '20210910:162105.644845:+0000',
                                                                            '20210910:162105.666325:+0000',
                                                                            '20210910:162105.687062:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ͽɍ½ˊьJώӯĄźҹӽҹɢśϟНǩ˼ƏɟДήϢϺӋ3б~\x88',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
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
                'identifier': ';ǐƂJw',
                'categories': [
                    'configuration',
                ],
                'error_message': {
                    'catalog': 'ϕу',
                    'message': 'A',
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
            'locale_code': 'ǭͰ½ŨƙАϋ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'Ӱ',

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
            'catalog_name': 'Ǳ҉Ґ\x90Ź\u03a2Î͵ƕΑ҆ΉђƒЗʑ:àЏԧΥυӬƽʪϧŨ\x8bӡҒ',
            'locale_codes': [
                '÷ͻϑ',
                'ҭ\xadōΩƌʋıĨ4',
                'Ѧύ',
                '\x8b',
                'Ӯӕb',
                'Ʀʱ©ǑΒБĀ',
                'ŎĢ©ӾýԝӘȝʶϵ',
                'NŌȟčƆр΄ʼĲ',
                '¿ýϛЦʔ',
                'ˍԃҙΡ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog_name': 'ȁɕœ',

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
                    'catalog_name': 'ǀђŶF¶λʲ҂gɱřϔʕԌǱѹÆ҇ǞųÂҍԨěїȅˬӗə˺',
                    'locale_codes': [
                            'өϚҧͲӖϺɜ',
                            'Η˝ҕ',
                            'ʇҎȠɕώ',
                            'λ¡ǹ',
                            'Ě˗Ʊ\x85Ǝ',
                            'Ìʟɻ',
                            'ś',
                            '²Ӥ',
                            '5Ș',
                            'ĕĮϏȈŢ',
                        ],
                },
                {
                    'catalog_name': 'κʇĥZǢçϻļŚɛěхȋŚІ"Ƶԇ¼ȥԝÒƂМѴǊ\xa0ǮÉĞ',
                    'locale_codes': [
                            'ʐұ',
                            'ŀȌӠÃǰ',
                            'ȠϺȆǗƒ˱Вǚω',
                            'ʯʄȜъąǶuΒ',
                            'ȅҬ)Ĺ',
                            '\x9c\x7f',
                            '\x87U\x9b/ӜƊʉ',
                            'ˊ',
                            'ȢӔԠҷѡS',
                            'ʲȠɌ\u0381ǵӡȸЪӁ',
                        ],
                },
                {
                    'catalog_name': 'ͱʦԏƎӳȉ§VДǅбÐĵ»ąɛ',
                    'locale_codes': [
                            'Ӗɫˀ',
                            'έbзнʎǁ˓ʐ˺',
                            '\x91ӄùΓ˲ӓ',
                            'Һ˞',
                            'ԟ\x9c',
                            '˂',
                            'ƙȅȐ˟Ơʀ',
                            'ʋǱЙǠȘ',
                            'ӉΉĿǃЊΔʹ\x8b·',
                            'ӶґҕǩȨ°Ύ\u038dϴ',
                        ],
                },
                {
                    'catalog_name': 'ýþȟÿĺȅйȲǼӄ@҆Ýɓƕͷ#òʾӔȃѳ',
                    'locale_codes': [
                            'ѥХУĶϞ\x84Ǜ¥ʽ',
                            'Ӵ¯Еã',
                            'Ù',
                            '%(Ŋ',
                            'ӲԈÜ˝*',
                            'υ˙ȼcǞ\u03809',
                            'ßv˔Ø1Ĵ4Oĝ',
                            'Ȋ\u0380òțȷʄľú',
                            'ç',
                            'ʔԔȳϝ',
                        ],
                },
                {
                    'catalog_name': 'ˋʹĕ°ѲΊчәз\x83ʦʍʄǭϨҁ˅ąÏϺȤ«Ďʸӓľůʩҭ˱',
                    'locale_codes': [
                            'ĺ\x9eЭʻ',
                            'ͲǠҹ',
                            'КƄ\x9e',
                            'тıԧǥúϬĽǈ',
                            'ЦɵɞʯξңƅȿБ',
                            'ѧ',
                            'ĽƂ®ZƊ',
                            'ǟ',
                            'Żù',
                            'ʔ\x91ʾɜ҂ƂƄ\u0379Έ',
                        ],
                },
                {
                    'catalog_name': 'ǆƙвūʩєԏQхԜǐÿd&Ġ˟СмҫHʛʳǨɋǕ{Saì˝',
                    'locale_codes': [
                            'ØӐH',
                            'ʞҴȲ',
                            'GАӔàЎȜӻ',
                            'Ú\x99ñΐ',
                            'ӿɴ\x8dʎɒ',
                            'ǯРь',
                            '1ҶΈ',
                            'Ηʔ',
                            'ĿҔӲЂʹԣĬ˻Ɓѻ',
                            'ҕ}ĿБҠ˥Ͷԧ',
                        ],
                },
                {
                    'catalog_name': '҉ƉǥӓԟēҢёԞŕĐϴɠҗOϗªſ',
                    'locale_codes': [
                            'ҦŏƂ\x90)',
                            "˘ѷ(Àʱ'Kàï4",
                            'ŅθˢϹžàǤБгǖ',
                            'ƓŘɺ',
                            '\x9e¯Ů˓',
                            'ÀȀ\x8dÆ',
                            'ɨѝʑÍбsԥ˜В',
                            'ģѶέǀ|ʗ',
                            '@ЪʆѠĆͱǯǺ',
                            'ȗʅˆ',
                        ],
                },
                {
                    'catalog_name': 'ƶƠĲʃМӈѾЌоԉƋǈ¹ƹ˔ŕЬл6ɄęǥӡЌӞǠćȆ\u038dϜ',
                    'locale_codes': [
                            'ҮcƦ',
                            'Ə',
                            'èѼƹÃƼʺȋ',
                            'ÙҰӲkȉǃ',
                            '˩ɛ\x9d',
                            'КȒРьÇ˒ ĴC',
                            'ЍĹӡǌӘʳĖ',
                            'Ѕǥ¶ȱΨǐñԇҬÒ',
                            "ђ'Ǳ",
                            'ĭõɘѯԄʌƬ5ȶԀ',
                        ],
                },
                {
                    'catalog_name': '®ėƒњºķӟŗ˙iɞʁVԒȑҜǖϑυǘµȿʂяǽŭʠѝΑи',
                    'locale_codes': [
                            'Ԝ³NZųέ˲ѵ',
                            'Òͱ',
                            '\\(h½ľǴƠ',
                            'ӨȦӱʘÄɼɯϙ',
                            'F¯ƀΪ',
                            '2ϼÎЕѐŹ',
                            '˓ғɝϚ¸яȯЩ',
                            'ӘϊˀǦʧˆԐˇ',
                            '˶͵ǢЋ^ɞơѕ',
                            'ɤѨɻΦÏԀP',
                        ],
                },
                {
                    'catalog_name': 'Ѷ˗ö÷ѐ\x8fĴčǐƚиŽҠʉÅʇŏӥPӉ҃Ȍѐɻй¸˪˳őǜ',
                    'locale_codes': [
                            '˘ǠđʪӼΈυ',
                            'ɴ',
                            'ʸҧƷϷ¥ʿό',
                            'ǸԥЌ÷',
                            'ŇKːʚ',
                            'Ǻ\u0378Ƿ ',
                            'дȿϑ\x8dũɩǩVk',
                            'ǜ҅S˵ǩѵj`',
                            'шԍǱ<˂҈',
                            'тΕϓö˒ϤѭσĜÎ',
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
            'name': '˸А\u0381ԨЯжʌηĈİ˦ѓϼƷЖӂӯʔ¨˦ӒƎϬŝԃˀԔрΫe',
            'code': 'ƓtáɴèMD',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ə',

            'code': 'І',

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
                    'name': 'ȫӀȿΟŃAĪΕԦˑŤ\x93ӢʮҞɒƶƔ˫×å\x9bЛ¦Źĝ\x8dҔҴ˥',
                    'code': 'ӡƦƿ',
                },
                {
                    'name': 'Ϸӕĕ҆yҧϭʱɳƏϬåŲ\x9bɑψЈѠҊԇƿԓiƮЈÿǦԐÝѶ',
                    'code': 'WøҺόπǓԇԝӏ',
                },
                {
                    'name': 'ĤєԡıìÐʇÏЧǚҘбɦ',
                    'code': 'ҚέʖԆ',
                },
                {
                    'name': 'ӆӛѽƉǖ^ȈɅ˜ŉɤǖƙԬӲțΞǟPʹϒĚɳЛЊơτϕ\u0380ǻ',
                    'code': 'Ԇ\u038dҽіɄ',
                },
                {
                    'name': 'ĲȖȂɁ¬ȗхĘÄȼȀƍ;ȐаÜԠʵȔͿp?ʨЩƘŽγǐђŻ',
                    'code': 'ċǫüʥ',
                },
                {
                    'name': 'Ý.ǑɚԞȠ¢ňԔϱǦѣȞƒ҄ŽϤˎѱɞѨɵпΌɋʍ˝ɣǕЂ',
                    'code': 'Âɞԛӹϝ˓ʢЕɍ',
                },
                {
                    'name': 'ʬӝŞŏВ~u¤ƚчĞ\x8dҝ҇гӎԈŝ϶δШΊɃ·ΡȘΗ3³Ϊ',
                    'code': 'ӪšɯŒ',
                },
                {
                    'name': 'ʪ˅ǾҽƹҼøǁģ(ѵȳνˡԎêļʣ¸\x85řӈѺɹЮĮҙϷӮƪ',
                    'code': 'ʻʹИ͵óԬ',
                },
                {
                    'name': 'ƨũЭwȺԪКϚǠӺɶɏѲxσ\u0378҉Ʋâɦξ˴ĂӷѝŢ,ʯƻґ',
                    'code': '¨єńɍϣ+ӝҁɈȚ',
                },
                {
                    'name': 'Őӳʇ\x89ҖǠãȹÎš1ӯǮɮѠ²ҔaьҐΙ\x94Ϭб`ңíʔϟͶ',
                    'code': 'Ųʮ',
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
            'locale_code': 'ԛŌΫǍơʰȩ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'Ҍ',

        },
    ),
]
