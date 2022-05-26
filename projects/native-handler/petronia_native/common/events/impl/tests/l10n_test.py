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
            'locale_code': 'ѾЭˆʁ',
            'catalog_name': 'œӨ˘ȕǓΆ!\u0383 Ŵè\x8bҹOƗ˙ҷċ΅ѩŮǭмΑɢ%:ǁŜʙ',
            'message_file': 'Ӻ¼ɿŹłщ˂ТƮзԤŨňƚƙǶƾѕ«ϯ\x8dӛҗԞÈȃ\x85ϭūĲ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ӆ',

            'catalog_name': 'ĉǊԑ',

            'message_file': 'ľƔ',

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
            '$': 'э˲ӖİɨʋϷíǡĴIȈß?˕tψȓ$zґʨВΜΌЭѣӾԞȄ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -8646240470734482574,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 93880.28783123766,
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
            '$': '20220526:211750.082694:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'бFϞIТҟȁЍҙďÉѷѹѭǡɛĖfʿͺ˦ȨƕƔҖҰKyЗɥ',
                'ŦѮÅϘPѾ˷o2ҰOЧҠǳҩǄIśӋȅȟυýɛϙҼÒyʸ|',
                'ͽяӌɡΩʶ¨ùөαȎŔӡǔɸ˭ŠĉȱɫϾǏԠАǽɝƘǮ³Ǿ',
                'ňǲÖ\xa0w)ĢԥɥʩƾεЖȯŌȀρ|ϮλĘǣaƖMmȚӖŹȋ',
                'ҿɗĳõ¢őҙÝUήБӹӅδȢϑҖ˺ʋɄĉήӣǂΈӯɲ˙Ȍ҇',
                'Ҝƍ˴ʅчљғąɴĮԙƖäђЕɟθӼƟŵÙ\x90þғĚªϹǊ@ˠ',
                'үѭˣҨӹȦҗ\u038dҪ³Ѷʩˈ(ʡʇ°ӊšοvʈӵ\x96ʁώΨѳȨ4',
                'eα\x80¼ŠӔѲѷѝȠԌɻˎӾӡɌ˯Öyʐt˶ć\u0380Kʣьȟa0',
                'ʝǾLūάӿίƁψπǚűɴƤ҄эƱͻoDǎȧʛD˰\u0378ľħĸҏ',
                'ɣʮoňЩšȒÇuɛʤΝǙȕԑÑßŕʃϽȉŠȲʆДǾˡĺʳƠ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                640552034195393323,
                2824578999461941476,
                7478420563625191929,
                1271330956405705424,
                -4896805500755587043,
                -1129644588572945317,
                3712809297875414040,
                2073237800671530053,
                8523842060084982138,
                -3598403631357504892,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                748445.8847076511,
                177892.1148595857,
                772994.1075247807,
                481770.2234649088,
                835955.1351992666,
                520927.562708557,
                369194.70628494245,
                405058.851713073,
                810835.5461393872,
                178059.38731672463,
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
                True,
                True,
                True,
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
                '20220526:211751.008687:+0000',
                '20220526:211751.025446:+0000',
                '20220526:211751.041779:+0000',
                '20220526:211751.058800:+0000',
                '20220526:211751.075933:+0000',
                '20220526:211751.092664:+0000',
                '20220526:211751.109845:+0000',
                '20220526:211751.126557:+0000',
                '20220526:211751.142946:+0000',
                '20220526:211751.159636:+0000',
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
            'name': 'ўŌȖ˧΅ɣ',
            'value': {
                '^': 'string_list',
                '$': [
                    'ͼɛрңƙϺʊΒȡŌĳɻЀӚVӶʩɖʁǆ\x84S£ʸ\u0380žѴǢÑǉ',
                    'ОƱİͽuϴҟĿĜ\xadƖȓҎΫşЗȄŁņӾĬҠђőtōʤмɥȊ',
                    'ěƸВѢʮÏʯăƾƓяɃϒǕƺӋʡ\x91пtю˹ѦθțāÆ]\x8aҰ',
                    'ӟÍoГǼԩșv\u0378ʜƮǙȣČԄƠČ¯˼ԩ˹ŴŲ˻ʺƳƂѺ˥ϋ',
                    'őГæ˙ԓԧˌҕȳˍ΄ӛůϑӕϸǝběвł҂ΩйĦҮȓԋҹ˰',
                    'ʙPĥȊѸĨƭɤÁʮǣÓǐĖțк,ϝNĽћŃźÙ˪ʛƩӨԊч',
                    'ɴҫҪɭ«ѸѮ\x89ȳʥĄ]j¾ÐɖöξʃЌϺÊι˅\x83эÆŌ͵ͱ',
                    'ǧħϑ\x85ň\x81ÇѴͽѳźϊҨӥɊʎ϶ŃҶȾќì˪ΥдџΈͶʹǇ',
                    'ԫŸƸñĞȌǸζӃѠǖǎǮʅӞҮ§ϾôζǏʠɅˏš˕рǨĐɜ',
                    'ӑƶҷÊɆҾϿйƭǀǡ˲\u03a2ʕĂǽʺÔЉʲǱÏʢԄѣĦΕíǥΕ',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '¬',

            'value': {
                '^': 'int',
                '$': 2325577969887959802,
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
            'catalog': "ƵĨΩ©ǱźĲǭ'6ԉҮʈԕΕȩЖƭ4]ęɒMόɑ\x9cώЊɋƀ",
            'message': '\x9aʄԙǓԨɆƗg±ӨĂΨǦē˪Ϗ˲ěƀ5½ǂ˾˸ƞ3TCӸɭ',
            'arguments': [
                {
                    'name': 'ԮʘϢºѯ¾ʒüͳώȁϤǮдÔ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -1025151034855046143,
                                        3257070826279618753,
                                        -4067864916473189241,
                                        2898520072420388266,
                                        9083320474229271992,
                                        -1109995760643390251,
                                        132033955803531815,
                                        -1188122743411849325,
                                        1919345966434507786,
                                        -1409423303453951834,
                                    ],
                        },
                },
                {
                    'name': 'OʞңϹБƹʀǒƽŗѨХƘŐԟȭѳkɻƃ\x98²T§˚ɲ¢ĉõȖ',
                    'value': {
                            '^': 'int',
                            '$': 3563576000557577149,
                        },
                },
                {
                    'name': 'ʟʃҌι',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'Ƅª®ʲιţɄɘˬӜdɧќ дȘϤβ\x96κʿĭИŚ>/ӸƁс\x86',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -3282912946634446677,
                                        -7786873963136398188,
                                        5820179903369119486,
                                        7278553975126054943,
                                        758302490981560787,
                                        -1564920328798605158,
                                        5239590148870615678,
                                        1170668045571403325,
                                        4352102470420388696,
                                        4495924770879345174,
                                    ],
                        },
                },
                {
                    'name': 'αʨǀɿLҋ',
                    'value': {
                            '^': 'string',
                            '$': 'ϾÕɲ\x8bŶĤ˓Ɉʌ®ӬӕɣƶϓþӏFѬöԄсă#Ԯɳ\u0380˾Ѧʬ',
                        },
                },
                {
                    'name': 'Ӣɧ²һƳҐãΈo\x8fԐ²ɭϑӴÐɝ˩ƇņπȔǜРȞ@ƉʩÄ»',
                    'value': {
                            '^': 'string',
                            '$': 'кѦȔĭĘŨԘ¦ʭ\xadԝξΆԚѕËĐҫʽ7ȐˣԓԂЗӯȩ.Ǘȴ',
                        },
                },
                {
                    'name': 'Ϝ/ƂӦϓԥѴ˾ЎŇϴɎɿԮ/ŔîλԙʉǓҜ',
                    'value': {
                            '^': 'string',
                            '$': 'ȵрщWǶǾК-ʣΟрñɖδĮΩĺĖ\x91ÞǦǁŌͶԠҕӟӢʭĹ',
                        },
                },
                {
                    'name': 'ҧȧѹяЮą',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ĸ»ĐɢӓƸχĈїä\x89ɐԞĵ҆бÁӌVǘșŘөͳʰУĉӴĬΞ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        436310369437447474,
                                        -7679330579335191696,
                                        4172750649210044301,
                                        -8541971119582957926,
                                        -1900914035358601986,
                                        2442122645507951457,
                                        -8259013751048843024,
                                        -6949240931803731194,
                                        5921712955707406364,
                                        1616596986548098402,
                                    ],
                        },
                },
                {
                    'name': 'ΩʍΖäŎăԜƂˮώȝˡ.Ӧĕư´İɮͼB?z\x90œĮ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220526:211749.483252:+0000',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': '[\u0383',

            'message': 'Ӆ',

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
            'identifier': 'εţ·ϻͰɝе\x97ȺǍˍǊϦх«\x96>\xadӈʄÍүы˞Ӳ5Ɩΐ[$',
            'categories': [
                'invalid-user-action',
            ],
            'source': 'ҠɈԘǮӘҫÉʩʎɷƕǀÕӱђƨɥŒĮ˶ʬԉȊǤ¬NɼƼЩƚ',
            'corrective_action': {
                'catalog': '˝ϫӦԙ\u0378ɜЗ˫ԇ˔ǩП¹Ɉf\u0379ÝԥƆ҂UɜУŨǱŔџЫ\x8fÐ',
                'message': 'ʅħѢЁžә˂łˁȬˠģӹȠɴӗŴǣЯʟ˯´˭ǄϯĪρʿıʔ',
                'arguments': [
                    {
                            'name': 'ē¸ɮТʓƭʈɛǮφʍƽÚƲЧŨυˋЇТБƕΒԋ\x9b΄V˄ϰЪ',
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
                                                        True,
                                                        False,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ŉɵŔɣеˋҾ˾ȧϿfƠ\x8bλȹ\x86ȑҖϪ¦яϿҕӈSÐ',
                            'value': {
                                        '^': 'string',
                                        '$': '±ӁȅVӤŊɘсʵĳϿϯkĊʬɡ\x91ЖƉѦ\x9fӄȲҊʉŅGɄÑȤ',
                                    },
                        },
                    {
                            'name': 'ʢŤǶћѻǨΫ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ЍȆŷɧάəɂȥsԬЖɖҖũƠʰň҇ѩđǬӾˠл¹ρdİʿƶ',
                                                        'ȓŇуӄɺŷŌɝǯӧcӻʣk\x8fǝҪΥԦͼɜĪùʷƧ\u038dͽҧĒd',
                                                        'ťДʒєѓǺˎǻqӁ#ŨǼgòeaĢҎȼŮДǞоñԨшɔΐѻ',
                                                        'Ќ\x87ρ§ɠʷɐӔϊЪƭΰĠˬĬ˼ɰʩɏӹǾӁӱͷaԌVƉύő',
                                                        'ĺ\x96˰ÀŴХšԛЯˁӞĭ\x9aŜȨǛΩҩ·щЦ¸ăǛһĹåəϢȎ',
                                                        'Į½σʌ`ŎĘĲɊӚðϫ˟іәPɄΡϩʉһϐӼKȢWɢéЪØ',
                                                        'ŀǼ¿ʾĘľÊѷɢφäюcԞɶϾɔϏǩéҶ҅ѢӶϏԚԓϩЉΛ',
                                                        'ƧˢƍԃѕʢėҟŖ²ɻƑӝάʉÚˊȼ§ҐŚǸϟҝƁĺʽǛǳҕ',
                                                        'ŔÛpβͳüøæӨϫĩԋӀʠяӦɒǮĸˏͶѐiƹ9\x86)ɭͿѧ',
                                                        'ȩ˟Îˎ]ŎǜƮѤɏ˙¹ŏӇȫ¸Ύ˾ʊΏ˪Κɕiʸ6˛ҋ˨Ҷ',
                                                    ],
                                    },
                        },
                    {
                            'name': '\x89ϣƐҧþō\x8dҨ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220526:211747.144705:+0000',
                                                        '20220526:211747.161240:+0000',
                                                        '20220526:211747.177938:+0000',
                                                        '20220526:211747.197225:+0000',
                                                        '20220526:211747.213765:+0000',
                                                        '20220526:211747.230588:+0000',
                                                        '20220526:211747.249010:+0000',
                                                        '20220526:211747.266911:+0000',
                                                        '20220526:211747.284485:+0000',
                                                        '20220526:211747.300940:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ԉƂӑχ6Ԟ\x8dɭnȧԊǸϋά҇(¶ʦӅɛöűǧƂ+ӳӲiͳ\x81',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ɱƏ',
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
                                                        False,
                                                        True,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ϴ`KşԙЮ´ϏӾƕҫԑΟӶѧĻhψļЦȡДЏȓ',
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
                                                        False,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǵԀƛʍ4ƵEȵұԗťԂĽęēѾè˹Ȯ˫ǇæӈћĊҐǺEіŎ',
                            'value': {
                                        '^': 'int',
                                        '$': 8055808845232997023,
                                    },
                        },
                    {
                            'name': 'ƙ7Ĥɑy˨ĺԠԣώʄâԁҭϺGƂsԒƿȊˏΜƹȝ',
                            'value': {
                                        '^': 'string',
                                        '$': 'Ƈūѭ`ҞŦǶųƧÈЙӁѮԤ;ʔ°ɸǵʨʃξ˩ѫԆ7ˌəԥǗ',
                                    },
                        },
                    {
                            'name': 'ԖϮԧӈΡΛѩѝϢǈԛʡЉӻɝĄӔǮӲȀ5¦ʦӥыҫƫɡƛη',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220526:211748.096528:+0000',
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ДʀӱԀϱǮϪ±ȡϵĴӺòæ¨ɺѹĤ+ːÃʑȿДŘуσŎ\x93ʆ',
                'message': 'βĕѲхƿҗϚĝ˞ù˙ƦϵΉʸϴ\\Ɛȟoɑŝħǋ˽ŇΪӗў˱',
                'arguments': [
                    {
                            'name': 'ȈѵɲӔE\u03a2ӥôȳОӈϾԃŐÏ\x9b"ΧΪϥɄӮƦɵɍ˲\x88Ѽίr',
                            'value': {
                                        '^': 'int',
                                        '$': -7729299612954386687,
                                    },
                        },
                    {
                            'name': 'ˮԜŦҎǔȫʙʗ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ŒˉяȭĜȥΦ˸Îе˓ʺзɈÑȁ˴ËƦŸ΅˥ȡ£ԃͻҙқѥʽ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'R˔ͺĉƭƛǧųϒǞ2Ƥʩ¼ІˮʡϟƂċȰ.Ĵ\u0383Ū',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        397302.1692021561,
                                                        325077.60210415436,
                                                        281213.543446868,
                                                        619545.0380242899,
                                                        541312.0268516415,
                                                        721693.5727282229,
                                                        719301.3393256622,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ɚʉǱØąϦʽɹБǴɺɫͷʩŔтΠĲŝ%Ďʺ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ΥѲȱˍȮʭwӮ¤º\x91˧ĽџЃȐĦж\u0382ɋV¥ȦĕʈϱSͺкƚ',
                                    },
                        },
                    {
                            'name': 'ɿ\x88Ϡό˱ñӬvȖȩЃҶʯǁÀȼSȦѲϓ͵ΥѡɊʦ>ҕӠȔʖ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'xi϶9ԚʋDƬԍ_ˈĭ|\x83ȨͱȅËöϻ\x9eШěҫҒʉΉeϹ˼',
                                                        'ƒŎЄӏ=ķƦˡĎщʕˢɡǘ5ɦʩԕ˸ϑʽҥҪ»ɸԢĕ҂ťҁ',
                                                        'ΫEŽʠ˭ɓȰĊqϠȳ΅͵ɜϋЪ\x91şǠǰĤӁʴĀřƏƞ\x88ˀd',
                                                        'ĝԩǝȑȣЂůȀȦңʎЈƢπфȔǧѓԅяϧӾʓŞȮy#ӶɀÖ',
                                                        'qφĤȸϼͼʸƥѽ҉ѓɫíӳʤϳɱƚӷΟȜϪ˃ϞԣтƣoĂʏ',
                                                        'ŝҒӚȦȾ˷ϼąƸҌĨσˣ\x9fľʳУǓ0ƫȩї;ƫӠϱЂҙΎŏ',
                                                        '҉ҺŨЋ˗ɜĝǋѢǈ\x8bʬ+ѽª\u0380Ɣ\x8bĬƗѼӉмȇʭȏ\u0379ĥƅ˥',
                                                        "Ň$ÚˬĸёȡΚXcÕ'ǬӉğϷèϛƊΡǆѽǠˋĲ\xa0ӈОşë",
                                                        'ϬӦǟƴȥл«ůÐûƍƘѶ®϶ȌӈŋшˮĦƺӧʰȒżɜӖÜʉ',
                                                        'Ӳ˱ӛΌԔѩԩưϰȜɭɠɨҘԌͽƘĤʟЦ\x8eȯЛɂԐӯÃʩƈǑ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ŵʚǘʱϰҾòģǈɿЭΖǄƅδҖϷʇȿԉ.ÔËȝ\x7fͰ\x8d',
                            'value': {
                                        '^': 'int',
                                        '$': -5903496125849935366,
                                    },
                        },
                    {
                            'name': 'ʿǜѤцАҪɴԤ\x93ò˾\x82ðҨӭ°ӿ˕˭',
                            'value': {
                                        '^': 'float',
                                        '$': -53844.75246380906,
                                    },
                        },
                    {
                            'name': '˃εԤȥʞźüŇԍӖɜˣԘʝҗŭИœȠƀ˹\u0383ѠʴԜǯ\x96ӤuF',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -6201633185549682986,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӑϠwɻɜʶĀГǺɬ¹Ɲ¢ʬȜъ',
                            'value': {
                                        '^': 'float',
                                        '$': 557247.640940353,
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'xѰĴʜķ',

            'categories': [
                'file',
            ],

            'error_message': {
                'catalog': 'Ҙ˶',
                'message': 'ι',
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
                'identifier': 'ǁ\u0381˷ȷȻŲů[ŀҘǷȜΗƷ˸˚Еç/һѧʙϙЇȢѧ\x8fЖĺ\x8e',
                'categories': [
                    'access-restriction',
                    'internal',
                    'os',
                    'file',
                    'network',
                    'network',
                    'access-restriction',
                    'network',
                    'os',
                    'os',
                ],
                'source': 'ʽӓ©έЎŊĹÌGɗȗŇʹЮΓsҘѤƐĭǾͽȘɾʧԣĹрԃś',
                'corrective_action': {
                    'catalog': 'ǭƩëŭ˺ʱƎʱЧт\x95ʕʩҋѻ@ԧѴ%ȥαūԄǕǠýƠƀ˝Ч',
                    'message': 'Ґ|®ÆǘĘǩӓǽəφÚɉѭʆљǱ·пϞǡľˁҴϵįîɡѰм',
                    'arguments': [
                            {
                                        'name': 'ӈҖюЛ˻\u0378ĮфōғʎǄȗ\x8fɸ˒\x87ǣ˓ȽȔ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'PԜ¶ŀӪƅпЋĻʞǔɇҊɢʏă-¿Ҁ\x8fѝ¸ӑҠűʉɥÐМ˪',
                                                    },
                                    },
                            {
                                        'name': 'ϦÃʽԫȠ\x830',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ѾñΛϘΧĄЀǅ·ЙύϽëΗѦû5˦πӌЇƍȻ\x9d',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            357975.2449813095,
                                                                            938200.4111813473,
                                                                            981658.3859607016,
                                                                            342254.8041555785,
                                                                            924386.9436166615,
                                                                            482419.03152896196,
                                                                            969918.3955721545,
                                                                            56337.532006133086,
                                                                            280350.33820847055,
                                                                            91178.85751148386,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'PŞҶˌœҡÛȭҏɶӨ§нĘǓË˲ΘӹéХ˫ͼϲþΚѽƌĀ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3514724198276346176,
                                                    },
                                    },
                            {
                                        'name': 'і\x94ѷêҪɑȣΑǱʆѷ§ЊŎɵĝýǏ˳ԓřƍνϋϚӨʮѭȊ\x9e',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211745.277450:+0000',
                                                    },
                                    },
                            {
                                        'name': "'ыŞҲɗ\x8bLʘÔɄAγнӓЅӊ³ԝŒοƜƽ͵ˇ\u038d",
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǞŌĔƇЏӥĐŮĽŸ\x9dъԂѶԕȺͶʲ\x7fŁԘŭ˅\x96ԉϓ˲µѤ˼',
                                                                            'ǫˇȚ@Ҽ˹ʌѦɅǭȚ',
                                                                            'лʎ<νÑͷϻɧѲ÷ȭˈΙȏΫOZ¶ȷԝËű©5ΠWîƅȩ\x9e',
                                                                            '˒ʺƪԏq]ȯԎΣӌ¾ɰӫĜĒǞζʸўȕ²ˠȑȮ˞.ƧǼͺ£',
                                                                            'Ӻƚ\u0379ǿϱȤԚαȺȺēϢÚDµĘɠҮ=ѝȸΜÉM҅Ȑh4]Ͱ',
                                                                            '˻ί\x81ÄǨӴ˯ӈȏËˇƤĳӿӭЬ;ϨΦ˞\u0380ΏΤνОԀҚU¹ē',
                                                                            'ŲʙáȑǠɲɽӰĝӲʉ\x94ÁӯҀÔmƔƱыɡ˘˶Р9ДŋϧФC',
                                                                            'Ȉɋԭ҄ņɺΈ\x86ӭ\u0380ć\x97ȠϫΤˋԃ\x99ÓЇʎŻϝҤƻӽπӽǘӸ',
                                                                            'λƉҚШʹ,гėϦԅʝϜɦӡÖʚżĵţɪÁо;ɌbȆ°ѡЧͺ',
                                                                            "ɫˆёԚψΗ'\xa0Ȩıġѷ˪ɤϺƁГÊ8=ʯŶӻТшҰǀáĭх",
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8cʙвŎϾдȄɋĢŃʵǅn}^ȟő·Ψҭ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '*ɏҩʟťђȭĘǌҳЩ¡˧\u0383¼ѿιĨθÕȏčɇĺ"źԡɼαƖ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211745.640786:+0000',
                                                    },
                                    },
                            {
                                        'name': 'РCΉϞǆΰĆĊӝƿƌ`ðҗΐόϴ;ӱĠZЯɞş\x8fӖǯΤԭǜ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211745.705025:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ЖԓhɼƎҏӧі\x81˼˾ϥɷӛ΄çßōΟ˃ЇϑўӁхǦԍơ˹Ȩ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9181717281983877008,
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ʐϨāʯñĿҏƊӪÅĤΝїԡ\x98ĂɊ\x80ìàéƗɨϪƵŘʥҝ\u03a2Ѐ',
                    'message': 'àǒľÏκΡюŸė¢)ϸ\x9fϲЗӚǒȢϕϽԆȸφҤ˟ЩÆˁķˁ',
                    'arguments': [
                            {
                                        'name': 'νҞ£ʾŁԬƵŋ\x82aŘ¨μ½\u038dШ6˱ιɐҌƑНћªɉ¤Ė',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3646575565089061392,
                                                                            2889902687068817067,
                                                                            -7251946920379815662,
                                                                            2047086765699183360,
                                                                            -5158499164120154069,
                                                                            -3969362900362045418,
                                                                            4267755024536940605,
                                                                            -2379889185662800842,
                                                                            -7468603688922973502,
                                                                            -5899343514828641277,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѲѱÂζŮǳʡ\x95Ȝӛ¥ZϦĔɳʅh^ęȇɅɚαǖǰ¿m\x8cύе',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2440116730590091859,
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
                'identifier': 'ѣƞњԝʐ',
                'categories': [
                    'file',
                ],
                'error_message': {
                    'catalog': 'å\u0380',
                    'message': 'Ϗ',
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
            'locale_code': 'ԭ\x8fǹ\x92ѓŭ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'Я',

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
            'catalog_name': 'ǋƭĄ\xa0ĕ?ʄԡê˕ӭȄǚťΓӺŅȥȡόпѭnɖљ҃˼ͺČ˷',
            'locale_codes': [
                'ҬмWɤΏŪЄ',
                'Ќ҅Ą',
                'ԕ',
                'ѵȦğȳπʿǡ˟Ԟ',
                'ʋӟͼЧ',
                'ʎʐǃǡЬЄĆȧԢ˶',
                'Ɛ҈ŉĜŊ\x88Ӡ',
                'tЃʎҴǕ',
                'ԊDţ',
                'ьӠɭɇ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog_name': 'V»ɮ',

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
                    'catalog_name': 'Ɔϗі҃dͱѿ_Ȁ˯ˌϕƖѰɈƴĆ<ɧψžϤď҅ŖѽȢȻǠȾ',
                    'locale_codes': [
                            'ɐљӆЇťѼ˻',
                            'ѧVȪǳ&ҟ',
                            '2Ƥԍʏς',
                            'ЎȆÙ',
                            '҂Оҿ',
                            'ɂΞʋÙʒõ',
                            'ѷӥZȭύϠҭȤƄ',
                            'ӂ˵ÔɯͲЯć',
                            'ς',
                            '¹á',
                        ],
                },
                {
                    'catalog_name': 'ɠɴƀǱķƴŖĜӹ0Ыɔšϕ«ӦҿԬ\x88ͳԅнΈǻ¯˜\u0383\x98ˡπ',
                    'locale_codes': [
                            'ǾѾȋЈμĈ˕ˍƝ',
                            'ΫєƳӆ',
                            'Ó',
                            'Ѱɘ҂Ȃσқ',
                            'âì΅ˡʧĝêν',
                            'ԆҏҖϹ',
                            'ȕзƇƞ\x96ǵ',
                            'ѐ˗1ΝςСĹұƩˈ',
                            'ŃΣˣƮ\x9d\x82ԝʒțԫ',
                            '˼÷',
                        ],
                },
                {
                    'catalog_name': 'ǁȉАɸǨ¥дĽǺ\u0378âǎκŴ˃ũĊϱĕȱ˂ŏȓ÷ıǋєӷŌІ',
                    'locale_codes': [
                            'ʐ6șħ',
                            'ʧҽǃʺƒ',
                            'С',
                            'ћοɥÜ',
                            'þɑƘ',
                            'ня9ҷ',
                            'ρϮԝɽģ',
                            'oλ,ϕĳЈ',
                            'ƹ',
                            'dрɸǫҺС',
                        ],
                },
                {
                    'catalog_name': 'ʴʮљѺʔϰѰʍӤɝΒą\u038dǏǫЧӺÁΎ_EȱȈlȧ',
                    'locale_codes': [
                            '\u0379˯ǰ',
                            'ĸҠʎɡ\xa0҉ȓɊ¹Ԁ',
                            'ưȥõѺƵ\u0382cҐʔ',
                            'ĠûʈȮǘ',
                            '&ѮоǦςò\x94Βв',
                            'ʏΒÍfԖTΜǙȰ',
                            'ҷ',
                            'ӫԈ',
                            ',ι',
                            '$ѻ',
                        ],
                },
                {
                    'catalog_name': 'Ӑò`Ƀӯ¬ԏɬΏÈСð˘Ѫǻӹ҃ĘƵŐԢԣӾǗ\x87ːƗ˯ƶʫ',
                    'locale_codes': [
                            'Ȃ\x8aȬ',
                            'ƻɩxƈÿöԜ¶ԬΔ',
                            'Г)\x86',
                            'ǭĊ˚˥Ұǩ.Ͷ\x92ɏ',
                            '˧ĜԐȵɴǋrϣ',
                            'ΌÞ͵ĤÖ¯Ȯ\x92ǯ',
                            '˫=Ԁ',
                            'І',
                            'Ɨõͱϣ',
                            'ϰ',
                        ],
                },
                {
                    'catalog_name': 'ѝɄΠʹɟҩőÏƌМĆųʺӇƶĀνοӾЌԚȥԎѮȏķ(»Ӊĝ',
                    'locale_codes': [
                            '|sСǖŉх',
                            'Ŀď˧ӚȹƷǍ',
                            'ȋϸȨ˼ϲcŘ',
                            'Úáıё',
                            ';ȃˮë',
                            'ʞˊǔР',
                            'ԚԝɹǲwŹǱ',
                            'ɨĺѻӲӆŚ',
                            'ɱǇЊņ\u0381',
                            'ǜ§ŀ\x9b',
                        ],
                },
                {
                    'catalog_name': 'Ҹӱд¸ϨČ,ÅêƱ\x9eƢÔǃԨˌēȢʚԔΖƈФȡɰӧϘϖЛć',
                    'locale_codes': [
                            'GŖƁ',
                            'ԖљʪСjϕŭ¸ɢˁ',
                            'иîũ\x85ӗġ˗Ƣɤ',
                            '$ΜǶǪVҸҟϐҾQ',
                            'x',
                            'Ʒж\x85',
                            'ɃˀĴѲԛĻҭ',
                            'ͻšΏѤɵƄЛˡȼ',
                            'ϛʛȺŸӾ',
                            '\x9e˥˫',
                        ],
                },
                {
                    'catalog_name': 'ΡϢʒŊЭīʌ˲ҿϱƳ;ЫƑɌһҌӥƩɧАΩОҾ҉ȵњpƓ˅',
                    'locale_codes': [
                            'Ȕźϩ\x9f',
                            'ԞłȄĎ',
                            'Ϟē',
                            '\x82ңêȁǮʦ',
                            'nχσ',
                            'ÌȒŞ',
                            '¨ԂѴǱŃ',
                            'ȿǂӇɩƤԥѬˤг',
                            'Ȧ˧ϸŴɴҷԍΠ',
                            'ҳíʪ×tɅ˚ǟȬ',
                        ],
                },
                {
                    'catalog_name': 'à҈ӨлjʶŞóĊΉz¥єЅ?҄Ѐͻ˥˔ҚЗ¸йÿʾʏ~άԣ',
                    'locale_codes': [
                            'WùѷƞΝ˅',
                            'ňȋJїΔѦԩǘG',
                            'ɿ',
                            'ҲџԆÆõMô<',
                            'ŠzΨcƯχϚӥ',
                            'ǆ¯ɨ',
                            '˶',
                            'ҎïԄÝӐѬԄŏù',
                            'ǳ',
                            '\u038dÛȄǰƊĀ',
                        ],
                },
                {
                    'catalog_name': 'ĢkAuİjўѿԕӼƻ҇ɒͰѴԑҮǭʁϝϡǒΩјΓŧȘϨNĸ',
                    'locale_codes': [
                            'ƶ˩ŇθҥũΡ',
                            'џͳМοʙwƂһ',
                            '<ơíĉ*ȁ',
                            'ƱȈHʹá¤ǃǨ_',
                            'нŤĹάӇȧ',
                            'ӧ',
                            'эςÿ҆\x87/ńΐ×',
                            'Ǧѫ',
                            'ȋȪҿďӏȥʹɟ',
                            'ѢЬɁ˽Ÿ',
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
            'name': 'ʾπҶ)\x83νω˭Ŷ*ʬȐˀԓѝЋϓȌƇɭαǊԗĲϧȧÛԝɃԩ',
            'code': 'Aʆ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ŀ',

            'code': 'Ԑ',

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
                    'name': 'ĭĒњ˸áʿ\u0379ҁҲϚ˩²ƺƐ\u0380ȼЪƇȇ&ӚԃлϊϘϒʪҨèϜ',
                    'code': 'ҠЪɤ',
                },
                {
                    'name': 'Þ\x88ʗ¾ΘЈqӯМľңɊһЪǩѳҟʍǰˍ!ӛɡ\u0382ȣʿŰȸώ˯',
                    'code': 'Υо',
                },
                {
                    'name': 'ǘӍӆƺάȿ¹\x97Ϩ)ϓɹǅϝȬҁȂǫɭƅØѰǒҮrɿǨłǖҗ',
                    'code': 'ѭѤϊˈϻь',
                },
                {
                    'name': 'ǡȿơҘԤΚƦˬ¿ˉȪˀ\x83ȧ@ʴϋź϶ƼǃΏΘÇМĒȿ!Ҥý',
                    'code': 'ʫψÞÒƪ',
                },
                {
                    'name': 'Ǉoхˡ.Ƚ=˟\x87ŃΞβҽӒƝȁªģӏţΏɯMǑʉFϧѩҷ\x91',
                    'code': 'Ɩmε)ǡ',
                },
                {
                    'name': 'ӽϷ',
                    'code': 'ȋˊȭшȵǵř',
                },
                {
                    'name': 'tӞǫǾ¡įǵҀӪ˶ȥȇ',
                    'code': 'ϱʡɇÂя҂',
                },
                {
                    'name': 'ǚƲɊ',
                    'code': 'Ѱjϣ˘ʡ',
                },
                {
                    'name': 'ĒӐį-ǪjǙŕĨːϦ@ɺęͶѻũŜ\x9fǩkϢҶȐɢ¼˼џǔŢ',
                    'code': 'ƳȡӂԇқƠ',
                },
                {
                    'name': 'αq#ԉʍÊӚƟĐԥƃ¤ϊʸѓӧǅ˪.ȓśȶŶe"\x98ąӟɉϔ',
                    'code': 'ϑ·σҟњȣɜΉлí',
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
            'locale_code': 'Ξ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ɜ',

        },
    ),
]
