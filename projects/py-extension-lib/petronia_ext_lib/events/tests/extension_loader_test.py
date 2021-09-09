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
            'name': 'ȲÈҞȜεăҾʭˍfŢˠ½}ӑƛƮӮɜӌϵјȻ(ƒȦʻˍчί',
            'minimum_version': [
                -8133834566546857819,
                -6336835057699872118,
                -4505728656283504326,
            ],
            'below_version': [
                -4845876453784726076,
                -5783165168727243512,
                -4669779571954326613,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ȇҒ/',

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
            '$': 'ȠԖĚͼȟҽ+Ņѹ\x98ˉÈϲѳБĔăȷϭʨƓ³чνäоĈɅҴԦ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -8472166003380924998,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 954356.1766381429,
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
            '$': '20210909:201650.257338:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'зǹÖ!ÜΪԉá\u038d6ѹâԝļµîӮɻ²ʹƪϿϺҿɧζҊʗŧ\x82',
                'ǝЙ¨υЉӠњҫpяƅӌϋɽÛӏѺŐѸχžƌȝˢɺЛ˗ǂЭű',
                'Ѳ\x9e¶ńɛȼƭNœȣψϝ\x87ƀŚҝŝǠɂŢfwψӃjѡɟԟԠȳ',
                'ʦ,ŝŻӥ˟ЉҒòȿѽԣǠɒ<ΙȿӋљʎƋ˵ǞѿVsѧϷĵɸ',
                "aϙR¡ПќͷĦ'зwϪɹȊЉƐҘɣčԕ¼·ЛĉӤЩӛîԄω",
                'ВҔ˦\x91҂͵ʑǀΤ\x96ƛъоƁ\u03a2Ȋƃ˹ϹœѻŽƦͳƸԙɩŔȡā',
                'ϲҘĩ\x8cƆЭӢ˚Ӆʴђ˝ƋȇièѥНŀӠҸΔȀÛԐʇʧъÜȽ',
                'ǷЇǼșțÃʿʤˬƺĆÅїɧҗνĹ¯[āѤʅɔ\x90K\u0383ѢӚŪǟ',
                'Ϣ˱κӢԢϔδ@ЉÙûѐԬÉ˭ΪǢÉ ˭ǰїҭ¾ʡ҉Ä\x80ϢӘ',
                'ϓĢΝРʆ\x9cҗȻÁǂęÌ˖ӟ;ɲϞ³u˟\xadԞĩɲ҅ŢČɒԩɊ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                283652272680193240,
                6373266330268431624,
                -4104405274626427077,
                3924978028885723573,
                -7290050787179706260,
                4638623309413703780,
                -1107128027040968813,
                2070058078118636475,
                2724744960293652510,
                4454455631774513617,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                70200.829423066,
                293255.476238309,
                -93226.34487986096,
                891814.082230416,
                251669.39434521663,
                738678.3628459466,
                838565.0604642516,
                978532.7092408182,
                81182.56791073462,
                -15470.499115587023,
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
                True,
                True,
                True,
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
                '20210909:201651.155570:+0000',
                '20210909:201651.174849:+0000',
                '20210909:201651.194561:+0000',
                '20210909:201651.213614:+0000',
                '20210909:201651.229899:+0000',
                '20210909:201651.246401:+0000',
                '20210909:201651.261950:+0000',
                '20210909:201651.277754:+0000',
                '20210909:201651.294027:+0000',
                '20210909:201651.314604:+0000',
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
            'name': 'ϻȉ',
            'value': {
                '^': 'int_list',
                '$': [
                    4367250381330372671,
                    6016802251104098943,
                    -1351910731799063477,
                    -6245989990131687349,
                    436784084238592568,
                    3828405671423397107,
                    822702844161158571,
                    -5664650792344663638,
                    -5303015769227998108,
                    263736873660883080,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ΐ',

            'value': {
                '^': 'float',
                '$': 116132.01303459349,
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
            'catalog': 'ķóѵƂCɢӔAŤӟΚŖǋĕ»ǅʑϮȺ˙ŏԘ]ΩԝʫZÇԀƁ',
            'message': 'ԍȝѸѷvηυӛůӳbÅɏäaкȔƊϪԩɘϹώеʱȷŉΏьţ',
            'arguments': [
                {
                    'name': '·ԗϨè',
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
                    'name': 'B)ї',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'Ǥύǲ8ϞıӅέʛγΚӳŃ΅ʁҫФеЍȄ\xa0ԌЋΝɏĘƚЄ¾Ҿ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        241769.26271413546,
                                        93003.02407010033,
                                        125839.6728526442,
                                        53635.750500649534,
                                        562139.0897387975,
                                        572215.1900763582,
                                        587762.4407971036,
                                        757484.1004093282,
                                        166636.73677644494,
                                        60383.692524821556,
                                    ],
                        },
                },
                {
                    'name': 'ѰƹƻеѦ#\u0383\u038bʻϢ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'чԧвɺİĳѬԟVŒѻbǻɜQѽʬȼ˃ȩȌϊ͵Ӹ˙ѵżԬԪӑ',
                                        'ӔɎȒѡҵȆ}\xa0ӞҖȬĊтΐӎԭˆι\x8cĝҗЃԋǛτӡʋˋʇÎ',
                                        'ѼβΊΎƯПAѹWЋͲЫɽǧ˒ɺƧύιȗÏ\u038dĩľϊÎεťǎǘ',
                                        'ŪҹɀΛƦ9ͱ˦ŶɇgɗӀWɛǷƭƉFоҥTɘƀʤ]ӟ[Ǭđ',
                                        'ӹďʇÌж¡і҃ҽĝ ιǛ˽Ѿӆě¸ӹȮɓʇЋ҇ÄцϞśæı',
                                        'ŎˡēʮíϏѸȸ\u038dҥһ©¯3λΦƌήǢҾ˭ĶПɶыËə7ҧϗ',
                                        'ӢҷН\x86Ƽ\x86Ђ\x9f˩ͰàЍϱ\x81ԗɴȓΖώˮƕӆȖӋ\u038dÄĊԆӒʡ',
                                        'ѭơƺǬƭ\x84ǊχΫJȑψʨȲ˚ңņϮÂ˜Ȧƭ¢ũǐ#îĴ*҆',
                                        '˯~ǈ΄Ýzԕș҄ќȼŻĽәĲМςͷО\xad\x84ɵʃԒӹϗΠɖɸơ',
                                        'Ϡɕlǔ҅ÏιԚЙÆwҫȱ}ƈÐΈƸΞƿӾБȜɉɟңϔWЄʹ',
                                    ],
                        },
                },
                {
                    'name': 'ЉƈĨ˰êҠΐōÖˉӧɓόȯ˸ѰÓ]˚ԦԀѼƳɓˠĢŔȕ˥ө',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210909:201649.181022:+0000',
                                        '20210909:201649.196732:+0000',
                                        '20210909:201649.212445:+0000',
                                        '20210909:201649.229840:+0000',
                                        '20210909:201649.246788:+0000',
                                        '20210909:201649.262878:+0000',
                                        '20210909:201649.278473:+0000',
                                        '20210909:201649.295002:+0000',
                                        '20210909:201649.310993:+0000',
                                        '20210909:201649.326592:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ĳ&=ϗϚӐ3ŉǚćħ˨ǁȓǝӢɄ҅vČϨЋːʠЃʘІʽҿƒ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210909:201649.412872:+0000',
                        },
                },
                {
                    'name': 'ʿɂѤԚҴLВτй',
                    'value': {
                            '^': 'string',
                            '$': 'ӔԝƦȬʀ!·ȱ˪ŎиŘȒӀĊӗѥȬϧȴĹΗхʾԇɌѿʛÒɢ',
                        },
                },
                {
                    'name': 'ɔҌlǑȧ³úæoõkƫ[˪´јәàƹɯȁЫϋҼīɯůӞÛɇ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210909:201649.551151:+0000',
                        },
                },
                {
                    'name': 'ЊĒΉʖS4gнȶǙћϼEƽƾǸɮɀϿŰωҚШϟҸҵȫϕhѻ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ɽİɩ\x86ĦȽ\x9bƘɕΓ½',
                    'value': {
                            '^': 'float',
                            '$': 636567.0415648309,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ɋɚ',

            'message': 'ć',

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
            'identifier': 'ΘЗʇǂͻ°ԂΤȰƶϟƎҽпӉƈǟӄԆ¤¿cϯѭ҃Ƥә¶σɎ',
            'categories': [
                'configuration',
                'file',
                'internal',
                'internal',
                'access-restriction',
                'access-restriction',
                'internal',
                'invalid-user-action',
                'file',
                'access-restriction',
            ],
            'source': 'ԟŢ\x87ɱŔʋdƅ˞ŗ$Ѩ\x81ŜƬȄ҈śДӴIǲϫӟӮÔʠԤ?Ł',
            'messages': [
                {
                    'catalog': 'яʸӟŷÏƒщ§ӲŖʼʹNІԏĤʹӢҺθgʋѧ^ÇωԈϰÿȍ',
                    'message': 'ǪǴӔ£˸˞ŷ7пĶϮƁƖɚ6ʲӞƪϐбƢƤȔϖŉβүɴ$҃',
                    'arguments': [
                            {
                                        'name': 'ΩÖʛˡȤІ\x8eϰфӻɯþδgˤяѴӕTȓϾ\x84Κϯ1NԪ²Ƶś',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˸',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȢҘӔҀĖŒǎШƠŸʣhѨΫʶ®˒Ѡǂ×N\x99˱ʎӦәԋѠӭā',
                                                    },
                                    },
                            {
                                        'name': 'ΊЋÄ¤ãӧϰíȢ\\ц\x8eӐɎҼύőÎяƸřЫi˴ʾƝΎƥӛԮ',
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
                                        'name': 'ѝʱ˃ȕÚŝϒØƥʺӭΈȞûтΠ2ϔəʇ\x94˾ТТ)϶ǜðΕ˻',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 63288.90419163584,
                                                    },
                                    },
                            {
                                        'name': 'uϐј˥dˈĚұŶįȵȓ\u0380ȠȡʓEԘҰѵ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201634.293127:+0000',
                                                                            '20210909:201634.308441:+0000',
                                                                            '20210909:201634.324541:+0000',
                                                                            '20210909:201634.340353:+0000',
                                                                            '20210909:201634.357050:+0000',
                                                                            '20210909:201634.372982:+0000',
                                                                            '20210909:201634.388395:+0000',
                                                                            '20210909:201634.404093:+0000',
                                                                            '20210909:201634.422600:+0000',
                                                                            '20210909:201634.443545:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÙˣĔӪѮ£ьȗb˯ĆǵăPҜ\x86ťКCƉʶʃțǷёАӀ˱ҕɲ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201634.563189:+0000',
                                                                            '20210909:201634.583897:+0000',
                                                                            '20210909:201634.599700:+0000',
                                                                            '20210909:201634.615035:+0000',
                                                                            '20210909:201634.632330:+0000',
                                                                            '20210909:201634.648068:+0000',
                                                                            '20210909:201634.664524:+0000',
                                                                            '20210909:201634.680740:+0000',
                                                                            '20210909:201634.697131:+0000',
                                                                            '20210909:201634.713773:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҉',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ë˷żĦϽƗ®ŻԋhˀÔ\x8eԬbɉΞӨцԓȷȱtÅč6ȱԃĩ˺',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 119004.77227732411,
                                                    },
                                    },
                            {
                                        'name': 'ǉõΞǮIȳԥǮñӨņνŦʉǗΈĂͽɧDϰāƺ\x94',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7016948155075113489,
                                                    },
                                    },
                            {
                                        'name': 'ϝγɑѷҫȔϮңÖˢŐŃǷйpΦŻŢ҆сƠәɦƎƃàУȇΓӎ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʴæʜQʧБÐ¥ʶǋҎfќԙÕґȓįηŚȉǗӚɁүҙФǈʆž',
                                                                            'ůԐԄџɂιȴϚ\x96РβӸҶĸÁԃǋĀϵPɮδҜʆ·ǈԊčʵī',
                                                                            'ǍΪӾɷʚFƫϪвԢ{ŽɰϹѼˈƂӭɗ˛șѤʑǼʦʄ\x8fıćȢ',
                                                                            'ϞŪɿԜÿɕџ˔Ϩ\x98ˠȠʁ,ԛmˤ\x89ʧƋԮȁ`ȇȊɾΑЧŁЛ',
                                                                            'ÃȋˤԫвϨ`µȐƮ²ëŜЯԖǩ\u0383ԐҼӖҋƊѲɼɎӪԉƣϏʆ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʿ͵ĸөÝʁүӐҵǿʖ\x9bƟƒӔúԂȄҼӮżӡȪļ˷ĐϹϔďŘ',
                    'message': 'Ķ\x9cҍϤƪƕưƢǀϠΝщԐϾƊѸɽȖ\x98ΞĤԎǛĬʄӒдǘŐ˅',
                    'arguments': [
                            {
                                        'name': 'ӌΘęԔӌӍоĮɀ҂Күϗ¦ОŒáȐǬô҃Ɣƃѐˉȗ\x9dɹуȄ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201635.464961:+0000',
                                                    },
                                    },
                            {
                                        'name': 'μʜʋ˱ŬƅɄһԝяKǪϞS',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6937169427365773574,
                                                    },
                                    },
                            {
                                        'name': 'ĸʜ˲UʦƽԈMy',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'оɋ:',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ɋ˃ϴтȕѼ\x85çчЙԎʹŴ~?Ћñѧ!ӷ¸ҳ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ҿʚˍōƵӶӎѮ½Ãѣɣҧҳ˪\x8aŘԏӲӧɟԒèˮåƈǄǘҖŽ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŝʪϏӨϙYĊɈ:WѱΛѽæˑȦʕ˨ɴÔѤһҸʩƖ6lӀūɆ',
                                                                            'ŵȪ¿Ϗ˕ãԭЁϕє¢Áį\x86V6Áӓ˩ϫғЋӻέʌƅënƒΕ',
                                                                            'ҢĻĉɫΧˎђ¾ӯԢԡǀđқ˔ĜӿòŔŷńǣώǓӆўæɰɝǳ',
                                                                            'ԣҰɦūиӚԈƣŬ˸˻ɗǶ҄ЋıÞăԖϛРӜї\x93ѯ˳ѾԑŀɁ',
                                                                            'ŉǏЄѼœƨöNȫӲâ¨ŨʁĿlkӁȂЛɂ\u0383ΥӋҚÏŤѠʋŴ',
                                                                            'ʘ˾Ї\x91ș҇(λʌөĪĊѶ=ų˳ʅʸɋЃɵʜƬӫϊўȯԊ\x80Ѿ',
                                                                            '\x90ӫŧԚȭѫʍOKĖ\x92ԫˡ\x98ӣȍΑʒνԞ~ϰťŵӖѿLȳөЈ',
                                                                            'eҲɘͲȃɢǜѰʕƼԙșфäϐȜȝ6ΠбвӿбcͲѺ˺ʳФɷ',
                                                                            'ÒʅƸĎӮtҽȞεļŷ5ҦÁљŗɐѶĦ҂ħƊеόĔɏƤʪ\x8d\x8c',
                                                                            'mӨӌĜϚʒӞγʾȮlǓȶ2ѶÂĕӪČΩɦϜѨiӹЗԀéаϿ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '<ī˶ɬǩӺѱȸҏεϗζĽ\x94ɌӪżĺҤʥӞ҈į\x9f«ʥɴōԍŘ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'O¢ѹȊ˘ӑǌ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 288742.0689044457,
                                                    },
                                    },
                            {
                                        'name': 'ǽǣŬǺɭƶįҎ˻ŷɑŎЄ²³iƏѱ˖в˺ϋ˄àЦɼȌҹ\u0378Ζ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˈϬľ¢˯Ӯ¶ɜ¦tѝģÒɴEʶΞÛʪ²ЛŕǻɀɶȈȍ҇NÅ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6399729220042875348,
                                                                            -2158733771271308077,
                                                                            -8607460502828664183,
                                                                            -7348686626892071460,
                                                                            -3665178612746891397,
                                                                            1607547566419722617,
                                                                            1544196576670492833,
                                                                            -4093305623054788254,
                                                                            -1362348726448255457,
                                                                            8488480467266447123,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѪκΪѻ|ƔԃˇξеԇȵɈ$Ëãý·ԀѹNΫĔȹǊĘ«Ӛ-Ж',
                    'message': 'bЉĸȎϱΛМ[ǘӕƷȸǗ΄ȘüȸԀ\xadъҮ8ΆǇċƻΙԢåĳ',
                    'arguments': [
                            {
                                        'name': 'ϧ#Ϫӽ¼ɥХ˃ǻϴúίĲϺʣː˧ŘԡȻŌľпĵr',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -84210.8313531548,
                                                                            819838.4113426977,
                                                                            240206.97889021138,
                                                                            175682.19304573192,
                                                                            761124.6137044413,
                                                                            675054.8416669194,
                                                                            -83402.31138447765,
                                                                            538522.4260382833,
                                                                            274168.6030193858,
                                                                            662259.4323131958,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӌʝϒ4\x80ŗrǾɁɦȚҐ΅ЩɬȗΠÌƪˀ°ȔʽӇϛĒÑΒʛΜ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -552712108505499413,
                                                                            -9185179144560395319,
                                                                            4456876079752072759,
                                                                            6675877263366213644,
                                                                            300524386283085078,
                                                                            -8222930011378498549,
                                                                            806058082415121965,
                                                                            -2949027325633248701,
                                                                            5520260041696273595,
                                                                            5753639517866284695,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĩ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            89791.8007091814,
                                                                            719716.4405492619,
                                                                            640591.1809402127,
                                                                            517965.0092488198,
                                                                            909060.6774755197,
                                                                            143934.7031538872,
                                                                            -93165.39814424902,
                                                                            -77748.45295574769,
                                                                            426057.0550142954,
                                                                            867661.4216867494,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'uǂĄςВλǋҧьǑǧǼƯƯѕ¬ɘҥCDӳŗǤƶȭ\\Rw°;',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϦǹеӋǡƪĜϱ-ˤœǝǳԔϲԬʈχЋ˷ԟˣȨί˸ǂȽ˽óѫ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201637.927977:+0000',
                                                                            '20210909:201637.947966:+0000',
                                                                            '20210909:201637.969572:+0000',
                                                                            '20210909:201637.990270:+0000',
                                                                            '20210909:201638.009940:+0000',
                                                                            '20210909:201638.033255:+0000',
                                                                            '20210909:201638.056013:+0000',
                                                                            '20210909:201638.078703:+0000',
                                                                            '20210909:201638.099310:+0000',
                                                                            '20210909:201638.114762:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѕεɁҷtѮɨ«ƼȄ¦ȕĨìʂʾZЉʷƍɪ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -7392.778221601475,
                                                    },
                                    },
                            {
                                        'name': '[ɫЙ\u038døȕǺѾӂȊƚάɑ˭Ý\x81ʃsßÕ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201638.265908:+0000',
                                                    },
                                    },
                            {
                                        'name': '?äōőУ˗ΨDқÏģ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 592919.3605570827,
                                                    },
                                    },
                            {
                                        'name': '\u038dЭҔ\u0379ģҐТϧÊёЗ&ԒɽɏȇF¥ΐĢɮ²õ\u0381ԋυˈγ:˟',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201638.420927:+0000',
                                                                            '20210909:201638.440086:+0000',
                                                                            '20210909:201638.460231:+0000',
                                                                            '20210909:201638.481346:+0000',
                                                                            '20210909:201638.502049:+0000',
                                                                            '20210909:201638.521622:+0000',
                                                                            '20210909:201638.538977:+0000',
                                                                            '20210909:201638.555337:+0000',
                                                                            '20210909:201638.571684:+0000',
                                                                            '20210909:201638.595721:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҲƋӋų\u0381ӻω¬',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ːάLğԃԌƈ×ҩΦѾȧͲūǠϢљöϧ˷Ѥȅ΄ɑˊʗЎΕÚǧ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȣǤϙͼϘϫμƙɺàЪҳ2ÑrԙЕ\x80ϖӬЊͳϚԝɝџ:ӝҳԉ',
                    'message': 'ИҊɀ˨Ð=ȆȺќːӃӟV˳ϥɂÎԙ,ρȇќȝ˹ъŜ\x87Ȳɮҧ',
                    'arguments': [
                            {
                                        'name': 'Ċ˭ɓʭ\x9cď9ХԊ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǾеɨĊƵWÁтӪӖϸѺԃ˛ʟômģϪφΌʯқïŀĹŦµǏr',
                                                    },
                                    },
                            {
                                        'name': '\x90˚ƢϥȌ^ǻõD҅ÝǱČ҈ŕĸˤԞ˸˦ǖͳҕȨǃϭяŪӐ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -195453099171381993,
                                                    },
                                    },
                            {
                                        'name': 'ǣĻҼ҄ɈЩˌȏӶÕÜɠХƓˍÇ\x80ˆɰΖİæ\u0381ʬǒ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -39351.358989304674,
                                                    },
                                    },
                            {
                                        'name': 'ĘΞҧҰ{ʯ\u0381ɉȇ5ЌɂӲѻǀȋ\x83ԧμԃEдќΦǉϓѩǂƷū',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'œħĎţ\x86ȊǅԄĵʇ҇ЛΗÌњĠЌˬ+˷ Ėΐ?ĭԢɴʟӊΫ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            676308.138563943,
                                                                            757846.2313025062,
                                                                            829090.7409000488,
                                                                            811283.1153653373,
                                                                            795699.3013118724,
                                                                            286793.33258002735,
                                                                            570197.0165671789,
                                                                            512598.18774017075,
                                                                            911867.0269449967,
                                                                            496564.0208728091,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƣɽ½ԧѯǯхAҮџцͼɥґξ\x92ӯʑ\x87ǂêƩ¨ĉӕĵΊϧӘϲ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201639.493775:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ā˵OǏʷӹǚȇ˱Ԧʇ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӪƚӁӒĆėĨúiYѱϘӳǺͷқpƔџҶûԦӧϫšѱΫƶNκ',
                                                    },
                                    },
                            {
                                        'name': 'ŎѴR',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4428283634054059533,
                                                    },
                                    },
                            {
                                        'name': 'ǱϨʫӀǭøˎćhưԐ@ѰʉƎ˱пϮ8>ζĭԐŦį',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3873391435434265751,
                                                    },
                                    },
                            {
                                        'name': 'ĄН¢ˋĤƈʸσĉқSƦɢƍÑϵɌÙԡʖȏѕȡ@ʐþαżϓƠ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8008152873984998827,
                                                                            -7082842751179543428,
                                                                            6833192328521014000,
                                                                            8903044074540247139,
                                                                            -8162116137487191120,
                                                                            -1479946886921477629,
                                                                            4764989781940421429,
                                                                            -2889150129376308374,
                                                                            -4202152494112330340,
                                                                            -3711427027345279634,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'õĽϧºҪэɕҴԬƯʐʜԮǥgη˙ȩΗφӋ¤ѤϧƋ҇\u0378љ.ƭ',
                    'message': 'ɿĻΖҭȶϽѰȋȌȠƃɰʢɾ>εčк\u0380Ǥ͵ʧĖͷƧƦԜԝЍԂ',
                    'arguments': [
                            {
                                        'name': '\x88ɹζǨ \x9e\x9cˁȝͱʲǇĘϬԔЫĭƺȁđǻʡȷԃмъѸ¼Ήь',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': 'ǡØĄ:ųҽǽϣ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6330728012349580885,
                                                                            6462734907740983932,
                                                                            -7781976417440312222,
                                                                            2298030285294261266,
                                                                            4064804814461882271,
                                                                            -3598221202413343213,
                                                                            -7166497170136800449,
                                                                            -3863201477692302092,
                                                                            505545024914391312,
                                                                            9176316979916968862,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'şβԫҮˡó½ϛbĖϜɛξϬêĥҚĘѾĊˡȚúѽнʫƈ',
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
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '©Ƚǂ҆',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5913281769158822485,
                                                    },
                                    },
                            {
                                        'name': '\u0383eχѠ˽ɿǝ+ӥǶϴ³Ȇˆб˽\x90¨ėѸ\u0380ĴĩƑɩȱЁц¾ș',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            131788.9695271843,
                                                                            212354.6957558344,
                                                                            791890.21947272,
                                                                            -55958.92721195149,
                                                                            291800.6980576085,
                                                                            337494.30325392727,
                                                                            273858.73699465307,
                                                                            648718.4639682003,
                                                                            126491.56979459329,
                                                                            815632.8732693502,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ėʫ҄ŧĸZěЧƕĚ31Ӫâļρē˓АȏɌȸϏÙőˮŞԛĥҾ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201641.129661:+0000',
                                                                            '20210909:201641.145340:+0000',
                                                                            '20210909:201641.163120:+0000',
                                                                            '20210909:201641.179144:+0000',
                                                                            '20210909:201641.194676:+0000',
                                                                            '20210909:201641.210130:+0000',
                                                                            '20210909:201641.225796:+0000',
                                                                            '20210909:201641.241764:+0000',
                                                                            '20210909:201641.257414:+0000',
                                                                            '20210909:201641.275501:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϟiˈρȝÅ\x84ԕҖHӆǢӈϣƗκ\x99˫Ɏ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201641.362528:+0000',
                                                    },
                                    },
                            {
                                        'name': 'EǄĐɜɜԀĲҹȞɣԒʳp˼ɟҸϋŇȧɚЧËʈɱ\x86ÅѡӤЁť',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 248565.11058740393,
                                                    },
                                    },
                            {
                                        'name': 'əʼʮʭσҩΙԃȔμ9Ǥ\x9aɫȽ4¹ӲϕˉΪǃ"ԜǤχһӁǎˉ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɶƝɀ˳ſЄȹŭɟ[˨NˣϢƆÞæǥӣǿҔʘǨ˵ӅԇԂхˠљ',
                                                                            'ˢńϕҋΗԃȪÇԒԝYԘѢʥ\x89HʇϫѲφεȠҐOưƾЈΕѢƫ',
                                                                            '˱QϳГʆɜɨ\x8fФųˑҖʹɐƼѢŇʐösϮȨβƩʌ×ɯρ¶з',
                                                                            'ɄţąӛϘāĽÎɪԆ\u0381ıeŢҢкϟȶØĻѻ\x84ǿτԂТҦzҠя',
                                                                            'UΐƱƀ\\\x82ЁŷɟӁϣ7ȝӧЭϑ\u0379˝ήÕЂɌʐ\u0379|ɿ\x94ʫɗȿ',
                                                                            'ˢӟν\x9dĐПЖƎ҄εŭ¥ӊˈӝǄѰ¸ѼƗʠÝԍи˚čɖ\x85ˆğ',
                                                                            '΄ɖɬƙђҮ\xa0ĶтɗɡɴҨԇşǁȀȵԑǻщ˲ԮĎňȹϵ˝ѫņ',
                                                                            'ˈEˌҺӸ·ğǤӿjƷȀǙԨȸ\x8cϸõӎƠŔª˴ȫĿɎUҸЇΨ',
                                                                            'ϗ\x82ĘΌӍӮĸϦ>ԂɎϚƵƃŁƎͲлƣКͽʃӓ\x87Ţ¬ħǃԟӸ',
                                                                            'lԃŸŰќы0EҧҗΉͳʵɬ\x89ЯӇЗđȊ\x7f҂ԞôУ\x88ѿ¥D;',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ε',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӹ-\x90\x80ҸWȵί\\ˇĀϬȺ ȻȆȉ˹ƴϮĦȡҺʚқʙ×ΏVȗ',
                    'message': 'ІIШǬ\x99˰ǘţ;͵˖Ԙ@ҽϷƣǏÅΧɻǻƞǲȋLϗӅĦ>Ƴ',
                    'arguments': [
                            {
                                        'name': 'Gυhʮɶǜʖ\x93ӝSϰĦҵ¿ƌ¼ϢŧӸʙ}\x87ɹ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '¨ȣ˒ƄҌ7ŗ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŶőԑͱёӶˋѭѫɃΦΟΫʈδƟӍ˨ҒϲșрӂɑȆ(Ǚξ˻ĕ',
                                                                            'Ǯªư«ǽǒǾèϥEҧ˃ӄӍԞѿЕƘӘƋ˳ēťІuA·ǴǈĹ',
                                                                            'Ы\x91Ͽȸ×В˙˅ѺϑԠ˱˃ƅ\x8d¡ШѧũҲļҢĉɇȦůϭƏҊӳ',
                                                                            'ēhƒθàɌʃAѰŧʜϐW]EɁǭЂv±еÔʁѩϋíэгüѳ',
                                                                            'ҩ¶ʚΊŕәИĜԙťºʋ\x88ΉȰǬΞΌɞˤMѿäԋƫ˗çΏœО',
                                                                            'UƠʸ͵æ\x7fǌӖʃЃɧщњìƁʥрşӡőőW҅zщƞԎѹȲ\x99',
                                                                            'ԗξϻӊÏƽҫύǎΞȂ\x92Τіȑ řѬŗŪӥ´ƙΟӁƋ˭ĳƱϨ',
                                                                            ' ÌƋѪs;ѺЌ«āӶӂkλhҊΏDҭɗtʕªïҜɊяͳǑɭ',
                                                                            'ɵҶ˥љ˥ȂűҞţ\x92¿л©xDɯS˙ŶгȬʥʈŧʀѱřʢțӸ',
                                                                            'ƆСɕǎӦˢͼ;ѪЕāӽоȐ˞ШHԓԪêAӣȓЌҡ\x97ѥǂѢԜ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'μɍјį`ʹ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '7Ȼţźǃ\xa0¼ҢEѴҊԫΦ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            567318.8753708681,
                                                                            -98339.12600466284,
                                                                            821734.0096063456,
                                                                            191242.02549281158,
                                                                            173940.14191640972,
                                                                            496296.7991697022,
                                                                            215415.18833771,
                                                                            50279.42195436946,
                                                                            836689.4198451093,
                                                                            800538.6593958343,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'в˸ƾàҼҐԐΛĵӧњŏʠѓŦСΖDɹ\xa0ʧƴԀџ«\x8fιůeӞ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6124185526055461678,
                                                    },
                                    },
                            {
                                        'name': 'ıѫ-ԒɁԠΗϮ\x88ԧ¿ҒӔɔʽ8sâʦӞӞͿɺÍ³\x99ǾˌцԐ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '¨˻Ώ)ϻʁˍˀөXHӂżˈԮ˜śȣŏ\x83ɐϡѰрҺǬÇƒÈƵ',
                                                    },
                                    },
                            {
                                        'name': 'ϧŀοƀʤ|ϨɹϨʅˑ˰ÌǤȕ~mɜ!ϧ_ɎЃ˸ŏПimďƮ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '8\x90ƿǉҩȲЯǵ,',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĄĺȥŮԁƝɬʂĩǬʃð6Θȉ\x89ÙЙΡɇÚъāϘ¥Ɋι˳ˆД',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201642.906683:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x96ɊʎŌ\u0379HƺЌБȬȓуҝǪēмʄσѺδĜʿϸΧȯ0ÃД£ȵ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѻԇȤƄïιИӦѮΪӨϰp\x92҅ǩʾɟǞӡыɏб³ă˚ɛԈ©1',
                    'message': ']\x88Ș»şÁÒoȱʠWΩ\x9bҲԇŞˇǯΠʟȮÀϥͻеыѡïζέ',
                    'arguments': [
                            {
                                        'name': 'ĽΚϵ˦ƑҫɱЙ²Ó\x8f',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -14824.999765607688,
                                                    },
                                    },
                            {
                                        'name': 'ӀйѾȘʬǇОҜÌūʚêԧŐRȆ"ЄȈʥíҴəģ\u03818ҿҥ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'Ƣʢę_҆ʭ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'őвҼǰΎʑόӓƌĉѪ˟Ρѵ\xadm&ѻ˺ťʦȞҹįʐĚǵͷԆb',
                                                    },
                                    },
                            {
                                        'name': 'ōүϔ\x8aɋӂļȲ҈ϒÓ\u038b¾тү~ɬ΅\x98ђʫԃĎ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 710279.5790667444,
                                                    },
                                    },
                            {
                                        'name': 'ѷƬы',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201643.550759:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǫÎτͺϮǔѸΥ\x94ρƫģƲ;ѣ˝ǊȕҼĹ\u03a2ѩѯČĒ\x9eϝʭǊ5',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201643.615711:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÝŎȃ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4380849042117448884,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'òĻJʒ˅W΅ѐ#ҹǄʪƊЛ˝àž˥Ѻȋȱ\x89ǃȍͳˬ\u03a2ғǰш',
                    'message': 'Σґԙû\u038bӘĞәŏЮɲȭηάʺȖϹӿԭMƋɼΤʡ˟ϲçйҏʽ',
                    'arguments': [
                            {
                                        'name': 'Ѷ΅ĨһοĀӸˊƥćhѬ˄ԛyKŬĊȍĥƥŋӗ¹ƈÿГ˾ҼY',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4895898437141030152,
                                                    },
                                    },
                            {
                                        'name': 'öɐ2ˢ\x8eӳӣ¯ňŃзҦӬ°ԉ]ȣєҊӈɄҸǋΔ¼¼Ɨҽ˺L',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԣΪ}Ψϭџ˚ѢΞŧʄӒ\x98ҙ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
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
                            {
                                        'name': 'Ѳ-ǽҸҚΑΦȿ\x8dˬʮҳļƑηϮѽқʉ[ԪӭŅÍˤ˄τʞȗȠ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҀɒÔ÷ԓ³ĦċӤ\xadaɣϓξɝʆĺλҪǉȑĕϯƻÎԧΎʻʰƻ',
                                                                            'ɭ¼íſγήӖɵѹüƸͲƂцAĸɦŽљŷЈɖáͰҁȖƕʙǔϴ',
                                                                            'ǀǗӨӾa\x92ϐƅҡϊаǀɻɾАӶN-Ѩoü˺ÖØĴ\x9cƚˑɗϳ',
                                                                            'rƴIZςгԫɝǴĞԮǯ\xa0ȽäЦʢǧϤ3ϲϴÁ¦Н˵Еɩˮȓ',
                                                                            'ˀбψҙȦˁ4űț\x8cσӪʢFɽƦЄɳѤƦҹåĝo͵ģИԠʵӿ',
                                                                            'ѥіћǡʛ£ʡϿѸ³Ƥͺ\x80ċҎҊƑʼʑ͵ǅѸѐΛӾÕǁŢqд',
                                                                            'ӮŸʬƗΌϛʕӪϫ\x85ӍȷųǂɯƷε\x9bˇ×ӷǄȝʩҒǕɺƢсń',
                                                                            "\x91˃«ϔsӭ˷ҳȑİ'ȆĻŊѽRӼʠҦŨѧȐҫӕD\x98Ӗ˔ǹч",
                                                                            "ʴϏ¢ʮǠӜuӶ'ҥǢǳƭӮӄG_Ҍ",
                                                                            'зȸ\x93ҌϬȟҲsȻЦϜ˫Ͱ\x98ƕ·ғӂŢ+ҖɺӊWŗŸѹӵɒh',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ιӈ¿ӎ=đ\x80ȠɝЋǢѫ)KҪ\x87¨ūA^ϐДѳSɌ˨ɨԨȖӾ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʨѶ"йԧŹǩƇԓɏ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʩпњΥ±ʺΑƱƁĜŁȕƍűʝóˆЏƊʪ˲Ѯż¯!ĕφƬѴɰ',
                                                    },
                                    },
                            {
                                        'name': 'ÙЗ˘ĜTΚhÎϮԫνҎȆΌΡĀЫǔУΔǯɺȦËЯɰӓdǮŃ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201644.704611:+0000',
                                                                            '20210909:201644.720714:+0000',
                                                                            '20210909:201644.736698:+0000',
                                                                            '20210909:201644.752407:+0000',
                                                                            '20210909:201644.767993:+0000',
                                                                            '20210909:201644.783566:+0000',
                                                                            '20210909:201644.799880:+0000',
                                                                            '20210909:201644.821005:+0000',
                                                                            '20210909:201644.839157:+0000',
                                                                            '20210909:201644.857909:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȲԮƤŻԗœˎ˩ϢĐõȥÑѼơʹʷӪϫӡſӫȎǥƃ˽Óвąģ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 156262.96019806643,
                                                    },
                                    },
                            {
                                        'name': 'ǥʼǦ˂',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȧɓ;ѝ¨ĚƭƅԡΣˌъПӬσ҃ɑ-ģŵϜϊ-?ѼʘьˊУё',
                                                                            'ФӡïöſčԤʆÀǐѿųɴѕԛ\x93Ͼ×Ò˲ŏÓȏϜӦϢɮι(ˤ',
                                                                            'ŢүњʀΤʒѝφΗΙZɑȷϼҿƲϾԞüӭSüϨўъĉ×Êјɴ',
                                                                            '\x84ĥǰΑ˞˥Ī¤ǪɫʊŹÓӚɋˮϬŧЕČÏǌʌηNοҥ˶\x7fƽ',
                                                                            'ΰÁ˹Ԝ\x864ԫϽ\x89ǺԙĝӑĭϿȍϕĶ\x8eСƼϕӮȕύʔʴӧȪɢ',
                                                                            '©ˌШ¥Ȩ".ƎԘǮǮXЋϐѕЀǨԡˠɩȍ¥=БϾΦȹωñ˚',
                                                                            'ҊІΓ¬Sȹ˓đκТӬŜɒãЩϑюĻ«ѧȆƢǄΚƴљт˄Ѳç',
                                                                            'ƈÒҶУӺ˳ʫɸʾ®ВА˾Î˅ǬԠƚƚɽɐ³ǣѨĜ\u0380çǩMѳ',
                                                                            'ǻҪŜƚŔƇҤʋ˥ΕřԏҮщПУ\x9d\x98ͲiӘrʔɌӪѱϡЗ͵ò',
                                                                            'ʤѡƌĐ\x8dНόŧNȬĻĊ\u0382\x89~сɎɋѨʚ¾ϰδĊѐôËҪʣψ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĂИɋӣǞȯDǶLѨĆϕңʊӠϤȤʨе¦Ͻ ӽћƳǨ<˄gh',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 533786136264608609,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '¹ϣҪɡʘǢԇϹ˥˙ЉžęԈѿ\x90ӝώ\x8aɆƣ\x80ŠФ',
                    'message': "˵˖ʇȄŅʱëѣÿľΏʟǀǮЮ\x7f˯ǝŷЭӮгʈDš'ЖԘOԖ",
                    'arguments': [
                            {
                                        'name': 'ůЂԖƀϹ˂ɅBʑŦϪҧˈϞˮɫә£¸ǨΙ³ҧ\x9cϻßԆϵ\x99',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201645.414035:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƚɉʿȩδƬƈκԩȷµϐÊΫĢ҃ψ˂Ш=Ж;čʫÜ\x9a¨ȕxƟ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԘҭɕǼèÀϽԭƂӨԖԮƂŹĒΤҞŉϟoåCĞƈŰҠǚƊԗ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 7489.3784108366235,
                                                    },
                                    },
                            {
                                        'name': '\u0379ҔɅԧʪŃď¯',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -48396.4162599331,
                                                    },
                                    },
                            {
                                        'name': 'ʋΟΙ\x9cͳ\x9d˨±ҕǐӐƫȲίЁŞŸƬϠǔϗĘХźɊєŃы΄Џ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            465236.13848755916,
                                                                            207991.19239520963,
                                                                            5284.895189482675,
                                                                            719611.1040379888,
                                                                            680636.7910295284,
                                                                            745122.2755999486,
                                                                            -10098.0662002194,
                                                                            602487.6488485944,
                                                                            50188.40673979523,
                                                                            535525.7450194908,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʟ·Ƅʖǿ˾ѥѤϐ\x81˺ҨƇˊpèŷˀƐ\x98ԣĖԑӀÛɷЙͲ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            393886.6401686015,
                                                                            219056.52478723013,
                                                                            162817.95072919433,
                                                                            840839.7009834793,
                                                                            70664.3732063105,
                                                                            174405.41554765415,
                                                                            425220.15360260755,
                                                                            506783.79966820055,
                                                                            453408.74572047975,
                                                                            -75993.06971874728,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЧˢȣɃԍŞˁĲƖǓ=áùϺ˺O',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 425794519703394979,
                                                    },
                                    },
                            {
                                        'name': 'ϙ£ӮƲȞĐºɋZьӅӛȹѭϴǸƖҘ\x8eƛǌƢˌВŋҹğ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -14187.1727572253,
                                                    },
                                    },
                            {
                                        'name': 'øГԣӓ4зӅÆϲԝϽʟġϩɎ!ȝ¼ʻóǷӁĨϮϧHφʏҾг',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201646.318987:+0000',
                                                    },
                                    },
                            {
                                        'name': 'įƓϸʚҰĤʝ\x83\x87dłȠҏÀуϾɻҟ-ɿΦ\x94Ƹ˖Ϝʉú\u0383H˄',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201646.387193:+0000',
                                                                            '20210909:201646.406586:+0000',
                                                                            '20210909:201646.426267:+0000',
                                                                            '20210909:201646.450607:+0000',
                                                                            '20210909:201646.466600:+0000',
                                                                            '20210909:201646.483953:+0000',
                                                                            '20210909:201646.501288:+0000',
                                                                            '20210909:201646.518698:+0000',
                                                                            '20210909:201646.537241:+0000',
                                                                            '20210909:201646.554182:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'êXѳͿǌӡӠӲИeϔǎȳ\x99ƽ¾ƛ\x96żř˷ǆϠģȀҮ¹¸Πȿ',
                    'message': 'ƈҌЬˉņȨȻǃϫƕͰҠɰȗɭЪīһԙǑĬ˰ƾ¦џӭӚƒʧӿ',
                    'arguments': [
                            {
                                        'name': 'ѓӗӆϰΫǉŋƎąGǈÊԌ¡εʗ˞ȦɧȳˀśӫϼѶȶˎ\xadȖó',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 259145.72936094704,
                                                    },
                                    },
                            {
                                        'name': 'ŞŽ3âɡ҅Ӝ˛ɥȿЅѻӶ\u0381Ҁ?9Ȫ˱дΚŞϧéǰŦȍ¥uƱ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ıĀϜсvď{ɉȆÑ͵ˤДȘ´Ŝ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʩƧҒĝɉϣɐɳϊľȌϴВϻѳί^ȁҔŭΖęіǬĽ˔υɠAϖ',
                                                    },
                                    },
                            {
                                        'name': 'ŕ¦ϵIӈɖɛEѽáĵͷʴјӷěɞкОιАѡќәˢԫћǁʡȁ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201646.910473:+0000',
                                                                            '20210909:201646.929457:+0000',
                                                                            '20210909:201646.946523:+0000',
                                                                            '20210909:201646.966927:+0000',
                                                                            '20210909:201646.990181:+0000',
                                                                            '20210909:201647.011874:+0000',
                                                                            '20210909:201647.033584:+0000',
                                                                            '20210909:201647.054088:+0000',
                                                                            '20210909:201647.072186:+0000',
                                                                            '20210909:201647.089126:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƇƻˠҥĈπŽԡʹƆΙǤɟǂӛѽʪӧmƀȏoтԛҬċˎ\x86Ýļ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201647.174771:+0000',
                                                    },
                                    },
                            {
                                        'name': 'İӬĦɦkюϔЖ2ԚѾЕĮԉжб\u0382WɤđЙŞԒӝ¼%ǇˍɒȒ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8648004849417900907,
                                                    },
                                    },
                            {
                                        'name': '\u0378ЫɹƏȊԑ\x8dҡĝϧЂӋğΥȂѱŸʞѾ;ΐȥě¢ȳİîʺУŉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 794982.6504863745,
                                                    },
                                    },
                            {
                                        'name': 'ƻҾϧСŢ˔þçʳԔӾҔ҃ζaðԀӱĭʔɒϯÞхƊϝĊƜ ě',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƷȔȝϔȷҶțπǩ"ЂʲτʠĬʮњԥͿÏѻѕʫÿȄɆɸԊÈ*',
                                                                            'ЍʩғпɎϟϚɍеҝȀGȦ˄ϧČɳ)ӢΨ.{ӫğѩȎʾɁgΩ',
                                                                            'Ɉ˟АƖƠӬ΅ҟ\x89²шЎώƆϞɶåɚѠјɔΊκŪ=ǛĊϸȂϳ',
                                                                            'ǯÃ/϶ͱϑԅšΉӂɑêΚǫÁԆҞԆƔЎɄϝʥώԨéșӯƢË',
                                                                            'ƧϸʝşÖ\u0378Şɧ\x9eėîЯ4ѩȃņ5ӳӻȔŏɣȕɄ\x7fϧȄϖЯК',
                                                                            'ȗ}ØɐӤˠӍϻƻkӏŒӖłŬϡЫëӷqԜĸǾǚɧĲɇȰб¹',
                                                                            'ηͽ×çЬĤˮΓˑȨa\x89ЅԖԄΊȿ\u038dͲ%τͲÝԅғҝ\x9fҗϜſ',
                                                                            'ƠǽėάĮĜɍç-фԬňȇԔϨŊ\x95Ѫͼ˸˻ѼЈӐƻӔӋϛ²ʜ',
                                                                            '/_ӉɾԕǚȫӷˬҳҙѣҠĐѣвBҽņĶr҇ЇſˊŊƅBѧȖ',
                                                                            'ΛÂɆ³[ӈŽñѴʈ#ѕɶȲHgʾűрöèԟʶ¯ȶΖƲźϒҶ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĦжĈþɅ˟Һ-Ͱűи',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6902789231351301469,
                                                                            4121988147226259009,
                                                                            -1760163735904622921,
                                                                            -7984327673587566882,
                                                                            -6400146678985475135,
                                                                            -1464383788927719530,
                                                                            5346238318033745329,
                                                                            4079601884339123305,
                                                                            1002704142437920374,
                                                                            5561455607588982678,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9bǙˀǧ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2033922758585987269,
                                                                            1929597405424124457,
                                                                            3466072738620616870,
                                                                            2467836944154952309,
                                                                            5722736391119818824,
                                                                            5173750991328167394,
                                                                            294746129197188281,
                                                                            -54580270914134235,
                                                                            -923436292009174573,
                                                                            -3899691162819684719,
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

            'identifier': '˻ÆӫӐʐ',

            'categories': [
                'configuration',
            ],

            'messages': [
                {
                    'catalog': 'ƜЧ',
                    'message': 'ǵ',
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
            'name': 'ԧȽːЇҕΫǼӵϙҬɗȠĒȾǯŇŹҞЂоïõѯԪƻɰǝʑϮ˛',
            'error': {
                'identifier': 'ρŝőfϳƍÙ˯ÐϑƸȜȌ˃žλ\x8dpϯːȸńǳɴҒ\x80ƭȳÎŸ',
                'categories': [
                    'file',
                    'file',
                    'file',
                    'invalid-user-action',
                    'invalid-user-action',
                    'os',
                    'configuration',
                    'access-restriction',
                    'internal',
                    'invalid-user-action',
                ],
                'source': 'ѹʋż˴ʖȷàξϜĆvεɈӶ$ӝ\x98҈˳ǡтПѥ˨ŚɄύǍѶэ',
                'messages': [
                    {
                            'catalog': 'ßƲƥɟ¦ӍȮҋбÃŦөǷӳѭ¥όƷäΥҋ?ǥӡАǶ\xadҵҕӡ',
                            'message': 'IҦǓωɵѷǉ\x9d7ˁѥԛҙʱχωIĊҦαԊʺɹƺДΆ΄ӀПː',
                            'arguments': [
                                        {
                                                        'name': 'ȧɪԡԉCЙʲȸѻʛϩʶУŻRŹԆ˦ԅƨœԊōńȾ$ԄųƣѤ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŴͻԁӾҝԢЈѐԐɅřӹɄҥȂøɱƊӝɞѿмнĝ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ų@ΜvҝrƮԠ\xa0.ѕīƐʞϒѰȮƹªиĘԪʉԄρвɾϼʒӑ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8090628625600559343,
                                                                        },
                                                    },
                                        {
                                                        'name': "ȋǥÏũϙў·©\x84ЙԋʲīŘȂӠɀϔω'%ȥҐʶNӊԙЌG\x8b",
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǛЌƃτ\xad˚ӔҔǁΪq³ԞԒ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɓѨǷyҒ~ј˝ҞԦnЫèщǬÓηŅʗǥ˴ԂԜǩ\x7f\x83ѡjԔƛ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ψӠʷ˫Ғ˩ʻˮЈѢҟS}\x8fηҁЇƚſԚŭ҂ΫǋʽˠӋЌəѬ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѿ˖ϋќċIɩ®ҬҝæыԥϦʼ\x97ȯ\x80ѱњýˑԓѪx«ǉҼ~s',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÕʶþóӕʌqљĊϾйͺ\u0381ďɾɕřǢΪҋ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'HóǾǨцКӍӌŻ¤ԙć˵ӶǧǎΜӽҠŐ˫\x88ư6ҥǆʖ˺IЭ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ìø\x87ɮήw`ҰƆȨъÂѶʑȂů0ƽȪЙŪсċюŏјɈ\u0380ðr',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɣͽɿbυѽûâ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': "Ù˗=Ż&\\˳ҲàǛӀ;ƴфсәŕ\x82'½И\x9eѢʋҝϤһǞѰҴ",
                            'message': 'ʣʔB¬M˴ѵіʻŭĢͱ:ҩ\u0382ЉƵàҬƿȷEҵ͵Ҝϗпʹźƙ',
                            'arguments': [
                                        {
                                                        'name': 'ψMƂłūĵƼĚĮ\u0381ЩǔıŒúʋϖŖӦѨϾϦ\u03a2\u03a2˩ëӲеϐƜ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˾ԉǂɅÃӆτɩͺǷ˕ҺҢҢӤɆʐ³ǯǪЉʌӘɯ>ΪԀΟɟU',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĩ!ɾɀʓ°\x98ƾǈ³ʳӨ?Ӯēƀ\x80ʦǬԅ,ЖˎĄԓΟ˹cŁŃ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'EԐϝįɲŤ\x91ͳƽˮȭ҈ʧ?˲Fэȶ;ҏɎ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƝљƀųӅȧŢɗҞňҏɇɲHϝɒ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '¤őɏɃуƿрΧƱȃѱ¡˖ũǏΌƤžϠфӰʻӣѼǨΧώƔĨƊ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɮӢZԉǛÔҿϔWʣʈ¼Ҿţ1чˁьӘ;ЃνÐ-ƄɅĶ\u038bты',
                            'message': 'ӵαȄϒˤǌѻӟЎ°Íĥǝѣ5ɘ҃ͶŚǑɘ4ȦƤ-ˑ҇ȅeН',
                            'arguments': [
                                        {
                                                        'name': '˔',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʔ`ĪǮǉőӫɌӵтύϴ˄',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǆѓԣˤǇǦƭɧȉԧPÌ8ϋ\x81Qǽj',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʲɋш¬щԠđҋƏԇʯЙϱԒɬ`ВȤÑЈ\x87ʁĹЋ\u0382Ҁԓŋ˭Ũ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:201627.328137:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȀɒƵħК¤РɂɂʋľAԎǝΪ\x98ѥ˰ɱȴͳӿʬ5ԣńƣǐòγ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĆTБʴ˧ͽaƯ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԤǤ;¦ҋƮ§ζ˪ѢŢ;ŞʀѬ\u0383˸ť\u038dϾԘԎсɉ3Ļɵѵÿ\\',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 406340.64181173505,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8f҂ê«ɩϛоÎĨnϪҝϴǪʅӦ¹џgє',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӊҾ\x9d¶Ǻԫ)ʒǚÙ¿ùɉѮȂ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1373449165943964021,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȖĲAĝѺɘҴѭ;˧ſȹę\x90˳äƐɜÛʰѮ˷өπǶώ˲ϻº͵',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϻҿȭʢƹ\u03a2ƁʣȫȘ-дĘƺӕƝϗŦíȬƤʏƎΕúw˦ώ˹ρ',
                            'message': '«ăԜПåλΑǦɷ8ħȄ{¹Чɭƃҫ\x7fûЙˇӕɽ;ÌӝχГȍ',
                            'arguments': [
                                        {
                                                        'name': 'τġʦԇƂ˘σҁąӦȉʆŲѝʣΩϒǤ˔Ӳьːʌ\u0382ӖϴΩªƧȼ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '´ӗќċȥ¿ΆјơȺҗ˾\x80ϪǝѯӺř˅ԎԆʠmŒ>%ӋôηҰ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6875487020199880360,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɠ6ĂΟçʡΐ¡Ɂ˖ЎϖӾ\x9bɆXĻÏĭNȊƯMӐșĿҹӊt˰',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 118938.11873848998,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӷßd,ˌʴс\x8eʵřΉĈͼ˪ҫԙѷ҈ĽǶΝА\x9d˼Ǧԝσ\x9bňБ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 612452.7867666236,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɕĖRôʱPӿԎ2Ź˓¤ɊR',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǝ\x8fp',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:201628.212323:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϩ¢ƠɥʦŊþӨϦʬʲ˱',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': "'ԍȔˁ\x8eÇѲƖûԐϕɕ4ԡμѩ",
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӯԜ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȱþ˦ɃΝўùϟY˔¨ϸѕѣƗēΕЁҥЮӹȰӎǍȐӚƷŋ˦W',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 9778.82555001002,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': "Åƺѝę҆ƙďӌˎȘѮԄϹДǶЄsÜǩ\x95ѭʭǾʜǨәÅИӱ'",
                            'message': 'ɊɦΣƢʼѓԘϡʝǟɳӫĝγǙӔćʶϲԮƞ¨Ǩˑėʅұˢ˸Õ',
                            'arguments': [
                                        {
                                                        'name': 'ǀİƻΆ±ϩзˉԀì¦ϰ\x87ąƌǉӛ$Ҡ¨ϞĹéÊЉŸʊȿƦԔ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'TϚĆƂҏə»\x8fɿ\\ƀȍÇñʰ\x88ԆЛʠBƀӱȦĎӁɲÐɾýǸ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Γ\x80ǘϜΪǮϳőƆ\x87ѾВќ˖ȫƆƚ˻\u0381Иʢƹ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ђ˂ĽɆċɀ1ұǍɠ˵e˳ʺǝүԎԑГȵΕʹ˳',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3686712597920570181,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѮƗǟΊŌBЙϋΈʎƬǁƈԢÂ¾ȒǤюИXǽʘγͼѣ϶ʒ˚ő',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ыÖƲųXªύԭČhҢƉʭЙгxύΤ˷ϜΞĪ\x92ɄƋgфpѣΠ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Хƶ7ŪɎăт˞ѐ³Ļ\x95ԅʻ>ʛʯňØԤɁǩÉʜԁѥҽӀÎT',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΆȻпϑҙǎÚŲԟŹŚƙǔ®ώ×pόǙϾԨњȾаҟhřԪҟі',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8eά',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҜȢҤɱԟĺŪ҇ȊюӻĿǬǾ4\x82ΚˀȃԋȭʝþϠƞĦԇԎΔ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǉxĕͲĶЅȤԫɇԍЈňʁҭɪʧřϋÙӾ˛ɩÂӛȦ˼ůӪ˴©',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʎʁюıĽćɄұ\x90˵ȎəƀίөÙǠġŨēʞ˙ʆлҴсĮ÷èϷ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƛ\x9aѻͻǭßˀƺŬЎʼӢɻĺpʻˣϗɺΛ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӢԖŃʢϓʵɁьЪԏhχƚú³ʈgĥѮϦǁªʋѷƀöӴ¶ƿҸ',
                            'message': '\x8a]ҼӟʍҲȤKϽȢ\x7fԏħƽѿϜĈʓÞњǗʺЧűϧ϶d\xa0ʛı',
                            'arguments': [
                                        {
                                                        'name': 'υǈ˩ąӮ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ŷѵʽǉԛϭB¦Ιȇ¿GǱɕ'вƣƳČϥӵ:ҽKӋѼɢåƒΘ",
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:201629.475025:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'χπBӝ\x8bǇҏГƑԆҳčԇϤȗȆОϺˁɽьÑǃȗƦδ˵ҭНȶ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:201629.544243:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ļ!ɐ˲їϹɑύɖùŤұѣªєԥ\x8a҃ԠŗӴШӫ(ØϘú˓ɰț',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǵďŘǙŊŵЏҗŊ\u0383ϱӽōRеƣyҠĸѤǫɻŽɬxƣʀІͷԧ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 219132.61356114462,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȸîт˨ұƃaʙżʧˎӵȩŎ±¬\x8eЏʔϐ¯ԩЖĕҞ_èЍȽӵ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŃКoéŀΏʴԙϲǹ͵ϕȔғűӏЄƹГȣʐŹΆ\u03a2˶ĿȏӺ˩Ѝ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƊʰËȜ\x8fŪǌ\x82˵&ǫμʧʧĬӱƤǑʥ°ԨӽΧɫYȗõØġ˹',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǯӚƲǅӽҏ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '[ēҖņΆȱ^ƾÙ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɇiԑѴǐGŋωƆÊж&ŔśrυҍÔϗˮӭ\x89',
                            'message': '˔ÐŀӍĥϒӚϥϛȋʴʫƚʝǙӵЎ˒ǅħ¢ů8˽їīŊʰĎƮ',
                            'arguments': [
                                        {
                                                        'name': 'ȠϘ«·ʷˋĄқĘ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѕɶɛџ˹ǮƋԉԧįƿŦЗȿӲBųїȒӆӑśʯӍɃϷǕȯʆЙ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038dŐƹƙαĕòЫˇ%Ҁʂёԗäјȿˠ°ãȱәθņҿ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʋΖş',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŪȵΧȑ[ǵĴӔѴʺ¼ʐ˯ͱǶµήˍ²Ѿ΄ҐȇǡìЫȜѕǆΏ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 772435.2644893851,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʚӽñà˹θΝƓӲʑɸÏϸХȵ±Ϻ1ɒǮȦÅ¹',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȁ҄Ǐ˟Ɩʊб',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '¥ŏӐíůêCŗňĶҒМʛǿɄқÏZɿкϰǝȹ~ŌόʬŀͲȠ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǹԟɎŭɪҔϡӒɺ˧ïɘǒˬԮѱ\u03a2ӍσҙŊĠƪήӟүĿǼΆĀ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŬɝԥčњɌʒŖǟѿҲɖƝěƥǒҨȝԐЕƹȔõ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŞJǊĵʝҫҸȦ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѓɈÞɍʛҢˉͰԕӁƴϵʪѦͱŬҘh˟ȡȇИĤͺžȘȠЗ`ӕ',
                            'message': 'ͻcʻԞԍXćȽmңȤηɝϸΌĝǉɰϴϊ±ƊĮӄˋŏ¤Ͷӯɉ',
                            'arguments': [
                                        {
                                                        'name': 'ϋԦàʒÖӋƹҕӜʣ¹ЧͰĉҭ$˔ǜϰȜȪҭ\u0381ӯ4ð˾ŭå\x9b',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Șø`ˏƄȝ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:201631.053602:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˀ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:201631.120801:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ğÝüΘћŒȓЏЀȝϸϷPäȾхōţ6қΫͳŽɬȢzү',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˲',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӑβǂ8ǫӬ˃ϬΣŅĦǐчȔҢÂƤˣΜρ<ǪŞʗϞƮƃχѠɃ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'МѝԅƑ_ԙαʓɋһԒҘΦɋ\x8fһҤʹ\x91Ɣ\x86?ìԥɓԜɗУěț',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x86ΝĜӪǄƵ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'КβаИƞӥХ?ДӢЫë&˞ǸͲņ£ԂɅ\x9aлÎАēѕȞʭκɇ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȰȨÿҞǝИҝŨʴϫӭǤöŷ˹õ˖ÙÊԧҼΊŚҵõ\\ƫ¬јƛ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -9080034430709298717,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͶҦćɉˮß˵ѦdԠγŵӿԔhMͲӟ-ԫӚìѺëɉϑŘKӅŉ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '9ьҔ\x93ʏϹѥΆƵįǟšÇɐӶˎûƙ¢ʢȭˇŲʭĐ¡ϕŻɈϯ',
                            'message': 'Ǟɦ˚Κ¤ҭʈ¤ΩʙǞ<ΚúĹǽσqȾyɫɣӱЗʄ^˽ɭď.',
                            'arguments': [
                                        {
                                                        'name': '\x8cͻɇʗġÏt\\Ȅ˞ȵƵ*ǤԒEˡϣĀ\x92ƢiǥϏƹǼӠȌϒu',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 104075.814707109,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ňˆΒлѯ˚Ώӿб\xa0ϲæǹҲΊЀҰΚʮ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǗЦǹ˟ΗԩдϿƿҗ\x91ЯӖηԔ˯yǝәԀ϶ˤЏӅI\u03a2\u0381mЍʞ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǊčоëԅͱË',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'δȲҝҐŒ}ϢʹĈϗɦò·К`А3ğԡ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʚԞӿΉɔɄİĂȀԍōʝԔǪϸJ\x80śγƓ˵',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'șʾ˧ǠѓˌŒҕTǂјPx\u038bԖȝϗҧлƾΎԤӥƀїƊԏ_˘у',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƕîƗЕǕҰ3Δ-Ҙ\x8aƖΟɟǹǇ\u0383Ƕ\x8bӝĵŃɎŢ҇ƧǂþϺy',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÖǓ\u0383Ӿēȡɾʸšδ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǵβ҇ˬïτō,ɂŦɃӋƿ\x85ñұ]Ͽɱ\\\x82ҤŷʻѮŗÁ˃Ђʯ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϕȌʗˆΒʀҒmӃʆʂԎЪӼѾЋфӀ\x9eŋЧ\x92zĂλу\x84ȫɏɃ',
                            'message': 'ʻˏˣЂБĐϜńΕȿǫŴ·ξɘ\\Φԃȓѕц҈Ύƨ˼ʇђųԍ˫',
                            'arguments': [
                                        {
                                                        'name': 'ʣӥKԉ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210909:201632.505798:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'irϰ\x86;λĄ,ȜǬгЙzɠϊǍɃҩŐŉɺЯиʪʺǠńɭҐƅ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʰʭòKϟ3¯ÀӬЉƱ@ѾǩƌŷҳήӂǺϹ¨ӎȝˡΨǾϗ£ӈ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3641892498505144039,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȦȐǡǡĤԎҀĔβԛÐҙåЫȢȲȺɪ\xadяΒΕƐʵ\x9cÐОΉ˭Ő',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϗǥӄђʁҿЬѺˠкΜх-ȅϔ\xadɧÖҎ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x81ʐŏƧɱЁ8ҚĄїſƺЍǤю˦λԂʑ˟˵°ƫˈ\x88ëȇUǍʇ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƫϝπϤVĜʑÇƺųΝȖЌϠÜŖÃɅ˕´ŵѱņω',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԕӅþǌ\x85˽Λȟɕfȍ\xa0ϒ\x82ɆИĐī\x84ȤƽϢǗ¨Ԛ΄ćɩôз',
                                                                        },
                                                    },
                                        {
                                                        'name': '¶ҜϨҊưÞi',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7068097365465826763,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x81ПñſӨpƟȗ\x9bĀфɩ0ωҒ¯ϋԏː\u0378ΖņΓŎ˹ʜá˨Ͽú',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1787247126281712483,
                                                                        },
                                                    },
                                        {
                                                        'name': '˾Φ]ƀʲϹƢԝƵRȯΑЊ´ˠ\x94˼˕ɚΑñґѱȞ',
                                                        'value': {
                                                                            '^': 'float_list',
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

            'name': 'ŊΣǗ',

            'error': {
                'identifier': 'ŦӡӶƄй',
                'categories': [
                    'configuration',
                ],
                'messages': [
                    {
                            'catalog': 'ƫƿ',
                            'message': '~',
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
            'name': 'јάшRƛɸЂČĦàřQțсӞђŵƉӈЦҲҹÁÓƖΡǗͲƈ˲',
            'version': [
                -5664712353297855680,
                -3131274425645050485,
                -3268762416552159859,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӱʿǦ',

            'version': [
                -2698340289794208940,
                -4015751231825714854,
                -6662094364284736641,
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
            'event_id': '\x8f.҃öłϗÖÃ\x9eџī0Ԉȟ¨~\x8bǮ˝ǽĿƜȰԇОԋ³Ԣłɬ',
            'target_id': 'Ǝδ\x95χҪ8ʘƟ)ʙ\x9a˶˄ŖɕɩɲƜŶЭ\x92öȀɭ"\x84ǽɺѓé',
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
                    'event_id': 'ΐCˇϺƓѸlƱΊͼ63ϣƱƾĖāΙĕ\x96ĀԁˠʽɤɴkĖƥщ',
                    'target_id': 'ќѠԁƎӏмSOʢҐĸ%ӾҨOĐЕʃȑΠʈʾ\x9eǨǹНĲʻϱέ',
                },
                {
                    'event_id': 'ªĎʽRщȄҖѭ˺ÔΧǢΞҗɐ8ǹ\x91ƨζԣΫǻŹŏʚǂþΙɖ',
                    'target_id': 'ɞ¨ɪЫůʿŹɃYłŀηtӫͶө\x95ΒɈƗqԧȳӃϟαӟƭϑύ',
                },
                {
                    'event_id': 'гԜΜӐĳ\u0382ǽʔČɽŸѦoʔТɷҬęŠsѧŤϹʡơĳ\x97²˃Ё',
                    'target_id': 'Ήʓ6\x9eɮƁeɏԊŹɤțɽSĄχʾтЛǯѾ~\x9cĭǆê-Pſѳ',
                },
                {
                    'event_id': 'ũɢƵχȐѨ˖\x93Ɂнï͵ҹзǳ>mѶϬԉӠʔƮѝɡӓ˽ъÛǉ',
                    'target_id': 'οƣУŘǽфˇ\u0382ǘɕşLɄϋ¿ɸȑǄ[đȤҔ4ʬ\x89Ͳȉ\u0378҄ɓ',
                },
                {
                    'event_id': '΅ļ±яѧӧ\x80\u0379ĴôƐԕѥδ˃\x8dϣz҈œȼңǶʴɃƑάǄГJ',
                    'target_id': 'әԎȫȀ˻Μ\x8dƀňȾŴԒюӷŢrѧҔϬѲŒˑԅ҇țйiζѢϫ',
                },
                {
                    'event_id': '˩ǈŋˡЎξ½÷ԧ˱ùzΦäɔŷϘǄϯǞŧ|ώŠĊŗʕë\x9bŠ',
                    'target_id': 'ϐлg²ɓżϣÁΏñƐȷΈЦùŦÖѬ\x83\\4ʼ\x9e\u03a2ԪѯЇǤԂӅ',
                },
                {
                    'event_id': 'ƫC®ЙɡџȣԗȈыÚ/ț˄ǉVʠʕЙƑsԚϣϝӰgǫlǈʙ',
                    'target_id': 'ͽľњɗƅˁƾ´êǑζę˴ÅęŒȰ϶ǘѰ\u0378ФԧɿѳӪ;ǝ(Ҫ',
                },
                {
                    'event_id': 'ʫӅ¡ќ6ʣɿϞҩʯ\x84ҍƌΛϛ¦҆gѴԦцɲʷѶũŇğӜ҈Ă',
                    'target_id': 'ĖȍӯÓŒҠɑzÕεșǺƇ\x92ΖɫԓҴϕΥЊĥҭɩ҃ԃʫĊ\x85ɝ',
                },
                {
                    'event_id': 'ćǊ©ĀӍȅȤũŊg\x99Ĳǆѐ\x90Ƕέǩ\x875Ӕ\x84@ȿ·˵ĀԊŵʑ',
                    'target_id': 'ůΒӷϢƲǌΑɧ\x9cЁƙ9ɛ·wƳȭʑɀΛш˝ƒƦӏѸʯēŷǻ',
                },
                {
                    'event_id': 'źϫȚԟāMȐǯːƲӬɥѠϨƮ×ӫʁģҫήȯƴʗʒҍĽȜĨϢ',
                    'target_id': 'ȄЍΑɌYǞʚӔƀ˳ͷΡͻȺĠóҫϥɏ{ƝƼԩaΉ΄;ƀ\x82ʇ',
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
                    'event_id': 'ǭϵӖБĸðɀʫȋɦԞÙӨĮ\x9e¢ȕʇ˘ê\x94μʛФǰӰԤÛϝĞ',
                    'target_id': 'ĔșЊÂˬЀ×]Éőɪҙɗɠ÷ŵԂǝɆĖ@Ў\u03809ԐӋϊӨ˴Һ',
                },
                {
                    'event_id': '˴ƑØΝƳσǼьƘȽûӏИPάǷѧǷӅTҪűŉѧŚ[@űϾλ',
                    'target_id': 'гʸϔȺĖƿѤҟΘőѿĬ+ңƓˁ©ѼɢˁиÿйѓIȑ҈cҜћ',
                },
                {
                    'event_id': 'ŠʿħÌаȏϫƀŝƓɻΎȎӀŘӮǳ҃ȪȋлÆу0÷Ǵ\x95кԥÒ',
                    'target_id': 'ƕԧЏԟ\x84ɣȷĝů\x89ȏgŘ2ӉˑчȆŢÛj˚ËĎбN\x8dƌѮǇ',
                },
                {
                    'event_id': 'XɲʆƓȸʋďƴԕƧќĤηϷƅʄʷҐҁѧϦІāɃťÅήӺѶΖ',
                    'target_id': 'yҁīrѧ˂ӿǙĀΚԙȗîόŸɹϡοЁ\x9bƤřȿ˥ɑ\x95ɸϦʩʵ',
                },
                {
                    'event_id': 'ŮһȚÚ҄ȞþĉҴ˾˹˶ŧʝɹǥӇŎƱ\u0379ԤãʥҦǃΖ͵ĻĕԢ',
                    'target_id': '´±ǋЀ\x81ǞȞϗʖӾǷЫʮɃȯȋɅӨ\x9bǳǪʄɆÖѭɖÞǞĮϫ',
                },
                {
                    'event_id': 'έά\x95ȻʊěʹϔĞ\x99C\x92EÜĊϑҡѯХԋēȡЕɸc\x8dƈԥуҦ',
                    'target_id': '?ʇɭɡʒΌ҃ԨıɴϦʷĕϑӿƞӱсиДÙƣԀ\x84ǥʉłǈΜ\x93',
                },
                {
                    'event_id': '˪Ĕ$ƦР˛ҒȥҀȥ®Ԑp˙ѵΞ˧ʑΐьгԂԬԠĳµƲͷʞǡ',
                    'target_id': 'ԃӰÚŗԞɂĵǓмØÏ҆ȖˊӂȼѼ*҈ǀѴǻѹȢɵʦѰѐȆΞ',
                },
                {
                    'event_id': 'ŃƜϼή˔ŻҘÇǰǤ+ͺҨ\u0381Ŝ9',
                    'target_id': 'ηΗЇǋˁ˒\x96ҴӜʱɣȾˍӴ\x9aǒǤǠԖϿчЛӰʁ\x94ӎ«Āѥŭ',
                },
                {
                    'event_id': '\u038dϵƨ҆ѽͽʅʟѶШЗрʌ˓ʫȔÌ˒ˊɇƚŽʜƦԥĦǞĀ;ƀ',
                    'target_id': '\x93ϞѡԮğѴәʥʪӦģЖιжͲ\u0378ʨǳʛƴΧüԅū\x92ǑӦгΪó',
                },
                {
                    'event_id': '2њÅͽυҢʱʣȌѾƷȑβ£ΡƲϠӆ$˵ƧZȲȺȒ°\xad\xadќɘ',
                    'target_id': 'ȈqӨЮώԥԭѯΜӢϺȀφȊϟӏƁόΧŲưƿϘљuÎʕȵѿϪ',
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
