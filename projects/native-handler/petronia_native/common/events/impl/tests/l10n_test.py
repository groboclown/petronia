# GENERATED CODE - DO NOT MODIFY

"""
Tests for the l10n module.
Extension petronia.core.api.native.l10n, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

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
            'locale_code': 'ʩж',
            'catalog_name': '\x93|ŋĘπӜR\x95ӎ\x8d·\x86ƬԖȏΪɉǬı\x92ԏƻГÿƗԤνɎѲ\x9e',
            'message_file': 'ȍęǉɺƕ\x84\u0383ÄѡӹӄЋӊŋӄǲ$ǄÞĺĺӹҀ΄ӋŜ¿ȆŰԫ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': '`',

            'catalog_name': 'c\x93Ă',

            'message_file': 'πӮ',

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
            '$': 'Ѧ·ДȬͺӒd`˶ɕЭřТçТÄԋϟƦӷÑyʫϳŗԅѴЭʯ´',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 6378563694642843895,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 582375.513051933,
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
            '$': '20210327:034312.711266:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ѤΗäӭȶӷѵϟ~ɹƏщПƈ#PĩϽΤŷņЩßΦʨԏóvԝѰ',
                '˪ˆӣƇϮʞȚˠŔҁʏʢюʕξŷЁ¥ԟΓǊǵΌĄϐĩñ\x9aԏ˪',
                'Ý˷ʏϵžťȀĿӆЅÐ\x81ȣѣ¸ûы³ĜĢʷ½ҋчоǓӭȗˍƐ',
                'Ǻ}ѲнÇŒ8Ǖ\x9dԓȴ{GŚǺȆ]Ьɣ˅ӺϣȒ˺ѶғʿɤґϨ',
                'ɌÁȖYԢοɚШԮĕïϜӃσȚ!νϭiҬғ¬ǃ\x8c˸÷ȍЫ>ҕ',
                'ϔ¶ɝѦȵȨνǭϻΪƍǽțŲȡáĦ>ɟȰsӌƑҞȺEʑΉя*',
                'ˮ«ҐѿɪϋϋҠΏàѿŧИǹȺȾʳҎԌХɝӃęҰƚѼǖǊϷƓ',
                'ȰȴűԜʲȼϞұÖdĀԍҡ\x98ȀɶӖʃƃƅԖӅȲҽѰįԩӬҀƱ',
                'ēΔӉÙӠʳҕԄŌɂΑҰԫԌĄ®ԅӔѐѥȘ/ľΈǐ&\u038d2¿δ',
                'ΝĭϧΐƺΑWɫg5ѪȰĆˮфԄɥΎγχԫ\x82ӹƴҠЅ˥ɫŒϨ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                2565345171419878934,
                2913320857828595344,
                -3388164186830782210,
                -6340587336635118059,
                7258412844793066772,
                -5773558261179444312,
                -5496524772548418716,
                7169977417547195471,
                6230293114464436045,
                -1791223727786039194,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                954888.3911527374,
                69459.03938444599,
                525065.1476683688,
                106916.91734232544,
                750404.2194745935,
                995977.9298682592,
                835092.4986665428,
                47072.89379882271,
                544989.5864927905,
                694016.8939659786,
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
                False,
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
                '20210327:034313.715939:+0000',
                '20210327:034313.735038:+0000',
                '20210327:034313.751760:+0000',
                '20210327:034313.769265:+0000',
                '20210327:034313.786098:+0000',
                '20210327:034313.803308:+0000',
                '20210327:034313.820183:+0000',
                '20210327:034313.837172:+0000',
                '20210327:034313.854261:+0000',
                '20210327:034313.871087:+0000',
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
            'name': 'Ơ',
            'value': {
                '^': 'datetime',
                '$': '20210327:034312.449388:+0000',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ϥ',

            'value': {
                '^': 'string_list',
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
            'catalog': 'ѯƻӐɖů\x9bŸЇβƣǳ˾ǼіΉҐʲɴ\x88Ǭåʅ˂ɩѷ,ʷȿѤҝ',
            'message': 'ӷ3¤ӔƬӅӶ-ӟîȹæҎ¥лʢǾ8(ȣԕUӄʬƦʒӻҍ_ɧ',
            'arguments': [
                {
                    'name': 'ѷÉȈƻ˚ɵ˼~»Ʃԑ]εѯӔϼэéĻ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -7879713927714272617,
                                        -8474007679837285914,
                                        558602888753390285,
                                        1450416132961010361,
                                        -4096962488532039809,
                                        -8473942572843142008,
                                        -8617419921494985266,
                                        4225459249674703846,
                                        -1812587894541776027,
                                        8956661409071072508,
                                    ],
                        },
                },
                {
                    'name': 'ƌʵǬ˓õ7ԇЭͻȗ\x85ϫúŧôϡҮԃЯιȸƭ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        True,
                                        False,
                                        True,
                                        True,
                                        True,
                                        False,
                                        True,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ˍӪ˔ɞИӬ\x99Ēˍŏ4ãԟ;ÛӀ\u0383ĦǽѱǎȼďBɮз×PǝҤ',
                    'value': {
                            '^': 'int',
                            '$': -8302833652284600326,
                        },
                },
                {
                    'name': 'ҭ\xa0Æŝǌϧ˓ĩԖCŀҎĸìӹȚԘǢŔ×Ǥԅe\u03a2r¡ΦMŭί',
                    'value': {
                            '^': 'int',
                            '$': 194131670874675759,
                        },
                },
                {
                    'name': 'ӱÕщɛă',
                    'value': {
                            '^': 'datetime',
                            '$': '20210327:034311.384312:+0000',
                        },
                },
                {
                    'name': 'ӗ˳ӔźȮѪÖԨˑ¶ɠʕŚǽĨ^tɒǍӑSǾ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        8392311275427568622,
                                        -1028039845577516334,
                                        -8125802763580998061,
                                        7725795422673404047,
                                        -987131378417776777,
                                        -633365193064333907,
                                        -3234889596625005298,
                                        -4818317311178460653,
                                        -5646908694583283768,
                                        -3846477734048944125,
                                    ],
                        },
                },
                {
                    'name': '\x80\x8aĎҽҼĐ˲ѻǦǉʔψƀĵӻǄ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210327:034311.698255:+0000',
                                        '20210327:034311.720975:+0000',
                                        '20210327:034311.744406:+0000',
                                        '20210327:034311.771870:+0000',
                                        '20210327:034311.796810:+0000',
                                        '20210327:034311.820130:+0000',
                                        '20210327:034311.839746:+0000',
                                        '20210327:034311.859873:+0000',
                                        '20210327:034311.879789:+0000',
                                        '20210327:034311.900100:+0000',
                                    ],
                        },
                },
                {
                    'name': '\x9aßɁϘ@ǹʴųĮћµƶҧңƱʩӸŊƑʧȍƧĦ˼ҧț¨Ӟ˥Ϟ',
                    'value': {
                            '^': 'float',
                            '$': 994695.1577357722,
                        },
                },
                {
                    'name': 'ϟĒНȊʹпϧǹČΨǯǝ-ƙ\x8dϕƣԁ»Ħ˄ĥΏӆϷW҅Ѫųģ',
                    'value': {
                            '^': 'string',
                            '$': 'ʿЧӮʺɬԨǃɎƄɊЕ\x97Ƥʢΰ²˃˪ƌƋ`ҨėЗÈ1ŤҰϬ\x89',
                        },
                },
                {
                    'name': 'Ρό\x8cЇ˟ѓғеҭӮʘtͽîÈ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -7289815473652461929,
                                        491454778884357833,
                                        -1817872042355868038,
                                        -8133459140333103717,
                                        -5209110241018828085,
                                        -2100039228196999995,
                                        2836499754751201776,
                                        -8224991981784574673,
                                        -7985014414242542671,
                                        -1077337921054089212,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ÿΊ',

            'message': 'έ',

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
            'identifier': 'һ\x9bǒϐʖЖʀÝʇ˩a\x97Ӽ\x9cÅɅ¸ӊлҌϨßΧ-ӱȝȬӕƞζ',
            'categories': [
                'access-restriction',
                'network',
                'internal',
                'configuration',
                'os',
                'os',
                'os',
                'internal',
                'internal',
                'invalid-user-action',
            ],
            'source': 'җΡҞhɲŠҍɨǣŮȔǭXƒǂСěȫŦöʪzˆϽӁ˕+ϰћ\x7f',
            'corrective_action': {
                'catalog': 'yҫ©ӿϖÈ)ʒ\u0382ђϧYПνҗ',
                'message': 'Ҝ#ӕȴ˝ɝA#\x98Õ\x8fԕӼʯηΞҭӱЩҥXLҖҸÿԬPŞ¥Ĝ',
                'arguments': [
                    {
                            'name': 'ɑӴ·ѐģ\x8eŚ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        983349.2525788909,
                                                        427658.7272389877,
                                                        822188.7082575706,
                                                        186962.8156688151,
                                                        455766.64829395746,
                                                        292719.9579745115,
                                                        779009.8981001994,
                                                        831153.5911222287,
                                                        530331.3275550366,
                                                        490600.5152072018,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ҚÕɵфƯԑѐȪʎѡ¤ѕ÷ȿ)ȒB˩ʍƄҸvÃϵӣȊ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'Ȟ\x86®ƺЅʅĽƿøɗƻԡʾ͵¹ʟǮŃzҳӐȂ\x8cƥƂʂδǌ҃Ѧ',
                                                        'Ō2ǈΙʱƙŭȖӼǆТ˝ΤʰɾȅѐЅϗѳȻώʖʹƓ[żȊüę',
                                                        'Ӻ˺\x8cς҂ϼѬeǾǺϵҰƓƂԒƌ҃ΔҧԪҮҦԏυƻȭΨÙÃƸ',
                                                        'ӊȤľԞѷµɆԐȝΟѰЛü]åŅ҉ƚʨ¼İϬ\x9fģ|ñǬŢʹƝ',
                                                        'Őĺɟ˅ͱȄϿĭʶťʛơŃ*ʩɧ<ŽѳˊƖϡҹǓʡΓ ԙŝȨ',
                                                        'ɜʡ^яȬĤʱùϾΟ҈ѲŜÆԁϗѢѯҵEʿўV΄ĊҦàŕҦ¼',
                                                        '΄nïHɝ\x82ʾвƭσҞĸƕͳљǜñѰЦԁōȚ8%ѽ˺Ҙǚgƾ',
                                                        'ÜӨϸƋӝуĸŪ҃ҦR˽ƄĹүѷ|Íǚ҃BҕѤåɜӏԑǾ/ӕ',
                                                        '˜ÁŪjÀƎӜˢàʿƭȳ·Ćќѯŏˉ˭ŎɜӮҠʼ\u0381\u03a2җχξƓ',
                                                        'ĸūɒҋǌνѽ±эϦžΖʀѵ°ӕΎ\x9aΕŪ¶3śѬҨʿŖʨϫ\u0379',
                                                    ],
                                    },
                        },
                    {
                            'name': ':ȌәζzóӄβȤeӒЅΫԊɵȨΥв$ëϢԥ\x93\x9cѲˈņͶĕԏ',
                            'value': {
                                        '^': 'int',
                                        '$': 7672195310998694911,
                                    },
                        },
                    {
                            'name': 'ˊĞȖ\u0379μІrӰтȓʧԁʦĚнWΉЈʋԏgɥˡʾӽȷцɲҊÔ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        119360941394767044,
                                                        1170767301395833474,
                                                        9042769856105903406,
                                                        1345662520892263981,
                                                        1721326518003380353,
                                                        -9092200605524587144,
                                                        2079137090375177846,
                                                        -1612963270056596468,
                                                        7365374814096061192,
                                                        2442241543343775919,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ɪjңƜǹćҗƹßҏ6лА ȥ΄˕ƻ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210327:034309.033894:+0000',
                                                        '20210327:034309.053813:+0000',
                                                        '20210327:034309.073301:+0000',
                                                        '20210327:034309.091976:+0000',
                                                        '20210327:034309.110217:+0000',
                                                        '20210327:034309.127986:+0000',
                                                        '20210327:034309.148103:+0000',
                                                        '20210327:034309.169665:+0000',
                                                        '20210327:034309.196938:+0000',
                                                        '20210327:034309.215193:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ˇԟƻӨ˃Ã;ȃɠȚrί˖еȀĳưϲĂѲȴĬǨҠrщ£ϹΞҤ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -2718383562553281136,
                                                        -5674084561901374227,
                                                        6842836603220627435,
                                                        5940892661497913653,
                                                        6369972743547322470,
                                                        -3760373236113556737,
                                                        7737986982330230027,
                                                        -8178612876951107275,
                                                        -2809835785540608325,
                                                        -4038794936460394396,
                                                    ],
                                    },
                        },
                    {
                            'name': '\x82ЛτɝÍͺȦɉ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        False,
                                                        False,
                                                        False,
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
                            'name': 'aȆƕΓǏõδʄԚИϛŽàȅГǿÎŅΞŜǦ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        542450.3110909192,
                                                        599681.764102292,
                                                        612570.0320285242,
                                                        375887.761823779,
                                                        681125.6644686335,
                                                        600705.0996101014,
                                                        128509.58531941753,
                                                        200074.47004093818,
                                                        356951.58847858245,
                                                        303543.8351978897,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ҩѫƇ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ӉӱƎĻԢ\x89ÿȚϞɜқąǻsϦũӢυ϶eѫ˟FΠŐƥFơŘϒ',
                                                        'ʘЄԊпȭ\u038dҠгǇёʙēƣĤӁMӍ`ҿҢɵʥȨƛĈƳ\x89ɞҥD',
                                                        "Ͻ\x9cňφĠǪµӥǋǻ*ӫ˃ӀþΆ'GѨѣʳӭ»úɌϋȞʔϹƍ",
                                                        'о҄ÑҤϧɀƅʱέRθ6˭ţ\x9fȐ:ƙƷƿϚЎǴȖpNͼÇЬ˧',
                                                        '˺ǡʞƵŬQӝʽʞòχαлÉɀéҽʳÚȨя·˅Əʣñ΄ʖϦ˲',
                                                        'ЫqʌæˬƧӵwƴ`m͵oԏѣʜɏ\x8aҶ\x86Âϧ˩ΒɖҋԨǨĞʂ',
                                                        'ɪŶ˺ƍˊҸґüҽċӄӮ˦ʐ\x9fΠ˙Џ˕їʉˬʝóêǹǫǒӦŉ',
                                                        'с\x95ʜʵǌϺЎѾǷ©˲пŴ˅ƴѨDѨƑђΓɼʢԀĉ\x85~@\x91ɀ',
                                                        '҂ȕ3ěȷO\x99\x90О\u0379ƹјŒɮЁȢɻҁ*ёɖİԮzшã3ȏǝЀ',
                                                        'ӭ®į˟\u0379žƌȣӯʿΆ¤ϠŅʋʏӢҨɇħȀƩԡр÷ŏӰʁѳƦ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'łÑϟñӝвŚĒͶ\x8f҅ΤʵЕЉ',
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
                ],
            },
            'error_message': {
                'catalog': 'ɵ£μͱҢţώǣ¿Пɔī\u038dЫȋʋ$ӄўĞɬҬɬԠ\u0380ŮŅrιȋ',
                'message': 'ǚЄȏԓȁŃϡȥˠȣȅȗyΓƎĹÔң7ȕưҫZʹϏӑýи\x9cӭ',
                'arguments': [
                    {
                            'name': 'ɧiƧèěϏ7ǼĪԤˬĠƄ}ҷҺʌɽЬ҄ɡЦ_ЕԎМ',
                            'value': {
                                        '^': 'string',
                                        '$': 'Sʚ\u038dƿЈɨġАǤʙώδńҖԥɯɋөĠӃȕʴӮğ˭ќǆšԘÝ',
                                    },
                        },
                    {
                            'name': 'ѲѺϢԍΕŠǺľW˛ǪzҚ҄ѫƪÂӭʷȧę@tµѲª²Ľϟƛ',
                            'value': {
                                        '^': 'float',
                                        '$': 951294.8196334483,
                                    },
                        },
                    {
                            'name': 'Ѷ\x8cƩИ®ΫŨƳƾԃХĪπÆё}ĝӭі ȪхБǠƢÛΰµŨ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ǩϙǐϧǑѪvѧʧϝĚȲԮǽɋσìĭȸƆʆŬӰе\x8fǫŗʥkĹ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210327:034314.324071:+0000',
                                    },
                        },
                    {
                            'name': 'ƞőƩǫљ',
                            'value': {
                                        '^': 'int',
                                        '$': 1076366776906872275,
                                    },
                        },
                    {
                            'name': 'ӢùɈԬĘə˼íáÔėҦǼҴǅɳϞ҈\x8aοҫрǜ÷Ƹԟ9γĎ˼',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210327:034314.464440:+0000',
                                                        '20210327:034314.486997:+0000',
                                                        '20210327:034314.514763:+0000',
                                                        '20210327:034314.543286:+0000',
                                                        '20210327:034314.567510:+0000',
                                                        '20210327:034314.587344:+0000',
                                                        '20210327:034314.607783:+0000',
                                                        '20210327:034314.628368:+0000',
                                                        '20210327:034314.648253:+0000',
                                                        '20210327:034314.667343:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӘȅȹŘåŘ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210327:034314.768545:+0000',
                                                        '20210327:034314.788990:+0000',
                                                        '20210327:034314.810538:+0000',
                                                        '20210327:034314.830653:+0000',
                                                        '20210327:034314.848670:+0000',
                                                        '20210327:034314.867631:+0000',
                                                        '20210327:034314.884281:+0000',
                                                        '20210327:034314.901211:+0000',
                                                        '20210327:034314.917831:+0000',
                                                        '20210327:034314.936325:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӱȴѫƬʖ.ƟђƎΧ=ĝͶβYȿΝŮǲáԪыͱ¢ҝ\x8eүӴ˵Ʀ',
                            'value': {
                                        '^': 'float',
                                        '$': 919268.3491953716,
                                    },
                        },
                    {
                            'name': 'ĥʝĬȐȢӂќɀƟǽυΫȏҘʓкMԕzǝҞħéȆ;ɽEΝæҋ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'шϔϸɆOĭʛ\x95ɻԁЬŐïƷϭ¸¨ԡʉßҨϡÓԢŀΧԆϾ˪˲',
                                                        'íçöΊæ˒лĭqҒōǠϑƆd\x94ƐȚYķȩvұ΅Ѝ\x88ѕђύҺ',
                                                        'ѰυӰΦȱԒʻǷ\x86ӞƢ˙ÉƦȨʙҳρȝ˄˾ŕҗˏâɖǢјʼȻ',
                                                        'ǣόYσˑȵɼςčĎΧΨƷϐЙȢвǾϷ·ЫŮǩ±ҼǊÃƝǽǦ',
                                                        'ϰưәŔΟӑв\x8cίЭåW\x82ɀԧҏʖЛɅΊԃҍûǽZŗɵǀԕΓ',
                                                        '\x88ʹ˖«ԦĉА˻oԎѐА½ŧ΄\x99ΔĲθμҾѪпџŽŐPƵЈ\u0378',
                                                        'ǴԖЩƀ˜ʫŠ\x86ԨůѦýѧЭлАpʲČŖԧԪâʓƔԚɸҔӜҬ',
                                                        'ůӉԈǍԭэȣɁʠǮÌ¤ӓĈǟ˭ҦÞǲďƾɯϧљƳФŻƗԗǔ',
                                                        'ӒđϏȹ˕μ˜ɰɐӋăçƝȣėҔȷ[įuΎɃǹѡƾˉjmĉΖ',
                                                        'ɵɋȊčƈŌϡʿũήԈуӼǹИµƎɻϥƁǘǠΧ҂ɠöҠͶĬ\x96',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ґ´ʪÌаУњȋƀ˽ɏǰɋ(üƹӞǊӒрǍѓͳǹʈǣęƜͿŌ',
                            'value': {
                                        '^': 'float',
                                        '$': 602464.7526339869,
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ԣɬ6RР',

            'categories': [
                'invalid-user-action',
            ],

            'error_message': {
                'catalog': '҈ś',
                'message': 'ã',
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
                'identifier': '\x89дԕcˮƶȿĴҖ˵ŕ\x92\x8f4҇ƺfˌØѠʺΛÛȺԆΣ(ŽС',
                'categories': [
                    'os',
                    'configuration',
                    'network',
                    'configuration',
                    'os',
                    'network',
                    'access-restriction',
                    'network',
                    'network',
                    'internal',
                ],
                'source': 'ŻɺƕЉʑЈƷàQCеȭО˙υĻČϛԏ˛ҶУϘĩĢĒŁƸ!Ѣ',
                'corrective_action': {
                    'catalog': 'Ť\x84ϑbůϸΗƪЛ Ɵɪ2ƔэƲ˧ԈӵȪ¢ΨεԨϘʄŏΝѡ²',
                    'message': 'άϖďѮԒUӨЛ҈ĪʅϿÒ\x95ʝԆİƴɠОĕмɤϝԌо˕Ҁʔҿ',
                    'arguments': [
                            {
                                        'name': 'ƬóɻԆĳӥҸȲ³ĄҎǞ˒ϩĭƍѦΚϨ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ѻǩ҅ƭʌϴϼ¼ӉϒѤǬǪ¨\x8aЬԨШŕ{÷ǜύϫҩʜĵÅ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ĵ˹ӡОɕˤɜ¦ʿůЋȌÆΦĒɪ͵ŴзƘĳÇԉДͻ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 961192.6208011771,
                                                    },
                                    },
                            {
                                        'name': '΅ŅНʙΥƗҁҽԋƷʚХ˄\x8dԏή˽Đ4ͶЁδϠҐ;ɐ˹',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034305.491839:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʀŒ\x88ŔƟ˧ŏ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034305.560274:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҙ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -89129.77616445234,
                                                    },
                                    },
                            {
                                        'name': 'Үǃǖɚ˹ӊԘ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            817877.6486719567,
                                                                            633430.4923382045,
                                                                            -47290.826969342306,
                                                                            -7284.910933238192,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȰІʔŋ]ҟɛ¡ˆǂɐqГē˱ЎΡν\x88',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7182366934478236553,
                                                    },
                                    },
                            {
                                        'name': 'ʑŇȗӗяˢ˻Ԛϒƃ˛ƂÖǳӲŵÂȢŉŴȘΖŁψԑˉѿʵͼȮ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 958958.9973650798,
                                                    },
                                    },
                            {
                                        'name': 'c',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 169772.37499078712,
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ůȃσXĲ;ʼá~Ƨуο҄ҐȘэǪΓΛžұ³æѬXϠԏ\x8fИϙ',
                    'message': 'ŹɪӮѫțƫɭΤʙĸӦaϬʉƖˡЂԪУ˱҉ÙѮϓƋ·˷ѠԮŕ',
                    'arguments': [
                            {
                                        'name': 'ʩ˪¬ԋʗғԨŝƆ_Ɉ1ӂŒY',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034306.109219:+0000',
                                                                            '20210327:034306.126255:+0000',
                                                                            '20210327:034306.143040:+0000',
                                                                            '20210327:034306.162268:+0000',
                                                                            '20210327:034306.180103:+0000',
                                                                            '20210327:034306.197772:+0000',
                                                                            '20210327:034306.214875:+0000',
                                                                            '20210327:034306.232312:+0000',
                                                                            '20210327:034306.249450:+0000',
                                                                            '20210327:034306.266546:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'šǆԏeγʣëʋɭĉBȴÚѡȭϠʺЬǤʩƴʡҋøKЋişѫɵ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034306.365191:+0000',
                                                    },
                                    },
                            {
                                        'name': 'зvЅΘĪċŶуӝ˂˙Π˝ąȟùMːɚԚȻϝҷ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            283168.43032315635,
                                                                            734428.5196930895,
                                                                            157940.79848360005,
                                                                            957569.8865116308,
                                                                            585000.7632586182,
                                                                            444342.99348562676,
                                                                            929644.5294777531,
                                                                            346597.9421956354,
                                                                            585795.656839724,
                                                                            198425.73130221356,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӟĎɪD˵ˇҊҎѽµƾƽĽѰé˞ԮûĜʋœ#kÿƊƼ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            770018.7447040139,
                                                                            432624.362801353,
                                                                            807096.9411689694,
                                                                            798335.7838634942,
                                                                            692120.1387084977,
                                                                            156995.36115050068,
                                                                            268568.42432639335,
                                                                            603760.817037685,
                                                                            254217.60107092635,
                                                                            333483.87572195946,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'rƩфк\u0379}ӔY΅ǚ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҢőǊɿϒɨōįΞȅЗŽϯһпҕłāыÀȽÜԅѧӮҶ\x8eӋNΥ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034307.005738:+0000',
                                                                            '20210327:034307.022432:+0000',
                                                                            '20210327:034307.039207:+0000',
                                                                            '20210327:034307.056532:+0000',
                                                                            '20210327:034307.073389:+0000',
                                                                            '20210327:034307.090487:+0000',
                                                                            '20210327:034307.107067:+0000',
                                                                            '20210327:034307.124180:+0000',
                                                                            '20210327:034307.138652:+0000',
                                                                            '20210327:034307.151508:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǔйʶү˧Ή¦\u038dҳϛҸԎ҈ӃǣƔ\x94ӔȅѶЄϼ*',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7772792419129845880,
                                                    },
                                    },
                            {
                                        'name': 'ҢɥӈƏĆіΝ˙ǳ˅YԚǹɨ\x9cșŖήȥoˑϲǚˀў®Хșĩѫ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 317258.00373564067,
                                                    },
                                    },
                            {
                                        'name': '˽ÞʭЗϨǿɓʞϑƂĔʂ°è;¶ÈǤɮόΟˍξĔÚʪβ˽ʉ»',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 728301.0223063233,
                                                    },
                                    },
                            {
                                        'name': 'ʲΠљχǞЖˉȉɠӏӻƆÐϤʇϘԣƑâĶ9ǩҒ:\\ěʑɊЅɕ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034307.408226:+0000',
                                                                            '20210327:034307.424914:+0000',
                                                                            '20210327:034307.442825:+0000',
                                                                            '20210327:034307.459730:+0000',
                                                                            '20210327:034307.477368:+0000',
                                                                            '20210327:034307.495297:+0000',
                                                                            '20210327:034307.512819:+0000',
                                                                            '20210327:034307.530124:+0000',
                                                                            '20210327:034307.549398:+0000',
                                                                            '20210327:034307.566539:+0000',
                                                                        ],
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
                'identifier': 'ȧȓaΥё',
                'categories': [
                    'file',
                ],
                'error_message': {
                    'catalog': 'ƴΛ',
                    'message': 'ʙ',
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
            'locale_code': 'ѠƷ.à',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ő',

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
            'catalog_name': '5ÅɒІҎȘʗŌH˪:aȖǶƿбȌͼѨǐƮҵěÖ0ɥ{§ɑн',
            'locale_codes': [
                'ѐ',
                'žЙѦȈ',
                'ȚҴÜŎΐ҆˙',
                'Һγ',
                'ːƶğчT',
                '˶ԠˢĄƳѯɘ\x8dĞ',
                'œ¤ѵęћǃхԩ!ѥ',
                'ϥżȰƕ',
                'ǹʯǝɀΌѮéȭл',
                'Ȣ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog_name': 'ѪÚǚ',

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
                    'catalog_name': 'ήąҌԄǉӨȘԩËһƎΘ˒mȐɒʻȉѝΪȏ§ԔśbƊȳ҆ŲϷ',
                    'locale_codes': [
                            '\xadɇԊȀϲд',
                            'ɦpǜŒԊǃ',
                            'ůĤÔѱȴ',
                            'FЖ¢¼ŋRӺȳѧ',
                            'ǁʁļ',
                            'ҢǩъĘ',
                            'ʋѨ',
                            'ůɗ\x8fȻöѫÌ',
                            'ӻòԁ',
                            'ƾԔЌ\x88˶әцë',
                        ],
                },
                {
                    'catalog_name': 'ǠĻωúӒЏȶĂҔӒȓҮЩыɖęǄвɤΡҶσФʂԎƻʝΨ;Ѣ',
                    'locale_codes': [
                            'Ѱʤư',
                            'ʟ',
                            'CѐΖȣԗϼԒH',
                            'Ҥӷɒōʦʉů',
                            'ȥÆӨӳѼU·ԦӾʭ',
                            '#ӛ\x95ɖ',
                            'ģĒāЍÀʋ˹',
                            'ØԦξӗ',
                            'ЈȬ',
                            'ҌҳιёɷȔŤƋ',
                        ],
                },
                {
                    'catalog_name': 'ƞѕҵϮƪqʾчBԚƷʴʔξǢӠʨlȽ\u03a2ԫсҼϫŔIʒЙȲΔ',
                    'locale_codes': [
                            'GŦ',
                            'ԏŔѼʇǠ',
                            'ȇ',
                            'ђ?˸Ԅӡƫ',
                            'ѬɫαϦοХΡŉ',
                            'řҪ˴ʗ',
                            'ȳ',
                            'ˠΏϣҏӶҽʸųͽ',
                            '9ʃ',
                            'ʣ\x9eʉ\x9cԙɤ',
                        ],
                },
                {
                    'catalog_name': 'pǓVѺºĠFŘȞҠԞ\xadɤӢίː\x98Ƽ˯ěѰɡФѬʜĮŞЬϸҘ',
                    'locale_codes': [
                            'ˊ¤ʞӹʟԒůϣ',
                            'OțѼ',
                            '5\x84áЙЅȾȮ',
                            'M',
                            'ķω!ǊЯϛ',
                            'Ϟ[ҷȣŚҼϢāҘԩ',
                            '˦ɊмȱǵԆӔį',
                            'Ĳʜω˘ʗĶǃƞ',
                            'œ',
                            'Ϧȯɒ',
                        ],
                },
                {
                    'catalog_name': 'òǛâ\x87ԌƃҹŀΫНĜϬǰȔGʟɔ®ңȻÖӜԝ\x82ĞʵÌęKŸ',
                    'locale_codes': [
                            '\x7fУЊπ',
                            'ϟӑ\x7f҃',
                            'ưòǠМ',
                            'οÒѲǯÛ',
                            'ОԀ',
                            'ʻ',
                            '\x98\x9fą>Lѵß',
                            'ŬŘ\x87ȳǧʣjƤƻ',
                            ')Ʀň~ǣДϗ',
                            'ЯлԞѷÏƾ#ѵΑп',
                        ],
                },
                {
                    'catalog_name': 'Ӎϴ4ɔŗʫéѯѢΥŹԏ˷Υӽɾ˟гÔêʇљľԩϗÂѱȊέо',
                    'locale_codes': [
                            'Ƀʚ',
                            '·ƌƒʮΉǪüн',
                            '\x9bЉӰƽϾ',
                            'ΰьФȑˮҦƩ',
                            'ӍξJɡ',
                            'nҤɃ',
                            '҈Ɲþѵ˅žәɵ',
                            'ȿȐÔΗŖférФ',
                            'ȘϚЪśΩ',
                            'Ҷο#ĖΟƠҺ',
                        ],
                },
                {
                    'catalog_name': 'οĝҐзѫˏčÇɾ\x98ˣġυĎlϽjĸʄԘsĵαјɧοΫƥļŸ',
                    'locale_codes': [
                            "Ԍ'гҝǴӜ",
                            'ƢxґԛŬĩӞȆ',
                            'ɪ',
                            'Ǌѩëɀä',
                            'ˡΤΕԁή',
                            'ȩǀЮȖʣKЙýŜǖ',
                            'αĬĄĀ҇ӗΉ˩ũő',
                            'Ұ¥Ňϕ',
                            'ԪȴǑĜ϶˖ʽɟЬ',
                            'ƕˑaӞԓϛµİ',
                        ],
                },
                {
                    'catalog_name': 'ù˨ȹɷϷʿ\x93ОĜŮłďƉ˃ÎȦОɀÄ',
                    'locale_codes': [
                            'ґѓ',
                            'ӆʲϚź',
                            'ʥҍԬØ\u0378ħй',
                            'ƺԃ\x80«',
                            'sƓƨΚ¼ыöԆΛ',
                            'Śˍ',
                            'Bε',
                            'ŕ',
                            'ЦЖ@ӁơɉˑԭϨ',
                            ',Áǣ`є®Ή',
                        ],
                },
                {
                    'catalog_name': 'ԪÔ§ԤλŀίmTҍ%ŨѤĥԁźӄƑԙTǎƄӦ\x8cºƁȄƼ\u0378ȫ',
                    'locale_codes': [
                            '4ːΛǣ2ѴȍӜ',
                            'Ίэн˛ї',
                            'ɜŲȀ',
                            'ΏŌɸȀƉЗАЄƠ',
                            'ŔӄȭӡԍN',
                            'ŰΪúϖɓĜǳϜɠ',
                            'ɆˋX>]έ',
                            'Ϛ\x84ŊΠ\x82',
                            'ÚRϨƴƀ',
                            '҄ȼѐòȏŁȰ',
                        ],
                },
                {
                    'catalog_name': 'ԔƵӨʅĖаЮϤɈȦϟ¸ƝĀ҇=f*\x93ŕŬԁӻҎœŨâǮόɻ',
                    'locale_codes': [
                            'ȅӬυΠ',
                            'ЇΜǨ',
                            'ˊТŔóňǩЍ',
                            'ƣҴ',
                            'úƨϐĺ',
                            '\x83\u038d',
                            'ԣ',
                            'ƾŞ',
                            'ƗϠɞšҡ¢',
                            'Łņ±',
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
            'name': '˝ĳΕƽ,΅ʠú¼ΏΞŁԬRŜӯɨȮ҃',
            'code': 'ԁÏǦЛ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ɯ',

            'code': '\x98',

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
                    'name': 'ЇϱȞÎjŗΠʫΐȻǵÔҟʁDԖàʅŝҘΞƈϘРĩЉÕǟƢӥ',
                    'code': 'ɩȽ',
                },
                {
                    'name': 'kéuǎϙƟƯŔŵ˺ІҲŚÛȻņͱðҾģŖɦ¦ҞԙƮѝˀϧʱ',
                    'code': '҈ŏ',
                },
                {
                    'name': 'оԊϓřǯЄΖҋ\x9fіεЌǨЎġΔîÆī\x86Π˭ȴşǅĊԛǗҀ\x98',
                    'code': 'Ҙr\x8a',
                },
                {
                    'name': 'ʼҢά¨\x91œȰГҁџkԩѺFҎΞӳēϣϝЂΞǸʕԡӌшѳī}',
                    'code': 'ԬǀiѮӲͼɒ',
                },
                {
                    'name': 'ˁAǒģĄÛɍӔŃҺPϺǶю˼ʾÀ;ο˟ϮԒuиȎ=ϯΎѕԮ',
                    'code': '$ϼЂЫ',
                },
                {
                    'name': 'ˌÇґϩУrԫϳΟĬ%\x94ɐʩðǏʄΒΔÄǎ\x8aϵ{҄эʘˋһ¯',
                    'code': '\x8d=Ƃ\x8eƀ=ГϙˀŘ',
                },
                {
                    'name': '\x8cӎÒŋˡӚѩȟԙ#ɾ·ƁΑ±ǀ\x8fȬуɱӭӼΗơǀTȑēǁЦ',
                    'code': 'üΙ®ȶҽ',
                },
                {
                    'name': 'ѹ˞Гɤn]ҿϑϏvƕlӄԐ\u0379wǭâǝǯǀԮwǯʗөЗãһǕ',
                    'code': 'εĞɌԝ:ǐĨ-ŕϯ',
                },
                {
                    'name': 'ȿòcɓǛіͽщ҆϶πϏѢЖ',
                    'code': 'ԢҾƴì',
                },
                {
                    'name': 'ĐԎʎĺҔ<ϦÒB\x8eҙѯѝѶ«ƺԊ%˦ʃșɦ!ΏƞҵƮˤˮж',
                    'code': '\x8eӆΛʭ',
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
            'locale_code': 'ǌă',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'Ϥ',

        },
    ),
]
