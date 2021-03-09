# GENERATED CODE - DO NOT MODIFY

"""
Tests for the i10n module.
Extension petronia.core.api.native.i10n, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import i10n

class RegisterTranslationEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_TRANSLATION_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisterTranslationEvent.parse_data(test_data)
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
                res = i10n.RegisterTranslationEvent.parse_data(test_data)
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
            'locale_code': 'Ќϋ',
            'catalog_name': 'fĕӲµӎ©МϏŉϣųˁwӂϞҊƽęĪʄѡƼӎӠë¤ʪĺԗɎ',
            'message_file': 'êƘιʈcѮλͼŋɔӫРNɁӾĐȖ\xadǧԦǭɈѻ¶ώҽɐǆψӞ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ƶ',

            'catalog_name': 'ÀŲŇ',

            'message_file': 'ʳԉ',

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
                res = i10n.RegisterTranslationSuccessEvent.parse_data(test_data)
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
                res = i10n.MessageArgumentValue.parse_data(test_data)
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
                res = i10n.MessageArgumentValue.parse_data(test_data)
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
            '$': '\x8dĺʓǩ\x82ǚѱĎƅӲ˧ɞęӣƁUȑɔӦlʲщókƼȤѧԈ\x8dǈ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -1015075338439718988,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 252440.56721030537,
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
            '$': '20210309:035832.928893:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'îʡQ˼ҦԆΈɍƞʕƄëďìʦ˗ӇDӾȨº˄ѐƛɫǡȭǵǳѰ',
                'Ƨ\\ʜдʬɮʉ҄ʷƪȱοΓȟ°ʊҖȊĎĤŹӥŘҠĦ%ņΨЅƯ',
                'ˣú©Ϻ·ǶǲϹʢˢǰȖȉêƭŴҠOǓЖѵǡtƎʶʊȯˀϏт',
                'МΉH¬аМȳк\x9fɟƅϞƖɑ϶ΜϏВήΑӼĊŨȹΟΜ¿\x9aϮĠ',
                'ǜƝȑď.А\u0381ñǠʨòʛǠuŊΐϧ҃ʿӠýХӶțϰ*[Ñӗë',
                'ΩЅŕɔѓ¤Ěѱɣϙ\x99\x8cҦψ˒Ҵīĵԑ\u038dȬƶ×ЇʦԌЩJèЯ',
                'ʑʻƑňҥŵПӖWāɶʥŨϨσďҙÓƹɝƬпƿȭăҳͰТǣƜ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -1422979641940708713,
                4995136522711313841,
                -3934831882043604731,
                3106266865109242779,
                4602964556038357093,
                6456229171359793988,
                8387331940626346828,
                7986953160525838539,
                -4914074484260579024,
                -4505415565255612170,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                943420.0760168725,
                775505.6291000115,
                841170.2046786838,
                633170.6296612693,
                457985.98138918995,
                132087.53603064764,
                37264.14787015194,
                -84556.45916458289,
                926468.005506311,
                788291.6904323124,
            ],
        },
    ),

    (
        'bool_list',
        {
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
                False,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210309:035834.057098:+0000',
                '20210309:035834.076478:+0000',
                '20210309:035834.098065:+0000',
                '20210309:035834.117688:+0000',
                '20210309:035834.138639:+0000',
                '20210309:035834.159205:+0000',
                '20210309:035834.178837:+0000',
                '20210309:035834.200678:+0000',
                '20210309:035834.224397:+0000',
                '20210309:035834.246860:+0000',
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
                res = i10n.MessageArgument.parse_data(test_data)
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
                res = i10n.MessageArgument.parse_data(test_data)
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
            'name': 'ӦχɩϯȐмϘ\x85íĂǓǾ',
            'value': {
                '^': 'datetime',
                '$': '20210309:035832.598993:+0000',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ǥ',

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
                res = i10n.LocalizableMessage.parse_data(test_data)
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
                res = i10n.LocalizableMessage.parse_data(test_data)
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
            'catalog': 'ƾЏѠӈ\x88pƹЂϢƻʕϽѧʺԣșӤǻѬεŽǳîҀƔԏɥҮƏį',
            'message': 'ƀďċԢ˔R<ϬѪ˦ʈɒБšɏeʗ¡öƤÓҎΪȝʈƅŸɱҠQ',
            'arguments': [
                {
                    'name': 'ѭ0ēȓҬĎ˞ȧĝӚЗɂ0șӬǋѭ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210309:035830.426476:+0000',
                        },
                },
                {
                    'name': '¢˹&ϑϹğ˷H4ɥơ)Ԩ<"ӗѡѿȅɨѮ6ӔѝӏĂĊʄĐӅ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ǹ&ρΙYѩʮQʷʈԠқǯŘʉȇųȺêԚŌʷұεƱԦ*ӍƎn',
                                        'Ϗʊƀӌϱ\x82ԅƘΈÕOɛӫƫ¾ǳƒѶ\x95Ȧΰ.ˍљЉӧλŖȳ¾',
                                        'ԤθţŞӺѕԐԗé҄Ҍĩ\x84ŤÚɳƬ˞ԢИƃԨόϝϺƵ҇2~Ò',
                                        'ԅmǭѮȚҫԞŝΛͳƋɋ˖ѾŻɹԏǅͽÿĘЖɨ˥Ъ˲Ο(Ӥѩ',
                                        '˾ǱҪԠҍшϺΦӲӝȎӴŹԜˆāW!ȟɞƊGў˸Ƀ«ƖƉԅʃ',
                                        'ǛʞúvӫȪԆѲƼʒE\x99ȧöԊãУͿНϰƎɬҶƱмðʣó\x99ϱ',
                                        'ȴҼϸ°ưН˚ŎŽȀÖ҉ΪЋ|ʥέę5ŊЇӡ\x96\x9cΆƃџöyƩ',
                                        'Rµ^ƲĤɫɓɔĿʛүӥǡƴƗʶɸАŖǉє;ƺΥ˄ȥʪрɼͼ',
                                        '\x8dôӌƉɲΫЯӌřήӵķŋлӦƲT˼ʏƋÀɷYƳɧԏiŴʬ~',
                                        'ИҰʄСңҼƘɀɗØÊмϽ]\x95ԦŐ®φЊąƏԞεӿκѿӑǊԁ',
                                    ],
                        },
                },
                {
                    'name': 'Ņ҈ϛӷǺȹĐÃо\u0378ю˒ǤǵѤϒpĎªόÎħeҗϣ\x8fɭ˖ǹʏ',
                    'value': {
                            '^': 'string',
                            '$': 'ǭºТˀĵőЌχѠǹ\x87ɟŜƊҳ\x9eșĸø˗і˯ĢPȭїΔЎͲŝ',
                        },
                },
                {
                    'name': 'Ϊ˭È\x88Ȍԙ6ƃƓåԍƗɘһĸɗ˽Ȧ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        512945.7173109442,
                                        695245.0787175626,
                                        974763.4229197169,
                                        587655.8235066464,
                                        393159.7180294855,
                                        115423.26062331675,
                                        400024.1996916899,
                                        206026.2204355924,
                                        434430.8121314844,
                                        2509.247458837155,
                                    ],
                        },
                },
                {
                    'name': 'ąӚΊξϭ}ɀ0:ɹ˛˯Țͱ\x81џӚȮƊƹʒΕ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210309:035831.183192:+0000',
                                        '20210309:035831.200442:+0000',
                                        '20210309:035831.218924:+0000',
                                        '20210309:035831.241304:+0000',
                                        '20210309:035831.264082:+0000',
                                        '20210309:035831.287830:+0000',
                                        '20210309:035831.309061:+0000',
                                        '20210309:035831.326260:+0000',
                                        '20210309:035831.347240:+0000',
                                        '20210309:035831.368955:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ӱȌɱӓƶо˷ǩЗÒËǖʂʏ\x9b˧ɉQѽ.',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        False,
                                        False,
                                        True,
                                        True,
                                        True,
                                        True,
                                        False,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ƎЂ%ȢʏŨȕ\x7f\x91ϴӬŁӤ~ѝёƅÒҥ΅ˢʷΉ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                    ],
                        },
                },
                {
                    'name': 'ńǴӑ»ñδʊҢ\x8e',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ɅӂϖѷyơìБǶÇHžҪыʳ¤ȇи~\x85ҷǃłΚ÷Œ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        6387168589192594051,
                                        3842201437467932726,
                                        2280665442757978862,
                                        -2221561162773190310,
                                        8499571853763295589,
                                        683997340910966902,
                                        -8071031371487833429,
                                        4111219932040415039,
                                        -831057566395429830,
                                        7909912371442645196,
                                    ],
                        },
                },
                {
                    'name': 'уĸȱɭ\u0379ϑɲдԕӌгƃĴˀʓвзłѱѱˣ¼ό',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        -74187.7686111206,
                                        243293.8508868119,
                                        257974.95539644378,
                                        811957.4255220349,
                                        155682.35659506658,
                                        712821.3599740351,
                                        408186.7705723198,
                                        150798.75199529214,
                                        323955.2619841991,
                                        365394.9617254083,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ɏT',

            'message': 'Ԇ',

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
                res = i10n.Error.parse_data(test_data)
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
                res = i10n.Error.parse_data(test_data)
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
            'identifier': 'ʖӞȊ·˞ɿƎıҁŒљ·ȹ(ȱҫѣϾˇТнŒçӡªΈƉС]Ә',
            'categories': [
                'network',
                'internal',
                'file',
                'file',
                'network',
                'network',
                'internal',
                'os',
                'configuration',
                'invalid-user-action',
            ],
            'source': 'OÉԀþ\x97һӕUЛĴΰƖń\u0380kɱ˲Ў\x82ZҜƑʚ\x89ԬǸŁƭ£ϙ',
            'corrective_action': {
                'catalog': '³ƤǾšǟϬāʨĂĢ˝Ͼͻ˺Ʃ\x8fγψ¿Ӭǧύƹʝć¶ңƼȼĖ',
                'message': '¶ÚΒԃИǀ҂ƴɫǞƆƘҗìʐάɆЊÂώ\x8dŋҷѐԒМʵҌȐԨ',
                'arguments': [
                    {
                            'name': 'ҤɐύȤϽSǵʎŖǛІ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210309:035828.246625:+0000',
                                    },
                        },
                    {
                            'name': 'ΕōȂʵʒ©çϝŤҊȲӌѸӝԎ\x8c',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -6410143799617351035,
                                                        8432052875503437995,
                                                        -5652539737626128148,
                                                        -3970936381321991158,
                                                        8222057012027492937,
                                                        5074632719385816766,
                                                        -3529556190482464930,
                                                        3479167556416705322,
                                                        279303464833138525,
                                                        -3228862144683630414,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǠŖӌѿγͲĨŸĀȀđJђɬљȝJҀѨȝǜ',
                            'value': {
                                        '^': 'int',
                                        '$': -1598151550138483027,
                                    },
                        },
                    {
                            'name': 'Μɹ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -5892158676638899457,
                                                        -2997343249053446459,
                                                        6058844197623345260,
                                                        -6264103487047235662,
                                                        -8969663998289720786,
                                                        -4127063863240661769,
                                                        8631996218264889903,
                                                        8043192785738649419,
                                                        2324924715457020350,
                                                        -3120943153932270488,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ƮªŌЩƂ˫XȻȘ\x9aɉѼЬΧѨñ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210309:035829.026884:+0000',
                                                        '20210309:035829.047647:+0000',
                                                        '20210309:035829.069546:+0000',
                                                        '20210309:035829.089225:+0000',
                                                        '20210309:035829.108633:+0000',
                                                        '20210309:035829.127835:+0000',
                                                        '20210309:035829.147270:+0000',
                                                        '20210309:035829.168818:+0000',
                                                        '20210309:035829.189369:+0000',
                                                        '20210309:035829.208488:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ƺƖ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210309:035829.302251:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ɺƇĕ˫ʹҸŒ\u038bPХŗǷ»ĳŔӂ˞ʍԬҵѣɚƙģŗїΐdӎ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ѲŗӞȯюŦ«αļМŜͱŐӋKГҺ:ˈôəN$ԭˇʏŀǵō˝',
                                                        'ϳƬϓÖѷɰĤʘƮɿˈүԦǒÚ \x7fҠдԜ\x8fΫƈ¦ȲϪҟȃxɗ',
                                                        'Ͳžϱϻñƀгć˅\x86Ǯͷ˸©Êǵѿk]ΤΫ\x89|Ǎű˓ʳtǈ¬',
                                                        'ԔΒŹМҜéˣҍĲӈōӈнҘhɧ˪ЏϱıŢϫʙbƗƵŸɩίˆ',
                                                        'ѭХ{ʯҖҨȣŵгσϙ0ΘύŽ˔"ɰҚԩͽҞ3ß˗ԁ΄\x89ѝ$',
                                                        'ъҙJ˙ƝƔòӟσƈ҃ԁFśĕӕŶΣɺǅ©ѴɜĬǉԥǈ\u038dϡԮ',
                                                        'ғ©͵o¯ϢΎѡѣѾͼД£Ѭ\x84αи˾ҥʑÓѥԝ\x85ªǘІɜãѨ',
                                                        'ȻЉȜ˅ѵ|Ʈʴº£ҹѾҺιŧнǕԈ˽\x8bC\\ǧǉǫŁԁηуˇ',
                                                        'Ӱ·ȔɡơԜƢДҒțcƷŇɮͿІǖЖĕӧӕэǮқΪˍԢӳǒΫ',
                                                        'ǡ*ӴȦ\x9f"ʁʶϐȷҔì͵ѹñΌҗшǩԖŰҲҼ×ѣ}ϸԟξк',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӏÄȀƯԖʓν\x99ϩϋ\x84їȻǥЋ ðȆϒËʖŃϣӼȭӭW}ơɒ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -140695463828409229,
                                                        4399700753653656610,
                                                        -2988144761346636162,
                                                        -7053736062403225995,
                                                        3441505540267969048,
                                                        1960435595650089506,
                                                        2762343821483963531,
                                                        5965428702363623017,
                                                        2402401185225258885,
                                                        7158221256228356391,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ÄõǸόѱCĺжɪǝԠʇȌӫƪ@ВīǙҗШƥӉ:ʏіΒʁλË',
                            'value': {
                                        '^': 'float',
                                        '$': 121242.30163409188,
                                    },
                        },
                    {
                            'name': '\x9b\u038d˨ɗ´ҲԏŹſǞû«˽ħƼҵҵҏԄ\x98ȚĒ+µҥȡėșϖΉ',
                            'value': {
                                        '^': 'float',
                                        '$': 565566.6283210805,
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ȐӝԛĻѵҝ¨ȀЌȩaȠѨ˄МҴŜĘĝӲùǍԢʒЃŀԮӷß2',
                'message': 'АВʩӔěɖͲȟ\x89ǰŉʦġƀʰƤɖWȯĿοԎɍўΥѓʃҌζȧ',
                'arguments': [
                    {
                            'name': 'B\x90ɏ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        '44˝Фȩ¢ȥƖЮˎЗưӆɘĕÕȶíÂΔ\\āҡ?FҜ\x80ƕџʹ',
                                                        'ôĒΫϱ˺ǞϷųѨɐԔɩwɟŭҚО«Ӕö\x8eѓˡǇҋǆ9Ƕϑǖ',
                                                        '˗˩ɜįÎʽȌο³=ɘȔϪɁʬπҼ\x81ȣөӱǛǮԊ{cӖдǢĂ',
                                                        'ƒȚҡø\x9e˧ԖЋ;ԣʧǅGӒŽFԝΟϸƯȫ˚\u0381ċГȾӌǖЯř',
                                                        'ÊǇҎԝ>ӃȣƫĿƴƶΰΒǥʛŦ£ŶɕǾϠӣƤˁӛ˜ĳӥɖˠ',
                                                        'ʔÝԃȑΎɿɾɥĊɞùϞŔǱ¦Š\xadʱ@ͺΖÏˀҬλͰȉͿǭf',
                                                        'àҁəĆh²ȜӸб\x9cŗɽϢȭ#˻ѷԚǕΦǶЇәÐыЪʙU{m',
                                                        'kŒґѮǕ˷ǜɨȪȶǔҴ\x9eǉ.:ρǥųĸŪʾ˛ǮԔӋ\u038d\x9fԊв',
                                                        'Ӭ˼ɇφ\x9cǵˈșɣˈ\x87Яí;ǾˑűįѿīϪӨË҇ɵĩćbφɧ',
                                                        '\x85\x8eĤɗЄӍГϘЈбɎĖƶԈȕ+ǆ\x86˫\x9aǚЯԣӫŲΗϥӶъŸ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ȗɣЛΔȲ˧ϡʄgśǉȽʧɈΖȌп£ȖΆԮ˚УΒèώʅȳÝѣ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        955931.5125758371,
                                                        978621.6704324668,
                                                        836064.57434845,
                                                        17168.3021199129,
                                                        91778.74753118589,
                                                        853282.4381409147,
                                                        516951.69879199076,
                                                        121534.69558492559,
                                                        85992.11962127639,
                                                        568792.8023396272,
                                                    ],
                                    },
                        },
                    {
                            'name': 'мҸƜѡÄ˪ѮԡοdМ',
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
                            'name': 'ʓԡОӦ˗k˴ŷ΄Ԯ)ͺӂĀрăԅΧɏtʆϽͼȔŠӿ$ƏƗϽ',
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
                                                        True,
                                                        True,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ԉ¸\x82UĄӺ\x86ҺɘԜԪѿůѯͺԐѼ\x95ΐʜƎ͵ћэґæǤ\x8aϣˢ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210309:035835.738219:+0000',
                                                        '20210309:035835.755486:+0000',
                                                        '20210309:035835.776688:+0000',
                                                        '20210309:035835.793353:+0000',
                                                        '20210309:035835.809201:+0000',
                                                        '20210309:035835.824967:+0000',
                                                        '20210309:035835.840814:+0000',
                                                        '20210309:035835.855443:+0000',
                                                        '20210309:035835.872259:+0000',
                                                        '20210309:035835.890410:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ȟǥ',
                            'value': {
                                        '^': 'float',
                                        '$': 963114.28489234,
                                    },
                        },
                    {
                            'name': 'Ơ˭ŐΒǟHΡuѮчԚòɀŸϾgċϦÅŀˍЭΓԔˁӊMҁԮ҈',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210309:035836.093703:+0000',
                                    },
                        },
                    {
                            'name': 'ǈŦԩαĚΑγξǐӰ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -2856204299962621258,
                                                        8320676401107348375,
                                                        -8509199092111293816,
                                                        3135326334319384686,
                                                        2732531491501840080,
                                                        4537760939741440659,
                                                        -7790948233237776794,
                                                        -9051492097848751032,
                                                        5339813509229296052,
                                                        1466835502114828764,
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ƕ?Ԕļ˨҅ěņ`Ƒǉņӗî$ТĠүӥҕXȞǢż',
                            'value': {
                                        '^': 'float',
                                        '$': -7388.6013950449415,
                                    },
                        },
                    {
                            'name': 'ТѢҷѮuZЌΪğХѭrɕĚìȐĐҽʤ\x8cˊӟêĊæ\x84Э¯oʂ',
                            'value': {
                                        '^': 'float',
                                        '$': 887609.0791494867,
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ÊϼúӨϫ',

            'categories': [
                'os',
            ],

            'error_message': {
                'catalog': 'Ȉċ',
                'message': 'ϰ',
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
                res = i10n.RegisterTranslationFailedEvent.parse_data(test_data)
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
                res = i10n.RegisterTranslationFailedEvent.parse_data(test_data)
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
                'identifier': 'ëԔě ϋ¤×ȲƢɀќάΕ®ʎŏϛɣӪũɆ*Њːˆ0ȓoOi',
                'categories': [
                    'access-restriction',
                    'network',
                    'network',
                    'network',
                    'invalid-user-action',
                    'invalid-user-action',
                    'os',
                    'internal',
                    'internal',
                    'os',
                ],
                'source': 'ΦçŵõʒʣԆ\x8eĖʀϱν˧ƙâȳİʷ\x86ǬҔYǖЇĵIҸΟƢͳ',
                'corrective_action': {
                    'catalog': 'Nћ˘ʚϘ˂ϷΏćӷǿʙǄɖԚԗϭЏҫʥҎюSԦĦА˭ŜЭ˾',
                    'message': 'ĭӎбϞæ^цɆȀ˳ȃȷł¢ӓЅαʢωǂȜʀ҈шЌԀȆæɃЅ',
                    'arguments': [
                            {
                                        'name': 'шӸXҍʷƸb˳ĺЩÍɳȝĹs0ʦ¼ѩňȫѶӲúҷàǰdČǣ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035824.502308:+0000',
                                                                            '20210309:035824.519521:+0000',
                                                                            '20210309:035824.537426:+0000',
                                                                            '20210309:035824.554926:+0000',
                                                                            '20210309:035824.572369:+0000',
                                                                            '20210309:035824.589464:+0000',
                                                                            '20210309:035824.607093:+0000',
                                                                            '20210309:035824.624238:+0000',
                                                                            '20210309:035824.641098:+0000',
                                                                            '20210309:035824.658457:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӰÚˏǋҫ\x84δ\x88κ(ſ˾ȹƈѻīǂҍΉǮƈĝ8ô\x86ƾͼȄϴ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'р8φӗŮǿӄʉ¬эřʅʯŘӾҒʻҨԆʀʺГΕ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6066116042030149006,
                                                    },
                                    },
                            {
                                        'name': 'ʝҒˁЦҀǍ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǭǛʤоǘϨȾŗŇͳȹǜȸϫΞʊņ˜·ȲϝëŻûɢŽɠ˟ӂǍ',
                                                    },
                                    },
                            {
                                        'name': 'ϔƆʚϡчǌіϢĉԧӑʣŒҺǚ˕ΠƸΆǌƼш?ȑϡАԣԈӪž',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            609190.5914899417,
                                                                            846098.8937437302,
                                                                            475132.5087549025,
                                                                            640575.5007944767,
                                                                            -10855.990975883295,
                                                                            974181.4216587984,
                                                                            930349.6667342071,
                                                                            721641.6063205808,
                                                                            -50849.625435359034,
                                                                            447755.09900045744,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '>ΦѵӸȵϑɨɊżЂĵʘa˸ȟĽ#й]ºşӊԜ9с³ŭ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1790502583622201446,
                                                                            7956933979415015833,
                                                                            3900901839128250793,
                                                                            5918635834391746792,
                                                                            7963220635716362040,
                                                                            -7787849922689662047,
                                                                            4265982693541797732,
                                                                            3639225747697478291,
                                                                            -3125057895413456385,
                                                                            -2520060459846085947,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӂƅӆ\x9dϤȼҺʉ҉ΦΦʙ°ѓГȡԔǣɆҜÐ\u03a2҄ЗƟӉǹʘΐλ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6986236772312661214,
                                                                            5507819179199991144,
                                                                            8307183358276984984,
                                                                            1745600365349231720,
                                                                            8925623909238394151,
                                                                            -6742090599372051061,
                                                                            6987977490611793372,
                                                                            136606438343870553,
                                                                            -6596683949431739647,
                                                                            615577416704763529,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΑŇҋ\x96ŊʩgΕεԁʼҷҨȏʆņˊѤέԙº˞ˋɾј«.ϽϧӰ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȚΙÃĉưϷçŁʝĝɤӄ§˄IгʜϡɁǈӛ7ЌӏЀДδǈЭѳ',
                                                                            'ӯӜӥζǞΘԂϏſӶƇԪüÕətʚΑͿάÄԗЂá§Ąʓсѫȱ',
                                                                            '9ԋӻ\x9cöAЮŗљӸɊ˷ɃŞɥi\x96ɸąГΦӺƲÏҪʩ¨Үġҍ',
                                                                            'ϥÔŘkӘƯňңƋԐӿːŅʓϗлҀΓҤЈ)ҟίïԙ҃\u038dĪǩ ',
                                                                            'в÷ϴĐyɱљ\x9eԞў_ΒʫǬÛȂǻͲϘÝʧɯ˹ĎIӵĦԧф\u0379',
                                                                            'мӓʸԡǯǕä1ĤŷӱѸ\x91ГϝÞӳѺфƦˡĶѻˇɳ\x88óГżƇ',
                                                                            'ăВŗθǽ\x81ϫʃ\x93ҏǻƫˡΌȦĴһŧ¤҉ɌǡҮ˾ΉџʷϰϢЂ',
                                                                            'ψўLſӭΪɺ1Ђ\u0382΅ċҠФѬίбȇʿǿůĳѽőƂȰͼëƌά',
                                                                            'дıζώνЗђŠ½ƥŜԒҊ\x87Ǡ\x85Ȅґ\x97ҞǇҹ˘ϨȾ˹ġ˒ƌё',
                                                                            'ĝƮƊĝɄΔΥʎʽ\x9bΩeǃѡэʐВ\x9aσHƜƼɽШϐŽѢFʄŹ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u038bȫĆʦʳɄȳæ¶ԋȯ¡ϯȲҬЮ¢ĵǈÌZɌƔï˳ĿϽǌaԍ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɾǯ҂ȟтƪɑѡɠЏʲǈċʖ§ʘˋĤeTλȝɭʯʜӏԧ,ҭҵ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            289605.58467976743,
                                                                            611526.163933762,
                                                                            97020.91085739387,
                                                                            336024.856478096,
                                                                            873028.9683736752,
                                                                            512137.92479761026,
                                                                            323242.29416392016,
                                                                            -78531.61103798889,
                                                                            36322.1978541188,
                                                                            -29214.366521694596,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ԂԘâŴϏτŔǶԇƸǨΘȔѺӢӒǰ\x88\x91өԪτEKˈɿӦİѓʹ',
                    'message': 'ωʴĥ*+ÞđdϢΑȡȈόGήӒԗ˥ϗHӥЧāƽѠӞɧɻΔʋ',
                    'arguments': [
                            {
                                        'name': 'ЗǱўϓƞőɨ\x8aŕǆĕȂķŰƑϘɉϮғƲȵŴɾΞԖƶѴş!˷',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ăҋʾʬВϘˈԈͽķƷДtɇоòǎԈǸʒǚȨɤcȟɓҽҀҪӳ',
                                                                            'ʶęϹΩƱýmǸЃ)ƽƀʠҥ˒ΞˀŖҳѻT1ЩөύȦйõ\x87Φ',
                                                                            'ԋ˟ΤѱλϴSеԒӳϛʒȔΉƭƇîХӡԔӹԜͱͺѯΊϷӮʿѷ',
                                                                            'ɺѻʖÆдφǂàҾϋξͷЖԘϙ\\Ǻ\x82ϐĳʂʱФ7ЧŽ\x93ʄσ\u0378',
                                                                            'ʱԮĂȫԤGƥӜȼ·ӄРʫɁˇÛƕҝƚƁòĕϵʳκÐĜ\u0383ĸɲ',
                                                                            'ʾǜŹВΔɗɇ3ѿ΄Bá˸ƶԠВƍƔɇї³ϭѺ$ЮўϬӡʑ\xa0',
                                                                            '\xadɪéԕԌŠ3ɱʁŲ\x9bŻpǿșʱNȈӒrćӜĘŤ\u03a2ěϞʩÂȲ',
                                                                            "ѽjȬÊΟЧåȔwʢҘȰ'ɘ\x8dΐ\x94Ӗ˘ЏӝХĮЋҭ$ǐѩΉ×",
                                                                            'ȳǭЈȷ{ʚ\x90ӲԊǪ¢ϏĉƱϹǙȉƐǥяԏϭȱǖԬ˔ɞʎ\xadǻ',
                                                                            'ϫ0ǠªʮϼңΈϗӺѮͿďʼ<ԌÉӎNŨҖӐϘĠˋϵԄѠсʎ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɒΝЧǼXüҦƪúØ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'øȿʹĀӯѴάāŃäˀþÕ´ͰÑ¯үȞгȠ˥˗ňѯŝȋ\x87˼ȗ',
                                                    },
                                    },
                            {
                                        'name': 'ȭƜŃҬǪКȢįėƖȟƑǂƿ\u03a2әȮ˒ïѮƹяtǽʹΔǡνœ\x97',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
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
                                        'name': 'ΕӾĢμ˹ϛɵѠǠfęҭ˻ÄȒӶІɎYKζԭϛИ˲ͱѪѭҳ\x8a',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'șӬʜԩȇƁȝǩJ\x9dҁьŃ҃OѾȊɘǋżӅĨӝŠЛҙҗŀԛɹ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035827.391281:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΜԖɲӡíïͰŪʑ҅ӆq҇ӭЩϽ\u0382˂ЈԀ\u03a2Ø',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 254593.61267863412,
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
                'identifier': 'ԖҪƅɃ°',
                'categories': [
                    'internal',
                ],
                'error_message': {
                    'catalog': '¨ǡ',
                    'message': 'ǈ',
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
                res = i10n.SetLocaleEvent.parse_data(test_data)
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
                res = i10n.SetLocaleEvent.parse_data(test_data)
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
            'locale_code': 'Ͻ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': '˯',

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
                res = i10n.RegisteredTranslationCatalog.parse_data(test_data)
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
                res = i10n.RegisteredTranslationCatalog.parse_data(test_data)
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
            'catalog_name': 'ЗЎЧɩӇWˋ\x97е˰ŬÑˊŌώȼ΅Ԇ;ԩ˙ԟнѤɍËˑùώϽ',
            'locale_codes': [
                '2ʕä',
                'ȓˁΊʀV',
                'δǲ',
                'ưTƘςŹѪ',
                'ɞGZғԤјҺгҩ',
                'ǅ\xa0ŵämǯɱҮ',
                'ʑЧɈŒŏ͵м',
                'Άɜ',
                'ř',
                'lȏ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog_name': 'ҟκȃ',

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
                res = i10n.TranslationsState.parse_data(test_data)
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
                res = i10n.TranslationsState.parse_data(test_data)
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
                    'catalog_name': 'ǃҹƃ÷ʬԚɒŤĎͲˢŽҿɠ`ɨȘДҢӫŠ҈\u0380ϥъ¤άŦy˕',
                    'locale_codes': [
                            '˖NҤм',
                            'ˊăţР˳',
                            'ЛÃβÃǼ',
                            'Ċ',
                            'Āʷȗš',
                            'Ȼ\x8fμё',
                            'мƪ',
                            'ˮɃ3ʪǳÆǺĸǓ§',
                            'βʬӢƍǯĢ',
                            '˕\u0383Ȉԏ',
                        ],
                },
                {
                    'catalog_name': 'ĆȳŐƁ¥ɉǾŃэźӲѡˆТʶԣöтɈȯӠŊáӇҶη\x88cӇȅ',
                    'locale_codes': [
                            'ȤȂӺѥlίҖŗȲ',
                            'ĩыMƞkɩхɤ',
                            '\x9eЃǊɗĝrǊʰɨʾ',
                            '҂\u038dŋ˘ȢȺг]\u0379',
                            '\u0380ȟɤҞVɩҬԒ',
                            '¤ÿ±Ԟ˫Ȗ',
                            'ЭN\x80ĳĄӰ¢',
                            'ŕҡĖ',
                            'ӮԞ\u0378Ǟ',
                            'ʐĂȚҋБҫʅӦʚѶ',
                        ],
                },
                {
                    'catalog_name': '£ιƆп҄§Ғʭʵӓ+ʴāʄÊĨƐʻґ/Ѡȋ»ɝ·ˊӹʞŎÍ',
                    'locale_codes': [
                            'Ϣ',
                            'ʜʛԗñˣµҰƎ',
                            'ȨǮʘғ',
                            'ҘӏȣˊŹӑt&ʁ',
                            '3Ϟ˅',
                            'êԞȿЙ\x88\x95',
                            'ɇƂүͱϠЉ\x89ĝ',
                            'ϛԢƞԉǔзƬ[ψx',
                            'ӣьҫ\u03a2ѩҷȃʏ\u0378',
                            'ʰӸŸĖÛɤb˚īă',
                        ],
                },
                {
                    'catalog_name': 'ʿuѱʹяι\x94Ǽ˼ƛƘϺģϜÍ˗\x927Ȑ\x85\x9bіН¯Ϭɤż һȠ',
                    'locale_codes': [
                            'оІҊε˙ѸʣÊȖȶ',
                            '$ϝПĔ',
                            '×ӀɳΖ',
                            'ȉΞȞ',
                            'ĒϩʼŰ',
                            'ŠȦѩШ',
                            'ɟȎģtĎěΞ',
                            'ŦϠsӕ\x9bÁ˜ɥ',
                            'τӈӓ҂ɏĦͿȾʠ',
                            'ďÈƓ',
                        ],
                },
                {
                    'catalog_name': 'хÅҔЬΞǦWҍӍʤӎлˉƷϘкӤҎϸГǹ\x96KԓRԞΫʌ4ϕ',
                    'locale_codes': [
                            'ǖѳϧ\u0383ͺĦ',
                            'ђȸ˚bӬȔŐ"Ԋ.',
                            '2ȵʕƕπ2ĻŇη',
                            '\u0382ʛù:ɦśбȞ',
                            'ǟȘʝŅȲ',
                            '˕˪W',
                            'ԌқҚɒ',
                            'ÞЬ',
                            'Хȷӿϝđǳ\x94',
                            'ȆѫɠŎҋѨȞž',
                        ],
                },
                {
                    'catalog_name': 'ЪʽɯŁʝųʪɡʜɦȴӖϟŜʖϩԇҼȤ`˺ӐÉȈȋȆ˚_Лή',
                    'locale_codes': [
                            'ΨѠԣԉҟˣKғ˦B',
                            'ŢҢҔѓ',
                            'ě',
                            'ƍƓūµȥϺσ',
                            'Ӟʁі',
                            'KȱƘAƺҽ×',
                            'Ũ\x97˘ǎљŘů',
                            'кНiǰ',
                            'ʊù',
                            '\x7f\x8dҷï˫Ɗɥ',
                        ],
                },
                {
                    'catalog_name': 'Ƅòӡ\x95Ƴ˻ғҾȴЉθ\x9a˺ΒϱƝ˺љϮƈőΧʂѽӧΤćфҶГ',
                    'locale_codes': [
                            'ƞ',
                            'Îš+ÃеП˲Ĵ',
                            'ӏƿѦцˑщ\x9f',
                            'ϿЋȼ˾τ',
                            'ƜȓдƸr',
                            'Ǡˠҥ҉ĆȰοǥЋ',
                            '˻ВĬѷмǲ',
                            'Ì',
                            'х¼˓ż$Ν',
                            'ɳԉ',
                        ],
                },
                {
                    'catalog_name': 'ʄ~ЄîҝҔŧ=ƴν2ХâµʅИɻªǏēȚƧȘȗʨӻʝaΠĬ',
                    'locale_codes': [
                            'KˠԞԆȲѵɊϧѩ',
                            'ѲѺ˭9ƹ',
                            'ԪԄȵQ˜Ɩ',
                            'Ȼ',
                            'ɊԛȄ˳ˢÅśУ',
                            'ɭąȹʯ',
                            'ÞȲҽ',
                            'Ʌǃхj',
                            'ȇЕ˗ВгʫԚΏ\x98O',
                            'Ѫ',
                        ],
                },
                {
                    'catalog_name': 'ԓӺ͵\u03a2ɢҷԛ°ʋӸƥЊ҉ǲƃƠmϨҾɛŽИϔ`іЈӎǪҚҘ',
                    'locale_codes': [
                            'ηÊʈęž',
                            'ˉĕχҁƮ\x82λ',
                            'ʊ§љӤί˓Ŭ',
                            'įȲȖϔˀ˦-',
                            'ǖűóˀʨſяɖ',
                            'ɃʈnAÝ',
                            'ΓҤяш',
                            'ρԣӸ',
                            'ӱлӜğ',
                            'ʭӇĀɄǬȆƧѽϣ',
                        ],
                },
                {
                    'catalog_name': 'ǀҹ!Ӥ£ƀҜбҎӚǒđʖɘͻӅæѩӖ˔,uҿНϦӎkȺҶH',
                    'locale_codes': [
                            'ĘҎņLÂƺԘҙĩΔ',
                            'ӂҩѼʙǶxΜӰѩ¡',
                            'ğЂN¥ʋ',
                            'ʲLԭӮʒɳzҰ',
                            '\x93qeȔκљŉҐĳ',
                            'ʌǾŮӃûɛşԠӯ',
                            '\x8c',
                            'θpsǫҕǙѡҾ',
                            'ϓ',
                            'Hύ',
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
                res = i10n.Locales.parse_data(test_data)
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
                res = i10n.Locales.parse_data(test_data)
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
            'name': 'ǎͳĳȚΓѠʰӗíğĞƽƙȠӻȐҨǼƧԚpаÆөǜҝ\u0381пʘԥ',
            'code': '0\x93ɑŀĴƪʻˣϳ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '˹',

            'code': 'y',

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
                res = i10n.LocalesState.parse_data(test_data)
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
                res = i10n.LocalesState.parse_data(test_data)
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
                    'name': 'ǼĈɨÓȠЀʔю\x83ѕðԘǼʝĴˮȬſε°.ӘɜЙҔύǶɋԇͱ',
                    'code': 'ÛϣΰѝˆĒҏɸ"ԫ',
                },
                {
                    'name': 'ҭ˺ɛȌМ҉īɐȌǙʏӰſȟŢãƒӀ҅\xad\x91ԙĆȣΓʥ÷\x98Ȉӥ',
                    'code': 'Ч´',
                },
                {
                    'name': 'ƈđϒӾƌeҎ˄ɱ;ЏϞƃșί:˼ɧ˙ÿāâǮεªрƲǳʺ\x84',
                    'code': 'ZЂʹ8Σ6',
                },
                {
                    'name': 'ԣþјX¶tȦѤɮɠ¡ȭĸђ¡ύφͶѥƈňҪΝíƁ˘ɢƥŉу',
                    'code': 'ӅļԘ¡ǋӫ',
                },
                {
                    'name': 'нũǃƓƬ"ːƆӿԫ:xɺWø\x89fԑ\x91ùɚˤȞΫЏgР2Ŝͳ',
                    'code': 'ί·ˠҒ',
                },
                {
                    'name': '*ҥYƈЌԙȽЅЛßϼԅŐГdɒʼԙĶŷĥʷӌӠΏɵңф,O',
                    'code': 'ԪĮΑϥЯ',
                },
                {
                    'name': 'ǀԁ-ĥΆҖ˻ˎΏԐ%ɂɡɊҠӟ±ʻȀϼ˄ȪƬûńĉ±ǌБǍ',
                    'code': '˔ķĤʫ\x90@ȷʣÕ',
                },
                {
                    'name': 'ÏÊл˼xҳҼ˔Ƌҏ[@ЇѡӲǯκǐ\u038bƶ\x87˧ȤӶʐʎλʃżȾ',
                    'code': 'ȿςˌӀŜяƈϫcȯ',
                },
                {
                    'name': 'ьΤǫ$įƕƆ-',
                    'code': 'ʑçʧTĵʭή˄',
                },
                {
                    'name': 'Ťŧήѽö˻aǲ=ЮƘœƎƨЫŅХ˽˃ж\x7fUžѾҮКќʆŃĽ',
                    'code': 'ԋȺϣтɓͳ°ϓϙ',
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
                res = i10n.ActiveLocaleState.parse_data(test_data)
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
                res = i10n.ActiveLocaleState.parse_data(test_data)
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
            'locale_code': 'ιɼǶɀŀ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ǹ',

        },
    ),
]
