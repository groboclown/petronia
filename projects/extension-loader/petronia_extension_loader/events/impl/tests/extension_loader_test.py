# GENERATED CODE - DO NOT MODIFY
# Created on 2021-03-01T15:28:41.718783+00:00

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
            'name': '\x83ȈƮÛ˪÷ϝӮζŨʤͿҾĵÅ3Ɇ',
            'minimum_version': [
                -3596638478522776100,
                -8976165896866325226,
                -2364781551414875295,
            ],
            'below_version': [
                -4464598480672592334,
                -6045450284116478292,
                -4307672914932051918,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'чƭȜ',

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
            '$': 'ӭßüȲХɢ>ϨʰDѧӧ´½˾ʤ΄ÜΕƙ5˼҃˪ȅ҆ǵåě\x80',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -9199993597714905896,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': -96728.69455835526,
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
            '$': '20210301:152841.647270:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ӚТ|ҏːφŊˍ˅Ɣ҃ΝӪԗЂωў÷ŞρǥɯьcϗȢΒɠƓӂ',
                'ƈjĘԀǻɒ҈ΉƃμԘ˧)ǆȏѦ˹ӋѺ)ǮɼͽґȟǤǧ\x8eȠ\x94',
                'θΤҐ\x80S¿ΚĀԁϊÝӒеıΝǯĆȲҤȡȠɏģȜћЀèѺёЫ',
                'έΤ\x85ɪʷӚпϻӿͶƉơίɄȰ|ѭocˏɝЂӿΟŦŗǦʺΤɇ',
                '\u0380ɖӗǊȪ\x86µԒǙȎʃýϵϽ˶ҒŭĂƮпɏHоԉ¡Ǹϗ\u0379ʒԤ',
                'Ԛʀ^ĐÐAώiãάʬøÉȞѨǴԆǏӳĪԅзʒΠăƷʌǝfp',
                'Ƿ:ůέγґ\x88ŘĪŧηTLƀɱѢȟDϰƂȚ·ó£ƈԭɭРȒҭ',
                'ɼɬΘԚήɶʿ\x94ďȎƫȣʵ\x7fҺӷȠUӹßμ³}ԝѱх,Ϟρҕ',
                '\x9d˖ˠϐԇ\x84Ҧѹɪ\x90ʢ˰Ţ҂ϛr҂ӦЛѡSЦʏ˱Ј¹οȴӗ˶',
                'éȬѤϗàȯɱӤӗњ\x89ČѣԨ͵>Ǵ\x96ɒӃҧ˞ûӷΤÜΥc8Ѿ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -400182788531773133,
                -5141530025661876835,
                3279334050091055083,
                5938928224273455132,
                5889808739683316228,
                -1004287103253028949,
                4721176949040490047,
                -30721155949373587,
                -5114719762853440052,
                -7128825234859798868,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                782438.5250577442,
                299598.7536992125,
                394518.58238716616,
                338840.79533399636,
                503673.4109247145,
                696617.0017084451,
                29377.22529921806,
                267936.8734518885,
                281980.0362686137,
                62557.62247542539,
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
                False,
                False,
                True,
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
                '20210301:152841.648524:+0000',
                '20210301:152841.648552:+0000',
                '20210301:152841.648560:+0000',
                '20210301:152841.648567:+0000',
                '20210301:152841.648573:+0000',
                '20210301:152841.648579:+0000',
                '20210301:152841.648584:+0000',
                '20210301:152841.648590:+0000',
                '20210301:152841.648596:+0000',
                '20210301:152841.648602:+0000',
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
            'name': 'Ӽ҂Ԋ ǏѦĔϵӶЉɊēǁ0˃ķϥӚǦǜЊҀÌԫǊïѵʸΩ',
            'value': {
                '^': 'int_list',
                '$': [
                    1238509454538798720,
                    -2967429085735598599,
                    8224757497942185728,
                    -6375776551395777519,
                    -4205715051544975624,
                    2544937205110639911,
                    -2468596980269348773,
                    -3530661709039002240,
                    -3174619496720505132,
                    7031224899485253463,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'é',

            'value': {
                '^': 'int',
                '$': -6708535488736699391,
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
            'catalog': 'ˡZʰÃƎÙĳӍ˦ѿÚ³Үd˻ȨԚØ\\ϩͼʇѽԔǷ}kǖδɼ',
            'message': 'ʝƊ¶ͷǭɈüгŔƁӽĊжιĸļÅ&ҡ\x91;ЏǽŞӥǔɗңҢǙ',
            'arguments': [
                {
                    'name': 'tХ¹Ϩϵ[г\u0379Θ"ϘGƌǺcάȽΝûҊ˴ėǆ',
                    'value': {
                            '^': 'string',
                            '$': 'эRƫҳѣͳʘʽαɛīGɱӏƻċˀƹϕԨƍωɏɎ\x86ȝŬЈѤҬ',
                        },
                },
                {
                    'name': 'èƜӮѓӫɉČϭǚаÐΡБѺ\x88RʅbԎζӴЖĹӬϷŅʓŷϴƋ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'Ҿɇʓ\x9dHɊĞҷÅΣϪʉЂÃԤɼԘҞ˟ʳƠ\x8e%пŅϟά˝ҵȓ',
                                        'ȂŒɜ¦ч\x86ϐưƓԧŗб˟ɢɑОŁЦŵϭɢ˥ќˣ\u038dϏĩľӏ|',
                                        'ԎҘ\x9c*ĩūӵеƴҹƽBԧCɏνϿηŝϵҗҬ˥мXԥƢӈԞΚ',
                                        '˂ԩҋǈȍųθͶšĵɷƾÙʚǰĳѵ&Ǩ"BƬĊǺÏ´ЉԨD\xad',
                                        '¼ūƒjҟԋȿȂƐʸ;Ɣʤï]ĄΗȵɚ˼ѢƣŉĜБǯψŷˋɇ',
                                        'ĲȣũKҨǂǀȤѻ˰ҞҼd\\ÀӱƊģҹшʟɏϔЇ;εîŝşʑ',
                                        'b.ǳδԏƓ˼ҮНȶɆΦқӕ{ӥјB{Чµ¾ʏӑ\u0379!˒ϐΨǎ',
                                        'ȫǏɕҮȠƿȹьʊʫ/ƿêˍЦŇɤЁêЙԢÏӿϷʙð¥ώȟ\x80',
                                        'ƣҽϽĬИB:ѤǝǪԊһȴĘΟПϟȔÜ/ȳˆƢʫͻʜͳ¿\xadШ',
                                        'ҋSĝэǣԀȀԗϽ\u0383ʣéȥΠƳÂΩʳɺOɾԊȓǴ;ǶҿχƔт',
                                    ],
                        },
                },
                {
                    'name': 'яНYƁЏΠ&ѡгƼˆýĕÍҌнϊϣˍҊ\u0379җͷΓȊԣ]ԔЗљ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210301:152841.643780:+0000',
                        },
                },
                {
                    'name': 'Ǚ\x88\u0378:ң.˧ΫбtȒΊĨӵϛԞ˪ƾɗɗͿǩϢ΄Φ²',
                    'value': {
                            '^': 'datetime',
                            '$': '20210301:152841.643921:+0000',
                        },
                },
                {
                    'name': '˯ϥĪǲçϥԃǕȄƘŽǰәʆʊĬ2ώɞȻŘĿȔϖƾ˭<\x8a˕Ӛ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        4669435963668315327,
                                        4822522538756166261,
                                        -7676700022449455246,
                                        -9014612947953673485,
                                        -1188213849333815523,
                                        847360686951482378,
                                        -1927465310404269653,
                                        -333371128342270489,
                                        1980397956771294636,
                                        1406734813632233256,
                                    ],
                        },
                },
                {
                    'name': '˦ĦѣБԞƨŭΉʭҞĚTʹÍȭӱˠĶ\x8eδҕч',
                    'value': {
                            '^': 'string',
                            '$': 'ɨт"упˊþ˹ɸÓə¯ҟѴĥǧИÌɘêҩʑҒχ\x8c\x85ƝѦeԬ',
                        },
                },
                {
                    'name': 'üΔǥΊNʎčťгоĳϸţΜĴ\x9aǎю[',
                    'value': {
                            '^': 'datetime',
                            '$': '20210301:152841.644492:+0000',
                        },
                },
                {
                    'name': 'ιˤȩ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ӋțҭѴ˯ΧәɘǍпXԖʸ3\x9cΜ˟',
                    'value': {
                            '^': 'int',
                            '$': -5202275839663887724,
                        },
                },
                {
                    'name': '\x96ΆȷǪƼŪαњϛʊԘӀϪҸɂΆƲ @`ʨΚf˽ɧȳǽȪrɧ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        1993895236975796134,
                                        4651105380050862934,
                                        6298003323689718510,
                                        -4240706315477568245,
                                        5199289405916599349,
                                        9006056199401299492,
                                        -3810282126615076473,
                                        1949303954728593002,
                                        -8751747122246187937,
                                        -612396668051787122,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'eȨ',

            'message': 'ѐ',

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
            'identifier': 'Ŭ\x87ϒǽͻ˰PŞҳʽϵȳЍƋ³ӋȂ\x8fçϐė˦ԓқb҄ԣ;ˈȢ',
            'categories': [
                'configuration',
                'invalid-user-action',
                'access-restriction',
                'invalid-user-action',
                'access-restriction',
                'file',
                'internal',
                'network',
                'access-restriction',
                'os',
            ],
            'source': 'ǔҒ˘',
            'messages': [
                {
                    'catalog': 'өЯˆP(ȑҸǫĩƜύҐĦƍɶϰɸŐȵgOƮОӎɄgҠĔƃʑ',
                    'message': 'ΈuäĴĠŶŊͿİ\x83ЮʫĵɓŽȉǓңЙ˂щΗԝǓŁϴʳɳ˹ɟ',
                    'arguments': [
                            {
                                        'name': 'ûˤɸ*ßɿϛЈĵʯȍkɸԍ}ӹ\xadϐŁԃѶʠѻ\x85ҜȪӍľTǑ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 177045.24921933148,
                                                    },
                                    },
                            {
                                        'name': 'ǶȋʘƠΝӪкҾâĞϠ&ИɣҨʌӮĹ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɇԢϿϼƀ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': '\x86Ӵ\x92ǜ҈\x83ϯѶϣ{σѮɕɮó\x86вǙÏĉʂȁϧġԜϻӘɆҳԬ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ѽɞ~JȟʟɆªŹАԕļŦʾ˘ԦʕύԎBVтʉÀbɼ΅μʬƽ',
                                                                            'µϵԔ˕ӊZī¶ʋHХЪwħȡϯʸāΛϔȑōyĶĮϝ˷ǁ\x88ģ',
                                                                            '\x82R˨ʄήёƸƄǟӫӸɳыѩͶ΄ɥ6¯ӊǺɱȨˤƼԪQҌ4Һ',
                                                                            'ӗ=Ƨq®´\x86Ԫʩķȑ˙Гȏӵō˽ýʐĊŽјзҜƘĝˡȁ\x81ˡ',
                                                                            'Υ\x99ѣҶ8ȗё6[ʰƩӱϙʠ\x8aϕɂӄſ҂QYNĹĳíɝғ·ķ',
                                                                            'χѷŔӁɾʿǠľȒǦӯŷŜ˗©ŕІƙǛˇҺĘԒfƤȨ\u0381ʖŪЄ',
                                                                            "\u0378˪'ɨɘȜйǷɶ]fȓϸɗơεŤƳˡʧЎʅ˲ҚlǅѦĀĳ)",
                                                                            'řɰхДβŮЁAϜŶ\x93˩ǭƴ+ͷӨήѠ]ӺԒĺUʫǥƆԮξö',
                                                                            'ȫЗΝʳçĪȞбĉɁσ*ϵˈ\x98ˆȮ\xadǦԀ˨Ҝ\\ыӾыåѢ~Ə',
                                                                            'rӴӓϥÌїр³ï¶áσϓ˻ʛυˏǞ˼Ϗ±ӰÄˉMȽ´dЫʹ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǁԎͻԥϠƦǣșьɇʶҿԜϭʃйϋɌΪʿɓÅÎĺԊůʜÕ΄ť',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5131563059383137425,
                                                                            -8251221039809714938,
                                                                            -8903971516793795812,
                                                                            -1334854075951632048,
                                                                            -4645040439324643064,
                                                                            2542261587887337900,
                                                                            -5197185462521036186,
                                                                            -5649146353500765256,
                                                                            7607318295079863999,
                                                                            6214447092312531244,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҕқі˧ǼЎ҅ϱƏūĺƩе[ɒ·ňƙȫиȆ˸ŹѾ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¬ɏɍԩs|ǻ\x85ǆǥ˅ǳа҄Ԥ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 44630.42334322576,
                                                    },
                                    },
                            {
                                        'name': 'Ω',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.617116:+0000',
                                                                            '20210301:152841.617141:+0000',
                                                                            '20210301:152841.617150:+0000',
                                                                            '20210301:152841.617157:+0000',
                                                                            '20210301:152841.617164:+0000',
                                                                            '20210301:152841.617171:+0000',
                                                                            '20210301:152841.617177:+0000',
                                                                            '20210301:152841.617183:+0000',
                                                                            '20210301:152841.617189:+0000',
                                                                            '20210301:152841.617195:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ӔˏΉϛ'ʺŃºȃXƌăӔʖ:ҿшԘƧѵҷŲЃýΎˆžнƑį",
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŗѝҬԂǌ\x96ΝÍƉȸĥȁР*\u0379/ωɻʕЅƂʌ²ÒѳĆӿҀƽï',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
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
                {
                    'catalog': 'ˏɚƸ\x89Ǒԧӝл',
                    'message': 'ƍϷϠļčɊӡȊǤЙ«{ѺȓŮìΆȪȖÇƎǔęɲϤϛdƶúϸ',
                    'arguments': [
                            {
                                        'name': 'Ҕѓîαљ(',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.618259:+0000',
                                                                            '20210301:152841.618273:+0000',
                                                                            '20210301:152841.618281:+0000',
                                                                            '20210301:152841.618288:+0000',
                                                                            '20210301:152841.618294:+0000',
                                                                            '20210301:152841.618300:+0000',
                                                                            '20210301:152841.618307:+0000',
                                                                            '20210301:152841.618313:+0000',
                                                                            '20210301:152841.618319:+0000',
                                                                            '20210301:152841.618326:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŢͱѠйȔԘЪRęűÌζȱHƨóŋʽʈ\x8d\u038d:ҿȥ˱Ůǒиӭĥ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŔǲґƜŖ3ΫԚĨЋǤвΚϚȷƳ#¼ήЄƯ9ѱɚЪŃ˯\x8a҇Ы',
                                                                            'ϊɐ§ɒΔʟ+ĵҟjщɃϯ°˱ʨѯƻƓЧɋ¯șxӚŧÈƊ9Ď',
                                                                            'ƅґǍѲӃΨͽХϽ\u0378ïȲȀ+ϝͷп\x88ŷСĲǈȹeыƱԪцҜL',
                                                                            'ÿɈƊϾ@īǛ\x91ȥұ!ҘŤɥƎƈʩǱƝłГɧҷYѤԐāҷÜԇ',
                                                                            'СǭюԬǁŒȈˈЪ\x8ekʲÄƩ˽πφϋÜįǊ!ɝȟԣɯ˝ƒǯı',
                                                                            'ΔƄɬƿȌӶΧԣĉTɷҍψÐ˺ǜѣȐȽʞűΆŨʕƏϲ÷Ѻćπ',
                                                                            '҆ɷǚБϕЮʣџɸǆϩОûÜΤԖӮɖΉìЩωԜŨ[ҤРӇԌÞ',
                                                                            'ǘԡɗʤǯȜѫȻЫɿ®ӀЃԐҌԒĴϺƏѓǌ҂iԩɇӹ3¶¦ǐ',
                                                                            'ǵҗŢɄÑƮГɄАзŗǗuĲŉЊǴϧ˖ѨМәƥ˷\x94AȿЂϼł',
                                                                            'ɱў҈эԄѾȜӄԀƂίѻҏ{Н¶ήѢЛȎнϗѝϭÃĪ½˖ɓϱ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˭ѧѹ΄Ǟˌ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 262501.5323407182,
                                                    },
                                    },
                            {
                                        'name': 'ɰИǙĂÛûЪĚŸҍʔԞѺԂŔ9ԤƆ˧ʎфƂɃШѝƵƎҰӫə',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1033559333386977813,
                                                                            8085994438985466734,
                                                                            -7285676136837793709,
                                                                            722554919767494191,
                                                                            7879170089417605902,
                                                                            962472070278583290,
                                                                            -8074875653136861385,
                                                                            7708381166089645980,
                                                                            1077094174158730643,
                                                                            -5615663246204347979,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƂӡӶŠœ\u038dȅC°ӕ4ȀũTîˍƒгʨŘ\x82\x82ÇχТɧʅѤʨҳ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʹùƊ\u0381Пɘħ;ņϸӨƆǔʚӞȻ\x86ɌыƆa\u0379șƂ¾Ùʍƃ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.619664:+0000',
                                                                            '20210301:152841.619677:+0000',
                                                                            '20210301:152841.619684:+0000',
                                                                            '20210301:152841.619691:+0000',
                                                                            '20210301:152841.619698:+0000',
                                                                            '20210301:152841.619704:+0000',
                                                                            '20210301:152841.619711:+0000',
                                                                            '20210301:152841.619717:+0000',
                                                                            '20210301:152841.619723:+0000',
                                                                            '20210301:152841.619729:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʖ&ǶˀϞŵҀӗϛͳƝЉđʎōƀėƺʀӦҞϔȤǌĭӈѫһ¢ʠ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            24500.62004725942,
                                                                            996953.130490422,
                                                                            7169.228026575642,
                                                                            304975.7416848105,
                                                                            869725.1731609566,
                                                                            281658.57541862316,
                                                                            565119.8082160554,
                                                                            783665.5667131736,
                                                                            803336.9045168338,
                                                                            827114.3870853599,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʪșĢîѮGǑө½ŎéɽʹŸҴӎ¨ȳǐƷÍѵԚɠˁҫчɮŹʝ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǜˇϱ:ʤμǉӸΪƤβĞʞϘ˵\\ρĕǖƲƻӨʡІŨȉ\x94ҽϦˣ',
                                                                            'NĿӇϯЀΣBȁĢϸÂ+њԞǎ\x9c\x8dˉÆǕƞŎȶøʶǣúU˷Ԉ',
                                                                            '\x9eѴŧʑĴӰ\x9eѦȵӍЮRƅŬšˤˉMΣő҂φțͻˉ\x89Ē˕ϟџ',
                                                                            'ˠ\x8c6ˬˌ-ûƻԫCǲԚʰȔƘĊù˄˞ǽ΅ы\x83Ԑӟǳɵgȑd',
                                                                            'țʦνӦ˶ȗɽǰŚʦ¦ìǄȲjΨŠĹȵ«ӼϦɣȂ˾ԛˏҚɌљ',
                                                                            'Ѓ¸ŃӖĨǰϯmыũƔҫѪʤӒӞӋӼĭЀЬ˝.İ\x88\x8fЛɿɦɵ',
                                                                            'ƦęĲÓÍǥʈȳҀ*ȏҬѱΆˌôԚϩǱɛǤʚƝúǃêŐϯӹΨ',
                                                                            'ңһ˙ҹÈ;ԦYŁɠ \x8c2¶ϐӜӢӻҙԗ\x9aǙƣƗΟĔƌĈɉĂ',
                                                                            '˝ĩӼ˟ʷҪЃCғŰˠɐҺΝ˚)ʜȜԂĺØέħҦɂˑҪϯ˨ʂ',
                                                                            'ĤотӔϘƊ¸ԫ˜ϾӾŞȯɴ˕Ӗɭ<Ŵ¹ҥtϐáԄĉƧҮıτ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϗɋŧԤ҃ӘәɵНʓĴư¹ˣэǗBԕѰːÓ,ɠѳƸƉ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3882259554091245871,
                                                    },
                                    },
                            {
                                        'name': 'ԁѪķςΠòԨÏ˓lŭ˴ʆζȬϐĎ\x9aſʵЁǋ˃',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152841.620823:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŬɌºαΐ;ѬмʇƩυ Ӳ˽нԘϻˠѾΜƳ˛ċϺİy\u0379нĨʪ',
                    'message': 'ƯүΪǙϞѤǲƻʼÓѶŒӚǝȮÒ\x9eЇLĮ@Ȝғȉ°ÿǴȹɟɨ',
                    'arguments': [
                            {
                                        'name': 'gЂǗĮҝϺɆĮ"ȉΑĝjǕɽӵЋάɧѠԔɀõȜĵДЗЁӢӕ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʹ0ҠƠƔϓҪӏ\x9dyƸєȌˣɯ Õѐ˴ΌƭӜĩøːѰʃċԙѡ',
                                                    },
                                    },
                            {
                                        'name': 'vŗvʫҶВĮԉĤԆÜȦĈԅƠЅµÎϪ˩ӒÎȈϱġɵʤ҃ѝɊ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            513084.353258607,
                                                                            142265.68880233038,
                                                                            173959.7377551496,
                                                                            750126.7675682744,
                                                                            771145.0395510205,
                                                                            752669.8836386516,
                                                                            225897.79249544442,
                                                                            594204.7705689403,
                                                                            954917.3048032753,
                                                                            53932.92218873519,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ć±ӯrсɼ.Ӡд',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            77518.94531128745,
                                                                            374876.83857403026,
                                                                            358485.8442090953,
                                                                            541291.1644470668,
                                                                            51435.679673383216,
                                                                            144367.36441227677,
                                                                            952065.1315295286,
                                                                            438732.64027948305,
                                                                            864273.4176833235,
                                                                            961917.8854338771,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɗΕB˥ąðԘΙđψӆĩӛLϰўΦȍɰN)åӞΆΝ˾Ƴіҥǒ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3811661976768012159,
                                                                            7315374849744195259,
                                                                            -2184547663499162636,
                                                                            2289074814354216598,
                                                                            -1336085217940537960,
                                                                            346570364984026883,
                                                                            -8433514752277010904,
                                                                            3271501852012482415,
                                                                            -1397390123192587288,
                                                                            -8034001583843411469,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Кǭ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7018100121730253768,
                                                                            -3176733707871892800,
                                                                            5248614506068760981,
                                                                            -6774961506048169453,
                                                                            -380740913175583338,
                                                                            3434228566068074308,
                                                                            7388666148390993816,
                                                                            -6660678398585225834,
                                                                            -1251143610402955676,
                                                                            4076175627336034037,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '°ɳˤӱɱǒ]ȇĠɢ½ÑӘüżBӬɥӹ˙ίίŷǷҩ\x94´ϦҮǂ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            974106.1082717297,
                                                                            902731.9442325615,
                                                                            223273.56963545416,
                                                                            -11414.564494476726,
                                                                            774241.6225052222,
                                                                            379279.3840096074,
                                                                            475674.73246270616,
                                                                            384958.97092611465,
                                                                            334936.3445332838,
                                                                            96088.34497286688,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Š/CȩˆȨȅҽ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.622705:+0000',
                                                                            '20210301:152841.622720:+0000',
                                                                            '20210301:152841.622727:+0000',
                                                                            '20210301:152841.622734:+0000',
                                                                            '20210301:152841.622739:+0000',
                                                                            '20210301:152841.622745:+0000',
                                                                            '20210301:152841.622752:+0000',
                                                                            '20210301:152841.622758:+0000',
                                                                            '20210301:152841.622764:+0000',
                                                                            '20210301:152841.622770:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϦdЇƗ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1672170964159655930,
                                                                            -2612352773962530629,
                                                                            -3796364010447537320,
                                                                            -3571973635661077417,
                                                                            1813289251069415325,
                                                                            1467846575462457748,
                                                                            8017048280567201872,
                                                                            -8134246154858861399,
                                                                            -4952238907503709971,
                                                                            8796196345525995635,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΎčжѲ~ԗéĔԌϥʡOɴǦǱғ´˴OɣmӛԏĀǝΔǚƦϣΞ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˄AήɊϧҨͳΌпбǖԨ<ƆӨƉ˳Ӱïї˖ȼ\x94ǗáHǋτƬƵ',
                                                    },
                                    },
                            {
                                        'name': 'ҭ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӅäўӫĝфǘϴϷѕԞǅϨS¼sƥѭŉǩШʥČΏǙȃМ¡εƁ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƓϹјЀĉыʂԊʠӗŕϏӝģĚɛϗǭǺØԝЛǬҸΧС˝˗χČ',
                    'message': 'ƆˢſǒǓԟŤʼ\x84ťſșǨƼ\u0380ɺ¹ôϵӍYɠyцԂϢlϊͻ;',
                    'arguments': [
                            {
                                        'name': 'ąΛʟƉ×ɢ˗ԎдÄщʪğ"ť˺˟ϡюȤƐP\x91ӷǰǳЏɠ\x8aӑ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԪʓɧãʪҢҳуĄ҈\x8bƟÚπɨɇʘĲŝĲǕĆɆŔфϮԈʗ~Ʌ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            31124.10221544496,
                                                                            712833.6211411203,
                                                                            358028.9799051199,
                                                                            298320.4123864248,
                                                                            333394.90928154124,
                                                                            535234.1612101161,
                                                                            654324.4796548617,
                                                                            854104.818784808,
                                                                            -6647.292226610196,
                                                                            356205.89463809953,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĮŐԎǺ\u038b',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.624282:+0000',
                                                                            '20210301:152841.624297:+0000',
                                                                            '20210301:152841.624306:+0000',
                                                                            '20210301:152841.624314:+0000',
                                                                            '20210301:152841.624321:+0000',
                                                                            '20210301:152841.624327:+0000',
                                                                            '20210301:152841.624334:+0000',
                                                                            '20210301:152841.624341:+0000',
                                                                            '20210301:152841.624347:+0000',
                                                                            '20210301:152841.624353:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǫ˘ûǏ#Ҷ҄zƵ>ƖõҔƕ)ѓĀϤƢԣʦΊӲǺˏбĬӯ³B',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            397267.37753677164,
                                                                            632786.3954111778,
                                                                            558425.8134685735,
                                                                            500755.5771462476,
                                                                            350802.0705276892,
                                                                            -89203.38201041026,
                                                                            492472.0392988222,
                                                                            727980.5212045063,
                                                                            11664.152206332408,
                                                                            143035.3218630528,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˜ÀϏǡɟǮʡƴϪǲŸ¸ʓǖ\x8bӦȽƹȸʞЩҼˌӈ\x9dν',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҽΌЦěъĪѰʔĸӈϤwŋšҊԮˬӴĞ˕ɑɩĉǼȜԟJ:ϠŚ',
                                                                            'Єċà°қԪƧ˵úȝM°ʘ\u0381УŞȝʈɧԪΉǑʒn´ǫľǽ\x80ź',
                                                                            'ǴˊÂ˓ћѷУˤҥɷÆƆʛά\x8eёͶÈ,ԮѿʛǥźʆԬԅȊ·ζ',
                                                                            'ίҀÕʈҎ\x9bȓ¤ɔˮƒ;ЍƪɳĢƱͿɜƎϼҍƤO¨ʾδ҆ʾ˽',
                                                                            'ǔʹå»ǡēӕƘЪҋɄɱӆӥĦǭʂàĄQеПӣÍљʼĔцπˍ',
                                                                            'ƶȳñɃĒƉЈƚПô˘Γ®ɂ҂ϩЅɦȍ˷ZʧjЂśЍʧ҅ƔØ',
                                                                            'ǙʈЛɎ·ǱǊԤϨҞұа¿ƥϣӥÜàŎҿFĤ¢Þеӡƹԧа:',
                                                                            'ӳɎѮəíŽԒ\x98ҨŨϞϯ\x9c˙ʹ\x9bʿҀȸѩÎťВİҀԟϵưϾѷ',
                                                                            '\x8eƊǍJvԬʞI\u038b˗ǪtʪϏѢӪ,ї×ʍ\x96ïӨpUӝԡɤбǐ',
                                                                            'ɀŘȚˮɘĉΦȃѺɦăϡǨшӷʯ¢ç$ƳϏЋ\x7fŔа\\ʺźZà',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϖ²õϣήѪěòҾЈĞѫыϕ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ЊίԌ˞ωкӼɈғɒEʳŘǟʹɛ`ˎԮʦѲ˕ѷȈ\x92rԓƲїɽ',
                                                                            'ӞӡԤÃάňϖ¹ӁǗǓɏ\x87ȳѣΓЧȚCˏRɰ¯ÙʀԨʲθȜӋ',
                                                                            'ǍŃɃ#ɲўľҺҹʨξðäʣҩÃʩʞ~ǱjϏƔӬˎҖқʌˤϻ',
                                                                            '˅ɵǈџϾ;Ѱγӂҋҽ˭Ŋù~ӟˤ˚˟iɿ҅ϷŬȚʟȇȈɢх',
                                                                            'ˢǣǜ½ԋȔʬԂәȷӄѨϯљϝϺӠ¶ԐЄʹӕǺKԕëҴ÷&À',
                                                                            'ҤκŲˁŷϢΈҫѴȢÐĽӣȠʳĎʪǱśΪȼȽҹYͻȽŭĚÜʯ',
                                                                            'ч°ʻďѼ«úӹǐ\u0380ȩΖ©ʐɲ*ԛʖɠпǿħҫȁćȷЎªͰȯ',
                                                                            'EɿϡşŸϚȕɢĜƲō¾ϟβӉƍʩѼŢ\x96ňҚѓȔʻϦВźʗн',
                                                                            'ħιԀʞʉίƄ)тĔƜЛÉĊĴɘ0ԋȁêѥˬƴİ¼Ʉƺǭǵ\x9c',
                                                                            'ΦҞůŪpϝρŞ\u0378ƁύҚҫҵĿɮӿ¿ҴɁҩȣˁʊΔ˚ǀҵƸQ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŐʢɃˈūϑÓƆɅȂëѫQ\x82ǐφÍǇƹџӖʳұǲ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5651916259153705232,
                                                                            1352281455545910461,
                                                                            2698165699802376099,
                                                                            -6075800607923408765,
                                                                            8761113169053263202,
                                                                            -9157689817455783588,
                                                                            814501613727938982,
                                                                            7244380634280916729,
                                                                            -3868555792041794387,
                                                                            -6701865497793120829,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΠÉѠͿ;ʑϋόχҽԄϵҹȲkɌ=їрŴɮΠƪȗӬʩƎƜҠD',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӬǐНϣӃÆɫϚҥйϷҗœƵĘСµ÷ȑԎȎЕ˱ƻÝҪҖԎǅϑ',
                                                                            'ȩ´ɏǑ\x9eŻѶЙuŤИЀ˸ŚԠMеҐ˟´\x8f˝Н\u0379~Ǐ˽ʱƫĽ',
                                                                            'ҸqˈɸDõϡ˫L\u0378ȿǪҒϳQÄԢЕŮͱЦĚŞăđӼyͳʆn',
                                                                            'ĠJ?ěǏТӁōŤԣԏχ˴ҿˌ£¿ĭǃíԍѝ΅Њӟˌϲ\\Ǧò',
                                                                            'ҔώĵwϚƊ ıɘҴӭҫſЫʼϋЪ!ЈǚɈʾbʘmŇ¬ơϢӕ',
                                                                            'ďȘƼʒNʭδӪȋΑλӮ2ԡ˫ȘԭɖĬЖϞǎѻԞɖЮ˂ΰrȧ',
                                                                            'ƦͳǁoЦжӈȒӧºƬЧɅƏΨɮҒҎ҂ҷʙˌʁ¢JVǁϔЋƗ',
                                                                            'sȳ͵ґүŗƅʽʵȌԟǹˬӒ5ҞÖ˰ŇԕνΔΩϲď҃ϒ\x8fӨǳ',
                                                                            'ҼČЋĒӂè\x99ЩƿӿпЏǹǊkί\x86ŊȾįůîʘԄĸˈöƁʘĐ',
                                                                            'ʟ+ʴƼ¨Ϯ˛ˠ˗1ʲѫӳʫāПѺɤțҎѵÑŋӤҡϬJ˸ʎ)',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĪρЈӡȄŒϪӡqɇűϏҪ˂ȫČʘŔԪԘҷ\x9dʹ\x81ĻȆȃҔ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': 'ѪȂ\u0379øԖʁӈȭŤ\u0382˃ƛďÎTĲμtŨƉήHȳѠɛ%ΣӴњʧ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            441941977258292365,
                                                                            4729937631343681423,
                                                                            -4033498469468283420,
                                                                            8684899087344845024,
                                                                            -987978755846424741,
                                                                            1116288505367446118,
                                                                            -4923325107281060638,
                                                                            106712440535152349,
                                                                            -6099840558141670050,
                                                                            8425285292908264538,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˥ѼʲзĒƫ\x8bσȞ˵ЕɄԘϢ\x92ƞ¹ţɖţ',
                    'message': 'C$ҋʨßшǐĂЂ©éȸΙƝɄΈȕAÚΥш7εΟΞҎǧȎΓƽ',
                    'arguments': [
                            {
                                        'name': 'ɁӧџǯÆĹӭǫǖÉʅ˷ӆԈ5Ʒ҆ԜŐß¹\x7fʊӁǍԥ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'јÃ-˄˨qЎć˞ĊșҏґĜѶӢӯȇҟ˵ƧĜöҩΦʖϩВĽх',
                                                    },
                                    },
                            {
                                        'name': 'ʟŦĵɻњɦĆƤѱ_ǐǿҴȭжɣϠǕ¸˱ӌȔЮĽβұ\u038bңбɋ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĲѝƫɔιҙŇfµnʌЃӇ҄ӭûκŅϑȘ˟ǐӠŬɳʘƗȀќ˂',
                                                    },
                                    },
                            {
                                        'name': 'Ĺèʊ˂ӐҲ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152841.627563:+0000',
                                                    },
                                    },
                            {
                                        'name': '#ǤʰĲЋƑĴҎˆφˏ"ȗȮˇ\x8dƙұӂ+ԣÉΪxӯЭ\x8bǖ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            723666.2451623307,
                                                                            442678.18151589565,
                                                                            759345.98575597,
                                                                            157927.44587402238,
                                                                            786373.3183667599,
                                                                            463019.10982602055,
                                                                            227788.62212619057,
                                                                            257037.12307186465,
                                                                            657869.2644299451,
                                                                            138219.31133726105,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ċõƾљύҹԀʵӍŸɈǚʎȟпŤ/ǸˁʗўЏǂǺȢăȗ˄Ǹɨ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8438747747886140896,
                                                    },
                                    },
                            {
                                        'name': 'ҹϱʽʟĈĕӢнɳҡ×ŨˢԛӋȍɧĪȘιʺǇǉͰŔ\u0382đϬǰ4',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            342689.35138947633,
                                                                            606832.0130460174,
                                                                            560345.3839806372,
                                                                            821927.7152545771,
                                                                            78983.24633935143,
                                                                            193436.7537324581,
                                                                            548282.881811595,
                                                                            743983.8967587999,
                                                                            486387.66120774474,
                                                                            40943.527596210915,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĖɣƂ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152841.628309:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ςĆËɱǺ³ʣϣvkŶ½ҌɸЪ¼ƴrʰϢ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΙĳʾȲԄ\x94ˁɚҭóүɹЁʓЦϣӊϗѿԃ\x96ɕԢάȼĊЭɞѼԭ',
                                                    },
                                    },
                            {
                                        'name': 'ſѹŅɠJԆϹãйȥɣɤɪйȥƴЫþȖțμ¡ӣӢ\x8b',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.628595:+0000',
                                                                            '20210301:152841.628607:+0000',
                                                                            '20210301:152841.628614:+0000',
                                                                            '20210301:152841.628620:+0000',
                                                                            '20210301:152841.628626:+0000',
                                                                            '20210301:152841.628632:+0000',
                                                                            '20210301:152841.628638:+0000',
                                                                            '20210301:152841.628644:+0000',
                                                                            '20210301:152841.628650:+0000',
                                                                            '20210301:152841.628655:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'дĺÆľˆΊġǜ˚ǹчǲӡʂLƗ³',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ńıθĸςǒʅр˃ƾāӪî²ǂùƵҎґÐЄфʓǬ˨ʲžȹȟM',
                                                                            'ƏЫƖ4U҃ƵfҞɯǠʜ˷Χ˼ӛϮЫѝԁ҂˵ӅéɌԄÔ_?ż',
                                                                            '҃œБΎЖЏСИͱ7ȝӷ&ɍƲųҀƭҝɝɲǥѽкȧuÜҨĥƌ',
                                                                            'ϲѣӸɇфòŠ:ˤԔƈ±ЯдѫπЇùŠǯʥ˲ȯǝ҈ΒƎĳάЙ',
                                                                            '˓ʊɍūøϠĀӠÍ]ȥôƈȤѵГǋɰˎӣҁøνƎҕԟѧÉŀǛ',
                                                                            'íѶʫŊȇҡʘ~Ь\x97˸ҾɦСвέKԟ<9ƨƑ9ʷA-ÀӳϘк',
                                                                            'ĎĺfǇòЊĄπҝ&ưЭƻѰHʣΥΆπǵʩӐŜ_ӺɟǦʹŨĢ',
                                                                            'ɱұлÔӌ\u038dňóſɸӲˍ¼˭ʰӸŶҴǶÅǲȦĺΓŕ:dУDÓ',
                                                                            'āԭ\x9bϘҽ¿ʋət҄ōБeҷЪ˕БĬˇÏ¦Ԛӑƻαʶϵɪ&Љ',
                                                                            'ғÏԠśΔďӣƕϵœȞϚ\x84ͳǊԦQ/9ɽђӤ҄àȾǃǗӥѰҟ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'әκ˳Ľ҈ǾҖÀȼ;ŲǛŰáӍˡ˂эǛҐǯûв·ǍχǇŻȁѵ',
                    'message': '˻úʑлͳϚϟʘ¼aǲ¹ŮÔóèΟɤɒ˦ϞǗŋȬК˴Ӡ:ćԫ',
                    'arguments': [
                            {
                                        'name': 'µOѐĆȏϳõǠφҙ¼ҖјԜʂ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 304138.04769825144,
                                                    },
                                    },
                            {
                                        'name': 'ĪЗČ˨ʗχӪɁ\x8dҏ\xadӦʦȴϋ҇\x83ΜÄ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǹ·ǤŦІLÝҒ÷ñɱЬƝǥԥ\u03a2ѭѓѱӣ\x8fĻƬɶǧ_жϿȃH',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'џȽɑΜΖ҉ƂЁнǟńϋԔɄĳȇïĵĜƭńÒŪɼȆʨГͱǵц',
                                                    },
                                    },
                            {
                                        'name': "ɰ˪ďɓԀƆɨӂƬҞȋ'Ė",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5019821181886134176,
                                                                            5460979109227833429,
                                                                            5937927662668935040,
                                                                            -4034373186504480830,
                                                                            8390102706944222570,
                                                                            -6458753315253488267,
                                                                            8981190517768642501,
                                                                            -6040420444232907684,
                                                                            -7465325513210099595,
                                                                            7982986948221249194,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '·ÇˑƮʷɱŌαɰҢƛpЌƥɨǉLűԜ\u038d²ˏƕҳϩДʸӪҚʴ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152841.631003:+0000',
                                                    },
                                    },
                            {
                                        'name': '˦ЫϪÒϿxȴŃ¼ВРÒ˸/',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'œӋȉћʪƹӹѭөԑԛȥ\x80ҤԍėƬHʌ4ԛˀԑѴ˶ǺΖwʒĐ',
                                                    },
                                    },
                            {
                                        'name': 'ν\x90żеɃȠĢɯɘɧđ\u038bԕƺΧ;u˻ѠԈ¡ǆȶӝɥΝìǼƋÁ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152841.631349:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɏƢƸђҖàɐϬƟ±ıƣǕǆ\u038bϊå\x96˴ȡ˫ҭɛȡчʮčӴћ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            257867.30855703395,
                                                                            -97562.65027424667,
                                                                            781628.4794836809,
                                                                            262910.42041620176,
                                                                            918170.9908009861,
                                                                            262665.44702496135,
                                                                            731781.1839105431,
                                                                            490834.67787190806,
                                                                            677033.7668099562,
                                                                            459054.58480953355,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȧƌъ˳ʲȲźˉӮˈ;Ξǣĸ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʮӏĚǘÊĄΤɩЯЃÉβɱЯӯѪ˜±ŉϋ{ӟяRҼqƔԞϓ˄',
                                                                            'ĺϚЍφͱ˅ԥӑћԧԚńŹˮǲѶ·Ǐ°Ȉńǉε¦ɗəȂTÂ\x9c',
                                                                            '¼žɧț]ѐѠȋΌкѐϤлҫƧ½ďʝĵȇҘҝ˘rїѵр\xadQù',
                                                                            'ʵȏʪĸ9ѵǜӧѭ˶ɧ\x90ϬВ\x87Ы\x9aӢʯǌ4ϵSʐʎɣˌʲƥԍ',
                                                                            '²чȁ\\҉ӥȁԑ2зƜɺ˛ƣɚ˞ˆ˙Ј×ӏʈƽȻҫΞˋѲɫτ',
                                                                            'ʽȒFˏȾ´ƋԛľιɨӎYѮʀ°ˤpĝɡӏȕʧрȃĈу(ɑ#',
                                                                            'ǌʹ˭ϿяӌäʘʐƀҞB\x99ӮϗʵěȓԠΛńӄϾ\xadǠā"Ϩœԣ',
                                                                            'εħɘї˳Ӧ˛ʆμӦӉp¤ЌǓɌųȑɲ\x9bËäɱәԩ"˄ƕƳÄ',
                                                                            'Ӓԝ*ұɿʲѯӲŠϘʊѠͳɌǀ\x97СʊƕҟÐ¼˧vȮ%ӼƿѭҨ',
                                                                            '9ƚѨͷlóƤˎˡͺ\x8aŽƵɑ/ϱǮӿƧԘĂuΛυţБʸɀѫЯ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȱϬ+ǯȊɫĆõƏ-Q`ɫȘφ¦Õɰ҃мʐ7ȴͲTāʢǄ©Ǣ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɏѢ\x8d˟ʌӉѡϾӍυŀˎԒеȽǌʬ˽˖ҋң<ηӤљ;ĒɇB¶',
                    'message': 'ʶ\xa0ȍ±ѓˊ˵ʪʥ¯ƾŮЌлɩĔİҖÎӵɄǹɜʍѿŷDǕȿʲ',
                    'arguments': [
                            {
                                        'name': 'ʕđäŐˇ¤ƝàēŚМŷ\x9eӱ˨ѣŻΎ҉ǈѬ˨ϡѳǪ¢ȗ˖Ѕо',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 344535.06543905975,
                                                    },
                                    },
                            {
                                        'name': 'ǫʡƈOΙʭȆȞԌǣĩɈ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 647326.6968564638,
                                                    },
                                    },
                            {
                                        'name': 'ÄӺ4Ɔʀ\x8aŌˬɼțìˆŇβ˯B"f¹ҮӭɬҬĢ˃',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.632891:+0000',
                                                                            '20210301:152841.632905:+0000',
                                                                            '20210301:152841.632912:+0000',
                                                                            '20210301:152841.632917:+0000',
                                                                            '20210301:152841.632923:+0000',
                                                                            '20210301:152841.632929:+0000',
                                                                            '20210301:152841.632934:+0000',
                                                                            '20210301:152841.632940:+0000',
                                                                            '20210301:152841.632945:+0000',
                                                                            '20210301:152841.632951:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˘ЮѴ·ǼŨ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152841.633153:+0000',
                                                    },
                                    },
                            {
                                        'name': '˜ŖщġͻбɱǦǵʬϲѷ[ɆīƮɜћÉ4ɵÒӟćȟԔƆƿ]ƥ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2725568238982628656,
                                                                            5941651816597791689,
                                                                            -5881543826850698192,
                                                                            3561143085824129455,
                                                                            7376656719790560474,
                                                                            4736419656639079752,
                                                                            4412775910112615181,
                                                                            6822965153787877954,
                                                                            9118211497793398823,
                                                                            7253489190647035680,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĈÌƄԚ½ʡċɁśǌo˾#n˨ȌЇ/мŘˬĳȧ˦ѬĲǅ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ͶõЩƫŶ|íӬȡ\u0381ӀŴˊÑ~·ØсЀĵƌëԫӫϝŨϊуɳĠ',
                                                    },
                                    },
                            {
                                        'name': 'џÆһȋǮƓѼԝùҡÚѲ˽ʭԠŘ·ҼΆҏΠ\u038dƣӏϏˤƏӏ}҃',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            888676093146653564,
                                                                            7677114984697357253,
                                                                            -4921227541999907997,
                                                                            1370342910404735339,
                                                                            -8841297259215691730,
                                                                            6658358543556762603,
                                                                            -7596686088350982800,
                                                                            6024774704769573846,
                                                                            9017208684625795835,
                                                                            4865186793084961087,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ğѵ!ɇȖЖςѵǣ(\x86˜ԨaϞ˘ԬʶԜ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4113781608638729873,
                                                                            -4613079790648342650,
                                                                            -2616048527666261975,
                                                                            6756506677980708592,
                                                                            5495010327474528373,
                                                                            -8958525277175931978,
                                                                            3721728778094652220,
                                                                            -528892968065950185,
                                                                            -2841618590234112850,
                                                                            262416658694877369,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǕɔǢԋεzƉȜNǐɿʔȷѐϠòȋϕψтҋҠʐƚǴˇÁųԃұ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152841.634114:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȾϚäΦϐя˲ĕƪМ¨îМĎԆɃɏǢĶҬԦԞTƬ¦ɂǑƑĒɵ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 756741.4425746145,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ưϾѸϢȠΗŤɨȇˮҰŹ҇æÐɼóaĉԪǗ҆\u0383Ӫ¸˗ÚΫϏ\xad',
                    'message': 'ұі¶ҸǚӖӃ¬šľɠӧÜЅҸ»ь\u0382ΪƯˋӥǆϸʤ$шgłϨ',
                    'arguments': [
                            {
                                        'name': 'ĚшϞɱԚ®YѐxȝҼЩѫ\x86e˸ĘƌǢ˳ºɡƮЯ\x8eì\x8a˱Ԃό',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'тő\x88˜ÊɲБɔsɮȕ±ˇùǧ\x93ԄΉϛƐ\x84ȐŉeƀɪɏƉͳ\x82',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'жȪoӽĂԜƼǩΗԨҟéȞау¯ΗӇӿƨHɌћαƍɭ?Ģѵb',
                                                    },
                                    },
                            {
                                        'name': 'ɑљҭҼа¢Ĉ˪ʶȈg\x89чс1\x89иȿӖñЈԓǼèĊτҭƕÜ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            980046.4592093984,
                                                                            -16176.98367937615,
                                                                            800126.9199550713,
                                                                            750558.7578949413,
                                                                            481020.39678319346,
                                                                            127606.68950638064,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҝҺΌģ\x81Ȇέњ\x89ΉԘÓ×ÜӌΒÏӀʸŇО˅ǣ҆ǽŐÎҽ\x8cӴ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            295878.44149156765,
                                                                            389931.75144343975,
                                                                            171865.7146012248,
                                                                            480928.62015103514,
                                                                            775836.8579372702,
                                                                            464224.10137353535,
                                                                            515521.27784520795,
                                                                            853935.9839476765,
                                                                            234109.94661403476,
                                                                            735264.5002503542,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƅʉѹцʑŉ¡ΩˆϤԂԣÓ\x9c˽ƛӵѼςѹȂгūŻ϶ĺ˨Ơ҈ʟ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǊВķǀӔгI\x7fԭКƄЉͶƧȜįũрĆӷ˘ÞǞрį©ɯҐ\u0381ԫ',
                                                                            'ɇ\x8bӳäÌˁʚǮΟɕϱ\u038dӅşŔԓϨәȌʿԬİđʓϬЬҋеҤ\x89',
                                                                            'EȾƅŧʏҽжІŔԈƎһԋȚяӅβĈWɞ%ʟjˣËąҋҚƝǤ',
                                                                            'Ƈ҇˸ξӳ\x97Ф\u0383ɌǣрНӯϧĄďȸΰѣϫ\x8f.ӠҰ}iʽÊʎ5',
                                                                            'ѤӮЁʓˢɵǘɗȤŀðЇĄ\x9aĐȉHΑәʝѾɦ҂ΐÝȨ\xa0дҺ˪',
                                                                            'ʔtżéɹѶ\x91Ĝ§ơåƣΪțѼ\u0381ɵS×ҤƟ˝Ϸʆʝ˒ЫƠңѧ',
                                                                            'ȓȲ\x8aĴƣ½ƫХĽʢϠѦоңӣԙǇĕžƌbɞʾɧQ1ɘӁŏʵ',
                                                                            'ҮӁɨξтȉǡÌԤõi\x91ƀφĦЩĠ\x9dҫȜΧʛӤЕεÎȥ2òґ',
                                                                            'R%©ʽǎϰμˤҔћҝѨȎɷÕԭňɵжѩĩԨшƌϓйҔҐЭј',
                                                                            'bϫёɺҖǭβ½ͱԞΧϤƒġʇ\x8a\u0378ʤŤ;ʖѸʱϧҭȂ˚\u038bѰǾ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȝƥʰāөø\x88ҥˎƟҮͿʇ¿ʼѲ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ÝƸĉεʵʐßӤԝρ\x81ʴТI',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            435237.25501842203,
                                                                            486521.9466668753,
                                                                            162446.83038126281,
                                                                            -15218.605976755847,
                                                                            570292.2667882021,
                                                                            644891.7957801551,
                                                                            180315.51329509506,
                                                                            675753.3640879054,
                                                                            796422.969587128,
                                                                            799056.2653583516,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʾÎȴзĲρɂħÚŝωҶ4īĥͲǵ\\Ȭ˧ŉɫ˝.ϹϝˬżĞ˔',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.636359:+0000',
                                                                            '20210301:152841.636373:+0000',
                                                                            '20210301:152841.636380:+0000',
                                                                            '20210301:152841.636386:+0000',
                                                                            '20210301:152841.636392:+0000',
                                                                            '20210301:152841.636398:+0000',
                                                                            '20210301:152841.636404:+0000',
                                                                            '20210301:152841.636409:+0000',
                                                                            '20210301:152841.636414:+0000',
                                                                            '20210301:152841.636420:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ûŌӑƅњѐʪqԘԁбŞ2ƒӚʊ`',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ЫЗ\xa0ϢѫӡʬèĐğüɀȴά\x97θʿËОҨǵъYŃ.ĉЫЧȟV',
                                                    },
                                    },
                            {
                                        'name': "ΎѸǝҁѪʾԎϚȪ'õ×ƭɌŢƂЪΎϣȷkһʒ¾8",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152841.636770:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ό.ΓӓΎ\x9bîȳɁԋǥηÀӢûįκŖʰϷұŜƏəӕ©!ǑǗҒ',
                    'message': 'ΕЀƄʻԃ·Ŕ˲sϧ>ĦÑȆҖΰ*ɯɃĲ\x9dÇҼȕ§\x84қ˽Õк',
                    'arguments': [
                            {
                                        'name': '¼ŀÙɻœ҈ȅƗьϐʼÓƓĊЅǃ˸Җʧ˓ɋȂĊ˘ŉВΉµ˩ɧ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 568883.3763354431,
                                                    },
                                    },
                            {
                                        'name': 'HƇΒɑń',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -84487.93536046374,
                                                                            940401.6270433316,
                                                                            731843.7458811902,
                                                                            754956.9683956096,
                                                                            708077.977359281,
                                                                            745866.8230768273,
                                                                            -83448.69058025564,
                                                                            530417.012456819,
                                                                            585823.708922301,
                                                                            364877.8382507044,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Үҍkɳ1Ƙ\x7f#ȾʔƗԔʵ˟ȓǐ\x9fҫΐʵʲϢŠЈҟĈ9ËԚś',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ĥ\x9eΘкŲΞÉǳ,ŴĞϻǜʻћȐˌĘĴӃ\x8bҦдϴԆɲvχƬͲ',
                                                                            'ʹӋΊ˟ǖØȷùßŦҤôѹђʦǝ.ĒˀpаԓʕʞȕЖǛͳ\x9cv',
                                                                            'иƱΫъѽȣƃĤ¾ÉѩǨОӷĚŎλȲȈʛáӝĎǿϕÁёȚмƚ',
                                                                            'ҥpťАʭöԤɃҊϫÜψϐЅĩļӻſӗ!ƁɸҒѡβԐǋԆǘҩ',
                                                                            'ʳǞʥmҢƦôŚζбѥρ1βɶʄ;ʸԜʷƭЋ²ȋſͽĿeǺǊ',
                                                                            'å˸ӖȏϬʆƷYˑӫȇŘӞϚ]kҖӻԦ҇.ӝʵǿáú3ƟԘЇ',
                                                                            'ԋɝ\x90ŜɟԈԕʍɆƻͶƳȥːǓƅŚͰʘěæЂūҾ͵ϔ¡ΚЎÙ',
                                                                            'ɆѦ"ˈcґ˲Ɓ[ʭϳѳЖρҫҳԭ\x9eѪΖϐҥʛɁǦҿԩĞxќ',
                                                                            'ɨƄʖʴǶΉ˴ԃЕŵǚΰɳЎЦɟϯĦϫͳ˯śПхΈȮʣˬ\x8bĪ',
                                                                            'ļоʀ˯&ўɜԆȼψ,ɎѠŝΎǚʍ?ƫԃ˴ΏˏåkӾɚĊϛǊ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӻѵϿӉʰȈϔ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7961810948807981713,
                                                    },
                                    },
                            {
                                        'name': '˧ɫĺǮȎʓ"ԍɼ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2160725880930938498,
                                                    },
                                    },
                            {
                                        'name': 'Ʈȅ\x91ӗѹʽ˃ӍΆьА˩ů˓ǥӶrʳ˅ʾÀŁԡ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5614224475488171673,
                                                                            -7309250691437731242,
                                                                            7316106705277354406,
                                                                            -5286974381714483860,
                                                                            -7363555091458348221,
                                                                            -6773329933499242421,
                                                                            -5661360933941186165,
                                                                            3771845341266335147,
                                                                            5942363652116509585,
                                                                            -7301250040091800922,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ıŧП;ΚéͲӟƮЩԊԛĨԑȿͶ-ЖňԁƷȊıäВʃ\x94Æˎä',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 381945.5684346656,
                                                    },
                                    },
                            {
                                        'name': 'ӿÔѩĺӡ;ȂǙԎ\x88ζğȻȻЯɜƫϔ`śɏɎɖƎÒ¿ШѪæß',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.638512:+0000',
                                                                            '20210301:152841.638524:+0000',
                                                                            '20210301:152841.638532:+0000',
                                                                            '20210301:152841.638538:+0000',
                                                                            '20210301:152841.638543:+0000',
                                                                            '20210301:152841.638549:+0000',
                                                                            '20210301:152841.638555:+0000',
                                                                            '20210301:152841.638561:+0000',
                                                                            '20210301:152841.638566:+0000',
                                                                            '20210301:152841.638572:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѵFĒςƭӠĴŷoӀº',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ѡʅԔǯӲЦʇȾ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8167147030774101120,
                                                                            6736775885172736175,
                                                                            -7648963277064747404,
                                                                            -4041474906541027769,
                                                                            5979328414982449357,
                                                                            -841132065903687452,
                                                                            -370455516081306290,
                                                                            620162147456601442,
                                                                            3653395571396645622,
                                                                            6739599854427971855,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'іŧԡҊŜѨʥѡÇɚΦϷěļ\x88DѰҧƺÐЎrѫʕĂğʍҼūѴ',
                    'message': 'ȤÓʭӠƧBπӜӛdčȃ˄@Ł0Рѐ¼ʍɧŜԅύԄŘĵҘ°Ȓ',
                    'arguments': [
                            {
                                        'name': 'ҁʈЁpÃ}ǴԎЌĪǪƗ_Ή<j\x8euüђЦ˪ΨӥЈŸҨţ˓',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƫãϸ°˅ϵ\x84ԮȕŝУȥ\x90ȎŞ·υʪĠ+ЄƾŒИɏ҈ìαԁƉ',
                                                    },
                                    },
                            {
                                        'name': 'ӣðSʤŧӁъ˟ҋӹӈ;ӵß\x98ϴ[Ҙʡ{Ѵ˚szýʀΞξS©',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.639616:+0000',
                                                                            '20210301:152841.639630:+0000',
                                                                            '20210301:152841.639637:+0000',
                                                                            '20210301:152841.639643:+0000',
                                                                            '20210301:152841.639649:+0000',
                                                                            '20210301:152841.639654:+0000',
                                                                            '20210301:152841.639660:+0000',
                                                                            '20210301:152841.639666:+0000',
                                                                            '20210301:152841.639671:+0000',
                                                                            '20210301:152841.639689:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'шҍʄƶɍʪТrɀƇƙȳ\x93ʧ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 270458.7923506041,
                                                    },
                                    },
                            {
                                        'name': 'Ⱦ¹ÉƹЯРƥÁ_˒ćɶŜ%ѐÌʷКº˺ǄƨϴѨŴіơͿǂV',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.640082:+0000',
                                                                            '20210301:152841.640094:+0000',
                                                                            '20210301:152841.640102:+0000',
                                                                            '20210301:152841.640109:+0000',
                                                                            '20210301:152841.640116:+0000',
                                                                            '20210301:152841.640122:+0000',
                                                                            '20210301:152841.640129:+0000',
                                                                            '20210301:152841.640135:+0000',
                                                                            '20210301:152841.640141:+0000',
                                                                            '20210301:152841.640146:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u038dΒϿʽǔʠһӊʆɳѣҁӧлЉ\x9eɹǷϮȁƨѥΉѢӹ±ϽњёƔ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϗ˸Οʖϒщɐ\x9b˽ӖѝɜǛɒǮηГƱÄ"SȾԩʇҼʰΖɒԖķ',
                                                                            'ȭÜȪpѦҲҠÛδÛхϫɡʍȅĖʵɶȋӡùӍͰЎɈҞƚ(ʊҥ',
                                                                            'ϊȞɄ\x86ˇɹТƾ˪ǵӑŋ˕ĠΟǀдÌӇ;ɉѣӁɷωȁ>˷¼=',
                                                                            'ӻŴ\x88Ԙϲҳ7ʂʲɥǅºȵ\x9fҼŃϪπǽҝςŊЋ\u0380ûХ˫ȨșƦ',
                                                                            'τρëˉΤȜŢͰʞűҫϰą\x92Ңãπϴ7Ĝԝ҈ɜ{ЕԧΆ«Űѭ',
                                                                            'Ο\x82ȎΝŜҍ˳ҰĢӹæĺʆȤχӦʆ(\x80ϹԙνɴțƇåԇƏ˴Ԭ',
                                                                            'kүƸ˗ĞŅҍѰĠјĔʁÃǪɍɝΏȫ˓џƂѱϧӭɿ\x9b9єˎΝ',
                                                                            '˝Ɯä\u0382ʹɴӽç8ʝЎǋӦ\x86ʅћǩт\x83ˢʭΰ˙ЅĤʁ\x8fǯŘΏ',
                                                                            'Ƕëʼ\x82άʹĈģҘɢҴ҈ñϱŮʂƀWΓԚΫAŽϑԃαҚʶǓª',
                                                                            'YηƘǫѫԐ҄ķƖȻΗЖɗŦΝҌŨБƙψ3ƫ¬ė:ϫѝŰ#ϛ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x7fѶλ\x83ÀÊɯȘԀuЏ\x9fа',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.640814:+0000',
                                                                            '20210301:152841.640827:+0000',
                                                                            '20210301:152841.640835:+0000',
                                                                            '20210301:152841.640842:+0000',
                                                                            '20210301:152841.640849:+0000',
                                                                            '20210301:152841.640855:+0000',
                                                                            '20210301:152841.640861:+0000',
                                                                            '20210301:152841.640867:+0000',
                                                                            '20210301:152841.640873:+0000',
                                                                            '20210301:152841.640879:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˰p$èѤӮAŷuƠҎҺ^ǵȔn=˓\x90',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɝӉԆĮԘæƨȴ¶ҵ®ëѓӳΫ˼Ǳ\x9aτɺХєìʹĊφȈƟЦɜ',
                                                    },
                                    },
                            {
                                        'name': 'ʺƟаȗ˼Ԏȏϖњ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152841.641264:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ХμĕζʟüϰaԓOЀƝӲѸɐϒȍϜѓо\x8f',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.641414:+0000',
                                                                            '20210301:152841.641425:+0000',
                                                                            '20210301:152841.641433:+0000',
                                                                            '20210301:152841.641471:+0000',
                                                                            '20210301:152841.641477:+0000',
                                                                            '20210301:152841.641483:+0000',
                                                                            '20210301:152841.641489:+0000',
                                                                            '20210301:152841.641495:+0000',
                                                                            '20210301:152841.641500:+0000',
                                                                            '20210301:152841.641506:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǇǇȶˮͶ҆Ζѯ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3051925029093091191,
                                                                            9135369092036704958,
                                                                            -5781445994328759683,
                                                                            21823716172655018,
                                                                            -7163057542940558297,
                                                                            -2010456655902601073,
                                                                            2569144923249090475,
                                                                            -886217431986682982,
                                                                            -8409367506515827357,
                                                                            6547046678101933245,
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

            'identifier': 'ɵòðħù',

            'categories': [
                'file',
            ],

            'messages': [
                {
                    'catalog': 'ĮҖ',
                    'message': 'й',
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
            'name': 'ĻоӫɘԗˉǑΧԨԏ]ϣɳƇѧ\x8fϙ;ԬīЍ˷ŵїЂӖӐǑ\x81ɐ',
            'error': {
                'identifier': 'ѴaΌʉϸӄƯ\x80ȀϲάπʺҭѢɄȔʊǱǽǟůȔҷεѤϡ\u0382ķĖ',
                'categories': [
                    'invalid-user-action',
                    'access-restriction',
                    'configuration',
                    'access-restriction',
                    'file',
                    'network',
                    'internal',
                    'access-restriction',
                    'invalid-user-action',
                    'os',
                ],
                'source': 'Ӈ҂ʩʃЂЉʌӱӺɌ&ЕƽԣҒϩąлҰǂŁύө Ԯı¤ЁæĴ',
                'messages': [
                    {
                            'catalog': 'kxѠ¹ϴɺ¨7Ҩ˔\x96˞˻˟ҀїƨſϳΎ¶ɇȞǝȻΩԆŤǭǤ',
                            'message': 'ő\u0378_\x86ʮÛ\\ϘpưЯǪĻƘƇҔĂƭõˣҨºрЄő˝ĩǼ\x82Ǆ',
                            'arguments': [
                                        {
                                                        'name': '\x83æЌǀ>HƯǻƁѐҨΫ¶ťl¦òԣƞχɮбӃ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŧӁɫˎϜԏͷſӄǈͳ\u038bưʼɚ¿Óƾ¯ȪώϫԆʭĠӛɯȅÛÓ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1140286771028470244,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƔԘζƵȫ΄ʟ҃ӅͻԙhǬԠƏэ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.596285:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӍǜcљӜɵЛŉVÿȧĞԭ˂bѪȼɛůōӾ*ðҭîȐŹχϘʠ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'єЄŢȺˀȩ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȇҡ˥їżǪǵλԔ+ќeΧȥΕeȫË\xadжҲ¯òԞǩћͷΞ&E',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԔϚ˛ԏҹǩɰǏ*ʻɵ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7655225706554096649,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҺčǊȟſӗÆˋҌȰéіŮӯѨʡ;ˆԩʪǪɍə=Ϛҝʸʵʔď',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3351259609018037990,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȈΛιkΝɻʋňjоǲVwсĿˎˋ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.597001:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʫǂʥ¾ĦîХѪćŒϊҜЈϸʪȵÐөӌЂӕGǌĜςѠƗʱЍȤ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҁǪЕ6˹ǯϸMОȝѳИˢʱҦƥѣˁҳƹŦωӞӑеƠԩȪŐ#',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ǖ{ƔϦǢȌƶɀǏ΄ÖʻΘӿ\x8a\u0380ͻNȶǻ(ˠ\\ӯǰʈбĐƛĹ',
                            'message': 'ӈǵͻǗ\x8aaʀΨЖѠă\xadȗ\u038b\x80Ƙ˯ʡþЬáŢDѲŦ\x8fʰǰǴ΅',
                            'arguments': [
                                        {
                                                        'name': 'ɨӜďɝťβ\x87ƈ҉āҺƍ·ǸΥɐſӎɓƫǌ\x8fįɛѼԡχ³ˊϾ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.597713:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΊӸō',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԏǞWƥ˕ǃ¯*ıμƷ΅ҞӉ/˨Ң\u038bƮυǹjϚГ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1673663259926595978,
                                                                        },
                                                    },
                                        {
                                                        'name': 'іӀŉˤ½ŁǎϠ˞˙ѿИΕԜŏÁƝɹЊʗŶβʽʑ¤ʬ˩ϲ¸ǹ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 976517.1131800239,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƦřҴʏ\x87ǺϤќԗŁЎ϶ůÇΘɞGԊgǷυΗҏſòÔÈҐȚɃ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.599429:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Mƈǲ2ɻяΜãɺƬɒ\x8aʬѵȬЎύƔӳƵʜ\u03a2˸ȶӟ϶ыǞ\\ύ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǌк˱eñǘѵȎ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8006159409330394842,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԣοʛʒ\x8aƤǖ»ҖŞˈęįŽМԆ²ƟĢǋӔҖƔȼŗϠ;ȰƔ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ļ˸ӏɑĹCт\x9bϾР¬њ¡Ţä©',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƿΫͲҔɬçǜԎ\u0380ŢʃΎϱҾî7ŶʚÀ\x9aӝϿɂΝ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϡʵ\x95ÊµѧJʣҝý\\ҞАƗчÁɉѱѧǑĎŜэ\\Ù˰ïҶƑԡ',
                            'message': '\x8f҅lǴȄӍ\u038bϽйīƁƋbРҵɭȯ҂Аҟ\x95AҨΒԪ˯șjǈȝ',
                            'arguments': [
                                        {
                                                        'name': 'ƢрғʯиûɖʧξƠRδǑπ˜ȨÎːύʲɂŧʗѓƛ\x93Ŀő',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'æȎҍʉΗTБÕ\x81¥\x9dªƺƴҟȫěȳЋǑVԭԇʼ£Λύwʤƣ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԀŮҜđԊËȩΥŨҫ9ȳDԥf\x9dҕԙʝőŖϜԜʡӽҹʂVIϹ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -904791712404015980,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԬʨσΒԪǂțȇʊуʿɏǹ]āʘˠ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 435579.953505885,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѧYˈɥ˲΅±',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.601226:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˻ȲzĭƈЭģʥįȽӠƠ¸µʀ˝[ʸҡѪ\x84ӞɘӑL΅ɺA\x92˳',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϠʼӛƟſ\x95č)ɝȶŭˊƁҊƑӒӻщƷξӆήŬȮΑźɡϸǿΊ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'αȗ\u03a2ԩϨţԦ˶ȹɝŁӄľȧԍЗӿæӁЏǷӚє˘Ŕӭ˙ӝԉȡ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӵ\x9e˼ЬΓʒЗάЍǶƵТǑіţѩéӴéȡтЬЩZδŠԪǖ5ԅ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʭӁȼҖǉ˒ʎы\x8eʧóє˄;ԝĩљȀʭǇĳǋđήЧϳ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'іDëʑΩɄȝРеǙԭЁSɑϧϺȱþ\x9eǺĨʳʘӑ¡ҙҝԠ˕Č',
                            'message': 'ďɾÃƌӰҧЃ\x91Ԓ»ΈОΣǃȘόˀŬƁ҄ӜħȪόυȤȗ҄ȋñ',
                            'arguments': [
                                        {
                                                        'name': 'Ȓњԍ˞ϼG˱4ȑņɧȍʗĸȠȫ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƞȺʎʂǺƌӜʣD',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŬƝϡþǤ©Ö.кФÞ\x9eɴʙšƲɀϽţҺѮƫʯӈ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȱͲӤĪӬзжӛŚɘ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.602917:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'нʓԓVӳàɾŸоǩ\u0381,ϋ\x92ѢdǝͿćˋΜҊŎȐɇʄˤAҷĐ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӛǎ\xa0Ӗ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'œΓjԬ$GƥǺƻыƬ˸ bѶɊҷÈǏƲƤљԆӖӥTͻȑτԙ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'žʹΙ',
                            'message': 'ɝKԊƀǃӤȏҹϛEúʌŭ˟˸3ÞХσ\u0380À¸Щ\x83SɏϾ\u03a2Cǵ',
                            'arguments': [
                                        {
                                                        'name': 'ǆҒΈ˳«čɱ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 334303.65914951597,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƩÈÍйňȿ_ϳÆԚϔʍГͰѐԌđ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŌŁɤǸ½\x91ġЯ˶ιȕ3Ҷǣűˬȩ%ƺϱĕnӛмȘȇÕſͳș',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '3Щөԍ¨ȭ\x99ӹ\u0380ň',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'юνԇǣYҺǡҬĸ\x84Ӊϔ#nЬѬЮĈ&ƢȐӼ¯ϊƇĬ!ˀƫƋ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4872179029507215614,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҝ<ʹƽьεǠ˹Ώɼх9ÛĔΧUƨRӟˣVŹ[ӉʫɼǊ˅γԆ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΥÍȕɄȻƫĪĞŚÏ˸\x81иŘӈʏğůɑſЭ¾ĆƉʱ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'цȖЊȀřϖȽεкʔΜ~ƕӑʪ{в',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8619473340410024139,
                                                                        },
                                                    },
                                        {
                                                        'name': "ĭКϾн'ŨΟɹ!V6ȵʌĤϣƖ\x9eӜȵ|ӒĽԓÁnϽșϙɖѳ",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '+ȝǊҡųѶǦȶϏԒϤʓԣԩǭˣč\u0378цŠүӈƧĄąǸȺ˫cČ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'мʲĽʫ¦ɕϐƜʙӴʴ',
                            'message': 'ǓČȆʡǱ\x99κҜӠԇπɑĮˁЗ6ғΐªʕϯ|öρąӺѫҭϨӟ',
                            'arguments': [
                                        {
                                                        'name': 'Ңʀѥ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ó҈QʢɍÅĘƳμзϝŎЩĥѵ1˶ŪТͽц˄ѓǲƙząǓӖʬ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8eQǤǹüƢγɔʰŘЋ:ϪɁϋЍЏИӼЏʙЇ\x9aԑϰɝԇҵ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ì˗ǻp¡ɒьŒӓҚYƪɋŲºӰƷƦҮĩɡӰʜ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\u0381џȻЗȃҘƲIԡÄҚʭøρ҈ʼ˖ԥ½ňɕϮсƕʷĢÓќPҬ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŗȿ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.606014:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '$ҲҒϩ\x85ĻӒ\u0378`ζÎ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.606145:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѭź£ɕˬҳVЊƊ$ŔɴҝΑҍзʄĶіњɀÐĳɊaȴŽңŊŊ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʸώŞΟҶăĂĄ˺µлТøǪťú',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǹ\\Φ0ϵ\u0382Ɖƌ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǇŔ\u03a2ȀʩιŀԄēΫČǈɴˠ˰ºΈȰĀʰїйԞżő&ΈԂ˚Ⱥ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʚOǡ9(ͼΔѭ[\u038dϣƻĦәξĴԗǂ˥ͲʐǐTЄϽïЧ\x97ʥǸ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ǣÿɬ\u0382ÚφӦçҫΉ\x94ǪSԪǳэϾҎşЭϳàʊɟŚŉЪ\x8aԃP',
                            'message': 'ȱΚхˋ\x96ȳμρȸŏи|,ˠǇ\x94ŵŵƢɝ˷ͿԇǬХϿƢԟτǡ',
                            'arguments': [
                                        {
                                                        'name': 'Û°²ƢȐԋȣZƹɩǌ!ˏčȓɥϢОшĦѐ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ôȰüσϭɆìȨȤдǣѧ6Ň',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÉðĔpʞнӲѼǽʙїĜˑŁğӏǈ˻ѭʐΨʸԪAʸȔѲЪԚά',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǘƏƦčƉЩъ£\x82ʻ·zӋæϏ˼ˋɰȗÞΪKǇ¼ƐÍ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƗqкΐΟȫĎ\x95ѾƷƯҏԐƮʒÆϲхґСΠƻŒУӕзОҽǐħ',
                                                                        },
                                                    },
                                        {
                                                        'name': ' Ӏԗ:ɛ\x7f¢ȈʞѲÌʋѰƏ5ҢåΰѭįȀĔμԇʇԬͶÒhǙ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɧʶӻşɏΠқϛʱƅWɒЦЕěǷсѮƏ˾ѻȶDĲɒϪǆΕώŘ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'г˞',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'śŌʕҚ>Ǜ\x98ӱƱΔҨ\x93¦ͲЩʧԫºά<ϩӖΈxÓˋΒ\x8c',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ұҚaƷΛƞǾȚ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҦЎŎ7[\\ӝѽУȯŗ˫ӗй8ԇдѻηuҋƿŀ·ͺɴĕȣ¸Ӌ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.608677:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ϲ\x8bφƋȖ҂ӸɱôЏ˴ŹЎǃԀùȯ˨Ҵʕˁ\x9bŎ΄˹ʽĳĕÂξ',
                            'message': 'õщѸʮɟlĄÖǹEԖͻЈ¨ψƪ`ǎ\u0380˽ϫҢ҅ǽλáϤӺʗ˰',
                            'arguments': [
                                        {
                                                        'name': 'ɚԧҳϑ«ŬƵϏ˞фħȨéԌХʙŐǄŏ\x96ͿÄ˴Θĕ¹¦\x8bļ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7591692413936236988,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӷӍңo',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '6PɊƍƐɕʷļјlϵR˳ӛӪͼĤ˓υ΅ԒӔʅηȐ.Ϋˎԉȷ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'oøʑˬŉϲâɬƊϱɔΠʵǶҶҫРȻҫ!Ō¤Ԧԙɑ\x85ԇ¾ýѤ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҮчҶĪǩМҨҠԠѭΓȽѱɬßU#˜ЪÎɌŠrЉӽ$ȧˮϙÕ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǫЈпɈœ\x9bцǨЎÈôʆƚưĀéĩҁˠņ£ӀΝЫ*ҶƧΠʹͽ',
                            'message': 'ĸϧɆȋǆϙјԙДȐӔȰŦͽŬȯőǦɳæªґŽ0ФpэȢɡǁ',
                            'arguments': [
                                        {
                                                        'name': 'įŠʮӤŜƞǳƹϋƾϦ\x85ҒʼӉџϣЖǋϽ·əϟŬĚǚ˰ϞƷͼ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.609933:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '!Ǡ˛sŻƷɤѶ˚°θҳї\x86śϘКĐƘƤѨΒʴήȴŏ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Уԅȹɣϴ!ǔҶʅӲʫȇɺìǍ5Ĭλт3ʝұѼǯѐҮBĞʙӏ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʇƾЃƍǁʷɚÆ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĠѯȤɺ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 731679.952823429,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɇԙň˚ԜҩȺϫŞĨƆ҈ǘԈɅ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǉ˼ƇɝΏѺ¤ŻʼӴϘӓҽñЂ˽ř\u0381ɳƮγȝʦΆ҂ЅʛΚҴþ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ː?ÓʠҝĚʎԎŝʥӴÁůų',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ąђҢʁǕʪӲԠKÁŬʤAԬ΅ªƠҪЈŪЛĀʅƞ_\x89ùȜˇѫ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʻGǭƸʴӒ©Ɂ¹ǹ&\x84ӫϒԇ¦ϮӟЃү϶Ͳăɴ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˳1˺˾ԈԔ.˞Ŋѧɲ6ǅ˖FΆҋƥŏȪ+ϟЛЦ«ɻϯнѧÊ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'yŅԏїήŨŻȥ\x97ưqӶˀʩѳɸԈπΕʳĔˍԍŔ˜˼ŜӋuǴ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 756568.1400613177,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ДïʢϞŘǟɝЗĪáŀƺ\x9fĿѐҍǶțΥƉԓĎȩЋȾùԁ\x7fўѲ',
                            'message': 'ŪƪΆĀϏ\u038břȃзÚʮ˗ʌôǙǔ.\x86Ɔɧԛ$ÑɮήʵkÚҍw',
                            'arguments': [
                                        {
                                                        'name': 'ʪБzѫŸΩӽř\u038bӕØȠҎǈ>Ƈǯ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˆƛϴ-ŰΔϻºȯǚʅϹŭВ<ɐϧġƻɎOĲǐļƦȅˆ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3113473012951965481,
                                                                        },
                                                    },
                                        {
                                                        'name': 'º!ɵɕǦћ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÌȳǯѧҵяɪƘҘͽgӝДȐƥĬŏcǣТőэˣƸƐɷӯĔfΥ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.612097:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǳȮ÷ёĴѣѵĢƤѰëЁ҈ˏɕδǁNɥ\u038bΔɫɘӽϥǥw˾јȲ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŤÔҢďȇĻɫ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӳǅ¸ʵ˔Ӫɣ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x89#ʶɣǖΥσљˢ¡ĩ\u0379ѫɴI#ѯ4ЎύѭƙҿóſЏ·Ϭ¯Ί',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'śŧ}ĭѓ˃ӽτaōυάKϜ˽ΰ¡\x9cВǉ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʠҫіώӝÅƶªƔΙЯЁȢˇԭѹԠʂȊɺ÷ϞΎšмԢ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5875386881374956872,
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

            'name': 'ӺŬ҇',

            'error': {
                'identifier': 'ўÄċ%Ƥ',
                'categories': [
                    'os',
                ],
                'messages': [
                    {
                            'catalog': 'ΏҺ',
                            'message': 'ȏ',
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
            'name': '˄ԍćϋÉʩҪҺɃǍԁѬĢкǺǟΒ',
            'version': [
                -5015615415286654668,
                -2580726018722533802,
                -4134949069933925969,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ѮϮԘ',

            'version': [
                -4333473026253316565,
                -321773624494596538,
                -5434465020177788083,
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
            'event_id': 'Ƒл;ΑŶȦӽƌśƠ|ŹϳҜƠʡÎ{ƲŸǌªȐы\x9eɛFĥȼӀ',
            'target_id': '˪ЕǙ\x810ɅŨ\u0381ԐǧͶОĶɱƮʶСыҳΘ\x8eөġҎþҊȽÈԨϓ',
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
                    'event_id': 'ӃԮГřҏʐ£ҬҏҖ˲ФēԝʇʛĊƊͶħӌӽ&ȱǨÛʮ!ʇΆ',
                    'target_id': 'ШƋ²ȉӣˋı,Хѹ\x8aĮΒÛĕ\xadҐǶƍɧƈƦ\x9fśQ¶\x9b%ϘɈ',
                },
                {
                    'event_id': 'ǎĺėƼȵδ;ɿȶӲ˓Ε҂ӷԤ°ȻǴӁĴʻƞϙҘЮØ³ѷĽϻ',
                    'target_id': 'ƯʷŹ˥ӠʭȼϏȢ˶ԪÕғД˱ѦƃϭҠŶïȶѴɿЪ\x8aǡщĎӊ',
                },
                {
                    'event_id': 'ͰҕѢȡ<á',
                    'target_id': 'ˮǺȒžǊʎΈqđҫŽэȭԊʌόйЮЊε˱ʄпϙèÖÈҎǣҩ',
                },
                {
                    'event_id': 'ʑïӂΙļȻĈŦuʨОЩҽ˻ѥΫƬWЊєҩϭжϵ÷¤ɽʥǁ\u0379',
                    'target_id': '˭ǇŴ˶еɁǴԨΛњ:ɭɕԚǘƭɟҷ˭ƇзɯѸωBǫ\x84Ϲì ',
                },
                {
                    'event_id': 'ҎτƺˈУɱ\u03830',
                    'target_id': 'řȇпԐİ-ǬԒѺλҷӲĳŷļĴ˰ĳöàѸç¶YïѦѧĦӯϕ',
                },
                {
                    'event_id': 'ЫʵĈүͱˏӽȽɻǂ¡ʤӺʋͶŷƐʈйʰVϴ˨ƏϋȩȬөdϥ',
                    'target_id': 'șԅ\x91ƞҢғß˔ʕÄӋҩʩђΣ¦ʖſτ*ЬԈ˂ҎщŞԅԊ!қ',
                },
                {
                    'event_id': 'ҐˏјѲҧҶҟҳƴ\u0382ČԄѐɶʡοлÒӨɡԊϳҬѹĒρȎʗ+ʮ',
                    'target_id': 'ЮėəxʿʹʧBɏɘϥŋȋǯ¿\x8cƷ\x93ȒȕɑĩǚϼʜґCӘΜá',
                },
                {
                    'event_id': '\x9fˋɣуǢΥŤʀ˞ͰŬ˟ӁЄ£ĲұđкӖĕԭʦ\x9b@:ĢȽ2.',
                    'target_id': '\xa0ĥ÷ŝĎȂś´ɡǅҧΧďūɌȓɍΦ\x94ї˻ЀɦƛÀǗгvŸƩ',
                },
                {
                    'event_id': 'ʿņЄ΅\x85ӪôҸĜŭ5ӵ{ÛРãӺƌǯ>ϓɂʑСǱǓԉѲЉķ',
                    'target_id': '4-ʢýI\x89αьŭӴǩóаrĘқɦƛÖɹǭƔxq°ԫǗԨÏü',
                },
                {
                    'event_id': 'ŜüЧ;ҾǗơұӪҁÙăӮΘΩuЮѵЁśԭġŻǞάˈщΈҥа',
                    'target_id': '҈ɏΙӎǀʷsϴȿоşΆЉđɛүǼϦкҕҗʰʩƨɻǞώƘҘÕ',
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
                    'event_id': 'ʈŏ¯ԢͿīüǇӜӌWƎĪčÊĔ\u038bЂűČ*ďǅ˾Ƙͳӧ͵҉ͼ',
                    'target_id': 'èӲΛ҅ΒÖΑHèȻoȝɳjϸɀƈɖłҕƇǣηÊˍäϥòБϴ',
                },
                {
                    'event_id': '¯ɐ\u0381Ξ,AɎœ҂ǄBɛԘѧʆˬУ¶nΧ7ʎͻөΞɞε˺ȥǍ',
                    'target_id': 'şʴϘЯ\x81ЖɸӏϜ|˻úбӃ\x91åœƎˉô¬щҞӞÂĤ\x80\x8dǵϕ',
                },
                {
                    'event_id': 'ÒȞƽʆƩʧԏǷѧѝљμɬÖӽњԁƭ\x81ÌԊ\x9eЊŞќ˯ƣĀďʨ',
                    'target_id': 'ŠӑΫЭč˰ӦѥǋȞήðɓ˓ŋƊӥßĶǜůΌʍÕʳƮѯȚȖЫ',
                },
                {
                    'event_id': 'ώĭȴҸɥˠˇȫˆдŢԔǢɧУԛƊѳҏĚџ˪ВŉěʢƆԀлё',
                    'target_id': 'Jȶѕ\u03a2ǄʂθҘӦƞҵӍѷȠΓҨÔȆҒʫΝͻBϳκŽϼȩȠƿ',
                },
                {
                    'event_id': 'УͰ4ǔȲƉğ¼wӰϘŋе˚Аù΅Ȁõ˽\x95ƴ˔ǎiҿé˶ϓU',
                    'target_id': 'ôǄČˋҫίӎӽарɹŚθņŐǿԅîӏː҅Ƀʀфɉƃɫϵϗλ',
                },
                {
                    'event_id': 'ǛцĢЌұǻһȊͿу͵ԥԒѱ¦ϓ\u038bȓžŴȢԥ÷ĤpхŹrɆʁ',
                    'target_id': 'ęƌΘÏƺšƃǘοȣζϢQΈʊ\x99ȝЍź\u0378øɂӝɡˎ=ӰǗ Ԛ',
                },
                {
                    'event_id': 'ɯ3΅ƅСƷù˥ȠƗ\u03a2ϤϑϘέñ¥ȄЋxîƘƁ}ŨŎtɶͺî',
                    'target_id': 'ӗΖ\x82Ęȋ\x8aӥѐɆԠшЇȩɺӾʩўЍȹB˴ȂԧN¯ʤ\u038dĖȐŤ',
                },
                {
                    'event_id': '£ǰɱtoʛGÓŌQćϢÑΉáӭʊͻρѮƣȥŷǸԦѳǇŦnæ',
                    'target_id': 'ĞҐΔĳˀ¬Éŭ1a\x82ӕҠˇɬɢέɏʥǉČȇʏϪĺϮӉНЉʐ',
                },
                {
                    'event_id': '·˒оĉȆƼ˰ѱѹёњљ»ӰӊǂҔǧƠΦκЇĺľчѻÊӚƪȺ',
                    'target_id': '¯ѯ˻σǃ΅ʆƌ\x93UƮ2˴\x9fЋ¡ӹʆљĢХ҅ӸӦżÙķÒʭϘ',
                },
                {
                    'event_id': '\x9bƗȴӊƼŊʟŋºϭ',
                    'target_id': '˸ρѾȈī\u0382ǷǂԒhŰķēĂźaҜķιǂŮͼԘĉƵѢѫӧҗF',
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
            'name': 'ǇȑмÁƑԇЃ',
            'version': [
                -2914995368187681305,
                -7860812663386389186,
                -1005166147482935835,
            ],
            'about': 'ҍ҈ĂǍѠ¥˭ҊɩнǹȜʈƲЇȲàŨÓņӺʁuÑÎèλ¯ĴK',
            'description': 'ʤAȬ΄ӕГʃΓԬŚpǟũԁˢɊӸ\x86ˮӦҦϦş˄¶МǁϤšϘ',
            'authors': [
                'Ś˫yΤЫηӿ\x9e)ŅƾήÚŮǸʋǫ˽¿ѰεϟȬȹªѿԟǲƮÿ',
                'ƹϺɮΫȏMĺȣќĖ\x97ϽÕӰ\x86ǁďЄ\u0380˦ΩĂϭӬȉљvʟөʥ',
                '҄ÊΞϼǈǤɭР҄JԁNËˇ˥ŉЁͱȝ\x9cĤ«ϽǢɞÎΊđȎҷ',
                'ĬŬӚ7ͻɋ\x83҂ξЫN\x95ˍЙʀŅԉĽ҂ɞ˦ϩэҪɿµӤǵɡǰ',
                '˾ԀϡΥοÜ˥ү!АǳІҔӇЗӃ',
                'Ɠϝˁ\x885ĒԖҮǟӒfʕȈDЋɮѿŻ\x7fπԬґӒЕԪųɉ_\u0378Ʈ',
                'ɠΛ]҈ʋ˔ĐdυɥžƼħŞČӿǈƇǪĸΣКƌˮ`ΠϞĈɒö',
                'њä˚\xa0Aʏěˇ\x9e˖CӽǞƷϽƗ˘ˢ\x8aȎȇʤшŃҏƥʕʇшG',
                '˖ɓʊжЬǯȿҺЧȧԀɠŻӴÇќÉGђ/ϣμƨ^ƬКеӰш˯',
                'ſǒŢќӖ˩\x88ùȑˎΌǤ-ęƟ/åȃħάĀԄ˭ЭːIρѠě҉',
            ],
            'licenses': [
                'Ѓ¯Ά4ȢʿɅӸӂԍұʍϨ\x7fůүϤԃ5ʎϫ\x84ҀƚχҲҠ|Χе',
                'ӐόŹҼ\x92ӻǍйҼ\x87UÄҗΞԌÈ·ԈȜ©ɬќŷĶЗЋ˂Ҭʍȱ',
                'ϜУÉҾǣΑđ˻ZʱÈ*˽ʼʞеďȐ2LƜwǏΆ]žϦ˷ʔǞ',
                'ʗÒǖǂĜԣҝ\x8cǖϓʜ´ӲėŜĮFÍxZԆӉѾбθəӾuϽБ',
                'ƦɑϽȆÓʕԨ˩ЮNԝƩYȔŵčɴЦŨå¬ģђԕǁαġʇҘʫ',
                "ԑļĴƹǄÑǃ#Д'ƄǾϼ ϥįҾѧϑĝ§ҕl~¯ԪӚϐϳұ",
                '@ģν\x93ǝľ¯ԈȭǸEүі\x97ӐҴЬȚѝʯˎ˂ɺʛѱÈΙҷƠщ',
                'ԧΡʑвŎѾƧ҉ƖɎȨʜ˨шǷŁѧ˰ǭȐɢϽҀéJѩbſÊľ',
                'ьЮϟ\x89ƦдƤüюϏϡ;ϾȋβĜσąηZɳΤCϋЕǹ\u038dˣžҎ',
                'ÕЋұӋԎ˾\u0383ťʥԚҮàŗяʧȩӨɊȌªКԚė҄Фӎкҩқҽ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʼɽȊ',

            'version': [
                -8384790761168487907,
                -9198020520590740245,
                -3072366302305564030,
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
                    'name': 'ϘŷčσɻщϩέŚΈɫɗтȒǐЬÄ˓ƚţѐŁϚʃщԭҝϳŏƮ',
                    'version': [
                            -6424792842912101111,
                            -8759734614239667089,
                            -389583848059721261,
                        ],
                    'about': 'ҏÎґԗǏ҉ŐĀ΅[ˇɥ&ĭȻѣђŴðƮȽτɱЇƙӆ,ɗѮӢ',
                    'description': 'ЎϰϸJŴƠһȅǂϹєы\x91\u038dːÐƲѥӍƙиīʰԄȟʈкЃɡδ',
                    'authors': [
                            'юѐˡłіĻ9ħӹAͶ˃%ΠɋTȒ˼Ȓϸэϔϖɺrõϛ˓Ӎ˩',
                            'ѩʃEȥʗɡ~ΕԜ΄΄ʑÐӮŐφɪŜрΓɪ\x85ӽΚŚŃǖýǓӜ',
                            'ǞѺFȥ\x9fĠɄѪęʝӐЎŃԣӻƑɫҡϊіέʍƹˍǰˇχđїÄ',
                            '9\xadϮķĐӻıʒъƒ\x90ɶƚҐάӸð\x93íԩЙŹҟӒПĕ\u0380ɌȥԄ',
                            '˳ӶÊƲ¦ɉtΈöɡ´_áӿԫτϽϵШqÛ˶ǏͶȇЖѡ·БϿ',
                            '?ƫПHȀäҷʔҺƊԓʴʵ\x8cʧͱŇǣůɬʕϷҾсĚёҵӋϺ{',
                            'ʒňѤҮ\x81PͺԫȳбȥϣȶΈ\x8cΊƫЭ϶ĨƝӊʖĻÕȨˤŮô\x9c',
                            'ҺǴȮтÄĖǎӃαЩĆņǏĄψãŧ4Mњ˟ŻǮŮϾohŇϥf',
                            'мȅЉ°KКƪӳůğÀƀϺ¶ӦŲ˹nΕЧZȝŀĀǘzĆΙӀŕ',
                            'Ϸ`ҨѺͷ¡Ң\x92кªς\x82TѸɆkȟԬϦҒ˯ȸбǟŜӑːɆԘǊ',
                        ],
                    'licenses': [
                            'χ°ŏєɯϿœЗȹйϝԞùӫ˷ɷЏvŢ9ӊѭϖƳԦțͲʺǊѢ',
                            'Ò-Ȯŷ6ƀԬΖӱɟҽқIҤɨųƂԅïƞX\x8a¤KѤƞьbϖ\x83',
                            'ĭɟЇŕӶ¾Ҙ˪Ӽä\x91ǇȇĞƻǍԝƪĉӯîϲԍ¥ϠӉϸϭɡԑ',
                            'ʞƃԘѓ\x97үĚ˞Ӑӱȹȋύ¼΅ƽ˕ɇİʉýMǧ\x99¼ŊáβĬΒ',
                            'hǋȢϰʤͳҷΩʈϱСÀ҇ơҩˇĻɧ¢ѼʤȏӚÁҋ~ѯ=ĸɾ',
                        ],
                },
                {
                    'name': "Ѐ'˲öŷǻR¿ԣZӾĹШÿёĴ˻ӢɸǷτJ¼ˁӆ\x9cӬQӎӰ",
                    'version': [
                            -3603997157946338564,
                            -7328839165167924269,
                            -4190378302915539931,
                        ],
                    'about': 'ȬҊфGшЇԡўәǇԗȃΖȂϭŢĜʤ@ɜɇiɢΊԤȪќʙ\u03a2Ͳ',
                    'description': 'fʷφˌ˪3ˁĮºЄцiӑÍ˶ҀѲʋ˟ɱӼə\x90ϦǾñѤȊϡԪ',
                    'authors': [
                            'ǆžÁҫӴЩыɄʀµʿϭџǬыϯǲƒ',
                            '˱ӟЬϹ¸ʙȌ\x8c\x9dϊȳɦ˖ƛ÷ŕŋοΦҹoԞ¥\x91îƔԚ°ΣǇ',
                            'zɠϲʏǅύìǣǳЊʹхѮŉϸŹ½Η+РQѤŴƘƳã±˽ӑȂ',
                            "¹ǂВƏ҄lЪȗĘ'ˮ¹ɰ҇ԢľùǬдʓЀҴωϝφ»Ԝ1˽\x88",
                            'Ĝ\x96ƤЉͶg\x85ƨԍЕϦш6өўȔ\u0383ŁÕȈпȶ˄бӳϬѸμƪϟ',
                            'іѿaʈƅԏԋ\x82WȒɼ\xa0Ш˽ĂњʾɣǝɄȁɪķȖͻřӌԉǑҧ',
                            'ԛȐóчĹʱ҅ӟʹьʙԠԗYϰDԟмƲɝѸоŠΛЧiЙɀǈү',
                            'şЯǎʽкМԡ[ˮʺ"ҽĪЉ˧șҸͺ¹ű×Ȼ˷ƕΣƐʳҬνӗ',
                            'σͻϧѴâõéͳƓÍŪŏϚѐʬμШüb\u038b¨ь˫ɫĂãҐǱųѕ',
                            'tҟ¶Ȉ8źΖԫ\u0381Uɚcȑё0ϖƓ5RʚѠʂcԈҪʂӆӶɶƙ',
                        ],
                    'licenses': [
                            'ɟʣϲėɄғLј\x8fŁбɆĞ˖ĔɅɁҶήȧ\x98¦ËôҺҩϓэbˆ',
                            'ФëΆѴÆtʍε9ϣǀϵҀȧɽ\x89ȵsï˩ѿҙԠɪϲbΟƋʖé',
                            'ʽҏл\x9cʋ|ѣ\u0381ŶĚƁӲЛʻś˸Ѳa&ӲˏȔ˕ӑíњѦɗƭϫ',
                            'ԈȺϭ]ǜʎSƿɤҒÞǄɆȉ҂ÙЕҢSŭQфВɟǙӏИǵͷΜ',
                            'ЇȈЬ҆jЅǑȢӌƠŌԩήϩÒʝ˻ěѻʧŐłԫΗŴěхМʔү',
                            'İ\x93ьʛˣǷÕӵǞƲӲƏъǛѪңƕКòFʡҴϋȓ®јƍŦÃң',
                            '²ńľζɛǓŲѵήʙοѩȄѳҾΦIʜԪ˼ѓӝ\x89Дƚ҈',
                            'σīÖӬ1δʄΪŤъūĞ˩ƉÂ˼ϖ"\x8bѶӪΖаƦĭ¶˟[ɇʳ',
                            'ϡАҶϟϼϢǚсÏƵ˒Ǥ¡ϣ˃ҖǳƞɂɣcυĂΆȳˀФ΅ƢЌ',
                        ],
                },
                {
                    'name': '¡ҖѰƹҺͺǰHȜϘȾ˟ʘӃρüĚêϐӕνiʿʄқСřzԣА',
                    'version': [
                            -1712911037497033097,
                            -6734127551788833851,
                            -1129340100632907048,
                        ],
                    'about': 'ŇкѠˤFlТǑŻ´ȳǮƼ˼Ӏ˨ɦɃßōǕ\u0379ØLʵԝW\x86ȟF',
                    'description': 'Æ1Пʳƿ\x93ȝŨӲҴӭѹèáäƜØɂѿ©d#êƍԦ¾нĀӅӠ',
                    'authors': [
                            "Ҏ/˃\x9dƠȥşӗƬ{ԝVɉ±Ѯ\x8blʚ\u0379ŵțīˊʊƑȂԧƎӌ'",
                            '¨ћϴ\x82Ú˝ďȯКќƫȐ\u03a2ţRtԩǏNØJĵŲЊΠÄwłʉҏ',
                            'Ͽhԣː²ѺʷʁͳɘēϲɰȾǝȳ҇ĬԟУ',
                            'Ԉŭ:ҲĨδȡÉK)ԫĉÁƼńö˺ҼӢˀεuɗҢӪЊʏΩřȰ',
                            'ŃŲҶ\xad\xa0шȒӖʗɍŔεŤϫ\x97Ƞ˙ƧĬ˰êӑȖѧҍĊцȢ˘ơ',
                            'ƃΧȬN\u03a2ЍԪ\u038dϽɤӋƥüșӧҐϞśƘ\x8cßȟtc^ĝƮǌČΛ',
                            'ƌƎmГҧʊXȢѠžҒɺđ˰\x8e˶oţӻҖΰɒ«ʟӳȯ΄ȗŎϳ',
                            'ʾűpĎ˟`ƃϵϾҭɓDƌöʑɠӑӻǁЂˌǎıǷ\x92˚äʊĝ˃',
                            '˅ȏәĘɀόǺϱЖȣ2ȣ\x9däоҹԖӒ҄ŤΚӇΒɽ\x8dϻțүҦȿ',
                            'ѕƩϵȌɢÂΖ\x96ƣƵҊÓҏ\x7fʈ\x93ҴԪǈ\u038bνǰϪʷĤìϱϱĵƕ',
                        ],
                    'licenses': [
                            '© |ΌԜӞȚΣӏšϽͳ\x84ǃЊɌЈӋԟϗǈӃҒΚϩ,ďńҌ˹',
                            'ÅÏϒśӰɿ\x83Ϧӳ)әoѣÚZBӱ(ҊҥӤĔԣϽÀßʷȱ\x9fΑ',
                            'ԕѻȦʤЦӐťЉщѿЎǙĚДϕѩɫź\u0379ɂЭÛёɎΌʭ˞ЊÇι',
                            "ķˉĔɋȕ˛ХƓ&δȚҧȌЬ÷Ґ!¿Ӎϣˋ'ƤċɁƍÀǔȺǦ",
                            'ӌϙʿ˭ӔɅ|ěҌǲϔɳоˋʿɏҊƻɯƥ\\ӧøćţAöӛɤұ',
                            'ΏϩWǊҭàҸƕ%Wҳ',
                            'ǌ\x9akˢ~ӨҪѦE˕ǢĂũȣŵνӤ|Ӗ¡ɐzȖĆżЃĊԛ\u0380¤',
                            'GϛϩȁWŷѽʅјǜĴjĕͷЏґϩҘԬϕǿəȩқ˨¬Ĝ˰СĦ',
                        ],
                },
                {
                    'name': 'ұɵς÷·ʖƢЩǥɊ\x9bЎԒwʼĘ˰ƈÊΩͱрəƏΓ2Ǥ˧Мζ',
                    'version': [
                            -8863030419618911169,
                            -2496716820760139597,
                            -4942521770482911381,
                        ],
                    'about': 'Ǭ^mʒƿӢȇӀȲ\u038dԗϸѪˀʽЃÝÈȆţùōӠдŃӉԑȲҺǲ',
                    'description': 'õ\u0381šAȋʭöǴRΌнƴĻѰ4oēʼѾτԫɹ[ѯÙ\u0382ŵЩԜҿ',
                    'authors': [
                            '[ѬӐɠFğØϗɔɜҹˍ˚Ѯ=ѩ\x93ʙӶŃː\x84ǋʬīˊҏɱϝƵ',
                            'Ȓ',
                            'Ǩ.˛ȁ',
                            'ɰѢԥEİǕɁƒжѱ˥ȴÆŰӡŅĚΌǭƉʀϐćѭœǯχ˶˖Ǭ',
                            'ђъ(ϝ[ŝөŬˌӗҵƑŎњ\x96ωȮƬĥіðу;ɸGˁҚοËŤ',
                            'kέÅҤɦɂӓѹέƪ\x8dʚђ>tԤůŏǭȇԭöʕΕè»ҩӷ±ê',
                            'ΰӃĒщϋˍΤĖʘðƂɆʪêǴΆǧś\x92\u0379ΤNȯҎ҂їΟSҖϗ',
                            "\x97ӍǇЄɺίʊРÓϣψǝϑԖόɰ§ƫϐԝnѽ'ƾʧƵƆӹωέ",
                            'OȰǌωԑǻŵɘΡҰ\x8fɪDŷчԏȢϝΑӞŇџ¶ɰćӤƌΘĕ˺',
                            'ѨΦɰϵǑѭÏΪ¹Ҥ˱ŁʵηŁǭԓæ$ɂƔЁɆгƌҙľɼӏǿ',
                        ],
                    'licenses': [
                            'ʦЪ{ɔÉѠȏMĤƌʃĔФȆɌŉɅҕpĻӂɹȒfµǾrϟǏ˱',
                            '˵ɗͻѱȸVăԡǻӊСыЏЋĵ¤ɱśȅЍȳӆƙʊʰкùȕӘè',
                        ],
                },
                {
                    'name': '\x96÷ɆŞɺ\u0380ҢʂӕӫőŧԐԔʚğͶό',
                    'version': [
                            -5605162927663891218,
                            -6612081848104525759,
                            -1015275123898883985,
                        ],
                    'about': 'ģӠ˨ˁԢĢƿҸюŴĊƢŏʯƑƋåʭÚø҉˺ĉʵƮҢʬǥҰˍ',
                    'description': 'ǍԁƿʭԆҾ˨ÀʌŻ˫ǜώͷɽԮJŎɷ\x8e]ҎlіʔŕƐь΅Ι',
                    'authors': [
                            'ˤ·ˠtЩìԜæȬĕ8ʣ',
                            '9БгɌˎƠҠСðÐɆҘϴϵʹ',
                            '˕ɒЬχƕʽƀËѢȭϚ\xadҍϟ\x89ɂӯǪ\x9f˘ҠԌĵΎɊҶŮĂЮӵ',
                            'ξ\x80ɣЪЬĵӅǾә˔ɾ˭ɲ҉˖ŸīʀšĹκЏѪ\x9dΌǯӎҬƥx',
                            'Шįԅ˥ȵԣъӬgƹ·ǎҩҳԗƼʥJe˄®ϻîŦʚȣ\x8fХϝͱ',
                            'ʺȾёöȵƖϚʧγ˪ԉʇ$Űўӣ\u0382ęĴșϮ\x94ӄʲԢȘûɼŷғ',
                            'ȅíϢѺȿʫԙӆ>ˑѦ^\u0380ҙʏͰŗĽЇ\x91ҤӹʦΕºƼύϣâ˱',
                            'Ŗͷƈ˴ǏƒǶΠбˁѡҢ˯ȇϯĒ\x7fҋӗé\u0378ĮԓӾȝʡ˚Sˮő',
                            'ǹļĸƻÃÎӑ҄Ĭӟʙ$řǒƉøúƑåȰҟѲĲСƬűТɹȁǳ',
                            'Ϟ˻ʕңȔǀƨмҌàѡήɠȦpĊȤ˾ȸԪ˸Č\x9c·ŵпŁ˓ÓZ',
                        ],
                    'licenses': [
                            "?Ԑǔɇȧ¤ҤҼŧŝϭ\x8cǬzӊϭĊѪӽ҂щфƾ\x82\x91ǭȦ'ԩƯ",
                            'ўО˵ĆɒӡЖҒӫҔ\x9bΈͻАąı¼ɘұĻˠďԅѲ˯ǵʐõгĨ',
                            'ď˧бʎ0ʌʽΦoΗҡɑɇūԅˡқʯƎiɻƼ҅ńý͵ÁɈрİ',
                            'ğ|ӯΛ˾ƅҽ˪þGǟ¸Ăɶɰ\u0382Ǆӳu)¿ŕßʮýҖѩZçԇ',
                            'ŲˇЅˁ\x84Ôţ,ɹĕư˳ƈ',
                            'ˋǠȵΐӦΙĜɾȜÀƐƏϞХӲ\x96ѦȜӓǇҒ\u0382ԪƣьǟΡΫԪԃ',
                            '˔ģӯ\u03a2ʱLèİȠЏʞ˛ŝҔʥŞδɭˣēΊƙԭ\x93',
                            'ԅŨ\x84ĮӾғ§úԩƦ˧҄˞Ȕ\x93q!°ǟЩ\x81џƒǨЦӍӥȢ#ï',
                            'ӓѡÅѮ\x93ӍɁȊǄŲƱԚҵʍӵюРɈňΝƝфƩҒүıɣͱʢ×',
                            'õѣǇRȮҠӳƱʕ',
                        ],
                },
                {
                    'name': 'ǆø¨ʁFЊƬÁҍőҦǷȶę˶έQ£płҹ?ŤɹǁԓˎКȤą',
                    'version': [
                            -7221858931650248580,
                            -4452460367085419166,
                            -951924427206192326,
                        ],
                    'about': 'ЎʣwsӒŊ¸ТɎΛσҌ΅ѡl\x85ÞςÞȗԒ¢ʭÕǀʬ;ĵ˫ȍ',
                    'description': '˼\x94ǯʅ˒ѳԆѮ*ΆҎŚӢɶïœΟʀόÇ\x80κƘȗŘȘүԓΤ÷',
                    'authors': [
                            'ĶŀϛƿӐƄʲŞϰοЃЄ%ѹ˷Ҕǅ.ʷҗйí1ʄ¼ͺƣиfЕ',
                            'ǝвǕ|ĦȅЉԪĤƀƘΡïԁ«˷Њԟӷ\x88˸ϕȔʫΊŃҬμ¿ȳ',
                            'ȻŰΣѸ\x82ǏƼʱĬѽRϐëȑΉʙ~ЙГʥȈƀ\x80ƾǚҿ˴\u0382ǶU',
                            'ԒϟҾɄȶĕɳͽșȜҭʅǿ\x8aʃϓwʨɌўѼŨƃЍƔѰĈřɋͻ',
                            'ȟ³ΛӐRҧήȴˮѠđнɶƄ÷\x98Åƀџ҉ȤâκϹηȄ\x98ĹцŊ',
                            'RBЙӫ˥ӣÓƚʦȎԆ¦ӥĸοʄɩƒѮţȜɆĪ҆RӻѶӂҎę',
                            'ǡӂԉǦƞʜцѸ×ҜSʎʸʂџʰċҏÁԙ\x85ĥÝԤӰТ΅ǸϫǗ',
                            'kľ˻ϷΧÙÄǽϸĕҙœǨǹŠÿʞɃʋÝǦЧͲȔ\x81ȣĊβŐȭ',
                            'ɌȮӶɺˋԭɼ;ӥԁԞȿňѵдȉȬëѭëßÓӐǣυŉӺŢҾĆ',
                            'ȩЙҽ_Τќʯ£вȔɧ˜Ҿ˯ɮҒԍʓÜнԪÅǸ4ӹß=НȖә',
                        ],
                    'licenses': [
                            '^ЕТщŜǨȵєԨſ',
                            '²ǸʽǦĳ˷ɚ˨}ʮʅԤǵԇǒˇƭҥ«ŉ\x87ǾĿƔɸ϶ˈƬԕК',
                            'YŽɪΚҼàI<ƊŌͰˑʹѱǃґǅłˠǸ"ϓɦ²ŕҋ',
                            'ЄԎѶèԄvͼΫΟҞΐΚӷʉǚfϋҨϤԡӳΔ\x9bɞˎя΅ɨӊ˓',
                            'ҞǌʠϷˊŗd¸ɣёǣӲψɱqҴ˚ςʅĩӯȁëҙƢŭҤǨwњ',
                        ],
                },
                {
                    'name': 'ˬČÀ\x90ҏ˸ăǠѡέÈѾéɏǖ¡ϮǞ\x8cĄÆǔɂȊЧЫ´ĆęԔ',
                    'version': [
                            -3095703110056948627,
                            -2249138742419484122,
                            -6782297633754621903,
                        ],
                    'about': '˧νЁԀƿǗϺӷǠƨЅσÙƢİĔȝȚƼkԫǅζĎӂϗѫ;Ƀĵ',
                    'description': 'ėƣĊtӍѹÄͻϮϓΖȏҙӸҰũ˨ŭҪđąBĐïӞ\x8dǅ\x91Уʨ',
                    'authors': [
                            'ȹ˥|˂ӀϪƟ~aˣҬơϪŻƋ\x8fƮƲħːΊЬўӣП»ɬԐӨθ',
                            'ǀÓʦː²ÓԍцсǝԩО\x82ŧΛ"ӏˢШțӔ²Ψ΄ȮɒџȞɂɛ',
                            'ɀˆЈʚɆũԪiĒӊәˡђƠԠŞ˕ɤĬφǛѾƔϤƥ',
                            'Ķ pВяȈϿɨȡȕāõ˷ňҁǲ\x92ˑԀάHǟęʩĢƚSʱӖɗ',
                            'zƸaтťԙʸɅqȣ°āĝңԁԉϙҙǁοɳeĚӼȞĻҺĺ1ʣ',
                            'ĆΜȞűYĊ}ȆрӮ\x98ʄļ\x8aғ¡ҪЉ(җ˸ҕӬЬӂÇ¼ɘ]ɜ',
                            '&ӱƠĈҁϗǉҭMǮβъƝʠ˨Şʮǒƒa',
                            '\u03a2ʟåЈŦͲђȻśљÇ¥ΐϯрӳřXćˎÑRЈȖʭƽȜРď¾',
                            'ūӢΣЧ˭ƛ\x8aМнʶlϣѷƂґɮǇПЦόԭё.ļԭѧ~ΎɩΜ',
                            'ѼɛĹl¹\x89ʞƉuɫӇǱҬ΅ʮҾΑlɆүЀǁƎƖʾőӇζɔϯ',
                        ],
                    'licenses': [
                            'Ζŏ=ųɌŮ˷ƿƲ¸RԨǣ͵ǊÉ5ϷŨԪϙɬʈЗӲď2Ԫćο',
                            'ЎƱ\u0379ΨԂqüƶ|§ʵ\x9bŭΣѳėХȅЌϫэџϯѺ˒Κζφ\x82ў',
                            'ĶӊԈҲє\u0383Æ÷«ӣƘӒϑ\x85\x9dũͺɃUˮǠɕƸҾǱÂԉƪƴ\xa0',
                            'ѷěȃӨĎʅӍʈƂӊƱÒȆØ%\x91ƧҚӾ҂ЄԚϘѱŊӷмʾ҇Ƴ',
                            '˂ϘԑœǕû#ɔʃұƭѵʼΜљ¢\u03a2éÀȢœǽ®ŹʸʉȝϛΌӔ',
                            'ȳǃԬǠÂδѶʿ\u038dҍѷ˘ʒϠʑ˷ɎҭϾљâȗ£ZʄɰԈѴª\x8e',
                        ],
                },
                {
                    'name': 'ϋȀк˝\x84ÙİȅӝкĩǁŒkϗˎĔøΪҤŊȦȢΗʀˤԫԆǎǘ',
                    'version': [
                            -6320041319068614629,
                            -7844283464785206802,
                            -2507171626138066419,
                        ],
                    'about': 'ґτŭôӈàü˸έȿ\x98ţҎ\x82ʚшˣπӤʹžǡŏʍpħɡǤсČ',
                    'description': 'Ҩ\x98ɍŪʋƐ˓ɒŐȄǢȈтüCӶŔǧĝÈҦӬхkЄAӃ˭lÝ',
                    'authors': [
                            '\x7fЈXǂȀƈ˶\x96ѡŐҰ{`˷ȶԕϯ\u0378ҘαĕɋħϒЏЧʢ\x8eέs',
                            'жǻý˸ϏЦʿÎͳģʚ˒ʟ¬ʫґΦӁҪԮȖʲƚϟЖɚϱĲҠę',
                            'ɪԥ˥UyňǐԀͷˀȷmЃпȟεҸЂLÝӸȐŹȰнѠѧлӌǗ',
                            '¼ƁǬɹǯǷѾɽóԧͰЧ-éÕӟɢ_ʛčêϋϮîŋǎȖΡȖϟ',
                            'ÆűȗЂEƘӋȹӶҒʮɟɛSź\u038dċ:ɹħà˜ȺԎОâƌVˈέ',
                            'ȏȍѲƒ͵çĴΦȐƒλҠĐαˉϹԑ;ȰғŉˑĝАӕϊƃ¿ŨǬ',
                            "үȖŔ˧ѫȈȅԂ·љоϕώƗɬ\u03a2åΞ΄ӐbXʤ'ǂÄǓ\x8aрȩ",
                            'ҧĂȉѡŝǯȋŸƩıǴӕżĺfϪю¦ͺȇ϶ЊȿΔɺǊΗϧυ±',
                            'ʂζ¥ηҥş',
                            'ΛΒҘ˶ŜвJѺΰʻûҚ¬ϧʄŌ\x97ͽ˙ŞɍƑwţ_óŻ҂ͲŃ',
                        ],
                    'licenses': [
                            'ǞũƎ\\ʜèɈĶȬɠуӧЩ҅˗ԗҭȨΈѾԜ\x96ˑαƼɽÐʁήã',
                            'ċŀқȝЌÁϷƒǊӗźшҘоϙǊ˸ʑВԥӶǽ,ɡӵĊѮċͲÐ',
                            '/˹ξ»ʘƻȓΥƘũ˂ѷWͼұӤԅұƕ˵ҽīͺЍжЍǢ%ɠÝ',
                            'ŶЁÙϡʃ¶ʱĝӇƵІΨē\x80ϳӗΨÃӸ˶0ʸԝɃЙưπ˙ƣɈ',
                            'ͳςő҈ÁƫȿɂѰų\x8bȚÆя·ȿ\x81PѥɘϟˌUǝɕЬƝУʓϼ',
                            'ʶȉɢȥýѣƶŅǊҞ<Ԁóʓɝáӭ҆ΐąХē҆îwːϑВЛƈ',
                            'ϨȫăɆӟпʀR\u0378ŘğŁ',
                            'ѿ˚ƵOȢŬҍȔ»ԕˬ\u0380ȶƑӶɱĽżę!åɚ˽ћΊGȄϢφψ',
                            'ЏȥɑšŧǡÌӏÄŹ©ƳТȭѧÑ\x87ɺʔǄųŷÐˤӒČӑπǔ^',
                            'ʯʹȷѴˈ@ƌҸƜҬǙǖ\x9fɭƸѯ\x8cĨ·ЦϮЋ\x89IͽΫѕgş`',
                        ],
                },
                {
                    'name': 'ŉȬԐԏˮ0҉ǷνОӁӕџ7ÙЌҾ«ҬȮǳԮźuͷʷҎɛӇҘ',
                    'version': [
                            -737217980961658145,
                            -1882084922220037828,
                            -8159993518418495875,
                        ],
                    'about': 'Ωϵ£ÈȦ_úµɸǥϬ\u0382éҩxзύȿЧҽвАȋҞԈʙȾѬŃҚ',
                    'description': "ҪδϬÊωӛƛ\u0382sˀӿtčÿ'ɣǌ¯xҏƋҖԋzȵÍʝŮŌӿ",
                    'authors': [
                            'ˑˢȐǮðͻԚѩԏuƪҦԖɕϻɇʓηшϠɄƅˁҐ˻!Ƭ¹έ\x9b',
                            'uÚɭľҁҴǰ˞XьąɍφŀϵƆʢƔ\x93ˁʩĤ®·ØɃΏeГi',
                            'čʝŒљжɼДŖϣʎ@ΐÎГӁχҥШűљÑјpЋOɪѦôƓS',
                            'Һʡωӑ˭ғrҺαǼΥǸɴńϢIʵϗȫҩԡ)ɭӦƶɨȍĝԕƐ',
                            'ƧӛƾӽǳΫʮћΘӀԥυΰŵϠԁѕʞԎ¸ˁɺȎϢò\x80˫ԘÅĎ',
                            '£ӷȋÎѪђ\x9aʕѪԬǸÚĔýԜĮҪҋ+ãʷĪЂσĎKĶ¬Ɓī',
                            'ʿҞҨбϕːԂΔɎҲʡҰͿϞȝѿɪԩеâdĂͲƜЪѠȡΝUˉ',
                            'ī(÷ʃʃĿnÒǈÿӌһЇ\x98ĨΛ\x8fжһ\x91Łúһöˉˎ\x9d¦Sʯ',
                            'ʱЖͳʋȍќȣΟfХĺɀ\x89rƦϥ˽Мґ\x92ĈĕҸµ˰\x9bÛȎxѢ',
                            'ϴ˳ʌɺƷfǟ҈ɓϮϸѱϬ˾ĸŽ.ǏĳϮӨ¬+ĊƇØΉƿ»ʆ',
                        ],
                    'licenses': [
                            'ΉϥÞēȸϏśŷË˄Υф˪ͼѾbΦƢҁѡτ¦AʒųԫĢżʨς',
                            'Ԩ\x87Ǘ2әЎĎ©',
                            '˒ϭӊœǦçQɄɌÍťǝ˛ʜPШ\x93\x82ɲǞ\x80ǲǻ˦ʹҘүȡŨʃ',
                        ],
                },
                {
                    'name': 'ǖԌ\x8fЮǲǿζҀǀϯҺэkƛԇ~ϚўЩĠ=ʩȕԮ,ĆҾҥĨϔ',
                    'version': [
                            -4343878747287293569,
                            -4707407530141818417,
                            -7778901508938383085,
                        ],
                    'about': 'ФǟǝžӊƑцͿÑ5ʯЀƞеƝăЍıѻƏȘæωĺ˩Ƽ/Ίhͺ',
                    'description': 'ДҁˉƛȡȸВΤƉȲ~ӴǶ϶ɿӥԞBɇʨÕЕzƊΒƳēɺĜɼ',
                    'authors': [
                            '3ϯɞ~þӪïσɕàѕž҂ı\\ɪЌıkɆʦˆϗdƥ˫ĵÄЙЪ',
                            '˜Гκƕ\x93ϑbȸ\x83ŉɳȀ¾ѼȬɎȩ҅ōʷɞŪǏƬΕĥҙCĩР',
                        ],
                    'licenses': [
                            'ӌʵƁ\x95ʮŒλ',
                            'ԚųɗƢȎ9ӐϑǰёйӼӐƂΘ±ŠКАͼԗҶŎĠкń²ȮԎ҈',
                            'ʇϯɎ˨ϹǔăΎȤȶǪ͵ʎ®ÅԤӧӡăƮ¸ВƁҋƿӊƩbΈѫ',
                            'ȏɌʕʡԂǶȧƎĉŤ§ІΌ\u0378\x9aŢɖΛԪDӅѢ˂ʿąȉ£ˀзʑ',
                            'ϫÒƺÓǰ҉ƱŴqɾʟԮѰc3Í˧ʺʩȂʡŵҟӯԈӭËɖӣ˳',
                            'ÙǄ˫æɣƸҹÐ\x97ĖԛεϳȰίɥ?Ϣ\x96ϥ˾ӷűІ˔Ģʶγʅȩ',
                            'ϿԈƒ˻\u038bǙę\u0378ЎJ˰мσМßÏҕѻ˻ęϕƆԊ+ѝԬŘъÕΫ',
                            'ĐЯĕӈӋħǽFӼ˓˔óüǔiǂÕӤ˩ȳθвԈȻԤӊϦēʹŷ',
                            'ƀ£ҙѡąʛɌ@ҢĬӵЊδӔʙʎƅӡßťƼjƂƜАËаǬѯá',
                            'ӗŌӆrʣԒƗxʳĩӘΘǐυȿ¹ɕ\\ӛʑЍˎӌTеS\\ȜЁX',
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
                    'name': 'ΛǎH',
                    'version': [
                            -7051745842802173333,
                            -2125422622827100467,
                            -6097388804402866133,
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
