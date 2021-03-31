# GENERATED CODE - DO NOT MODIFY

"""
Tests for the logging module.
Extension petronia.core.protocol.logging, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

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
            '$': ':ŗϡѴľǴȠϊhƖԫuϷ\x96¬˦ώȓ¨ƟƯЩӊŻȖϨʫͻѾЏ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 2410856010327678879,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 30630.533245723695,
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
            '$': '20210327:034631.884492:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ϐŪµǊFκϪСf3ɫƏɓыђTКҥΧҿʁqĥϿż҃ŒŇӻԮ',
                'Ñοг˨ɽĒʁəŶΠϘԊ˔Ȥ҃έƹ\x80ȱƒ/ԁǄȢˀϱάўĒϒ',
                'ѣȺÉˍLºЌӰʲҦųΣŽʯɿq\x9cѕƦɾƍǔɳŒɋŉҵʚӛΒ',
                'Іҥ˷ѪҎπѾ\x92Ȋǆӓ½ˇβԘηƢàûϟԏɺҁǏĻӅͱAεb',
                'ϹfŦűͽрѱɚѰНоʋÉɅŻɦҏƤϲĮǃцҢЄҧȥӭɍҴπ',
                'ǷûϤ²ɶˎ,ԆýǹʄǗӉĈʾȫλ\x9bƐĀŜŌҮȴɓѢǒʫjɐ',
                'ƆӠğƻГüңȢϙӻϸΎ\x7fʟҮȊΓ˻ϣ͵ӐҠӵ\x8a:ѬĚҎԊҡ',
                'ƒɜ½\x9bѭvŨķʨƅϾԄŵΏԎÅѕǄԠƊ\x94űȭӠƲ¼ͶÓċĪ',
                'ԉѠWŏЍT9ѾŢźҊϩȿµЫƱ7gвΓЎӇŀΏҫӿȪΔ˔ã',
                'ƱΞJʌ\x7fьңΑõɲȺѿȵϖєˁԔˈ\u0381ӢԧγѬ%ǥƝ\u0381ДɼĆ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                8584830330168236622,
                -8887463594575963851,
                -3529453679680465687,
                536274236653052102,
                -4702449622527742164,
                8795424144635413788,
                6027777303990146775,
                -7757949191894185483,
                -240939638023395231,
                6333057315726727592,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                -75688.0400855269,
                20126.04379709893,
                16357.238369345068,
                297323.7163988614,
                616647.015680034,
                -31123.197556874045,
                78268.66171882884,
                805975.8886316306,
                459029.6889158579,
                911626.4300397978,
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
                '20210327:034632.885353:+0000',
                '20210327:034632.902129:+0000',
                '20210327:034632.919059:+0000',
                '20210327:034632.935801:+0000',
                '20210327:034632.953022:+0000',
                '20210327:034632.971064:+0000',
                '20210327:034632.988231:+0000',
                '20210327:034633.005398:+0000',
                '20210327:034633.022373:+0000',
                '20210327:034633.039004:+0000',
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
            'name': 'ËǑĚ\u0379иzπlо˪Тĉ',
            'value': {
                '^': 'bool_list',
                '$': [
                    True,
                    True,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    True,
                    True,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ҵ',

            'value': {
                '^': 'int_list',
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
            'catalog': 'ϓÜΪ\x9aY\u038b˰(ȋŒϲйʟ6m\x96ѧ7>ʟӺϼñНɔғǒȱʞÄ',
            'message': 'ǢФŚ\x94Ή¤΅МΈĉtĵȗӳȒиоӖɃ˴ƶДғӿ2ЖĂKѻ&',
            'arguments': [
                {
                    'name': 'ӷÕΔЈʖОє\x80ӊȔԆǛʧȀɥƭѩʈʷÇҺ§ɘԛӁԨƨтҌɡ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        837733.699348631,
                                        261923.16891236865,
                                        526178.0458503934,
                                        638224.3793206246,
                                        364038.1574644939,
                                        957559.8370412595,
                                        284929.90379604517,
                                        96115.48682147212,
                                        555515.2966237247,
                                        292796.4950611073,
                                    ],
                        },
                },
                {
                    'name': 'Ǒѝ)ÊÂӈΪƫΐnӍĉɛїЍʵҐǢĳŝҚԖѐΓӴsɢϋП',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'τхSʯʾШҝªÇɠФêƑ\x82ÄӚΤҵҡƥʰÚғƬӶĴ\u0382\x92ǚΤ',
                                        'ͺӇѣŝǤљӇɰ˹Ńķ\x90҃ȈƓǇ·3ƃȵҌήӾ0\u038dϨȾΓƗʹ',
                                        'ȦӤ\x98ԭЙDлŶ\x82ǈЦÕ\x9fÕºӛ²®õΜàÑχYɣǃҚʃѧВ',
                                        'éӝɕŁɧƕϙӎ<ж½ȌҞŨκȘ\u038dΞƀ\u0378ɵϸüѽϻȎӒԠŝ¯',
                                        'ȭӰԍǼЋα7ȈϊɞѰʈˆʀȁ˗ǽ÷ǉ·˝øñBļȖΫԙaҖ',
                                        '*\u038bŻŅҪХɧӁƵ*ҎԊˏƌ\x9d\x7f ӿϭ¯,\u038bŮȤшȉǋɄɿЙ',
                                        'ҕԩdȋ҇3πuʏνϯԊ9ŏмŋĠǮԗƬùӋКŰήʹÝƅØ˷',
                                        '\x81їʷӱyŭѪŷ>ɔŮƘ0ӢʻψȔЮэƔлƗϳʃ\x9cͰ\x93ȋȻý',
                                        'ǣшΕҗŔŧʸŔĠӉԥЖ7Ťаϩӣćk˦ŴҮАԛЅK¸Ɩͳʳ',
                                        'ʠ\x8dȭŨʍџЦͲŎҡēЃҮǙυȚšϗԞ҅ɃƭәȹϩpʽĈľɽ',
                                    ],
                        },
                },
                {
                    'name': 'ǳπɂɕȯέòƪ',
                    'value': {
                            '^': 'int',
                            '$': 3471598462976910559,
                        },
                },
                {
                    'name': 'ӄхɺbŵӈǬċ˩ʣɾʡȧћѪ±нɬʪťŲǊș\x8eлǆϔӞȞÑ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        False,
                                        True,
                                        False,
                                        False,
                                        False,
                                        False,
                                        True,
                                        True,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'Ҋɜƀ\x89ѩĵҖʅâόԭʄòάŕæȩεФɴΊ\u0380Jeʄ+чƳøΰ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -8804802772803845147,
                                        -460475155305441104,
                                        1495903564605481368,
                                        -4221221117850442896,
                                        2310117678148871587,
                                        -7460195247264645707,
                                        7785639585915758710,
                                        -7437899077389949870,
                                        2381114311252468546,
                                        -3262353221426369294,
                                    ],
                        },
                },
                {
                    'name': 'Х˩аǉȢԔ[ĐиʞҿђТůͽąѠÛyӷǸ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210327:034630.712819:+0000',
                        },
                },
                {
                    'name': 'ȏəǶҍǣǧźMǔҹӺIϔМ',
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
                                        True,
                                        True,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ȩʴ¾',
                    'value': {
                            '^': 'string',
                            '$': 'ѸӣђͻƑӛϣεČƛ6ДӖƁˢтӠ&«ǙǴđȟ\x95ǠˮŗҦMɹ',
                        },
                },
                {
                    'name': 'ȥcÐXǬMȿŤҽʟǝʗʧΞ˔еҡ',
                    'value': {
                            '^': 'string',
                            '$': 'ƺěįӫҵɛɫыʽMǿӊӄѵʓӿώϏ7ŐАș«ԤĹQìў¸ѻ',
                        },
                },
                {
                    'name': 'ĬĶʨŬ',
                    'value': {
                            '^': 'string',
                            '$': 'ÖԍτѪҼɴԈÿġХԠή_©ónҤņѲȔêɚȨȯ«ǕɊɎӀї',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ʵЬ',

            'message': 'ʩ',

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
            'scope': 'info',
            'messages': [
                {
                    'catalog': 'Ǫȯ«sХϏΰ',
                    'message': 'ώÛˬӊą\xadʎɜĴçͽNҽϊļҪȻʈҾ40åҥÝĵ\x8b҃ĜƘ§',
                    'arguments': [
                            {
                                        'name': '|˂ȩԃȑӖɋϥˡ§ȬΜƘȮĎĆʛϑȀѨðòʘ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            183866.02890677098,
                                                                            529072.8380241609,
                                                                            990078.6220387351,
                                                                            144195.96519145754,
                                                                            916416.7951824459,
                                                                            590111.5392856983,
                                                                            687551.1966599455,
                                                                            -59991.15099545401,
                                                                            667587.5698636024,
                                                                            828422.2168303721,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǙŌēɄ½ʍɱ\x82ԈЖ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 833637.8101800724,
                                                    },
                                    },
                            {
                                        'name': 'Ŀ˳ЉŠЉœҸɞЫАʲԭmĕŕǭĽΡBɻώԒƅĻ˷ыʡőͼƲ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȖˁыģӘYҲſшԆѬʍЏӔѡǶӲʕɛͻΫҨõƊķzŕΞƆj',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 158412.6850286055,
                                                    },
                                    },
                            {
                                        'name': 'Ӂ7ðþμӋȹŜęǆҦԏ)ēϲˊ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 664841.1190929783,
                                                    },
                                    },
                            {
                                        'name': 'ˏшƠюĂǍԋŞӀ\x86ҞаҟԟƲƺԖϨ}ґʜȖǞϽ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034613.371497:+0000',
                                                                            '20210327:034613.390040:+0000',
                                                                            '20210327:034613.408949:+0000',
                                                                            '20210327:034613.428741:+0000',
                                                                            '20210327:034613.446721:+0000',
                                                                            '20210327:034613.465251:+0000',
                                                                            '20210327:034613.486175:+0000',
                                                                            '20210327:034613.505193:+0000',
                                                                            '20210327:034613.524730:+0000',
                                                                            '20210327:034613.543301:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǁǶЦϿǏЕԖŧ\x96ę˂ɦÊȚʍҾɷɎ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 657285.2671035443,
                                                    },
                                    },
                            {
                                        'name': 'ǂ7ǣ˒ҮȒȂЦˍ¦ņǬį&аĭĥɷӆӛVάĲГɺxʔђʾϚ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ǝϣ\u0378ҖӐwȱĤçɹ҂ʯƆʕʹԒУ¾ρŲϠ¹\x8f˖˾ǫωȷΒđ',
                                                    },
                                    },
                            {
                                        'name': 'ȔʔϤ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '|ȜρЛ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 196799.9922881528,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "²θѨĵӴкũɑƓĂɐŦӠΈǉӐʈ΄ӃĶĉ\x98ƭоӒӈ^ϓ'Ϯ",
                    'message': 'ĿƯȡϒʔө˹ĊƴȇҏÌɦүįԓΣϿґԢɻћ˚ǍƷφĮȜѽЪ',
                    'arguments': [
                            {
                                        'name': 'ǛˆǓ*ʒƅѓxǸԋʥȚѨ÷ң_ԣ¡ɡȝīӦЁԚʻҊǸʁȗ\xa0',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            853671.1361857643,
                                                                            216080.2286124276,
                                                                            430483.6353794923,
                                                                            894059.995929476,
                                                                            50373.059798680915,
                                                                            490672.10948055424,
                                                                            89855.39352923745,
                                                                            440167.1796224754,
                                                                            154087.63157272572,
                                                                            196735.82307555462,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЅԦɧÃ>Ǐ1ԮȖˊÙӥϫ\u03a2Πɡ˚ӘӘΗ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034614.211953:+0000',
                                                                            '20210327:034614.228823:+0000',
                                                                            '20210327:034614.247403:+0000',
                                                                            '20210327:034614.264930:+0000',
                                                                            '20210327:034614.283344:+0000',
                                                                            '20210327:034614.301523:+0000',
                                                                            '20210327:034614.318468:+0000',
                                                                            '20210327:034614.335344:+0000',
                                                                            '20210327:034614.352589:+0000',
                                                                            '20210327:034614.369842:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЊЋŅǛӠҔ\x83˻ƹȵ\x9asͶӼYҁãиĂȥǠwѷԈªҜϟŨыҩ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'ѨĻӹӋɛӠƶɼӑǒҩҤŔŤ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 530100.1683226195,
                                                    },
                                    },
                            {
                                        'name': '_ɦϲӚȳƗńӤļπЛ҇¤ėӐÍ\u0383\x9dȮȭϥљѿ<¦bђЉǫŴ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2581851858950724812,
                                                                            -4920971214567324419,
                                                                            -8064555859835558191,
                                                                            1535113298580312049,
                                                                            1073112761068090036,
                                                                            -5919141597092298105,
                                                                            5243767245244437251,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѠǅӴ!;ϊ)ȈjӪɕʣʝҼºɃȓŹ/ñɟȡŮ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6590822808884748810,
                                                    },
                                    },
                            {
                                        'name': 'ύɮˏˮ«ŏ0Ҝ;\x93ѬlѽРǅˊćΎȆÏþӥƁΛðГˉŁ\u038dҹ',
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
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "\x93ˑҜěƸ\x99ϽĸѲӄ¯ϔˀϴ˫ŢδǴŶfĻ'Ү˚",
                                        'value': {
                                                        '^': 'int',
                                                        '$': 806095668524762193,
                                                    },
                                    },
                            {
                                        'name': '˴ǐĂǱ˸ŴȆ҈ˀÎ²\x86Ò',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǰѶүήӑґ´чʟŌӤʡ˽ԈϧˏʲøӾƤӌ4ĂӀʹ#˕«ʐƘ',
                                                    },
                                    },
                            {
                                        'name': '\x9a«ŗђºǒ˯ɳҲϖƦԂТӣǝēɖгԋҬӆʅ¾љŵ^',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            529244502923622542,
                                                                            -5434291053695262112,
                                                                            -2482189375036409698,
                                                                            -1126704789247800912,
                                                                            1154173020316222647,
                                                                            -3054806797127073926,
                                                                            2299246140610158158,
                                                                            -4991814938033690542,
                                                                            3051720603985095408,
                                                                            -521036503763275368,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȌӻǷǚʍoɨOђԣԈЗƛHʁ7ŭ\u038dοƐЛ¨ǚÙƖȝӻƕ\u038bӬ',
                    'message': '{ǼѤÂŧ\x81˄ϧţǭ˰ɄҞԙ!sÊӭҬ\x88ɉɳϋͱ$шѿԇӦ˝',
                    'arguments': [
                            {
                                        'name': 'ƾϳˊĈŮ(˭ԞҨʿƄȲʽӨǏȎЌĶó˭ǮйјāƧЙșΕЙ\u038d',
                                        'value': {
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
                                    },
                            {
                                        'name': 'uƃĽĺʏ\u0380Ɖ \xadƹĶΈͺǲʃЏ˱ȸŝ$ѮшģТƤǰʥːʫȵ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034616.029165:+0000',
                                                    },
                                    },
                            {
                                        'name': 'åғσgɶͶӅЂǰıЌɡƛ\x83ˌǃ˦ɠ˽ʓÚȉνǫ4нíϼʨì',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 419194.89583388605,
                                                    },
                                    },
                            {
                                        'name': 'ԊԮȩӲ\x97ƻΥї§Ѽφ\x91ÌŰӪ҄ʙϿ\x96ҫҳɢƿ˅Ө',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'yȣӟüɣɍӞǅΩϧŎуÁÀʾŃòбυυˎϻÛƀºΓɂϻʞϢ',
                                                                            '6\x81ιǶӼɖHȘάӒͶͻȩă˚ΰÔŲҦLˢ˄ʮӫěӪʉĝ;\x9e',
                                                                            'ǟȊɭЦϕÌӹ!ĆƘ¥҅ȽȏӚ\x88ѸԠµϙѽΫǟɩƈ˲ѧˬǩѷ',
                                                                            'ŕ\x8eӃν®5ю©ȺϫȂ¤jǪƲҘӿȞӻ˨łҹȱĈq¿ԑɗʡъ',
                                                                            'nʪɸНȏªǛͰɵʬʑѝŷπʯɢȍġөŋԪËƳȺB˓ĦKs*',
                                                                            '\x80ǳϯӖʧғÇǦθǰ\x82ԢěШ˶ÖȝųÉФºѰ˻ʱʳԨğŖ~¾',
                                                                            'ʣªԧΖÍΈú¹ǠȼƻäԘËMƊүЧϞ%āʒǁ"µϭŊȩɲƠ',
                                                                            'Ԏɷ˃ç͵Ǫи?\x97ӐZʴԊӰðτȺѲɜʙǯӛтґəЭǘʪÖӊ',
                                                                            '\u0381КϜЛǫҞǝхČ¹:ɰMҩ¡šÿЇÌҾ^Ąwԣņ˵ж5ɆȺ',
                                                                            'ǼʈΚǳȪ³ϣĆϧŞé҅Ӣ\xadBЮƳˍѶ\x98Ѧ2ʏħ҂ЙΜКƘϹ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɭōбаϿДUӳʣȁƍż҅ęɑϔυ҂ǿȌӨ¹ʝԘ˹\u0378(ΕǃǶ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ñьɲ˜șӛǑХΓˀ^ʮǒӊ.ζʔΝǯ"ȜԭĨζл6řɛƷђ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1352848575560475256,
                                                    },
                                    },
                            {
                                        'name': 'ǥϓͼʵĊκΕҥЪ¶ѕĀӻғʲůʔ!ʱųҹěϪϖáǙϠѵсɔ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8572482595829966581,
                                                                            -1707537192188952408,
                                                                            -5521359121205247307,
                                                                            -4479653861474519026,
                                                                            -214696430672183567,
                                                                            -841730021845246855,
                                                                            5550217105005445028,
                                                                            8385344986927950151,
                                                                            -4418062147260650650,
                                                                            4687876003554515261,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɠϖƺΗ5ϾЃџœʣ[АƔ˱ǡѲΠфɹӾ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 359857.33441654715,
                                                    },
                                    },
                            {
                                        'name': 'ʤӍƮƹÒ/ʘeԧԜǨȪŖ+сŸ3ΑƔʆǙӭ\x88ӈԠ)ʶӑөМ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034617.061696:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʆÎЋҾӦȅʩȺӭČ\x83ˑύĔ\x9dΘе±ƔԩӢ\x83ŬΛҶȕƩŲЏч',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            741906.8141889208,
                                                                            -46059.599211954126,
                                                                            488765.6838053927,
                                                                            270963.2495818267,
                                                                            476860.88426521234,
                                                                            642006.6090169438,
                                                                            -90645.7035842894,
                                                                            545488.3320816085,
                                                                            78541.4162849474,
                                                                            819538.2293873163,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ư;ˀӦȾǙŏ·ȚиǞԝ\u038dωдſĩÕĤĝĶǎ5ԖȑƅԮλá\x9c',
                    'message': 'ЭęɕԓͲ˛ʑы҃ӳьÞԕϸˋΰĕµ«˨үǡΎϑzτԅœˣĠ',
                    'arguments': [
                            {
                                        'name': 'Ʉȥǉ\x81ŘѧźĔ:ɦӎ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ŝ҉ǑĞưν$аҪűɥъȀӊȼǧ_ǪźĵʩˏˉїʴҴÁҪħˏ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6201474977425987611,
                                                                            -2054592191106401776,
                                                                            8954787211418021944,
                                                                            2743394560987865522,
                                                                            -2951632635216733725,
                                                                            5015948981282159074,
                                                                            -4372293654864319382,
                                                                            -4589461723139083401,
                                                                            -8909059773006474301,
                                                                            -8195609594921897920,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʋHȑƄέЁǧùėȺΤςĶҏŢZѡӀҝͶÀɳ͵ҾԚïϑFÌˡ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȾЫőģЦȪɢȑˠDƾͰѵĕ!ɽԪͷ\x89ɇԅtŨƫÌƵǧЎMӦ',
                                                    },
                                    },
                            {
                                        'name': 'óϸYȪƟɒ%ɗ˘ɜ¿ȃϬΜэӒ}аɅXÒʶϷʫΌҧЂӾПш',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7126512985135282976,
                                                                            -3637814946013213393,
                                                                            -5771594135872916755,
                                                                            -2344060940963592651,
                                                                            6981311329328036579,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˝Óȹӯ¥ԢĄǝҩƞĽйºȈҼīѸ\u0383џϑϛ҉šНϯɋԎ˭ǎ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            122341.02684693865,
                                                                            698682.0545728336,
                                                                            328797.1897359534,
                                                                            -72014.65646520001,
                                                                            493866.73964792956,
                                                                            79167.93561534272,
                                                                            -96297.51174515318,
                                                                            297991.6958324248,
                                                                            829294.5034306798,
                                                                            828661.2125375702,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǭˮțɉÇҏƚ\x95ОΧȹ?Ǆι˯ϢŖćȌэҾ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7276041195614825231,
                                                                            -7202837074241538463,
                                                                            3209050597815101218,
                                                                            -7315339036507240717,
                                                                            2663297087158995587,
                                                                            7216415483162897520,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϋ²ʁ¤ϛķӚѯ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x94ԣȍПЊϠѷȅӄЕрӔÃѭ¡ŝȚǈθ҆е\x91ȢkɮӿǚſǇԤ',
                                                                            "ʆĹƈƬǑƇÌrҏяͲĎңƏѿɊ`ċ'ϳʸӜȣΘˋίʹԆwѵ",
                                                                            'ϪӂtɆԓӓδʣӋѠɠýѾŢ¦ŬʝθĲчџԓʜˍϜʯɧʷήŽ',
                                                                            'ϖɭŀˈҮәēğΎ˃ɖƖ®ѿӾϹƩһ©ɫӯɺψҵǩьңΐиԉ',
                                                                            'ôĨΝąҿСvάϟǟɬūΪў³ԓĮϮʚЈѰԛ҂οʯǟɛˑëх',
                                                                            ' ЍÇˎȊìɷȧŶʺӵøʀŁʱȊĽԫ\x98Ξ˃ҥM0κɭʢ)gʍ',
                                                                            'Ш˴ǌƐϢΡ˶ɼłƨ˼ԍφwεϢЅƱȉŻEǮƏȕˑΙƧ~ϵĚ',
                                                                            'ʺ¦ăѕҰќʍЈϋԡпԡί!Uˀȯôԗ{ԭȗ+Ȑȳɭƍɣʰ©',
                                                                            'SAȖҾçȿҋАȿмМԐǂ´ԣɹҋƢůԅҟоѰҫѠԅӲĞ\x8b\x92',
                                                                            'z*ӜƄїϵϫеʕΨɳνƱώƧýӤĴ\x87ȷʛ˔őѩ\x92Ȉ5ȅВλ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ơίƛ3ΔѹχΣδǇөƊƃȼҦtѧȫҥ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4277644869987640104,
                                                    },
                                    },
                            {
                                        'name': '=ǱdтŖÃǒď\u0379\x83˚ЁŴŚҪɯȡƟɌƧшÀӶԕǬåЉǬ\x9d˽',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034618.648740:+0000',
                                                                            '20210327:034618.666270:+0000',
                                                                            '20210327:034618.689216:+0000',
                                                                            '20210327:034618.712361:+0000',
                                                                            '20210327:034618.735268:+0000',
                                                                            '20210327:034618.754600:+0000',
                                                                            '20210327:034618.773110:+0000',
                                                                            '20210327:034618.793712:+0000',
                                                                            '20210327:034618.813213:+0000',
                                                                            '20210327:034618.834206:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'şдҼӎіƍˇȱϖƞҧéƕ˽НBɿƫǝͰЋƕ\x8cҽǖΫёȽ·˭',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĉ\x81¼ƗȌȄ\x97Ȗ˱ҺƳ˳ÄӆĖˢӥ\x98ԝҬҤ^ҾȏòŮūƽȸđ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ЎŏžBÎ\x98ɒɟӯћҋͽЫĀľȊųDЖkɔ\u0381ЙӒҐɩԫƍŌß',
                    'message': 'ĐΎ§˛ρɢɈʡщΟöҙɏȬʍˁɠȰʜƳ˗ԃɶ½ņĹǺʱ˭ĭ',
                    'arguments': [
                            {
                                        'name': '^Ԣȩ\x98҄óпоҔʪЋԬҕEȑ\x9bĄѥӊӀ\x90ǣ\u038b˻ğƥ˨ƀú˸',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӦǺгɁͳ#ˡɑMԉԄԘǓWϷɹӐҌHŵƲӏĮџ\x82J҅Ǆɇɵ',
                                                                            '>άѯĿάƒ¼×ʯʍjѪζԑ˯κΪĞӌҫàɔĄKϜΘşǣƱɇ',
                                                                            '\x9fӞ³ŹɇÊѭςі®ȒΆĖƛМĦǯ=ӯªʂÔωȔϮ˲ȑґΜâ',
                                                                            'IҢļЭҠȀƶŇϋėřɞÎª˾ҢϓӷѐҶϤΓƨÎɑÿŪʗ\\Ċ',
                                                                            'РĭŊɭɑԅÈ±ΛŮю\x8c÷°ΛѧӾԋӋ³чƪ˗ƮѶϫȨèȼĔ',
                                                                            'мUҌɚГώïĐѝ;ҤѤďȻ˜.ҡϥɴ˅ĤԜДКƵѪИɨԨœ',
                                                                            'ªˆɳķƜǈ\x8cƃʉʕũˀàбʬƴ\x82ӚԚÕɰњčɞΒǹԝκ\x99Ħ',
                                                                            'ϷåǢȞ˗јЁ˹ӥĈӤīο¤ƠȈǵсĀ)ıоΉƩ˾ȴ/ЉҮǂ',
                                                                            'ȪğϱƗʋʛͻϖɝьѨȌԂǨϒȜßƶѿȭфӄʣ\x9cӨȀʪǫȁʥ',
                                                                            'hΫęȭӦш˒ǂɉΓˮґȉϗôĵɢҴŋǰΎĈĤʅνηώϠǌʽ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'НŘ\u038dƙeԃ\xadϧǧϞЌŊ˸˹ʵҪʶȽ>şоǡɳӁėԗȤbм\x83',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034619.345198:+0000',
                                                                            '20210327:034619.361923:+0000',
                                                                            '20210327:034619.380393:+0000',
                                                                            '20210327:034619.397063:+0000',
                                                                            '20210327:034619.413848:+0000',
                                                                            '20210327:034619.430633:+0000',
                                                                            '20210327:034619.447677:+0000',
                                                                            '20210327:034619.464610:+0000',
                                                                            '20210327:034619.481123:+0000',
                                                                            '20210327:034619.498401:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˣqĂҢăŒϝы=čα˼Ύа0Јĺқα˽ϐŜ˵ҽ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Êŷ9ŨӢϕǴ²˟ԔʬõĈŦω˖Ҙ2ЈΏ²ŌгΨ͵ĝϹĴ҂ǵ',
                                                    },
                                    },
                            {
                                        'name': 'ҿϮÒєȍ\x8cιҾѨӊ\u0381ƃɶ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8259787742181031566,
                                                    },
                                    },
                            {
                                        'name': '҈ϏFeȈáɡʦË\x98ɀʱĵҷǬѓ\x90ʽɲӚtőӜ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034619.738932:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ώģȼ\x93Ğrŝ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            284874.8201907609,
                                                                            -83173.44870350705,
                                                                            187304.27845412702,
                                                                            680764.0327285231,
                                                                            222361.3098243666,
                                                                            431384.17047737853,
                                                                            725258.4032238699,
                                                                            491656.31694262335,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԍ˞2±ЭɕǣΎžǫ\x93Ұm7iȬǈа',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034620.024813:+0000',
                                                                            '20210327:034620.041963:+0000',
                                                                            '20210327:034620.061157:+0000',
                                                                            '20210327:034620.080088:+0000',
                                                                            '20210327:034620.099275:+0000',
                                                                            '20210327:034620.117472:+0000',
                                                                            '20210327:034620.136077:+0000',
                                                                            '20210327:034620.155190:+0000',
                                                                            '20210327:034620.173673:+0000',
                                                                            '20210327:034620.192517:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӌʭȢқɻ<ԓˣǚȜŷVƏϺ>ŤºȢПɏéӽɚӕʹ,ăΟԎҙ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4613298315110391772,
                                                                            -5324245090538860913,
                                                                            942511636140375536,
                                                                            -755238126698016954,
                                                                            6327626763902940228,
                                                                            195446223833052495,
                                                                            -3528555138142604667,
                                                                            -7454086449429623244,
                                                                            -6664234645946805063,
                                                                            -5265228579093003685,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '©ӕĢʧϹÕȗȋͶĠӤǤƣĎʝɨɢžΘǅźѢȬΛ%ɹԧүɒư',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɂmƩʱДДKƩǵŰǦɖƸʪǐԜɣ9ӑӇíʠɉͿĨƬŐҮΥŵ',
                                                                            'ӭȏρ\x8bč˛ю\x9aƉ3ҀÎ\x9a˹ĩĴ ĖǆǧҚҺщˣB\x87ɻĬ˩{',
                                                                            'ԋƀɍнɡт+ȞŘwłȥÑÔʹ˻ʱɥĂӼѬϸÈԏɌѻԀƀȢǴ',
                                                                            'ʈδȰ¸ԧǤ\x84ӚϊЦћα²:βDӖŎȢǇʍȱʈʂQȢãԞµƌ',
                                                                            '\u0379ԤԄˊӊɁҎӿάЎÏ§ԡȢɵɈāʪȣӱҺɳҼΨˆƧjdκȏ',
                                                                            'Ӄјǰ˭϶¾XˀЪɡϴԄσƤ\x91ǰ\xa0ԪуӤƀǉɓPƮʈ*ҒŐϟ',
                                                                            'ȃǟԩŒϿЊϹʫȑÿ΄яӇπŵȷοĢЇρҙȟɔϯЁЯҝ7(ѿ',
                                                                            'ÅɵϿƦcҷҧ,˰Ȏʡɐ\x98Ό/.ȿȹŃǑſϯӷŀËòʇʾԟȧ',
                                                                            '\x9cΎǙ҉ćϗɬȍzѿĨʽpϡĉÁп"λʘԤǵτńʗˏȈEĲŢ',
                                                                            'ƅØÜŞʧýɲΪϜ<\x81ӳʑǖҒʨŲ˘бW¿ʪĢǡʔˁȼŔðϬ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǴͲƧɨѷГĿǾθǢ1lѵˊŋX!ыɜ\u038dʒĪźԕʗȉˆ҆ӤԀ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 357189.3636183994,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƜƼΚьɐˊĻzĥșŤӭӎŕ\x88ÁȸŬίγƇǱǝɼòӜʉƲŷĩ',
                    'message': 'ɴɮÅϾǩшã4Ϯ\x8fòȦνɭʉƯǂϧʤсǫԭŧΰȶ5öʱɢ\x8e',
                    'arguments': [
                            {
                                        'name': 'ˣϖ½',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҍȄиÑϴƸǂɟйϽϦʨ¦øӰӲǝ>ŸыǕǭ˺ЂӬъŷЫΜå',
                                                                            'ɭμ˕ƦʛǍŌːϸǨ˸ɸHƆÞӶǧљϦÖğΩ˃ѯǬббς\x87¥',
                                                                            'Ħ˽hɚѫõ8ъɢЦѸxǌƹ҇˜˖ģʒТТğ\\Ҵҭӄж˯\u0381Ғ',
                                                                            '(ˬŝѻҳΏǒ˴ÈɎҸǉѽҕȄэ5ƬŖņ\x8fʧÕΚŹĔйҒēь',
                                                                            '²Pе\x88ŮċˀŋÛÕѐΌԝŔӒϡÆLњȫСWǴӭţȉËтЌÆ',
                                                                            'ʆ1ɪςrËԢʷɞοƩïQϟ˳ЦȤZȋɔÁžƟ-ƌӂԙȽ˘С',
                                                                            'ϺϞеƅӾ\x9eÁƚiRīӫҴéɈȱɒ+Ⱥ\x87ɚǹӶƞjЁÆԫϿҸ',
                                                                            'ɶӔƨΊĿƕ˯ȵǱϏɬϰůˁǅυԂ˻UωlʂРөĔʞĸ˰ϻŢ',
                                                                            'uϓâбēҍʸǭǦʬɴǘϗгƬ҆ӛuҢҿҟÍ҄ѸȘԮ]@Āә',
                                                                            'ʷȒŚјĘȘŜʸƪ£ɓǿ\x83íέӦɤϼɘˣӰʹĉƕȟȉа(ϖҪ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'xɯι\x9dŲӄθƑƭϯɎ\x8eнΝ+\x99һ´ŴӰ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            171031.7420318845,
                                                                            342212.05530636554,
                                                                            610343.5426660223,
                                                                            226432.41164709802,
                                                                            824484.3738804028,
                                                                            238633.06546117103,
                                                                            585496.8858837241,
                                                                            -7479.953201915094,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĉɮѽɢéҶʊɗɕмұǺpψϏ+*đǥұƐƬ\u03a2ѢѼʅρɖýъ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɔΰϽɵԒЩβԍʭŦƅŴɻȁǣ\x93rˢȨAϚϠȭΕ¨\x9a¤Ϗͻ\x90',
                                                    },
                                    },
                            {
                                        'name': 'ҒĻԦȽʷӊ\x91ĸǈ\x8eӤĚĥmҍӶÌĜʹ/Ǯ+¼ШҀȂϠёɢɔ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            398350.67675161664,
                                                                            489552.3067064574,
                                                                            99794.24266486755,
                                                                            627737.424065754,
                                                                            976930.1022672735,
                                                                            809585.5974889873,
                                                                            52508.20745680228,
                                                                            956251.6104423897,
                                                                            344279.6680083742,
                                                                            601811.5212930494,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΚϢɧĦLʱʋВͳ˷ȱǴǪLÓ,ʉhԓѥλƤЫõЏ_ԘώĳǓ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2870274313752926089,
                                                                            90545036790877549,
                                                                            -980961831691476717,
                                                                            1051961247265168669,
                                                                            -4452054522978652111,
                                                                            3896601661568350619,
                                                                            -1994171823145292014,
                                                                            1505547179246572001,
                                                                            -250364691894014071,
                                                                            -4260707634480968884,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɚʯЌ\u0382ĥɆЪ҃ȑ·ηn\x93άƺƘӝŽө®ǽΛ$ҖԒźԃƟʥї',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034621.958736:+0000',
                                                                            '20210327:034621.975817:+0000',
                                                                            '20210327:034621.993497:+0000',
                                                                            '20210327:034622.010846:+0000',
                                                                            '20210327:034622.027437:+0000',
                                                                            '20210327:034622.044497:+0000',
                                                                            '20210327:034622.062577:+0000',
                                                                            '20210327:034622.080097:+0000',
                                                                            '20210327:034622.096838:+0000',
                                                                            '20210327:034622.113869:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˌÑȪ0МѴҋ+ϝ\x84҅!ȺѝӱʛzԈƭͷΗƣǵϥ˾Ϻ|ӍƧφ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034622.202358:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ԣɑҕҟɪ_{¶ǍȠҸɶΖĘ\u0380ԫӳԔƎȳʹdјŰʵβңΐȺĽ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034622.273266:+0000',
                                                                            '20210327:034622.289942:+0000',
                                                                            '20210327:034622.307318:+0000',
                                                                            '20210327:034622.324248:+0000',
                                                                            '20210327:034622.343172:+0000',
                                                                            '20210327:034622.360842:+0000',
                                                                            '20210327:034622.377697:+0000',
                                                                            '20210327:034622.394696:+0000',
                                                                            '20210327:034622.411967:+0000',
                                                                            '20210327:034622.428888:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӣĤľЭҜΏĤ£т@DҎũʚΆÁԟ\u0381Ҡʍӳp',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034622.513340:+0000',
                                                    },
                                    },
                            {
                                        'name': 'σԉğлČӻˣӳәЅӢĉǶˍúкÍӤМӠԛ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -9204777546928458132,
                                                                            -8753523874966863451,
                                                                            5328581074942123143,
                                                                            1790125546287183207,
                                                                            -7740965550242193579,
                                                                            8708317562545298139,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʾƙ;ϒҨΟӼ˞&ưƎȶҎ4Ҷ(ƍԪǞˊʿQԝǜʉŃ˝τ¥˦',
                    'message': '¼ƁßͷѥȫªȘȔťЃҚɾŭʕˈˉʱĹб·Ҿâ˶ýН˲Ϟ|Ȁ',
                    'arguments': [
                            {
                                        'name': 'J°ʶ}}ƟыƑӗBqѕжſӐP»XÉ-ëPȁҔƿŴΒʍ\x84ѕ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'дͼѰʔ¢ïİƠĪ˓ԃВ~ȶȭцтͳѳɫπIBҥ˥ʜÔиƮҳ',
                                                    },
                                    },
                            {
                                        'name': 'ƪŦӔ8\u0379Nǝ˒ȦͽЃñϬϕӯïҁΥȫҥÕӨϱĂŐωҙ(',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 665976.4911896376,
                                                    },
                                    },
                            {
                                        'name': '˱Ƞìϣʌ˚ѬŲǝ-ɯ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3970892381694598427,
                                                    },
                                    },
                            {
                                        'name': 'ȤŘɇǙҒӍƢӉļĦͱ@ɝб\x88Ⱦʴԏğfǚǯ\x83ĜϕϜɱөʍÓ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ыԝē\u03a2\\҉ҶԏӶŇЧǁǞ˞ҳǘњ\xa0ӾχͲˑɀ\u0381=ŀ7ΈТϡ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2190114537304309262,
                                                                            -7272785177171339927,
                                                                            5786776132985541215,
                                                                            -2775754714303051671,
                                                                            616032152465146961,
                                                                            3326836754208883590,
                                                                            -2289267710150025518,
                                                                            -7992980336210523990,
                                                                            -3995894733216174192,
                                                                            4261180632548453109,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǖʕSǨBͲ\x89ĶâѷžlНәÜЗĥl\u0379Αμ¼Ѩ˻ʻБƺϾЊȋ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǺõÙͻȄ2ǐ¿ƴgƌюϢ\x98ӵѭƌͷȻ͵ɓjБ\x9av',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034623.618787:+0000',
                                                    },
                                    },
                            {
                                        'name': 'acȦԐϱʥ¯ΟӖãŨȼƦ˯ϰԝˤ\x83ϼˎ?ӟЈӽΪҕĒҎȏȨ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            411964.5891899303,
                                                                            582209.2087886182,
                                                                            727527.0541825778,
                                                                            -2034.056252720853,
                                                                            724300.7375501365,
                                                                            -1667.165938137754,
                                                                            911344.7455636392,
                                                                            96379.96058531365,
                                                                            852776.8659307236,
                                                                            872171.8068550982,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'еȐ˚ɓдʨʆѥΈƴɝηЅįͶ#ōϗΑԢȑÇĴ\x8bǘƊġӈɠ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '\x8e',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'œĸȀɘ',
                    'message': 'LΙѠф˝ȋɧΔxmӆư½ȳǇљƸǫũԀĹö΅#ƴɋӾΛȈϬ',
                    'arguments': [
                            {
                                        'name': '˲ PӪXǩѕǺȦӾɛɎʛăӱɭGҩӽȝŋňѝӱЃӌ˻ԝѨS',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034624.115132:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˣƢǘɯȝÑαӝ\x86ſ˱ȫ¸ąŘȂԇџβƩɤ§ʦǔΩČҬМɜЅ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 319450.5011439663,
                                                    },
                                    },
                            {
                                        'name': 'jƷÜɌθ¿<!ǎUЄ\x8bĈЕΘǥЄёɸɡ<Ʈȭp\x96ӏɐŭϢΓ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2360967550992411325,
                                                                            6914891033795248621,
                                                                            3865318256561140079,
                                                                            -78745494650974481,
                                                                            6307086912626264045,
                                                                            -3369592494482607639,
                                                                            804272496739515028,
                                                                            6902497144872270042,
                                                                            -394820941640826836,
                                                                            2335469647680941652,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'їΖӜɈˬEơķϺτɾ˅ƜȝԠвĈ҅ͺΉөŦȚњΩW',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǰÞ&\u0382˛ԋɪͽmӘˍĀóԦυӊҜ+ɃŽș²˱Ӳǆұ£¸өȜ',
                                                                            'ʢĨϩәȀ˩ƈԆaџɩ˟ϋҊϽёǿѳØƸЃȾͿɊǗŋǕфўѼ',
                                                                            'Īśʘɑ]ҖøӫĦљ÷ťȎзѷƓǠҍ¯φӝΩιŽ\'"ъĚεҞ',
                                                                            'ӊԌʟɿɊκϛѨϔ˞ϽȽĪɩʚХË\x86ŚΎԕԕÑжˋЫҝ˪ώˍ',
                                                                            'ʡʊîǐеͽӱȚ˃ÝʻҎҍȩ]ҶāȦʧѦҶӱŌĩϹνșћ&ȓ',
                                                                            'ÐιϰȰ˭˂ǌϤƧΧϽϰǽÀˮҕϹӭԅΓɹ©УԈΡfɢŐyɷ',
                                                                            'ԈĠԊÕÍŒʨǣԩCůʆ\xa0ˇɴĚ˙Ц\x82ǄΑҟť©ԔÄǯЊªb',
                                                                            'ԘĔʖXȱBќӬэ҉Ȩõȿм˳ɉŰǶ"ӎɸâO˧ΦĮ˖ѰéĬ',
                                                                            'c˵ΫŀČİ¹ԑɎэ\x8dĹӢβ˺ћͺїʙΎ\x8aĖÓӭҀӋ<ȊǨү',
                                                                            '¬ô7ΞόĀiЬΗвΡǗɖҪ±żȫoҤɶǨʿџϺ<ȊǔЮGҖ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ř˲҅ѦϢГЌƾ!ҙdҽϵЃǈUδʽɟӞĝϯįìĶļÑȉҾɲ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 67242064362562787,
                                                    },
                                    },
                            {
                                        'name': 'ϋ\u038dӷ\x81ȂűςЇtԝɩɗӠϤΏԌσӇʖӤƶѝŌϩƈʆǃґşӵ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '@Ǐ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ΐѬӉ ΪƇŃЂĝѯƄƀɋΥɑϓ+.Àƣȭԫԥόŵϟħζɰҁ',
                                                                            'ʰɤӫʄӝ!ʍΧҍҤ5MaŦ˱(}ĴˍбͳΕǆԑѻԨȁ2\x8aʸ',
                                                                            '\x97ғ³ʊοŶщʮҎҝȯÌԗǗ[΅ǔŽԅɴ҉ԏϕԆͱŹ҂ϼҽĮ',
                                                                            'ŨЃÌĝǜҬѭǂÒӑɫӁњ˘ƥʀƘƘņƨϞȑ˵˼ԤѹĲѹӑΙ',
                                                                            '΄ƺʬʻʌTŇˑǊʭŒίƚѥĦĻ\x88ΐĞʜѴļĿ͵ӵ\xadуɤɃӱ',
                                                                            'ƍǩÕƬȉƀ§ЀɰГ\x84дýϬǭο>ĵʨþιрřъšӞЃΈȤС',
                                                                            'ԞɏȻрѿϳͳȬиɹǇƲȼ˛ž˼ѤʆĄɅŧĬȓϬŭȵѾ˅Ƹź',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ў&С˽ćĳԈmʠЙøőʉ\x8fȳǆĹ²ЍōщȉòƄЙφÌ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ΫʌИ˵æİÈʰĽ˞Ƶϯ7óɞWѽѧ˙ć\x9b\u0380ʴдσŝ҈ғУʘ',
                                                                            'Ǆs\x8eќʷȸǌ©\x88ćˍ˃Ƕ҇ѿ\x9e¼ǹʋƐƣg¹ɜͳ\xa07Ϋѭů',
                                                                            'ĉϷӷô˽\x99ӗŃ%ϱѽƮҁ\x96źӞ˪ӕ˕ӾҲ)ԅɄл»ԬͺήҦ',
                                                                            'φ˟ŹȟЇǞԠѯбϷӇԋļƌóƭɞ϶ԕźƝcƘӃϒΣҞυĠʪ',
                                                                            'ŐӴȫϛҸӪĸ~ȿυƓ®ƕǌπͰΈľԀƵˌ&:\x92ǽжɩƹȣώ',
                                                                            'ŻȌYɰ˞àȷ2˒ϊҒԈVĔФ˰ˀΖύ}ӋSșŉԂϧɃɭũǄ',
                                                                            'ĎʤԅȗиɈΓʦ϶ǢɢěͽɂƆāđǔ˴ҩ҅˝ƢƎtǿŘӟūƨ',
                                                                            '\x96Õ¥Ȳӏ҂ȵčÉƊԡ˽ÐƽϓˤԮȉĻǀ\u0380đϐ\xa0ѵʰcӛʅ»',
                                                                            'ѿќƋƼřƬђȱˡȡɷ\x97ʹЛ˶сБǝηϸBɹȉǁʷЭñѣąӎ',
                                                                            'ʂʥȞȧӴϿƉΘ͵ĲĢфˊ\xadΑȨɆǏʷEȆӉϯȐȋÆҞʅŏg',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϯӫ\x9c',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΐĜΖϫƝƞ˩ĺΈϤѻѱԈԭɩΉΘěΏďƜȦҋ1˾YЇ˓el',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ÑԎҟɯ˦é¹ϣΎ0ţ˛ѱȾλȸҠЋԁԥōóƧ´˩ʢΖƴĕã',
                                                                            'љŔ\u03a2ǉɄ˺ŀƿƆϴʓҀǶӘЭƦҳőƋƻжхʕ9Ǎő\u0381ԏƤʾ',
                                                                            'νģȼƺϞúŧǧхњўĴҴÎǬƩ˺ȲƜFʹσюϤǡȝ\x83Ӷу΄',
                                                                            'ǹЁǵˎҚҚŌҥԘ˺ӨӜȁ&ǞΩĭǌŨÎύɚϹӤĚƕļͻѬӫ',
                                                                            'ǌЗͽĭφ˒ǟӕ¢ӂϢÐЇνª`Ҏˣϰ\x8cĕºƘLʔӌŋƵǧɳ',
                                                                            'ҥďǆÊŌ#ȈĈʖóͿʣ\xa0жщǴĩЧÈʬXӴł¿ȨҨӭԝΓɟ',
                                                                            'ɅβЌӖxħÃԇêĻЙəљͺŶџВ˧HnɌѬҡѾƱЄȹ£Ɂα',
                                                                            'ÏlʏΦʐʦȅƪ˩ǚɶƘƏΑҫ7åāʭŻƏ+ǫ˜bȟ¨˥Ę#',
                                                                            'ɳhЪǋǟѧε*Ϧɢ\u03a2ϧÉŸ˩ɽƳħϔ҅Ǻǅϭ˥¤ƗʁɎĸѻ',
                                                                            '˻҉/ρǞϠԣŌҸŵπƆɑϷǼΖӀϼ˻ʾѷґǝƵȘзʞҷřɧ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŝíɽǞʋҬŶɥ҈˦ЩƿӍʳЌҖb˯ʺóЈƹɉǓ҈ΐð:Sϖ',
                    'message': 'ȱӝŔҶEԙĭǵƿϠɳ˫\x96Ѣ҈ϩħáɱҐһƏÃΐѳÐ\x9bůțϧ',
                    'arguments': [
                            {
                                        'name': 'У®ǃǺԚϪҼӭòҞǖƈȾ˃',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6868272695784833968,
                                                    },
                                    },
                            {
                                        'name': 'ϗïɥ¸Ċ=˗ɍ¯ɅԋӊŽĀi5ńÝѴ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': 'ѣʻĥƣӫϲԌÎЧʐϕΙ\x8eǧԊĠҨ˝ȶϴȯэʫǜΤчǱɁӐӡ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034626.423028:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ʈƕӟǵʫ\x87ѥȱҹϞм{ØтüЎ\u0381şɦ¿ʔ¼ʝҥԒϭԬϻʵɰ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
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
                            {
                                        'name': 'ŞǧύíǗǖΞϸȱTѪɗҨϏϣîӋ˪ˋŦǴI\x9aϨˌː}ψƗʏ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ԗ'\x99h«ɍǙʲπȋŪƣƹ\x9aҳȆJìŮĊǂΞԥΛσȓП",
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'mϬцȜ\x83҆ğȌґɌӫˇÐέĚǭʜӄƄ\x85ÿʱҍӝį_ɅɬˊӮ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ұm:ӉOĿËȷӗĿƔӢȜöİȹáŢĭǶĔɴӑēƠΑQŉԘӕ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'тӌŴċ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034627.361400:+0000',
                                                                            '20210327:034627.382738:+0000',
                                                                            '20210327:034627.401643:+0000',
                                                                            '20210327:034627.421262:+0000',
                                                                            '20210327:034627.437891:+0000',
                                                                            '20210327:034627.454538:+0000',
                                                                            '20210327:034627.471231:+0000',
                                                                            '20210327:034627.487952:+0000',
                                                                            '20210327:034627.504544:+0000',
                                                                            '20210327:034627.521605:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɶѐ$\u03a2łȄȂԮϠʓ\x95ƚXЄǖƗ˖ΰѻ\x86ŶƼԤZµЋҪа\x88Ȼ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ͽ͵ʜȗƠȘ`ρԃêƠБӽϴӣ˽Ͳ\x8bˤɄьШɼǢѝæéíˁ»',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŧҍȬϮϠҧ˫ӛ\u038dȚѳқɺґI@ɮŷӳØnˬȲw϶ɠԜΟԭӎ',
                    'message': '9ϑőѕȰÿҏ\x94Ƽʫƍėԥҕɥ˭˪Ǩēʴκʋ˴ʓӧűÁякǨ',
                    'arguments': [
                            {
                                        'name': 'ĮâǤƹ\u0379ɳµƫǝӭĽĨΪɌȒǐΙnsʂǭ%űȘΏΤƄ7',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            49847.51442981826,
                                                                            993645.0349471546,
                                                                            -40075.650308433986,
                                                                            809679.3060663264,
                                                                            772140.8928417352,
                                                                            354267.81470524473,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѝEě˨ąЭĴӮǛƕϟм',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6042464782953339457,
                                                    },
                                    },
                            {
                                        'name': 'øčŒϩǮұˋ\x84ŽLԘуИϢыϦ˸&ҸŬɆǾ\x87Ǐ˰Ìʌ[ƙʎ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034627.989199:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѩɴ×ɜÕЈǡɄηоѨǮΔӏΒЦģĞ&ΫĚƿφÎΕЗ2ǵșǂ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʹЀ¨ӗŕőϼ¨ϖùϷӠāÐέϯʅLЯуm+5ɽû¨¢ӧςǟ',
                                                                            'ΞɠľșɃѕʨѣ^҃ӤįBξȠУҸѭӔҔ×ȺȗӓϹШϤĝ7ȭ',
                                                                            'hɿӍH\x82ʠ)\x99ЩæΣĞɖˌПΜѱӽηͺųжǚʫƁʬΏʳȈț',
                                                                            'σͽͽƌÑњѬЧĨϗ˟ȃ˰ң¡eȀЏĐˁіƔřǗȠʌˊҋΔÆ',
                                                                            'џ[7ŴǏʆƝłԉq\x84Ș\u0380\xad˸·ҝйȜΕРpҷ҄ɵM$ѾӂX',
                                                                            'ƷͲ½Ǉ\x8f/ͰԪɘͶbʫÜ¸ϔʂѲmɬʩҳϑŊʭƹӾϪнȂԚ',
                                                                            'óǹ˶ģÝĦɨɓȄ\xad\x9bÐЕλǋǎʽĊҔN±ϘйśʈƴϿ\x9c҇}',
                                                                            'ԙδҶԝmeȞĂӬƗї˰ҀTʬçˇ.ǩŕσʊЗ±±ȫ\xa0Ō˳ū',
                                                                            'ȸΒǽԡʋɮɸːƮľNʻʗǸʋӰ˱Ӟΐ\x94˅ƄЈEǇгͽөßĝ',
                                                                            'ӒʖЎΎYι!ȨÑН7Ԙԋ#ʽҩ®ƧɭІYɶùΫđЫζƜǞӪ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '°vѼʥω3ƆМГʹɁɎѵϑ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '҈ѧˑЌȝȃ\x95ԉҬƌŴȽŴŌϵ\u0382ġ\x8bƷJЬȠýɽŠŠˇĮļͽ',
                                                                            'ƀ˸ԁ˄ѧƀʯΟƥЇɪĲɷʑ˃ӍǲЉЯŪÈԍ¸ѿƖńʙԓҁˀ',
                                                                            "ʕѧ\u038d^ʿ'џVɫλҔ˔ÊŚŊĎ}ӴǭńөĴѴǓǦď\x84Ć˚Ǜ",
                                                                            'ϡӏȖƉ©ЁʊƈӆϊѼuɻɒĠӥ˙ϱɬŜДǉə8˖œ+SǹҖ',
                                                                            '×ҎЖͽȅMȭƑʀ\u038bФÛǷ:\x9dӔ¿ν¶˺\u0381ǩѶԐʋɣɬˌϮΤ',
                                                                            'ˮřÕӓ҆Ͻ^ǗΩȫξί¦ʢӪʤŬϮʪхƏʹ˂ǔHȐșЅŗʜ',
                                                                            '\x92ӰαĐ2әķʈԖȆõƹҨŊӂ¥˭ʱ"ρюȤƉĠҡŘҡüȥϾ',
                                                                            'J`Ǟɲ҆\x9aԀɗȡȴһɧǒЬ\x99ϷҊˊʱ¤^ʞǝƂåʤŖщ˫Ѝ',
                                                                            'ѳԥŨД҆ц Ð5Ԝԭѿǲы]ԋŲ˧İ˗Ɏ\\ɠΪňƅϮ\u0383z¦',
                                                                            'љđľɢȂȘөϾƋѰíţɾÝЛʪыŊГĔДЈɹĞʀӌ˧Аüψ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѵñ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            568404.7025453747,
                                                                            683068.1055149849,
                                                                            -40883.87239404279,
                                                                            686042.372547974,
                                                                            -93786.98772107116,
                                                                            417439.10194668546,
                                                                            28440.201854059313,
                                                                            108883.94462065012,
                                                                            -69485.88282502978,
                                                                            879449.5205667297,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8eӕŰɪɸƐĬѶ\u0381ʑIԡόƖӂҞұÐӃо',
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
                                        'name': '˙±ԙуҾԂӯ\x9aȠȁАɒȗ\u0382Ҵʼ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʲκɮϼKɟŭűҶė#«Ӿƃ\x83Қ҉ˉȭӓʺËӆцZ\xadńíȤИ',
                                                    },
                                    },
                            {
                                        'name': 'ʥƉØɊǣ\x99jӨŤÀԥɦԡьĺǉѬҗ\x80Ԑ˞ďфɺ˂ˆԘŋӒ҂',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034629.159139:+0000',
                                                                            '20210327:034629.176785:+0000',
                                                                            '20210327:034629.196174:+0000',
                                                                            '20210327:034629.213196:+0000',
                                                                            '20210327:034629.229800:+0000',
                                                                            '20210327:034629.246478:+0000',
                                                                            '20210327:034629.266197:+0000',
                                                                            '20210327:034629.283053:+0000',
                                                                            '20210327:034629.300122:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԅԑȅԑ½Ǉ˅й+ȪӸͰƝнɎλˣԁ×¤ΖÅňȻŗԢӆҽХǲ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 425669.0701993033,
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

            'scope': 'debug',

            'messages': [
                {
                    'catalog': 'ŋɹ',
                    'message': '\u0379',
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
            'identifier': '\u038dѿѓԂ»ӸŃєκwɡVѮлʜŗÄϙǰx;Ɛ{ԚтѪǾϽâɹ',
            'categories': [
                'os',
                'os',
                'os',
                'access-restriction',
                'access-restriction',
                'access-restriction',
                'invalid-user-action',
                'internal',
                'file',
                'file',
            ],
            'source': 'ѪїӧǏӨҀӏ&ÃȮӛ\u0382ʴſ\x9fЌҢѹ]ϚŲűӃȽӀѓ˵ͼt˧',
            'messages': [
                {
                    'catalog': 'Ŷ\xa0ЍĶԒҾǙ˖҅Ǳƺƴ-ɨѨҞԐˡ˵҅řĠӯːȬÚӧЅϕ҇',
                    'message': 'ӵ˓ʜƦFԙɺ˗ϋʧņɕсäoԟ%ѰӬhóȷ4ωчϊ΄U³Ƿ',
                    'arguments': [
                            {
                                        'name': 'ѥõU҈Ѿϻʯȏ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034641.322008:+0000',
                                                                            '20210327:034641.339012:+0000',
                                                                            '20210327:034641.355837:+0000',
                                                                            '20210327:034641.372585:+0000',
                                                                            '20210327:034641.389123:+0000',
                                                                            '20210327:034641.406268:+0000',
                                                                            '20210327:034641.423282:+0000',
                                                                            '20210327:034641.440125:+0000',
                                                                            '20210327:034641.456777:+0000',
                                                                            '20210327:034641.476326:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0379ƚɘЗĊŬющëԇϛòѿІїσǡʁɧƆɊĶȫ\x86',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4662646287140547913,
                                                    },
                                    },
                            {
                                        'name': 'ҨĘwͷȭ%Ɲʗɵ\x84ŷьVȤѨŶ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 634711.0184953668,
                                                    },
                                    },
                            {
                                        'name': '=ȆǣԁѡŔˎ\u0379Ȥ˱Əɾ˭qÁȹ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ƦȎεҥбІoЋтѷǅǱэЀųèɾď˷ɰĕǥαԗñȩ\x83Ї',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ҵҴʀƴԂǟûΉϤА¿ɯ¬ˆǭįҡȀο',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ΝƷʵԑįԗɫ»ȹί÷μì\x99',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 918780.6919211973,
                                                    },
                                    },
                            {
                                        'name': 'ȐǨɶЉǉõҵʍƄѧӦ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'җϡâčɍáΌ4ŲƶҪїǫË·ǖȒшҁśˡɾϤĪõǪÆмƩȽ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʻǌǔΦ\xa0˝+ңÌҸԭ;Ҡ˟¨ӄƅ˔зƗ¯ɢìǤ%˯¦ҭΚL',
                    'message': 'Ǉ˃ÜDÔŠ×ѰлĢʵǱ҇ҵ\x88ҾɫǶϗƄǃΓǬkҚԜȋsGƎ',
                    'arguments': [
                            {
                                        'name': 'ӓЌи',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5746344698271187777,
                                                    },
                                    },
                            {
                                        'name': 'Kɦ˳ϒ\u0380ƘϨśÓяҶЬӖAˡΚǇҩϞƔϻýþÙΡqǂƬpθ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            246926.2242195757,
                                                                            567056.9080839314,
                                                                            -20143.236208518138,
                                                                            -77623.0392995528,
                                                                            530698.1360156654,
                                                                            147614.6888993508,
                                                                            724945.647792597,
                                                                            161857.7819432042,
                                                                            -22034.623181525953,
                                                                            386017.17039618565,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'H/ŅʿÍƧȋ<ħͳo˪ƨŤҜԀ|ϓГғϥҭѧŬȃ˺ϒΨǆ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 168513985603195364,
                                                    },
                                    },
                            {
                                        'name': 'ɲʕ˅àӽǫˢς˽ƌŃŧĿɹd\x8cќʇӴɓ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ƽҖКĪШƴÐ҆ԧɏџщʱŹΛȟŒ҄Ԉî¿bHϥ«ʀœȍƷӬ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034642.608343:+0000',
                                                                            '20210327:034642.625107:+0000',
                                                                            '20210327:034642.642032:+0000',
                                                                            '20210327:034642.658645:+0000',
                                                                            '20210327:034642.676287:+0000',
                                                                            '20210327:034642.695612:+0000',
                                                                            '20210327:034642.714518:+0000',
                                                                            '20210327:034642.737192:+0000',
                                                                            '20210327:034642.754103:+0000',
                                                                            '20210327:034642.771457:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΏƲʦ˹ȬρόıԄłäǛnЂϢѫʥƁ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '/КŞȁȲѭÁ\x90-тЋҲП5ʄЏɩÒǁɾϪƣĊ§ҪοӹÍîì',
                                                                            'Ǻг\x89πȻ\x91ɄƫčÄǝēԊĂŞԖǢǩ9ΙőȦϕχƏʾĿvŧѸ',
                                                                            'ëæVȝòʟʶχŸ¿%ԤƬȦŽύ£ьdͼϾκҀ|\x9b˴ʓĪ˸Ќ',
                                                                            "Lӟđʺ§ȜRԩ\x96βűŽύŸæɚӿι=ȟȜ'Ǵ˂ĐӔ\x92ѢπϦ",
                                                                            'ǔèƧƊЙĕľV\x8bĲӗɜјˎŊĮĵӏԎ:ӻбôћѫəӾӎǶϞ',
                                                                            'ĠЧҭĪҚъˉȩсѮ\xa0ǥ\u0379͵ӦňǫҨРƻl\x87аɎĚˊњΒɎŷ',
                                                                            'ƓɒŨ˸ȇ˼\x81ЖȷΜŒΫΔгʖ\x8dҭȫ˕Ďpҭ˵ЬČǳˉѡӤΥ',
                                                                            'ҋĔʅ² ҖƞȀԢŬԋ-ȘïӸ˜ӿɒƐɵЭѤоĠЌͽʯԑǧƜ',
                                                                            'ЋȋɂôҢҐГӡǊͶҸѤɹҋЪŊʻ\x94ȣӥȺϟėŨ)оŃȎ«˖',
                                                                            'Ǽ\u038dώǏȳŃƀ˄ͷƫбϼȮǜөğˀ;ÒδȊҜƩÆĜŕНĩɵǐ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Kԧ˘˰ӽĎкӽĝa:ԠӌǦЃ˜ȼԝIζҸԕʂɊ˅',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034643.028445:+0000',
                                                                            '20210327:034643.041717:+0000',
                                                                            '20210327:034643.054605:+0000',
                                                                            '20210327:034643.067784:+0000',
                                                                            '20210327:034643.080666:+0000',
                                                                            '20210327:034643.093660:+0000',
                                                                            '20210327:034643.106881:+0000',
                                                                            '20210327:034643.119716:+0000',
                                                                            '20210327:034643.133948:+0000',
                                                                            '20210327:034643.146713:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϝѦʙrǵ:ϐY˒ίԠɝӎüĜωÞĚƗʟØȧҴΌЁɿ(юȄώ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -93537413679479473,
                                                                            5716145611270791154,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʵдLˁ˷É Ѥɠűуʑș',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8934941501441878990,
                                                    },
                                    },
                            {
                                        'name': 'ȝς¼νҒ҉ӦεӢ˦ŃͺôǐɓΊ˳¾ǳҞȞŧŨӋџȳʦ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034643.407379:+0000',
                                                                            '20210327:034643.424273:+0000',
                                                                            '20210327:034643.440918:+0000',
                                                                            '20210327:034643.463148:+0000',
                                                                            '20210327:034643.488007:+0000',
                                                                            '20210327:034643.516372:+0000',
                                                                            '20210327:034643.537201:+0000',
                                                                            '20210327:034643.558074:+0000',
                                                                            '20210327:034643.578059:+0000',
                                                                            '20210327:034643.599829:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '¨īƋÁèɑϏ˦ſБ˟ԀѤ}ӫĦ\x8eǥȁČф\x8dxϤ΅ëƑĉàř',
                    'message': 'μщ¦ӤҀҨȖǭϳΰ˴\x85ŭ˘ƣɢşȭΗlìȔŇҔѲȌԨԑŃΊ',
                    'arguments': [
                            {
                                        'name': 'ÌϏԁүxƎ§їҚΡξМʌ²уŘԃΚŇϼѫїgɶƃ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -2775.714125639177,
                                                                            938110.2834548255,
                                                                            715794.5250888537,
                                                                            387989.00863497413,
                                                                            774724.1529485477,
                                                                            939867.7715711492,
                                                                            429634.45150969573,
                                                                            47120.272559865,
                                                                            981710.0781606894,
                                                                            37089.899492957076,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Њ3ǜү;˛αιÃ#ԏGѯ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ůğŗ\x9fϨӽшΘʿ1ʷ\x90ʟϋżȁýӏˉʧΕ\x8dƗȁɲ×ΧΦƀɪ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϣ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7984060580605860638,
                                                                            8208695929058169314,
                                                                            5088265226413093579,
                                                                            3805120352464959777,
                                                                            2547831844835679761,
                                                                            -4553726782550840487,
                                                                            3080716513277863298,
                                                                            5192838101867329060,
                                                                            7422504853086094466,
                                                                            -4676625730031571304,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҸΨȚЯưuȘʡfʎϘżԏɵýŵ©ϺǝzӥϠϱĀæІ҄ȸдЕ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "ͳ,)ϨʙʹԊͺυ'F=ǯȺӼϓȵδԞԁý\x7fÍӌȲԚwϬэЄ",
                                                                            '¨¾ɖʿϸħёĤԥφ§Ͷ:Ќ˼ʪѹɼȬӛԉͶćѣӲƤűöѵl',
                                                                            'Ņ˦ѓȑ÷ǈĳƍ˂\x89ʮȫ^ƛӈ҅οФωđȹΧ˗ɂʨƸ´ȿљԏ',
                                                                            '϶ԍAǖOКѩĪ\u0382ʀӕҜ˽\u038bPȽԇ]ǭзˎʰλɈȃ×ѣѮ\x96˂',
                                                                            '҂ȧƷǬϚԢŔǬ\x99U(¼ƘӌͺԄ ¬\x9ařőѴśϷşİǛȣʤȚ',
                                                                            'ѾAӱ˦ǛΠåǅĳҚύӷɐԜӑϑǁäɞ҉ǊȁөтȰŴǓБҘ˭',
                                                                            '\x98\x97ˁơ²ǷǧÿŎԙ͵ȮŌëЃ˓ӑǗ˙һԚƽʩPȽӳОưĵω',
                                                                            'ÜʰEɎ1$ұ\u0379ӿēʥ˄ðΔõЇӐϵķˇıŚМVBÐFеĭȊ',
                                                                            'ΡѩwĉԪéŏ˸ɵƠұˣ4ʸԇѮ\u0382ʚÉƨpòĨțӜΖҭϽώө',
                                                                            'јԛҼĎҋǧƶȴŕ°ǘɫӘЬĘɤÁхϕæƙ\xad\x85AшÁĝ\x9aϾǘ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɿȶĻśÒeχҀҩӱӬɽé',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9146194960062117894,
                                                    },
                                    },
                            {
                                        'name': 'РǮůʘқÏlˣњŸҡЀԗ\x85\u0383Ʀɍ˩ѼčɻȪϻϜѝҎģǆэ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034644.627302:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɂŏԙԏϴOӋ[Ǡ\x8bӑԛ҉ű/ǛͲϞԚӇƍ"åӐҾХüȤ3ŀ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 527233.7781105577,
                                                    },
                                    },
                            {
                                        'name': 'ƾг˞ʅԫ˃ϺӭӾ]ЍϧΪOӳïȻiƥĹ¸åӊ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʨ\\þƴјц҃ԁåȢȥˉ;ɦϝbďлҞϡįƲÔðǢ˱ÓӁŊϏ',
                                                    },
                                    },
                            {
                                        'name': 'ƿšϐǕƊӄΪ˶ˌЧў΄ƯҎѫΊźĐı]ш΅H7ҖÇŇψƦ<',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 857240.2159997287,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Œ;ɋԀʦџчȃҪʹ\x9dъНϳτǭȻȶoğ˩ƕЗңƠϟ&ɲіϰ',
                    'message': 'ΩӷǍƉ:ЈȜǶΪθУdͽ`ҒӶӀϖİǋЎɠǀѓнɜĭʩӶĆ',
                    'arguments': [
                            {
                                        'name': 'ʸH;ʂϕ\x8aҟΖǜρĢ͵ӜԎɘӤԡ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034644.981482:+0000',
                                                    },
                                    },
                            {
                                        'name': 'è%ÍŋϮяτ\x9dŢ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -83705.60511409551,
                                                    },
                                    },
                            {
                                        'name': 'ɃĬͱɹ\x8f´Ŋ˸ΎňƎӅƮě˕ŀԪɀӀŊĕͻǽԁɔψ8\xa0-Ӡ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2524737121454536529,
                                                                            1346222559881989098,
                                                                            7296277214580972109,
                                                                            4697930713168729774,
                                                                            -6128058563061561454,
                                                                            -4204883967420807940,
                                                                            7492734012874623213,
                                                                            -3860938426890988858,
                                                                            -4174528323535706107,
                                                                            7070701873311299758,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '$ă£Ѹ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
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
                                        'name': '˶\u0382ԐʕƇͼӢÀЅ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 416200.9252449679,
                                                    },
                                    },
                            {
                                        'name': 'ӰrˠəĮ)ŦŒŉȿРʟѳ҈θвįłўÝύҙχƹʣњʆ\xadʁӠ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˤňű҂\x8eԠālɻȘВ\x91ǂϡ\x87өҪ\x85ĀˋȕſΦЯūnâĽț\x91',
                                                    },
                                    },
                            {
                                        'name': 'żђ˅ӂáȒвǑҴȰĜӪ*Ѡ·ϊҺ\x8cΒ-ˈҍɏʤUĭïɖƫȥ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 173637.96264728392,
                                                    },
                                    },
                            {
                                        'name': 'Ȱņ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 492272.44861445413,
                                                    },
                                    },
                            {
                                        'name': 'ȾǤͼ҉ǠϧȾƯƾÁχǄǸˈºăĽĒCχʿǢÔψώÓ/ɃԙÎ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӊӼЍˑËΩȧ҅ʍϪɋʹϩʯс\x9dԌӀжўȀƲӒѤЯȇÛɘƨk',
                                                                            'ǍѻOӁmӣΙűʟθŰʚωʪ°čЉӡ\x9aĀˬñʕLˀьϚźȺӼ',
                                                                            '\x97ÍшϷАåɧ½ɎǜуΕɲ\x95ǋ˳ҎɰѬ²ԡƕ\x8dНɕı¶ԑӼc',
                                                                            '~*ԪkƔҬ8ʒʸĄ˅ЭʋΤ˞ŅðƑͷȏӍҸХ\u03a2ºρȁ\x80ğŧ',
                                                                            'ɭSŧƵϒķԒ·ԓѪ\x86ʼΥƘӡуÀӡɺɨҿȶ\x8d˭ҘêҍԭɮŻ',
                                                                            'ˎϡĒɆè\x9doҀɷņƄɩİϏʽτӒ\x94ĝǓǵʂΰѧҸӟȧ)вķ',
                                                                            'āԡӷLҶ²üѣςҩºϕHÊˮĠӮGīǝц˚ѰȦΏØĤäȤ{',
                                                                            '³ěЀòįöȉķʧċzėlΔλ˟Ќԗʯҟ0\x90ΑåƬыΤ¼Ǧ˟',
                                                                            'ìӿŽӜʝƚǕ:ƦOʣƶЧŇƺlĩÁ˵vԇ¡˖˹7±Х§ϔǉ',
                                                                            '˺ԚίˏεԣɛǛОиöŻʉπǽ˸ɦɾƵ˹2ӯϹâƏǞÏӝĭ\x90',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҵϗŨĮԜɾ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӰnǮn\x86ʧȠ˶£Ļǘ/ǑɩыϧѦ&ÍчѴϻʦâŔ6ҏ1ҏΟ',
                                                                            'jϱˆ2VҷɑԭќͱɨǵѥЪȜҟŌɏ¤ίʣҌƑѦ\u038bǄķЕҧȩ',
                                                                            'ƔψьʪӋѭҶȊѲ×Ǭ˪ΙˆԦĘԨǰԨƺȖъǽΧύʢÄκҀԁ',
                                                                            '«ɁͺȒƪÀзȮ˽ȍǎ˃˜ͶĲ\u038d и˼ϥѕҠζӧӖΈʜȉҼϩ',
                                                                            'Ȼǜŉ˯εƫԉ¤-ʬɬǏːȰ\x8dеүCĺƺhȆ\x99҅ʙѸ\u0381ȑǃç',
                                                                            'ŷͲŅ˝ʭŞ҉ÖȢßЁѦiɩνϝϏ²Ăƥĺ\x96ǲτϗˮʣԬȞʹ',
                                                                            'Ș(ʐà\x9bĒɸИňΝϙΌʜ7ӧԚŌνƋʚPŗŉԁԆӑϖӰƞϤ',
                                                                            'ƴΈĸǁéɃҘĖҰԝӚɟԤQԇĈӣŷȜУĿӀĭ˒˞ƮͶϔǄʙ',
                                                                            '%ºӊȬăӤԐӦ\u0380˰ȺˡўЕəƻўұţΗȐиҊȖӂΒӨļɭŦ',
                                                                            'Ƭʄ ǃàɱǔӵlʱʧġǳϧҝϧĀ#ΆҦįFΣҢǦOȘǲçӱ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ťƅоΚȯҷʄϗƸđȭζɊǗ\x83\x80˟ʂŖ5҂ӒϬÕǕӪЬѩПȟ',
                    'message': 'ǅϔÓ¤өʒρΘƭΊxӆlԩ\x98ςLtҳ҄ʹ˰҆ũʦǰӵԅêә',
                    'arguments': [
                            {
                                        'name': 'ƹđюĽĴæξŦʧɮхłӺαвӝɆȻ˩ȷȻʽп\x90ɭȒğϙγΓ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -9073132001698549491,
                                                                            -7191638415424592726,
                                                                            -7720549989861473679,
                                                                            21479364482094022,
                                                                            -3621045951823099879,
                                                                            -455105953849356149,
                                                                            9061634851710324883,
                                                                            5367024397996865438,
                                                                            7094574456401932791,
                                                                            6052922878856244260,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȴȻʷǖ˦ʔ*ǪҕɗiťʍȳҭЏ\x84Šʋǎӝҝ˱\x93ȱGƏÀ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
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
                            {
                                        'name': 'ԫҚȎȭ\x9eƪĤʲǑӳѬ8%',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -287994369653169180,
                                                                            -1490603538486642731,
                                                                            -6185154379111504824,
                                                                            -6427141205600269174,
                                                                            -382025248810869470,
                                                                            -141523920372224772,
                                                                            8565551170752611287,
                                                                            -6489589949349624465,
                                                                            793853489198689659,
                                                                            2876523291222946784,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˶ƀ\x8břΞêȎ±"',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034647.246292:+0000',
                                                                            '20210327:034647.267140:+0000',
                                                                            '20210327:034647.285474:+0000',
                                                                            '20210327:034647.302454:+0000',
                                                                            '20210327:034647.319137:+0000',
                                                                            '20210327:034647.336202:+0000',
                                                                            '20210327:034647.352953:+0000',
                                                                            '20210327:034647.368408:+0000',
                                                                            '20210327:034647.381433:+0000',
                                                                            '20210327:034647.394252:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ɣɭ\x93ԫ¨Қʝ¬ĥǷÛĺҘ˨вÑś<ł\x8eÅūϑÇʹȽТyƦƩ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            242786.52623347944,
                                                                            976832.3755423937,
                                                                            489796.1345617636,
                                                                            301266.568056511,
                                                                            480358.4685511547,
                                                                            203857.25264440203,
                                                                            147718.19199301302,
                                                                            736631.36089619,
                                                                            596427.3968860295,
                                                                            224307.699569321,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'άɐΟȣJˊӐ+ƓďЍ=˸ǳÄŧҬȔeΧrȟϙǮ˙ӈŁԕːƒ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ț\x87ɔ\x83Yλřρɶ˰ԩPƎĚπĬАʝԗȪҡшѓżɴШϢĄƿȽ',
                                                                            'ʙΪ\u038bˡĿʞʤˆŜҔyǣñԓȵзѲɿǳɏа"ȚØ΅ч\x89yыɉ',
                                                                            'ĺđŐýӣȏǩҩϣ£uϴӞȪǗěϦ/ƚ¬јбҡЏȯȔīԦôM',
                                                                            'їÇԋИԐҡǔпȡʸΪʶӨӦёƤˑΪǌȻЦ)Ӌ\x87Ȳ\u03a2*UɥĘ',
                                                                            'ƯɃƂŪź҇ɶΩƃǲŦvɤˈŨԜǻӴˑɓҦϦNґˇъȸϫʓĠ',
                                                                            '\x89əɾɫɈʠϛğŢĳɹґɸЬÒӕҎȘɺй˝lέȱҮўҼ¬ȵß',
                                                                            'ʇξЙыѬЬ,ɳſӮͶȇ@ŻƈȐКӷӭрsǐҘʠӹңǉɊōi',
                                                                            'óˬǹÒҽΦѡωӊёψpѝƓćέҢ¾CԐìœԜȳ;өɰſӬИ',
                                                                            'ЈÀΥôiҩvӨÜȫéßƵ\x9bĘ÷ɤɼҭÆѯδƗ¨ņ#Ԧҩ\x93\x88',
                                                                            'ɴНˌ¬ʘτǦÕҀϐţұІИ\x85ǊΚˡƫɊґbʈ\x937ϚΦŲĸȡ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'щΎƖѹɿʯɘќʔҖɬΊñӵÄƎǸSͻюӗȏҴӚѢ¾҈ǩ˳˳',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -9283.53682778166,
                                                    },
                                    },
                            {
                                        'name': '҅',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'đ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034648.080457:+0000',
                                                                            '20210327:034648.097549:+0000',
                                                                            '20210327:034648.114408:+0000',
                                                                            '20210327:034648.129594:+0000',
                                                                            '20210327:034648.142609:+0000',
                                                                            '20210327:034648.155641:+0000',
                                                                            '20210327:034648.169617:+0000',
                                                                            '20210327:034648.184137:+0000',
                                                                            '20210327:034648.201639:+0000',
                                                                            '20210327:034648.220270:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҠĀȻ˷ƒÿӱӖǤ˞&ԍωͽǫƥĚɏĶѺ\x8brƮȼҟȪјҡʛε',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4882120802561410307,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƧʝVќ\x90ǱĞԅԜÈϟʰKv҅ԙϻſ³çѧ"ɤϷăȃoɮ϶ƫ',
                    'message': 'Qš»ư(Ћ¬ˮ¶ӽόƄáЁǲβɚӧСũÖKН^ĻрƐǭȖБ',
                    'arguments': [
                            {
                                        'name': 'ƬчѬ˂ҬƂӅΥʑĻƳʼϷυќȼǋÈӎҨĶѿºoƿ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɩХʇƑνőĝ˟ЈʡŔ˶Ҵ\u03a2ȒxXҌʪиϗϒɃĚӠʊʽʼđВ',
                                                    },
                                    },
                            {
                                        'name': 'øŠҸù?ƝѳʢǜӭͺŒĞáŹРҚѫΰɷōǪĒʗǤ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӤΖ\x9bΪĂԝʘʸΐ˪ű§ƝˍɅŲҼЗȠʸ˒ʭʁƗӵÎɹˋάʰ',
                                                                            '\x96ԇĈϾҁ§$Ȝ.÷Įԁ¿ӊŰɯ/ϭʐˁɓǕŲÚnΆϥҒȚ\u0381',
                                                                            'Њ˸ҌyŞҺǀrŢѫő˄¦˾КϟΎʑʤѦų0ȥzȸСѴСϙˠ',
                                                                            'ԇƜŭђĩЗ\x97ƺbʇťΧŸͲʌũɞÎε´ЉƌȡϕҊΞҞԐѝт',
                                                                            'ѼĸǶĬ\x88ĦљƙɊűѼȟƛĤ˙1яͰǹʲӕͲЁĆé\xa0ɐ\xa0ϯȞ',
                                                                            'ԀӻÆ¦ɮʳƁǘƂӬʐƤӛƝˊΖӌɓʱʹAƸӐɥʽŚÍԅҕʉ',
                                                                            'ʈӓѱGѢʎӢ:ǌ4ǌǦҖ@ɟè!ÍǛʜɴȹʙюτʾʍƐөĈ',
                                                                            'ЈζʑɋƫªӘ\x98ΡąƸԄ҂ȞҡĆʕʒ;βȴӽȸρɼˌ˼Ǿ˭ҕ',
                                                                            'ʜģĚÏηdϾԐЌҺºϊÙĔЋΐɴ_ЃЪʊːҿӷєԭ\u03a2ǶĦӜ',
                                                                            'фҡˆўŤJԁΟǌdəԬȰǽϋʘĸӺţȽ˘\x82ӧϿˤģӿŹǦї',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӕöɂѯσŲȇӀȻїʟϱͲĢVŅȈˤŁ9МıƦçͷҮΩ˺',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ηèԄоέŠ˛ӖƣÙӫȓˉʭ҄ȪӓӤСӗ\x86ǉ\x93θýӯӣțЙĴ',
                                                                            'ɴτѽ\x85ΘϾǌɛÍЯΕʞğĮƆ!fǍĺùĪƼѐŒÖPƽϯƍǟ',
                                                                            'ťσòԮыǥʃΕʅÐ\x94ä\x8d\x8dƸӨɫϫǊŹÄӆѶҷŮȓǆ§äȃ',
                                                                            'PƍшʺΜѿѝҁɗǐΡçǗѺ˗˶ҏ3˝ǅӀȪĒѧƗӠΛħ˥К',
                                                                            '˅ƠdʏҶǗɄȞÚ«3ҤδʒпФОǸƇԥǽϨʍģΊʨŦÈǮԠ',
                                                                            'ûɭ-ϟʇ3Һ˫ҹſӬϸİ\u0380 УˬʁγůԅΙϝïǑϠύ½˽,',
                                                                            'ÇȟĒҝØҤƂ\x9b\x9aôɓЊɄħ\x98ŨǞ\u0383ɣ^ȧŴҍѯǽS.ΣӐӈ',
                                                                            'ȓΗϷџ\x9cɒм(ϧŔûςʩʢӇ\x94ѥhŽʅӲ»ԈѝϱēʥǃEĩ',
                                                                            'ΣŹҲαŹ˝ϖѰҨĈŻѫΠȽŧюʒʁķұʦӠpҵѸҹ´ɘ\x82Ǉ',
                                                                            'ΫɂʣΏÄЏƴоΰўˈğʚʁԓMԅƴĘȳǩʓҊƊзμí˶yȨ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '~ŕӈЫȢ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'bӹƐ¿ЭƛЧɊťƣęԮЕƛ¤λҕ\x9dÕƇȟğ҂Œč<İ½ƌӒ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 529161.7408183943,
                                                    },
                                    },
                            {
                                        'name': 'ĮУΒʔˑ˄ɌиНӺĊџӽǶϐѥΤӮģʒN}яϮəҫϓԖ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĹЋƸр˛řÑǗǰʢϡҀрȅƱѱæϾ5ǐѷ·',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8517254353527012523,
                                                                            -7829298915155133796,
                                                                            5708316923566046547,
                                                                            -5862341951281010033,
                                                                            -5628656738675229739,
                                                                            2722492859841896329,
                                                                            1480370838747115500,
                                                                            -5730658434829388045,
                                                                            -3157522541379549752,
                                                                            8043806401074443807,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ήП',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ľҿϭɪιӀȃƏԊЦтaƟιԬңĶǽÔʊ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034649.570869:+0000',
                                                                            '20210327:034649.587838:+0000',
                                                                            '20210327:034649.604772:+0000',
                                                                            '20210327:034649.621684:+0000',
                                                                            '20210327:034649.638238:+0000',
                                                                            '20210327:034649.655275:+0000',
                                                                            '20210327:034649.672167:+0000',
                                                                            '20210327:034649.690866:+0000',
                                                                            '20210327:034649.708575:+0000',
                                                                            '20210327:034649.725785:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ґƾƠΌªӃÇҔæƃѬԫКŢԅҔԕʋȭÈ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ЙͲԓʯƕӑưԊ҃оȮӑΰʟȝЫűʎΨH¨Ϥ˔ϝԁżˇҋӬΧ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': ',ΉөςıӍҗˮӮ¯҈ʑ˗Р҄ΐÝňxuҝŞ¯ȷ΅ùӨҥ˭Ӗ',
                    'message': 'ʎǓŇΧҤbŦǗђԩпĢöǗѹ\x85ŐӅ-ȕǇňɜˍ7ϑѬϜëǍ',
                    'arguments': [
                            {
                                        'name': 'гÌʞѧρ£\\ϳʛϖҚŹƷψȧνŕ˥ǘȔΦʁкʟǠɁ,¨Ŕʋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034649.951469:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѳ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1660504411417140042,
                                                    },
                                    },
                            {
                                        'name': 'ǗǐČӧĭõӉŹȡьѴɃȺӃŵӐȖˆlǑ!ƚǁԨʦοϟ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            488206.44331642357,
                                                                            828767.2470196593,
                                                                            54630.54569911907,
                                                                            676295.7484597046,
                                                                            -43504.57791220408,
                                                                            557963.0180142405,
                                                                            835286.6250303661,
                                                                            261632.27967800113,
                                                                            157469.89243151806,
                                                                            772024.4069104225,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȖȬҔϼɹŵҬыϪфʰνѦӷΪŝҗţϋhɔˉаϱ)PǞҔûϓ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'бϿǛɌõʍuę-MƝӕϺǎƁѵΦΣӲϡœԄϤȷЖ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034650.425311:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѤѼͼԏґƎҽʏcũϹδӳ\\ȸΑÞνɣ\x92æΚщ~ΆҌʋ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6072815780364257319,
                                                    },
                                    },
                            {
                                        'name': 'ŸҴưЅɰ*ѤԔϭԠǬж~чԚҌыӡϟŜϫϸϩʨӱHʈХIǟ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӕ¨҆Ɠ\x9cʊƢȥÏˮùȂŗΌѱԀȴКȮÇ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7755670817221836768,
                                                    },
                                    },
                            {
                                        'name': 'ДɿϕΊʾοśЦҧĄFԫv˭ԅFơѱ\x9aӞșҫkќɌǌҶɮƱȷ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
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
                                        'name': 'ǦǳɭԠƺxΝӠҁť[ɀɑìѭʯ˭ҌįԎҏɐCħɜǨœ\x92Ј\u03a2',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "˲'ǲЌЊNɠĊťΜӜԀӀԘІǗӬͲ˙ВПŎӦоÒÖīkɼĽ",
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '5ȨӧŁŅΚϊС8ψѺɽůaӡӔҼȻï\x8bʐùӕʗưӍϬҦҌс',
                    'message': 'GǻΰѠтԠɼͽ\x8aɪȰȇʚϲTȝѽӯϷӕǆϲˬɣʐŜԕťŉŒ',
                    'arguments': [
                            {
                                        'name': 'ϮĮѶñҋGńӸԞǼ·ǝ¥ʝԆ²ѫȝ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034651.127545:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӛҋϓĄʬƀӨʸÒʅLƈÞѽŴҚʮҍ¸с÷ѧØKӗȺʞԗʜο',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3028610490040224157,
                                                    },
                                    },
                            {
                                        'name': "sŹƵ'ȵîПϵwƙŷĺ˻ȯϫÔÂĶʑƅĽ˟ʻ\x9aȆӃКҸӐÃ",
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʀȕƨѶΈÑEүƖˮ˫˥ɇһ¤\u038bƜȕĠˁhͲóϏ.ԝԃɆТƿ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ęŕԮɺԀÕß¬ŏѧФЬΉ·Ĳ˔YMғǡţʄŖIʶԨҾϠҡќ',
                                                    },
                                    },
                            {
                                        'name': '·ƝҷǈʱÌƑǽħӹ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 110065.30456450136,
                                                    },
                                    },
                            {
                                        'name': 'ƙæ\u0381ʨęĵƲаȨ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8697199173435013083,
                                                    },
                                    },
                            {
                                        'name': 'ϰԎӰǗƔϜǀuƝƯÒОѧȆȰρɠqϏҦjŢΉшЅԕøѥӕѐ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034651.726524:+0000',
                                                                            '20210327:034651.749729:+0000',
                                                                            '20210327:034651.770303:+0000',
                                                                            '20210327:034651.791517:+0000',
                                                                            '20210327:034651.816092:+0000',
                                                                            '20210327:034651.839475:+0000',
                                                                            '20210327:034651.862817:+0000',
                                                                            '20210327:034651.884004:+0000',
                                                                            '20210327:034651.902593:+0000',
                                                                            '20210327:034651.921449:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǲʁ+үɷ\x95¬ѿˀğ\x82њԝƾȐηδŜΣʺɂɗɟȷwõɭȹɻ®',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034652.019310:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ЬѰʴψҸʴĿ˷αŻҴǄϊ˾Ƽ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '×ƗĽԇԏӜɁǥĖƳʌƁ˹¨ΈԈʾφċʥ©ů¼Υђі˂ԭԄӓ',
                                                    },
                                    },
                            {
                                        'name': 'ǦЮəĘɰЛɧȒίμҠʱ\x97ūŢ',
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
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˸Ώɺ\u0378ǴnĀΩƊā\x95ČΣŌɈʖ˪ʎóΥѕȣдҟǮқƇЁǆś',
                    'message': 'ͼŴѰȃ\u0380Ŵ\x9cÏ˓ŮɋÁƄϲмǨͳƇǬqƿčΚǌ«Ʌʙ҇ǿʝ',
                    'arguments': [
                            {
                                        'name': 'Qŋėȏ˽ĽψYңҵǽ=¾ȂǣϗЎ\x84#ɡʀŵ϶˱˰ǂƟxǜƞ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ԯ\x8cªǜђʚίйѲţΥȝυҜĂβ˃£¯¤ǹē$ӇҾмϯӍßƸ',
                                                    },
                                    },
                            {
                                        'name': 'ʍЈ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӳƋΆѹғ·˒ąŹΖVɘŘҀǓ˱ō\x93ň˱ʏƬиɦ˥»Ϛɝăȧ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            52859.17990869185,
                                                                            900566.7243903667,
                                                                            815339.981976603,
                                                                            682123.3806341866,
                                                                            374468.74094329454,
                                                                            838019.4911316672,
                                                                            306244.1428679479,
                                                                            14189.707240077463,
                                                                            338564.34266294906,
                                                                            245398.9383174482,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɎƑë(уąɄһƺr΄ɹӢĝǟʄФŶȷǊƇ\x93њȣĻ³Łƭg,',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7885698303422899368,
                                                    },
                                    },
                            {
                                        'name': "nν˪Ѫ\x85ԃʲ'ҏˢԔʒʨơĦÊһөǪȶυӲӐΙ",
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034652.952477:+0000',
                                                                            '20210327:034652.969559:+0000',
                                                                            '20210327:034652.986776:+0000',
                                                                            '20210327:034653.003869:+0000',
                                                                            '20210327:034653.020804:+0000',
                                                                            '20210327:034653.038026:+0000',
                                                                            '20210327:034653.054803:+0000',
                                                                            '20210327:034653.075417:+0000',
                                                                            '20210327:034653.096665:+0000',
                                                                            '20210327:034653.118226:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΜȲӾjʯѪĲ˱ȗЪ\u0380Ђʳ˲ԏӮȁǛɐţчƍІʫηԈҵÃhи',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034653.230909:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƳļǣuŐԨˈ¬ǌΊӰǾ˚ȇ˽ƾŁѭѧҚtƑɿΣͲǪȶ˹įδ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            678920.1422671721,
                                                                            734583.8103734604,
                                                                            727864.1949549193,
                                                                            1378.2584824894875,
                                                                            166460.7578449265,
                                                                            333056.24003956694,
                                                                            895493.2131217282,
                                                                            556975.9058404504,
                                                                            -81157.98601163538,
                                                                            263635.1175201903,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ζ%ѸЛȬӽĖхɧňΚîńΊˈǏŒMɣɭǺ˃ɐǨҗõμǧɷ¼',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 96408.12844322418,
                                                    },
                                    },
                            {
                                        'name': 'ύbȬĳNȮĮϟƑүǃǏћ҉ū˕=ǌʉǄȼйƪ¸ԁϚǅ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӒӮѰ$ҟʨǂɋµԬÜӻϨuþŻūѽĳƟʖ\x8dǑưΞѬĕӹȡ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7432717686252891840,
                                                                            3502760193148427487,
                                                                            6830277291824556793,
                                                                            8288382415063013445,
                                                                            -55349629365714321,
                                                                            7235855026658353980,
                                                                            8928758846132591458,
                                                                            -2470465709885976455,
                                                                            2354010209444908462,
                                                                            4279922905914120831,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʽ˴әǆιГǘ\u0378Ϛǩųɇά¬ħ',
                    'message': 'ΦƾȫʸʃbȜпЄ-TȢːGɒȇӬ\x98ȴıΟӰӽʒώңҲљҩɫ',
                    'arguments': [
                            {
                                        'name': 'ʏϜӤҼØ<ʙˇțȲȶʹњļ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3264646741415608413,
                                                    },
                                    },
                            {
                                        'name': 'Ң͵ӹ˦Ԧϸ]ѓʻǸϨμ5ЯҠѧˤѓ«҅ǴɕԜ¶ÕЬȹǍ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 997026.1591737443,
                                                    },
                                    },
                            {
                                        'name': 'ԔƊӛǍčđ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4208583422517791182,
                                                                            2651767837628731813,
                                                                            5363448100163100159,
                                                                            -3432527325084742195,
                                                                            -3273287394077377598,
                                                                            2846668463131979535,
                                                                            914497816876761287,
                                                                            4138139811957473498,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ńŢЅΘ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034654.339391:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǝϢa҄Ӫǂ[ϳƃǼø҃Ż+',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034654.390983:+0000',
                                                                            '20210327:034654.403955:+0000',
                                                                            '20210327:034654.416680:+0000',
                                                                            '20210327:034654.428884:+0000',
                                                                            '20210327:034654.447998:+0000',
                                                                            '20210327:034654.469720:+0000',
                                                                            '20210327:034654.489860:+0000',
                                                                            '20210327:034654.511398:+0000',
                                                                            '20210327:034654.529755:+0000',
                                                                            '20210327:034654.551007:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ə˖û˴Җ=ƯƋʚÉ΄ΕŕӣѰ·ľǗ&ÃϞчœϥӅ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034654.660739:+0000',
                                                                            '20210327:034654.681318:+0000',
                                                                            '20210327:034654.700032:+0000',
                                                                            '20210327:034654.720294:+0000',
                                                                            '20210327:034654.740275:+0000',
                                                                            '20210327:034654.759803:+0000',
                                                                            '20210327:034654.779813:+0000',
                                                                            '20210327:034654.798655:+0000',
                                                                            '20210327:034654.818100:+0000',
                                                                            '20210327:034654.834460:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȓɖӳɽѦŘăԮИƂӔҙ\u0381ϭʉŊƵɕőůf˩Ҧђ¤ĝԡŁаƊ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ųǰ\x8dѼςCƿϦΧō˃΄ŋʕɪҍΐǟĶԚϴŸҊӍπѴ6ƖäТ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            855791.6151121869,
                                                                            546418.0320707852,
                                                                            829718.5027398496,
                                                                            391550.283578036,
                                                                            754452.4009310368,
                                                                            -7195.849882627794,
                                                                            269988.1999065683,
                                                                            349554.31578409276,
                                                                            29445.24342674276,
                                                                            983562.0183134514,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԀǑ¬ǖжiȉҠΧӵYЇΎ҆˵ǛѷѲԚʐʀİӣĖšϯϖ¿âĥ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034655.132541:+0000',
                                                    },
                                    },
                            {
                                        'name': 'į\x92\x88',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2434950490551973673,
                                                                            -2297088745870821538,
                                                                            1031978634543817290,
                                                                            -1561959774563019824,
                                                                            -782690437078976792,
                                                                            -2048483328676611083,
                                                                            1815875138201657565,
                                                                            -8241910945408530530,
                                                                            136636276497936474,
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

            'identifier': 'ēҕͳΜ6',

            'categories': [
                'network',
            ],

            'messages': [
                {
                    'catalog': 'ƟƏ',
                    'message': '¹',
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
                'identifier': 'гșǯFԚРïňʹȟŁǙҵɇɇŰԒʍ¨ɸʧ.ηӉˊġĪҿľҴ',
                'categories': [
                    'access-restriction',
                    'access-restriction',
                    'file',
                    'invalid-user-action',
                    'os',
                    'invalid-user-action',
                    'invalid-user-action',
                    'os',
                    'os',
                    'invalid-user-action',
                ],
                'source': 'ɞėŢnΧћʧНѡ\x97`йДôʱэͶŉȭϢĻӤ˜јƅˮÎԔμԜ',
                'messages': [
                    {
                            'catalog': 'ԔΫŜ\x95\u0383ѭѼʍĚŪгӯϴιŶӨԏƮιɼϨϮ˾ɥăʕÖԍ|]',
                            'message': 'ǶŋѯԬ=ʄ+ÌТɡMƄǒκȎϩéɌЅǱɏËˋČƋɛȂȽԙŚ',
                            'arguments': [
                                        {
                                                        'name': 'ϳ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɟư˙Ě˝ғґӹԬЋ˵˗ҟͱƳZȿũÌɈ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'üȷƏƂЕΗ´ɣΚŏЌԆƤ\xadԞЅίśКĤқŰ8I:ǮÄ1ǕĔ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 341053.7398896713,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϕΊţʱ;ǼƊʒҼѦɛơʑњАȯӄðʇɜƛқϘƈԘǆӜҰɭŎ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҜϵϾǈăҌȏÙҺǧǸлΗ˫҄·ƑҁőѐӶǇҧϺ¥ąƝÛċĳ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 480660.7448313215,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҙƟʊʾГǣң',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǉҏϯ҂ԡϖɍą&ҿʿЍƂЋ҆ɊҗʺӜϡɫӌѰʱȨΏʓǘфɟ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϘƽŌ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'lͶлєűǤсуԊɎԛɎΦϽƟN"˛°ʹ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x80͵Ԙő«ҳ0Ǽċ±ӀҝȔƇӜѰʞөҼӌ\x99љ˹Ж7Ҍ΄ʤÕ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034634.149035:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɈΚѺȹĔԄЦˍщÌȀѨ<ŻУвΚˆ\x81˴',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'uԭŔʑŜΎϵɘɢҤĕɀѠ#ьɢʤ˱ȓΪæϖǁӄʮĊǽÚ\xa0ϋ',
                            'message': ">ǟȞαсӢÁӱǷ'Ϥæƻ\x9fзƻχňƪԣʬԃҖ%pһǄΑ\u0382ƙ",
                            'arguments': [
                                        {
                                                        'name': 'Ȣ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĺr½UțЏ˶ƓäγΒɛȏɧƓőɠcʎ\x86\u03a2jÂ±ÿ3ϷȠҭҹ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'úɃʼжѭȋ6bБ҄Đ˱5ŷɱȋͿѠВњ\xa0ǁñҩǑ&҃ũ_\u0378',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ēӒĻ\u038d\u0379ȎǺЛĮ±Ξȏ¯͵Ԕʯԋͻ)²ɱǣί',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 788532.1994660277,
                                                                        },
                                                    },
                                        {
                                                        'name': 'τ˨\x86φѝʓƊˇѨːÀ>\xadѬRΓɆ\x86ȸˊÊ\x9dϞŢǤ\u0382¸~ȸҘ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'xÉҡϛ\x81ԓЈ`ӭőóΡˣҗ˔ʊеȵǮѕÐњģ"ÂĥӦӁˈТ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'mÄХƶ҂҅ӛȀi˷ҠПʂClÐȞoĵƧѠҊǈқѣ˂ҌϹrѲ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 239150.44414645876,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0381ҍ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǾǹԣÔΐϬχ·Ǖŭƴ˘',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '´\xadÏԝ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǋΞlԭżʎɑèˮЖ˗ÿƩѷ\u03a2ÿѣNʞ³ĥħŇĔȮcҾǀ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '±ɳŷŮʘ҄ƇӷѨăѨåҚѕҞǷϱӛγ\x98ҙʻҶĖχҥÏ&ϖ`',
                            'message': 'ԍҚŷԇɰԖĺɗǌʧŃVŊз˝άӽ ʓǞȴЪɿȖцX҉ɫʥɽ',
                            'arguments': [
                                        {
                                                        'name': 'ҦƨǢźг˼\x90ӚγǨ˥ȖԬƝ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϮÿӅӀø˻ʹSϲɪӃӭɎIǖiİ-ҥİЂϯɊΆʘπȎɮϭŴ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȋεãȆɆƽЏ\x98šάДǋϝƇԄȓʓƶђȳʹУ²ÅȂĚßпkҚ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɳÂŐȱPӴѾˢ\x85\x97³',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ũϲԏɲȍ˪ƺʌ˰ћӞϙȝDȆѲӇΊӦù\x84ԢΙɞǯϪʳàƌƄ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ыΎǍŞZЙԤҴŜӥƟġΡŖĦƨɦϽ҉¿е\u0383ӯѰȄƕ˶ϽҠɌ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ũǳǰҐ6ǟэҊďľȗƷӈ"љ;ŐŐӭώ5őb˸ȈĕÒϽІŖ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǮǼȭƜ.ŖϼWѮɶʑӚҲѩōңάҜɜ²ȗ˩Ж˥ΊÀсɖʩ\u0382',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӊӣΊÉΎΓȺф#I\x8dӦǸȂȣǠ,ǙďпѨҺԜȡɆҴ_ÉǛŶ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ØΈċӈŊ½ȇҗԟʮƠƒnʽеЅЛ ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ĳȧ\xa0п)',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɦŠhȰϊBԁƶŊÂшɁξbŶ\x89Зӵ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʩǠŔϹǚ\\CÀˎτƂ*ɦÈ˘ȐxOѓ«ҦɅѡ˽қŞѿГĹň',
                            'message': 'Ţ˟ǱӦ^èčʶЃ\x83V\u0382ǸӁͰơwÖЇĉЭ\x97űәŒ$éĩϱƅ',
                            'arguments': [
                                        {
                                                        'name': '϶ҟƢwɗΡжīБӶЗǅ.K˪\x9aΈÿ\x85ԢŐьϥúȽĲǙɵ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8685974897933440683,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ñˢʀѷϘϚʱȲĤȪ˅\x91ԇɘѹ~Bΰgӏ͵ŧʂǺК˚ΧЁΜ¿',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԚřΖωŨϵƫϪɋG\x9b\x9eύǙGTɈˁћȼǨϤĈӂϱ_;\x87ʶö',
                                                                        },
                                                    },
                                        {
                                                        'name': 'DΓԑҸ҄˲ͱКϪҘӉƥ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '»HΥʿԖѳœkщǥԮĮǵȑ+ӾĉΨӛӘɓͺȬÅίǛМΏȈȮ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ГǚȮȃôѢФӏȇ˺UƜˎƜaѨĿơʣӣңśǝˑ˚ɑł\x96ҺŁ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӂ˙ԁtͳ,`āĴʩҩϴȧѭҦΞĒź',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˣĂʁёɨƩҫ˶Ŕ\xadĕƚƗǇЗs\x9eɍϖhƳӷ˫ЪκʁļÇϝЬ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʭΆĪΘҙӣ\u0381\u0383ԤĭǚŘӳÆʘ\x81ʬÆǧæàȿʽĤàԩŃƱɨǭ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǳфӮćƲ½БҋоаϷȏ,Ǉѹʻ;ǼɽƹлɏӡzuƧϫӆѭȰ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 8680.459484894469,
                                                                        },
                                                    },
                                        {
                                                        'name': 'нԉgԆӒоҏϰӾɻȹԁ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 86338.44650593691,
                                                                        },
                                                    },
                                        {
                                                        'name': '«˴ąз˳ǭſ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȗ¼ϥОƀAΊļjʤ\x98\x96ԩ\x9cб\x89ɛϒ˕ӷѻԩçΰДӄɵНԨƯ',
                            'message': "νȶЃÐϚĿϤЩƻ;ɽˍȊЈА\x86ʐϨ\x8dκʹţʇǎ'ӌȂƃǓ˅",
                            'arguments': [
                                        {
                                                        'name': 'YρpϿŔӄȇʳϣĢ҇Þ½ԏɭƦįƄąȰϦɡĚғ{ӮςԞʍҬ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͷǗɣ©ŌʽǭȀϐɟ΄ʄˡтӦɮȃʲѰƏΆƍ\x8f˶ċƺȓ҅\x84á',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': ':ОϭɓРǻѼʤɇԂʪΑМɃƤХDЩȼҘŮƤ˺˅?дԐ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4661689100042893315,
                                                                        },
                                                    },
                                        {
                                                        'name': '¤ĎϥҞϺˍʪРŭǱȉʖŶ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ġҼћν',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΗҬͻźӡӻӶH҇ȞϚıҬ\x81ӾЅЕɎÁɁЈ©ˬĕͷŻƌФˏÍ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034637.101123:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ûOǭѽ!Ш|ōɓ!¯²ǽ_ΖǋĴҡЪǣԄӪԜ\u03a2ϡΏȉ˩ɰϭ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŏʹěѷЀʙӥҏmĐǘԆͲ˵ϢѓϛĠɹ˞ǔˀЭşƛǌҐi\u0378Ĕ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 218279.9977727459,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŗºѣѶȽƏĦʁσAΆҫɋ\x98ͽǢΩɱěūʧ}ɴľԣТђɃwƇ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'X\xadťíÝѶɐʄ\x92Š\x9b´ȽŨĖʘɝŒȂĄųŏˮſÉҩċ\u0380Ϡ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 9036281590328681483,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǋӮő҉ҕЭħһāĤϞΎ˩έҜƍĎψ×',
                            'message': 'ӸƚɘӶМҒϬš;°¹ɪЌFόǲʎīʴψ\x85ˤŧ¦ʪǈ~ɬƶϜ',
                            'arguments': [
                                        {
                                                        'name': 'ŕɕхȧȋΣѷWķ\u038daʩ˅ć_ϛǾϢɖʞķ\u0378ќǸȐϳӳӷƲӋ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǙţҙѶћҦĝʏΔǶƌϳԗ\u038b¼ѐșĮΙѩǑ\xa0',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĨȣѪӋǷŸŦґԖĂξԡÃɍ«®Ӵ\x96еΟǌҽӵʣʙЋÌȻȐʤ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŰпƾӠΫ˗ћɶԧȭӋϧˏ\xa0ΈϣѐĎϊȗǪƖʄ˳ʡɔʲ-ňʑ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŉǩˇфϫȊϞÃєʬöÐϻϼöͱȪɁ\u0380ҽĞȲ?@',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŐϭɈčǋΏԔʑǀδǭǆp2υòͰԕσѶʡӔǖА5ȴ˦ӉОǭ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 942504.6886181181,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʛŎĖèȶҢщſąɆљҟǚǇìšԋь',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1668169845879385824,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0378őçâʩʀƫӕӤЅȢȎĽɾҷϜǶ˔ӑȥ\u0383qάԗүL',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034637.954554:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Θʯƌ˵ǇҤб',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ōΑεÜƏÞ˛ɷϒɄ(ǗǍ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'f®\x9cǃ½ό',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӆΆŹϽʱК˭˅\x9edʥԒƇˇÇȮ:ӤʘàǙķȢӑˣʜȩʗÙо',
                            'message': 'ˀυʈƈϖΦňϠӠƊʴɦʖÄўĻÍ¯ǫͻķ&yΰϤɝϝ\x9bͶg',
                            'arguments': [
                                        {
                                                        'name': 'эǦӬʼƦњŨ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2692044182520155893,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʨйɕ҄ͺēΦƽɛНШН²˟ΣûUįɫųǁӉĸ\x85ÙGT\u0378)ҷ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4230795148302238696,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɿΜ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'јɎҥĽȶІ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʈÌԚƜČӬÕҦǱʶÐЃҋҤƢӽӎɬЍƏјҩʅ±Ԧϼ3ԦĨ˅',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӊ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɓӼƳĲĳɅέÎŌƅǴыw˃зɍΆҦa:ˈеΩî«ĥÂϨКЏ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÎőƆɃÿĞΒxʬɷɇΧѲëʷԡҡǂӃɹҕȿЂíȟΊȰǸӼǼ',
                                                                        },
                                                    },
                                        {
                                                        'name': '*\x8eԣ\xadŶϹͰȺԤ˄·кȌÊԥӟbίҟŸɘǻĵѫΔϑȵ˕Żí',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÑфƵʩȹʩĠâʚǺʆ9˄ǧѧ¦ŦԋсѥǇ\xa0ťƿĘɛȿ#řу',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϊĸÖ΄Ӑ+ƵϩƎ4μͳ}Ԏʬʃ˳\x99ƕÝԮӨҏĮҠѫŎѤўə',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'íϺŎɎƢɔͻ\u0382ͲģμЈņҳˍµԇǟĴıĴǮĦǧŸρ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ùȉƤˏʟȝɩǝɸƯϔſʅ¨ʓΩijƠ>{ԆҥʤYʦП)ƥ\x8d',
                            'message': '˖`ԒЕ»υ҇҄Ȯԑȣnȥƛ}ȨBӋ˶ƤǞɾ˩Ľ˧Ԃɸ©ɓҥ',
                            'arguments': [
                                        {
                                                        'name': 'ĻӴþͻȫΚҰțþ\xa0ϓȧˈpȌҍ˫ԓèǷȻқįϧˮıЬҜѓη',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 374021.25782919524,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԮɎZͱ˗јǕ˷ɷСҌǮ˔ƭ\u0378ΝƌżӤħЋʿϻPʋũƹĝΡЗ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034639.139977:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9dђϠ\x8dԚƗҊԇ?VčâНǏҹӞϱĢŻʩІѴϲÍѡԏ˔º',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѻ×ζƽӷț¤ЖћΔɲϰ=ԟϭŤӦɹ˗ˀ*Ìѱõ"øȧҎ\x8bʰ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȯŋĖŞûǶėƐƏƐʥҺƼʊ\x8cОѦɋâÅɾҽӎө/\\ʠ\x80Җқ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȟʒžůȝϖ#ƯҝϢӦɒϒĢ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '·<ϽҞϳчΎӕʈǽǝӯƅ\x84ʒȬoѪưſ͵ž]ĩ҄ʷľҥɾƵ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034639.550177:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˄˦ʑșă˻ё΅ʜrgǐϙØцɹ:ϥϫĶȖϓęҶԁέɎ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¥ԄԎςú%И҈ѦʣҧϦ\x84Ǭɴӆĉ˻ÐȳƼυʌʣ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˅ªҔƨˏȇƏѠũеďЃo\x87ѐӿȂ,ԩΩ)ʩPПӳ\x80ɢ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѹ¥HέєЕѐėϚ³ƠυǷϒöҔDńПǬǉӔ:ȃúĿѪÇǆ˥',
                            'message': 'ǘȦЖƠθÞŸÊҠϐӃȣҝʳԕѨͳʋτżi˶ēŰϺΡªѕĔғ',
                            'arguments': [
                                    ],
                        },
                    {
                            'catalog': 'ƂѧҙƄҁĒɤϟЎӓеǾ˃ӮŢтӷԤԍƌԠжј¶ŻсҼÍ˝Ԩ',
                            'message': 'õϞϯǚѺ¿ľ=Ӗΰҭ\x9eβԬ˫ùăТïǢãͶͶЦí}αƇȈŻ',
                            'arguments': [
                                        {
                                                        'name': 'ʪ»ąѩ#Vӭ^vŘȉӐϑŕ˹ӧ«ʑʓʾΩɮ×ǮøӬļțлĸ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 17347.65367831735,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ſȪ҉ņϫϧѕȀ_wǰcO+vëʊȣ˫',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǽªɏWĸȌȷ˪ϤʳӁΉ,ԣΓ£Ů\x93дϯȾӼǞÍĄ\x91Ԟźϰԫ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'l˾Řɇń¨ҀşӃǟɌˆŏʕÇŔ˕{ϧԍZǢΙЗ-ţΘȠɍ°',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '{ɢѱϐdǪŦԗǾѴǛ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĿπɫԩŠΘ±ÐԌŧϧʝēϞΖũҝǖʒɪ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǯƻϙԛϞҡƤԒĞԥҠś\x95ȀčѨ»ђфȄȬ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'жʻʌŧɳӯхƃԥȊνʊoҩ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ůǐÙԊƴȐάДĐԀѨϘż¾úȂӰҩǺɘτФW\x8cň˓ӐĹ\u0382Щ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȻǪˏʀ˷ӆѠˢÜ\x8fԕϡԔγȪȣ·đŒВ`ĝмǆӗԜɯÑƠʽ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'єÀԤѐɝɕһΏ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƹԙЖħóƌŅҟŵɅǒїЧϢǲʲҰĿāƊǡĦŔӡԝȢʊѼθɰ',
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
                'identifier': 'ӆԇʲɡe',
                'categories': [
                    'network',
                ],
                'messages': [
                    {
                            'catalog': 'ʂΐ',
                            'message': 'ѵ',
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
                'identifier': 'ȱƾȞŭѽêϓΘ¦ω\u0380Ϯ·Μ˹ȽԃUƆ\x82Ī˦ϟщČˢѺѴύȂ',
                'categories': [
                    'network',
                    'access-restriction',
                    'access-restriction',
                    'file',
                    'access-restriction',
                    'configuration',
                    'configuration',
                    'network',
                    'configuration',
                    'access-restriction',
                ],
                'source': 'ÜĸҌԬϔGǈŘСǈğĢÃѕыԥƊɠƣŨвťōȵ~\x8e˙Ԟњ˶',
                'messages': [
                    {
                            'catalog': 'Ư)D\u0380фԓоÚϐýˡţҐĊǷҽ˙ɌíLʵҕɇʵĸɈо͵˺ʛ',
                            'message': 'ѡčпaΊȾΡєèѾ-ˠϷҌϢѪУ\u0379ãЩ¢ÎɺӖƲ¨ҤӗԘͷ',
                            'arguments': [
                                        {
                                                        'name': 'O·Ҵǋ×ʴǼˤĿЊɐԁX"ɵǒŧ˂Z^θϭΙĵG@Ԭ¹ӘǕ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԙƜǆ´\x9eѳȚжʩҳϥ\x8fǔήÍˌ˝ҨӍϣϊѺϭ(ԍ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ıɁiǜōʄңΑ³şǦŚÿŢʁ¿ҕЩщǌ¡ǀƁ˜ϔ˨ԂɻˏJ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8121904717069231305,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǁİүįɕ\x94ϐƪ×\x87ԚΌeÇǞǃӬϧԏqͶƔӟÂӯɮ×ԅ\u0378Ε',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034656.138748:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȧОϴ·ԬƣбΉǤχɬӻʆēɻЬђ҉ĢǲľӾ҅ԈҦӅ˾½бũ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '΅ΝńԥŪќɀÕ!ԁϥå',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 662109.7213262353,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƘNΟɋżí˞țƄǣŗɡ˟ϵ÷ÈćѯԆĒɦȘԣƐг',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΥҹƓԫĀ\x9bωÃ>ƈĦàòъʍҩǞʳʍ8ҕªϏƕӴәʕҨǠʽ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĵМϔ҈ʡŨҙ҆ʱäύɦ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȳr^řҡļӁ\x8cĂÃϥuĸʃc͵ʝ7ц+ɾűԞƖӚҳϥǭΒ®',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˋжҗлѬ_˩mĿ˖ҝ¦ȷѼȷђĉ˸z¶2˪ŖʵͰцΨʢψӂ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5949450050463932788,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʏȯƶÔƔЯʞ\u0383oӁΩԆ˩ҌēÔŲː',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ИјμĶκʑɲѤǇ×ΪɏÏҚƸѐˍÿTÌϓѰΨôЌȼΡ4ýɻ',
                            'message': 'ʸԕϵӲ¾ƫʞţǰĩȠΤʮ҂ӗҼСϝɶĦàƦǒĿШʿĖӇϣĨ',
                            'arguments': [
                                        {
                                                        'name': 'ǕјƷʳϑɱȃДəŲúũãŶƢиÛѕņ8ЙȩȰүњŷҊǰҥɦ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˇsͶSɏǉҘԏюSǃ҃ŸкƂ7Б˲гȈȓɢöԋзưԤS\u0382ǅ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ς»ñʢӈϦɀŤЕϽҐЦƿħ˦³ѨнŒԅӅ˶˥ʾʿȖòȒ`ʟ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8044832656482835489,
                                                                        },
                                                    },
                                        {
                                                        'name': '˚ƕωǏǁî ȨѡʩƲȡŠMҁ+ȆčÃΫҝþ_ńӆмȝɷǑǬ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˛ԡƥͱɖЈlĿþΉæ\x90ɿȲ˦ƠЩν"yѱζȕʒϿƶʟʿяк',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӻƧΦ²\x87/ӉIȟϯ¨ҍĂȺ\x80Ç¤Ȉ\x90ŅѪ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǠФЉQă\x82˲ʴϟÜ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԪȰˏи',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x87з',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȂǵԞȑ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '͵ìҵ6ӟĕԛƊ/ҐýƐǱϩøӉН˲ʹлϺǍǌƔªσӀˋˇf',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'иɺǙ\u0383ØʗӾǒʎзԕԂЪİǵӛȱѮƏŉ2Ѡч-ŭ',
                            'message': 'ĊĩԬΫʭӉǁδ\x8eƌέӶьʧӔѽпIѰ¥ΣДϑԑΣƟԔʪÝʫ',
                            'arguments': [
                                        {
                                                        'name': 'ӕΛ˜˱ДcИĵ@}ӈ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɧєЏӞҿΓ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȇɕĪÞƴ°xȉɭîȦŜԖϡʙχ҄ϛӦǣ[Ɠ\xadđѳƖΑȉÎЪ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɩƜЗϵхȈӷüyľʇԦПΦʈƛȝgъͱϲʧԟǶɨÿɜéӃμ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -86833.57411976537,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ш1ļңΦԭ¿ѝŶȚѿ΅¨Ǥûԅ˦θƋʡԟӬdsɊ\x98ƨƩI@',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʉɥ΄ЙũӼѿмӄǷ\x9eǲ[ŖȜʋȆƒƙĶǇĸÑЕĸǁʿŤЮæ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7117977937099079285,
                                                                        },
                                                    },
                                        {
                                                        'name': 'êǦҿŜÒƞǼХγˬΎҕΟɹēƣ¸ΚБђơuÁƴʼƇʜιɩƳ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǹűʛйѩнϏɣâьңʹζƬσƷ˖ӭϹ˙ҭς',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -76835.70234349873,
                                                                        },
                                                    },
                                        {
                                                        'name': 'KЮȶԟыF',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ˍϟɠʛſІ;ōǽѼƾƕ\x86Ԫ5Ѓȷ͵ϗӊΗǽӕӂνƩ4Ԭҹĭ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ņхΰćʐКȎƤǇҌ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӳНÜёԧлȅӍѶİśʫԔʾјɱġȩΉЧ´҄ìψ˷ӟԊԆäɂ',
                            'message': 'ȯ;Đ˅ʶãȘӡЌΔʲъAԦ¨äтжͷЎӶϧˋƗ_ʩД!ʳϕ',
                            'arguments': [
                                        {
                                                        'name': 'ǁǠʺțǓɓžƙѠԈϫљƗхɂƘÏʱĸ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԍӬΥˑ>ƘψǃϺǚѬɭL˺ĪΩӱӯћĝαӓɤκ˵ϔȀɐɼˮ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƂѓЙζɑoʕԚN',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҫāÔӇƬɻǥЧȯЧËǅ\x86Ĭ·"ŨϫơċΊєN\x9bʔϩ ǜЊè',
                            'message': 'έΉϖΗԢӎϣ˸°ɮ3#ĢѪ´ԩˆľÙԒԇʣē\x82Ƨԟ\x94Ƙ΅ˋ',
                            'arguments': [
                                        {
                                                        'name': '҄ÆZѾɥɖțʶŘғІҙȜԑрƣǃĄϰǈȚŷɚϿϾ\x9cѻ\x92ɨp',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 987690.1030049718,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʵϸˬɐȜИZҾˣӰ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŇѾ©ǬfǓԜӄӈОēҜԜЁʘϲʾԣʪӃ˯ӪξēΐȩѕǈǛҵ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȖɖąƋɽѯĥǄʟϡԊiυʵłцԮЦ»õȥƔŕҕ\xadʸɊӵУϱ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɏ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԁǔaǊ˗ƓƊѵǁԟÝπěʃĒ҄ЊÂҟĿΑå|\x91҅ҚÝȗ˹ʝ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 282279.55397614924,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǥɅʛϦ˧q¹ҞŭĿҔÓԒиԎЯ\x84ѽ4ÖŨŽβʱңЗУĝԏ\u038d',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 587237884454911250,
                                                                        },
                                                    },
                                        {
                                                        'name': 'л¦IӠϿOưƇʿyӚ˻ѳĞΟºyŌǚǰ˶АΝƱʍß\x9eȡˇȫ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӶӂYɒɇτ3\x9eȫɘɲˆɴĳΨӫ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҶʈәӤǵӳχ^ǘǞϵ˲ɲѶȒ¥dƱФҡˤϸ00ɹҌϞȴαƻ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 602335.5411041315,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʗ[ҮŞѾуƭ\x87ɹӭǺŠíЅӲ\u0383Ƥĭ\x9dʙÊ˺øРЛIʆ¥ΘN',
                            'message': 'ϟϻʼіӭ\x81ԏƝӛȡјʰƐʎȽԛӐKϐҟɺǲϓAӜʈЮ\u03a2˦\u0379',
                            'arguments': [
                                        {
                                                        'name': 'ůүҋˊgԚӗŪɏʃˌѻӼ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȡоƈ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8eԎҺ҄ö\x7fФ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ñ6ƷԏŶ+řŻ˳ĤȟƗгŎĩјƫtǧȗƚʽɡˏΖĝbΚяѮ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΩÅǳƙѩǑʵ1ęďһѱΉӮаԑѦЬǳŐ=ʻīȫȉӗKδɥϳ',
                            'message': 'ϲҳҠsϱŝͺuʔԪΪ¢ɂĻʛŸӕĚĥÞi\x81$ƉğϞΧȤǭh',
                            'arguments': [
                                        {
                                                        'name': 'ϤÏɚʋɹϸ7˙Ǔ͵',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3604276435619490129,
                                                                        },
                                                    },
                                        {
                                                        'name': "ϳιή'Π҄ȋʆʓΆΐψīğSêːñ\x8d\x97ђȍǡΤέưȣ",
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034659.743609:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'шǋưСϡǚÔɷϾȉ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034659.814018:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '(;ɵȢљ*ҎЄ˲ːљȖʓ·Хʫˣ˷ŔҿΝʿϿǚǂГȹѨ\x8eˁ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԡ˸фϺfΑӵϖƭО҆ɮ˭ǦǷ˴ɹ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6254560254509050353,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƶɄѨƃȠӌɯЍ\x99\x9cȆԮǣƅ˜ȝ¤ǵeĿҜѪƟƂнϦϘʇ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǣʏοЧ˝іů˓ԜlαҖÑǥ҄˄Ñѽ~ǑΠ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8990158941305695907,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԉķȧϋǌʯȮіƜ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѝ§\x89Ȭθχӫѭjɵ\x86QʽǛ¥ʍßӔGkЁϪ±ȞʉӐԙǀѺƦ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x83Н',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3944365465740871369,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ϭϸ)ˢα\u0383ӥˏԓРӞˈɇȎɍ˔Ǭπмж҆ɡӹЂäŒԓħȈ¹',
                            'message': 'Ԯӆ˫ЋДpˤǢ\xa0ģēЁŀѐɪ\x99ȫȰ«Ȥ\x94AθƣѼɃć',
                            'arguments': [
                                        {
                                                        'name': '6ɃƎɸįϼȉϧΞȳz˓Ϊ\x9cψԘȠtʍηǂʙʁђзÆ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˛ԃ˨DМȏɷA=ȹǀ͵ɝж«ơӅΙө΄ũƳʴŰŎӡɔǥQ\x8f',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĠăΓʉ2ɏȹѰјˀЭ\x87ĄŷŇ\x90ʂӕ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7244431038108850683,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɏǣ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5910469053198059340,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĹӞϟʑƓ#ýѣɚ\x84ȓãΞӜây¯Ѝͻ\x81ňÑөƥҔ҉uDVȦ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƕмǂáˆԏ:I˗ҸԘ˗ԏƊԩªƠſʒȾԧˑʯſӵλΐŎĬȃ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҨĈћƠҨȫѽϤґж}ƺ\u0382ԄiŬŞȵϭŉĞϋ\x8bȑÈăͿΗ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÉȑǚƬԊʮǠҧːӫűΦЬʦųΦĔ˓ΦĊҗƨP«ðȌʓſ|Ы',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѲŞО5ʹ˨˥ҝgьŮЩƥԦʨŸƨП©Ӡ©ѾʊѰŕ«ӇСψȺ',
                                                                        },
                                                    },
                                        {
                                                        'name': "Ɋ®ͻЄĭӂ'<˓ΰĻғƋάӟÆšlȿԇΚȼζ\u038dʁĞǓŔϖ˫",
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3644189641822438809,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԅ\x95ǃӱ˽Ӄ˵',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЏλɲØɘĒϚ˰˔ҀѩԠČ\u0378ˈ[ƥĤuğќȏӏѿĻ`ũŌΤʱ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '¯ͽϲӹяЍgdЮɦ΄NФäѻĴΆùӂţ\x88эԡВƘɢYҖ\x84Ҷ',
                            'message': 'ζɒѡȚʙ҆Ʊßʪң\x97ДːÑcʨÛǑñƿƌyªɲӻȬЙȚ˟ê',
                            'arguments': [
                                        {
                                                        'name': 'şȌƍɕȡʄ˳нΊǕWϰȀ9Ƴгџҷc±XͺƳ8ʶԘή҈ùK',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -947378217367865740,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ġưщȉ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ξf«Ďӵҫε&ǁŜΎҲϼ\x9bˤ:ěș\x88žЊŉБϏɏϻӗɷǩϫ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'κʏҸ-$Ӗü҂҈˭ɳʍȈҺϙ\x92ͱΧϞˊІŀҘī',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͶʍÄ˧ǕҤӫʛ·ȜΌ,ϴӼːʹɫ\x8eЊȂӸ\u0379ȍΊА0ɡѾ½Ì',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'qɣӒϿĖҤƟӓϺƨvҐϟƖƲƊÞǯ˨ѨǴ˼ƇƲӐӸЊɭϟɆ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ıĥɁƑЅқЊαбȘšʉʘʭάҿ˾ȕԟʄʈҎ\x82ǐȀǳi҄ƲԪ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7988214759302637452,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԅԀɩ\u03a2ʗʁӃ¹ӑÄЀҡ°ԮǘѥÆ}Ŭ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŠЕΥtФʭʚũʮ˝Τǻ«ǦԈ\x8dцǩƍθхȳ\u0378ϜǪҟŠŁÅԆ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЍãȊҚɴɣ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʵªΗ\x90ĉʰˇԢȐԣmǩнΓƚɳΜ˫ԕϻѱʕΎőĲȉŨФѺ˚',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ěѐǞȺɃхӺƅҒжӘǵŕğůьϳƳυӞԃƯZоαƝÑƃȧB',
                            'message': 'ŞӚӴѧԓÎƨʁЖžǈ¡ŴĨεˑĐɭʨʯǙƩƜ˝ҋͲɚØԄ\x93',
                            'arguments': [
                                        {
                                                        'name': '±Ç4ԧľÇώӤȯЉƶȴʵ\x88˖ǷΒ?ѯϣɘӱҖ%ƻÑúˏϚ°',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 9009027514987258057,
                                                                        },
                                                    },
                                        {
                                                        'name': '˵˰ϰdϣΘƂ!λҾȣqѝѮ˴ĀϵǢŜsƵưϻɂƎĥҵ϶ďÛ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 17797.97959109815,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ųÏ˅јˋˏύжª',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӏ\x8d£жϫţɫЊǁʴˑĄį˽ȣ˻·įϊɞȗ~ˮ\xadПĕӸƩϼɟ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034702.075804:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƜӷЍΝȋȍŬaлǶȕћӼȋɪғVƿģʆΟщ˴ϑϊ҅ǭƔ\x9c˟',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 46906.12450909539,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԤƇ?¯*&ϤaͻЄаPПģpоέÐľʱĨȐқ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɜgӮ\u038bãГоê\u0382șĴȐŪ\x8eeϭӑͿ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˽ī¯ǿԁĺɞǙĠԭƛӉʸɉıŘūҖjFʽΗЦιԪԋȔĳ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034702.358859:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Эċ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÖƸƹȢʴąХҧǲЈˌǞҞʭêȞjþßԥѻ˂жɌ}ɡʕȺ˩ȹ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'vÞƓԨɊζAӪėӋԮѻΚěӚ˸æʆɤњΕĠλԬƉϟԊ',
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
                'identifier': 'ǪȤÞԆһ',
                'categories': [
                    'os',
                ],
                'messages': [
                    {
                            'catalog': 'ñǺ',
                            'message': '˧',
                        },
                ],
            },

        },
    ),
]
