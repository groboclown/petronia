# GENERATED CODE - DO NOT MODIFY
# Created on 2021-03-02T16:54:05.495201+00:00

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
            'name': 'įǦ˭ĂϪѧņŁΨʓüԃǅʨyȯśҴ`\x8bÁ¤ӘԘ\x9dǕоиҰ×',
            'minimum_version': [
                -1428060035044323868,
                -1649564774068751228,
                -1719170460643168544,
            ],
            'below_version': [
                -1108132886293902718,
                -4145691853342824357,
                -8525257653548321413,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ϗ˄Å',

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
            '$': 'éтºԏƢǚΛŗԝōȸƸϑԠƛǝŝФʿ¬˄ȋѺԆͰƤԞƺιρ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 8252959988644080113,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': -94960.45166926723,
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
            '$': '20210302:165354.597783:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ľŔЪɌŎˁƤµĥʨӪɖ\x98ӵΠӅýɲҴɕƅҊăȰћ¸ǟɨЄʡ',
                'ϋȭǽτp˃¶ƿęӁϹҩƘЀăнӈƊƼ\x9aЀȾϻ˾бš˺ĽĢҒ',
                'ǕÎ˪ʰ_ϱ§ƃʠЙŤԇӋȽџˎ1ȍšɳϖϾсѽ˂șΜԐ9Ƨ',
                'ˊ\x84ӳȷǑӰʎлĮŢºqŶHŘĉĚĆʷ¶ѹºɲӖ\u038b˥ɌΜԗɮ',
                '0Ħɖς΅ŧóƏƓĈ(Р·oЦѐĝƅήǟӾĸәĸЬXҞңŹ˺',
                'ÆΞϊˇ~ʸѽςПϒ˅ȕԉȳĭˌЎAŹğrФ˓ϔʪҝǂƈ>È',
                'ӭ¯ƾӛ!ĸԀɾFҘ@ϗǾ\x9aÉǼɱ˥ɯ˒у˔ԍцӢӠųԉȶʡ',
                '˩şŞ˞ůāҏ+ȜȯʝҁLÑJŌÎ\x80ɣξЍуҠӰŪ\x89ĶҁѼǸ',
                'ǘòɺзǜɌЫӔъaЪqȷџ9ЩβɆӮҙʙ;ȏŰƐҚӏѥ\xadŅ',
                'ѹφʓ˴ƨԫ¹ҪłУ҉ʬȃвʡǆěîȈΔˀӾωСűƹ˘Ŧʡ\u03a2',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -2291046845150222572,
                974949007965235049,
                7078722052756561462,
                -8561761710748639045,
                -1036533664510752852,
                7903557463292681543,
                4158238246916243481,
                4572198398488352453,
                5163205935391454235,
                -847209122301115383,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                463833.25399327534,
                629198.791667345,
                -43409.038952092524,
                969728.8145490768,
                586581.5129057011,
                935869.4697709949,
                160020.0905423254,
                821961.3203983944,
                524659.2528542604,
                429279.9301957636,
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
                False,
                False,
                False,
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
                '20210302:165355.995018:+0000',
                '20210302:165356.022073:+0000',
                '20210302:165356.049125:+0000',
                '20210302:165356.078765:+0000',
                '20210302:165356.106139:+0000',
                '20210302:165356.135036:+0000',
                '20210302:165356.165242:+0000',
                '20210302:165356.196059:+0000',
                '20210302:165356.230618:+0000',
                '20210302:165356.268045:+0000',
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
            'name': 'ƔñȆɕŊɻ\x988ʦѧ÷\x83Ƃ҇Ū^ůĮMƏƝ',
            'value': {
                '^': 'datetime_list',
                '$': [
                    '20210302:165353.927110:+0000',
                    '20210302:165353.950669:+0000',
                    '20210302:165353.984338:+0000',
                    '20210302:165354.017505:+0000',
                    '20210302:165354.046556:+0000',
                    '20210302:165354.074285:+0000',
                    '20210302:165354.098101:+0000',
                    '20210302:165354.122500:+0000',
                    '20210302:165354.146506:+0000',
                    '20210302:165354.172430:+0000',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ȧ',

            'value': {
                '^': 'float',
                '$': 508324.7720644976,
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
            'catalog': 'ϰʐƗ\x8cԟԭƱΉkȘǊãīĵ\x86ûȱUįϦӛļϬŒˊєѴӢʺĈ',
            'message': 'ҳʰ҉ЭjАǳȋ0ɡŭӞ°¢ɀ˼eӻʓӠяȁũǘƧκǟ\u0381Ӭϟ',
            'arguments': [
                {
                    'name': 'Ǖ˰\x88FґːƁ˪Ôŕҹ˄ѻοoj\u0381Ȇϥ˱àϏ\x8cҡԍĬɋζΥϿ',
                    'value': {
                            '^': 'float',
                            '$': 772585.8534867715,
                        },
                },
                {
                    'name': 'ȷʆƠџҺΈʾ҃8љϵȈ$',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        796562.0028701467,
                                        -3933.7818759079673,
                                        836518.8742386228,
                                        712570.712819919,
                                        27716.146491999156,
                                        33040.36664671198,
                                        463436.55194497446,
                                        112169.80427703873,
                                        596820.8535149702,
                                        534794.8027892122,
                                    ],
                        },
                },
                {
                    'name': '\x96ʗϥѾąԤоʼǦǹԂΩӌ¿ĚǑȯҤ7Ǉԥʯ(ҝӃŪпƝτƇ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        469100.9071764054,
                                        75651.91939590411,
                                        55867.253982414375,
                                        683774.3006562471,
                                        916745.7451470338,
                                        900107.5991057538,
                                        595048.6202540953,
                                        181563.95883239765,
                                        486864.54430421034,
                                        851194.0506256821,
                                    ],
                        },
                },
                {
                    'name': 'ĺŦӌÞƨöƔž˓іЌǬFΫώƻʻʈ˫ãzԦȢϭɏ˯',
                    'value': {
                            '^': 'datetime',
                            '$': '20210302:165353.428810:+0000',
                        },
                },
                {
                    'name': 'ǖ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        970692.7737949674,
                                        645707.3409246821,
                                        188551.41360232694,
                                        752183.3822672444,
                                        997000.8991452595,
                                        -22782.20010254995,
                                        611263.1742217159,
                                        254674.84653200867,
                                        702585.7686977711,
                                        107285.60284287034,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'θЦ',

            'message': 'B',

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
            'identifier': 'ēƨ£ɀ²¤\x97O҃ÖˠpȈɫËÒ˃»ȍǹԤƍˉXȯ˼Ƴ·Ӛª',
            'categories': [
                'file',
                'invalid-user-action',
                'os',
                'configuration',
                'configuration',
                'os',
                'configuration',
                'os',
                'access-restriction',
                'internal',
            ],
            'source': 'ԎĥӖɰAϝĜɽ%ɒЖϽŷǦ\x8fҢƯ',
            'messages': [
                {
                    'catalog': 'ѕçȋԆɛρ',
                    'message': 'ŇħҺʀ[ǎëǦҩŅ]ê²ѧ҈ŃɖˊρʔǧϖҖƄҜϜåЛĭʟ',
                    'arguments': [
                            {
                                        'name': 'ǘGƶƒԃ˭ǹUʽ;ΨʩǚЩƌÕԌЇΣžђʄԋϛǚɽƴӼ¤Ƿ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɿƚȋӣý˥ƅЁϳǦɡυưДԔҘҜЎȿĕΣƶŦԭϨɉΈЩźƉ',
                                                                            'ėѕǇʀˌʴŏɯ\xa0гԞͿĴΏǾ\x91Ӷ\\ѰѶԝȍϩɂƑ˄ǽːΛƍ',
                                                                            'ö8ѢäƺϸϟѝҭɋʧђѠѢƂνθĀΏĺʭӸƇӒɿÊŎӫÓӓ',
                                                                            'xTЎҮƁϩͽȡԓϔμѢģǰǙӾʚϚÃ\x8dьԖ\x81ǁҎјaɲ\x92˼',
                                                                            '˛ˈ"\x8cһɸʱѯZǬɏ1ɍΨȗ\x89ӆπӐͻŒĞȆǚэɺģ˘Ъд',
                                                                            'ʥϬ\xa0ĝ³Ʃ˭ǆφНЈԌʗăаϖҼɓɯѵʞтƪζ~ŎĖʚ`ʮ',
                                                                            'ŜԎȋϐɥoƋüλ>ˏǒȹƟĭА5ʩҌàη¦Цăӛđ˳Ĕĩƫ',
                                                                            'ʤ\x95RɲʓӧǓƀ$Ġıɓ҆ʔǑşӝ9ԂʌԊʘϘǄћǐȺѭ§Ӫ',
                                                                            'ëԊēǢϰԇʴƏʣԫѤӸŘѱjˬѯӳԨʃϷʴΦɱ\x90ɭαïѢӛ',
                                                                            'ԇƓ\x91ϒȐêƮǽδмˢьLӞҠƮкǎīÚ\x85Ȗίƃț˳ҌҍЯ˒',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'л\x8eԏǋΖ·ɳӶˮʬЁřџˡҠʄŴîȓРT\x9dǞīѯǾɝӮ˪ϥ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԤWɣǳÂɉ³ҠҁΐӽaŬő7ɴsΓƤќȒʿϡYǀʹOǌѪ»',
                                                    },
                                    },
                            {
                                        'name': 'ϻ[ӱ\x9eҭ??ҡШ҃ѓʹǸǠȀªҁĬӒ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԔɦįǾҜͳĕǆхҝÖҲǈӴ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165331.667920:+0000',
                                                                            '20210302:165331.688861:+0000',
                                                                            '20210302:165331.709574:+0000',
                                                                            '20210302:165331.730059:+0000',
                                                                            '20210302:165331.750701:+0000',
                                                                            '20210302:165331.772194:+0000',
                                                                            '20210302:165331.793125:+0000',
                                                                            '20210302:165331.813677:+0000',
                                                                            '20210302:165331.835193:+0000',
                                                                            '20210302:165331.856148:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӌ˨ψǍϷ˔ӮԪɊĴÕɣŊϾäǜc',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ҭ˩ӨŞɶʳ.ś˖ƃ΅ǃІķңšԓӻǿ˱ɀЈΉ:ƑгĶǝʲѧ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Bºʲ҅ÛȖСNŲº˯ŦƒЊ\u0383ԥҨиǸ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 415968.8425145992,
                                                    },
                                    },
                            {
                                        'name': 'ͼ\x9aƨҷm ҤȁЮȯÁȚ7\x9cϑŇıʵԗÂ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            729405.1213541811,
                                                                            306328.7270940696,
                                                                            348982.20497761434,
                                                                            355555.0161311358,
                                                                            89076.09719599367,
                                                                            952359.9940242909,
                                                                            85232.6241963972,
                                                                            -49782.390937241784,
                                                                            40975.96244218643,
                                                                            109242.5143735751,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȞŠȏӑûъАÅÉЈƸˋ0ȥÏЮǆĒøɰǏϟΑȣ\x92ԛҜƃĺƝ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 640564.080312089,
                                                    },
                                    },
                            {
                                        'name': '{ЧÀϔЦбƣãçŮҖǨпLҡϥmгԒ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȶȮ@ё˙ǢѥÙΌ˕ǟ@бϤїϴøğтӴӥѴѤøЀǇєѻGҘ',
                    'message': "ȄԠЇӳҗɠϐǃΏӡ\u038dϥ˸ĳԢЧĴ'ԮΞA=ԚǽН¨κЃ°ʷ",
                    'arguments': [
                            {
                                        'name': 'ŵμƟч\x8d͵ɀƚΟςЛϚʂŻЇù\x87«ĭƌǵϼǈӷ˸ș',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5536306281794217866,
                                                    },
                                    },
                            {
                                        'name': 'ȿϣ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'дƦǉȜϋԛϬĥŇҗĉu}\u0382ʿȍŚƍρ£ϠâЫˉƗŤŋʙȠή',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɚǔɟǰҔͰ\x8eƱɂҤɤҮĬ±ԙ¡Ғ1ћ`ӎ˄²ıнßɂΦõė',
                                                    },
                                    },
                            {
                                        'name': 'ǋɊ˃ԔҋȵϩĤԠ³η˖1ȵӝԩəʈßϴԋȸȏҳǔϴͰЀƽԇ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            981875.4261885735,
                                                                            713689.9286964675,
                                                                            135886.94300243,
                                                                            484656.1638852991,
                                                                            863728.7117288912,
                                                                            979326.0457411674,
                                                                            211157.84658273275,
                                                                            433324.67296923057,
                                                                            246212.73882319656,
                                                                            774028.2892951879,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ςèϻˉÚŉǟĴžһʑƴН)ɚƃŐѮîIČȎɰΑЂγʽϿ\x8fɚ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165333.573283:+0000',
                                                    },
                                    },
                            {
                                        'name': '˅ηȱƁΓó˺(\x8dđϏǔҿxƄˏҌȪ¸ʁȆήԊѓcҽԅ½ǑƮ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165333.667229:+0000',
                                                                            '20210302:165333.685171:+0000',
                                                                            '20210302:165333.706270:+0000',
                                                                            '20210302:165333.726875:+0000',
                                                                            '20210302:165333.748074:+0000',
                                                                            '20210302:165333.768512:+0000',
                                                                            '20210302:165333.792444:+0000',
                                                                            '20210302:165333.822090:+0000',
                                                                            '20210302:165333.872385:+0000',
                                                                            '20210302:165333.962575:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'śùäҵPΈ§ŹˊЬ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            486674.0360752245,
                                                                            368239.5892556176,
                                                                            782651.867006045,
                                                                            576302.3593724525,
                                                                            316995.2879682355,
                                                                            6808.846466866118,
                                                                            -94406.2028624754,
                                                                            975841.8597825496,
                                                                            652625.8729008222,
                                                                            838951.4919898269,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҃\x92ȥёѿɣĔћŇьoǩɹҊƑĉЫҫʋҷԚIѽϳΓԇ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 768604.1994217327,
                                                    },
                                    },
                            {
                                        'name': '§ăҵà',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165334.827966:+0000',
                                                                            '20210302:165334.870425:+0000',
                                                                            '20210302:165334.942808:+0000',
                                                                            '20210302:165334.966525:+0000',
                                                                            '20210302:165334.990878:+0000',
                                                                            '20210302:165335.014120:+0000',
                                                                            '20210302:165335.033904:+0000',
                                                                            '20210302:165335.066277:+0000',
                                                                            '20210302:165335.090089:+0000',
                                                                            '20210302:165335.111690:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'κÜɆż',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            598707.9138200971,
                                                                            212614.46062081802,
                                                                            -23704.434855956206,
                                                                            212296.18792392494,
                                                                            609485.4939111153,
                                                                            551255.8881031061,
                                                                            162164.99566456955,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŞΈĨɌŉưӔАŉӘ,ěxǄɽĽ½ʃЯ϶˴ԅpЏłҲTχxϛ',
                    'message': 'ù˂˷ȒķąȔ˄ԤńˢřѹҰōɇȧʱŢîȒԮφљ\x97ʺȼɕƣÞ',
                    'arguments': [
                            {
                                        'name': 'ȜЬαȼƆ\x8ađǰȃԩƽΑĹ҃ъƊåЎҧ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӱаȄύˁЊϢѲʃ˲ǉ͵ԩόɜ7ӻ˛ìƑjұÆ҉ǽƓǚӒѻҤ',
                                                                            'ҜÍӋĴWʺС\x80iѸӓúњөҾhýәɿӨʱ´',
                                                                            'ëԁӂƲϹ¸ŮѫЧԟϖůĹƽīώćˆJ$ӈʳѲΜŠУӌƧ%û',
                                                                            'ơŸªԂγӋƞ¡²\u0378Ӕɕԅɘ˭ƣҎҕВяʮKМ÷ƾƹÊзȵº',
                                                                            '\u0380ȻǉȚɛĶÁXƉԫ˺ƆʈȓʅуόÍөӤĂΟƙ2ΏŌƇƬʤ\x93',
                                                                            'ĉǹɬĦɣʷɏȲǻӻǳȇǿΨϮĮʆӳ҅҉Ȯ;âλƦʮȥӬϺ˵',
                                                                            'Ȼʴћŷŀԫѻ-өǂΩ˧ƜƑʹ¬ΡЊIƕ˴ħîёƯӀʎǕǥœ',
                                                                            'ηjʮƜĚu\x8cʔмЄƿâýӫʃӑƢϷӣԉd\x8e¥ˈȾΣŢ\x83ϥȕ',
                                                                            'Ď=ŌυϝfѭӜÇǷLɐƁр˛Ŷ\x9aēO˜ѮɻщΟ϶ĹԍGʥϑ',
                                                                            'ӹрΧǟŬŧϯ\x8eσņÇϾǉΞʲӇʞлˉǵ҆bΰǹŪʼĻʻɥр',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'γƿ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҪʊS#\x97ӓӼоŤơҥǡҶΘԦ§˳ѴχîƋíЊɰϸ҈ςЬʢτ',
                                                    },
                                    },
                            {
                                        'name': 'ķćθċӕέ҄\x98',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165336.596161:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x89ΉȍǻΏƗҺРЁŌʼӦ҆\u0381',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            239318.1993963705,
                                                                            91097.72716402978,
                                                                            479147.5099379852,
                                                                            234752.58797462418,
                                                                            762195.5491611458,
                                                                            -55245.35198098387,
                                                                            326201.71480354463,
                                                                            187549.54261309752,
                                                                            210357.15715387417,
                                                                            -8727.61985905128,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'мʹΩұɳĝȌӊԇΞұԢ¤Ȯ˴Ǆ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165337.086488:+0000',
                                                                            '20210302:165337.116356:+0000',
                                                                            '20210302:165337.142066:+0000',
                                                                            '20210302:165337.164833:+0000',
                                                                            '20210302:165337.187816:+0000',
                                                                            '20210302:165337.210402:+0000',
                                                                            '20210302:165337.235282:+0000',
                                                                            '20210302:165337.263630:+0000',
                                                                            '20210302:165337.292390:+0000',
                                                                            '20210302:165337.320857:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÖųʰşμÍ»Ǧ´ȴư)љʽЎɪÝƓ7ǯ%ˠʟ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x88Ĉǘƍ˻˙\u038d˸ΑЌȥԛӒƧΞΊʾӎԜѧҜɴӶӕ\x7fɊ˷ʅѷѶ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165337.938246:+0000',
                                                                            '20210302:165337.963220:+0000',
                                                                            '20210302:165337.990158:+0000',
                                                                            '20210302:165338.019299:+0000',
                                                                            '20210302:165338.044786:+0000',
                                                                            '20210302:165338.068426:+0000',
                                                                            '20210302:165338.094454:+0000',
                                                                            '20210302:165338.127993:+0000',
                                                                            '20210302:165338.158012:+0000',
                                                                            '20210302:165338.178889:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѭƅѷʿ"æǂɀʜΝѦӦėͽ˭Ƽɰѓӥ˖HǬĔɀȠϏ;Ҽгȭ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5552944553228417200,
                                                                            -1922573068834713016,
                                                                            3541336683929966379,
                                                                            -4779517264314820141,
                                                                            -5791564949412212889,
                                                                            -2049409223817428211,
                                                                            -1199773782913019475,
                                                                            -6700726453325609867,
                                                                            5569697557620634781,
                                                                            8399973238632811948,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 's.ʷŦΫ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҸƉҠҽӫ³ǔ˝ǎĵ7Ĉ«ƗѾӷɷԑ\u038dљǦѵɆɲɻĀҊˠǌĬ',
                                                                            'źӧÖӐѹƍǱӏŨ\x89ǋǦɟ XŦ¨҅˓\u03a2ѻϏǏʡǮ˯ιʫʓƓ',
                                                                            'ʱÇ=ǒÁЯяUʁԈƻÙaϘţʾȪ˖ì˽ɼĮ;ЂÆѿGԂ§Ө',
                                                                            'ЮƹŹȞϥҝφx˱nΎӸ?āӔǪђīƂЧϿɒşʁӄÃғɉĩƙ',
                                                                            'ԘͶøэșϋШĆϦҸʷǭè˘ϨӤѥɎėӴϼϗҊĉԎѻˤϟυϙ',
                                                                            'ԟȐņ\x85ϐÀĞҡÍ(ˌxΎʆʩǉя|ϵԖɏɒƞЅѼtTӑųΑ',
                                                                            '˂Ԯζʗ\\%Ȕтԓ«´ÒÌҪȌūȴʴѼêǱƖʪǉπˠ;ĝƒǃ',
                                                                            'ʀLʃ»ΐÊBʱÀəķȃȃńѼȾʊǪȯϔєˌƒĵнańϺΙ¨',
                                                                            'Λҝ»φćРˎʳҀҩʨКлˢҢҴҬƍƸýΧuϫӴ˷ˆԤˋˊĴ',
                                                                            'ǔʟâҹάĵȶЛƆѫƋǜЌҞˣ\x8aõ/œȼĥԩӡ\x81<ȊƊÜњŪ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΔÎԣġӄ¬¥ĆѻήȃȵӤǡϮŠѡý',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                        ],
                },
                {
                    'catalog': 'ӆқɚòɌŠҟa¼ϕŸǑơɝεȝԬҲŖɮϧДʼҡыűҮЛŵ˶',
                    'message': 'ϸ½șӋ8ĘnҌΠԋſˣȉȵɏбΚϳȃƦƑюŧƲ³Čȇ҇Șƪ',
                    'arguments': [
                            {
                                        'name': '˪ӠҼ7ϧ$уȫʰƣЋ¾ĐԕЉ˧ѯȫӁ¶ĠҷϯNъĦѢ¿ЬǢ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '$Ϣ\x7f˶ɌàɆư˗ιңƗzâӨԨԡҝώlƀŮӝ¬¸Ħ«ӺͿӑ',
                                                    },
                                    },
                            {
                                        'name': 'õфƔ˜ϝä҄ƵÐ¤ˠӀPŏԣǤŽԒ:VÆƗ˄ҝĹɩǸŰǚʘ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ЪǋIΟϕʑ\x9eųԕїǦƯÙÎĈ1˴ϹЅɩҋӧaӋē˺ΞʮǰƢ',
                                                    },
                                    },
                            {
                                        'name': 'яȳĄǡ΅ï˞Ǿ1ѥ1ВѕӥBЬѡ΄˪ȊζζϴһΦƑӸπɝ˃',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 297730.9718726407,
                                                    },
                                    },
                            {
                                        'name': '\x8bȼʿʽпŵϋʄ~˽kԋӨ҅ŵ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ƅљԣʵ¶Κ˪ТЂťһϹτʭ2άCȳчˉǣȗ|q+ҢԕȮ˃а',
                                                                            'ȨƚĠJƶŃɼϗWʏȪȚςŗϓљϩјǰdûǋĎŤĜ\\ȻήĿͶ',
                                                                            'ԒɐôΉ΄ǾΔĚԓҘҀùԢҠ\x9fɥ\x88шŹȡʗԕΊŻňēƨӳǞȗ',
                                                                            'ȻɽE\x97ԋğҊė\x88ȜĻȯ¾§еƄʪÛɗ£Ũ\x80ĿϦéԌęӦӕƎ',
                                                                            'īɨңËӤǰˇʨʞҏҰQҹĝѻǸĔʝɛѲΓùҪʢΒɰê·˓e',
                                                                            'ˊή\x88˔гРɭІБ˔˪ϖ\x83Ԩ\u038dȥnɟɁŘӱĆťæ\x8aĬЋХŬҶ',
                                                                            'ōȸќ\u038b¬\u03a2UvˎԁȞБ÷ʪ\x86ǅϋ˶\x89ɰ\x87åʩǓʟƇЙćɠƎ',
                                                                            'ƴΧKŃЀũɰŊˍƚϖʠŜδ\u0381ҧƎ҃ԕǍ\x9d\x84ɹϔіȪͽʡ҉Ɗ',
                                                                            'ʲ˗ϕлĨµӚԚӱɖ\u03a2κфǋʾϖkŲŭǴ½Ѭ˔ĸǣ>\x84\x8fÒƲ',
                                                                            'Ǎ΄ţłƺŻȢƄļƼԝϤǖÍɌԩҰ˂ȵȘҜЁūϺтӂԏ\u0379·Q',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ƕğэ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ùƥ˟ˠZɿԅ\x8eȓm½Ο˺Ƶ¥Ėˆȇ˫ж',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            739917.2994833646,
                                                                            822716.9251940168,
                                                                            -7786.651268547823,
                                                                            180618.4171139846,
                                                                            -52849.0416077548,
                                                                            484348.77196470473,
                                                                            863652.3352833575,
                                                                            -88691.82498369725,
                                                                            962846.5464996079,
                                                                            599227.1999669943,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҪʘҘǛΑɅҪѾĆżΊʭÏƼĢλΤĕÒϸԜ˘ԊD4żβԭgǨ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -64366.30103943943,
                                                    },
                                    },
                            {
                                        'name': 'ȣрÁʵÖԦŊʅʴ_Á˽˃Ɛ\x84ǫĘȍɁʭѾԗСφ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƘƳ³§˦ξ˲Ół˫џĲ;҇όɜʅΞɖ+ȀƩż,ÅΛǽԡʋˁ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8009931820213852030,
                                                                            -7858582723736058853,
                                                                            -2801745989045967288,
                                                                            3977396293241803113,
                                                                            -2349915975268671142,
                                                                            8818126110856120517,
                                                                            -9195214296382056548,
                                                                            5622564730328093237,
                                                                            -4452602971111053375,
                                                                            5138257536052099400,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǝҮǒ\u0383ΥҢԫĭxУȾϱ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϛéȚщ¼ЕǻӈϲÜȧÌ\u038dƥǌŸȱ,ӗ˶ҹȎȧɧ΄ǀɯβ˘Ő',
                    'message': '˞ȺơӌЀǟ\x9cҩѝѬşΎȮ˓ņΉŅƘśðԄ˵ԒӎǸќйɶ\u0381ϫ',
                    'arguments': [
                            {
                                        'name': 'ϠǳMŸƓԫѪŹȦҒßЃƇͻǽӆǟŚ\x83ͱε9ȣŽɞΆѓÕȖČ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӒШϽȋͺј]ΦΈ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            564069.9281841557,
                                                                            935929.037883377,
                                                                            39937.51427602861,
                                                                            131.5706327666121,
                                                                            771029.7717244886,
                                                                            146093.7288647586,
                                                                            478755.74101168767,
                                                                            543354.0139808727,
                                                                            117198.58103919373,
                                                                            -56628.920569739435,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˵ϕƱԍţeԘȕêЉȰ°Ԫȕ?ϭҾɣӠҒКʏįɠљͳҔöęȤ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165341.955621:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƞφΤɌʎ˘ˣԒҷƞǕĂǬˠŨͲ\x8fʹЅ}ϲʣɌĢȡʏʥԉA©',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -677655859943266506,
                                                    },
                                    },
                            {
                                        'name': 'ϧǁӰƇc҄y\u0379ҨҖɧ˭\xa0¸ɘ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȞϹȥ\x94Ƹѧ+ƉšͶљ×Ɛçʤʄ\x8eЄӫϺnѣqЭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165342.295782:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϊ˂ϧŔҙĵ@˞ԗͰ҇ϷϹɻʫЅ=ɾǓίËǛÔѳӖѫǓҼҮʋ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 191666.86008558894,
                                                    },
                                    },
                            {
                                        'name': 'ӯƻ8ԎǘОӪЄӫӨ+úЄ?Ώӯ}Ąǔҍť˓ĚҒ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ëʳπ`ϕ0ʊźϸПɲ˚\x8eȯ\x92ԊǙχëиĵ·7ԓμģ\x93άԟŧ',
                                                    },
                                    },
                            {
                                        'name': 'eϸǻһņ\xad˪ǼҀƥÿŲʹęoӵ\x92ǊԌŹҒIǷȴ-ѠǑь8Ƕ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\x97Ť\x84ΉǞϖĎ\x84¶˰ǣȋӻүΈė˺ɚєԢСˢwɲ\x95Ƀӌϣέϫ',
                                                    },
                                    },
                            {
                                        'name': 'ǳŸɱ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165342.796699:+0000',
                                                                            '20210302:165342.821773:+0000',
                                                                            '20210302:165342.846338:+0000',
                                                                            '20210302:165342.914216:+0000',
                                                                            '20210302:165342.938609:+0000',
                                                                            '20210302:165342.961396:+0000',
                                                                            '20210302:165342.984184:+0000',
                                                                            '20210302:165343.006589:+0000',
                                                                            '20210302:165343.028692:+0000',
                                                                            '20210302:165343.050999:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '§цĳцԤŇӷʏɍҫѧӐäƾҏÙſΐŌƉˠ)˧ķƲrŴȘÄǒ',
                    'message': 'ˉӒӤ\x8eQɗɺʵαɳ˷ã>ɹԂԪäZɹŶː˯\x7f¬˳љоϭþƴ',
                    'arguments': [
                            {
                                        'name': 'ӜŕŐΖƓ˨ǁÒӱѹƍцӪǮί\u03a2Ԉ[ėƐҩҹϺdˈ\x95ʆԧԧҹ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8550648266892881212,
                                                                            8931424802753502403,
                                                                            -4697509337707068382,
                                                                            530316428531823295,
                                                                            902929406706091746,
                                                                            -7085140555270027935,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɼˊÅљĮѴ\u0383Ϥ\xad+ԟаѝƴğҕԄӯȄġˎԇӓʷǞŹЛɂJҀ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165343.512422:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӂϹɔґʓR1ӁYūʆƺʚѥɏƥˆ\x95Ηǭ\x84Ш°θˁԗɴ\x90фǐ',
                    'message': 'эǽƌˑөŜѪ\xadҘϝ¨ŠɪƌƏõаơĤǽˇѥʸŃжʾҲӖғϱ',
                    'arguments': [
                            {
                                        'name': 'ƶ˘òŹчѐǨɢҤģŦȰРВưƪͺφʬҐĿ¤ÏҽÎŇĒƐɜӍ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6811807093935941619,
                                                                            -7194444584584083181,
                                                                            -506066936670553640,
                                                                            -5053711162461321593,
                                                                            1942484573989642216,
                                                                            7749683409146634975,
                                                                            1718832962565200949,
                                                                            -7326552868886379769,
                                                                            -6436604076997362739,
                                                                            3981941252150577791,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŽǨӈιƽŒǋƌѼǒ"GΥԀ˥<]ȹ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3174656010713231198,
                                                    },
                                    },
                            {
                                        'name': 'ĮʊȱņӚВ\x8bӇ\x81ƖӄϰԭϓβƼҳŏєȓѾľ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 951651.6858799194,
                                                    },
                                    },
                            {
                                        'name': 'ŐӲɕϓɴøgϾɚťϭȥѻę´ǴEҽsżϟȯAýӻɍň\x84ʅƉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 886885.2840991735,
                                                    },
                                    },
                            {
                                        'name': 'ҙά\u0378ӡȜѿơȆӬ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˯ӫѹϻ)ŰİɆӂəˢӼΣH?\x8cʩÿɪѲґĹśҙŘǻ҂ˆˎӏ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3111501145762117892,
                                                    },
                                    },
                            {
                                        'name': '\u0380śʌƀΥϘʓȥ\x91ʬcРСЧǐ˅Ԅ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʊȰʶвʄȏĀәєƓʏ/>ɋпѢϲ҉˫¸øɟŇҴԆӔЖʢĂԑ',
                                                    },
                                    },
                            {
                                        'name': 'nǗƹϧ¯βψɨŇɵ·!˩ζН',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3186781447236383452,
                                                    },
                                    },
                            {
                                        'name': '˴',
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɰʻ˩ҴғҚȑǼƇ\x96ԜɿˍÁÕʞˉғзӖĶˆǇ\x7fѐʪϺѤ;ɻ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8909312389116536605,
                                                                            3164770800939118603,
                                                                            -1925674885888637486,
                                                                            3066354056776118483,
                                                                            6852548788037189451,
                                                                            9055729560736103390,
                                                                            2067517016052854850,
                                                                            -8255763816902049429,
                                                                            -8825588204237825654,
                                                                            6901212632052218585,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӀҪǙ+ʜΰİ˭ųǉЬjƛĉ+˙ɻƃńÉÒĳwňɄʾȇҵķȥ',
                    'message': 'ԒαŴͿiфĭŜӸӻr˔ȞɳÈѰς˲Ԩ\xadCѶԗǳƧʶ˫сѬʨ',
                    'arguments': [
                            {
                                        'name': 'ʼѨ)',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɏ¤ԥŢѐɆƞтХKӅ+ϗ®ǤÃΥХvĮΆŘ\x9eăӓѓυÓԫЌ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165346.488054:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǐ\x85ӺȚËĴ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165346.566031:+0000',
                                                                            '20210302:165346.585511:+0000',
                                                                            '20210302:165346.606928:+0000',
                                                                            '20210302:165346.626882:+0000',
                                                                            '20210302:165346.647172:+0000',
                                                                            '20210302:165346.666198:+0000',
                                                                            '20210302:165346.686317:+0000',
                                                                            '20210302:165346.705078:+0000',
                                                                            '20210302:165346.723236:+0000',
                                                                            '20210302:165346.744390:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'клƯbυêљϩΌϮŴѸϒԥԩʍӞҹ5Ǆʴѿԉϋǰ¿',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4535575387390326333,
                                                                            1615840408218670586,
                                                                            7801766836309377321,
                                                                            -3008921000072528597,
                                                                            5154064479730742871,
                                                                            -475508797318178560,
                                                                            -7544214450639036394,
                                                                            -2223588572971614628,
                                                                            -5333979856995298154,
                                                                            4016724602212557073,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѝ˰ʎύаǐ\u0378ωÂΰϰÞҵΉ\x86ǊŽďɫˇΚĕЕǒ¤Ӈ\u0378ʂϗ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ˬZĒαȇͰΉū˸β÷˔ƒČƴˇЃԃɎ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165347.182831:+0000',
                                                    },
                                    },
                            {
                                        'name': '˪ϳɰңđgǏӁʰϋΛƸȍҁʹќςʝ˧Đǐˍ˲ʬρţЋϖμǛ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            848346.1099963798,
                                                                            367083.7283362131,
                                                                            32239.873602252424,
                                                                            756151.4498370622,
                                                                            222414.67076634336,
                                                                            952203.5681984155,
                                                                            558912.2211813892,
                                                                            66436.49701424842,
                                                                            915897.6107584193,
                                                                            460062.3371228544,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '²|ύơй\x97пɹɬҰūɇŔҒǶȘıҟàҠХҭƎʻʄҀɩ=мˍ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5233312094901695799,
                                                    },
                                    },
                            {
                                        'name': '˺Ǩ˝ȦЩǆÃӵӳͷʉǙˀыδǨŦ˚ˑɨ½=ɷˮƖ»ʛÑȝů',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƝτŀBΝȣ\x9cϼʗǑ͵őЅІԑɈӶÎʵњ΄ǫҐ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ͱрĠ\x9eΜ˷ƙϮӽȒо˦ΪĆ1\x81ŮųɑΔΟӟ˂ɦʆ?πҒǲŘ',
                                                                            'ϫˮĥǠ\x8c¼ʴľDěÝĊρύłѿҷхɢщ\x92Řğ*TķЋVӯԎ',
                                                                            'ĠΏǂВɢѷɽƤŗцəχԋĦϋƛкϣȁχĂIžΠÙ˨в˰Žα',
                                                                            'ɍǼʵϜkĥΞȅÙʻџβјȄґіt\u038d\x98Ӡʱ˕ƤRļҎгԠɼư',
                                                                            'ΩƆȀ\u038bąſ\u0378ǂÁ΄АшŦν˦ŦчÑӌšƄǈѢϺʧӐʷƭƟǣ',
                                                                            'ǋԡҏ#϶αωҼ´ȔŒлưļѢ\x95ҚíˏōŅȠʻʗőďȬȬѕˣ',
                                                                            'ŚŋњɒкȀǷòγϨϡø\x95ԆEЀЭѐé҈ǖȼƈʁåјzɇÅί',
                                                                            'ϛзȞйҪɊ ŻǷ2ʉλ|Ѵа¦&νΰΗґΒƚÒƫŁҏГʰ\x91',
                                                                            'ѕƀȮ\u038bψUǌȇӁˇcFſňoϨĩԣӏϹЭҽԖЕЉΖӮľ΅҆',
                                                                            'вИďҳњŶξΚѹ;ƣǻǘfѲÛǉǸБąʈÒҲљ\xa0ŰĚˡнԅ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƕŦǐЀ\x88ƧSЮϣśðς',
                    'message': '˳ЂêŋχǟʫŔɛªȹňҹɃƦҘӃХǂȓϗʄŕħťϴɳĮвТ',
                    'arguments': [
                            {
                                        'name': 'аĮļ˼ȁɶŋĀŗГǜԘʝʟҏӷҿˬÔłяƖ×ӧɶǓ`hҠͷ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6612426011396717603,
                                                                            6569679486952466416,
                                                                            -1456859697970888630,
                                                                            -4102789015415038318,
                                                                            2578494247587365580,
                                                                            5529568389688404067,
                                                                            -1032552189244480750,
                                                                            -3450840992847969349,
                                                                            -2713797827012403121,
                                                                            -1319342372575053376,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȋҼЕÝԎǿÒȤȜʊ¿ͼÞғÄЂɢ\x97º˹ƣȌ\x8bʫ˱ĹЦèŝɥ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': 'ϔҚ¤ͶȶϨǔȏιϝɮтʍʳȃʭ*\x8aBɟϰ҃ǿ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1153595045324387853,
                                                    },
                                    },
                            {
                                        'name': 'қˀźӶŗˀљ҃МПқʟѸɊńΝЦ¹+˟ϼҁȢϡ¶',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7720957252422216593,
                                                    },
                                    },
                            {
                                        'name': 'ȬѸϧΆsҌÈs<ϻǍzϰāźȫβϟɆΜЌʲѰ˳ЦÍÓрiθ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '҆ɮÊ\x96ȸԣӣŃ¥ԁҠ\x91\x86˴ʫĆԏψе\x98ˋԭǱ˖ϪȎÄоҥǝ',
                                                                            'ҳWïSЎǠʋðϕ¯҃ʪɛύԓǣ½ƽ4ԩȰТp˒LɲИԞbÄ',
                                                                            'ȁԑ˾ЭћŪþŐʭ×CʼыÜʻȑµҏȒ˅ÎӍƠӘ9ҦӇˮ\x8aŨ',
                                                                            'ҎӑˊїϓѪĐýŢǫоѾԅɿƷǜLȥСɯԨϪӸĄ\x97ӀéЌƺʞ',
                                                                            '`ҪΥå҅ĩÎѵΨʛ\x8dМΚХԠAαǊХϦҌʤóˈӼЀŝĚĤɰ',
                                                                            'ƖүҦԂɶɟì!ӹǨԣЄŎƤ\x90ϴԞԒϫʳȉť`ʭϦȰɒҔЋ;',
                                                                            'ƾӷӔ¢ј΄ˁfŏЧљĶңŷǥʼ¡ŪƣƃĆǌrл;ϑ¸Ǽ\u0378İ',
                                                                            'Ȑҫ˗ƯӃÍwǋŚN˭Ȣ ˫ϒʳˁӡΔɚǟԔɎцƒѵǅɅкÅ',
                                                                            "ϩ»ұϐȽǚɷԄ\x91ҷӣ·ɨüɦӠəυϓɺÇƾьDԀ¾ʙƐ\u0383'",
                                                                            'һɁǴŀ˟;έæȾјҐϙÌĪĳĢÇ˷ǜs\x92ɍϽ\x8eρΤ\x7fԃňɎ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'мȕΣ!Ǟ¿ϜĉłĴϰǓ\x94',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѯдβƨƖмΙ9ƅҹǇʍ\x94ǵ\x8bәǍbΖЍӼҕƂΒ×ˊƍʢǌӊ',
                                                    },
                                    },
                            {
                                        'name': 'ʥЌЁɝȘ҅ξ˯ϲɆʍǥϠҡĊҜ)ԓʅБ8Ό\u0378āƢɚӪΧэƇ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            225774.54995808785,
                                                                            312602.3370814432,
                                                                            636523.4651391604,
                                                                            534036.4052666349,
                                                                            104501.4949089633,
                                                                            667961.4706942693,
                                                                            280999.5597632448,
                                                                            508953.98018382455,
                                                                            605388.6640156215,
                                                                            283295.9433007142,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҟҶŦÀú´ȹ϶Ѝ҅4¿ƁСπïѪρȋȳǔ˷ɦC˨§ſƋʃǃ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŽƣϸѼҎΏѮџԣCƳɏžȄKζϹԩʿ˯єɩӲÈ˖ѰĥʟǤΗ',
                                                                            'ʘѻȐŤƕ\x9fѫ˱Ԣ\x92ƛǝıÂȜǷɥεŪɉĬѳӅǔąơłԭˤů',
                                                                            'шǑɾϛʪďʭМΆϡИ͵τͿĶ¼ĹцԍіƻƐѓŕ=\x98\x8f҄Ȗ.',
                                                                            'əŢԅѝѳD!Ξү\u0382әúɛċϤ҅öϕaƊĽͻ¹˒ưφȎ;Ӆ±',
                                                                            'ƽ÷LǯĈӔԈɘϾƂўǜ˩ЄΓӻ¢ΗѳŋǼŇŖµ\x97˔±Рϗϛ',
                                                                            'ΕÑfͲ҄ӽԓӌ·ϒɓĜƣȥҊȞóǵЮΧčXϯɐÜǼԤͼєΚ',
                                                                            'ѦϺɧȈäʕВʶĻʤǟUпzʬͳĳˎʲƣȕǂ˾ΠǦĔ\u0381ĂƩˠ',
                                                                            'ɷΚ\x87\x87\x8dȌӋȏΥ˦ѿƭӈԠʜ҇˧ȯtLҲȉĐˍĴɡƳʠэŤ',
                                                                            '\x8aŻШlʭ˻Ńχ\x8dҡШǌԮӉзǥ5ͳž°˞Ƽ΄ǟcϺ¿Ǭʳ`',
                                                                            'ϕȅљʙ)όҟāί\x860ƈǏ˪1·ШϽːǹӫœhӭσ˞ȀйХŏ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¤ʩЖ˃ĞѿъǤϡŐƎěȃ͵Ƅ˧ϧƭlʥӽԩ6ǑÏĲˬB˽č',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8233001183574544458,
                                                                            3786386896242508171,
                                                                            2168890507882391781,
                                                                            7785881401249747346,
                                                                            -3956130804457212928,
                                                                            5866896304019453988,
                                                                            4668668830812261747,
                                                                            2010684186798284263,
                                                                            8494354342727347691,
                                                                            -8073244985139915603,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '"˧ћѐƲȻʂƆȱǴˊϏщԎȋӋϢΐƞ¦ÉƑqӟмǩ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2378582309223043436,
                                                                            -7384042772746890699,
                                                                            -2958688985108830514,
                                                                            -8986238411872797389,
                                                                            3855096938022160925,
                                                                            8005941164281631916,
                                                                            1499611289164901150,
                                                                            -2080371361543749175,
                                                                            -8218046129383796891,
                                                                            -3438532282798080045,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԑтˑɽΥӦѕȫЋȗ˴ӍӃʹåхЭηӑѥoGŮԅѨ¤ЋФԁɖ',
                    'message': '˟ťǙԤФҳͲΨԥƭѯίƅʽĮ˻ĿʂЂǙĭƮҺǘèΜƃςĠϖ',
                    'arguments': [
                            {
                                        'name': 'ҳŢɛɠìђćǺ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3756891831712058905,
                                                                            -3926511207155365132,
                                                                            2630280353506360825,
                                                                            -3845788436787430448,
                                                                            6316154146064612024,
                                                                            906085828705169532,
                                                                            -6946261890381742853,
                                                                            -2598629275832397784,
                                                                            3760413417209706248,
                                                                            6923041869660714620,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƜLƸĠ҄ɭҔé\x94ʗŚӍưƽωέҏyȡģˢ£ă',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'esԞѰϗА˛˕]Ŭ҉ҭ\x9bĴťύ|Ԇ\x92ҕɆʷҙҩƖ,ë˷ě9',
                                                                            'Ā˟ɃűȨXкB½ɽǼϙЌѩϵИˑЂʹǑĊÑu\x9eχ˼\x94¿Ĳɞ',
                                                                            'ǥϦ˴ǛͳhǉԊːȉ\x80ʚ%ŷ\x82ӖÚðǤѤɧƯџʂµ϶ȸҧǅӻ',
                                                                            "\\ʭ'ȪĆȓƬɕÃьѠƷɁȤѰȎhǄƯЀôŁ:шʶɒǸζɐ\u0382",
                                                                            'ŧғΧɇѨχΜ\x86ъӉЮΞΩԅЋȁı˱^FŋΔÊ\x9a¢?ǂ˓˪Ґ',
                                                                            'ҿ¬ȎщƱШ˯ИȤʣѓ\x97±Ķϡ\\ƱŰːʯϕǤǍ\x98řǌòȐáÆ',
                                                                            'łЋʦϿxѓ҂±ԫƎțȰДϧǖӱѽοűυëӷȧƌӲæѫӱǧŅ',
                                                                            'ƑÒўΦǐʒ˫ΖĢĖѥύċʩūʍΫˈǹØʹӺНгɠʋÄɫˮϷ',
                                                                            'HŰʻ˲ӫĸӮҋʉɨ]eɿӖķĴ!ǙªĭƆˈŜħ1ʩччì#',
                                                                            'ïƖӶԦȘϏOϑϵ§Ъă˹ΜǊoЂӝѺҽõˎϨԠȷҕԋʆɗҺ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѩДÉǅҐйӂ\x9fīǺϔźdĪŉȗӄΠåЅȢΖŘƶǼ˺ȽŁӽӈ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165351.324173:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȧϟǓéƨǳ\x8aɨңº×ӠњčǆˋŻɨO\x93ƀřʈʋχĬԞФѰƃ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǍȳцrÀªwӐԋԢȎʎΐƊÏƫƊћԂŊ~ɳ˄ӗԞϦEʞӗƧ',
                                                    },
                                    },
                            {
                                        'name': '\x8dӛƝɨӨĊԁЗɀɎˆǎӢãɭƟ˸Ęψá϶Ŋ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ǟ4ˋӅіĸȃ҂ӆвШӜɛƞāΣ}Ξŀ˭ӷƝϚˈGҁҳ¡ȹĝ',
                                                    },
                                    },
                            {
                                        'name': 'Ύ\x83ǼÓ˂ɗϙ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            758125.8153626492,
                                                                            216123.88954130502,
                                                                            517560.927956335,
                                                                            479226.73631269974,
                                                                            126359.14199742654,
                                                                            213997.94433914346,
                                                                            752037.1162015641,
                                                                            856378.1787923279,
                                                                            590399.4056256454,
                                                                            207034.92347201175,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϫʘƪ˳ƄƞΊQûѰѽXěǠÛɀʲʞп±ʋҔҢϒeЩǧ\x80âԍ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 45284.63514636617,
                                                    },
                                    },
                            {
                                        'name': '\x80',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ζ>Ƹɋĝɐѐхˬԡ%ñśÁ\x94º·ɔĔȋȄˋŔȁҠƶƹĻˉԩ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165352.052866:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϿϨ8ʒƒŵ\x9cȽŧɑ\u0383˅ʀȥωƧ\x80ȄƷÉşһ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165352.136684:+0000',
                                                                            '20210302:165352.157708:+0000',
                                                                            '20210302:165352.178583:+0000',
                                                                            '20210302:165352.199902:+0000',
                                                                            '20210302:165352.222531:+0000',
                                                                            '20210302:165352.243868:+0000',
                                                                            '20210302:165352.268842:+0000',
                                                                            '20210302:165352.289854:+0000',
                                                                            '20210302:165352.311210:+0000',
                                                                            '20210302:165352.331791:+0000',
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

            'identifier': 'śŻƼȿѥ',

            'categories': [
                'network',
            ],

            'messages': [
                {
                    'catalog': 'әɉ',
                    'message': 'B',
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
            'name': 'ǌ&Ӆɍɵˠ\x9bџǂó¥ȵƬǝҎƉҖ',
            'error': {
                'identifier': 'ϼʢ¶ùɰΒЭěŪѻѩԞ˶\x8dƫ\xadȭ¿ϝ˅Ǎц$9ÕĐ˒Ԁ˳ϯ',
                'categories': [
                    'configuration',
                    'invalid-user-action',
                    'network',
                    'file',
                    'invalid-user-action',
                    'network',
                    'os',
                    'file',
                    'network',
                    'configuration',
                ],
                'source': 'єƪôЍх˹ʓŔȰǒÐɼϹXɏАżӫĭʞļcѻΣgƢΕľÒѧ',
                'messages': [
                    {
                            'catalog': 'ƇЋаaȈ\x81ΛдӶ˔ƳĢӲΓȗȭˇҕěƛʵΡǏϡПĔъ^ĴИ',
                            'message': 'ЂǦ˼ÞʴԆőӮΠ\x98Ƶ˵˼ǏЅ҃І˙ˍЎr\xa0ТƁӉϹ·ӻʨ˟',
                            'arguments': [
                                    ],
                        },
                    {
                            'catalog': 'ҲδҨȶŵů7ɚȳǎǚц˓҃IȕҘʘИфϼТɕ_Тɷ\x87ŵԬΊ',
                            'message': '\x9a¸ʖ\u038bȺҶϬáӏ҂ѩĪϡΡϳѮӲѓXyԭʅ\x9d\x99Ͻ6Ǧʸ_Ɏ',
                            'arguments': [
                                        {
                                                        'name': 'ɝʂƭϦ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'çǒΠʽɷđ_Ӎǿ±Ąӆѹƌ΅ˆΑΑЩȟɃ,ūŌIӜӠ˵ήѠ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԈʭȘŵťȲԩъRˣΫÕǚ}ξûӗØΙʚ˴˹ԙʼ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165320.908162:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʡԐѐǪ£Ӡ£ȪèɽýĺѫҶ·ɫž˛ćħʯΝ\u0382ȖŐԝ˶ɒъɘ',
                            'message': 'ƆӚίĵӦˎͺĳËɩġҮОýԂÓĺřӔǽέÀĥƉаʖԒȆĬȘ',
                            'arguments': [
                                        {
                                                        'name': 'ΗɓΈϳǩɢŅӚơѯǯĘԡϱҖėҧ]ЩĥҠƩ\x91ĪɌğ\x8cʑŨ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΕːʜũÆʤěȋ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5753416106985077508,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɼɭvϻз@ԓɮГɻӡԡРĈϔƊǻǾ\x96ÙԄ?\x9c}Ǫ\x8a˪ӽϹʞ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԜҬѿԨíɚЗϚЈԝƋϮ\x8d±ʚͷϫĳҮȯýiѣҟʏuЀΘ\xadȦ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɮɑ\x91^Ҝѯͼɇ§ŗ˴ӰӢШȖʭϚяȳƤϝпǽԖŢĜmɷ·Ѐ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŠGͶzӯʆљψУІĘĝҐʵƗ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¸ŦǿªƂҠуӧĢ8˫ʸəв͵ѹ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'vϰӮһȥușƊϨЋ=ȂąӠҚѹÿƬгԗҩɛιƕƤ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ІˉǌÙ\x81ӮôͿϘpΠϪƉ?Ԃ˼Еϕɬſϕ§ķБȎηç\u038dmœ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɷɨƟҹҷ˖НĽ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ŰχȪǂƷũЩԮЧ˗ǓПЌƓŉ\x90ĔҭҫϤʨ?µ\u03821äК˪S±',
                            'message': '6=ƞǎĺв˳чώɂҚϱͽΎƯi\xa0Ѣӑ҃ҧӑǟ҄ҠɠƚÓǌʂ',
                            'arguments': [
                                        {
                                                        'name': ':Řȹȱɦ~ћӭǅǭ<_ʈ¸ČӛßýěϋʳӳɺμȋғԂʻѓĤ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165322.134178:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƑƬϔ\x84ĹȞæӉgƩҮšŔ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '%ƙтęθñʈӸªƳ\u0382',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ћϗӅ±ӏâʯƄíƃȣɪϺϟӝȐѫɠӂϪρʮʒпϛ0ȩ\x9dǰԏ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'žΑĈͶΝϷӁӫԨЕѻĳ˙ӞΖƅЃԗŜʲсʂҍəȺѤɍЬƒԝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'χǻ\x8f,þ϶ϋ!АхґőÖ^ƨŹΞ`ҹ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165322.634846:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'řŔʥʫŅ´юпɻĕӲ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'юȦмMϊЕˏ˯ъƷÚ©ɝˎӷϸѝЕŒʗȚɾύΆŲҒȓɬњȁ',
                                                                        },
                                                    },
                                        {
                                                        'name': '³=ԪÛÏȭЍ˟ӃƎŶΆǙ)ӖȅЦГȱ¥ɭҡΜ\x80ą\x7fɾӠϩƌ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÐɩάƆєɖҨЬȩð˒ϵχđǗјЋυԙƨƏ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "Xʘʀ`ΕŤ'ƗЇɠМψśŘW\x8dѐłN˴χȉѱόÄеҒϔ˦ȣ",
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѯȒϙɾʙӱžGȜќʷʁĲì˛˛ǽƩƁȰȼȽԨΓҌƁэʒIȠ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8805713650937458443,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĹԞӳТ\x89ʑ°=ǛÚ҇ΛӓĐȽυыҗвŤԖԐӟςÿʑðѧԗȹ',
                            'message': 'ɊҮӛ϶«˜ɼÞ˙ί6ԕŨ¶Æԕʸҫʵӿ%Ɖɔζӻ=ЉÓϤѬ',
                            'arguments': [
                                        {
                                                        'name': 'ҒʉϴcʬȸңϦЃУυ\xadɕɠōӤ\x9f',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165323.117177:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЗGEǡ.Ʉ3Ȑ˚Γ1ñҘɡԏ5',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4982918781544667278,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЫҒɫд',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʲɪŊзʆ˨И`ƹűɉϥ΄ӖӕʬĠǰȕԓ}ňԈłȸʿ ȥǡʒ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'τϸˮƵ˃Ʀ&ο9ʹPƴ|˅ɞĝ:ǼÊÜƌӧŭ{ȆǨåϋӾП',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͰĄʒOä|Ҽ\xadβθʘǲѳƒӫО˟ӥγʢèǅԙ΅MrϏҬêH',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165323.426220:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȫ˨=\x81ʿȟÞRʗjӅƗĄǼҿɅʀƠŕǈԖәĭÈ\x85ɡĭќԑм',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˨͵ҙ3ƬѾƓϐԨçgә\x89ŌԜȑȢ;Α˸΅ʥąŶѳȥέ(\u038bȌ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЎԔƨlˋȯǪɸ7Âкԁ^ǟôͼѮʭȘ³ӅĖѭ\x9c҂)ǼƶɕĄ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165323.677477:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˠ˟Ěśҏȝ2\u0382ѸǕΣυnϿ§Фâ6D',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165323.788764:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʚԢnЛPƟӸ˅Ėυ˱ʑғǠǗȐ\u0380ǲˮ,ǍZʲѴʊʚҒĲěȻ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ѝ»ҢҶɀϻԋфÿҽƀÐ¿ɡ}ŕ^9ЕǵϺѵІPӼҒǲΥʗή',
                            'message': '\x8cɐˌïğBĵЏƹЭЎϤќƵțˠɭ͵ǿȽ,Ξè˛șǛÑэŻƔ',
                            'arguments': [
                                        {
                                                        'name': 'Üùѷ˴VєΐЄ"ѨӉðÉМwØȜƵǹЍϬǢȋĔ9Čҕкɡϒ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƨŠǗĳӘO·УďƼ\x8eӼҧɪ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɞ°˞Зƶȭ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'öȲƍ\x9fˤƾXʲэȣӾҎȥˀǂφ¿Ξ+Ӄ˗ćҹİʴ\x96үϨǝԄ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŘŞÊH',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 141197.16904634365,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x7f(«ӖΙϔ΄ʜÕӹ˘ϷïѸȽ·ʷÑѷӔȥЊҙӏѮАȤǮÁ҄',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 513127.89841892454,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɨȹСΣŞʼ҆ʦϽƏūһΛǞő˂˹ɾҤԞa\x92ҰIĬӛ҂Ĥԙș',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165324.944654:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΞĴͰeɹȥ·ŠɮˌҰĥԞϸ[СʴдFʹʯȵ1ʙ\x83ƥӱƲȗĤ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4080111176944321051,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӗɞ]ОϳƑ»ȥƟɂƴˍǲ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165325.176816:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ėȱѤˁǄƙĒɀҺпζӶǉǈңѝҔÇ΄¥ΕϙéӰɲ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165325.255905:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɮͿкͷĉǜǵöˡħŃнɀ\x84ˮ\x9aхɯ+ü9ίύ҇¦ьҩFҐȽ',
                            'message': 'ʸˍ˵ϵӔÿÉѮˢюіԁͿŨʔ(ŪŪӣΆɽ\x92ԘƋϦ҉Ӟ˷ʚŴ',
                            'arguments': [
                                        {
                                                        'name': 'ԆһϢϮǖεΜƛæɑȢŉȐ˔ȺЕ\x88҈ţǱӠΝɰƛŠ\u0381',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʋΐéԞѫӐLŦƾÿОӑϷÒйǨïŇHӍΖȇ¬ҭӌξ\x81Щ˒Ν',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǨΚúčǫǽμȠȯŻŦ˓ɾД˄=Ԡ~bԕ}Ä¤ĳДԫƨɺØʊ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 454500.1542627737,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԒԥλɦчӴШȢѬΪԐǯŎļΜǻȄǢԆǎҙҸſÛӔɂ/˰Ϥǐ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԇ¥ΗˇKЏÜԁ\x95įғϝ\x93÷*Ǣ˧ȄǑȼĳ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¼ҽĸɱĿ҈ƫʗ<ZǍ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ңȥɵȂԅЉϲƑĹԚǌ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƾ\x86ȇˈӱ³ӯuRƨʉpҿƩſűԤȇǃʝň·hȇϻ"bʇĂʜ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7628658769514185784,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ңĖˢ!ŌʓƅӅăʭƴӽȬτɺeԒї2VϣĒϖˎ\x95ΙЈ\xa0ˣȜ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'әɛǊщαл˥ʖ҆иЙӄ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "ϣӡԊþFҜęд~>р\x9eɃÜɻǆRČű¯ɲʾɁj'ϻҔʱӣȣ",
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƟJ½ɽϐųʟ˄¬ĉǀҼҋsԘсˆίšlĀ˲Rgʞˡʮ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'lƺ˼ĘP¹äȍƩƀǩʳʂѵ\u0383ʝƣЯԘɒĸ£ɤҜΕ˘ɞÓó\u0379',
                            'message': 'ӣΣƕЩβƼˣ˽ɆȹœԘд:МƋōȜuѫ\x8dШÌР9õƋʜªҞ',
                            'arguments': [
                                        {
                                                        'name': 'ҞǾӁԬƋŨΤӶ˵£Ŏ5ɃӍԏǫʩ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԚМѪ˵ε\xa0®ҢτĪɔнσӹŠʏɩŖϝʴʐȻˇȕĭƪĳŉѪÆ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȘÅѰȻΨʖ\u0379ŷʉȆЎŢóԗʌʊӀÎ;ɊʻʷĻϵͱΤðęɝ)',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӛǶϿƫҔӋĶˤŶɪԌΑϜϚ˨˖ʇ˹ȐȷĶĥǭCϭүʵƔЁw',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 917410.9605690538,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӌψāɒҿζƨЕ҉¬¼ɿΩˆͼԦʪuѼ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165327.080056:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '^ȸӮƏԚɪ8ʻȘͽӹʁ^ˉԦѥŎөƻÜÕÖ½цԬȱǞі',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '0ȆƐ˫×Ѧ˒ÒɐɊǑɥȹŗxгҁˢǬУðč·Á˚¼Ў\x91ΟȺ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѻӹЭԄӓΔϝύӼνӯ\u0380ԫìǱīϏʆċԄЈƥǙӒËԫƦďƪӣ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǮƈƀɪŗēәΤˁΜ{Ňϙhɉ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165327.541625:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x94\x7fŧ5ɱĞҶɇӝŅ:ăBŗ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'đ\u0378НɹʮϘ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 655091.6358542533,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЇƎӜ´¼Ӡ\x85ěԥˬeЁʦEđȪŋɤšÔȎ˨ϙӿЋ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165327.937942:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': "'Ư˩ҢrΉΗ\x98ʧԍ7ӱԋԐΧáBǤ\x9aӵԖ˷ǣʎҡ҆Ϫ°Οɹ",
                            'message': 'Ɉɤ3Ƶvs¥ХĆӤƓΦČǆŜɤώѶ\x97YͲɅ`ʮϣ\u0380ȘѡϞԘ',
                            'arguments': [
                                        {
                                                        'name': 'ԩɄ\x80·\x82ԬƒΝзʅȞ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԚϦ҉ԎϼӛҮ¨фǪLưӲԍmċŸǜåRÄƼºρiҖѭ8ȍŻ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ћԘҘʁ=ƿʙßǞӭƻŬʋˌ˕ɼӃʁҰάΨʴѐÅԭԥéТȥǩ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӈѩǼɠ\u0378μѸʅ<üΨ¢FΔʀgɦs"όνu˹ϰйϽǬ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8945197483455616089,
                                                                        },
                                                    },
                                        {
                                                        'name': 'μ=˥Вϣ˅˘ǃ˵Φ\u0379R5μҞÏҏңÏƐ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȫγr \u038d>ĊӧŊҐϷуѨtɨþŇűʓѲԉôļűǨŎԛʳļ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɕ1ϺыFҖԢşˍ\u0380ƱϮ£Ů˧ԏǨΐϹюԋ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2800047768484710941,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȽĒ˵ĪЀҲȲб\x95Ąʝƴ¨(·Ι˖ʲЪ҅ǸƒкЖɮ9ӌ\x8bҾ\u038d',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѫ˭ΟŴшҕн\x84\x80Ǥ\x89Ÿč˙˫ȽΔ±Ѳο¡ɘѓρ˸Ƈхԝ\x86ϊ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1114133579922828056,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϳŝʝ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165329.038861:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƺԅ\x84aͽ\x9aӸfҷϚ¢ƍѬȇԮÞΐЅSϚΧ2đѻüГŗƲɊ˧',
                            'message': 'ʲǬ9˄ŐӁϯæȵϞɀ²єѽ¥ғɹԃΝЊԣæΘҋш5BмόǷ',
                            'arguments': [
                                        {
                                                        'name': 'ɯђ\u0383ЍMÁƃſĦBʺŕĔ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165329.410240:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '§ӝҮȨŻøĨӒѧȰʦƪćzЂτȮƬǄCԑ«ƥ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǌĪưъceDåҝɵòĝƱǳĒ˖ё˭>7ЎR˩ԧѲŌ˳Ëˬԅ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǬѹþеӫҠӞӢψȻ¬ɇȡLύΤЫνԉ\x9aĆəʶʦ8ԫκª\u038bѕ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҡΖƝͶӼϞ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϟ\x99{âŸğ¿ȸ¨ȼ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƈͽ+ҚΝΟί,еШŖZßºæÌ¸2ǳќŎːѠɟҞ˟Ǵdɔх',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӂѐ.ŶʰŁҜʍǨĊÿ¡ǅ\x8eӗͻԥőέƍ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165329.932688:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ļ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '³ɗѓ˅ѲNÕΧ\x84°ԏҕύӒԦ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1946202251662153808,
                                                                        },
                                                    },
                                        {
                                                        'name': 'HҘǐѼϣ\x8fͰŴɱˎǵ˰\x85ѾąƜΑşԙζЦѯωҟ\x98ˬȣΝʱ)',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҟΩƼȹ÷İӿɨѻ\x8eĤĆηĔђæ\x81ШѠԢξ\x85ҁΦȤɧ¯\x9fωŒ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 9014665224924433322,
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

            'name': 'ʥˍŻ',

            'error': {
                'identifier': 'ǳųҞѼӚ',
                'categories': [
                    'os',
                ],
                'messages': [
                    {
                            'catalog': 'ӻԕ',
                            'message': 'ɚ',
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
            'name': 'чâŀŹʋƽȴşcɝӘѻǀ˛kѫıҤɩăǴμҖßǾǉȉˣ{Ԇ',
            'version': [
                -2120324791988044265,
                -4070186487793405069,
                -1871945737628745936,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '³Ԏч',

            'version': [
                -8728492599949190367,
                -8575893674792835618,
                -3552560720797831304,
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
            'event_id': 'łĿρФƩԍФɴɥԄ8ͳÁAтԟģ˙˲MŏЂʙȁӕ˹Ӣȣ\x80ʣ',
            'target_id': 'şŮԎҪκ$ÆȰȔÑʯǠɥЁӪǲӻƙΜȕűκƃÆǻʤȆŔ\u0378Α',
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
                    'event_id': 'ĔѳѭԑϓѓĒлԞȥƮŊơϐǚW\x80ȆĺөĠ\x94ѺɹȕϾχʂϰ:',
                    'target_id': 'Į\x8e\\ϭÇһƼӛϩˏƟʲëŋ_Ѽ˴ǵ\x96Ë³҇ӿʛϏ~ҁöcӰ',
                },
                {
                    'event_id': 'ϚӁɃЄʈГɥφĮҹ҃˩Ќʌ˙ʟδ҉ŀέȎ\x82ҰÊƯƴ˕ʒ\x8fȲ',
                    'target_id': '\x9bʼŠú˅Ԁʐ#Ҋȳɀ҂ˤʐ-ϱ«јȨGŲʥ!¾ѧ\u0378ǦřǩC',
                },
                {
                    'event_id': '˯ǀ˪Ǽ˴ʜɞЍĶʟ½ȡŁíŵϥ%\xa0ӭ҃гҸ\\\\ˬϭџŦɺҾ',
                    'target_id': 'ԘɎϮ\x94EӨ˵GӊαͱƟȳӃʾDәµkɩѢiҎө¥ϗ҂ӈǱȨ',
                },
                {
                    'event_id': 'ԠψТɚƣĿɣˣгŘġϸ΅ʳɱĒǻJʘͳЉͷҏӂωІϺʠуª',
                    'target_id': 'ӛPԧҙʳβȹϯˆơ˻\x8fҕɓȈūԔˆӟӗԆȪҠҧʈɉľǊȜą',
                },
                {
                    'event_id': 'ϲ\x96ȤЙȷŊΗԋ\x8cYэҐɐǶ\x9eсϯμĢӊȕƥʿˆҩƦЮ\x99ԮƇ',
                    'target_id': 'ҤȜοˀ˨\x80ȳġ`ƦюНѤ˛ƻċɱÃԣԤԔ?ɟơϞƒ´ÛÑΔ',
                },
                {
                    'event_id': 'ʅĲωԇҎãЃåAeƥʿҖӻïϭҜΥɇʈІÎ\x8aЛKˤɅɺɠО',
                    'target_id': 'ϸǛîÌƅȬɤѬԋȒȩ°\x89еĉΏVԑФ\x90',
                },
                {
                    'event_id': 'QҜɯDūφʰ8\x84ȈɳПӾрʮǞҲʫȸ˄\x99ǛÆʼʵ\u0381ǎŅʦ²',
                    'target_id': 'ɓαΰһѭŌƐ£˂ÏʓѻӦȻæΫ=ȨʸǯǓ$ȞϫɄ\x9aȿďqΚ',
                },
                {
                    'event_id': '?ȮԣˊGQΦӻѳǋ϶αØƩĴϐ;ʐûͻɘo¶´Ҷƺф_ԉÆ',
                    'target_id': 'ΤĚδѫϦҷÈδȒĻËΦKȲʾdʦϨ˩Ə¢ʹҜϿѠȫԘǓʬā',
                },
                {
                    'event_id': 'ҋϸ˄ғŌ\x98ĬªϯѿɞȤ£ҦсԂÝĲϭǲΨǀӭ0\x8cҧ\x95ϫV˽',
                    'target_id': '1u҉ĮЉǩȟnƙΣҎđˏԚˈʱ¼Ɔʿ˫˱ǸцÓĔ;\u0381ьξԨ',
                },
                {
                    'event_id': '˞ĥ˛ɩĸіˑɽΧӔ҆˖ќɎӳѝƜȩʝӐΦÞґƕǲȨʁҊ\x8eƗ',
                    'target_id': 'ûЦӹχԥԮEÊŕəöԮϳŪǣԇ¥ƽѢɋͰʿŧȒΌˡŗÍFĈ',
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
                    'event_id': "τԓΛԪŔѯĹ+'Ą˽FѷέBѰҺзђ\u0381ȝӱ,ѩlZȐƂԔȴ",
                    'target_id': 'ӰíĖɂŝЫëǤϷɬ&ѡǯɲǄȨѐҍӰ»ǬԩţƫҜˁ¼упȞ',
                },
                {
                    'event_id': 'ЂɣŸрѫˡ9ˋҞφʣΛӻ-о˸ĳîҮȻŐǻ˟ΡɲƃǪŶΥþ',
                    'target_id': 'ʉ\x8bΘЁ˼ňbɑŌχԗɒȘԄϳ£ƌА/ġϛǌѱєȬ҈љFƥϴ',
                },
                {
                    'event_id': 'ˋΡ-ɾȵŤҰɄɒpӕѤ\x87ѹ\x98KΒȈ˥ƛ Ê˻ʧuγҠūѰԪ',
                    'target_id': 'ǰԋƳĝȐ϶&VŦĄɓƒϔо˅ə˭ǆȎːɽʽ΄ҊʳèŪĸĸɵ',
                },
                {
                    'event_id': 'iʛ|ɦ˺Ң\u03a2ˀѐŌǢѲгːkô2МЅǀŅɼΙΙά\\ϔѮ³¸',
                    'target_id': '|Ƙʬη{λÛšȜ¶ŶƦ\x91ҹhƓʐʁµɕɆɝ˦ƱίºǷԒ˳ɿ',
                },
                {
                    'event_id': '"ϫЙʎӃҝŵ\x82ѳĸǉǶƤĨĥW\u0379˧Ș{čδȧȉѳԋɉԄwŢ',
                    'target_id': '~Ŷ˒ѧoĮǵĝϬƷŚ',
                },
                {
                    'event_id': '0зŏϽ\x93\x8eʎԛ³ӽҭǕθ\x81Ӌŧɏϩř˴ȝΕʫƧȆƮøρƓȉ',
                    'target_id': 'ʠϏŐЛ]šӒχСѨȧʊĀсҙӨȿѤɴѱԈНκƋʲƭŪςˍǹ',
                },
                {
                    'event_id': 'ƤԨɞšтӀʼ¶҆ŌGԂħć˻ˤƣāƆB´ήrǙıÝƪũǭʞ',
                    'target_id': 'ʟγżΖφ\x8cŵ0Ȧ2Ì;Ҿŝˌťҷ£ňϦΎҮƅȼƤ×ŧίőѺ',
                },
                {
                    'event_id': '-ƓίŉΆƻϋɭԗҮʔţʱwōҀӶɅȬҽыϥӰƄ˲кǄѓȼ!',
                    'target_id': '|ƺɻϾΈƸӊ[IΚäԛů\x88˗ƆͰưρпɗʔƥύ;ԁϮưQə',
                },
                {
                    'event_id': 'ӄʟкŕӪțˀҭβčҥǼɒȫØ"ĩŃҭ§ιäʷχȏȧϟ҃˶ņ',
                    'target_id': 'ͰŶ˅ӇΉК"NӏɇɜIǙĠǄϟ\x7fĤɇɞˑρɠƂ¹ӿΤəώȀ',
                },
                {
                    'event_id': "IɈӀϦ½ґҮʑɩĺ;ҔńԌŀӪǈ©βʯǚҎҩ'Ľ˱Ūɏ",
                    'target_id': 'ӒŇϣШҸȶәƲWҞ=Ţ¦ʘͱӲƜȉƱˇÉӬѬ»˵ǔ-ļȫӨ',
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
            'name': 'ÙϨTĢώƙſԋlϭԎ\x9cˑůχǱ҇ÙõԄƾĩ<ĎɈ³РΡʘʇ',
            'version': [
                -4707503660618219362,
                -2707099761184925579,
                -1777359251370626183,
            ],
            'about': 'ϺіФӞмɆίɶäϓҕήҷ\x99·ʦӞ4ɡʾƼҾʄĐŃƩÉƺǺW',
            'description': 'µѓ%ŅʀҠӶњǕъǒӴ ƌƂǀѧƓǗɟ[ʠϰϱƼӜʙĵЂƜ',
            'authors': [
                '\x99ВÝ-ķĚЁhȡ\xadȐɎÕЭC£ʸϳϷҏʛēӓʄԡˮͲ»Ȃą',
                'ζiʰʩόϿ,ҷŵ\x87\x80ӪʨЏʲȨϝɼȚʓőǿǵɩӸϻƍθÊg',
                '҃ɤȊðǴъƚɬѱ˵ȀѿǤ?ˑɱèȃ˥χВΤ˙ќΣđϢφǶƕ',
                'uȃθƛʀŢƉЉμȐӔΈԙō΄ѿÿͳˣ¨ɲͰ£ʏϟɭčþʀÙ',
                'ǙȑҋҗΠǔņ\x89ß£ƚԫ',
                'ˊʭȏʧӷĜȶȃ\x9aŚŪҨʁ\x85¬ʕϝʿʅÙԇʐ©ǓϦȨħʪÝ>',
                'Ҕɞцʌǥύʀ+\x9cѫПҚӸβǠɭĤĹҭҨţбҽÚũ@Ҭ\x95\x8aԣ',
                'ŴЀʊρӰɎәЃфƗСҍʻġ\x8bƊȥFƓƘ\x8f%UłʆȾƲōѪƚ',
                'ѮäтԆŝz©ěәøǐ>ѱԧ˩ȠIҒoɒˆļҸþǿoҐöΒɤ',
                'îǘ@ӝƍǉɿ˧ѺηǯǓíңåǓȏǱтԤӻҾԄͽτFòƦ¢ц',
            ],
            'licenses': [
                'ʟɍШ\u0382ІƹɏԕɋҝɟψғÁԄƩǻΒʆȈтӴ?πШοσɌҟ϶',
                'џȦ˫ƤƶȦδ]¦ҡАєʊȈԅęԠєƻЭΑɼɎϣø<ԩ±ʪʏ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ĺɫ΄',

            'version': [
                -7675852121492730259,
                -1114044208373229451,
                -5982131371294485728,
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
                    'name': 'Ǝќӝντǯëʨǋ˵ȌʮöȶˊӭµчҷɗΖɾªέÇʼӤιԞҪ',
                    'version': [
                            -827208914325165410,
                            -475027270154338163,
                            -962100540347580042,
                        ],
                    'about': 'ԅǵϓίʺŁm«ĖкìȧԖҠҖǢt:ԗ9(¢®˒ėȥģғƎ\x8c',
                    'description': 'ɫƟƖβøϩѽѕЛĚҪʥж?Ɏ˞iɱęΜǚϝԃУβϣ\x93WΆω',
                    'authors': [
                            'ʝőȑҠǋƝҥӼԝ҆˴ϦĵĿőȃh\x8c2ğВʞЈԜӲϕЗʏбɋ',
                            'Ø\x87ԦԤğӓɦʾȋѾɺēЕżʨ˰ǹn҉ǀ˓ɇӛȣĂſ¾Ϝφº',
                            'ϘύȻӴІj΄ɚ\x89ͷԆЮѯΒҩ´ӪǗ˽űǘѳřӤΙсYUѦѧ',
                            '˃ӏŰʽϵʡş',
                            'ώ_õ\x8f¦ѹӈÈҥ˹\u03a2ӆǣɖҝęʱѐĝƅŷƮϩȝӪǡƛТʍ ',
                            '˾˰ЎӤϓ¶ſˁϔôхɪəкȀԐЗƭϰÏŀϢƪËŵÐę˅ҥ=',
                            'ĀːДƧħ\u038dÛΣŰȻ',
                            '"ˑ¥ʽȰʨyɍĠȄǹϷBЩĩΎςԞɫĥљ\x8cÑɡϰˋŜSí%',
                            'ƨɑҀ^Ɇ/Êԙ˒ȋǦʔäƵŵԟƺȊÐʈԍRŭŎҼ^ӷɷ3»',
                            '҆˨ƮӑȐ',
                        ],
                    'licenses': [
                            'ήϵѮ˄ОˎºȉɞҘǝ˓ëȳɦΑ¼ƚ˗ØǽČԊυӱZŅäҮ˛',
                            'ūɦΡÇΤџʻRςԛəБʜʊ˭ΞԖɑ\x94\x8dζ8ҊȶӐ\\Ũ£ǿĂ',
                            'ȲǝԍВĚľқH)Ƈ#ʭMƎȗƦѸɰҟʘЀʆ©āÜáěƸΩǃ',
                            'μѬ\x9eźӕ\x94ņԚƻ҈ĳԍÆxʧϮǙɶŹ҅4эϖɃ³ΚʌҴɍǼ',
                            'ҸŨɱʮŮϢɘӘʶөÞӶΠAѣԡñúʅ',
                            'Ī˂қԂŐƶӋǨƵÔҔϗΓԣϵυʹhԥɓƅķҹàԉDЌ\x9aāĖ',
                        ],
                },
                {
                    'name': 'ԂʣʙÍǖˋīʶѯĂҚΤΒDǅ\x9cıӋӢǕţˍԀʞЏҬ¹ˇĥÂ',
                    'version': [
                            -2192956322693157759,
                            -2190062033843403216,
                            -6687148071449045530,
                        ],
                    'about': '¶˻˭ЅФҒɇ¤йʲŦэųȱЛʢѐĻöϯȕРǝÌӕѝˏѻɌШ',
                    'description': 'ˡÂĿǧұǷΙѭĨӆģ;ϭǂиɪAÖϒƷƐƎш(ĨīMFϙ΅',
                    'authors': [
                            '¶ФѸӿ',
                            '0ʤƒŝĢǛǍҖKЬSıэ~øѾԛƨǴϱʡǾɟƅȷ˸ȶӫˉʸ',
                            'Čʠơ-TІřɎǙPԆҮǷΒ¡ǃʉ\u0381ΆɚǺ˴g˺o]ÅŅӹԗ',
                            '\x99ŇФΧԒϫğӁљɎˉ¸ˆ9ŭͰëΙωƎӗϦø§ȣȂƻ',
                            'ʾʢΡśƯǯǌԖɺԀÁĦɄѓ˩ǭï,ϗҎ˱°ӆ@ÕĠ\x8aƧʭΎ',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': 'ÅȺѶɹӭȬэCЭŧ\xadϪзʽ,ѮȅÎþў«¼ԫȵҿ¸ΔŞ\x94\x9d',
                    'version': [
                            -4329475269371221112,
                            -5659500221106186105,
                            -1459828348216117254,
                        ],
                    'about': "ʲ˸ƛʲэˊɁ\x85ƿʌąԟɞ½Ɓ'ъǼȄùйиβAC£Ǭԏìğ",
                    'description': 'ҾȈиϵҰʚҳɊêšȥΕj\x8cƋӍιʝӅʪɫҁ˅ξĞôǜΎÒ˾',
                    'authors': [
                            'ǠψǳνΝ}ÐҲôÆĐʃҖŧɵΖɩλɝϡΙóМШ\x87ӂԨȧνK',
                            'Ŕ˄Һѯҝ˜\u0381ҘҳϹˇmɥ\xa0ΉИҊ¬˞ȉ˦āϽөσАǛ½ӄμ',
                            'ѼƬšӆȉʺҮώĭ˚ƇԦƼҔίȿʴԉɱβЩƎġѵÑ_ȸǴΞʗ',
                            'ʕƼΜȧǭӽùȍӀǏƞȄȧ\u0381\x89˝Ԩ"\x8fСΞ\x85ȋǪ\u0383ɓąŏ¤s',
                            'ɆƥΣƗÙƀCĥюß"Еε\x82ƣҗɿβӅζǧŬқ÷ˌ϶ăľÂƗ',
                            'ϼÅӸηӂШШʕǂȻɝȈѼӗхSɳŊǇôǊɃÄȓǱϐ˪Oƭě',
                            'ΰɩ˘mŇ˯˄ɟƬˋĠξђУ˖\x85ĵŗƠĭʰнɡǽ×ӂ\x95˟ЈI',
                            'ʲæɑπſ\u0378ȏŘăȇԁͲ˲ΙąóƿɦŕѲӛ˴Ǳͳ˥Ʋ\x82ưƆh',
                            'ŷ\x83äͿуʩ˄ØЀԮƻ˒ͼƢŌϨ˺P{ŪҾƪǳŘ҃ҏɥ·Ϻμ',
                            'ġƏҀѱːžÅµ®ŧԙŖ\u0378$ӫȩ¨тȟłɥѧŀ.ϡ9ʣӍƔͷ',
                        ],
                    'licenses': [
                            '˱ϙʢ҆ǝСȕѝƠɡφƜwßƑԨĺÊҘƭʺдЦʓҳPrϺɃӭ',
                            '|ȮƠҴТȵʭŅüʒοз˨ÞˠğҏɸδєƂŸ҃ҟӋʪˁƣԣ˱',
                            'ǦԐϝϹҬϸϑƩӂҊˋť˴ӻ¹҇ΎηǶÞˢĮ˃ПŊĠΦ',
                            'ΐӁȴ²БѺÊÉȸӀжYƿǄ¡ýѠÎо^Ѭϧʔǣƀ;ӊΛƗº',
                            'υǔɮİȺĕњљԌǍˬѤϴÞǉ',
                            'ХǨЫʻ_˨җĐ˼Ѕ\x7f˱ÖϘÂґЧåƁԎƧͿˋ\x87ԎŞ\xadЮ\x9dƪ',
                        ],
                },
                {
                    'name': 'ȦʆɅν»Xѥƶį˹њɅ%ҌȥʟьΓԕ<ǌĘ˗ԓ«Ҷ²ȳóΉ',
                    'version': [
                            -8031102739524770363,
                            -7744266134043408687,
                            -7786961122870231889,
                        ],
                    'about': 'ғZȂȁ˅\u0383ȰюυɝЮϐϞϜ~ȽłœȜìɋ\x91ȒÑӋΝÉċ˧\u0381',
                    'description': 'ԉӢΜ\u038d_Ɲ?ƽȧƇġФћȀԚ1ˤɬ\u0380˰ϴʒɆ±˘\x88ΌΚKǆ',
                    'authors': [
                            'êп8ҕǥɦʋőάχĚϠɃʃƟ¬Ǒəσѕʛɷŀҧѷ=ˍ˴Εʩ',
                            'һŨГıƄМєϖʇƂɖЪțНÿƼԜъȘȸɈɵηÍ\x88ңYфʤϷ',
                            'ÙƹƣVʻГȫŪŗĔ+ѐ\x94ΆɃäSӟˍƜNҦԉӇɾΙȒ-ӀY',
                            'ЄEмз\x7f͵ӐŘӕԞĚҟη\x92ҁťʸϢʻʆǐϥѩÃǅҩʉǍξҮ',
                            'HҀŔƇƨ\x89ԓǘǼŽŋǖˮǒȜЁԇŉÌɇȎŀѰΠÙǓԉɗH¼',
                            'ҥğĄόюиÀЃʕǒÕӉ\u0382ѼȲϰҌšЅΚʂŃ\x9bˍɑȿˠўʒк',
                            'ſѕêν1ʨȦӻâćʐɈӺ˙Тǝҙ\u0382ʄȎJзΈӖҹ\x9d҉ҖĜ˺',
                            'ȋǇɼӊ\x81Ίx˶҄ǻƳbȳ˺\x85ʩ<¬ɎƝ\x88Ӝ',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': 'Ŏǒӫyʒ˒ͻŅƐӛüșÅȻϪԛѣȒǇŉ¸ȁz҄ëяǌѺñϷ',
                    'version': [
                            -8461673615061583798,
                            -4133073974742807877,
                            -702275499654677355,
                        ],
                    'about': 'ϑºȷİǊJəľÏ4ιĵӦԎŇ˵ϿПÑƫҦɈ\xadɝ1łУυԖҗ',
                    'description': 'ήī\x8eҁҹμχӇӎς×ƆƤ\x8aĄґƧ΄ӬɷӸȇÐҐȶўƕʽπó',
                    'authors': [
                            'цʑǈњ2Ҳ6ÂԁǋƎɽҴӇǑӠǊԊҁʭɐĸŉӸɀ҆ƭˇΊ¨',
                            'ρɐˋÏ2ӿɭò\u0380ŷӗɸʧĄʝƏԨʗӦĢÉǮËӸϘϜɿ*ϳ˄',
                            'ҰԂGϚ\xadó\x8dƄĐ˳ɇÜΰ³ťPӞ\u0379ѧǚΎԈЋ˕ыͼϪƘιɕ',
                            'ĜȩưͱˍӮ˱ҡÑӴ"ʬ²ҩɾȭ҉ʜѳйĕϨȊЗӍӡ{ƔĦП',
                            'ϓň˄ΫɛvϵӶнˁËίҤёĵҟώȌ.ÚˆфιФȴ=\u0379˞˩ѱ',
                            'Ȩ}\x8bԐҬ¤ʋĚƐҞʃ_ʘҲūBɗʜģɷûʎʊŒϠǒćήԀĩ',
                            'ΤĩŽÛЊŒӇҌêӜάǆʝ¯ҤϲҤȨÇǜɄɀƱǕÒŮ9Ԃʋǔ',
                            'ɓğ˔ʶ^ȅȀȼʢɰςһЮДЫу˗ŧĺӄTɿҊΎӓʆʱƕů]',
                            'ÄϲVЕāӷǪʒyƙȎǋŲɣ҈σʟјϔƱҤȲĮĠϺɮʩɄңͲ',
                            'Ǫ|ʬ˴ɄǭŕƙΚγǹѻ|ɲҠƛg҅ΦĶ0ñɉĪҬǀ+\x8bʩŦ',
                        ],
                    'licenses': [
                            'Ȼ¼ÇԈċˬƲӽȾ҃ЯĞŽġʫϊ\u0383ß\x961ėԬˠƊ:\x9aÞǗԐШ',
                            'ӛİȝïƟϤμȨŗţɎûѳʝġżϬǇь6ͷŋĄ˯ȫfьdʝӧ',
                            'ΐ\x98Ƕɍʏ҉ɜɧɔȳԔιȂ1ȑǴ\u0379ÖƃfİϪP¦rҚϟǚГƓ',
                        ],
                },
                {
                    'name': '҇\x8fԓ˵ǧҶʑȥӔɸ',
                    'version': [
                            -8325497242255012483,
                            -3369225929675567429,
                            -54918393748969841,
                        ],
                    'about': 'ϣο\x9dĺƓѽ¾Іύ+ȡĠˌҐӰͻĄǊšǔрЃ\x84ά@ʓ>ɔӸë',
                    'description': 'ϖʻΰϨǃO҈ƒƗҁӕǂɦȩĐˀù±RƏÃΥʳ\x9aɭɇɼΩʿĸ',
                    'authors': [
                            'б˾;ͽȓрԅԙӲG\x98ˌџϟØ˗ǅÿµ!қғɅʧѰɸīȸԊϱ',
                            '\x99иĆϠ<ǅʸǗӵѐȇƐӍԘɊƿ҂ĘҸқҖΧ.ɧůЮÙÆʜɡ',
                            'ʲȼĐMoϷǿŭň$¸Þƹ ѵ§cѾǧѷưБƬ˭ʻŇa\x9fĦο',
                            'ϕ˺К˳vѷԎđғɏȉWѪԡǚȀvŎλ\u0379ҠҒʰѾͰHϫ\x93ĺѓ',
                            'Î˱ȂʳɎοʽǴʧЇŶ\u0378ҞÚ±ʫ˂ŽИɸΝõѷXȟʹΐҝˇ˂',
                            'ъԗя ԄϢɁԗəҳǕƻЩӌæт¿?ʼhϞ҇Čɐø¹ʶķαĉ',
                            'ӿǕƊǁцҧp˸Ǖŧæ¥c\u038bʐŗŶiǪϝʤԖĀϘɹұ҂$Ϣˊ',
                            'ϪÞЇ˻ѸɊŸÙʫϲ]ӢԏǧB\x8b&цƽмӧΤԃûӖϷЅԓÁ\x93',
                            "Ίɥǿǋʫ'ԌϝӈԊԁϧtʛȩΈEКύȰʰљϪƞσҽûvŉǆ",
                            '\x94˱͵ύΧϚΑԐƚʧDМ˶ӼÐƄԢςƓɷ˻Ӽӆ˟ҟΛɞӒʠϊ',
                        ],
                    'licenses': [
                            'Ȓ\x9eģǘɯŭfƢɝȱǞĊǝÞӄǌŹҾӯŹɥӼĪҬӜҍtªǮƒ',
                            'ʟ˖(ЯϾȳğ\x91ɂэϯ˧ϽňϡƶӍˊýɌӆˉʂѯυωɿ\x7fЙȎ',
                            'ѣLʹăѪȾχɜѠvАϡϟ\u038bсĜƒ!ϩ\x8bʄÃÙƘȝ\x8aəĸҨϥ',
                            'ƆʋūѩȗέКҙcѫ;шҭрӟȸыƎ\u0380ΗhþӯЙҭɑǅζ˳ˆ',
                        ],
                },
                {
                    'name': 'ȅĄԅ˯6ϽѦœǙƔҊǾ«҉˧ȯǧβʉʏЮǅțӃΨȲȚԄŘ˸',
                    'version': [
                            -4723755123425372981,
                            -3232996814467499619,
                            -3564937091545967427,
                        ],
                    'about': 'ΈťšÈǲɚБĊ%öϔŁǆ»\x91ř»\x86˩\x7fӲϤҮΛƄö\x93ǏƋɘ',
                    'description': 'ȻȤ ӡŨ҈ӸɤʞѶĐӟʀʹ˷ǆΩˆҰ\x95ӜǬϘЭʾә˲ѲɨĮ',
                    'authors': [
                            'ʈԖϭϜ¹Ě˞ȀȊʛŁΗпϰȊҸƄŋζи4пúő\x9dΧҼҢɟʟ',
                            'ǹȆrрǙϘϐ˷ŬaÚ˲ǣ҂ŎҺȍѩҝ4®ҞǔĨʅƌÂŲЯʿ',
                            'ǘʠĪǴʕÈʡÜȥƪ˓ŬĦʮѲÃȖ!˩ϓ\x9e£GHɒӾ\x9dǑˍЧ',
                        ],
                    'licenses': [
                            'fɉȤéΎĸ҅ӂŲɛˏҒɼɳ\x9cʪǫǠѕǨÂŜΠˉƬȱλ˽ǔ\x83',
                            'ƎҺñӑƧ·ØþɈƜԃȰ±`zƖɪӚҰîϒȵkȇрĈѩзҙȿ',
                            'ш\u03a2ȬŚ¾ӔſîñÐ©ˍӹҳĴʹ˩˫Ͽç˙һǆΊ_ĔƶʂbУ',
                        ],
                },
                {
                    'name': 'Ӂ¨¿șŁıǡЧːѵѠԭ\x9b\u0381ԑəѯ{τʂԄƵџΨτƮˈ±Ȱs',
                    'version': [
                            -5890920289128956568,
                            -5874660329602451426,
                            -3743687725644514995,
                        ],
                    'about': 'ҧāиʍŊ˄øѡъCҋŰʲśơщаӥ\x95ϲ\xa0цƞɇʃȭυˎΒɅ',
                    'description': 'ӑÊ{¡âӤ\\ːʃǁҁЀłʱEŠɡƤhЏɝԧҝǶĮƸӜɛνʠ',
                    'authors': [
                            'ϚɬĒѰѣӌҿ˲КŭůЙѣɘԖ}àκǭŦƸͼӽoȌƳȒæ°ˀ',
                            'ȌӹƾʲȍЭzӣЙȡнAXЅȉїʎŚѻѺЄБ§ϷǚӚʩǏ×œ',
                            'УvƘ°ËЋϙ;ϊÙǽ˱υӒϹÂĞƃӹÖɳѕĄɞʹдJјóō',
                            '{ƴɌ\u038bȀЙңϛǘЎͱĺӕÈϯЧlɣʅȊǘҙTƗПѠИϱȟъ',
                            'ԘȊԪҹ˞ƳǒΥȬРѻĝϕϋȀǦˤҞÎƹԋГӀſľҌΥӴв\u0382',
                            'Ƀ×ûžĨĿÌέɰ˺wȸǌӻԧǪǺɷʋfʖŉǑΓƝŮŜɆųț',
                            'BŚýœɥũïȱGʑÏо<ŨƺхԮɪϱáúȑͶňϒνΚŦƫӏ',
                            'ÅʟƞδЋТʚ˔vvŹǭˍķ?ɷҐȾӫӎсίʧˠɕʃɧІэƛ',
                            'ѨѧɎ\u0382ΕfӉsͻГΝźμŏРБӌǵʪΛԜśſ˼Σșђȋ˭ȟ',
                            'îʫԃƤ$\u03a2¦ӎҗŽαǠҵ\x97ǶΘɻѿҕ˘ѕӱϫyӥ¶ʛ^гƍ',
                        ],
                    'licenses': [
                            'șϰήљıбЌфɻ"ő£(ȼȼˡ$Àħҹ¡ĝĭԙȶԁҮʅʺӠ',
                            'TŦˇвŊ½$ϖʂ\x95ӡЏȞȾŝӱǴą{҂Ɉ$MЅɇ\u0383ȭĴȍÑ',
                        ],
                },
                {
                    'name': '҃ɘĜҌMҷҖŉǥÌÍ6ǇΆ˶ӯĳƩdӹˌŽӹɛʮӔԢξЦM',
                    'version': [
                            -3655913712340151764,
                            -5257161853131801856,
                            -6417623756348026705,
                        ],
                    'about': 'ĄԢʫ˜ШȲӹȷɺƭѵƶҙϛȳѶǷΖӿżЇҗƛπˇѵŊȉåɤ',
                    'description': 'Ӝð\u0382ӖRҹ҈Ҫ¶їǪԍж\u038dǈʰϺɔѶҖщ\x83ǙȻɇȉğͻΈԈ',
                    'authors': [
                            'ѴŴԥǧƭѥʄϖɗ%ǂДØîÓʪԚ§ӍíчԮиʉˡϕЪӔČϐ',
                            '˳ԉ',
                            'ŐȐӫφ-ɃοӭЄ¦»ҧAÓɨÈʗź҆ƍҏȘģщӄĴПђΐЕ',
                            'δԉӰ·\x9bʻкLѱȔŬϦϜ\u0378˘ΤűIĒëїЂȲӃ˾]ЗƟԀď',
                            'σәú4\u03a2ƷǄɽƴьӹΟʏùʍŐmЄˀxбӥǛʺ˝)Ш',
                            'ɸљ\u038bПвԐZȚƱҗŏ\x9aſ˓ʒþѡoɃǎ˝ßʐɳΔ9ȿŮʕǯ',
                            "¹-ԬĕòҿʁĆԣπĦ?ƹӪü'Ǫ@CӰԪęƅrиǺѲЉԍȬ",
                            'ƵȑǅάΩŅΚƆȫħιŵŦıǮӳðЧɚƐˤӵN',
                            'ˀŒé˰uÇԎĻʐʢȴ£įрŵуȀŹеИ¸ÛɡѺҒӧʐΨяŌ',
                            'ýԔʜϣЮʷƷѝŮԊӺǦЮϋĬҾĶʆΛīԋˉƍȸϴ:Γ\u0383ǨѶ',
                        ],
                    'licenses': [
                            '҈#ǈ϶ʂŖεʞԃJʅ\x97ǝĤϟѪϲƉʖĉϔˇù,Ӈ8ǱŞԏ\x8f',
                            'ҳǖ϶˵Юŭʻ҉϶ȚѣƩҧ\x97ԇŧҧ\x91ΘɊ>н',
                            'ѯʻȓ¾ҎʠТKŒŏ\u0380ԏ˳£\x9bOÊɣ˼\x98ҏ͵ϩƽЕ¯Ą˪ζ³',
                        ],
                },
                {
                    'name': '%ŧŻԃҡȺÍgŷЯāԑҠ˄hK',
                    'version': [
                            -4522118647003056967,
                            -6441229563596064511,
                            -4395419971728221261,
                        ],
                    'about': 'ŤŕǈǔȉʡҦ˸ɭ\xa0',
                    'description': 'ї\x90ѵėϡǬυȏ\x82ʿѡɄɹΚѿƻLʏǏĈ˟ӶĀйʹ҂ҰǤяԀ',
                    'authors': [
                            'Ȟơʏĸ\x8bˀǋʢǍͳӫҟƾǚ˷\x8eǪȟӨѸʃΫ\x8bBњþáǙӳī',
                            'ҭƒãѨóюκģ\x99еJɽʝ_ҘNΒ%ɻƪϕĮʦҺļӡɗʵʒƸ',
                            'ѳÿ',
                            'ʶӪɺǾȀɆˣˋǦĄÙʚԌƋϷǓɺΏʄӑǶǬÆȊ¥ȊӮĒЋǌ',
                            'ȼƽӱʺІȨɴ÷rŎĪ\x90ԛþΫʹӲȌɅ§ҋӗʟɛǳдѶ«ҏë',
                            'évҍĎȥJýy¼\x8fГƢͰΩϞƨƢ®čӄʞȀͻÁĔʎóëčê',
                            'Ǎà˔ҖсҞÀ#\x89ӥԛҔªŔ\x86ȴʱȰũʧ+ԔlӄŔһȼǦûǈ',
                            'ԏΟɗ»ȫџʯʔѯϼȧǇДԃȡԁMдӽѤ"ϢHΞ˷ˮҞ>ɱc',
                            'Ӑ½ԤˣήS¤ÝɌʤřϢ\u03a2ЦӣҥюӞџěӻΟӴŃ\x7fɟ*}Ӆë',
                            'ʍźԁӣӿȾˌǡŪӷūʿ\x95ʹǭīԜű\\ʕÞΩȏ˶зĜәΌ,Ɓ',
                        ],
                    'licenses': [
                            '\x9fԠɉӧϩЊĠŜ˕Ƒԫfԭ\xadrтъƱɶѻӸŁůΛљ>йЩυѭ',
                            'ùwҩϙÛƯѾӠːåʣˑ˫ѱѻүӉӻȏȄýӓҝрÇžɬ˻Æ ',
                            'сЇҦ',
                            'ҝĈδϥķ+ƽ!¾ӿÅѣƚӬÞˋѾɵġӀȬŌȃĐӅЎя¨ϭĞ',
                            'ʐƃϷ˗ƸǴyƿʖ#҂ҙƁԥõсͼʥ\u0381άɁӉѭӘŇӟųÇĪҧ',
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
                    'name': 'ĉżƵ',
                    'version': [
                            -8282866622222473066,
                            -4413778793706814406,
                            -5535982580115322877,
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
