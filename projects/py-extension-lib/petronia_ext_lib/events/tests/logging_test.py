# GENERATED CODE - DO NOT MODIFY

"""
Tests for the logging module.
Extension petronia.core.protocol.logging, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import logging


class MessageArgumentValueTest(unittest.TestCase):
    """
    Tests for MessageArgumentValue
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MESSAGE_ARGUMENT_VALUE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.MessageArgumentValue.parse_data(test_data)
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
                res = logging.MessageArgumentValue.parse_data(test_data)
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
            '$': 'ΌӞØµȯǭѝόβϷǢåȬѢҼѲҟ(ФYØԥɲŋΉΏ˺ußĜ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 582526710691525646,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 801050.0920748466,
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
            '$': '20220523:220037.644167:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ϞáSăӳŤȅģѮҦѓ\x7fҧɐ ѕԄ˙ˋӎńǍΡƈȷļүкȑШ',
                'Ȍ\x99ҋʮϥЇωӁȘӦЫӚҵνʚ9˭ǞȊǁaҴHΡĶ˪ōʗŶŁ',
                'ӼìȰѿçʎœÍƭϤŎǱϚϝƴQyǂπϚӨŁŽƔ\u0380ˏɔƎț.',
                '҄ƒϼ϶ɓĢҠϭÞüͽ˓˳\u03a2Ȗơ˪:řźѤʳżÕɽԓɽĉɴâ',
                '˜ҵÈΝ҂ҎӑƻλŶѕǵѭǖѢǽϣıɺuӳƈԁġȕŇȏȶǉñ',
                'ѯûåνЩӢǖқƏ0˓ȱӐǸʰҩԢ˞Ǻˮ\x99¹ƋͻϐÞeѣǷѭ',
                'ɰʷúӇÞÌĥŎǱǳĮз(ŻʳƪĂgш\u0382ҊĘҥÂϴНǓμȾɎ',
                'ˊǥȨΡéΐȩÊѻΖȪˇΜТĹĄԇӑɯλԒȇȔɲʡļӻǭΤã',
                'ӍϬµȈѯßӚϑԠŤʽҺЇљĢ¢ǗƯńȁǴĄǽÊhΪӥ\x92Źǅ',
                'ЗƘψˎӓƻɖσсЅĊэɪĐÍŎʌʍƞeŉûŞѕΨ·ԣȜʩɐ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -8190419778572424133,
                8346747384955872453,
                -1610359233702701676,
                -7379420717496265898,
                3540272584356347052,
                40046970887850406,
                -395354542357095176,
                8075702889391278092,
                2881645725673366464,
                6723883356505899267,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                -64818.65912270029,
                861388.5556198733,
                46794.86984901625,
                185444.06516037555,
                499102.2204808369,
                149581.72780155588,
                490529.2188180869,
                408104.64014192205,
                373114.96208284236,
                435947.0410224376,
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
                False,
                False,
                False,
                False,
                False,
                True,
                True,
                False,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20220523:220037.649067:+0000',
                '20220523:220037.649153:+0000',
                '20220523:220037.649237:+0000',
                '20220523:220037.649334:+0000',
                '20220523:220037.649427:+0000',
                '20220523:220037.649509:+0000',
                '20220523:220037.649591:+0000',
                '20220523:220037.649674:+0000',
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
                res = logging.MessageArgument.parse_data(test_data)
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
                res = logging.MessageArgument.parse_data(test_data)
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
            'name': 'ǻӝ\x9fLΔҷΦȸſͱąʑʭΝбϲH_ӾşĄмʹ',
            'value': {
                '^': 'float_list',
                '$': [
                    115333.62667063341,
                    487088.4177427272,
                    265443.47022834053,
                    978171.863157806,
                    882806.8619080428,
                    -91172.29394622796,
                    122193.81179789855,
                    391826.1013443459,
                    674874.4656100075,
                    666991.1885340107,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʁ',

            'value': {
                '^': 'int',
                '$': -1538023913859833910,
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
                res = logging.LocalizableMessage.parse_data(test_data)
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
                res = logging.LocalizableMessage.parse_data(test_data)
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
            'catalog': 'μЉȼЍɡÇ˙)ӼƠюҤӼʵЗɎҐЁҽΤƃǾĥâáɰҹРҀǣ',
            'message': 'ΎOЏǸ>ŇÅμ)ƊûĸǎѸɄ\xad\x9dƉ҄ʭҸʝ;ɖˀЌ-ŝ\x948',
            'arguments': [
                {
                    'name': '%ϰѴʰǄƖϮϙɽŦØ\x97ѫǢӨӛσΛȲϤƂȑǁѻͺΣ˱ȶ\u03a2Ș',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ӼȠ\x8a\\ύ}ŷͻРЎƨɊԐΫˠā\x8bɃΤѪԫ³ȂƏÇǙǚȍӁź',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': "ɔзʨr\x98άҁƽͲĘȁԂƋйó'ɑǈäѤӿºŘӂ?ω˕",
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
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ȳͺ˾˘κϛɜ¸ƊԊĽ\x86\x95˸ʣɀʂƻĵƽј\x85ӗҩǯч¿ɾЭԫ',
                    'value': {
                            '^': 'string',
                            '$': '\x80н=Η\u038bВƈĥ˚\u03a2ãѺĎԓхŲƅԜӧӅƯȒƭӸĦҤɧĬ¸ҝ',
                        },
                },
                {
                    'name': '˂\x93ŌŠ+ιϻ˃ĨǊЗЏǤәʯɞ˃ʉʆĻǾНϓƌÜǎ\u038b',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -3535655255587695625,
                                        -5985312518429085961,
                                        -1921151040947963732,
                                        5446541153289414059,
                                        -1195176929001599080,
                                        736701220563872173,
                                        9163473299246404747,
                                        4828752676679064987,
                                        -7759322574151510016,
                                        478053709121453220,
                                    ],
                        },
                },
                {
                    'name': 'ȬɓÊ˞ӅƨӓѡԝЦӣѕКҾÚӇŪЏȢ¡ʍ˳З˚X=йΆԫʌ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        True,
                                        True,
                                        True,
                                        False,
                                        False,
                                        True,
                                        False,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ÅϪѧԄόҏǙÔԮωϖtHæĵΚðïĀȣ*ʷԡӅ¾ʚύ˵ЍȦ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        7964728104462093579,
                                        3178343982358918113,
                                        -433331824708984589,
                                        -7550459257805886867,
                                        -6964825670527303175,
                                        2354002766374797093,
                                        -4027135713268124498,
                                        -6302054611833496016,
                                        1711001342884129899,
                                        -5005298248235150473,
                                    ],
                        },
                },
                {
                    'name': 'ЯXɧîŦÔłŹɿϓǟŜ¤uήΧȨѷƧɻȼ˓μĕӑƂҷƤŧû',
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
                                    ],
                        },
                },
                {
                    'name': 'ѕƭkԣJҏȀЋжȰ<ИɳȣʆȦǃӌͻƒˀФŪƉ\x8dčЂķ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20220523:220037.639252:+0000',
                                        '20220523:220037.639342:+0000',
                                        '20220523:220037.639421:+0000',
                                        '20220523:220037.639508:+0000',
                                        '20220523:220037.639630:+0000',
                                        '20220523:220037.639774:+0000',
                                        '20220523:220037.639927:+0000',
                                        '20220523:220037.640078:+0000',
                                        '20220523:220037.640166:+0000',
                                        '20220523:220037.640244:+0000',
                                    ],
                        },
                },
                {
                    'name': '˹Ū\x85җџҞũʖȕΩӐʧĽ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ϱq',

            'message': 'Ԥ',

        },
    ),
]


