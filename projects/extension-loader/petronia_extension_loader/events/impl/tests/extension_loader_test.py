# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-06T22:09:17.033617

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
            'name': 'õǒʥҳТԊԢҩϤ\x9cƆĥºàȲǉžʵƪŮ\x96ɠĨаõθ¢kƔɂ',
            'minimum_version': [
                -9021464067315246532,
                -6054451480399700890,
                -9140189377452937996,
            ],
            'below_version': [
                -58496828819867998,
                -5108005967549936100,
                -5294419202638579674,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӖԃԪ',

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
            '$': 'ӔǔMȴԐúҌ˥өĈʼ¹ČÀΐ¨ŅØӕȅĕƱͼԨǋ\x8eϬиʰȕ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 4702493825248091442,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 265083.23891061713,
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
            '$': '20210206:220916.944596:+0000',
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
                -6573513780879268978,
                -7570841505741347467,
                -1239630022839417965,
                5086722973417965513,
                -7065302512768883666,
                8541532107062241058,
                -894484509822557939,
                -8110911771827602473,
                785224597144808315,
                -8869167372375083087,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                -80915.51247448938,
                673361.6618008276,
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
                False,
                False,
                True,
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
                '20210206:220916.945859:+0000',
                '20210206:220916.945879:+0000',
                '20210206:220916.945892:+0000',
                '20210206:220916.945904:+0000',
                '20210206:220916.945916:+0000',
                '20210206:220916.945928:+0000',
                '20210206:220916.945940:+0000',
                '20210206:220916.945952:+0000',
                '20210206:220916.945964:+0000',
                '20210206:220916.945976:+0000',
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
            'name': 'ȳωǽťϟĶШӗ\x9a²ʳяŷбэǋʢ˗ÖɳʻЎˀζʹӇҽĚ\x81ш',
            'value': {
                '^': 'float',
                '$': 994053.4892782043,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '%',

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
            'catalog': 'ҁç˶ūʮˢӅȮкɠʃТӡɬɼpѦŋӻԧƈѸ˅˔ſʙɵо҇Ƭ',
            'message': 'Ñ5ƳɱӆѐØȝңӊӘȅГċцӋˀ˦Ԫʅ=ЉɢƛƇӮҴȾȈ\x87',
            'arguments': [
                {
                    'name': '5ʴ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210206:220916.938333:+0000',
                                        '20210206:220916.938367:+0000',
                                        '20210206:220916.938380:+0000',
                                        '20210206:220916.938391:+0000',
                                        '20210206:220916.938401:+0000',
                                        '20210206:220916.938411:+0000',
                                        '20210206:220916.938421:+0000',
                                        '20210206:220916.938431:+0000',
                                        '20210206:220916.938441:+0000',
                                        '20210206:220916.938451:+0000',
                                    ],
                        },
                },
                {
                    'name': '¯κôʁú\u038bŪɼĚµϡȏӠξƛҮǚźϳӯdg\x8aαѥȳ\x82Ѿ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ЍI\x89ҜĬыÄɞќűέԕǺʶKΖΕɃǬǅþE}јԪ4ӊŕȍү',
                                        '°ʨΈǽˊǖ\u03a2ɢǧñԡó4ԮÄ\x82˂ǃǻǸҕçĩˎÙǃ1˲\x8eŅ',
                                        'ϊ/Ðƌ°ź\x87ӚҴôÆ+=ˀʶQ\x83˦ŉƍÁ˔˞ȗϤӎϿУ&θ',
                                        'æΐ˙ͱȃԭΓͱĳϙĺäƳ\x9eɮ˩ǉԂΤȡéǘЃбѲĚΥ\u038bʣZ',
                                        'ҕТȍȡ\xadǞиϹɠ¶Ϳ5ѴψˇƜǬϸǂԁǲϿϧ§ƣŃΠ\x8aŢС',
                                        'ҢBЛѠԀ0ӡƏ}ľ\u0379¶ɌΫcđūόãӄϣƀČМԣĶӹɆΎҼ',
                                        'ҹˋˑ҃ЗЏҫɀjǬŤУ±ȫҗǂԣȵҐɧÆѭģȖɨ\x80Öɒ\x9e¸',
                                        'ʒȭʍͷnĮάǼȸѝʗѺѕǵкŷ;àҩ\u0381Рϲ·ďǺ!ѳǎyӭ',
                                        'ӳӐĊЪωʊӤɤĊƵ#ҌΫ˓ŨȭǭɳƆĵЈԔҸkʵŌɞϞΚÈ',
                                        'ѝԞʙɃƑñΟ|.ͳƜɘѻĦɐȼĚțϗǪǩƆ˚ОѸ+˗\x88ӽ\x8f',
                                    ],
                        },
                },
                {
                    'name': 'ÎϗԈӫ\x85ˮӟψWĪ3PĘƾtϯӍȲ\x8bȐδҕÚϤʆgҶÕǘί',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
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
                {
                    'name': 'o5ШȊǽ\x8fʘў˖ʯӑȩȶӶíƘΧɍƷʉDħǱî϶ћ˱ǈĴ!',
                    'value': {
                            '^': 'string',
                            '$': 'ˤȱǍʿʆĒʨѻҀ˳ǧ7κӸѻиǛϫYʄԘԡ҉ƭYЇҳƝƹɋ',
                        },
                },
                {
                    'name': 'ЇˎΪĽcǾċɽӶӸP',
                    'value': {
                            '^': 'float',
                            '$': 785878.2837544006,
                        },
                },
                {
                    'name': 'ӒǊ¬ϬǃжēĄ˽¸s·ϽɵǑκĹϱƼқѦȶʡŠ)ĳӮОǱТ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        3457150979545717369,
                                        -7072524881125175198,
                                        8025313704156198083,
                                        6485831362446021180,
                                        -571353825949433546,
                                        5218068904889630177,
                                        3742290318890431766,
                                        -8697083546137917020,
                                        -3511353943898832971,
                                        8043809901960171920,
                                    ],
                        },
                },
                {
                    'name': '\u0381LΰĕôÄŝơô3ԨϝɠÁFӈȩ/\x83ɁȪ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -6510782220489044108,
                                        5171640534173828087,
                                        3157491766112429108,
                                        3322043549501408017,
                                        6658884557809292624,
                                        -5016812414838175768,
                                        -2079655236314266913,
                                        1626363497786211870,
                                        7860855621961545432,
                                        -1529579931331361002,
                                    ],
                        },
                },
                {
                    'name': 'ͳɼıөҾГҙϸȅΖҸ˻ǢŦΫƟƨöĴԏƽӉԫĒĐӟ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210206:220916.942090:+0000',
                        },
                },
                {
                    'name': 'ɜΙӕÕƋ˭`ŪȒȺ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210206:220916.942390:+0000',
                                        '20210206:220916.942411:+0000',
                                        '20210206:220916.942425:+0000',
                                        '20210206:220916.942437:+0000',
                                        '20210206:220916.942450:+0000',
                                        '20210206:220916.942462:+0000',
                                        '20210206:220916.942474:+0000',
                                        '20210206:220916.942486:+0000',
                                        '20210206:220916.942498:+0000',
                                        '20210206:220916.942511:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ѬJ>ήǛдǊȃΞɅƬ½žďϻΪͰԏ˩E½ӞΆ\x89ʶΉǇj\x8dÐ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        False,
                                        False,
                                        True,
                                        True,
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
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ɗŃ',

            'message': 'ʬ',

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
            'identifier': 'ŞϻĜɺŝͻĖħɚwɿɣϫƈAʍѻ\x97эˎ£яR)²ˠϤҘˤź',
            'categories': [
                'internal',
                'configuration',
                'os',
                'file',
                'configuration',
                'internal',
                'os',
                'network',
                'invalid-user-action',
                'network',
            ],
            'source': 'Ȱ˨ɨрǎĢЕъ΅рǿˠ;ƜИEϓѥщōzCӗѭż˪φ\x9aǋʼ',
            'corrective_action': {
                'catalog': '6ҘіXǤĊşпъŮňȘ˶ӄŵϷŧ˜ŔѡӫѹĨºҸ±ǈ\x9eËɸ',
                'message': 'ɑωǄșʱϗʯ×˦ŋ˝ǄӒƫôԃ§ʵεЁȐԋЌǑϬØʐʜ˽ɪ',
                'arguments': [
                    {
                            'name': 'ӭ',
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
                                                        False,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ԓʯ!ƭЃƨüʾӁсӏɜϵÆӃɼюçûΌŵʦĘÕϖǦɹȦӽ³',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ʮȦȠΩBǮόɬ˧ȏʵӅԠѣţÎǒĶɑ˟ҦϷĬùɹБԐŖťà',
                                                        "ɼâƲeŅӞ;Ɂϔ©ǠЋԜԍʥȮƏаΚȽ®VďČӌEQ'ԫt",
                                                        '¨žʝĖƐͶÆǥē˙ҏсƫЊҢɵƕÑ\x99+ƽƉĭŘś9ˆҷΐǽ',
                                                        'ɎѾѨĥчԌͿϴҼdˑiŹ ÅͽŽԄÀƺɁƐӹϯʼЩӄϱǳΔ',
                                                        'ɘԙԜдӋ˨ˊҨОÎҖőɛӃŨǁƬАȮǜůø0Ҵ«LʲжѥЉ',
                                                        'Αӡɵzɮ\x80ʡʲΎҵ7ӊνҝōϒ˰ƱҧԀʓЅʠҌŢΌӯ:ÇЪ',
                                                        '\x9bεѨŇҶӳӷMƗҰ˗ƿńʾЉШũɡ´pΚʄ\x7fЋүȎŇҰŧӸ',
                                                        'љòý9ǎӘǉ\x93ϼфӇȪƷɩϮԂǕƪԃϼǒђΫÎϲǕҶХƺê',
                                                        'ȱɄмУɟƻоѹŸʅǐvӛςȬ³ҫqε\x9aƘ|Ψήͺҝǭɭ.ʺ',
                                                        'ǭRн҈ǵLŤīҽӮāЩѡŒԣвŐƗͰ\x92őΝԄϟɢθƆɕΙŰ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ϙ˸¢˄Χ',
                            'value': {
                                        '^': 'int',
                                        '$': 6871022976362588716,
                                    },
                        },
                    {
                            'name': 'ɬΊ\x8eRǂШљǼјɟҥҜǳӲзӹʥʬūÚȨ˪ñҢ!˽ѥǨʘҞ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        914741.8386178263,
                                                        587831.0700065129,
                                                        356438.0573341898,
                                                        507817.8473266794,
                                                    ],
                                    },
                        },
                    {
                            'name': 'џѽЃȸԎϱoӄƊƳʦϮʾДɃ\x8dԍƻ\x9cŠӊĹǭĢº\x97˵ɐԗÛ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        -56619.29076964469,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӶɌɉƀ˥җҴ×ϬɾQúԖxɃѾԈ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210206:220916.934550:+0000',
                                                        '20210206:220916.934583:+0000',
                                                        '20210206:220916.934596:+0000',
                                                        '20210206:220916.934606:+0000',
                                                        '20210206:220916.934615:+0000',
                                                        '20210206:220916.934625:+0000',
                                                        '20210206:220916.934635:+0000',
                                                        '20210206:220916.934645:+0000',
                                                        '20210206:220916.934654:+0000',
                                                        '20210206:220916.934664:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ȞˇǚƓʋÄӽ҄ӏӫЭЍѐǸɺ8ŝѦĔɷˁȍɴɰҜ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ӼȩυѱѮϴ\u0382ԔƋԝπѳͼ\u038dĨ\x92Ȝѯ˘ƉƻưÿęȅWŽө-Ӟ',
                                                        '\x9eԜŘ¯Šкʉˍϳӎxɰ\x88¥ĠȾɛ˚ƔĒҥԒ\x80ˮĶĹıҕяѽ',
                                                        'ϬȂŀ˞7-ԋόѧσԗζʿʪӌǃЃԬ˟ƉϞkѓϑҞɕȖ¥Ҏf',
                                                        'ˋѷƄeҊНѽÒǂԛυ³ȓĚΞѮɱΩķKĢӍ\x91ˎŌȯƬϮɩʠ',
                                                        'ǚɆǶäΞ\x93ʍд˚ƤÂӲûӒŅhѹͼƊҬ^҆)0IJɡζİ\x94',
                                                        '˜ԔѮȦʆȂѕǥԘǝț҆ҜÍĠsàóƹŭĖƸț_ɁŬͽǩɛӶ',
                                                        '\x8fƔ\u0381ŽŁʗƇѸ\u03a2ҐљҰɏηͲˆЯɮʪfҀȄĞÑцʟůǰ²f',
                                                        'ȎɔŶΏїɏWСιǢŇ\x9eĖɑʖӜԣÿǆʞЭÙӯЋ\x92i˚ēɧɟ',
                                                        'ȔH2àμȞřÚԩҜҤϱөϮΑaҼиƃ\x99әe+ФΎҗʐɔƬƯ',
                                                        'Ԟ˦\x9fлЃѺŦØɶԎVʲҕχҧėѢ§ŃŤѣ°ʊƩҿƓȿԒϫҰ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ЎĐҜ',
                            'value': {
                                        '^': 'int',
                                        '$': -1015402188462436937,
                                    },
                        },
                    {
                            'name': 'șҼǯˡ*ԆΓ\x95Ѥөщʩҡб5s\x88ԡҴɞťӝҳǬлŹӺ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -3687988540676506926,
                                                        5771183738355599718,
                                                        8923777932587784004,
                                                        -7288165973467972110,
                                                        7855763674281101045,
                                                        -8431728956441700062,
                                                        7431880828310569720,
                                                        6980938884565982124,
                                                        -1496325564466534253,
                                                        -5652073602408033493,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ˏÙϒҀΚǩĺҠ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ԓāɒɻш«ӽɯŚÆΩɀμ˰ϋƩǊǲʤɈŞԠ˃ǙȲϷѸƤĠӚ',
                'message': 'ԦǠƶɁӀƉԖ$ƉΰοďiԭŲҊɺƦ\x99Ҵɟ`ßԈНԃȣҵрϸ',
                'arguments': [
                    {
                            'name': 'ɔ¹ʼȨϟʨˀʡηфҽƥĖĖμтųÝ\x99ïȯԢ˅ǑʐbХúƸȣ',
                            'value': {
                                        '^': 'string',
                                        '$': 'НĠ)јȾšˑяΆЧ0ѳĵưƾƾˊ·ÑϕĜęщВȤǠёќǑƐ',
                                    },
                        },
                    {
                            'name': 'ŧýӆÂѧжK»ԓǼκɳ:įѣѪhь#ͱŖȳƆʠɩVʭľӽ҈',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        4645861815813302544,
                                                        1933611710917704086,
                                                        -4239611381252289305,
                                                        -13192732896113389,
                                                        -6317073164357151109,
                                                        -2013954615518390353,
                                                        8669011873944003692,
                                                        -5717749162983841838,
                                                        -1420335001485289434,
                                                        -5017720250845320382,
                                                    ],
                                    },
                        },
                    {
                            'name': 'өȐ±Ҁ\x80үӸ?ȌԂѻҵ+τУȼӽȷƽȠʒҴĞ\u038bʡČϞ҅Ӱѫ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        False,
                                                        True,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ėԎΩZҊǉ\x8dɗϒíƀʑϻːɰМΎĽͶ˩ǘö˕нόИ\x9d8ΰ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210206:220916.947865:+0000',
                                                        '20210206:220916.947887:+0000',
                                                        '20210206:220916.947900:+0000',
                                                        '20210206:220916.947912:+0000',
                                                        '20210206:220916.947924:+0000',
                                                        '20210206:220916.947937:+0000',
                                                        '20210206:220916.947949:+0000',
                                                        '20210206:220916.947961:+0000',
                                                        '20210206:220916.947973:+0000',
                                                        '20210206:220916.947985:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ˉǴȢć²ӉëϟӖʃη»ϳŭɅͽƵиńû',
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
                                                        True,
                                                        True,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ɒҐƓЄʏкeǅ\u03a2æƂјgʏЖlȤщÈѶƎ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
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
                            'name': 'ªȭκźǕÛ˗Ϛ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': '\x97íӒƗȁ;ΈtƬΓԔʸƍȆ϶Ź¿˹ÕɨģŀӪĎʇГУҘӾѼ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ďҜQ=ÐЄѝόͲĺȯ-ӳԃҲӛÛʊ¼¬ҒԥҘϮǧӧr¸őɢ',
                                    },
                        },
                    {
                            'name': 'ȀǓ²ѕǪ\u038dɨ˚ͿǠԐˈȰŪ\u0383ГԥēѧΖЫǱöРĢĴƜʅɡˇ',
                            'value': {
                                        '^': 'float',
                                        '$': 291787.47615458665,
                                    },
                        },
                    {
                            'name': 'ȏԛɄѳӔԠЕґҏҟǞӎˏυʖƎʌƳԅѸФËíγßӮŜҿζÇ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ɚƳɕ˘ƣ',

            'categories': [
                'access-restriction',
            ],

            'error_message': {
                'catalog': 'Lӻ',
                'message': 'ʝ',
            },

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
            'name': 'ĤңԂɎͳʄѮ{ϜЩƣŭґЭ΄ҞЌǟʕEϑƫίЎȕ<Çàƈү',
            'error': {
                'identifier': 'ĪĴ˧ƽӋΓüf\x9fΘРȗɃ2ƅĪϩǭźΒƤ\xadȠєҗ҂љӊİŴ',
                'categories': [
                    'os',
                    'access-restriction',
                    'access-restriction',
                    'os',
                    'access-restriction',
                    'access-restriction',
                    'invalid-user-action',
                    'os',
                    'invalid-user-action',
                    'invalid-user-action',
                ],
                'source': 'ɣӓǿγȼŖƑƍϙȨ\x82ҵȅУƾӆʃӑď¿WхПãΝ˺ƴЏΣξ',
                'corrective_action': {
                    'catalog': 'ºӴĬҁг®ͰˡóśĪψϽ˾ŢϋĪȝž\x80ȧԈƮàǞǣ\x91¾ªμ',
                    'message': '˫ÂΓ˫ǒΘ\u03a2ПȀΎåʹҸʡɴĹ\x8fɱǛЃ!ɳϧʱӀûŻɤΐө',
                    'arguments': [
                            {
                                        'name': 'ӂĤѫѮӽ×Үԡ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˘ȆƛϦ\x8bǇҧfõǏԈ;΅Žùçʰ+сΪӒƧʆɵɛԁ\xadĺƍ¸',
                                                    },
                                    },
                            {
                                        'name': 'ƛvÄôоȀ\u03a2ǿͶ)іʣwĐϑ7θƋҞ˾Ɇΐ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'éɒԬŋҰ˺ɠƋ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ƺɈŸıˍȮӳɚǰΗыӞҾGҩ5Ԩԉ\x89ŝӚȪЀӥԅϧȜɅӂʕ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7755327341988710184,
                                                                            282496321529606093,
                                                                            -3380233391168306170,
                                                                            -8080629874137652395,
                                                                            -1915464717897216671,
                                                                            7796062559084540355,
                                                                            -3292207947080196485,
                                                                            -3630971152569109100,
                                                                            7359603254823437319,
                                                                            5440720920400139132,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '}xß¯˰ѾʷҒ\x83НȻ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2082425903684039660,
                                                                            -430785166547785558,
                                                                            -5266772246685945645,
                                                                            -1792707077942523115,
                                                                            -8268099439548270852,
                                                                            924025452300341198,
                                                                            2892711171850641123,
                                                                            -734898458384650782,
                                                                            7890688628903337986,
                                                                            6551502528915803244,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƅBƹTΊԜʵĘ\x80ɁτÀԜό¤ãѴƄxЪˣĔ2ΫҒ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220916.922492:+0000',
                                                                            '20210206:220916.922530:+0000',
                                                                            '20210206:220916.922547:+0000',
                                                                            '20210206:220916.922560:+0000',
                                                                            '20210206:220916.922574:+0000',
                                                                            '20210206:220916.922587:+0000',
                                                                            '20210206:220916.922599:+0000',
                                                                            '20210206:220916.922611:+0000',
                                                                            '20210206:220916.922623:+0000',
                                                                            '20210206:220916.922635:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϛƷƈōӽʔʿȚɻʩ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 324308.1126584501,
                                                    },
                                    },
                            {
                                        'name': 'Ŭĵâ\x86ĤҗyƈļʡӌΝͻćӝǜ¸ȳȱ˫JͼŸԓ΅ĭƍ˦ʩǈ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8195127568414181964,
                                                    },
                                    },
                            {
                                        'name': 'ʤ˦єΰƠÀgǘ\xadÕϻΖΗDƕrw˗˚ЊҀʘЏҝΚʯ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210206:220916.923691:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԢǤрœ˗ȻĸӻΛ\x8a˗ǔԊԧЅԩ\x8cӊ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 525750933298826288,
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': '\xadЩ˪ăѺԇʪÒӧɩǨлԬΛξ4ҥђɶȜԢˏ\u038b\x93Ԕÿ˾\xa0ҕʸ',
                    'message': '˩Ȯ\x9cʚ_\u038b\x96rvˤúƤǡŧˡѧӗƃԋɬì͵ǺϨ*\x92ɻАМ´',
                    'arguments': [
                            {
                                        'name': 'γbЁҔѺҦʽ2ŧŦƎ\u0379ǾυǖжЫҗ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1730957968139306168,
                                                                            1096145731892653476,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȇʀŴbŷөӵʚǸǄņшœʺŰąӘʾu˯ǆ£ӗӬ\x8fƂŒ\u03a2υɽ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'δŶǝ%έʅοʩіλǰЎŻ˷GҔÅDɒ\x8eÂ˙ƞѩͽæɱƮ_ҟ',
                                                                            'ɫӁԨĐ\u03a2ŞͲͷˑ˳ǁНѭеϜ©:ԪԑɱУžņϣύģŹѣԩӥ',
                                                                            'ɁÂӑМˌЊЯȭËɰØφʴѨȋƹȷɤTЦƂÉÜʌмԈσđ[ғ',
                                                                            'șҼʡʧʙѿ\x9eEsųŕ¿\\Ǒƍҙʵ˛®Ϟϱˮǝʂ@ӳɆȣ҇˃',
                                                                            'Ϡ˄ʏ\x90ǋʽҫȍϿļΪӦ0ǴɗĜκĢϠ=ҶБǨ\x80ξõΠӾƒ\x81',
                                                                            'ӁӠėģſυǈɃʥǫĄΉˀ\x7fʩ\x8fĻϸ$½шЮТƒƭ\x90ɵ\x9fäP',
                                                                            'ÑЍ¥ѴҴѭáL\x93śωΨ¢ǗϊѦǉXȏӯͲӮĴϕӜL҅ҒǯĄ',
                                                                            '˾ƓӡѝξҶɐǷϊΛďɨѾɬīĲʻǗɔўū\x8aϢѫȉȠӂß\x9bї',
                                                                            'ŋτχgѢӫĭЊϸƠҖΙĢƮɰ\x95žƊ\u038bϓɤɥǪ\x9bϼğ\x8dȁƸʛ',
                                                                            'ȌъѧɌƂҴĝŧгХɫχ΅ʭ¯ĶʧȊƾɧάǓмƾČƼӼǸѪҬ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʤ˒ɘАԆҺ˙ϜŉӮ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 80444.76916969512,
                                                    },
                                    },
                            {
                                        'name': 'ϬƐӯǯӫϺ&ґҸwôаζäĽϠР\x9d½¿ƕǩŷÏ´Ԕʃӈ`ї',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '·TʙԂ˺˃˝κʗЄжõ҂ƎǭπʽvѩðǓłȌƿW/ǻԬʒƴ',
                                                    },
                                    },
                            {
                                        'name': '˃ѩ=ϋѪ~Vύϣž®ҊӁƈɇЁ×ѧřǐ˰;һϷҪћыϏőĿ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ύʔť\x99Ǡ\x88tRȃӌùсι˨ǍЮěαԛϹɯͰJ_ʮòОҞd˗',
                                                    },
                                    },
                            {
                                        'name': 'ΤŇϜƎӗ҈ȕ\x9fϷǛѳ˛ԗΆȚαϙoЬĴȜԔÓȱϬΗХԄɬȝ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѶȶжеÛÚȋУŉʌågщŦÎ͵ϺɐФțêІӧʢȣӈö\x9dό:',
                                                    },
                                    },
                            {
                                        'name': 'şԅЖӬȇҋȒϋɎɳ˺ҀJǄƏ$.MÛƎµȶŎРTʀ˶иЈ˳',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210206:220916.928172:+0000',
                                                                            '20210206:220916.928205:+0000',
                                                                            '20210206:220916.928219:+0000',
                                                                            '20210206:220916.928231:+0000',
                                                                            '20210206:220916.928242:+0000',
                                                                            '20210206:220916.928254:+0000',
                                                                            '20210206:220916.928265:+0000',
                                                                            '20210206:220916.928276:+0000',
                                                                            '20210206:220916.928288:+0000',
                                                                            '20210206:220916.928299:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɥЄӆΡϭǓɁĘİ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 950517.3784555322,
                                                    },
                                    },
                            {
                                        'name': 'ǜАқŵɹ\x81\x98ȴʂνŜЂ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӔѮĳўŧǔ2Ģɭ?ňÛτʬԆϭкϥǺŷĆëIǲƸŔ˖\x8eδʵ',
                                                                            'ȘɫʭҢӆȒĹЛÜΊ҄ȪǺ\x93ǭтŬƙԋȡʹȥŴʯͱ\x8b¨ΥŖɐ',
                                                                            'ōľƤъѡsɯ˹ЮɽŖ\u0383ƿ«ӸǆƴΣѮĹ"þɯӿŋęŠ\x8bĆʋ',
                                                                            'Ӹʲ{ҴƵɭΊԚFȅ\x97НѹÀƿĂԝ\x88ϓέǲːԃ}ȣ+фŜÿͼ',
                                                                            'ģÒĳ"ǇϻŚԎ;\\ǞϰϡҎɱԦĊǫˇƫҒȈͲԦɈŤˑ\x9a҄œ',
                                                                            'ʩѩεόԧңЋӢόͷ¨ǲ\x96ɞĳаˏĨҙԟɨπÖ˻ъȤĩŲӗƐ',
                                                                            'ǋĠϺЬżϾΨͼѡ¯\x88РɣÄӵĵ-˼ŮǰӅįϑԥ˜)Ŀїļ\u0378',
                                                                            'ÑŕǦ˭ХÜі\x87ǙϛɏΜ7ĀѐϦlɓP\x8cŰ\x93ñŊ˕Ǒɿѭϋǭ',
                                                                            'ӬҷɢşęҙŁҥҕĨɌɫŖAˉʙǢΊɥgДýȦǴϥÖ\x945ĤΉ',
                                                                            '˄фǖàʌ|Ӷͽ\x94ʢʲ ʘόǗҗ\x9fŒǐ¼\u0382ΑБʾŊÃ\x92äĆá',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŔОĈ\x91˦ЛȾʌŗϕԇЄ5ĨTçŇëϊұɓFԮuюЭҦʱĖԊ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 287555.7810041558,
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

            'name': 'ʫ\u0379Ђ',

            'error': {
                'identifier': '!πʍƀʱ',
                'categories': [
                    'internal',
                ],
                'error_message': {
                    'catalog': 'ËҸ',
                    'message': '\x9e',
                },
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
            'name': 'īƃ\x97Ǣ\x9c²ύцóǯλƔĤȀӀ«±ϑƾjƟhĠǋŢǻЯǸȗľ',
            'version': [
                -3728567712652522278,
                -8738936339728642753,
                -5737989033570691532,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'У\u0380c',

            'version': [
                -8398706661465343805,
                -2762672121733048871,
                -6222655445023334091,
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
            'event_id': '¾ΈȉӵНǈҟҲĚɦƽɶĹÖάÐʗΤӾų§ȈčȟέM\u03a2ƓС«',
            'target_id': 'ȣǈʌϊԒĜɉͲǵж҄ǺЬʑԋƂŋ_ӗ+ƕСFΣŉҥÎҬǢȢ',
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
                    'event_id': 'ѵăοζ\x81ˠʆβÿáϐѥȳ¦ύ˸żʎƂʗrȹŗƹЫăDɏαρ',
                    'target_id': 'ȍˎ$XԓѱΩНȍӍȃӂύˣĵͷ²ŎòĎ]ӧ˯˴ЂƪһÅƪɖ',
                },
                {
                    'event_id': 'ĲÿʳӟϣӟѰʠŗӮ!ȿЄsʡÅҚҋ×ë¨äɘõ`êdʐėö',
                    'target_id': 'жȣԓ¾Ģь\x80ԙԉˋԑȆѯлČѵĕ\x97iʞƚѯ¦һӒϦ\x99ƞˆ΅',
                },
                {
                    'event_id': 'ǂѣƌШˁʾЂZŧâĻțłrϽŠВɠӖыğĶŘоƧԦʺˢ»ы',
                    'target_id': 'ρҊ\x85Ͼӗ',
                },
                {
                    'event_id': 'ђƮˌɇȞǎßʏļɕˎĎфѓȚzƿŀЛԭ^ƮʚԞYǐɀėˣǼ',
                    'target_id': '\x84ƀȍƾƒҒȦAϘĄƾǿǽсɤɥФǶȷŰ?wƏѯqύĬʤŲӶ',
                },
                {
                    'event_id': 'кӃƝѮǷ\u0378іʨΩ¹˽Ԋʖӑ˖ΩҨȧхʙͷÊǥÉƦЈ˰ĘĨͳ',
                    'target_id': 'ƈԩ\u0381-àȿφȿσĳMԂΨʨɬӂhн\x8eńҁòшɀԡˌӝʩе\x93',
                },
                {
                    'event_id': 'рǊεƎʙїîèƢȴԌӼԣũŀˈŌƐĞǝНǶȭѱƅĄӸųȥ´',
                    'target_id': 'ȼȴБϧªċ4ΒĄǴš]Ә˞ĪӣЎYӋČΘώэĽάɧɎѪЀщ',
                },
                {
                    'event_id': '͵Ϧʚ8ӫԅȚҸ\x93ΤҿęЂƛӟ\x8e!ѯŶˎAΩΰ^ц#Ѥɣѩm',
                    'target_id': 'ƀưɪԭìĩ?űė>ѣ˷ӻ\x93ǇϲӉҎύɁѡ|cŸƯƄωӺԔҬ',
                },
                {
                    'event_id': 'ăЖ҇еȠӒǃĲȔП\u0379Ǩǒ]2ʾεА˨α`ʧ\x7f<ԄяѴ\x95ҧʵ',
                    'target_id': 'ĠԨӔұ6¶½ѽFŐƑëƿȔӀԖȵ˰ѕҹċԭ˚ϛѰùʙÄѨŊ',
                },
                {
                    'event_id': 'ƶƢŁұӑҼѧȎԛ÷Ξ˽ˀԎ˔ҺŷӼ6ԞϜѺеФЩŪӤѻя˶',
                    'target_id': '˭ѫrǥиĳű0эŸtώ\x7fћȆ҃ŰѴОϫʲɭ\u038bcƦҕƼТҭл',
                },
                {
                    'event_id': 'Ő˖ɜ©ǏӶƪȓжɦωɮҗÒɨƍãģ\x8fʱÅcìĝ0ať\u03a2\x90ͻ',
                    'target_id': 'Ώĺ¸ĤuΛΩШӝζЕηĘ\x9a1Ϣ\x9eÖʡȥӟҁԆşßЕƺ\x82æ҉',
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
                    'event_id': 'ɛǲȩŢӖ5ʲΟŨȨĩÅ¥ǫӍυп8ƚˉԩƛĿƥҜҐ˱ϞΩĳ',
                    'target_id': '˻ȾԬԭ͵цËćůˠІюԀƈҥ˼Ķļǧǰ˘бҡ^ýǔ\xadȰώʘ',
                },
                {
                    'event_id': 'РђвƧΊʠǡƎϹƘҩ˾ÕԧʲǘɯƊŞĶʗԚȰԠɩҲӀʅ°ƿ',
                    'target_id': 'ȍɶƋʩɆƇƻvԄǉîÙǵǨȭͿͻҸ˭ϛʲÈýȶĦOėѸεʅ',
                },
                {
                    'event_id': 'ϑǩӏȯȰɪΙА&ǭ9ƴίǮ/7уǕĶѮÚoԮ0ǛԠĿƃ˔ɢ',
                    'target_id': 'ѵԩĚȘ˞tӕӸι˙ɛđ\x84ȤĲѸΏӷԖЗ',
                },
                {
                    'event_id': 'ȳúС?Ҝȫϙю¢ɐѹß\x84ӍԑЈʄˮ+ЄϢƙϵțЙßĦ˱Ӥο',
                    'target_id': 'В\x9eέм¢ðŊѹӯȁÊ\u0378ѰĔΒȳ˓Ήђ(pĽƀʞą\x9eҴвĂd',
                },
                {
                    'event_id': 'ħPŘɂԅ¤ЉʱǣʆԒapəĳуӍӅЛˁȯşƺĞѪƱёÄHȁ',
                    'target_id': 'ɠǞдɑέł0VͼÞèəǾӶƬԏˣ\x9cÃиǄЛůҙ\x88˫ͱΝѠ9',
                },
                {
                    'event_id': 'wgȌƾͻ҃åӯ#ԍɶKʚµǦԍȔʃЍϢcɌǏϙʶʥÕǐƞԤ',
                    'target_id': 'ǀϱY\x8d˨ԠÿΜļѝãǹ!ΏƃϭƔʘ˰ʗƃѕōή\x96ȢǏͿӯƌ',
                },
                {
                    'event_id': 'ÈˊˤĪÛϻ\x8aɝēεˇʔŻjĠϖӹӾĽĐĜѺǣΰđȪѱВϻќ',
                    'target_id': 'ǎ=ŝўʿϜΰҘ\u038dԩѭsbѩȄѠƃŸ\x9f˚ÈʺӮȢ˲ȳӎʟʘɎ',
                },
                {
                    'event_id': 'ɐρӲГɑǨҰ\x88үųЂÌʠ˚ƂƜǄѕʜ˪¥ϕϭ\x8dʃжîƑòѮ',
                    'target_id': 'ÔĤǞΥл\x96ÄˮͻųɡɦђИЍɨĥЅśΔʢɞ\x92˵ŬѝԣϺɻϦ',
                },
                {
                    'event_id': 'ΟӦъԡǲƃɋҴʖǏʎҰɣåƞԒҳІtõ˳Ɉģ¡ ȵÜǦ˕ԭ',
                    'target_id': '˅ѽǒљɃņ!˶eǒŹJǎ˱ІÙŞΞӢʝǓѸΰʘлԗϰĳʫǷ',
                },
                {
                    'event_id': 'ǎѾгȿǖ˪ǱДǄPʶɆΐųSԄS©¥чŷξˬӍɊϦΈʶ',
                    'target_id': 'Ь\\ıЫΖƌʳѥãʑŎѓƂƳљĘǧ)ƸÉӔӄϝƑπзľԪԄ\u03a2',
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
            'name': '\u038bǐѶ¯ɢγЭҨʠоȻΊ˕ѓĺćȩƃāЏ˳ӌиŲӟҮӛϿ˦ǐ',
            'version': [
                -6791054742992460067,
                -1997047233135254343,
                -2808091501627754061,
            ],
            'about': 'Ė˒ƤȲӋƯԕĤÌωɫǦšԏhÀƺʒäϋǇЈҪȎǫеѹSĴ˙',
            'description': 'ΖэʠͲӝťϺ҆ˬ0ɓƢƬȯƪĲ+ħʙҵсӞƷɀČ|ӎˑǗĹ',
            'authors': [
                'Γ$βƩʦƬɰ4\x9bƦŰҕǿȔǭĚ˯ЋϳӜ0\x9fϒΈʘǮbƨƆā',
                'ɫђɉҸӿїԊϢʘ\x95âϋΤŔǠɴƠɫę˛/Ɂ`ɣԠΙʝɾȺʋ',
                'Ёȟǖ2ЃƓŞΓŇжÑԬũĦ˳Ίʉȇdʔɳ˷Ҡԍӡ·ʡũя\x9c',
                'ùƈҫ҉ƟˬΡȮŒѧɌϧє',
                'ã&\x93ӆƋӝҫ˦˧˱ʌ˻φҁУҌSŲPɇлï\u038dɛұƳӘûėĒ',
                'ӿ°ԋҩʹϖɴпc\x90ŔʕӟŮҟԧгɶƆԔӇʂłFHŨІϹǼ\u0383',
                'юȀȹǷӱHиɐ[Ѡ(ϯӔɈfӆƭ_êˡƻƋѐ͵Ʌсήиƺ5',
                'ӬʦĐRƺȿαEȐàёӌˬӕӽϠԦĶǇëɨŻЭɌɐӉқӱΫļ',
                'ѓΐÏңʞćǄ˭ƠƬ\x85ӢņԎ˟Ϡʩ±ʵˮ˫Ɣ',
                '½ѴɔƢśȜ/Ρ\u0383ˌbИӊ˖mЭ[ʁǅmƾĠ,åҋ;˃ˈǊӓ',
            ],
            'licenses': [
                'ӬôɾΊԜƫȀғ\x80ˎΓʯǬϴ˃9йқǎh|ơŮœÊѿԉ\x80ȰF',
                'ϗїӌΨ{ˆ˒Ӱ˝ʥ½ҢưÒϮɊûϳͽˇȎ҆ϩŨпūțҞӛ˫',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ԓїȵ',

            'version': [
                -2873256870778041516,
                -2672435346303706225,
                -1134401437921810821,
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
                    'name': 'N£¬ŖÌʬÃϲԬĤȓпѵȲҼϡŽҼԁɶчșҽŭäΓӿ˱tы',
                    'version': [
                            -1069122348878369843,
                            -5756050309518895183,
                            -504639351189372680,
                        ],
                    'about': 'ȵΖ½ҟɟʂιҤΜԩюӖ˫ѫʠƥīʸƉƼȆϒ˒ʳѢƣʲɾƺɈ',
                    'description': 'ұ˧ǫĔiĐ˗ҨƂŚϵ\x9aǍɑïǗɪ\xad\x82Zэ\x98ʚɬҁǐ҇ʠ\x89Ҁ',
                    'authors': [
                            'є͵ȿЖLàă~сӇϟȒʵњƚѼΧνͻ-Ϧ˚ŌŲ*ɗ͵ѢӈȂ',
                            'ʘъΞϦǕɇІϫȪr+ѫ˞џԋωҧҨЕΛθĊʊåҙǪǡɵùǏ',
                            'ӑʿҋʟӖ-ɊĐɂЂʲҦқҔ\x87ˤ«ɹҖʄƗWʊϚӖňѫӞӓѲ',
                            'Қ;ŠțȖҋӌȤԮʽҖ$\xad1ȇȆӰƇĲħĭф2ТɁčΨ7Ʋê',
                        ],
                    'licenses': [
                            'ԉø`Sʍ˺ėǳØʴ\x91ɡͷжųĀ҃ӨүƯɄɆ\x7fлӨƇȧ©ʄ-',
                            'Ϗ]\x84єҹМѡɣ³ФAπԜТ\u038dǁϖţ£ǏϋԉȃÚӤƹӕ\x9aʼǽ',
                            'rȁЈʫ˖ұϰʷϘǐǿȔϝəţɦԙǜ^Θ[ϤıшӚ˻˃Ϊg˝',
                            'ŏ˷ʩǻˎԥĚŊGζЏӮӜˢҋůÉǘĮɲ\x85αɞΤɏʇχşΙ˂',
                            'ơѻƕ҇ɮ2ȐӚĂ©\x95đѡKjǹԡУГǼĀԇЄҾС\u0383<Ŧяɱ',
                            'Μ@ƴCmԣȧɲäҪςҴӢΨOӌŶ\x89ͶÃ®ƋӸʉƏǩƊȭʬƯ',
                        ],
                },
                {
                    'name': 'ϗЕƻƂɜ\x9fƑūǚƷ¨²¨ҴɧҁҷѿҭӴўЈHƈȇÏġ\xa0ϊȌ',
                    'version': [
                            -2059456889604387676,
                            -1564962436464791294,
                            -4611736145410427814,
                        ],
                    'about': '\x91»ùԜʞËѐʽͻҵ˛P+\u0382ԌЄ˽¯¸ҰХӘѶįӨ²ȒКѮȱ',
                    'description': '\x8eѻêȜϥDŢӭȁӽƂ˧ϷƉχҰɩуʬҹӢҶӡʰƇƆͷӐɐK',
                    'authors': [
                            'Ƥɦԡ˼Ҋǚ\u038dʛѱˁϟҵɚĲƾĶөʌԦϔɋÈͶԚUӝЌȝʋӓ',
                            'đҌȒЇ\xa0˪řѫɕ˴ΦТČӽϟ:ǳЭбUƌЭЮĐȴĝɿԊŪ҄',
                            'ΉӴҮȑŘǄĨơ˩Ħ·ǼԨҨτ]ƺðеϦӧhƩёҌűėˡʺǑ',
                            'ΘŘѨɸůϛÐųþĠΒEҶϿӹɷQф¿ɣ\x9cɅԛҰѽǽŒАDҘ',
                            '\u0380Ůǟz<ƁɊԜOǤҩīĪԎȌ˱ɀԜϔŵԌӳʛϽϻǀǡЊ˙\x9b',
                            'ʖȭɩǩ¾pȪ÷ȹĻȩɿǗȻƝʰϚԚϾεƔ˂дΪʼӣɗΏuŐ',
                            '}Ͻ§ЭˇЄӌКʢǝт\xa0ˋπĦɶȔõȮΞіĒӭжȺӖÔƆЛɂ',
                            'ȱ\x94ϑӰÇʇҶÃƥ½\x90ʁфČ˜ʨԇjưΛ*Ƕ˒ȗˆƣȒȂôɝ',
                            'ɚɦʂ\x85҉ćʀΦι\xa0ƿϙAŌҠЏӻ˼/Ҙ\u0379čČÔԋϝщ\u038dҨί',
                            '\x93љԠσé˵пɈ\x89ńɠąч',
                        ],
                    'licenses': [
                            'ĵѡƕǳŲ˳ƸѲǕΪƨЭҭ\x80¥ŪϪΥȞνӒü\u0381ʱ\u03a2êϲǚΜƥ',
                            'ɾнʔӟˆŎɿҢɨɋxŚʞɁρý_ȻɺȌҴǝ˶wİтʻǙӑ\x82',
                            'ӛӊҪKӈğˌ˧ϰЁĭsXӠɕ4åǼyΆʸΚƉ»\x83\u038bīğɨę',
                            'ӦӠȐ˪δūŅкςǤѡĔϑȭϬǭҽӼΠήǆɞ˦ēÛàδИҟͽ',
                            'ȮrɢдɊΩΞ˘ˡţшɗ¼ҎӋƭͿөΚʿųȠдЛҋ҄ȇȑȂś',
                        ],
                },
                {
                    'name': 'Ś%ƯƄďΰĻəΒΪ˧ͶƑ\u0378èþŰŘǰpα"еԟǮȨȫŌʘý',
                    'version': [
                            -5738315426083483882,
                            -7855733519187644561,
                            -6973571030541685022,
                        ],
                    'about': '˽ҽǕŧ˟ј҅ņ˃ΩѡÄùńåԅѽU˥ӅԎԊāϩ˲ʴʗǾƵâ',
                    'description': 'ҭћø\u038dǸŗɮɑĀˎɟђΟĵѬΏŝϫϡƅ_мӄȿҢХМԃ\u038dŦ',
                    'authors': [
                            "'ϪӞĭӛÄȸÎ=˦ЖȑԐψǡïЮИȧӁįѪƨɪɽPˑúџĤ",
                            '|В\x8fјѪµĘȸ$ίǦύΚϒ\xa0ӝФʈuџҩɚΘӌ˼ϐӼжԞӿ',
                            'ѝ*£Ϸ\x82Ưʦ\xa0ɴЍ\x89Кaɂӿ˓cơ|ӹƈP[\x88Ȅϥ$ʉGɤ',
                            'ΪӯӵΔǨļÎΤΥžǶԏЏĐɰǰĦŻнβ\x8aШśˤç',
                            '˩\x86˲ũсɠϕ^ϭǖǰɬūʗƗƱǬÎ·ŎǞѢЉǶаlϨνE_',
                            'һӱħ\x82УˑΪǵ,\u0378ʋāƌѣӵУʝʙǐəϚώôЁЯ:ȨЊ³ƭ',
                            'ȠВĶɢHĒĸëɏȄɤlƥȽǜϑMȯʗ{nЏ˄ʫ˒ŗҬʨɖǇ',
                            'ȻǢɠөԨ4ǉ¹˟ЁʞӥĆԜĤϿȷƪ˝ҀĤg\xa0ЩɔGȑ¬ϔó',
                            'ʊϢ\x82ˍӁÁτÅǫϿĞŅʕ҇ͰͽӴĚӕȫΧΊ\x82æϞɃԆZÕϚ',
                            '¹²ТɑÌɵǏè-ʐӱΆǭү^ӪȱđҸɖˍˡǅĻǙ',
                        ],
                    'licenses': [
                            '9ȽԬ\x98Ҧ.ȎКǝǑͰŉ+\x9cŶŗҺŲɽȾĎ\x82ǔ;ƟĲ΄İȍʇ',
                            'ĊԨǙ˟Ԅȿϱʼ\u0379ӘšȚɪʡŠɛҍÌhԀϱʊӐȌΘĕ˒ŵџӅ',
                        ],
                },
                {
                    'name': 'î¶Ԋț',
                    'version': [
                            -821881190477628259,
                            -9000352709139680235,
                            -111480318169753330,
                        ],
                    'about': 'ӲңЄĩ¬ˆwѧUɒǬͼΕԔӤÝѽ˃ɬζʌѹπĆӣАѝêȃЖ',
                    'description': '\xa0їƒϤБҥċ)Ѧòӑƿ*ԐǫȍUΙ;ˮŇӔƸ˟0=˟ƦŹȧ',
                    'authors': [
                            'ҢȸЮĦ҃єΤ¼ϊԢӵԕкǳŤѓтėĬˆȿͿϤƘɂƑĿԑȐѡ',
                            'ХǬϢʳǘȢǖӭԃȇŹ\x93ЌÙкJÜĳӚӗЂȖáĀҹĈ|Y˼ć',
                            'ϔУϞʏƄç˕ˁҢɫъ@ǘʤơԃҽ\x8dΨЫԉЦҒ$ҿСúƟȇȘ',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': 'ϙzȟȒq\u0381Ѽȟ˼ϯʻǷ}šҪ°λ³òӽϔҲ¾ņƏѲϞħ΅ť',
                    'version': [
                            -3440311103439453663,
                            -5933246801108598025,
                            -6349311932966844336,
                        ],
                    'about': 'ΰ˂ʶǺҰýǻϊѠê\\ӝӤƺ\x95ŗƈϝӡȼʯʞĜԊͰӒLƜ\x8cQ',
                    'description': 'ΚЎҥĀңƃǉσƸ˫ǥʒ\x9bғʃƤåȮƲȬЗFɠУьjɂíǇϙ',
                    'authors': [
                            'ʳίϠӑцĬʚCӌ`Ɩї2¶ξǢɯӾʶɞS"ʄŠcɇ\u0379×±ʪ',
                            'ZʼʁԪѲӒǉǯȭгѮӆϵњԌǋƣ3ӠҒW',
                            'аϘiΰªǃԐƸѧѸжЏ˹ôѮéʍϞѦÌԣʏuюυËБɤãҤ',
                            "ǿƥԒ\u038dŊȱ'ǚыԃΕĻȽ\x98ƞѕνǉԅ=ӜХϬΩёƍ˭˭¡ɉ",
                            'ɆµŻ\u038bΦѤŝȅΑʓ$ǻ\x89ѽԈΨ˭εȡ\x99*ǭƗѤуϪэɀØ\x81',
                            'ӱȨːϤǌ&ё',
                            'ϢѮ§ΡȭʃǤɠΐҀD Ж±\x8bǬļÛɉʗ˥ƳɳɼΈɗÙӊ¶ȯ',
                            '¼ӕųNˍìӦåΩǿȐҁΞƧ\x93!э˴ɝeΧȥӠїƦ˂ĞǨƘχ',
                            'ˋѦϴзʙ-ȴΎǮmǅ ώ',
                            'ԭς҄ԃҊǎɁAӠʷӴƜȺўð\x86ďπЪÇ;ъʘԤÑɄ®Є',
                        ],
                    'licenses': [
                            'ʮғοűǄќí&\x82īõɆɰČƾœƯĂ\x8cƌʝĕɳуǮϠƘŇɴǦ',
                            'ŽʴɉɃ\x89ɹҨӵ_ºȖĒŚȊӅӪΗΫaоƵԤʸƽĉÍĂӯɨҡ',
                        ],
                },
                {
                    'name': 'ǇƷʝȎȢͺƯхѳɵòëЙАĥӭÑļÿг9ˋ¨£ɍǷĬ\x98Ӻԗ',
                    'version': [
                            -1940791777516845003,
                            -7212938629863425423,
                            -6321601659511486622,
                        ],
                    'about': 'pϑʮƵúЏАҩɄčjЮτHƩӎɭԋʚΌąłƛћʈȫҩ˧\x88ʅ',
                    'description': "ԟΤʭҀȽSαŧҊĠ\xad'^ϧƢdҀԘΎЦͺϲɈκӁ*Ȇԋӷʏ",
                    'authors': [
                            'ŞƫͺĲ¿ɬΞeÑ\u03a2ƠБʃѼNΓȂ\x96ŏˈȲџчäԤґϸѫЊ+',
                            'ùϾäȊõӲ˭ʶ:ҹ·˝ўԀʄͷҴñҤÅӒԉÇÎʮԨΩу`ȧ',
                            'ż Å',
                            'ːӂƅΠIǹ\x8cѴӘƌëǉkʹЪЦԬϻ®ǆǔɻ¢ɀʲʘ@őPA',
                            'ĈԤ˕˩ɚ˞ҥȉ˷ȃӌ\x8eʘȗıȇΒ\x90ҚФԤўƧʒ(ȖɦʡåÙ',
                            'ˢʘñԮuʣť&ƱɎТv\u038dɣϱıʭǋҐBҸҴɈÇĪɺ˚ǐȕ΄',
                            'ŐĥĊçɓɑԛѮŠRǥ\u0382ǘӗ5ʼ:·їѨűӒƝƇ6ʮµүǷӮ',
                            'ӹǂ"ϫ˵\x95ѷěӪƵ»˳sΥƁƷѨЕǍғуǠ˖ԀǹɾҊɆԟǦ',
                            'ɔVǐȍʨʀǄҙȵѼŗNͶɊFĮǬҐɈͷϨħЙΧˇ9ĚҗǦƷ',
                            'ɰыӲ>ќӷɉƛÚԙϲ\u0378ɈʽԣȪΤʧΝǖŴ\x8bxȐɼŽZϚǳɰ',
                        ],
                    'licenses': [
                            'ΥĳƺӾȒʶα\x90ˡ\x7fȢɌϫʣɿҬσ\x98]/ƠϓӦžЃˢԪԖÁ{',
                            'æϤɆÖsÊĚȈȶ˥ȅͺѬoӭŇ˛еƕϋҜǢɖȥǈЦɨƗԮл',
                            'ϒϮʇЪͳηǗʰƆʫsς˞ɀӥġ ĉɌʂȧшơӅԥʅΘήӑɼ',
                            'А˔®ìȃǏɽŰ\x85ΥǎМ\x86ēž_Ѵ\u0383ˈˮӬʌ\u0382ɆԙŁϭΩĴɔ',
                            '҂ɭ҈ХԉѦж!ĵѴπμЯҙƵΌŁϐl&[¾(ҎРύǤǒğ\x84',
                            '¤Ş5ɜǳѩΝĭνżcѦΏ¦ǕŠąñԎƮģġ˭ВҜĮӹëΥν',
                            'ӌˀ\x7fĉW˧:˯ӝΤǋˍНʔЊÑ˷\x98ΓʔΆѶҝМСƴ\xa0ӔËԪ',
                            'ЎͼęϬʘ\x95ÕӻчʏľǮĀҶÒҮÁǏϾʸԐ¥ǖμ7K҈ӷƒͼ',
                            'ƒķсЏʃӺϟͻöûŷÑªƸʌéρΪ£Ɩπ\x81Ͷ˻˘Ԙ˥ԜŌҏ',
                            'ћҳͺœΙЏaϗӋКԊÔπҫϏĀ\x93ΛŎјέǮʪϭФɡжưΝϜ',
                        ],
                },
                {
                    'name': 'ŻҰɋΛӾѯĬĲȱίӼ§ȄÏѬ.ˌԒϕӅʃƝȅѰpҙõ˚ʐʆ',
                    'version': [
                            -3677233719797705641,
                            -4365334815844781685,
                            -3948593247191622164,
                        ],
                    'about': 'ŤǢũʹѱˬêŴȉɎƊQX\x9dũҩΫψʋčѥɮĀƌЇ˱\x89ђԋѷ',
                    'description': 'Ѥ˄ŷɊ>ēӧԄrĮ7ѸƯеȃÞ҃,Ӈ ªɣҝ,ĢɆˡƐê?',
                    'authors': [
                            'Ɂ˹˲ɻԃ¹.ÂХȌҍԂξΧԜƪȳ=\u038bŢͶȰȜ¥ÜÞ˄\x9e˼Ö',
                            'ӨKЫ\x8bͼσǋʴΩŴӋ¯ÄɅѩгˊĢϭ>,ӠѧåӼǑϢӪ\x9cí',
                            'ѷȔϾΓйßƺђǗƗӡԄțΡŤΠƎƪԝOҤƶ¿gšѐˣʸӆǔ',
                            'щHʡÙɿɕόƛƯˢŇūʩԢƐļ¿őϷs\x84ɨӶұ\u038dƫӅǬҭϰ',
                            'ӤîЛȞЈԑԮ}ĥҐ-˒˳ŀΦĵɅȔԕŊЌɞɾȝβ©ȾƠȹƀ',
                            'ʼηȕ1ˈ@ɀŸӕ6Иăҥђ\x8dʔǏĬЮϷԀȈӂё²\x88ɍċͰЎ',
                            'ӻɱɩ˧ɬǯЏʐĕņҾęҋ^ǹΫг\xa0еӁӰƉ·яʕɧ]șԤǼ',
                            'ЧˣʐǱǵ\x86ѬͰѴĂѢÍеŭÛόǳłѵЏ˴ƼŰЧɶʯĆ;ę{',
                            'ԅĺtғ¿ɆȔ˭ưɭȵˆŋˎŦÇȌǽʨхv:ʩ˾ħŖΧ\x8cΎǎ',
                            'NʟҾ1ԊɗѧӾϦԥČŃzΖИƬƟǏҳɧƦŋ\x92@ԋvƂԜ\u038dſ',
                        ],
                    'licenses': [
                            '»Ҫʤ\x9dƅŗʒԍψφȗшũ\u0380¡Кϥǡʊ\x95ҞɰҜΏxüɀȆʨӲ',
                            'Ϗοƙ!\x9d_ψɟƎǆγɔПƥȳĺȳϵͱЭϑ´ːȤҜʝɒûѼŃ',
                            'ĪκͼȔԉȋ\x8bˆΥӻÞCoΈӨȋúːτʸŻļͷŎԛüΪâͰ\x81',
                            'ʼùәχŏǼÆlƶӇɖɶʽȨϸ¨ŸȆ\x9fćӫũÃĉʚѫĜνтƻ',
                            '\x8eϰȿÊҘ҄ѕʣѴÆϧ\u038b҂§¹ʤӝД˃)ԕȆѱƎрѽԏӻŪ˵',
                            'ȠΣlϋĔƄљʪΚūͺӆ¨ʛ§ђʯɖʯƝĨȮĦԄӟʩԡɔ҃Ɓ',
                            'ϦªiмŐнßƔǉϤԄГϳȂɟϟрԜЕɯΞʧŉă|ˮȢbũР',
                        ],
                },
                {
                    'name': '~ĸƍѭΒßшú˪Ċˊ¬Ӡ?˧ѐАȉʹŲ\x85Ўːђ҉ƐяӘҔΌ',
                    'version': [
                            -5163791334604845750,
                            -1598175249150817048,
                            -6791851289320878863,
                        ],
                    'about': 'θʈŶсʐ!ҥɃКӘк˷_ʇѶÌΡҝÃϋȨҲuǍêʠΌǔĎ¿',
                    'description': 'Ń\x92ϖ\x7ftОʷ&ˆūūŮŀѧϜɮǢӪğ8ŸǋѶ\x98ӱŉЧƾέͶ',
                    'authors': [
                            'ǊƥԘͰÝĶǳɰđ¢¢ĸѨҮǌUǏȢңɏƿǻϥŶɻʲȱlƢʰ',
                            'ϋĒѼǷ¤ΖÝѺȔёȘʌǡƽƨȕśʕ²ˏгþғԞҾʩλ˦ɫĹ',
                            'ʹàʙ\u0381ʄdңǹyƆΧǽü]͵ÎMƣ˒ċDIԦ|ʨğƓӦΑҪ',
                            'ԄƛҝѷʋȷŜæń6ԅ˜˂ϔЪѯȺӐyɏм\x89VҬВƕȵµЅʹ',
                            'ΐζĈʈ˗ёЛɐāɂӭ·νїΏ҇҉ǉċϫƻƧʵӋ}',
                            '\u0379ΤөǽŪҷ\\пȒλļЋӧÙΣ¼ҸȯԄϛѠϝϊYсˍŘĉęƉ',
                            'ɡ`ĳ«\x8aΪʛϘВʘɗó°ѓΙҴńҋɨӡǣɗ¹ȠŵҚγ҄ÓͰ',
                            '\x92ʓƊʎӕ{өȷϻ',
                            'ϭCǠȮnĊӠ˜ϔāȬ˵ƐƿŻʽʓtʮʲҫ:ŐҽħҴɦѕċ\u03a2',
                            'Ǜ4İљԞɿЅʜсЎˇɢӏѠʎҒƙˉӆЀʩƵǼΙ&ҪͰ5ʜӕ',
                        ],
                    'licenses': [
                            '\x89ɜͽϱʩӒʤ\x89ˏӧĘЇҰļǖ',
                            'j˧Ѳ\x94ǦeԮƘ҃é\x9fԪӬÊЅʹіϑwίԭҚє½ΐƱЦÓŠȠ',
                            'əӐðĀΐҋǚӟ,%Σ\xadȼOѶýɻșǺԓ1ƔĂӬȂȵєΨ\x94Ѝ',
                            'ƘύӢӤ҇ήƺĵϒˎʏɗˮǆ˖ϺʠŕЀÿϣӠVÓӼG¢Ӓºƾ',
                            '¬˙ʜoόɛkǥØz΅˩˺Ŕ˭ˎӓΉȡÝ˝ҩ0С·ȶȮԝʹª',
                            'ɚѕƵòҬӐҐˤΪɁѴ\x913ϑҸԄǩԞτƜaӿŋ˴љҗІȜgȡ',
                            'ŊηĭƆvǬĆ˞5а7яμӐŐƬ²{ǀη҈˝Ǯũ&΄ĹӭϘƂ',
                        ],
                },
                {
                    'name': 'ŘҴԬøŷƷ\u0380ŢŲgʁϹЕȡċαӂҬуӸŜƨ΅ôΊғπ˻ϾӒ',
                    'version': [
                            -3681305985358694563,
                            -8616089017301948508,
                            -1574641558972714252,
                        ],
                    'about': 'ųǆͱũŸʡȦЩĸРŇ=ǅδÝпÉ˭ЛϑӍǀϓʠ\x95ĿКřW(',
                    'description': 'ļˌKҏåʛ΄ĮҞƊʧѬԂɬqμѯǺѐӟӻВԧTǉ΄ѭÎ"\x9f',
                    'authors': [
                            'ҽτɋ¾ſ0ΗԪИΈΦ\u0381ћ˘ғΆŋĭȄьγсˋϗҞȧŦиmЂ',
                            'ʪ˭сȋўÕȀŴȓěϑҍ\xadΠӕėͳӺɮǋǥʚԦ¹Іɲрʘцƃ',
                            'ӮĳNԩȝΠʇˈɽÂĚóźǢʠԭŲΰ˽ɄЋЂԍΉϯ\x8aɨ\x9fѳ¹',
                            'ǗωѪʳäϯ˯ԝóĝ˵ŹĈƭÚ˜ҟˮƻɶзѸ˽ԜȝΔˬƍІА',
                            'ĲΌțϫʠԇԬ´ѴӒŞОǧпǻϹΫļҚ³ȷǲ͵Ь:Ϝѐȥ˲И',
                            'ÁˎπʳȱʘϘǳÏȉеɵӽҍчϔˈȸыκӟ1\x89ƂÌȣˀ ǤƷ',
                            'PćIσԙtʫàѣ\x90ʷˬɤĺΣƾ˥Ψ˯ɮˏҮƿѠѳÖεȫӘú',
                            'òӜȻ\x82ҬǑѦǓgςΚԀЏҲυːϰƝŝѨϡŝƚyȍƊӼӷÃC',
                            'ίȉ˦ƎθѼǝӽҜϺӛ\x95ύ˯ӃjÑûЮˤэǞ.ёΪϸȕ?ɻÑ',
                            'ϚΠϡˇ0ҷʇɩѿɒӡлǊΈΌťӝѷȫŉ˱Å\x99ЦɞѢϊϚúè',
                        ],
                    'licenses': [
                            'Úưō',
                            '7ǨǅŔɂ¦ȞȤбdҔm\x97ϰы-ÃMΕ˰ўбɶǷҝҼŚĚƏҴ',
                            '˥ϬȆΜӶȗзЃɤԩĚ?ƘE§ǏЙuÓ\x99ȗЪŮƚпˍƳҟʪΚ',
                            'ƑʽѭƬˎӷƃı΄£ǮӘɉ\x8cԎʳĲǘͰZӐʐÿȌзǮ҈<ɉӫ',
                            '^ӣ-эʌѡҁԧæ˟ԊԨЉÿέ΅ȹиƭħɑŋʠĐʮǵʌΥЃʡ',
                            'ϑĴɘΎĥǔư҃ƇˋȍőѬȗȍΑͰʿтʱɄˊě˩юŦ˃ʉǹǫ',
                            '˯¹ſӎ¾ÝƬέɵʿ',
                            'Ñ˜ЩϗǧʰÊȢŉȷɝǟ/˵ϩý˨ƹҴϽϲǁҿоĻ©ɚǣѤď',
                        ],
                },
                {
                    'name': 'ΰ\x85=%ԭˁѶţɈқž>ʛЩ˲νąΔΖ˃ήԣͶȧϥ//υɊԕ',
                    'version': [
                            -6824889593633673239,
                            -3858452465791767362,
                            -3922120870529829435,
                        ],
                    'about': '\x9fƯUҊȁџºĭӘƹĩƢʩǤͿЃǻ\xa0˅;ΈҠ͵ü\x85HϵǴ4Ψ',
                    'description': 'ʋƦӕѤ˖ҝÛ\x8dʤҾĕ\x9dДЄ_ŶƝâ҄QƇɶƥƊÌĎÃμ¤n',
                    'authors': [
                            'ћψʞưεХϡҢgƻ\x81ŖˏVʞÿѸƱƉƄŒʅčӮʪԫƅԋĵȆ',
                            'ɁϏ˱ʑȻӣ˧ɴώώϿȋyşәǲȍĺɡơ\x94ĒɗŇήеԣŦɽҺ',
                            'ӌĲŽӟȄſԖώȇƾċƽ΅Ûǚ}δ˲ϨϕЗ~˪ͱɜʆдϳϢ˔',
                            'ǟȱĤêЂʯ˗ԚΧԣҧÜӐʸΚғίӶθ\x81Ǿ.ˤʮзȭèςʹŁ',
                            "ǌAԍŝԕѶ'Ԁё¼B˕ȲӴəˏǰӁΆԔҐӽЌȮ^ΪӱӾʢĞ",
                            'ҬĥŘưÖԊ˝Ȃ˂\x80gӏϺѸӠӿәȳƢʗ\xa0ԞĽӎѲͲ;\x9fȼ2',
                            '×ͶǗÍʮ\x82ǺćҤ˪А\u0383ƯņȡЏʙѲԓыҐЧ¾ǱѮÆĐƲč<',
                            'Ѩόɴˮñǧʋӽ˾ˉγ3ЄЫhѠ˴ƆŶԃȂ˽ǸќɚĚ˕ӏʗʇ',
                            'ǎŠԒ˖ôΡм\x81ԈƪʀӑͶˬԖ¾ɵʨѾ:Ō0ʹΖƤˢԡњű\\',
                            'žЧћőӸѺǗīI?ėѨȮкĮŦǃfŅjг¨ЃèҋѸCʢƎÍ',
                        ],
                    'licenses': [
                            '}Ҙʍ\x92ʈɿŦʵùƞӥљĨΓїÜӑјĊɿ\x9aɑlˑ˰ͼїǭɉ\x98',
                            "RӉˠӹ'ӀȔơϏҨɁѴҤɼѐȰ\x93ұҧͿȂϒ˫ӦŮ\x86˭Ӆо˟",
                            'ОʭàΔùʢоӝͽˎɗӼãӍȿҞΩƤǪʵȾĞΏϼǡƚ,ҼƽȐ',
                            '\xad\x8eÓȆŚͶ\x8fñ£\x89Ρǎ҉ˋfͽϝʏĴƐԗԡŎΝϳШƆӒÍЅ',
                            'ϨϹΙÒӘ"҄ёǝÏΨΌǹƠƑӺ\xadϜÈӂɜ>пɧʬэͰˮ¼ϐ',
                            'ҦӘðȭЃϕƉѯƮͲʠ͵tƢʚƜԤқɻʳϚɲqΘ¸ƾӃϙƸЀ',
                            '9ƙǫŽIƔӏȂϕˣӾƇ.ƵȅЯÎӝÍǉӫŇ[ȷϗг˅ԔЭӥ',
                            '÷˞ȥËɤʾǪ\x9cž+ӭɏʎҕЦžǶҺͲɒїã˱ҼƚМXȏoȷ',
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
                    'name': '©ƦӒ',
                    'version': [
                            -4468425374303760646,
                            -6645723140420406657,
                            -8310323026492830430,
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
