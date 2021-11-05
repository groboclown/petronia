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
            'name': 'ŊŋΫІɋȩӯ;ĻƁԁӪĸɃӣĳгʊćпʕϿiɤ˭\u038dҽљȟQ',
            'minimum_version': [
                -5243200123596869651,
                -6820548220818371483,
                -2518006830977843364,
            ],
            'below_version': [
                -306783603073422294,
                -329348142322128420,
                -2507535402725602842,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ˡίȚ',

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
            '$': 'ǔ˺ЪDĠȯΈ\x88ЦϹΊɒƵȑɺưҗÛϪŌ˖˯ΰ"ʳь\x8dӿцԛ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -4957807941675270687,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 733229.7120403007,
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
            '$': '20211104:182045.487265:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -6471222147147027666,
                -5831520851767581768,
                -2208072758240750747,
                4244401440877566205,
                -4032281859208580298,
                -8245514877492547275,
                -9011132774591132483,
                4002709667542109309,
                -3207535566427954887,
                8752461420001081632,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                766333.4250257743,
                330773.16405475273,
                161928.8446734803,
                -74302.80088797238,
                662098.9070245093,
                574435.3723547345,
                704076.381220409,
                396895.2472595248,
                440351.5273934768,
                613964.4549718372,
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
                '20211104:182046.254353:+0000',
                '20211104:182046.272756:+0000',
                '20211104:182046.289832:+0000',
                '20211104:182046.309572:+0000',
                '20211104:182046.326851:+0000',
                '20211104:182046.343456:+0000',
                '20211104:182046.360205:+0000',
                '20211104:182046.378360:+0000',
                '20211104:182046.396039:+0000',
                '20211104:182046.413504:+0000',
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
            'name': 'ХϊʜȺȪŏˆϟĒϺϫ',
            'value': {
                '^': 'string',
                '$': 'ЉĖԚoˆϊ\x92Ԉ÷Ɂљ˝øɽĦÁ\x84{ёҦȀ ԇʴ˷Ȃҋʈѿ˯',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʸ',

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
            'catalog': 'ҐĞԘΙђ˓ȸӞԀŕÍƚĤʫ',
            'message': '@҅ǠȼeљƜ˫фŞ҈ǾŃ\x95ϼг˷ųҚǿØʬɢ®ßǴШɎºΤ',
            'arguments': [
                {
                    'name': 'ǛĺǁʹÈǋ˹a',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        385463.12542919326,
                                        888964.7266218767,
                                        141330.24156212003,
                                        230620.13639428635,
                                        971953.7045537638,
                                        -21811.864137057317,
                                        525305.07323759,
                                        -22461.784478287387,
                                        727076.3835663501,
                                        621188.7439670347,
                                    ],
                        },
                },
                {
                    'name': '˨ЩԧxíӘ\u0379I\x9b×(Ľž˺ʀԢÊI҇ģԎеΘɤęϲüƮ\u038dŇ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20211104:182043.807429:+0000',
                                        '20211104:182043.825484:+0000',
                                        '20211104:182043.842674:+0000',
                                        '20211104:182043.859179:+0000',
                                        '20211104:182043.876002:+0000',
                                        '20211104:182043.894916:+0000',
                                        '20211104:182043.913953:+0000',
                                        '20211104:182043.931872:+0000',
                                        '20211104:182043.949982:+0000',
                                        '20211104:182043.967103:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ϻɓĴ˖І=˺ĆG\x99Ox\u0382',
                    'value': {
                            '^': 'datetime',
                            '$': '20211104:182044.054392:+0000',
                        },
                },
                {
                    'name': 'ŉѕʘ˱ҺʋļƠӡŃĆT\u0382ƻӅЋѶ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        105438.24474450835,
                                        122290.69292841331,
                                        -30365.36036775603,
                                        162490.36650633387,
                                        254633.0090872562,
                                        38838.21249563951,
                                        593606.1230961494,
                                        188017.27979788085,
                                        -64945.74050032982,
                                        925159.4802230119,
                                    ],
                        },
                },
                {
                    'name': 'ˢњEЭvЁÿ',
                    'value': {
                            '^': 'string',
                            '$': 'ŕøʇǭҍҸѢӮȢΦɥŬƇЉäșЊͰ҂ĕŭŋњԓʕĺԥ¤ɚϘ',
                        },
                },
                {
                    'name': '\xadАȷрҫϑˤ´ǗiňǛ˸\x9dϰсӿ£ѣ\x94ΤĶөˏˆυ7ԪĒ˴',
                    'value': {
                            '^': 'datetime',
                            '$': '20211104:182044.437477:+0000',
                        },
                },
                {
                    'name': 'ԫϔ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20211104:182044.507657:+0000',
                                        '20211104:182044.524890:+0000',
                                        '20211104:182044.541813:+0000',
                                        '20211104:182044.558443:+0000',
                                        '20211104:182044.578064:+0000',
                                        '20211104:182044.600049:+0000',
                                        '20211104:182044.622117:+0000',
                                        '20211104:182044.646001:+0000',
                                        '20211104:182044.664620:+0000',
                                        '20211104:182044.681466:+0000',
                                    ],
                        },
                },
                {
                    'name': 'êҌʸȍȏ\x90ʴԑăӋ',
                    'value': {
                            '^': 'float',
                            '$': 129152.68768184201,
                        },
                },
                {
                    'name': 'пΘǯɵҠҶ\x9dʮĻ·˰˚ȂʯϗѨR\u0378҇Ƨ\x98žúӡ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20211104:182044.836709:+0000',
                                        '20211104:182044.854159:+0000',
                                        '20211104:182044.870811:+0000',
                                        '20211104:182044.889705:+0000',
                                        '20211104:182044.911126:+0000',
                                        '20211104:182044.928787:+0000',
                                        '20211104:182044.945789:+0000',
                                        '20211104:182044.962741:+0000',
                                        '20211104:182044.979660:+0000',
                                        '20211104:182044.995992:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ΠӀԓʟΗƛåЁάϿҬĹЦ\x9dț·ĤÏŸΨӰѦ^Ⱥê?˙˺фϏ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ʊȁ',

            'message': 'Ȑ',

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
            'identifier': 'ʣǁö]ΜŮƏİСǖT8еǘʏŦҽEηԘ҈Ǟɱɴvͺǽ˼ůƓ',
            'categories': [
                'internal',
                'configuration',
                'access-restriction',
                'configuration',
                'file',
                'internal',
                'invalid-user-action',
                'os',
                'configuration',
                'access-restriction',
            ],
            'source': 'Ġ¢ΝÞЙ]đȽЋ\x87τǑ$ӉщŚˆǀŋӆӧŸџЦӒӲԍϰФϨ',
            'messages': [
                {
                    'catalog': '˩ҠˣʒʹϷɡԗ¿CǁΡǱʡϺ҂˗ǹΑƆ\xa0Ҁ͵ø\u0382ћǣϯӿ˪',
                    'message': 'êз?˅Ϸӄ\x9e˳˟ɴ§ͼɯϡȏĿɺ¿œ˽\u038dʩǫыǀ©ėyҵȤ',
                    'arguments': [
                            {
                                        'name': 'Ơ͵ƢķsӴҴЭьɈįҔȹЉϰĞΜЉYӥĚɿԏčÌUʁŇЁɏ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            983612.0956236674,
                                                                            514058.6779227911,
                                                                            740897.3070501725,
                                                                            744835.1361573911,
                                                                            394268.1340615083,
                                                                            871377.1856916689,
                                                                            917918.8248525896,
                                                                            552245.9816568467,
                                                                            179394.51909555652,
                                                                            796625.9813124874,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԈїǕŹÇӵǴ<ͻǣіʽ²·ˈ\x82ÁĶǑΑҨԈоϚΥѾęҬmł',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4632990560134811192,
                                                    },
                                    },
                            {
                                        'name': 'ԣľ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 713511.7221149403,
                                                    },
                                    },
                            {
                                        'name': 'ĹКɃҏфӜΕη·˝Ԋĥ¼ɀȆ%εӼŖȆÕǉƏԅΚŎʾɫłƾ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -63726.96725235988,
                                                    },
                                    },
                            {
                                        'name': 'Ǔ҄ΧƦƚȰàʺ\x80',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȼӋƛŧόβîʪơŔɏȴȜBҞ˃Âýϖŀʯѷ\x88ɓ\x8bϪó\x91ʲɅ',
                                                    },
                                    },
                            {
                                        'name': '\x9c¶ԆЀƬ+Ɖζ҃ûιǯϸӃŬ\x84ĞǔѮЫζøғ\x86˦қķƎČʎ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ͼЫWьĂн ȯӹԔǶϗӑƉϜѴŸÀӫӕӣˈөƥԃξŖ[ŭ˫',
                                                    },
                                    },
                            {
                                        'name': 'ʁ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҺҀӂҐ˯ͲìƍάʬƶҷѳɀÀψüΑѕƧǾɫøŜȓŲĒɔ\u0383ў',
                    'message': '˴ԕόΗњӲҝˀʊѺΆÙφӬǺϘ&ѓƌίƬ¼ĹʵϧƄÍЬkƬ',
                    'arguments': [
                            {
                                        'name': ';Ӕ\x97tʽd\u0380ϫˡϰĦϡÆԀȋkŷԂŵċĖϐЪмġ\x90ƧƢɢӌ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'OӻкĢЖʜɵŢӨӆ˰ёǠʳʼбÿˌŚğˋɹűѓнƶσŚ\x8bЇ',
                                                    },
                                    },
                            {
                                        'name': 'ĖX§',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 760332.281377468,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԟ˳»ɞΔРаPµƐȐӿηӛůʽΦѱԇОҼŸλʎȯǺӮćЛɟ',
                    'message': 'yȋưωȮǳԭǞŸ˛ҟϊʩіɐωϦ˙˖ʝ:ұÎ҂ǣTРȈΐG',
                    'arguments': [
                            {
                                        'name': 'Ƚ×ȳ\x90ȻѧФЊƧΣԐҸƖ\x81˧ʜҶΎѢʌ»',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5261935822047915909,
                                                    },
                                    },
                            {
                                        'name': 'ˤśѐчӡ҈ИјɑжɡϡvχҩН',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ǉĻJsԮǑİŗȡϑäÉˮӂ]ŰҼɭɀʧѨƵu',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -183212147623408863,
                                                                            -4362409994985886692,
                                                                            -6026235652693791253,
                                                                            4443307389079163805,
                                                                            -2737194760188980341,
                                                                            -2125219933271418357,
                                                                            1049032695657366129,
                                                                            8686981189325902663,
                                                                            -8006300718345362349,
                                                                            2602474584159019058,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÄlƶӍӲĂǿŜʫαθʭқҎ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 249813.87064164074,
                                                    },
                                    },
                            {
                                        'name': 'ŦŁӖƣoЀǨӋӓhłŪˌɴbƆϷɪ˪ǿԬȂŰÇ?©ȘϺюѝ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '\x90φÔȖlˇҒɦЀǴҙnʴЙÛΫNЁ¼ӷƀĚ¡˰·ҏбͽӂԍ',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƿǝʄȄΒԪĆѐӿȆ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 694356.1951297749,
                                                    },
                                    },
                            {
                                        'name': 'ɞӹħɫ,ʟѻ͵ӣŤϯ\x96áÜ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7270622388963633609,
                                                    },
                                    },
                            {
                                        'name': 'Ɠõ\x8căiȢāȶʲҕñǵ\x8dξ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6735318467334995565,
                                                                            -1499546587185218171,
                                                                            -6504238777962258137,
                                                                            5815456077875126293,
                                                                            -6740840816585547101,
                                                                            3084257553050810854,
                                                                            221489195352712331,
                                                                            986122370711507111,
                                                                            -8145065637717598461,
                                                                            -2414410420478269936,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ùʝ¶ʇ˜[Ѕ\u0380ɢɴӦ£ʢʭςѸϸхϲȐ҇ѓųýŃǖȍŢρĂ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:182032.334274:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'С\u0383ɪ\x84ѣ\x9dȣħÏԗҹʵϿ¶ŹǇ¦ӚʛΣĲzҩӣϗȶɸϸǤҔ',
                    'message': 'Ƒ\x9dɉŖлӦO˥г6żɚʟǰѩȻȫΕЅ\x9fĺ˅ңŐǖˉʙȴфÅ',
                    'arguments': [
                            {
                                        'name': '\u038b',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            84034.74660265946,
                                                                            419151.6142946484,
                                                                            897447.8443000993,
                                                                            220923.83041141182,
                                                                            593003.4783330087,
                                                                            557303.4984741673,
                                                                            412481.7836644097,
                                                                            324820.25283610343,
                                                                            182897.65109417576,
                                                                            414050.6261470433,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȿЗ\\\xad\u0379ςǡΞÚʃү˸ØԞċĬʥΓΘȼσɔ˧ӭϥ&αˍԠi',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
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
                                        'name': 'ĺɁȈªǺBƕzM@ʂμB\x96ưǨD',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ɽϾ¾϶ӿϫԘВˎ'\x81ÌZ",
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            20975.2303228402,
                                                                            654808.6974374658,
                                                                            550138.2836333106,
                                                                            -39281.49694692606,
                                                                            578835.5282028565,
                                                                            690611.08883826,
                                                                            579261.517198936,
                                                                            680432.8453897296,
                                                                            830626.1440510335,
                                                                            528294.7187892477,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʋĭ',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʰӽȪԜ˜ʜ&NӥťȴΚ˽θк҉ȢԖXǻӻҩȰƥȠǵE\x9b¸',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϦΌԁΉɿА˰ζȁҿӏ¼ʦć˾˩ӛțӦŲњѳȃ͵ʉĲͺ҆´T',
                                                    },
                                    },
                            {
                                        'name': 'Ò˺C˩\x89ЫҶӟǛtԙԛƯ)5ɳŦ&2ǋАĳ˸џέϽȳ\x86ʧψ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 845602.4485885674,
                                                    },
                                    },
                            {
                                        'name': 'Ɇĩɿ¨ʄʋЂЦЙӒ\x7fÿҗЌȦѫƯҸǠƺĉԭȏДΉҺЍɬÊŲ',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĸȲʘŷƼƼїĄĈө¥ʵɅǼѐҧ¨ŻʀҮ¸ȩϢҖΣӤѝҶϽœ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʛˎǘn\x96ƮʎɥВȦǰŸЈɑʘÂʓjmбŧϚ˓rȸȔ®rɚГ',
                                                    },
                                    },
                            {
                                        'name': 'ѬœʾЁșƐǹšìϤϪɂчǒӈ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182034.166920:+0000',
                                                                            '20211104:182034.183216:+0000',
                                                                            '20211104:182034.200888:+0000',
                                                                            '20211104:182034.223366:+0000',
                                                                            '20211104:182034.246610:+0000',
                                                                            '20211104:182034.269192:+0000',
                                                                            '20211104:182034.290323:+0000',
                                                                            '20211104:182034.310487:+0000',
                                                                            '20211104:182034.330823:+0000',
                                                                            '20211104:182034.353518:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƋÔUЛҿʃϑήȒʏɅƔ\x9bҼŇØʕɈЛ5*ґľȢʿĞ\\āɦƷ',
                    'message': ':qγҢÓѹȺϋӝ¨éǒɹʹǸΝϟфͿҲˆ\x85ŔǖãʌģϙҤã',
                    'arguments': [
                            {
                                        'name': 'ΌǬƊΩòŗúш^ϩǎʅAÇȗϚDĞгŵ¦«ǛЙЋɦŰҐǈ\\',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7888838124448817314,
                                                    },
                                    },
                            {
                                        'name': 'ȫˈɀџśƽTӶɠόŘéʻ\x91;ûȽҨÂʎЎϷ\x89ѵƹωͲ\x87˄ӂ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 170488.5619211988,
                                                    },
                                    },
                            {
                                        'name': 'ȜL',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 825998.1992198852,
                                                    },
                                    },
                            {
                                        'name': 'ĈζŗӸюǮıĔÖȠĕʬӐΉ\x85ĞҏҁƤxκ#ёĢ҉\u0378İͼưɨ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'lțоŇ#\x9aɯԟǊƼοʾhΛФҢԝͻʂ<OЈВϗƉ"ΑǮĈʧ',
                                                                            'Ȉ¾ҙР,ɡгzѕҋϫʇÞƬƤĽӈӓτϩϧщέ¤ΤŲ˳ǃ5ѭ',
                                                                            'ʱ\u0383ǏǣƐӄēʼňεЫ6ĎȃČҼˏȜêÝǃρʳȘ\x9cjš˩ʫү',
                                                                            'ǽʀȽǶ8Ɂ5͵Ǩ´ɚɨɎԧºΟԑƤΓķ΄ԥȗњǎҳԓӂҋӇ',
                                                                            'ȳǙӽMúƷѹʛêѣҿBœǌɁ ҍʹȈ˥ŕΔɲ˳ЩǙƟ?0Ү',
                                                                            '˴8ԁȖǬȦɱӊ{ѡűƱŤȁԤӓȾ˦Eί\x9eͼʻӀʥԆĞǡΉ\x7f',
                                                                            'âȬʣd\x98ӂʇzҮÞϻȎ\x90ʍѝźƜԆʡԢÖǘϜƝʒе]ɚ\x9dˊ',
                                                                            'Κ\x92ʅҕŮĨŇ\x90\x8eϞаӴĿȍˇϓp¦YĂOȓӦӚиyқǨĄҙ',
                                                                            'ĆҡŷЊñŤúϒЗӉȵƈà·ΨɉФVϑˮǛԙbócŶǳΚӗЋ',
                                                                            'ԍԓԥЍ0\x90Ŷȫ·ί½ʛуѱʂѐΎÎƀΨ¶ŊȱҔΧŘɵƙǽŁ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '6Ēԑ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                                        'name': 'ȨʃĤʨЖįӬǖƅgӆ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3026968099596472523,
                                                    },
                                    },
                            {
                                        'name': 'ˉĮĳнǾƭҪŋǿЂ˓UџīɢǗ҅ŐЬ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Гƀ\x9bİŉơΓӀҡŢˠϑ[ɱȐӪƸΰˣƁΔů҉ԨÅ~ҟ\u03a2ɫΕ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϖdĢ˛҂ǀ˷ŹЖǓ˚ЗΙџ˲Ƒˆіʹĉ˽ӟ˱ȯɘʧǪӽ½Ө',
                                                                            'ԖҘȲԖ˪˪ӆȵƜ҆ѴÜȒȋ\x8d¢ѣ\xa0ʯǇӐԐɬИȩɰǡά\u0382Ԁ',
                                                                            'θѻȄʼůƚ΄ԚѹқԔԇʾî¼àʭӽť\x9aϩӇĀΡzȊĂǆӫү',
                                                                            'ϜӝÿɬƃΎԑӨҪǈӘ)ӘԒƔH˺όlόĬγ~ĺζА\x9dϴŴȂ',
                                                                            'Ƶ5ȊҸΟғ\x84˦Ԉ҉Æ\x8cͱ\u0381t3{υ˾ԮŀǉЋǎǷϤΜƞƺʛ',
                                                                            'ъĠΟЍԐĺʹźƩιήӆǷѵκɌкzΜđџĈɡԫӶʝĔіȊƽ',
                                                                            'Тϴλ˸İȴϱѿҕƥЪҡԅĚʈ҆ǺԫʣũȀє\x96ŲͳʗgМŜŒ',
                                                                            'ѡЇЃ˂ʅi\u0381αǢԩŧɗƚȨПԓυÍŷЦɋʧ\x9fĪ[˱ˇŸūó',
                                                                            'ɩӱÙƘͷɌѶdƛŲԖȟ΄ЖӁЩ˰ȸ\u0378͵Ͱ$ћǂѦɖÉŬЁE',
                                                                            '\x92ǮЭ\u038dˡGƪ)Iδƈ]ïҶΎӥҬʘĢƍϕTҫ:΄ǻȏ϶ōτ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '͵ʣŕѫЯоԀȩԑȚ*ýƌȈьЌ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'iϺвЎȅӾϤЯİxƓϥĎӪѬÌЏˆԏѨȿǎ\x90ҰӈýǩĿÛʆ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            243905.0285101051,
                                                                            97107.94634091397,
                                                                            889684.6519464318,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'υϙѢΖʣμΆµБʔʃщ×ƨΫδЕӌƌûԅ҂mϟė˔˲ԦǑƗ',
                    'message': 'Ľ«ʙžӠǶΝԣſТƢΕȏŃɡhȩɷ¡Ȇ\x82˵ЛüτϔϨπƋʔ',
                    'arguments': [
                            {
                                        'name': 'ŒЖԍɼ¯˕͵L®ϦӍȕҌҡǽМʦéȊǀ˨Ȼåˢû\x88ɡėǜÂ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            383748.08806033374,
                                                                            479334.02592020994,
                                                                            776568.1493265544,
                                                                            416493.92783485644,
                                                                            575768.9670094867,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˘ĵ˂ɠкƊmřщĐɅ&]ɬÌѮοѿеjŌ\x9b(ÁĿ\x96ë*ǋӃ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\u0383Ǣ˨Úуb°ѐȽҲνͺΜұ˜ԑŎ½ҲņŅƚǎцɲЊǾĝϜˑ',
                                                                            '»ƤҟǺööʓ˾ÊԇλґӫЏĶσҬÊżȰЃ҄җŦҩ΄ίǥЕ˘',
                                                                            "ǦġΧrϟ±¡'ʑǟНҮϚԟǞ\x98БŹ&ǶҀĉĞbÕϺŦ˓ǢЉ",
                                                                            '³ĥ\u0379ŷ˲ǭΘѨ϶ҙ˭¤¼ǿǔƎ5Ⱥ}ӼӦDϩԈϪyİϩ\x92Å',
                                                                            '>ӆҨ˼ĄɾǈЁζƴήƴџχɮҗȷƍƮάĿӇҪȯŔƍͺ˰Ĳϓ',
                                                                            'ȷĦӄͶɥɿҤ¹ƩǓuñәȪӇƌȐϨSp#ɊʃɰşσǪȣћf',
                                                                            'Ⱦ\u038dąǛЧ³ƵÎ{ɗȴΫÖʟĚŇúїģƭĽҸćМɜȉǛƟҤȧ',
                                                                            '{ĕԊЛЯʲβɮīȸʝʭĒϦŉǣ¦áϦǁ\x84Ď\u0382ÔǭԦу΅ʑŅ',
                                                                            '˽ɤȹӃπЯΛÎʀЯƇĨѦӺƛԓѶңǷҞªǙ^ʱǉGҀɎʮϠ',
                                                                            '¤ʉƲFƦń\x8fҸ¯ŕԊÊɍʾӡ˷ϨēΏȀˀɉɻƋ²ϥŐѴѾў',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӡq˪ϗǉфҞm$ҍģԞŉĄAƒӲǳҎԠŞ҆Їϡ˞ʹȳæʠǭ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 762609.1354412211,
                                                    },
                                    },
                            {
                                        'name': 'ҳαƽÌҝҮăӻҔԇǜʂӫΜŘЪɧүƛÿұ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5589206538363397977,
                                                                            3936245200097003518,
                                                                            7290298210198581670,
                                                                            -4185403857632525681,
                                                                            1251608939839526797,
                                                                            427179699896730555,
                                                                            -855820812415400654,
                                                                            7747399503807046542,
                                                                            1068521229645693938,
                                                                            -4955388525649635077,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'WХŘ\x96ʉϤԭ%ύͶâťҩȴӯҨĘԄӾύ,Õŕ\xadɋˬ§ҩҿӾ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182036.758898:+0000',
                                                                            '20211104:182036.775539:+0000',
                                                                            '20211104:182036.792170:+0000',
                                                                            '20211104:182036.808751:+0000',
                                                                            '20211104:182036.826102:+0000',
                                                                            '20211104:182036.842889:+0000',
                                                                            '20211104:182036.859352:+0000',
                                                                            '20211104:182036.878268:+0000',
                                                                            '20211104:182036.895479:+0000',
                                                                            '20211104:182036.913657:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϬBXϪΛЄŧbWǓǥϰŕʝƘҕşĨ͵ӟҜΌȓЇӫБЁ΄Ыã',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8599392217733098781,
                                                    },
                                    },
                            {
                                        'name': 'ѻɦ!҅ȣP',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϟԠ҉ɋ¶ѦǰΑóǂnǥѕЬɾѮðԄ˽Ӳ҄~ÆŒŉԞҭĨҩ²',
                                                    },
                                    },
                            {
                                        'name': 'NˡƶΡɔнņőU\u038bƋѽҋǭ˷©ϳĜĚļ\x96ưѩЫԃϥҙǰґȢ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ҟҀ«˜\x94Ί\x8aɄſ«ȟҥ$<ϫԑĿľǑӤӚ2Ο\x9bſʘ#ŵҏ˵',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 286720.617223031,
                                                    },
                                    },
                            {
                                        'name': 'ʗțԭˌʋΦʛ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182037.474820:+0000',
                                                                            '20211104:182037.498213:+0000',
                                                                            '20211104:182037.516911:+0000',
                                                                            '20211104:182037.533391:+0000',
                                                                            '20211104:182037.549766:+0000',
                                                                            '20211104:182037.566251:+0000',
                                                                            '20211104:182037.583926:+0000',
                                                                            '20211104:182037.600807:+0000',
                                                                            '20211104:182037.617724:+0000',
                                                                            '20211104:182037.634151:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҘѱʋɏΥ\x7fɫȚΫγЏ҂ӣΚ7ӈƆξżǵӸϙ\xa0ʌʺԙϽɭXÝ',
                    'message': 'ȿӻŶ\u0381śċϗʐϛӞ҇ҥǑѳɛʏеMÇΖnҁԬƦĿ\x8aƵ$ͲΊ',
                    'arguments': [
                            {
                                        'name': 'VŲӍѳȀϥШӃɗ˓\x83ǴɅʴµȨϏĊӜǙʼϫҞĎǨAŧ½θ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 769858.5056286213,
                                                    },
                                    },
                            {
                                        'name': 'ԑcϬŝѬ,к˒˜ͺǲƪ\u0379ɆΛϙŤԊқíǮΞЀȐ\x88˖ʛƫˋΥ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ĤơˁĹĜɝȮчƝϜ\x83ε<¾łɜоɑƥѶпΓmǞɅǤƳ϶\x9dL',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'õșɈɼԮƐѸǜɊeŽʳ\u0381ҊȐωǃß˗ʲӎOɳԓϚ¤SԛɇȬ',
                                                                            'č˭ĈХ\x90źɴŏʃƴѺӽþÂԉÇjðѵƙǡρ˞Ȟ\x9eȰΑ˭Б2',
                                                                            'ȅԊҠǏȗ9ŁFÍǰƃˤqԮЖΩȁ¢ʣƎʍѢźǆvƮѓαЕǸ',
                                                                            '˂ʕͳčNϗүʏҖʭŇŋΌʞh˭ʃңŎƌűΆҼʗҘΗˣǱͻǂ',
                                                                            'ŌҵǉÍæĦɠӚ˂ѶΒӇȳƏЩ\x9eǳϓҦȾӧҿ͵ĤqɄRХǠh',
                                                                            'ЉȗʠЮіʹ\x80Ʃʂ®ӻƲ҈ǛţƗѪ͵éˍ˴ҵˡʐŪɥ҇ӰɘɊ',
                                                                            'ǂЩѧИӫőŎǣьӅ)ǠæЖәàdӬҼΥˉȳԞӐɘPĥī˂é',
                                                                            'ʲǾѠɐΠŖrϰ²И\x86ğJĈ[KŶïϦãӫҽȶ\x8bǅ\u0380˴\x9fͽ!',
                                                                            'ĜэǇ\x80ɇπϧëÏ¹ǍƢҍģ˄}ƾĸʑСȯκӇЃΡŪ]\x9e3Ĥ',
                                                                            'ƏʹˏЃʷĦŜѼkǉMҷԊѾǳԡЗЍϤώԇȪѦόИЗΣʼЩŰ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƷɈ˲ҠϢˆȮâɃΎȎȷǒЎƉƛϦǭǵɕ҉ӉȤĤ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӱĜԚȢĠ˲ϖÅԈȲǮǳđaɲǐґǄΟɟεǦҍ>ÁͳêԘΘӖ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɮԐРǵBΐĞԂѪѦʷȢƘ6эͿѱʃȒӘƷÌȹɬѕů\x86ҽˉ˂',
                                                    },
                                    },
                            {
                                        'name': 'ǗџωԧEͲύɂϏGǙȨʚҎ\x8cʹ˄˚ȹɱϱɩ˷-ӑŚÊČȈļ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -845697108059814883,
                                                    },
                                    },
                            {
                                        'name': "ӼǹƎŔԓƗŨԃќƿвɀÉɰе˾'ъѢŕǟ",
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            327016.8122192388,
                                                                            661545.6060319999,
                                                                            978803.471629983,
                                                                            153772.8997734736,
                                                                            739521.3793739586,
                                                                            62055.26336337952,
                                                                            945189.8042126984,
                                                                            456824.3017379538,
                                                                            28545.118213124573,
                                                                            156448.13116209806,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ěƜȑϞϹϩćҟ³ӣª',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7014157467661895535,
                                                    },
                                    },
                            {
                                        'name': 'ϥɵˤϰɰȇΚŎʁӊűǻʐƚˌ*ĩʩЌǚRpԥӣÊϠɨŕ˄ɰ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            79412.12226083424,
                                                                            187510.05217778846,
                                                                            317016.4780295735,
                                                                            328985.90996856824,
                                                                            517989.679405818,
                                                                            382239.1675977188,
                                                                            135827.92497063667,
                                                                            -69094.3602857403,
                                                                            246973.91714648687,
                                                                            380932.5447971309,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'чƞ,',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϐЎĆʵˍşåӵ®ųǃǻϫˇӚѩƥ\\ϭ\x98ēЍzʁɽ©ʌƋΠӭ',
                    'message': 'Ɣϼώ5ΜɚʧʆʡʿыėѼ0ƋˢöÉʀϓ\\ȈÀ҉GҭγԫĀŹ',
                    'arguments': [
                            {
                                        'name': 'Ùщ˵ӻαŏԥҹˮǴ\x95ř҇ӿǰӎРԜσц\x94ΞӦDϜȮç',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8078917831355364066,
                                                                            5481053038532260986,
                                                                            2444137133846519010,
                                                                            -1867264582088566735,
                                                                            -161437679721131536,
                                                                            -2530084131497685297,
                                                                            3051658150177160592,
                                                                            -8479498618771713443,
                                                                            -8001352914511955690,
                                                                            6590076963328325855,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ЋӔЅơѭ˲Ҭ\u0382ɃξÿѳȜѣ'YЗǠς˺ӧͶёǭˋʐ",
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4341665862048907467,
                                                    },
                                    },
                            {
                                        'name': 'ƅˡďӵѱÎĄğǐͷӕǏгș˽Bč\x7f҃ɧ}ȈēԋėȎŵǱɖӹ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:182039.583337:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʹĜ˒ʨ\u038dǖʔÜǳIʘƱ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7552050940005619495,
                                                                            687174534735555191,
                                                                            -219140829275680589,
                                                                            6229721754659272797,
                                                                            6318463492926533020,
                                                                            1567196413384585487,
                                                                            3674043743499928447,
                                                                            4811251175064425293,
                                                                            3921774205282582211,
                                                                            -8001936477189825157,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ύʌёƪқӄʩȝùėɞʛŲοɔd',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': 'ƯйĖƊºŐąќů',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 758678.0076944855,
                                                    },
                                    },
                            {
                                        'name': 'ŕ˦ʢѝȄϹǞаȆ˶ǃǁŚǋӰś˾ԒŃoŀ\x87ÕřБǬ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7988465646783469604,
                                                    },
                                    },
                            {
                                        'name': "Ғʢʅ²ʍnГwˣҿ˯ҰxˡαƼg'˯5ÜλӉѢȩӽÕüŮј",
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7607708823275303629,
                                                    },
                                    },
                            {
                                        'name': 'Ә˶Ѵǯí˴ӱѳ\x99ȇ;Ρ¢ӵMǝҰϩo^1ќśҧ£ДԔǒеԓ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3775415454484349974,
                                                                            -791826776829688585,
                                                                            -8044094293729727492,
                                                                            8118868822595709817,
                                                                            -8753489069495371363,
                                                                            -466895993962253438,
                                                                            4174003988619465602,
                                                                            -1759842051882019656,
                                                                            -6731806468161033662,
                                                                            -1258332115413252571,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʻӄ\\ʷͿÑýȰʁGÕɆġТŕĩϑȱʶǓxĺǡԌ˅ϑόЁßʳ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȐΌ$Ң¦ȩŕӯҀɿϬʛŞЈ˪\x99ѥΆғɀSȜǱԮLiŖ0͵Ѯ',
                                                                            '˓ъƎǑέíΤˈȾӂԞІ¥җѹşϠʲԇ*ˑȸ«ΗŒ´ԠbÜʒ',
                                                                            'ͳ˚ξһĈǠϳϐҺӥʘWÐiǊŪMԠƂˆϚӃƽèʆģЕЅөƶ',
                                                                            'wιʆȕ˨ϟȿ1ƥſıԌǏʉʲǔιŒƉɓҩˌɨϔğȍņ\x91Ĥł',
                                                                            'њӶ\x9e΅KĠĬѴ\xadΫϽuĝĿҎЋҗɕ\u0382Ӡ˜ȅԦǎƪźԅÚΖӃ',
                                                                            '˺ƗǍ\x8cȻǊſсӳʁϏǨƿήNʨԩĮƾɁ©ɈΛ҆ΒԡҤŕќ\xa0',
                                                                            '[ѹƚӢɪύƇҙ\x87ƝѾɩ\x93ΙӦǁƀǯǯϧƚȈКÁ²ɲɭʙϖϓ',
                                                                            'Ө҉ųΔηљŤʹǰƣœ\u0383ʀΔНǘьˠҬ˞Ĳ®ɉØ\u038dҘʔѡϮO',
                                                                            'ʵ˕ѾíŉЗЍҺƙWʓòϷΖwӊԏʭǣɀɂеʽ˶ʳ$Čľԏʋ',
                                                                            'ƨҦ˸χϭъӟX϶РƅҘӁȲϒǁъϫĹëɋɵЌӿ˕ƈ˸ӄяĸ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΛŨМϓɠԪĴ˵ԉŀƿʊȍѵԅAŚѴũѨêАȇŊɘϰһ˄ʍ˭',
                    'message': 'ԨԝđҲƇĪʰɚѪƤÜȯÖʹПȚiƈ|×ʉȘӕӚÛĞŜˏǥǹ',
                    'arguments': [
                            {
                                        'name': '·\x80ȽԁǬέԠĦѦҾ\x95ɗgĹԉ˝ψԀ1ĜǙǺ΅ѾßΚƟsаͱ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʱӓӥĐ¡ԟчô_Ӛ\u0378СpыcҘҭÈ҂Q҅ɇɄʔàiφǔʛƉ',
                                                                            'Ɵ˘\u0380υЌěгwŏŴþ®ήȰҩdԁԣІǅúҺȥЬ\x91Ӷ˩ʙʯȷ',
                                                                            "ſżԄͺӮɸ¤Væʓ¦'QҖΙҍƲ³ˊȣʩғԞηůǱԪ\x9a˔\x90",
                                                                            'ФƦЃ]ƢDаɺ«ȿ˓ΤtйņԡƌHʊɝʳŎ\xadϪɏȉƽȐäԑ',
                                                                            'ɟѕҧƥϐē½ӊ:ǐDԉʖ\x94zԋʘϰļǀϸȁɄʌÈǃӾҭɖЙ',
                                                                            'ɌʝȵŶζ˫ϺӡӃʩƻΑǩӸĊϋήϟѭēǉ+˱ЀԄ\u0381ѶВSԜ',
                                                                            'ǴʹɩгӃϠǜRʦˤŕѓАȃʜɝa\x9bȈӏǐ\u0382\x90ǔĘѾМɖМɗ',
                                                                            'ɸяŏɭϛʑȍЅŘǟЁŭǻǱķ¿¡ϳφʇϊǃï]җVɐľțƭ',
                                                                            'ԣЏ_Ï·H÷ȺΟǺʿ\u0381uǟʲKԒϾ£ƴ\x88ƅĀҰзRÇԡɇô',
                                                                            'ȷПüǢӂ҅жêhǠȊ³ύĕԑȶͱʧƹͻɽ\x95ȉȑȤʉȂɫ˧Ň',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'įҝʠϋɱʖӲƓӧЁƞȢ\x87Ɠһ\u038bѹɂːК÷|đnʿѹӽάFǄ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԎˀåѻӴ3ΫSŞ˨ŠĈóxӳnȹϋˣϴ7\xa0\x87Xԋ&ЍӼɋҮ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'єŜćԊв`ǦŬϤϴǤĸʸŴƇ˳Ӭ҂˶ΉäȂĹӈ8ŘԏļЩҚ',
                                                    },
                                    },
                            {
                                        'name': 'ˮΏĻГŻγǌĳŇńŁčΥ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Гƣõ΄ӃɌèЦɀŨӽʅӢԋvѽ˾ÒĈśǺ˒\x92ǹȠʲɯLťҞ',
                                                                            'qԎŔνқɆ9ӗșϻΝĎԓϊӠɳˋɦѤȣΌƚԍƺσɨˍгLÖ',
                                                                            'Ŀ˼Ԡӿӏ9ϥǩѶǔӵɇВƜӹơțǟϊςеβͽ-Ԃ¸Çǅξζ',
                                                                            'łѳȩľʻƴӕϩŌʃ»Ӻ´?¥ϑԧƛ={ƘmcңЀ˄ӘÚůŢ',
                                                                            'ʝɨʭ\x8aÀŠȾԔӘŻȸéϹùƿ˸ϩɽʄˤĝ{ψɐņΜɚŚE˼',
                                                                            'ѻЇʶɁŸϔӹǻӽпƴǽϙȀɛԙˮԔο҆ӴҠӣʕУ6˂Æǟи',
                                                                            'êѳɮċžѼʓƓɜɽƠŚ<ϐ\x95ӘßӵϥѳΡĽÜԫgѝÝǔЯͿ',
                                                                            'ӟӃί\x85ɲǍGњЩŰb!îȄſҟŦϴȑҙ$ΚЯυǽԦ˳ŏȡ|',
                                                                            'ѼĻɅϤϔͲԋԢѭƷѐǀˎӣąǑӭЅѨȧѸ˂\x86ȍǘΚqȾCȫ',
                                                                            'ӰƸԕŕѓǌͰĢzȬ}ħϒa\xadɺǵѷȞɲψτӜдGњњʅǙж',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ĕѳmǫ%ìʂĸӟҡϹӿɗ˟ЛĶƩёŢĚѺ\x8fǆŭεғӛʨўϸ',
                    'message': 'ȗΕơȢЖѪΒŗԖŻɊЗʖȧϢÐǞ˹ͻLҸζƉӐҲӐВԖ{1',
                    'arguments': [
                            {
                                        'name': 'иåȨĀÙѡ¯Űˣ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            138610.16717459686,
                                                                            681034.9368107822,
                                                                            919916.4936277618,
                                                                            224489.9326898781,
                                                                            162936.83737056598,
                                                                            514021.1300596682,
                                                                            193158.25031703385,
                                                                            667995.290991709,
                                                                            -15033.973048388521,
                                                                            289959.2229489943,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϵҦέˊ-ƠьӅřǩ²ĤЫȩšIeȐf\x82',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 647095.7007890346,
                                                    },
                                    },
                            {
                                        'name': 'ӆҘΡʨʮ˗ɰҠƀʉσȤҚԃӅҾԔɞƺˡǀÊnŮɉˣʗӒ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 360926265660882432,
                                                    },
                                    },
                            {
                                        'name': 'ØӍʩĒэŌӤͰσɲĪěǏȊʼĆ\\б\x94ˍϘͱÖøήĳȌWŧ¿',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8645470924327074181,
                                                                            -8534463324784853626,
                                                                            -4583548746890278702,
                                                                            -8615411563565969851,
                                                                            -3945371299904672893,
                                                                            4130341191182094280,
                                                                            -735989487598637621,
                                                                            8976258039230358176,
                                                                            949392291974763196,
                                                                            -3893593960463168100,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŅÇҪҘЃĹȒƭˌ˸ğʟҰâY<ș¬6ʣϹѾ=҄ӀҞԃҚëΖ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:182042.343636:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԡνѭēθĆѡIȰŖВƿԆŃj',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -16272.207794615533,
                                                                            623866.9658943316,
                                                                            555384.295914715,
                                                                            991440.3606820719,
                                                                            831470.9236723382,
                                                                            391901.03871304623,
                                                                            724958.743172687,
                                                                            769647.248461185,
                                                                            559649.1163529173,
                                                                            193839.02875153697,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ďЕɝȫԤőȑƫӘ_ʥʡʸʓӾғсǹƮҤʄȐçŤɷĎӛΙ˹˞',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
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
                                        'name': 'ǗԋѭϽ³ȚӂѲ˗ӔϻԁԎʓǂɅκ˺ϽЌ҃ʓӍ,ΕȪ)wʹŘ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:182042.928666:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʭʹϝϞOƽˀҁϢϾҀ\\ŬȰʤʉvQ<ȜлÊƟ\xa0ƙεżъʻå',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3822669949733077803,
                                                                            -4859705800211341800,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǨŻҭŷʣǾ\x9eɈҕЎʹӦʭčеʈŮ{ШԣӽǷ#Ԉǲˮ҉Јȵq',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            23754.142350745416,
                                                                            785509.9078657823,
                                                                            385801.3611250231,
                                                                            692694.2863506319,
                                                                            520273.05605186184,
                                                                            536472.1442450477,
                                                                            366938.032877283,
                                                                            793158.1269626443,
                                                                            513700.3404566926,
                                                                            31618.67845911358,
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

            'identifier': 'ˆ¬Ȝ¸ĵ',

            'categories': [
                'configuration',
            ],

            'messages': [
                {
                    'catalog': '¨ư',
                    'message': 'π',
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
            'name': 'áÝ3ȁċЛԝȶΪǬ\u038bԒʞɄϗВō˹ǺýŃĝ^ѓǯϔžɪΌŵ',
            'error': {
                'identifier': 'Є\x8dәʢŎԒȾȏʓÝȒ§җӫʿÐҙȟԉĶ5ƵƑĕӨȅŊЙRǫ',
                'categories': [
                    'access-restriction',
                    'configuration',
                    'internal',
                    'file',
                    'os',
                    'invalid-user-action',
                    'internal',
                    'file',
                    'os',
                    'file',
                ],
                'source': 'сǢ˔ƶťҵƳχΩçЃJţƞĩӹFѾ\x92яȻǼӲǕóӯƆѨƊʁ',
                'messages': [
                    {
                            'catalog': 'ėΠ$ӵʹɽϩǻǗƳʎӉƥƖšíЬϬΓȵԟѰɼűǌîNǪƫѕ',
                            'message': 'ȞΘɚʳŬҀϩєŮЦɳҎҽˢьϳΓĞ\x88ŠβŇǮˮГǧŢ˹ʻǒ',
                            'arguments': [
                                        {
                                                        'name': 'ѽŠΤΌҵ\x92ȝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ūшʀ\x8dϚӻԜЬʌ%$ǡҰʦѭϨɂɢɹɍШʮǏ\u0378ʶϧц˚kЮ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182025.447928:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '.ЇjǼФ˾jŇԐѱȗδһѠˮϼʚӘϡĞʽ^Ų˄ɤΟÙВcӟ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƷóЮǯԥǜnѳѦ\x84ƜƹȸÃ²ÿԈĜðѫ±ҟ˰ѶѡˋMοΪж',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɺ4ʦ[ѧĈ\x9aƟƍɠɊʙɂӃéӒĐƵVѴRȶʑύǽ˚',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϠСӻΙĆǴӑςͰїǿԋϩЫ.ЮǉҏǴǒӖŭûìǆˈ˧ʠϿU',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɿϬʯъΈГʢԑˌӒ->˨Ҹȓx¦ŋҁɓ§ȊĕɖʴϮѠȇϴќ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'w\x84ψєŜɤѺÁGǲ˔',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɺγёűĲӜ˶ҶƫҨˇҾňτáɂӲÉîʛƟν¹ЊρʗǼΛʋԨ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182025.855811:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '?Ȝб϶əҋƙQ=ɚӾzˑǇԋƊɎňTӅAƶǜ\u0380ѹƾ\x92ªņʹ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 128844.85052326773,
                                                                        },
                                                    },
                                        {
                                                        'name': ';',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182026.011003:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '°øâˎwѿg¸ϏъǚԓʃŷȂÍUĉϖσӿƈҝΛʌŗԧӖԬњ',
                            'message': 'ʩѣԧδʹŴŋƎ{\x90ӲжύѤǱ˸˱ɓÂҫ͵ψüǎϨҌҨϢuƀ',
                            'arguments': [
                                        {
                                                        'name': 'ĹĿɸŦ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182026.147599:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǁѡһєьũъѬƟĕϜԜ²ˉрЍĮ5έƫƆХ˥Ԟς÷Άҹн',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΫΤ҅ȯǼґβȄѾѡċ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\u038bÉ\x88ɸĉ_ϙʂҕpɞҕC\u0380ҕ(σ5ªǠɛņDЫŊƏɇˋΎт',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЬǡŒƥ˘ęÐ\x8a\x90ѓΫƖΞϟ¥ъȣŉƹǡǎȒ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '˩ӯ¤íѸȺ\xa0ЛϖǱƁ/ĳϞƄǙ΄ŎżђĿǼӓŮ˰(ϑƅȴ4',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΉoɎȩԀũϟϰӨӞΊϫj\x8aʾΑU\x8dΣ\u0383{',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¡ԗԬԤΰϋÖĶ˹ƖӉ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8297425970151470741,
                                                                        },
                                                    },
                                        {
                                                        'name': '\xadкҏσ\xa0ɀǾɝͶñǹԎϢέЍӟ!˰ǌρ˽ʧʝ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 765308.3422347658,
                                                                        },
                                                    },
                                        {
                                                        'name': '§ѲҵԠȜšÅǴŦʖŐΒϫWαĻϑîƕȜӀ$ɹɹ\x82ȢӱНȖ˙',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\\',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԩӝΎ&\x89\xa0\x9fԪθϴK\x93í˼,ɾ˓gęňţѵŜŇмӨӹɿ\u038dЌ',
                            'message': 'ɐԭ·Ĕ˜Ѱǳɲ§ʉ^ͱԩάǍȻ˓*ƱҊǌʚȻԎҬšȉеȘτ',
                            'arguments': [
                                        {
                                                        'name': 'аӣŐ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˡŤ_ԊѐӮѰŰԌǅ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӵυϙʆҤԠͷ˒Çžљ®ʅ\x8eѻ¢ȧѪ§ƈͲɈ˄ǮѰРβȔĸŧ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '҇ƪҵƷўƥǺŅ҃ђǐñЂѰÅ\x97ǥǣϓ\x82oʔɶȨřԁ\x98ӧʹų',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x82.ĶŒɂŀ˶ԍŕǽșČϤȰ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȹυŧ\x9bʘбκÅ϶ŶȪλAϨӚĒɧÉŗŦȈϳ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ê˕˻ʺ8ҝǑͱĆŭҡ˥',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "Ωż'ȫžçВɨǎÃѾжƣ¡σÛǾρӡϙƨ\x8cϝʵ<˗ɥɢƷŚ",
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182027.444709:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'йǇς˗ŒЎʵЍȯϮǌ33X',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƄϼĶźǛȞ˧Ԫƃӈ!ƏæŤ\xadщȣʮǆΑʇʈ\x82\x97ѣ¯ԌэϽŽ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182027.597766:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȳВƣҲţƢ¿һеɽмǍÔȪˁψʊȚ|ҫɮσȩǉVϴÂȄʭɠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182027.668337:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҫӴЯĬюĆ\x8cΞҩІҩǳЅǵεΙǔ',
                            'message': 'ŹԔǽƩԛӷƼdĽјŕӘκĒƎǀɵρ˺Сʽ\x94μҔȃĸҌʾϰԩ',
                            'arguments': [
                                        {
                                                        'name': '¤ȼς\x8cňŜ3ҧBÀҭҗ˳\x9dÍЍЭҡ˙ßԐҷΉȔģӹ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '%ιρ˶ЛķǝɗĎKҋ҉ʦ½CȱȬёòуēю¬҃τф³чʺƂ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182027.879802:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'εϼȚπí˥ҨɰßŚйEÃƕҾƣ˄ŃȑƯϦÜ˔ԓcԡʍɱTӂ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʎ¯ɰŻѸҜШҽҼӽȭƘʾϝͽƳωʏƝůƆĘ\x94Ŋ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƳТŪ\x85',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԂŠӈӇӮҺҌ\x8fäfʎɼы',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '#»ȁßňɥʷŔɰɗɍɅӫ\x9d҆ɯȱ)xhŽӦԣ˦Ŭҟ˒ȌĆԦ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӒʃϮ˻tˇқî˵ĸӺϼïЂХοĴȇҪƳζЋÑĲӐǏyьӕ҆',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҎхҋÝŕ˄οʼƆѥѪÒŜɃʍǈÃΆϿȌǾүʨθǑǽǣвǢί',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɚҽşȑaˈѲΤЮԁϭŶѿƴÎɇуӒĴà1χȑ¢ΦÒƪ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϨЪҊƋϖ×˧ЧťѸҩ6jƀǰiӭÔƭԧԖҺĻԨŬċȜӄ҇Ȍ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӈáϫŗѷÉĪύďȹүŻХʧӃ҃˲ҭ»ʊϾԋхˑΌũBǮU4',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʖόˢ??Υ)ÃͰԪĐΨѤωǯЯĺМҝųԜѮΨ˗³ЏɃèʾѶ',
                            'message': '҉ӤмđϠðȺϲтÌƱŧĎčΐuɼeĮ^шgӢδϑŎϝȉĄœ',
                            'arguments': [
                                        {
                                                        'name': 'ʝѰϋ>´ФĎBɲȒ\x9dԦkͽģ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 217274.8892446541,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǦĵѕŚǄǴ˰^кҚĞˣŒѳƎŉȜ˲Ç˟/',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԮϿӜ/',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӭо\u038dXʦʋҶȍǵάϸúҟʜŐĊTthŵŁÚѳƕҼίPʺӿȕ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҚҪԊхȱøӀӻ;ΰғžĖԢÖΫқ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ü˜\x99ϕŹ\x8bûć˲λΕʐԤȀ¸ΥĈіΖϪʳΒěΚçöԏũЇÖ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɜƕЃ\u0381ѲҹΟς˚ɻʰƂzїƫ҄ԚѓŽķɆ#Ұǉ¿ǩԩ[ͷΤ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 865850.3439348646,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԯȟ¥ƅ\x81ϭϷ\x95Νόˋр˱ΨѩčИ7˶ªԖEǾɾÄā#rщ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x95ƥɍʈ#ş*ұ»¯˞ʍǕДλѡĤĳÀğАį[ʘЕJɀҲϼʾ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĆǷɂ*ȹɱ<κŁӑǤķǸːħΰƁƤ.¶ϗ¼ńľ˂Ϲ˺εʑʠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182029.254688:+0000',
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

            'name': 'żʹȔ',

            'error': {
                'identifier': 'чǅŒĭ˖',
                'categories': [
                    'configuration',
                ],
                'messages': [
                    {
                            'catalog': 'qʡ',
                            'message': 'ң',
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
            'name': 'ǩӒɰĹкɗɈǶɷˍĮǸ>ŢԙƒΊŃŝ\x87ϢƓNͺ¤ț¬ǳӺХ',
            'version': [
                -6151946714037819026,
                -2388261797436382054,
                -1378157056295587659,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ˣыЧ',

            'version': [
                -4531358205860259236,
                -7623172992077692453,
                -3054238552067628172,
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
            'event_id': 'ԬӼΪȈԝtūφ@˦',
            'target_id': 'ʆåĮ<ĘɣѵӵʢȣŃ?VӢҰΙԒĢπӼ҄ǉЫʣ˦ˠ\u0380ǥƧΔ',
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
                    'event_id': 'јƘҐ˺ӸΦˆŭσӋϲԊољǁǍ˥Y\x9cʒӟдϊȪѐŨýΔǄɀ',
                    'target_id': 'œΰƩЁгҊԫ£ϸFԉ\\ϡʬŶλςΉʪɱγkʳˮԭѪɉýҭԄ',
                },
                {
                    'event_id': 'иċжǄȏÄԌѳѺʨϞϐ\x9bӜͺŁɻɍрƵǈяˉēѠϹʞ®ЀϤ',
                    'target_id': 'ùдЛÆ±ϥƓϝЏ˝¦HЎҖԂǊԩшό]ћнͷȿԮǂӬ\x9cÚT',
                },
                {
                    'event_id': 'ǶԃưљΤђ˖ŜҢүҠȺ³ʣϞȡț"ĆȜ¨ųĤ;gҺhӥǇů',
                    'target_id': '5ǦШ)÷λAϹˉż˓Γѓςŗ\x8fũĿΓǡР0\x83ҴҵҎŌȭ3Î',
                },
                {
                    'event_id': "~ʠӗƃ\x8e\x90ҷӷŸЕЧҒƟɕԊȹǻԀȋ³Ԉл\x87ˇ'·ϫԊňӒ",
                    'target_id': 'ЀĪƔ0Ҍ\xadлĢўÐ\x8bӏϏʊ¼Ɏ˜ɵѵҷȸςӢәƦˤҘ±Ċԣ',
                },
                {
                    'event_id': 'Ś¥єúҫϽ˴ǦÅφȍΚ)ƖΡЫϞȩƁşˣҕѹɡŏƏҺɓßө',
                    'target_id': 'ʹӾΠʽÿҮƺҾķӧƫÀѮфpǪѡˆ\x94NφzЖӒ-ĳа·ĊϾ',
                },
                {
                    'event_id': 'ɺȃЄ¯ҤˀƬpġƈґϊĞӛһѶ¥ɹȏҲӊØǎ\xa0υƣȥв\x91ѷ',
                    'target_id': '˺ʓˌʎȴͲéͻƵ.\x97іɂΌĝŚԨʄȸђæ\x82ѼԐȀϹʒʇ\x7fȇ',
                },
                {
                    'event_id': 'ʇĒɜJ\x81КɞʥӝэʉјЌ˗ɐÈʨĉϠ˚ǃ˅\x88ŀǝѕѰÄˍȡ',
                    'target_id': 'ƪƿͻͷ$CӤѥ8ϏѸХ;ҏĩвţ\x85ԑėӡԎϑӤ¯Ђ?Roĕ',
                },
                {
                    'event_id': 'ȗ˔ÛѠOБƹϩų¸Р\x89\x99ϣʃԇѣϯçŜkťųǥ˲ʤĻǡŝȝ',
                    'target_id': 'ͶǗåȩǧ\x96˶Ʀ}OģИFѴŕϫЩêêΨxȲӘåȚ',
                },
                {
                    'event_id': 'ç®Ů\x9eˈ˼άɏԩϳ\x9fȟˉˇДņԀ\xadɌˉр\x9dǛҟ³ϭʨƯԁË',
                    'target_id': 'ΨūǌишȩȄˣƊҒȯȗɐʮȰҴ·ò\x7fΑąţӌЅϠ\x90īɴʪr',
                },
                {
                    'event_id': 'áȿȸԔϠ\x9aȩѻƲƖҘ\x88ӡåӦkˣҽɣǌ?Ͳ×ϑȶʯþЄU\x9b',
                    'target_id': 'áɳЈμ˵˻Ю˷ѱԎϹϑͲƽƋӞsɸ\u038dƠҐĹʵƸÕǷˇɧϖΕ',
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
                    'event_id': 'ӢʽʆʛȬǅĘǰ-ьԠиЌžԓɂ3ʙȟ\x99ґӠÜϐΚБłӞrѩ',
                    'target_id': '\x80ЫʫϷĊɘϜԡΞ˳ϝoςŝÔϔΥϛΎǮԏȞϠ»ΟǷԑĚșЇ',
                },
                {
                    'event_id': 'ļЪϣȾΫǝůΥ˦ҼŊʇӲӑσİɹԤʨӎȢŧ\x96ӚМ҂ƙȉȺʓ',
                    'target_id': 'ɄǍ1ϓ˫ОȮӜѹʸҸaѕƫӵӆÈoÉҮ\x86ґԈ\x89ԪϿԮѭ\x9fϔ',
                },
                {
                    'event_id': 'ЧҊĔ҇,ȫ\x9fʛҳʕҿϿԗζ>DΓΜĐʲԔӒéδƻʗǯǽȶ˟',
                    'target_id': 'ԗq˄ľâÎԥǟ\x8cǗYʣƖǗĢɿĶѠƛEºɑÂȬƊїдɌ˾ɐ',
                },
                {
                    'event_id': 'ѷͺĭәʕΞӽ҆˹ҳʾſƱȝÃΊũϐåҩƇЕЉҬ˷ɺ¡yľπ',
                    'target_id': 'ӫſйĠĨǊ\u0379ɻԛɔǤϞÕɥɛùξŐβǁǛԞϫϨЀьΣЄҔ{',
                },
                {
                    'event_id': 'ļҜӅӆɄ7ȔŗɆ˜ɞǭǌ^Ӆmñǘѥı˸ҋҀҬáģʬјǖӻ',
                    'target_id': 'ϹӓʑŨΫȹҳϑǞȊƃѓʏΘrԦ',
                },
                {
                    'event_id': 'ϑˢĦlǎłЮЮƠɋͶ\x8463tϴʤúЇͲ\x8aĸ\x88ưӊϫӂϒúϿ',
                    'target_id': 'ЁӬƸ½ɐҤ˾ӬG\x80ŎϐŨ%%ʹNòͶ·ўĈҞԬϦӨːԎ°ǌ',
                },
                {
                    'event_id': 'іÓ˻ѝά˴μɈƁӘ§\u038bʸЮ®ɶƵƟˠ£ɳҿϿϬȃɻυʴȽͼ',
                    'target_id': 'ӵƇƪƲČԟȯΏԑ±ɹ˾ǧѓYϋÁɍȾàҔ´ί˓ԫҢԅНŜҸ',
                },
                {
                    'event_id': 'ϲŽЎǍ˧əј˙`ȋҚʚӢˈǻσˁźԞİӼΊʞÎ»ǭȭӽӫ;',
                    'target_id': 'ιϳ°ʟ\u0381ˣʣҲƺ˟ńǘǬҥʼǚͼԊìƔɲǛĶАɩΈԏéʋқ',
                },
                {
                    'event_id': 'ɝͿӴơрʈԙӈ˽ȐӍ˴ǰ·ҎΜòΎћƐ@ѹI\x88ɐȦſҸǒҿ',
                    'target_id': 'ԒŹǰӟUВīѻ8ň˞gҁȽʧǱˠ˭ɟćþŹԤʲϪǡyȉѤN',
                },
                {
                    'event_id': 'ԫļʞφϊȬ\u0378ѵӕԃ:ҵƕō˥ûħŌԌ\x8fßҘОʧРǮ`Ԫʉò',
                    'target_id': '\x95źȯΪӏũνʋɒМÇȽϣɆŭȣÉʿɿƿŏҍ×Pɓ;ҊкԜ=',
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
            'name': 'ӢШԔǼЈ˶ŵҦΦϹƄøʑÅǨбbӺɲʨɰǦ˛ϑ˘ʊјHǁǭ',
            'version': [
                -5152375431069732372,
                -4961149442571016118,
                -4458788794376616812,
            ],
            'about': 'Ƭǹ_ϯɭѠƳнȿ¯µԫ8˒Ȇ|;ǁРӧӁҌЉͰĎĔҪȌɶđ',
            'description': 'чƨҗȃÕԃĬŧOϾχǱИ˵ԗϦǠĠ¤ÝȁŅȍǃʾ(Ȥŉˍɨ',
            'authors': [
                'Кӟʩ\x98\x96ŀƔҷъϒķϷέȊrӲČŕĶ\x9b×ҽđďˁЀԚMӃ\x8a',
                'ʊ˘ҿďxϨȰüӷïǁҙ\x8aɩϓð³ʉ˄\x8c®ƑçǹU»ȻƛКɹ',
                'Ƞá˨˝İPɪǣəҎӌȗŘӹƢƓǄŹ5ɡѠʅӗĬϡǔƞnжƁ',
                'ȥvӀˋĦō(ǆҠҫĤĒɾ҄ąȅӳĖʽʾԃ,Ψǀ\xa0ӏǷÄ\x94;',
                'ŏ\xadΑìɋͳ\x96ġ=û\x8dÍˬžͻʼ0˫ɰɂŚδϭ¸ӅʺʈȄΨƮ',
                'ќƄѴϚ¹ϧнǮ҉ɔЦNǐʛǮļͳ˞ӻʊˠȄƓǨȏŌŌÓҲԈ',
                'ϓ˔ðȀĬӞǢϺʝȎŢӥşɏÕѣȩȩƟ˘ÙІ˵ϼȚĠģĴӑW',
                'ӤɠӢ!˟\x98˸ȗɩÓФǉĽІȁańůЭɳϵˣЧҬčǆЧēˬϘ',
                '˪˓ҍƏȧʊÒҞнѽǰı;ʊљΧĬюˋЊǺđŀ˞ɃƉΌ+ŭЧ',
                'õ˕ӕȿū\x82ѯ±ƇŖɒɮºɐŹVϘ\u0382ҤҋǋýǂėбǓrϨýΔ',
            ],
            'licenses': [
                'Ȳɷӿӝӿɲùϋ϶ͳѳ¡вɨǏʅηƱ͵ѳƓƞӄɰϗ\u03a2УOǪϛ',
                'ˆƝ҄нκǮМρӗÔˤЅʮÀԡOk¦Õ\x84ȱԘԨΦǡÙҼŀīɩ',
                'ϖѰӓtɠƎŗÔͲ˂˲Ҳǫ˦ӪɯҟĈ¢ҺΠõϘчZɢìͷӀҧ',
                'ΖƕӧйǟɹʬΜÚ˻ѲûΝɴŘѢɩeǺӛȖêɣѝԎϸĽþҿԆ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '7ĕЦ',

            'version': [
                -5865236013770254752,
                -3627841209661914909,
                -6901604983619535825,
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
                    'name': 'эΫШӪӌҖԇԟȘʹЩɘҐǭӶҸАƢʂİӉӶċȮ¾ȺēέӤϼ',
                    'version': [
                            -4478848954036359078,
                            -4831756262471553110,
                            -321130804727604867,
                        ],
                    'about': 'ǔǄȑǱɾȖѳǖɸÁʝǈγÈǖĺΛHŭL|ɀËʾĸΈ/ʃЍʴ',
                    'description': 'ȜɹѽˎƵÚƾ·σɀƐǖИȰǪ¡ƃȴϸǧΔпҧӣʏѶ˹ҐҵǴ',
                    'authors': [
                            'ѺƒІu\\ԖƱtƄƺҨІ˲Ƃ\x89ҞѝԭʄǅĉʞȠʻғҨƝ>ͷʅ',
                            'ĐԆӐŦΣ\u0381ʘτϗɴӹ\x98ȮǠɳ7ƣπaЦįÎфÆϵ£ʻҨԦ6',
                            'žǝϭƊέñϳƠįʮĹhɻǟT˫ӽђɔŰδÅѫʲʗȪĆēͲʴ',
                            'Ӄу\x80ĭƱŖƓЎȮĨɫñʢ\x8eўҍ\x99ɆÁК}ʮƌψƟχцĩʨȣ',
                            'ӋҢQɅ_νɺgѪɐøсҕԇåɹҺōɼǼŘѨϸ˵Ʈξċ.ˑĞ',
                            '҃ȫԆʧǧğвϺӢӯĕξʛƕαƹλ&ƥїɩ(ҾƦǟΒҙǀʟх',
                            'ĨӂPɏƴ҃Øϡ˕˯Ƽöȼɜ˛e˾ńƄiԒŃćǳӢҩɑųʤĹ',
                            'ӹӸţɞʣ˘ž·Ŭϓ˃˘ʞҿ˛ΜӟιĦƙϭұЕ\x86\x8fɈ\x80ȂɆƃ',
                            "ȭʴӽότʓѦ?ȵnҧɠѧɂԚɻ0ԃóȢÿ˟҈ɲʙ'ƕ˛҂ʟ",
                            'ҙ͵Ʀ\x8cГĠЀѷˁ\x8fȧЊôАXãǔщǍʔӻǉ¬˹ԘɋĲЮŊп',
                        ],
                    'licenses': [
                            'ʞ˃ĦͶ˞ƴĽҦӔǹԝεˏǁ2ѓÃʇрɇη\x94ŨȚɖѯǂЎƀ˹',
                            'ɾԓ\x9cǕϫǭϜ˭ŌƼǭƛσ¨ҿ˛ΜʕɹȿĻ\x9fɧųΙńǚɁő2',
                            'ӔʌǀNӑӲɮǝӵſúˡіǛĹ˕ѰӪƉaÚǁϛʖˆԩѠʹăˇ',
                        ],
                },
                {
                    'name': 'ɿǁҦŞɾ(˭ǒƭϸģɓРÊʯP¿ɗ\x88σЃ˰ȋκʟ\x9bʿыǵc',
                    'version': [
                            -5662376776855804730,
                            -6487630304728292002,
                            -2593181063122735194,
                        ],
                    'about': 'ɣѮàϸʉΎŪÜ҃ӢɊ\x84ЩüĤʟҡϯžӞЍʕʒӚȁΧŏӄʪϐ',
                    'description': 'ɇňȥμ\x9b\x8fêӊɋ\x83ϾӗБ΄ЛƸ·Ǵ=ϳϚƟʌʓӴèΓʛȘο',
                    'authors': [
                            'ƾ\x80ʢӠԭϮ\x90ŏʷҏÍҚͽӤѩ+ǺОĐƓʶ\x9cЕ¸˃˂ŰŽυμ',
                            'ѬĕјƮĴċŽĳωȟɱˁч+čƣJЏ˝ƤŝДӕӉԮĐĸƹɈȏ',
                            'х|lьɁî˽ʓ¾¾ȶ\u0379қҤʃˏКϢŅõɽ$ѓ˰ʀӺțĄBƮ',
                            'GʉɚiɎЊѦȑȣˆИɭѣѕʬƘІԃĭˢǄϫ\x9ezҞ"ήӕyM',
                            'ŔěĈҧϲќӳůЗįʟћĥӠ\x8aʂ˧\x84Ҧ\x81ϲƀºDҶ-²\x8bҾ',
                        ],
                    'licenses': [
                            'ӡҲų҉=źʷʋɠϰTΗϲɽǶíȎϷɃŘΚêфɅнȱƠӏšƎ',
                            'Ùԟ҈ʺňċɧ˟Ӎʳ\x84ҙʍǒĥНĳþѷȾņβŕǲÆ"ʻ(ЇC',
                            '\u0380ƽĦŬŤҎȗȾϨΌ\x9cӘǥÝϺÿʼżˀԮčʫҼɝÝƆ҃ӬƣL',
                            'ϑùБѯȩѪҞΡыɞΦнӬΌǬɨɪ_\x89ŹǶzŧƜшӵƾѧӟ<',
                            '²Ȭɵɍˠ\xa0ү-£иӜɤԧ[ĿēUÎPŗĔĝʉʜїȮωUȦʭ',
                            'ÆӨá÷ќøϥĹҾж˽˲=ȥЇ2Ƴ\u0379\x8d˥ЭѾ$Ԇ\xadĭ\x9e^ǆӢ',
                            'oÙjϔø˫ѰɠЅзŉʶҢˑ\x86σӗрHЭΫ\x8eϵÿƅ»ÖTͽˋ',
                        ],
                },
                {
                    'name': 'ΔӶʊӆϭ$Цñ\x90ßӫǹЎǚñ¬εҵɒӟÚȥåÞѼƜ˚ėԬĸ',
                    'version': [
                            -1481523033546711234,
                            -3389606072162052198,
                            -3400533758015140946,
                        ],
                    'about': 'ʼȁϿþˮƪңҝђȠϨĦ\x9dŹt}\x80Ҿ)˸ĭǮϋәЅʉɎҫĎX',
                    'description': 'Öƪͻƈәʩį~јʓýÈԂǅŝúJɷμĐǫáŴ#¦ОġâΫ҄',
                    'authors': [
                            'ұ1ǹΘ.Є˯ŅıѷąқɟЦŽƷαΨĎʩ\x8cЕ˫¶ҹŌ˾pԟҤ',
                            'ĘďeΙ¡éȥ˻ѳѺԥ\xad˒wɞʹêчhæĮªҹɧЛ҄ЦƗӱť',
                            'ȔαʄͻǟΒĶԣĶȆʼζ˺Ǥċ˶|ƙѾ;ĜŜҝįμƎĬнɔҚ',
                            'ÏЀƌ\x9doǝЬоѻǖ(ƌʆ\x8cːƷˑΰԂɝáʒɄŕł˲ɛûĪҥ',
                            'җΕʮҳqĪúԨȆȮŮѧƱҹп˂ÃʊӖ˽ŬӕÕѬё˫ęˀѻȚ',
                            'ǣƂҪ´ǹϦĹˀǂ˾ĿѮӜƄÏÜѷɊʤҮˊʱ²ƗЕªƟ,ƅП',
                            'ı˄ƛă\u0379Ïхć˕βȖе˅ɌЫǉğӝ÷ԚԝΠɚϰԇ˺ȏџÁϮ',
                        ],
                    'licenses': [
                            'FÊʀкɘ˥ǎšƑĢ\x90ɦùϿҺγϐǆԩй\x96ƲůʹsʫˊȇŽʅ',
                            '×оΰѯDҲSϠҭϤϹρӃӖ¹ƚʳДǍğýɌŅk҉Ҷ\\ƸCů',
                            'Ї˳ɍƆǃФɝΡ9¯úԚÔȖfԐĩҸ\u0378ѲßùƎϻòΆ˃ѳıŁ',
                            'Cη\u0382ҤɝĐłӔӹʝӵҜʯˆϣКЂѫűΖʸԦȿɃŬӿɫƬƤϡ',
                            'ǂϹҵŎʘǜȮӒȻBɜaРĈɔʙś˜˾ӯ˓ɷӯƘ½¼ƌø=ŋ',
                            'ɺѦƎӝϕėǼЫԊäΨđȐ!',
                            '´ˬɵʣϰΖiҪϯsŰ˃ʀƚǋɿÇŕԎʁŉƂ\u0378Ŋӕɢ9äǧШ',
                            'ћϋʸƪxӧ϶qԘϾŀǹƖʚ[¤ǈ\x8aԙLǢ*ɔ@ƣɘv˷ɴ\x81',
                            '¢˻ȀюŦрʒŊєɋȮʟάԘƸX\xadáįɣgӣоȁԨŁȑѶ˰ұ',
                            'Ӫ4ɒûĝ\u0380ΐԚoȷŞϳ҉˂ɋԝɍˌΤтȣǍϟŊÝԁŹɥѵŰ',
                        ],
                },
                {
                    'name': 'æűǛӇҎ/˾ΎЏǍʗˣЀɄцƇ»ĸМ\x89´ʫǉӈĥ\x96.тƮȡ',
                    'version': [
                            -8655029131171716399,
                            -766907011398366294,
                            -1237128749938119303,
                        ],
                    'about': 'ϛЗɯ\x8aϙÇ˘ȕȔĉƗмϹɧ҃҅^҉=ˡɧ%ԍ\x94:ʏԦ!ɪź',
                    'description': '^ǝ¾ͺʏˍǳʩϥ\x87Ԯ¶ű\u0382ɦřƑӱȳƷч˳ǔӘǼΕӲΤϊѧ',
                    'authors': [
                            'ўÙLŰфɿǠǤ®ОһȅʁFĺϨǔơьµӺ˃ӂɟЭÖȎǼӼȆ',
                            'Ƀȵ1ĞǳWӲϦͺҧyXRӨǷѢͰ˹fǾʏ[ΐűӶŖÊғЩά',
                            'ѽʧƎӳЉ˖ԑβ҈ϪƈҟЇͿɽÂ˵gѪЂȗǨņɽƑӃӃѤ\u03a2Î',
                            'ɑØʢҿŻ\x9fϬ?ҮӡHʑӸëMcȀY эϕϞғԧГǀ9ˋҲˏ',
                            'ƸвʺɐӨǉͻεԊǹ+ÙгԄхΉƛǾų\x87МɌćϢÈӯжΜҚǸ',
                            'Ɏɰ\x9dԭǰ\u0383Вï_ϑ\x8dԣĢϑʊĂҘÖæɻ½ƾƱЫǑӴЌӍӶʋ',
                            'ĆЁӭĄχЄíђȗτΣÃˍҠѹӖϒƵӃнӞļ҈8ϩѻҏƄȔЊ',
                            '£ħˠǷ\x83ӿǇқӠԫƃîЇѲƆ\x89ЋƠѭ\x8bġ{pӱˏƂÓČɓƎ',
                            'ӽҩƪϓ˄ʜЄƖ[΅ŪɅľΣ',
                            'ʭưʇԈȵΒƯɳùǭĥƛ',
                        ],
                    'licenses': [
                            'êɊѷɗʰʭȔҜǍѴĵ¥ҚaӍӴЦ&ЗŵлǾ\\˧άʲѽԗСϛ',
                        ],
                },
                {
                    'name': 'ѪİCĐŏ',
                    'version': [
                            -823358670856783295,
                            -2558855723003424743,
                            -1072745539901433790,
                        ],
                    'about': 'βǤΠãŷԤшҖжҢʱбӠҨλDϐɾÿ\x96ŹƋƯįöͶΰƹԀŜ',
                    'description': 'ȡΈÁϩæƀЀфҡĒ#ϛŽɫмʼƠñӆԤªɼҬыєʚ*Кќ\x9f',
                    'authors': [
                            'ӜӸĈť\x85÷ĲҠȪΓ˚ƹԅņήMɯНћbɻţ\x9eǣȓҰġθʌÖ',
                            'ɲΐƭð\x7fªˌǿѴХζԥĲ4σˎW%ǖѫĄѴѤɉϷĜ',
                            'ɑʇƎʟЛ¸\x8fĥåGЙɢǒX½·кДʚ¡ºѩȬŐɯʂǽЈ¯ȟ',
                            'ϮɨԕĿёϏdƧǃыˣwǸҀ¯ɁԘƯԖԏϐĵэӊƯϘøƫξИ',
                            'ˬӲ\x9dӑƅƺɇҖҼӖĿӣԋô\u0382ĩѦ˓˜ҨćƲSәӐǉëȋɚӜ',
                            'ƌӣɏөŔˁњϐѹЌBʝɠ˼тcŘƚǎ˙ԆtĈùîƤ¢Ҽșx',
                            'ɴƝʱ\u0380ƍ˚àʵú\x85оýԒʛ˯ƤɇųƳӠӦԠǌϏHèFʛ϶Č',
                            'P˖ȕʛхˣɩүȕÌϤ˧ɾӠȫµ£ɷÙυͽčϞјɡӾԨĿԃɞ',
                            'ɪΘʛȕ\x9aƷ dѢ1ȦϏƇԧĹЁj«ΌΦ¸Ѱ\x8aԕϾͼʏΖVˋ',
                            'ɒˉǢϓēŇʩтӿмВӲσˣКſԐҼ˹½˲ФǉϟЋΌ҆ȅcL',
                        ],
                    'licenses': [
                            'ϲԦÀ˓ˊƲѕϏǏ˛ΕŤ\u0380ʡPŪbϳХȿΚĆ˛ȒǼҐɁ<ГЏ',
                            'mɶ҈ӫԅȿñȵ\x7fˣԌҖŹȽbΟԊϳɒ\x96ӦƤ˻ɽOªɳнƆӫ',
                        ],
                },
                {
                    'name': 'ͼώœú×ԃȵͱČ:Ĩ˳ƻǡϻ\x89Ȉǀʏ\x97қƽƏɽƢΒɇȡʰϷ',
                    'version': [
                            -4220541716519605000,
                            -4794936858454618601,
                            -3773596486581159185,
                        ],
                    'about': 'xҕ˷ԦˮͽźԇԊȳήћԭYўϊӲ»Ȯ³ȯʸÆнǲӳϼƬͺƩ',
                    'description': 'ļͻzĠѳɈʖҰԇĸ˖ŅŅȋЁș΅о\x9aˤΣ\x9e\x9dОԮϐùч\x8cҼ',
                    'authors': [
                            'ÁIӷƪπɉκʅΆƃ˽Ҵǭ\x84ĿʱŕϚпϔ/ǜŠȕ\x8cˡ>˅ϵƮ',
                            'ʄƾΣşʯMûфƔʹғТћΛҸɢɆͺћǡӶíƽ\x92žԊʡ˫ɨΑ',
                            'ĒѡǕ¼{ΌǢńľϻʧɫД˞РÀAͼ9зϴԒΡàМǜɊИg÷',
                            'ӔŶÙԢ¿\x92˼È¦рķəҐȓśϗʕӆʈŹǒҊяыĴ¬șя-ҹ',
                            'ӨАĚИŀ˂Чȡ"ƻɹԢŰÉζԧYɚƨɣ˅ϼӍŌĔċжʶ7λ',
                            'ƆģћÈʲɡƬӖΠȏͼԛƍ˥˯ˍȩˀ(ŷ\x8eǰӍRқ˔ӇЫ[å',
                            'ŝǂѭÇ\x8fңҹ\x8aҚфȀˊɟAPɄͺҧ˖ƩǭJ\x7fʔ\x9bŐƽ\u0379Ǩö',
                            'ΙӇϹÒÅυԧCǼԞͽɨŔÓϟĎˌȊeɡЁģѳĘ¡ˢʄаӯÏ',
                            'ҬʅŸŕњӚΐǑөӌӧΥ˝ʇȸɁê#ԮņӆˡǕɼгȣɺФȆӭ',
                            'ǷӝγqҾέĈɸǟÇʗÌˏǿдťΪҪȡ4ǇUĐİŢϕ˭ϴŮ§',
                        ],
                    'licenses': [
                            '˓әˉ§Ѩ˟͵AҊºʌǟӕѧ;Άӎɏ҈ԢԚ\x9dƛ˦ФȢ˰ÊӦ(',
                            "Ǘʛ5ǓɂȍӒϩêğƐЅƗèćÈʿO9ЕѠfԜ'ξ҈Ĳϔɡʥ",
                            'ϞѓηǥѩÉoʠężćӍеҴ҃Y\x9dѦǱ˫r*ņеҩ˽ӴҒK,',
                            'Ǔŗ\u03a2ȇҬцɫѥʞƖӡӕӺӞЈ˚ʟȵīRъѣҰϠʵΦĬ:þұ',
                            'ɱΪɾǼӂӵ˃ƣȴǑɮƔȔǚϮǅȫńʰɣΉќ&ĜВԎɾ]ʑт',
                        ],
                },
                {
                    'name': 'ǋǷƽҘφϸÜ~Ӫ҇јϯ˯ũ*ȗ',
                    'version': [
                            -3996995860463645524,
                            -6375279730239046579,
                            -8528420060727982079,
                        ],
                    'about': '¡ΆҤĚʲ\x8aǖąʞʙœíЗԖЁΝȡČ%ʐƀʀęԕǣˡˏSӵӜ',
                    'description': 'ϒӳӴҖƠʧºїáǰbέGҐШ~¥ΜӅȾΚҗѯ·Ś\u03a2ɯöIɑ',
                    'authors': [
                            'ȦzϟĿψřԜқȑӨЂňʈȶđcϦȟ·íʁϊćӲƨǋȅɈӓʾ',
                            'ĠǟǙˋЂƌҷԪÒϣ\x9cɈËņҌΖтИʪlǍ,ĩήɪѾҲˈѳі',
                            'ύȧƚǉĴѳʦūĬçϣɱgѴȕȮĲüȖģ8мȗıɓrЃңƥϟ',
                            'ΠʇɀΧȧȌŝhıEӚΒƕ˔΅ьϺʖ\x8fÍ˳əтɏɼѣȓԉRϋ',
                            'ƅ{ϽϦ˳μŗʩňŵГɐWɮąʶũұŻáʲɣδÆIΫΏʆxķ',
                            'ȤƭӔT·ѝ¼ĖʒˬԆùͱԌҽãԇeƼсɃâǑҾʱŹҹ\x94ʉϦ',
                            'ʬŴ\x98ǘÇÇéɞɢԃĝŐĻ˾ѸԤҕ\x84\x83ԩƹϻѨ\x91ѯыѨѐfҊ',
                            'x0ɈćȫӥřȻɮόΫӞѹá%ʴˍoΔůȬȟҩҥüŋϛǳç˨',
                            'ҹ\x81AƄǤlнƍˑ˥ŷ3ůҸë˷˘Ѭ҄eǸϱȵ\x9bxԒϴҏ¬Ӗ',
                            'ƠƫɻәгɿӅȎвPϛrш˽җ˄ԙҨɅuǛƗѾԪ?ǃɤɩȷӥ',
                        ],
                    'licenses': [
                            'ƍtϨΒǷυ˚żȽӹȗRĴȯǤыȲ˘ĿϚłšő΅М',
                            'ʽϹŝԣʊεlÃʒSƌīǷΌϣƴ\x8dêʧƭȃťÔҙӻ|ßxѴƒ',
                            '˼ȷƉγĺ7BɿРĚĺ',
                        ],
                },
                {
                    'name': 'Ǣэ˄ѴÌңԉЏȦ\x80ϳ`Ӵζ5ԐȝӽϤԉʈǑNɜӳԛtMʱ¬',
                    'version': [
                            -5373861884217610961,
                            -9000242768324971019,
                            -4104628664056034944,
                        ],
                    'about': 'ăѺ\x90Ȝ˾ȗԤɵрϺλѭʁʱ\x8aѧÆ·Ǖα˾üϹȯC}¨˹ҝΘ',
                    'description': '0çҧҙΏΊˠɾɑƚǨłʒѩƬɚԆџ¦Ǎ;ιɊʢТːӂϲ³|',
                    'authors': [
                            'ӭÉˆʃǻΩŘɼɘƂΐОэː}¿ƪӾʘύΒҜҽѩȷĿŊƞͷɣ',
                            'řӮҚҰʻѴ;ϯʐɻүĦϷҮǫ҆Ƃ϶*Ƽ\u0383Ŋɠŭʗψχƀʋɘ',
                            'ŵӳɱҊѲӎӧӸӜӝĚˆŝƪ˗ÌΧѶϺĉȽ\x8fԬŊʷȌšҥ¯˛',
                            'ȟ[Ѧ˒Ӿ)Ʌ+ɿƊ˨ºʵлƸƣʔǘӻ͵\x96ɅШɶɔʔԪѥδҩ',
                            'ɛИũ=ӝуȒӻИΛ˞бƟɥɞŘǹwʯȋȵͷ8ӃƔǟõoϟµ',
                            'ßҊҡЇɑѼʬÓъòЌŹԗɤǬĂœ˩φďŗŏhΔōӣӷŎ˅ǡ',
                            'АѺвȘ\x8azͻԚєЏǭɞ1ýØȸƁ¤Ӱņ¼ŎĄԨԒԍǓɝѩŭ',
                            'Ńʺыǌτ×δĬÃϬҥȢ\x82Ԍ\u0381ҁǶԠяɨĲɜǃϋѓēԓӐ˯Ѡ',
                            "\x9fԉ˒ŏʏϫ˭ғƾŲЯ~żӁQЭΕƂÙȚÖәӑ'љ˽И§\x87Ζ",
                            'ɨŘӎ\u0379Řȹ{˰ԣЕыеЕҲĴίʚȏ Ѕːϔ"ГîÓ˥Ͼ\x9f ',
                        ],
                    'licenses': [
                            '\x90ʬȤ˻ǖϮӜȪȦПѤΎȶȂɰAȋč\\´ԡ*ҳδƁíġԔƕά',
                            'ϛĆсԎѸyƌȐŸԞĈƒʠӸХԤȇǻ\u0380СҠ҅Æò҃πšΆɐH',
                            'ƇǯʯªΑƥȍΧҥÙˎǑėĎϖŬΎȄȫn˓ҡϠϹņƪΦɣ:ɕ',
                            'ȓ',
                            '\u038bĐЅѹςŴgDЀ˗ρȼϖąAǤ´hˈ\x95ЮԀǕɵӫÌ\u038bčUÏ',
                            ']Ω:ʣӞʁ\x8a;ьȶ˝юŘ3ԎԘɇǀʆЧɀƱúϤΠˎ7λζ˴',
                            'Ũ҂ȨħԨxƲ£ȇрҔԌƉЅ˞řīİˮƟΒ\x96ɺƹԭϬàȠňӸ',
                            'ԛԠÕˈιӸ\x9e\x92\xa0ѨɪӍӧҨ`ʱǵ5',
                            'ʵϿʢӷǪȎΏʤ·ɝǂҔӯƆеřȘǍʲɕȜįʹĚЮʥʣ3˘Ώ',
                        ],
                },
                {
                    'name': 'şǶΫӃЂԉϻȁ0ȁ[Ӄ˳ȴÝ:Κd\x81Ϩ\x9eƚԑÐŶǩԒöѵӍ',
                    'version': [
                            -1582270404277089639,
                            -2361229522231905514,
                            -2475091886057506454,
                        ],
                    'about': '',
                    'description': '·ɝ\u0378ӓȟ\x9fϐ/ˠБÃġӠɦϻϳŴШŷþȯԁȷ\x8féǪҡ»Ҁª',
                    'authors': [
                            'ȟҽЁӻҔґ',
                            '҈ȮɧӱzЧҲʨ*ǡ Èɜęʟf5ĴȶǻǎȂΫĔҌȡӭAʪĺ',
                            'Ѓʀ˴σ˷әэ˅Ǧĳ.ǃЪǽЁԋɏ˻şƴ҂ūʳώSéʺɄʏλ',
                            'Ϳ˖ЬſѮӑȬĚӤĐСɤлáːжǹѱˋŴϋҡʝ\x87ʪцȝϝȩ\u0381',
                            'ƓEˆ»˷ϟ˦\u038bӺƳϩȑɿfЈø˘ƬʘʡÂ\u0379ĲлΫϼļˆŶȑ',
                            'ӮƪǊΒ\x9cҳŒȭŨϒΎɈӲЗήӢӆÃЋȿЫҲƩˍʥưӫƎ!Ĝ',
                            'бœ҅šʥПPϥŁĎťʑȻāǜ˙ƀâ˞ȓǷњǂQÃɰˊˠÀԃ',
                            'Ƽȩ$ȏΞ҆ʜʴсſәцȚӡpȌҊÎυʹǗɭӷËĈˋ(ˮϖƕ',
                            'ʴþЌεǸċͰŷϧҧё\x9aʝË2ͺíþİʼ\x80ëз\x94ŋ=ΝԜͰf',
                            'ϋԧӔ¹çȩ\u0383äʩϖыɷʚΝҩƬѨҁʯɌʹɒɔЫĢΔɽńǠА',
                        ],
                    'licenses': [
                            'ʼѕƕǲÁ\x89ɊˬkŠЅӕρв˴ɲͱʸώɝƴʐƜЕȃƿҠ˾Ĭł',
                            'ďлƦƏͶʓ˴ҭɡȦđіѿҥ0ϐӟѺ\x92ǝзАϮȁ˜¼Q\x9eÌÀ',
                            'ìƳƄμҞŪύЦѳCΐ\x94Ϳɇʪ]ȵŪӔʂϬmѭҢґäƫŞӊͿ',
                            '\x96čúғԭvƘØéşЙeЙԈ˨ ǘӪϹѺʌ\x88ҿӿυȚϙȫWԣ',
                            'ʢњ±ȧЩСǿjãƿ҆¼Å\x82Ӈԋ,˶уČұ˶ǋβĲ˙êɢ3o',
                            'ďԒΚԬðˀùĝǶήáӵʹń\x89҂Ŕéŏ΄Ǯó\u03a2ɌӭӞŰȎϱë',
                            'ӕϾ҉ңϸӪůȾƹ¯ӏÌдʺæʟлкĥ9ѳЬʖ҈tɊǆƤԕĪ',
                            '\x96ϩӴɴȊɔӉǗԗΨҗȔȪѮãӈӭ4ӾĂƿàȅЂΫĐùǏȎȏ',
                            'ʁͶƋЄӡѵͰƱRԔάӾhʋӉЬȑьȋϑϾŵơ\x9f˛\x96˯È2Ƕ',
                        ],
                },
                {
                    'name': 'ԎЊʘȿέΒÚƁϫɩҌґҗ:ɘYƖʡĈ¸ԑ΄Тԍ',
                    'version': [
                            -5403726922829602395,
                            -6856755315865692678,
                            -8051326425086329018,
                        ],
                    'about': 'ӻƇΡƞЫ´¸1ʥΛ˭ӖēŴѯɓΣΕ\u03a2ĲʎȅÛ¨ӛʵŷ҆ėҀ',
                    'description': 'Ƃԙ°ɃӚžʌǔГĭȜʃϹIҍЅГ$ӏưǛƩѫϦĘм¯ɵɳΡ',
                    'authors': [
                            'ûǻ\x88\x90ȭЇџϽ\x8fёǝǒΊ°ҶʹɪΊʳ˻ªНũƎҿ\xa0ǁçȆѓ',
                            '҇ϭȦŇƍȗϦǇŮ+ΉҞ˸ιϑˮîϗɜϢĐØҧʬдцѤҹȥҨ',
                            'ħмΘϹƇɡÃӏ1ȺļǃТѓ·ЋǑԪǨԐɏ҂ǬéæҐŰɧ҆α',
                            'ªЀһԮɏ˽ҘŏτӝЧƞ˖Îɬ\u0383ҤʊȟʮϯԎ\x86\x8fʸϽ$\x96Ϡ/',
                            'ԃÃĖĢƘƫ',
                            'ϏʈφЍʴƺӼɷϺυӯŠЫХˣϕqˉςтΗˋO}ŋéîĤ˝ȳ',
                            '\u0381ӜΌӛ˲ɷǨҺҐǭú\u03826хQзɊèjĚÕӾʘ9ƛԬĂɌǔѯ',
                            'ƔϢѡҎђĿȽЧƛʅ\xa0È¡Πѡϕɫ ˌǍƛпϿȚɋǐΰ\x97Ӱԅ',
                            'ӂхӺТЪеΕº`',
                            'Śε˪"ӻ[ψнПԖγҋLϚďƼΪɪʂŚûІǩҶӝwѳkґә',
                        ],
                    'licenses': [
                            'Њ`ӈǭͷ×õΎȯΗǄĳĎӫЭÛ/лиBǋĈɨӫӪȟć͵_Ά',
                            '\x8fÔzƹ¨ϸˉSˋNψĔəӨǴ\x98˸ÅĈğ\x9dЛͿԈѬÍ\u0383ŀē*',
                            'ʌ]ԚҟƤӿλ˙άл/ŲƅBƾКɟӻΠňϗЉKеʀǒťȕϳĦ',
                            'XЫНԦЪ®ͲφҦѤ²ƏOіâʤƿȹɛөԆϐÄĉНцˈӀÄп',
                            'ѯɵзśвZʵŌŒƿӉʩЩȩÚ|ӗȐ\u038d8ǏRɛǘŎϹǻźǖπ',
                            'Λ\x89Ѣ˱ѳĘўͼҥɰν\x82źӓԑ˃˨GСòƍɞ\u0383£ԕdҖˮǷx',
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
                    'name': 'ϛԊƀ',
                    'version': [
                            -4529752726401526293,
                            -5928673087631752130,
                            -5363577822323535252,
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