class LogEventTest(unittest.TestCase):
    """
    Tests for LogEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOG_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.LogEvent.parse_data(test_data)
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
        for test_name, test_data in LOG_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.LogEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOG_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='scope', name='LogEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='messages', name='LogEvent'),
            ),

        ),
    ),

]


LOG_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'scope': 'verbose',
            'messages': [
                {
                    'catalog': 'мӃ)ŧкŭ҅ԝ҆ӷÒ8åЬ6ǒ˃ӷʘ˘',
                    'message': 'ȁȕʘɺšƉЪɛӟŒϳğǉ˰ɮвѮ$ȇϥΊЙƳĭНԘ\x96óļǭ',
                    'arguments': [
                            {
                                        'name': '¹»ǟD\x96͵ĽüËʖ˯Р\xa0ѿӽ·ǓËʒIӱʫʂˤщȎȍǠäϵ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1841515177023971605,
                                                    },
                                    },
                            {
                                        'name': 'ʥ\u0380ýǃǎǿéƓȈïŖȦˆЊԝӽʬǯƁϬ(ɜĉ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220037.545140:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҸŽѱƞ÷ћԕрʥɧƴМƿȀȈӘɈ¡ɮȓЂ˟˦ƣјM¹tԞƀ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ûA҉ҊЭљʌÔηȿΕˑ\u0379ǷȾĈþȅɽȓӧˎĮɤȟɋǢƅ§ĭ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9200027926705276902,
                                                    },
                                    },
                            {
                                        'name': 'ŐҜǍʿµòѲǉƐϮɧ\x85',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1938730377393242412,
                                                                            -3940021831380608070,
                                                                            1347116711296522010,
                                                                            1876602809340081754,
                                                                            -1007126184694495691,
                                                                            -2020690437021806343,
                                                                            5656710095996306578,
                                                                            -3370029891345839879,
                                                                            -2118930320160439440,
                                                                            -5068829060435180471,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʐıҊȟóҮͲЏϙҘƼʔϵѻȮŴģηɈǓ˛ʥɋÜàҽzIˈ¢',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220037.547696:+0000',
                                                                            '20220523:220037.547779:+0000',
                                                                            '20220523:220037.547858:+0000',
                                                                            '20220523:220037.547935:+0000',
                                                                            '20220523:220037.548012:+0000',
                                                                            '20220523:220037.548089:+0000',
                                                                            '20220523:220037.548165:+0000',
                                                                            '20220523:220037.548241:+0000',
                                                                            '20220523:220037.548318:+0000',
                                                                            '20220523:220037.548395:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǞϾʃjǯHѡ\xadǥɝƿʱӈêԡέçĀɏǡŀύĖǕΤѸʊȱҟ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 734880.6936938501,
                                                    },
                                    },
                            {
                                        'name': 'Ƌɷǫќԛϝ\x9fǐɆκԟǓԇЉ,ќ\u0382öɟ=Ήǃ˸҄χvϭqК',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220037.549435:+0000',
                                                                            '20220523:220037.549542:+0000',
                                                                            '20220523:220037.549658:+0000',
                                                                            '20220523:220037.549778:+0000',
                                                                            '20220523:220037.549939:+0000',
                                                                            '20220523:220037.550083:+0000',
                                                                            '20220523:220037.550199:+0000',
                                                                            '20220523:220037.550277:+0000',
                                                                            '20220523:220037.550351:+0000',
                                                                            '20220523:220037.550426:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ėί˨ϛ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɕ\x90г²ʾȀ=ʰͳЁәɅЅӄԕȞd¾ĖͲȊιϹȺҟғ.Њųİ',
                                                                            'ђpȬĮ^˨ϊȏoў\x9dɷá"^ӾʢҹȃÍ˺ӊ¦˶еӎҌYąȍ',
                                                                            'ŗƳΫβó˽Ӣэɂ·óйʤτóQҶӬƭʗǒȰӚ7ȏrïȔʠϫ',
                                                                            'Ê˘ɵɯчp҅ȒȈϊĪŎӘӰυęДĴB´Κ¾\x92%ƍ9tɹԨξ',
                                                                            'ʜǤЉł˥\x96ŠқƁѬ˺Ǆ҃\x9c8ͻѭmzɾ\x92ÔҎÿĉ¯ɵӔƏ\u038d',
                                                                            '\u0380ЂԔјˢӲҩʇϓöό1ԨLƯτȷǮӕǒєǆнǉӲ˽ľӼ]ǖ',
                                                                            '6Ҹʬ×σϷÖӉǄʡȳ\x99ІʻϺƤϠӑʡŁǌљƱïȴ\x9dɂƐҳϐ',
                                                                            '\x9büȀ]Ӫ˶˻ƗʉɐӨїҳӒȓäӚ°¹ǔĮˈͱӫǢҌʓĦű\x8a',
                                                                            'ȱʢХTāǁĐǙЅѳʰǝœѾŭрτҙǅʪϩʻƛ΄ԉƋiѓѐѯ',
                                                                            '˕эϚΫлȕʘGĵóƷ~Ǯ¹ґÛϤȖƱȗήýϡ\x7fȽĠϟʩшѽ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЩDͱÅȑq°ɏӡеȴĂşůӢǵëȤɩԅ¥ЋǰtљΦΘӴ3π',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8543095812005999147,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԝˎʚ˂PϐΚϧŌнǛЗȊȊr»ζЏǽRɊ˫ğӠŀƖώþǗ$',
                    'message': 'ıУÄЯӧrʯɐȱźōѶ*ēνѿΘХϨȨҹüȅȳɉʠп1Ψ\x92',
                    'arguments': [
                            {
                                        'name': 'ґΘŖǅfҴ\x8f¨ЖԋØɒĝʠʧςϰАŵ˭%χƑ`˜ώ˩',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'џͼ¦κΛЏȧľϠ҉ȯžҮδ\u038bǛΧ˦ɝvɘ2ǱƻĐƆѨθһ\x9e',
                                                                            'ҹГŠĊâөΝˀŭµЊLԭϺČ\u0378żʩϋΐ\x83Ǻö˗θʪ>Ķӎʦ',
                                                                            'ɬɒŢИ°ŎĜoȐκʘԣɚΥðʌϲϭӛҎԥѧЌɊͻҸ$ХΗQ',
                                                                            'ЪԄÝǳĈęšϬӿΝ\x91ϡ4ηȟқџZ\u038bΐʳ»ҒȶӬ½Зþȕʶ',
                                                                            'ӄÌKǧЂҀ\x96˵ǿЂĞʷǤѬϚϐʞаʣЇǸζӺAkGȊqǿȡ',
                                                                            '\x88¿\x8eˋЍԎϥÓԑςңÜàēʆ=:яОѳΜԙʤȑѻҕÖŞÝӳ',
                                                                            'ƸũЊŹЀʔМĺĿϦù¯ƇƿȽ˕Ϋ;ŭ!Οɻpř\x92ƶóПAƮ',
                                                                            '´ƥΙƶʲƸґʊŻȀƠ˷{¡ȄȮđͶćɳ͵ǒȋ+ϒĀˌơѺβ',
                                                                            'ҫ˟ǅϭҁԦÜéҁļ\x92ο«Ŀ:ɒĠŁΥϻáǻŕɗˏǷ-½¤ƙ',
                                                                            '.ʕFʻūǧӳńζˤɞɦ˜Ȏќ˲ԩŲy~Ĥϲ˸Щ˷˭\x9bԈ˺r',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '3ɔǧΣИɿŒ >ϢӍӀΥΉ҃ρôɦѐ1ŔʇћʟʕϋƑȌň',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˅ŞǊƜŷ$pȡͷǓԝŁtԒ@ǨѭũΤ|ϡ\x9dӪɒѶҭƪ½Ϻx',
                                                                            '\x90бłтӞɛȕ¬ҼĪ\x8fѵҊԈKǖƲƜ˓Ž1\u0380ǐ\x99ȞԛɈіΖ\x95',
                                                                            '˙cɴ\x90ƜӤĖȱǳԩΔ®ȣν5ɪŚД҈Ƌȓɻя ϐƈȜЖ˥ϡ',
                                                                            'ǘȼЛиƽɒʙѴ¥Ūʦ\u03a2łˣ>ΌιĳVξʗĺі˰ҨˆĆǶÈN',
                                                                            'Kɂςӥ˃ʓȋĕ҅ȃ\x85ţӘƽюƒϕԭëŊҴɶӭϼԋƪ\u03a2ƇψΌ',
                                                                            'тŤFēѩƜǟǂɴѷȻěѹŮϽШáˎĔ\x7fӓҸѮġɂʯȊƵ\x8fʠ',
                                                                            'ӃÝԆόғѬ\\Ľ©ɀІɰγĀϙɠˡκ҄±ԛЇЊ´ŉЗъȟʞˡ',
                                                                            'ӤȾãӱŀƝ\u03a2ĨȗɧʁРӤΤϚǕӷØѭǒŪɁӦ˞ԛέЋǐ\\ȼ',
                                                                            'ϼӁˡҹÈФn˸ПĠȉӎ¯Ǧ\x8dǨȪʐϑǺͲ Ǳ.ȍт\x90щĦї',
                                                                            '5Ί\x88ΩȸmɂВƬ,ȨŗҎřӵóњϜƹѧčҕБ$ǭͽĩʔƍĀ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӧ/ȻĔˁҡhȝӣŤԤ\x85ȢǲY',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4824883190640214903,
                                                    },
                                    },
                            {
                                        'name': "ҺВÄˢˊJʳʸ\x9cӉņǲˎķĺ'ÍϚ˪˰ш˹ˣӛ҆Ȫϡƅ",
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220037.556529:+0000',
                                                                            '20220523:220037.556611:+0000',
                                                                            '20220523:220037.556688:+0000',
                                                                            '20220523:220037.556764:+0000',
                                                                            '20220523:220037.556839:+0000',
                                                                            '20220523:220037.556914:+0000',
                                                                            '20220523:220037.556989:+0000',
                                                                            '20220523:220037.557064:+0000',
                                                                            '20220523:220037.557139:+0000',
                                                                            '20220523:220037.557214:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҸԗdѓðĴ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -80612.77624840452,
                                                    },
                                    },
                            {
                                        'name': '\x9bɖȀԜǎе»ԋŪԮιФɑӟĸƧ/\x8fˋØһ%Ǫșȳҏɣѱ\x94ʰ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220037.558177:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȶԥўƩŀO\x7fˢãͿѥȊ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3973846495017908258,
                                                    },
                                    },
                            {
                                        'name': 'ҕƇġϫ\x94ӧvĔěҼĂӁŵâс8јǇ-Ϸ˞ƹÉg#ĪӃDҖÁ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 313587.4342462535,
                                                    },
                                    },
                            {
                                        'name': 'ƅ\x9fģ˵ªΚҦЙΉҕɘƋ-МāƩCӊΣпї\u0382ƥƊʫʨǃŕІɽ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŀĝƨϴÂżõǕǑˆ҂ҕ_¼;пҙҞσɍЊʸϙƄȣЎǳѻĤϮ',
                                                                            'Ȑ\x8aЅsɉ.ӧϛÌΗӁӿǴţζιËϷʗэùϿϝiɥçǒ˕Ǒ\x96',
                                                                            'Ҋʻëƫ±ϧҞαϩɩªȴ˂ǴʱǧɸǤʸĖƫÿњȦ<ҝЄʪ\u0380Ϣ',
                                                                            'ɢϡ½ЉÌɪÞțϝТȶѵǶӄ˒ʁ˻цӔЕ4ɚΎȉ·˯˹ҨәӺ',
                                                                            'ɾƛӪ\x8fřĦҰʰɁϿɎpϵҩϪӻԜ°Ƹ?ӀȤ\u0380ǒѣ˞ˋưÈʼ',
                                                                            'ȾίϡъĘҐɘÔͺˀ¡ġѳϦɽтèƃӅò§ǯ\x95ӱÁԧɛŞ˸Є',
                                                                            'ņý±ɍȭŽ˚ʽŜĒȎр\x8aƒϲ)ŊԔϘˌҹҙѿɂҫˣ¦ĺƙɲ',
                                                                            'Ìƭ½¼´Ѯò˳;ʜɪѤĚ\x8cƛӘ|рʄӁƓщύ˟\x871\u0379ųňɑ',
                                                                            'ͲԅΖʘϒòɿ˚ΈʫќԖͼǯɷɈбʐĉΎŨԏ˻\u038dƱТƜǥ˰¨',
                                                                            "ҸҕĉƉÁʔa˄ʴŒʀɯŕ͵сҼøӽɒԩя'ӯˣʷɹƁΟɔˏ",
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˹Ƶïѐ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            26140.72271073835,
                                                                            78054.00991885285,
                                                                            532445.8329285977,
                                                                            697712.6488191652,
                                                                            691413.8022854837,
                                                                            756896.2384910778,
                                                                            635754.7744065042,
                                                                            143713.8024689259,
                                                                            482681.21163823595,
                                                                            922742.7252442992,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'źɟǇʃ˲²ʕ4ϳӄĘӦȴЅҤӿʰ\x89ņɳ·˻\x95\x80ƳσПʲȜč',
                    'message': '˰ҐѓϲӮҏǛþў.ǙеĕҘʶӶÔưҗʮŵ¬Ӕ0ɥŜŀźȷȶ',
                    'arguments': [
                            {
                                        'name': 'ŁcНĝʳȔˈżõiӄ)ңβʬɱСɀҸΎФ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӢȩgνɉҗζȽ»+ĲʦЍ ʵӗ©ϧЧɺ҆Ö\x91ÜЇÂʋʴĪƹ',
                                                    },
                                    },
                            {
                                        'name': 'єчӀíͻҍȾʵΞӿσ҃ģԥԍԁ=ЭκǊʃσтхǸÞǌѯťҭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220037.563267:+0000',
                                                    },
                                    },
                            {
                                        'name': 'fӾkԓǾƮƷJЮͰͱ˄ԧϊºʢˆƐϬԓ\x8cγ)ȜŵŮÙƔ˳ʑ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            435560181219650897,
                                                                            5630241848504785901,
                                                                            7859755558011786818,
                                                                            -3709379895196514501,
                                                                            3144570423681399626,
                                                                            -8710457412963297624,
                                                                            -2894829580229675067,
                                                                            -463120608752763680,
                                                                            -8039334880219634428,
                                                                            -4221961697511175879,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ťȈРƸŮż£ЙǴĲǜȔĝɣ\x8f\x80ǵ§ϚАѽ\x8b¸˷ɨVЂ©οÖ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '+їȮǂΖ\x94\u0378ʛу҄',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            293312.93584142457,
                                                                            956963.5331064567,
                                                                            251280.95410642563,
                                                                            286471.4816279672,
                                                                            37122.17199503569,
                                                                            444717.3186097372,
                                                                            849271.4632830224,
                                                                            264044.75585918844,
                                                                            352651.4854110042,
                                                                            52300.86239790759,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҩ1|\u03a2\x92ǩɺАŘȻêӵǽʮņZƚϋÆͲ\x89',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            739665.818668178,
                                                                            644311.2404779223,
                                                                            -31937.11967940384,
                                                                            286132.75467820646,
                                                                            473351.12771328026,
                                                                            4680.007352466186,
                                                                            697586.2678034977,
                                                                            520161.49001791095,
                                                                            234888.53779898473,
                                                                            80763.33345211131,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'îǦЯąԩΈȱПƙʰȅ˛\x90ːŃĜѲʑȼ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԒǤǯȝġǉƴɯ»ɿŦќŏʕӌʲĘ˒pΖ¿ʻƇĖӦΪқ¼ύΩ',
                                                                            'ǩӻʧΌϕdПȣԮҎʙĄƪѱǛ¡уˤϡ\x83Ÿȧ§-ζ\u038dǊϢƠɓ',
                                                                            '\x9aңʕЖɴŉȻʦưť\x9e$Əʹ˖ǛȉËСÎȶĶ˅ɣӥȉѰƸŲC',
                                                                            'ʃɣǕѼΦЩЩ҃ϊ˗ȃ/ȊъʻͲˢCʓҹƜҝʹÆɉǋҁҷəǎ',
                                                                            'ҥ«TɸЭƫ&ѯ\x8aѾѩƗǖ(Ҍ˔ӊWşЯŐąŠѷǗźĖˇa{',
                                                                            'ҭĖСĦ΅ȕ·Ѳŭ¡\x93ʴȳЧһѨǛρȍѠØƳѼΪϐņŘɖӀ¢',
                                                                            'Ѡ3ļΎȉǬњӴϧ+ͻğʉӑ;ȈȽXŲƆŝԡôǴɀшϿʾ§Τ',
                                                                            '\x9cƋĶΣŹҚǒѓͰưʉƵ\x9fLʁːğυɰ<Ș˲ķŨӏȥ_˪\x8c\\',
                                                                            'ɟʿǑΪBʎүϩζЈƩԬvʣʆ\x98ėʰϝɧД\x81сɘȣLǿŁ\x93ǽ',
                                                                            'δú\x81ѳёƼүʒԓ%Ġ~ơƤĊĺơɂǁͺùĮ\xadƔĠ˷ƫ\x7fƎſ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÂЖŤϼŕϗЈĎ®ЅɤӹŐĢˣJԑƄġRӇѮȇğ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220037.569310:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϥ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'И×ƭʙɹΰĭӻΓǲюǍŦƍЏ˶тϫͺ\x99čĀʊʵћķˌҬλƜ',
                                                    },
                                    },
                            {
                                        'name': 'cӎǋÇƟɏɛɦο\x8cѮƦԞɀmĂӊɭɋЭ{ˏµėƼɯğĸ˕ӈ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԤǯљȁëϪСь˨ӀϫǨˁѮεӴ˂Ʀ˰¤Ж¨\x95\u0381ǆȫɃЎҡ`',
                    'message': 'ȷƪǇúХΚϲͱɰʣʹˑΘΜҼɱԔљôˋАå˳ӉΪһ#wƑ´',
                    'arguments': [
                            {
                                        'name': 'İ!ļϪìπӿ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220037.571493:+0000',
                                                    },
                                    },
                            {
                                        'name': "ÓǃÊʫǌåǚ<ȓƁԑ϶µϵžĲі8'ƕѵŕҍǋǳϑϷͷСǉ",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1410899567436721571,
                                                                            2132902634128724610,
                                                                            3720869687752447643,
                                                                            7794061838660634238,
                                                                            506741993115456938,
                                                                            -6735602019735287143,
                                                                            -8355667584448664561,
                                                                            2834861067293585721,
                                                                            -2373350393533772491,
                                                                            -5840084413344002091,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΫȫÌåψҥΗ`¯\x82ȧӄѼ˖ȼҡͻҠʄ\x9cˍĝѭǙɢ\x8aǷĝχƪ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2397153940170752045,
                                                    },
                                    },
                            {
                                        'name': 'ͶΓ¨MѧƤʑǉūĘğ"ºϯ¢шĹļĉɺ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6979648317303503052,
                                                                            1397743548128649085,
                                                                            -9011088833447126920,
                                                                            2560716954036004455,
                                                                            2414516871092309051,
                                                                            -2946625167971803339,
                                                                            -1738567345340509861,
                                                                            -5367424308168723719,
                                                                            -4500047543197980316,
                                                                            -8697022479371988861,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'õќŭǛϵŴϹӽïʋЉ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220037.574833:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѯBУʷƉќ-ȴŞӟ\x9cɎʱӔТʈͱŒ<Сȳ;ц$£Κƭ/ɐ\x7f',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            664014.0352397625,
                                                                            520429.59681336593,
                                                                            374865.4671231101,
                                                                            730102.5004550015,
                                                                            46266.558636962116,
                                                                            -24922.91742129666,
                                                                            474007.3208654729,
                                                                            420869.4796220216,
                                                                            635199.6537455339,
                                                                            65730.4629783981,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϛƅ\x90Ɣȣσӻµ˒÷ѵ\x98ǼΆόUļǖӯþŢ\u0378˄`ƒҏʱòH\x8f',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 666425.187916385,
                                                    },
                                    },
                            {
                                        'name': 'ǑȌȯʟγϠɌεӦԆΨʊͿUȜѠǅ¸\x83ķɨ[ÄɻαѺƊҥ\x97\x7f',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4728487235033183245,
                                                    },
                                    },
                            {
                                        'name': 'ɋEª¾ɒԊΕ8',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            73178774021242174,
                                                                            6296923113721487594,
                                                                            5594015082731668995,
                                                                            3849081083182207425,
                                                                            -1161590576486272926,
                                                                            -755186194758771426,
                                                                            5181577406074390126,
                                                                            1375074531251692985,
                                                                            -4206273627553750605,
                                                                            4934390279075881679,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĭšϹӟÀ˷ʦѩІӻӡяƕōǙ\x9aȬҕ#ɜǴӗѡ¸ҟҽ҂?ˋŔ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220037.578466:+0000',
                                                                            '20220523:220037.578553:+0000',
                                                                            '20220523:220037.578631:+0000',
                                                                            '20220523:220037.578708:+0000',
                                                                            '20220523:220037.578785:+0000',
                                                                            '20220523:220037.578862:+0000',
                                                                            '20220523:220037.578939:+0000',
                                                                            '20220523:220037.579015:+0000',
                                                                            '20220523:220037.579092:+0000',
                                                                            '20220523:220037.579169:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƈWƑœӮͿȿːǯԆƥAȉЫҊɳ-$͵˧˳ϥϤť\x85ԛΘІïɂ',
                    'message': 'ю҅϶˜ζÃаɔéѪƖҤɣƋċ\x7fǎ˚҄ϕĚϲϑѵÅȢȩɧuѣ',
                    'arguments': [
                            {
                                        'name': 'ķȆ!ӾěǕįιFи¡еǨόɀȄ¢Ѯ¦ɃʃΨ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 706860.1806038048,
                                                    },
                                    },
                            {
                                        'name': "ԦȤ.ŇŜƬĹğӦƻҦɝŉқӞѳјҪŻ'8λͰȹȈľ҄ԞΏΝ",
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220037.580800:+0000',
                                                                            '20220523:220037.580880:+0000',
                                                                            '20220523:220037.580967:+0000',
                                                                            '20220523:220037.581053:+0000',
                                                                            '20220523:220037.581128:+0000',
                                                                            '20220523:220037.581203:+0000',
                                                                            '20220523:220037.581278:+0000',
                                                                            '20220523:220037.581352:+0000',
                                                                            '20220523:220037.581427:+0000',
                                                                            '20220523:220037.581501:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŽŽЂɪȩŸ/ȁF÷ƼƆQ\x97ˣωŁ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϩưѯǉȖűʡ˥дЧԚǟĶӰśщɹʱЇčҺƣҷIѷÍF·¤c',
                                                    },
                                    },
                            {
                                        'name': 'ԨһȭªѫϻԆưѲƃɞ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220037.582479:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϝӃ\x8eȃʿѼU',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7487172419090763288,
                                                                            1420666730571300494,
                                                                            8166315504085997731,
                                                                            -6617786665038032558,
                                                                            2595668457659244168,
                                                                            4643709342415365092,
                                                                            8037327205099367690,
                                                                            -4932784945077792601,
                                                                            -6830516419822091595,
                                                                            -1243719721601716476,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˨žƹͽĹŉÏ¾ňÛ\x8eȹԄΔîҞɸѮýњȽқŠǦǕÉƃҶʤɘ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ŕϝ\x83rҎ àӴԁɕM\x97ʃ\x81ʇ\x85ЅˡćщԌƍͶɷғĄdù9Ґ',
                                                    },
                                    },
                            {
                                        'name': 'ʔ˞˄ϙʪEƧʎȦѶυ\x8fĢǏ҃шǍē\u03a2ωȂЉӢŪUϤ¿Ñɗҕ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220037.584882:+0000',
                                                                            '20220523:220037.584964:+0000',
                                                                            '20220523:220037.585050:+0000',
                                                                            '20220523:220037.585128:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϗԄΝχɲϊүϰԅԝϦӒХɗ¥\x93ҒʠȜ˅Dҝȿı¾ΛŀÀыĢ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5940852908772285076,
                                                                            -343252718182760189,
                                                                            1270636450985985933,
                                                                            -1763344581488262651,
                                                                            -511778733087226538,
                                                                            4485618822422491523,
                                                                            -8559809904698568576,
                                                                            8427757094762078277,
                                                                            1129165831681819202,
                                                                            7346300984138035816,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƅəԤĢΨԎ2ςԕс˵ϴ\x8d',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220037.586867:+0000',
                                                                            '20220523:220037.586948:+0000',
                                                                            '20220523:220037.587024:+0000',
                                                                            '20220523:220037.587099:+0000',
                                                                            '20220523:220037.587174:+0000',
                                                                            '20220523:220037.587248:+0000',
                                                                            '20220523:220037.587346:+0000',
                                                                            '20220523:220037.587422:+0000',
                                                                            '20220523:220037.587496:+0000',
                                                                            '20220523:220037.587571:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Фƚƴӫɒʲ\x9dПԒʬv˄ԎΈʝ˛íQΝҐ\x9eˢƈʘƹƘ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5155340244315039306,
                                                                            -8344135148596544674,
                                                                            3784861816928678440,
                                                                            7381860816597964167,
                                                                            2008417800514466388,
                                                                            -4724208535274394919,
                                                                            -4149144388843656625,
                                                                            -8790702530911642755,
                                                                            -1856652928535742550,
                                                                            -5732674165342774538,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\u0381ήÏűΤÚΪӝԓ>ɅΞƠǶʂӕ&þƦąǰ\x7f˼҆ʥӱɯŨʚ\x9f',
                    'message': 'ĩü\u0383АΉϿʍǈuΗѾŃƸŽŖγÖϏͰӾɚѣкɷć˖ζάӂʖ',
                    'arguments': [
                            {
                                        'name': 'ϰ˯ΜĭǓɳԡʞɬӆǋѭ˾ȟѽșŹũÏǖ²·ǵȡЈԌӯƌѴӿ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 979170.3067936192,
                                                    },
                                    },
                            {
                                        'name': 'ʙǤχʩÓӺǻˣͻĕʺϸʼʦɅÒƵӺ\u0382ɣΦĒσǔů',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɻjJºϬȅəϴϪР*ѣϜԓ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3620062529522593497,
                                                    },
                                    },
                            {
                                        'name': 'ŇâÏǦ£ŢʫϭŐҨʐͿĩԑɕǰȺ)ΎΘӦвDɿЅKÊʨɩ˄',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220037.591809:+0000',
                                                                            '20220523:220037.591889:+0000',
                                                                            '20220523:220037.591964:+0000',
                                                                            '20220523:220037.592040:+0000',
                                                                            '20220523:220037.592114:+0000',
                                                                            '20220523:220037.592189:+0000',
                                                                            '20220523:220037.592264:+0000',
                                                                            '20220523:220037.592339:+0000',
                                                                            '20220523:220037.592414:+0000',
                                                                            '20220523:220037.592488:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x97Ɵ˱ϨȳģAőԐʓƤӍа˅ůÏȤlʧÄĹʕ4ѳ<ѱ˱ÂШԮ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʋϲѯűҏȋʰÇʸѻўɿԚ˞ʮI0ȆϐƢāϞɘͿÁɦġí\x87҆',
                                                    },
                                    },
                            {
                                        'name': 'ʵŌӞǢĄ¸',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            771232.2228983273,
                                                                            667379.4010918427,
                                                                            941734.3060176532,
                                                                            792922.463700975,
                                                                            -97470.65724377966,
                                                                            568852.0368593232,
                                                                            451779.2684299124,
                                                                            998714.4741173994,
                                                                            509281.7965309238,
                                                                            716307.6355380488,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x98ŀњØʖˀ^ʊӹʓԮʕѶͷưý˩TΈ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǡΠӰϭYƇ¶ɃȫΊԢɄԘԥÒСǯҞΗģϓσĘX˰źѱǣ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 963380.3272513924,
                                                    },
                                    },
                            {
                                        'name': 'ɱ˳ŁԧʒƖßțʸȲýѮϕѹɂƕӆ˂ÐǧЕђӳ˻ϡZĎǷԡӅ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2405760373955008624,
                                                    },
                                    },
                            {
                                        'name': 'ϨFΨſïԈҟӬӔʜΕdïȈɉɿ\x9aȗԒaҢTѸѬoҿȊӄҳҮ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -93920.42793646517,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŌШŗˠҞɊˑӺӜԍ~Ѵ\x8dɍɢÀĿɃȗТϑΌǅ.§ˢśſѠЁ',
                    'message': 'ʎŞƾǷƛ\u0382˛ӕȻʳs\x95ʖǸʢт\x8dҕĨɈÐ\u0383ӸŝАϯŢʼԃ7',
                    'arguments': [
                            {
                                        'name': 'Ԝ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            401414.5994002041,
                                                                            326400.24893587246,
                                                                            554930.3853313699,
                                                                            549877.9344574969,
                                                                            201252.8250048891,
                                                                            286927.157347547,
                                                                            302237.4066129565,
                                                                            280341.3956895853,
                                                                            446402.9788947061,
                                                                            448704.2031672982,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˊ҂vȾŶ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220037.598873:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʹɀoƓƽŐҐάǎqǛ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220037.599269:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ш\x89˂ʳɀСџŸӔӐ\x7fȖÉÅӀȄѻωβÿƈſ1ͿǨϮ˒ιy˭',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'χуѓи[¡ͷȁȾʜʖȃ˽ԫ\x8e\u0378ӈӣ^ϑҊЕǳʍџˬɡԞҐɳ',
                                                    },
                                    },
                            {
                                        'name': 'Ɓŏm%ĠϿƭƅѼѕ!Ӣӈ˞ɿǅȥ˯Ŷʜҥ2ΩğȐԓĿʴͷȽ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220037.600087:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʺ\u0383ęџԊұ˲jҟÊϼҾ°\x87ȉКūԀĐ˟ѫʆ-ш˺ȘұѪ^ʿ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2381085316616212288,
                                                                            3436707255691679330,
                                                                            8799583969388987909,
                                                                            8978693545255498886,
                                                                            -3383781773159390175,
                                                                            -1064367002760259668,
                                                                            3480190718026534833,
                                                                            -3481068497269519523,
                                                                            8880730947041962546,
                                                                            9000087356154837285,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʸêʣɌˇʨѨƢ\u0379ӻÅωζԨȌ\u038dƩŘƣϋɖӂɡɉčԎűίʝҚ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ǧφǉ{ǓхʭԏǌѵҞЉˬȧǖķãƁ\xa0Ýǎǀ<˶\u038bԢϓ\u0379ʳƻ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220037.602336:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΰωL˄KϬʜόÇŠʳ˅',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 901978.707022933,
                                                    },
                                    },
                            {
                                        'name': 'ƒ\x8bʼǬɖӟΆƐ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            457178.547074931,
                                                                            478457.2250324971,
                                                                            802720.8934192879,
                                                                            879234.0981859118,
                                                                            642900.8858503504,
                                                                            569695.2548029621,
                                                                            901497.8113608857,
                                                                            631573.9064808908,
                                                                            570036.2100761917,
                                                                            810233.702501543,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɎˈŇŦΰƓӅXǺʞ·śԜǼѪӜǒ03ӊŵğȼʐÏoμ!Ĳɟ',
                    'message': 'цБʑӱĆӯψȁɯ(ˍÞvʛ\xadΉǆŜҔ˅ӟА`иԚӒΕϬȮR',
                    'arguments': [
                            {
                                        'name': 'Ϲ0TͱʘΡƟųĿӺǮόϔӵ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǴƅҬ͵ҫƣȹƌÛĭǵϱʪ˾ӄϰJŚμ҆ʹӝϫˮ˙',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӂҪЁӃY˛κѐ˔ʓʃşТ˼ǷĠэǛҬǎȭûú\u0383ʇ\u03a2˩ͲƲӍ',
                                                    },
                                    },
                            {
                                        'name': 'ɖ¼ΰųŏ,Ŕе',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5258614112303812857,
                                                    },
                                    },
                            {
                                        'name': 'ɲВОҚƯѨԜY˚ͷĵӐɽϑлϬȢșїfofͱӢǈǩEŐԖɩ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΕÅɑԭdĽӅȔ!әÃуǇӡύӽ`ψÝȕϲɁƸʍ˾ǮϞǶȘԚ',
                                                    },
                                    },
                            {
                                        'name': 'ȈҬ¶Ȝ\x93¼e$ˮÉӃˤŷШѻЏ\x86ɹҰə˕ǥѺßҨĂ҂ð',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'āМŁǥŅСΎȬʙЈɮȆF\x9cƚʎѳзȅŪԙЍUʭӧǶΫ˹ɔϥ',
                                                                            "ċϿЂɐˍԖӐԮ]Ò0¨ÅϨŴ<ʖíΫԦÚǐЉӟ'ΥmӼөԔ",
                                                                            'ǾҋɓŃ\x82ξ·ͽÚɛǛÌ\x8bʒӁѧːŨïоǭЄτɇĐӂǲϊwѷ',
                                                                            '\x94Ǟ¬Ϫö®ŏΉ҆ѯ˸Тâɋʣ\u0379ϧĮ#ϝғӛŃϠ³ȶřʨȵś',
                                                                            'µҴƓĚ1Ѻ¼EмȲǡĴόʆҔʝӜ\xadԉĥ\x81ӡЈɉɼǍɆİӆİ',
                                                                            'ԫǇȠʐԌӖȄ¾ʫǥ)Ƞ+Ɨҁ\x8cļӃɚСϚʶʲċɨŬƞŴŔҮ',
                                                                            'ӐɓɄǧ˭ΗŨΏΰdтÇΒÕ¡ȽťƂѕѲϨБŧеϒdƁ\x84eͽ',
                                                                            'ȒĎЏԉɠʘȑ҂ʈʞŌăɼʦ˖æ҄ЬeԧʀҮ˶ëɝʙҷÚǠç',
                                                                            'ťҟÖЉи\x9fϤӗʝҰЋƙȽ¹ïҸξΌGӰƢϐтϼϕÿҡƺȑΒ',
                                                                            'ѸǠȎÉƭnӬ\x9aȴářΒԛΒǵԪɬÕȸҍԒӃÌĕ7Ͷҗĝηd',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɟˣȒъ7ľҮJǝˑǱ%ŇГa',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4141249695409694241,
                                                    },
                                    },
                            {
                                        'name': 'ђҐħżƤȟśʥͿʛ\x9eÈΫӊ҂їơ˩Ԛ¨¬ͿӇԭǺ\u0381Ɖ»˱',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            104418.8325741165,
                                                                            588919.582427485,
                                                                            -93610.6634600819,
                                                                            94759.61773000823,
                                                                            -7801.411095211006,
                                                                            984276.5437483226,
                                                                            177595.4176271443,
                                                                            933696.3385554493,
                                                                            150316.3237523758,
                                                                            105092.64670343709,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˰ҝԎǀʦſ²СǋȑŲѷ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ªΒϊϨϐΞғθϼɾ˾ȱø˅ψʖǬȹѫӗԮɐƸʶƠǿǼÆųΆ',
                                                                            '˓ǖЄћγˌ~ӽ˲UʺВҒǹңϫӐΟϑȪʇƕҊȯ´ӆĜΒƳo',
                                                                            'ҔжҞ\x87ӳΑ½;ӞÉĻɾӀrßДɧԦΏӭɔƹЩ5ӳԆ˯ċĘϥ',
                                                                            '}ȉΔĶԃҿͶϯ¯ΞċӢ\x9eŚ҈˷җĶŀ˙ǓӻĨýљòƙͰтǡ',
                                                                            'ɟμҐˊБ·ғ\x9fë\x95ɁУԭͼƥǉɀΈmƍϯȄȤˊȨЎЅ|ȢΊ',
                                                                            '¯ÉϡŶǑʬĠШύƮıҿȵԉõ\x80ϻεˏÆʢӫШγĽ\x97рԃΧĨ',
                                                                            'ęбËӚɊ·ˆƣÙϳêzƍ\x94\u0378ǨʧŨʣѵӋӚ\x80ϛ˹ԅȄuхӋ',
                                                                            'Ӽǉ:Е2ƃƂЍƻԚȒѳ˱Ǝĉ\u03a2\x96ѓLõƒǯÒä͵ԑӮω{ă',
                                                                            'ſӋ[ƣчӬѯȾŤʈӖɮŇ҂νѼӷ-ŢÿӓƯʰ\x83ɶӽνȝӿǆ',
                                                                            'ʡѴːŰʙ5ӕñ"ҤɃǘҚƍßˈӣԧˠѶzʝ˭ҩɼǧǇάщ@',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӑԄί',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "ҦӟŹӷ ȗεǺФ'ƐКƋȇϘÔӥТˇкΖ©ƴ{šǲfʵȥӖ",
                                                    },
                                    },
                            {
                                        'name': '\u0379ԕϠßʳžƷӈ!ЎɲтѵƭҾȪЭ˱Ӗя®ˠ˨οԈȵĵЛΧР',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220037.611378:+0000',
                                                                            '20220523:220037.611459:+0000',
                                                                            '20220523:220037.611535:+0000',
                                                                            '20220523:220037.611611:+0000',
                                                                            '20220523:220037.611707:+0000',
                                                                            '20220523:220037.611782:+0000',
                                                                            '20220523:220037.611857:+0000',
                                                                            '20220523:220037.611931:+0000',
                                                                            '20220523:220037.612006:+0000',
                                                                            '20220523:220037.612080:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ǯê´ѣØцЛǛƶЇȫšʗūʖ7ɸ҆Ō˶ļЕ\x8eԣɗǱŽȲɡԡ',
                    'message': 'ħӏəӛũϖΔͰƅ\x96ǵƸˈɃʗϱš|˨ŌϹɘũĲƩӦυʢd´',
                    'arguments': [
                            {
                                        'name': 'ģȌěĴǉӝЍґȕɨ˖Ǿ\u038dɁĔWҏÆȧăѾúϫ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ûψʆɒ\u03a2Ù\x80ǻɵĢϙƸüɏɲ˞Ú\x81ӏƩӼϑǝ\x82\x8fĀ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2223287105515323343,
                                                    },
                                    },
                            {
                                        'name': 'ŕɶҾцΒыOԆ"˼ҟЩӱƁ˾˂πɭ§˰Ψ}Ϙ˰ņ\x83ˈоƈɏ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -70296.98980056623,
                                                    },
                                    },
                            {
                                        'name': '˼υАǓǿхy',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɷğǠƕԤ\x8f˽ØR®˰ҡɐϞˤʡӉɅČӾ\x98ҙǛǥåʍ«QηƢ',
                                                                            'ʁɄĽhЪʴтҖѓѻȔǽиЫŜȲÁfяɚǧćЅщĩʟʑҕˀΨ',
                                                                            'ńѠϨΝ³ȟƅьčſǖǾ5\x99ǡэѣѤɗÝʀøɐɋ.ǁңoԖԚ',
                                                                            'ʏǳѭЁЀҷҌĲЀĵʻͿ÷ϓˤȡǈĐƾĚОĶȉŮ\u0381ű˄ѻɗĵ',
                                                                            'ȋņ˽ϞɭƌFɹƬŒȧ\x84ӿƩɮ]ƒГǤȮͳƏ%ǡiŘÉјƏū',
                                                                            'ʐӈҖϙіѯԏHĬÇрҵюѪҎɅǞҫ<ƹΒѕЁхӶyԥϾǴӒ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'љөɸ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˋԦσϝpԮѾȻƘďǺė:ҔόҪŷѤЊҙĜǊ\x97ÔWʻȆȹǱΜ',
                                                    },
                                    },
                            {
                                        'name': 'җϒ&ϘÜѧ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220037.616537:+0000',
                                                                            '20220523:220037.616616:+0000',
                                                                            '20220523:220037.616692:+0000',
                                                                            '20220523:220037.616768:+0000',
                                                                            '20220523:220037.616843:+0000',
                                                                            '20220523:220037.616917:+0000',
                                                                            '20220523:220037.616992:+0000',
                                                                            '20220523:220037.617065:+0000',
                                                                            '20220523:220037.617139:+0000',
                                                                            '20220523:220037.617213:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Řǖίӄѥǯ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 500168.6502343423,
                                                    },
                                    },
                            {
                                        'name': 'ӏȌ¬ƢȗɀmĄΝǲϢȾ}Ӵ+ʥυԫӾɬяϐЇј˸ӝɓƐǅȣ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 994858.2404904745,
                                                    },
                                    },
                            {
                                        'name': 'þӦ¾ήȦʱ˘',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220037.618838:+0000',
                                                                            '20220523:220037.618918:+0000',
                                                                            '20220523:220037.618994:+0000',
                                                                            '20220523:220037.619069:+0000',
                                                                            '20220523:220037.619143:+0000',
                                                                            '20220523:220037.619217:+0000',
                                                                            '20220523:220037.619292:+0000',
                                                                            '20220523:220037.619396:+0000',
                                                                            '20220523:220037.619472:+0000',
                                                                            '20220523:220037.619546:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΜªÞԁђӬȂϽŦҴӮҭѦƏǇFǟ4ȫыOԎΥˬĪқ÷˞Ûԍ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϐBΓʷξǗɩÏόːCʱϗ(ʟȟӱ˭ȟzǧɞԄƋǍԆϬ¿¡6',
                                                                            'ӗ\x9aԙɩˈɶϘф˓ΉʖɩǮPδγϒсͿͿϾӔŸǴӾƝźȴЫ2',
                                                                            'RӡԦȍ\u0381cιˍΆ,ϒŘˋƬ³ΈԦкʔҵǢēÃʁ¦ӬǟŗҤ˼',
                                                                            'ľбѶϝϕОŌЏɧɟɪҪĪԆəƉʰʯҽɵϳ\x92\x9bɀnӹϳíͰʿ',
                                                                            'Ȭ%СҥǌŒ\x99jƶЧˈʫďϯ2ǳ\x93QƤĘϭћИ£ľƦ\x89˜Іч',
                                                                            'ӑɖǎҪʮ˧lÂÍÒԤƏοϱьOӁ±¬әûѱҰɒ˰îʭSԅ\xa0',
                                                                            'ʖûǬӼєQɍҡďēξϖѳӢǧεϕŶʥ.˵æĊ˜ŒøƳΉJʴ',
                                                                            'ŉӓɚƲĀͲ˽ΰλ§ČҤʙӶżŗсǰʑɀԃӍГʮʖ±ϩǠ˜ȳ',
                                                                            '®ʯϑ˲ϗPҮ͵ƠÈҽѭʛΨaыƈѬМ\xa0ǫƠʫƸ\x81ɝрã҇ƕ',
                                                                            '\u0378ʽǲǝҴѝľ©ͿУ҆ÍрåŀˆƢӎҤƽӌ˭ѸЦƖϨԔӽҴѲ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԌЧȀwŨΒυҚƟѥ½˻ѴəʪǉϼǮԜԫаƢѠϢǪϡĨǋȅȐ',
                    'message': 'ȳћͿʆϋеʑţŌ\x99ϥӥɐǨȥɿãВӲĨϜ˖\u0382ŮѺńӣ˭pʟ',
                    'arguments': [
                            {
                                        'name': 'ӥŜǆ\x80YÂэņ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĎһƅqЗͲǹϐţȒςнѳ˱ҽ\x9dˉ¯Ĥ\x96ğѐԥҜƣˮЫˊŒЕ',
                                                    },
                                    },
                            {
                                        'name': 'δƞȄÉūԂӷɮДд»ʝƊщƥƆЊǷţӃƘ\x99ъŴӑƜpõǨˏ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2781849707800928941,
                                                    },
                                    },
                            {
                                        'name': 'ʣСˬϹғjԢǰnŝσŅšˢϑԊТūƌϓƒěʈďʔΟšnɐԡ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ēȓзΫˈjþǚʷƕ·ҺÍƦɈÅţăЌѲЧ\x83ʪñ˛ͽZΚ˖¾',
                                                                            'ΐŕӸǦŮĦҕҊ¡DȚѺŻɀљʭǉʿЃҶчǍŅӝě«ҠƸκĤ',
                                                                            'ʫ=҉ӎӺńñuˑӥςЬɄȠÌ²ÀȴɄǚĿõνͶĠ ƥƱöȾ',
                                                                            'ѠӳńǢĳmҨϱөˇĖFҒѺÏѽĚČʳҸԇχˇǷНҖʄή˂Ä',
                                                                            'ʓ^ı˷.żǅқѶϭȼӟ\x97ԌԡϟùΥb\xa0ʑċʉϗsǁӶ\x83ʏη',
                                                                            'ЦUҏƩȖӀǪÐýĶƱŨŤʿɾÚÛŵͲӤ¶áɪƦλ\x8eПĚϢʭ',
                                                                            'pƎīӑƾ\\¢ļŃѿҞƞǆǃȴĉ{ŏ\xadʢяźǐĊҮȄǂƯҝŹ',
                                                                            'ʻŅѿΕӓбȂ1λɢɜԚͶĆђΤϴԮɋãӿ7ŲѕǷĥ˪Үрí',
                                                                            'α˴ԠɀȄˊҳ°¦˟ȠОȼȑœϞEϖɰ#¤˭ȥǤɝΗӜ\u03a2ʨҀ',
                                                                            'ʭEԞÀȺ\x85}ϺËʇÍ\x9fãМˈͿˁèɣɜ`αέҠIĜѐ:ѴΩ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ľĝϲȉȽԁŨӢӣɎcǳЛǚΚrУ˴˷ԑԂΦV@ŎȢ,ќӱʔ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ѕɻ\x96(ÂóІűЇėǎǶгĴ\x83ǱͶΞˍǿѽ6ѵЎ9\x9bơ҇˵Ĉ',
                                                    },
                                    },
                            {
                                        'name': 'FЇ\x90ЀȢîԌɢȝӗƘƘБĒΥөφӃĹԗxˏʑĝȱЗёƅƌɐ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'qѫ˽ШĵƈʚƣŞŦŎ\x97ӐȅçԇƳˏ\x9fńǸӛҪİӰʖéLϏѪ',
                                                                            'ƅÓχǀәуßτŭϳ˧˛КʱҥˑʂѓæԐĕjȖćБ\x88ÌʚԌҔ',
                                                                            'êҁђϭÃ¥ʏƶʰДāǰрțӐЈҡ×ͼɄʴьŰԪͼ;ϲǦȾұ',
                                                                            'ŏ¼ť˔ϱԅĠ!ҴĬҒƬYĎńҤƵzúŭǽѕοƑ§ӗͺѝȧǁ',
                                                                            'ЌѮԎŶОĠħПÿӕyáɦđКĚҀҁʩѢƩшȇx,ƅǤ\x8fÇb',
                                                                            'ϞʁκΧϙӌð˥ȭϡéӡԅиҶӒŎϏƳʽϋˤ\x9fϔԐċ˼¯ØҰ',
                                                                            'ƟĺǌӚƽѾԐȲ®˗TѢěЙԂϠңүɖċʆԊԪӌƮҞɊϽÌȗ',
                                                                            'ëǳŪǴ2ƣŐэɣä˻ɼʜƃǴΟҕɦύĺӕβ\x86ј',
                                                                            'ҦӗüȰ4ҿUԆĜʩъȊEʐΠŧƋȭ˺˽ӑδƨϭˬTŎϚĨˎ',
                                                                            "\x9aϚŅάɈÖʙǳɩŧšϕȩӷƶ\x8fÚˋωGӡ'ЏöέßқĞσŜ",
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѬŚɫġКŻ\x936R',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɬɠͱǫ5ђĪîĲӻ\x8aҩ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ƶќ\x9ahŰӦtëķʚɭ҅˶єɐϚ\x86ǏȺ˳ɞůжH˒ϚČԗbҏ',
                                                    },
                                    },
                            {
                                        'name': 'ǯԗϵͷҥœϦȢԇϗţĐƆɕήи',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'νƠɴΉ\x93œΛ½ϘΕϦҪɎŜ¸ԚɰȒӿéđɮɎӮDȌҊϴŸ¡',
                                                                            'ɝü˟žЄ;ȗ3Ä\u0380Ƙӿ[ϟɫ\x96ʳ\u038dɷIǠǕθǾè\x98ɭºқų',
                                                                            'ФȗӺlāӱTХΧўĵƪ\u038bӁӳзˇԔǦ҃×Í0ʻǶɓ\x9fʸ¸ŕ',
                                                                            '\x81Ԏ΅ϜȝĜʫ˟%ȄȰǩʣͷХâɌɾŞȕí҉ɦΛĕɓƙ\u0382Ǟι',
                                                                            '҃ǩĻpǘΠǾϪÝŊԛǵҺÂƊŦoϢǄĂҟϥƃĬӿˁˠƌҗƇ',
                                                                            'Ɖƃ˕\x89ӟƍȊȱҏȲ,ŰĂғͼ҅ȯвɅ\x8fϕϹЏҋχѣʭɽȖӭ',
                                                                            'ĘҘǮϵȀˤ\u0383ӌĪǛБјĜÅћӕ˩ҁӅȑ§\x98˛/4ԦŴȱjʵ',
                                                                            '(ΌÌϓĔ˄яȷƽʘ˧ǻ@ÃǳɆƝʊǡĎҫĔˎϸʤҥήsΟȈ',
                                                                            'Ҷԗ\x80ɖˑzʀǯÒ˭ȧӤɩĞ±éţњôҫʃҕξҊȩ҅Éşȣ*',
                                                                            'ƯѻύoƝèӜǬ½\u0380ɒгҪҝűΒщʒϭӷȎªjаʥѤƴϳ±ʨ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ГȻӘԩөÜƛƳtӇ҂ʐ\x98ūļˀЖʁԎűҹɽԆǐƳ«ϥēЕǅ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            923116.8955157654,
                                                                            114589.96309171064,
                                                                            803765.9852067333,
                                                                            921782.629944811,
                                                                            353998.3374937428,
                                                                            971368.0407900456,
                                                                            973789.8055876258,
                                                                            852202.6684873168,
                                                                            379186.8414221541,
                                                                            197198.67979205644,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƂϜšƳŧĎ\x9e\x8dΐʣѝʘǛ˓¤ýÈЌЮĴ\\Ґ\x87§ʡļҡ¬ӣě',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
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

            'scope': 'info',

            'messages': [
                {
                    'catalog': '\x9fƪ',
                    'message': 'Ɯ',
                },
            ],

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
                res = logging.Error.parse_data(test_data)
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
                res = logging.Error.parse_data(test_data)
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
            'identifier': 'ǓȎҗœĝɨʨøԩҊēѸӢɲmɄҗԫ\x91ҪȨзÍǐŞšǺǷň˜',
            'categories': [
                'network',
                'network',
                'access-restriction',
                'file',
                'access-restriction',
                'configuration',
                'invalid-user-action',
                'os',
                'internal',
                'file',
            ],
            'source': 'ЪʢķŸǨƽɱä\x8fϬèǑ¼ÒʠȁԆɞBԐºůȁɠðӈЏяƌϷ',
            'messages': [
                {
                    'catalog': 'ʹϔƛҢ2oɛōŰĉƵѼ\x8bĚԌɁϯzLӐE\\;ǒϼӠү»Ԝț',
                    'message': 'Тĩ}фÍ˥Ñ¸ǲœɣĥćʊȃĽƟĭƷʘţŦȅ;ƣЮĞЃΧͿ',
                    'arguments': [
                            {
                                        'name': '҃\x9dƳYɓӯ\\ɒҐϛɯĳv',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            979596.6219754566,
                                                                            154289.3471309674,
                                                                            243288.28062683222,
                                                                            199816.8244207211,
                                                                            483916.68731070077,
                                                                            225876.11631247407,
                                                                            993184.326283311,
                                                                            346089.9355409997,
                                                                            122986.97905158595,
                                                                            417921.9307957524,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĪФVʩϊɓЧPʮǖƳȄϣŕϣtӫĸλÖĈŷǽƾэÁӃũ\x9fϬ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʱǠ Ǎʊƅʤљ˛òϜzЧŨʔKPԘҜнĲȱͰĳȫȄːҌȧD',
                                                                            'Ƣĉ\x9aѾʠϑϲԣԘʮo\x95ЇѡBʈ¸ХœǔĜɮǏѬϴĤѕŤ˸ό',
                                                                            'ʒƾΐǱWǵΈ\x82ӽź·Қ¡άӧӡҍŁ»ǯɘȔʜǪùӫôƃ½Ѷ',
                                                                            'ΖɁΡ˭ѾAÉ¤ЖΘӲû´ɘȃԋǵьСǩӥǒŜʞΔďś÷áě',
                                                                            'ЃȬäćɯɠқʡǾhˏλϭӀĝʸ\x91ц\x81ͻˇѣ¼ǎÚHſҐӵϴ',
                                                                            'ƱӏϰЏʸΎD\x82ƣӋͺƎ\u0379еɮɜýМΓhǃąˈΪɲψĽҊˀԦ',
                                                                            'ƬþӺϬǗɢÆЎԋΉԖFáΏǘª˲ƶãɋɄ˽\x97\\ƀʕѐǸυɂ',
                                                                            'ĘеˤʮĆƧʦǨʯˏƊԏɪǸΝЦ˾vȿѴĦəŦѽȁϴúʴʨő',
                                                                            'ʹӛʻ\x7fÈǻΡɞԭɹǑŮʃԗѹzȟԒТʻԫŐˀĴХЮŴƜˠԛ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'οѹƕˍЭǠɎƧħεƺжӃɽ»ŉǗΪĆˤԑúȖӢƩǗԎģȽЬ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϒˑϔ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 83017.99510186608,
                                                    },
                                    },
                            {
                                        'name': '\u03a2ưȡθƮªҼɭҨѠҾȜԦĘѵčĵƹќӰʙԆHӌϤϱҷÿ˼ƭ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220037.693012:+0000',
                                                                            '20220523:220037.693098:+0000',
                                                                            '20220523:220037.693179:+0000',
                                                                            '20220523:220037.693260:+0000',
                                                                            '20220523:220037.693341:+0000',
                                                                            '20220523:220037.693421:+0000',
                                                                            '20220523:220037.693501:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԗΡ\x96ѡ˼ЮԓƄє˺ɧ§ЬʂúϘǎǥäěģˎLŭǞӽƂщɹЇ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220037.694102:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǿə~Ϲ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220037.694517:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x99ȐÒјjϊ\x86ӯ;żşɂ?҇ɔŃȫʢә\xadŁƎͱ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2634383319482455502,
                                                                            3558059406968121913,
                                                                            -6894640286686282964,
                                                                            -7825304237258078385,
                                                                            8286970739829608093,
                                                                            952681287007931682,
                                                                            2853623892900770689,
                                                                            8313194080521488680,
                                                                            -4360346361322971111,
                                                                            -4853476618572072438,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˯ƄŜӡʜщŵӴүНƚ˹шƍ¢ϦʹǆԖТӀͻȰɹуư¸ƫΎ§',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʅˌūǼӺġ΅Īέ¢ˠĽϳƍ˨ɫËε˘ȯǨľȲіɡºΦʵӚπ',
                                                    },
                                    },
                            {
                                        'name': 'ԋѩr;Ũ҆я',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǼɳԇȽςIüмϦϿǜӛ\x93ȭʧΪˈʵή\x9aϛáЍƿĹ®ѰЛGϚ',
                    'message': '˕ʡĐҐɏɪȇƧɶþ҉ŵԂɠıΩáͳʂǆАͺĺӴǽɫҘ˰қĄ',
                    'arguments': [
                            {
                                        'name': '7ԤĬʿͿЎǩȁͲԗȖbҨҟǑөԧѯƲĺƎНΈ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220037.697837:+0000',
                                                                            '20220523:220037.697934:+0000',
                                                                            '20220523:220037.698019:+0000',
                                                                            '20220523:220037.698102:+0000',
                                                                            '20220523:220037.698183:+0000',
                                                                            '20220523:220037.698265:+0000',
                                                                            '20220523:220037.698347:+0000',
                                                                            '20220523:220037.698429:+0000',
                                                                            '20220523:220037.698511:+0000',
                                                                            '20220523:220037.698592:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԫѢýƥʓԖƙюңɚҤӲΓȎŧǥÑŋИǵMʽІѥԍɭԡ¨ɵԫ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            597936.3377783031,
                                                                            614850.3905055375,
                                                                            341910.84491353366,
                                                                            870257.1963388461,
                                                                            211855.33148846246,
                                                                            77426.01669987128,
                                                                            568781.5058027549,
                                                                            587032.4294515542,
                                                                            542284.5094269936,
                                                                            605826.267351262,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɥǎǎēʪ§ͱȺϢϕʜĹю',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 353770.23870544386,
                                                    },
                                    },
                            {
                                        'name': 'PȦÖϮϏ-',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5274256035573302333,
                                                    },
                                    },
                            {
                                        'name': 'ӦÀЌţ\x90ԢҝҒҤ˅`ӆßƜиӂeŤ˷ѻұʙȅҧόƯίz»',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5218023110690828404,
                                                                            231543594837943347,
                                                                            -5867722190654833411,
                                                                            6465915591558579253,
                                                                            -8780746584074819941,
                                                                            -7786252007378485772,
                                                                            -2180377873246039845,
                                                                            8603024634630715214,
                                                                            -2824132137879140868,
                                                                            -5888024088647109178,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'þſҐԣÞЈϝӽӦȨ\\ǂͷʿďɢƐѰӭϻб\x92¿ԍƿċʼƙȣϊ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԏϬԝŽƣϐԐϖдΪɺ\x9eċΓĎҠĝ&ŴȦʈǴÑ˾ʑƖËƒÿ\x88',
                                                                            'ͿŢơёЎȘ˂ř£мώɚӱˌϱ˕ŴљŊɪЇӬɥĤͽҦōԄÞĆ',
                                                                            'Ȓыʇ\x8fğњ\xad\x80άʌ˹ʼ{1ëûԭ\x84ȚʹȨūľɹӈÜcǇԔȁ',
                                                                            'ӃëӮȱǻпƭʿΪʥыƔԑƯȊyνӜΧHӐƇџˤЌȈŢÊӐǿ',
                                                                            'ŖtЦƭŨtɪÙaúˡѦƂθӗԗȒɰ£ƌȈ~\u038bPӒƼìӸƝӫ',
                                                                            'ɲǏȻƆѐǉǊËȹhѹ\u0381ÒˮГԃʼɽoΠϡǉʸiԤɩӆԔѵʫ',
                                                                            'ƿȻėǜѺƐÍʊƏˢӶZɒƣȗǮBҧƛ˃0ЗϢʓNЮҷɘłƝ',
                                                                            'ΊǰЙʯˆǈſ:ЕϷϊĥœҴĜΏ˚ϧƋ\x7fсѝϝˀƿʊˉЖřԫ',
                                                                            'ԦѤæЁȱ͵ϿæERѦ»?ȧћȩˀĦӵȋѽɧȒʳƼїҺұÃɋ',
                                                                            'ЪǀϲǽӚӲʒŇӊưήdňԗϷŻȀǶż˷½ǹӅϹ˹ͲˎɡĐȔ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʲͱрҬӂũԩɏθˇã¾¶ͻҳĝʆ«˫ϰͽYʵŭѬϡŃ_ŏϠ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -86559.58803553229,
                                                                            122173.69338699288,
                                                                            433351.59940509615,
                                                                            673608.797707717,
                                                                            833486.4251606571,
                                                                            875051.482610189,
                                                                            116116.32574053819,
                                                                            584153.2680648164,
                                                                            716855.6090200883,
                                                                            51799.78714046549,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'җ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 343547.21371420135,
                                                    },
                                    },
                            {
                                        'name': 'ȸȸU',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -883699833275989102,
                                                    },
                                    },
                            {
                                        'name': 'Öȓ*ДÁӡɆȥ8',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 683852.7114302022,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԨɕĢρîɋHʆӹŽżƯ\u03a2ʾ¦śˉ˲ʤͼԦΏŽδɭȦȾʃѺ/',
                    'message': 'JżԖЈőͶюΕӠ"ΨЦСVʳʣĉŉȱΧȏ%ƚɶ\x85Ǎ\xadƬpº',
                    'arguments': [
                            {
                                        'name': 'ȪԞĦʴŋƦνж\x8fҤ=ɎʨƓɠԚзTӠȹĪϹӂԃЦǌũɐ˸Ȥ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -78062.40875252412,
                                                                            823407.8407534547,
                                                                            6433.417940351617,
                                                                            940663.7390235345,
                                                                            138057.04400730447,
                                                                            370385.22146545234,
                                                                            590257.1004347282,
                                                                            -90911.6117788556,
                                                                            716716.9451820503,
                                                                            660191.5664469247,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ūȠɸ7dё8Ƃ¦гìȔ\x9eƫӺБĝΎΐøHϋҭUԗɄœ¸ǿА',
                    'message': ' ѠŻǄńɇŬæř¿ǡсЕiь\u0381˚ńϻFȉǍʹƂΑǍѪίÍŁ',
                    'arguments': [
                            {
                                        'name': '½ɾŖ\x87˓ŌЂȭ©ϜɨêȖϸԠęЦk\\ǖҪǅƴGƜɳyåԊķ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ň±ʈЧ¼ǩΫlɌƒӜѽĮȎЀҬɯ,gˎ˰ƢŁRҶҽTͽĴŌ',
                                                                            '˫ѭΨÃрŹòƶˆȊ˅˴ǘăŚѻŵеKčǙ˥ͷŢяɝǝǷΝ˜',
                                                                            'Ӳɿnΐì«*ӤÅЖđ\xa0ҽǾҀ˥ԙɵ˒ʨƁŵѝϳðʮԪӆĢӜ',
                                                                            'iϠƫ˓ӪȀȽʝǧϙǄɉвɪȲºο˙ҩӒҡѩęɩŤ/ɲͷ(ˣ',
                                                                            '3õԮüΗǺ\x9f˒İ¾v/ĮȸĚԤ+ˌťӟѽǳƁӚYÁΓΙΚ\u0380',
                                                                            'ÏӱӔѤϳͷȽ¶ԓ}Ğ^ĳØЙŌŃҭБ½ИӲ\x95ФʉĘōҞԏɼ',
                                                                            'ҞɜδÆƼӗӸťSЗԎƢńöϜLӯ;іȭħԇÉEυԕʈϨӮō',
                                                                            'ϱʂӼʯӕ˥ǏѹКǅ7ɞEҒ\x82\u0383«αǙһΣўЄϒĞħĥhӓԏ',
                                                                            'Ũʧ\u0380ө͵ӒǴďƓøƙӬϟКΆ*мΧȍΧάȌŎʤİǹɋӆϛҝ',
                                                                            'ʅʑʎʰˆƿ˥ɰОKÌԆΝ˺ӢΌʇČËĥŦΖ϶\x87éƾɋƴǿ®',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѕʃʏȐÆĕƍԇӛӏπʨgƄͰǑ˅\x90\u0380ǭȁĿхȇˀэƳ\x9b˝T',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'δĚBқƒ\x8bԚ˫ǌŝɧҍŉ³ŢʹǈĞʘYĎċҟ¿ϝ;Ԩҧ˺â',
                                                    },
                                    },
                            {
                                        'name': 'ΕψǾˆɞʭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220037.711217:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҎLˠʚ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220037.711629:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʺККʨӴɵŕťɼmϢΉͶƙɯқЂɵɣӷÅқ¢ӔȌʥjЫʹԋ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ѽэğsƚНȍ?½Ƕ·ёˇԃƣǳȤҼϡ\xa0ԥϚєϻǊӗӀӾӬj',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220037.713222:+0000',
                                                    },
                                    },
                            {
                                        'name': '«ŔΩƠНƱíĸßЌɯ8ȚȼłҸїǦʒ±ÝѸġˀĵΝƃϥ¹\xa0',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220037.713647:+0000',
                                                    },
                                    },
                            {
                                        'name': '҇ǄϦ˰РɕȓҏʼҢƿдЧǼ˚ʋ½ǍҺȱҨ\x95҃\x91ǌĿɫŵΜ4',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1229202334576496964,
                                                    },
                                    },
                            {
                                        'name': 'ǡƌĮѿԚɃÀ]ȰҫXı҉Ƃȿĉ]Ґø',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "ȃʄΑ˙эÀçlκȞȤƨŋԐüΑ\x94tʐѹώǨÚĠ҄'ģãңý",
                                                                            '˝ԞƔЯĂÚHĪӔʠ»ǼӔȟƶľɅʘ\x93ζƪ˽ʔӆʬõΧѷӁw',
                                                                            'ԉ˾ɔ4ʍʫìТǚșȿʹʾŏшŤɺњłʹōƏ¼ΙìɶԫϫЦ˞',
                                                                            'Ҟɫцƣ\x8dMéӬϴѼ"ɈĀϗӕҘȞˑ\x90\x98ǌёөȟŸ¡ğӾ҄Á',
                                                                            '˻϶ӷͱ˟ǎƞˍԡ\u0382ðțҠåƽƷɀôԦҔϗ\u038dƳ\u03a2ɓѬϥǘσО',
                                                                            'ǨɀțƔω\x84ĢѶĜԑ9ŀΦƃϢӅʇ˥ԝ¯ȨӢЂˎ˥мΛѪŊū',
                                                                            'ƛ¨ԪëѿǠˬŌѾFԗʻ÷ū¡ô\x85Ǧσīϭ9ȇʃĎȗ5ԙȀV',
                                                                            'ԔȺǑѱѵЮ¬ĉʹπjť˅ʴÃɭ¤ӻӵҧźƲţǍˀ-ɮųȺŶ',
                                                                            'ŕΜЃʜɋΑƩƗʝҘˏ˚ʳũѽ.˫\x90ѾЋӂРŚ½Ѯś˙҂Ʀă',
                                                                            'Ȍʦɂϵ®ǲÅԗѠňʑѿƙ˼˨ѽơӊŁћÅǓÂц\u0378νʜʉнΰ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƎЃҠ\xadƧëɔƧ˝ѼӵòήˇԓɞѲɂʒɒΛɕżͶ¿\x84nϠ˒ʈ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 474460.6070511254,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'WĤӉŏ®ȿӡԮşҲӳŇǨФ\x99ΞˆŒʧ;ўҤ˒ѿϓȋжόЍɞ',
                    'message': '4Ìғ˧ԑ\x92ҜԋłȫΙϺ˽ˊȎȂʶ˼ͶіƹʏɚƱ\u038bÌѯÃԧL',
                    'arguments': [
                            {
                                        'name': 'ҙǲԖɽŋƭȚ^ŀӅƌdѽƍĜ;ʑŔHҾџŐȣ\x82Ѯ\u0379ҊÎМX',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 559857.5750890302,
                                                    },
                                    },
                            {
                                        'name': 'Üøſ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220037.717560:+0000',
                                                                            '20220523:220037.717646:+0000',
                                                                            '20220523:220037.717727:+0000',
                                                                            '20220523:220037.717808:+0000',
                                                                            '20220523:220037.717888:+0000',
                                                                            '20220523:220037.717968:+0000',
                                                                            '20220523:220037.718048:+0000',
                                                                            '20220523:220037.718128:+0000',
                                                                            '20220523:220037.718207:+0000',
                                                                            '20220523:220037.718287:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȑ҃ƃƂjҙώ˄{ȧƏʤɚԐϰɢșԞҴƣƴʚøɅ Ԕ˹|˻ǹ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 602003.3761574471,
                                                    },
                                    },
                            {
                                        'name': 'ʣҪͳδӜŎ\x8aƙіԥԂɔӚľȨӶҔЋǚϖș\x9d',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ƒǴтƓˁԠЩ¸\x9aĄnҊҧԮʩɼđӞo҂\u03a2Μ#ԕϖқұ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ǵƊӀȪH6ʈʻҐˢϷʼЯАƬŜÊ¡ҳZѻԙɅzȠȰ˃Å\u038bϋ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3440812148707080875,
                                                    },
                                    },
                            {
                                        'name': 'ϕϓˉΡȜʙʅɺФīƧΔʮÄŏǉƄ҂\u0382уȿːǍ҂ŉƔXŎ\x8eȠ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220037.721361:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΊǓǦ\u0380-ÆƮʓȃǝЬȕǾǳʟľʎşɗЌʥǆčˏϭгůӰ˱A',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            798872.7822881449,
                                                                            600741.0252283458,
                                                                            -52339.90032947483,
                                                                            662179.3380291224,
                                                                            409687.4088820468,
                                                                            673890.6280635215,
                                                                            417062.5155083272,
                                                                            909691.668511518,
                                                                            594438.2018791675,
                                                                            -21058.098735338397,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѧˈɢ˖ϏԊňǞθ\x81ĖԭΰԍɹґΪΝʍɇ:',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220037.723327:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ǆԡø¢êϥԚ¥ŞƝɷƶƁХcӲԤҨŐÂªЧƇŅŵȯήľӐŇ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1349623915863258971,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ġǎʳ¥ԜЍGԅфξѮҒϥåÝʬˑĺҝԋ˧',
                    'message': '>ӛɷɔ×QɱȶӖƁҶһƦʅOӷ4ɞ»Ζń\u038bŦЫĚǵǵ#Σӑ',
                    'arguments': [
                            {
                                        'name': 'ΌƐÕƳȿ\u03a2ԧƫΫ§Ӊ҅Цź<*Ψ҂Ϡ˚Юĉ˸ѱΊ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2069672214556658394,
                                                                            -7658668134055336218,
                                                                            -7782690002393600029,
                                                                            3432755926084279508,
                                                                            2259570977058179575,
                                                                            4995831240570765387,
                                                                            -1640802268403805702,
                                                                            -7106174316350827958,
                                                                            -2398855990488781052,
                                                                            6297290572082194583,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʓˎӥɼɚOҒѺjѕâ\x80ҴҼѹ\x93ŷаnѡÑɍјpǺȈʯ˅ӕ˳',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            551509.6518972842,
                                                                            446037.89435517124,
                                                                            856932.7469508047,
                                                                            792728.7134179133,
                                                                            -75775.25330133393,
                                                                            77465.99968018493,
                                                                            439967.7334937117,
                                                                            883940.8887207456,
                                                                            143130.54128116308,
                                                                            910964.4385549289,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӶƱøˍЋ,Úǜԕ˱ӚͱфДНʚӝӪȞǒÃVʓĎƯʶŮ˓',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8872663665968578618,
                                                                            3796147321793462666,
                                                                            -2234335649428335996,
                                                                            -7965444017000600473,
                                                                            -4855173997180732974,
                                                                            6209436938305665896,
                                                                            5898285021322737119,
                                                                            -5152820787432994564,
                                                                            5176038857650531978,
                                                                            1459170062350834835,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĸӽҵӢːƟӸ½ďÉήh@ʮD',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            277257.03444883815,
                                                                            563291.1226919559,
                                                                            478053.2592210311,
                                                                            223067.3703081063,
                                                                            485936.9380693515,
                                                                            252856.48880204215,
                                                                            902307.6327258982,
                                                                            402760.4919626837,
                                                                            356930.8225223302,
                                                                            165189.73203882237,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '`οӈ\x82ѐ˅Εƪˁ\xa06Ⱥ¼ƄͶnēĚ˃\x92ӟŵϣˠʕʷԎP\x8aӃ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220037.729668:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԭ҈˴űŀ!чҦŌ\x88ć\u0379ǥǓȕ\x96¤ȤǽѓӁǂԣǛ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԃ\x8eQԨɍţфɓĄУǁůvɢšfΥÉҠӇǿЍƍǡ\u0380ЫČːϿѣ',
                                                    },
                                    },
                            {
                                        'name': '»ȱѥ+ȯŸЙę˚ΗӖªº\x81kǊʡcѱȝЍƉ}ҏÒΗȻН˧+',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ѿĬ\x9bǤȺϓæȟϮġɮЙхԩͻŊВәҰӟZ¢ҜŸɴӝĆΩЎі',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƘӓƗ˲љõʐ¢Šѯ\x92ċōƊɾ\x95ģȻƉ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -788343210084949323,
                                                                            -355827363390919553,
                                                                            -8677150245555593900,
                                                                            4768522110894331931,
                                                                            -600385729458824200,
                                                                            -7976888867588064017,
                                                                            -8065444908267278383,
                                                                            -7511027135238317506,
                                                                            -1345665828691509008,
                                                                            -1265119402277731136,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'бŜ˹\x85ƌȟħѵ1ʆ˷ǫӍԝ\\ʕљҗ"\x9bôӥӐήӈҽˇʻǈʰ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ØжĵǓȯģЧ\x87НѭӆѬSϿȾ҉ȯǢÏƹԭҔɝщɡӪǯ2ǥʚ',
                    'message': '_fћÙдwȺɅðŝҬԩ˸ΦŵͻȂęΰɏɃŻЌȔɲ»ųɇ˻ʿ',
                    'arguments': [
                            {
                                        'name': 'ҕҏÉĝΟzǟ÷Ӧʳџзǹϵ\x8aǆťŝǕŉɸʐԑ˸\u03a2\x8c',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ͷ\x82ҼŦϋѬʀȭɜDІƳ˽ƳȺ½ʏʓʲԝАƻ\u0381РјÄlǻœж',
                                                    },
                                    },
                            {
                                        'name': 'ΫȌ>ϻƺɋŚгӖ\x9fʋƟŒŪʍ˭ҎŶbõЪȴлʏǯJ҃',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'СEñЏЗďśХŊ˗ʖgMϱēԊҲʫϖǑƘƤȐЌ~ӏÀɌòф',
                                                    },
                                    },
                            {
                                        'name': 'DӭɏŎ%˓лôΞƘяұǣɈɉ}šΒǧѵ£ȥĸ\x83\x9f˫ϙǙƢʖ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 512396.3990016965,
                                                    },
                                    },
                            {
                                        'name': 'ɕϦôƈΨǿϜɟɊvȀǘӘʏ¬ńɇу8ŬªƆϏѰȱĽоԥѴʃ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȳlƣŎ_χȳɨɝcǈӃ¹Ҳĭ\x91ДqԬȻыƯwˉ\x7fȜҭƎɫä',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '΅ʞμ«ǸOGɊÄΠ)ʜɆΜʞǼ¸ӍӆÎҾӸȊӊͳXԭƞ͵Ή',
                                                                            'ªͳÐζǢďϔϾχӭŰǁʾЏʯŁɗľǀLÒ˷ǿЧϕǫϸ\u0379ɌŁ',
                                                                            'ѢνȌҾлθZǼȑɽƉħȱȧљĉЌ\x8eъ҂ͿɅƬ҅ΊȦҍŝϬɐ',
                                                                            'ы½ͽĐɂÀϡԞΡĠПʴҹӐƭʳ;ǄɖˑȠѱɐȼÆнԀԔӁr',
                                                                            "\x9cɿӗϔ\u0382ԉǻțԏǖTĻѧŴλң'ƏяџǛҀѐɗŶӶ҂ЏzĜ",
                                                                            'ʰɑьǆӹӐΙRľĈɭ²ηĥļ\u0381рПǅҊìϟˎθԖŷâ\xad˜m',
                                                                            'Βжĥϗx½ʝÒŉŞƖÿ=ǝ(ʒʚрΥĊƈ˻ƻй¿҄ӸȘ˶P',
                                                                            'ƶҘѶѴΉԀŲGȻԣ˟КȼʢϋĲφōÍ]π\u0380łʶϤӍ,ʈҌȉ',
                                                                            'ӐĮ˔ΥƄϩҶɒÍǙąПʋѬ°ĻΝÁΝöПʆңƍʎƊĬϴГ˞',
                                                                            '®eФɊ8ťʿϷ<ҋԧӪťƉĎѿ\xadɟźǕƦѿ˩ǵτ2˜ѮѾ\x82',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѱȃ˷ься˪=ПƃÊĕҩУȁưƨѕƬԟƜ|ČǒзӖőԠъɽ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            311197.51716083044,
                                                                            394484.5538220352,
                                                                            271366.3442070795,
                                                                            267833.98511657014,
                                                                            375926.24302478216,
                                                                            756141.9712862098,
                                                                            30459.606122608282,
                                                                            141571.94482610037,
                                                                            572901.7200246844,
                                                                            249048.36907281162,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "DĀԎõū'ǀԤң6˶ĿƝҎ\\ĽŁȌŠÁʎѷà|υœ+ƵŸӳ",
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1545340257795734188,
                                                    },
                                    },
                            {
                                        'name': 'Ύ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1983936543395979576,
                                                                            -2445196568493247136,
                                                                            -871440833669721759,
                                                                            -4471869977331583817,
                                                                            -6869042582968790156,
                                                                            29854878958500534,
                                                                            1694692977799082769,
                                                                            5574736146973356564,
                                                                            -5227843070129272029,
                                                                            -6823053075316635303,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΥҨ˽ҍĿ¥νƙb®ƆƳɹѴńÓӫ.ê˒',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǿԮΝɿԄгшɢԕǬ$ΡÃёĲvĤ\x91ȄӨӉӋ\u0379ĺќјĝ,Ȓˠ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ЈӝȓӍK]Ј\u0381Ȥľ·ЃԫǼȧмʺΡ+Ö\x8aԩҾhӤɶӄež,',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'єԘµʊɎƥҬΓƩʷæ}Д˧ǋżΫͱԝπө\x8cԃOˋʅӑхЯ\x98',
                    'message': 'řȉȖдαҿȳѮˬșҽѡȷÔɒˎЮͰΪˤǖӇԣp˲ʧΘy\x8fϑ',
                    'arguments': [
                            {
                                        'name': 'ǠťȖǰXѱώƖƦϢɛ¥ɚ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5711660307962708312,
                                                    },
                                    },
                            {
                                        'name': 'ňȺɄH<āҋɀςмXɎοԑɳŏӇѥJʵѮĜɶû',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            314793.80862027424,
                                                                            778038.9546913224,
                                                                            351851.954914074,
                                                                            632276.0455548741,
                                                                            894382.3073194071,
                                                                            -87420.96337817072,
                                                                            227344.04784827976,
                                                                            929609.8629983268,
                                                                            16139.02014906911,
                                                                            919485.014951962,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǐǎgǢŚʷČͿσӂӎƒɼ¾ͼǚșο8Рɮʚҭ:ѽ˻ёēǰӳ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "ÕǙΪȈΪ\x8dϠЬӢȼƅȚ¡˯ɂöԢģʾÀǛʁτ˥'řǽΎǐɖ",
                                                    },
                                    },
                            {
                                        'name': '8ʘƘͰ˺ɢΑхƩʾ¯ΘǩҚȹԠΆϦǽ҉',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            675964.8430999508,
                                                                            762081.5595099058,
                                                                            957396.6683469967,
                                                                            -8388.837384602724,
                                                                            565448.9191791057,
                                                                            222152.65530148824,
                                                                            118740.45806542411,
                                                                            386376.3919216752,
                                                                            707609.5835128593,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x86ԟӷԀɐ˴ϣȉÝͼԁҵ˻Ǵ˝Ǧ\x8cùҜ<řʢĎ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŌѶOì҆ĨzÒDƔŎѐƾҁˁϙƎȃ˼C\u038dθҳʧщ˧ЮԄȖα',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŎӾҖƸϝčΘє˽ΊjӼĠԦ²ũ\x98(ӨӦѡ\x97;ŢʙρŊ΄ӕj',
                                                                            'ϚʫΉέCĭ\x81ĂϐτκџaЈqǄїȍѥԖj[ȆԗÑŊӮϋȏͶ',
                                                                            'ɵЍςѥgиƹұ\x86/ƀҎ\x95ΝĥАyʕϱ+ǒvѾɌƾ2<š\u0381ƈ',
                                                                            'ˆφʔȥШǏǈÇɌӦ¿ɷҲԚȕӹBɩλѵѨҁԧȚˬƶjҪԫш',
                                                                            'њϾŻȸ»Į˶ѴϤȧĥ҇Ѓ\x91ԑҎ\x96g\x9fї¿¹żѹʴҧ;űğƚ',
                                                                            'ǅ*ԫRĵʖ˄ʀʾѴɅiʉЩѧ¨ϔɥ\xa0ζƍάԏ˩ӝώҔƖϽԃ',
                                                                            'ɉҭŽʲы\x93ΫúϲǽŢәɑˊСЍȫǼȮ8ͻ5ԆʃλǊŎʧȤҀ',
                                                                            'ҎŰˇд˗ÙʚǐË\xa0δǜɟώHǟҁP\x9b±άï\x86ӦӾӚKҌѰ\x93',
                                                                            'ǮðϤеʙèŹξѣІŐѽĚӎςϥʻĞà\xa0ΤɭŨà6ÄϖѶϢȋ',
                                                                            'Ąӂ˕ĪƕƁƫȈѨҕҸíѓ¯ʭРϨɲƹ\x9fğŀȌϽoΎǀˍͼǟ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ďǥѣрîυʹԣ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 135255.6765287608,
                                                    },
                                    },
                            {
                                        'name': 'ɺ\x8fˡ§ҧ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 476423836707347095,
                                                    },
                                    },
                            {
                                        'name': 'ƪ\xa0ӋÁġļ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            439321.7599179505,
                                                                            578155.3815215325,
                                                                            320684.7378776165,
                                                                            289207.8278056215,
                                                                            521304.7490732336,
                                                                            672589.1724110142,
                                                                            706952.5612922786,
                                                                            130092.4890509735,
                                                                            745327.3137476214,
                                                                            854485.1306793254,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u038d\x9aҋФʣĈƪɝϔͷ\\ӺȤСӀƗþɊʫȷџɥƽȠĒДΉ¬љʶ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7405008397022665504,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ã¶ǇΘɌǬʩáШӼцè\x97¥Ѧӻ\x8bҹȣϝΦˈҪǰӮѓӫʘȍԑ',
                    'message': '˗ŅȘÆӅƢƁO¬ʐʆϛʔ=˷ϹǩŊ΅ҫr\x88ԅ]ȷмƜDøѴ',
                    'arguments': [
                            {
                                        'name': '\x8dԗԅҀ\x8dƶϋgɛΘ҈ӮķƾżJāđѼȸʯ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '}ςȋď1лï ϧǩǚʒȶoǶӐ$mʺś,ʆʗʯîłϽģʕӁ',
                                                                            'UƊǣˢ]ƽэȲѡʸƠ&ÙɭͿЬɷ±ӎΜϞˉϘɵЍ˜ѻǚζþ',
                                                                            'ħρƵʙǤѡĜϧ˄ƢҡƶȦӍŁЪW3ȻңϗӀȃǏƳěϓʺһ˧',
                                                                            '¼ɅǯκL-ҠбөӊҰųĽ3ĐĘȥȲˉŶҿȲȽSқЈԑ',
                                                                            'U¿TѶɹȦˡǪɔ\\ʠĂʨɌūӳřԛ_JӚ˔РÒˋȵ/Œϰϝ',
                                                                            'åȤԃЮԚǽɱωбȭβh˖ǲԡǪǲNԢƬȖѡӎҰǗͰǽɱɔŚ',
                                                                            'ВˡΨˊȍ˞Ќ˶ѷҖΧ\x86ƌϱˇςűɄŖœϘőϨŃэƛëÅĂƳ',
                                                                            'ћʣчɈůП£ʛ_γϋҿΧ4Ⱥ˦ÕǴȿȽʶżʹΧԗȲПϭ˃6',
                                                                            '˻ïҷơǜˌҶȷÏȲњɫΖԢѮˢѸԞѪǌԒºӑ¹ˁƊHϧαȘ',
                                                                            '˟yҕ ƃԌтЁҥҚɾѣĜҠɹɴΓɼ`ұʈԠƬ·>ɾƦƟ\x8aά',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƁǑˢűšϪ¡вҢҺӃÕυ¼ƑнDԕÃȜaвќїƍôϹίǍ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220037.753330:+0000',
                                                                            '20220523:220037.753416:+0000',
                                                                            '20220523:220037.753498:+0000',
                                                                            '20220523:220037.753579:+0000',
                                                                            '20220523:220037.753669:+0000',
                                                                            '20220523:220037.753760:+0000',
                                                                            '20220523:220037.753840:+0000',
                                                                            '20220523:220037.753920:+0000',
                                                                            '20220523:220037.754000:+0000',
                                                                            '20220523:220037.754080:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ÎӋ4ӇΧҼǾґɯ\u0380ԚЍ\x86ѧіѝĠФ˻ˮǸŅÎŵĥɁәźǪǒ',
                    'message': 'ѐŖ;ȜɸŧγĊңҎέ³Э\x94ŏҍÎƚ4ĩiǈ\x81ʫʥΐΐӚƊϋ',
                    'arguments': [
                            {
                                        'name': 'ŐΙЍőȣγѦŝ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            688293.1646704016,
                                                                            580346.7637045772,
                                                                            505763.6031399708,
                                                                            664753.4413152857,
                                                                            666261.7416737921,
                                                                            857807.7440417691,
                                                                            122316.58522134428,
                                                                            528688.8535588,
                                                                            280908.7505599576,
                                                                            222368.34351867303,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʦҊȈÄĸˎȖɦŉȖҭǎ˳,˵Χ(Ҵȧ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʦʿűдȡϲхʣ±ɖΝϬϭЊ˷ƩԐԃȫҨѥЇӛţʲҨˍȫѢʊ',
                                                                            'Ǐ1ř~ÑԔ\x88ԫǖƒŸ±еLҗæĤǀˮʓaˢфė˲БǠĚϦ˱',
                                                                            'ϊҽ\x9cłƧԥ˰DãëБcİĭ`Ǔӌч˲Ø҃ϞҰɹ¿ʒѓȿԈѳ',
                                                                            'ΰԇͳɓVӔȼƵҘĞʌґАɡŕɚԎԝǯԔѾȬš½Аȷʱȹ1Ť',
                                                                            'ΑɶΖѼƟʄ±CŵȄΠʝȎĳĽʮЮõɼ˶ƵқѹƗŦĘΜҝͰӮ',
                                                                            'įĎчĂѮėӥġϰRƛԎϝŚʆƣǔʞġʄїǕ\x8aӮšљʬԊѥ\x94',
                                                                            '\u0379È\u0382Ĵ»ǸæΌę)áºÉϑφͱ˘ôŀÌƾȍ6ɵ°ǧԝ;AӋ',
                                                                            'ƆʟҨȢϹ9ˊѳƔʻИҔ˗ΞƈŢĠλͲϠуǵæÑяѧґθʊũ',
                                                                            'ǄӡƯɹȊԨΆjѣӤ\x98·ϮnȤӽ\xad#ʣŲϑƱˏ˺Ѝɦŝ\x8cʭδ',
                                                                            'ϴĥÃ\u0381Α/ĭ\x99ĿҗӔԗѱMɬɾeǑ3ωɛԔԍǯƧ\u0383ɍǟȬɔ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͼэӾ#ŏǰǟҢђ$ʆůоХΛһ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            682982.0807313242,
                                                                            733969.7176228141,
                                                                            246807.543801634,
                                                                            673230.8458731171,
                                                                            793668.177890913,
                                                                            765538.2021654702,
                                                                            -11970.504332343073,
                                                                            768127.0214987017,
                                                                            14579.344949553037,
                                                                            102258.2677964399,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЙȧƃſЖɑķ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʨѤМѦɜËɓϹơҦϐĠ҆ğ¯ʃƕϣǻ±ѣǽԕАГԈӪϷҳӣ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ʰɹМĎƐΕѽO.ӢȋǴЬ˔ǲödƫǞʜNǍԆ\x81ϏǺπЦӑČ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'òϿçȶʔõÇɳiΚНǉҔԢ˃Ϧƕ¸ůÎƅǾ-Î¦Мϐĳ¡Ӑ',
                                                    },
                                    },
                            {
                                        'name': 'ðˡʤśо',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            848520.0803613459,
                                                                            550503.8519816226,
                                                                            206700.01133766613,
                                                                            857090.422129505,
                                                                            87128.98982500526,
                                                                            138798.8967458625,
                                                                            -59968.98062408196,
                                                                            990602.9001291548,
                                                                            801566.7017073389,
                                                                            886719.2019369595,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ίκϸǉ҇tĎȊƚɯǄӱνƬǎCÈȜϒZ¥Ǝ;ϓ£',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8221807816870865545,
                                                                            -2122374293292745897,
                                                                            8773435578685679833,
                                                                            -1023508029586165398,
                                                                            2535590850696102555,
                                                                            -4964587633941725778,
                                                                            4555697322690890289,
                                                                            -161481051043126099,
                                                                            8547762232456877695,
                                                                            -5589897594266258804,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϮiОwLңƅЀȑϵƛҧļ\x93Ρс^ХɬҝƼʻÚ\x8fFԃʋƋТ©',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -29959.22553803229,
                                                                            636658.9034842261,
                                                                            189363.04166334553,
                                                                            314220.6371684463,
                                                                            603300.6022758584,
                                                                            222888.3527965916,
                                                                            23284.505090091858,
                                                                            290372.12699856877,
                                                                            511131.3890182341,
                                                                            896431.2876440964,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ρȕΝнǯƠȐŎɝϪȃӸԢ\x95ϑţɗșВɲ҂˒ӷň\x8eĵǮİŊʤ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 569575.9772128783,
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

            'identifier': 'ё΅өŦӕ',

            'categories': [
                'file',
            ],

            'messages': [
                {
                    'catalog': 'ҎΦ',
                    'message': 'ӗ',
                },
            ],

        },
    ),
]


class SystemErrorEventTest(unittest.TestCase):
    """
    Tests for SystemErrorEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SYSTEM_ERROR_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.SystemErrorEvent.parse_data(test_data)
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
        for test_name, test_data in SYSTEM_ERROR_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.SystemErrorEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SYSTEM_ERROR_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='SystemErrorEvent'),
            ),

        ),
    ),

]


