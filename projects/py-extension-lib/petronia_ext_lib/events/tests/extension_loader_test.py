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
            'name': 'ӏõȵɮťʖƲʬƠ˸ͰȼОǪюǵÐѤ\x8c=ȅʧʃœÏϘƔԄѣƎ',
            'minimum_version': [
                -417604884010304865,
                -1164517890724463040,
                -3540405192911332737,
            ],
            'below_version': [
                -2046700186907859663,
                -7099581892717894511,
                -5703130901615511758,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ƨŝԂ',

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
            '$': 'ȱҭӚʞɉɁϑĞԙчôУ?оÍưʘ\x9cǉ҂ǠЖɠíτaûйȠƻ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -8293790220362534738,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 881852.3488729183,
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
            '$': '20220523:220037.899563:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ǫӡ\x86ťԘҭĒ˽нΤȾԑԬϢ~ϻǥȺћӷƒvāБɀԢˋƿεŏ',
                'ĻE\x85ϑĩ§ÐȵχΣҤų\x8eǧӥѧȆ+҆҇ȉÑѢŌ\x97ѡʡҟЂѸ',
                'ǘžpѽʀё͵ÃHɧӼԄʑұĂȟȫɁʹĴɷæȭ\u038dÑ]ɒΣЍĢ',
                'ƔȤıʯμ΄ƞ+Ԟ×ǿϾǜǿXƩЈǛō\x91Ƿ\x8eȰΊҾÛГҮ˘n',
                '\x90Ә#ј˭ϣʨƀпiΒǾØʥȉƵJШԩΪȮ\u03a2ǽќĒYƀΥЮӀ',
                'ͱɓѕџȍʣпɗў?ӪΆĬˠÊϑϵ\xadɬӋƒǷ Õȏɜзɵ´Ą',
                'TҥʲŝιɢôӌȉӣƢõƙʕҸşƗӢӊʷΕзʙԗōŠ§:Ӆª',
                'Ʌҿʽ4ąş϶ŹɂɷȝӲwϗѮѐҎƉĶҺðcFǮ\x83оƮƸæ҇',
                'ӑɝʠђ\u0378хŏ^ǛΩŪÛßӾūͽʪrɁƋɁɯгÉϤƺѣӾԃӟ',
                'ϹϺ\x8eӛ³ʹǂƸ\x8fԓԢξ˰ǮćК˶¾ʴȲ˞˷зǵǃȇК?Ӷƻ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -6331860141113930912,
                -5388439601252654711,
                -1871379845020028199,
                2545557504220445247,
                -6471843591057079155,
                3915009143616528287,
                -3909819813701001015,
                -937570238091689769,
                -7536722985467079065,
                -1624307258472532626,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                619817.8752930023,
                415821.2200396595,
                786564.9381155147,
                593660.0324088164,
                97041.8348292853,
                81113.71129439824,
                303595.0510053707,
                -72212.46683102647,
                902626.7768696995,
                291378.200101856,
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
                False,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20220523:220037.904641:+0000',
                '20220523:220037.904733:+0000',
                '20220523:220037.904822:+0000',
                '20220523:220037.904910:+0000',
                '20220523:220037.904998:+0000',
                '20220523:220037.905085:+0000',
                '20220523:220037.905173:+0000',
                '20220523:220037.905260:+0000',
                '20220523:220037.905347:+0000',
                '20220523:220037.905434:+0000',
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
            'name': 'ͽʘ˪ҍԜˆDǂҍɳԄ˛˛ɉɗ¿ČĞpģEɄɓ΄ɠ)ҹɵņϻ',
            'value': {
                '^': 'int_list',
                '$': [
                    -5499307986959128006,
                    -477748850928793930,
                    3089676125431470363,
                    6477028016920082178,
                    -4053716243605600248,
                    -6713961048480138418,
                    -7064091893980589011,
                    -8690902639990910409,
                    -5502570033830298572,
                    -7678900054547485021,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ϡ',

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
            'catalog': 'ȨҳѴҗÙʐԂþϻȔѵ\x9eθȭεĚŪğz\x82҂ҤƈŰӨȜӇϦȦԣ',
            'message': 'ʿĴӊÁĜҐ´ξͻJõϠҤǋлӑɳ҂ЍɐǞԅԇϑ+ӌЗȗΜԔ',
            'arguments': [
                {
                    'name': 'ЈʹÉĬѧǟΝӝпyџҐŪŅμǓɴҴˍ¯ϸҬʬ˔¯ѭǙ˯ӟ1',
                    'value': {
                            '^': 'int',
                            '$': 618963644736913960,
                        },
                },
                {
                    'name': 'ς¶QсJéѱжΌӮȨʳãķ\x8düNŀƒŔ˥ʘ\x87ңȧȾɃȅэά',
                    'value': {
                            '^': 'int',
                            '$': -2016497508305673681,
                        },
                },
                {
                    'name': 'ȦˮӣϻӠǫȑњЫOǼȩІ\x85Ɣ\x84҅Țćæ<ϼȱƹćǀӋXƒť',
                    'value': {
                            '^': 'float',
                            '$': 424581.2641820371,
                        },
                },
                {
                    'name': '¶Ζèţǡ®ԓž\u038b*ȃϹaӟɦ˭ƄȕұƢ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ΌˀΜΒɥſǃѬÜ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ƕЩЬЛaѼЊͶʝҝÍѸĝЭ',
                    'value': {
                            '^': 'float',
                            '$': 150278.81350603348,
                        },
                },
                {
                    'name': 'ɆR;Ѻϕʌʸ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        249201.6267617063,
                                        84069.03983755401,
                                        962447.5378104886,
                                        686789.6233739089,
                                        231788.40311321692,
                                        953608.4095159993,
                                        55712.349555137334,
                                        593982.8073712626,
                                        183171.7522519771,
                                        988939.4388851693,
                                    ],
                        },
                },
                {
                    'name': 'ɿΕťΜȏιүŢǄԧÆєӮϻҲhζЇҠǅėѸ¶ώyɎұλâè',
                    'value': {
                            '^': 'int',
                            '$': 8591320983245020116,
                        },
                },
                {
                    'name': 'łþɲԏЦґ5ȌǗʐ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220523:220037.895184:+0000',
                        },
                },
                {
                    'name': 'Цϗ1ƝǋǄΰɬЀ\x89Ȗp˽ƮÂĺ˰ҐӶƣƹ®ɽҔШϊǖËNΩ',
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
                                        True,
                                        False,
                                        True,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': '~đ',

            'message': 'V',

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
            'identifier': 'ŨӚʰŸĘͳϵ¿ϑӅѪʋҗ&ŭŘǭтωɢЎˡ˶ҭʞ\x9eҌЄcƿ',
            'categories': [
                'access-restriction',
                'configuration',
                'network',
                'os',
                'internal',
                'file',
                'internal',
                'configuration',
                'network',
                'file',
            ],
            'source': 'ˢˁҌӯnŏŹЅϕŎØȐє\x93ƠǭӾţҌɺ¡ɯƳǰǏ$ļԘļѭ',
            'messages': [
                {
                    'catalog': 'ŖϽǶ §ÙƝ˻ǕȒ\x93ԏ-ƀǡЛȘË1ūŝøƧjłşç*ñ$',
                    'message': 'ШřCτЭǹГ¶Çʘͺъ\xadȎGҧķӵʣOªĪƏɓƝɿзϚɎϴ',
                    'arguments': [
                            {
                                        'name': '¤ɵƥǱ\x89ĥљƿϛӰϲćѣƇѕЪϤȓȸ!ϡϸΒӵƜлVƽƽĈ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4843965549781500618,
                                                                            3076459678545452510,
                                                                            -444179416418130658,
                                                                            -107629491705347923,
                                                                            -7519978108937822987,
                                                                            8893014767678322667,
                                                                            -4652555853359102241,
                                                                            -3522251667256073162,
                                                                            8732241132743118533,
                                                                            6644409785451858335,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '϶˰ʦ˃ηÃӀϔǲǑ[ϐЌȧªɔВČÂΕ˕',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6968556188731065824,
                                                                            -7564231690064655227,
                                                                            -3523311959632785436,
                                                                            854297337320597928,
                                                                            984197037262030975,
                                                                            -837598464100759803,
                                                                            -1035274091473782813,
                                                                            8935739345636683578,
                                                                            3000236489770543460,
                                                                            4985820085574964530,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȰǖͶoӐǬŌҶʢƍØǐĎUӝ4ϊкǄ\u0382ɪĂΫƼ˟ÏǿЁȝЯ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 790.3815087705734,
                                                    },
                                    },
                            {
                                        'name': 'Κ6Ļȉ˫ѾшҭɆŻäÔ҄ɎԜƵɃӹ҄ͻʄOǁȺɸ¨ϋȡŌ5',
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
                                        'name': '9*0\u0379¤ў\x96ӎϯЭǥЄŮ\u0383=Ѐ«\u038d',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҷƱзвϿȉҬǊ¯ЇȚӵԣ±˝<EɠƏǖʤҺԙ@áƨʟϑxѽ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĒŴ¬ϝҏԑӰ³ÍҕʭʣԠɊŝԘȵԥǨƳԡŴµƦËQʂȆ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 860361.0355239408,
                                                    },
                                    },
                            {
                                        'name': 'УԒ\x8dž[ӂaȪ˕Ϗ9ӯǰ˪B·ίɸАqɊΖӞҥƴӍΰΈйӧ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˱Ѵɓӑӗйǿ҈ɿú˼ǏҰԠŴӐ¶ҕʌɄѻǇ˖ϓȃĿƃӥ|²',
                                                                            'эüԪĵϥԐҭ/ΊήŨӨǬ\x86<ͲĽÇӵԌЂ«lȱÍǡĀγƢу',
                                                                            'ŧƗȗѥddɳMǀć×ǻςΐƝӇ|ǂδΚɩӍŃóI\x8fЁ¼[ā',
                                                                            'ʡǲĄYʚ˴˟ʱǾʁĿԋ˻ГĖ1ԢĭМ®ȻɆȕžɞɳ˘ĭćŊ',
                                                                            "ǆǔ˙ˊ!ҎϠćĲƒ}ɻƍˆȒέ'хXҺƓʗӃǘƚВзË\x90\x9e",
                                                                            'ʿ¸ƠèɥiͲδŻϋʻӴҞ˫еwӇ˾İïҙԔ?íĒĒϸþŋҖ',
                                                                            'ԙÊԦ˶ĉȵ\xadѲʎ©ЀʆÁ\x8aԖˢόȰԥʧΟҳРĪwњŊӠcǂ',
                                                                            '\u038bǢɈð\x8cĥдΣϰEK&Êµ¼ǐѓϱȈ҈ÿώҧĲ0ȉԢȕѧЇ',
                                                                            'ȺʣΏ×ɣΑȦȔŋϵЅAʘ\x88ˀŴΜÜjΩąԨҿƪҳòϙƖ7\x87',
                                                                            'ƂдєђʍӸхѬʭ\u03a2ъӾυȼãӒŪʵЬɵCɬdČҍϻӝ\x95Ƨǉ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'iӘˣǚҫĊɁӅŁƿϑԣà\u0380ɟʐӦǼʥƑιƄκçǃƾɭƻ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3625149023958571129,
                                                    },
                                    },
                            {
                                        'name': 'ϓԦiŜBѮӁƒΑĺĻҼ\x93šԦЈϧùј',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220037.888358:+0000',
                                                                            '20220523:220037.888443:+0000',
                                                                            '20220523:220037.888526:+0000',
                                                                            '20220523:220037.888607:+0000',
                                                                            '20220523:220037.888687:+0000',
                                                                            '20220523:220037.888767:+0000',
                                                                            '20220523:220037.888847:+0000',
                                                                            '20220523:220037.888926:+0000',
                                                                            '20220523:220037.889006:+0000',
                                                                            '20220523:220037.889085:+0000',
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

            'identifier': 'ĄƻԔǫä',

            'categories': [
                'network',
            ],

            'messages': [
                {
                    'catalog': 'ǦǊ',
                    'message': 'Њ',
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
            'name': 'ӕԟɨǙ>˫\x81˳ǾįϷžƭζ˥ȏЎӭϥЂҥ¼\x82ϢˁҪЎʨ\x8d;',
            'error': {
                'identifier': 'ÜɑѣӫωГұÈбͳ͵ǷʉҨʤɴĖȄҌθǙВĲԛ˄әǟӆėƌ',
                'categories': [
                    'access-restriction',
                    'internal',
                    'invalid-user-action',
                    'internal',
                    'network',
                    'file',
                    'access-restriction',
                    'os',
                ],
                'source': 'Ͽ\x88͵Șд±оȉɸĖŠʭһęӯ\x94ĸӅұȈςrзЊǯÅʖÙӪʎ',
                'messages': [
                    {
                            'catalog': 'Ӳ§КύɠˢžэNBϷИЦԘ\x8eʓΤƩϫϑ[mίȶӛ%ώʏѣ\x95',
                            'message': 'ČɐЍʵϧƤȡȊǙiŝыƩƸǠͿTӓʗДʣēӌʻӜˎɇĵ\x86Ă',
                            'arguments': [
                                        {
                                                        'name': '͵Ӳǖғñ҅Ũ\x9fħ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϣɀ\x9eсSǞЌƐԪˋҟӇÞȍ6źlӲϿӳĸʢɩőɂԩȝ˥¸ӏ',
                                                                        },
                                                    },
                                        {
                                                        'name': '¤ͽҲҤӤΝΟʶ\u03a2ȸʞÑˢ\x7fƻъ8ΩԘϓȩěƒ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -8904.35867602835,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɫєԠΡǛ\x89¶ӽȸȋțāҍ·ʣǥˀҸϘЁвɞɶËσϡԧlğŏ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220037.835529:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȃԀʥäӿӮŏюʺȌӺϮпϷЧɰӈTӪΘ\x92˝Ƶ˳ńʃӻˠѐԩ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 294621.7254385005,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŕ҅άӣĝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'гҲĺˏ×ұͷͽ\x84ȏʛɶœРȖϛҎзŮčƭѪŠdǓƜgҎȵȽ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3583396298261776953,
                                                                        },
                                                    },
                                        {
                                                        'name': 'η¡ќ˞ŅáљȌԤȏϡćҴÃ3ϧ[ɐ\u038bˤǩѬԥφŚ˂дĬӦр',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 810998.3710742759,
                                                                        },
                                                    },
                                        {
                                                        'name': 'iʐǆîϮд,έþ2ҫ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Кƕəɉǅɕ\x93ƌ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '¶ǽSЁȁҌȂҞqрΙļěψʥ`ԟȽõДĎLʔûʾ˭TҐwˀ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȇvєϟ0ΦȭԚѓʦʆԜϗєÉҙκũЯÈѠȡbғǥѺˌЭ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ь\x8břʃɁ˙Ĥ˽ʃ˧HɗŜǼΩӗʵΦԁӐȉDțҖ-ОҶƓĬ˨',
                            'message': 'ԚӎǨώ\x9dũͱɃȿұǿЅҮѓɬԥæŇ¼ɻȮ\x82ș{ȳоǍȬϵÊ',
                            'arguments': [
                                        {
                                                        'name': 'ˆmɒÍȰŊ˲*Ƴ˔ӜÖ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŀƿ1ϿʖиſBœˀƅϙ#ҙòĞԬnɵɋ\x8dƧůƉ˙ΖǓϙĔ˞',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'wǊ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϵцвȌЏӻϺĊT¦ľ¢ǀÏÅ÷ȪȊ\x80ȃѦ-8Ťϊ˥ĦʂχԘ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 634007.1589744735,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʈǙĂԞȻȰğӫ˭úŇԘԎˑǠĎāԗȺѯĉ-ǬȋҦρʉӒϬ˻',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˹¿',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŀźӥòяͻϯӳàϺѺƱƢĽŖԂAnҧαɵßҹ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220037.841851:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǻЊҝĄ϶Іʷ˅˅ϔõ҃}ɩԉɰ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¶Ɍʸɏŋƴ\x8bǡԔɟɛЅЙ¬Ԕˌԛ\u038dƤʪҭӉҊ˸\u03a2ҌȦЮʖˆ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7688270124489405774,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӀΧτá£ϪɿЀГœӽМ\x82ĔϨԩȵԔBȱ˛ϠƭĕɸϩΠʢ҆Ό',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԍєˆε\u0379ʩ3Ǝѷ\x9bȌDȩơUɟŮϲοʳǭƜϞӝԇʚŽ˨ѧԓ',
                            'message': '҇ơªϨԑźжʔ;ÇСĢzЅ\x92ģөi\u0378ʼϵǻŖӣξҞӱӷ;˫',
                            'arguments': [
                                        {
                                                        'name': 'ѯËӊΦǄϪΘêР',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȪΪiiуȎѻ˵ɱæȫ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7998734319042491771,
                                                                        },
                                                    },
                                        {
                                                        'name': '҅Vϧi×Ċ˓ӁƻӶԜǱҳƈǶƲʔȵҥӍѧǧϨӬˎɆɩǠȮϽ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '+"ƹxǱŠЃϊʇіǟBß˨ż/ЖªĔƤ˟ӞӪǚŋľ¹Čßȝ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1443430471651244650,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԝӥ\xa0ǡП\\ԗϳȳʓÎȾϿӫ\x9cȪ\x8eΧɱјǟƷ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ұàζр4ˣáӾʺȝŕЖ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'нɆϣѪѰԀв\x8fɭЖʍ8ϣĂ¯ºӲɈѾǎ\x8aEнˉȕ˚яóϷ\x8e',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӊ×ҠЋkq˱Ǯђ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '?ӼΔӂêìƌʵͶˇ˪ϥӡʀʇȢÍѴǊǌԉƕĈɼФÁϬϝҏȯ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3184945873422855854,
                                                                        },
                                                    },
                                        {
                                                        'name': '|YæÑӗ҂ų«¼\x9cXЗeы',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƚϕůӃŻƉηʞӴӛӟʷ?Ȅ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɷ˻ǫоЄbÞҸ«ѩȰΕΚȡ;Nϰ.λŰӗſ\x92ƈĠ\u0380҂Ӣчv',
                            'message': 'ƣȑĭ,ΕΙӀӠҭԆҺҽѧǣĨčǬUΣӌ~ϨʋɌďȅҪƞ¦Ĝ',
                            'arguments': [
                                        {
                                                        'name': 'ȥ\x9dԐÙ˻ќn҇ƀӴόĵѺЅԓíʄ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȼϡdөԫɺԩӦ_,ʋdмƩѮ˽ġӡfӷɹˡ¼öɇЫϻҰҌѳ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŚȐµŤIҦӦҐǲŁč˹ČþȼϰԝŊ:ʗŝţȷюɷëҏԮůЖ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Φ˅ԎñȤͱϠ\x9eŏӡыƍɖӗӗιҒҔɩɛʾqʚзŦɌȔǴƤʈ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЃȑϙʘǒLВ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ťԛɧѥƢNԮԛҨŔ®ȴɱȄјǿѷƀȬɇɲєћ1Гϔʿʑ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˘©ӊӚǋĢΠÎˬƷћǶůǬϻŉùɻсȣңϛÍĉ®ԀǪԊѹȧ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΒҤɰʗñ¨éX˾ІτǋÏǧƥӏÑ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҶяôԔÎɾɪ$ǆŕÃȵĖшӨ˸¥˓ĶΣĳɄ˳ˏԦӛůϿѭȫ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x94ЅΜĶ¶ÌȔɱ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϫƛІһʫƙ˺ѩ҅ќєǨö˕ǽΕ(ѮȌ\x7fϠЧϾӅȆ\x7fμǈĻό',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ũ˪\x7f ȇőӥðʄłǁVѡńŠǅȐǢηĝȞпŅүûPĐJŭ҇',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 695870.0632708505,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'қ\x80өѬ-ȐŇȂªȷ}ȝӁԟŎ\x80ǃȳɫŪǶàȷÚʌÙͿÃӵñ',
                            'message': 'Ȱ(ʗѡƛʐ·ӷ҉ӺǾɁςN0ŐʖȆΆѬǷ´1ʂαϑŢƼАҟ',
                            'arguments': [
                                        {
                                                        'name': 'ÿĖӊɪԀǤƈE',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220037.853324:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˊȖч\u038dŜӬȶӨ\x87ʀ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӅѤóƻɄƲa|',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3163394505188470574,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ÓǹɉԡԖˠΏЮΌȘŶƙȈàӥǢǈЯ|9ȓΗGº҆ëɉэʺӿ',
                            'message': 'Ɉ҇уъƴҳԘК\xa0υmјЎ\x95ƔƔȌɠƳΞ\x9aөåɁι˫ǓĕơƠ',
                            'arguments': [
                                        {
                                                        'name': 'ûϞϕșӤʮĳ\x8aɠǎтRåԒ(ŏӏ$ºûԑ¸Л',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 705769.0150024247,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʰƄˏԟhrħƝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɇǻʏ\x9cŋĈфѪʳʰӥƜɠӞϝәĮɣŇʔȵѶӅÂ÷śŐǠƎϺ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "¾ƪҫ˚мʵȮ'ʛδвǕϲϸƩҳԛ",
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĝ ΛԚОҙŇǪŭKЉAˤР;Ő˘ѬɑıЪϧʝaϋ˯мǲÖï',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220037.856680:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǤʊůÌŝԡ\x83˯ģ΄ǶŴǻԏì,Àśϝ!ԭѹđЙ¤Ыҫˋ˕ѳ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƈļфNZϚ\x89ΰӊҼ҇ƵѼőхҚȝ1',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӅɈ\x9c\x9bҊϤΔͻ˚ˌ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 161413.41303119157,
                                                                        },
                                                    },
                                        {
                                                        'name': 'АҸѮҋϢσӲɑƠΡϒȩİäԥΌȾ¶àʍēΡ҂ҒÌȊϮpҕŀ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӡαθʡ;ʹƟ˾ʈɌ1ѹƿЉƎϊˡˮΔʎ3˫ȲчˍɣǘƮ$ϖ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΆӮkȶǃĈҀĵɠϖĚÏ\x8cȞϜћēξʭšҳхЂȦӷÈȱϡ˦\x83',
                            'message': 'ƉφѫЪŹŰρϹϟɤ°ǥǲzӶQΛMʱĪӆлȤΧȸ\x9cғʔ6\x83',
                            'arguments': [
                                        {
                                                        'name': 'ԕäªǼʨ˩¿ΓXϨɾʢ¢Ѵ<',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ōʔ΄Ϙϻύȥϛӛ\u0380\u038d\x99Ҭϻ¦Ƶɺ\x84ƸНˢәȉȦҎϘˡʁűɓ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҿʣsşʠУɋҹчϕҍҗϞǪěǔʹүӜϱŐĸǨˊɴҰ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 422028.1580230533,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȃàȴԥĨ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѯƕƢˮĊƅĳ5ȅǰ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǊŪ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˯±¾ԜǶiǃѡÌӃσĀ\x85ŭ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 749516.3975557565,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Βϵ˽',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 18989.830295776017,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӎґǱjҬόǾ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9dӼŹӶѨȀҼǓǐɧňů҈јāĐɂӖӋ˒ʘÏ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŋҞɓΙǂӯӏȪӍTɦŶļѲԅPԟʞüɶĻ\x9e[',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҭrĆќǰɭqӳҊӆӤ҉Θǡиɏ\xadãӢϚʘʉϕơԢѓ҅¥Ԍ§',
                            'message': 'ħǸmȊΫǒǀĉӲƞĥŨѨзˏĳÖѻġдҾ\x93ˠǂҁϸʋӌӲР',
                            'arguments': [
                                        {
                                                        'name': 'ÉыŲʞąɻȼѣȩǷƎĢͲʣŲЈÌȿɧȉ}ùӅźӀΩƆ\xad@Ԓ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "ҧ'Ǟȃɣ\x87Ŏ҃ўͶѽǥӮ˸ưmЬǗԅʵɷɥӼːȍԤԀԩзʚ",
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԮÈȬn҂Øv҂ǙӓƙƼԉςʥɗ*ǅƈː²ŻӐǫԭΎ©ιȽl',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϼɛůӇϺԉΫȫĳϘа¶ȁ҄ĔϳʎӒԁĞ\x8aō˽Ӿͷǅԋ;\x8aϐ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɼɶ\x87ľӊǴĚӣǲfʽǦȜԛĄȔ]ȸłԙæЯӰÆԎ\u038dƼҰɰҡ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǀŭҸêϥʹюµÒҭɉǮ3ҍƜþŉƭĨԕǪκʄıԟð\u038dGΒӰ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'īŷȺʳфɍҍñDɲʮÞωѸƅYͲӕ±ӹʧʽŘ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҟьҬɎҖDӣřӡѾǯŇаȕ\x89ćǅŽíTҹłɇɍ;ϞӮѭČŌ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͱƛɡfώƗљчԈñҖȴΰ˩Ġƞэ˽Ī:ԣҧɠŚȣÌBʴ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǋӇδɚˮ>Мſҳϖʡ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ό>',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԣӧBĲрӓԖȲǂӓǋɪŰͺ\u0379Œ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 222046.75289010972,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӤČ\x80\x8bӁ¡ϻ#ɈɅáǅǟWǺǦҨхѨўˉǢӣҀӮϳƳ',
                            'message': 'ȣϨȼӉ˲ԔĞЋfǧkϯұæ~=ƋЯ©ȶӖϏɐҋŌ˕Ӑ΅Ԫ\x96',
                            'arguments': [
                                        {
                                                        'name': 'ÙȅʶƬΛϰȇ[=',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5821579087046305015,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɟ\x90\u03a2ʴӴѭˈӍʍĕƋÂ$˽нӑαȴƑœɤˤҒҌɖƙʸʰ\x86ʔ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 853212.9965478922,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӨΐŁҍȫéКĒӱĒκ\x81ʼȱԥΏƿҧ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΎȨĦѕI',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҊͺЇ\u0383Ŋľǘʯ\x9aǂΑҤƔƘĳs~ЯŲũӡΦҙ\u03a2Ӻű$ǮӖϏ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƙƱ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҚķуҔͽԒȀ±ϰͶǩ\x98К tƔ[łȿŪ˻Ԋң=˱Ŝ˘ñƏЌ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɃūɝʩͿӒʥ1Νҙĵ҄ϴ\x9a\x8fʠ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 547157.4453372952,
                                                                        },
                                                    },
                                        {
                                                        'name': 'җ7Ň\x90Ď\x91Ӣȧ+ÄϞϼКfȒɢϠtǛǳͷˍΎƹ7ˏΪҏӡҎ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĔΌ˰\x81',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '"ȇțхԞΗʽŸʧȲʢʛγ˖ơДѪƓ\u03a2ĀȪ˥ςҮӥ',
                            'message': 'ĬШƗȗ\x9fʡӆԊͼOˉʛË$ҞƟîΨQѕа˥ʦҙˉҗʠʉ©Ԅ',
                            'arguments': [
                                        {
                                                        'name': 'ʽ\x90ΣЪƜҗȺɫҷуvǀSÛ˫ƪ5ҭĶ\x9eїĤѥ[˖ПϸSӸƇ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԅƮħЈɆȒ3όųЯɢґÌàΛЇɢłİ˗ũˏłUҠē\x7fɍΞҮ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȗ¤ξРʹҝΨËƻěȸȯǑЍëñʻ2',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 214469.83287573163,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԗӆϘǉϫĎ\x7fĳåϵй/£ēȨȗфѽŬÖ¸Нʋ˥aӸЧΤ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "¦љӿaҊΉ'ӍɞʼѧȁԮϪǥӄϢϺŖƠÙÁƙōƧPūˡǉˬ",
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӛĪňûȢʠε¬ЛȂΕѾγȄȲƛƓƔɅǇϥņο\x8fӔϼϱǻɔˢ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҧľ˦έ¶ǃѷÝςЙщͳƍπĮ҇Α\x82ϚƹƐԍѧΟźń˚čȠƎ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȇ\x9d»ʑÛ\x87іίͷĞH[ԥрƞΓōϒļfѾ\x8aɱ\u0383ȡӵҙ¹ƉУ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŇɴΕ8ӠƸӓ˭[˾Əʑyʥɔſ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӤнЀʊǓԐɹъơȌt˧Ԡ\x8cԞԦŎ\x97Ѭ¶Ҩ˖ԣrф(ȞȚʮɟ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǔ\u03a2ԤΆźІ#ЇˎƤԪńΪ˟ҕˈЋ˕Oӵ²ƴ\u0382\u0381ąМ˪ԙƾϨ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1518572283969170884,
                                                                        },
                                                    },
                                        {
                                                        'name': '˶ʪѺˣͱhǔȗÔ\x81\x8bÖǙůÂőMÀ4Ѿ~Ҷ',
                                                        'value': {
                                                                            '^': 'datetime_list',
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

            'name': 'Ĕʧä',

            'error': {
                'identifier': 'ϰłĤϏp',
                'categories': [
                    'network',
                ],
                'messages': [
                    {
                            'catalog': 'Ȟ\\',
                            'message': 'ҕ',
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
            'name': 'Ϙȏ\x93Э\x81ρдŖ\x90ΞɞȿıĶNƶť˰\x88˹ҪӖçèΨƪɑԏӁϭ',
            'version': [
                -8663661713088526999,
                -6196368153200521363,
                -1015614871778565529,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': ']Ǎˊ',

            'version': [
                -6884761112013378757,
                -8453763294471285312,
                -600497847256398588,
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
            'event_id': 'ӫЬҿ҃ͱ-ӫƯџɂæ¼ȝɼ³\x9d\x8eşuҮ°ǝƄƹѮ˜ƃ\x86Ҋʶ',
            'target_id': 'FĲшÇûȿϖʎƒɼ˩ˇçсΤͼǁҸǗӛѷӐȞ˯чҶî\x87Ԗι',
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
                    'event_id': 'Ǉ\x89҅ϱζа|ȗǿϊˆģ¶ƯƁǭŔͰ˒РīʗɷӸƶДɋ*ҷ҃',
                    'target_id': '\x9eҊГЉЮͰΔΦíeǎϞɃ\\ŪпĦӉоƵǱȩϾ˚әsɠÇj,',
                },
                {
                    'event_id': 'Ԗпӿ¹ǍdǧʝӥĂ МԕƟҋ˙ĿӡеʤϮн҃ʓăȉ\x8aӹώ˺',
                    'target_id': 'Ƿ\u0381ǶɸŪñƀ)˰бЛɞ˷UɢŉјҖԍƂýƲŧҽбʨ҂ćȲ˺',
                },
                {
                    'event_id': 'ĿŉӟŪԁÿɨЛҸϷ{ŷų҅ԦƺѦȍʢӓӗYөѽԔƏȉάțF',
                    'target_id': 'ΩɍӠб=~ƷƗђҭ°·НçͳǡǗ˩ýИʼʌЎϛŉЇԬ˧Ϯ҂',
                },
                {
                    'event_id': 'ӰóRɖЄоГЭʚƎȞԝǜɚƫ\u0383ÍѾɛ\x86и҄ʣԒɔ˷ϯ˩\u038dǵ',
                    'target_id': 'Ω,όȎЋƆ1˓Ņ˫ƵìɩʗɒыЖӆөÌЬ˖ȢtŽҟшԗɴѬ',
                },
                {
                    'event_id': 'ʕʃϋȞ\x83ÁѻÇԭ˾˱ӴʏϗθӌҴõεƗД˯˩ǫѹŁĂƞЅɏ',
                    'target_id': 'ǣӉÝ=£\u03a2˪ǷЫɎΔ*ɚѺʾʶƒȳȔƎˁŸƌĬˢϴύњāϡ',
                },
                {
                    'event_id': 'ƦŖǔƴљ«ђ˛ҼŬӖ%ӤŏύſдƀƣҗԊϱʇҗ\u0383ӻCҠʛ)',
                    'target_id': 'ӁҰҍҴĝ\x8fĶ\x8dԪԆ˰ͰЙįѴĒμʦǃȼãƄǚӲŬϠьǷԘƫ',
                },
                {
                    'event_id': '\x8f·ѮȠԆњňѫƅ§ϓԅҙğΪBͳɳ§ƙԟȩӨɁ˧±ЉɣÌҎ',
                    'target_id': 'ӻǬρŭĬǈǋƪˑвˑăíėȻʩӾɊЗɇĩĶɣÅˎʊ˘zҺщ',
                },
                {
                    'event_id': 'ʁƊΝԥǯʝɄDлɩӲΟVɣÈѠ˝ȗʛıϻЃɄȣʦ>ҳɉƅʤ',
                    'target_id': 'ɛ¤ĒǮ\x93QЎǡ¡ėϛkɑJǙȢҹÛш\xadǒòƧĖĴΐǲҾҊș',
                },
                {
                    'event_id': 'ϻԈŧ˂~Ǎ%їǬPΙɉSƥёïμɨӊήôӽȝĺİêǗΉ\u0382Ø',
                    'target_id': 'ʝǱĪȱ\x97Җŷ&ЫBËӼ͵ԏШуҊɲLÞ\x98ƵɁοʂԨŤѣĳ¶',
                },
                {
                    'event_id': 'УǘȊeԛˌȭƢ\x8cӢˏΝ÷ф˴ŏо¹řVɒөɾϞ¡ѾӔƸɋɏ',
                    'target_id': 'ƑԆϱ\x8dӥрҔ8ӽˈȅ}Ѻ˾UȮàƮԚύΦšΝЀӯ¼\x94ҚѨP',
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
                    'event_id': 'ʶ˛Ԭç˷Ñ3ʑÑγȗʪżШ˞ςƲρ˜ʡϙΪѴΝŌϝ~˚WЗ',
                    'target_id': 'ҖȬѱǲŤЦӉľȠ>ԈȄmůÇ3ӨѨԮͷіŜʘʚЎ\x94ӽȒȒǮ',
                },
                {
                    'event_id': 'Ԝ¼˩ƏȇͱΗĹΥϹFλïӦхϫΗʡ˳ӘҠɩ˰ԋCçʬˀέś',
                    'target_id': 'ȱѺМǤΣĎŚԧ3Ƅɠőˍŗˁ˛?ȅɩ¸hϭҬ!ďĪšϥӦŸ',
                },
                {
                    'event_id': 'ɱˉͿӫ»Мё)ѷæ\x81ðˤӃɏ\x7fƢʵŭpγԐҵ8ɩÖƻͶғϽ',
                    'target_id': 'ύɘΈ@ȒǒɓɃʜƇǎõ3śԝӿϞȏԐβ\x8cƅԖʗȔǶпāђǸ',
                },
                {
                    'event_id': '˞ϴ\u0379Å\xadҰӴƢӸŝÄŨϖšý\x9d:σǘȦΐЕʂʕ҈ԫǫɁҝǜ',
                    'target_id': 'Ӻ˨Ԫʽɯϊԙǿ4Ƀ\x8fƶЭыʚ\x8cȯѦҰȻƭėŷӸ˵pƁƪѡ\xa0',
                },
                {
                    'event_id': 'ƢǋĘќњЁĢˇ˲6\x99Ď¿˰ҝȕ§цΩѴMAΓɇўΜ>_ȉ˔',
                    'target_id': 'ǥŉķ˟˨΄ƤzǽƐѩ¢ǮȈѫȡԤȽԏӶȥŹә\x94˻Ѽӏʧԥϙ',
                },
                {
                    'event_id': 'îҩƓǱĈȞȥiѓѤŸҼʐћϠƊ˸nԗ˃ӯѸ@ɆӰӳƜѢӣԍ',
                    'target_id': 'і˄ҙϤѴäĠǇ!ҢǵқҬΔ!ľƵАǻҙĜȯӷΘȿȧĆ˓ЅѰ',
                },
                {
                    'event_id': 'ӦʒӮȫRǈʬϨÜɜúͼǥäɒɋ\x87ρ,*ԞϦˠԘӂʵԝѣƂӂ',
                    'target_id': '\x91ӦҟƹҢӷ΄ŪɕДō*îӤӹ˅ɬΓǝнưĘƴŭϥѸàϋ',
                },
                {
                    'event_id': 'ȃŬћΖŶȨΖɯÄʓϫ7>бȇÑȲ&ƂѨĂР\x9b\x80ʥрӇļōɤ',
                    'target_id': 'Ӹ˾Ϻʜ¯ǻɈʡŝ\u0380ǞȚØч\x83ǫƟѢʃ҉LɲŨȪӱͺƙ˔Ό\x86',
                },
                {
                    'event_id': 'ΓѽАOҩάӮȪԂčЏŶыäѧķŖхΟ',
                    'target_id': '\u0381ːΠϿʊԣɚĶ{ƍğɐƒÞʽČӱ§Ĵʽƹԡįɠȗӝ˷Ěе˛',
                },
                {
                    'event_id': 'ÛȸŵıʷɫñΙԑ,Jӷ΅ͳͻ˵ΤҮ˕ӚĦĘΥǽ\x8fãʥ˸tЍ',
                    'target_id': 'БʩЖÐӲΙτϷȒӅɋϝdЪ˥ԟѩ\u0381҄GΨʗʐԔƮқ`ɫƪÌ',
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
