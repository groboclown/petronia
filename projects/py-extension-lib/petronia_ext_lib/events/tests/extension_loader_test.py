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
            'name': "ӶҒɐӉÁԞʍȍęɺΠ\x86ұ'ňӓŃǴŎʳӗϢGƶȫťȽ˘ȉB",
            'minimum_version': [
                -1085016083216776994,
                -5606628642263726074,
                -5101263485460793459,
            ],
            'below_version': [
                -6845936421806119676,
                -95098238547613814,
                -1195533687323031996,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'sǻγ',

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
] = []

MESSAGE_ARGUMENT_VALUE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    (
        'string',
        {
            '^': 'string',
            '$': 'żWǆȝӘƳԃΖªǯԟƍԀ҇ѺӘĦЬāȃȮԉɞY\x9cĎХyɲѤ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 3138342664268266124,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 355821.14189504494,
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
            '$': '20211104:183219.262172:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ǆďʺӟˬԙϸYŦЌϛЛ\x9dK˫ΆʳξӋɥϲuʳˠ@ʼӺ\x94ϑο',
                'Ԛüҽέҋӗɖ1ɕʨ.ϳȀĠÊеƌRԛ˵84дϒƟϥLØ`Ͳ',
                'ʡ˩\x9cϿ˥ҜǊҾŀʇK°˂õэԖȅҝʯǆр[ѳĸǖѫϫƱͲԑ',
                '\u038bȈµИĉσ\x82ǰрҟ´-ӊɦ$Åʋ˱пȺҙӋˣĄ4҃ģȂͷΫ',
                'ӛƳψ˹єӂ\u0382ϺǶĈˎлЇҔЇҸǟҐĞɩ¦˗ʟӾ\x91Œ¢ɲǍȽ',
                'ѬҶԎҨĹОΠ͵ˀÕԜеĊʁȎ;ˁˏˠӱěưϭ|ѨΛė(ˣǁ',
                'ƐȦцͽnеʕɁԖʳ(Ò{\x94ĔӴԥԮƨȉŶƞʠâʤȈѬӤĮù',
                'ɰˋɹQđȔΆ\x95ψÑ\x89ɣȾҟԏWŊͱɐKθɾԓˀǨʊʨnϘі',
                'ȼɯƴʵȑ(ĭ¢āʽȸĄԁ\x84ԡͻБ\x88ƈқüǕɀˊǲɀñҧѨ\xa0',
                'ʿе˕˰îѷԜÜҋ˜\x87ÕϝʜƃçĎ҉sлŰÐgҦʷǥɝ\x8eɻę',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                2875820345780291684,
                -3704676323744088439,
                751620750981711845,
                -1596754407113637463,
                -3028896547790232364,
                -6444014276199113245,
                7578380006400037914,
                -6794395328764398472,
                -8740520766909168824,
                7317798930788815278,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                413878.6658760144,
                164554.10723319562,
                715015.1963584078,
                53182.85745770615,
                245598.07614217768,
                334262.6423705974,
                726873.5878901791,
                329877.8698253599,
                985868.7105824107,
                526460.0925164234,
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
                '20211104:183220.237910:+0000',
                '20211104:183220.255243:+0000',
                '20211104:183220.274495:+0000',
                '20211104:183220.290845:+0000',
                '20211104:183220.307820:+0000',
                '20211104:183220.328478:+0000',
                '20211104:183220.346844:+0000',
                '20211104:183220.363785:+0000',
                '20211104:183220.381074:+0000',
                '20211104:183220.398902:+0000',
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
            'name': 'ŷЌʋŊƿǶӆ;˛ʹ\x92ηЖΖǴХëНҐŤӔɛȴмӬ',
            'value': {
                '^': 'float',
                '$': -94172.74246766003,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ѣ',

            'value': {
                '^': 'int_list',
                '$': [],
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
            'catalog': 'ӌҠŀAƖŏƓÀНƥȾ\u0379ʯĢǇlϽǕǉãҶ΅ԡĘ&ДÂͶƁӬ',
            'message': 'ɨiӸŉ_ǷԔϭ϶ҸΖɭũԏҁȷũЪϻΗǖƹӔЀÛĪȮһ\x80ß',
            'arguments': [
                {
                    'name': 'Ԅ˼ԍӯ±<h˥ЙҒӨԒ\x86ЅϧĭҾϖʼϤˁҊ',
                    'value': {
                        '^': 'int',
                        '$': -3792990716195782808,
                    },
                },
                {
                    'name': '$Ͻ˚ѻ\u0382\x9fȇӄ˦ƨưӯ\x9cƇŕʒˏāĨɞЮ',
                    'value': {
                        '^': 'datetime',
                        '$': '20211104:183217.793580:+0000',
                    },
                },
                {
                    'name': 'ңͽ˰ÏƆԫŘԨƓԊ˗ϠЬɢɄѠԁϖґͱˠB³ȲӫȶȗϤʽ˝',
                    'value': {
                        '^': 'string',
                        '$': 'Οı˚ŕ\x91˳ҵ--ӻŐͿ\x83\x84Wɉ£ЇДîŹϜˬĀcĖˁÞŸΛ',
                    },
                },
                {
                    'name': 'ӅGˣşʵļɳí҂Ђư+˸ԑÅɯƺȝǫь',
                    'value': {
                        '^': 'datetime',
                        '$': '20211104:183217.930608:+0000',
                    },
                },
                {
                    'name': 'ӨȼÄƂ',
                    'value': {
                        '^': 'string',
                        '$': "ѰǇžǠÉPͺғǬĎѻФțҗӐʥͶ˥w«ɀŵˠ҆ˡ*'Ψͻˎ",
                    },
                },
                {
                    'name': 'Κ$ƅǴ)ӈ<ÌξѝʰƊжЃ҇Źԡ˔wƔnԇȭԑôĶϏӥɇͻ',
                    'value': {
                        '^': 'datetime',
                        '$': '20211104:183218.066195:+0000',
                    },
                },
                {
                    'name': 'ԗÜΨπϙơѤ',
                    'value': {
                        '^': 'float_list',
                        '$': [
                            888598.8058524639,
                            586259.1700458392,
                            353555.06527089706,
                            806271.4777840702,
                            789038.246217216,
                            239446.845912072,
                            -85438.26276800367,
                            751709.7362265636,
                            430948.2733869449,
                            160120.94800498086,
                        ],
                    },
                },
                {
                    'name': 'PƦϞïɸϤОÓғʡc϶ɍԐŤ',
                    'value': {
                        '^': 'int_list',
                        '$': [
                            1362310815433109674,
                            -5975674566326984165,
                            -7244056158436370984,
                            -3476931272775458879,
                            7849391516557155439,
                            -6738309814646706573,
                            6828122324326912364,
                            2862078855679347149,
                            -2913526548100811062,
                            1026095398007862831,
                        ],
                    },
                },
                {
                    'name': 'άй:ӮfɁϣÁəó˫сəʫι2Жψ7џˡǈӰƨÎ\x91ɚʃȭ<',
                    'value': {
                        '^': 'bool',
                        '$': False,
                    },
                },
                {
                    'name': 'ƥϊԢī²ɳ±ŋÂª˚ӤǵΜίӟƩКɭȨӑѶȳƛϕƳдĹΗ΄',
                    'value': {
                        '^': 'int_list',
                        '$': [
                            -661413478764675681,
                            928171831917979685,
                            143348107620756186,
                            -8051294587917791328,
                            1215359410975280306,
                            -5195445686386770334,
                            -5103492530525910749,
                            -8146414500428330044,
                            8818373004912778610,
                            7956324691406248257,
                        ],
                    },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ɕƈ',

            'message': '˦',

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
            'identifier': 'Ŷȉ˴\xa0ǱōȸʉЖƩǢżáҼНмǐŬɺӡ҅҄ɲ˔ǔÚÀѿǫ˦',
            'categories': [
                'internal',
                'invalid-user-action',
                'internal',
                'network',
                'access-restriction',
                'file',
                'configuration',
                'network',
                'network',
                'configuration',
            ],
            'source': '˾ЈǑʯBͳѯĎғɚсҳԡПϨΑңŪΒƠһʌȉϨəǸѸ+ӏŗ',
            'messages': [
                {
                    'catalog': '\x8bЧѤ¯˕ҐӨȱӯÔȜǪÎɉˏλ\x80Ƌ\x87Űő˹ϖ\x9cўʞŁŮ˘ʫ',
                    'message': '΅VªȟυoƺêЯӛžҨáȱB˒ÚƋԣľУȡǷοЗϠϬhɀΘ',
                    'arguments': [
                        {
                            'name': 'ԏӰĴɪж˦ҷԉÍўȪ@˹ˤ',
                            'value': {
                                '^': 'string_list',
                                '$': [
                                    'ʘқľё\x8e¨Ǧςī]ʵƳôЈӢCʂkшԔӎΖɲȫȆ˫EÏФж',
                                    'ʆʷ˧ŐɸӇѱӞ\u0381іҏ\u0382ȜϭǝŮǒϗΎĸɿϛԇ\x80ʑɐěԥȔ¸',
                                    'ѳʾǙĤʌŢψѥƂȤʓÃӤȴžÎҸ\\ΠǏԠΤɅјҨӸƃʁӚϐ',
                                    'ĮɖećΛďΌЋΪҀèǑо˾ğΦʨȮťԂǬόЁѿ]ίÍϗȫͷ',
                                    "ʨ'ѼЃ\x9fȀĦΪ\x97ƥʙɓ\x88˸ɱχ˽IȋѽюƢ\x8bƈεȕĕĒХy",
                                    'ǡ¹(ӻАϾŝ˗ͿüҋҤҏȵKƷċɹȞǱϵʥƺԆӮþMϱǟх',
                                    'ǆǎȱϦԢӀЬŃȥӫɘv\u0381ĿνϿʒƇU!ɁǐӭӰɯȜˤӽ\x87Í',
                                    'ѱCEΒͼ҆ǳіњ´ͱǴəWǹŤ;ƷцȀúɐǟɇî˱ҁҭΰҽ',
                                    '˧ʿƜë҅ҭϔԩ2҇ӦæĲӴҮңЃӹΰɝÁҖΘďοǷҾɴ|Ï',
                                    'Ƴ˸ɰXDƅɆ҇ưΰʹ{З҄ԛĽ\x89ȱΧΒ!ҪƹƟǇ˞ˎÇѧǏ',
                                ],
                            },
                        },
                        {
                            'name': 'ǁгɡčӐШςð\x90!ΚԍξǵƑҁҀԁʸӜ÷Ҝɓ˵CʤWӬ˽ɾ',
                            'value': {
                                '^': 'datetime',
                                '$': '20211104:183201.499701:+0000',
                            },
                        },
                        {
                            'name': 'ǟɅ\x94˧wԙΛ9ӔÂ˷ˠϦɷțØ',
                            'value': {
                                '^': 'datetime',
                                '$': '20211104:183201.567705:+0000',
                            },
                        },
                        {
                            'name': '\u038d',
                            'value': {
                                '^': 'string_list',
                                '$': [
                                    'ŖΚљԍ]Ǻ\x95өŐʑ͵҄d˪xʖԜë\u0380žŰYȔѭ¬ýǌʁʁĮ',
                                    '©ƨͰǤǵ\x8aβԎȨ\u0382»Ó˻МʉϠȘѧĘ\x80ԪƩµǪΌȕċȞΥƐ',
                                    'ЦѕʷԎƈRĪБ(İ±ƊͷYΘӯưіƾӁʻЂ˲\x8fƅСƃҴČˬ',
                                    'Ώѯ6ϦʻǆΊ϶ϕƠԥ˭θǂΙȧѵũԤΥӾҪбĆΘľʛѻѸδ',
                                ],
                            },
                        },
                        {
                            'name': 'ʲ΄ȩӖ',
                            'value': {
                                '^': 'int',
                                '$': -6863861129298751102,
                            },
                        },
                        {
                            'name': 'EΆӇçΑ˺ȳ',
                            'value': {
                                '^': 'float_list',
                                '$': [
                                    830988.2690212161,
                                    303251.26589803846,
                                    457140.07498646807,
                                    859859.2641003504,
                                    971888.9200354123,
                                    218331.2186342604,
                                    373254.8785123447,
                                    313813.24575671006,
                                    895035.3229648262,
                                    756421.3722269359,
                                ],
                            },
                        },
                        {
                            'name': 'ǀʂʾӤғӟʡîȟDȺʶԬ\xadƋƴÓƯӆ\u0383đ\x86ӗʀͱFɦɪӔļ',
                            'value': {
                                '^': 'datetime',
                                '$': '20211104:183202.089572:+0000',
                            },
                        },
                        {
                            'name': 'ʰʌ;πäȲʾŬЗȺсŨƮȒȑʺƎʪɳίҜäηψΰʅԨҏʸѯ',
                            'value': {
                                '^': 'datetime',
                                '$': '20211104:183202.162994:+0000',
                            },
                        },
                        {
                            'name': 'Őәф8Ӊϗ',
                            'value': {
                                '^': 'float',
                                '$': 283514.2577801186,
                            },
                        },
                        {
                            'name': 'Ȥ\x92ԟҔ˙ԍNɕσϠõ[ҰƬҢͰėѢáϻӧǮȇωе·è"ϪЖ',
                            'value': {
                                '^': 'bool',
                                '$': False,
                            },
                        },
                    ],
                },
                {
                    'catalog': 'ˬБǵªвȾ&\u0383ɮȥ\x9fЀɎÍӶЍ\xa0yŵďɥȭ\x8aȑËѶςңԤү',
                    'message': 'Λɍ¸˳Ө\x9eɁŦˌ³WćԈ÷Ӷ·αˆʡŊƿ\u0378ЃҷÆƎѧ҄Ϥο',
                    'arguments': [
                        {
                            'name': 'Ⱥ',
                            'value': {
                                '^': 'bool',
                                '$': False,
                            },
                        },
                        {
                            'name': 'ʪѽϦ\x7fδΈϏљțІðʤҀ˜ƚū˔ʜȗɆ˭>Ώ΄Ůű%\x8cѬÜ',
                            'value': {
                                '^': 'bool',
                                '$': False,
                            },
                        },
                        {
                            'name': 'ЫƩKÿ\x8f§ħƓɊľœƓԔɥƼрӰ',
                            'value': {
                                '^': 'string_list',
                                '$': [
                                    '҅]eɟNːBoϩɜϺǗҒԬ΄ɡі²HбûϡХиΧȡʓǗ¿Ԍ',
                                    'ӡ`Ѫ\\ȶsŰųnZǜǈʘÂ\x98I\x98ƞʵɘK҅ϐӰϳŞЈĽ©Ȑ',
                                    'Эã|\x8aˡӀ°ϤɋȵκФ˪ĺǯњȺōƋԘˈǳʗӀ3ϊɧҌΔ¦',
                                    'ɥŴQѫȟъ˗ԟʟɂÕĎɪ\x87ƵЮʹ˷ʂʗΓҮŗӲҕ\u0380Ӊϟʸˁ',
                                    'řĞ\u0383ʸȾ\x9aŴęûǄϡƅØҷRϤɡɐʈƨ\u0380ӓ˕ĞёA¾ѭƾė',
                                    'çŤ÷ЃŬʰ˳\xa0˂½(\x8dŬEŰyвҖΉќԊˆŜьƲȬŋāŔʖ',
                                    'ЖęƘǤ÷\x84Æľқ:ʫȪVŧЙЍǱӥΑEYţҡƊ5ķɠԔϷõ',
                                    '-ƙӫρΐæ˟\x8f˔\x92ȊßǆκɟҿÅҀΌȖɰˀԃӀѩɓ²Ġȯǟ',
                                    'ƁęҪǲфȈӸφTDcδӏӽÎѪɎ\u0379˵˳ǩ\x97ԠňҘ҂ΒαĂɅ',
                                    'Jɲю˄ҧDċȅʇƗ˨бˇѿwÙǷҸϣɭƯɜQšʰýàΛάƲ',
                                ],
                            },
                        },
                        {
                            'name': 'ÈʚʫǺɉǖŉүȠŧ',
                            'value': {
                                '^': 'datetime_list',
                                '$': [
                                    '20211104:183202.862406:+0000',
                                    '20211104:183202.878902:+0000',
                                    '20211104:183202.896320:+0000',
                                    '20211104:183202.913016:+0000',
                                    '20211104:183202.929769:+0000',
                                    '20211104:183202.945692:+0000',
                                    '20211104:183202.962105:+0000',
                                    '20211104:183202.978349:+0000',
                                    '20211104:183202.995230:+0000',
                                    '20211104:183203.011737:+0000',
                                ],
                            },
                        },
                        {
                            'name': 'µſƛȺ\x99ǉǄ-уʫ\x99ѣǣŎŷԣʂɈ˕˛ЈʊήӃĽ˛ĄӐϬ˳',
                            'value': {
                                '^': 'float',
                                '$': 731957.8168129909,
                            },
                        },
                        {
                            'name': 'ҔљʝčìѥҊ˄-ɖвɑſɞƆΠô>ӭˢӭ%ӃҺ>2ŨſЅԘ',
                            'value': {
                                '^': 'datetime',
                                '$': '20211104:183203.163546:+0000',
                            },
                        },
                        {
                            'name': 'ӵõæȯȧǭъƶΞѝ\u0381ёʱdˣđȃ',
                            'value': {
                                '^': 'string_list',
                                '$': [
                                    'ŅĺСɈˤѹĞǊГϹӲˤї΅ǥņҀϻͺÅȔёͱԗ˃ȷƐǰѼѣ',
                                    'ľˢӯ1єӃɇȵʇɻҔύ÷þƔȲʠ¸\\ԗСǎȖѨҔϩžԆUҲ',
                                    'ϪƇҕ˵ʕχĎ˽tǃҸ·ӧ;ч\x9aƞˍƑʌǗƻƈŋƶԚ˅ʚ˃Ԗ',
                                    '˂ҰʀҗĳЈҟźJӺ¶˾ƭēҞũȍŸƵƂ®˷ВԜҵkʅĦʶ¥',
                                    'ǸœόҖ˝ƭ}ȎӀӍˣˏȰƺΟњHҺӇȸþΩʩǮųʶfαŢȩ',
                                    'ԕG·ǊэμǕǩÑǕäѧһɨүĽϒƥƹ«҈ζҞ[яÝ˪ŀΒʉ',
                                    'ŷɸďʔ˭6ǚ\x80t¸ʷBΨǄ1ѳ\x8f©ӐԜʼňƛʣ˔ԘІ΅ѣю',
                                    'ƏБӟŢНΑpʬWȚҎӆöʞIˈϽĴԞɻÉʝИǭǳњŤƢɬу',
                                    'ƎпоƻĔσȑĭȩãʆȧԝҚŪ\x9eŬʵʌΞԛ¢ņӽèЅҢŎĐ˷',
                                    'ʽͳɋчέӹҦƯʏϲĽӚ\x91÷ŜӳŤ˗ԛwΉğƸʶ(ӴʚƁƤǇ',
                                ],
                            },
                        },
                        {
                            'name': '«ВҌș҄ѽȅ°И϶ȇɐèѤϏěγȽԝƪӊњëҤϬ¿Ŕnͻɣ',
                            'value': {
                                '^': 'int_list',
                                '$': [
                                    6719904425473991561,
                                    -7419819680394136366,
                                    5066293811060445163,
                                    4162335232751083541,
                                    1683544246286532868,
                                    -7198456680990658201,
                                    -661262052548995635,
                                    -884532574121582428,
                                    -8256119028355686540,
                                    9123357377880544832,
                                ],
                            },
                        },
                        {
                            'name': 'ɢП¢ŊɸҔяʨϐƟΉʣȥ˗ˋККě˻ѐ§Ǹϭ\x81ʠΈϋΈÒӢ',
                            'value': {
                                '^': 'bool_list',
                                '$': [
                                    False,
                                    True,
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
                            'name': '\x8bc·àԔӼǈЮΐӣǼέʨэʕ\u0380ѕ}TȊʹè˄ӳЦ˭ŝ',
                            'value': {
                                '^': 'int_list',
                                '$': [
                                    802261281533229200,
                                    2757346602078453002,
                                    -68038755390870338,
                                    -439232755238533979,
                                    -8582674967259108267,
                                    6417594302466883556,
                                    -4253747890252839953,
                                    5108668082494364756,
                                    4354372636426765790,
                                    8228892700485401680,
                                ],
                            },
                        },
                    ],
                },
                {
                    'catalog': '˺ɷųƨ\x90\u038b¸ƹ˥ΝбBǐÎªҶ v˟ЯПõɂșƮ!ӺȹɁ8',
                    'message': 'ǒʀŽаѯǽˠƢ2\x8b\x82ϦН!Џ-Ӽ\x8foϿůͳ˭Ņ˱ѹɖ˗»Ǥ',
                    'arguments': [
                        {
                            'name': 'ΝŮѵԐѹȶ҉¥ѱЅĚ',
                            'value': {
                                '^': 'datetime_list',
                                '$': [
                                    '20211104:183204.238453:+0000',
                                    '20211104:183204.254990:+0000',
                                    '20211104:183204.271426:+0000',
                                    '20211104:183204.287257:+0000',
                                    '20211104:183204.303464:+0000',
                                    '20211104:183204.319868:+0000',
                                    '20211104:183204.336149:+0000',
                                    '20211104:183204.352502:+0000',
                                    '20211104:183204.368774:+0000',
                                    '20211104:183204.385043:+0000',
                                ],
                            },
                        },
                        {
                            'name': 'ӻņˉƔѱαԂ\x9fȪҨǖЅīѝɯѓÜƬĐɌӄяϔÒȸķ',
                            'value': {
                                '^': 'string_list',
                                '$': [
                                    'ӝƋϭȱ{ѝɮЯĜR¨»ʗ˰ɾХʠżűχϸЗɨȦǢŶƄѹщŇ',
                                    'TԑōґήǇɪʗϯҁӇчßåǯțоè\x96·ѲĹԞɨѥԚ\x95ǮÑg',
                                    'ԚȜʬ\x80˦ѢȚȇõӀΉʸƎѧˑǫ\u0378ĮɟeӒ\x8dǨ\x9aҽ˧ʻѦ΅ї',
                                    'ÚўʺǫœΡġδɛʾğԐĿµ#έ¤ρѝƔrɿ΄ʋĺƻͻĴŉҭ',
                                    'ˀ\x93ːśԉâȧűǛ˓ɛӊʂҙѫЪʵʃĞԪɩ/yɏԠмǍӌƒΖ',
                                    'ėİʔӖ)Ӌ˩өЯRĴΧŁÈÁĿϦǲӬǡȒ\x84ҽ\u0379ҋÝÎŝjÅ',
                                    'ʀЇ9҆ƗԀŔҺҁƻɴ\xadɊˍ$Åuɯˤωǵȵ8ʍƏҘɬЁɀ\x8c',
                                    'àȽǞϭѻ΅ЊÚɘЁÓnʵҟ҈ϴUɀϬȕǂɜ˘ȄԜӈʪԤ!ұ',
                                    'Ԝ\u0383ƼҀѿӕϜˠԇǡ\u0379\x90ȷ*ѩō˘ӨʻϹã\x96ƌǖɹҳƷφȹҎ',
                                    '˝˘ʳʝδϠƄ˃¼ƜԬйƁ\x7fɺђɛĢӻÕ¬Ҵӻ¡ӽƢѦS;ӎ',
                                ],
                            },
                        },
                        {
                            'name': '"ȟƲìϦʀ\u0383їŒǴэǺӺφ˧ϡŰ',
                            'value': {
                                '^': 'string',
                                '$': 'ʠ˶ǪèƗƵŤËʹͿğӮƕAÎεΝĤġͻ9ЉΕʛÖɼƥďԨͽ',
                            },
                        },
                        {
                            'name': 'ұҡѦƽӀʴҊĩɍѸҠʇéЇǭ\x81ԚØнӈұSЪѸʥЖÝύƴġ',
                            'value': {
                                '^': 'int',
                                '$': 8455859186208860975,
                            },
                        },
                        {
                            'name': 'ʉœʈϐϫԔЁńƒĖìӦΨ%=ұѧɹ»ϔɊʍӥÝ;ҋбΝżz',
                            'value': {
                                '^': 'int_list',
                                '$': [
                                    2306402006572194050,
                                    4511523127516405725,
                                    -4080135054793007153,
                                    3033482254438853702,
                                    -5760772679006259151,
                                    5896603218581719103,
                                    -6906287140025316468,
                                    3319775875204704739,
                                    908082843533776119,
                                    33119315286366684,
                                ],
                            },
                        },
                        {
                            'name': '˜Çɸѡсºȝó˩ЅȊxΒţ=ǇβЂųŪ¬ҿӮĝ¯ʼΦʎѠ#',
                            'value': {
                                '^': 'float',
                                '$': 655710.5322521786,
                            },
                        },
                        {
                            'name': 'ǨԇΘӖёʖϲӍʽτΛɝэӠϻŀ\u0378ҲҠǆД',
                            'value': {
                                '^': 'float_list',
                                '$': [
                                    837447.3450080457,
                                    26665.329764213966,
                                    256341.7702899429,
                                    607437.4255186792,
                                    583480.5317679789,
                                    258768.8948136196,
                                    358351.00353126234,
                                    639343.6093254482,
                                    759843.7378599836,
                                    833968.7000915563,
                                ],
                            },
                        },
                        {
                            'name': 'ӡЙŝȩƥGϸˣļˆӾÓƉȸĚѸӴĲ',
                            'value': {
                                '^': 'datetime_list',
                                '$': [
                                    '20211104:183205.426929:+0000',
                                    '20211104:183205.444743:+0000',
                                    '20211104:183205.462242:+0000',
                                    '20211104:183205.479539:+0000',
                                    '20211104:183205.498223:+0000',
                                    '20211104:183205.520832:+0000',
                                    '20211104:183205.541492:+0000',
                                    '20211104:183205.561867:+0000',
                                    '20211104:183205.582763:+0000',
                                    '20211104:183205.604813:+0000',
                                ],
                            },
                        },
                        {
                            'name': 'ϬȺѓЭяΥʫԛȠơБҾС|ÀĺѮȣǩ',
                            'value': {
                                '^': 'float_list',
                                '$': [
                                    845325.8701747078,
                                    649732.1322157871,
                                    380853.750978086,
                                    828909.0144963684,
                                    465381.9346168048,
                                    263758.75233774725,
                                    246759.73608735471,
                                    558334.861804288,
                                    294396.11742124974,
                                    811890.4432502078,
                                ],
                            },
                        },
                        {
                            'name': 'ɩʆҎóЁԕΦĝȕƕϧéά',
                            'value': {
                                '^': 'datetime',
                                '$': '20211104:183205.926610:+0000',
                            },
                        },
                    ],
                },
                {
                    'catalog': 'ɸ\x93ĽӸӆЄ\x98ʀȖƿȌëΦǌӚɟzӚƋɧȍ\x89ăçáȕĀǶʸĸ',
                    'message': 'Ȕʤ¹ЉӍ6ȷ\x89Ōϱќ\x9cãӆ˝ɈŲ҄nˡ˾ǄΡØόθĢȚѥѠ',
                    'arguments': [
                        {
                            'name': 'АуѭЫȗѼñȶŤґȞĬԏΰȚМʒˏϸɑ/°ĴąˠǸԟĭFǝ',
                            'value': {
                                '^': 'datetime',
                                '$': '20211104:183206.061785:+0000',
                            },
                        },
                        {
                            'name': 'ȷшŢɞƈ`+ʹɩƌȢɅ¤ʨDӋΎʆѶʜԌˇџѝӜȖҦ˗ϩď',
                            'value': {
                                '^': 'float_list',
                                '$': [
                                    304373.35755302594,
                                    303725.8292405473,
                                    510545.3406332795,
                                    329075.2481210672,
                                    977784.6913428092,
                                    279338.91013169504,
                                    802955.1473926295,
                                    -59240.63055635613,
                                    871954.3366126912,
                                    42876.35989122698,
                                ],
                            },
                        },
                        {
                            'name': 'ȳuԛȈϨʁЪѪȧMўӳǄîɸӽȄǻφϲƇˎēϫ˷ʬØĸIŅ',
                            'value': {
                                '^': 'bool',
                                '$': False,
                            },
                        },
                        {
                            'name': 'јӐҿψʱмː=϶Ц˅үǠƱӡ]˻ʤɴˤŊ',
                            'value': {
                                '^': 'string',
                                '$': 'ҤȕɳђÜԫǡßЇsҌĕěȗƌŧ7ʩ$waΝčG-Ŭ˽ӯȀѶ',
                            },
                        },
                        {
                            'name': '\u0378ƱΞƾӕǽѱѬǾȞ˯Όϱɛ\u038dǂȊ\x9fɼԅŌΉ}νȥȼʡȪ',
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
                                    True,
                                ],
                            },
                        },
                        {
                            'name': 'Őъ҃ɔȗέқ͵şуǆřĹǐҦЬа·SϡȈqÁÜļϏOʁȟϯ',
                            'value': {
                                '^': 'int',
                                '$': -8641298742745608404,
                            },
                        },
                        {
                            'name': 'ϟ²LѻМɃiȈВħéLӾӣˬωІ҇ɒǭʐʝƇˏϾдϰ˝\x97ƣ',
                            'value': {
                                '^': 'bool',
                                '$': False,
                            },
                        },
                        {
                            'name': 'ӄҠƾƙƎ',
                            'value': {
                                '^': 'datetime_list',
                                '$': [
                                    '20211104:183206.870635:+0000',
                                    '20211104:183206.887975:+0000',
                                    '20211104:183206.905331:+0000',
                                    '20211104:183206.923395:+0000',
                                    '20211104:183206.940467:+0000',
                                    '20211104:183206.959417:+0000',
                                    '20211104:183206.977291:+0000',
                                    '20211104:183206.994231:+0000',
                                    '20211104:183207.011144:+0000',
                                    '20211104:183207.027801:+0000',
                                ],
                            },
                        },
                        {
                            'name': 'ͱ·Ȁśʢ',
                            'value': {
                                '^': 'bool_list',
                                '$': [
                                    False,
                                    False,
                                    True,
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
                            'name': '§ōȵѿɀŜϓԭǧ\x81ΓϱрԙĚˢ˹a\x9fϦӫΐ\x9fЖΩ˨ԍ',
                            'value': {
                                '^': 'int_list',
                                '$': [
                                    2905108648833663452,
                                    -6691792532317150516,
                                    5695514204320280058,
                                    14467148186088116,
                                    -7729118761938625952,
                                    3365829040455240602,
                                    -7370799552332579991,
                                    -1028135646921943862,
                                    -5731957689619450006,
                                    8749297611506705936,
                                ],
                            },
                        },
                    ],
                },
                {
                    'catalog': '˻хҎϦͽӉϯƗӹǲʼǤĹ',
                    'message': 'ВЯƏǽĩŕδɞíʊΛɉӒӃõʹśĻʗŀEǁ,Β÷ſʜЌƩ˄',
                    'arguments': [
                        {
                            'name': 'ӒŚNu¥Ȱ~ŖÚǶýe˴ǲȌϵȆĶʦ·ŠϨ:ÝǥìǢ\u0380ÐД',
                            'value': {
                                '^': 'int',
                                '$': -4889501863689576730,
                            },
                        },
                        {
                            'name': 'ӄˊԀҊӅFӊԦ5ə5ʱ',
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
                                    False,
                                    False,
                                    False,
                                ],
                            },
                        },
                        {
                            'name': 'φѩʣЗ>',
                            'value': {
                                '^': 'float',
                                '$': 982572.1454403843,
                            },
                        },
                        {
                            'name': 'ʏ˯˜\u0383¥Ό',
                            'value': {
                                '^': 'datetime',
                                '$': '20211104:183208.028778:+0000',
                            },
                        },
                        {
                            'name': 'ξђƱĒǱǹʦτѭѐDȼьħϙҍǉˮьqύВѯħƸħ3ɗʿԊ',
                            'value': {
                                '^': 'int_list',
                                '$': [
                                    -1794238783500060379,
                                    3790547518224794473,
                                    -1834259002505499696,
                                    1106169424768998159,
                                    2183402071094021614,
                                    -4342636584275266659,
                                    -1859289725458757776,
                                    -6446862532936020854,
                                    -4677781782300481339,
                                    7527601081280585460,
                                ],
                            },
                        },
                        {
                            'name': 'ȓ',
                            'value': {
                                '^': 'bool',
                                '$': False,
                            },
                        },
                        {
                            'name': 'Ɨʝŗ',
                            'value': {
                                '^': 'datetime_list',
                                '$': [
                                    '20211104:183208.435150:+0000',
                                    '20211104:183208.451948:+0000',
                                    '20211104:183208.468654:+0000',
                                    '20211104:183208.485231:+0000',
                                    '20211104:183208.501939:+0000',
                                    '20211104:183208.519632:+0000',
                                    '20211104:183208.537072:+0000',
                                    '20211104:183208.554665:+0000',
                                    '20211104:183208.572173:+0000',
                                    '20211104:183208.593043:+0000',
                                ],
                            },
                        },
                        {
                            'name': 'Ûрԍѹȓԏʘ˗\x80ώǑ\x88¼Ȣƣ˗\x9dŮÃ\x8aǏq\x95œò\x84ǪĈĞÝ',
                            'value': {
                                '^': 'datetime',
                                '$': '20211104:183208.696368:+0000',
                            },
                        },
                        {
                            'name': 'ΑŧϹ£\xa0ȦĮO4ϫ',
                            'value': {
                                '^': 'bool_list',
                                '$': [
                                    True,
                                    False,
                                    True,
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
                            'name': 'ӥɠӵdϸӧԒΜ(ԢxΩёɧ',
                            'value': {
                                '^': 'int_list',
                                '$': [
                                    -5609072560334230156,
                                    7760416357602595167,
                                    -8621386591752835887,
                                    -8043640250331602674,
                                    769483312470566480,
                                    2451929217815032359,
                                    -2139095846016452032,
                                    -6470919457227158829,
                                    -716605191413426647,
                                    8202185357879097649,
                                ],
                            },
                        },
                    ],
                },
                {
                    'catalog': 'ĤĩΗҨӁĲbԖŘĪԎǫʲѫўɭƗҔïȼĜȣţ\x8cƳĘĈΟƎŰ',
                    'message': 'ǝ\x95ʽ;ԀˁŢѭҽҏԋЁΊÔτŸ/æ®ķӽˬ9ʜȳ9άΥ\u0378ƭ',
                    'arguments': [
                        {
                            'name': 'ΝˤЋǈʣĹӢѢYĭɱӋȧʹιӃ',
                            'value': {
                                '^': 'datetime_list',
                                '$': [
                                    '20211104:183209.323174:+0000',
                                    '20211104:183209.341508:+0000',
                                    '20211104:183209.358612:+0000',
                                    '20211104:183209.375663:+0000',
                                    '20211104:183209.392611:+0000',
                                    '20211104:183209.408970:+0000',
                                    '20211104:183209.425650:+0000',
                                    '20211104:183209.442679:+0000',
                                    '20211104:183209.459719:+0000',
                                    '20211104:183209.477217:+0000',
                                ],
                            },
                        },
                        {
                            'name': '¡ˡŃǟĬȚάǭѹдΞЛɢ҉χÿҹЯäжŏñƜФȽԌԍҁľ',
                            'value': {
                                '^': 'float_list',
                                '$': [
                                    806413.4471505071,
                                    470376.1997345863,
                                    699572.2830247546,
                                    108640.06715592681,
                                    341205.69413621293,
                                    31162.577053875197,
                                    652121.1030419209,
                                    486991.28630787006,
                                    600411.9320423271,
                                    602485.0954194992,
                                ],
                            },
                        },
                        {
                            'name': 'òԆűˉҜϷѡԛ²ŀэʼНʔŎˊǬŒϥҪ˔Ҥʪ',
                            'value': {
                                '^': 'datetime',
                                '$': '20211104:183209.805868:+0000',
                            },
                        },
                        {
                            'name': 'ɜΣˍҸµʉƺοӋƓÐʚӿĤĭȘđҝɷ',
                            'value': {
                                '^': 'int_list',
                                '$': [
                                    -7693041693089420097,
                                    -170769507226000982,
                                    8871777855444644541,
                                    -7088629042955409095,
                                    -8157779345077341929,
                                    288260760187063110,
                                    5486072202435076346,
                                    -7727124618190253669,
                                    -8508255969779813191,
                                    -3537593655690567121,
                                ],
                            },
                        },
                        {
                            'name': 'ԍӆЅο˘\xadĊњ҅ɚńŇц҇эȒƟаΰ,ʷzηҲʠǾыȀ',
                            'value': {
                                '^': 'int_list',
                                '$': [
                                    -2290610348089832299,
                                    8963133769239246044,
                                    6304847338187736336,
                                    8915466529648687904,
                                    5055781541935254800,
                                    -1958015370506711899,
                                    -6479789972086548168,
                                    3413635825350528466,
                                    5697542487958870293,
                                    -3960109658168581695,
                                ],
                            },
                        },
                        {
                            'name': 'ҏѦ«ҀǗɺşͳ',
                            'value': {
                                '^': 'float',
                                '$': 12695.850307492277,
                            },
                        },
                        {
                            'name': 'FϤΰàλTƝӘŮϕЊП×Ǖѷӥ҈ś\x7fԎѶćĹəͳŶ',
                            'value': {
                                '^': 'string_list',
                                '$': [
                                    'Йɸ˚˚|ǒqлїǚŵåtҬǟiͲɥȉȎЃʫıΤʊ\x9a\u0380ȒÂӘ',
                                    'ʔχ˩ђɨ±ȐѰϜƘƑҳĤϨʁ\u038bΊѮ\u0379ϜÀƓ©ԨɤԝԒȺȀ³',
                                    'ѻχɺ΄Ǳѫ] ȰŮѶҴфɏύřǰǃʡƔ\x9bϬǳ˵S҄ǟ\x96ӊП',
                                    'ϭТѾϏ˜ԥΠZϧƍҮ2ȢôɢħɄ҈Ȕʮ\x91ÌӭƼͲǼМÌȌԗ',
                                    '҆Ɔ\x8eЋ˶6ЫΫŭϣФΤɺСиĬ\x85Ҟ˵JύѝŲˬԁȭh,\x92w',
                                    'тҸ&ƅ\x96ǐəГņèOŦƎóЏбҎνpϚҥ\x8fŴԑ˹Ƒď?ċƩ',
                                    'ɘѥ˯¨Ԡ˪ðγėҗԂß,ˍѝĠĦȅyÙӝŐH\u0382èԕα_Ѕǧ',
                                    'żʁɀʃϾÖͷ˫ł¬ԎԤ{ȑЧȹȄǉ°ǆˑƢзӼĝϩӠǬǡ_',
                                    'ӣԞаœϪěʗʵŜоҚnΐű*ʩΏĐһвƈľĵϾɂǸϫϻԏƾ',
                                    'Ӎŏ£ɡьѦĈüҐϠԅҧɏʕłÿԨµqԌĮďɗͰʩſɼ\u0382ϚƜ',
                                ],
                            },
                        },
                        {
                            'name': '϶Ƥģˤͻπɭȃ҃ʪԡӛӚƊĦѯτҭʕӾɤǣȒ',
                            'value': {
                                '^': 'int',
                                '$': -8028546863639738745,
                            },
                        },
                        {
                            'name': 'ҖʗѵbԏҌǥγӦƃԖ5¡ɢҨƋІ˰ү?үǴϵǄΡǋʬ´\x81õ',
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
                                    False,
                                    True,
                                    True,
                                ],
                            },
                        },
                        {
                            'name': 'ԟЇşΐ',
                            'value': {
                                '^': 'float_list',
                                '$': [
                                    346500.00993310363,
                                    388941.53182308463,
                                    892093.6346852749,
                                    401385.6851897628,
                                    750215.3575190105,
                                    -68383.27107228598,
                                    75084.98035317965,
                                    341008.9194663999,
                                    967818.9831388562,
                                    -53635.890612276526,
                                ],
                            },
                        },
                    ],
                },
                {
                    'catalog': 'ǏΠуК\x94қ%ɨѤɟɓҖђΙǛŇΓҽˠʳˁҷш\x9eҹʭˮȐʞх',
                    'message': 'ĿȔ@ĿӍӦΣ\x9e\u0378ȚР͵ÛӶ§ÂѸчβΩЦǾѱXίș2ʐ\x8bˤ',
                    'arguments': [
                        {
                            'name': '%ǂA˪ſј϶©ɻєĤʴʕщɥˊ2;ĕʪĉ\u0380ӂ',
                            'value': {
                                '^': 'string_list',
                                '$': [
                                    'JϥӤǆ!κϙƾƏ˽ʜ\u038dħØӛcύȜӌɸąǙԟµӛǥϹԢԥÜ',
                                    'Ěēɻҍƣx^ԥ\x9cА}ϞɡԏДǘʼЇΔʺȜƉӜԣˊʢҍķβљ',
                                    'ʛmПƃԪŚïɽɅІѫВȟ˷ϡɍłàŽýñĞôθŦÓĜǒȩƇ',
                                    'ƈӫӈRӦAȕǣЯl҆ǗĒ\x99ҥāҋԭǄфğˎǸ)cÙĸԇϜϒ',
                                    'ЎџśĝÎ˃ѵȝǗɲȌʫԄǜӛľrΜФĺԈϭȳǳƑĠΒ˂İѥ',
                                    'ÁҼÙƢӲŵƠŘ³ʂīŦƩɢɺ1ɡĜǦĉϡeoþǭ˺ǃ˪ɣϚ',
                                    'Ӄ\x9dΛȇΒƉWɆҡÏ˙ǋȊbΰΚɳԨϓ˥ϥСǡˠЁ5ˑĸ4\x99',
                                    '\x8cđ˕!ωʦӉɆłm҅\u0379ӻɈRЎnϜʳƝɒïǧѥƎńϛȤ¬˕',
                                    'ϧРǎǱEϘҸЗӈɟƎ¾ªϹ΅ęźį\x82рӵӺТƨHʦԈΟǬЖ',
                                    'Ίšʠѷӎϵ·ɐĨ˙ҲȘǭɵȓ҂ŸќԄ\x88ʄтͷԀƽɰǦϓȶà',
                                ],
                            },
                        },
                        {
                            'name': 'ѢȀԉ)ż',
                            'value': {
                                '^': 'int',
                                '$': 3571418831388792022,
                            },
                        },
                        {
                            'name': 'ʟʲûř?ˌŵзǅӦĹˇ$ìԎЊ¿ХВĭѸ',
                            'value': {
                                '^': 'int_list',
                                '$': [
                                    2413091626198106918,
                                    -2354788785355140406,
                                    7005430666757533394,
                                    2432940963665295468,
                                    5016915387934834636,
                                    6007256404403676007,
                                    2900083092577973430,
                                    6658047630840236691,
                                    6657544998002414630,
                                    7195765010288703507,
                                ],
                            },
                        },
                        {
                            'name': 'ħĭ\x92ŒÄÄѥ«ўҎYˮɣȲ˻ç',
                            'value': {
                                '^': 'float_list',
                                '$': [
                                    812623.2894669942,
                                    101266.04510907092,
                                    83483.74087716403,
                                    815197.4679280238,
                                    997164.5907616555,
                                    -9673.614485429658,
                                    171507.85202113364,
                                    -95453.3304593672,
                                    584071.3570683501,
                                    895309.9268297026,
                                ],
                            },
                        },
                        {
                            'name': 'ШӱÍlЦƇԑКΔ',
                            'value': {
                                '^': 'int',
                                '$': -101383481534831935,
                            },
                        },
                        {
                            'name': 'ɉЖî"ǌ ɞ´ơλƒpƔӣȊƼƇдԩ÷ǧԍѸѿξʅѶҿҼ˃',
                            'value': {
                                '^': 'string_list',
                                '$': [
                                    '^˃ϼγ˷ȍӨҍ˩Ƭ³ƨ˯ȥǊЫťӁǢǆҮ\x8eОƕȚ3ѭOӾѓ',
                                    'ŉԖυόάҴũԐĽѰĘѴя\u0380\u0383ƽˑ҇ψºØʩ˓äȩӿϷ϶Ԁӧ',
                                    'ʱϞ˱7ЫīqϦq\x83ɩСуϭ4ʥ÷ЂĊȯҵԌÒԗϻ\x89ˌѮ˱Ô',
                                    '˦ΉсӌϜǕȖGӕȲ\x8eҁ\x83ιŻȹЌӶО[1ąƥĳ}1ʬëƸƟ',
                                    'ɢɦѱЃ˖џǫΔǫʩҌѨӖ\u0381ɬßЧɞӂĢ\x91ƍæюʤǅʁǐɯϾ',
                                    'цяZԑŜԉάϛťȷçҥіѼÿϘť>ƋƚĄŋˉˁҊҟѨˤпƝ',
                                    'ԡʙuόCȃƁʺ³Ʊͽҧ/ЁЃĨ~Ѱɫ¡ӣ{ӳĨѝĮɋˋѰƵ',
                                    'ҢǃЃԪĹʲɠʓȋϞӨƴҌϱœҔ˙˵˅GÁуeɏћтʫʴǎԮ',
                                    'ΤҝΤԤĉƪҊ®ˑˌʴīʹȮùЬѽɂЉƈ½°ɾЀˌԛUӷøž',
                                    '˟ÃƮйЖԟѭ\x8bҒвԝҕѩҗʦŋ\x93óÓȬҗƣƑ\x85ԬЖѻФȅɲ',
                                ],
                            },
                        },
                        {
                            'name': 'ӳʼǑΕȉδŵеҸ\x9dτŐ¡',
                            'value': {
                                '^': 'datetime_list',
                                '$': [
                                    '20211104:183212.454691:+0000',
                                    '20211104:183212.472202:+0000',
                                    '20211104:183212.489816:+0000',
                                    '20211104:183212.507250:+0000',
                                    '20211104:183212.524778:+0000',
                                    '20211104:183212.542645:+0000',
                                    '20211104:183212.560375:+0000',
                                    '20211104:183212.577437:+0000',
                                    '20211104:183212.594421:+0000',
                                    '20211104:183212.611544:+0000',
                                ],
                            },
                        },
                        {
                            'name': '\x9fƨŞȓǓřžȊI«ѭ\x90˯Ϩа',
                            'value': {
                                '^': 'string',
                                '$': '3˧¢ͻƮάˏæ\x91S=ÞҫҹL˅˝Ϸ˱ԄǋŕĆГ(ȠԋƨΰϽ',
                            },
                        },
                        {
                            'name': ';Țźν9Ώńˏˤƹѭί˨',
                            'value': {
                                '^': 'int',
                                '$': -6910577514692165685,
                            },
                        },
                        {
                            'name': 'ŐӟǤ¯ȘλөŽίҗѫΉ1ÛąͷrQʆɜMaРԐÅ\u038d˴Ԑ',
                            'value': {
                                '^': 'datetime_list',
                                '$': [
                                    '20211104:183212.880953:+0000',
                                    '20211104:183212.902342:+0000',
                                    '20211104:183212.923924:+0000',
                                    '20211104:183212.941311:+0000',
                                    '20211104:183212.964585:+0000',
                                    '20211104:183212.993146:+0000',
                                    '20211104:183213.010459:+0000',
                                    '20211104:183213.027524:+0000',
                                    '20211104:183213.044147:+0000',
                                    '20211104:183213.060842:+0000',
                                ],
                            },
                        },
                    ],
                },
                {
                    'catalog': 'ҰāˏѺóÏĳӼˋҘɦɘĸАϔҝɆŦȎ˲ӎʣ²ԛРӣΨȕыē',
                    'message': 'ɑƮӊɖ[\\ʎƘβѐŇȜѕ´åǊưǐȈԭʂyĹʯʜĝʇТʲə',
                    'arguments': [
                        {
                            'name': 'y.\x81>с˓ʉȏŲӫçʁīŝ˞˺',
                            'value': {
                                '^': 'bool',
                                '$': True,
                            },
                        },
                        {
                            'name': 'Ӵ\x81Ԫӳ:\x87ϝӶɳȴĂʮ\x86RÖũѺƆʃǅӆЁ\x83ɔ˰ʵĘ\x88ȡǙ',
                            'value': {
                                '^': 'int',
                                '$': -5118613461566671552,
                            },
                        },
                        {
                            'name': 'ѺšѨρƠ\x82ѵėǴ˶OȻȈ*ҋq©·Mҝ\x9aĈϜƔƟɏЗŖȊЎ',
                            'value': {
                                '^': 'float_list',
                                '$': [
                                    279226.319705958,
                                    726405.5936473536,
                                    168619.1977275571,
                                    94368.06860761819,
                                    901756.7162589098,
                                    68504.46187881543,
                                    967312.7962018372,
                                    413004.9963942349,
                                    852709.9906889092,
                                    737590.1828224114,
                                ],
                            },
                        },
                        {
                            'name': 'ϤӱJɀЄƮϷʃχωǴȻϯ¬Þ͵ɇ˖Ǹ˄˞гɇ϶ʷǬЬі˽ʧ',
                            'value': {
                                '^': 'datetime_list',
                                '$': [
                                    '20211104:183213.596731:+0000',
                                    '20211104:183213.613162:+0000',
                                    '20211104:183213.629485:+0000',
                                    '20211104:183213.646792:+0000',
                                    '20211104:183213.664173:+0000',
                                    '20211104:183213.681317:+0000',
                                ],
                            },
                        },
                        {
                            'name': '+ѱϭЌ\x8bгӏеɫɒ',
                            'value': {
                                '^': 'int',
                                '$': -6977474721638596372,
                            },
                        },
                        {
                            'name': 'ȣȈƬԪǐʬюșʧțϼÉӎɢҧɺ»ǂЛ˜ҪǂíάFԇѭ˯яΘ',
                            'value': {
                                '^': 'string',
                                '$': 'ͰȌř{ϡʚӀŸЯľѥǺ©žԓ˜˝ƗӫåѫΰЪѳËϻˉʫȎҲ',
                            },
                        },
                        {
                            'name': 'ŔĻOȰĖŪҌϬςˏϳę`ϓ)¢ҋϣƆс\xadʁˉʫ6\x85',
                            'value': {
                                '^': 'float_list',
                                '$': [
                                    285322.021634828,
                                    839128.769453762,
                                    943915.8010611074,
                                    188062.02383000904,
                                    220341.88394789834,
                                    250857.9376836277,
                                    317614.3502060255,
                                    327744.82936311513,
                                    471102.3040427937,
                                    343.4009412478772,
                                ],
                            },
                        },
                        {
                            'name': 'y¼Ɍ{΄ō§ý0ĩɤҎɻ҅ϤƤĿԬЂӬĩϴ',
                            'value': {
                                '^': 'int',
                                '$': 1116580829292617340,
                            },
                        },
                        {
                            'name': 'ć\x9aӵ¤ʤϒɆћȨŉуɸ\x82Ï£ȳҟɽɕ\u0382ҋ\x95тλ˭ҝэΑƈұ',
                            'value': {
                                '^': 'float_list',
                                '$': [
                                    207220.0713517617,
                                    -9721.235150981898,
                                    856717.5477735364,
                                    -23756.442046672193,
                                    973500.1307686779,
                                    927025.6795788363,
                                    930895.9105666648,
                                    184904.04720167053,
                                    508408.7844771483,
                                    511572.99677920283,
                                ],
                            },
                        },
                        {
                            'name': 'у҉ԚѳӥƇɎŇǏͷƹMƊ˧',
                            'value': {
                                '^': 'float',
                                '$': 19286.930448058716,
                            },
                        },
                    ],
                },
                {
                    'catalog': 'Ʈ\x99Ώ¼҈ȒԌΏFuɩϒѨɌ«ʭӁRO;сԐȂϚ@Ҏ³EѓѮ',
                    'message': 'ʏșƥȁŚʡǛſʗǑvҢɠ\u0380ŜÔǇȂφƂЈjňƿӋȨKʤӫv',
                    'arguments': [
                        {
                            'name': 'ДÚϛʩʛӅmԮȸӸĚџӅϡģ$ĥ ŢѽԔґĴąԨЕƿѺΥ',
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
                                    False,
                                    False,
                                    False,
                                ],
                            },
                        },
                        {
                            'name': 'ɐҭ\x83đȖʒ',
                            'value': {
                                '^': 'datetime_list',
                                '$': [
                                    '20211104:183214.843968:+0000',
                                    '20211104:183214.862725:+0000',
                                    '20211104:183214.879208:+0000',
                                    '20211104:183214.896823:+0000',
                                    '20211104:183214.913502:+0000',
                                    '20211104:183214.930473:+0000',
                                    '20211104:183214.947168:+0000',
                                    '20211104:183214.963911:+0000',
                                    '20211104:183214.980702:+0000',
                                    '20211104:183214.999114:+0000',
                                ],
                            },
                        },
                        {
                            'name': 'ѽÏ',
                            'value': {
                                '^': 'float',
                                '$': -77441.75685489006,
                            },
                        },
                        {
                            'name': 'νƦœҢ˓ϕщǈαƮĭϨ°Ǝƒ˦ɛȇБïƕԨ',
                            'value': {
                                '^': 'bool_list',
                                '$': [
                                    True,
                                    True,
                                    False,
                                    False,
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
                            'name': 'WƷŔψďӒěͿÁoӮҗňϘͰ˴҆җΠбȧɗӎƶαƜǖӲ(˲',
                            'value': {
                                '^': 'bool_list',
                                '$': [],
                            },
                        },
                        {
                            'name': 'ѧЅă˯;ΐŉĞӻҪþоԒɻԛŹшӨ',
                            'value': {
                                '^': 'datetime_list',
                                '$': [
                                    '20211104:183215.483267:+0000',
                                    '20211104:183215.499765:+0000',
                                    '20211104:183215.516603:+0000',
                                    '20211104:183215.533355:+0000',
                                    '20211104:183215.552445:+0000',
                                    '20211104:183215.571095:+0000',
                                    '20211104:183215.587451:+0000',
                                    '20211104:183215.603880:+0000',
                                    '20211104:183215.619913:+0000',
                                    '20211104:183215.636383:+0000',
                                ],
                            },
                        },
                        {
                            'name': 'ԠʾϽŠħ\\ƵĒȘҼҕǄǷ#ʈŀNl\x9dƘѢȴϖ\u0383ԝőøœϘú',
                            'value': {
                                '^': 'string_list',
                                '$': [
                                    'ǫФͼώÛӳѠǲˢïȶȪҸʄӣƻŐȈùѶϞҪԂѵĸcΤɐσƼ',
                                    'ýĕϝ˙ȦѳΉŲ\u038dҜЫѓаęʃФIǖƇɡɉ§[ǃɺϾΦ\x89˭ԉ',
                                    'əďłϨҘ˪Ю¤ȀϰĽʡ҃ϭшʄƤćӍǏ\x92ƒɓϾʚƑϻaƯʿ',
                                    'ɕěҞɨѤ˧ȕˬÙ÷İɝǈͿÝōʠǙÉ|Iuϳϣʦӫ˰ƦϊǙ',
                                    'ӷӋƒҨǫɫљĢђЊƌɋԆõϠ˞οƭ©\u0380ÊΫ!ńΡżŹbvњ',
                                    'â6\x80ωϛЕДȘ϶ΝԚZϙΟƀ˻ï\x95ҺȃĄbEԁҵȻũεКϣ',
                                    '¦ŏʁϿ5\x99ƦԓĢĐӼϽѢHȓеѻř\x9cĄŎ\x96È\u0383ȥӴѻ!Ĉk',
                                    'Ő˪ѥǮҁiЪАɥÎņǳԞ*ÃƦ҃MцƂЕƪҳӣōϪʁϲЏ>',
                                    ')Ȧ˨ϦżѺƣȿƀŧƻ΅ȴɝǡʾӷԓӫŅĔϮҢőǇ\x97ȕpǋǎ',
                                    '˂ȵŦгħćԃϼљЪƈƶғ¼єϱԙԡ_ʞLăǸ\x8fԐȣ)ӟǥʼ',
                                ],
                            },
                        },
                        {
                            'name': 'ĤM ў˔ǂɨËƋȚԋДƏʑȂ8Ϋ˰ɯƃƜɇzȸÅʔλǁҶͱ',
                            'value': {
                                '^': 'datetime',
                                '$': '20211104:183215.954662:+0000',
                            },
                        },
                        {
                            'name': 'ʓYԊѠѡӖΩɺχί\x90\u0378бѡŻΫªΏҿƋŎǷД\x9aˡʲa,Ͳ,',
                            'value': {
                                '^': 'bool',
                                '$': False,
                            },
                        },
                        {
                            'name': 'ĘɲÆ\x95ňΔ\u0382RԈǿƜˬâҘ\x9cĎШȗȝҒ2ʷяД',
                            'value': {
                                '^': 'string',
                                '$': 'ÔƌҎͽń\x9bW«2ƅº$ƻ¯ӞũˬMɓÌˤԗЭX5ӆʿϲǤ\x8b',
                            },
                        },
                    ],
                },
                {
                    'catalog': 'ʹϼԩ˼͵ĞȿѡԏʣӃȖęă˒ŦÈѵŮ˷гȟŏыϴκǅΞƸ¨',
                    'message': '˪ʾ¯˝ǟӪ\x7fЈɠɛҥƖӗƫϗʰλɪƪ]Ы˅ѳęΤ˺ƠŀãȌ',
                    'arguments': [
                        {
                            'name': '§_×ӷ×пѬȒįťĺćʬЩ8 üğʉϸԐ˺ďǹυǦЧĢ˜Í',
                            'value': {
                                '^': 'bool',
                                '$': True,
                            },
                        },
                        {
                            'name': 'jɧюљǟϚ$cӖÅŐʁʲʙ£',
                            'value': {
                                '^': 'int',
                                '$': -4464612406378620921,
                            },
                        },
                        {
                            'name': 'λùƗϟɐϖ?ˆƜǮƬɧÌѓƈ˗ǟƊԉЋ',
                            'value': {
                                '^': 'int_list',
                                '$': [
                                    -951872221529202782,
                                    -4811102469104896056,
                                    -4458901971224334360,
                                    1011847923363214387,
                                    7216954762190573361,
                                    -475725118872513093,
                                    -1839919129472913077,
                                    881849779601115785,
                                    -1984980068195249409,
                                    -4308237958777034162,
                                ],
                            },
                        },
                        {
                            'name': 'зξ&ȂΉê\x95ґGʅӹ˪ѾɆҶһԜjŔʻĆȹʹяĕӔΓïˢЉ',
                            'value': {
                                '^': 'string',
                                '$': 'ҚƍSʌʛȈǗԪυˍƵı¸Τ˓ӉǩǫɦΝСĸ˅Ï¹ΌʷǍıԨ',
                            },
                        },
                        {
                            'name': 'ʦ\x91ʝƬљˈ£çӏFʡԒĻȄƟŽ¸ƞȯcƐʛϗƢȼҊȟŸð˫',
                            'value': {
                                '^': 'int_list',
                                '$': [
                                    -1842870544170036857,
                                    4757475435297955507,
                                    -9024169570782774630,
                                    2352126141213905358,
                                    1902655309614058460,
                                    7308402162181484626,
                                    5739677774123681797,
                                    7410241913142629006,
                                    8021963708173170583,
                                    8497837315699956943,
                                ],
                            },
                        },
                        {
                            'name': 'ҲŽʈ>Ԝ\x9cƐӵѭЙƈҏǛǟΜ/όĐ5ȤиžʭϩĉїҳĆӅС',
                            'value': {
                                '^': 'string',
                                '$': '>ƃ˱ƙӊƁĖЮϔΪʳғĴ&Äԥĳ˕*ʱșl}óɟūǯЙŝƯ',
                            },
                        },
                        {
                            'name': 'ŐϖȈӽϻӔӦĮsèŇȂФИЫ4ҞuӅЗԌĒ҆бÐ¯ĆϢўҥ',
                            'value': {
                                '^': 'datetime',
                                '$': '20211104:183217.034141:+0000',
                            },
                        },
                        {
                            'name': 'ʒʴәȊԆԁҐӽβϱΑƆŗñɷ',
                            'value': {
                                '^': 'string',
                                '$': 'ʝǶίќȝӆӸӝϩ\u0379ĥˍѥϪԧѣҲɲΡѳʛӳθǌ¨¯ˁ\x81ĺʾ',
                            },
                        },
                        {
                            'name': 'Ń',
                            'value': {
                                '^': 'int_list',
                                '$': [
                                    -1019669301867836366,
                                    4478862832004619046,
                                    -3276753467151101360,
                                    4058480247570798814,
                                    -5214274235078587500,
                                    -3984379597791236665,
                                    1800247292498449612,
                                    -2542694216410315716,
                                    -596344137334080859,
                                    8466585154886671086,
                                ],
                            },
                        },
                        {
                            'name': 'ȅÜɗ',
                            'value': {
                                '^': 'string',
                                '$': '\x98˲6ҼĪĄӓԝΣΤøӜ*ӌ;Ŕe1QϪ\x93эŁϏǋɒǚͿΣѝ',
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

            'identifier': 'ЌΤʲʪť',

            'categories': [
                'network',
            ],

            'messages': [
                {
                    'catalog': 'Ȑl',
                    'message': 'ʕ',
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
            'name': '| Į£ӌϏ˗ѿÐȁƓƉȒԔʙį"ŨѻȮӌɈʂҮҴȯϮԌƿƥ',
            'error': {
                'identifier': 'ѪƎӲǗ\x96σʫлϛɛƑѿõΧʝϕĥȐҐÑȜÔяȣΔȸɺδΐʚ',
                'categories': [
                    'os',
                    'invalid-user-action',
                    'os',
                    'access-restriction',
                    'invalid-user-action',
                    'invalid-user-action',
                    'access-restriction',
                    'access-restriction',
                    'file',
                    'internal',
                ],
                'source': 'ӾȺʉŮѮΉ¢˜єáȍ\x90ҹ˖ѕÌƇǔĄēʦƟɀʟπ!śɺθ\x95',
                'messages': [
                    {
                        'catalog': 'Ԉ\x90и҅ˡïѮ϶ԅƚуēΖϺ\x91ĞɧeĩԕвťήЂ¿ζΫʳɕД',
                        'message': 'ãǚˑ1Ɛʷ·Ľĩ\x91V΄I˲zɞʕǀҀӽūJɄћŧʨ6ɦʢӟ',
                        'arguments': [
                            {
                                'name': '΅ɪԀ˞@ŝȶɚԔӗͿǅȬʟªʖЏĺһòĊ˅',
                                'value': {
                                    '^': 'bool',
                                    '$': False,
                                },
                            },
                            {
                                'name': 'Ϛ˄ŎËʨљʗ˄ˡҗωьƁƨ|cȔе҃қ˺Ȋ=~ҲѬϸπɺƠ',
                                'value': {
                                    '^': 'int',
                                    '$': -3615711220152903230,
                                },
                            },
                            {
                                'name': 'ˑʽӐː˓ɧώϿ]ʪʦϛӞ˅ɹѰҝãӴȳҦŰǞұƎ¦ĭü:ǃ',
                                'value': {
                                    '^': 'string_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ͱόӉǿѭÜшʸǶ',
                                'value': {
                                    '^': 'bool_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ˢРшͲѷǖϣ͵ŤаϳҨӪϤǠğOӰėïԬöѱӒ³ΤѮϴˁυ',
                                'value': {
                                    '^': 'bool_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ʗһѮԞäSʨϑӵʊ%6L',
                                'value': {
                                    '^': 'string_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ҶԦįԫŨǟӺʉĐɄxġяΚǙ_À\u0381',
                                'value': {
                                    '^': 'datetime',
                                    '$': '20211104:183153.081604:+0000',
                                },
                            },
                            {
                                'name': 'ƂÖʮɛмͺλцɨӾ¹}ĺƍVқkĦƘīƋJűǰȢ\x8b;˘ʱƇ',
                                'value': {
                                    '^': 'float_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ſΦʥɟƉĩǷǥҪưɇĊƄԅȝϹÅһġϝ˜Ο',
                                'value': {
                                    '^': 'bool',
                                    '$': True,
                                },
                            },
                            {
                                'name': 'w¥V7',
                                'value': {
                                    '^': 'float',
                                    '$': 836093.7450796303,
                                },
                            },
                        ],
                    },
                    {
                        'catalog': 'öʛŖԑȑĴǶe\x87ǸĿʄʐҷӈɠȨЅľҒ&ȂӯʡƑÂϿӧυк',
                        'message': 'Ӳӥ,ҭċ8ɽСʄɮχѯƘ¨чьfǀԋƚǄǗКôѼΕѤ"Ѷ9',
                        'arguments': [
                            {
                                'name': 'ÁIø',
                                'value': {
                                    '^': 'int_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ɭƽƣʒǞˋԜЫĪʊƨ(ӵѹʉĈԟӷûʭôeȶƨ(ȩ}Ɍа¹',
                                'value': {
                                    '^': 'bool_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'Ĕ\xa0ΗŉѻƻϗĊЗԡíǯϟ',
                                'value': {
                                    '^': 'int',
                                    '$': 2093533787761899530,
                                },
                            },
                            {
                                'name': 'ΈTΈȏÚѐӲҽòħEʷВÅ˔ğưҷΐΤЗўĶτѩʲЀƦȥ®',
                                'value': {
                                    '^': 'int',
                                    '$': 1464534903481875592,
                                },
                            },
                            {
                                'name': 'ĵ\u038bғźuȇìԥӶǪƳǛ\x87έÆƘàūͿȟƖńȝˍѦÅ',
                                'value': {
                                    '^': 'bool',
                                    '$': False,
                                },
                            },
                            {
                                'name': 'ӟÂȤμŀЈӄÕΓҀ',
                                'value': {
                                    '^': 'datetime',
                                    '$': '20211104:183153.845431:+0000',
                                },
                            },
                            {
                                'name': 'чԠɿ>ǟƗм\x85ūʏбšϹŘNԏèǷāǘŮΙɚ',
                                'value': {
                                    '^': 'int_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'śʫϸЀě1',
                                'value': {
                                    '^': 'float',
                                    '$': 581171.1427164585,
                                },
                            },
                            {
                                'name': 'ʆΖӫȩĝωɑ˓ȃԊ˶ňɞ',
                                'value': {
                                    '^': 'bool',
                                    '$': False,
                                },
                            },
                            {
                                'name': 'k?ǝʄϗǤŭԍѮ0ĿřLȜӂϋӯ',
                                'value': {
                                    '^': 'int',
                                    '$': -4242169140261362608,
                                },
                            },
                        ],
                    },
                    {
                        'catalog': 'ϟόҥԊӒϪҤƌĭ ΗҶ\x9dήƤϵŤѴҳÎ%Ƈ҅Ҁϱ˞ӋǬûǭ',
                        'message': 'ɃɌțзRǾ{ɹŬɳˑљТʐșҔО˥˵Ģʀԫˉ\x85ľğ3ÃcÌ',
                        'arguments': [
                            {
                                'name': 'ԮÚʓЧ\x90τОьQЅћϨɞ&ǔЙиȼӃƁÛ¾ҷάӿϙŐΝʿт',
                                'value': {
                                    '^': 'float_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'Ή',
                                'value': {
                                    '^': 'bool_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ǘŲZ\x8aƈɱƪпӆǎŮğǃ\x95ƯÆģ˺$ůҁД\x8cΙǮȈŭЗǜV',
                                'value': {
                                    '^': 'datetime',
                                    '$': '20211104:183154.512866:+0000',
                                },
                            },
                            {
                                'name': 'рǵ\u038dѱǙϫеƹόƐȲ7ɰʓƝѴʮJшϮęfГR˄ȣϧȧ˯Ȑ',
                                'value': {
                                    '^': 'bool_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ʳǶП˷бҖ\x88țЙʱɭǵ˪¥˽ƿʶЖӊýћɭ=@ӏˮãɈхԖ',
                                'value': {
                                    '^': 'bool',
                                    '$': True,
                                },
                            },
                            {
                                'name': 'қʙɍ˕ŻҖӄ||ԖăF϶Ñ×˥ąΦЎʶƲǉƐ˼Ϡ¶+Ŏ8Ϸ',
                                'value': {
                                    '^': 'datetime',
                                    '$': '20211104:183154.751823:+0000',
                                },
                            },
                            {
                                'name': 'ʚ¥ЁϰȀҁɝȂӐøТɌѐϻ6^śȍԢĆʟϺиɕwĕщęЧƦ',
                                'value': {
                                    '^': 'float',
                                    '$': 392885.95111894317,
                                },
                            },
                            {
                                'name': 'ŜɩȢϔɟȹϱɆʻΎʡΌɸŢŰȶûКśϐöӧ˃ÑΗ}',
                                'value': {
                                    '^': 'int',
                                    '$': -1944153460172700961,
                                },
                            },
                            {
                                'name': 'ѧӥҵʭ¹eҴÐύǑǨ\x9bΏƪɁˣ˸ҒЂʞĳɠɩa',
                                'value': {
                                    '^': 'float_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ƲńʱÕJԣʴ"\x811nȨÙʏԍʆΒ\u03a2',
                                'value': {
                                    '^': 'datetime_list',
                                    '$': [],
                                },
                            },
                        ],
                    },
                    {
                        'catalog': 'đӱԋeò\x97űҊŕǹcη\x9d4ȓ²ʴӭʝˠhÜłÄ',
                        'message': "\x89XТʯ˖җƍϞȫȚԇɀǋȌûΎԢāԟɨθӴԅ¸ʥɦԂå'ѝ",
                        'arguments': [
                            {
                                'name': 'ɠӈғʓɃôЅϛԙɶ',
                                'value': {
                                    '^': 'string_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ЄȥӌӁe҄ЪTˬԤ˜ÔɷΌɧǰџǎ',
                                'value': {
                                    '^': 'string_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ȏӽȻ\u03a2eЄȪʴ\x96ԓҷÆĩү˜ǖæƍԐˁŘµñɑ\x97ǨȈˀɽʃ',
                                'value': {
                                    '^': 'string',
                                    '$': 'ԭŜѾŁþиņǑɊğŘԀ¦Ԭ˓ЀƙПƘɖҴñЏǞňӖýȿ;і',
                                },
                            },
                            {
                                'name': 'ȭӌԁʀ¹ϛЫőǖƞŶʪŜăЍч\u0379ЄPӎǑӏ(Ⱦπİ',
                                'value': {
                                    '^': 'string_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'Ş°ԎÖˏѸǈҡ',
                                'value': {
                                    '^': 'int_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': '9Ӫьё\x8aҮωҴԃұșɖŖɴȌÆfȻŽԞýƦǞ»ɿŹʇcĖΡ',
                                'value': {
                                    '^': 'float_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ӱҎ9˪љűĺȹͽԬƲԔϡыщ«ӋŮ»ŲǧɈǼĸ˰ȵĚǩšӻ',
                                'value': {
                                    '^': 'bool_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ë´ƲìØ$(НҮћɈҪˡĀǲ˚ϝǋƉåђ҅Ϟк òɔɜвԧ',
                                'value': {
                                    '^': 'float_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ʙʉɱŹĖïίśԘƆΊѧFpǻԀ$ȣΉҍ˲Ԯҡ',
                                'value': {
                                    '^': 'string',
                                    '$': 'ŲąȎΚə΄ӶΜʏÈŪǜ³ơωѸҀĀҶԮʔº˪ЧΫßΦȔʬҮ',
                                },
                            },
                            {
                                'name': 'ӧMԬʻǄѠȓӤ',
                                'value': {
                                    '^': 'int',
                                    '$': 6345923573957006187,
                                },
                            },
                        ],
                    },
                    {
                        'catalog': 'ʼøǹϙɢѫίʾӂΪŲѡҤ˥Ð>ҬļœҀ1ϜӻȚЌ~ӦçҐ¥',
                        'message': 'ˑňѭŘÖӹCMɃTӗϠЇ-ҢЅŽΉҡҙέψԡҷ\x97Ԛţ\x86ϸň',
                        'arguments': [
                            {
                                'name': '˪ǇϘħΞɯМЍ˾',
                                'value': {
                                    '^': 'datetime_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ƄñiÌКѼǓчɉԒ¥ϢϓљӣĸËρûÒ´\x8aǒνu)șĹҞʞ',
                                'value': {
                                    '^': 'bool_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ȇĺϔJɪÊΞ¨ƶɼŅĝŃʛъϑ\x8eѥТыķę·˖κʔ\x80ƄĎӋ',
                                'value': {
                                    '^': 'float',
                                    '$': 752841.4142423458,
                                },
                            },
                            {
                                'name': 'ˢǥϨҍɡɮҹʵСϟŔӾìŅԆhԉԊŀԌeğӶ',
                                'value': {
                                    '^': 'datetime',
                                    '$': '20211104:183156.349873:+0000',
                                },
                            },
                            {
                                'name': '˘',
                                'value': {
                                    '^': 'datetime_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ĸk\x9eŻƪƗɈмβÒ˙Ɣʑʤ˞Ԃ.ĐüɁ·ʯ&ҀθȊʾɌѾ',
                                'value': {
                                    '^': 'int_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'γƴɇ8ǚҪ',
                                'value': {
                                    '^': 'float',
                                    '$': 237478.5546736,
                                },
                            },
                            {
                                'name': 'ӻύςČα҃ǵΫЂǣė˽λԫƬѢӘϟ',
                                'value': {
                                    '^': 'float_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ʹǸîƂͺʧΔ%ȊʊɀȎˍԘ˧ȩȝ\x8fƟĭɈɚɎƜȊƧϱ¿cѵ',
                                'value': {
                                    '^': 'bool',
                                    '$': False,
                                },
                            },
                            {
                                'name': 'е\x80ɯ$EȚęĎźх¶ұӥǠΑĻʑʣţÿƖ˄њʗȫƯϭμɼē',
                                'value': {
                                    '^': 'float',
                                    '$': 234354.49838618014,
                                },
                            },
                        ],
                    },
                    {
                        'catalog': '\x9a;ȋ϶Ͷ·ΩΔҭ\u0378ŻƣȦ\x98ёӀΠɩϞŉчѧҠƼȝҥãΨҵɧ',
                        'message': 'ɃʀΈϿĳȌǐêУ\x80ÂЄϠӞǄΝĄЯώ¾УßâʽľƗӈŗНӫ',
                        'arguments': [
                            {
                                'name': '´TԕӝɗāҖԗġǥͿϮŠF˼Ņ҄аľԭӅƲбѳƓ˸ΊĺÅʒ',
                                'value': {
                                    '^': 'float',
                                    '$': 680047.0840035289,
                                },
                            },
                            {
                                'name': 'ǵĴsə˧Ӓԥũŕ$Εęʠωˊ\u038dƟ-',
                                'value': {
                                    '^': 'float_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ξ9ǴΟÌӋǪɞÆƬҔö;ǛǭVíÅҡʊĸѪғќ_',
                                'value': {
                                    '^': 'int_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ɗĘҫ5ȵȝӴÒɳ#ͳƭĴ҂ǭӗ',
                                'value': {
                                    '^': 'datetime',
                                    '$': '20211104:183157.173910:+0000',
                                },
                            },
                            {
                                'name': 'ͶƖΐɅ\x8a˒ґțǆʁϰyͿˤŋàϺΣüѶƫɛЀȣα',
                                'value': {
                                    '^': 'int',
                                    '$': -706626505310419626,
                                },
                            },
                            {
                                'name': 'ɍ˼Łmãɵ˹ǘӪŢўƛĉ',
                                'value': {
                                    '^': 'bool',
                                    '$': True,
                                },
                            },
                            {
                                'name': 'gĠԏϛ\xa0νŢœϘԣMԖʿȕgϳʖǲϼԑ',
                                'value': {
                                    '^': 'datetime',
                                    '$': '20211104:183157.441561:+0000',
                                },
                            },
                            {
                                'name': 'җКŝƴ',
                                'value': {
                                    '^': 'string_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ÒăơɢѱǐЙƜĉʿů·ѸńҲѨҳɖӤƳÇ¯ρң7ȳ|˨RÓ',
                                'value': {
                                    '^': 'datetime',
                                    '$': '20211104:183157.577724:+0000',
                                },
                            },
                            {
                                'name': 'ŁϬԕȜȨҡ',
                                'value': {
                                    '^': 'int',
                                    '$': -1791520388365067566,
                                },
                            },
                        ],
                    },
                    {
                        'catalog': '҇=ǧНÌǫԏƶhöħΟӲ-ӺîԮqǭиӼˉ\x8fȃȂ<ΗХɷҷ',
                        'message': 'ǀѼѰӹɠԚǷȨϗƛČǃȞǼćΡ҆Uйόˀз˸æ0ɿʨЅƎŏ',
                        'arguments': [
                            {
                                'name': 'єʏƺȳȫˆǜǠϺӬҏɞѧКǈ҇҄Ѻԩһ',
                                'value': {
                                    '^': 'bool_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': '҉ˡ]¦Һ',
                                'value': {
                                    '^': 'float',
                                    '$': 421496.1724554112,
                                },
                            },
                            {
                                'name': 'ψɞɤϖťőћҩÖчЇ¯ȓϴϡԔˣΛĥêĀȿƽҩӻ{Ҭîh0',
                                'value': {
                                    '^': 'float',
                                    '$': 754190.7671197004,
                                },
                            },
                            {
                                'name': 'ϻɚ',
                                'value': {
                                    '^': 'int_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'Ҋ\x8c³ƯÆ˦ɎȋÈˊ÷ȍƙ×λѲѥB˔³ʛѺɕɨʵ`ĒӠωȩ',
                                'value': {
                                    '^': 'float',
                                    '$': 707748.1154387415,
                                },
                            },
                            {
                                'name': 'ļʆΊƷǻȈ-ʖʘXԝɀǜȥΕɩ˳ˣ',
                                'value': {
                                    '^': 'int',
                                    '$': 160096869252787889,
                                },
                            },
                            {
                                'name': 'EĴƇқΧƙҌ\u038bXɗxùΞȇѶ/аζũӐʤ\u03a2ʯűԣ<ѵ\x84ɑƼ',
                                'value': {
                                    '^': 'int',
                                    '$': -2557580076794630409,
                                },
                            },
                            {
                                'name': 'Ƿ,ǻĎɯÀ;ǾƮ¸ɃPȵɖԉƼǖĿОŽΝ˩lɛ4',
                                'value': {
                                    '^': 'datetime_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ѥXA˂˚áȖρĔі©òŖVǗӥȠϹԬӨШΘʂ',
                                'value': {
                                    '^': 'bool',
                                    '$': False,
                                },
                            },
                            {
                                'name': 'ȽӄҘԁ˗ŕљ\u0378Ӽ',
                                'value': {
                                    '^': 'bool',
                                    '$': False,
                                },
                            },
                        ],
                    },
                    {
                        'catalog': 'ʾȏҍóY˨ѸŶŶʭǋņҙԨ*3ӻƙжʌʑБ˞ғƾϴх³ʰϷ',
                        'message': 'șΆӋɊš²ɐ.ԢÝ·$ʢÌǢʏɧєʿкζʡǞʄƌѱ\x8eǸΨĖ',
                        'arguments': [
                            {
                                'name': 'Ȧ£ȝΰpҼ',
                                'value': {
                                    '^': 'float',
                                    '$': 504303.8860834399,
                                },
                            },
                            {
                                'name': 'Ʌm,ȠҾԄϹʽϩȪȖűƺɦϹ˾ѸȀEȦôəѿҕGЩɐȦΔ²',
                                'value': {
                                    '^': 'int_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ǵԞϔɠЯфϜβԧõɄŚϰΒǓωЅӗÊ',
                                'value': {
                                    '^': 'datetime',
                                    '$': '20211104:183158.830343:+0000',
                                },
                            },
                            {
                                'name': 'ɫȇÈҙñ\xa0ѣйʱϵˬԟʌʮΎȒΒҤ×ԀѣèǻǱǑʫȥʜɧ҂',
                                'value': {
                                    '^': 'string',
                                    '$': 'рӻ˟ǱȤyŶ¯еӱРνϭКˍͰ}ŸҾϳʭͽʌŇƛÂ\u038dƁ¡ß',
                                },
                            },
                            {
                                'name': '4ψqχμǉ\x7fҺɓʤƳđ˛[ӍƫƎʄČȽĞÚÐgҼʅcŻȁƌ',
                                'value': {
                                    '^': 'string_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ͼƦѧϛǠŔѭʯԂЀˡ',
                                'value': {
                                    '^': 'datetime',
                                    '$': '20211104:183159.037134:+0000',
                                },
                            },
                            {
                                'name': 'ɟʀъȅ\x9eʔΞ`ӭ7æΘ<ϐŞÀ˝ˇƙǤ҃γǗÎґҸѭǥҟÈ',
                                'value': {
                                    '^': 'bool_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ȯǷΑԏɝҚԌÈĀɢбȰƝÛƧ\xadʃӈĸ½ĄǙњˠпŠČʜ҇ð',
                                'value': {
                                    '^': 'bool',
                                    '$': True,
                                },
                            },
                            {
                                'name': 'ȦѻśĭĲϯѵ°ӦΔʗ>\x90ʦԅȝÕ?Ο',
                                'value': {
                                    '^': 'string',
                                    '$': 'Ȫ\x92ºҀτǳɉБSƺ²Ђ\x93ȱѡƥјь+ʤƚѬ͵У%ǂńÖÀ\x87',
                                },
                            },
                            {
                                'name': 'ϞâɫкɔʶˌƉǓƽв\x99ѸϿ',
                                'value': {
                                    '^': 'float',
                                    '$': 701294.2707669759,
                                },
                            },
                        ],
                    },
                    {
                        'catalog': 'ŝбҝCΗυԍΝʂž`ŔѢіƩЪϳǻåҲəQʇ͵œʋ˴Ǫƴˆ',
                        'message': 'Ԩδ҇Ӿ˫ϱǂҦ/Ҵ¯ғƇªNƥҮǧʧҀǖ˻qǝˮԑԊɸĚȯ',
                        'arguments': [
                            {
                                'name': '˷ɹθΫķӚӄ˔QīӬϳxϪҶ¸ŌüϝȜ\x97>ɗ\x9aϽӽӉãØЄ',
                                'value': {
                                    '^': 'float_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ȇ¶ǺƊЌąҫǊҶȏĭȣȴǕǛʙĴqƁЉҲә\\αǰӄҕɫǃ\x82',
                                'value': {
                                    '^': 'int',
                                    '$': 4819948648076632284,
                                },
                            },
                            {
                                'name': '\x80˵Jʛ¿˥ǍϜӵEϣUԞɖɆ°ϗŧƻȓʵɥˮŝͶͺ\x84ҭ´ĸ',
                                'value': {
                                    '^': 'bool_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ѦSƚüѾ\x98ʧ˙CΤʗϏȞǧϽһЗœ˚ɮđφŻϭœʨӥϕǵι',
                                'value': {
                                    '^': 'float',
                                    '$': 295080.73888398916,
                                },
                            },
                            {
                                'name': 'ĽҌѐȴĊ¾ʮåεɸβZϰŝЏɲ·šǮ-ǫċʤʣρîɮŝѤԉ',
                                'value': {
                                    '^': 'float',
                                    '$': 41817.60387874878,
                                },
                            },
                            {
                                'name': 'ʓÞţч·˃ïʁʞɫӄš,ȅǇÕҼӘǝǮ°\x87ѕŁԙŷӨǝ,Ȝ',
                                'value': {
                                    '^': 'float',
                                    '$': 988603.9921861016,
                                },
                            },
                        ],
                    },
                    {
                        'catalog': '҇ʌŞɚԜȱѝԃuĵ=ʰx#ƃԣΥ\x8dƨ¸˙ӗʛbȉϵΙǺǒ\u0381',
                        'message': 'ήΔ˹ȍҠ9ŇǎŃˮͺ˓\x83\x84Ϟ×фÿƉҲ8ƫφˋŞΥVȖ\x82u',
                        'arguments': [
                            {
                                'name': 'ǠʫҴҼʊˀǠ\x92˺ћgéόļʩϰ',
                                'value': {
                                    '^': 'datetime_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ѳſ¬ȱЈ',
                                'value': {
                                    '^': 'float_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'Êǅ{ŏσȄŸϐǽЉˠķȢҪɗĂ\u03a2ǯʳʝ',
                                'value': {
                                    '^': 'float_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': '÷ÿ\x92śǱˌŝƍϗƞϬҚӔǇ;ĦѧХԇΠόȼf-ΚɢѴć\u0379϶',
                                'value': {
                                    '^': 'int',
                                    '$': -2742589099094611015,
                                },
                            },
                            {
                                'name': '»ҪνŀʎΏѤњӮβсϪȮɦү',
                                'value': {
                                    '^': 'bool',
                                    '$': True,
                                },
                            },
                            {
                                'name': 'ϬӇӍӱƑԃԘƹЪǷδϛh\x95Ǵſɾ',
                                'value': {
                                    '^': 'bool',
                                    '$': True,
                                },
                            },
                            {
                                'name': 'ſʕЪӹĜȄʹǨȶǣϙ¸ʻ5АȺĀôҦƆͰċÆԆ',
                                'value': {
                                    '^': 'bool_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ΓFϸƨ\x9eϐвıЭɦËǼēӨáЊϠɸˊĜƆĬϓȲöВ˱ϖ',
                                'value': {
                                    '^': 'string_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'ɺҿųϽʋǭƔɖбӤѪ\u0379ΘŊ\u0380©Ŀbю\u0383Ġžȥ\x86ϭÄʠѲæȷ',
                                'value': {
                                    '^': 'float_list',
                                    '$': [],
                                },
                            },
                            {
                                'name': 'Ȍ˸ʹ',
                                'value': {
                                    '^': 'float_list',
                                    '$': [],
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

            'name': 'aÔɫ',

            'error': {
                'identifier': 'ˍӼÖβӰ',
                'categories': [
                    'access-restriction',
                ],
                'messages': [
                    {
                        'catalog': 'ъԛ',
                        'message': 'Ž',
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
            'name': 'ŌÈиɷР7ȂӣҮǓϏ¤˔ı1ʔћϙ',
            'version': [
                -6275568387665225701,
                -3752373048390279732,
                -8231514706918596750,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'X&Ӈ',

            'version': [
                -7006813663690952727,
                -2518405170013231607,
                -4743628712546337192,
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
] = []

EVENT_LISTENER_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'event_id': 'ԋFΜǞхʅy#ғ˺҂ќԍšϩАȽȃҌÉƌɑñǨ\u0382ΨŃ\x9d\x9fȟ',
            'target_id': 'Ʉ˟ƒԌĿлǛˡƖђηʭѹzŕʩ\x82_ŘȪ\x8d\u0379ȨҒǠÀɄΆśğ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {},
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
                    'event_id': 'ўǽ˚ÙўФÛyÛәʧҠǙȬӥȌªŲϤœԖ\x8fȺʶԛʈĖƏΞˀ',
                    'target_id': 'њ\xadǰΡѷˬʯγŕę\x8cǻÂŦъ˶ϙ\x8bĊҀXԞſгɂϹШʮŽĿ',
                },
                {
                    'event_id': 'ТųУǲԕӋͶĜ˲jϫɆϒңĜǳԜÁ\xa0ÆJҩ½Ӥ¯ȶơɭǤν',
                    'target_id': '_ǆʸЦżӸʾȐˋZӰΈЀËϑ%ЀЫҌϏʈɂХҹģƽ\u0380ġ϶ĉ',
                },
                {
                    'event_id': 'ÌʢÈ\u0379ʕŔҾӠϪҚƪÔƵŅҽ×ЀɃêӿȀΑ\x85ђŎȐl+Ʃϱ',
                    'target_id': 'ýeЁ\\*пėƦȫ\x8cԏ˳ķЫĔξѽēYυӸĐƶƪ\x9aƭ˄Ǻ/ɥ',
                },
                {
                    'event_id': 'çɼ^ǟˏθÚЫVū\u038dҢńɊÔσҭȭяǒɌȞθԩļƴПɫΫ¬',
                    'target_id': 'ƕӒРΒǷȭ¹ƾΧìʄˋ&ìʑԛҎyӃϡёΥʹǯxVҶɏšҜ',
                },
                {
                    'event_id': '\u0379ǂrò\x95Ȩ1ˋїéқς\x90рǷǾƙђ¢нȑӻãå˙ŝчƘϝʬ',
                    'target_id': 'Ҍ¥ϕ\x83ϖoʀѻ\xa0PĭŒʸȑ±ӯȪϜ˂ОĴ/ɹ>¦ŅCЌ˝ǆ',
                },
                {
                    'event_id': 'κёȑ˸ҡʧЭǺ.ƲʋғӒ\x8aɿŴį\x9fɵЌ\x86ʖȰϪÒţ·\x91Īˣ',
                    'target_id': 'ǠĚʫҐϯ<ˮͺưǚʚĐҋτӑɷ!ĀшĶ˫ǌ˴ƾȧϖӒ\x88ϒø',
                },
                {
                    'event_id': 'ϩʟÊӶ)ҌВˀƔpЗǾϖ£ɹήҦ\x8cƒƧԤaЮǠãĔǥ˗˧ˊ',
                    'target_id': 'ԥϘʃӉȷ|˨ĸƛӌ϶ʄ~Ȉ\x9eϖɲĒы˞ЦĠОîŒДЪȥЊй',
                },
                {
                    'event_id': 'ŤҲϻɮΞОǙʄɛϗӒƆăłӡя҇·ҬϿĴүȆ¨ĸě;qƨȵ',
                    'target_id': 'ΛӉҠӖãӊƁҞʒҖҜϩʔˢъ\x8cžˠͶƸΔȋ(ӥɓҶǭąɱϲ',
                },
                {
                    'event_id': '+ӌѳӹШПӖҀʪГ˃Ć\u038bŧƵРơҶǧ\x90ƉəyДˊҲƦʉƊ½',
                    'target_id': 'пŷȻІMӫϰʮǓΒ\x9eŭɑ\x83лʴ˪$č1HԮïŰ[ȬˋѰιɽ',
                },
                {
                    'event_id': 'Ͷɹ²хA˯ĜЌП^B®ҬÅϸϿӄқήКùƩˑЈ,ԬǴ¸`ȑ',
                    'target_id': 'бũϠǆŹΣɝϽɂҤȖҍСlΔёӣҊғϡ:å˧ɪƍϦμ ǼĎ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'events': [
                {},
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
                    'event_id': 'ҙԞÒÖƣõ҅Ϟ×ŵқǆŵЕÑŘĒʘȸǦ;˅Ҭȗ҆Ǻ˪dԊƷ',
                    'target_id': 'ЋѱшӥȪЎѠ\x88)ʈӉñˀ©ǖ5xĞřҡӨωįAŀӌƽǍ¾ō',
                },
                {
                    'event_id': 'ÀƸæб\x84ӈǺͱҹòХԂӔɻОʨȉZ\x93ɍƲјċǎθ=3ģҫϏ',
                    'target_id': 'Ǽ\x9eƺŸò\x9dȍӌǭЭ˻ϑGɿêͼȢtCЏĕЍԭçϱΐ:˯Џҥ',
                },
                {
                    'event_id': 'ÔŔȹɟДmˌкȩϔǰɇɖ`;Ӄn\x89»ԧѦɭӂ˵ĐθӔƟīԐ',
                    'target_id': 'ѷ\x8aɒŲѰΞ˔χƛ\x86ǊʹĀҠǣƥҙŽ˓ĵԓɗŇɻŷԕçӵƮԟ',
                },
                {
                    'event_id': 'ǇɳĹԭ\x96ɥkϯǾЈӅģƓ˺βǉ\u038dɺǙɸӰѼЄгɵ²ɡϛͿм',
                    'target_id': 'ċҡӖҋυ×ɷ˺ˤͶħǐǉˉ҈Øʵ\x89Ŏ-ƯȪƛÖρŤ\x89ȷаʵ',
                },
                {
                    'event_id': 'љѶȑǲ¡ӎƇȔ¾ԤGʛåƢəbΕĈӎæϞБŌφa\x84ǳȌÒŤ',
                    'target_id': 'ΒˠȳŨӤ¼ɵƥƘµнȿυǻ`ȇǶŪ{ŮΧ(¢ÈҍcčƽǕƼ',
                },
                {
                    'event_id': 'ϳҾҸ˶Î˫ӯωʖ-6ʏ¬źǯ´rú\x86ġͲȅĭԆͿѓðӪƺY',
                    'target_id': 'ÆԆ϶ȌӔяͳΆǐʭˑ\x8dҎ×ȷӒŠѫŊ8¨ӃЉíϱāҋԣȇΫ',
                },
                {
                    'event_id': 'Âѳ҇ϡʲɈйTҡʯѐnЈ\x86ŋΫÙѼӧΥϣΩˌӬ\xadȰǱ˟ӽC',
                    'target_id': 'ɮϪ˭ĥőҤĚǱΨȟуΝ¢ѧϓӨ\u0382ϥҚоˍ҈\x9dǟòʀ˓ƽϻѦ',
                },
                {
                    'event_id': 'ԖңӃĵĉѷɣūİì\x83Ӗ4ӷ',
                    'target_id': 'ӆu˦ȱԬĸԓyřɯŵÖƙӄ0ɶŨФΤȼŎϻşŲȐ5Ӌȓȡз',
                },
                {
                    'event_id': 'ҌĄӎ˺ŮѨԩǿ˦ǒǲԗØɖ¾ǺƀţҭԧВͼţїʰĎƠcԓϺ',
                    'target_id': 'ǓьӜJԕƒǠǟͺˉӦ;ɏʞȼlȐәѥɩԎχÃӷԔ|ĒĴȝϐ',
                },
                {
                    'event_id': 'Ү\x8cōȘƍǣɚǂƆСǼΰĒ\x7f˺áғŇɅ˘ϴҫǟɌ˸ώÍΡÆǙ',
                    'target_id': 'ҧȣĶӻ˖ʜʺ\x81ʖΙʆŔξЩưôξEϦҫӀǗƇġјƸˣ\xa0ҡѝ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'events': [
                {},
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