SYSTEM_ERROR_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'error': {
                'identifier': 'ȔѠƉ?ȴŚьОŕêɲҐћ˛Ĕu®ũϫƈӮЖѤŗ¢Η\x89Έһĳ',
                'categories': [
                    'access-restriction',
                    'file',
                    'os',
                    'internal',
                    'network',
                    'access-restriction',
                    'os',
                    'access-restriction',
                    'os',
                    'configuration',
                ],
                'source': 'иŷѱǷĶʛ¦ƗȪѝΈ©ȚϦʹѫ',
                'messages': [
                    {
                            'catalog': '˶Вɫȟ˾ҥƆmǀ(һĨó\x9bѡќәĉӜɨϖѼƛӃ˴ũȄΆ\x95ɞ',
                            'message': 'ͼϰ˶ăЋŊțϞЬԇϊ;ЍͱʲɊҧћȑǈʀǓϐŻ\u0378ňʱȜĂӘ',
                            'arguments': [
                                        {
                                                        'name': 'ЎΑæӲĲϸʶΣtʜԃΤĄДҸbɛ(ҌÝ˛˸ȫʲ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 497814.04218423914,
                                                                        },
                                                    },
                                        {
                                                        'name': '¼ΑХҙɔɬӾŸʺļ¸ѹӏӆǢ˾ԥˤ˨ЍӨĴǇҮСԔ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'źӔӯӜ+ëŵôżΔө\x82ҡӐԧơŤ\x81¥ϮÜ*ʴcȖŚƦ\x82ţҠ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĩҖЙƤˎ˽',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'т˃ϑhǶԍG{˥ɯˑ\x9fȑΐƹхв¢ѠїЯɰҴÄęѫɯӛγē',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'îȏʯǰ¦',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ό҈҄ƈЌһǗұƀñԈ˝Ӄ\x97L\x8bɬҺΩóҋǢʴӁ"҃Ϡ˨\u0383\u0379',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220037.654431:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŰɭОʌҵӉϟĳӛßƣĜŖԡȕΜҵԀɠĻOÄʠʇCPȱâȕҜ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220037.654851:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Nɧ˾ӕ»Ø¤(ž¤Ԝ˥ϿҞ*ƿͶ¾ɫȇҍƀҀːÔǞȆȭ˶Ѕ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 145282.7337688835,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĪÜӊkʾϳȩҊȷìBˉХˎùZԢȍ¸ȆǌԈƧʀùɔҍҘƘď',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8211723558659281867,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͼȶ϶҇ЙǨŝ»ʝϢӣ7ʽšõɻͲ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ͿҡΌʪѰ˙πйοҒмѾ.ӍŁâϱΆSu\x82їȁʹ˪ѬȨӒέ½',
                            'message': 'ĘӨļjќ¬ȷԀҷүғʘ¥űȄÙ\u038bɋϛ®Ȁðɍ\x9dЈ§ƍˊƈˆ',
                            'arguments': [
                                        {
                                                        'name': 'щ°gɬ˃\x8dű\x8c¹)Ҟʌӝˎǎɭϲˊȝ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ļʖĢɬʩƻӭɌȕσӖϢ˩Ͽ_',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ť\x89ӱʉɓѵФѴѻĵчόĢѭɺTŦȨĔ˵Ηː1ȖȤѮˋɒЖÙ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Υ"ìǏβ˹ǦƧЪсŀ-*ˡԏǎѸѴ˖ɇЖɹʢ˹',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 659175.5231568994,
                                                                        },
                                                    },
                                        {
                                                        'name': 'êƙЗͰӾϔ˶ā\u0379НɆˠɣɁЬԢ3ҧńϥϐȬăʦsҼƨӘ=t',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ϚӓΙѐΫҲ˝ťϰϛſɧÎӕӜԥкȴҘχѪíѮ˸Г{\x90'",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƘΐолӴˋ\x99ɃēКǇɕÝӜ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 479089.79726254183,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ü×дӆΖςѰ\x9aş˪ȎǑɇΞϱΩΝˣԈǎƻʙԙ˼ȧȧƁЏ˚ԍ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϩǩȘ@˩ϬƣԙВĕ˓+Э˸įƫȔԃ҅ԓʣƶɛȎǗϫϣхԩ|',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ąɟ˩mȉβɪZ őˬ˨ǕӢԤíűǎŸҟżƐ˅įǩЄψĳѯc',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2128851525577784551,
                                                                        },
                                                    },
                                        {
                                                        'name': '?ǬюӯȐXȜҴ΄\x88ĲΘϐ˽ʫΟɃԎƿчÓȄƵãӑǨ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѣҽɻ\u0379\xa0ЅӓĄ\x9e¸ŨöȄŕԭɊΨ˱ԐţиҎˉŧŐЃҶƌѭғ',
                            'message': 'ɼɼɽȞԖ-őĥґҀˎ˄]ЀȇѱԠʓ\u038bϕǎȺʉ\u0380ƣɋԈhɛ͵',
                            'arguments': [
                                        {
                                                        'name': '¼Ɖ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 897734.4771569078,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϰʧĸщŦǆɝúʎœɒ϶ҢȔ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΫƞɘΩ˭ʿɎҞԗɱԄŴţƯԁӚŪSѠy',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɉ¦Ǩ˅҃äŻѭ£ȺЎ6ōУI1ӣһϽԠ[Ɖǧ˭ϖ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɇ\x83řȈƦȂФDЅҊƸ÷ӸǟȨ˪ėGϜŅMΩ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΠÚ]їŹȑřԁƍҹ¹ҚϊĜӚɨŅŞȑˮˀɼƋ)Ǉə´ӟȯŏ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѿϖŖϸŽɅ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 944875.1068451038,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x92ΖƚʯƅԣƩ*řԟмĭ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 416267.66094109433,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x89Ѡ\u038b͵ϡʁƭ˵ͺӋHχ}ЄͺЛÇͺīďίōĴϿʸрî&\x81I',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӷѷǼ½žƞԙ+ӟɈñŃɺҾһҏќäƮЪΘέƷĂAϾWȓÃˊ',
                                                                        },
                                                    },
                                        {
                                                        'name': '¦\x8aʹʃʟÿѝЦйѹʁʫԛԞ˟\x88ϖϺɕǵȜ Eʦż',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɄqƊыvҋá-ҸѨЏЦѠʮ˘/Ō\u038dƸӃԒϥĎŸ˺ȦƸɷĩȦ',
                            'message': 'Ѭvҗ˗ȇƏҪÿǜЌӖȧäθӨł{ǨΉǸ³xğԓԃñҵѕΝʅ',
                            'arguments': [
                                        {
                                                        'name': '΄Ɔԙǭ\x98?',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʹϷĶґϜʗȿDёǀȀϊѠ§',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѳԈɀˡ*ʯƘƈuЇo=ãʒǜ>ŊʏˎŗϧȏƌΕdʩʋ|0χ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӈċ˒ƥҀΏˮ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '7Ο\x9eƻȨӽϖɛ\x83',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4460815433706457677,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȘяuÓǔгѽƱǌ\x89ưԬ˂ǜȏ¢ŅǧE',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĈɳĐīєVӹԚŧošНɑÜİеξҝȻϹЫŌМƊĢȑːӪȀŧ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЄɒгŜ҉ąÅǹ\x8eΩțΜѹpƇιЮ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 907878.7045200032,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԁȶȚѺҟɣ/Ñ\u038d\u038b˷üϊNѼȔѓұmѼǺUʑŬϜ\u0381ɢҠDϓ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǯ·ϣɩĹʫ\x85ӅbʮԙOвɲҢĕŊСÁÏСσѫһ˛Ǖϵʀ\x96ѻ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '·Ņóˋʁý¶ʂĝĊӾÒҡĹF8]ѳ¼Ůơǚ҃ǏѮӵы\x80üѿ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѴǇӪƙџsˬѵʗİҋˉ˧ȥԚΌңφɉÉĒδҡÄ-ĪoοǃӴ',
                            'message': '˭ȰӇӒˑʠЩȂɯ7ƋҺ%ԓĺƛЧчȇĬʍѹĴεӿԞτĬ×Ӽ',
                            'arguments': [
                                        {
                                                        'name': '˶ûϠəЧˁɛ,yѯ˥ÇͰȸɀщȶΗԗΓƲS«ϫ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '|ѫŕһ¢sʙɠ ŠŵʗΓӘɱʕ_ӣѬŋ\x8fӲġб\x8dobʻũӆ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɅʝĜԥ˫ȓϤūƺͻ#ZɴĹÁͰǌƺԋѽρƷϸҌĶTΧɞȒȽ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7624085754162999730,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȞĿȵ,Ǧѓ:ēǌȚѸĽҍʢøŊϕĎ҅Ƒԋ˽ҌĆӪċýяX_',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӰŹJ\x9cɻΡϞåԇǨΟǵԋϷuɺʥˌ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǦɃtǥЉәǈĻũ²ŷ˺ʽҽſԙˎƧɶɒšĞϞ˸ñűӟҊǏѢ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ď\x8d!ƣȿɱǜЇÍфϔǴ\x95ѡ\x83ӨȁÔǘOʉћ×ˢįҪʘСёΈ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƘƟ\x96ыȮ+´çҩKчΓΈӱǵӠҥɖϳщʈϫϗ`3˓Î²ţǾ',
                            'message': 'ľʾԗìȟǯԜԚ÷ʎǹ{Ӓ˹ƶµҐ\u0381Ù\x93ϏĴѾΣό\u0380ЈЙΑ8',
                            'arguments': [
                                        {
                                                        'name': 'ΰĪˬʹəұϾԔϫЮ\x96´ɋĆŀϼ-ĪӐмȢȄШ҄r!kOɷ\x8e',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŦҕċͽĥȝĲȳҗƓҊǯӐϿƐɚϳÄж˒εǮϱ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220037.676764:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '8ŇķśȨħƬłƈ£\\ѓ˧ͲǈCƢpʈ\x9f\x8fǔԐȶÆϨģӑӥ%',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѿϺқɳõԧň',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʢ°ŁˬϑλčшµAӃу˴ԏª\x8aӴяɂħƋǟҖìҠŏɌґςƐ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220037.678062:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'нȶ9ҢћƫɘҰ¥ҏόʂɼĨϠǈ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȪԬԨâ¨èl|ҰΑɺбȎ?ѝOγ\u0378ѵřrљɘ.ȸ˃ʈ³͵L',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220037.678850:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĈżȣʳӚпdӁԢǶÖÊȻƇςō',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6184668630119114682,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӚȥEĐüΥӾѴÚÐ˹\u038dΒƩ˺Ĉҕg÷ˆȞ˖ϞЇ:ӆ°яĆх',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǕϹɫ\x9eāъԝԢćǭ¬}tǮНø9ïҊƃ²ˠȧȉϏɐҎȣўS',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϷƏƢӬОĢĕҥϒ˔ŶǦXơþ»УƁ˪Ӗ\x87ɵEćbʀӆЛˍƎ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҒʆªȬͱȡÈ˭ˬԘİόˍĎ|BȰίĨΟΙÙǇʺԬηЫʏ[p',
                            'message': 'ıҳĊϤ˂ѓʁŊ\x8dƧ]ђ²ХνΦɴиƒӬԓРˆµ§ѻΝǸʶβ',
                            'arguments': [
                                        {
                                                        'name': 'ǛϐɲϩϕˌȘҥɰǀ˖ӖñӴɒϵɂϼĳɈ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԅþˤϜʃ}кnԅöƟдżÉʀѣƐΤЖȂĮçɺǖŢŔȂѿԝɊ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɴ`ҢðЌɗƉι',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȅtҒ҇ƲӔԠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220037.682124:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƞʙ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'БƟԒϊңʧПƒɈ˺ůӐҾΏѿãʩƪ˛ÛϳȨӵɾȧfǆȪę˚',
                                                                        },
                                                    },
                                        {
                                                        'name': 'θȈЁƗȜ7Ά~Ƌ űɅûѡӯ©ĢǷɫŦȈÿ˻ҶˏԖˊ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҃ͷŦFʑˢɷbԢ҉Ǫɼʣ©ƨκʅΫқ\xad',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '®^ʝȽ\\\x89\x9dӌж˷Ȣ\x99Ύ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЖӰԊѰ˨ĸŻɑСɲĂ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ІпҼȏіһƆ\x83ŞǖVźÂ˵чԅіЩʩ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЮоΑĩˡæ˂ȧӸyɒȌҎƁƅӹŴΊœȌŻԏȝxËɓˇźǢ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɛŝȞаɵѽȠɆZϝɳ¿¿\x91ĨxǢүɓʚɳԧLȰ®aД·џǬ',
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

            'error': {
                'identifier': 'Ь¿ȡǽΕ',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': 'рŷ',
                            'message': 'ȝ',
                        },
                ],
            },

        },
    ),
]


class UserErrorEventTest(unittest.TestCase):
    """
    Tests for UserErrorEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in USER_ERROR_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.UserErrorEvent.parse_data(test_data)
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
        for test_name, test_data in USER_ERROR_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.UserErrorEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


USER_ERROR_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='user_error', name='UserErrorEvent'),
            ),

        ),
    ),

]


USER_ERROR_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'user_error': {
                'identifier': 'ӉʢӭӚͺŹΚǗȲҸȝąȲҷѪΐɦǐ\x87ǷӗǸѡӻȏɪζ\u0383ΪȎ',
                'categories': [
                    'access-restriction',
                    'file',
                    'internal',
                    'file',
                    'internal',
                    'internal',
                    'os',
                    'file',
                    'network',
                    'network',
                ],
                'source': 'ӁӘϺԤьϧ4\x84ĹҒʦȌĨÓӛΛǵĨʄУюŐӖƃĄϩº˟zВ',
                'messages': [
                    {
                            'catalog': 'фԩθƐŝԔ½ҌΜ˒ůʅХ7ŤŇʎϐƴcфǗԧgLõŷǨèѰ',
                            'message': 'Ɨu\x9eˏńɤóҎќȗηʟ*ŷѠ\x93ːɏ[ùǧɗӛŒϊ»Ǜɶѯή',
                            'arguments': [
                                        {
                                                        'name': 'Ȃƛш\x94Ώψ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŶђǦԨǳ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƛČԡБ¡ΐҶͲ˶ÏĩӋɠԀǱȬ*Ѹԇ\x83ȔTɍÀǇƆĈǚŧÊ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǸӈǸʇɲӨʉǵËƎƾѥǏĩ%ţƬĝÈřѸǰUӦƱiЬϬͽȵ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': "´\x9cө'þȄɉŃâƸҭýˎ·ƶәʬ\x8dϗĐь\x89¾L[ȰˬƕПȃ",
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɎƶćϽǯöÉ\u0383rӟԧƱԃƠpҭɐ˼ѾŁ˾ӮʫͼʑƊξBº¶',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԂǱð?ºӮүͼUŠԣȎ˰ϡѩʦ)sƿƪͲԟjƨ˴ùȯ«ӴÔ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʬљζʫЭԀįԡ{Ҩ\u0382ň<ʮå\x9cΩĶˊ%Оĵəϛ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ѡ˅«łĆЍԠ˂ȭȱіǓÈԧҾÞǩӧČЊ҅϶ýӅƎņҿr\x91Q',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǋʲ(ьǝ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220037.772029:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΠΞӉԑƘ\x8fqǊ(aͺөϤƕɹϫώȇòԂǒΒʉ˹ʷj]Ƞ¢Ҝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ſąƱ\x7fήϧЅɋЉ¼ě˜ȟϏӔč˪6ŒЉȁɼ©Ǉϭ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɗўºġ\x92ɮĵğϝЄǼѲϦҩÈѷˀ˘ūôѩÄіƲǇ˅ЈɾӊВ',
                            'message': 'Ӻάʱϒ½ɕʆіſ;ιƒŌҬϰĮƕΌȧÔѿӞĳ˵ĲбmҴҫŬ',
                            'arguments': [
                                        {
                                                        'name': '¥ŬƼѪђʇ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '!ѸƵȊɾȽĆԧԄҒȮџҁȒÄŌ§ʡ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '{У˰ȟŒпūԒUʆҪӺɵĽӗɵğˉ:ΒʎȶӚγ˨ԉӨlΒĵ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǆӚШőʹǃӉʥДĐӄΨ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ю¶ƓɳǟƊģŋǻΠǊѤʛŦϮɫҍ˰ӂ¹ԧФѳĿÆo°ԒӐӞ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 354754.1527365195,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ј2ȳšͶЧĵϢɌɏʅъҗŹ<#өĖɥӂRǡʚļˢȵԌћü˞',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9bƤ\u0379ӔҔǚĲĵԡ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'àβÏȁǧ\x8bѩТ˕ƑΥɔ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038dļɣѮў ˀɧϙɱǍ±ǽϺǫĐϭƎƴȡО*ÍѣӤŇѨЉȃȴ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220037.777773:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'φɤϏʸ˱ǇЂҩã\x89˽˩ÂͽʢǱԅŬϧƏѓʘјЎʶùеĜԡL',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '@Ϛ\x9aȿKϡғҔȭәԂωʠ=ƒδlɳΛŘ.ˮҕөûЀɲӵϽԢ',
                            'message': 'ɝd\x9b˜²C\x93ΓàȹêăӕɬЫʏγ+ρϔщҊɄȢҶKʎĤΏƇ',
                            'arguments': [
                                        {
                                                        'name': 'ЏПGϊÃưӌŎ}úЃΆҮȺəʢЖϸ\u0382ςԆǸëȏƨԩȑ·ĈѠ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8dűȺѯыʄϔ˷ɶƼĞŉЊļÇVͼƲ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ε{˞Ǆπӑ˲ԇшЇǼ©ѪϘȨǛ˻\x95ѧǁǃÊʋɔċŚǶƽͱȉ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "ҒɒЅıёӁȻȑŲК\x96ѯι˝î˚ӹȫԥаΨȢфԃȃѡċæ'W",
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƹ¹жƋИųҳ\x96ЊƟзϮɦƴӨ\x7fӬϻѨǱΚţǠ˟ƥΟɬǒ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɘΖǡІǪҫ[ĖӪśHԃϒbßλϓďô\x82ѐîΨӮͰѨƖƮӧţ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŁΗϥýĆԌĉćсā$6ԚƵǺƖȸȉběӧʅ\xa0ƀ°ĎˌɒŬǲ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǌƛѝӬåī˕ĚGòӷȝ#:їҞфæ´ұԑ˳ʤҴȯҕ¯Фˍϊ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¸жҋӸuξҬΑ\x93Ӎčæɨʒҳ\x98ҀƴҷУćǠƿʿêȰ˸ԎԧΫ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŦԚϠЂκǾ\x8eԊǽԓԎвȇϙȸѱg\x89\x8eґ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˤϲςĞʕƂȒȰĭ\u03a2.ӺǻȘp]ЁҷʽɀƚȷˤӏӖÛƢȆħ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӌŻў×ŵŒ¼gȊӥŅ҂ǡӖҰͲхļ\x97ѶĦƢĎȃǟ˖ωǽϼϼ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'өΔ˕ȥѱԂњ҇ǃʂ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ˉȭӋŶ\x87:˵Ҁ\x9aʬèɱϭpĬԉȚɾ˶ÆĸӋήҊԪт˄Ч¹ʺ',
                            'message': 'ːβȲɱƐөҿϾϨЦύu˗ϞӿʗMǙԑϸϟȒƎЗĢΦʞ0Ҿǳ',
                            'arguments': [
                                    ],
                        },
                    {
                            'catalog': 'EƦʛӤƞѼǷɛωȟ<ˈ˰τ\xadʑƠɟҐ϶ƠԠϱӬƖšʹԠˮƲ',
                            'message': '˨ӄ|:ƨÈLˏϚвԠʔȳƬҿIӹ\u0382ʹåёƩӪɝų\u0381ɋÆÌȲ',
                            'arguments': [
                                        {
                                                        'name': 'ƺũĭĩV\x98ɂ1ȉ\x81ʝϪЁ҅Ϭϯk',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'кӪΦѼɽÂӨ]˷Ԧ-ʕ\u0383e@ѕό·ԑƏЎĢ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѐ±пЖÔ¦θť9ƨɟ\x8cʟȬ΄ШԫǮЮӔ\x8aØSǅNɥŢʭ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ő\x9aϲ"ŋĺˀ\x88ҔĮ|ѧѡҚƯҼҵυϩ˭ΝͰƢħΡ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220037.785609:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʦɄѻhӠ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˗ȓϏǯσĝѷĘNΕǝǛȚʡИÉԣԇя]¨ńãÞȍԘď҂Ԍʩ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǧνΓӢ˝ƒǌˆӁƟÀƔ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "ԅƆ³ÑƼȒɜ±ˏňη'φ5ËŪԘǿŚ¶єϝʞϷ˟$ҹ\u03a2ΏȀ",
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϊ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ə',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϱƢΩϩÇsȧЩɯҢŰʁȽ҅©\x84ԑ¡ɑïʘȠʥΎз',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ÖӹϭȏԜŸѯŜΐ϶τϟƣԪʥȝъƘCҏØϛĥ\x86ǵɦЁǰѮl',
                            'message': 'Ω\xad҄ѠƑԢʍŗǄˢСǝТěϠ҃Ƨʫë҇ŵ¯уήԂҥ?Ƈº˰',
                            'arguments': [
                                        {
                                                        'name': 'ϫτӨ:ОǄ˦ΟΙ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҽɼˢƠϢҽʜʋȠ\x91ÿŽӰπʷΤϙÕҋ¢ц˻ÉѢȽƓ҅іΥъ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 407376.4110812262,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͶЏУΆЂѻԁÛSчԗ\x97ͶρźɋҜԡ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220037.790395:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŊѮ϶ѫѠǳӼƇȐ˕ťƁɗԢ\x82ʰƻϖmΫɖÅƮȶŌłĄàЁ˹',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '[ҤζÀǦѰǩϒîЗɀԘ·^ӯўų',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9eӗɆԬԓӵÞͲǨ\x80ԘёŃ\x98ˏ˸ΙͿӄȞ\x82ΒҀTлаʌ¯Ӛű',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 242985.708110862,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǚ˔ąr\x8f¬ƄʬhӢđǶ!ФʮȾ0ЦШĆԭƒЪļŢÔπҾ\x96Ӹ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɊǯҦοÈ`өŉşƯːĆҼ\x9eӫȃ˰ŐЉɠҴπŧˊ;Ųӟ|½W',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 691027.2513770228,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԜʾҭѨЁϦʀқЉɆKĪʧƧÊʦҚššӄʃÔƈƀψļĨşʡђ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¸ÐԄыȦȒǮ-ԎӇ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 269829.487141215,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΏďӌҵĽUǞɬ-ρǟΨǎDǊέϹ9Ө)ɼԒƸɶϏͳԒľԝű',
                            'message': '\x9fҏЫSȋΡΠԩɏʳɰȝѽΕӬ΄Ӱˈӱ·ρŌԬÖȑʘʓԘȨԗ',
                            'arguments': [
                                        {
                                                        'name': 'ÏˠУğӍԖҤƥ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "кʋ˫ϑìӜȍѹǉĈƦ^'ϯ®сɾҠBĒҌ~Ϝɏľ˱Ϛ§ҬҦ",
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϙӲəЈ˭НѶǏʅ.ŶǵΠȑřΓһǫǊſѣӮǠϷϿČǵҞΣΝ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8958010905898688459,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǇȒƯŸѣǨϹȆΖŋŮëɆΜÂӐ͵,öАǼ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220037.795022:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѓϛ?э˜Ŀ8ɑȋʰĀщĞԉԄӸҲԆƪʗўɎʾΥώλқʈ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'f˭Ͳ}ɘӺʰϧˬɀ\x9a¤ŬPѦДƾħɲΡȇЉтѾ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'òİηºҾĭuːηȺӒ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ě҉ȘԗyӵƁžϒʈҔЬζҲщǆ\x9dɧCĕΥl˵QƸӖƳĒ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220037.796759:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'мѬөķӢ3ʡÌƥcĕӭƩſȦщϥʂǮƽ¶¢ȒÞŒƏϩ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƾҗLЪʝэϻǸǪ\x9dѫȳż˕ȈȊȿҞѲ\x94˱bϬƾ½ʴҺҍ´Ͻ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ї´çȖɺҋȜƍӿҙҥɘҐѩѻχĬьBŬÀŰħƌʕΒ\x9aұƏа',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԥ¡ʮɅĵŢϊ˪ԠҥɎοpϤɓāԧҰ_ӘÓѽԥǫѶĩ»γ·ԏ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': "ÇҪЍ'ıʾɯĘĵ˛ˁҲЋŷҗõϪĪЄ°ĥϣЮŒɶ\x97έψĢø",
                            'message': 'ŰԖъмҊɸɗӦȀɗ2ɕŶȬλ҄æa˕ҺΎҹŶƏȓĮŁĿȈɠ',
                            'arguments': [
                                        {
                                                        'name': '˗Íϸ҇ż\x90ɈԀʮ\x9eNȠɮ\x9bǍПӮсѣſßϭȒeϞé',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '/İЫϟϢØȋȣĬŽҮʠ\x8eƢԓ\x8bВθ;ΔϩɂϙêԭÞõšΡƄ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'őǸ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҮҜӞЖѝȐǏǍȏԙ^ӜųʒʺɗЉСĄΡŖɐ\u03a2МϑǈѯЪƟǉ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӜȮ˥ï΄ƙтЧRϜǇşñǥǐѦɿɬжſƴÆӳҶӔӱϩȄƵЖ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ő\x9f',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȳȶΕ\x87ˠПňʂò®ʅμͱČÍʹ˔ƣÆʖ˹ǲ°ǘƿϟϯˈȏ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8049070668327004734,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʣОʎĻԏҍÍӸ˔ęȁǠɰψōξǋϽɫɻЋτɝʎӇŗѱˋ\x83ѐ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǈυҰҙԛʎ*ЀӴĵҘɑtτ\u0380Źӂ\x89ϩϥѽȞƂ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '|˚ȐĒʋŨǿǖσԔƸԊч˽ѨƥpkjԄЀ϶ϲѧ<ǋəĵІӶ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҧ<ǔσĐɅӊԬ˧ĔŻԚ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2033419184528411647,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŘeнԥļñӠΤϱҕƀҽɡϽàАëÝɍр¶ʦƵъӀΞʊȎǏ2',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 267314.82472803054,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѢÍƉǛѻŃƸʓÜĐˢҥJѯһϙµˁúáϙңѴɄѰɜǜď˪$',
                            'message': 'ʗʏƣȪAŞzϘԧ˧ΡΔӝΦӽІ*ˇȦȿ¾˥ƕņǅčЄ\x80˂Ͱ',
                            'arguments': [
                                        {
                                                        'name': 'ëʑјӀĒіȰƘƖ[',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѣѰíƞЬǺρ\x93\x8dϤɔZҭ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7808795630731006334,
                                                                        },
                                                    },
                                        {
                                                        'name': ':ϒȄʛ\x8dΔɟͲ҉хxиƇɛ»ʁʋvˏƉӈʡNϏǗǘѢ\x97җ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӝӔġ˲"¸ȲΈ\x84˜ʜ[Мūɬ˱õŃȍěӮɂǅќȹ\x8aԮÔʪΐ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȫʺФƹϟϞėЉƆԆԜÔŖW˕șŋʔћӝɤāҠÓҩƤǎӶʾΠ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƨõԦҐ˕ӡ\x93ѕƋVǡά\x98Ġ\x83ÐʥєӄΥɪӗɴћGыϚϭэʟ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʛƗ˥ŷԏѡӿѪģɜȶąҺųȕǢҚXҘͱbͽӱƈ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʡʉʑӽ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6507745088059297854,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӳGƗЛ˔ť¿Ř3ӐˈīϱΥɅȩȝ:ŀãТȒЁΧâȈŜȔєȺ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 576934.378872097,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʀʶ#Ø҃ƣŷТɵԣя²ɵҟԣʮцǃĖȸß«İA©MΦӷȸİ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1449446685050234666,
                                                                        },
                                                    },
                                        {
                                                        'name': '}γЖΑ¶˳ТҗˊӻÿŃʅĭ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѸϳÌÐȭҘϊ6AƔϳђѷˣϫɬçόЫɀý4ƺʼюͳϱĮôМ',
                            'message': 'Ô)ʢ"ӣѫÿҭĹ\x8cЗԞŔĿGΰԈʓϝӗʰǰ\x97eЯԤþŬȅ[',
                            'arguments': [
                                        {
                                                        'name': 'ІȬӘΕϘΟˈӟ\x91;ˀҾ˟ɘ˄ȅοѸ\x8f˃˧ҲӡТĿͲΏƗºʪ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˤϽһβψҰ¸âÈƕŊʸǰåʧαȭơdƿȾζ1ǰŨԠԤΈшϕ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ˀŬΦǴË˽ЍϾӗ\x98$ʆмǡԈϢҜŧŢЇǫЍŌšɫǞʓӬ!ɵ',
                                                                        },
                                                    },
                                        {
                                                        'name': '¢Ѻɸƻϻ\x81ӑľǧź^ѺҀĆʰʯÒǯȋĂԧ¨Ӧ"ӗlҡȂҡȃ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 255134.13266942505,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԉĪŦ0¸çǓ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x96ɒɼεɒъ϶ƥÇҒҮѺЀȤΤӻ˛ϫѷǛщшáөƴѨ˟\u0380ýo',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɘҧ)ĚЉ¥ˈηЫ\u038bȫӿϥȗʠӌǯÃѬ±ǨϥЂġЩėШˉ҅:',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 178303.65706625907,
                                                                        },
                                                    },
                                        {
                                                        'name': "ϡFƈO'ÂΟʄ˜ѹҼȉ¹ƘԀƫɪЩȲ[˽÷έȟȀ\u038dĪӟ",
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220037.811268:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƨɯġ\x9cϬξ˴јƌзӾљ$ԋbĬТůĸ·˰Ӝѭ\u038d\x96ҾԄΜįɠ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ųяΪːǉѥβԧҟӏʔİԙЯĞśűʲ͵ѣχȰЉΪӟҧɟʸDω',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԗϷȅȊǉΥǆӓEɖӼԛƠǒʹϰÖ\u0381ӱҦΖɾΨǖ\x96ǮʬŚʯ"',
                                                        'value': {
                                                                            '^': 'int_list',
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

            'user_error': {
                'identifier': 'uǠҾĤȴ',
                'categories': [
                    'file',
                ],
                'messages': [
                    {
                            'catalog': 'ѮҪ',
                            'message': 'ſ',
                        },
                ],
            },

        },
    ),
]
