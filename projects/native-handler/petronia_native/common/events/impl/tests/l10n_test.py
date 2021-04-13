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
            'locale_code': 'ɍĘ\xadԠ͵ŢΔ',
            'catalog_name': 'ΤQŇŰȝʪѺʃ?ũNȋûǹ²',
            'message_file': 'ϏҖʯЭ¼Ϧ[ҨYұƌ˯˓ͽøϥχϡˈԓ|іĀ˦ѨƘԮ\x8bӚʆ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ď',

            'catalog_name': 'Q˗Ǥ',

            'message_file': 'ƙǅ',

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
            '$': 'Ǖ˜˶ϧʀAÊϴŞЏk2ĀʊΑІǆҨά˴ǷƾΥͷʟƣƘДŗǑ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -6463815642387011611,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 97194.83429265645,
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
            '$': '20210413:001705.282184:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                '\x9dδҡΫϤҏяǱф5ϵEċjEΏʁËJÿï\x9eíҐŕ¾ʞȸyɕ',
                ']ϾĒ\xa0Үä×ΚˤϬ<ǱӞӈķAԩIЂƋӨɘѩ²ӃóђьӞ%',
                'ɚȰ˛Ӟž͵ūǜƸΐщП˛ȨĻƄŃӃЖŽԍŰćɓFǱśйƟŧ',
                'ԑӪГ˭҉Ҏ\\ΪӣϱϋϠасˬkƹѳƏʖínƝ0æϢʌԡӘҝ',
                '˼ąŻ˾\x88ÞqʥԃìОʘϒϺҦсӰpΰҍɾɽԞʖНÆȲϏǴƹ',
                'ŎҫѐΫНCԃʃγʛſԤęĥ\x8b¿ƣŔļΆʯѮЈϛШǄӓĻĹĄ',
                'ʫȢӣ/ƄʾЬ҆ПeӺɔӅǔ˖юƃѓԁРҋѧNʱĦэČЭXӛ',
                'Ũ˺һIϱԜҫЄȃèɟЂҒҸ$˳ƘљâϬČϢǜΧ˫ʓąƕȃΏ',
                'ϱГPͺўΆƽæ×QӮű½ɖѯǎΛƐĖϏǺ\x8fEˢèƨȌԊÎǳ',
                'ęɭόćɏ\\ĉǿϪԠͷp9ǏɖӠԐŽȶлÄӅ\x83ԡ\x91\x8bŐήЀĀ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                2930248412204821626,
                -1000350502622383235,
                8415201630455184343,
                5429495175573141321,
                -5112923601130559778,
                34300038848353383,
                -1105473498259569915,
                2235450522818873315,
                -5499060257688664266,
                -8125651872004019380,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                503221.21310650615,
                378043.64804844937,
                174672.45494400914,
                221138.75788176252,
                652382.1706850283,
                882478.145097431,
                672844.5579303358,
                597577.0348746524,
                575790.2335690156,
                965807.5000927413,
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
                False,
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
                '20210413:001706.309445:+0000',
                '20210413:001706.327641:+0000',
                '20210413:001706.347168:+0000',
                '20210413:001706.365138:+0000',
                '20210413:001706.382524:+0000',
                '20210413:001706.401372:+0000',
                '20210413:001706.418349:+0000',
                '20210413:001706.436350:+0000',
                '20210413:001706.452376:+0000',
                '20210413:001706.469505:+0000',
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
            'name': 'ӮʃԚúOơԒȋʦpÈƻͷ¤Әŀăϯ˷ϛ',
            'value': {
                '^': 'float_list',
                '$': [
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ҕ',

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
            'catalog': 'ӭáțċӫƉӟ\u0381ǂԃɒӋҼqҽÀΨ³\x7fƸа¬Ñ×Н6ɛŠюҒ',
            'message': 'ҬŢӟыƵß]ľÓǏŢ¼åωӡûȑ͵ǣӉіɴßӊǁŕ°Ѿɚā',
            'arguments': [
                {
                    'name': 'ɊŻнξ§ğɏłĘ ƠʂʘŖɅƌ˅ВȬ´ƆɐwӛԒTӜÈӼȕ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ҮҶ˓ϿÜãԇØΰHˑΨʴѵʆʊ\u038bҍʼʱÅτҶȦ¬ҋČˁêǋ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210413:001703.692944:+0000',
                        },
                },
                {
                    'name': "˖ʁ˷'\u038dƱƲίǩΓҊӋşm҉ϋ",
                    'value': {
                            '^': 'int',
                            '$': 5610978112968856753,
                        },
                },
                {
                    'name': '\x86Ɵ\x97ѳŰЍĽ¤ьŋьƢÚхѫț4ԝöϢǶ9ƺwʺәĹĜ9Ə',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        1933023848061052906,
                                        -5741567521678870904,
                                        -9086715367579371057,
                                        -4488874193701558195,
                                        2620096472759437446,
                                        -7383510636439177125,
                                        4311199332037832286,
                                        -5222662601388311824,
                                        5749610795507009104,
                                        -642874208121035330,
                                    ],
                        },
                },
                {
                    'name': 'ѤIα˸ȕʰēɶ3Ѳ¬˞πƺƈƀѧ˦βȁ~ŉ΅ƋƑȖĨʅ2ө',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
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
                    'name': 'лӔΟΪɊĈ',
                    'value': {
                            '^': 'float',
                            '$': 40831.7939842871,
                        },
                },
                {
                    'name': 'êÀɫ',
                    'value': {
                            '^': 'float',
                            '$': -14944.19450292323,
                        },
                },
                {
                    'name': 'ɭdѲúɷãŬΔÞƬ¬uɹʮǰơͷѯǢҾҧƘʣɹ˘ӛà',
                    'value': {
                            '^': 'float',
                            '$': -26201.207579973765,
                        },
                },
                {
                    'name': 'ƳϏ˴É',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        83532.4376997732,
                                        387904.4977635942,
                                        187877.1734170292,
                                        324471.63259560603,
                                        208452.94879773777,
                                        670972.0482278435,
                                        105607.21857907044,
                                        996750.5989829232,
                                        601050.2570524726,
                                        564055.4205320594,
                                    ],
                        },
                },
                {
                    'name': 'ƻ2Ѝ҄ǃń΅ʇǐƼƾ:šİЭƗӻϑ\x8dϠ˯ԁʊӔ˶ʄɖˡΎc',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        4786647480230458493,
                                        -2388945429243841723,
                                        -1328976311377590196,
                                        5021400627303492441,
                                        -3791690158279135850,
                                        -1777321475856274238,
                                        -6571649299657239806,
                                        -444307311239717662,
                                        -8833843556247805895,
                                        -8995414665171245420,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ğΥ',

            'message': '˄',

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
            'identifier': 'ͱΣͰҢ\x8bɮÑӺЀǔңɩ˻kŸÅӪҜȹ\xa0åKǩȘʺtЍұѠȊ',
            'categories': [
                'internal',
                'invalid-user-action',
                'invalid-user-action',
                'access-restriction',
                'configuration',
                'network',
                'network',
                'internal',
                'network',
                'file',
            ],
            'source': 'ԚĮ҆ήͺĤϕ˹\u0382ɚЯƚƄӽĕγ2½ʐŰĘҫǱ΄ɺİϠΏѹ¼',
            'corrective_action': {
                'catalog': 'ӁÎҫĬƎ ҕԀȢҍĿĥɦƮƮĚ˒ĄґɪѕНǓЋ¼˹ĸγȪл',
                'message': '\x87ӭӞĶ˭Ĉç˪ѐʂƢðéΫϨʪɰƐϭŹǞ+ΈϜλĐƚ¬ΑЪ',
                'arguments': [
                    {
                            'name': 'ӑrŏƦʮVǁϓԑƖŨ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210413:001702.737854:+0000',
                                    },
                        },
                    {
                            'name': '\x9c,˒ȾίĿϼǇ͵]í\x89%ƃϻρÞŨӷǧӫϞ\x98Ԥ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210413:001702.865247:+0000',
                                    },
                        },
                    {
                            'name': '%ʼƤѪʦęјVȀˮǜǓҺϚҤʆŶ]ʋӣϗ#ĴҧоƐàȂҌç',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ͻȢĩŅВăǞɷOѳӦqǀʒȧȵћѯҌӬ¹ӁȩǴǱÀȭ҄ɧ5',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        972499.3950646494,
                                                        99952.51463106187,
                                                        555788.9005489012,
                                                        579745.9788937648,
                                                        711566.0410522225,
                                                        628263.2502284591,
                                                        266396.73260181904,
                                                        7691.468909420888,
                                                        888595.773413039,
                                                        -91943.80538028316,
                                                    ],
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': '\u03a2"¾ăӣɂŰȹÅʉҏØǩ¸хԖȧ¡ƘČʞζўҎО³ĚƎђԦ',
                'message': 'Ă˶ɑǦȰʔѱȭwʹȐȃ˞ҲƥϚƼѫì£ˬƥӣөт˟Ϭċn˼',
                'arguments': [
                    {
                            'name': '\x8cưɅ4ԇʮ˴в»ГӶƪТːЄƘĤƠO',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210413:001706.730091:+0000',
                                    },
                        },
                    {
                            'name': 'ɺ϶ʉАԛʕ\x8eͺɉɦƸѴǔüΥƀѧ҂В˅ҾŢΣ¾˱ӯ\xa0Сӣʸ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'йθӒˈʧ¸ơѾøʞ˜v`\u038dЀƮψӔɖ˙ΤçȨȳÿɹfÊԦk',
                                                        '\u0381Ǣʸ?ӥƝԩčNĲ+ʮŠΖƹʐʛȠʥϒƞҜыЋxƪόŻɹȷ',
                                                        'κʖӒҽ˯kӘЧÊӔżǴԥϻǟίӚŘłўƦVǪҞʟ÷µ×$ԍ',
                                                        'ĽқĞrʟνҋϠлªɵԌĘӽĄˡмɒáӟʍѪ4õɎїƴι^ɘ',
                                                        'ĐҶĦiĐěϟ§ω\x9cʞҁœѕ£ãƙіӰŅ˽ÕŇ\u0378ȄjȺk\x81ԑ',
                                                        'ąѤӈϒĂϽĀȞœíŁζȭʢǖ\u03a2˸ЊъҏИˀǁɞȲğśРɵѹ',
                                                        "Ψ˷ϣˏҿАуͲƞӇǖǦƬҶξŸ˶ʀʣʡ'ʹԖҌϖŉұϮԏǘ",
                                                        'qďȴԀƱµºѕΝʬȠѐąºà\u0379сȊŕӴn҈?ҠȊȖϾ\x99əɳ',
                                                        "ɄԦšǾѵÎ˸Ξ\x85Ԍңŧ5ϨȣϿѩOƽѕǪpԠǒэШƗԗ'ӎ",
                                                        'ƶ\x9aЯƏӁΦ\u0378ʩȑФvǌЈϐжƄȢŉŉƃɵʝЙĐгÁΈїĥј',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʟϫEɺʤӰȫҨʝBɸƵdƨБŤȢђ|ɝʠӞͷͻˇϡЦ˂ʴū',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210413:001707.079634:+0000',
                                                        '20210413:001707.098418:+0000',
                                                        '20210413:001707.118888:+0000',
                                                        '20210413:001707.136339:+0000',
                                                        '20210413:001707.155081:+0000',
                                                        '20210413:001707.171673:+0000',
                                                        '20210413:001707.189470:+0000',
                                                        '20210413:001707.205443:+0000',
                                                        '20210413:001707.225354:+0000',
                                                        '20210413:001707.240213:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'úʽӍ\u03a2εҦåʦeҀή\x99ӅϓÿԄԩȯmѨŕ˕Żȍ',
                            'value': {
                                        '^': 'string',
                                        '$': 'Ǯ\x9dƘÏφşϱˀĎОЯϿɝĉʠ+т˗ŢδǀԮžΔѴɯ+\x9cτɗ',
                                    },
                        },
                    {
                            'name': 'ыàtǌЫvƘЛƈǩǫӴѾͺΐψЯ;īͱϑƬϹsʯөśҟԛѕ',
                            'value': {
                                        '^': 'float',
                                        '$': -34763.20372620647,
                                    },
                        },
                    {
                            'name': 'ҳʑŊӑҹӯQ¶ěʐ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210413:001707.447053:+0000',
                                                        '20210413:001707.464752:+0000',
                                                        '20210413:001707.481166:+0000',
                                                        '20210413:001707.498593:+0000',
                                                        '20210413:001707.516477:+0000',
                                                        '20210413:001707.533524:+0000',
                                                        '20210413:001707.547309:+0000',
                                                        '20210413:001707.560678:+0000',
                                                        '20210413:001707.574103:+0000',
                                                        '20210413:001707.587934:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ԊϲʅĕʸϯʒǺǱˏКƃЇ\x91һɉӏʹɳɺíдңӁ˪¿«ɯПȿ',
                            'value': {
                                        '^': 'float',
                                        '$': 582033.476400933,
                                    },
                        },
                    {
                            'name': "ЗȪД\x8d˻ԭėɃ¡'āиʴ\x89ʡŦŖǌʯk;5ҚΨīƨʯˊFʛ",
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
                                                        True,
                                                        True,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ĲĚцΠнɵƈУĪʫWȞɌћ˃ӀʉԀԜɽѣҊƀӧύӺɤƥхE',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210413:001707.985847:+0000',
                                    },
                        },
                    {
                            'name': 'ұäȖ\x8fzŕȰuǸӟЁ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'шѤǪȺЍȲ˾êƧҏÿԘчѧ«мΆşɟʣɞѵ\x85њđƤ˻ϰԆǟ',
                                                        'ɜȷʜΥͶ˟Ӕˡԭ˃ˏӃȭ\u0379§ЧIȮˇżο:ÿĽʕºʖͺˎƻ',
                                                        'ʏяԝӁʒϋǗôǋоʊȘϚ,ȋѴîƤǌȟ\u038dӝҟ\x84ЩԒӳˆęξ',
                                                        'ǧĪ҃͵ȁсѫƐsķуы³ÀƳ\x8fȌƓŨɊԬ¡ŒәӧƯǼōΡ1',
                                                        '\u0378ȓƏ×xϡÖȅΝɷϨǦõϯ˄ėF³ĲșŒцFŜŌ<ОʹӰǝ',
                                                        'ҮʹҴâʤǕȹʹӓϩǰĝǚȟɐϯιóÏώԓ˕ĂɀL҃ɏjɋɲ',
                                                        'ƪðˋǺѰƄȐΤжĔϰԅÅ"φˢүϢʫԮҵ¿ώãҐçЄѧǆ\x93',
                                                        'ΥѴbâʋő68ώ΄ƀά¬Ŧǂȕϟ\x8fԈȿúǛ¢˖ɉĸҺϔҐĐ',
                                                        'ÅЂƱƘĎGƹĲȃυQǈȅάѰć˻ѮǥǓǕИˊÈtäˆǢӮë',
                                                        'Ț®φȐųˤŮԛϼÍϾԔ)ƴӳԆÍϋêãƶ Ϧʳ3ťѾ\x90ĉê',
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

            'identifier': 'ĴʎʖΒǟ',

            'categories': [
                'invalid-user-action',
            ],

            'error_message': {
                'catalog': 'ǭȎ',
                'message': 'λ',
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
                'identifier': 'ӚL҉¥іЭӂēeŒѤșԬɑÁÇȩˉ:0ƾȕѪκӎąvȅĠ˨',
                'categories': [
                    'network',
                    'network',
                    'os',
                    'os',
                    'internal',
                    'internal',
                    'network',
                    'network',
                    'os',
                    'os',
                ],
                'source': '\x8aɡġӋӀȗ\\άɾ0\x85λƖКȨъűͶƣÇʗӀӳәҶϖǠцÌB',
                'corrective_action': {
                    'catalog': 'Ûçʭ΄Ӝ(9ӅѣɑƒԇȯǯʧѬοўϫĚЙ҃',
                    'message': 'Ѫǽȇ\x9bҦΥƅǮԡÉџͻЌԖųҗйҋԌӭ:ɑ˖Ѫ҂ǐ\x7fɡūƁ',
                    'arguments': [
                            {
                                        'name': '˲ĸƓǎ\x91|Ԗ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6011549483408290361,
                                                    },
                                    },
                            {
                                        'name': 'ƩќgϣǾɛăѭмȝ¹ƣӲǀʯǱ˭ъȧ˥Ȉˠ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -77592.83384033722,
                                                    },
                                    },
                            {
                                        'name': 'ɇ˭ϷǄӝČüÊƺ*Ð\x99ӔêғԜˡԀɛǢgӟЁe˞ͳ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƗͼҥǥԦȵʭŸƘä\x97ǔǾcʽwƪĦːıҌѦβԮɍϩД҃ќ˜',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'įɰǞěѻʼ\x85Ƌˌж˸ʗķǛʛţł΄ǟԡśѺΌЕ\x8dϻӫćɑÈ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -98047967470024546,
                                                    },
                                    },
                            {
                                        'name': '˵țҌԦŪN\x8bӐŵɗϸȑƼ\x9eèЖƹʥǾ\xa0ϸԚÿɿřµ¹&ȮѴ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            431308.7596994644,
                                                                            -95496.35073066049,
                                                                            992757.2247646993,
                                                                            370658.52680121287,
                                                                            255654.00932018098,
                                                                            87907.11487378896,
                                                                            -22183.361093872518,
                                                                            944876.2278006463,
                                                                            56964.11703025701,
                                                                            769262.0188981555,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'FʶȬǙª\x92ˊыƚȼɋ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƆȽҔɲƱʥƌɍƘˢŘxŌóϓƑĂ҇ͰφƽЈˍ¼ҚʰŽѠΨƊ',
                                                    },
                                    },
                            {
                                        'name': 'ǠʄџW¥ҘԀǀ҈ӭMЕ@ʘқU&ĮϲÖʏʳýӴҨԩ]ӁўȬ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʢуƴԁҷƩτˍ]ȶΏ˨ΪέŴŠ\x86ȔӶ\x83ІѽàʯóʵǏɏMƄ',
                                                                            '\x87˞ξƺΆ\\ɇәǐǆ?ροԩơȄΏŀɉɳҗĊΎǬǞɭȕӪөǟ',
                                                                            '`ЛԣĢνǊҡɝɰÓϥɭҜˏVÖηҫԑѩźˊ˵Ġ0ȆӦÝĠԔ',
                                                                            'ħҼϡ\u0380\x8eŕ$ҫŖΧԣˎʇӴŮ˩OҖȍȁӉӇrόǷőʁʝąϲ',
                                                                            'ĿlϦÇěȊǫъÑ®Ҍѫőʇɷˏɱʩ%˘ĢҨԪ҉Ϋ˙ıӄ\x8dС',
                                                                            'ǟJė˳ȬǦэЛ<Oʍ8ͺʾԂ˒ЇŲȠβ°ЌθӃĺҎͲ˧ψχ',
                                                                            '\x9eЧ\u0380˸ȳψǫɞ$ɨΏ$łғ¾ϼʉƦϞӷÔƋɢȖČ˞ŹȺ¹Ȕ',
                                                                            'μŖԧŲӿǞǾöôƻԆĐҝʖȸƞʵιƃȕʨʬѵԭĞγБØѪҰ',
                                                                            'ʌҡŅҔ\x9eǱ\xadȆԢҹ҃æȲԥǻȦèɜɍз˩ɦͿ#ĠӈƩʣΓǲ',
                                                                            'WųҸѽƌǮ϶ŵ\x92ӼјÁǼCȟαҷϏтĜʀϐĊúʼщûàȸЎ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЛŗѤєȌҫQǖϘȁÐēӰҦӠԪWſӥ\x9eӺßŀӮƉ@ѥ˺^',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'цʊѻķĀˮĭí҇ҢԨӄʿȳàȮ!ҬɃ҉',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'xҭɰşțҩġѱ΄ŀÒ҈ōöǄѱªӗ˰ƂϕӹӬǝҢЍӅ7ȡĽ',
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ƓΔѪɑŨˁ˖¾ҥҸϙŨŭǨŸԬľö\x8eȔ҆DĂЎʴ˅ɋВƥƑ',
                    'message': 'ԝĲї\x7fßӯϚі\x8cΌĤōɄʴɪG4Ǚ\x81ˈŊŜͼǱ¬ЫϬHґǹ',
                    'arguments': [
                            {
                                        'name': '·¢Ų2ůӞз˥ԀƸ"¹ɥǼԧωǦ˨ԟ«ǖǛĒϸ4Ê˾Ɋө˯',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001700.517967:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʵѵóϢǚţɥеèɅԚѤҨѸ\x9bM˹',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
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
                                        'name': 'ӌ\x80ǚóƖЏƥZǝІФƭˠǔӄ{&eӻƸ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ƭň\x9b\x8f˶ԪXȟɋɪȒʑÈŰΓ|ǶŌѲ\u038bĨҨʄűɣɥʐЀɍӟ',
                                                                            'Ʃ\xaduӦыϓPµƃԕҒʙưұƜЈжY©ҵџӋƣƼҩĒЗɹʑĸ',
                                                                            'ΝϟҾҳϞ¿ǀτƙ˨ɁŢòɒҚ҂ưϑ¨І\u0379ĵȺοďĚǚȼԮɘ',
                                                                            'μ&ɉɩҳȂʛұĞҐԦКːѻЍm8ΒӧԒɺԤЂǖȪӮԆҸәǏ',
                                                                            "ԜɃŘê˲ѝԉƗϳ\x86ǷƲţϙӎȂυŶрѩϣ\x88'җǭҝɪӬӬŏ",
                                                                            'ϡŗёǫ;χʿǱəвΦϐȣǕƵ\x9dɣТ\u0382ԞΔʲ˱ӭʖγҏŒʬį',
                                                                            'κĄéуϧєǰěԄǽΐʬɱψĐčˍ˛Ԡп5ϰ˗ӽʞпQȾѕƎ',
                                                                            'ȉ΅ƫȯúѥƤƜΔQĚȕƪҾʫҷĸÍ·҂VȝђԢ\xa0ňƆϠȄΎ',
                                                                            'ʄŤщƘƖ¤Ш½πҠϜŶdΖŽĢԒ#EϸɹϓͳĺŊїǢ\u0383Ϸą',
                                                                            '§ʑǯΫѕҐǍ¹Ŧ\x9d>͵Ɣ\x89ЌшҔӪǪøӼ"˵ѺŌ\u0381ЙUǎt',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʪɺӳ· ƌ΅ӐTә®ńóρ-ƥɄӿӣԍğƭƅ¥ǬҬŰӲʀҐ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҍƮ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƓДϫĞ\x93ɭ˜ʗǫͳϓÂɜ˃φɐϻѥѱҭȻұǃ\x83\xadƳĉʲœȂ',
                                                    },
                                    },
                            {
                                        'name': 'ɏȰƓǖ!ϵς\x9fΨʝԈʘJàѺċűŵԦļȦЂ\x93ƛηģӽҾΚɟ',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȱɭí\u0383ӆǯ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -67278.19450317786,
                                                                            359258.6831375623,
                                                                            829021.8089312367,
                                                                            898887.1717004142,
                                                                            -64314.64983354869,
                                                                            -68728.4914844989,
                                                                            200521.01082317525,
                                                                            244368.51962997817,
                                                                            830240.4786665933,
                                                                            799940.1012712892,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ђcς\xadɯԏƍҷƻΏŃĶ(҅ƆԬӋ¯ǤґԂѿΨϸǥ\u03a2хҗÑƮ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '(£ӅàĬʷʣ˔ɒɈǈɣҹңmɷʸʘҐ˙їǽȍӰȥԔӺŕӽʜ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ʬҍκӔɪʶУҨħlɇŔŊάҬџ˚ůƴ϶˻іΓԬӨІ˔ʐıƩ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:001701.925180:+0000',
                                                                            '20210413:001701.942302:+0000',
                                                                            '20210413:001701.960097:+0000',
                                                                            '20210413:001701.976644:+0000',
                                                                            '20210413:001701.993357:+0000',
                                                                            '20210413:001702.010467:+0000',
                                                                            '20210413:001702.028661:+0000',
                                                                            '20210413:001702.045028:+0000',
                                                                            '20210413:001702.058141:+0000',
                                                                            '20210413:001702.071530:+0000',
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
                'identifier': 'ԎíѲԗ˷',
                'categories': [
                    'file',
                ],
                'error_message': {
                    'catalog': '\u0380_',
                    'message': '˭',
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
            'locale_code': 'ѳǵ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ï',

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
            'catalog_name': 'ҕʉɱԥōЦНΣȚSˆɶӼЦϸʐ͵ΛȞҷ\x86Ѽ§λĐӅЧƶ˩b',
            'locale_codes': [
                'Ȏ',
                'Ѱ',
                'ǉ',
                '§\x8e',
                'ϬɈϺʵ',
                'ϡǓ҉ȔêXɏ',
                'ʱ',
                'ŷ,Ǔѽ',
                '΄Ич,',
                'ϰԟŵ\x8bҚҀΖˬ ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog_name': 'дĄφ',

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
                    'catalog_name': 'ϺˇɅТХŰˠχɲƻηҿԠZʹВʴΧӽ½ƤǹΞϪÛϜΓʗ,Ũ',
                    'locale_codes': [
                            'ɛŢʂʦхԊ',
                            'ą҆',
                            '˪ҩ.',
                            'Q',
                            'тϝ',
                            'śɝҡԄ',
                            'ƯǑϢUþ˘ѴÊ˷Ș',
                            'ҰΐӲЂЮ¶Н+ƾτ',
                            'Őу',
                            'ƲˑӪ',
                        ],
                },
                {
                    'catalog_name': 'ǇȻ҈zł,@ѓäųǘĽƭԦӲˢˈҝСţɷΐľŸkԓѷѧˣӑ',
                    'locale_codes': [
                            'Ĝъj',
                            'ь',
                            'ǝŐβ\x93ˤ6',
                            'ąvѪȀȺγ¼Ń',
                            'Ͼ\u0382Óԅsқ',
                            'УѳϒʐӄɎŲDҷ',
                            'ėcȾӢ\x81ԃľ',
                            'Ԥu',
                            'ԗщѣДӬƸ',
                            'Эñ\x9cŔ\x8eю+',
                        ],
                },
                {
                    'catalog_name': '_ҴÐƫɓêΥĹ¯ѯǩ\x91ЎԐǱĒȕїȰĳºύː½ҩȦǹmѣǨ',
                    'locale_codes': [
                            'ȢӊӫîҽӀʽLхҘ',
                            'ƿ£˰Ҟɰαҹ0ѹѧ',
                            'ȶ',
                            'к˨',
                            ';oԖź¶+ϔ',
                            'ǏȕA«ōƦίϼ',
                            'LǩR',
                            'ſ',
                            'җĵ',
                            'ƙǱғЩ˧ԀԀɓ',
                        ],
                },
                {
                    'catalog_name': 'ĢÊ\x98˷ӛõԂҖИ»uśƤíԜʲŋȣӞƦŴԩнßϟǘøkÂu',
                    'locale_codes': [
                            'ϻǩĹšͰƄъșӠ¨',
                            'ȩҒ҃ӻӖЂƕ',
                            'ғȵ@΄¸ОљӌҊΉ',
                            '\u0383\x88oɱ˩ʹÛ',
                            'ę\u0379ĪèҦéǶАͰa',
                            'gʰ',
                            'Ȅ',
                            'ʙ',
                            'õ5½ȁȿƘО',
                            'ǛŊʚ',
                        ],
                },
                {
                    'catalog_name': 'òƱâѽЌɺͼ',
                    'locale_codes': [
                            'OûҺϵԋ-Ԧпх',
                            'Ωоœԙǰ÷ĝήζ\x88',
                            'Ūθǿʒ',
                            'ΈɁшřΩHbу',
                            'əȶ',
                            'ИԖʩȪ)Ϡ',
                            'ˍƊ',
                            'Ƴԕʊ÷',
                            'οŝϼԌqϹη',
                            'ÑҕҼΌ˘҃ȰѾ',
                        ],
                },
                {
                    'catalog_name': '¸Ȁ1ҿԗ\x7fѲϷϣç҄ȪЙəèåˉԬϬFLΝѕİśȕʥӼ\x83ɝ',
                    'locale_codes': [
                            'ÁШҡʸȀ',
                            'ӏȕƊ',
                            '\x8bǝϩɠύˁ',
                            'ʋқϕЩ˸ìV',
                            'Ɋĉ¿ƍӣΐ¥',
                            'Ɩ',
                            'ȋ҂ЋųɂÆБϦ',
                            'ʤěƺ',
                            '<ʝΟ',
                            'ɚϮ|ÒΓ˝˷',
                        ],
                },
                {
                    'catalog_name': '˳ЏϽіҼηǈõȁωмʌ˾˵ŵǈҰӠѕшe¿Өā ŕɷʔƺň',
                    'locale_codes': [
                            'ʷәƆͲҦʗƎ',
                            '˓',
                            'ѝƹҾʄǢфέɨȫö',
                            'ÝΘĉǏŰЭcAþ',
                            'ԤԊ\x86ӚĉȼƜ',
                            'ȺÞŏƾ\u038bA',
                            'ŝɗѩ',
                            'Bҹ¼уåeȼÖ',
                            'ŬĀҞΧϊǤ\x91Ś',
                            '±υсҹ˞',
                        ],
                },
                {
                    'catalog_name': '\x85µһќRǒгИ\x8fģ\u0382ΦҀɗ\x9cч',
                    'locale_codes': [
                            'Ѥ͵мҹϸ\x8fɐβȝ',
                            'ÐƝ˱ӶŌƐ',
                            'қ',
                            'ŪĿɉ',
                            '<Ҁ;҄Ҡђʁwɩϡ',
                            'Ȩ·ӟҗ&',
                            'ś9ϊѐŪҦ:ʒΖϔ',
                            'Řȉɖм=iͿv',
                            '˪',
                            'ØǗԉƸŃÁƝ',
                        ],
                },
                {
                    'catalog_name': 'ȅҺȻˁӀͽɞɳǆ˥ԊǇӈɺǮң҆εӟϔȜћӫа',
                    'locale_codes': [
                            'ҹųӷҀUå',
                            'ƚʶűƇͶţ',
                            'ǿ',
                            'ǰ\x83δθԖБŝǇ',
                            'Р',
                            'ɼēSϕĉԆØҪ\x98',
                            'π',
                            'ί\\q',
                            'Ѣѩ\x8c',
                            '³',
                        ],
                },
                {
                    'catalog_name': 'ϋúF\u0380ʹʢʋľҲȹ˃ѭµ®ԓǟª˚IǬ;ʞŭӍ˟ĳʣɍʘ@',
                    'locale_codes': [
                            'ɷϑ',
                            'ҤИnӆ\xa0ΩӍӺ',
                            'ЦƭΜ·Ө',
                            'њǠ\x82œ',
                            'Ťьǌ',
                            'ʀăӋЭƙθń{Ɖ',
                            'БǬĭӹ¼',
                            'νœ',
                            'Ұψƿ+^ΏΊϠ',
                            'Μ˛άогġș',
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
            'name': '\u0382ҟǧӞeƛҴʚɅҶɮ7ɡԛ˻ԑͻљҍгԝʲӭŏ˹ϗýśǣʼ',
            'code': 'DΚѧŁ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ä',

            'code': 'ȿ',

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
                    'name': '¼ƁǏĚÖыЫȂȲǦΜĪʂȘĒθƌƸɾνψê\x85bч҈ѼҫƎʮ',
                    'code': 'ψυ',
                },
                {
                    'name': 'ЦьбƴŉĘ˫ĎªˏпȣѩXʁʉǒ\x9e}ӤƳĎӼѫΫбƞKʠν',
                    'code': '\x8dϿ',
                },
                {
                    'name': 'ȅʱͼɄԗƙΌчıѯƋӊǜіӸΟwЭĵЈȤОșέτµЇͼčɑ',
                    'code': 'ƢҔˌ˅',
                },
                {
                    'name': 'ŽŒǒΡΚƐčϜɖϹ˽ƗҋʔԕɯґэΊ΄ʣѕӷÌѩҞ˦ӻEх',
                    'code': '˦БȋýΊξŞί',
                },
                {
                    'name': 'гӵŷǗɋɮ҇xё˫ɡ¤Æ\x90wƑ)ÚĤŶϞЉȡѩcˮİ,ϑʼ',
                    'code': '\u0378ɦŵϷμȝӫ',
                },
                {
                    'name': 'ʰțшԌͿЀ\u0379äŠƅВ˓òǱȼш',
                    'code': 'đѸϖɨ˄ЅҦ$ӱ',
                },
                {
                    'name': '4ɝʞçԮåΏǬaƌżφʇƏ¶ƵˊʆҽĊÃϻưĵ˦ԍԃʍǚɂ',
                    'code': 'ʀӓЕƿ[Ǫ',
                },
                {
                    'name': 'ӆſCøӄɮЀťĂЩÇϿү®ЖöǬΥ\x91\x83¯ȲƑNŲ\x8fǾħɋс',
                    'code': 'Ӕ',
                },
                {
                    'name': 'ԧȺҼşəǐӸɐʴӮσͱΑȲ\x9cŃ+ɀ/AʋЛҴԏԛʽϡ΄ūʓ',
                    'code': 'ʷЉɟ\xa0ͷİèӹŊ',
                },
                {
                    'name': 'ȟůӣό@˃ʊҳȿƃ˃ѥĪǗǘ;©ϬʧԝԆԚɃŰѐŜ Җѯɝ',
                    'code': 'ѣÞѣё',
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
            'locale_code': 'ӈϬŅʍTȐ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ʪ',

        },
    ),
]
