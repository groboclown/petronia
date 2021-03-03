# GENERATED CODE - DO NOT MODIFY
# Created on 2021-03-02T16:58:20.203475+00:00

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
            'locale_code': 'εƫɉΉâӏУĩ˖c',
            'catalog_name': 'Ɔ\x82rǣ~ƮCkΞˏѹӷrҵǑſϡȡТȮ§ƿXӲǝҵņÊLÊ',
            'message_file': 'ΔІűƭϢӎǕөҕʭώHĤɲʆJsƜɵϱʹЦÆ^ρƌĕΤÀ˴',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': '\u0383',

            'catalog_name': '}ŬŴ',

            'message_file': '\u0378ĳ',

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
            '$': 'γҍҎMΗʕƕ\u0381ŕ\xadşӳԐŗђɊɲƎȿŝʟӟҼӑʳűƍʁʗΕ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 5053008642577690275,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 416221.7559392051,
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
            '$': '20210302:165811.606636:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'êǞ˓ʛчӢǓ˔Q¯ȹˇzƄɟȳͶ^!ƶзάđ˾ϕ×ΨĨŴ]',
                'ѧ®Ґ˹З)JǆԟҰԑԍÓƦϩęEˡƾɼѧӡέƒɳκÐƺǾӟ',
                'Œ˓ĔυкȈºZɁɐя\x94XԓѴыʘĢöɉВŷӭƪÿ\x97ûԣҦ5',
                '¯˝ˠȘƎ\x86ΦҍŪ]ĿȎΊJѝ«ԁǙƼŤɢϠɯԫÝӈĥèѶӵ',
                'ѶȅΐЪѽπȋҸʣÜȅίǽˣʷϜ˙ïĻƓƦΥϺΤȞƬƨΌņԕ',
                'ĢӫҳԦӝɐ\x9d МvĕăЛэʤЈɮˀħÏN˼}ɵˊǰüˤгƚ',
                'ȋѣίΡͰ®0ʢʉ\u0379ùЯ=ųȎΓԒľҗӲÄȣȤҗąύƨÈʑɰ',
                'ГÑЊnГǍӃǁұī°Ι\x86Ȱϋ\x9fШÞΆ˰˚ǈūѝӜҰƒԚҩ\x98',
                'ˉȞӧϓĹϋ+ƍϾ*ÔԣǅЈ\u0379?\x95КӞьɇɔ˵ȈҜ;җǐāԟ',
                'ͳ\u0383ĚȅõдȾ\x9fϺÕʾѯԗ{ˮС³ȸˏǦγǗϒÁҘǊǰȎȫã',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                8892054674820570140,
                4564581781840853559,
                -5358888941187281778,
                8329752645318574630,
                4406538441221311811,
                -3307632990674363658,
                -5310270891839680760,
                3727462959891604709,
                -98532838505189156,
                -638186759225772951,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                565305.5548813549,
                -40396.49412852073,
                437548.2972129971,
                321218.3451460007,
                817242.8331946058,
                502521.82763595635,
                23258.19317477,
                286871.8137676583,
                598421.609211964,
                -46713.88092090268,
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
                True,
                False,
                False,
                True,
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
                '20210302:165812.824070:+0000',
                '20210302:165812.851216:+0000',
                '20210302:165812.878836:+0000',
                '20210302:165812.905819:+0000',
                '20210302:165812.933087:+0000',
                '20210302:165812.958961:+0000',
                '20210302:165812.981169:+0000',
                '20210302:165813.001581:+0000',
                '20210302:165813.021819:+0000',
                '20210302:165813.042187:+0000',
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
            'name': 'Ũ˃ѷ΅',
            'value': {
                '^': 'datetime_list',
                '$': [
                    '20210302:165810.966346:+0000',
                    '20210302:165810.987379:+0000',
                    '20210302:165811.008313:+0000',
                    '20210302:165811.029559:+0000',
                    '20210302:165811.050834:+0000',
                    '20210302:165811.071064:+0000',
                    '20210302:165811.091525:+0000',
                    '20210302:165811.113358:+0000',
                    '20210302:165811.141785:+0000',
                    '20210302:165811.172625:+0000',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'å',

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
            'catalog': 'φƣǀƵÂɳÒȓȣʌʇԟʇƕŖJƟčΏƒǷʦӇϛб\u0379\x83ψ˜Ӕ',
            'message': 'ГпȳǺƋĔϼӦfһ}ѲéФƓBΒžā\x9bùŠĖʩӷҨ\x9cʚлȿ',
            'arguments': [
                {
                    'name': 'Ɵņʗ˃ȉʑĖĸÛƺӘîƊǠ`ϥˆϫŲŶĎɒӞɆŌϔÛӃҒϤ',
                    'value': {
                            '^': 'int',
                            '$': 7012618032093832192,
                        },
                },
                {
                    'name': 'ǟƨПġʃ\x8a¦\x84Ѐˮ˂ѡɞ\u0378ZŲǷãѽ˥ƉȀͼÅ˒xǧɋϬĠ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        65771.65914611146,
                                        528678.524866074,
                                        387993.81010948087,
                                        666012.2849338993,
                                        655312.2813023631,
                                        542652.0395672118,
                                        713733.0647236045,
                                        175659.4899426498,
                                        637060.3026004254,
                                        924785.9520344585,
                                    ],
                        },
                },
                {
                    'name': 'ψϋɗɿpú\x88˒Χ±ŸӚѧ˩ʧШ*Ǡʫȡ<ʫ',
                    'value': {
                            '^': 'string',
                            '$': '\x86ƺИɢӼςɩѳ˺ůЁ´Ӣ͵ԈɫЬɽʢǲūȧĆʒ\x8c\x8fҚµԇΔ',
                        },
                },
                {
                    'name': 'Ϙ˗ΓǍűеĮæаǽҀӴǥΟ\x9eѫnϙϝ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210302:165809.082806:+0000',
                                        '20210302:165809.103782:+0000',
                                        '20210302:165809.123937:+0000',
                                        '20210302:165809.145331:+0000',
                                        '20210302:165809.167559:+0000',
                                        '20210302:165809.194176:+0000',
                                        '20210302:165809.219814:+0000',
                                        '20210302:165809.245029:+0000',
                                        '20210302:165809.269620:+0000',
                                        '20210302:165809.292961:+0000',
                                    ],
                        },
                },
                {
                    'name': 'Њщ³˛˵ɄƧѿɴď´CŞԁKɳËԞɃmƎ\x82Ɖ:ҊʽЅ·\x96Ζ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210302:165809.401513:+0000',
                                        '20210302:165809.423259:+0000',
                                        '20210302:165809.446703:+0000',
                                        '20210302:165809.468155:+0000',
                                        '20210302:165809.490093:+0000',
                                        '20210302:165809.511603:+0000',
                                        '20210302:165809.532609:+0000',
                                        '20210302:165809.554940:+0000',
                                        '20210302:165809.576720:+0000',
                                        '20210302:165809.598751:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ɜ\x8eƴͱw˜¯Ҩб˳ɍ˽ɝӀԬҁȀ\u0379ɕ>ɃѱXŤҊǇ\x8bˋµѺ',
                    'value': {
                            '^': 'int',
                            '$': 2863229688190221881,
                        },
                },
                {
                    'name': 'ҏˡμv\u038dӍɝʱϡƧӛӥѵҞʈҏΙň\x8dѕƧǛҪɧҡɮĺє˙ʒ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        4953731747220091056,
                                        2865800204444157966,
                                        -3080790419477466834,
                                        581805509153183329,
                                        -7647447808537718171,
                                        -3682096786282042,
                                        3560982697278692042,
                                        -5268181401649672051,
                                        4726094420152731194,
                                        -492327516662461147,
                                    ],
                        },
                },
                {
                    'name': 'ΠћБ\u0381ВҼɠҎӏɯԋbTɱȶ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': '϶ƂŽсœěʕɺɞȔϭÚŇɈ\x8dșŌǢWÆЮɺȏȐˋӳȒЦȊƫ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210302:165810.296003:+0000',
                                        '20210302:165810.317611:+0000',
                                        '20210302:165810.337818:+0000',
                                        '20210302:165810.358993:+0000',
                                        '20210302:165810.379479:+0000',
                                        '20210302:165810.400175:+0000',
                                        '20210302:165810.421663:+0000',
                                        '20210302:165810.443786:+0000',
                                        '20210302:165810.464325:+0000',
                                        '20210302:165810.484972:+0000',
                                    ],
                        },
                },
                {
                    'name': '³у',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ɐѣΦƛθ#ΐˣɐиɰʞϟЍͰºϯʼƣԦʜǽāҍBĄЫ\x93TG',
                                        'ʮɎϑ˰4ȋρӥɨȌΝĸӎƵџͺÿΕųˊөįÊìďǚǲ;МƸ',
                                        'źӯ΄Þѿϯǵӊӷ=ԍҡîҸȁ\u0382ɸӲϬћвѨΡ4ɆnюʓΚ\xa0',
                                        'ΜͻӯlÒ7ӣ\x88ʹ\u03a2οəƖâҪԨίµĕѱÍǻђΗҤѦDÇÈń',
                                        'ΎðɯӛΎͺŚр\x90ӎюİТˠNȐƹ˹ȪʽƜ҈MĝϽӇԮϫǶæ',
                                        'ɑʿÉǿǈĕԘҫôŚÇ\x92ɩћŚϿ ˖ʯΑRԥWͳÚƄƆţҋʯ',
                                        'Ӡ҇<ÐΖ˩ѥ\u038dѢҒһŽǐ\u038dѳǭвʜˈϾÜΆɰʹҵɍ˘ѾҘč',
                                        'ŖϪ˥έƀҤҟˊʡà˼ĴВӲĴɂǏϘ˟ŰҟbωŏΓȡˢˬȘì',
                                        'ӒǉǊΊΗѶŐʽтʳɐ_żίĞÑ[ĉζǯˈˣΪ\x9bўѯӰˑňȳ',
                                        'żΚȥȑɈϐЅjʿŴʻћƓ˒ǗӫҌϩҚάъƴԗȞǻԐȐЪƀԡ',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ĺʮ',

            'message': 'ʧ',

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
            'identifier': 'ʟ±ː΄ѼМԙҋ\x98ԋáʉŧΔӧωļӨľϯUņԉœʜÿǿrÌӻ',
            'categories': [
                'configuration',
                'invalid-user-action',
                'invalid-user-action',
                'internal',
                'file',
                'invalid-user-action',
                'configuration',
                'os',
                'file',
                'network',
            ],
            'source': 'ӯςąćϛ\x98ԋɸǕʖx˳uĜӹęͺ»τŒήҔҸ˖g¼ǵӒǵə',
            'corrective_action': {
                'catalog': 'ҜÀЯƕɩ͵˴·\x80ǑũðͷɤԓŜæΫѵЍѿʫ҇ŕУƙ»ρȷʽ',
                'message': 'ш¬şͳ˦ɺǦ{Ӆη˷Ȫ\x8aŬʬμÄԛɤʻӬəұԐ\xadÅ5ǗÿЯ',
                'arguments': [
                    {
                            'name': 'ԔķѲæǡʵȚÏß&êǘ,Ȁ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'GĤÅɔϑʯHǅ¼ƵűҘĒˋăķİҖÚȃϴɸӕűșWŭÂǣψ',
                                                        'ĨƫΘƑǳ˟ǏԗȾŅƩӗƮʀ\x96ӶӪǒ΄Ņʋyɹ˦ӠсκӖΚʧ',
                                                        'ʚԥőӾЋǙҜхӔɯɻѝŅßǭƳӐĘѿ#ŢАӺ˾¯ʨŚӒ&Ħ',
                                                        '¥τӾӖ˔Ü/:ϨҿĵԟÈʙŮοOӷŭҎȩ¼ЬũԌӢӣΫƳé',
                                                        '\x8aǈßйŻƦ§ų²ұʙ˝ŨσĉưԈƗǸҠ¿ģŋɥ\x9fȘ\x9fȩĩћ',
                                                        'ŷŮ¹ҜŜǗϣΏGɽέǢҦǴ;ЈɥȎҐǀЍƢȣЙĪҕęŞǠԜ',
                                                        'ѢÜǫŤшlӄŷaҕŴҫӨБʖӾѬӅϊϔŹΌɟчџԔȬиҞԞ',
                                                        'ҩνįђFЮȇkZËɺτ˵ϊԗc÷ħǮƗėÓǖ\x81ʝѯ\u0378ɯʛҢ',
                                                        'ȚΘӹԇгфͼȱΣƽȵ˗ȹ\x91ѧŭԝЍĈШ\u0383ðǿԙ҉ǤQɩǛ>',
                                                        'ϘǲϗιКύŹĺÐ\x99\x9dЍĚφϟдϦƽȪз˝_ҜðʧǌÏԞϊɕ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǣŕҧАƲȅСЮȨнӅϟŐƱĳ\x86#',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ςĦȳĻũӋĬǋė˜ȅ·ɤȜ!Ù˴fΨϦϒп3ѧŀԕԘǵaĜ',
                                                        'Ϻѫӄ˦_Һ`ΚѴƔʾʗ˭ҕƄ˹ŴИԓȂʧϲȎҲąƧ°ŻҾǺ',
                                                        'ѨƩč"ǾϙНǅɖЍʒԇϚѴЫſҥӔŹͷϯǱͻӘǘаCвþԗ',
                                                        'χРǕΣҙСϹиɵŒŷӌӜȉĎгК³ҢҸЧмʚҜŐǍˬϰϳȍ',
                                                        'сˍȄȶĥ}ѥъ\x85҃ϼŽϑǫн1ŞКȞƈÐ ˇ«θƟӼƒ¸Ǳ',
                                                        'ľĈH˽ƛȰóϘŔĻ\x84ɟĚɠІͽ\u0380ȑĂҊҐUјǋЫȁϹʍǢ-',
                                                        'Ψ`ˏӏʜ˸п÷ϭƁ\x8eψ\x85HǊҽ\x9eЅǇƆyƪĳҿǰ˲6ѽƠȦ',
                                                        'ɦӆЫ.ԋǢӭ|ǅɍǒdдɈѹ5ѺʙѼҮԎïŞ\x80ȃҨŏuϠG',
                                                        '˳ǴÔÓűЪԈԩŅÈёˢєυCξήΧŪĖ˾ԘвäѲĜ5¨ɲύ',
                                                        'ʧҁҞӍԍǱӚŏä0YѐғĦƫϓϲȴŕӱӘêѶɜƚʵƩсžȑ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Yʈ\x99˨ԁϼӕǸǼ҈ĐΊЇϊΠʍ\x9dɻяÝ?ˢ˺Г҇ǣҼ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        372711.75281585654,
                                                        864474.9389992882,
                                                        834075.8209639802,
                                                        908892.9998937553,
                                                        693941.3352068438,
                                                        -18498.949480789466,
                                                        -76218.14880377962,
                                                        636331.2232468737,
                                                        472131.673379526,
                                                        977668.593265113,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʆɸhяȓĸĺĿѭiԌӐҨĸ[ĝŰҢ\x98ĤÅʥƽěəѨĹöįá',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'Όǚēz˺',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        112513.8127858087,
                                                        408269.0891914284,
                                                        587517.8065594847,
                                                        707704.8255198523,
                                                        220255.1893272678,
                                                        655160.0696701616,
                                                        310759.7493184053,
                                                        738614.057287901,
                                                        286046.839073754,
                                                        242584.88102643675,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ѥ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        True,
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
                            'name': 'ϐȆΫӡӏԗɷΠЀ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -1002242241597026890,
                                                        6747245764990545146,
                                                        -8091415762359134127,
                                                        9041326699007994154,
                                                        5152631361910015383,
                                                        311531558889142524,
                                                        -641738411910517632,
                                                        1843849277214445527,
                                                        3923594498526813446,
                                                        -6923130525024032563,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ȹԂɗˤƶϪÒƟΪʡǕȓԏʟɋӀˤӞИȢ΅ʒż.Ťɂӭˉ˂Ϛ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        6435214891146023525,
                                                        6003823471574693167,
                                                        -2302236694730601246,
                                                        4411592071609580152,
                                                        -9036979615934213341,
                                                        6792084578434693533,
                                                        -5453227956195177267,
                                                        -2751586268902711119,
                                                        -5264016889472102295,
                                                        -5855497113897071103,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ńÏϡӟOΖ҆ȓŐŰϾlÄ\x96e\x8bӻδґƜÜʹϵlǪƀşȳv\x82',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ˣ͵˅ӆßƢŉιϻθãͷOҤԟϖӍȋӣӽϳ¤',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210302:165808.180722:+0000',
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'Ҋӛ\x90мӜȎ\x8eͱĽӣ\x90±ˉтʃkȤʗԋɂЪÖ8ÙԎėΎŘϘɟ',
                'message': 'ӏ˱ʮͳϹӒԈžҴúœˣӷӣðϒäэÙʜŢƔĤɛ¨ŢԠȢӑғ',
                'arguments': [
                    {
                            'name': 'ĕŌ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'Ĝ˱ӳҭεʕѰ;έɅҪѴɜŕȺҼˎүΣčӈ7ʵļˇʾЛɟɏҢ',
                            'value': {
                                        '^': 'float',
                                        '$': -70012.80067396049,
                                    },
                        },
                    {
                            'name': 'ĦȂіȔƊǊʫc˽ԈУдќψ°Ғϗ¨\x93ўʲҹϩǌσΦ˽Пȗǥ',
                            'value': {
                                        '^': 'int',
                                        '$': -6055888314624102798,
                                    },
                        },
                    {
                            'name': 'Ȭ˰\x8dZԒɌÇŨѯͻǦǁőǆΜӊƢŝӳɾłЊǳ¨ƲˌɀˎԖ£',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        False,
                                                        False,
                                                        False,
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
                            'name': 'ōГˆͱҧ¶˷ɰ\u0380ѥŤŘΏǠӁ',
                            'value': {
                                        '^': 'string',
                                        '$': 'γ£ѩŮ·жЛǧňʪŔΎʋԕҋǶ\u0379Ãп7>ÆӚОĹ\x9cϥҸ˛ƀ',
                                    },
                        },
                    {
                            'name': 'їͿƣßƃÇӅӟʄū҈ЕɐÎƟ͵\x87ƵЭҞ\u03a2ɂ«лԈѱҠԮRɑ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        481124.94617180096,
                                                        458704.50552884536,
                                                        177772.10287618916,
                                                        689242.4045107857,
                                                        585215.7210931708,
                                                        468334.18128138734,
                                                        914146.1520666357,
                                                        690171.8541980293,
                                                        436155.86800382356,
                                                        256546.10438973055,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ȬӏƦЋGģƝĜǨϓƬȋϠȮ˅ЙǤљȶ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        False,
                                                        True,
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
                            'name': 'ŊšЌƂƜěȢ\x87ҩǤԋĤҔ҈ˮÓӧϺ\x91гӯǜ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ҎЮŎӝлɇËɏƀӟҪК"ăŁpъɗųѰі\x7f!ɄԄѹĈɄƢΎ',
                                                        'ќŧüԟȊψʲС˂ОƁм^Ĩʬ˸ȧɧˍWҁҫʄϒ´áʲʪӡ˘',
                                                        'çǙэϥμ\xa0ΙǱҏϬԏǱǳŹ<ƺƘήӮ\x81ӍҠʍɦ\xadҡӴĴů~',
                                                        'WȿӗJȩɠ˛ѹǻÏҊ˾{ΠќÐȕQϟ©ĥĢ\x9fԊɚѫҝɌϲζ',
                                                        'ºӓĐ(ӳʉÂǫͺϟӘ˖Ζ҅ɆӶźжԙɴӄ΄ңă\u0379ņĵΠBͻ',
                                                        '˘Å˒Ϸк¿ԁVǡƫѩњϬʾŠƬŢÉÝѲęЦƟҤÝӦȷQХΔ',
                                                        'ХуӅ҈ӌéʟɝƎȵńǣӮгù˧èФюʳSң2ØȗӳƧτȉ²',
                                                        '5őφȬ˂î-ϳ\x89ϓΠ˙Ȥɖї>ťȴˇ8ΒчȦώҋˣƼԉƌȃ',
                                                        'Ӯȫțįǿ¤ǜˊӏЧǝ>İéϻˁȜӅɀӧǦϠŞЉ!МѬȗĕϐ',
                                                        'ɳԑЖǕÃ˱ϽԁuҦƨ%ԃΪAȻ˵čțɴlƳΣìШ\u0380ЉЦƹì',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ͽ΄ʮ<K·ʼ~Ќв³ț˻ΘВιʞϔùQkʡɭΏ˗',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210302:165814.990051:+0000',
                                    },
                        },
                    {
                            'name': '2xəːʹɄɔϟЎͽΒŋԪǽϓʨԄͱ\u0380ƨ',
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
                                                        True,
                                                        True,
                                                        False,
                                                    ],
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ΚԤɧчϹ',

            'categories': [
                'os',
            ],

            'error_message': {
                'catalog': 'ȓ\x91',
                'message': 'ǔ',
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
                'identifier': '˱ŸȐΨ˜ðʨПɰʗ]ªɛȔÊŴάçůlǔ\u0381Ϧŕ²șГɈ\x84ԓ',
                'categories': [
                    'access-restriction',
                    'configuration',
                    'file',
                    'network',
                    'configuration',
                    'access-restriction',
                    'os',
                    'os',
                    'os',
                    'os',
                ],
                'source': 'ɝϸҔͷʃӀéʶ]ҋƊʦҹoëɠϻϫȍϚƪɓȻРӟɀǷĤÓ˥',
                'corrective_action': {
                    'catalog': 'ѴεƂѴʃїҀԫζάǦǰЗʈҡÂŘƑВϾ-ɫ¤ɋɱxϪ҃γҒ',
                    'message': 'ϕҸȚˉкԊо˲ͿПȨɓԇ|ȸԌѬԚӆĚ\x85ȳΧüɢƓФΫԀq',
                    'arguments': [
                            {
                                        'name': 'ҿ҂đŖĔŇόbԦɾċ©ӝɲ¶©ƟҐ˹Ɩɖɿŋԕԍύtȸǖϖ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165802.160531:+0000',
                                                                            '20210302:165802.176744:+0000',
                                                                            '20210302:165802.193594:+0000',
                                                                            '20210302:165802.208797:+0000',
                                                                            '20210302:165802.224854:+0000',
                                                                            '20210302:165802.240605:+0000',
                                                                            '20210302:165802.257820:+0000',
                                                                            '20210302:165802.276417:+0000',
                                                                            '20210302:165802.293797:+0000',
                                                                            '20210302:165802.309020:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ҫ˼ǨµѕǂԏƊȻ¬ZȋȡønĘʝʾʇ¸ĞӿϠȓӓĖ˰ȴ×Ѫ',
                    'message': 'ϝɗʔðΡͿ¤ӤȶȐÌʾŪLЯŀŕʧýʎɏЗҌůˢĚӠӟˮÐ',
                    'arguments': [
                            {
                                        'name': 'ÐOfЯğϔ¤Ϊ!ĳˑ¿ʢø¢ĩѭѴ\u0380',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÿίĠƓәо9LJгǔøʹɰʜҿƥƬ҃ϕ øѱĘ4ȇ6ǁЇԅ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            5445.743731947878,
                                                                            75884.32172692829,
                                                                            54694.03976291086,
                                                                            428061.11031745444,
                                                                            864641.7701761251,
                                                                            579346.493735874,
                                                                            269436.2005162779,
                                                                            168324.04528384074,
                                                                            820894.7478071214,
                                                                            733554.6922068277,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'тɨѯʁʸġdұʼħŶƳ˳ˊӞ\x8aɿɀYėԋŋȰ˙',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '_Ůǥǳͳʠ˖ĈÐ\x84ҍ\x8aę˩ȑØёʤӄԦќˌˤϧԒĨtơ\x84Ȕ',
                                                    },
                                    },
                            {
                                        'name': '҆ǙĀĸѴƭėЮ¹ÒǿΪӈľϝŕȍɈ©ʶҲŚ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɗӆȸΣéƑҕšĿ)ĜӼT\x8bάȸϬDӒƔůÑÃPοɸΔϩРż',
                                                    },
                                    },
                            {
                                        'name': 'ȻϵʥƕʺǮѺ˔ȍԟɿɚҔyΏ˛ï',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165803.313939:+0000',
                                                                            '20210302:165803.336032:+0000',
                                                                            '20210302:165803.357712:+0000',
                                                                            '20210302:165803.379402:+0000',
                                                                            '20210302:165803.401150:+0000',
                                                                            '20210302:165803.422787:+0000',
                                                                            '20210302:165803.446677:+0000',
                                                                            '20210302:165803.467281:+0000',
                                                                            '20210302:165803.487684:+0000',
                                                                            '20210302:165803.508142:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ˏfìǮϛÜӖ'ʲϷŢ]ʓϏЫƤơ\u03a2\x94Ǐ",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6531939818731777562,
                                                                            -2599907775163459771,
                                                                            7057312021174372817,
                                                                            2697423031193716525,
                                                                            -7143677287714369113,
                                                                            -8500752621783416041,
                                                                            6323433967109429701,
                                                                            -8701675909876806259,
                                                                            -1772583294704868954,
                                                                            4067365646253336339,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϸÎBšгNeȰԭÏƐʡʩƾӣѣТӕόɰѠҗВȿ\x80Ȉ/Χʦʶ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ӽnԈř',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŉҹЊ!šѣãОʙɞƇӈ˼\xa0жÒԫϭΐā˒\x86ȊѼʇǂDāǶŮ',
                                                                            'ћџ˕ǜďĺјѠŔćŸѰĤӐµĈϫƕіĈƥȃʍȾŝǸġ΄ԛŐ',
                                                                            'ЖѮɂȢ;ɒΛvӮЗvȢϷɼÄǴЫԎԉ͵ɂьǁƇ«ĭŋӂɴÒ',
                                                                            'ÓǓĝ˒c-ıˣȢǠˏѷӠʛкƊһʵЉԂέԙц\x86ѫѷъĬϣϥ',
                                                                            'ϊԅȓ\x8bƼɬŤһӓȊ҃ɸɔ˾uѽǢ¢ɈƌŀɈϐþƭʳØƁ϶Ǧ',
                                                                            'rˊļōҫͰȁTʐNƋƀ˅Ѐţч΅Ǹ*gҮӷƉ˻ǰƒкĿjd',
                                                                            'ѠύțȐ҆˔ɫΡǦȚɁȒ)ьɼǵĐŭσťɕŘȁ¶ЌаǥӔÉś',
                                                                            'Ǧ˭ɭɵͼʚϕ\x96ĘŞсŖǭĘ¾ŃÜǗÔΣКЧƝʻϠ\u0380ʍҰ>ǖ',
                                                                            'Ҹ\xadѿġӾÿĢŅΐԝ§Jıĝŵ-ͻĹŒӕƵұƾŶʶԑ^ëԑĦ',
                                                                            'ϠԙԟHǷɘ\x9fӸlϓƸƵԆãʹΘÖƱƒψҬ.¡ψĜǯϞΤȺɛ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӟƻŋýöčÐíϕńûǛѰŘ\x8bжĳΓŎÔЀʊɑѴθʙ\x99ǀũɤ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            872434.8931195168,
                                                                            565701.1597926111,
                                                                            -58371.83308946156,
                                                                            918148.4737172307,
                                                                            182230.12956532987,
                                                                            151365.00501643072,
                                                                            861916.2147611582,
                                                                            710836.2039944563,
                                                                            522309.20074535825,
                                                                            607135.5018748917,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȃβ˙',
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
                'identifier': 'ҲӳЙӄФ',
                'categories': [
                    'access-restriction',
                ],
                'error_message': {
                    'catalog': 'Ԯѥ',
                    'message': 'Һ',
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
            'locale_code': 'ɗʗɮ%',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ϝ',

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
            'catalog_name': 'μӛ\x84ńȖԥϴʍġʮȒҲƕԕNϒѲʕϱήʰԝ·üԆơƕѓҳи',
            'locale_codes': [
                'ѵHз"',
                'ԜƭЕĺѦРІ\x8bƜ',
                'ҺЌ·əҾĪǢķ',
                'ƍÑ;ë˄ʕƳӧЁ',
                'ǡϫѣζɬͽǗ',
                '\x9eЍӶӔÐ',
                '^љǭφ',
                'ǋКϊÞ',
                'ľƳʂȟ\x85*ҁËˌ',
                'ċƧȜ˓',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog_name': 'ͱŃԫ',

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
                    'catalog_name': 'ӧʴԑİȎɎИϥιѝϳŜέŵ˾ʞєǍɍŐ¢ǃ˘Ǽ҆ȢJ\x8cïԇ',
                    'locale_codes': [
                            'ЯМƱ˚΅',
                            'ȿ',
                            'їӧȫÅɩŌӍĻϣ',
                            'δĸǄű\u0381ͽ',
                            'ñϴ',
                            '\u0381ſc',
                            'ęϼ9',
                            '˴ś\x8dUҥӞ',
                            'QδǛɽҖɛ',
                            'łԤ',
                        ],
                },
                {
                    'catalog_name': 'шЕǣŰЅÒŽã ҆Ȝ˱ϙӇ½ӏЧѬͶȯΎԤӧӾǇЩƠK[Ϋ',
                    'locale_codes': [
                            'z',
                            'ΨĮ',
                            'Ӹ',
                            'ô_ǃɛɜπɇ',
                            'ļç',
                            'ʋ\u0380ʎ˭ƒԝҁ',
                            '϶Ѐį',
                            '˗Ǵū\xadѷҙEҤn',
                            'ʀӅ',
                            'ɘӰРӋ¢ё¦μʴ',
                        ],
                },
                {
                    'catalog_name': 'ѷIӢƳȢβǏɫòϋƳϰԮʏ>ŦЍ˭ѦЁšӨʐēȁɞϩҢ\x7fӦ',
                    'locale_codes': [
                            'ŧӟбĈƕԟȧѿӤ',
                            'ШЏ\x98SʁҐӅШњ',
                            'ʯρƊԒqȺýϟ\u0383',
                            'ʍ',
                            'ӏɀK',
                            'íωйüѧãǔѡ',
                            '˗ŘЫԝˢʩȰͿʩm',
                            'σҵ ª',
                            'ҕ',
                            'ʧǔњǡѽ¶',
                        ],
                },
                {
                    'catalog_name': 'ɬ˴ŽȮ~ř',
                    'locale_codes': [
                            '˅ł\x8d',
                            'ԄŚƧ#Ҹȼ',
                            'ŉӄXŅʄǘԆ',
                            'ӟˌΦͳωп',
                            '`҆',
                            'м',
                            'ɜ.ԩҔ',
                            'ԩņЌϮĔS',
                            'ҰȝǸѣ',
                            'ǖѵʄ',
                        ],
                },
                {
                    'catalog_name': 'MŖԝƖˡʯņԂήйĢɧɧәǀ"ƴȀВȄʾͷϺ˼ǕВ4ɯԧ҄',
                    'locale_codes': [
                            'τzҺȈ',
                            'ѨǬ\x91',
                            '~жѐ',
                            'цǼȻɌЗНǽŖ',
                            'ÏЧмęԄ',
                            'ͷt\x98',
                            'ɰpѶЕԁ҈ҽáˢ',
                            'ƫ\x9bʮи',
                            'юЁ˭ǋӿʣ\x9a',
                            'ϼΦˡ˫ßԢȆҜѿ',
                        ],
                },
                {
                    'catalog_name': 'ȣ4«Ўf˱ϛɑČ«ȘԫǢŹĒs˃ʁѢїҀ\x81ĥʻʇΔҐкǩˠ',
                    'locale_codes': [
                            'ȫȋ¼ň',
                            'Δ\x9bѱ',
                            'ҪҧӊϨϩŚУoϿ',
                            'ηЩɕϽɼǆɪDӰş',
                            'Ȫ\x84\x95ΑОϘσƙ',
                            '҃ÏһƝɇć·',
                            'ēԮҤϊҗƌϕ',
                            'źԬьɤȺ',
                            'Ѻ?҇Ǚ;',
                            'ˇѯңĩΟԢ˛ξ',
                        ],
                },
                {
                    'catalog_name': '\u0379ҙʑ×Ћǝʈȗ^ъ҉ȶɨєŜѷɹɨΈӛÒκѪȕxθǟʅUҕ',
                    'locale_codes': [
                            'ǔɫ¬ô\x9f!ЮԞҹҩ',
                            '\x8fƇľӆřϢϠ',
                            'Όʲǖñ\x82є\u0380',
                            'Ķόř˙\x8bǟQʳ',
                            'Ң\x86ԝΞ]®ĘЇ',
                            'ΫoʢȆӂ˺',
                            'ҐӶʞp',
                            'ҬхЎĘƆŊ',
                            'кɵӁԁУj',
                            '%ęȅɺ',
                        ],
                },
                {
                    'catalog_name': 'ԦǱ²bƻНƒźΠAðĴʽɛŐ\x8eхçĝԛӆCHFÁΈñɕѲĒ',
                    'locale_codes': [
                            'εø\x95',
                            '@\x81уѢϣΡ',
                            'ȿΚ»ӢӉĞϺɡ',
                            '¬ҞǻĚа',
                            'ɶɿӸ\x9fʒŴ',
                            'ӖɎ)/ˣ',
                            'ʩЛʳƜԪ҅ɄƱэ',
                            'ӷȹԛρ(ˎʋͺ',
                            'ѧĝ',
                            'ЫdɹДǹÚoʬ',
                        ],
                },
                {
                    'catalog_name': 'ԪЧģwq\u0381ʗӑʫПДɖЌǷδuƷŘҴФΓëͻŧΈҷƥЙұɼ',
                    'locale_codes': [
                            '\x91˅ԏΐԛϿȦ',
                            'ͺΣΠ',
                            'ӮӹɅЧãȒ҄Ӽ',
                            'ԈˉӤЀĤRХϡÍ',
                            'Ԡ',
                            'ʖԢpԣнɿŸ',
                            'ӾĦŨɼνΘы',
                            'Ï4ʎфѼ°Ў',
                            'œӛӈ.V',
                            'ʤĂȔφö',
                        ],
                },
                {
                    'catalog_name': 'фĿŻϟƷƹϠʙɔͱ',
                    'locale_codes': [
                            'σ',
                            'ȓˎҁeƪ˛Ǵ',
                            'ұ?Ȋϩ\x80ɎÎѩ',
                            'ЏҵΣɿĄέy',
                            'Ůč¥ҵ¤',
                            'ȀÀԞʪ',
                            'ɝΩ',
                            'ʦɌk',
                            'Ńԡңʾ',
                            'ʃǥӳǔɇĎ',
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
            'name': 'ɋǶϸϣϤԢȯѻøůΚΙʹ5BħƜŵÑςŦŚ]ǞșБƹбşɤ',
            'code': 'OɬҰǗ\x94',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ƥ',

            'code': 'ȫ',

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
                    'name': 'ϝʣӣʲɤўæˣE\u0379ѵːǾI`ǌsȏҬŰʒa)˶ω:Єӱ;ǎ',
                    'code': 'uЃ´ж:Ћ',
                },
                {
                    'name': 'вԛҲǛϒĀΑŅȆ΅"ԃðїˁǹԇϪґюźвȨ¯˶lǮ\x85¦͵',
                    'code': '¡Ĝ',
                },
                {
                    'name': 'yųэɫďЪ*ԉʌɅ\x86qƪŔϚĊ˃ЅϲĶϭ\x9cr÷ɂµΘГģӍ',
                    'code': 'ԍѠӊ',
                },
                {
                    'name': 'џ\u0379oɓϼЮ\x92ń\x89Ϡΐƚȷҵʩ˾ǢӦРӐëɬŋБǍŀКԣŤЕ',
                    'code': '"Ӗο',
                },
                {
                    'name': 'ƈ˝ɯƾǇŸӆ8ȨӐΘΚҬҢ^ѹȲ\x87Vʿƿ%ķҙЀҔԋƐȲԆ',
                    'code': 'ӛɃ\x84ԜԆÂʘɕ',
                },
                {
                    'name': 'æȏԕ˲ÇƮǅǈҏǁˀϺПŷƺʕːӰӖĞɪǜ¥ȌÌDϴǭӗӭ',
                    'code': 'ЃӻԋюÉˋ',
                },
                {
                    'name': '҂tӬÿӮ҃Χ~ǱƏŸŻШӐɒƿ¼¾зΟѯ',
                    'code': 'yЫ<ĪԂ',
                },
                {
                    'name': 'ǎ¹ʸФ\x88ƘӋԨ¯=ſǭРϻΎʲŶ\u0378ҜÃ΅˲уȥΘԄѧФδϯ',
                    'code': 'ń',
                },
                {
                    'name': ']Ж҇ԃԌȃō<ЫҍρΡʡǏĪôȆԞ\x98ԅҾŚȴ˳Ņˁ˧Λľʼ',
                    'code': 'мNǅ¾ŭɻǉ˙',
                },
                {
                    'name': 'Ǜǹ.)ЖųѷɏÂƅϩ˟Χ\x98ЖǖʣɇҒ}ѫҖɛÙˡɆҭ]ƴƆ',
                    'code': 'ĭ\x8c',
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
            'locale_code': 'ŃЭqЖŌˬξȕӫ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'Ö',

        },
    ),
]
